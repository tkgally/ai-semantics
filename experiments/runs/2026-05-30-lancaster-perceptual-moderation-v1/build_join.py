#!/usr/bin/env python3
"""Build the frozen Lancaster-perceptual join table for the moderation re-analysis.

Reads:
  - experiments/data/lancaster/Lancaster_sensorimotor_norms_for_39707_words.csv
    (gitignored; CC BY 4.0; OSF node rwhs6 file 48wsc;
     sha256 445d363fb1f9f3e50b86d88e2f46cdc9a22b5dd8a713ce4e7be2a773d57f43c5)
  - the lexical-v1 manifest (the 43 DWUG EN lemmas) — only to know which lemmas to look up.

Emits (committed):
  - lemma_perceptual.csv : one row per DWUG EN lemma with its Lancaster scores.

The join is by the POS-stripped lemma surface, upper-cased, matched against the
Lancaster `Word` column. No corpus text, no model output — a tiny derived extract of
a CC BY 4.0 human-rated resource (attributed in the run record), not redistribution.
"""
import csv, os, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LANC = os.path.join(ROOT, "experiments/data/lancaster/Lancaster_sensorimotor_norms_for_39707_words.csv")
MANIFEST = os.path.join(ROOT, "experiments/runs/2026-05-30-lexical-sense-gradience-probe-v1/manifest.csv")
OUT = os.path.join(HERE, "lemma_perceptual.csv")

# columns we carry from Lancaster (mean perceptual/action strengths + derived summaries)
COLS = [
    "Max_strength.perceptual", "Minkowski3.perceptual", "Visual.mean", "Haptic.mean",
    "Auditory.mean", "Max_strength.sensorimotor", "Dominant.perceptual",
    "Percent_known.perceptual",
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    # lemmas present in the frozen lexical-v1 manifest
    lemmas = sorted({r["lemma"] for r in csv.DictReader(open(MANIFEST, newline=""))})
    base = {l: l.rsplit("_", 1)[0].upper() for l in lemmas}

    norms = {}
    with open(LANC, newline="") as f:
        for row in csv.DictReader(f):
            w = row["Word"].strip().upper()
            norms[w] = row

    rows = []
    for lem in lemmas:
        w = base[lem]
        n = norms.get(w)
        if n is None:
            rows.append({"lemma": lem, "word": w.lower(), "covered": 0,
                         **{c: "" for c in COLS}})
        else:
            rows.append({"lemma": lem, "word": w.lower(), "covered": 1,
                         **{c: n[c] for c in COLS}})

    with open(OUT, "w", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=["lemma", "word", "covered"] + COLS)
        wr.writeheader()
        wr.writerows(rows)

    cov = sum(r["covered"] for r in rows)
    print(f"lemmas: {len(rows)}  covered by Lancaster: {cov}  uncovered: "
          f"{[r['lemma'] for r in rows if not r['covered']]}")
    print("Lancaster CSV sha256:", sha256(LANC))
    print("manifest    sha256:", sha256(MANIFEST))
    print("wrote", OUT, "sha256:", sha256(OUT))


if __name__ == "__main__":
    main()
