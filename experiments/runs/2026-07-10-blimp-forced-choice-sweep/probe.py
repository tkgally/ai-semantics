#!/usr/bin/env python3
"""probe.py — behavioral 2AFC forced-choice over the frozen BLiMP subsample (A3b, s205, Q2-A).

PREREG.md is frozen BEFORE this runs; all thresholds/verdicts live in analyze.py. This script only
elicits, parses, and records — no scoring decision is taken here.

Q2-A: for each minimal pair, present the two sentences as "Sentence 1 / Sentence 2" and ask which is the
more grammatically acceptable sentence of standard written English (answer 1 or 2). Run BOTH presentation
orders per pair (good-first and good-second) to net out position bias; the order-flip rate is a
diagnostic. A pick is CORRECT if the model selects sentence_good.

Usage: python3 probe.py --model A|B|C        (one model over all 40 paradigms; idempotent per paradigm)
Idempotent: skips raw/{model}-{uid}.json files that already exist.
"""
import argparse, json, os, re, sys, time
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

HERE = Path(__file__).parent
RAW = HERE / "raw"
RAW.mkdir(exist_ok=True)
ITEMS = json.load(open(HERE / "items.json"))
PARADIGMS = [p["uid"] for p in ITEMS["paradigms"]]
ABORT_USD = 1.60      # per-model hard abort (design est: claude ~$0.5, gpt ~$0.1, gemini wildcard)

SYSTEM = "You are a careful judge of English grammatical acceptability."

PROMPT = ('Which of these two sentences is the more grammatically acceptable sentence of standard '
          'written English?\n\nSentence 1: {s1}\nSentence 2: {s2}\n\n'
          'Answer with ONLY the single digit 1 or 2 — no other text.')


def parse_choice(text):
    """Return 1 or 2 (the chosen sentence number), or None."""
    if text is None:
        return None
    t = text.strip()
    if t[:1] in ("1", "2"):
        return int(t[:1])
    m = re.search(r"\b([12])\b", t)
    if m:
        return int(m.group(1))
    # last-resort: "sentence one/two", "first/second"
    tl = t.lower()
    if "sentence 1" in tl or "first" in tl or " one" in tl:
        return 1
    if "sentence 2" in tl or "second" in tl or " two" in tl:
        return 2
    return None


def ask(slot, user):
    if slot == "C":  # google: suppress reasoning tokens, small cap (forced-choice = one digit)
        return call(PANEL[slot], SYSTEM, user, max_tokens=128, temperature=0,
                    reasoning={"effort": "minimal"})
    return call(PANEL[slot], SYSTEM, user, max_tokens=16, temperature=0)


def run_paradigm(slot, uid, records):
    out = RAW / f"{slot}-{uid}.json"
    if out.exists():
        print(f"skip {out} (exists)", flush=True)
        return
    pairs = ITEMS["items"][uid]
    rows = []
    for p in pairs:
        good, bad = p["good"], p["bad"]
        for order in ("gf", "gs"):          # good-first, good-second
            if order == "gf":
                s1, s2, good_pos = good, bad, 1
            else:
                s1, s2, good_pos = bad, good, 2
            r = ask(slot, PROMPT.format(s1=s1, s2=s2))
            choice = parse_choice(r["content"])
            if choice is None and not r.get("error"):
                r = ask(slot, PROMPT.format(s1=s1, s2=s2))   # one verbatim retry
                choice = parse_choice(r["content"])
            rows.append({"uid": uid, "pairID": p["pairID"], "order": order,
                         "good_pos": good_pos, "choice": choice,
                         "correct": (choice == good_pos) if choice is not None else None,
                         "raw": r["content"], "usage": r.get("usage"), "error": r.get("error")})
            records.append(r)
            time.sleep(0.03)
    cst = billed_cost([records])[0]
    json.dump(rows, open(out, "w"), indent=1)
    miss = sum(1 for x in rows if x["choice"] is None)
    print(f"{slot}/{uid}: {len(rows)} calls, {miss} unparsed -> {out}  cum ${cst:.3f}", flush=True)
    if cst >= ABORT_USD:
        print(f"ABORT ${ABORT_USD} reached (cum ${cst:.3f}); stopping.", flush=True)
        sys.exit(2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["A", "B", "C"], required=True)
    args = ap.parse_args()
    records = []
    for uid in PARADIGMS:
        run_paradigm(args.model, uid, records)
    total = billed_cost([records])[0]
    print(f"TOTAL billed this invocation ({args.model}): ${total:.4f}", flush=True)
    with open(RAW / "cost-log.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} model={args.model} "
                f"billed=${total:.4f}\n")
    (RAW / f".done-{args.model}").write_text("done\n")


if __name__ == "__main__":
    main()
