#!/usr/bin/env python3
"""probe.py — the ONLY API caller for the projection trigger-inventory probe.

Run 2026-07-01-projection-trigger-inventory. For each of the 96 frozen item-conditions (prep.py)
and each panel model, sends one plain forced-choice completion — "does [target] follow from [framed
sentence]? YES / NO / UNCLEAR" — and records the raw answer. Scoring (endorsement parse, survival
rates, projection gap, verdict) lives in analyze.py; this file only collects raw traces.

Text-only, single-turn, temperature 0. No tools. gemini reasoning effort minimal (config/models.md
caveat). The system prompt never mentions presupposition / projection / the "right" answer.

FREEZE GUARD: refuses to run unless prep.py --check passes (frozen sha intact) and PREREG.md +
analyze.py exist — so items/spec cannot drift after the pre-run critic signs off.

ABORT_USD guards a runaway bill (pre-flight expectation is a few cents; see PREREG §cost).

Usage: OPENROUTER_API_KEY=... python3 probe.py [--model A|B|C] [--limit N]
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402
from prep import ITEMS, SYS, manifest_sha, FROZEN_SHA  # noqa: E402

HERE = Path(__file__).parent
RAW = HERE / "raw"
RAW.mkdir(exist_ok=True)
ABORT_USD = 1.00  # pre-flight ~few cents; hard stop well under the $2.50/run flag.


def freeze_guard():
    out = subprocess.run([sys.executable, str(HERE / "prep.py"), "--check"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        sys.exit(f"FREEZE GUARD failed:\n{out.stdout}\n{out.stderr}")
    assert manifest_sha() == FROZEN_SHA, "manifest sha drift"
    for f in ("PREREG.md", "analyze.py"):
        if not (HERE / f).exists():
            sys.exit(f"FREEZE GUARD: missing {f}")


def run_model(slot, limit=None):
    model = PANEL[slot]
    items = ITEMS[:limit] if limit else ITEMS
    is_google = model.startswith("google/")
    reasoning = {"effort": "minimal"} if is_google else None
    max_tokens = 512 if is_google else 16   # a single word; gemini needs headroom for reasoning.
    recs = []
    for it in items:
        r = call(model, SYS, it["prompt"], max_tokens=max_tokens, temperature=0,
                 reasoning=reasoning)
        content = r.get("content")
        rec = {
            "id": it["id"], "sid": it["sid"], "family": it["family"],
            "frame": it["frame"], "cancelling": it["cancelling"],
            "target_type": it["target_type"], "target": it["target"],
            "sentence": it["sentence"],
            "answer": content,
            "answer_sha": hashlib.sha256((content or "").encode()).hexdigest()[:16],
            "usage": r.get("usage", {}),
            "error": r.get("error"),
        }
        recs.append(rec)
        cost, have, miss = billed_cost([recs])
        if cost > ABORT_USD:
            sys.exit(f"ABORT: billed {cost:.4f} exceeds {ABORT_USD}")
    (RAW / f"{slot}.json").write_text(json.dumps(recs, indent=2, ensure_ascii=True) + "\n")
    cost, have, miss = billed_cost([recs])
    print(f"[{slot}] {model}: {len(recs)} items, billed ${cost:.4f} (cost on {have}, missing {miss})")
    return recs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["A", "B", "C"])
    ap.add_argument("--limit", type=int)
    args = ap.parse_args()
    freeze_guard()
    slots = [args.model] if args.model else ["A", "B", "C"]
    all_recs = []
    for slot in slots:
        recs = run_model(slot, args.limit)
        all_recs.append(recs)
        time.sleep(1)
    cost, have, miss = billed_cost(all_recs)
    print(f"TOTAL billed ${cost:.4f} (missing cost on {miss})")


if __name__ == "__main__":
    main()
