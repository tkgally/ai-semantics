"""EXPLORATION (no model calls) — survey the WiC homonym pool under the WordNet
lexicographer-file + hypernym stratification rule (gate Q2, the WordNet-preferred form
Tom endorsed this round). NOT the frozen build; this is to size the homonym pool and
decide N before freezing build_items.py.

WordNet structural rule (per gate Q2, the preferred WordNet form):
  For a (lemma, POS), take its WordNet synsets. Cluster them: two senses are RELATED if
  their lowest common hypernym is below the unique-beginner (root) level; DISTINCT if their
  only common ancestor is a unique beginner (root) or there is none. A lemma is a
  HOMONYM CANDIDATE if its senses fall into >=2 mutually-distinct clusters spanning >=2
  lexicographer files (lexnames); a POLYSEME CANDIDATE if all senses form one related
  cluster. (The etymology AND-condition the gate names is applied by hand to the candidate
  list afterwards, to demote known single-origin metaphorical extensions; this script only
  computes the structural signal + WiC item availability.)
"""
import csv
import hashlib
import os
import urllib.request
import zipfile
from collections import defaultdict

import nltk
for pkg in ("wordnet", "omw-1.4"):
    try:
        nltk.data.find(f"corpora/{pkg}")
    except LookupError:
        nltk.download(pkg, quiet=True)
from nltk.corpus import wordnet as wn  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
WIC_DIR = os.path.abspath(os.path.join(HERE, "..", "..", "data", "wic"))
ZIP_PATH = os.path.join(WIC_DIR, "WiC_dataset.zip")
WIC_URL = "https://pilehvar.github.io/wic/package/WiC_dataset.zip"
EXPECTED_ZIP_SHA256 = "f1a2fb67d903c5b9b1180f1035d4228f7c0254e8f5f868d556235457046bd4b2"


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ensure_wic():
    if not os.path.exists(ZIP_PATH):
        os.makedirs(WIC_DIR, exist_ok=True)
        print(f"downloading WiC -> {ZIP_PATH}")
        urllib.request.urlretrieve(WIC_URL, ZIP_PATH)
    h = sha256_file(ZIP_PATH)
    print(f"WiC_dataset.zip sha256 = {h}")
    assert h == EXPECTED_ZIP_SHA256, f"sha256 mismatch! got {h}"
    extract = os.path.join(WIC_DIR, "extracted")
    if not os.path.isdir(extract):
        with zipfile.ZipFile(ZIP_PATH) as z:
            z.extractall(extract)
    return extract


def load_wic(extract):
    """Return list of items: dict(target, pos, idx1, idx2, ctx1, ctx2, gold, split)."""
    items = []
    for split in ("train", "dev", "test"):
        base = os.path.join(extract, split, split)
        data_f = base + ".data.txt"
        gold_f = base + ".gold.txt"
        if not os.path.exists(data_f):
            # some zips nest differently; search
            for root, _, files in os.walk(extract):
                for fn in files:
                    if fn == f"{split}.data.txt":
                        data_f = os.path.join(root, fn)
                    if fn == f"{split}.gold.txt":
                        gold_f = os.path.join(root, fn)
        with open(data_f, encoding="utf-8") as df, open(gold_f, encoding="utf-8") as gf:
            for dl, gl in zip(df, gf):
                p = dl.rstrip("\n").split("\t")
                if len(p) < 5:
                    continue
                tw, pos, idx, c1, c2 = p[0], p[1], p[2], p[3], p[4]
                i1, i2 = idx.split("-")
                items.append({"target": tw, "pos": pos, "idx1": int(i1),
                              "idx2": int(i2), "ctx1": c1, "ctx2": c2,
                              "gold": gl.strip(), "split": split})
    return items


POS_MAP = {"N": wn.NOUN, "V": wn.VERB}


def root_distinct(s1, s2):
    """True if s1,s2 share no hypernym below a unique-beginner (root) synset."""
    lch = s1.lowest_common_hypernyms(s2)
    if not lch:
        return True
    return all(h.min_depth() == 0 for h in lch)


def cluster_synsets(synsets):
    """Union-find: merge senses that are RELATED (share a non-root hypernym)."""
    n = len(synsets)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        parent[find(a)] = find(b)

    for i in range(n):
        for j in range(i + 1, n):
            if not root_distinct(synsets[i], synsets[j]):
                union(i, j)
    groups = defaultdict(list)
    for i in range(n):
        groups[find(i)].append(i)
    return list(groups.values())


