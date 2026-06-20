#!/usr/bin/env python3
"""prep.py — FREEZE the POWERED let-alone item set (recipe only). NO API calls.

Run 2026-06-20-scivetti-let-alone-powered-rerun. The trigger-(g) POWERED re-run of the
session-60 forced-decomposition probe (2026-06-20-scivetti-let-alone-forced-decomposition).

Session 60 left a PARTIAL WITNESS: with uptake forced, gpt-5.4-mini's let-alone accuracy
rose to 0.583 on n=24 test items — directional but underpowered (vs-offered sign test
p=0.090) and BELOW the ≈0.90 human baseline (CI hi 0.755 < 0.90). The correct continuation
(essay/witness-seeking-economics §"The partial witness"; essay/output-channel-confound
trigger (b)) is a POWERED re-run of the SAME forced-decomposition axis with MORE let-alone
items — exempt from the "more of the same probe cannot" caution because the first run left
a directional SIGNAL, not a null.

This run holds the forced-decomposition INSTRUMENT byte-identical to session 60 and ENLARGES
the let-alone target set with the only additional human-annotated let-alone items in the
upstream release: the 9 let-alone items in the CxNLI 3-examples TRAIN split, which are
DISJOINT from the 24 test items (0 shared premise/hypothesis pairs, verified below). So the
let-alone target grows 24 -> 33 (24 test + 9 train), giving a tighter Wilson CI vs 0.90 and
an internal replication of the session-60 24-item result. The comparative-correlative
CEILING CONTROL is held byte-identical (the SAME 30 test items as sessions 57/58/60).

Recipe-not-corpus: reads the human-annotated NLI files from the locally-cloned Scivetti repo
(gitignored under experiments/data/scivetti/, NO license upstream), selects the target +
control items, computes sha256 over their canonical serialization, and writes a MANIFEST
carrying ONLY hashes + counts + provenance — NEVER the premise/hypothesis text.

Frozen item set:
  * let-alone TEST  (24 items, 8/8/8) — the session-60 target set (CxNLI_3_examples_test.tsv).
  * let-alone TRAIN ( 9 items, 3/3/3) — NEW, DISJOINT (CxNLI_3_examples_train.csv).
  * comp-correlative TEST (30 items, 10/10/10) — CEILING CONTROL (test.tsv, byte-identical
    to sessions 57/58/60).
  Combined let-alone target n = 33.

Cross-checks re-asserted so the upstream data is provably the same corpus sessions 57/58/60
scored: the 390-item full-set sha == 1c5cffb18c5ef78e, AND the 54-item session-57/58/60
subset sha == 9be31a8fea8d7f166 (24 let-alone test + 30 comp-corr).

Upstream: github.com/melissatorgbi/beyond-memorization @ 82699473 (re-cloned 2026-06-20).
  test  file: data/CxNLI/CxNLI_3_examples_test.tsv   (TAB-delimited, 3 rows/item).
  train file: data/CxNLI/CxNLI_3_examples_train.csv  (COMMA-delimited, 3 rows/item).

Usage:  python3 prep.py            # parse + write stimuli-manifest.json, print shas
        python3 prep.py --check    # re-parse, assert all shas + disjointness match frozen
"""
import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / ".." / ".." / "data" / "scivetti" / "data" / "CxNLI"
TEST_SRC = DATA / "CxNLI_3_examples_test.tsv"
TRAIN_SRC = DATA / "CxNLI_3_examples_train.csv"
UPSTREAM_COMMIT = "82699473b5bd2295d87524a4df1a148ec4ce4b1f"
UPSTREAM_URL = "https://github.com/melissatorgbi/beyond-memorization"
MANIFEST = HERE / "stimuli-manifest.json"

# Cross-check anchors (prefixes) from sessions 57/58/60.
FULLSET_SHA = "1c5cffb18c5ef78e"   # 390-item test set
S60_SUBSET_SHA = "9be31a8fea8d7f1"  # 54-item session-57/58/60 subset (24 LA test + 30 CC)
TARGET = "let-alone"
CONTROL = "comparative-correlative"


