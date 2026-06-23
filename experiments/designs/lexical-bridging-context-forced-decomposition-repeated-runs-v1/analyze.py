"""De-noise gpt's forced-decomposition commitment posture from K repeated temp-0 runs.

Reads raw/run{k}_c_third.json (DECLINE axis -- the disputed one) and raw/run{k}_b_conf.json
(CONFIDENCE axis) for k=1..K and computes the pre-registered resolver objects (see PREREG.md):

DECLINE (c_third):
  - per-run %UNCLEAR per class (bridging / clear-same / clear-different)
  - K-draw range on bridging decline; whether it spans the s82 (2/24=8.3%) and s82b (0/24)
    point estimates (-> the disagreement is run-to-run jitter)
  - per-bridging-item UNCLEAR-count over K, and churn (fraction whose UNCLEAR status varies)
  - de-noised MAJORITY-VOTE bridging decline (UNCLEAR in > K/2 runs) + Wilson + lemma-clustered
    bootstrap CI
  - mean pairwise agreement of the UNCLEAR label across the C(K,2) run pairs
CONFIDENCE (b_conf):
  - per-run mean confidence per class; pooled bridging vs clear-same difference + clustered CI
    (CI includes 0 == "no robust crack", the posture both s82 and s82b agreed on)
Plus the clear-class precondition per run and the PREREG verdict.

No API. Run after repeated_probe.py. Reads only the sanitized fields (no corpus text).
"""
import json
import math
import os
import random
from collections import defaultdict
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
K = int(os.environ.get("KRUNS", "5"))
SEED = 20260623
BOOT = 10000
CLASSES = ["clear-same", "bridging", "clear-different"]


def load(fr):
    runs = []
    for k in range(1, K + 1):
        runs.append(json.load(open(os.path.join(RAW, f"run{k}_{fr}.json"), encoding="utf-8")))
    return runs


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def clustered_ci(by_lemma, stat, reps=BOOT, seed=SEED):
    lemmas = list(by_lemma.keys())
    rng = random.Random(seed)
    vals = []
    for _ in range(reps):
        pooled = []
        for _ in lemmas:
            pooled += by_lemma[rng.choice(lemmas)]
        vals.append(stat(pooled))
    vals.sort()
    return (round(vals[int(0.025 * len(vals))], 4), round(vals[int(0.975 * len(vals))], 4))


