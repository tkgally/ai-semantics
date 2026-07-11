#!/usr/bin/env python3
"""analyze_partial.py — the BLiMP R1 frequency control (C8, program A3b). Computes the PARTIAL Spearman
of per-paradigm accuracy vs human-agreement CONTROLLING the Q2-A frequency proxy F(p), per model with a
bootstrap CI, plus the collinearity branch (G6), two pre-registered negative controls (G1'), and the G7
proxy-validity audit. Every threshold is FROZEN in PREREG.md and copied here as a constant; nothing is
tuned post-hoc. This is the FIRST point at which F(p) meets the paradigm→H mapping.

Inputs (all frozen upstream):
  results.json (s205)  -> per_model[m].per_paradigm[uid]  (order-averaged accuracy, the frozen record)
  items.json   (s205)  -> paradigms[*].human_agreement    (committed BLiMP per-paradigm human agreement H)
  freq.json    (s208)  -> F_primary[uid], F_sensitivity[uid], audit_* (computed blind to accuracy/H)

Reading (RATIFIED s208, Q1-C / Q2-A / Q3-A + G6/G8): the COVARIATE ARM outcome. Per G8 the covariate arm
alone earns a ROBUSTNESS / CORROBORATION result, never a promotion (the swap arm, deferred, is required
for a promotion). SURVIVES/BREAKS bands and the collinearity guard are frozen below.
"""
import json, math, os
from pathlib import Path
import numpy as np

HERE = Path(__file__).parent
S205 = HERE.parent / "2026-07-10-blimp-forced-choice-sweep"
SLOTS = ["A", "B", "C"]

# ---- FROZEN thresholds (PREREG §V) ----
SURVIVE_MAJ = 2            # SURVIVES iff partial CI excludes 0 on >= this many of 3 models
CORR_LOW = 0.20           # |Spearman(F,H)| < this -> confound ABSENT (corr(F,H)~=0 corroboration branch)
CORR_HIGH = 0.70          # |Spearman(F,H)| > this -> strong collinearity -> INCONCLUSIVE (over-control)
PARTIAL_FLOOR = 0.30      # non-binding SURVIVES floor (the CI-exclusion is the binding gate; df=37 =>
                          #   CI-exclusion already needs partial |rho| ~ 0.325, above this floor)
BOOT = 5000
SEED = 20260711


def rankdata(v):
    v = np.asarray(v, float)
    order = v.argsort()
    r = np.empty(len(v)); r[order] = np.arange(len(v))
    _, inv, cnt = np.unique(v, return_inverse=True, return_counts=True)
    sums = np.zeros(len(cnt)); np.add.at(sums, inv, r)
    return (sums / cnt)[inv]


def pearson(x, y):
    x = np.asarray(x, float) - np.mean(x)
    y = np.asarray(y, float) - np.mean(y)
    d = math.sqrt((x @ x) * (y @ y))
    return float(x @ y / d) if d else float("nan")


def spearman(x, y):
    return pearson(rankdata(x), rankdata(y))


def partial_spearman(acc, hum, freq):
    """Spearman partial correlation r(acc,hum . freq) on ranks."""
    ra, rh, rf = rankdata(acc), rankdata(hum), rankdata(freq)
    r_ah, r_af, r_hf = pearson(ra, rh), pearson(ra, rf), pearson(rh, rf)
    denom = math.sqrt(max(0.0, (1 - r_af ** 2) * (1 - r_hf ** 2)))
    return (r_ah - r_af * r_hf) / denom if denom > 1e-12 else float("nan")


def boot_ci(fn, n, rng):
    boots = [fn(rng.integers(0, n, n)) for _ in range(BOOT)]
    boots = [b for b in boots if not math.isnan(b)]
    lo, hi = np.percentile(boots, [2.5, 97.5])
    return float(lo), float(hi), float(np.mean([1.0 if b > 0 else 0.0 for b in boots]))


