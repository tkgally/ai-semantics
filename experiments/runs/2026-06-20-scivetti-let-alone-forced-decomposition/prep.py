#!/usr/bin/env python3
"""prep.py — FREEZE the let-alone + comparative-correlative subset of the Scivetti
CxNLI Exp-1 test set (recipe only). NO API calls.

Run 2026-06-20-scivetti-let-alone-working-surface. This is a FORMAT-ONLY follow-up to
2026-06-20-scivetti-cxnli-answer-key (session 57). It re-runs the SAME items under a
working-surface response format to test whether let-alone's near-chance forced-format
failure is a competence-absence or an output-channel artifact (essay/output-channel-
confound, essay/floor-is-not-a-ceiling).

Recipe-not-corpus: reads the human-annotated NLI test file from the locally-cloned
Scivetti repo (gitignored under experiments/data/scivetti/, NO license upstream),
selects the two target constructions, computes a sha256 over their canonical
serialization, and writes a MANIFEST carrying ONLY the hash + counts + provenance —
NEVER the premise/hypothesis text.

Subset:
  * let-alone               (24 items, 8/8/8) — the TARGET (forced-format near-chance
                            in session 57: claude 0.542 / gpt 0.458 / gemini 0.667).
  * comparative-correlative (30 items, 10/10/10) — the CEILING CONTROL (forced-format
                            claude 1.000 / gpt 0.900 / gemini 1.000 in session 57);
                            confirms the working surface does not break the instrument.

The full-set freeze is the session-57 manifest (sha256 1c5cffb18c5ef78e, 390 items);
this run pins the SUBSET sha and ALSO re-asserts the full-set sha so the upstream data
is provably the same corpus session 57 scored.

Upstream: github.com/melissatorgbi/beyond-memorization @ 82699473 (re-cloned 2026-06-20).
Test file: data/CxNLI/CxNLI_3_examples_test.tsv (3 rows/item: premise/hypothesis/relation).

Usage:  python3 prep.py            # parse + write stimuli-manifest.json, print sha256
        python3 prep.py --check    # re-parse, assert subset + full-set sha match frozen
"""
import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / ".." / ".." / "data" / "scivetti" / "data" / "CxNLI" / "CxNLI_3_examples_test.tsv"
UPSTREAM_COMMIT = "82699473b5bd2295d87524a4df1a148ec4ce4b1f"
UPSTREAM_URL = "https://github.com/melissatorgbi/beyond-memorization"
MANIFEST = HERE / "stimuli-manifest.json"

# Session-57 full-set sha (recomputed here as a cross-check that the corpus is identical).
FULLSET_SHA = "1c5cffb18c5ef78e"  # prefix; session-57 stimuli-manifest.json
TARGET = "let-alone"
CONTROL = "comparative-correlative"
SUBSET = {TARGET, CONTROL}


def parse_items(path):
    """Return the list of 390 items, each {cxn, num, premise, hyp, gold}. gold is the
    integer 0/1/2 parsed from the 'relation' row's leading digit. (VERBATIM parse logic
    from the session-57 prep.py, so the recovered text is provably identical.)"""
    items = []
    cur = None
    cxn = None
    with open(path, newline="") as f:
        r = csv.reader(f, delimiter="\t")
        header = next(r)
        assert header[0] == "CxN Type", f"unexpected header: {header}"
        for row in r:
            if len(row) < 4:
                continue
            t, num, ph, txt = row[0].strip(), row[1].strip(), row[2].strip(), row[3]
            if t:
                cxn = t
            if ph == "premise":
                cur = {"cxn": cxn, "num": num, "premise": txt}
            elif ph == "hypothesis":
                cur["hyp"] = txt
            elif ph == "relation":
                digs = [c for c in txt.strip()[:1] if c in "012"]
                assert digs, f"no gold digit in {txt!r}"
                cur["gold"] = int(digs[0])
                items.append(cur)
                cur = None
    return items


