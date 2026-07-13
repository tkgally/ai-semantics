#!/usr/bin/env python3
"""analyze_merged.py -- POOLED powered-magnitude analysis for the genitive possessor-animacy line.

The A2a-MERGED magnitude attachment (s222; the path NEXT.md s221 named to lift the promoted
`claim/genitive-alternation-animacy` from DIRECTION-ONLY to a within-model magnitude+interval).

The MEASUREMENT instrument is byte-frozen: probe.py / build_cooc_gen.py are sha-identical to
rep2/s218 and common.py differs only in the HARD_STOP budget constant (documented in-file). This
ANALYSIS script is NEW and PRE-REGISTERED (PREREG.md): it POOLS the within-FRAME typical-arm animacy
shift across the THREE mutually-DISJOINT typical arms --

    shift(frame) = mean(s-pref | animate) - mean(s-pref | inanimate)     [averaged over A/B]

    s218 (36 frames) + rep2 (36 frames) + mag (36 fresh-blind frames) = 108 pooled typical frames

-- and reports, PER MODEL, the pooled-frame mean MAGNITUDE with a nonparametric bootstrap 95% CI
over the 108 frames (resampling unit = the FRAME, ratified S3) and a one-sided sign test.

Three estimates per model: POOLED-108 (headline magnitude), NEW-36-only (the blind fresh estimate,
so the reader can see the magnitude on never-seen items alone), PRIOR-72-only (s218+rep2).

Covariate-adjusted pooled magnitude b0 (OLS shift ~ propensity_diff over the 108 frames, merged
frozen UD-EWT covariate freq_control.json) is reported as CORROBORATION only -- the covariate
was near-vacuous (R2 <= 0.013) in both prior runs, so the HEADLINE is the RAW pooled magnitude.

NONCE is NOT re-run: the shortcut firewall already replicated 3/3 twice (s218 + s220). The magnitude
is a typical-arm quantity; this run attaches magnitude, it does not re-litigate the firewall.

Run: python3 analyze_merged.py
"""
import hashlib
import json
import math
import os

import numpy as np

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.dirname(HERE)
RNG = np.random.default_rng(20260713)

# (label, dir) -- the three disjoint typical arms, pooled.
ARMS = [
    ("s218", os.path.join(RUNS, "2026-07-13-genitive-alternation-animacy")),
    ("rep2", os.path.join(RUNS, "2026-07-13-genitive-alternation-animacy-rep2")),
    ("mag",  HERE),
]
MODELS = list(C.MODELS)                                   # claude, gemini, gpt
FREQ = json.load(open(os.path.join(HERE, "freq_control.json")))


def read_jsonl(path):
    return [json.loads(l) for l in open(path)] if os.path.exists(path) else []


def typical_frame_map(run_dir):
    """frame_id -> (animate_lemma, inanimate_lemma) for the TYPICAL arm of one run."""
    stim = json.load(open(os.path.join(run_dir, "stimuli.json")))
    noun = lambda x: x.split()[-1].lower()
    return {f["id"]: (noun(f["animate"]), noun(f["inanimate"]))
            for f in stim["frames"] if f["arm"] == "typical"}


def frame_shifts_for_model(model):
    """List of (arm_label, frame_id, shift, anim_lemma, inan_lemma) across all three arms."""
    out = []
    for label, run_dir in ARMS:
        fmap = typical_frame_map(run_dir)
        rows = read_jsonl(os.path.join(run_dir, "raw", f"probe-{model}.jsonl"))
        by_cell = {}
        for r in rows:
            if r["arm"] != "typical" or r["s_pref"] is None:
                continue
            by_cell.setdefault((r["frame"], r["level"]), []).append(r["s_pref"])
        for fid, (anim, inan) in fmap.items():
            av = by_cell.get((fid, "animate"))
            iv = by_cell.get((fid, "inanimate"))
            if av and iv:
                out.append((label, fid, float(np.mean(av)) - float(np.mean(iv)), anim, inan))
    return out


def boot_ci(vals, n=10000):
    vals = np.asarray(vals, float)
    if not len(vals):
        return float("nan"), float("nan"), float("nan")
    boot = np.array([np.mean(RNG.choice(vals, len(vals), replace=True)) for _ in range(n)])
    lo, hi = np.percentile(boot, [2.5, 97.5])
    return float(np.mean(vals)), float(lo), float(hi)


def sign_p(vals):
    vals = np.asarray(vals, float)
    n, k = len(vals), int((vals > 0).sum())
    if not n:
        return float("nan")
    return sum(math.comb(n, i) for i in range(k, n + 1)) / (2 ** n)


def propensity(lemma):
    rec = FREQ["per_lemma"].get(lemma)
    return rec["marginal_s_propensity_smoothed"] if rec else FREQ["corpus_meta"]["corpus_base_rate_s"]


