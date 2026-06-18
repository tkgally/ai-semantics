#!/usr/bin/env python3
"""common.py -- shared machinery for the WORKED-EXAMPLE-SCAFFOLD WITNESS-SEEKING re-run of the
Option-C ORDER-SENSITIVE COMPOSITION probe (non-commuting operation semantics).

WHAT THIS IS (witness-seeking on the CHAINING axis -- the axis the figure-to-figure run LOCALIZED).
The Option-C probe found a SPLIT (claude RESPECTS-ORDER at ceiling; BOTH gemini and gpt FAILED the
on-demand DIRECT gate -> UNINTERPRETABLE). Two easings have since failed to find a witness:
  - K=6->K=4 state-space (2026-06-18-...-k4): OFF-signature; split survived (gemini 0.594, gpt 0.438).
  - figure-to-figure rendering (2026-06-18-...-fig): the on-signature read-off easing; split survived
    (gemini DIRECT 0.656, gpt 0.250). Decisively, even when TOLD THE ORDER on the DIRECT arm, gpt
    applied only ONE of the two moves 65.6% of the time (gemini 21.9%). So the residual difficulty is
    NOT the per-move read-off (the figure-maps removed it) but CHAINING ITSELF -- holding two
    operations and applying BOTH in sequence. essay/witness-seeking-economics and the fig-run result
    name the two un-eased on-signature axes: a WORKED-EXAMPLE SCAFFOLD (demonstrate that both stamped
    moves must be applied) and FEWER CHAINING STEPS. This probe eases the FIRST of those: it is the
    first easing of the CHAINING axis the fig run implicated, and the first easing of a NEW axis
    (the three prior runs eased state-space and read-off, never chaining).

THE SINGLE MANIPULATED VARIABLE IS A WORKED EXAMPLE (added to the byte-identical fig-run rendering).
The underlying trials are BYTE-IDENTICAL to the K=4 / figure-to-figure runs: build_trials.py, SEED0,
the 96 records/model (64 COMP + 32 DIRECT), the geometry, the shortcut-proofing asserts, analyze.py,
the thresholds, and the verdict map are all UNCHANGED, so stimuli.json's sha256 is IDENTICAL
(975e31bc...88ba). The figure-to-figure RENDERING is also unchanged (each move is an explicit
figure->figure table, no positions shown). The ONLY change from the fig run is the insertion of a
single WORKED EXAMPLE block (WORKED_EXAMPLE below) that demonstrates how two moves are combined in
sequence: apply the FIRST move to the starting figure, then apply the SECOND move to the RESULT of
the first. So the cleanest single-variable comparison is fig-run (no scaffold) -> THIS run (scaffold),
on the very same trials, same rendering -- isolating the worked-example / chaining scaffold.

CRITICAL DESIGN CONSTRAINT (per NEXT.md / the fig-run reopen condition): the worked example must ease
the CHAINING axis WITHOUT teaching STAMP-RESOLUTION (how to read the round stamps to decide which move
is first), else it would contaminate the COMP spontaneity measurement. The example therefore (a) uses
a DISJOINT illustrative item set (colored lights, not the figures) and DISJOINT move names (PUSH/TURN,
not STEP/FLIP), so no trial answer or trial map leaks; and (b) gives the order EXPLICITLY ("first PUSH,
then TURN") -- it NEVER shows inferring order from round numbers. It teaches only the chaining
mechanic (feed the first move's output into the second), which is exactly the single-move-reader
failure the fig run implicated; it leaves the COMP question (spontaneously ordering the two moves BY
THEIR STAMPS) untaught. The DIRECT arm (order stated) thus gets the easing; the COMP spontaneity arm
does not.

So this is a WITHIN-TRIAL comparison: the very same 96 trials, fig-rendered, with vs. without one
worked example.
- WITNESS (gemini/gpt clear DIRECT >= 0.80 under the scaffold where they failed without it):
  attributes the fig-run failure to the chaining-demonstration gap -- demonstrating that both moves
  must be applied in sequence let them compose on demand; re-opens the COMP order question for them.
- NON-WITNESS (DIRECT still fails with the scaffold): the composition inability is robust even to a
  worked demonstration of chaining -- a strong on-signature bound that further localizes the
  difficulty and warrants UPDATING the witness-search suspension note -- NOT a closure (a behavioral
  negative is never closed; essay/undischargeable-negative).
- claude = POSITIVE CONTROL: it should still clear DIRECT (and ideally RESPECTS-ORDER); a claude
  failure would mean the scaffold broke the instrument, not that the others are limited.
The DIRECT gate is the empirical arbiter of "easier" -- the easiness claim is MEASURED, not assumed.

Same ratified frame. This is a worked-example / presentation easing of the already-ratified Option-C
instrument under decisions/resolved/relational-rung-iii-path-dependence and the already-ratified
internal-contrast-only relational posture -- the non-commuting operation pair, the two stamped moves,
the stamp-order=composition semantics, the symmetric verdict map, the thresholds, and the thin
adjudication are all unchanged (the trials are byte-identical, the fig rendering unchanged). As with
the K=4 scale easing, the figure-to-figure easing, and the gpt third-model extension, no new
wiki/decisions/open entry is owed; the in-session independent pre-run critic gates instrument validity
(and the no-stamp-leak property of the worked example) and may flag if it judges otherwise. The
binding ADJUDICATION carries over unchanged: an operation-order gap here is THIN (the stamped move-list
and the maps are in the record; single-reader-recoverable), reported as "respects operation order",
NEVER promoted to rung (iii); the rich-side rung (iii) is documented structurally closed for
text-only stimuli. anchor: internal-contrast-only; NO human-comparison claim.

Design (non-commuting operation semantics; FIGURE-TO-FIGURE rendering of the K=4 trials, + scaffold).
  K=4 distinct figures (shapes). A coined token "DAX" starts on a stated figure. TWO kinds of move
  exist, each a permutation of the four figures, given to the model as an explicit figure->figure
  table derived from the record's `track`:
    STEP : the dihedral 4-cycle on the track (p -> (p+1)%4), rendered figure->figure.
    FLIP : the dihedral mirror on the track (p -> 3-p; the 2-swaps 1<->4, 2<->3), rendered fig->fig.
  STEP and FLIP do NOT commute, so applying them in stamp order (lower round first) lands DAX on a
  DIFFERENT figure than reversed. The two stamped move-lines ("Round r: DAX made move STEP/FLIP") are
  shown in round order in HALF the records and reversed in the other half (display order decoupled
  from stamp order), so "apply the moves in printed order" is NOT "apply them in stamp order".

  COMP (headline, spontaneous): the two stamped move-lines are shown (possibly out of round order)
    and the query asks only which figure DAX sits on now -- it does NOT say which move came first. A
    reader who applies the moves in PRINT order, or in a FIXED canonical order, gets the right figure
    only when print/canonical order happens to equal stamp order = exactly HALF the records = 0.50.
    Beating 0.50 (Wilson-95 lower bound > 0.50) requires ordering the two moves BY THEIR STAMPS.
  DIRECT (on-demand manipulation check): same trials; the query states the order explicitly
    ("first ... then ...") and asks for the figure. Confirms the model CAN compose the two moves in
    THIS (figure-map) instrument. Gate: direct_acc >= DIRECT_FLOOR. If it fails, COMP is
    UNINTERPRETABLE (cannot tell spontaneous order-blindness from inability-to-compose).

Shortcut-proofing is INHERITED UNCHANGED from the byte-identical K=4 trials (certified at build by
build_trials.assert_balance and on idealized-reader fixtures): the target figure is uniform over the
4 figures (constant-figure picker = 1/K); print-order and both canonical-order readers = exactly
0.50; start / single-move / reversed-order readers = 0; frequency flat. The track-position picker is
moot (no positions are shown). So only ordering the two moves by their stamps clears the 0.50 bar.
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

# Full three-model panel: the witness targets are gemini + gpt (both FAILED the K=4 DIRECT gate);
# claude is the POSITIVE CONTROL (it RESPECTS-ORDER on these trials at K=4 positions, so it should
# still clear DIRECT under the figure-map rendering if it is a valid non-commuting composition).
MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"], "gpt": PANEL["B"]}
SEED0 = 20260619               # IDENTICAL to the K=4 run -> byte-identical stimuli.json

# ---- frozen design parameters (PREREG) -- IDENTICAL to the K=4 run ----------------------
K = 4                          # figures = answer space
N_BLOCKS_COMP = 16             # COMP blocks x K records -> 64 COMP records/model
N_BLOCKS_DIRECT = 8            # DIRECT blocks x K records -> 32 DIRECT records/model
POS_CHANCE = 1.0 / K           # 1/4 = 0.25 (figure-identity chance)
PRINT_CEILING = 0.50           # print-order / canonical-order reader caps here (proven at build)
DIRECT_FLOOR = 0.80            # on-demand composition manipulation gate
COMP_CI = 1.96                 # z for the COMP composition Wilson interval (LB must exceed 0.50)

SHAPES = ["triangle", "circle", "square", "star"]  # 4 distinct, discriminable; FIXED canonical order
TERM = "DAX"                   # coined nonce; no lexical prior bears on where it sits

# Frozen non-contiguous round PAIRS for the two moves (lo=earlier move, hi=later move).
ROUND_PAIRS = [
    [3, 8],
    [2, 7],
    [4, 9],
    [1, 6],
    [3, 9],
    [2, 8],
]


# ---- the non-commuting operations (0-indexed track positions 0..K-1) --------------------
# These define the GEOMETRY (used by build_trials.py, byte-identical to the K=4 run). The model
# never sees positions; it sees the figure->figure tables derived from each record's `track`.
def op_step(p):
    return (p + 1) % K


def op_flip(p):
    return (K - 1) - p


OPS = {"STEP": op_step, "FLIP": op_flip}
ORDER_OPS = {"SF": ("STEP", "FLIP"), "FS": ("FLIP", "STEP")}


def apply_order(start, order):
    lo, hi = ORDER_OPS[order]
    return OPS[hi](OPS[lo](start))


def swapped_pos(start, order):
    lo, hi = ORDER_OPS[order]
    return OPS[lo](OPS[hi](start))


# ---- elicitation (forced format; cap 512 so truncation is RARE, not impossible) ----------
MAX_TOKENS = 512  # a reply with finish_reason == "length" is NEVER parsed
REASONING = {"google/": {"effort": "minimal"}}  # config/models.md caveat 1
HARD_STOP_USD = 0.60  # pre-registered hard stop on PROJECTED total billed cost (3 models @ K=4)

SYS = (
    "You are tracking where a coined token sits among a set of figures, recalling a short record of "
    "moves you and your partner agreed it made over a couple of rounds of a game. Read the move "
    "rules and the record, then answer the single question. Reply with EXACTLY ONE figure name "
    "(e.g. \"{example}\") and NOTHING ELSE -- no explanation, no reasoning, no restatement.")

INTRO_FIGS = "There are {k} figures: {fig_list}."
INTRO_RULES = (
    "Two kinds of move can be made. Each kind of move sends the token from whichever figure it is "
    "currently on to another figure, exactly as follows:")
INTRO_HIST = (
    "Here is a record of what you and your partner agreed about where the coined token \"{term}\" "
    "sits. \"{term}\" began on {start_phrase}. Then, over two rounds, it made two moves. Each move "
    "is stamped with the round it was agreed in (a higher round number means it was agreed more "
    "recently). The two moves are NOT necessarily listed in round order:")

QUERY_TEXT = {
    "COMP": "Question: Which figure does the token \"{term}\" sit on now?",
    "DIRECT": ("Question: Starting from {start_phrase}, \"{term}\" first (round {r_lo}) made move "
               "{op_lo}, and then (round {r_hi}) made move {op_hi}. Which figure does \"{term}\" "
               "sit on now?"),
}

STERN = ("\n\nIMPORTANT: your reply must be EXACTLY ONE of these figure names ({label_list}) -- a "
         "single figure name on a single line, with no other text whatsoever.")

# ---- THE SINGLE MANIPULATED VARIABLE: a worked example demonstrating CHAINING ------------
# This block (and ONLY this block) is what distinguishes this run from the byte-identical
# figure-to-figure run. It demonstrates the chaining mechanic the fig run localized as the residual
# difficulty (apply the first move to the start, then the second move to the RESULT of the first --
# the exact thing single-move readers fail to do). It is carefully built NOT to teach stamp-resolution
# (the COMP spontaneity question): it uses DISJOINT items (colored lights, not the figures) and
# DISJOINT move names (PUSH/TURN, not STEP/FLIP), so no trial answer or trial map leaks, and it gives
# the order EXPLICITLY ("first PUSH, then TURN") -- it NEVER infers order from round numbers. The
# example arithmetic is self-consistent and correct: PUSH is the forward 3-cycle red->green->blue->red;
# TURN swaps red<->blue and fixes green; starting on green, PUSH -> blue, then TURN(blue) -> red, so the
# marker ends on red (start green, intermediate blue, final red -- all distinct, both moves applied).
WORKED_EXAMPLE = (
    "Here is a worked example using DIFFERENT items and DIFFERENT moves, only to show how two moves "
    "are combined in sequence. Suppose there are three lights -- a red light, a green light, a blue "
    "light -- and two example moves:\n"
    "- Move PUSH: a red light becomes a green light, a green light becomes a blue light, a blue light "
    "becomes a red light.\n"
    "- Move TURN: a red light becomes a blue light, a green light becomes a green light, a blue light "
    "becomes a red light.\n"
    "Suppose a marker starts on a green light and first makes move PUSH, then makes move TURN. Apply "
    "the FIRST move to the start: PUSH sends a green light to a blue light, so after PUSH the marker "
    "is on a blue light. Then apply the SECOND move to that result: TURN sends a blue light to a red "
    "light, so after TURN the marker is on a red light. So the marker ends on a red light. The point "
    "of the example: apply the first move to the starting figure, then apply the second move to the "
    "RESULT of the first move -- BOTH moves are applied, one after the other.")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def shape_phrase(shape):
    return f"a {shape}"


def move_map(track, op):
    """The figure->figure table for `op`, derived from this record's `track` (track[p] = the figure
    at position p). step_map[fig] = figure one position forward; flip_map[fig] = figure at the mirror
    position. Returned keyed by figure name; rendered in FIXED canonical SHAPES order so no positional
    information leaks."""
    fn = OPS[op]
    pos = {fig: p for p, fig in enumerate(track)}
    return {fig: track[fn(pos[fig])] for fig in track}


def render_rules(track):
    """The two move tables (STEP, FLIP), each listing all K figure->figure mappings in canonical
    SHAPES order. No positions appear."""
    out = []
    for op in ("STEP", "FLIP"):
        mp = move_map(track, op)
        parts = ", ".join(f"{shape_phrase(s)} becomes {shape_phrase(mp[s])}" for s in SHAPES)
        out.append(f"- Move {op}: {parts}.")
    return "\n".join(out)


def render_history(rec):
    """the two stamped move-lines, in the record's frozen DISPLAY order (decoupled from stamp
    order). Each line names which move was made in which round (the move's effect is in the rules)."""
    out = []
    for ln in rec["hist_display"]:
        out.append(f'- Round {ln["round"]}: "{TERM}" made move {ln["op"]}.')
    return "\n".join(out)


def build_user(rec):
    track = rec["track"]
    start_phrase = shape_phrase(rec["start_shape"])
    fig_list = ", ".join(shape_phrase(s) for s in SHAPES)
    rules = render_rules(track)
    if rec["query"] == "DIRECT":
        q = QUERY_TEXT["DIRECT"].format(
            term=TERM, start_phrase=start_phrase, r_lo=rec["r_lo"], r_hi=rec["r_hi"],
            op_lo=rec["op_lo"], op_hi=rec["op_hi"])
    else:
        q = QUERY_TEXT["COMP"].format(term=TERM)
    hist = render_history(rec)
    label_list = ", ".join(shape_phrase(s) for s in SHAPES)
    return (f"{INTRO_FIGS.format(k=K, fig_list=fig_list)}\n\n"
            f"{INTRO_RULES}\n{rules}\n\n"
            f"{WORKED_EXAMPLE}\n\n"
            f"{INTRO_HIST.format(term=TERM, start_phrase=start_phrase)}\n{hist}\n\n{q}\n"
            f"Reply with exactly one figure name ({label_list}) and nothing else.")


# ---- forced parse: reply must be exactly one of the present shape names ------------------
def parse_forced(txt, present):
    """(pick, mode): mode in {strict, non-strict, None}. `present` = set of shape words (lower)."""
    if not txt:
        return None, None
    s = txt.strip().strip(string.punctuation + string.whitespace).lower()
    m = re.fullmatch(r"(?:an?\s+)?([a-z]+)", s)
    if m and m.group(1) in present:
        return m.group(1), "strict"
    lines = [ln for ln in txt.splitlines() if ln.strip()]
    if lines:
        toks = [w for w in re.findall(r"[a-z]+", lines[-1].lower()) if w in present]
        toks = list(dict.fromkeys(toks))
        if len(toks) == 1:
            return toks[0], "non-strict"
    return None, None


def call_fr(model, system, user, max_tokens=None, temperature=0, retries=4, timeout=120,
            reasoning=None):
    """One completion that ALSO surfaces finish_reason (a length-truncated reply is never parsed)."""
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
    sys_p = SYS.format(example=shape_phrase(sorted(present)[0]))
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
