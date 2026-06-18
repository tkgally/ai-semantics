#!/usr/bin/env python3
"""common.py -- shared machinery for the EASIER (K=4) WITNESS-SEEKING re-run of the Option-C
ORDER-SENSITIVE COMPOSITION probe (non-commuting operation semantics).

WHAT THIS IS (witness-seeking, not a re-run of the hard instrument). The Option-C probe
(experiments/runs/2026-06-18-relational-order-composition-c, K=6 STEP/FLIP track) found a SPLIT:
claude RESPECTS-ORDER at ceiling, but BOTH gemini-3.5-flash and gpt-5.4-mini FAILED the DIRECT
on-demand gate (gemini 0.583, gpt 0.194 < 0.80) -- they could not compose the two non-commuting
moves even when told the order, so their COMP was UNINTERPRETABLE. essay/undischargeable-negative
makes the methodological point: re-running the SAME hard instrument cannot move an UNINTERPRETABLE
verdict (it is another instance of the same universal-over-elicitations). Only a WITNESS-SEEKING
probe -- an EASIER elicitation of the SAME capability -- can flip a negative to a positive. This is
that probe (essay/capability-split trigger (b), named in NEXT.md as the single most informative
cheap test).

The single manipulated variable is INSTRUMENT LOAD: the track is shrunk from K=6 to K=4 -- the SAME
non-commuting STEP/FLIP operation pair (the dihedral generators of a ring), only smaller. The mirror
is a clean 2-swap derangement (1<->4, 2<->3; no fixed point), the state space is halved, and there
are fewer distractor figures. NOTHING ELSE changes: same prompt skeleton, same two arms (COMP /
DIRECT), same shortcut-proofing, same symmetric verdict map. So a WITNESS (gemini/gpt clear DIRECT
>= 0.80 at K=4 where they failed at K=6) cleanly attributes the K=6 failure to instrument load and
re-opens the COMP order-sensitivity question for them; a NON-WITNESS (DIRECT still fails at K=4)
shows the composition inability is robust to halving the instrument and SHARPENS the claude-only
reading. The DIRECT gate is the empirical arbiter of "easier" -- the easiness claim is not assumed,
it is measured. claude is re-run as a POSITIVE CONTROL: if the K=4 instrument is a valid
non-commuting composition, claude should still clear DIRECT and (ideally) RESPECTS-ORDER; a claude
failure would mean the instrument is broken, not that the others are limited.

Same ratified frame. This is a SCALE PARAMETER (K) of the already-ratified Option-C instrument under
decisions/resolved/relational-rung-iii-path-dependence and the already-ratified internal-contrast-
only relational posture -- exactly as the gpt third-model extension was the same instrument with a
different panel. No new wiki/decisions/open entry is owed; the in-session independent pre-run critic
gates instrument validity, as for every relational probe. The binding ADJUDICATION carries over
unchanged: an operation-order gap here is THIN (the stamped move-list is in the record;
single-reader-recoverable), reported as "respects operation order," NEVER promoted to rung (iii);
the rich-side rung (iii) is documented structurally closed for text-only stimuli. anchor:
internal-contrast-only; NO human-comparison claim.

Context. The relational ladder (essay/update-is-not-constitution) has firm, replicated rungs:
  rung (i)  -- order-sensitive OVERWRITE (latest-binding-wins): claim/relational-order-sensitive-
               reassignment (supported).
  rung (ii) -- non-overwrite INTEGRATION (a compatible earlier turn SURVIVES): result/relational-
               integration-rung-ii (INTEGRATION) + result/relational-integration-depth (robust to
               burial depth 2).
Both are on the THIN / single-reader-recoverable side of the essay's thin/rich criterion. The
rung-(ii) probe's own scope note 3 flags the gap this probe fills (verbatim): "Tests non-overwrite,
not order-sensitive composition ... it does NOT test whether the composition is itself order-
sensitive (a commutative conjunction would pass equally)." claim scope-limit 2 calls
order-sensitive composition "a further, untested refinement." This probe tests exactly that.

It is the OPTION-C design ratified in decisions/resolved/relational-rung-iii-path-dependence:
turns are NON-COMMUTING OPERATIONS on a referent's position; two orders of the same operation-set
reach genuinely different end states, so a shuffle is not a no-op. The ratification fixed the
yardstick under a binding PRE-RUN ADJUDICATION GATE, biased AGAINST the rich reading: an operation-
order gap whose end state the record still fully encodes (a single reader applies the stamped
operation list in order and reads off the answer) is THIN -- "respects operation order" -- and is
NOT promoted to rung (iii) / constitution. The rich-side rung-(iii) program is documented as
STRUCTURALLY CLOSED for text-only stimuli (a transcript IS a final content+stamps record). So both
verdicts here are thin; the rich-side closure is the parallel headline. anchor: internal-contrast-
only (a within-model contrast over balanced/order-permuted content; NO human-comparison claim --
ratified for the relational line 2026-06-16; re-ratified internal-contrast-only for this design).

Design (non-commuting operation semantics; EASIER K=4 instance).
  K=4 distinct figures (shapes) lie along a TRACK in a stated order (position 1..4). A coined token
  "DAX" starts on a stated figure. Across stamped rounds it undergoes TWO relative moves drawn from
  a non-commuting pair (the dihedral generators of a 4-ring):
    STEP : DAX moves one position toward the back of the track (wrapping back->front). p -> (p+1)%4.
    FLIP : DAX moves to its mirror position (1<->4, 2<->3).                              p -> 3-p.
  STEP and FLIP do NOT commute, so applying them in stamp order (lower round first) lands DAX on a
  DIFFERENT figure than applying them in the reversed order. The two op-lines are displayed in
  round order in HALF the records and reversed in the other half (display order decoupled from
  stamp order), so "read the operations in the order they're printed" is NOT the same as "read them
  in stamp order".

  COMP (headline, spontaneous): the two stamped op-lines are shown (possibly out of round order) and
    the query asks only which figure DAX sits on now -- it does NOT say which move came first. A
    reader who applies the moves in PRINT order, or in a FIXED canonical order, gets the right
    figure only when print/canonical order happens to equal stamp order = exactly HALF the records
    = 0.50 (proven at build). Beating 0.50 (Wilson-95 lower bound > 0.50) requires ordering the two
    moves BY THEIR STAMPS -- i.e. respecting the operation order = order-sensitive COMPOSITION.
  DIRECT (on-demand manipulation check): same stimuli; the query states the order explicitly
    ("first ... then ...") and asks for the figure. Confirms the model CAN compose the two moves in
    THIS instrument. Gate: direct_acc >= DIRECT_FLOOR. If it fails, COMP is UNINTERPRETABLE (cannot
    tell spontaneous order-blindness from inability-to-compose).

Shortcut-proofing (certified at build + on idealized-reader fixtures, BEFORE any model is queried).
The answer space is the 4 track figures. Records are built so that, over each subset:
  (a) the TARGET figure (stamp-order end) is UNIFORM over the 4 figures => every fixed figure-
      identity picker scores exactly 1/K;
  (b) the TARGET's TRACK POSITION is balanced => every fixed track-position picker scores <= 1/K
      (and never the 0.50 bar);
  (c) print-order (and either fixed canonical order, STEP-then-FLIP or FLIP-then-STEP) is matched to
      stamp order in EXACTLY half the records => every print-order / canonical-order reader scores
      EXACTLY 0.50;
  (d) the start figure and each single-move reader (STEP-only, FLIP-only from the start) and the
      reversed-order ("swapped") reader are EXCLUDED from being the target by construction =>
      each scores 0 on the target;
  (e) frequency flat (4 distinct figures once each).
So no figure-identity / track-position / print-order / canonical-order / start / single-move /
reversed-order shortcut can clear the 0.50 bar; only ordering the two moves by their stamps can.
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

# Full three-model panel: the witness targets are gemini + gpt (both FAILED the K=6 DIRECT gate);
# claude is the POSITIVE CONTROL (it RESPECTS-ORDER at K=6, so it should still clear DIRECT at K=4
# if the easier instrument is a valid non-commuting composition).
MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"], "gpt": PANEL["B"]}
SEED0 = 20260619               # distinct from the K=6 run's SEED0=20260618

# ---- frozen design parameters (PREREG) --------------------------------------------------
K = 4                          # figures on the track = answer space (EASIER: halved from K=6)
N_BLOCKS_COMP = 16             # COMP blocks x K records -> 64 COMP records/model
N_BLOCKS_DIRECT = 8            # DIRECT blocks x K records -> 32 DIRECT records/model
POS_CHANCE = 1.0 / K           # 1/4 = 0.25 (figure-identity / track-position chance)
PRINT_CEILING = 0.50           # print-order / canonical-order reader caps here (proven at build)
DIRECT_FLOOR = 0.80            # on-demand composition manipulation gate
COMP_CI = 1.96                 # z for the COMP composition Wilson interval (LB must exceed 0.50)

SHAPES = ["triangle", "circle", "square", "star"]  # 4 distinct, discriminable
TERM = "DAX"                   # coined nonce; no lexical prior bears on where it sits

# Frozen non-contiguous round PAIRS for the two moves (lo=earlier move, hi=later move).
# Non-contiguous + not {1,2}: forces reading the actual stamp value to know which move is later.
ROUND_PAIRS = [
    [3, 8],
    [2, 7],
    [4, 9],
    [1, 6],
    [3, 9],
    [2, 8],
]


# ---- the non-commuting operations (0-indexed track positions 0..K-1) --------------------
def op_step(p):
    return (p + 1) % K


def op_flip(p):
    return (K - 1) - p


OPS = {"STEP": op_step, "FLIP": op_flip}
# A move-pair ORDER: "SF" = STEP at the lower stamp then FLIP; "FS" = FLIP then STEP.
ORDER_OPS = {"SF": ("STEP", "FLIP"), "FS": ("FLIP", "STEP")}


def apply_order(start, order):
    """final position applying op_lo (lower stamp) then op_hi (higher stamp)."""
    lo, hi = ORDER_OPS[order]
    return OPS[hi](OPS[lo](start))


def swapped_pos(start, order):
    """final position if the two moves are applied in the REVERSED (op_hi then op_lo) order."""
    lo, hi = ORDER_OPS[order]
    return OPS[lo](OPS[hi](start))


OP_DESC = {
    "STEP": ("moved one position toward the back of the track (and from the back position it wraps "
             "around to the front position)"),
    "FLIP": ("moved to its mirror position on the track (position 1 swaps with position 4, "
             "and position 2 with position 3)"),
}

# ---- elicitation (forced format; cap 512 so truncation is RARE, not impossible) ----------
MAX_TOKENS = 512  # a reply with finish_reason == "length" is NEVER parsed
REASONING = {"google/": {"effort": "minimal"}}  # config/models.md caveat 1
HARD_STOP_USD = 0.60  # pre-registered hard stop on PROJECTED total billed cost (3 models @ K=4)

SYS = (
    "You are tracking where a coined token sits on a track of figures, recalling a short record of "
    "moves you and your partner agreed it made over a couple of rounds of a game. Read the track "
    "and the record, then answer the single question. Reply with EXACTLY ONE figure name (e.g. "
    "\"{example}\") and NOTHING ELSE -- no explanation, no reasoning, no restatement.")

INTRO_TRACK = (
    "The figures lie along a track. From the front (position 1) to the back (position {k}), the "
    "order is:")
INTRO_HIST = (
    "Here is a record of what you and your partner agreed about where the coined token \"{term}\" "
    "sits on the track. \"{term}\" began on {start_phrase}. Then, over two rounds, it moved. Each "
    "move is stamped with the round it was agreed in (a higher round number means it was agreed "
    "more recently). The two moves are NOT necessarily listed in round order:")

QUERY_TEXT = {
    "COMP": "Question: Which figure does the token \"{term}\" sit on now?",
    "DIRECT": ("Question: Starting from {start_phrase}, \"{term}\" first (round {r_lo}) {desc_lo}, "
               "and then (round {r_hi}) {desc_hi}. Which figure does \"{term}\" sit on now?"),
}

STERN = ("\n\nIMPORTANT: your reply must be EXACTLY ONE of these figure names ({label_list}) -- a "
         "single figure name on a single line, with no other text whatsoever.")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def shape_phrase(shape):
    return f"a {shape}"


def render_track(track):
    """track: list of K shape strings in track-position order (position 1..K)."""
    return "\n".join(f"- Position {i+1}: {shape_phrase(s)}" for i, s in enumerate(track))


def render_history(rec):
    """the two stamped move-lines, in the record's frozen DISPLAY order (decoupled from stamp
    order). Each line states ONE relative move and its round stamp."""
    out = []
    for ln in rec["hist_display"]:
        out.append(f'- Round {ln["round"]}: "{TERM}" {OP_DESC[ln["op"]]}.')
    return "\n".join(out)


def build_user(rec):
    track = render_track(rec["track"])
    start_phrase = shape_phrase(rec["start_shape"])
    if rec["query"] == "DIRECT":
        q = QUERY_TEXT["DIRECT"].format(
            term=TERM, start_phrase=start_phrase, r_lo=rec["r_lo"], r_hi=rec["r_hi"],
            desc_lo=OP_DESC[rec["op_lo"]], desc_hi=OP_DESC[rec["op_hi"]])
    else:
        q = QUERY_TEXT["COMP"].format(term=TERM)
    hist = render_history(rec)
    label_list = ", ".join(shape_phrase(s) for s in rec["track"])
    return (f"{INTRO_TRACK.format(k=K)}\n{track}\n\n"
            f"{INTRO_HIST.format(term=TERM, start_phrase=start_phrase)}\n{hist}\n\n{q}\n"
            f"Reply with exactly one figure name ({label_list}) and nothing else.")


# ---- forced parse: reply must be exactly one of the present shape names ------------------
def parse_forced(txt, present):
    """(pick, mode): mode in {strict, non-strict, None}. `present` = set of shape words (lower).
    Returns the matched shape word (lower-case) or None."""
    if not txt:
        return None, None
    s = txt.strip().strip(string.punctuation + string.whitespace).lower()
    # strict: the whole reply is "a triangle" / "triangle" / "triangle."
    m = re.fullmatch(r"(?:an?\s+)?([a-z]+)", s)
    if m and m.group(1) in present:
        return m.group(1), "strict"
    # non-strict: exactly one present shape word appears on the LAST non-empty line
    lines = [ln for ln in txt.splitlines() if ln.strip()]
    if lines:
        toks = [w for w in re.findall(r"[a-z]+", lines[-1].lower()) if w in present]
        toks = list(dict.fromkeys(toks))
        if len(toks) == 1:
            return toks[0], "non-strict"
    return None, None


def call_fr(model, system, user, max_tokens=None, temperature=0, retries=4, timeout=120,
            reasoning=None):
    """One completion that ALSO surfaces finish_reason (a length-truncated reply is never parsed).
    Transport mirrored from lib/openrouter.call (usage-include flag, retry/backoff)."""
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
