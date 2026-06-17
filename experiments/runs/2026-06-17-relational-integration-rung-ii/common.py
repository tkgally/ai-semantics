#!/usr/bin/env python3
"""common.py — shared machinery for the relational RUNG-(ii) INTEGRATION probe.

Context. claim/relational-order-sensitive-reassignment (supported, internal-contrast-only) shows
both panel models recover a REASSIGNED coined term by its most-recent binding -- order-sensitive,
but at the BOTTOM rung of the relational ladder: a thin latest-binding-wins / OVERWRITE rule
("the latest agreement supersedes earlier ones"). essay/update-is-not-constitution names the next
rung up:

  Rung (ii) -- order-sensitive INTEGRATION / non-overwrite repair. The recovered convention
  reflects the COMBINATION of an earlier and a later agreement, not just the last state. Signature
  (verbatim from the essay): "recovery that is a function of more than the max-stamp binding --
  measurably sensitive to a NON-TERMINAL turn whose content an overwrite rule would throw away."
  Proposed discriminating design (verbatim): "hold the final turn fixed and vary an earlier
  refining turn; an OVERWRITE reader (rung i) is invariant to that change, an INTEGRATING reader
  is not." It is the first rung an overwrite rule fails: it separates "the latest agreement
  supersedes" from "the agreements compose." (Both (i) and (ii) are still single-reader-recoverable
  -- THIN; a positive here does NOT approach constitution. No human comparison is made.)

This probe operationalizes that signature with a two-constraint refinement design:

  A coined term "DAX" is pinned down across TWO stamped rounds about a 2x2 figure grid
  (2 shapes x 2 patterns -> 4 present figures, e.g. {striped triangle, striped circle,
  dotted triangle, dotted circle}):
    - EARLIER round (lower stamp): "we agreed DAX was a {shape}"   -- a SHAPE constraint (the
      non-terminal turn an overwrite rule discards). Matches 2 of the 4 figures.
    - LATEST  round (higher stamp): "we agreed DAX was {pattern}"  -- a PATTERN constraint (the
      terminal turn). Matches 2 of the 4 figures.
  Exactly ONE present figure satisfies BOTH (the {pattern} {shape}) = the integration TARGET.

  INTEG (headline, spontaneous): query = "Which of your figures does DAX refer to?" -- the model
    is NOT told to combine. An OVERWRITE reader keeps only the latest (pattern) constraint -> 2
    candidates -> scores 1/2 = 0.50. An EARLIER-only reader keeps the shape -> 1/2. ANY single
    -attribute reader caps at 0.50 (each constraint is 2-way ambiguous; only the conjunction is
    unique). Beating 0.50 (Wilson-95 lower bound > 0.50) requires using BOTH turns = the earlier,
    non-terminal turn SURVIVED into the interpretation = INTEGRATION (rung ii). A rate ~0.50 with
    the on-demand gate passed is the OVERWRITE-OR-WEAKER null (sharpens the thin verdict:
    overwrite, not integration, even when integration was available -- essay revision trigger (a)).

  DIRECT (on-demand manipulation check): same stimuli, the query EXPLICITLY restates both
    constraints and asks for the single figure. Confirms the model CAN conjoin the two constraints
    when directed, in THIS instrument. Gate: DIRECT acc >= DIRECT_FLOOR. If it fails, INTEG is
    UNINTERPRETABLE (cannot tell spontaneous-non-integration from inability-to-conjoin).

Shortcut-proofing (the load-bearing certification; mirrors the Option-A/B balanced-block proof).
Within each subset every record's answer space is the 4 present figures; the design is a
balanced-block roster: N_BLOCKS distinct 2x2 grids x K=4 records under a Latin square so that
within each block the TARGET cycles through all 4 present figures once AND its physical grid slot
cycles through all 4 slots once. Consequences, asserted at build (assert_balance) and demonstrated
on idealized-reader fixtures BEFORE any model is queried:
  (a) every constant-grid-slot follower scores exactly 1/K = 0.25;
  (b) every fixed figure-IDENTITY preference scores exactly 1/K (target uniform within each block
      -> the top-ranked present figure equals the target in exactly 1 of K records per block; this
      is analytic from the within-block uniformity assert, and is spot-checked over all 16
      constant-figure pickers + a large random sample of full orderings);
  (c) every SINGLE-ATTRIBUTE reader (latest-pattern-only = overwrite; earlier-shape-only) scores
      exactly 0.50 (each constraint matches exactly 2 present figures incl. the target, and the
      target's rank within that pair is balanced; checked for the concrete lower/higher-slot and
      lower/higher-pool-index tie-breaks);
  (d) frequency is flat (each present figure appears once; the 4 figures are distinct).
So NO position / figure-identity / single-attribute / frequency shortcut can clear the 0.50
integration bar; only conjoining the latest AND the earlier turn can. (b)+(a) also pin every
non-integrating reader's INTEG rate at or below 0.50.

anchor: internal-contrast-only (a within-model behavioural contrast over balanced content; no
human-comparison claim -- ratified 2026-06-16 for the relational line). Brennan & Clark report an
order-INSENSITIVE human statistic; none is owed because no human contrast is asserted here.
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

# A-eligible relational panel carried from v4/B/Option-A: claude + gemini (both passed Option B).
MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"]}
SEED0 = 20260617

# ---- frozen design parameters (PREREG) --------------------------------------------------
K = 4                          # present figures per record (a 2x2 shape x pattern sub-grid)
N_BLOCKS_INTEG = 12            # INTEG present-sets -> 48 INTEG records/model
N_BLOCKS_DIRECT = 8            # DIRECT present-sets -> 32 DIRECT records/model
POS_CHANCE = 1.0 / K           # 0.25 (grid-position-follower / figure-preference chance)
OVERWRITE_CEILING = 0.50       # any SINGLE-attribute (latest-only OR earlier-only) reader caps here
DIRECT_FLOOR = 0.80            # on-demand conjunction manipulation gate
INTEG_CI = 1.96                # z for the INTEG integration Wilson interval (LB must exceed 0.50)

# Two-attribute figure space: 4 shapes x 4 patterns = 16 distinct figures. A figure is described
# "a {pattern} {shape}". Shapes and patterns are trivially discriminable (the only hard step is
# COMBINING the two constraints, never telling the figures apart -- as in Option A, near-twins are
# deliberately excluded so an integration failure is never a discrimination failure).
SHAPES = ["triangle", "circle", "square", "diamond"]
PATTERNS = ["striped", "dotted", "checkered", "shaded"]
TERM = "DAX"                    # coined nonce; no lexical prior bears on which figure it "means"


def fig_desc(shape, pattern):
    return f"a {pattern} {shape}"


# Frozen non-contiguous round PAIRS (earlier=low stamp -> SHAPE; latest=high stamp -> PATTERN).
# Non-contiguous + not {1,2}: forces reading the actual stamp value to know which turn is latest.
ROUND_PAIRS = [
    [3, 8],
    [2, 7],
    [4, 9],
    [1, 6],
    [3, 9],
    [2, 8],
]

# ---- elicitation (forced format; cap 512 so truncation is RARE, not impossible) ----------
MAX_TOKENS = 512  # a reply with finish_reason == "length" is NEVER parsed
REASONING = {"google/": {"effort": "minimal"}}  # config/models.md caveat 1
HARD_STOP_USD = 0.50  # pre-registered hard stop on PROJECTED total billed cost

SYS = (
    "You are matching a coined term to one of your figures, recalling a short record of what you "
    "and your partner agreed the term meant over a couple of rounds of a game. Read the figures "
    "and the record, then answer the single question. Reply with EXACTLY ONE figure label (e.g. "
    "{example}) and NOTHING ELSE -- no explanation, no reasoning, no restatement.")

INTRO_GRID = "Your figures:"
INTRO_HIST = (
    "Here is a record of what you and your partner agreed about the coined term \"{term}\" over "
    "two rounds. Each line is stamped with the round it was said in (a higher round number means "
    "it was said more recently). The lines are NOT necessarily listed in round order:")

# SPONT (INTEG): no instruction to combine. DIRECT: explicitly restate both constraints + combine.
QUERY_TEXT = {
    "INTEG": "Question: Which of your figures does the term \"{term}\" refer to?",
    "DIRECT": ("Question: Earlier (round {r_lo}) you agreed \"{term}\" was {shape_phrase}, and "
               "most recently (round {r_hi}) that \"{term}\" was {pattern}. Which single figure "
               "does \"{term}\" refer to?"),
}

STERN = ("\n\nIMPORTANT: your reply must be EXACTLY ONE of these labels ({label_list}) -- a "
         "single label on a single line, with no other text whatsoever.")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def render_grid(display):
    """display: list of {label, shape, pattern} in physical (display) order. Answer space = the
    labels. Label is tied to grid slot, so a 'fixed-label' strategy reduces to a grid-position
    follower (scores 1/K, proven at build)."""
    return "\n".join(f"- {d['label']}: {fig_desc(d['shape'], d['pattern'])}" for d in display)


def render_history(hist):
    """hist: list of {round, kind, value} in PHYSICAL (display) order. kind in {shape, pattern}.
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
        q = QUERY_TEXT["DIRECT"].format(term=TERM, r_lo=rec["r_lo"], r_hi=rec["r_hi"],
                                        shape_phrase=f"a {rec['shape']}", pattern=rec["pattern"])
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
        toks = [w for w in re.findall(r"G[1-4]", lines[-1].upper()) if w in present]
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
