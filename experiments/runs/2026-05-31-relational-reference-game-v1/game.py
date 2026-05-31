#!/usr/bin/env python3
"""game.py — the two-AI iterated dyadic reference-game relational pilot (v1).

Operationalizes open-question/relational-meaning-pilot under decisions/resolved/relational-pilot-go
("Decision 9", GO). The load-bearing contrast is TRAJECTORY-DEPENDENCE: does a fresh matcher's
interpretation of a coined term depend on the ORDERED interaction history, with the CONTENT of the
prior turns held byte-identical and only their ORDER destroyed?

DESIGN (homogeneous dyads first: same model in BOTH roles, so a gap cannot be an artifact of two
different systems talking past each other). All agent memory is serialized into the prompt text
(stateless calls), which makes the shuffle control EXACT: the "shuffled" condition is the very same
history lines, reordered. Temperature 0 throughout.

Per model, per game (seeded):
  1. LIVE dyad game over K hard-to-name figures x R repetitions. Director (sees its private
     D-array) writes a <=WORD_BUDGET-word description of the target; Matcher (sees its independent
     P-array) picks. Real hit/miss feedback accrues per figure -> entrainment + repair trajectories.
     -> records the online success/compression curve (calibrated vs resource/hawkins-tangrams) AND
        the per-figure description history (the "convention record").
  2. ORDERED-replay probe: a FRESH matcher is given the full per-figure convention record in
     chronological order + the final coined term, and must pick the figure.
  3. SHUFFLED-replay probe: identical, but the record lines are randomly permuted (SHUF_PERMS
     independent permutations; content byte-identical, order destroyed) -- the deflationary
     "averaged-within" control.
  4. SINGLE-AGENT monologue baseline: the same model compresses a label for each figure over R
     passes with NO partner / NO feedback; the ordered/shuffled probe is re-run on these monologue
     records. Bar (b) of the open question: a relational gap must EXCEED this intra-agent floor.

PRIMARY (de-confounded, order-isolating) measure: ordered-replay accuracy - shuffled-replay accuracy,
on DYADIC convention records (both arms are fresh one-shot matchers; only order differs). The
ratified design names "live vs shuffled"; live-online accuracy is also reported, but it confounds
order with incremental self-generated exposure, so the clean number is ordered-replay vs shuffled.
A live ~= shuffled result is a FIRST-CLASS relational null (coordination, not constitution) -- write
it, do not retune. See PREREG.md.

Usage:
  python3 game.py liveness    # 4-call plumbing check (~$0.01)
  python3 game.py preflight   # 1 model, 1 short game + probes; prints billed cost extrapolation
  python3 game.py full        # full grid -> raw/results.json
"""
import json
import os
import re
import sys
import random

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

MODELS = {"claude": PANEL["A"], "gpt": PANEL["B"], "gemini": PANEL["C"]}


def flat_cost(recs):
    """Records here store `usage` as a LIST of per-call usage dicts (director+matcher, or one).
    Flatten to the {usage: dict} shape billed_cost expects, then sum the API-billed usage.cost."""
    flat = []
    for r in recs:
        u = r.get("usage")
        if isinstance(u, list):
            flat += [{"usage": x} for x in u if x]
        elif u:
            flat.append({"usage": u})
    return billed_cost([flat])

# ---- frozen design parameters (PREREG) -------------------------------------------------
WORD_BUDGET = 12      # director description length cap (forces holistic coining, not cell-listing)
R = 5                 # repetitions per figure (entrainment x-axis; Hawkins uses 6)
N_GAMES = 2           # independent live games per model (-> more coined-term probe trials)
SHUF_PERMS = 3        # shuffled-replay permutations per coined term (variance reduction)
SEED0 = 90210         # master seed; per (model,game) seeds derived from it

# google/* burns reasoning tokens (the budget ledger's dominant cost driver) and REQUIRES
# reasoning on this endpoint (cannot be disabled -> HTTP 400). These tasks (short label / single
# pick) need no extended reasoning, so cap it to "minimal" effort for google: verified to still
# answer correctly at ~1 completion token / ~$3e-5 per call (vs ~$0.0009 default). Others use
# library defaults (max_tokens=64, no reasoning field).
REASONING = {"google/": {"effort": "minimal"}}

