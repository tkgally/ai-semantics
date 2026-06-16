#!/usr/bin/env python3
"""common.py — shared machinery for the relational STAMP-COMPREHENSION pre-probe (Option B).

This is the Option-B stamp-comprehension pre-probe ratified by the 2026-06-16 adversarial
review of decisions/open/relational-v5-text-position-neutralization (adopt-default: B then A,
staged; C the binding fallback). Its ONLY job is a gate: do the panel models read the round
STAMP *as a recency value at all*, when physical line-position is neutralized so only the
stamp value disambiguates? v4 found both models follow physical text-position, and its binding
scope limit is that "position-following here is indistinguishable from stamp-blindness". B
resolves exactly that ambiguity, cheaply, BEFORE any geometry-decoupled chronology arm (A)
is built. A B-fail for both surviving models CLOSES the line at Option C (no stamp-format
retune — anti-cheat carry-forward).

Instrument family is inherited from relational-history-perturbation-v4 (stamped per-line
rounds; forced single-label elicitation; never-parse-`finish_reason: length`; cost ledger +
hard stop), but B needs NO harvested near-twin descriptions — the "convention" each round
coins is a frozen nonce label, so there is no stimulus-certification burden (design §B
"low stimulus-certification burden"). Panel = claude + gemini, the A-eligible panel carried
from v4 (gpt was dropped from the finding-bearing relational panel for a stimulus-generation
reason, not a comprehension one; B does not re-open that).

anchor: internal-contrast-only (within-model behavioural check over byte-identical content;
no human-comparison claim — ratified 2026-06-16).
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

# A-eligible relational panel carried from v4: claude + gemini.
MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"]}
SEED0 = 20260616

# ---- frozen design parameters (PREREG) --------------------------------------------------
K = 4                       # lines (rounds) per record
QUERIES = ["MR", "LR"]      # MR = most-recent (max round); LR = earliest (min round)
N_BLOCKS = 12               # distinct present-sets (4-nonce subsets), each used K=4 times
# Construction (build_trials): 12 balanced present-sets x 4 records each = 48 records/model.
# Within each present-set's 4 records, the CORRECT nonce cycles through all 4 members exactly
# once AND the correct line's physical position cycles through all 4 slots exactly once (a
# Latin square). Consequence: (a) a position-follower scores exactly 1/K; (b) conditional on
# the present-set the correct nonce is UNIFORM over its members, so ANY fixed nonce-preference
# ordering also scores exactly 1/K (the residual-lexical-cue fix, 2026-06-16 pre-run critic
# blocker 2). Both bounds are asserted empirically at build (over all K! position strategies
# and all 8! nonce orderings).
PASS_FLOOR = 0.80           # pre-registered comprehension floor (pooled MR+LR accuracy)
POS_CHANCE = 1.0 / K        # 0.25 — both a position-follower AND a nonce-preference shortcut
                            # score here (proven at build); only stamp-value reading clears 0.80.
# Frozen non-contiguous round quadruples (NOT {1,2,3,4}: forces reading the actual stamp
# value, and spreads gaps so "min/max round" is the only consistent recency reading). Each
# is sorted; the build assigns nonces to rounds independently of value, then shuffles display
# order. Cycled across records.
ROUND_SETS = [
    [2, 4, 7, 9],
    [1, 3, 6, 8],
    [3, 5, 6, 9],
    [2, 5, 7, 8],
    [1, 4, 5, 9],
    [3, 4, 7, 8],
]
# Frozen nonce pool (clearly distinct non-words; none a substring of another).
NONCES = ["GORLAX", "MIVUNT", "ZEPHRO", "QUANDIL", "BRELTOM", "FANUKE", "SPOGDEX", "WURVANE"]

# ---- elicitation (forced format; cap 512 so truncation is RARE, not impossible) ----------
MAX_TOKENS = 512  # a reply with finish_reason == "length" is NEVER parsed
REASONING = {"google/": {"effort": "minimal"}}  # config/models.md caveat 1
HARD_STOP_USD = 0.50  # pre-registered hard stop on PROJECTED total billed cost (B is cheap)

SYS = (
    "You are recalling a short record of how you and your partner named ONE figure over "
    "several rounds of a game. Read the record and answer the single question. Reply with "
    "EXACTLY ONE name (one word) and NOTHING ELSE -- no explanation, no reasoning, no "
    "restatement (e.g. {example}).")

# Neutral INTRO (does NOT tell the model to weight recency or position — whether it reads the
# stamp value as recency is exactly what is measured). Stamps carry chronology; physical line
# order is independent and balanced.
INTRO = (
    "Here is a record of the names you and your partner used for ONE figure over several "
    "rounds. Each line is stamped with the round it was said in (a higher round number means "
    "it was said more recently). The lines are NOT necessarily listed in round order:")

QUERY_TEXT = {
    "MR": "Question: Which name did you agree on MOST RECENTLY (in the latest round)?",
    "LR": "Question: Which name did you agree on EARLIEST (in the very first round)?",
}

STERN = ("\n\nIMPORTANT: your reply must be EXACTLY ONE of these names ({label_list}) -- a "
         "single word on a single line, with no other text whatsoever.")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def render_record(lines):
    """lines: list of dicts {round, nonce} in PHYSICAL (display) order."""
    return "\n".join(f'- Round {ln["round"]}: we agreed to call it "{ln["nonce"]}".'
                     for ln in lines)


def build_user(rec):
    body = render_record(rec["lines_display"])
    return f"{INTRO}\n\n{body}\n\n{QUERY_TEXT[rec['query']]}"


# ---- forced parse: reply must be exactly one of the present nonces ------------------------
def parse_forced(txt, present):
    """(pick, mode): mode in {strict, non-strict, None}. `present` = set of nonces in record."""
    if not txt:
        return None, None
    s = txt.strip().strip(string.punctuation + string.whitespace).upper()
    if s in present:
        return s, "strict"
    # non-strict: a single present nonce as a whole word on the last non-empty line
    lines = [ln for ln in txt.splitlines() if ln.strip()]
    if lines:
        toks = [w for w in re.findall(r"[A-Z]+", lines[-1].upper()) if w in present]
        toks = list(dict.fromkeys(toks))  # dedupe, keep order
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
