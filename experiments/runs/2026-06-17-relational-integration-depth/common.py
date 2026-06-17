#!/usr/bin/env python3
"""common.py -- shared machinery for the relational INTEGRATION-UNDER-LOAD probe (burial depth 2).

Context. result/relational-integration-rung-ii (proposed, internal-contrast-only) showed both
panel models INTEGRATE a compatible earlier turn at ceiling: across TWO stamped rounds (earlier =
shape, latest = pattern) over a 2x2 grid, both models recover the unique both-match figure (INTEG
target 1.000), beating the 0.50 single-attribute ceiling -- the earlier, non-terminal turn
SURVIVES; agreements COMPOSE. That result is SATURATED at ceiling, and its own honesty box names
the untested weak point verbatim:

  "it does not rule out overwrite behaviour under harder load (more turns, larger grids, or
   refinements that partially conflict rather than cleanly compose)"  -- and -- "because DIRECT
   and INTEG are both at ceiling, the conjunction is easy enough that a ceiling on the spontaneous
   (no-instruction) arm is *weaker* evidence of genuinely spontaneous composition than a mid-range
   result would be."

This probe attacks the FIRST horn -- "more turns" -- the most tractable harder-load axis, by
testing whether integration survives GREATER BURIAL DEPTH. The structure is the rung-(ii) design
generalized from 2 attributes / 2 rounds to 3 attributes / 3 rounds:

  A coined term "DAX" is pinned down across THREE stamped rounds about a 2x2x2 figure grid
  (2 shapes x 2 patterns x 2 colors -> 8 present figures, e.g. {red striped triangle, ...}):
    - EARLIEST round (lowest stamp)  : "DAX was a {shape}"   -- the SHAPE constraint, buried under
      TWO later turns (the deep survival test). Matches 4 of 8 figures.
    - MIDDLE   round (middle stamp)  : "DAX was {pattern}"    -- the PATTERN constraint. Matches 4.
    - LATEST   round (highest stamp) : "DAX was {color}"      -- the terminal turn. Matches 4.
  Exactly ONE present figure satisfies ALL THREE = the integration TARGET (the {color} {pattern}
  {shape}). The three constraints are mutually COMPATIBLE (a figure can be all three).

Why this is "harder load" and not retuning. The rung-(ii) design (depth 1) put exactly one turn
between the buried turn and the query; ANY reader dropping a turn fell to the 0.50 floor, so the
only contrast was integrate-vs-not. Here the EARLIEST turn is separated from the query by TWO
intervening compatible turns, and a NATURAL recency-bounded strategy is now behaviourally
available and DISTINCT from the integration target:

  RECENT-TWO reader (keep the latest two turns = pattern + color, DROP the buried earliest shape):
  narrows to {target, twin_shape} (the two figures sharing the target's pattern AND color, differing
  only in shape) -> 2 candidates -> tie-break -> 0.50. To EXCEED 0.50 the model must retain ALL
  THREE turns, including the earliest (shape) buried under two later ones. So a clean recency-decay
  / "shed the oldest" behaviour scores EXACTLY 0.50 and is a live alternative the rung-(ii) design
  could not even express.

  INTEG (headline, spontaneous): query = "Which of your figures does DAX refer to?" -- the model is
    NOT told to combine. Reader ceilings on the balanced roster (K=8 present figures; proven at
    build, demonstrated on idealized-reader fixtures BEFORE any model is queried):
      grid-position follower / figure-identity preference : exactly 1/K = 0.125
      any SINGLE-attribute reader (color-only = overwrite; pattern-only; shape-only/earliest-only):
        4 candidates -> <= SINGLE_ATTR_CEILING = 0.25
      any TWO-attribute reader (drop ONE turn: recent-two; shape+color; shape+pattern):
        2 candidates -> <= TWO_ATTR_CEILING = 0.50
      full integrator (all three turns) : 1.000
    Beating 0.50 (target-rate Wilson-95 lower bound > TWO_ATTR_CEILING) can ONLY come from
    conjoining all three turns -> the buried earliest turn SURVIVED under depth-2 load =
    INTEGRATION-UNDER-LOAD. A rate ~0.50 with the on-demand gate passed is the
    PARTIAL-OR-OVERWRITE null: a turn is shed under load (the earliest most plausibly), which would
    BOUND claim/relational-order-sensitive-reassignment to depth-1 integration.

  DIRECT (on-demand manipulation check): same stimuli; the query EXPLICITLY restates all three
    constraints and asks for the single figure. Confirms the model CAN conjoin three compatible
    constraints in THIS instrument. Gate: DIRECT acc >= DIRECT_FLOOR. If it fails, INTEG is
    UNINTERPRETABLE (cannot tell spontaneous-non-integration from inability-to-conjoin-three).

Symmetric verdict map (anti-cheat): a ceiling STRENGTHENS the rung-(ii) reading (integration robust
to burial depth 2 / "more turns"); a drop to ~0.50 BOUNDS it (overwrite/partial reappears under
load). Neither outcome is the one the design "wants"; the bar (beat 0.50) is pre-registered and the
roster is shortcut-proof by construction.

anchor: internal-contrast-only (a within-model behavioural contrast over balanced content; no
human-comparison claim -- the ratified relational posture). This is a fresh frozen design under the
ALREADY-RATIFIED internal-contrast-only relational posture; no new decision is owed (a depth
generalization of an established within-model contrast, with a symmetric verdict map).
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

# A-eligible relational panel carried from rung-(ii)/Option-A: claude + gemini (both passed Option B).
MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"]}
SEED0 = 20260617

# ---- frozen design parameters (PREREG) --------------------------------------------------
K = 8                          # present figures per record (a 2x2x2 shape x pattern x color block)
N_BLOCKS_INTEG = 6             # INTEG present-sets -> 48 INTEG records/model
N_BLOCKS_DIRECT = 4            # DIRECT present-sets -> 32 DIRECT records/model
POS_CHANCE = 1.0 / K           # 0.125 (grid-position-follower / figure-preference chance)
SINGLE_ATTR_CEILING = 0.25     # any ONE-attribute reader (4 candidates) caps here
TWO_ATTR_CEILING = 0.50        # any TWO-attribute reader (drop one turn; 2 candidates) caps here
DIRECT_FLOOR = 0.80            # on-demand conjunction (of three) manipulation gate
INTEG_CI = 1.96                # z for the INTEG integration Wilson interval (LB must exceed 0.50)

# Three-attribute figure space: 4 shapes x 4 patterns x 4 colors = 64 distinct figures. A figure is
# described "a {color} {pattern} {shape}". All attribute values are trivially discriminable (the
# only hard step is COMBINING the three constraints, never telling the figures apart -- near-twins
# are NOT excluded structurally [twins-by-one-attribute are the diagnostic distractors], but no two
# present figures are identical and every attribute value is a plain word).
SHAPES = ["triangle", "circle", "square", "diamond"]
PATTERNS = ["striped", "dotted", "checkered", "shaded"]
COLORS = ["red", "blue", "green", "amber"]
TERM = "DAX"                    # coined nonce; no lexical prior bears on which figure it "means"

# round->attribute binding (FROZEN): earliest stamp = shape (buried), middle = pattern, latest =
# color (terminal). This is one operationalization (shape-always-earliest); generality over which
# attribute is buried is untested and noted in the design scope.
ATTR_ORDER = ["shape", "pattern", "color"]   # earliest -> latest


def fig_desc(color, pattern, shape):
    return f"a {color} {pattern} {shape}"


# Frozen non-contiguous round TRIPLES (sorted -> earliest=shape, middle=pattern, latest=color).
# Non-contiguous + not {1,2,3}: forces reading the actual stamp values to know the recency order.
ROUND_TRIPLES = [
    [2, 5, 9],
    [3, 6, 8],
    [1, 4, 7],
    [2, 6, 9],
    [3, 5, 8],
    [1, 5, 9],
]

# ---- elicitation (forced format; cap 512 so truncation is RARE, not impossible) ----------
MAX_TOKENS = 512  # a reply with finish_reason == "length" is NEVER parsed
REASONING = {"google/": {"effort": "minimal"}}  # config/models.md caveat 1
HARD_STOP_USD = 0.50  # pre-registered hard stop on PROJECTED total billed cost

SYS = (
    "You are matching a coined term to one of your figures, recalling a short record of what you "
    "and your partner agreed the term meant over a few rounds of a game. Read the figures and the "
    "record, then answer the single question. Reply with EXACTLY ONE figure label (e.g. {example}) "
    "and NOTHING ELSE -- no explanation, no reasoning, no restatement.")

INTRO_GRID = "Your figures:"
INTRO_HIST = (
    "Here is a record of what you and your partner agreed about the coined term \"{term}\" over "
    "three rounds. Each line is stamped with the round it was said in (a higher round number means "
    "it was said more recently). The lines are NOT necessarily listed in round order:")

# INTEG: no instruction to combine. DIRECT: explicitly restate all three constraints + combine.
QUERY_TEXT = {
    "INTEG": "Question: Which of your figures does the term \"{term}\" refer to?",
    "DIRECT": ("Question: Across the rounds you agreed \"{term}\" was a {shape} (round {r_shape}), "
               "was {pattern} (round {r_pattern}), and was {color} (round {r_color}). Which single "
               "figure does \"{term}\" refer to?"),
}

STERN = ("\n\nIMPORTANT: your reply must be EXACTLY ONE of these labels ({label_list}) -- a "
         "single label on a single line, with no other text whatsoever.")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def render_grid(display):
    """display: list of {label, color, pattern, shape} in physical (display) order. Answer space =
    the labels. Label is tied to grid slot, so a 'fixed-label' strategy reduces to a grid-position
    follower (scores 1/K, proven at build)."""
    return "\n".join(
        f"- {d['label']}: {fig_desc(d['color'], d['pattern'], d['shape'])}" for d in display)


def render_history(hist):
    """hist: list of {round, kind, value} in PHYSICAL (display) order. kind in {shape,pattern,color}.
    Each line states ONE attribute the term was agreed to have in that round."""
    out = []
    for ln in hist:
        if ln["kind"] == "shape":
            out.append(f'- Round {ln["round"]}: we agreed "{TERM}" was a {ln["value"]}.')
        else:
            out.append(f'- Round {ln["round"]}: we agreed "{TERM}" was {ln["value"]}.')
    return "\n".join(out)


def build_user(rec):
    grid = render_grid(rec["display"])
    hist = render_history(rec["hist_display"])
    label_list = ", ".join(d["label"] for d in rec["display"])
    if rec["query"] == "DIRECT":
        q = QUERY_TEXT["DIRECT"].format(
            term=TERM, shape=rec["shape"], pattern=rec["pattern"], color=rec["color"],
            r_shape=rec["r_shape"], r_pattern=rec["r_pattern"], r_color=rec["r_color"])
    else:
        q = QUERY_TEXT["INTEG"].format(term=TERM)
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
    lines = [ln for ln in txt.splitlines() if ln.strip()]
    if lines:
        toks = [w for w in re.findall(r"G[1-8]", lines[-1].upper()) if w in present]
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
