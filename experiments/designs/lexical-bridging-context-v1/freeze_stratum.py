#!/usr/bin/env python3
"""freeze_stratum.py — freeze the candidate bridging-context stratum for the
lexical bridging-context probe (v1), deterministically, from the already-committed
v1 manifest.

GROUNDWORK ONLY. This script runs NO model calls and makes NO claim about LLM
behavior. It reads the v1 within-period DWUG manifest, applies the binding
>=3-rater floor, assigns the three frozen item classes, writes stratum.csv
(manifest-derived columns only — NO corpus text, matching the v1 manifest's
CC BY-ND license posture), and prints per-class counts + lemma coverage +
spread distribution + a sha256 of the stratum file.

Binding conditions encoded here (from the two ratified decisions):
  - decisions/resolved/lexical-bridging-context-anchor.md
  - decisions/resolved/lexical-bridging-context-operationalization.md

Class definitions (frozen, on the rounded human DURel median):
  clear-same      : human_median >= 3.5   (DURel ~ Identical / Closely-Related top)
  bridging        : 1.5 < human_median < 3.5  (DURel 2-3 mid-scale, usage-similarity midpoint)
  clear-different : human_median <= 1.5   (DURel 1, Unrelated)

Rater floor (binding): human_n >= 3. The half-integer 2-rater levels are NOT
reliable graded gold (v1 caveat: 151/200 pairs rest on 2 annotators), so only
pairs with >=3 annotator judgments may enter any class.

Within-period: the source manifest is ALREADY within-period only. v1's
build_items.py skipped any pair whose two usages came from different DWUG
groupings (`ux["grouping"] != uy["grouping"] -> continue  # Q4 synchronic`),
and the manifest `period` column records the single shared period. So no
cross-period filtering is needed here; this script asserts the manifest is
within-period (single period per row) and records it.

LABEL DISCIPLINE (binding): a DWUG mid-scale pair is a HUMAN-RATED
USAGE-SIMILARITY midpoint, NOT a certified within-sense bridge. "bridging"
names the class being probed, never a certification that two senses co-occur.

No network, no model calls, deterministic.
"""

import csv
import hashlib
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
MANIFEST = os.path.join(
    REPO,
    "experiments",
    "runs",
    "2026-05-30-lexical-sense-gradience-probe-v1",
    "manifest.csv",
)
STRATUM_CSV = os.path.join(HERE, "stratum.csv")
STRATUM_SHA = os.path.join(HERE, "stratum.sha256")

RATER_FLOOR = 3  # human_n >= 3 (binding)

# manifest-derived columns only — NO corpus text (CC BY-ND posture)
OUT_COLS = [
    "item_id",
    "lemma",
    "pos",
    "period",
    "id1",
    "id2",
    "human_median",
    "human_mean",
    "human_n",
    "human_spread",
    "overlap_jaccard",
    "overlap_tokenf1",
    "bridging_class",
]


def classify(median: float) -> str:
    """Frozen class assignment on the human DURel median."""
    if median >= 3.5:
        return "clear-same"
    if median <= 1.5:
        return "clear-different"
    return "bridging"


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    if not os.path.exists(MANIFEST):
        sys.stderr.write(f"ERROR: source manifest not found: {MANIFEST}\n")
        return 1

    rows = []
    with open(MANIFEST, newline="") as f:
        for r in csv.DictReader(f):
            rows.append(r)

    # --- within-period assertion (manifest is single-period per row by construction) ---
    # each row carries exactly one `period` value; v1 enforced within-period at build.
    bad = [r for r in rows if r["period"] not in ("1", "2")]
    if bad:
        sys.stderr.write(
            f"ERROR: {len(bad)} rows carry an unexpected period value; "
            "manifest within-period invariant violated.\n"
        )
        return 1

    # --- rater floor + class assignment ---
    kept = []
    dropped_below_floor = 0
    for r in rows:
        if int(r["human_n"]) < RATER_FLOOR:
            dropped_below_floor += 1
            continue
        cls = classify(float(r["human_median"]))
        out = {c: r[c] for c in OUT_COLS if c != "bridging_class"}
        out["bridging_class"] = cls
        kept.append(out)

    # deterministic order: by item_id
    kept.sort(key=lambda d: d["item_id"])

    with open(STRATUM_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=OUT_COLS)
        w.writeheader()
        for d in kept:
            w.writerow(d)

    sha = sha256_file(STRATUM_CSV)
    with open(STRATUM_SHA, "w") as f:
        f.write(sha + "  stratum.csv\n")

    # --- report ---
    cls_counts = Counter(d["bridging_class"] for d in kept)
    lemmas_by_cls = defaultdict(set)
    spread_by_cls = defaultdict(Counter)
    median_by_cls = defaultdict(Counter)
    for d in kept:
        c = d["bridging_class"]
        lemmas_by_cls[c].add(d["lemma"])
        spread_by_cls[c][d["human_spread"]] += 1
        median_by_cls[c][d["human_median"]] += 1

    print("=" * 64)
    print("FROZEN BRIDGING-CONTEXT STRATUM (v1) — groundwork, no model calls")
    print("=" * 64)
    print(f"source manifest : {os.path.relpath(MANIFEST, REPO)}")
    print(f"manifest rows   : {len(rows)} (all within-period)")
    print(f"rater floor     : human_n >= {RATER_FLOOR}")
    print(f"dropped < floor : {dropped_below_floor}")
    print(f"surviving rows  : {len(kept)}")
    print()
    print("per-class pool sizes (median-band primary):")
    for c in ("clear-same", "bridging", "clear-different"):
        print(
            f"  {c:<16} pairs={cls_counts[c]:<3} lemmas={len(lemmas_by_cls[c])}"
        )
    print()
    print("per-class median distribution:")
    for c in ("clear-same", "bridging", "clear-different"):
        print(f"  {c:<16} {dict(sorted(median_by_cls[c].items()))}")
    print()
    print("per-class human_spread distribution (secondary disagreement descriptor):")
    for c in ("clear-same", "bridging", "clear-different"):
        print(f"  {c:<16} {dict(sorted(spread_by_cls[c].items()))}")
    print()
    print(f"stratum.csv sha256 : {sha}")
    print(f"written            : {os.path.relpath(STRATUM_CSV, REPO)}")
    print(f"                     {os.path.relpath(STRATUM_SHA, REPO)}")
    print()
    print(
        "LABEL DISCIPLINE: the 'bridging' class is a human-rated USAGE-SIMILARITY\n"
        "midpoint / high-disagreement stratum, NOT a certification of sense co-presence."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
