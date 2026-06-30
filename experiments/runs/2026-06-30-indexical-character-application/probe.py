#!/usr/bin/env python3
"""probe.py — the ONLY API caller for the indexical character-application probe.

For each of the 40 frozen items (prep.py) and each panel model, sends a fixed system prompt +
the item's described context and one resolution question, and records the model's FINAL answer.
The model is asked to resolve a single indexical (its Kaplanian CONTENT) against a DESCRIBED
origo. Scoring is in analyze.py (substring-accept against the frozen key); this file only
collects raw answers.

FREEZE GUARD: refuses to run unless prep.py --check passes (frozen manifest sha intact) and
PREREG.md + analyze.py exist. So the item set / verdict map cannot have drifted after the
pre-run critic signed off.

Settings: temperature 0; brief reasoning allowed, answer ends in a marked "FINAL:" line; gemini
reasoning effort minimal (config/models.md caveat). Pre-flight estimate well under the $2.50
single-run flag (see PREREG §cost); ABORT_USD guards a runaway bill.

Usage: OPENROUTER_API_KEY=... python3 probe.py [--model A|B|C] [--limit N]
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402
from prep import ITEMS, manifest_sha, FROZEN_SHA  # noqa: E402

HERE = Path(__file__).parent
RAW = HERE / "raw"
RAW.mkdir(exist_ok=True)
ABORT_USD = 1.50  # pre-flight ~$0.3-0.7 billed expectation; hard stop well under $2.50/run flag.

SYS = (
    "You resolve indexical and deictic expressions (such as 'I', 'you', 'here', 'now', "
    "'today', 'tomorrow', 'yesterday') to what they pick out in the situation described in the "
    "text. Use ONLY the situation as described. You may think briefly, then end your reply with "
    "a single final line in exactly this format:\n"
    "FINAL: <your answer>\n"
    "For a person, give the name. For a place, give the place name. For a date, give it as "
    "YYYY-MM-DD. Put only the answer after 'FINAL:'."
)


def parse_final(text):
    """Return (answer, parse_mode). Prefer the last 'FINAL:' line; else fall back to last line."""
    if not text:
        return "", "empty"
    matches = re.findall(r"FINAL:\s*(.+)", text, flags=re.IGNORECASE)
    if matches:
        return matches[-1].strip(), "final"
    # fallback: last non-empty line
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    return (lines[-1] if lines else text.strip()), "fallback"


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
    max_tokens = 4096 if is_google else 256
    recs = []
    for it in items:
        user = it["context"] + "\n\nQuestion: " + it["question"]
        r = call(model, SYS, user, max_tokens=max_tokens, temperature=0, reasoning=reasoning)
        content = r.get("content")
        ans, mode = parse_final(content or "")
        recs.append({
            "id": it["id"], "cond": it["cond"], "ind": it["ind"], "atype": it["atype"],
            "accept": it["accept"], "answer": ans, "parse_mode": mode,
            "content_sha": hashlib.sha256((content or "").encode()).hexdigest()[:16],
            "content_len": len(content or ""),
            "usage": r.get("usage", {}), "error": r.get("error"),
        })
        cost, have, miss = billed_cost([recs])
        if cost > ABORT_USD:
            sys.exit(f"ABORT: billed {cost:.4f} exceeds {ABORT_USD}")
    (RAW / f"{slot}.json").write_text(json.dumps(recs, indent=2, ensure_ascii=True) + "\n")
    cost, have, miss = billed_cost([recs])
    print(f"[{slot}] {model}: {len(recs)} items, billed ${cost:.4f} "
          f"(cost on {have}, missing {miss})")
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
        all_recs.append(run_model(slot, args.limit))
        time.sleep(1)
    cost, have, miss = billed_cost(all_recs)
    print(f"TOTAL billed ${cost:.4f} over {sum(len(r) for r in all_recs)} calls "
          f"(missing cost on {miss})")


if __name__ == "__main__":
    main()