def fullset_sha(items):
    payload = [[it["cxn"], it["num"], it["premise"], it["hyp"], it["gold"]] for it in items]
    blob = json.dumps(payload, ensure_ascii=False, sort_keys=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def subset_items(items):
    """The let-alone + comparative-correlative items, in read order."""
    return [it for it in items if it["cxn"] in SUBSET]


def subset_sha(sub):
    payload = [[it["cxn"], it["num"], it["premise"], it["hyp"], it["gold"]] for it in sub]
    blob = json.dumps(payload, ensure_ascii=False, sort_keys=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def assert_balance(sub):
    per_cxn = Counter(it["cxn"] for it in sub)
    assert per_cxn[TARGET] == 24, f"expected 24 {TARGET}, got {per_cxn[TARGET]}"
    assert per_cxn[CONTROL] == 30, f"expected 30 {CONTROL}, got {per_cxn[CONTROL]}"
    assert len(sub) == 54, f"expected 54 subset items, got {len(sub)}"
    la = [it for it in sub if it["cxn"] == TARGET]
    cc = [it for it in sub if it["cxn"] == CONTROL]
    assert Counter(it["gold"] for it in la) == {0: 8, 1: 8, 2: 8}, "let-alone not 8/8/8"
    assert Counter(it["gold"] for it in cc) == {0: 10, 1: 10, 2: 10}, "comp-corr not 10/10/10"
    assert all(it["gold"] in (0, 1, 2) for it in sub)


def build_manifest(items, sub):
    return {
        "source_url": UPSTREAM_URL,
        "source_commit": UPSTREAM_COMMIT,
        "source_file": "data/CxNLI/CxNLI_3_examples_test.tsv",
        "fetched": "2026-06-20",
        "fullset_sha256": fullset_sha(items),
        "fullset_n": len(items),
        "subset_constructions": sorted(SUBSET),
        "subset_n": len(sub),
        "subset_sha256": subset_sha(sub),
        "per_construction_counts": dict(sorted(Counter(it["cxn"] for it in sub).items())),
        "per_label_counts": {str(k): v for k, v in
                             sorted(Counter(it["gold"] for it in sub).items())},
        "label_scheme": {"0": "entailment", "1": "neutral", "2": "contradiction"},
        "ratified_anchor_constructions": [CONTROL],  # comp-corr is ratified; let-alone is not
        "human_baseline_exp1_accuracy": 0.90,
        "paired_baseline_run": "2026-06-20-scivetti-cxnli-answer-key (forced single-token format)",
        "note": ("Recipe-not-corpus: hash + counts only; the item text stays gitignored "
                 "under experiments/data/scivetti/. Re-clone the upstream commit to "
                 "reproduce. This run changes ONLY the response format vs the paired "
                 "baseline run (forced single token -> working surface)."),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="re-parse and assert subset + full-set sha match the frozen manifest")
    args = ap.parse_args()
    src = SRC.resolve()
    assert src.exists(), (f"source not found: {src}\nClone {UPSTREAM_URL} @ "
                          f"{UPSTREAM_COMMIT[:8]} into experiments/data/scivetti/ first.")
    items = parse_items(src)
    assert len(items) == 390, f"expected 390 full-set items, got {len(items)}"
    assert fullset_sha(items).startswith(FULLSET_SHA), (
        f"FULL-SET SHA MISMATCH: recomputed {fullset_sha(items)[:16]} != session-57 "
        f"{FULLSET_SHA} — upstream corpus drifted; do NOT run.")
    sub = subset_items(items)
    assert_balance(sub)
    man = build_manifest(items, sub)
    if args.check:
        assert MANIFEST.exists(), "no frozen manifest to check against"
        frozen = json.load(open(MANIFEST))
        assert frozen["subset_sha256"] == man["subset_sha256"], (
            f"SUBSET SHA MISMATCH: frozen {frozen['subset_sha256'][:16]} != recomputed "
            f"{man['subset_sha256'][:16]} — do NOT run.")
        assert frozen["fullset_sha256"] == man["fullset_sha256"], "full-set sha drifted"
        print(f"--check PASS: subset sha256 {man['subset_sha256'][:16]} "
              f"({man['subset_n']} items) + full-set sha {man['fullset_sha256'][:16]} match")
        return
    json.dump(man, open(MANIFEST, "w"), indent=2)
    print(f"wrote {MANIFEST.name}")
    print(f"  fullset_sha[:16] = {man['fullset_sha256'][:16]} (n={man['fullset_n']})")
    print(f"  subset_sha[:16]  = {man['subset_sha256'][:16]} (n={man['subset_n']})")
    print(f"  per-construction = {man['per_construction_counts']}")
    print(f"  per-label        = {man['per_label_counts']}")


if __name__ == "__main__":
    main()