def parse_items(path, delim):
    """Return items, each {cxn, num, premise, hyp, gold}. Robust to the P/H/R column's
    casing/truncation quirks (the train CSV writes 'Premi' for one row; startswith covers
    both files). gold = leading 0/1/2 digit of the relation row. Field set identical to
    the session-57/58/60 parser, so shared shas are provably the same text."""
    items, cur, cxn = [], None, None
    with open(path, newline="") as f:
        r = csv.reader(f, delimiter=delim)
        header = next(r)
        assert header[0].strip() == "CxN Type", f"unexpected header: {header}"
        for row in r:
            if len(row) < 4:
                continue
            t, num, ph, txt = row[0].strip(), row[1].strip(), row[2].strip(), row[3]
            if t:
                cxn = t
            pl = ph.lower()
            if pl.startswith("prem"):
                cur = {"cxn": cxn, "num": num, "premise": txt}
            elif pl.startswith("hyp"):
                cur["hyp"] = txt
            elif pl.startswith("rel"):
                digs = [c for c in txt.strip()[:1] if c in "012"]
                assert digs, f"no gold digit in {txt!r}"
                cur["gold"] = int(digs[0])
                items.append(cur)
                cur = None
    return items


def sha_over(rows):
    payload = [[it["cxn"], it["num"], it["premise"], it["hyp"], it["gold"]] for it in rows]
    blob = json.dumps(payload, ensure_ascii=False, sort_keys=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def key(it):
    return (it["premise"].strip(), it["hyp"].strip())


def build_sets(test_items, train_items):
    """Return (frozen_list, parts) where frozen_list is the ordered 63-item run set:
    24 let-alone test (read order) + 9 let-alone train (read order) + 30 comp-corr test."""
    la_test = [it for it in test_items if it["cxn"] == TARGET]
    cc_test = [it for it in test_items if it["cxn"] == CONTROL]
    la_train = [it for it in train_items if it["cxn"] == TARGET]
    # tag split
    for it in la_test:
        it["split"] = "test"
    for it in cc_test:
        it["split"] = "test"
    for it in la_train:
        it["split"] = "train"
    parts = {"la_test": la_test, "la_train": la_train, "cc_test": cc_test}
    frozen = la_test + la_train + cc_test
    return frozen, parts


def assert_structure(parts):
    la_test, la_train, cc_test = parts["la_test"], parts["la_train"], parts["cc_test"]
    assert len(la_test) == 24, f"expected 24 let-alone test, got {len(la_test)}"
    assert len(la_train) == 9, f"expected 9 let-alone train, got {len(la_train)}"
    assert len(cc_test) == 30, f"expected 30 comp-corr test, got {len(cc_test)}"
    assert Counter(it["gold"] for it in la_test) == {0: 8, 1: 8, 2: 8}, "LA-test not 8/8/8"
    assert Counter(it["gold"] for it in la_train) == {0: 3, 1: 3, 2: 3}, "LA-train not 3/3/3"
    assert Counter(it["gold"] for it in cc_test) == {0: 10, 1: 10, 2: 10}, "CC not 10/10/10"
    # DISJOINTNESS: no train let-alone item shares a (premise, hypothesis) with any test item.
    test_keys = {key(it) for it in la_test} | {key(it) for it in cc_test}
    train_keys = {key(it) for it in la_train}
    overlap = train_keys & test_keys
    assert not overlap, f"DISJOINTNESS VIOLATED: {len(overlap)} train items overlap test"
    # also premise-level disjointness (stronger: no shared source sentence)
    test_prem = {it["premise"].strip() for it in la_test}
    train_prem = {it["premise"].strip() for it in la_train}
    assert not (train_prem & test_prem), "train let-alone shares a premise with test let-alone"


def build_manifest(test_items, frozen, parts):
    la_test, la_train, cc_test = parts["la_test"], parts["la_train"], parts["cc_test"]
    return {
        "source_url": UPSTREAM_URL,
        "source_commit": UPSTREAM_COMMIT,
        "test_file": "data/CxNLI/CxNLI_3_examples_test.tsv",
        "train_file": "data/CxNLI/CxNLI_3_examples_train.csv",
        "fetched": "2026-06-20",
        # cross-checks vs sessions 57/58/60
        "fullset_sha256": sha_over(test_items),
        "fullset_n": len(test_items),
        "s60_subset_sha256": sha_over(la_test + cc_test),  # 24 LA test + 30 CC == s60 subset
        # this run's frozen set
        "frozen_sha256": sha_over(frozen),
        "frozen_n": len(frozen),
        "letalone_train_sha256": sha_over(la_train),
        "per_split_counts": {
            "let-alone:test": len(la_test),
            "let-alone:train": len(la_train),
            "comparative-correlative:test": len(cc_test),
        },
        "letalone_combined_n": len(la_test) + len(la_train),
        "per_label_counts_letalone_combined": {
            str(k): v for k, v in sorted(
                Counter(it["gold"] for it in (la_test + la_train)).items())
        },
        "label_scheme": {"0": "entailment", "1": "neutral", "2": "contradiction"},
        "ratified_anchor_constructions": [CONTROL],  # comp-corr ratified; let-alone descriptive
        "human_baseline_exp1_accuracy": 0.90,
        "instrument": "forced-decomposition (byte-identical to session 60 probe.py NLI_SYS_DECOMP)",
        "paired_forced_baseline_run": "2026-06-20-scivetti-let-alone-forced-decomposition (24 LA test, internal replication)",
        "note": ("Recipe-not-corpus: hashes + counts only; item text stays gitignored under "
                 "experiments/data/scivetti/. Re-clone the upstream commit to reproduce. "
                 "This run ENLARGES the let-alone target (24 test -> 33 = +9 DISJOINT train "
                 "items) under the SAME forced-decomposition instrument as session 60; the "
                 "comp-corr control is byte-identical to sessions 57/58/60."),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="re-parse and assert all shas + disjointness match the frozen manifest")
    args = ap.parse_args()
    tsrc, trsrc = TEST_SRC.resolve(), TRAIN_SRC.resolve()
    for p in (tsrc, trsrc):
        assert p.exists(), (f"source not found: {p}\nClone {UPSTREAM_URL} @ "
                            f"{UPSTREAM_COMMIT[:8]} into experiments/data/scivetti/ first.")
    test_items = parse_items(tsrc, "\t")
    train_items = parse_items(trsrc, ",")
    assert len(test_items) == 390, f"expected 390 test items, got {len(test_items)}"
    assert sha_over(test_items).startswith(FULLSET_SHA), (
        f"FULL-SET SHA MISMATCH: {sha_over(test_items)[:16]} != {FULLSET_SHA} — "
        f"upstream test corpus drifted; do NOT run.")
    frozen, parts = build_sets(test_items, train_items)
    assert_structure(parts)
    # re-assert the session-60 subset sha (24 LA test + 30 CC) as a cross-check
    s60_sub = sha_over(parts["la_test"] + parts["cc_test"])
    assert s60_sub.startswith(S60_SUBSET_SHA), (
        f"S60 SUBSET SHA MISMATCH: {s60_sub[:16]} != {S60_SUBSET_SHA} — test items drifted.")
    man = build_manifest(test_items, frozen, parts)
    if args.check:
        assert MANIFEST.exists(), "no frozen manifest to check against"
        frozen_man = json.load(open(MANIFEST))
        for k in ("frozen_sha256", "fullset_sha256", "s60_subset_sha256",
                  "letalone_train_sha256"):
            assert frozen_man[k] == man[k], (
                f"{k} MISMATCH: frozen {frozen_man[k][:16]} != recomputed {man[k][:16]} "
                f"— do NOT run.")
        print(f"--check PASS: frozen sha256 {man['frozen_sha256'][:16]} "
              f"({man['frozen_n']} items); let-alone combined n={man['letalone_combined_n']}; "
              f"full-set {man['fullset_sha256'][:16]}; s60-subset {man['s60_subset_sha256'][:16]}")
        return
    json.dump(man, open(MANIFEST, "w"), indent=2)
    print(f"wrote {MANIFEST.name}")
    print(f"  frozen_sha[:16]   = {man['frozen_sha256'][:16]} (n={man['frozen_n']})")
    print(f"  let-alone combined n = {man['letalone_combined_n']} "
          f"(label dist {man['per_label_counts_letalone_combined']})")
    print(f"  train-LA sha[:16] = {man['letalone_train_sha256'][:16]} (n=9)")
    print(f"  fullset_sha[:16]  = {man['fullset_sha256'][:16]} (cross-check {FULLSET_SHA})")
    print(f"  s60-subset[:16]   = {man['s60_subset_sha256'][:16]} (cross-check {S60_SUBSET_SHA})")
    print(f"  per-split = {man['per_split_counts']}")


if __name__ == "__main__":
    main()
