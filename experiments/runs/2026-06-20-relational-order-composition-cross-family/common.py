#!/usr/bin/env python3
"""common.py -- shared machinery for the CROSS-FAMILY (heterogeneous-operation) extension of the
Option-C ORDER-SENSITIVE COMPOSITION probe (working-surface format).

WHAT THIS IS (the cross-family generality axis: does the working-surface composition WITNESS extend
to composing two operations of DIFFERENT KINDS?).
Every prior Option-C run composed two (or three) operations of the SAME family: position
permutations rendered as opaque figure->figure tables (STEP/FLIP=D4, CYCLE/SWAP=A4, generic S6). The
working-surface run found a WITNESS and the alt-pair / K=6 / three-move runs replicated a composition
CAPACITY across the operation pair, grid size, and depth axes -- all panel-concordant RESPECTS-ORDER.
But to the model those were all the same task: compose two opaque permutations of one ground set.
claim/relational-order-sensitive-reassignment scope limit 2 names the still-untested generality axis
verbatim -- "generality (image referents, cross-family dyads) is untested" -- and
result/relational-order-composition-three-move (+ essay/witness-seeking-economics) names a *different
kind* of composition (not one more move of the same kind) as the higher-information next step.

THE SINGLE NEW HYPOTHESIS vs every prior Option-C run: the two stamped operations are TRANSPARENTLY
HETEROGENEOUS -- one moves a token in space, the other changes the token's attribute -- and they are
cross-conditional so they do NOT commute. The model must bind a SPATIAL update and an ATTRIBUTE
update in stamp order. This is the relational axis's core (composing updates of different kinds), and
it has a higher prior of strain than another homogeneous-permutation instrument, because the two
operations act on different dimensions of the same state.

THE TWO HETEROGENEOUS OPERATIONS (a coined token "DAX" lives on a row of K spots; each spot holds a
token of some COLOR; DAX has a color too).
  SWAP    (a SPATIAL move):    the tokens at two named spots exchange places (color travels with the
                               token). Acts on POSITION.
  RECOLOR (an ATTRIBUTE move): the token at one named spot is repainted a stated color. Acts on COLOR.
DAX always starts on one of the two SWAP spots, so SWAP moves DAX. RECOLOR targets one of the two
SWAP spots. They NON-COMMUTE on DAX's final color: applying SWAP first moves DAX out of (or into) the
recolor spot before the repaint lands, so whether DAX catches the new color depends on the order.

  Four geometry CELLS = recolor_target {a = DAX's start spot, b = the swap partner} x stamp_first
  {SWAP, RECOLOR}. Simulating DAX's (spot,color) through the two ops in stamp order gives, for DAX's
  start color C0 and the recolor color Cr (always C0 != Cr):
    cell (SWAP-first, recolor@a): DAX a->b, then recolor a hits the OTHER token -> DAX keeps C0.
    cell (SWAP-first, recolor@b): DAX a->b, then recolor b hits DAX        -> DAX = Cr.
    cell (RECOLOR-first, recolor@a): recolor a hits DAX -> Cr, then DAX a->b -> DAX = Cr.
    cell (RECOLOR-first, recolor@b): recolor b hits OTHER, then DAX a->b    -> DAX keeps C0.
  So the final color is C0 in cells {SWAP@a, RECOLOR@b} and Cr in {SWAP@b, RECOLOR@a}. The answer is
  determined by NEITHER the stamp order alone NOR the geometry alone -- only by BOTH together. So a
  reader who knows the order but not the geometry, OR the geometry but not the order, scores at most
  PRINT_CEILING = 0.50 (proven at build); ONLY composing the spatial and attribute updates IN STAMP
  ORDER recovers the color (= 1.0). Beating 0.50 (Wilson-95 lower bound > 0.50) = order-sensitive
  cross-family composition.

WHY THE 0.50 CEILING (same interpretive force as every prior Option-C run, re-proven for this
instrument in build_trials.assert_balance over the actual records): with the four cells equally
frequent the answer is C0 half the time and Cr half the time, so every non-composing reader tops out
at exactly 0.50 --
  - report DAX's start color C0 (= ignore RECOLOR / SWAP-only)             -> 0.50
  - report the recolor color Cr (= assume the repaint always catches DAX)  -> 0.50
  - apply only RECOLOR to DAX (ignore the SWAP)                            -> 0.50
  - apply both in a FIXED order regardless of stamps (SWAP-then-RECOLOR)   -> 0.50
  - apply both in the other FIXED order (RECOLOR-then-SWAP)                -> 0.50
  - apply both in PRINT/display order (decoupled from stamps)              -> 0.50
  - report any FIXED spot's initial or single-op color, or a CONST color   -> <= 1/numcolors-ish, < 0.50
Only a reader that applies the two operations in the per-trial STAMP order clears 0.50. (Note: unlike
the homogeneous-permutation runs, where a reversed-order reader scored 0, here a fixed-order reader
scores 0.50 -- with two heterogeneous ops and a binary {C0,Cr} answer a fixed order is right half the
time, exactly as canonical/print readers scored 0.50 in the original two-move STEP/FLIP run. The
ceiling is identical; what clears it is reading the per-trial order.)

Reading the outcome (per model; the DIRECT gate is the empirical arbiter of cross-family
composability, so the difficulty is MEASURED, not assumed):
- RESPECTS-ORDER (clears DIRECT >= 0.80 and COMP Wilson-LB > 0.50): the working-surface composition
  capacity extends to a HETEROGENEOUS operation pair -- corroborates the capacity reading on the
  cross-family axis claim scope limit 2 named; addresses a named generality gap.
- UNINTERPRETABLE (DIRECT < 0.80): the model cannot compose a spatial + an attribute update on demand
  in this instrument even WITH a working surface -- a cross-family-specific gap. Still UNDISCHARGEABLE
  (a behavioral negative is never a capacity verdict, per essay/undischargeable-negative) and still
  THIN; would be the FIRST non-witness since the working surface was opened, and an
  essay/output-channel-confound trigger-(b)-style contrast (a negative surviving the wide channel),
  to be reported as a witness-search reopening on a new axis, never as "M cannot".
- claude = POSITIVE CONTROL: it should clear DIRECT (ideally RESPECTS-ORDER); a claude failure would
  mean the cross-family instrument broke, not that the others are limited.

Same ratified frame, surfaced for the critic. This is a within-frame OPERATION-KIND variation of the
already-ratified Option-C instrument under decisions/resolved/relational-rung-iii-path-dependence and
the ratified internal-contrast-only relational posture: the stamp-order = composition semantics, the
working-surface format, the 0.50 print-ceiling, the symmetric verdict map, and the THIN adjudication
are all unchanged; only the KIND of the two operations (heterogeneous spatial+attribute, instead of a
homogeneous permutation pair) varies -- and, as a forced consequence, the state carries a color
attribute and the answer is a color rather than a figure. The decision adopted "non-commuting
operation semantics" AGNOSTIC to which operations realize them and did not freeze the operation kind
(indeed it explicitly contemplated "rotate / move" edits); like the alt-pair D4->A4 change, the K
grid size, and the move count -- none of which owed a new decision -- the operation-kind change is
SURFACED here and the design states no new wiki/decisions/open entry is owed; the independent pre-run
critic gates that judgement and may rule otherwise (if so, open a decision and mark the result
contingent). The binding ADJUDICATION carries over unchanged: an operation-order gap here is THIN
(the stamped operation list, the spots, and the colors are in the record; single-reader-recoverable),
reported as "respects operation order", NEVER promoted to rung (iii); the rich-side rung (iii) is
documented structurally closed for text-only stimuli. anchor: internal-contrast-only; NO
human-comparison claim. NOTE: permitting a working surface does NOT make the COMP arm non-spontaneous
-- COMP still does NOT state the order, so the model must still DECIDE to order the two operations by
their stamps; the scratchpad only lets it externalize whatever ordering it chooses.
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

# Full three-model panel: claude = POSITIVE CONTROL; gemini + gpt = the cross-family targets (all
# three cleared the two-move DIRECT gate once a working surface was opened -- the question is whether
# a HETEROGENEOUS operation pair defeats on-demand composition even WITH the scratchpad).
MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"], "gpt": PANEL["B"]}
SEED0 = 20260620               # placement seed (stimuli.json differs from every prior run -> new sha)

# ---- frozen design parameters (PREREG) -- two HETEROGENEOUS moves on a K=4 row -----------------
K = 4                          # number of spots in the row
N_BLOCKS_COMP = 12             # 4 cells x 3 geoms -> 12 blocks x 6 colors -> 72 COMP records/model
N_BLOCKS_DIRECT = 12           # 4 cells x 3 geoms -> 12 blocks x 3 colors -> 36 DIRECT records/model
PRINT_CEILING = 0.50           # every non-composing reader's cap (proven at build)
DIRECT_FLOOR = 0.80            # on-demand cross-family composition gate
COMP_CI = 1.96                 # z for the COMP composition Wilson interval (LB must exceed 0.50)

# 6 distinct colors = the answer space (a const-color picker scores 1/6 ~= 0.167). FIXED order.
COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]
NUM_COLORS = len(COLORS)
POS_CHANCE = 1.0 / NUM_COLORS   # 1/6 ~= 0.1667 (color-identity chance)
SHAPE = "block"                 # the tokens are identical plain "blocks"; DAX is named, not shaped
TERM = "DAX"                    # coined nonce; no lexical prior bears on it

MOVE_NAMES = ["SWAP", "RECOLOR"]   # the two heterogeneous operation kinds; carry NO inherent order

# The 4 geometry CELLS: (recolor_target, stamp_first). recolor_target in {"a","b"} where a = DAX's
# start spot, b = the swap partner spot; stamp_first in {"SWAP","RECOLOR"} = which op has the lower
# round stamp (is applied first). Answer = C0 in {(a,SWAP),(b,RECOLOR)}; Cr in {(b,SWAP),(a,RECOLOR)}.
CELLS = [("a", "SWAP"), ("b", "SWAP"), ("a", "RECOLOR"), ("b", "RECOLOR")]

# Three (a,b) spot geometries per cell (a = DAX start / swap spot 1, b = swap spot 2). Chosen so that
# across the 12 (cell x geom) selections every spot appears as 'a' and as 'b' a balanced number of
# times (verified by assert_balance's track-position check). a != b always.
GEOMS = [(0, 1), (1, 2), (2, 3), (3, 0)]   # cycled across the 4 cells x 3 geoms = 12 (one repeats)

# Frozen round PAIRS (r1 < r2; lo = earlier op, hi = later op). Non-contiguous; cycled across blocks.
ROUND_PAIRS = [[2, 6], [1, 5], [3, 8], [2, 7], [4, 9], [1, 6],
               [3, 7], [2, 8], [1, 7], [4, 8], [3, 9], [2, 9]]

# The 2 display orders of the two stamped op-lines (index into the stamp-ordered [first, second]
# list). Used balanced per block so the print-order reader hits its proven 0.50 ceiling.
DISPLAY_PERMS = [(0, 1), (1, 0)]


# ---- the heterogeneous operators, as functions on DAX's (spot, color) state ----------------
def apply_op(name, spot, color, a, b, recolor_target_spot, recolor_color):
    """Apply one operation to DAX's (spot, color). SWAP exchanges spots a<->b (DAX moves if on one of
    them); RECOLOR repaints whatever sits on `recolor_target_spot` (DAX recolored iff it is there)."""
    if name == "SWAP":
        if spot == a:
            return b, color
        if spot == b:
            return a, color
        return spot, color
    if name == "RECOLOR":
        if spot == recolor_target_spot:
            return spot, recolor_color
        return spot, color
    raise ValueError(name)


def apply_seq(seq, start_spot, start_color, a, b, recolor_target_spot, recolor_color):
    """Apply a sequence of op names left-to-right (seq[0] first) to DAX's state; return (spot,color)."""
    spot, color = start_spot, start_color
    for nm in seq:
        spot, color = apply_op(nm, spot, color, a, b, recolor_target_spot, recolor_color)
    return spot, color


