#!/usr/bin/env python3
"""Lexical bridging-context v1: WiC CLEAR-POLE supplement freeze (recipe-not-corpus).

Freezes a small, seeded, balanced WiC supplement for the TWO CLEAR POLES ONLY of the
lexical bridging-context probe — clear-same (WiC gold T) and clear-different (WiC gold F).
This unblocks the thin-pole problem reported in BUILDABILITY.md ("WiC supplementation of
the clear poles"): the DWUG-only floored clear-same pole is 9 pairs / 7 lemmas, marginal
for the clear-class precondition.

BINDING CONSTRAINT (anchor decision condition 1):
  wiki/decisions/resolved/lexical-bridging-context-anchor.md
  WiC T/F may supplement the two CLEAR POLES ONLY — NEVER the bridging stratum. WiC is
  binary by design and pruned its closest polyseme negatives, so it cannot certify a
  usage-similarity midpoint. This script therefore touches ONLY the clear poles. The
  >=3-rater floor that binds DWUG classes does NOT apply to WiC: WiC carries expert
  lexicographer-inventory gold, not a rating panel (resource/wic-word-in-context).

  human_median in the gitignored fulltext is a NOMINAL POLE LABEL, not a rating: it is set
  to the DURel pole value (4.0 for clear-same / 1.0 for clear-different) PURELY so the
  clear-pole precondition code can treat these as clear-class anchors alongside the DWUG
  rows. human_n is null because WiC has NO per-item rating panel.

LICENCE / DATA HANDLING (mirrors the DWUG prep.py posture; WiC is CC BY-NC 4.0). This
script is the committed, reproducible RECIPE, not the corpus. It:
  - downloads WiC_dataset.zip from pilehvar.github.io into experiments/data/wic/
    (gitignored: that dir's .gitignore is `*`) if absent, and PRINTS the archive sha256
    (no pre-existing pin is asserted here — this script establishes/records whatever sha
    the live package has; the resource page records f1a2fb6... for the 2026-05-31 copy);
  - writes a COMMITTABLE manifest wic_poles.csv (item_id, target, pos, gold, pole,
    wic_line — pointers + gold only, NO sentence text — research-analysis use, not
    redistribution) plus its sha256 sidecar wic_poles.sha256;
  - emits a gitignored, local-only fulltext wic_poles_fulltext.jsonl (with sentences +
    char spans) whose schema matches the DWUG path so ONE probe can read both.

TWO MODES (mirrors prep.py's re-map-the-frozen-stratum posture):
  - RE-MAP (default whenever wic_poles.csv already exists): the committed manifest is the
    FROZEN authority (its wic_line column is the 40 pole pointers). This script then ONLY
    re-maps those exact wic_line rows to their WiC sentences + token offsets and emits the
    gitignored fulltext; it does NOT re-select and does NOT overwrite the manifest. This is
    the run-time path — a fresh clone stages the corpus for the frozen poles.
  - FRESH-FREEZE (only when no manifest exists): the original seeded balanced selection,
    used once to create the freeze. Made reproducible across processes by seeding
    random.Random with a STRING key (random.Random's string seeding is salt-free, unlike
    the builtin hash() of a tuple, which is PYTHONHASHSEED-salted — the 2026-06-22 fix).

SELECTION (fresh-freeze path, deterministic, no API):
  SEED = 20260621; train split only. Candidates per gold class are sorted by a stable key
  (train line index) for reproducibility, capped to <=2 items per target lemma for
  diversity (relaxed only if a pole runs short, and the relaxation is reported), then
  shuffled with the seed and the first N_PER_POLE = 20 taken. The token->char offset of
  the target in each sentence is computed by splitting on whitespace and locating the
  char span of the given (0-based) token index; items whose token index is out of range
  are dropped and reported.

Reference (style model): experiments/data/subtlex-us/prep.py (committed recipe-not-corpus)
WiC train format: target<TAB>POS<TAB>idx1-idx2<TAB>sentence1<TAB>sentence2 ; gold = T|F.
  idx1/idx2 are the 0-based whitespace-token indices of the target in sentence1/sentence2.

Run: python3 prep_wic.py   (downloads WiC on first run; no API)
"""
import csv
import hashlib
import json
import os
import random
import urllib.request
import zipfile
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
WIC_DIR = os.path.abspath(os.path.join(HERE, "..", "..", "data", "wic"))
ZIP_PATH = os.path.join(WIC_DIR, "WiC_dataset.zip")
WIC_URL = "https://pilehvar.github.io/wic/package/WiC_dataset.zip"

