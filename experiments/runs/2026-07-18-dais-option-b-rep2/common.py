#!/usr/bin/env python3
"""common.py -- shared machinery for the DAIS Option-B graded-preference correlation REP2 (s250).

REPLICATION NOTE (s250): byte-identical to the s248 common.py EXCEPT the two budget hard-stop
constants below (HARD_STOP_PER_ARM_USD / HARD_STOP_USD), lowered so this rep2 run cannot breach the
$5/day UTC cap given the $1.826368 already spent UTC-2026-07-18 (s247+s248). Budget gates only; they
NEVER touch measurement, scoring, or the frozen stimuli. All SYS / USER_TMPL / parse / doc_pref /
call_graded machinery is byte-identical to s248 (the frozen indicator).

Indicator: the graded forced-choice ratified for the dative line
(decisions/resolved/dative-anchor-and-indicator, Q2 Option (i) -- distribute 100 points between
the double-object (DOC) and prepositional-dative (PD) phrasings), reused BYTE-SHAPE but with NO
discourse context (the Arm-defining difference from the givenness probe). The measure is a BARE
naturalness preference between the two isolated phrasings, matching DAIS's isolated-pair slider
task. We read DO-preference = DOC_points / (DOC_points + PD_points) in [0,1].

Contamination + anchor discipline: stimuli are project-constructed (build_trials.py); DAIS supplies
only the verb list + the human ratings. Scoring is target-blind (position-based parse; the DOC<->A/B
mapping is counterbalanced and frozen per trial) and BLIND to the human targets during collection
(the run writes raw model preferences only; human_targets.json is read only by analyze.py).
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
from openrouter import PANEL, URL, billed_cost  # noqa: E402,F401

RAW = os.path.join(HERE, "raw")
LEDGER_PATH = os.path.join(RAW, "cost-ledger.json")

# Full three-model panel (config/models.md). All three are SUBJECTS; cross-model divergence in the
# effect-size correlation is itself data (charter §6; conjecture prediction 3).
MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"], "gpt": PANEL["B"]}

MAX_TOKENS = 512   # gemini needs reasoning headroom; bare-preference visible output is short.
REASONING = {"google/": {"effort": "minimal"}}   # gemini cost-driver mitigation, held constant.

# Per-arm + total pre-registered hard stops on PROJECTED billed cost (Q2-A separable/splittable).
# Pre-flight: 1,200 calls (600 Arm A + 600 Arm B) of a BARE-preference graded forced-choice (shorter
# than the givenness probe's 512-tok justified outputs, so <= the ~$0.00217/call measured there).
# Expected ~$2.0-2.6 total. Per-arm ceiling $1.70 (each arm = 200 items x 3 models = 600 calls);
# total ceiling $3.40 -- above the ~$2.6 expectation so modest per-call variance does not spuriously
# trip, and far below the level that would breach the $5/day UTC cap (today's UTC-2026-07-18 ledger
# carries only $0.002286 prior, so a $3.40 ceiling caps the day at ~$3.40 < $5.00). ABOVE the $2.50
# single-run prudence flag => run as the day's only spend on this full-$5 UTC day (the s229
# precedent), OR split the two arms across UTC days (each arm an independent frozen instrument;
# splitting does not change either measurement). Pure budget gate, fixed BEFORE any model call; it
# never touches measurement, scoring, or the frozen stimuli sha.
HARD_STOP_PER_ARM_USD = 1.30
HARD_STOP_USD = 2.60   # s250 rep2: $1.826368 prior UTC-2026-07-18 + $2.60 cap = $4.43 < $5.00.

SYS = ("You are a careful native speaker of English judging how natural different phrasings sound. "
       "You are shown the SAME sentence phrased two ways and rate which sounds more natural as an "
       "isolated sentence, with no surrounding context. You MAY think briefly, but you MUST end your "
       "reply with a line in EXACTLY this form: FINAL: A=<number>, B=<number> -- two whole numbers "
       "that add up to 100, giving more points to the more natural phrasing.")

USER_TMPL = (
    "Here are two versions of the same sentence:\n"
    "A) {option_a}\n"
    "B) {option_b}\n\n"
    "Distribute 100 points between A and B according to how natural each one sounds as an isolated "
    "sentence (more points = more natural; the two numbers must add up to 100).\n"
    "End with a line of the form: FINAL: A=<number>, B=<number>.")

STERN = ("\n\nIMPORTANT: end with a line EXACTLY like 'FINAL: A=70, B=30' -- two whole numbers "
         "adding to 100.")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def build_user(trial):
    a = trial["doc"] if trial["doc_is_a"] else trial["pd"]
    b = trial["pd"] if trial["doc_is_a"] else trial["doc"]
    return USER_TMPL.format(option_a=a, option_b=b)


# ---- graded parse: extract A=<n>, B=<n> from the declared FINAL line --------------------
_FINAL_RE = re.compile(r"final\s*[:\-]*\s*a\s*=\s*(\d{1,3})\s*[,;/ ]+\s*b\s*=\s*(\d{1,3})")
_ANY_RE = re.compile(r"\ba\s*=\s*(\d{1,3})\s*[,;/ ]+\s*b\s*=\s*(\d{1,3})")


def parse_graded(txt):
    """Return (a_points, b_points, mode) or (None, None, None). Target-blind: keys on position in
    the reply, not on which option is DOC (the DOC<->A/B mapping is counterbalanced, applied in
    analysis via doc_pref)."""
    if not txt:
        return None, None, None
    low = txt.lower()
    finals = _FINAL_RE.findall(low)
    if finals:
        a, b = finals[-1]
        return int(a), int(b), "final-tag"
    anys = _ANY_RE.findall(low)
    if anys:
        a, b = anys[-1]
        return int(a), int(b), "any-pair"
    return None, None, None


def doc_pref(a_points, b_points, doc_is_a):
    """DO-preference in [0,1] from the two point allocations."""
    total = a_points + b_points
    if total <= 0:
        return None
    doc_pts = a_points if doc_is_a else b_points
    return doc_pts / total


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


def parse_reply(r):
    if r.get("finish_reason") == "length":
        return None, None, None
    return parse_graded(r.get("content"))


def call_graded(model, user):
    """One graded call; on transport error / length-truncation / parse-fail, ONE stern retry;
    persistent failure -> NA. Returns (record, a, b, mode, retried, usages)."""
    rsn = reasoning_for(model)
    r = call_fr(model, SYS, user, max_tokens=MAX_TOKENS, reasoning=rsn)
    a, b, mode = parse_reply(r)
    if not r.get("error") and a is not None:
        return r, a, b, mode, False, [r.get("usage", {})]
    r2 = call_fr(model, SYS, user + STERN, max_tokens=MAX_TOKENS, reasoning=rsn)
    a2, b2, mode2 = parse_reply(r2)
    usages = [u for u in (r.get("usage"), r2.get("usage")) if u]
    if a2 is not None or not r.get("content"):
        return r2, a2, b2, mode2, True, usages
    return r, a, b, mode, True, usages


def flat_cost(recs):
    flat = []
    for r in recs:
        u = r.get("usage")
        if isinstance(u, list):
            flat += [{"usage": x} for x in u if x]
        elif u:
            flat.append({"usage": u})
    return billed_cost([flat])


# ---- cost ledger + pre-registered hard stops --------------------------------------------
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
          f"-> cumulative ${total:.5f} (total hard stop ${HARD_STOP_USD:.2f})")
    return total


def check_hard_stop(projected_additional_usd, phase, arm_spent=None):
    spent = ledger_total()
    projected = spent + projected_additional_usd
    print(f"  [gate] {phase}: spent ${spent:.4f} + projected ${projected_additional_usd:.4f} "
          f"= ${projected:.4f} (total hard stop ${HARD_STOP_USD:.2f})")
    if projected > HARD_STOP_USD:
        sys.exit(f"HARD STOP: projected total ${projected:.4f} exceeds the pre-registered total "
                 f"${HARD_STOP_USD:.2f} cap. Re-design; do not push through.")
    if arm_spent is not None and arm_spent > HARD_STOP_PER_ARM_USD:
        sys.exit(f"HARD STOP: this arm's spend ${arm_spent:.4f} exceeds the per-arm "
                 f"${HARD_STOP_PER_ARM_USD:.2f} cap.")


def append_jsonl(path, rec):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as f:
        f.write(json.dumps(rec) + "\n")


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return [json.loads(ln) for ln in f if ln.strip()]
