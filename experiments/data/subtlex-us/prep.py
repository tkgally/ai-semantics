#!/usr/bin/env python3
"""SUBTLEX-US frequency-norm fetch + derive recipe (recipe-not-corpus).

The full 74,286-word list is gitignored; this script is the committed, reproducible
recipe that (1) documents the download + sha256 pin, and (2) derives the small,
committed seed-frequency table the function-word probe build session starts from.

Resource page: wiki/base/resources/subtlex-us-frequency.md
Decision (yardstick): wiki/decisions/resolved/function-word-anchor-design.md (Q1 norm)

Download (verified 2026-06-21):
    https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus/subtlexus2.zip
    -> SUBTLEXus74286wordstextversion.txt
    sha256 = c5f86f065fc5d057fbf366433b8c5ca550aa7c24e128362dea4394f2b29c86e4

Columns (tab-separated): Word  FREQcount  CDcount  FREQlow  Cdlow  SUBTLWF  Lg10WF  SUBTLCD  Lg10CD
  FREQcount = raw count in the 51M-word subtitle corpus
  Lg10WF    = log10(FREQcount+1)  -- the matching variable the probe uses
  SUBTLWF   = frequency per million words

Citation: Brysbaert, M., & New, B. (2009). Moving beyond Kucera and Francis: A critical
evaluation of current word frequency norms and the introduction of a new and improved
word frequency measure for American English. Behavior Research Methods, 41(4), 977-990.

NOTE ON SCOPE: this script ONLY emits the seed frequencies + a *candidate* content-word
pool. It does NOT freeze or select the probe's items -- that is the build session's job,
under an independent pre-run critic, per the resolved decision. The candidate pool is a
convenience, explicitly not the frozen set.
"""
import csv
import hashlib
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "SUBTLEXus74286wordstextversion.txt")
SHA256 = "c5f86f065fc5d057fbf366433b8c5ca550aa7c24e128362dea4394f2b29c86e4"
OUT = os.path.join(HERE, "function-word-seed-frequencies.csv")

# The function-word swap pairs the conjecture/decision name (the -> a; will -> would;
# because -> although; some -> every). Each pair is a swap-OUT / swap-IN.
FUNCTION_PAIRS = [
    ("the", "a", "determiner: definite -> indefinite"),
    ("will", "would", "modal: future -> conditional/irrealis"),
    ("because", "although", "subordinator: causal -> concessive"),
    ("some", "every", "quantifier: existential -> universal"),
]

# A closed-class stoplist used ONLY to keep the candidate content pool open-class.
# (Not a linguistic claim about the function/content boundary -- a convenience filter.)
CLOSED_CLASS = set("""
the a an this that these those some any every each all both either neither no none
i you he she it we they me him her us them my your his its our their mine yours hers ours theirs
am is are was were be been being do does did doing have has had having
will would shall should can could may might must ought need dare
to of in on at by for with from into onto upon over under above below between among through
during before after since until till about against around as than then so such
and or but nor yet because although though while whereas if unless whether
not no nor very too just only even still also again here there where when why how what which who whom whose
one two three four five six seven eight nine ten
""".split())


def load(path):
    rows = []
    with open(path, encoding="latin-1") as f:
        header = f.readline().rstrip("\n").split("\t")
        wi, fi, li = header.index("Word"), header.index("FREQcount"), header.index("Lg10WF")
        for line in f:
            p = line.rstrip("\n").split("\t")
            if len(p) <= li:
                continue
            rows.append((p[wi], int(p[fi]), float(p[li])))
    return rows


def check_sha(path):
    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    if h != SHA256:
        sys.exit(f"sha256 mismatch: got {h}, expected {SHA256}")
    return h


def main():
    if not os.path.exists(CORPUS):
        sys.exit(f"missing {CORPUS}; download subtlexus2.zip per the docstring first.")
    check_sha(CORPUS)
    rows = load(CORPUS)
    by_word = {w.lower(): (w, fc, lg) for (w, fc, lg) in rows}

    out = []
    # 1) the function-word swap targets + within-pair log-frequency gaps
    for a, b, gloss in FUNCTION_PAIRS:
        ra, rb = by_word[a], by_word[b]
        gap = abs(ra[2] - rb[2])
        out.append(dict(role="function-swap-out", word=a, freqcount=ra[1], lg10wf=ra[2],
                        pair=f"{a}->{b}", within_pair_lg10_gap=round(gap, 4), note=gloss))
        out.append(dict(role="function-swap-in", word=b, freqcount=rb[1], lg10wf=rb[2],
                        pair=f"{a}->{b}", within_pair_lg10_gap=round(gap, 4), note=gloss))

    # 2) candidate open-class content controls within +/-0.10 Lg10WF of each mid-band
    #    function word (the/a are too high-frequency to match an open-class word, so the
    #    band is anchored on would/some/every/because). Candidates are sorted by frequency
    #    proximity; the build session does the certified final selection, NOT this script.
    anchors = [w for w in ("would", "some", "every", "because")]
    for anc in anchors:
        target_lg = by_word[anc][2]
        cands = []
        for (w, fc, lg) in rows:
            wl = w.lower()
            if wl in CLOSED_CLASS or not w.isalpha() or len(w) < 2:
                continue
            if abs(lg - target_lg) <= 0.10:
                cands.append((abs(lg - target_lg), w, fc, lg))
        cands.sort()
        for d, w, fc, lg in cands[:12]:
            out.append(dict(role="content-candidate", word=w, freqcount=fc, lg10wf=lg,
                            pair=f"~{anc}", within_pair_lg10_gap=round(d, 4),
                            note=f"open-class candidate within 0.10 Lg10WF of '{anc}' (NOT frozen)"))

    with open(OUT, "w", newline="") as f:
        wtr = csv.DictWriter(f, fieldnames=["role", "word", "freqcount", "lg10wf",
                                            "pair", "within_pair_lg10_gap", "note"])
        wtr.writeheader()
        for r in out:
            wtr.writerow(r)
    print(f"wrote {OUT} ({len(out)} rows); corpus sha256 OK ({SHA256[:12]}...)")


if __name__ == "__main__":
    main()
