#!/usr/bin/env python3
"""DAIS license scout + firsthand inspection recipe (s244, 2026-07-17).

Recipe-not-corpus posture (see ../../../.gitignore DAIS block and
wiki/base/resources/dais-dative-ratings.md). This script re-downloads the DAIS
human-ratings release, verifies the pinned sha256, and regenerates the two
committed derived tables:

  - inspection_manifest.json    (summary counts + column list + sanity aggregates)
  - verb_recipient_means.csv    (200 verbs x 5 recipient conditions: mean human
                                 DOpreference — the graded human gradient a future
                                 dative probe would anchor to)

The raw 50,136-row judgment file is NEVER committed; it is mirrored to the
gitignored experiments/data/dais/ and read from there.

Source repo : https://github.com/taka-yamakoshi/neural_constructions  (branch master)
Data file   : DAIS/data/experiment_output/data_cleaned.zip  ->  data_cleaned.csv
License      : CC BY 4.0 (verified firsthand against the raw LICENSE file, 2026-07-17)
Paper        : Hawkins, Yamakoshi, Griffiths & Goldberg 2020, EMNLP pp.4653-4663,
               arXiv 2010.02375
Pinned sha256:
  data_cleaned.zip : f3860b93c6e7d5a7065ea3b7256360c8d1227112f340c790d3a00a192cc1c652
  data_cleaned.csv : 01ee1b163003e354cddf1c6c6be1b386123cbbce3424163bf198e9fbc4c251f9
"""
import csv, hashlib, json, os, statistics, subprocess, sys, zipfile
from collections import Counter, defaultdict

RAW_DIR = os.path.join(os.path.dirname(__file__), "../../data/dais")
ZIP_URL = ("https://raw.githubusercontent.com/taka-yamakoshi/neural_constructions/"
           "master/DAIS/data/experiment_output/data_cleaned.zip")
ZIP_SHA = "f3860b93c6e7d5a7065ea3b7256360c8d1227112f340c790d3a00a192cc1c652"
CSV_SHA = "01ee1b163003e354cddf1c6c6be1b386123cbbce3424163bf198e9fbc4c251f9"


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def fetch():
    os.makedirs(RAW_DIR, exist_ok=True)
    zpath = os.path.join(RAW_DIR, "data_cleaned.zip")
    if not os.path.exists(zpath):
        subprocess.run(["curl", "-sSL", "-o", zpath, ZIP_URL], check=True)
    assert sha256(zpath) == ZIP_SHA, "zip sha256 mismatch — upstream changed"
    with zipfile.ZipFile(zpath) as z:
        z.extractall(RAW_DIR)
    cpath = os.path.join(RAW_DIR, "data_cleaned.csv")
    assert sha256(cpath) == CSV_SHA, "csv sha256 mismatch"
    return cpath


def inspect(cpath):
    rows = list(csv.DictReader(open(cpath)))
    dp = [float(r["DOpreference"]) for r in rows]
    pairs = Counter((r["DOsentence"], r["PDsentence"]) for r in rows)
    byclass = defaultdict(list)
    byrec = defaultdict(list)
    grid = defaultdict(list)
    for r in rows:
        byclass[r["classification"]].append(float(r["DOpreference"]))
        byrec[r["recipient_id"]].append(float(r["DOpreference"]))
        grid[(r["verb"], r["recipient_id"])].append(float(r["DOpreference"]))
    manifest = {
        "source": ZIP_URL,
        "license": "CC BY 4.0 (verified firsthand against raw LICENSE, 2026-07-17)",
        "paper": "Hawkins, Yamakoshi, Griffiths, Goldberg 2020, EMNLP pp.4653-4663, arXiv 2010.02375",
        "zip_sha256": ZIP_SHA,
        "csv_sha256": CSV_SHA,
        "n_judgments": len(rows),
        "columns": list(rows[0].keys()),
        "n_unique_verbs": len({r["verb"] for r in rows}),
        "n_participants": len({r["participant_id"] for r in rows}),
        "n_unique_sentence_pairs": len(pairs),
        "judgments_per_pair": {"min": min(pairs.values()), "max": max(pairs.values()),
                                "mean": round(sum(pairs.values()) / len(pairs), 3)},
        "DOpreference": {"scale": "0-100 continuous slider; 0=strong PD/PO, 100=strong DO, 50=about the same",
                          "min": min(dp), "max": max(dp), "mean": round(statistics.mean(dp), 3),
                          "median": statistics.median(dp)},
        "recipient_conditions": sorted({r["recipient_id"] for r in rows}),
        "theme_types": sorted({r["theme_type"] for r in rows}),
        "classification_counts": dict(Counter(r["classification"] for r in rows)),
        "DOpref_by_classification": {k: round(statistics.mean(v), 3) for k, v in byclass.items()},
        "DOpref_by_recipient_condition": {k: round(statistics.mean(v), 3) for k, v in byrec.items()},
    }
    here = os.path.dirname(__file__)
    json.dump(manifest, open(os.path.join(here, "inspection_manifest.json"), "w"), indent=2)
    with open(os.path.join(here, "verb_recipient_means.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["verb", "recipient_condition", "mean_DOpreference", "n"])
        for (v, rc), xs in sorted(grid.items()):
            w.writerow([v, rc, round(statistics.mean(xs), 3), len(xs)])
    print(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    inspect(fetch())
