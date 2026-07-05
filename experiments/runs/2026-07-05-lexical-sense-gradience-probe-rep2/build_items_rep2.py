"""Build + freeze the lexical-sense-gradience REP2 item set from DWUG EN (2026-07-05).

A2a fresh-item, cross-date REPLICATION of design/lexical-sense-gradience-v1 (program A2a;
PROTOCOL §4). The instrument (probe.py, analyze.py) is BYTE-FROZEN identical to the v1 run
(sha256 verified in README-rep2.md). This build script differs from v1's build_items.py in
EXACTLY THREE ways, all mechanical, none touching the design:

  1. SEED 20260530 -> 20260705 (a fresh draw on a fresh date);
  2. an EXCLUSION set: every pair frozen in the v1 manifest is removed from the candidate
     pool BEFORE sampling, so the rep2 set is DISJOINT from v1 at the pair level (0 shared
     item pairs) — the "fresh disjoint items" requirement of a powered re-run (s175 dative,
     s178 AANN precedent);
  3. new output paths (rep2 run dir + a rep2-specific gitignored full-text file), so v1's
     frozen files are never touched.

Everything else — the within-period (Q4) filter, the >=2-judgment requirement, N_PER_LEVEL,
PER_LEMMA_LEVEL_CAP, the span-recovery B1 fix, the B2 span-sanity gate, the overlap covariate,
the STOP list, the manifest schema — is byte-identical to v1's build_items.py. The freeze hash
is the sha256 of the deterministic rep2 manifest; re-running reproduces it.

DATA/LICENCE (unchanged from v1): DWUG EN is CC BY-ND 4.0 over copyrighted CCOHA corpus text.
This script does NOT commit the raw archive or corpus sentences. It downloads dwug_en.zip from
Zenodo (URL + archive sha256 pinned, verified identical to v1), writes a gitignored full-text
file for the probe, and writes a COMMITTABLE manifest (pointers + human DURel gold + the derived
lexical-overlap covariate; research-analysis use, NOT dataset/corpus redistribution).

Run: python3 build_items_rep2.py    (downloads DWUG on first run; no API)
"""
import csv
import hashlib
import io
import json
import os
import random
import re
import statistics
import urllib.request
import zipfile
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DWUG_DIR = os.path.abspath(os.path.join(HERE, "..", "..", "data", "dwug"))
ZIP_PATH = os.path.join(DWUG_DIR, "dwug_en.zip")
EXTRACT = os.path.join(DWUG_DIR, "dwug_en")
ZENODO_URL = "https://zenodo.org/records/14028531/files/dwug_en.zip?download=1"
# archive sha256 recorded for reproducibility (DWUG EN v3.0.0, Zenodo 14028531; pinned 2026-05-30,
# byte-identical to the v1 freeze).
EXPECTED_ZIP_SHA256 = "64eef477154b82cb27925ab4ea8c030a8e23840b538dd06b6464aa1e55af2dbf"

FULLTEXT = os.path.join(DWUG_DIR, "lexical_rep2_fulltext.jsonl")  # gitignored, local-only
MANIFEST = os.path.join(HERE, "manifest.csv")                     # committed (no corpus text)
# v1 frozen manifest — the exclusion source (guarantees pair-level disjointness).
V1_MANIFEST = os.path.abspath(os.path.join(
    HERE, "..", "2026-05-30-lexical-sense-gradience-probe-v1", "manifest.csv"))

SEED = 20260705           # rep2: fresh draw, fresh date (v1 was 20260530)
N_PER_LEVEL = 50          # balanced across rounded-median DURel levels 1..4 (unchanged)
MIN_JUDGMENTS = 2         # require >=2 annotator judgments per pair (unchanged)
PER_LEMMA_LEVEL_CAP = 4   # <= this many sampled pairs per (lemma, level) (unchanged)