# Committable outputs (pointers + gold only; NO corpus sentences).
MANIFEST = os.path.join(HERE, "wic_poles.csv")
MANIFEST_SHA = os.path.join(HERE, "wic_poles.sha256")
# Gitignored, local-only full-text (sentences + char spans); the probe reads this.
FULLTEXT = os.path.join(WIC_DIR, "wic_poles_fulltext.jsonl")

SEED = 20260621
N_PER_POLE = 20
MAX_PER_LEMMA = 2            # diversity cap; relaxed only if a pole is short (reported)
POLE_OF = {"T": "clear-same", "F": "clear-different"}
NOMINAL_MEDIAN = {"clear-same": 4.0, "clear-different": 1.0}   # NOMINAL pole label, NOT a rating


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_wic():
    """Download (if absent) + extract WiC; PRINT the archive sha256 (no pin asserted)."""
    if not os.path.exists(ZIP_PATH):
        os.makedirs(WIC_DIR, exist_ok=True)
        print(f"downloading WiC -> {ZIP_PATH} ...")
        urllib.request.urlretrieve(WIC_URL, ZIP_PATH)
    h = sha256_file(ZIP_PATH)
    print(f"WiC_dataset.zip sha256 = {h}")
    extract = os.path.join(WIC_DIR, "extracted")
    if not os.path.isdir(extract):
        with zipfile.ZipFile(ZIP_PATH) as z:
            z.extractall(extract)
    return extract, h


def find_file(extract, name):
    for root, _, files in os.walk(extract):
        if name in files:
            return os.path.join(root, name)
    raise FileNotFoundError(f"{name} not found under {extract}")


def load_train(extract):
    """Load TRAIN split items keyed by 0-based line index. Returns list of dicts."""
    data_f = find_file(extract, "train.data.txt")
    gold_f = find_file(extract, "train.gold.txt")
    items = []
    with open(data_f, encoding="utf-8") as df, open(gold_f, encoding="utf-8") as gf:
        for i, (dl, gl) in enumerate(zip(df, gf)):
            p = dl.rstrip("\n").split("\t")
            if len(p) < 5:
                continue
            tw, pos, idx, c1, c2 = p[0], p[1], p[2], p[3], p[4]
            i1, i2 = idx.split("-")
            items.append({"wic_line": i, "target": tw, "pos": pos,
                          "idx1": int(i1), "idx2": int(i2),
                          "ctx1": c1, "ctx2": c2, "gold": gl.strip()})
    return items


def token_char_span(ctx, idx):
    """Char span [s, e) of the idx-th whitespace token (0-based). None if out of range.

    Sentences are split on single spaces (WiC contexts are pre-tokenized, space-joined);
    the char offset is recovered by summing token lengths + the separators before idx.
    """
    toks = ctx.split(" ")
    if not (0 <= idx < len(toks)):
        return None
    s = 0
    for t in toks[:idx]:
        s += len(t) + 1   # token + the single space separator
    e = s + len(toks[idx])
    surf = ctx[s:e]
    if surf != toks[idx]:        # sanity: recovered span must equal the token
        return None
    return s, e, surf


