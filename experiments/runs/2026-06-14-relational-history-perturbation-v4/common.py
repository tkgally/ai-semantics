#!/usr/bin/env python3
"""common.py — shared machinery for the relational history-perturbation v4 run.

v4 (experiments/designs/relational-history-perturbation-v4.md) keeps the v2/v3 instrument
class — text-grid referents, near-twin pairs, byte-identical content multisets, nonce
coined terms, fresh-matcher forced-format elicitation, internal within-model contrast —
and changes exactly two things at the machinery level:

1. **Chronology is carried by an EXPLICIT per-line round STAMP, not by physical position.**
   Each evidence line is rendered "- Round k: ...", and the INTRO states that the round
   number (not the line order) carries when it was said. This is what lets a single arm
   dissociate "chronologically latest" (stamp) from "physically last" (line order) — the
   one structural change the v3 verifier named as the real next step.
2. **The panel is claude + gemini only** (gpt dropped from the finding-bearing panel per
   the v3 fix-list: two harvest+certification attempts showed gpt cannot supply
   solo-decodable near-twin descriptions at this difficulty — design §Panel decision).

Everything else — the forced single-label elicitation, the pre-registered strict parse
rule (strict / non-strict / NA after one stern retry), the never-parse-`finish_reason ==
"length"` rule (critic blocker 2, carried from v3), the cost ledger + pre-registered
$1.50 hard stop, the clustered-bootstrap conventions, panel slugs imported from
experiments/lib/openrouter.py — is copied verbatim from v3's common.py so the two runs
cannot drift on the things the design requires identical.
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

V1 = os.path.abspath(os.path.join(HERE, "..", "2026-05-31-relational-reference-game-v1"))
RAW = os.path.join(HERE, "raw")
LEDGER_PATH = os.path.join(RAW, "cost-ledger.json")

# v4 finding-bearing panel: claude + gemini ONLY (gpt dropped, design §Panel decision).
MODELS = {"claude": PANEL["A"], "gemini": PANEL["C"]}
MODEL_SEED_OFFSET = {"claude": 11, "gemini": 37}  # v1/v2/v3 convention (gpt=23 retired here)
SEED0 = 20260614

# ---- frozen design parameters (v4 design §Conditions / this run's PREREG) ----------------
# The 2x2 carried within a single arm: chronologically-latest twin x decisive-line
# text-position. CLAST = which twin owns the two LATEST rounds (R3,R4); the decisive line
# is R4. DPOS = where the decisive (R4) line sits physically.
CLAST = ["X", "Y"]                       # chronologically-latest twin
DPOS = ["late", "early"]                 # decisive (R4) line: physically last vs non-terminal
N_VARIANTS = 4                           # frozen line-orderings per (clast x dpos) cell
N_SAMPLES = 4                            # 4 description samples/pair (v4 raises power; v3 had 3)
DESCS_PER_FIG = 8                        # 8 certified = 4 samples x 2 descriptions (v3 had 6)
N_CAND = 12                              # harvest candidates per call (v3 had 8; need 8 certified)
WORD_BUDGET = 12                         # v1 director budget, unchanged
N_ROUNDS = 4                             # 4 evidence rounds per mixed record (2 X + 2 Y)
# Fresh frozen non-descriptive nonces (no v3 carryover).
NONCE = {0: "GORLAX", 1: "MIVUNT", 2: "ZEPHRO"}
# v1 figures.json content hash the design pins ("original sha256 a2709582...").
FIGURES_SHA256 = "a2709582a58e54378190b3e6e15191be4fe1f05d27c37830856f958371deb6c4"

# ---- elicitation (forced format; cap 512 so truncation is RARE, not impossible) ----------
MAX_TOKENS = 512  # a reply with finish_reason == "length" is NEVER parsed (critic blocker 2)
REASONING = {"google/": {"effort": "minimal"}}  # config/models.md caveat 1
HARD_STOP_USD = 1.50  # pre-registered hard stop on PROJECTED TOTAL billed cost (carried from v3)

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

# v4 INTRO: chronology carried by the round STAMP, NOT by line order, stated explicitly and
# NEUTRALLY (it does NOT instruct the model to weight recency — whether it spontaneously
# weights the stamp, the line order, or treats the evidence as an order-free set is exactly
# what the probe measures). Single INTRO (no fwd/rev: physical position is now a manipulated
# factor (DPOS), so v3's presentation-direction carrier is subsumed; see PREREG/README).
INTRO = (
    "Your partner referred to ONE target figure using the label \"{nonce}\" over several "
    "rounds. Here is what they said. Each line is stamped with the round it was said in "
    "(a higher round number means it was said more recently); the lines are NOT necessarily "
    "listed in round order:")

# Sterner one-label-only reminder appended on the single retry.
STERN = ("\n\nIMPORTANT: your reply must be EXACTLY ONE label from ({label_list}) -- a single "
         "token on a single line, with no other text whatsoever.")


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def load_figures():
    """The 6 frozen v1 figures, unchanged (design §Conditions). Hash-checked."""
    import hashlib
    blob = open(os.path.join(V1, "figures.json"), "rb").read()
    if hashlib.sha256(blob.rstrip(b"\n")).hexdigest() != FIGURES_SHA256:
        sys.exit("FATAL: v1 figures.json content hash mismatch — figures are not the frozen "
                 f"v1 set (expected {FIGURES_SHA256[:8]}...). Refusing to build/probe.")
    return json.loads(blob)["figures"]


def figure_pairs(figs):
    pairs = {}
    for fid, f in figs.items():
        pairs.setdefault(f["pair"], []).append(fid)
    for p in pairs.values():
        p.sort()
    return pairs


def grid_block(order, fig):
    """order: list of (label, canonical_id) pairs. v2/v3 byte-identical rendering."""
    out = []
    for label, cid in order:
        out.append(f"[{label}]")
        out.extend("  " + row for row in fig[cid]["grid"])
    return "\n".join(out)


def render_history(stamped_lines):
    """stamped_lines: list of (round_number, description) in PHYSICAL (display) order.
    Renders the v4 stamped history block. Round number carries chronology; the physical
    order of this list carries text-position. The two are independent by construction."""
    return "\n".join(f'- Round {k}: partner said "{d}" (you FOUND the target)'
                     for k, d in stamped_lines)


# ---- the pre-registered strict parse rule (carried verbatim from v3) ----------------------
LABEL_RE = re.compile(r"\bP\s*([1-6])\b", re.IGNORECASE)


def parse_forced(txt, labels):
    """(pick, parse_mode): parse_mode in {"strict", "non-strict", None}. Verbatim from v3."""
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
    """One chat completion that ALSO surfaces choices[0].finish_reason (critic blocker 2:
    a finish_reason == "length" reply is never parsed). Transport mirrored from
    lib/openrouter.call verbatim (same body incl. usage-include flag, same retry/backoff).
    Verbatim from v3 common.py."""
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


def parse_reply(r, labels):
    """Strict parse rule; a length-truncated reply is NEVER parsed (critic blocker 2)."""
    if r.get("finish_reason") == "length":
        return None, None
    return parse_forced(r.get("content"), labels)


def call_forced(model, sys_p, user, labels, label_list):
    """One forced-format call; on transport error, length-truncation, or parse-fail, ONE
    retry with the stern reminder; persistent failure -> NA. Verbatim from v3."""
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


# ---- cost ledger + pre-registered hard stop (verbatim from v3) ----------------------------
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
