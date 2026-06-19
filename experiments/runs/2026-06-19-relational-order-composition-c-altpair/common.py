#!/usr/bin/env python3
"""common.py -- shared machinery for the ALT-PAIR GENERALITY re-run of the Option-C ORDER-SENSITIVE
COMPOSITION probe (a DIFFERENT non-commuting operation pair; figure-to-figure rendering; working-
surface format).

WHAT THIS IS (a generality test of the working-surface composition WITNESS over the OPERATION PAIR).
The execution-format (working-surface) run -- result/relational-order-composition-c-reasoning-scaffold
-- found a WITNESS: on the byte-identical figure-to-figure trials, opening a working surface (step-by-
step output permitted, FINAL-tag parsed; reasoning-effort knob held constant) flipped BOTH gemini and
gpt from UNINTERPRETABLE (forced single-token) to RESPECTS-ORDER at/near ceiling, so all three models
compose the two non-commuting moves given a place to externalize the execution. essay/output-channel-
confound draws the general lesson (the output channel is an instrument axis, a capability-masker) and
claims the dissolution reflects a composition CAPACITY, not an artifact of the one STEP/FLIP
instrument. That generalization is the open question this probe tests on a SINGLE substantive change.

THE SINGLE MANIPULATED VARIABLE vs the witness run IS THE OPERATION PAIR. Every prior Option-C run --
incl. the witness run -- used the dihedral pair STEP (the 4-cycle p->(p+1)%4) and FLIP (the reflection
p->3-p); the two generate the dihedral group D4. THIS run swaps that pair for a GENUINELY DIFFERENT
non-commuting pair:
    CYCLE : the 3-cycle (1 2 3) on the track positions (0 fixed; 1->2, 2->3, 3->1).
    SWAP  : the double transposition (0 1)(2 3) (positions 0<->1 and 2<->3).
CYCLE and SWAP generate A4 (the alternating group), NOT the dihedral D4 -- a different group, a
different cycle structure (a 3-cycle + a double transposition vs a 4-cycle + a reflection). So this is
a generality test over the operation pair, NOT a relabeling of the same pair. Everything else is held
identical to the witness run: K=4, the figure-to-figure rendering, the working-surface elicitation
(FINAL-tag parser, MAX_TOKENS=1024, gemini effort minimal held constant), the two arms (COMP + DIRECT),
SHAPES, TERM, ROUND_PAIRS, the thresholds, the symmetric verdict map, and the thin adjudication. Only
the two permutations (and their honest model-facing labels CYCLE/SWAP) and the balanced VALID_CONFIGS
differ; the stimuli are FRESHLY built (a new sha256, recorded in PREREG.md before any finding-bearing
call).

Reading the outcome (per model; the DIRECT gate is the empirical arbiter of composability on THIS pair,
so the easiness claim is MEASURED, not assumed):
- REPLICATES (all three clear DIRECT >= 0.80 and RESPECTS-ORDER on the alt pair): the working-surface
  composition witness generalizes BEYOND the specific STEP/FLIP pair -- strengthens essay/output-
  channel-confound's "capacity, not one-instrument artifact" reading.
- DOES NOT REPLICATE (a model that cleared DIRECT on STEP/FLIP fails it here): the witness is pair-
  specific -- the working surface does not by itself confer composition on an arbitrary non-commuting
  pair; bounds the generalization (still undischargeable, per essay/undischargeable-negative -- a
  behavioral negative is never a capacity verdict).
- claude = POSITIVE CONTROL: it should clear DIRECT (and ideally RESPECTS-ORDER); a claude failure
  would mean the alt pair broke the instrument, not that the others are limited.

Same ratified frame. This is a WITHIN-FRAME generality variation of the already-ratified Option-C
instrument under decisions/resolved/relational-rung-iii-path-dependence and the already-ratified
internal-contrast-only relational posture -- the stamp-order=composition semantics, the figure-to-
figure rendering, the working-surface format, the symmetric verdict map, the thresholds, and the thin
adjudication are all unchanged; only the non-commuting pair varies. As with the K=4 scale easing, the
figure-to-figure rendering, the worked-example scaffold, the gpt third-model extension, and the
working-surface easing -- none of which owed a new decision -- no new wiki/decisions/open entry is
owed; the operation pair is not a parameter that decision froze. The in-session independent pre-run
critic gates instrument validity and may flag if it judges otherwise. The binding ADJUDICATION carries
over unchanged: an operation-order gap here is THIN (the stamped move-list and the figure maps are in
the record; single-reader-recoverable), reported as "respects operation order", NEVER promoted to rung
(iii); the rich-side rung (iii) is documented structurally closed for text-only stimuli. anchor:
internal-contrast-only; NO human-comparison claim. NOTE: permitting a working surface does NOT make
the COMP arm non-spontaneous -- COMP still does NOT state the order, so the model must still DECIDE to
order by the stamps; the scratchpad only lets it externalize whatever ordering it chooses.

Design (DIFFERENT non-commuting operation pair; FIGURE-TO-FIGURE rendering, WORKING-SURFACE format).
  K=4 distinct figures (shapes). A coined token "DAX" starts on a stated figure. TWO kinds of move
  exist, each a permutation of the four figures, given to the model as an explicit figure->figure
  table derived from the record's `track`:
    CYCLE : the 3-cycle (1 2 3) on the track (0 fixed; 1->2, 2->3, 3->1), rendered figure->figure.
    SWAP  : the double transposition (0 1)(2 3) on the track, rendered figure->figure.
  CYCLE and SWAP do NOT commute, so applying them in stamp order (lower round first) lands DAX on a
  DIFFERENT figure than reversed. The two stamped move-lines ("Round r: DAX made move CYCLE/SWAP") are
  shown in round order in HALF the records and reversed in the other half (display order decoupled
  from stamp order), so "apply the moves in printed order" is NOT "apply them in stamp order".

  COMP (headline, spontaneous): the two stamped move-lines are shown (possibly out of round order)
    and the query asks only which figure DAX sits on now -- it does NOT say which move came first. A
    reader who applies the moves in PRINT order, or in a FIXED canonical order, gets the right figure
    only when print/canonical order happens to equal stamp order = exactly HALF the records = 0.50.
    Beating 0.50 (Wilson-95 lower bound > 0.50) requires ordering the two moves BY THEIR STAMPS.
  DIRECT (on-demand manipulation check): same trials; the query states the order explicitly
    ("first ... then ...") and asks for the figure. Confirms the model CAN compose the two moves in
    THIS (alt-pair figure-map) instrument. Gate: direct_acc >= DIRECT_FLOOR. If it fails, COMP is
    UNINTERPRETABLE (cannot tell spontaneous order-blindness from inability-to-compose).

Shortcut-proofing is RE-CERTIFIED for this pair at build (build_trials.assert_balance and the
idealized-reader fixtures): the target figure is uniform over the 4 figures (constant-figure picker =
1/K); print-order and both canonical-order readers = exactly 0.50; start / single-move (CYCLE-only,
SWAP-only) / reversed-order readers = 0; frequency flat. The track-position picker is moot (no
positions are shown). So only ordering the two moves by their stamps clears the 0.50 bar.
"""
import datetime
import json
import os
import re
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
# A DIFFERENT non-commuting pair from the STEP(4-cycle)/FLIP(reflection) dihedral pair of the witness
# run: CYCLE is a 3-cycle and SWAP a double transposition; the two generate A4, NOT the dihedral D4.
# These define the GEOMETRY (used by build_trials.py). The model never sees positions; it sees the
# figure->figure tables derived from each record's `track`. (K=4-specific permutations.)
def op_cycle(p):
    """3-cycle (1 2 3) on the 4 track positions: position 0 fixed; 1->2, 2->3, 3->1."""
    return (0, 2, 3, 1)[p]