def final_color(rec, order):
    """DAX's final color when the two ops are applied in `order` (a tuple of the two move names)."""
    rt = rec["a"] if rec["recolor_target"] == "a" else rec["b"]
    _, col = apply_seq(order, rec["a"], rec["start_color"], rec["a"], rec["b"], rt,
                       rec["recolor_color"])
    return col


# ---- elicitation (WORKING-SURFACE format; cap 1024 so working rarely truncates) ----
# The working-surface elicitation is held byte-identical in spirit to the prior Option-C runs: the
# model MAY think step by step and show its working, then must end with "FINAL: <color>". The
# reasoning-effort knob is held CONSTANT (gemini stays at effort minimal).
MAX_TOKENS = 1024  # a reply with finish_reason == "length" is NEVER parsed (NA/retry)
REASONING = {"google/": {"effort": "minimal"}}  # HELD CONSTANT with the prior working-surface runs
HARD_STOP_USD = 1.50  # pre-registered hard stop on PROJECTED total billed cost

SYS = (
    "You are tracking the color of a coined token, recalling a short record of moves you and your "
    "partner agreed it was involved in over a few rounds of a game. Read the move rules and the "
    "record, then work out the answer. You MAY think step by step and show your working if it helps. "
    "When you are done, write your final answer on the LAST line in EXACTLY this form: "
    "FINAL: <color> (for example, \"FINAL: {example}\").")