def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None

DIRECTOR_SYS = (
    "You are playing a reference game with a partner. You both see the SAME set of abstract "
    "figures, but each in a DIFFERENT private order with DIFFERENT labels, so you CANNOT refer to "
    "a figure by its label or position -- only by describing what it looks like. Each figure is an "
    "8x8 grid of '#' (filled) and '.' (empty). You are the DIRECTOR: describe the TARGET figure so "
    "your partner can pick it out of their own copies. Be brief -- at most {budget} words; a short "
    "memorable label is best. Reply with ONLY the description, no preamble.")

MATCHER_SYS = (
    "You are playing a reference game with a partner. You both see the SAME set of abstract "
    "figures, but each in a DIFFERENT private order with DIFFERENT labels. Each figure is an 8x8 "
    "grid of '#' (filled) and '.' (empty). You are the MATCHER: your partner (the director) "
    "describes one TARGET figure; decide which of YOUR figures it is. Reply with ONLY the label "
    "(e.g. {example}).")

MONO_SYS = (
    "You are labelling a set of abstract figures for your own later use. Each figure is an 8x8 "
    "grid of '#' (filled) and '.' (empty). Give the TARGET figure a SHORT memorable label (at most "
    "{budget} words) so you could pick it out again later. Reply with ONLY the label, no preamble.")

# Nickname elicitation: forces the coined term to be OPAQUE/compressed (<=3 words) so it does NOT
# self-describe the grid -- otherwise the probe is solvable from the term alone and the history
# (and its order) is irrelevant by construction (pre-run critic BLOCKER, 2026-05-31).
NICK_SYS_DYAD = (
    "You are the DIRECTOR in a reference game. Based on the rounds so far, give the TARGET figure "
    "the SHORTEST nickname you would now use so your partner can still identify it later -- at most "
    "3 words. Reply with ONLY the nickname, no preamble.")
NICK_SYS_SOLO = (
    "Give the TARGET figure the SHORTEST nickname for your own later use -- at most 3 words. Reply "
    "with ONLY the nickname, no preamble.")

# Source-neutral probe role (avoids 'your partner' for the monologue records).
PROBE_SYS = (
    "You match an abstract figure to a record. Each figure is an 8x8 grid of '#' (filled) and '.' "
    "(empty). You are shown a record about ONE target figure plus a short label for it; decide "
    "which of your figures is that target. Reply with ONLY the label (e.g. {example}).")


def load_figures():
    data = json.load(open(os.path.join(HERE, "figures.json")))
    return data["figures"]  # {F0: {id,pair,grid:[...8 rows...]}}


def grid_block(order, fig):
    """order: list of (label, canonical_id). Returns a text block of labelled grids."""
    out = []
    for label, cid in order:
        out.append(f"[{label}]")
        out.extend("  " + row for row in fig[cid]["grid"])
    return "\n".join(out)


def parse_label(txt, labels):
    """Pick the chosen label out of a possibly-chatty reply; take the LAST match (final answer)."""
    if not txt:
        return None
    found = re.findall(r"[A-Za-z]+\s*\d+", txt)
    norm = [f.replace(" ", "").upper() for f in found]
    cand = [x for x in norm if x in labels]
    return cand[-1] if cand else None


def perm_labels(prefix, canon_ids, rng):
    """Random private labelling: prefix+1.. assigned to a shuffled copy of canon_ids."""
    ids = list(canon_ids)
    rng.shuffle(ids)
    order = [(f"{prefix}{i+1}", cid) for i, cid in enumerate(ids)]
    label_of = {cid: lab for lab, cid in order}
    return order, label_of