STOP = set("a an the of to in on at for and or but with from by as is are was were be been "
           "being this that these those it its he she they we you i his her their our your my "
           "him them us not no so if then than too very can could would should will shall may "
           "might must do does did have has had which who whom whose what when where why how "
           "into onto over under up down out off about again more most some any all each".split())


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_v1_pairs():
    """Unordered {id1,id2} pairs frozen in v1 — the exclusion set for disjointness."""
    pairs = set()
    ids = set()
    with open(V1_MANIFEST, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            pairs.add(tuple(sorted((r["id1"], r["id2"]))))
            ids.add(r["id1"])
            ids.add(r["id2"])
    return pairs, ids


def ensure_dwug():
    if not os.path.exists(ZIP_PATH):
        os.makedirs(DWUG_DIR, exist_ok=True)
        print(f"downloading DWUG EN from Zenodo -> {ZIP_PATH} ...")
        urllib.request.urlretrieve(ZENODO_URL, ZIP_PATH)
    h = sha256_file(ZIP_PATH)
    print(f"dwug_en.zip sha256 = {h}")
    assert h == EXPECTED_ZIP_SHA256, f"DWUG archive sha256 mismatch: {h} != {EXPECTED_ZIP_SHA256}"
    if not os.path.isdir(EXTRACT):
        with zipfile.ZipFile(ZIP_PATH) as z:
            z.extractall(DWUG_DIR)
    for root, dirs, _ in os.walk(DWUG_DIR):
        if os.path.basename(root) == "data" and any(
                os.path.isdir(os.path.join(root, d)) for d in dirs):
            return root, h
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
    """Robustly recover the target word span (v1 B1 fix, byte-identical)."""
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


def content_tokens(sentence, target_surface):
    toks = re.findall(r"[a-z]+", sentence.lower())
    tgt = set(re.findall(r"[a-z]+", target_surface.lower()))
    return set(t for t in toks if t not in STOP and t not in tgt and len(t) > 1)


def overlap(s1, t1, s2, t2):
    a, b = content_tokens(s1, t1), content_tokens(s2, t2)
    if not a or not b:
        return 0.0, 0.0
    inter = len(a & b)
    jacc = inter / len(a | b)
    f1 = 2 * inter / (len(a) + len(b))
    return round(jacc, 4), round(f1, 4)


def load_lemma(data_dir, lemma):
    root = lemma.split("_")[0].lower()
    uses = {}
    with open(os.path.join(data_dir, lemma, "uses.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            parts = r["indexes_target_token"].split(":")
            if len(parts) != 2 or not all(p.strip().lstrip("-").isdigit() for p in parts):
                continue
            a, b = int(parts[0]), int(parts[1])
            got = extract_target(r["context"], a, b, root)
            if got is None:
                continue
            s, e, surface = got
            uses[r["identifier"]] = {"context": r["context"], "grouping": r["grouping"],
                                     "span": (s, e), "surface": surface,
                                     "pos": r["pos"], "date": r["date"]}
    pj = defaultdict(list)
    with open(os.path.join(data_dir, lemma, "judgments.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            try:
                j = float(r["judgment"])
            except ValueError:
                continue
            if j == 0:
                continue
            k = tuple(sorted((r["identifier1"], r["identifier2"])))
            pj[k].append(j)
    return uses, pj


def main():
    v1_pairs, v1_ids = load_v1_pairs()
    print(f"v1 exclusion set: {len(v1_pairs)} frozen pairs over {len(v1_ids)} distinct usages")
    data_dir, zip_sha = ensure_dwug()
    lemmas = sorted(d for d in os.listdir(data_dir)
                    if os.path.isdir(os.path.join(data_dir, d)))
    buckets = defaultdict(list)  # level -> list of candidate dicts
    n_excluded = 0
    for lemma in lemmas:
        uses, pj = load_lemma(data_dir, lemma)
        for (x, y), js in pj.items():
            if x not in uses or y not in uses:
                continue
            if tuple(sorted((x, y))) in v1_pairs:   # <-- rep2 disjointness: drop v1's pairs
                n_excluded += 1
                continue
            ux, uy = uses[x], uses[y]
            if ux["grouping"] != uy["grouping"]:
                continue  # Q4 synchronic: within-period only
            if len(js) < MIN_JUDGMENTS:
                continue
            med = statistics.median(js)
            level = round(med)
            if level not in (1, 2, 3, 4):
                continue
            spread = round(max(js) - min(js), 2)
            jacc, f1 = overlap(ux["context"], ux["surface"], uy["context"], uy["surface"])
            buckets[level].append({
                "lemma": lemma, "pos": ux["pos"], "period": ux["grouping"],
                "id1": x, "id2": y, "human_median": med, "human_mean": round(statistics.mean(js), 3),
                "human_n": len(js), "human_spread": spread,
                "overlap_jaccard": jacc, "overlap_tokenf1": f1,
                "ctx1": ux["context"], "span1": ux["span"], "surf1": ux["surface"],
                "ctx2": uy["context"], "span2": uy["span"], "surf2": uy["surface"],
            })
    print(f"excluded {n_excluded} v1 pairs from the candidate pool")
    print("candidate (rep2, v1-excluded) within-period >=2-judgment pairs by level:",
          {lvl: len(buckets[lvl]) for lvl in (1, 2, 3, 4)})

    rng = random.Random(SEED)
    selected = []
    for lvl in (1, 2, 3, 4):
        cands = sorted(buckets[lvl], key=lambda d: (d["lemma"], d["id1"], d["id2"]))
        rng.shuffle(cands)
        per_ll = defaultdict(int)
        picked = []
        for c in cands:
            if len(picked) >= N_PER_LEVEL:
                break
            if per_ll[c["lemma"]] >= PER_LEMMA_LEVEL_CAP:
                continue
            per_ll[c["lemma"]] += 1
            picked.append(c)
        if len(picked) < N_PER_LEVEL:  # relax cap if a level is short
            for c in cands:
                if len(picked) >= N_PER_LEVEL:
                    break
                if c not in picked:
                    picked.append(c)
        selected.extend(picked)
        print(f"  level {lvl}: selected {len(picked)} (from {len(cands)}; "
              f"{len(set(c['lemma'] for c in picked))} lemmas)")

    # B2 span-sanity gate (byte-identical to v1)
    for c in selected:
        root = c["lemma"].split("_")[0].lower()
        assert stem_match(c["surf1"], root) and stem_match(c["surf2"], root), \
            f"span-sanity fail {c['id1']}/{c['id2']} root={root} surf=({c['surf1']!r},{c['surf2']!r})"

    # DISJOINTNESS ASSERT: no selected pair may appear in v1.
    for c in selected:
        assert tuple(sorted((c["id1"], c["id2"]))) not in v1_pairs, \
            f"disjointness fail: {c['id1']}/{c['id2']} is a v1 pair"

    # usage-level overlap with v1 (reported, not gated — the item is a PAIR; pairs are disjoint)
    sel_usages = set()
    for c in selected:
        sel_usages.add(c["id1"])
        sel_usages.add(c["id2"])
    shared_usages = sel_usages & v1_ids
    print(f"\nDISJOINTNESS: 0 shared PAIRS with v1 (asserted). "
          f"Usage-level overlap (reported): {len(shared_usages)}/{len(sel_usages)} usages "
          f"also appear in some v1 pair (a usage can recombine into a fresh pair; the probed "
          f"item is the pair, and every pair is fresh).")

    # stable item ids
    selected.sort(key=lambda d: (d["human_median"], d["lemma"], d["id1"], d["id2"]))
    for i, c in enumerate(selected):
        c["item_id"] = f"lx-{c['human_median']:.0f}-{i:03d}"

    man_cols = ["item_id", "lemma", "pos", "period", "id1", "id2",
                "human_median", "human_mean", "human_n", "human_spread",
                "overlap_jaccard", "overlap_tokenf1"]
    with open(MANIFEST, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=man_cols)
        w.writeheader()
        for c in selected:
            w.writerow({k: c[k] for k in man_cols})
    man_sha = sha256_file(MANIFEST)

    with open(FULLTEXT, "w", encoding="utf-8") as f:
        for c in selected:
            f.write(json.dumps({
                "item_id": c["item_id"], "lemma": c["lemma"],
                "ctx1": c["ctx1"], "span1": list(c["span1"]), "surf1": c["surf1"],
                "ctx2": c["ctx2"], "span2": list(c["span2"]), "surf2": c["surf2"],
                "human_median": c["human_median"], "human_n": c["human_n"],
            }) + "\n")

    print(f"\nwrote {len(selected)} items")
    print(f"  manifest (committed, no corpus text): {MANIFEST}")
    print(f"  full-text (gitignored, local-only):   {FULLTEXT}")
    print(f"  lemmas covered: {len(set(c['lemma'] for c in selected))}")
    print(f"  archive sha256: {zip_sha}")
    print(f"  MANIFEST sha256 (FREEZE HASH): {man_sha}")


if __name__ == "__main__":
    main()
