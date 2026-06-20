#!/usr/bin/env python3
"""prep.py — fetch + parse + FREEZE the Scivetti CxNLI Exp-1 test set (recipe only).

Run 2026-06-20-scivetti-cxnli-answer-key. NO API calls. This is the recipe-not-corpus
freeze step: it reads the human-annotated NLI test file from the locally-cloned
Scivetti repo (gitignored under experiments/data/scivetti/, NO license file upstream),
parses the 390 Experiment-1 items, computes a sha256 over their canonical
serialization, and writes a MANIFEST that carries ONLY the hash + per-construction /
per-label counts + provenance — NEVER the premise/hypothesis text. The item text stays
gitignored; the committed artifact is the recipe + the hash, exactly as the
languageR / WiC / tangrams runs do.

Anchor: resource/scivetti-2025-cxnli-dataset (ratified 2026-05-29, Tom, as the human
NLI answer-key anchor for caused-motion / conative / way-manner / comparative-
correlative). Human baseline: native-speaker accuracy approximately 0.90 on Exp 1.

Upstream: github.com/melissatorgbi/beyond-memorization @ 82699473 (cloned 2026-06-20).
Test file: data/CxNLI/CxNLI_3_examples_test.tsv (3 rows/item: premise/hypothesis/relation).

Usage:  python3 prep.py            # parse + write stimuli-manifest.json, print sha256
        python3 prep.py --check    # re-parse, assert sha matches the frozen manifest
"""
import argparse
import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
# Recipe-not-corpus: the raw TSV lives gitignored under experiments/data/scivetti/.
SRC = HERE / ".." / ".." / "data" / "scivetti" / "data" / "CxNLI" / "CxNLI_3_examples_test.tsv"
UPSTREAM_COMMIT = "82699473b5bd2295d87524a4df1a148ec4ce4b1f"
UPSTREAM_URL = "https://github.com/melissatorgbi/beyond-memorization"
MANIFEST = HERE / "stimuli-manifest.json"

# The four constructions whose human anchor was RATIFIED (Tom, 2026-05-29) for an
# in-repo conjecture. The other four are part of the same human-annotated release and
# share the aggregate baseline, but carry no individually-ratified conjecture anchor.
RATIFIED = {"caused-motion", "conative", "way-manner", "comparative-correlative"}
# Monotonicity-asymmetry mapping (conjecture/constructional-monotonicity-asymmetry):
# which of the ratified four ADD a construction-contributed entailment vs CANCEL a
# lexical default. (Descriptive tag only; the add/cancel accuracy gap here is
# baseline-difficulty-confounded, NOT the matched-difficulty confirm test.)
ADD = {"caused-motion", "way-manner"}
CANCEL = {"conative"}


def parse_items(path):
    """Return the list of 390 items, each {cxn, num, premise, hyp, gold}. gold is the
    integer 0/1/2 parsed from the 'relation' row's leading digit."""
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
                # relation cell looks like "1 (neutral)"; take the leading 0/1/2.
                digs = [c for c in txt.strip()[:1] if c in "012"]
                assert digs, f"no gold digit in {txt!r}"
                cur["gold"] = int(digs[0])
                items.append(cur)
                cur = None
    return items


def canonical_sha(items):
    """sha256 over the canonical (premise, hypothesis, gold) serialization, ordered as
    read. Binds the exact item text WITHOUT committing it."""
    payload = [[it["cxn"], it["num"], it["premise"], it["hyp"], it["gold"]] for it in items]
    blob = json.dumps(payload, ensure_ascii=False, sort_keys=False).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()


def build_manifest(items):
    sha = canonical_sha(items)
    per_cxn = Counter(it["cxn"] for it in items)
    per_label = Counter(it["gold"] for it in items)
    return {
        "source_url": UPSTREAM_URL,
        "source_commit": UPSTREAM_COMMIT,
        "source_file": "data/CxNLI/CxNLI_3_examples_test.tsv",
        "fetched": "2026-06-20",
        "n_items": len(items),
        "sha256": sha,
        "per_construction_counts": dict(sorted(per_cxn.items())),
        "per_label_counts": {str(k): per_label[k] for k in sorted(per_label)},
        "label_scheme": {"0": "entailment", "1": "neutral", "2": "contradiction"},
        "ratified_anchor_constructions": sorted(RATIFIED),
        "human_baseline_exp1_accuracy": 0.90,
        "note": ("Recipe-not-corpus: this manifest pins the hash + counts only; the "
                 "390 premise/hypothesis items stay gitignored under "
                 "experiments/data/scivetti/. Re-clone the upstream commit to reproduce."),
    }


def assert_balance(items):
    assert len(items) == 390, f"expected 390 items, got {len(items)}"
    per_label = Counter(it["gold"] for it in items)
    assert per_label[0] == per_label[1] == per_label[2] == 130, \
        f"expected 130/130/130 label balance, got {dict(per_label)}"
    per_cxn = Counter(it["cxn"] for it in items)
    for c in RATIFIED:
        assert per_cxn[c] > 0, f"ratified construction {c} missing from test set"
    # No item is dropped for a missing gold.
    assert all(it["gold"] in (0, 1, 2) for it in items)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="re-parse and assert sha matches the frozen manifest")
    args = ap.parse_args()
    src = SRC.resolve()
    assert src.exists(), (f"source not found: {src}\nClone {UPSTREAM_URL} @ "
                          f"{UPSTREAM_COMMIT[:8]} into experiments/data/scivetti/ first.")
    items = parse_items(src)
    assert_balance(items)
    man = build_manifest(items)
    if args.check:
        assert MANIFEST.exists(), "no frozen manifest to check against"
        frozen = json.load(open(MANIFEST))
        assert frozen["sha256"] == man["sha256"], (
            f"SHA MISMATCH: frozen {frozen['sha256'][:16]} != recomputed "
            f"{man['sha256'][:16]} — the upstream data changed; do NOT run.")
        print(f"--check PASS: sha256 {man['sha256'][:16]} matches frozen manifest "
              f"({man['n_items']} items)")
        return
    json.dump(man, open(MANIFEST, "w"), indent=2)
    print(f"wrote {MANIFEST.name}")
    print(f"  n_items = {man['n_items']}")
    print(f"  sha256[:16] = {man['sha256'][:16]}")
    print(f"  per-construction = {man['per_construction_counts']}")
    print(f"  per-label = {man['per_label_counts']}")


if __name__ == "__main__":
    main()
