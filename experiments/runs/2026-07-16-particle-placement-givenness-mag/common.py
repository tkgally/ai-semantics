#!/usr/bin/env python3
"""common.py -- shared machinery for the VERB-PARTICLE-PLACEMENT object-givenness probe (A5, 3rd sibling).

Indicator (ratified decisions/resolved/particle-placement-anchor-and-indicator, Q2 Option (i)):
a logprob-free GRADED FORCED-CHOICE. Given a verb-particle proposition with the verb + particle +
object head-noun held fixed, the model distributes 100 points by naturalness between the two orders
of the SAME proposition -- the JOINED order ("picked up the box", V-Prt-DO) and the SPLIT order
("picked the box up", V-DO-Prt). We read split-pref = split_points / (split_points + joined_points).

The finding-bearing measures (see analyze.py) are WITHIN-FRAME shifts:
    Arm 1 (definiteness): shift1(frame) = mean(split-pref | definite) - mean(split-pref | indefinite)
    Arm 2 (firewall):     shift2(frame) = mean(split-pref | GIVEN)    - mean(split-pref | NEW-MENTIONED)
    Arm 3 (length):       shift3(frame) = mean(split-pref | short)    - mean(split-pref | long)
Human direction (Kim et al. 2016 / Gries 1999): definite/given/short object -> split, so shift > 0.
The split<->A/B mapping is counterbalanced and the parser is target-blind (keys on reply position,
not on which option is the split order). Port of the byte-frozen dative/genitive graded instrument.

Arm 2's scored strings are BYTE-IDENTICAL across conditions; the givenness manipulation lives ONLY in
the preceding discourse context (dative pattern). Arms 1 & 3 carry no context (the object string itself
varies), so build_user emits a context clause only when the trial supplies one.
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

# Pre-registered hard stop on PROJECTED total billed cost. Pure budget gate; never touches measurement
# or the frozen stimuli sha. This is the ONLY line in common.py that differs from the byte-frozen v1/rep2
# instrument: the MAG arm (session 238) is FIREWALL-ONLY (Arms 1 & 3 dropped), so it is 48 frames x 6
# firewall trials x 3 models = 864 calls (vs rep2's 2,016). At the v1/rep2 OBSERVED per-call prices
# (claude ~$0.00248, gemini ~$0.00173, gpt ~$0.00039) the firewall-only panel projects ~$1.32 (claude
# ~$0.71 + gemini ~$0.50 + gpt ~$0.11). HARD stop $1.60: above that projection (~21% headroom) so per-call
# variance does not spuriously trip, and far below the $5/day UTC cap. Set from the v1/rep2 REALITY (not
# the ~4x-too-low v1 pre-flight that halted s225). Run on a same-UTC-day with ~$3.68 headroom (s238).
#
# BUDGET-ONLY RAISE 1.60 -> 2.00 (s238, mid-run; the s225->s226 precedent). The initial 1.60 halted the
# run partway through gpt: claude billed $1.0208 (pricier than the ~$0.71 pre-flight -- longer graded
# justifications this occasion, $0.00355/call vs the v1/rep2 $0.00248) + gemini $0.5100 + liveness $0.0034
# = $1.5342, so gpt's projected $1.684 tripped 1.60. True full-run cost ~$1.64 (gpt ~$0.11 remaining). This
# is a PURE budget constant -- it never touches measurement, the prompt/parser/indicator, or the frozen
# stimuli/freq_control shas, and the run stayed BLIND through the halt (no analyze run, no raw peeked;
# claude 288/288, gemini 288/288, gpt 30/288 when halted). 2.00 clears the true ~$1.64 with margin, stays
# under the $2.50 single-run prudence flag, and far under the $5/day cap. Resume: `probe.py full`
# (crash-safe; skips the 576 done claude+gemini trials, finishes gpt from 30).
HARD_STOP_USD = 2.00

# Arms 1 & 3 present two orders of the SAME proposition with no discourse context (context-free).
SYS_PLAIN = ("You are a careful native speaker of English judging how natural different phrasings sound. "
             "You MAY think briefly, but you MUST end your reply with a line in EXACTLY this form: "
             "FINAL: A=<number>, B=<number> -- two whole numbers that add up to 100, giving more points "
             "to the more natural phrasing.")

# Arm 2 supplies a preceding discourse context; the model is told to weigh it (dative pattern).
SYS_CONTEXT = ("You are a careful native speaker of English judging how natural different phrasings sound "
               "in a given context. You weigh the discourse context (what has already been mentioned) "
               "when judging which phrasing flows better. You MAY think briefly, but you MUST end your "
               "reply with a line in EXACTLY this form: FINAL: A=<number>, B=<number> -- two whole "
               "numbers that add up to 100, giving more points to the more natural phrasing.")

USER_PLAIN = (
    "Here are two ways to phrase the same thing:\n"
    "A) {option_a}\n"
    "B) {option_b}\n\n"
    "Distribute 100 points between A and B according to how natural each phrasing sounds "
    "(more points = more natural; the two numbers must add up to 100).\n"
    "End with a line of the form: FINAL: A=<number>, B=<number>.")

USER_CONTEXT = (
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


def sys_for(trial):
    return SYS_CONTEXT if trial.get("context") else SYS_PLAIN


def build_user(trial):
    """Arm 2 trials carry a discourse `context` that establishes the object's information status;
    Arms 1 & 3 carry no context (the object string itself varies)."""
    if trial.get("context"):
        return USER_CONTEXT.format(context=trial["context"], option_a=trial["option_a"],
                                   option_b=trial["option_b"])
    return USER_PLAIN.format(option_a=trial["option_a"], option_b=trial["option_b"])


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


def split_pref(a_points, b_points, split_is_a):
    """split-order preference in [0,1]: split_points / (split_points + joined_points)."""
    total = a_points + b_points
    if total <= 0:
        return None
    split_pts = a_points if split_is_a else b_points
    return split_pts / total


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


def call_graded(model, trial):
    system = sys_for(trial)
    user = build_user(trial)
    rsn = reasoning_for(model)
    r = call_fr(model, system, user, max_tokens=MAX_TOKENS, reasoning=rsn)
    a, b, mode = parse_reply(r)
    if not r.get("error") and a is not None:
        return r, a, b, mode, False, [r.get("usage", {})]
    r2 = call_fr(model, system, user + STERN, max_tokens=MAX_TOKENS, reasoning=rsn)
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