# ---------------------------------------------------------------------------------------
# 1. LIVE dyad game
# ---------------------------------------------------------------------------------------
def run_live_game(mname, model, fig, seed):
    rng = random.Random(seed)
    canon = list(fig.keys())
    d_order, d_label = perm_labels("D", canon, rng)        # director's private array
    m_order, m_label = perm_labels("M", canon, rng)        # matcher's independent array
    d_block = grid_block(d_order, fig)
    m_block = grid_block(m_order, fig)
    rsn = reasoning_for(model)

    hist = {cid: [] for cid in canon}   # canonical_id -> list of {rep,desc,words,pick_cid,correct}
    recs = []
    for rep in range(1, R + 1):
        seq = list(canon)
        rng.shuffle(seq)
        for cid in seq:
            # ---- director ----
            prior = hist[cid]
            if prior:
                ph = "\n".join(
                    f"  round {h['rep']}: you said \"{h['desc']}\" -> partner "
                    f"{'FOUND it' if h['correct'] else 'guessed WRONG'}" for h in prior)
                phist = ("\nYour earlier rounds for THIS SAME target (reuse/shorten what worked, "
                         f"repair what failed):\n{ph}\n")
            else:
                phist = ""
            d_user = (f"Your figures:\n{d_block}\n{phist}\nTARGET: {d_label[cid]}\n"
                      f"Describe it for your partner (<= {WORD_BUDGET} words).")
            dr = call(model, DIRECTOR_SYS.format(budget=WORD_BUDGET), d_user,
                      max_tokens=80, reasoning=rsn)
            desc = (dr.get("content") or "").strip().strip('"').replace("\n", " ")
            words = len(desc.split())
            # ---- matcher ----
            if prior:
                mh = "\n".join(
                    f"  round {h['rep']}: partner said \"{h['desc']}\" -> you picked "
                    f"{h['pick'] or '?'} ({'correct' if h['correct'] else 'wrong'})" for h in prior)
                mhist = f"\nEarlier rounds for this target:\n{mh}\n"
            else:
                mhist = ""
            m_user = (f"Your figures:\n{m_block}\n{mhist}\nYour partner describes the TARGET as:\n"
                      f"\"{desc}\"\n\nWhich of your figures is it? Reply with only the label "
                      f"({', '.join(l for l, _ in m_order)}).")
            mr = call(model, MATCHER_SYS.format(example=m_order[0][0]), m_user,
                      max_tokens=64, reasoning=rsn)
            pick = parse_label(mr.get("content"), {l for l, _ in m_order})
            pick_cid = next((c for l, c in m_order if l == pick), None)
            correct = (pick_cid == cid)
            hist[cid].append({"rep": rep, "desc": desc, "words": words, "pick": pick,
                              "pick_cid": pick_cid, "correct": correct})
            recs.append({"phase": "live", "model": mname, "game_seed": seed, "rep": rep,
                         "target": cid, "desc": desc, "words": words, "pick": pick,
                         "pick_cid": pick_cid, "correct": correct,
                         "d_raw": dr.get("content"), "m_raw": mr.get("content"),
                         "usage": [dr.get("usage", {}), mr.get("usage", {})],
                         "err": [dr.get("error"), mr.get("error")]})
    return hist, recs, d_label, d_block


# ---------------------------------------------------------------------------------------
# 4. SINGLE-AGENT monologue baseline (no partner, no feedback)
# ---------------------------------------------------------------------------------------
def run_monologue(mname, model, fig, seed):
    rng = random.Random(seed ^ 0x5151)
    canon = list(fig.keys())
    d_order, d_label = perm_labels("D", canon, rng)
    d_block = grid_block(d_order, fig)
    rsn = reasoning_for(model)
    hist = {cid: [] for cid in canon}
    recs = []
    for rep in range(1, R + 1):
        seq = list(canon)
        rng.shuffle(seq)
        for cid in seq:
            prior = hist[cid]
            if prior:
                ph = "\n".join(f"  pass {h['rep']}: \"{h['desc']}\"" for h in prior)
                phist = f"\nYour earlier labels for THIS SAME figure (keep/shorten):\n{ph}\n"
            else:
                phist = ""
            user = (f"Figures:\n{d_block}\n{phist}\nTARGET: {d_label[cid]}\n"
                    f"Give it a short label (<= {WORD_BUDGET} words).")
            r = call(model, MONO_SYS.format(budget=WORD_BUDGET), user, max_tokens=80, reasoning=rsn)
            desc = (r.get("content") or "").strip().strip('"').replace("\n", " ")
            hist[cid].append({"rep": rep, "desc": desc, "words": len(desc.split()),
                              "correct": None, "pick": None})
            recs.append({"phase": "mono", "model": mname, "game_seed": seed, "rep": rep,
                         "target": cid, "desc": desc, "raw": r.get("content"),
                         "usage": [r.get("usage", {})], "err": [r.get("error")]})
    return hist, recs, d_label, d_block


