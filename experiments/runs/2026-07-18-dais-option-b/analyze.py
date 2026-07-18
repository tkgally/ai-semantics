#!/usr/bin/env python3
"""analyze.py -- post-run analysis for the DAIS Option-B graded-preference correlation probe (s248).

Reads ONLY raw/probe-{A,B}-<model>.jsonl (model preferences) + human_targets.json (human gradient)
+ freq_control.json (B2). Recomputes every figure from raw; a post-run verifier re-runs this to
reproduce. All bands + thresholds are FROZEN in PREREG.md; this script assigns them mechanically
(S3 deterministic decision-tree). Nothing here is tuned after seeing the numbers.
"""
import json
import os

import numpy as np
from scipy.stats import spearmanr, binomtest, rankdata

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
HT = json.load(open(os.path.join(HERE, "human_targets.json")))
FREQ = json.load(open(os.path.join(HERE, "freq_control.json")))
CONDS = HT["condition_order"]
HUM_RANKS = HT["human_direction_ranks"]
RHO_THR = HT["armb_rho_threshold"]
P0 = HT["armb_null_p0"]
CEILING = 0.95
RNG = np.random.default_rng(20260718)
NBOOT = 10000


def load_arm(arm):
    out = {}
    for name in C.MODELS:
        rows = C.read_jsonl(os.path.join(C.RAW, f"probe-{arm}-{name}.jsonl"))
        out[name] = rows
    return out


def boot_ci_spearman(x, y, nboot=NBOOT):
    x, y = np.asarray(x, float), np.asarray(y, float)
    n = len(x)
    rho = spearmanr(x, y).statistic
    idx = RNG.integers(0, n, size=(nboot, n))
    bs = np.array([spearmanr(x[i], y[i]).statistic for i in idx])
    bs = bs[~np.isnan(bs)]
    lo, hi = np.percentile(bs, [2.5, 97.5])
    return float(rho), float(lo), float(hi)


def partial_spearman(model, human, classif, rank):
    """Partial Spearman rho(model, human | classification, within-class freq rank). Rank-transform
    all, regress out the covariates linearly, correlate residuals (Pearson on ranks)."""
    m = rankdata(model); h = rankdata(human)
    cls = np.array([1.0 if c == "alternating" else 0.0 for c in classif])
    rk = rankdata(rank)
    Z = np.column_stack([np.ones_like(m), cls, rk])
    def resid(y):
        beta, *_ = np.linalg.lstsq(Z, y, rcond=None)
        return y - Z @ beta
    rm, rh = resid(m), resid(h)
    if rm.std() == 0 or rh.std() == 0:
        return float("nan")
    return float(np.corrcoef(rm, rh)[0, 1])


def arm_a():
    data = load_arm("A")
    hum_matched = HT["human_arma_matched"]
    hum_collapsed = HT["human_arma_collapsed"]
    res = {}
    for name, rows in data.items():
        pref = {r["verb"]: r["doc_pref"] for r in rows if r["doc_pref"] is not None}
        verbs = [v for v in sorted(hum_matched) if v in pref]
        na = 200 - len(verbs)
        mv = [pref[v] for v in verbs]
        hv = [hum_matched[v] for v in verbs]
        rho, lo, hi = boot_ci_spearman(mv, hv)
        # robustness: vs collapsed human mean
        rho_c, lo_c, hi_c = boot_ci_spearman(mv, [hum_collapsed[v] for v in verbs])
        # B2 control: alternating-only rho
        alt = [v for v in verbs if FREQ[v]["classification"] == "alternating"]
        mva = [pref[v] for v in alt]; hva = [hum_matched[v] for v in alt]
        rho_alt, lo_alt, hi_alt = boot_ci_spearman(mva, hva)
        # B2 control: partial rho | classification + within-class freq rank
        pr = partial_spearman(mv, hv, [FREQ[v]["classification"] for v in verbs],
                              [FREQ[v]["frequency_rank_within_class"] for v in verbs])
        res[name] = {
            "n_verbs": len(verbs), "n_na": na,
            "rho_matched": rho, "ci_matched": [lo, hi], "ci_lb_gt0": bool(lo > 0),
            "rho_collapsed": rho_c, "ci_collapsed": [lo_c, hi_c],
            "rho_alternating_only": rho_alt, "ci_alt": [lo_alt, hi_alt],
            "alt_ci_lb_gt0": bool(lo_alt > 0), "n_alt": len(alt),
            "partial_rho_freqclass": pr,
            "contamination_ceiling": bool(rho >= CEILING),
        }
    return res