def classify(lemma, pos_tag):
    wn_pos = POS_MAP[pos_tag]
    syns = wn.synsets(lemma, pos=wn_pos)
    if len(syns) < 2:
        return {"verdict": "MONOSEME_OR_ABSENT", "n_syn": len(syns),
                "n_clusters": len(syns), "lexfiles": sorted({s.lexname() for s in syns})}
    clusters = cluster_synsets(syns)
    lexfiles_per_cluster = [sorted({syns[i].lexname() for i in c}) for c in clusters]
    all_lexfiles = sorted({s.lexname() for s in syns})
    multi = len(clusters) >= 2 and len({lf for cl in lexfiles_per_cluster for lf in cl}) >= 2
    return {"verdict": "HOMONYM_CAND" if multi else "POLYSEME_CAND",
            "n_syn": len(syns), "n_clusters": len(clusters),
            "lexfiles": all_lexfiles,
            "cluster_example_synsets": [[syns[i].name() for i in c[:3]] for c in clusters]}


def main():
    extract = ensure_wic()
    items = load_wic(extract)
    print(f"\nloaded {len(items)} WiC items")
    by_gold = defaultdict(int)
    for it in items:
        by_gold[it["gold"]] += 1
    print("gold balance:", dict(by_gold))

    # availability of T/F items per (lemma, pos)
    avail = defaultdict(lambda: {"T": 0, "F": 0})
    for it in items:
        avail[(it["target"], it["pos"])][it["gold"]] += 1

    # classify each (lemma,pos) that has >=1 F and >=1 T item
    rows = []
    for (lemma, pos), cnt in avail.items():
        c = classify(lemma, pos)
        rows.append({"lemma": lemma, "pos": pos, "nT": cnt["T"], "nF": cnt["F"],
                     **c})

    homo = [r for r in rows if r["verdict"] == "HOMONYM_CAND"]
    poly = [r for r in rows if r["verdict"] == "POLYSEME_CAND"]
    print(f"\n(lemma,pos) keys with >=1 item: {len(rows)}")
    print(f"  HOMONYM_CAND : {len(homo)}")
    print(f"  POLYSEME_CAND: {len(poly)}")

    # the binding resource: homonym candidates with BOTH a T and an F item
    homo_both = sorted([r for r in homo if r["nT"] >= 1 and r["nF"] >= 1],
                       key=lambda r: -(r["nT"] + r["nF"]))
    poly_both = [r for r in poly if r["nT"] >= 1 and r["nF"] >= 1]
    print(f"\nHOMONYM_CAND with >=1 T AND >=1 F item: {len(homo_both)}")
    print(f"  total F items in those: {sum(r['nF'] for r in homo_both)}, "
          f"T items: {sum(r['nT'] for r in homo_both)}")
    print(f"POLYSEME_CAND with >=1 T AND >=1 F item: {len(poly_both)} "
          f"(F={sum(r['nF'] for r in poly_both)}, T={sum(r['nT'] for r in poly_both)})")

    print(f"\n--- all {len(homo_both)} HOMONYM candidates (lemma/pos: nT/nF, "
          f"clusters, lexfiles) ---")
    for r in homo_both:
        print(f"  {r['lemma']:14s} {r['pos']}  T={r['nT']:2d} F={r['nF']:2d}  "
              f"clusters={r['n_clusters']} syn={r['n_syn']:2d}  "
              f"{r['lexfiles']}")

    # write a candidate CSV for the by-hand etymology review
    out = os.path.join(HERE, "raw", "candidates.csv")
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["lemma", "pos", "verdict", "nT", "nF",
                                          "n_syn", "n_clusters", "lexfiles"])
        w.writeheader()
        for r in sorted(rows, key=lambda r: (r["verdict"], -(r["nT"] + r["nF"]))):
            w.writerow({"lemma": r["lemma"], "pos": r["pos"], "verdict": r["verdict"],
                        "nT": r["nT"], "nF": r["nF"], "n_syn": r["n_syn"],
                        "n_clusters": r["n_clusters"], "lexfiles": "|".join(r["lexfiles"])})
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
