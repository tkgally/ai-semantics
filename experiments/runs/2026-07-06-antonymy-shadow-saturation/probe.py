#!/usr/bin/env python3
"""probe.py — panel relatum production for the A1b antonymy shadow-saturation probe.

PREREG.md is frozen; thresholds/verdict live in analyze.py, not here. This script only
elicits, parses, and records — no scoring decision is taken here.

Arms:
- neutral (frame-suppressed): all 6 relations. The 𝒮(model) that enters the PRIMARY residual.
- frame (frame-present): antonymy ONLY — the J&K symmetric contrastive scaffold
  (versus / neither-nor / from-to). Enters the frame-ablation arm only.

Usage: python3 probe.py [--model A|B|C] [--rel antonymy|...] [--arm neutral|frame]
Idempotent: skips (model, rel, arm) files that already exist under raw/.
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
ITEMS = json.load(open(HERE / "items.json"))
RELS = ITEMS["relations"]
K = 3
ABORT_USD = 2.50   # PREREG single-run flag

SYSTEM = "You are a precise lexical assistant with expert knowledge of English word relations."

GLOSS = {
    "antonymy":  'the opposite of "{c}"',
    "synonymy":  'a synonym of "{c}" (a different word meaning the same thing)',
    "hypernymy": 'a more general category that a "{c}" is a kind of',
    "hyponymy":  'a specific kind of "{c}"',
    "holonymy":  'a whole that a "{c}" is a part or member of',
    "meronymy":  'a part or member of a "{c}"',
}

NEUTRAL = ('Give up to 3 single English words, each ' + '{gloss}' +
           '. Reply with ONLY the words, comma-separated — no other text.')

# antonymy frame-present: three symmetric contrastive frames (the essay's cuing signature)
FRAME = ('Complete each phrase with a single English word that is the opposite of "{c}":\n'
         '"{c} versus ___"\n"neither {c} nor ___"\n"from {c} to ___"\n'
         'Reply with ONLY the three filler words, comma-separated — no other text.')


def parse_words(text, k=K):
    if text is None:
        return None
    t = text.strip().strip(".").lower()
    # split on commas primarily, else whitespace/newlines
    parts = [p.strip(" .,;:!?\"'()") for p in t.replace("\n", ",").split(",")]
    words = []
    for p in parts:
        p = p.strip()
        if not p or " " in p:
            continue
        if p in words:
            continue
        words.append(p)
    return words[:k] if words else None


def ask(slot, user):
    kwargs = {"max_tokens": 512 if slot == "C" else 64}
    if slot == "C":
        kwargs["reasoning"] = {"effort": "minimal"}
    return call(PANEL[slot], SYSTEM, user, temperature=0, **kwargs)


def run(slot, rel, arm, records):
    out = RAW / f"{slot}-{rel}-{arm}.json"
    if out.exists():
        print(f"skip {out} (exists)")
        return
    rows = []
    for i, it in enumerate(ITEMS["items"][rel]):
        c = it["cue"]
        if arm == "frame":
            user = FRAME.format(c=c)
        else:
            user = NEUTRAL.format(gloss=GLOSS[rel].format(c=c))
        r = ask(slot, user)
        words = parse_words(r["content"])
        if words is None and not r.get("error"):
            r = ask(slot, user)          # one verbatim retry (PREREG)
            words = parse_words(r["content"])
        rows.append({"cue": c, "rel": rel, "arm": arm, "raw": r["content"],
                     "words": words, "usage": r.get("usage"), "error": r.get("error")})
        records.append(r)
        if (i + 1) % 40 == 0:
            cst = billed_cost([records])[0]
            print(f"  {slot}/{rel}/{arm}: {i+1}/{len(ITEMS['items'][rel])} ${cst:.3f}", flush=True)
            if cst >= ABORT_USD:
                json.dump(rows, open(str(out) + ".partial", "w"), indent=1)
                print(f"ABORT ${ABORT_USD} reached; wrote {out}.partial", flush=True)
                sys.exit(1)
        time.sleep(0.05)
    json.dump(rows, open(out, "w"), indent=1)
    miss = sum(1 for x in rows if not x["words"])
    print(f"{slot}/{rel}/{arm}: {len(rows)} rows, {miss} empty -> {out}", flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["A", "B", "C"], default=None)
    ap.add_argument("--rel", choices=RELS, default=None)
    ap.add_argument("--arm", choices=["neutral", "frame"], default=None)
    args = ap.parse_args()
    slots = [args.model] if args.model else ["A", "B", "C"]
    rels = [args.rel] if args.rel else RELS
    records = []
    for slot in slots:
        for rel in rels:
            arms = ["neutral", "frame"] if rel == "antonymy" else ["neutral"]
            if args.arm:
                arms = [args.arm] if (args.arm in arms) else []
            for arm in arms:
                run(slot, rel, arm, records)
    total = billed_cost([records])[0]
    print(f"TOTAL billed this invocation: ${total:.4f}")
    with open(RAW / "cost-log.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} "
                f"slots={slots} rels={rels} billed=${total:.4f}\n")


if __name__ == "__main__":
    main()
