#!/usr/bin/env python3
"""common.py — shared machinery for the relational history-perturbation v3 run.

One module so harvest.py / certify.py / probe.py cannot drift apart on the things the
design (experiments/designs/relational-history-perturbation-v3.md) requires to be
identical everywhere:

- the FORCED single-label elicitation format (fix 1: truncation-proof; completion cap 512,
  gemini reasoning effort "minimal" per config/models.md caveat 1),
- the pre-registered STRICT PARSE RULE (strict / non-strict / NA after one stern retry),
- the cost LEDGER and the pre-registered HARD STOP at $1.50 projected total,
- panel slugs (imported from experiments/lib/openrouter.py PANEL — never hardcoded),
- the frozen design constants (orders, directions, nonces, seeds).

Prompt strings marked "v2 byte-identical" are copied verbatim from
experiments/runs/2026-06-12-relational-history-perturbation-v2/probe.py, per the design
("the logic section of the v2 design carries over verbatim"; only the elicitation format
changes — fix 1).
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
from openrouter import PANEL, URL, call, billed_cost  # noqa: E402

V1 = os.path.abspath(os.path.join(HERE, "..", "2026-05-31-relational-reference-game-v1"))
RAW = os.path.join(HERE, "raw")
LEDGER_PATH = os.path.join(RAW, "cost-ledger.json")

MODELS = {"claude": PANEL["A"], "gpt": PANEL["B"], "gemini": PANEL["C"]}
MODEL_SEED_OFFSET = {"claude": 11, "gpt": 23, "gemini": 37}  # v1/v2 convention
SEED0 = 20260613

# ---- frozen design parameters (v3 design §Conditions / §Stimuli plan) -------------------
ORDERS = ["XXYY", "XYXY", "YXXY", "YYXX", "YXYX", "XYYX"]  # all 6 orders of {X,X,Y,Y}
DIRECTIONS = ["fwd", "rev"]                                # B1 arm retained (fix 5)
N_SAMPLES = 3                                              # 3 description samples/pair (fix 3)
DESCS_PER_FIG = 6                                          # 6 certified = 3 samples x 2
N_CAND = 8                                                 # harvest candidates per call
WORD_BUDGET = 12                                           # v1 director budget, unchanged
# Fresh frozen non-descriptive nonces (design: PLOVNEK / SKARMIL / VANTREX; no v2 carryover).
NONCE = {0: "PLOVNEK", 1: "SKARMIL", 2: "VANTREX"}
# v1 figures.json content hash the design pins ("original sha256 a2709582…").
FIGURES_SHA256 = "a2709582a58e54378190b3e6e15191be4fe1f05d27c37830856f958371deb6c4"

# ---- elicitation (fix 1: forced format; cap raised so truncation is RARE, not impossible)
MAX_TOKENS = 512  # v2 was 128; 512 makes truncation rare, NOT impossible — a reply with
                  # finish_reason == "length" is NEVER parsed (critic blocker 2, 2026-06-13)
REASONING = {"google/": {"effort": "minimal"}}  # config/models.md caveat 1
HARD_STOP_USD = 1.50  # pre-registered hard stop on PROJECTED TOTAL billed cost

PROBE_SYS = (
    "You match an abstract figure to a record. Each figure is an 8x8 grid of '#' (filled) and '.' "
    "(empty). You are shown a record about ONE target figure plus a short label for it; decide "
    "which of your figures is that target. Reply with EXACTLY ONE figure label and NOTHING ELSE "
    "-- no explanation, no reasoning, no restatement (e.g. {example}).")

CERT_SYS = (
    "You match an abstract figure to a description. Each figure is an 8x8 grid of '#' (filled) "
    "and '.' (empty). You are shown a single description of ONE target figure; decide which of "
    "your figures is that target. Reply with EXACTLY ONE figure label and NOTHING ELSE "
    "-- no explanation, no reasoning, no restatement (e.g. {example}).")

# v2 byte-identical (history intro per presentation direction):
INTRO = {
    "fwd": ("Your partner referred to ONE target figure over several rounds. What they said, "
            "in the order it happened (earliest first):"),
    "rev": ("Your partner referred to ONE target figure over several rounds. What they said, "
            "in reverse order (most recent first):"),
}

# Sterner one-label-only reminder appended on the single retry (design §Elicitation (c)).
STERN = ("\n\nIMPORTANT: your reply must be EXACTLY ONE label from ({label_list}) -- a single "
         "token on a single line, with no other text whatsoever.")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def load_figures():
    """The 6 frozen v1 figures, unchanged (design §Stimuli plan). Hash-checked."""
    import hashlib
    blob = open(os.path.join(V1, "figures.json"), "rb").read()
    # v1 build_figures.py hashed the JSON blob and then wrote blob + "\n".
    if hashlib.sha256(blob.rstrip(b"\n")).hexdigest() != FIGURES_SHA256:
        sys.exit("FATAL: v1 figures.json content hash mismatch — figures are not the frozen "
                 f"v1 set (expected {FIGURES_SHA256[:8]}…). Refusing to build/probe.")
    return json.loads(blob)["figures"]


def figure_pairs(figs):
    pairs = {}
    for fid, f in figs.items():
        pairs.setdefault(f["pair"], []).append(fid)
    for p in pairs.values():
        p.sort()
    return pairs


def grid_block(order, fig):
    """order: list of (label, canonical_id) pairs. v2 byte-identical rendering."""
    out = []
    for label, cid in order:
        out.append(f"[{label}]")
        out.extend("  " + row for row in fig[cid]["grid"])
    return "\n".join(out)


# ---- the pre-registered strict parse rule (design §Elicitation) --------------------------
LABEL_RE = re.compile(r"\bP\s*([1-6])\b", re.IGNORECASE)


def parse_forced(txt, labels):
    """Returns (pick, parse_mode): parse_mode in {"strict", "non-strict", None}.

    (a) reply that is exactly one label after whitespace/punctuation stripping -> strict;
    (b) else, if the final non-empty line contains exactly one label token -> non-strict;
    (c) else -> (None, None): caller retries once with the stern reminder, then NA.
    """
    if not txt:
        return None, None
    stripped = txt.strip().strip(string.punctuation + string.whitespace)
    s = stripped.upper().replace(" ", "")
    if s in labels:
        return s, "strict"
    lines = [ln for ln in txt.splitlines() if ln.strip()]
    if lines:
        toks = [f"P{m.group(1)}" for m in LABEL_RE.finditer(lines[-1])]
        toks = [t for t in toks if t in labels]
        if len(toks) == 1:
            return toks[0], "non-strict"
    return None, None


def call_fr(model, system, user, max_tokens=None, temperature=0, retries=4, timeout=120,
            reasoning=None):
    """One chat completion that ALSO surfaces choices[0].finish_reason.

    Critic blocker 2 (2026-06-13): a reply with finish_reason == "length" is NEVER
    parsed for a pick — its visible text is a truncated prefix and any label in it is
    untrustworthy. lib/openrouter.call discards finish_reason, so the transport is
    mirrored here verbatim (same body incl. the usage-include flag, same retry/backoff);
    flagged for upstreaming to lib/ in a later session rather than editing the shared
    module mid-run. Returns {content, usage, finish_reason[, error]}.
    """
    key = os.environ["OPENROUTER_API_KEY"]
    if max_tokens is None:
        max_tokens = 4096 if model.startswith("google/") else 64
    body = {"model": model,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
            "temperature": temperature, "max_tokens": max_tokens,
            "usage": {"include": True}}  # <- OpenRouter returns billed usage.cost
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


def parse_reply(r, labels):
    """Strict parse rule applied to one response dict — but a length-truncated reply
    (finish_reason == "length") is NEVER parsed for a pick: parse-fail, so the caller's
    stern retry, then NA (critic blocker 2; pre-registered)."""
    if r.get("finish_reason") == "length":
        return None, None
    return parse_forced(r.get("content"), labels)


def call_forced(model, sys_p, user, labels, label_list):
    """One forced-format call; on transport error, length-truncation, or parse-fail, ONE
    retry with the stern one-label-only reminder (design §Elicitation (c)); persistent
    failure -> NA. Returns (response, pick, parse_mode, retried, usages); the returned
    response carries `finish_reason` for the record."""
    rsn = reasoning_for(model)
    r = call_fr(model, sys_p, user, max_tokens=MAX_TOKENS, reasoning=rsn)
    pick, mode = parse_reply(r, labels)
    if not r.get("error") and pick is not None:
        return r, pick, mode, False, [r.get("usage", {})]
    r2 = call_fr(model, sys_p, user + STERN.format(label_list=label_list),
                 max_tokens=MAX_TOKENS, reasoning=rsn)
    pick2, mode2 = parse_reply(r2, labels)
    usages = [u for u in (r.get("usage"), r2.get("usage")) if u]
    if pick2 is not None or not r.get("content"):
        return r2, pick2, mode2, True, usages
    return r, pick, mode, True, usages


def flat_cost(recs):
    """Records store `usage` as a LIST of per-call usage dicts; flatten for billed_cost."""
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
    """Pre-registered phase checkpoint: spent-so-far + projection > $1.50 -> ABORT
    (design §Cost pre-flight: 're-design, don't push through')."""
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