def main():
    res = json.load(open(S205 / "results.json"))
    items = json.load(open(S205 / "items.json"))
    freq = json.load(open(HERE / "freq.json"))
    uids = [p["uid"] for p in items["paradigms"]]
    H = np.array([{p["uid"]: p["human_agreement"] for p in items["paradigms"]}[u] for u in uids])
    F = np.array([freq["F_primary"][u] for u in uids])
    F_sens = np.array([freq["F_sensitivity"][u] for u in uids])
    rng = np.random.default_rng(SEED)

    corr_FH = spearman(F, H)
    corr_FH_sens = spearman(F_sens, H)

    # ---- G7 proxy-validity audit (run + reported BEFORE the partial verdict is read) ----
    ulf = np.array([freq["audit_uni_logfreq"][u] for u in uids])
    wln = np.array([freq["audit_mean_wlen"][u] for u in uids])
    audit = {
        "F_vs_unigram_logfreq_spearman": round(spearman(F, ulf), 4),   # expect strong POSITIVE
        "F_vs_mean_wordlen_spearman": round(spearman(F, wln), 4),      # expect NEGATIVE (Zipf)
        "note": "Predicted before reading the partial: F tracks lexical frequency (strong +) and is "
                "shorter-word-heavier (Zipf, -). A failure here downgrades F to descriptive.",
    }

    per_model, per_model_sens, ncH, ncF = {}, {}, {}, {}
    for m in SLOTS:
        acc = np.array([res["per_model"][m]["per_paradigm"][u] for u in uids])
        raw = spearman(acc, H)
        part = partial_spearman(acc, H, F)
        lo, hi, pboot = boot_ci(lambda idx: partial_spearman(acc[idx], H[idx], F[idx]), len(uids), rng)
        per_model[m] = {"raw_rho": round(raw, 4), "partial_rho": round(part, 4),
                        "partial_ci": [round(lo, 4), round(hi, 4)], "drop": round(raw - part, 4),
                        "ci_excludes_0": bool(lo > 0 or hi < 0), "p_boot_pos": round(pboot, 4)}
        # sensitivity (bi-only F)
        parts = partial_spearman(acc, H, F_sens)
        los, his, _ = boot_ci(lambda idx: partial_spearman(acc[idx], H[idx], F_sens[idx]), len(uids), rng)
        per_model_sens[m] = {"partial_rho": round(parts, 4), "partial_ci": [round(los, 4), round(his, 4)],
                             "ci_excludes_0": bool(los > 0 or his < 0)}
        # NC1: scramble the paradigm->H mapping (real-signal check; expect partial ~0)
        Hs = H.copy(); rng.shuffle(Hs)
        ncH[m] = round(partial_spearman(acc, Hs, F), 4)
        # NC2: scramble F (partialling-machinery check; a random covariate should not move rho => ~raw)
        Fs = F.copy(); rng.shuffle(Fs)
        ncF[m] = round(partial_spearman(acc, Hs * 0 + H, Fs), 4)  # keep true H, random F

    n_excl = sum(1 for m in SLOTS if per_model[m]["ci_excludes_0"] and per_model[m]["partial_rho"] > 0)

    # ---- verdict with the collinearity branch (G6) ----
    if abs(corr_FH) < CORR_LOW:
        verdict = ("CORROBORATED-NO-CONFOUND (corr(F,H)~=0: the C8-posited frequency structure is absent, "
                   "so it cannot have inflated rho_prof; the partial ~ raw)")
    elif abs(corr_FH) > CORR_HIGH:
        verdict = ("INCONCLUSIVE-OVER-CONTROL-SUSPECT (corr(F,H) above the frozen collinearity ceiling: "
                   "the partial has inflated variance and, insofar as F tracks depth, partialling strips "
                   "shared structure)")
    else:
        verdict = ("SURVIVES-COVARIATE" if n_excl >= SURVIVE_MAJ else "BREAKS-COVARIATE")

    out = {
        "reading": "COVARIATE ARM (Q1-C covariate component). Per G8: robustness/corroboration only; the "
                   "deferred swap arm is required for a PROMOTION. Anchor: resource/blimp (human-comparison).",
        "corr_F_H_spearman": round(corr_FH, 4), "corr_F_H_sens_spearman": round(corr_FH_sens, 4),
        "collinearity_bands": {"low": CORR_LOW, "high": CORR_HIGH},
        "verdict": verdict, "n_models_partial_ci_excludes_0": n_excl,
        "per_model": per_model, "per_model_sensitivity_bi_only": per_model_sens,
        "neg_control_scrambleH_partial": ncH, "neg_control_scrambleF_partial": ncF,
        "proxy_validity_audit_G7": audit,
        "scope": ["Controls R1 only (not R2/R2h).",
                  "Q2-A controls SURFACE-LEXICAL familiarity, NOT construction frequency (G3').",
                  "C4 is a PROXY for the panel's unknown pretraining distribution (G3').",
                  "Covariate arm = robustness/corroboration; swap arm (deferred) required for promotion (G8)."],
    }
    json.dump(out, open(HERE / "results_partial.json", "w"), indent=1)

    print("=== BLiMP R1 frequency control — covariate arm (s208) ===")
    print(f"proxy-validity audit (G7): F vs unigram-logfreq rho={audit['F_vs_unigram_logfreq_spearman']:+.3f} "
          f"(expect strong +),  F vs mean-word-length rho={audit['F_vs_mean_wordlen_spearman']:+.3f} (expect -)")
    print(f"corr(F,H) Spearman = {corr_FH:+.4f}  (bands: |r|<{CORR_LOW} absent / |r|>{CORR_HIGH} over-control)")
    for m in SLOTS:
        d = per_model[m]
        print(f"[{m}] raw rho {d['raw_rho']:+.3f} -> partial {d['partial_rho']:+.3f} "
              f"CI[{d['partial_ci'][0]:+.3f},{d['partial_ci'][1]:+.3f}] "
              f"{'(excl 0)' if d['ci_excludes_0'] else '(incl 0)'}  drop {d['drop']:+.3f}  "
              f"bi-only partial {per_model_sens[m]['partial_rho']:+.3f}")
    print(f"NC scramble-H partial (expect ~0): {ncH}")
    print(f"NC scramble-F partial (expect ~raw): {ncF}")
    print("VERDICT:", verdict, f"  (partial CI excludes 0 on {n_excl}/3)")


if __name__ == "__main__":
    main()