def arm_b():
    data = load_arm("B")
    hum = HT["human_armb"]; verbs = HT["armb_verbs"]
    res = {}
    for name, rows in data.items():
        cell = {}
        for r in rows:
            if r["doc_pref"] is not None:
                cell[(r["verb"], r["condition"])] = r["doc_pref"]
        successes = 0; used = 0; rhos = []
        short_c = []; long_c = []
        for v in verbs:
            vals = [cell.get((v, c)) for c in CONDS]
            if any(x is None for x in vals):
                continue
            used += 1
            rs = spearmanr(vals, HUM_RANKS).statistic
            rhos.append(rs)
            if not np.isnan(rs) and rs >= RHO_THR:
                successes += 1
            # within-length definiteness contrasts (index: pronoun0 shortDef1 shortIndef2 longDef3 longIndef4)
            short_c.append(vals[1] - vals[2])   # shortDef - shortIndef
            long_c.append(vals[3] - vals[4])    # longDef - longIndef
        rate = successes / used if used else float("nan")
        binom_p = binomtest(successes, used, P0, alternative="greater").pvalue if used else 1.0
        sc = np.array(short_c); lc = np.array(long_c)
        def mean_ci(a):
            m = float(a.mean())
            idx = RNG.integers(0, len(a), size=(NBOOT, len(a)))
            bs = a[idx].mean(axis=1)
            return m, float(np.percentile(bs, 2.5)), float(np.percentile(bs, 97.5))
        sm, slo, shi = mean_ci(sc); lm, llo, lhi = mean_ci(lc)
        res[name] = {
            "n_verbs_used": used, "successes": successes, "monotonicity_rate": rate,
            "binom_p_vs_p0": float(binom_p), "beats_chance": bool(binom_p < 0.05),
            "mean_rho_s": float(np.nanmean(rhos)),
            "short_contrast_mean": sm, "short_ci": [slo, shi],
            "long_contrast_mean": lm, "long_ci": [llo, lhi],
            "within_length_pass": bool(slo > 0 and llo > 0),
            "5cond_dir_rho": float(spearmanr(
                [np.mean([cell[(v, c)] for v in verbs if (v, c) in cell]) for c in CONDS],
                HUM_RANKS).statistic),
        }
    return res


def decide(a, b):
    """S3 deterministic band-assignment decision-tree (identical wording in PREREG)."""
    n = lambda pred: sum(1 for m in C.MODELS if pred(m))
    armA_full = n(lambda m: a[m]["ci_lb_gt0"]) >= 2
    armA_ctrl = n(lambda m: a[m]["alt_ci_lb_gt0"]) >= 2         # B2 binding control
    armB_mono = n(lambda m: b[m]["beats_chance"]) >= 2
    armB_within = n(lambda m: b[m]["within_length_pass"]) >= 2  # binding definiteness control
    ceiling = any(a[m]["contamination_ceiling"] for m in C.MODELS)
    if armB_mono and armB_within:
        band = "TRACKS-HUMAN-SURFACE" if (armA_full and armA_ctrl) else "SURFACE-ONLY"
    elif armB_mono and not armB_within:
        band = "LENGTH-ONLY"
    elif armA_full and not armB_mono:
        band = "VERB-BIAS-ONLY" + ("" if armA_ctrl else " (may be lexical)")
    else:
        band = "DECOUPLED-OR-NULL"
    return {"band": band, "contamination_ceiling_flag": ceiling,
            "gates": {"armA_full_ci_lb_gt0_ge2of3": armA_full,
                      "armA_alt_control_ge2of3": armA_ctrl,
                      "armB_monotonicity_beats_chance_ge2of3": armB_mono,
                      "armB_within_length_definiteness_ge2of3": armB_within}}


def main():
    a = arm_a(); b = arm_b(); d = decide(a, b)
    out = {"arm_A": a, "arm_B": b, "verdict": d,
           "frozen": {"armb_rho_threshold": RHO_THR, "armb_null_p0": P0,
                      "contamination_ceiling_rho": CEILING,
                      "canonical_arma_condition": HT["canonical_arma_condition"]}}
    json.dump(out, open(os.path.join(HERE, "analysis.json"), "w"), indent=2)
    print(f"=== VERDICT: {d['band']}  (contamination-ceiling flag: {d['contamination_ceiling_flag']}) ===")
    print("gates:", json.dumps(d["gates"]))
    print("\nArm A (per-verb DO-pref vs human, matched condition):")
    for m in C.MODELS:
        r = a[m]
        print(f"  {m}: rho_matched={r['rho_matched']:+.3f} CI[{r['ci_matched'][0]:+.3f},"
              f"{r['ci_matched'][1]:+.3f}] | alt-only={r['rho_alternating_only']:+.3f} "
              f"CI-LB>0={r['alt_ci_lb_gt0']} | partial={r['partial_rho_freqclass']:+.3f} "
              f"| ceiling={r['contamination_ceiling']} (n={r['n_verbs']},NA={r['n_na']})")
    print("\nArm B (recipient definiteness/length gradient):")
    for m in C.MODELS:
        r = b[m]
        print(f"  {m}: mono_rate={r['monotonicity_rate']:.3f} ({r['successes']}/{r['n_verbs_used']}) "
              f"binom_p={r['binom_p_vs_p0']:.4f} beats_chance={r['beats_chance']} | "
              f"shortDef-Indef={r['short_contrast_mean']:+.3f} CI[{r['short_ci'][0]:+.3f},"
              f"{r['short_ci'][1]:+.3f}] longDef-Indef={r['long_contrast_mean']:+.3f} "
              f"within_pass={r['within_length_pass']}")


if __name__ == "__main__":
    main()
