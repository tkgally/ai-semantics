#!/usr/bin/env python3
"""common.py — shared machinery for the relational IMPLICIT-REASSIGNMENT control.

This is the IMPLICIT-reassignment control of result/relational-spontaneous-recency-a (Option A).
Option A found both panel models recover a REASSIGNED coined term by its most-recent binding,
spontaneously (SPONT latest-binding rate 1.000, position at chance, DIRECT on-demand 1.000) ->
claim/relational-order-sensitive-reassignment (order-sensitive / non-commutative in the regime
where recency disambiguates). That claim's sharpest open caveat (scope limit 4 / revision trigger
2) is that "spontaneous" there means QUERY-not-directed, NOT cue-free: Option A's INTRO told the
model the term "was reassigned ... in different rounds you agreed it referred to different
figures." This control removes exactly that sentence and re-measures the SPONT latest-binding rate.

  When a coined term IS used for different referents across several stamped rounds -- WITH NO
  sentence flagging that a reassignment occurred -- and the matcher is asked which referent the
  term picks out (no recency mention), does the model STILL spontaneously weight the round stamp
  (recover the most-recent binding), or does removing the explicit reassignment flag collapse the
  latest-binding-wins behaviour?

A PERSISTING ceiling strongly BOUNDS the surface-artifact reading: latest-binding-wins is not an
artifact of the "was reassigned" wording, strengthening the order-sensitivity claim. A COLLAPSE
to chance (COMMUTATIVE-HERE) NARROWS the claim to the explicit-reassignment frame. The entire
frozen stimuli roster is held BYTE-IDENTICAL to Option A (same sha256); the ONLY manipulation is
the one dropped INTRO sentence -- a clean single-factor control.

Because Option B passed (both models read the round STAMP as a recency value ON DEMAND,
result/relational-stamp-comprehension-b) and the DIRECT manipulation check is carried unchanged
here, a SPONT null is interpretable: it means "comprehends recency on demand but does not
spontaneously weight it WITHOUT the explicit reassignment flag" -- never inflated.

Two query conditions, each built as its own balanced-block roster:
  SPONT  (headline): "Which figure does \"{TERM}\" refer to?" -- NO recency mention. The
         latest-governs answer = the figure agreed at the MAX round; the min-round figure is
         tracked as the symmetric anti-recency diagnostic. Order-sensitivity in EITHER direction
         beating chance is evidence of a non-commutative (path-dependent) convention.
  DIRECT (manipulation check): B-style explicit-recency query ("...in the latest/earliest
         round?"). Re-confirms ON-DEMAND comprehension survives in THIS instrument (figures +
         reassignment + grid). NOT the headline; it gates interpretability of SPONT.

Shortcut-proofing (binding carry-forward 3 -- certify UNSOLVABLE by a positional/lexical
shortcut). Reused verbatim from the Option-B balanced-block proof, now over FIGURES: within each
subset (SPONT, DIRECT) every constant-physical-history-slot strategy scores exactly 1/K AND
every one of the (pool!) fixed figure-preference orderings scores exactly 1/K, and each figure
appears exactly once per record (frequency flat). So no position, lexical, or frequency shortcut
can clear the floor; only spontaneously reading the round stamp as recency can. Asserted at build
and demonstrated on idealized-reader fixtures BEFORE any model is queried (the v4 GO-discipline).

anchor: internal-contrast-only (within-model behavioural contrast over byte-identical content;
no human-comparison claim -- ratified 2026-06-16). The human side of the commutativity contrast
is undischargeable on current resources (Brennan & Clark report an order-INSENSITIVE statistic);
none is owed because no human contrast is asserted here.
"""
import datetime
import json
import os
import re
import string
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "lib")))
from openrouter import PANEL, URL, call, billed_cost  # noqa: E402,F401

RAW = os.path.join(HERE, "raw")
LEDGER_PATH = os.path.join(RAW, "cost-ledger.json")

# A-eligible relational panel carried from v4/B: claude + gemini (both passed Option B).
MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"]}
SEED0 = 20260616

