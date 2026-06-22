#!/usr/bin/env python3
"""Strip corpus-bearing text from the forced-decomposition raw before committing.

The forced surface makes gpt externalize a 3-step decomposition that QUOTES / paraphrases the
marked corpus sentences (DWUG = CC BY-ND, WiC = CC BY-NC; both gitignored as recipe-not-corpus).
So the committed raw must NOT carry the verbatim model output. This rewrites each raw/*.json in
place, removing `raw` (full model output) and `final_seg` (post-FINAL text), keeping ONLY:
item_id, lemma, bridging_class, source, framing, pred/pred2, had_final_tag, human_median, error,
usage, uptake (content_chars / pre_final_chars / n_steps / completion_tokens / reasoning_tokens
-- counts only, no text).

analyze.py uses none of the removed fields, so every number stays reproducible. Run AFTER
analyze.py and BEFORE `git add`. Idempotent; skips _calib and run_summary files.
"""
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
DROP = ("raw", "final_seg")


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
            for k in DROP:
                r.pop(k, None)
        json.dump(recs, open(p, "w"), indent=1)
        n += 1
        print(f"sanitized {base} ({len(recs)} records)")
    print(f"\n{n} files sanitized (CoT/corpus-bearing fields removed; parsed + count fields kept).")


if __name__ == "__main__":
    main()
