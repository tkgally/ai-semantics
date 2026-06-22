#!/usr/bin/env python3
"""Map the FROZEN WiC clear-pole manifest to local full text (recipe-not-corpus).

WHY THIS EXISTS (run session 2026-06-22 fix)
--------------------------------------------
prep_wic.py SELECTS the 20+20 clear-pole supplement by seeding a PRNG with
`(SEED, gold).__hash__()`. Python salts str/tuple hashing per process
(PYTHONHASHSEED is random unless pinned), so re-running prep_wic.py on a fresh
clone selects a DIFFERENT 40 items than the committed, frozen manifest
(`wic_poles.csv`, sha256 b8b1a7aa..., frozen session 76). The selection routine is
therefore NOT reproducible, and prep_wic.py overwrites the committed manifest with a
new selection on every run — a freeze-integrity defect.

THE FIX (this script): treat the COMMITTED MANIFEST as the authoritative freeze (it
records the exact `wic_line` of each frozen pole item, plus its gold/pole), and map
THOSE EXACT lines to their sentences + target spans. This is the recipe-not-corpus
pattern done right: the frozen manifest says WHICH items; this script only fetches
their text. It does NOT re-select, so it is fully reproducible against the committed
manifest. The WiC archive is re-fetched/located the same way prep_wic.py does
(CC BY-NC; gitignored data area); the token->char span recovery
(`token_char_span`) is copied verbatim from prep_wic.py so the SAME spans are used.

The WiC poles supplement the TWO CLEAR POLES ONLY (clear-same = gold T, clear-
different = gold F), never the bridging stratum (anchor decision condition 1). Each
item's class is fixed by its WiC gold label, so which items are frozen does not enter
any verdict about bridging — it only gives the clear-class precondition more mass.
human_median is the NOMINAL pole label (4.0 / 1.0), NOT a rating; human_n is null.

Run: python3 map_wic_fulltext.py   (re-fetches/locates WiC via prep_wic helpers; no API)
"""
import csv
import os

import prep_wic  # reuse ensure_wic / load_train / token_char_span verbatim

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(HERE, "wic_poles.csv")
import json  # noqa: E402

NOMINAL_MEDIAN = prep_wic.NOMINAL_MEDIAN
FULLTEXT = prep_wic.FULLTEXT


def main():
    extract, zip_sha = prep_wic.ensure_wic()
    train = prep_wic.load_train(extract)
    by_line = {it["wic_line"]: it for it in train}

    with open(MANIFEST, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print(f"frozen manifest rows: {len(rows)}")

    fulltext_rows, failures = [], []
    for r in rows:
        line = int(r["wic_line"])
        it = by_line.get(line)
        if it is None:
            failures.append((r["item_id"], line, "wic_line not found in train split"))
            continue
        # sanity: the frozen manifest's target/gold must match the live line
        if it["target"] != r["target"] or it["gold"] != r["gold"]:
            failures.append((r["item_id"], line,
                             f"mismatch: manifest {r['target']}/{r['gold']} "
                             f"vs live {it['target']}/{it['gold']}"))
            continue
        g1 = prep_wic.token_char_span(it["ctx1"], it["idx1"])
        g2 = prep_wic.token_char_span(it["ctx2"], it["idx2"])
        if g1 is None or g2 is None:
            failures.append((r["item_id"], line, "token offset unrecoverable"))
            continue
        pole = r["pole"]
        fulltext_rows.append({
            "item_id": r["item_id"], "lemma": it["target"], "bridging_class": pole,
            "ctx1": it["ctx1"], "span1": [g1[0], g1[1]], "surf1": g1[2],
            "ctx2": it["ctx2"], "span2": [g2[0], g2[1]], "surf2": g2[2],
            "human_median": NOMINAL_MEDIAN[pole], "human_n": None,
        })

    with open(FULLTEXT, "w", encoding="utf-8") as f:
        for rec in fulltext_rows:
            f.write(json.dumps(rec) + "\n")

    print(f"mapped {len(fulltext_rows)} / {len(rows)} frozen WiC poles -> {FULLTEXT}")
    if failures:
        print(f"{len(failures)} FAILED:")
        for iid, line, why in failures:
            print(f"  {iid} [line {line}]: {why}")
    else:
        print("all frozen WiC poles mapped (no failures).")
    print(f"WiC archive sha256 (recorded): {zip_sha}")
    return {"mapped": len(fulltext_rows), "total": len(rows),
            "failures": failures, "zip_sha256": zip_sha}


if __name__ == "__main__":
    main()
