#!/usr/bin/env python3
"""Lexical bridging-context v1: re-fetch DWUG + re-map the FROZEN stratum (recipe-not-corpus).

Unblocks blocker (a) of the lexical bridging-context probe: re-fetch the DWUG EN corpus text
and re-map the FROZEN stratum's usage identifiers (id1/id2) to their sentences + validated
target offsets, so the probe has a local full-text file to read.

This script does NOT re-select or re-filter items. It consumes the committed, frozen
`stratum.csv` (the 48 authoritative items; sha256 in `stratum.sha256`) and only re-maps the
id1/id2 of THOSE rows to corpus sentences + spans. The DWUG fetch + sentence/offset extraction
logic (ensure_dwug / load_lemma / extract_target / stem_match) is copied verbatim from the v1
builder (experiments/runs/2026-05-30-lexical-sense-gradience-probe-v1/build_items.py) so the
SAME +1-offset-robust span recovery is used; the script is deterministic and makes no API call.

LICENCE / DATA HANDLING (modeled on experiments/data/subtlex-us/prep.py): DWUG EN is
CC BY-ND 4.0 over copyrighted CCOHA corpus text. This script is the committed, reproducible
RECIPE, not the corpus. It:
  - downloads dwug_en.zip from Zenodo (record 14028531) into experiments/data/dwug/ (gitignored:
    that dir's .gitignore is `*`) if absent, and verifies the archive sha256 against the pin;
  - emits the full-text item file (sentences + target spans) to
    experiments/data/dwug/lexical_bridging_v1_fulltext.jsonl, which is gitignored / local-only —
    the probe reads it; NO corpus text is ever emitted into git.
The frozen `stratum.csv` it reads carries only DWUG identifiers + human DURel ratings + derived
overlap covariates (pointers, not corpus text), and stays committed.

Archive pin: DWUG EN v3.0.0, Zenodo 14028531, sha256
  64eef477154b82cb27925ab4ea8c030a8e23840b538dd06b6464aa1e55af2dbf
Zenodo URL: https://zenodo.org/records/14028531/files/dwug_en.zip?download=1

Run: python3 prep.py    (downloads DWUG on first run; no API)
"""
import csv
import hashlib
import json
import os
import urllib.request
import zipfile
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
DWUG_DIR = os.path.abspath(os.path.join(HERE, "..", "..", "data", "dwug"))
ZIP_PATH = os.path.join(DWUG_DIR, "dwug_en.zip")
EXTRACT = os.path.join(DWUG_DIR, "dwug_en")
ZENODO_URL = "https://zenodo.org/records/14028531/files/dwug_en.zip?download=1"
# archive sha256 recorded for reproducibility (DWUG EN v3.0.0, Zenodo 14028531; pinned 2026-05-30)
EXPECTED_ZIP_SHA256 = "64eef477154b82cb27925ab4ea8c030a8e23840b538dd06b6464aa1e55af2dbf"

STRATUM = os.path.join(HERE, "stratum.csv")                              # committed (no corpus text)
FULLTEXT = os.path.join(DWUG_DIR, "lexical_bridging_v1_fulltext.jsonl")  # gitignored, local-only

# Expected per-class counts in the frozen stratum (sanity targets, not a re-filter).
EXPECTED_CLASS_COUNTS = {"clear-same": 9, "bridging": 24, "clear-different": 15}
EXPECTED_TOTAL = 48


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_dwug():
    """Download (if absent) + extract DWUG EN; verify archive sha256. Returns (data_dir, sha)."""
    if not os.path.exists(ZIP_PATH):
        os.makedirs(DWUG_DIR, exist_ok=True)
        print(f"downloading DWUG EN from Zenodo -> {ZIP_PATH} ...")
        urllib.request.urlretrieve(ZENODO_URL, ZIP_PATH)
    h = sha256_file(ZIP_PATH)
    matched = (h == EXPECTED_ZIP_SHA256)
    print(f"dwug_en.zip sha256 = {h}")
    print(f"  expected (pin)   = {EXPECTED_ZIP_SHA256}")
    print(f"  MATCH = {matched}")
    if not os.path.isdir(EXTRACT):
        with zipfile.ZipFile(ZIP_PATH) as z:
            z.extractall(DWUG_DIR)
    # locate the data/ dir (archive nests dwug_en/dwug_en/data)
    for root, dirs, _ in os.walk(DWUG_DIR):
        if os.path.basename(root) == "data" and any(
                os.path.isdir(os.path.join(root, d)) for d in dirs):
            return root, h, matched
    raise RuntimeError("DWUG data/ dir not found after extraction")


def stem_match(token, root):
    """token (a surface form) is a plausible inflection of the lemma root."""
    t = token.lower()
    if not t.isalpha():
        return False
    need = min(4, len(root))
    cp = 0
    for x, y in zip(t, root):
        if x == y:
            cp += 1
        else:
            break
    return cp >= need or root in t or t in root


