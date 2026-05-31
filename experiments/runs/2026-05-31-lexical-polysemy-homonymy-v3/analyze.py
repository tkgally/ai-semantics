"""Lexical-v3 analysis (2026-05-31). Pure-Python (no numpy/scipy).

Tests conjecture/lexical-sense-gradience clause (b) on the homonymy-enriched WiC noun subset.
The human anchor is WiC's BINARY same(T)/different(F)-sense label; the model signal is its graded
relatedness rating r (durel 1-4 / cont 0-100). All indicators FROZEN before computing (no pass bar):

  (P-b-ii) per-stratum same/different SEPARATION: AUC of r against the binary WiC label (T vs F),
           computed SEPARATELY within the HOMONYM stratum and the POLYSEME stratum, plus mean T-F
           gap. Headline = AUC_homonym - AUC_polyseme (predicted POSITIVE: homonym different-sense
           pairs are unrelated => easy to floor => bigger gap). AUC = P(r_T > r_F) + 0.5 P(tie).
  (P-b-i)  separable LOW MODE for homonym F items: among F (different-sense) items, mean r and
           floor-fraction by stratum. Headline = floorfrac_homonymF - floorfrac_polysemeF
           (predicted POSITIVE) and mean_r_homonymF < mean_r_polysemeF.

  Uncertainty: whole-LEMMA label-permutation null (shuffle HOMONYM/POLYSEME labels across whole
  lemmas, preserving clustering) for BOTH headline diffs; bootstrap CI (resample items) on AUC diff.
  Matched control: overlap report by stratum x gold + AUC diff recomputed on the low-overlap subset
  (overlap below the global median), so a "homonyms share fewer context words" artifact is visible.

  Nulls (first-class): N1 no separable homonym low mode (floorfrac diff ~ 0); N2 equal separation
  (AUC diff ~ 0, perm p not significant). Lead with the null if N1/N2 hold.
"""
import csv
import json
import os
import random
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
MANIFEST = os.path.join(HERE, "manifest.csv")
PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
FRAMINGS = ("durel", "cont")
FLOOR = {"durel": 1, "cont": 10}   # pre-registered model-floor (design 5; cont band <=10)
SEED = 20260531
N_PERM = 10000
N_BOOT = 5000


def mean(v):
    return sum(v) / len(v) if v else None


def auc(pos, neg):
    """AUC = P(score(T) > score(F)) + 0.5 P(tie). pos=T scores, neg=F scores."""
    if not pos or not neg:
        return None
    gt = tie = 0
    for a in pos:
        for b in neg:
            if a > b:
                gt += 1
            elif a == b:
                tie += 1
    return (gt + 0.5 * tie) / (len(pos) * len(neg))


def stratum_stats(items, fr):
    """items: list of dicts with stratum, gold, r (the model rating for framing fr)."""
    out = {}
    for s in ("HOMONYM", "POLYSEME"):
        sub = [it for it in items if it["stratum"] == s]
        T = [it["r"] for it in sub if it["gold"] == "T"]
        F = [it["r"] for it in sub if it["gold"] == "F"]
        a = auc(T, F)
        fl = sum(1 for v in F if (v == FLOOR[fr] if fr == "durel" else v <= FLOOR[fr]))
        out[s] = {"nT": len(T), "nF": len(F), "auc": (round(a, 3) if a is not None else None),
                  "mean_T": (round(mean(T), 2) if T else None),
                  "mean_F": (round(mean(F), 2) if F else None),
                  "TF_gap": (round(mean(T) - mean(F), 2) if T and F else None),
                  "floorfrac_F": (round(fl / len(F), 3) if F else None)}
    hd_auc = (out["HOMONYM"]["auc"] - out["POLYSEME"]["auc"]
              if out["HOMONYM"]["auc"] is not None and out["POLYSEME"]["auc"] is not None
              else None)
    hd_floor = (out["HOMONYM"]["floorfrac_F"] - out["POLYSEME"]["floorfrac_F"]
                if out["HOMONYM"]["floorfrac_F"] is not None
                and out["POLYSEME"]["floorfrac_F"] is not None else None)
    return out, hd_auc, hd_floor


def perm_test(items, fr, obs_auc, obs_floor, rng):
    """Whole-lemma label permutation. Returns two-sided p for AUC diff + floor diff."""
    lemmas = sorted(set(it["lemma"] for it in items))
    labels = {l: next(it["stratum"] for it in items if it["lemma"] == l) for l in lemmas}
    lab_list = [labels[l] for l in lemmas]
    ge_auc = ge_floor = valid_auc = valid_floor = 0
    for _ in range(N_PERM):
        perm = lab_list[:]
        rng.shuffle(perm)
        pmap = dict(zip(lemmas, perm))
        pit = [{**it, "stratum": pmap[it["lemma"]]} for it in items]
        _, a, fdiff = stratum_stats(pit, fr)
        if a is not None and obs_auc is not None:
            valid_auc += 1
            if abs(a) >= abs(obs_auc):
                ge_auc += 1
        if fdiff is not None and obs_floor is not None:
            valid_floor += 1
            if abs(fdiff) >= abs(obs_floor):
                ge_floor += 1
    return (round(ge_auc / valid_auc, 4) if valid_auc else None,
            round(ge_floor / valid_floor, 4) if valid_floor else None)