def op_swap(p):
    """double transposition (0 1)(2 3): positions 0<->1 and 2<->3."""
    return (1, 0, 3, 2)[p]


OPS = {"CYCLE": op_cycle, "SWAP": op_swap}
ORDER_OPS = {"CS": ("CYCLE", "SWAP"), "SC": ("SWAP", "CYCLE")}


def apply_order(start, order):
    lo, hi = ORDER_OPS[order]
    return OPS[hi](OPS[lo](start))


def swapped_pos(start, order):
    lo, hi = ORDER_OPS[order]
    return OPS[lo](OPS[hi](start))


# ---- elicitation (WORKING-SURFACE format; cap raised to 1024 so working rarely truncates) ----
# THE SINGLE MANIPULATED VARIABLE vs the fig run: the model MAY now think step by step and show its
# working, then must end with "FINAL: <figure>". The reasoning-effort knob is held CONSTANT (gemini
# stays at effort minimal, exactly as in the four prior runs); the working surface is opened only in
# the visible OUTPUT channel. The cap raise (512 -> 1024) and the FINAL-tag parser are necessary
# consequences of permitting working, not independent manipulations.
MAX_TOKENS = 1024  # a reply with finish_reason == "length" is NEVER parsed (NA/retry)
REASONING = {"google/": {"effort": "minimal"}}  # HELD CONSTANT with the four prior runs
HARD_STOP_USD = 1.50  # pre-registered hard stop on PROJECTED total billed cost (working raises out-tok)

