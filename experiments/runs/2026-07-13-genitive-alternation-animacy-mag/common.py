#!/usr/bin/env python3
"""common.py -- shared machinery for the GENITIVE-alternation possessor-animacy probe.

Indicator (ratified decisions/resolved/genitive-alternation-anchor-and-indicator, Q2 Option (i)):
a logprob-free GRADED FORCED-CHOICE. Given a possessive proposition with the possessum held fixed,
the model distributes 100 points by naturalness between the two phrasings of the SAME proposition --
the s-genitive ("the judge's decision") and the of-genitive ("the decision of the judge"). We read
s-preference = s_points / (s_points + of_points) in [0,1].

The finding-bearing measure is the WITHIN-FRAME animacy shift (see analyze.py):
    shift(frame) = mean(s-pref | animate possessor) - mean(s-pref | inanimate possessor)
Human direction (Dubois et al. 2023): animate -> s-genitive, so shift > 0. The s-gen<->A/B mapping
is counterbalanced and the parser is target-blind (keys on reply position, not on which option is
the s-genitive). Port of the byte-frozen dative/CC graded instrument.
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

MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"], "gpt": PANEL["B"]}

MAX_TOKENS = 400   # brief justification then the FINAL line; gemini needs headroom for reasoning
REASONING = {"google/": {"effort": "minimal"}}

# Pre-registered hard stop on PROJECTED total billed cost. MAG (s222) pre-flight: this is the
# POWERED MAGNITUDE re-run — a TYPICAL-ONLY new arm of 36 fresh disjoint frames (no new nonce; the
# firewall already replicated 3/3 twice, s218+s220), pooled with the two prior disjoint 36-frame
# typical arms => 108 pooled typical frames for a within-model magnitude+interval (the A2a-merged
# pattern NEXT.md s221 named). 36 typical frames x 6 trials x 3 models = 648 calls. At the s218/rep2
# per-call billed rate (claude/gemini ~$0.0017, gpt ~$0.00034) => expect ~$0.81. HARD stop $1.20:
# above the expectation so per-call variance does not spuriously trip, well below the $2.50
# single-run prudence flag and the $5/day cap (UTC-2026-07-13 spend before this run $2.612545, so
# $2.61 + ~$0.81 ~ $3.42 of $5.00). This is the ONE documented constant change from the byte-frozen
# rep2/s218 common.py (mirrors the A2a re-run pattern where the frozen MEASUREMENT instrument differs
# only in a justified budget constant); it never touches measurement or the frozen stimuli sha. The
# ANALYSIS is a NEW pre-registered pooling script (analyze_merged.py), not the frozen analyze.py.
HARD_STOP_USD = 1.20

SYS = ("You are a careful native speaker of English judging how natural different phrasings sound. "
       "You MAY think briefly, but you MUST end your reply with a line in EXACTLY this form: "
       "FINAL: A=<number>, B=<number> -- two whole numbers that add up to 100, giving more points "
       "to the more natural phrasing.")

USER_TMPL = (
    "{setup}Here are two ways to phrase the same thing:\n"
    "A) {option_a}\n"
    "B) {option_b}\n\n"
    "Distribute 100 points between A and B according to how natural each phrasing sounds "
    "(more points = more natural; the two numbers must add up to 100).\n"
    "End with a line of the form: FINAL: A=<number>, B=<number>.")

STERN = ("\n\nIMPORTANT: end with a line EXACTLY like 'FINAL: A=70, B=30' -- two whole "
         "numbers adding to 100.")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def build_user(trial):
    """Nonce trials carry a one-clause gloss establishing the possessor's animacy (never its
    orthography). Typical trials have no setup clause."""
    gloss = trial.get("gloss")
    setup = f"Imagine {gloss}. " if gloss else ""
    return USER_TMPL.format(setup=setup, option_a=trial["option_a"], option_b=trial["option_b"])


_FINAL_RE = re.compile(r"final\s*[:\-]*\s*a\s*=\s*(\d{1,3})\s*[,;/ ]+\s*b\s*=\s*(\d{1,3})")
_ANY_RE = re.compile(r"\ba\s*=\s*(\d{1,3})\s*[,;/ ]+\s*b\s*=\s*(\d{1,3})")


def parse_graded(txt):
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


def s_pref(a_points, b_points, s_is_a):
    """s-genitive preference in [0,1]: s_points / (s_points + of_points)."""
    total = a_points + b_points
    if total <= 0:
        return None
    s_pts = a_points if s_is_a else b_points
    return s_pts / total


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
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                d = json.load(r)
            ch = d["choices"][0]
            return {"content": (ch["message"].get("content") or "").strip(),
                    "usage": d.get("usage", {}), "finish_reason": ch.get("finish_reason")}
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
    print(f"  [ledger] {phase}: ${billed:.5f} ({calls} calls, {missing} missing) "
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
