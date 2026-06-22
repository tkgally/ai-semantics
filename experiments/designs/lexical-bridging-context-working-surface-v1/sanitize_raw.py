#!/usr/bin/env python3
"""Strip corpus-bearing text from the working-surface raw outputs before committing.

WHY: unlike v1 (short single-label outputs), this variant's model outputs are full
chain-of-thought on a working surface, and that CoT may QUOTE the marked corpus
sentences (DWUG = CC BY-ND, WiC = CC BY-NC; both gitignored as recipe-not-corpus).
So the committed raw must NOT carry the verbatim CoT. This script rewrites each
raw/*.json in place, removing the `raw` (full model output) and `final_seg`
(post-FINAL text) fields and the a_forced `raws` list, keeping ONLY: item_id,
lemma, bridging_class, source, framing, pred/pred2, had_final_tag, human_median,
error, usage, uptake (and a_forced picks/had_final_tag/uptake_list/usage_list).

The analysis (analyze.py) uses none of the removed fields, so reproducibility of
every number is preserved. Run AFTER analyze.py (which may want nothing extra) and
BEFORE `git add`.

Run: python3 sanitize_raw.py    (idempotent; skips _calib files, which are not committed)
"""
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
DROP_SINGLE = ("raw", "final_seg")
DROP_A = ("raws",)


def main():
    n = 0
    for p in sorted(glob.glob(os.path.join(RAW, "*.json"))):
        base = os.path.basename(p)
        if "_calib" in base or base.startswith("run_summary"):
            continue
        recs = json.load(open(p, encoding="utf-8"))
        if not isinstance(recs, list):
            continue
        for r in recs:
            for k in DROP_SINGLE:
                r.pop(k, None)
            for k in DROP_A:
                r.pop(k, None)
        json.dump(recs, open(p, "w"), indent=1)
        n += 1
        print(f"sanitized {base} ({len(recs)} records)")
    print(f"\n{n} files sanitized (CoT/corpus-bearing fields removed; parsed fields kept).")


if __name__ == "__main__":
    main()