INTRO_SCENE = (
    "There are {k} spots in a row, numbered spot 1 to spot {k}. A token sits on each spot. Right now "
    "the tokens are colored as follows: {coloring}. One of the tokens is a coined token called "
    "\"{term}\".")
INTRO_RULES = (
    "Two kinds of move can be made to the tokens. They work as follows:\n"
    "- A SWAP move names two spots; the tokens on those two spots exchange places (each token keeps "
    "its own color as it moves).\n"
    "- A RECOLOR move names one spot and a color; the token on that spot is repainted that color "
    "(it does not move).")
INTRO_HIST = (
    "Here is a record of what you and your partner agreed happened to \"{term}\" over two rounds. "
    "\"{term}\" began on spot {a}, colored {c0}. Each move is stamped with the round it was agreed "
    "in (a higher round number means it was agreed more recently). The two moves are NOT necessarily "
    "listed in round order:")

QUERY_TEXT = {
    "COMP": "Question: What color is the token \"{term}\" now?",
    "DIRECT": ("Question: Starting from spot {a} colored {c0}, \"{term}\" was first (round {r1}) "
               "involved in {desc1}, and then (round {r2}) involved in {desc2}. What color is "
               "\"{term}\" now?"),
}

STERN = ("\n\nIMPORTANT: end your reply with a line of the form 'FINAL: <color>', where <color> is "
         "EXACTLY ONE of these colors ({label_list}).")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def _swap_desc(rec):
    return f"a SWAP of the tokens on spot {rec['a'] + 1} and spot {rec['b'] + 1}"