def select_pole(items, gold, rng):
    """Deterministic balanced selection for one gold class. Returns (selected, relaxed)."""
    cands = sorted((it for it in items if it["gold"] == gold), key=lambda it: it["wic_line"])
    # Validate token offsets; drop + report malformed.
    valid, dropped = [], []
    for it in cands:
        g1 = token_char_span(it["ctx1"], it["idx1"])
        g2 = token_char_span(it["ctx2"], it["idx2"])
        if g1 is None or g2 is None:
            dropped.append(it["wic_line"])
            continue
        it = dict(it)
        it["span1"], it["surf1"] = [g1[0], g1[1]], g1[2]
        it["span2"], it["surf2"] = [g2[0], g2[1]], g2[2]
        valid.append(it)
    if dropped:
        print(f"  gold {gold}: dropped {len(dropped)} item(s) with out-of-range/"
              f"unrecoverable token offsets (lines {dropped[:10]}{'...' if len(dropped) > 10 else ''})")

    # Shuffle deterministically, then take first N honoring the <=MAX_PER_LEMMA cap.
    order = list(valid)
    rng.shuffle(order)
    per_lemma = defaultdict(int)
    chosen, relaxed = [], False
    for it in order:
        if len(chosen) >= N_PER_POLE:
            break
        if per_lemma[it["target"]] < MAX_PER_LEMMA:
            chosen.append(it)
            per_lemma[it["target"]] += 1
    # Relax the diversity cap only if the pole is short.
    if len(chosen) < N_PER_POLE:
        relaxed = True
        chosen_lines = {it["wic_line"] for it in chosen}
        for it in order:
            if len(chosen) >= N_PER_POLE:
                break
            if it["wic_line"] not in chosen_lines:
                chosen.append(it)
                chosen_lines.add(it["wic_line"])
    return chosen, relaxed


def map_one(it):
    """Attach validated token char spans to a train item; return it or None if unmappable."""
    g1 = token_char_span(it["ctx1"], it["idx1"])
    g2 = token_char_span(it["ctx2"], it["idx2"])
    if g1 is None or g2 is None:
        return None
    it = dict(it)
    it["span1"], it["surf1"] = [g1[0], g1[1]], g1[2]
    it["span2"], it["surf2"] = [g2[0], g2[1]], g2[2]
    return it


def remap_frozen(items):
    """RE-MAP path: stage the gitignored fulltext for the FROZEN wic_poles.csv pointers.

    Reads the committed manifest's wic_line column (the 40 authoritative pole pointers),
    maps each to its WiC sentences + spans, and emits the fulltext. Does NOT re-select and
    does NOT touch the committed manifest/sha. Mirrors prep.py's re-map-the-stratum posture.
    """
    by_line = {it["wic_line"]: it for it in items}
    with open(MANIFEST, newline="", encoding="utf-8") as f:
        man_rows = list(csv.DictReader(f))
    fulltext_rows, failures = [], []
    for r in man_rows:
        line = int(r["wic_line"])
        it = by_line.get(line)
        mapped = map_one(it) if it is not None else None
        if mapped is None:
            failures.append((r["item_id"], line))
            continue
        pole = r["pole"]
        fulltext_rows.append({
            "item_id": r["item_id"], "lemma": mapped["target"], "bridging_class": pole,
            "ctx1": mapped["ctx1"], "span1": mapped["span1"], "surf1": mapped["surf1"],
            "ctx2": mapped["ctx2"], "span2": mapped["span2"], "surf2": mapped["surf2"],
            "human_median": NOMINAL_MEDIAN[pole], "human_n": None,
        })
    with open(FULLTEXT, "w", encoding="utf-8") as f:
        for rec in fulltext_rows:
            f.write(json.dumps(rec) + "\n")
    man_sha = sha256_file(MANIFEST)
    by_pole = Counter(r["bridging_class"] for r in fulltext_rows)
    print(f"\nRE-MAP mode (frozen wic_poles.csv exists; manifest NOT rewritten).")
    print(f"  manifest sha256 = {man_sha}  (frozen authority)")
    print(f"  re-mapped {len(fulltext_rows)} / {len(man_rows)} frozen pole items "
          f"(clear-same {by_pole.get('clear-same', 0)}, "
          f"clear-different {by_pole.get('clear-different', 0)})")
    if failures:
        print(f"  {len(failures)} FAILED to map: {failures}")
    else:
        print("  all frozen pole items mapped (no failures).")
    print(f"  wrote (gitignored, local-only) {FULLTEXT} ({len(fulltext_rows)} rows)")
    return {"mode": "remap", "manifest_sha256": man_sha,
            "mapped": len(fulltext_rows), "failures": failures}


