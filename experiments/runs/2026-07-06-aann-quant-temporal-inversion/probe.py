#!/usr/bin/env python3
"""AANN temporal held-out widening (v2b) — panel calls.

DO NOT RUN until PREREG is frozen (this run's PREREG-draft.md must pass the
independent pre-run critic and be committed as PREREG.md first). probe.py
also refuses to run if analyze.py is absent (pre-run critic blocker 4: the
analysis code must exist at freeze time, before any call).

THREE ARMS (pre-run critic 2026-06-13, GO after fixes), 432 calls total:
  heldout-temporal  80 items x 3 models = 240  primary 0-100 framing (P100,
                                               byte-identical to v2)
  tier0             24 pairs x 3 models =  72  fresh per-run Tier-0 forced
                                               choice (PT0, byte-identical to
                                               v2; pairs verbatim from v2)
  robustness        40 items x 3 models = 120  4-point framing (P4,
                                               byte-identical to v2) on the
                                               fixed pre-declared subsample
                                               in stimuli.json

Settings IDENTICAL to the ratified v2 instrument (per config/models.md):
temperature 0; max_tokens 64 (A, B) / 512 (C); C runs reasoning effort minimal.

Tier-0 parsing (critic blocker 1): the GATE value is the LAST standalone
A/B token (full-string parse first) — fixing v2's documented first-bare-token
defect, and matching the integer arms' last-token rule. The v2-style
FIRST-token parse is ALSO recorded per row (value_first_token) so analyze.py
can report the v2-continuity score descriptively. The retry triggers on the
gate (last-token) parse only.

Usage: python3 probe.py [--model A|B|C] [--arm heldout-temporal|tier0|robustness]
Raw JSON per (model, arm) under raw/. Idempotent: re-running skips files that
already exist. Cost: billed usage.cost summed; calls with MISSING cost are
counted and logged, never silently discarded (critic should-fix 8).
"""
import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

HERE = Path(__file__).parent
RAW = HERE / "raw"
RAW.mkdir(exist_ok=True)
STIMULI = json.load(open(HERE / "stimuli.json"))
ARMS = ["heldout-temporal", "tier0", "robustness"]

SYSTEM = "You are a careful native-speaker judge of English acceptability."
# All three prompts byte-identical to the v2 probe (instrument continuity).
P100 = ("Rate the naturalness/acceptability of the following English sentence for a native "
        "speaker, on a scale from 0 (completely unacceptable) to 100 (completely natural). "
        "Respond with ONLY the integer.\n\nSentence: {s}")
P4 = ("Rate the naturalness/acceptability of the following English sentence for a native "
      "speaker: 1 = completely unacceptable, 2 = somewhat unacceptable, 3 = somewhat "
      "acceptable, 4 = completely acceptable. Respond with ONLY the digit.\n\nSentence: {s}")
PT0 = ("Which sentence sounds more natural in English? Respond with ONLY the letter A or B."
       "\n\nA: {a}\nB: {b}")

ABORT_USD = 0.60  # PREREG single-run flag (pre-flight estimate ~ $0.15-0.30; 972 calls, ~1.5x v2b N)

SUBSET_IDS = set(STIMULI["robustness_4pt"]["ids"])
SUBSET_ITEMS = [s for s in STIMULI["items"] if s["id"] in SUBSET_IDS]
assert len(SUBSET_ITEMS) == 40, len(SUBSET_ITEMS)


def parse_int(text, lo, hi):
    """Full-string bare integer first; otherwise the LAST in-range token (v2
    pre-run critic S4: a first-token rule records a scale-echo like
    'of 0 to 100, 85' as 0 and never triggers the retry)."""
    if text is None:
        return None
    t = text.strip().rstrip(".")
    if t.isdigit() and lo <= int(t) <= hi:
        return int(t)
    found = None
    for tok in t.replace("\n", " ").split():
        tok = tok.strip(".,!:;")
        if tok.isdigit() and lo <= int(tok) <= hi:
            found = int(tok)
    return found


def parse_ab_last(text):
    """GATE parse for Tier-0 (critic blocker 1): full-string A/B first, else
    the LAST standalone A/B token — same last-token convention as parse_int,
    fixing the v2 first-bare-token defect (a preamble like 'Between A and B,
    ... B' must parse as B, and an echo must not freeze the first letter)."""
    if text is None:
        return None
    t = text.strip().upper().rstrip(".")
    if t in ("A", "B"):
        return t
    found = None
    for tok in t.replace("\n", " ").replace(":", " ").split():
        tok = tok.strip(".,!:;")
        if tok in ("A", "B"):
            found = tok
    return found