def extract_target(ctx, a, b, root):
    """Robustly recover the target word span (v1's +1-offset-robust recovery).

    Returns (start, end, surface) or None if no plausible inflection of the lemma root is found.
    """
    n = len(ctx)
    anchor = None
    for cand in (a, a + 1, a - 1, a + 2, a - 2):
        if 0 <= cand < n and ctx[cand].isalpha():
            anchor = cand
            break
    if anchor is None:
        return None
    s = anchor
    while s > 0 and ctx[s - 1].isalpha():
        s -= 1
    e = anchor
    while e < n and ctx[e].isalpha():
        e += 1
    surface = ctx[s:e]
    if not stem_match(surface, root):
        return None
    return s, e, surface


def load_lemma(data_dir, lemma):
    """Load a lemma's uses (identifier -> context/span/surface), validated as in v1."""
    root = lemma.split("_")[0].lower()
    uses = {}
    with open(os.path.join(data_dir, lemma, "uses.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            parts = r["indexes_target_token"].split(":")
            if len(parts) != 2 or not all(p.strip().lstrip("-").isdigit() for p in parts):
                continue  # malformed/missing target offset -> unusable usage
            a, b = int(parts[0]), int(parts[1])
            got = extract_target(r["context"], a, b, root)
            if got is None:
                continue  # span could not be validated against the lemma -> drop (B1 fix)
            s, e, surface = got
            uses[r["identifier"]] = {"context": r["context"], "grouping": r["grouping"],
                                     "span": (s, e), "surface": surface,
                                     "pos": r["pos"], "date": r["date"]}
    return uses


def read_stratum():
    with open(STRATUM, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    data_dir, zip_sha, matched = ensure_dwug()
    rows = read_stratum()
    print(f"\nstratum rows: {len(rows)} (expected {EXPECTED_TOTAL})")

    # cache uses per lemma (only lemmas present in the stratum)
    lemmas = sorted(set(r["lemma"] for r in rows))
    uses_by_lemma = {lemma: load_lemma(data_dir, lemma) for lemma in lemmas}

    mapped = []
    failures = []
    for r in rows:
        item_id, lemma = r["item_id"], r["lemma"]
        root = lemma.split("_")[0].lower()
        uses = uses_by_lemma.get(lemma, {})
        rec = {"item_id": item_id, "lemma": lemma, "bridging_class": r["bridging_class"],
               "human_median": float(r["human_median"]), "human_n": int(r["human_n"])}
        ok = True
        for n, idk in ((1, "id1"), (2, "id2")):
            ident = r[idk]
            u = uses.get(ident)
            if u is None:
                failures.append((item_id, idk, ident, "identifier not found / span failed validation"))
                ok = False
                break
            rec[f"ctx{n}"] = u["context"]
            rec[f"span{n}"] = [u["span"][0], u["span"][1]]
            rec[f"surf{n}"] = u["surface"]
        if not ok:
            continue
        mapped.append(rec)

    # write gitignored full-text file (probe reads this), exact schema
    with open(FULLTEXT, "w", encoding="utf-8") as f:
        for rec in mapped:
            f.write(json.dumps({
                "item_id": rec["item_id"], "lemma": rec["lemma"],
                "bridging_class": rec["bridging_class"],
                "ctx1": rec["ctx1"], "span1": rec["span1"], "surf1": rec["surf1"],
                "ctx2": rec["ctx2"], "span2": rec["span2"], "surf2": rec["surf2"],
                "human_median": rec["human_median"], "human_n": rec["human_n"],
            }) + "\n")

    mapped_counts = Counter(rec["bridging_class"] for rec in mapped)

    print(f"\nre-mapped {len(mapped)} / {len(rows)} stratum items successfully")
    print("per-class mapped vs expected:")
    for cls in ("clear-same", "bridging", "clear-different"):
        print(f"  {cls:16s}: mapped {mapped_counts.get(cls, 0):2d}  "
              f"expected {EXPECTED_CLASS_COUNTS[cls]:2d}")

    if failures:
        print(f"\n{len(failures)} item(s) FAILED to map:")
        for item_id, idk, ident, why in failures:
            print(f"  {item_id} [{idk}={ident}]: {why}")
    else:
        print("\nall stratum items mapped (no failures).")

    print(f"\narchive sha256: {zip_sha}  (matches pin: {matched})")
    print(f"full-text (gitignored, local-only): {FULLTEXT}")

    return {"total": len(rows), "mapped": len(mapped),
            "mapped_counts": dict(mapped_counts), "failures": failures,
            "zip_sha256": zip_sha, "sha_matched": matched}


if __name__ == "__main__":
    main()
