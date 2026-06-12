#!/usr/bin/env python3
"""AANN behavioral probe v2 — panel calls. PREREG.md is frozen; do not edit thresholds here.

Usage: python3 probe.py [--model A|B|C] [--arm anchored|robustness|heldout|tier0]
Defaults to all models, all arms. Raw JSON per (model, arm) under raw/.
Idempotent: re-running skips (model, arm) files that already exist.
"""
import argparse, json, os, sys, time
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

HERE = Path(__file__).parent
RAW = HERE / "raw"
RAW.mkdir(exist_ok=True)
STIMULI = json.load(open(HERE / "stimuli.json"))

SYSTEM = "You are a careful native-speaker judge of English acceptability."
P100 = ("Rate the naturalness/acceptability of the following English sentence for a native "
        "speaker, on a scale from 0 (completely unacceptable) to 100 (completely natural). "
        "Respond with ONLY the integer.\n\nSentence: {s}")
P4 = ("Rate the naturalness/acceptability of the following English sentence for a native "
      "speaker: 1 = completely unacceptable, 2 = somewhat unacceptable, 3 = somewhat "
      "acceptable, 4 = completely acceptable. Respond with ONLY the digit.\n\nSentence: {s}")
PT0 = ("Which sentence sounds more natural in English? Respond with ONLY the letter A or B."
       "\n\nA: {a}\nB: {b}")

ABORT_USD = 2.50  # PREREG single-run flag


def parse_int(text, lo, hi):
    if text is None:
        return None
    t = text.strip().rstrip(".")
    for tok in t.replace("\n", " ").split():
        tok = tok.strip(".,!")
        if tok.isdigit() and lo <= int(tok) <= hi:
            return int(tok)
    return None


def parse_ab(text):
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
    kwargs = {"max_tokens": 16}
    if slot == "C":
        kwargs["reasoning"] = {"effort": "minimal"}
    return call(PANEL[slot], SYSTEM, user, temperature=0, **kwargs)


def run_arm(slot, arm, records):
    out = RAW / f"{slot}-{arm}.json"
    if out.exists():
        print(f"skip {out} (exists)")
        return []
    rows = []
    if arm == "anchored":
        tasks = [(s, P100.format(s=s["sentence"]), 0, 100) for s in STIMULI["anchored"]]
    elif arm == "robustness":
        tasks = [(s, P4.format(s=s["sentence"]), 1, 4)
                 for s in STIMULI["anchored"] if s["robustness_4pt"]]
    elif arm == "heldout":
        tasks = [(s, P100.format(s=s["sentence"]), 0, 100) for s in STIMULI["held_out"]]
    else:  # tier0
        tasks = [(s, PT0.format(a=s["A"], b=s["B"]), None, None) for s in STIMULI["tier0"]]
    for i, (s, user, lo, hi) in enumerate(tasks):
        r = ask(slot, user)
        val = parse_ab(r["content"]) if arm == "tier0" else parse_int(r["content"], lo, hi)
        if val is None and not r.get("error"):
            r = ask(slot, user)  # one verbatim retry (PREREG)
            val = parse_ab(r["content"]) if arm == "tier0" else parse_int(r["content"], lo, hi)
        rows.append({"id": s["id"], "arm": arm, "raw": r["content"],
                     "value": val, "usage": r.get("usage"), "error": r.get("error")})
        records.append(r)
        if (i + 1) % 50 == 0:
            c = billed_cost(records)
            print(f"  {slot}/{arm}: {i+1}/{len(tasks)} cost so far ${c:.3f}", flush=True)
            if c >= ABORT_USD:
                print("ABORT: single-run flag reached", flush=True)
                break
        time.sleep(0.1)
    json.dump(rows, open(out, "w"), indent=1)
    miss = sum(1 for x in rows if x["value"] is None)
    print(f"{slot}/{arm}: {len(rows)} rows, {miss} missing -> {out}")
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["A", "B", "C"], default=None)
    ap.add_argument("--arm", choices=["anchored", "robustness", "heldout", "tier0"], default=None)
    args = ap.parse_args()
    slots = [args.model] if args.model else ["A", "B", "C"]
    arms = [args.arm] if args.arm else ["anchored", "robustness", "heldout", "tier0"]
    records = []
    for slot in slots:
        for arm in arms:
            run_arm(slot, arm, records)
    total = billed_cost(records)
    print(f"TOTAL billed this invocation: ${total:.4f}")
    with open(RAW / "cost-log.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} "
                f"slots={slots} arms={arms} billed=${total:.4f}\n")


if __name__ == "__main__":
    main()