def cov_b0(shift_tuples):
    """OLS shift = b0 + b1*propensity_diff over pooled frames; bootstrap CI on b0."""
    x = np.array([propensity(a) - propensity(i) for _, _, _, a, i in shift_tuples])
    y = np.array([s for _, _, s, _, _ in shift_tuples])
    if len(y) < 3:
        return (float("nan"),) * 5

    def fit(xx, yy):
        X = np.column_stack([np.ones(len(xx)), xx])
        beta, *_ = np.linalg.lstsq(X, yy, rcond=None)
        yhat = X @ beta
        ss_res = float(np.sum((yy - yhat) ** 2))
        ss_tot = float(np.sum((yy - yy.mean()) ** 2))
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else float("nan")
        return beta[0], beta[1], r2

    b0, b1, r2 = fit(x, y)
    idx = np.arange(len(y))
    b0s = []
    for _ in range(10000):
        s = RNG.choice(idx, len(idx), replace=True)
        try:
            bb0, _, _ = fit(x[s], y[s])
            b0s.append(bb0)
        except Exception:  # noqa: BLE001
            pass
    lo, hi = np.percentile(b0s, [2.5, 97.5]) if b0s else (float("nan"), float("nan"))
    return float(b0), float(lo), float(hi), float(b1), float(r2)


def summarize(model):
    tuples = frame_shifts_for_model(model)
    pooled = [t[2] for t in tuples]
    new = [t[2] for t in tuples if t[0] == "mag"]
    prior = [t[2] for t in tuples if t[0] in ("s218", "rep2")]
    p_mean, p_lo, p_hi = boot_ci(pooled)
    n_mean, n_lo, n_hi = boot_ci(new)
    r_mean, r_lo, r_hi = boot_ci(prior)
    b0, b0_lo, b0_hi, b1, r2 = cov_b0(tuples)
    return {
        "model": model,
        "n_frames_pooled": len(pooled), "n_frames_new": len(new), "n_frames_prior": len(prior),
        "pooled_magnitude": round(p_mean, 4), "pooled_ci95": [round(p_lo, 4), round(p_hi, 4)],
        "pooled_frames_pos": f"{int((np.array(pooled) > 0).sum())}/{len(pooled)}",
        "pooled_sign_p": round(sign_p(pooled), 6),
        "pooled_ci_lb_gt0": p_lo > 0,
        "new36_magnitude": round(n_mean, 4), "new36_ci95": [round(n_lo, 4), round(n_hi, 4)],
        "new36_frames_pos": f"{int((np.array(new) > 0).sum())}/{len(new)}",
        "new36_sign_p": round(sign_p(new), 6),
        "prior72_magnitude": round(r_mean, 4), "prior72_ci95": [round(r_lo, 4), round(r_hi, 4)],
        "cov_adj_b0": round(b0, 4), "cov_adj_ci95": [round(b0_lo, 4), round(b0_hi, 4)],
        "cov_slope_b1": round(b1, 4), "cov_r2": round(r2, 4),
    }


def main():
    results = [summarize(m) for m in MODELS]
    n_lb = sum(1 for r in results if r["pooled_ci_lb_gt0"])
    mags = [r["pooled_magnitude"] for r in results]

    # billed cost of the NEW mag arm only (this session's spend on this line)
    mag_rows = []
    for m in MODELS:
        mag_rows += [{"usage": u} for r in read_jsonl(os.path.join(HERE, "raw", f"probe-{m}.jsonl"))
                     for u in (r.get("usage") or [])]
    billed, have, missing = C.billed_cost([mag_rows])

    out = {
        "analysis": "pooled-magnitude (A2a-merged, s222)",
        "n_models_pooled_ci_lb_gt0": n_lb,
        "panel_magnitude_range": [round(min(mags), 4), round(max(mags), 4)],
        "panel_magnitude_mean": round(float(np.mean(mags)), 4),
        "mag_arm_billed_usd": round(billed, 6), "mag_arm_calls": have, "mag_arm_missing": missing,
        "mag_stimuli_sha256": hashlib.sha256(
            open(os.path.join(HERE, "stimuli.json"), "rb").read()).hexdigest(),
        "merged_freq_sha256": hashlib.sha256(
            open(os.path.join(HERE, "freq_control.json"), "rb").read()).hexdigest(),
        "models": results,
    }
    json.dump(out, open(os.path.join(HERE, "analysis_merged.json"), "w"), indent=2)

    print(f"POOLED MAGNITUDE (108 typical frames = s218 36 + rep2 36 + mag 36)")
    print(f"  models with pooled CI-LB > 0: {n_lb}/3   panel magnitude "
          f"range {out['panel_magnitude_range']} mean {out['panel_magnitude_mean']}")
    print(f"  mag arm billed ${billed:.5f} ({have} calls, {missing} missing)")
    for r in results:
        print(f"\n[{r['model']}]  POOLED magnitude={r['pooled_magnitude']} "
              f"CI={r['pooled_ci95']} pos={r['pooled_frames_pos']} "
              f"sign-p={r['pooled_sign_p']}  CI-LB>0={r['pooled_ci_lb_gt0']}")
        print(f"    new-36 (blind) ={r['new36_magnitude']} CI={r['new36_ci95']} "
              f"pos={r['new36_frames_pos']} sign-p={r['new36_sign_p']}")
        print(f"    prior-72       ={r['prior72_magnitude']} CI={r['prior72_ci95']}")
        print(f"    cov-adj b0={r['cov_adj_b0']} CI={r['cov_adj_ci95']} "
              f"b1={r['cov_slope_b1']} R2={r['cov_r2']} (corroboration; covariate near-vacuous)")


if __name__ == "__main__":
    main()