def main():
    extract, zip_sha = ensure_wic()
    items = load_train(extract)
    print(f"\nWiC train items loaded: {len(items)}")
    gold_counts = Counter(it["gold"] for it in items)
    print(f"  gold balance: T={gold_counts['T']}  F={gold_counts['F']}")

    # RE-MAP the frozen manifest if it exists (run-time path); fresh-freeze only otherwise.
    if os.path.exists(MANIFEST):
        out = remap_frozen(items)
        print(f"\nWiC archive sha256 (recorded, not pinned): {zip_sha}")
        return out

    print("\nNO frozen wic_poles.csv found -> FRESH-FREEZE selection.")
    selected = {}
    relaxed_poles = []
    # Order gold classes deterministically (T then F); string-keyed Random is salt-free.
    for gold in ("T", "F"):
        rng_g = random.Random(f"{SEED}-{gold}")
        sel, relaxed = select_pole(items, gold, rng_g)
        selected[gold] = sel
        if relaxed:
            relaxed_poles.append(POLE_OF[gold])
        pole = POLE_OF[gold]
        lemmas = sorted({it["target"] for it in sel})
        print(f"\npole {pole} (gold {gold}): selected {len(sel)} items, "
              f"{len(lemmas)} distinct lemmas"
              + (" [DIVERSITY CAP RELAXED — pole short]" if relaxed else ""))

    # Stable item ids: wic-<gold>-<3digit>, ordered by wic_line for reproducibility.
    manifest_rows, fulltext_rows = [], []
    for gold in ("T", "F"):
        pole = POLE_OF[gold]
        for n, it in enumerate(sorted(selected[gold], key=lambda x: x["wic_line"])):
            item_id = f"wic-{gold}-{n:03d}"
            manifest_rows.append({
                "item_id": item_id, "target": it["target"], "pos": it["pos"],
                "gold": gold, "pole": pole, "wic_line": it["wic_line"],
            })
            fulltext_rows.append({
                "item_id": item_id, "lemma": it["target"], "bridging_class": pole,
                "ctx1": it["ctx1"], "span1": it["span1"], "surf1": it["surf1"],
                "ctx2": it["ctx2"], "span2": it["span2"], "surf2": it["surf2"],
                "human_median": NOMINAL_MEDIAN[pole], "human_n": None,
            })

    # Committable manifest (NO sentence text).
    with open(MANIFEST, "w", newline="", encoding="utf-8") as f:
        wtr = csv.DictWriter(f, fieldnames=["item_id", "target", "pos", "gold",
                                            "pole", "wic_line"])
        wtr.writeheader()
        for r in manifest_rows:
            wtr.writerow(r)
    man_sha = sha256_file(MANIFEST)
    with open(MANIFEST_SHA, "w", encoding="utf-8") as f:
        f.write(f"{man_sha}  wic_poles.csv\n")

    # Gitignored, local-only fulltext (schema matches the DWUG path).
    with open(FULLTEXT, "w", encoding="utf-8") as f:
        for rec in fulltext_rows:
            f.write(json.dumps(rec) + "\n")

    print(f"\nwrote {MANIFEST} ({len(manifest_rows)} rows)")
    print(f"wic_poles.csv sha256 = {man_sha}")
    print(f"wrote {MANIFEST_SHA}")
    print(f"wrote (gitignored, local-only) {FULLTEXT} ({len(fulltext_rows)} rows)")
    if relaxed_poles:
        print(f"\nNOTE: diversity cap relaxed for pole(s): {', '.join(relaxed_poles)} "
              f"(pole shorter than {N_PER_POLE} under the <= {MAX_PER_LEMMA}/lemma cap)")
    print(f"\nWiC archive sha256 (recorded, not pinned): {zip_sha}")

    return {"zip_sha256": zip_sha, "manifest_sha256": man_sha,
            "counts": {POLE_OF[g]: len(selected[g]) for g in ("T", "F")},
            "relaxed": relaxed_poles}


if __name__ == "__main__":
    main()
