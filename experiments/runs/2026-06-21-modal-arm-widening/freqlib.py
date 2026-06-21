#!/usr/bin/env python3
"""freqlib.py -- SUBTLEX-US Lg10WF lookup for the function-word-vs-content-swap build.

The full 74,286-word list is gitignored (recipe-not-corpus); re-fetch via
experiments/data/subtlex-us/prep.py (URL + sha256 in its docstring). This module is the
read side: case-insensitive Lg10WF lookup (max-freq form per lowercased token), used by
build.py (frequency-matching the content controls) and certify.py (the shortcut readers).

Resource: wiki/base/resources/subtlex-us-frequency.md  (Lg10WF = log10(FREQcount+1)).
Decision (yardstick): wiki/decisions/resolved/function-word-anchor-design.md.
"""
import csv
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.abspath(os.path.join(
    HERE, "..", "..", "data", "subtlex-us", "SUBTLEXus74286wordstextversion.txt"))
SHA256 = "c5f86f065fc5d057fbf366433b8c5ca550aa7c24e128362dea4394f2b29c86e4"

_AGG = None


def _load():
    global _AGG
    if _AGG is not None:
        return _AGG
    if not os.path.exists(CORPUS):
        sys.exit(f"missing {CORPUS}; re-fetch via experiments/data/subtlex-us/prep.py "
                 "(gitignored recipe-not-corpus list).")
    h = hashlib.sha256(open(CORPUS, "rb").read()).hexdigest()
    if h != SHA256:
        sys.exit(f"SUBTLEX sha mismatch: {h} != {SHA256} (upstream drifted; do NOT use).")
    agg = {}
    with open(CORPUS, encoding="latin-1") as f:
        r = csv.reader(f, delimiter="\t")
        next(r)
        for row in r:
            if len(row) < 7:
                continue
            w, lg = row[0], float(row[6])
            wl = w.lower()
            if wl not in agg or lg > agg[wl]:
                agg[wl] = lg
    _AGG = agg
    return agg


def lg10wf(word):
    """Case-insensitive Lg10WF (max-freq cased form). None if not in the norm."""
    return _load().get(word.lower())


def require(word):
    v = lg10wf(word)
    if v is None:
        sys.exit(f"word {word!r} not in SUBTLEX-US norm")
    return v


if __name__ == "__main__":
    for w in sys.argv[1:]:
        print(f"{w}\t{lg10wf(w)}")