# ---- frozen design parameters (PREREG) --------------------------------------------------
K = 4                          # figures (and rounds) per record
N_BLOCKS_SPONT = 12            # SPONT present-sets -> 48 SPONT records/model
N_BLOCKS_DIRECT = 8            # DIRECT present-sets -> 32 records/model (16 DIR_MR + 16 DIR_LR)
                               # (n_blocks must be divisible by K so target_pos balances uniformly
                               # within each query direction under the Latin square; 8 works, 6
                               # does not -- DIR_MR uses j<K/2, DIR_LR uses j>=K/2 within a block)
# Construction (build_trials): each subset is an independent balanced-block roster. N_BLOCKS
# distinct K-figure present-sets (each figure in exactly N_BLOCKS*K/|pool| sets) x K records each
# under a Latin square, so within each present-set the GOVERNING figure cycles through all 4
# members exactly once AND the governing line's physical history-slot cycles through all 4 slots
# exactly once. Consequence (proven at build, separately per subset): (a) every constant-slot
# position-follower scores exactly 1/K; (b) every fixed figure-preference ordering scores exactly
# 1/K (the figure is uniform over the present-set's members); (c) each figure appears exactly once
# per record, so frequency is flat. Only spontaneously reading the round stamp clears the floors.
POS_CHANCE = 1.0 / K           # 0.25

# Verdict floors (frozen). SPONT order-sensitivity is judged by a Wilson-95 lower bound STRICTLY
# above chance (not a point estimate); DIRECT is the on-demand manipulation gate.
DIRECT_FLOOR = 0.80            # manipulation check: pooled DIRECT accuracy must clear this
SPONT_CI = 1.96                # z for the SPONT order-sensitivity Wilson interval

# Frozen non-contiguous round quadruples (NOT {1,2,3,4}: forces reading the actual stamp value;
# spreads gaps so "max/min round" is the only consistent recency reading). Cycled across records.
ROUND_SETS = [
    [2, 4, 7, 9],
    [1, 3, 6, 8],
    [3, 5, 6, 9],
    [2, 5, 7, 8],
    [1, 4, 5, 9],
    [3, 4, 7, 8],
]

# The coined term being reassigned (a frozen nonce; constant across records -- each record is an
# independent game). Clearly a non-word so no lexical prior bears on which figure it "should" mean.
TERM = "DAX"

# Frozen figure pool: 8 clearly DISTINCT, non-near-twin figures (label tied to identity, stable
# across records). Deliberately NOT near-twins: near-twins (the v4 harvest class) would confound a
# recency failure with a discrimination failure; Option A isolates spontaneous recency-weighting,
# so figures must be trivially discriminable and the ONLY hard step is reading the stamp. The
# answer space is the figure LABEL; the history references a figure by its DESCRIPTION (matcher
# maps description->label via the grid, as in the v4 instrument class). See the design doc and
# PREREG for why dropping near-twins is a deliberate, surfaced deviation from the Option-A sketch.
FIGURES = [
    {"label": "F1", "desc": "a coiled spring"},
    {"label": "F2", "desc": "a five-pointed star"},
    {"label": "F3", "desc": "a crescent moon"},
    {"label": "F4", "desc": "a stack of three cubes"},
    {"label": "F5", "desc": "a single teardrop shape"},
    {"label": "F6", "desc": "a checkerboard square"},
    {"label": "F7", "desc": "a jagged lightning bolt"},
    {"label": "F8", "desc": "a spiral seashell"},
]
LABELS = [f["label"] for f in FIGURES]
DESC = {f["label"]: f["desc"] for f in FIGURES}

# ---- elicitation (forced format; cap 512 so truncation is RARE, not impossible) ----------
MAX_TOKENS = 512  # a reply with finish_reason == "length" is NEVER parsed
REASONING = {"google/": {"effort": "minimal"}}  # config/models.md caveat 1
HARD_STOP_USD = 0.50  # pre-registered hard stop on PROJECTED total billed cost (A is cheap)

SYS = (
    "You are matching a coined term to one of your figures, recalling a short record of how you "
    "and your partner used the term over several rounds of a game. Read the figures and the "
    "record, then answer the single question. Reply with EXACTLY ONE figure label (e.g. {example}) "
    "and NOTHING ELSE -- no explanation, no reasoning, no restatement.")

