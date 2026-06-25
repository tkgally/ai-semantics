#!/usr/bin/env python3
"""Freeze the VWSD English gold-test item set for the grounding-headroom probe.

Reads the committed annotation overlay (frozen/en.test.data.v1.1.txt + gold), emits
frozen/items.json with a stable sha256. Each item:
  {id, word, phrase, candidates:[10 image names], gold_name, gold_idx (1-based)}

Anchors ONLY to the gold test split (463 EN). The training split is silver and is not
an anchor (resource/vwsd-semeval-2023). Images are referenced by name only; the bytes
live out of git in $VWSD_IMAGES.
"""
import json, os, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "frozen", "en.test.data.v1.1.txt")
GOLD = os.path.join(HERE, "frozen", "en.test.gold.v1.1.txt")
OUT = os.path.join(HERE, "frozen", "items.json")

def build():
    data = [l.rstrip("\n").split("\t") for l in open(DATA, encoding="utf-8") if l.strip()]
    gold = [l.strip() for l in open(GOLD, encoding="utf-8") if l.strip()]
    assert len(data) == len(gold) == 463, (len(data), len(gold))
    items = []
    for i, (row, g) in enumerate(zip(data, gold)):
        word, phrase = row[0], row[1]
        cands = row[2:]
        assert len(cands) == 10, (i, len(cands))
        assert g in cands, (i, g)
        items.append({
            "id": f"en-{i:03d}",
            "word": word,
            "phrase": phrase,
            "candidates": cands,
            "gold_name": g,
            "gold_idx": cands.index(g) + 1,  # 1-based, matches prompt numbering
        })
    json.dump(items, open(OUT, "w"), indent=2)
    sha = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    # gold-position balance check (humans randomized the gold slot among 10)
    from collections import Counter
    pos = Counter(it["gold_idx"] for it in items)
    print(f"wrote {OUT}  n={len(items)}  sha256={sha}")
    print(f"gold-position distribution (1..10): {[pos[k] for k in range(1, 11)]}")
    print(f"unique candidate images: {len({c for it in items for c in it['candidates']})}")

if __name__ == "__main__":
    build()