def elicit_nicknames(mname, model, fig, d_label, d_block, hist, source, seed):
    """Final compressed (<=3-word) coined term per figure -> the opaque label the probe tests."""
    rsn = reasoning_for(model)
    dyadic = (source == "dyadic")
    sys = NICK_SYS_DYAD if dyadic else NICK_SYS_SOLO
    nick, recs = {}, []
    for cid in fig:
        prior = hist[cid]
        if not prior:
            continue
        descs = "\n".join(f"  round {h['rep']}: \"{h['desc']}\"" for h in prior)
        user = (f"Your figures:\n{d_block}\n\nYour descriptions of TARGET {d_label[cid]} so far:\n"
                f"{descs}\n\nGive it the shortest nickname (<= 3 words).")
        r = call(model, sys, user, max_tokens=32, reasoning=rsn)
        nm = (r.get("content") or "").strip().strip('"').replace("\n", " ")
        nick[cid] = nm
        recs.append({"phase": "nick", "source": source, "model": mname, "game_seed": seed,
                     "target": cid, "nick": nm, "raw": r.get("content"),
                     "usage": [r.get("usage", {})], "err": [r.get("error")]})
    return nick, recs


# ---------------------------------------------------------------------------------------
# 2/3. ORDERED vs SHUFFLED replay probe (the load-bearing contrast)
# ---------------------------------------------------------------------------------------
def history_lines(prior, dyadic):
    """Render a per-figure convention record as a list of (string) lines, one per round."""
    lines = []
    for h in prior:
        if dyadic:
            tag = "you FOUND it" if h["correct"] else "you guessed WRONG"
            lines.append(f"round {h['rep']}: partner said \"{h['desc']}\" -> {tag}")
        else:
            lines.append(f"pass {h['rep']}: \"{h['desc']}\"")
    return lines


def run_probe(mname, model, fig, hist, nicknames, source, seed):
    """For each figure, probe a FRESH matcher with the OPAQUE coined nickname, under four arms:
      - coined_only : nickname, NO history  (diagnostic: is the history load-bearing at all?)
      - ordered     : nickname + chronological history
      - reversed    : nickname + reverse-chronological history  (coherence/position artifact control)
      - shuffled    : nickname + randomly permuted history  (SHUF_PERMS perms; the deflationary control)
    The load-bearing contrast is ordered - shuffled, interpretable ONLY where ordered > coined_only
    (history matters). reversed guards against "canonical order parses better" being mistaken for a
    trajectory effect. `source` in {"dyadic","mono"}."""
    rng = random.Random(seed ^ 0xABCD)
    canon = list(fig.keys())
    rsn = reasoning_for(model)
    recs = []
    dyadic = (source == "dyadic")
    intro = ("Your partner referred to ONE target figure over several rounds. Record of what they "
             "said and how it went:" if dyadic
             else "Here are the labels recorded for ONE target figure over several passes:")
    for cid in canon:
        prior = hist[cid]
        nick = nicknames.get(cid)
        if not prior or not nick:
            continue
        base_lines = history_lines(prior, dyadic)
        # fresh matcher array (independent labels), CONSTANT across the four arms for this figure
        p_order, _ = perm_labels("P", canon, rng)
        p_block = grid_block(p_order, fig)
        labels = {l for l, _ in p_order}
        target_label = next(l for l, c in p_order if c == cid)
        label_list = ", ".join(l for l, _ in p_order)

        def probe_once(lines, condition, perm_idx):
            if lines is None:
                hist_intro = ""
            else:
                hist_intro = f"{intro}\n" + "\n".join(lines) + "\n\n"
            user = (f"Your figures:\n{p_block}\n\n{hist_intro}"
                    f"The target is referred to as: \"{nick}\"\n\n"
                    f"Which of your figures is it? Reply with only the label ({label_list}).")
            r = call(model, PROBE_SYS.format(example=p_order[0][0]), user,
                     max_tokens=64, reasoning=rsn)
            pick = parse_label(r.get("content"), labels)
            return {"phase": "probe", "source": source, "model": mname, "game_seed": seed,
                    "target": cid, "nick": nick, "condition": condition, "perm": perm_idx,
                    "n_lines": (0 if lines is None else len(lines)), "pick": pick,
                    "correct": (pick == target_label), "raw": r.get("content"),
                    "usage": [r.get("usage", {})], "err": [r.get("error")]}

        recs.append(probe_once(None, "coined_only", 0))
        recs.append(probe_once(base_lines, "ordered", 0))
        recs.append(probe_once(list(reversed(base_lines)), "reversed", 0))
        for k in range(SHUF_PERMS):
            sl = list(base_lines)
            rng.shuffle(sl)
            recs.append(probe_once(sl, "shuffled", k))
    return recs