def main():
    out = {"k": K, "seed": SEED, "reps": BOOT}

    # ---- DECLINE axis (c_third) ----
    c = load("c_third")
    ids = [r["item_id"] for r in c[0]]
    cls = {r["item_id"]: r["bridging_class"] for r in c[0]}
    lem = {r["item_id"]: r["lemma"] for r in c[0]}
    # label[item_id] = list over K of (pred == "UNCLEAR")
    unclear = defaultdict(list)
    pred = defaultdict(list)
    for run in c:
        for r in run:
            unclear[r["item_id"]].append(r["pred"] == "UNCLEAR")
            pred[r["item_id"]].append(r["pred"])

    per_run_decline = {cl: [] for cl in CLASSES}
    for run in c:
        cnt = {cl: [0, 0] for cl in CLASSES}
        for r in run:
            cl = r["bridging_class"]
            cnt[cl][1] += 1
            if r["pred"] == "UNCLEAR":
                cnt[cl][0] += 1
        for cl in CLASSES:
            per_run_decline[cl].append(round(100 * cnt[cl][0] / cnt[cl][1], 1))
    out["decline_per_run_pct"] = per_run_decline
    out["decline_range_pct"] = {cl: round(max(v) - min(v), 1) for cl, v in per_run_decline.items()}

    bridging_ids = [i for i in ids if cls[i] == "bridging"]
    n_br = len(bridging_ids)
    # per-item UNCLEAR count over K
    item_unclear_count = {i: sum(unclear[i]) for i in bridging_ids}
    out["bridging_n_items"] = n_br
    # keyed by lemma+item_id so duplicate-lemma bridging items do not collide in display
    out["bridging_item_unclear_count_over_K"] = {
        f"{lem[i]} ({i})": item_unclear_count[i]
        for i in sorted(bridging_ids, key=lambda x: -item_unclear_count[x])
        if item_unclear_count[i] > 0} or "all 0/K"
    out["bridging_churn"] = {
        "n_churned": sum(1 for i in bridging_ids if 0 < item_unclear_count[i] < K),
        "frac": round(sum(1 for i in bridging_ids if 0 < item_unclear_count[i] < K) / n_br, 3)}

    # de-noised majority-vote decline (UNCLEAR in > K/2 runs)
    modal_unclear = {i: item_unclear_count[i] > K / 2 for i in bridging_ids}
    k_modal = sum(modal_unclear.values())
    wl, wh = wilson(k_modal, n_br)
    by_lemma_dec = defaultdict(list)
    for i in bridging_ids:
        by_lemma_dec[lem[i]].append(1.0 if modal_unclear[i] else 0.0)
    cl_lo, cl_hi = clustered_ci(by_lemma_dec, lambda xs: sum(xs) / len(xs))
    out["bridging_majority_vote_decline"] = {
        "k_unclear_modal": k_modal, "n": n_br, "pct": round(100 * k_modal / n_br, 1),
        "wilson95": [round(wl, 4), round(wh, 4)],
        "lemma_clustered_boot95": [cl_lo, cl_hi]}

    # mean pairwise agreement on the UNCLEAR label across run pairs (bridging)
    agrees = []
    for a, b in combinations(range(K), 2):
        same = sum(1 for i in bridging_ids if unclear[i][a] == unclear[i][b])
        agrees.append(same / n_br)
    out["bridging_mean_pairwise_unclear_agreement"] = round(sum(agrees) / len(agrees), 4)

    # does the K-draw range span the s82 (8.3%) and s82b (0.0%) bridging point estimates?
    br = per_run_decline["bridging"]
    out["spans_s82_s82b"] = {
        "draws_pct": br, "min": min(br), "max": max(br),
        "s82_8.3_in_range": min(br) <= 8.3 <= max(br),
        "s82b_0.0_in_range": min(br) <= 0.0 <= max(br)}

    # ---- CONFIDENCE axis (b_conf) ----
    bc = load("b_conf")
    conf_per_run = {cl: [] for cl in CLASSES}
    by_lemma_conf = {cl: defaultdict(list) for cl in CLASSES}
    # pooled per-item mean confidence over K, by class+lemma
    conf_acc = defaultdict(list)
    cls_b = {r["item_id"]: r["bridging_class"] for r in bc[0]}
    lem_b = {r["item_id"]: r["lemma"] for r in bc[0]}
    for run in bc:
        agg = {cl: [] for cl in CLASSES}
        for r in run:
            v = r.get("pred2")
            if v is not None:
                agg[r["bridging_class"]].append(v)
                conf_acc[r["item_id"]].append(v)
        for cl in CLASSES:
            conf_per_run[cl].append(round(sum(agg[cl]) / len(agg[cl]), 1) if agg[cl] else None)
    out["confidence_per_run_mean"] = conf_per_run
    out["confidence_range"] = {
        cl: round(max(v) - min(v), 1) for cl, v in conf_per_run.items() if all(x is not None for x in v)}
    # pooled per-item mean conf -> bridging vs clear-same difference + clustered CI
    item_conf = {i: sum(vs) / len(vs) for i, vs in conf_acc.items() if vs}
    for i, v in item_conf.items():
        by_lemma_conf[cls_b[i]][lem_b[i]].append(v)
    def lemma_mean(by_lemma):
        # mean over items, returns function-ready pooled list of per-item means
        pooled = []
        for vs in by_lemma.values():
            pooled += vs
        return pooled
    br_conf = lemma_mean(by_lemma_conf["bridging"])
    cs_conf = lemma_mean(by_lemma_conf["clear-same"])
    out["confidence_pooled_means"] = {
        "bridging": round(sum(br_conf) / len(br_conf), 2),
        "clear-same": round(sum(cs_conf) / len(cs_conf), 2)}
    # clustered bootstrap on (bridging - clear-same) pooled per-item mean confidence
    rng = random.Random(SEED + 1)
    br_lem = list(by_lemma_conf["bridging"].keys())
    cs_lem = list(by_lemma_conf["clear-same"].keys())
    diffs = []
    for _ in range(BOOT):
        bp = []
        for _ in br_lem:
            bp += by_lemma_conf["bridging"][rng.choice(br_lem)]
        cp = []
        for _ in cs_lem:
            cp += by_lemma_conf["clear-same"][rng.choice(cs_lem)]
        diffs.append(sum(bp) / len(bp) - sum(cp) / len(cp))
    diffs.sort()
    d_lo, d_hi = diffs[int(0.025 * BOOT)], diffs[int(0.975 * BOOT)]
    out["confidence_bridging_minus_clearsame_diff95"] = [round(d_lo, 2), round(d_hi, 2)]
    out["confidence_robust_crack"] = bool(d_hi < 0)  # CI strictly below 0 == robust crack

    # ---- clear-class precondition per run ----
    out["clear_class_precondition_per_run"] = {
        "clear_same_decline_pct": per_run_decline["clear-same"],
        "clear_diff_decline_pct": per_run_decline["clear-different"],
        "clear_same_conf_mean": conf_per_run["clear-same"],
        "clear_diff_conf_mean": conf_per_run["clear-different"],
        "all_runs_decline_lt20_conf_gt70": all(
            per_run_decline["clear-same"][k] < 20 and per_run_decline["clear-different"][k] < 20
            and (conf_per_run["clear-same"][k] or 0) > 70 and (conf_per_run["clear-different"][k] or 0) > 70
            for k in range(K))}

    # ---- PREREG verdict ----
    modal_pct = 100 * k_modal / n_br
    clear_modal_max = 0  # de-noised clear-class decline (modal) for elevation check
    for cl in ("clear-same", "clear-different"):
        ids_cl = [i for i in ids if cls[i] == cl]
        cm = sum(1 for i in ids_cl if sum(unclear[i]) > K / 2)
        clear_modal_max = max(clear_modal_max, 100 * cm / len(ids_cl))
    out["clear_class_majority_decline_pct_max"] = round(clear_modal_max, 1)
    if k_modal <= 1 and not (cl_lo > clear_modal_max / 100):
        verdict = ("NULL/CHANNEL-CONTROLLED de-noised: bridging majority-vote decline ~0 "
                   "and not robustly elevated over clear classes -- the s82 MIXED/WEAK 2/24 "
                   "was reading run-to-run jitter; the s82b null is the de-noised truth.")
    elif cl_lo > clear_modal_max / 100:
        verdict = ("MIXED/WEAK de-noised: bridging majority-vote decline robustly elevated "
                   "over clear classes -- the s82 reading survives de-noising.")
    else:
        verdict = ("INDETERMINATE at this K: bridging modal decline is small but its clustered "
                   "CI does not separate cleanly from the clear classes -- report the band.")
    out["VERDICT"] = verdict

    json.dump(out, open(os.path.join(HERE, "analysis.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
