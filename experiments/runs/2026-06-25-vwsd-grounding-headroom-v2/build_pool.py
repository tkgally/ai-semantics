#!/usr/bin/env python3
"""Freeze the ~200-item EN-gold POOL for VWSD grounding-headroom v2 (design B.6 step 1).

The pool is a seeded random draw of 200 of the 463 EN gold-test items. The Option-B
visual-form descriptors and the descriptor-based TEXT/separability covariate are computed
over THIS pool (text-only, no model-under-test image arm); the stratified N=120 run set is
then drawn FROM the scored pool by draw_stratified.py. Keeping a 200-pool (vs N=120) gives
the predicted-small under-determined band a real chance to supply >= 15 after stratification
(design Q2 / B.5).

Seed 20260625 (UTC day of the v2 build). Emits frozen/pool_items.json with a stable sha256.
Anchors ONLY to the gold test split (resource/vwsd-semeval-2023).
"""
import json, os, hashlib, random

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.join(HERE, "frozen", "items.json")
OUT = os.path.join(HERE, "frozen", "pool_items.json")
SEED = 20260625
POOL_N = 200

def build():
    items = json.load(open(ITEMS))
    assert len(items) == 463, len(items)
    idx = list(range(len(items)))
    random.Random(SEED).shuffle(idx)
    pool = [items[i] for i in sorted(idx[:POOL_N])]  # sorted by original id for stable order
    json.dump(pool, open(OUT, "w"), indent=2)
    sha = hashlib.sha256(open(OUT, "rb").read()).hexdigest()
    uniq = len({c for it in pool for c in it["candidates"]})
    print(f"wrote {OUT}  n={len(pool)}  seed={SEED}  sha256={sha}")
    print(f"unique candidate images in pool: {uniq}")

if __name__ == "__main__":
    build()