def boot_auc_diff(items, fr, rng):
    """Bootstrap CI for AUC_homonym - AUC_polyseme by resampling items within stratum/gold."""
    pools = defaultdict(list)
    for it in items:
        pools[(it["stratum"], it["gold"])].append(it["r"])
    diffs = []
    for _ in range(N_BOOT):
        rs = {}
        for k, v in pools.items():
            rs[k] = [v[rng.randrange(len(v))] for _ in range(len(v))] if v else []
        ah = auc(rs.get(("HOMONYM", "T"), []), rs.get(("HOMONYM", "F"), []))
        ap = auc(rs.get(("POLYSEME", "T"), []), rs.get(("POLYSEME", "F"), []))
        if ah is not None and ap is not None:
            diffs.append(ah - ap)
    if not diffs:
        return None
    diffs.sort()
    lo = diffs[int(0.025 * len(diffs))]
    hi = diffs[int(0.975 * len(diffs))]
    return [round(lo, 3), round(hi, 3)]


def main():
    man = {r["item_id"]: r for r in csv.DictReader(open(MANIFEST))}
    overlaps = {iid: float(r["overlap_jaccard"]) for iid, r in man.items()}
    ov_sorted = sorted(overlaps.values())
    ov_median = ov_sorted[len(ov_sorted) // 2] if ov_sorted else 0.0

    rng = random.Random(SEED)
    out = {"params": {"FLOOR": FLOOR, "N_PERM": N_PERM, "N_BOOT": N_BOOT, "SEED": SEED,
                      "overlap_median": round(ov_median, 4), "n_items": len(man)},
           "strat_counts": {}, "per_model": {}}
    sc = defaultdict(lambda: {"T": 0, "F": 0, "lemmas": set()})
    for r in man.values():
        sc[r["stratum"]][r["gold"]] += 1
        sc[r["stratum"]]["lemmas"].add(r["lemma"])
    out["strat_counts"] = {s: {"T": d["T"], "F": d["F"], "n_lemmas": len(d["lemmas"])}
                           for s, d in sc.items()}

    # overlap report by stratum x gold
    ovr = defaultdict(list)
    for iid, r in man.items():
        ovr[(r["stratum"], r["gold"])].append(overlaps[iid])
    out["overlap_by_stratum_gold"] = {f"{s}-{g}": round(mean(v), 4)
                                      for (s, g), v in sorted(ovr.items())}

    for slot, name in PANEL.items():
        m = {"model": name}
        for fr in FRAMINGS:
            preds = {r["item_id"]: r["pred"]
                     for r in json.load(open(os.path.join(RAW, f"{fr}_{slot}.json")))
                     if r.get("pred") is not None}
            items = [{"item_id": iid, "lemma": man[iid]["lemma"],
                      "stratum": man[iid]["stratum"], "gold": man[iid]["gold"],
                      "r": preds[iid]} for iid in man if iid in preds]
            stats, hd_auc, hd_floor = stratum_stats(items, fr)
            p_auc, p_floor = perm_test(items, fr, hd_auc, hd_floor, rng)
            boot = boot_auc_diff(items, fr, rng)
            # low-overlap matched subset
            low = [it for it in items if overlaps[it["item_id"]] <= ov_median]
            _, hd_auc_low, hd_floor_low = stratum_stats(low, fr)
            m[fr] = {"n_used": len(items), "by_stratum": stats,
                     "AUC_diff(H-P)": (round(hd_auc, 3) if hd_auc is not None else None),
                     "floorfrac_diff(H-P)": (round(hd_floor, 3) if hd_floor is not None else None),
                     "perm_p_AUC": p_auc, "perm_p_floor": p_floor,
                     "boot95_AUC_diff": boot,
                     "lowoverlap_AUC_diff(H-P)": (round(hd_auc_low, 3)
                                                  if hd_auc_low is not None else None),
                     "lowoverlap_n": len(low)}
        out["per_model"][slot] = m

    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)

    # console
    print("===== LEXICAL v3 — polysemy vs homonymy discreteness (WiC binary anchor) =====")
    print(f"strata: {out['strat_counts']}")
    print(f"overlap median={out['params']['overlap_median']}  "
          f"by stratum/gold: {out['overlap_by_stratum_gold']}")
    for slot, name in PANEL.items():
        print(f"\n[{name}]")
        for fr in FRAMINGS:
            c = out["per_model"][slot][fr]
            h, p = c["by_stratum"]["HOMONYM"], c["by_stratum"]["POLYSEME"]
            print(f"  {fr:5s} n={c['n_used']:3d}  "
                  f"AUC_H={h['auc']}(T{h['nT']}/F{h['nF']}) AUC_P={p['auc']}(T{p['nT']}/F{p['nF']})  "
                  f"AUCdiff={c['AUC_diff(H-P)']} permp={c['perm_p_AUC']} boot95={c['boot95_AUC_diff']}")
            print(f"        floorF_H={h['floorfrac_F']} floorF_P={p['floorfrac_F']} "
                  f"floordiff={c['floorfrac_diff(H-P)']} permp={c['perm_p_floor']}  "
                  f"meanF_H={h['mean_F']} meanF_P={p['mean_F']}  "
                  f"lowoverlap_AUCdiff={c['lowoverlap_AUC_diff(H-P)']}(n={c['lowoverlap_n']})")
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