def parse_ab_first_v2(text):
    """The v2 probe's parse, verbatim semantics (FIRST A/B token): recorded
    per row as value_first_token, reported descriptively for continuity with
    the v2 Tier-0 numbers. Never gate-bearing here."""
    if text is None:
        return None
    t = text.strip().upper().rstrip(".")
    if t in ("A", "B"):
        return t
    for tok in t.replace(":", " ").split():
        if tok in ("A", "B"):
            return tok
    return None


def ask(slot, user):
    # Per-slot max_tokens (v2 pre-run critic B3): output is one integer/letter,
    # but gemini burns small caps on hidden reasoning (2026-05-28 calibration)
    # -- C gets 512 with effort minimal; A/B get 64. A cap, not a purchase.
    kwargs = {"max_tokens": 512 if slot == "C" else 64}
    if slot == "C":
        kwargs["reasoning"] = {"effort": "minimal"}
    return call(PANEL[slot], SYSTEM, user, temperature=0, **kwargs)


def tasks_for(arm):
    if arm == "heldout-temporal":
        return [(s, P100.format(s=s["sentence"]), 0, 100) for s in STIMULI["items"]]
    if arm == "robustness":
        return [(s, P4.format(s=s["sentence"]), 1, 4) for s in SUBSET_ITEMS]
    # tier0
    return [(s, PT0.format(a=s["A"], b=s["B"]), None, None) for s in STIMULI["tier0"]]


def run_arm(slot, arm, records):
    out = RAW / f"{slot}-{arm}.json"
    if out.exists():
        print(f"skip {out} (exists)")
        return
    rows = []
    tasks = tasks_for(arm)
    for i, (s, user, lo, hi) in enumerate(tasks):
        r = ask(slot, user)
        val = parse_ab_last(r["content"]) if arm == "tier0" \
            else parse_int(r["content"], lo, hi)
        if val is None and not r.get("error"):
            r = ask(slot, user)  # one verbatim retry (PREREG), then missing
            val = parse_ab_last(r["content"]) if arm == "tier0" \
                else parse_int(r["content"], lo, hi)
        row = {"id": s["id"], "arm": arm, "raw": r["content"], "value": val,
               "usage": r.get("usage"), "error": r.get("error")}
        if arm == "tier0":
            # descriptive v2-continuity parse of the SAME final response text
            row["value_first_token"] = parse_ab_first_v2(r["content"])
        rows.append(row)
        records.append(r)
        if (i + 1) % 25 == 0:
            c, _, nmiss = billed_cost([records])
            print(f"  {slot}/{arm}: {i+1}/{len(tasks)} cost so far ${c:.4f}"
                  + (f" ({nmiss} calls missing usage.cost)" if nmiss else ""),
                  flush=True)
            if c >= ABORT_USD:
                # Real abort semantics (v2 critic S2): persist as .partial
                # (analysis ignores partials) and stop the whole invocation.
                json.dump(rows, open(str(out) + ".partial", "w"), indent=1)
                print(f"ABORT: single-run flag ${ABORT_USD} reached; wrote {out}.partial",
                      flush=True)
                sys.exit(1)
        time.sleep(0.1)
    json.dump(rows, open(out, "w"), indent=1)
    miss = sum(1 for x in rows if x["value"] is None)
    print(f"{slot}/{arm}: {len(rows)} rows, {miss} missing -> {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["A", "B", "C"], default=None)
    ap.add_argument("--arm", choices=ARMS, default=None)
    args = ap.parse_args()
    if not (HERE / "PREREG.md").exists():
        sys.exit("FATAL: PREREG.md not found — the pre-registration has not been "
                 "frozen (PREREG-draft.md must pass the independent pre-run critic "
                 "and be committed as PREREG.md before any model call).")
    if not (HERE / "analyze.py").exists():
        sys.exit("FATAL: analyze.py not found — the analysis code must exist at "
                 "freeze time, before any model call (pre-run critic blocker 4); "
                 "running calls without committed analysis code is forbidden.")
    slots = [args.model] if args.model else ["A", "B", "C"]
    arms = [args.arm] if args.arm else ARMS
    records = []
    for slot in slots:
        for arm in arms:
            run_arm(slot, arm, records)
    total, _, n_missing_cost = billed_cost([records])
    print(f"TOTAL billed this invocation: ${total:.4f}")
    if n_missing_cost:
        # critic should-fix 8: never silently discard the missing-cost count
        print(f"WARNING: {n_missing_cost} call(s) reported no usage.cost — the "
              f"billed total above UNDERCOUNTS; flag in the budget ledger.")
    with open(RAW / "cost-log.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} "
                f"slots={slots} arms={arms} billed=${total:.4f} "
                f"missing_cost_calls={n_missing_cost}\n")


if __name__ == "__main__":
    main()