SYS = (
    "You are tracking where a coined token sits among a set of figures, recalling a short record of "
    "moves you and your partner agreed it made over a couple of rounds of a game. Read the move "
    "rules and the record, then work out the answer. You MAY think step by step and show your "
    "working if it helps. When you are done, write your final answer on the LAST line in EXACTLY "
    "this form: FINAL: <figure name> (for example, \"FINAL: {example}\").")

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

STERN = ("\n\nIMPORTANT: end your reply with a line of the form 'FINAL: <figure>', where <figure> is "
         "EXACTLY ONE of these figure names ({label_list}).")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def shape_phrase(shape):
    return f"a {shape}"


def move_map(track, op):
    """The figure->figure table for `op` (CYCLE or SWAP), derived from this record's `track`
    (track[p] = the figure at position p): map[fig] = track[op(position-of-fig)]. Returned keyed by
    figure name; rendered in FIXED canonical SHAPES order so no positional information leaks."""
    fn = OPS[op]
    pos = {fig: p for p, fig in enumerate(track)}
    return {fig: track[fn(pos[fig])] for fig in track}


def render_rules(track):
    """The two move tables (STEP, FLIP), each listing all K figure->figure mappings in canonical
    SHAPES order. No positions appear."""
    out = []
    for op in ("CYCLE", "SWAP"):
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
            f"{INTRO_HIST.format(term=TERM, start_phrase=start_phrase)}\n{hist}\n\n{q}\n"
            f"You may show your working. End with a line of the form: FINAL: <figure>, where the "
            f"figure is one of: {label_list}.")


# ---- working-surface parse: extract the FINAL-tagged figure (never bias toward the target) ------
def parse_forced(txt, present):
    """(pick, mode): mode in {final-tag, last-line, None}. `present` = set of shape words (lower).

    The model may now produce step-by-step working, so we must read ONLY the declared final answer:
      1. PRIMARY: the LAST 'FINAL: <figure>' / 'FINAL ANSWER: <figure>' tag whose figure is present.
         The figure may be bare ("FINAL: circle") or with an article / quotes ("FINAL: a circle").
      2. FALLBACK (no tag): the LAST non-empty line, if it contains EXACTLY ONE present figure word.
    Reasoning text in the body is never scored -- only the final declaration. Returns the matched
    shape word (lower) or None. This parser is target-blind: it keys on position in the reply, not on
    which figure is correct."""
    if not txt:
        return None, None
    low = txt.lower()
    tags = re.findall(r"final(?:\s+answer)?\s*[:\-]+\s*[\"']?(?:an?\s+)?([a-z]+)", low)
    tags = [t for t in tags if t in present]
    if tags:
        return tags[-1], "final-tag"
    # fallback: last non-empty line with exactly one present figure word
    lines = [ln for ln in txt.splitlines() if ln.strip()]
    if lines:
        toks = [w for w in re.findall(r"[a-z]+", lines[-1].lower()) if w in present]
        toks = list(dict.fromkeys(toks))
        if len(toks) == 1:
            return toks[0], "last-line"
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
