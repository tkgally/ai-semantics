#!/usr/bin/env python3
"""common.py -- shared machinery for the DATIVE information-structure probe.

Indicator (ratified decisions/resolved/dative-anchor-and-indicator, Q2 Option (i)):
a logprob-free GRADED FORCED-CHOICE. The model is shown a discourse context (which
establishes whether the recipient or the theme is discourse-GIVEN) and the SAME
ditransitive proposition phrased two ways -- double-object (DOC, "gave the manager a
raise") vs. prepositional dative (PD, "gave a raise to the manager") -- and distributes
100 points between them by naturalness in that context. We read DOC-preference =
DOC_points / (DOC_points + PD_points) in [0,1].

The finding-bearing measure is the WITHIN-ITEM shift across contexts (see analyze.py);
because the two phrasings are byte-identical across an item's contexts, the shift is
immune to any length / position / order surface cue by construction (certified in
build_trials.py).

The givenness validity guard (ratification modification 4): the discourse context is the
ONLY thing that varies across an item's cells, so a context-insensitive shallow
preference shows up as zero shift; the neutral both-new baseline locates the default.
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

# Full three-model panel (config/models.md). All three are SUBJECTS; cross-model
# divergence in how cleanly each tracks information structure is itself data (charter §6;
# conjecture prediction 3).
MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"], "gpt": PANEL["B"]}

MAX_TOKENS = 512   # room for a brief justification before the FINAL line; gemini needs headroom
REASONING = {"google/": {"effort": "minimal"}}   # gemini cost-driver mitigation, held constant
# Pre-registered hard stop on PROJECTED total billed cost (V2 REPLICATION, session 53,
# 2026-06-20). Set from the v1 MEASURED bill, not the rate card: v1 (identical structure --
# 44 items, 240 trials/model, 720 calls) billed $1.578 total (claude $0.990, gemini $0.485,
# gpt $0.103) under this exact working-surface format. Pre-register $2.00 so a small
# per-call variance (esp. gemini, which ran ~5x its rate-card estimate in v1) does not
# spuriously trip mid-run and force a resume; $2.00 stays under the $2.50 single-run flag,
# and the day total after this run (session-51 $1.583 + ~$1.58) projects ~$3.16, well under
# the $5/day UTC cap. This is a pure budget gate, fixed BEFORE any model call; it never
# touches measurement, scoring, or the frozen stimuli sha.
HARD_STOP_USD = 2.00

SYS = ("You are a careful native speaker of English judging how natural different "
       "phrasings sound in a given context. You weigh the discourse context (what has "
       "already been mentioned) when judging which phrasing flows better. You MAY think "
       "briefly, but you MUST end your reply with a line in EXACTLY this form: "
       "FINAL: A=<number>, B=<number> -- two whole numbers that add up to 100, giving "
       "more points to the more natural phrasing.")

USER_TMPL = (
    "Context: {context}\n\n"
    "Now consider how the next sentence could be phrased. Here are two versions of the "
    "same sentence:\n"
    "A) {option_a}\n"
    "B) {option_b}\n\n"
    "Given the context above, distribute 100 points between A and B according to how "
    "natural each one sounds as the next sentence (more points = more natural; the two "
    "numbers must add up to 100).\n"
    "End with a line of the form: FINAL: A=<number>, B=<number>.")

STERN = ("\n\nIMPORTANT: end with a line EXACTLY like 'FINAL: A=70, B=30' -- two whole "
         "numbers adding to 100.")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def build_user(trial):
    a = trial["doc"] if trial["doc_is_a"] else trial["pd"]
    b = trial["pd"] if trial["doc_is_a"] else trial["doc"]
    return USER_TMPL.format(context=trial["context"], option_a=a, option_b=b)


# ---- graded parse: extract A=<n>, B=<n> from the declared FINAL line --------------------
_FINAL_RE = re.compile(r"final\s*[:\-]*\s*a\s*=\s*(\d{1,3})\s*[,;/ ]+\s*b\s*=\s*(\d{1,3})")
_ANY_RE = re.compile(r"\ba\s*=\s*(\d{1,3})\s*[,;/ ]+\s*b\s*=\s*(\d{1,3})")


def parse_graded(txt):
    """Return (a_points, b_points, mode) or (None, None, None).

    Reads the LAST 'A=<n>, B=<n>' on a FINAL line first; falls back to the last such
    pair anywhere. Target-blind: keys on position in the reply, not on which option is
    DOC (the DOC/PD<->A/B mapping is counterbalanced and applied in analysis)."""
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
    """DOC-preference in [0,1] from the two point allocations."""
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
    """One graded call; on transport error / length-truncation / parse-fail, ONE stern
    retry; persistent failure -> NA. Returns (record, a, b, mode, retried, usages)."""
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
