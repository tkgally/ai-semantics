#!/usr/bin/env python3
"""AANN temporal held-out widening (v2b) — panel calls.

DO NOT RUN until PREREG is frozen (this run's PREREG-draft.md must pass the
independent pre-run critic and be renamed/committed as PREREG.md first).

Single arm: heldout-temporal, 80 items x 3 models = 240 calls, primary 0-100
framing, settings IDENTICAL to the ratified v2 instrument
(experiments/designs/aann-construction-v2.md; per-model settings per
config/models.md): temperature 0; max_tokens 64 (A, B) / 512 (C);
C runs with reasoning effort minimal.

Usage: python3 probe.py [--model A|B|C]
Raw JSON per model under raw/. Idempotent: re-running skips models whose raw
file already exists. Parsing, one-verbatim-retry, and abort semantics carried
over from the v2 probe (pre-run critic fixes S2/S4 included).
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
ARM = "heldout-temporal"

SYSTEM = "You are a careful native-speaker judge of English acceptability."
# Byte-identical to the v2 primary framing (instrument continuity).
P100 = ("Rate the naturalness/acceptability of the following English sentence for a native "
        "speaker, on a scale from 0 (completely unacceptable) to 100 (completely natural). "
        "Respond with ONLY the integer.\n\nSentence: {s}")

ABORT_USD = 0.30  # PREREG-draft single-run flag (pre-flight estimate ~ $0.04-0.09)


def parse_int(text, lo=0, hi=100):
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


def ask(slot, user):
    # Per-slot max_tokens (v2 pre-run critic B3): output is one integer, but
    # gemini burns small caps on hidden reasoning (2026-05-28 calibration) --
    # C gets 512 with effort minimal; A/B get 64. max_tokens is a cap, not a purchase.
    kwargs = {"max_tokens": 512 if slot == "C" else 64}
    if slot == "C":
        kwargs["reasoning"] = {"effort": "minimal"}
    return call(PANEL[slot], SYSTEM, user, temperature=0, **kwargs)


def run_model(slot, records):
    out = RAW / f"{slot}-{ARM}.json"
    if out.exists():
        print(f"skip {out} (exists)")
        return
    rows = []
    tasks = [(s, P100.format(s=s["sentence"])) for s in STIMULI["items"]]
    for i, (s, user) in enumerate(tasks):
        r = ask(slot, user)
        val = parse_int(r["content"])
        if val is None and not r.get("error"):
            r = ask(slot, user)  # one verbatim retry (PREREG), then missing
            val = parse_int(r["content"])
        rows.append({"id": s["id"], "arm": ARM, "raw": r["content"],
                     "value": val, "usage": r.get("usage"), "error": r.get("error")})
        records.append(r)
        if (i + 1) % 25 == 0:
            c = billed_cost([records])[0]
            print(f"  {slot}: {i+1}/{len(tasks)} cost so far ${c:.4f}", flush=True)
            if c >= ABORT_USD:
                # Real abort semantics (v2 pre-run critic S2): persist as
                # .partial (analysis ignores partials) and stop the whole
                # invocation, not just this model.
                json.dump(rows, open(str(out) + ".partial", "w"), indent=1)
                print(f"ABORT: single-run flag ${ABORT_USD} reached; wrote {out}.partial",
                      flush=True)
                sys.exit(1)
        time.sleep(0.1)
    json.dump(rows, open(out, "w"), indent=1)
    miss = sum(1 for x in rows if x["value"] is None)
    print(f"{slot}: {len(rows)} rows, {miss} missing -> {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["A", "B", "C"], default=None)
    args = ap.parse_args()
    if not (HERE / "PREREG.md").exists():
        sys.exit("FATAL: PREREG.md not found — the pre-registration has not been "
                 "frozen (PREREG-draft.md must pass the independent pre-run critic "
                 "and be committed as PREREG.md before any model call).")
    slots = [args.model] if args.model else ["A", "B", "C"]
    records = []
    for slot in slots:
        run_model(slot, records)
    total = billed_cost([records])[0]
    print(f"TOTAL billed this invocation: ${total:.4f}")
    with open(RAW / "cost-log.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} "
                f"slots={slots} billed=${total:.4f}\n")


if __name__ == "__main__":
    main()
