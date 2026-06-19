#!/usr/bin/env python3
"""common.py -- shared machinery for the THREE-MOVE (deeper-composition) extension of the Option-C
ORDER-SENSITIVE COMPOSITION probe (working-surface format).

WHAT THIS IS (the >2-move generality axis: does the working-surface composition WITNESS survive a
DEEPER serial-composition load?).
Every prior Option-C run composed exactly TWO non-commuting moves. The working-surface run
(result/relational-order-composition-c-reasoning-scaffold) found a WITNESS -- opening a working
surface (step-by-step output permitted, FINAL-tag parsed; reasoning-effort knob held constant)
flipped both gemini (DIRECT 0.656->1.000) and gpt (0.250->0.969) from UNINTERPRETABLE to
RESPECTS-ORDER on the two-move task; the alt-pair (A4) and larger-grid (K=6) runs then REPLICATED a
two-move composition CAPACITY over the operation pair and grid-size axes. essay/output-channel-confound
draws the general lesson (the output channel is a capability-masker) and -- grounded by
source/li-2024-cot-serial (chain-of-thought lets a transformer perform inherently SERIAL computation a
forced single token cannot) -- predicts that the load-bearing axis is serial DEPTH. The honest signal
from the K=6 run was that gpt COMP dipped (0.953->0.906->0.861) across the three working-surface
two-move instruments (DIRECT at ceiling throughout; overlapping CIs -> suggestive only). This probe
adds the DEPTH axis directly: THREE stamped non-commuting moves instead of two. It is the
essay/output-channel-confound trigger-(b) CONTRAST CASE -- does a serial-depth gap SURVIVE the wide
working-surface channel (a channel-CONTROLLED bound, a real limit) or does the working surface absorb
the deeper load too (composition capacity extends to depth 3)?

THE SINGLE MANIPULATED VARIABLE vs the working-surface witness run IS THE NUMBER OF MOVES (2 -> 3).
The two-move runs used a dihedral STEP/FLIP (or A4 CYCLE/SWAP) pair whose two orderings let a
print/canonical reader reach exactly 0.50. With THREE moves there are 3! = 6 orderings; a reader that
fails to order ALL THREE by their stamps -- the "half-composer" who pins at most one move's slot from
the stamps and fills the rest from the print/display order -- tops out at exactly 0.50 (it gets the
remaining two-move sub-order right half the time). So the SAME 0.50 ceiling carries over with the SAME
interpretive force, but now beating it requires ordering THREE moves by their stamps, not two: a
genuinely deeper serial-composition test. (Derivation + brute-forced certification in build_trials.)

The three moves are THREE GENERIC non-commuting permutations of the six figures (NOT the dihedral
STEP/FLIP family -- the dihedral group is too structured: its products collapse, so no K<=12 config
isolates the true ordering). They are derangements (no figure maps to itself), pairwise non-commuting,
and chosen (search seed 20260619) so that for each of the 6 stamp-orderings there is EXACTLY ONE start
at which the true-stamp-order endpoint is hit by NO other path among all 16 sub-paths (start, the 3
single moves, the 6 ordered pairs, and the 5 OTHER full orderings). The model is shown only three
figure->figure lookup tables and three stamped move-lines; it never sees positions or any group
structure -- the permutation algebra is the designer's certification tool, not visible to the model.

Reading the outcome (per model; the DIRECT gate is the empirical arbiter of THREE-move composability,
so the difficulty of the deeper load is MEASURED, not assumed):
- DEPTH SURVIVES THE CHANNEL (all three clear DIRECT >= 0.80 and RESPECTS-ORDER at depth 3): the
  working-surface composition capacity extends to three moves -- strengthens essay/output-channel-
  confound's "capacity, not artifact" reading on the DEPTH axis; the trigger-(b) contrast comes back
  negative for a depth-3 bound (no channel-controlled limit found here).
- DEPTH DEFEATS THE CHANNEL (a model that cleared DIRECT at depth 2 fails it at depth 3): a
  serial-depth gap that SURVIVES the wide working-surface channel -- the first channel-CONTROLLED
  composition bound the line has found, exactly the essay/floor-is-not-a-ceiling objection (B) /
  essay/capability-split trigger-(b) contrast case, and consistent with source/li-2024-cot-serial's
  serial-depth prediction. Still UNDISCHARGEABLE (a behavioral negative is never a capacity verdict,
  per essay/undischargeable-negative) and still THIN.
- claude = POSITIVE CONTROL: it should still clear DIRECT (ideally RESPECTS-ORDER); a claude failure
  would mean the deeper instrument broke, not that the others are limited.

Same ratified frame, surfaced for the critic. This is a within-frame DEPTH variation of the already-
ratified Option-C instrument under decisions/resolved/relational-rung-iii-path-dependence and the
ratified internal-contrast-only relational posture -- the stamp-order = composition semantics, the
figure->figure rendering, the working-surface format, the 0.50 print-ceiling, the symmetric verdict
map, and the THIN adjudication are all unchanged; only the move COUNT (and, as a forced consequence,
the generic permutation set replacing the dihedral pair, since the dihedral group cannot be shortcut-
proofed at three moves) varies. Like the K=4 scale, the figure rendering, the worked-example scaffold,
the gpt third-model extension, the working-surface easing, the alt-pair operation pair, and the K=6
grid size -- none of which owed a new decision -- the move count is not a parameter that decision
froze (indeed the original Option-C narrowed FROM a larger instrument). The number-of-moves change is
SURFACED here and the design states no new wiki/decisions/open entry is owed; the independent pre-run
critic gates that judgement and may rule otherwise (if so, open a decision and mark the result
contingent). The binding ADJUDICATION carries over unchanged: an operation-order gap here is THIN (the
stamped move-list and the figure maps are in the record; single-reader-recoverable), reported as
"respects operation order", NEVER promoted to rung (iii); the rich-side rung (iii) is documented
structurally closed for text-only stimuli. anchor: internal-contrast-only; NO human-comparison claim.
NOTE: permitting a working surface does NOT make the COMP arm non-spontaneous -- COMP still does NOT
state the order, so the model must still DECIDE to order the three moves by their stamps; the
scratchpad only lets it externalize whatever ordering it chooses.

Design (THREE generic non-commuting permutations on a SIX-figure track; FIGURE-TO-FIGURE rendering,
WORKING-SURFACE format).
  K=6 distinct figures (shapes). A coined token "DAX" starts on a stated figure. THREE kinds of move
  exist, each a permutation of the six figures, given to the model as an explicit figure->figure table
  derived from the record's `track`:
    FLIP  : position-permutation [1,5,4,2,0,3] (a derangement), rendered figure->figure.
    SLIDE : position-permutation [4,2,5,0,3,1] (a derangement), rendered figure->figure.
    TWIST : position-permutation [3,0,1,5,2,4] (a derangement), rendered figure->figure.
  The three moves are PAIRWISE non-commuting, so the order in which they are applied matters. Each
  record stamps the three moves with three distinct rounds (a higher round = agreed more recently);
  the true composition applies them in STAMP order (lowest round first). The three stamped move-lines
  are shown in a DISPLAY order decoupled from stamp order (each block cycles all 6 display
  permutations once), so "apply the moves in printed order" is NOT "apply them in stamp order".

  COMP (headline, spontaneous): the three stamped move-lines are shown (display order decoupled) and
    the query asks only which figure DAX sits on now -- it does NOT say in which order to apply them.
    A reader who fails to order ALL THREE moves by their stamps scores at most PRINT_CEILING = 0.50
    (proven at build): every fixed canonical order and the print-order reader = 1/6; every half-
    composer (pin one slot by stamp, fill the rest by print) = exactly 0.50; every start / single-move
    / ordered-pair / reversed-order reader = 0; every figure / position picker = 1/K = 1/6. Beating
    0.50 (Wilson-95 lower bound > 0.50) requires ordering all THREE moves BY THEIR STAMPS.
  DIRECT (on-demand manipulation check): same trials; the query states the order explicitly
    ("first ... then ... and then ...") and asks for the figure. Confirms the model CAN compose the
    three moves in THIS instrument. Gate: direct_acc >= DIRECT_FLOOR. If it fails, COMP is
    UNINTERPRETABLE (cannot tell spontaneous order-blindness from inability-to-compose three moves).

Shortcut-proofing is CERTIFIED at build (build_trials.assert_balance and the idealized-reader
fixtures): the target figure is uniform over the 6 figures (constant-figure picker = 1/6); every fixed
canonical-order reader and the print-order reader = 1/6; every half-composer (one slot pinned by stamp,
rest by print) = exactly 0.50; start / single-move (x3) / ordered-pair (x6) / reversed-order readers =
0; frequency flat; the genuine stamp-order composer = 1.0. So the 0.50 bar is clean and only ordering
the three moves by their stamps clears it.
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

# Full three-model panel: claude = POSITIVE CONTROL; gemini + gpt = the deeper-load targets (both
# cleared the two-move DIRECT gate once a working surface was opened -- the question is whether a
# THIRD move defeats on-demand composition even WITH the scratchpad).
MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"], "gpt": PANEL["B"]}
SEED0 = 20260619               # placement seed (stimuli.json differs from every prior run -> new sha)

# ---- frozen design parameters (PREREG) -- THREE MOVES on a K=6 track ---------------------
K = 6                          # figures = answer space
N_BLOCKS_COMP = 12             # 6 configs x 2 reps -> 72 COMP records/model
N_BLOCKS_DIRECT = 6            # 6 configs x 1 rep  -> 36 DIRECT records/model
POS_CHANCE = 1.0 / K           # 1/6 ~= 0.1667 (figure-identity chance)
PRINT_CEILING = 0.50           # half-composer / canonical / print reader cap (proven at build)
DIRECT_FLOOR = 0.80            # on-demand THREE-move composition gate
COMP_CI = 1.96                 # z for the COMP composition Wilson interval (LB must exceed 0.50)

SHAPES = ["triangle", "circle", "square", "star", "diamond", "heart"]  # 6 distinct; FIXED canonical order
TERM = "DAX"                   # coined nonce; no lexical prior bears on where it sits

# ---- the three GENERIC non-commuting permutations (position -> position, 0-indexed) -------
# Found by search (seed 20260619) under three constraints: each a derangement (no fixed point),
# pairwise non-commuting, and admitting -- for each of the 6 stamp-orderings -- exactly one start at
# which the true-stamp-order endpoint is isolated from all 15 other sub-paths (see build_trials and
# PREREG for the full certification). The model NEVER sees these arrays; it sees figure->figure tables.
PERMS = {
    "FLIP":  [1, 5, 4, 2, 0, 3],
    "SLIDE": [4, 2, 5, 0, 3, 1],
    "TWIST": [3, 0, 1, 5, 2, 4],
}
MOVE_NAMES = ["FLIP", "SLIDE", "TWIST"]   # display label set; carries NO inherent order


def op(name, p):
    return PERMS[name][p]


def apply_seq(start, seq):
    """apply a sequence of move names left-to-right (seq[0] first)."""
    p = start
    for nm in seq:
        p = op(nm, p)
    return p


def reverse_seq(seq):
    return tuple(reversed(seq))


# The 6 strict-valid base configs: (start, true-stamp-order tuple). EXACTLY one start per ordering;
# targets fall one each on the 6 track positions (perfectly balanced). Frozen from the search.
CONFIGS = [
    (3, ("FLIP", "SLIDE", "TWIST")),    # target pos 4
    (1, ("FLIP", "TWIST", "SLIDE")),    # target pos 3
    (4, ("SLIDE", "FLIP", "TWIST")),    # target pos 1
    (2, ("SLIDE", "TWIST", "FLIP")),    # target pos 0
    (0, ("TWIST", "FLIP", "SLIDE")),    # target pos 5
    (5, ("TWIST", "SLIDE", "FLIP")),    # target pos 2
]

# Frozen round TRIPLES for the three moves (r1<r2<r3; lo=earliest move, hi=latest). Non-contiguous.
ROUND_TRIPLES = [
    [2, 5, 9],
    [1, 4, 8],
    [3, 6, 10],
    [2, 7, 11],
    [1, 5, 10],
    [3, 8, 12],
]

# The 6 display permutations of the three stamp-slots (index into the stamp-ordered move list). Used
# once each per block so the print-order reader and every half-composer hit their proven ceilings.
import itertools as _it  # noqa: E402

DISPLAY_PERMS = list(_it.permutations(range(3)))   # 6 perms of (0,1,2)


# ---- elicitation (WORKING-SURFACE format; cap raised to 1024 so working rarely truncates) ----
# THE SINGLE MANIPULATED VARIABLE vs the working-surface witness run is the NUMBER OF MOVES (2 -> 3).
# The working-surface elicitation is held byte-identical: the model MAY think step by step and show
# its working, then must end with "FINAL: <figure>". The reasoning-effort knob is held CONSTANT
# (gemini stays at effort minimal, exactly as in the working-surface, alt-pair, and K=6 runs).
MAX_TOKENS = 1024  # a reply with finish_reason == "length" is NEVER parsed (NA/retry)
REASONING = {"google/": {"effort": "minimal"}}  # HELD CONSTANT with the prior working-surface runs
HARD_STOP_USD = 1.80  # pre-registered hard stop on PROJECTED total billed cost (deeper CoT raises out-tok)

SYS = (
    "You are tracking where a coined token sits among a set of figures, recalling a short record of "
    "moves you and your partner agreed it made over a few rounds of a game. Read the move rules and "
    "the record, then work out the answer. You MAY think step by step and show your working if it "
    "helps. When you are done, write your final answer on the LAST line in EXACTLY this form: "
    "FINAL: <figure name> (for example, \"FINAL: {example}\").")

INTRO_FIGS = "There are {k} figures: {fig_list}."
INTRO_RULES = (
    "Three kinds of move can be made. Each kind of move sends the token from whichever figure it is "
    "currently on to another figure, exactly as follows:")
INTRO_HIST = (
    "Here is a record of what you and your partner agreed about where the coined token \"{term}\" "
    "sits. \"{term}\" began on {start_phrase}. Then, over three rounds, it made three moves. Each "
    "move is stamped with the round it was agreed in (a higher round number means it was agreed more "
    "recently). The three moves are NOT necessarily listed in round order:")

QUERY_TEXT = {
    "COMP": "Question: Which figure does the token \"{term}\" sit on now?",
    "DIRECT": ("Question: Starting from {start_phrase}, \"{term}\" first (round {r1}) made move "
               "{op1}, then (round {r2}) made move {op2}, and then (round {r3}) made move {op3}. "
               "Which figure does \"{term}\" sit on now?"),
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


def move_map(track, name):
    """The figure->figure table for move `name`, derived from this record's `track` (track[p] = the
    figure at position p). map[fig] = the figure at the position `name` sends fig's position to.
    Returned keyed by figure, rendered in FIXED canonical SHAPES order so no positional info leaks."""
    pos = {fig: p for p, fig in enumerate(track)}
    return {fig: track[op(name, pos[fig])] for fig in track}


def render_rules(track):
    """The three move tables (FLIP, SLIDE, TWIST), each listing all K figure->figure mappings in
    canonical SHAPES order. No positions appear."""
    out = []
    for name in MOVE_NAMES:
        mp = move_map(track, name)
        parts = ", ".join(f"{shape_phrase(s)} becomes {shape_phrase(mp[s])}" for s in SHAPES)
        out.append(f"- Move {name}: {parts}.")
    return "\n".join(out)


def render_history(rec):
    """the three stamped move-lines, in the record's frozen DISPLAY order (decoupled from stamp
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
        rounds = rec["rounds"]
        moves = rec["stamp_moves"]
        q = QUERY_TEXT["DIRECT"].format(
            term=TERM, start_phrase=start_phrase,
            r1=rounds[0], r2=rounds[1], r3=rounds[2],
            op1=moves[0], op2=moves[1], op3=moves[2])
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

    Reads ONLY the declared final answer:
      1. PRIMARY: the LAST 'FINAL: <figure>' / 'FINAL ANSWER: <figure>' tag whose figure is present.
      2. FALLBACK (no tag): the LAST non-empty line, if it contains EXACTLY ONE present figure word.
    Target-blind: keys on position in the reply, not on which figure is correct. (Byte-identical to
    the working-surface / K=6 runs.)"""
    if not txt:
        return None, None
    low = txt.lower()
    tags = re.findall(r"final(?:\s+answer)?\s*[:\-]+\s*[\"']?(?:an?\s+)?([a-z]+)", low)
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