# IMPLICIT-reassignment INTRO (the sole manipulation vs Option A). It states the stamp convention
# (a higher round number = more recently) and that lines are NOT in round order -- exactly the
# framing B proved both models read and that Option A used. It DELIBERATELY OMITS Option A's
# explicit reassignment flag ("The term was reassigned: in different rounds you agreed it referred
# to different figures."): here the term simply IS used for different figures across stamped rounds,
# with no sentence telling the model a reassignment / choice-among-bindings occurred. The model must
# itself notice the term picks out different figures in different rounds. It still does NOT tell the
# model to weight recency or position, nor that the latest agreement governs. Whether the
# latest-binding-wins behaviour from Option A survives WITHOUT the explicit "was reassigned" wording
# is exactly what this control measures (claim/relational-order-sensitive-reassignment revision
# trigger 2 / scope limit 4). Every other byte of the prompt, and the entire frozen stimuli roster,
# is held identical to Option A (same sha256), so the ONLY difference is this dropped sentence.
INTRO_GRID = "Your figures:"
INTRO_HIST = (
    "Here is a record of how you and your partner used the term \"{term}\" for these figures over "
    "several rounds. Each line is stamped with the round it was said in (a higher round number "
    "means it was said more recently). The lines are NOT necessarily listed in round order:")

# SPONT: no recency mention. DIR_MR / DIR_LR: explicit recency (the manipulation check).
QUERY_TEXT = {
    "SPONT": "Question: Which of your figures does the term \"{term}\" refer to?",
    "DIR_MR": "Question: Which figure did you agree \"{term}\" referred to MOST RECENTLY "
              "(in the latest round)?",
    "DIR_LR": "Question: Which figure did you agree \"{term}\" referred to EARLIEST "
              "(in the very first round)?",
}

STERN = ("\n\nIMPORTANT: your reply must be EXACTLY ONE of these labels ({label_list}) -- a "
         "single label on a single line, with no other text whatsoever.")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def render_grid(present_labels):
    """present_labels in pool (canonical) order. The grid order is a fixed function of the
    present-set, so a 'grid-position' strategy reduces to a fixed figure-preference ordering,
    which scores exactly 1/K (proven at build). Answer space = these labels."""
    return "\n".join(f"- {lab}: {DESC[lab]}" for lab in present_labels)


def render_history(lines):
    """lines: list of {round, label} in PHYSICAL (display) order; figure referenced by DESC."""
    return "\n".join(f'- Round {ln["round"]}: we agreed "{TERM}" referred to {DESC[ln["label"]]}.'
                     for ln in lines)


def build_user(rec):
    grid = render_grid(rec["present"])
    hist = render_history(rec["lines_display"])
    q = QUERY_TEXT[rec["query"]].format(term=TERM)
    label_list = ", ".join(rec["present"])
    return (f"{INTRO_GRID}\n{grid}\n\n{INTRO_HIST.format(term=TERM)}\n{hist}\n\n{q}\n"
            f"Reply with exactly one label ({label_list}) and nothing else.")


# ---- forced parse: reply must be exactly one of the present labels ------------------------
def parse_forced(txt, present):
    """(pick, mode): mode in {strict, non-strict, None}. `present` = set of labels in record."""
    if not txt:
        return None, None
    s = txt.strip().strip(string.punctuation + string.whitespace).upper()
    if s in present:
        return s, "strict"
    # non-strict: a single present label as a whole token on the last non-empty line
    lines = [ln for ln in txt.splitlines() if ln.strip()]
    if lines:
        toks = [w for w in re.findall(r"F[1-8]", lines[-1].upper()) if w in present]
        toks = list(dict.fromkeys(toks))
        if len(toks) == 1:
            return toks[0], "non-strict"
    return None, None


