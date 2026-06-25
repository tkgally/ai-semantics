#!/usr/bin/env python3
"""Draw the stratified N=120 run set from the scored 200-pool (design B.6 steps 2-3).

Reads raw/pool_text.json (the descriptor-based TEXT arm over the 200 pool items x 3 models),
computes the per-item separability covariate

    sep_i = fraction of the 3 panel models correct in the descriptor TEXT arm  (0, 1/3, 2/3, 1)

partitions the pool into strata, and draws a seeded N=120 that OVERSAMPLES the predicted-small
under-determined band so it has a real chance to clear the >=15 per-stratum floor (design B.5):

    under-determined  U: sep_i <= 1/3
    saturated         S: sep_i == 1
    intermediate      M: sep_i == 2/3   (counted in neither floor bin; carries the continuous read)

Draw rule (seeded 20260625, deterministic): take up to 45 under-determined items (3x the floor,
generous oversampling), then fill to 120 from S then M (saturated first, so the saturated floor is
met whenever the pool supplies >=15 saturated). Freezes:
    frozen/run_items.json   the 120 items (with their frozen sep_i + stratum)
    raw/text.json           the per-item / per-model TEXT covariate for exactly those 120

ALL of this is text-only and runs BEFORE any image arm (design condition b — no image result can
retune the draw or the covariate). Reports the stratum counts and whether each reported bin clears
the >=15 floor; a bin below floor means the binned interaction is NOT credited next session (the
analysis falls back to the continuous + rescue + distraction-null reads), per design.
"""
import json, os, hashlib, random
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
POOL = os.path.join(HERE, "frozen", "pool_items.json")
POOL_TEXT = os.path.join(HERE, "raw", "pool_text.json")
RUN_ITEMS = os.path.join(HERE, "frozen", "run_items.json")
TEXT = os.path.join(HERE, "raw", "text.json")
SEED = 20260625
N = 120
U_CAP = 45      # oversample cap for the under-determined band (3x the >=15 floor)
FLOOR = 15
MODELS = ("claude", "gpt", "gemini")

def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()

def main():
    pool = json.load(open(POOL))
    recs = json.load(open(POOL_TEXT))
    # sep_i per item = fraction of the 3 models correct (None counts as incorrect)
    by_item = defaultdict(dict)
    for r in recs:
        by_item[r["item_id"]][r["model"]] = bool(r["correct"])
    sep = {}
    for it in pool:
        c = by_item.get(it["id"], {})
        sep[it["id"]] = sum(1 for m in MODELS if c.get(m)) / len(MODELS)

    U = sorted(it["id"] for it in pool if sep[it["id"]] <= 1/3 + 1e-9)
    S = sorted(it["id"] for it in pool if abs(sep[it["id"]] - 1.0) < 1e-9)
    M = sorted(it["id"] for it in pool if abs(sep[it["id"]] - 2/3) < 1e-9)
    rng = random.Random(SEED)
    for g in (U, S, M):
        rng.shuffle(g)

    take_U = U[:U_CAP]
    need = N - len(take_U)
    fill_order = S + M  # saturated first
    take_fill = fill_order[:need]
    chosen_ids = set(take_U) | set(take_fill)
    if len(chosen_ids) < N:
        # pool smaller than 120 in S+M+U_cap (shouldn't happen with 200 pool); take all
        print(f"  WARNING: only {len(chosen_ids)} items available (< {N})")

    pool_by_id = {it["id"]: it for it in pool}
    chosen = []
    for iid in sorted(chosen_ids):
        it = dict(pool_by_id[iid])
        it["sep_i"] = sep[iid]
        it["stratum"] = ("under-determined" if sep[iid] <= 1/3 + 1e-9
                         else "saturated" if abs(sep[iid] - 1.0) < 1e-9
                         else "intermediate")
        chosen.append(it)

    json.dump(chosen, open(RUN_ITEMS, "w"), indent=2)
    # freeze the covariate (TEXT records) for exactly the chosen 120
    text_recs = [r for r in recs if r["item_id"] in chosen_ids]
    json.dump(text_recs, open(TEXT, "w"), indent=2)

    n_u = sum(1 for it in chosen if it["stratum"] == "under-determined")
    n_s = sum(1 for it in chosen if it["stratum"] == "saturated")
    n_m = sum(1 for it in chosen if it["stratum"] == "intermediate")
    print(f"POOL sep distribution: U(<=1/3)={len(U)}  M(2/3)={len(M)}  S(=1)={len(S)}  (n={len(pool)})")
    print(f"DRAW n={len(chosen)}  under-determined={n_u}  intermediate={n_m}  saturated={n_s}")
    print(f"  floor >= {FLOOR}:  under-determined {'PASS' if n_u>=FLOOR else 'FAIL'}  "
          f"saturated {'PASS' if n_s>=FLOOR else 'FAIL'}")
    if n_u < FLOOR:
        print("  -> binned interaction NOT credited next session; fall back to continuous + "
              "rescue + distraction-null reads (design B.5 / analysis).")
    print(f"wrote {RUN_ITEMS}  sha256={sha(RUN_ITEMS)}")
    print(f"wrote {TEXT}  sha256={sha(TEXT)}  ({len(text_recs)} records)")

if __name__ == "__main__":
    main()
