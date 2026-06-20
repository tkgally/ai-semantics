#!/usr/bin/env python3
"""common.py -- shared machinery for the CROSS-FAMILY (heterogeneous-operation) extension of the
Option-C ORDER-SENSITIVE COMPOSITION probe (working-surface format), POSITION-ANCHORED readout.

WHAT THIS IS (the cross-family generality axis: does the working-surface composition WITNESS extend
to composing two operations of DIFFERENT KINDS?).
Every prior Option-C run composed operations of the SAME family: position permutations rendered as
opaque figure->figure tables (STEP/FLIP=D4, CYCLE/SWAP=A4, generic S6). The working-surface run found
a WITNESS and the alt-pair / K=6 / three-move runs replicated a composition CAPACITY across the
operation pair, grid size, and depth axes -- all panel-concordant RESPECTS-ORDER. But to the model
those were all the same task: compose two opaque permutations of one ground set.
claim/relational-order-sensitive-reassignment scope limit 2 names the still-untested generality axis
verbatim -- "generality (image referents, cross-family dyads) is untested".

THE SINGLE NEW HYPOTHESIS vs every prior Option-C run: the two stamped operations are TRANSPARENTLY
HETEROGENEOUS -- one moves tokens in space, the other changes a token's attribute -- and they do NOT
commute on the queried readout. The model must bind a SPATIAL update and an ATTRIBUTE update in stamp
order. This is the relational axis's core (composing updates of different kinds).

THE TWO HETEROGENEOUS OPERATIONS (a row of K spots, each holding a token of some COLOR; one spot is
nicknamed the "DAX spot" and is the readout).
  SWAP    (a SPATIAL move):    the tokens on two named spots exchange places (color travels with the
                               token). Acts on POSITION.
  RECOLOR (an ATTRIBUTE move): the token on one named spot is repainted a stated color. Acts on COLOR.
The DAX spot `s` is one of the two SWAP spots, and the RECOLOR targets one of the two SWAP spots, so
both operations are LIVE at the readout. They NON-COMMUTE on the color at spot `s`: SWAP changes WHICH
token sits at `s`, RECOLOR changes a token's color, and the order decides what color ends up at `s`.

WHY POSITION-ANCHORED (the fix an independent reviewer found for the object-anchored design).
An earlier object-anchored readout ("what color is the moved token DAX?") admitted a stamp-using
single-op shortcut: anchoring the readout to the MOVED token makes the spatial op a follow-the-token
relabeling under which the attribute op is inert in most cells, so "apply only the earlier op" scored
0.75 and FALSELY cleared the bar (independent pre-run critic NO-GO, 2026-06-20). Anchoring the readout
to a FIXED SPOT `s` removes that: at a fixed spot BOTH ops are live in every order-discriminating cell
(SWAP fixes which token occupies `s`; RECOLOR fixes a color), so every single-op / stamp-using-partial
reader caps at 0.50. The fix changes ONLY the query (object-anchored -> position-anchored); the two
heterogeneous operations, the 6-color answer space, and the verdict map are unchanged.

THE FOUR GEOMETRY CELLS = readout-type {SAME = the DAX spot IS the recolor target; DIFF = the DAX spot
is the non-recolored swap spot} x stamp_first {SWAP, RECOLOR}. Simulating the color at spot `s`
through the two ops in stamp order (with the OTHER swap spot's initial color C_oth and the recolor
color Cr; the DAX spot's own initial color is always overwritten, so it is never the answer) gives the
answer in {C_oth, Cr}, fixed by NEITHER the stamp order alone NOR the geometry alone -- only by both.

WHY THE 0.50 CEILING (re-proven over the actual records in build_trials.assert_balance, now including
the stamp-using PARTIAL readers the reviewer flagged): with the four cells equally frequent the answer
is C_oth half the time and Cr half the time, so EVERY non-composing reader tops out at exactly 0.50 --
report-C_oth, report-Cr, swap-only, recolor-only, apply-only-the-stamp-EARLIER-op, apply-only-the-
stamp-LATER-op, apply-only-the-print-first/second-op, apply-both-in-a-FIXED-order (either way),
apply-both-in-reverse-stamp-order, apply-both-in-PRINT-order, and every fixed-spot initial/fixed-order
final color or const color reader. ONLY a reader that applies the two operations in the per-trial STAMP
order clears 0.50 (= 1.0). All brute-forced below, not asserted by hand.

Reading the outcome (per model; the DIRECT gate is the empirical arbiter of cross-family
composability, so the difficulty is MEASURED, not assumed):
- RESPECTS-ORDER (clears DIRECT >= 0.80 and COMP Wilson-LB > 0.50): the working-surface composition
  capacity extends to a HETEROGENEOUS operation pair -- corroborates the capacity reading on the
  cross-family axis claim scope limit 2 named.
- UNINTERPRETABLE (DIRECT < 0.80): the model cannot compose a spatial + an attribute update on demand
  in this instrument even WITH a working surface -- a cross-family-specific gap; the FIRST non-witness
  since the working surface was opened, to be reported as a witness-search reopening on a new axis,
  never as "M cannot" (essay/undischargeable-negative). Still THIN.
- claude = POSITIVE CONTROL.

Same ratified frame, surfaced for the critic. This is a within-frame OPERATION-KIND variation of the
already-ratified Option-C instrument under decisions/resolved/relational-rung-iii-path-dependence and
the ratified internal-contrast-only relational posture: the stamp-order = composition semantics, the
working-surface format, the 0.50 print-ceiling, the symmetric verdict map, and the THIN adjudication
are all unchanged; only the KIND of the two operations (heterogeneous spatial+attribute) varies, and
as a forced consequence the state carries a color attribute and the answer is a color. The decision
adopted "non-commuting operation semantics" AGNOSTIC to which operations realize them and did not
freeze the operation kind (it explicitly contemplated "rotate/move" edits); like the alt-pair D4->A4,
the grid size, and the move count -- none of which owed a new decision -- the operation-kind change is
SURFACED here and the design states no new wiki/decisions/open entry is owed; the independent pre-run
critic gates that judgement. The binding ADJUDICATION carries over unchanged: an operation-order gap
here is THIN (the stamped operation list, the spots, and the colors are in the record;
single-reader-recoverable), reported as "respects operation order", NEVER promoted to rung (iii); the
rich-side rung (iii) is documented structurally closed for text-only stimuli. anchor:
internal-contrast-only; NO human-comparison claim. NOTE: permitting a working surface does NOT make
the COMP arm non-spontaneous -- COMP still does NOT state the order.
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

MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"], "gpt": PANEL["B"]}
SEED0 = 20260620

# ---- frozen design parameters (PREREG) -- two HETEROGENEOUS moves on a K=4 row -----------------
K = 4                          # number of spots in the row
N_BLOCKS_COMP = 12             # 4 cells x 3 geoms -> 12 blocks x 6 colors -> 72 COMP records/model
N_BLOCKS_DIRECT = 12           # 4 cells x 3 geoms -> 12 blocks x 3 colors -> 36 DIRECT records/model
PRINT_CEILING = 0.50           # every non-composing reader's cap (proven at build)
DIRECT_FLOOR = 0.80            # on-demand cross-family composition gate
COMP_CI = 1.96                 # z for the COMP composition Wilson interval (LB must exceed 0.50)

COLORS = ["red", "blue", "green", "yellow", "purple", "orange"]
NUM_COLORS = len(COLORS)
POS_CHANCE = 1.0 / NUM_COLORS   # 1/6 ~= 0.1667 (color-identity chance)
TERM = "DAX"                    # coined nonce: nickname for a FIXED spot (the readout)

MOVE_NAMES = ["SWAP", "RECOLOR"]   # the two heterogeneous operation kinds; carry NO inherent order

# The 4 geometry CELLS: (readout_type, stamp_first). readout_type in {"SAME","DIFF"}: SAME = the DAX
# spot s IS the recolor target m; DIFF = s is the OTHER (non-recolored) swap spot. stamp_first in
# {SWAP,RECOLOR} = which op has the lower round stamp. Answer = Cr in {(SAME,SWAP),(DIFF,RECOLOR)};
# C_oth (the other swap spot's initial color) in {(SAME,RECOLOR),(DIFF,SWAP)}.
CELLS = [("SAME", "SWAP"), ("SAME", "RECOLOR"), ("DIFF", "SWAP"), ("DIFF", "RECOLOR")]

GEOMS = [(0, 1), (1, 2), (2, 3), (3, 0)]   # (a,b) swap pairs; cycled across the 4 cells x 3 geoms

ROUND_PAIRS = [[2, 6], [1, 5], [3, 8], [2, 7], [4, 9], [1, 6],
               [3, 7], [2, 8], [1, 7], [4, 8], [3, 9], [2, 9]]

DISPLAY_PERMS = [(0, 1), (1, 0)]


# ---- the heterogeneous operators, as a transition on the full K-spot coloring --------------
def full_state(rec, order):
    """The color on each of the K spots after applying the two ops in `order`. SWAP exchanges the
    colors at spots a,b (the tokens, with their colors, trade places); RECOLOR repaints spot m."""
    colors = list(rec["init_colors"])
    a, b, m = rec["a"], rec["b"], rec["m"]
    for nm in order:
        if nm == "SWAP":
            colors[a], colors[b] = colors[b], colors[a]
        else:  # RECOLOR
            colors[m] = rec["recolor_color"]
    return colors


def color_at(rec, order, spot):
    return full_state(rec, order)[spot]


def answer_color(rec):
    """The color on the DAX spot s after applying the two ops in STAMP order (the readout)."""
    return color_at(rec, tuple(rec["stamp_order"]), rec["s"])


# ---- elicitation (WORKING-SURFACE format; cap 1024) ----
MAX_TOKENS = 1024
REASONING = {"google/": {"effort": "minimal"}}  # HELD CONSTANT with the prior working-surface runs
HARD_STOP_USD = 1.50

SYS = (
    "You are tracking the color on a particular spot, recalling a short record of moves you and your "
    "partner agreed were made over a few rounds of a game. Read the move rules and the record, then "
    "work out the answer. You MAY think step by step and show your working if it helps. When you are "
    "done, write your final answer on the LAST line in EXACTLY this form: FINAL: <color> (for "
    "example, \"FINAL: {example}\").")

INTRO_SCENE = (
    "There are {k} spots in a row, numbered spot 1 to spot {k}. A token sits on each spot. Right now "
    "the tokens are colored as follows: {coloring}. One of the spots -- spot {s} -- is the one you "
    "and your partner nicknamed the \"{term}\" spot.")
INTRO_RULES = (
    "Two kinds of move can be made to the tokens. They work as follows:\n"
    "- A SWAP move names two spots; the tokens on those two spots exchange places (each token keeps "
    "its own color as it moves).\n"
    "- A RECOLOR move names one spot and a color; the token on that spot is repainted that color "
    "(it does not move).")
INTRO_HIST = (
    "Here is a record of what you and your partner agreed happened over two rounds. Each move is "
    "stamped with the round it was agreed in (a higher round number means it was agreed more "
    "recently). The two moves are NOT necessarily listed in round order:")

QUERY_TEXT = {
    "COMP": "Question: What color is the token on the \"{term}\" spot (spot {s}) now?",
    "DIRECT": ("Question: First (round {r1}) there was {desc1}, and then (round {r2}) there was "
               "{desc2}. What color is the token on the \"{term}\" spot (spot {s}) now?"),
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
    return f"a RECOLOR of the token on spot {rec['m'] + 1} to {rec['recolor_color']}"


def op_desc(rec, name):
    return _swap_desc(rec) if name == "SWAP" else _recolor_desc(rec)


def render_coloring(rec):
    return ", ".join(f"spot {p + 1} holds a {rec['init_colors'][p]} token" for p in range(K))


def render_history(rec):
    return "\n".join(f'- Round {ln["round"]}: there was {ln["desc"]}.' for ln in rec["hist_display"])


def build_user(rec):
    coloring = render_coloring(rec)
    label_list = ", ".join(COLORS)
    if rec["query"] == "DIRECT":
        rounds = rec["rounds"]
        first, second = rec["stamp_order"]
        q = QUERY_TEXT["DIRECT"].format(
            term=TERM, s=rec["s"] + 1, r1=rounds[0], r2=rounds[1],
            desc1=op_desc(rec, first), desc2=op_desc(rec, second))
    else:
        q = QUERY_TEXT["COMP"].format(term=TERM, s=rec["s"] + 1)
    hist = render_history(rec)
    return (f"{INTRO_SCENE.format(k=K, coloring=coloring, term=TERM, s=rec['s'] + 1)}\n\n"
            f"{INTRO_RULES}\n\n"
            f"{INTRO_HIST.format()}\n{hist}\n\n{q}\n"
            f"You may show your working. End with a line of the form: FINAL: <color>, where the "
            f"color is one of: {label_list}.")


# ---- working-surface parse: extract the FINAL-tagged color (never bias toward the target) ------
def parse_forced(txt, present):
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