# ---------------------------------------------------------------------------------------
MODEL_SEED_OFFSET = {"claude": 11, "gpt": 23, "gemini": 37}  # deterministic (str hash is randomized)


def run_model(mname, model, fig, games):
    allrecs = []
    for g in range(games):
        seed = SEED0 + 1000 * g + MODEL_SEED_OFFSET[mname]
        dh, dr, dl, db = run_live_game(mname, model, fig, seed)
        dnick, dnr = elicit_nicknames(mname, model, fig, dl, db, dh, "dyadic", seed)
        allrecs += dr + dnr
        allrecs += run_probe(mname, model, fig, dh, dnick, "dyadic", seed)
        mh, mr, ml, mb = run_monologue(mname, model, fig, seed)
        mnick, mnr = elicit_nicknames(mname, model, fig, ml, mb, mh, "mono", seed)
        allrecs += mr + mnr
        allrecs += run_probe(mname, model, fig, mh, mnick, "mono", seed)
    return allrecs


def liveness():
    fig = load_figures()
    canon = list(fig.keys())
    rng = random.Random(1)
    order, label = perm_labels("D", canon, rng)
    block = grid_block(order, fig)
    recs = []
    for mname, model in MODELS.items():
        r = call(model, DIRECTOR_SYS.format(budget=WORD_BUDGET),
                 f"Your figures:\n{block}\n\nTARGET: {order[0][0]}\nDescribe it (<= {WORD_BUDGET} words).",
                 max_tokens=80, reasoning=reasoning_for(model))
        print(f"  {mname:7s}: {r.get('content')!r}  cost={r.get('usage',{}).get('cost')}")
        recs.append(r)
    tot, have, miss = billed_cost([recs])  # liveness recs ARE single usage dicts
    print(f"liveness billed=${tot:.5f} (have={have} missing={miss})")


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "liveness"
    fig = load_figures()
    if mode == "liveness":
        liveness()
    elif mode == "preflight":
        recs = run_model("gpt", MODELS["gpt"], fig, games=1)   # cheapest model for pipeline validation
        os.makedirs(os.path.join(HERE, "raw"), exist_ok=True)
        json.dump(recs, open(os.path.join(HERE, "raw", "preflight.json"), "w"), indent=2)  # dump FIRST
        tot, have, miss = flat_cost(recs)
        nfail = sum(1 for r in recs if r["phase"] in ("live", "probe")
                    and r.get("pick") is None)
        print(f"\nPREFLIGHT (gpt, 1 game): {len(recs)} records, {nfail} pick-parse-fails, "
              f"billed=${tot:.5f} (have={have} missing={miss})")
        print(f"  rough full extrapolation (3 models x {N_GAMES} games, gemini cheaper): "
              f"~${tot*3*N_GAMES:.3f} upper-bound")
    elif mode == "full":
        allrecs = []
        os.makedirs(os.path.join(HERE, "raw"), exist_ok=True)
        for mname, model in MODELS.items():
            print(f"=== {mname} ===")
            rs = run_model(mname, model, fig, games=N_GAMES)
            allrecs += rs
            json.dump(allrecs, open(os.path.join(HERE, "raw", "results.json"), "w"), indent=2)  # dump per model
            t, h, m = flat_cost(rs)
            print(f"  {mname}: {len(rs)} records, billed=${t:.5f}")
        tot, have, miss = flat_cost(allrecs)
        print(f"\nFULL: {len(allrecs)} records, billed=${tot:.5f} (have={have} missing={miss})")
    else:
        print("usage: game.py [liveness|preflight|full]")


if __name__ == "__main__":
    main()