def call_fr(model, system, user, max_tokens=None, temperature=0, retries=4, timeout=120,
            reasoning=None):
    """One completion that ALSO surfaces finish_reason (a length-truncated reply is never
    parsed). Transport mirrored from lib/openrouter.call (usage-include flag, retry/backoff)."""
    key = os.environ["OPENROUTER_API_KEY"]
    if max_tokens is None:
        max_tokens = 4096 if model.startswith("google/") else 64
    body = {"model": model,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
            "temperature": temperature, "max_tokens": max_tokens,
            "usage": {"include": True}}
    if reasoning is not None:
        body["reasoning"] = reasoning
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                URL, data=json.dumps(body).encode(),
                headers={"Authorization": f"Bearer {key}",
                         "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                d = json.load(r)
            ch = d["choices"][0]
            return {"content": (ch["message"].get("content") or "").strip(),
                    "usage": d.get("usage", {}),
                    "finish_reason": ch.get("finish_reason")}
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read().decode()[:150]}"
        except Exception as e:  # noqa: BLE001
            last = f"{type(e).__name__}: {e}"
        time.sleep(2 ** attempt)
    return {"content": None, "usage": {}, "finish_reason": None, "error": last}


def parse_reply(r, present):
    if r.get("finish_reason") == "length":
        return None, None
    return parse_forced(r.get("content"), present)


def call_forced(model, user, present, label_list):
    """One forced call; on transport error / length-truncation / parse-fail, ONE stern retry;
    persistent failure -> NA. Returns (record, pick, mode, retried, usages)."""
    rsn = reasoning_for(model)
    sys_p = SYS.format(example=sorted(present)[0])
    r = call_fr(model, sys_p, user, max_tokens=MAX_TOKENS, reasoning=rsn)
    pick, mode = parse_reply(r, present)
    if not r.get("error") and pick is not None:
        return r, pick, mode, False, [r.get("usage", {})]
    r2 = call_fr(model, sys_p, user + STERN.format(label_list=label_list),
                 max_tokens=MAX_TOKENS, reasoning=rsn)
    pick2, mode2 = parse_reply(r2, present)
    usages = [u for u in (r.get("usage"), r2.get("usage")) if u]
    if pick2 is not None or not r.get("content"):
        return r2, pick2, mode2, True, usages
    return r, pick, mode, True, usages


def flat_cost(recs):
    flat = []
    for r in recs:
        u = r.get("usage")
        if isinstance(u, list):
            flat += [{"usage": x} for x in u if x]
        elif u:
            flat.append({"usage": u})
    return billed_cost([flat])


# ---- cost ledger + pre-registered hard stop ----------------------------------------------
def ledger_load():
    if os.path.exists(LEDGER_PATH):
        return json.load(open(LEDGER_PATH))
    return []


def ledger_total():
    return sum(e["billed_usd"] for e in ledger_load())


def ledger_append(phase, calls, billed, missing, note=""):
    os.makedirs(RAW, exist_ok=True)
    entries = ledger_load()
    entries.append({"phase": phase, "calls": calls, "billed_usd": round(billed, 6),
                    "missing_cost_fields": missing, "note": note,
                    "ts_utc": datetime.datetime.now(datetime.timezone.utc).isoformat()})
    json.dump(entries, open(LEDGER_PATH, "w"), indent=2)
    total = sum(e["billed_usd"] for e in entries)
    print(f"  [ledger] {phase}: ${billed:.5f} ({calls} calls, {missing} missing cost) "
          f"-> cumulative ${total:.5f} (hard stop ${HARD_STOP_USD:.2f})")
    return total


def check_hard_stop(projected_additional_usd, phase):
    spent = ledger_total()
    projected = spent + projected_additional_usd
    print(f"  [gate] {phase}: spent ${spent:.4f} + projected ${projected_additional_usd:.4f} "
          f"= ${projected:.4f} (hard stop ${HARD_STOP_USD:.2f})")
    if projected > HARD_STOP_USD:
        sys.exit(f"HARD STOP: projected total ${projected:.4f} exceeds the pre-registered "
                 f"${HARD_STOP_USD:.2f} cap. Re-design; do not push through.")


def append_jsonl(path, rec):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(rec) + "\n")


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return [json.loads(ln) for ln in f if ln.strip()]