def _recolor_desc(rec):
    rt = rec["a"] if rec["recolor_target"] == "a" else rec["b"]
    return f"a RECOLOR of the token on spot {rt + 1} to {rec['recolor_color']}"


def op_desc(rec, name):
    return _swap_desc(rec) if name == "SWAP" else _recolor_desc(rec)


def render_coloring(rec):
    """The initial coloring of all K spots, spot 1..K, in physical order (spots are 1-indexed to the
    model). DAX's spot carries C0; the others carry the frozen distractor colors."""
    parts = []
    for p in range(K):
        parts.append(f"spot {p + 1} holds a {rec['init_colors'][p]} token")
    return ", ".join(parts)


def render_history(rec):
    """The two stamped op-lines, in the record's frozen DISPLAY order (decoupled from stamp order).
    Each line names which kind of move was made in which round and its parameters."""
    out = []
    for ln in rec["hist_display"]:
        out.append(f'- Round {ln["round"]}: {ln["desc"]}.')
    return "\n".join(out)


def build_user(rec):
    coloring = render_coloring(rec)
    label_list = ", ".join(COLORS)
    if rec["query"] == "DIRECT":
        rounds = rec["rounds"]
        first, second = rec["stamp_order"]
        q = QUERY_TEXT["DIRECT"].format(
            term=TERM, a=rec["a"] + 1, c0=rec["start_color"],
            r1=rounds[0], r2=rounds[1],
            desc1=op_desc(rec, first), desc2=op_desc(rec, second))
    else:
        q = QUERY_TEXT["COMP"].format(term=TERM)
    hist = render_history(rec)
    return (f"{INTRO_SCENE.format(k=K, coloring=coloring, term=TERM)}\n\n"
            f"{INTRO_RULES}\n\n"
            f"{INTRO_HIST.format(term=TERM, a=rec['a'] + 1, c0=rec['start_color'])}\n{hist}\n\n{q}\n"
            f"You may show your working. End with a line of the form: FINAL: <color>, where the "
            f"color is one of: {label_list}.")


# ---- working-surface parse: extract the FINAL-tagged color (never bias toward the target) ------
def parse_forced(txt, present):
    """(pick, mode): mode in {final-tag, last-line, None}. `present` = set of color words (lower).

    Reads ONLY the declared final answer:
      1. PRIMARY: the LAST 'FINAL: <color>' / 'FINAL ANSWER: <color>' tag whose color is present.
      2. FALLBACK (no tag): the LAST non-empty line, if it contains EXACTLY ONE present color word.
    Target-blind: keys on position in the reply, not on which color is correct."""
    if not txt:
        return None, None
    low = txt.lower()
    tags = re.findall(r"final(?:\s+answer)?\s*[:\-]+\s*[\"']?([a-z]+)", low)
    tags = [t for t in tags if t in present]
    if tags:
        return tags[-1], "final-tag"
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
