#!/usr/bin/env python3
"""analyze.py -- pre-registered analysis for the GENITIVE-alternation possessor-animacy probe.

Resampling unit = the FRAME (a fixed possessum), per critic S3. Per model:

PRIMARY -- TYPICAL arm within-frame animacy shift
    shift(frame) = mean(s-pref | animate) - mean(s-pref | inanimate)   [averaged over A/B]
  reported with a nonparametric bootstrap 95% CI over frames + a one-sided sign test.

GRADED (prediction 2) -- mean s-pref at animate vs collective vs inanimate; monotone animate >
  collective > inanimate is the graded signature (else WEAK).

SHADOW CONTROL 1 (PRIMARY, critic B1/R3) -- NONCE arm within-frame animacy shift (animate nonce -
  inanimate nonce). A nonce possessor has NO per-lemma corpus genitive statistic and its animacy is
  carried only by the gloss, so a no-animacy marginal-frequency reader yields shift 0 here. This arm
  CARRIES the confirm.

SHADOW CONTROL 2 (corroboration, critic B2/R2) -- covariate-adjusted animacy effect on the TYPICAL
  arm: OLS  shift(frame) = b0 + b1 * propensity_diff(frame)  where propensity_diff = frozen marginal
  s-genitive propensity(animate possessor) - propensity(inanimate possessor). b0 = the animacy shift
  NOT attributable to the possessor's marginal genitive propensity. We ALSO report b1 and R^2 = the
  covariate's OWN predictive validity (R2): if the covariate barely varies / does not predict the
  shift, partialling it out is near-vacuous and CONFIRM rests on the nonce arm -- stated plainly.

PRE-REGISTERED VERDICT (B3, symmetric -- a null is first-class). Per model, three conditions:
    cond_typ   : typical shift > 0 AND bootstrap 95% lower bound > 0
    cond_nonce : nonce   shift > 0 AND bootstrap 95% lower bound > 0        (the firewall)
    cond_cov   : covariate-adjusted intercept b0 > 0 AND bootstrap 95% lower bound > 0
  Panel:
    CONFIRM  : >=2/3 models meet cond_typ AND >=2/3 meet cond_nonce AND >=2/3 meet cond_cov
    SHADOW   : >=2/3 meet cond_typ but the nonce and/or covariate leg fails at >=2/3
    WEAK     : typical shift > 0 (>=2/3) but not graded (animate>collective>inanimate fails)
    FALSIFY  : typical shift not > 0 (or reverses) at >=2/3
"""
import json
import math
import os

import numpy as np

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
STIM = json.load(open(os.path.join(HERE, "stimuli.json")))
FREQ = json.load(open(os.path.join(HERE, "freq_control.json")))
RNG = np.random.default_rng(20260713)

FRAMES = STIM["frames"]
TYP = [f for f in FRAMES if f["arm"] == "typical"]
NON = [f for f in FRAMES if f["arm"] == "nonce"]


def cell_pref(rows, frame_id, level):
    vals = [r["s_pref"] for r in rows
            if r["frame"] == frame_id and r["level"] == level and r["s_pref"] is not None]
    return float(np.mean(vals)) if vals else None


def frame_shifts(rows, frames, hi="animate", lo="inanimate"):
    out = {}
    for fr in frames:
        a, b = cell_pref(rows, fr["id"], hi), cell_pref(rows, fr["id"], lo)
        if a is not None and b is not None:
            out[fr["id"]] = a - b
    return out


def boot_ci(vals, stat=np.mean, n=10000):
    vals = np.asarray(vals, float)
    if not len(vals):
        return float("nan"), float("nan"), float("nan")
    boot = np.array([stat(RNG.choice(vals, len(vals), replace=True)) for _ in range(n)])
    lo, hi = np.percentile(boot, [2.5, 97.5])
    return float(stat(vals)), float(lo), float(hi)


def sign_test_p(vals):
    vals = np.asarray(vals, float)
    n, k = len(vals), int((np.asarray(vals) > 0).sum())
    if not n:
        return float("nan")
    return sum(math.comb(n, i) for i in range(k, n + 1)) / (2 ** n)


def propensity(noun):
    return FREQ["per_lemma"][noun.split()[-1].lower()]["marginal_s_propensity_smoothed"]


def covariate_adjust(shifts):
    """OLS shift = b0 + b1*propensity_diff over typical frames. Bootstrap CI on b0 over frames.
    Returns (b0, b0_lo, b0_hi, b1, r2, propdiff_sd)."""
    fr_ids = list(shifts.keys())
    fmap = {f["id"]: f for f in TYP}
    x = np.array([propensity(fmap[i]["animate"]) - propensity(fmap[i]["inanimate"]) for i in fr_ids])
    y = np.array([shifts[i] for i in fr_ids])
    if len(y) < 3:
        return (float("nan"),) * 6

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
    return float(b0), float(lo), float(hi), float(b1), float(r2), float(x.std())


def analyze_model(name):
    rows = C.read_jsonl(os.path.join(C.RAW, f"probe-{name}.jsonl"))
    n_total = len(rows)
    n_na = sum(1 for r in rows if r["s_pref"] is None)
    n_retried = sum(1 for r in rows if r.get("retried"))
    n_len = sum(1 for r in rows if r.get("finish_reason") == "length")

    typ_sh = frame_shifts(rows, TYP)
    non_sh = frame_shifts(rows, NON)
    tv = list(typ_sh.values())
    nv = list(non_sh.values())

    typ_mean, typ_lo, typ_hi = boot_ci(tv)
    non_mean, non_lo, non_hi = boot_ci(nv)
    b0, b0_lo, b0_hi, b1, r2, propdiff_sd = covariate_adjust(typ_sh)

    # graded means
    def level_mean(frames, level):
        vals = [cell_pref(rows, fr["id"], level) for fr in frames]
        vals = [v for v in vals if v is not None]
        return float(np.mean(vals)) if vals else None
    m_anim = level_mean(TYP, "animate")
    m_coll = level_mean(TYP, "collective")
    m_inan = level_mean(TYP, "inanimate")
    graded_ok = (m_anim is not None and m_coll is not None and m_inan is not None
                 and m_anim > m_coll > m_inan)

    # neutral default = grand mean s-pref (all trials) -> the model's own baseline s-gen rate
    all_pref = [r["s_pref"] for r in rows if r["s_pref"] is not None]
    default_s = float(np.mean(all_pref)) if all_pref else None

    cond_typ = typ_mean > 0 and typ_lo > 0
    cond_nonce = non_mean > 0 and non_lo > 0
    cond_cov = (not math.isnan(b0)) and b0 > 0 and b0_lo > 0

    if cond_typ and cond_nonce and cond_cov:
        verdict = "CONFIRM"
    elif cond_typ and not (cond_nonce and cond_cov):
        verdict = "SHADOW"
    elif cond_typ and not graded_ok:
        verdict = "WEAK"
    elif not cond_typ and typ_mean > 0:
        verdict = "WEAK"
    else:
        verdict = "FALSIFY"

    return {
        "model": name, "verdict": verdict,
        "cond_typ": cond_typ, "cond_nonce": cond_nonce, "cond_cov": cond_cov,
        "typical_mean_shift": round(typ_mean, 4), "typical_ci95": [round(typ_lo, 4), round(typ_hi, 4)],
        "typical_frames_pos": f"{int((np.array(tv) > 0).sum())}/{len(tv)}",
        "typical_sign_p": round(sign_test_p(tv), 5),
        "nonce_mean_shift": round(non_mean, 4), "nonce_ci95": [round(non_lo, 4), round(non_hi, 4)],
        "nonce_frames_pos": f"{int((np.array(nv) > 0).sum())}/{len(nv)}",
        "nonce_sign_p": round(sign_test_p(nv), 5),
        "covariate_adjusted_intercept_b0": round(b0, 4), "cov_adj_ci95": [round(b0_lo, 4), round(b0_hi, 4)],
        "covariate_slope_b1": round(b1, 4), "covariate_r2": round(r2, 4),
        "covariate_propdiff_sd": round(propdiff_sd, 5),
        "graded_means_anim_coll_inan": [round(m_anim, 4) if m_anim is not None else None,
                                        round(m_coll, 4) if m_coll is not None else None,
                                        round(m_inan, 4) if m_inan is not None else None],
        "graded_monotone_anim_gt_coll_gt_inan": graded_ok,
        "default_s_pref": round(default_s, 4) if default_s is not None else None,
        "data": {"n_total": n_total, "n_NA": n_na, "n_retried": n_retried, "n_length_trunc": n_len},
        "per_frame_typical_shift": {k: round(v, 3) for k, v in typ_sh.items()},
        "per_frame_nonce_shift": {k: round(v, 3) for k, v in non_sh.items()},
    }


def main():
    results = [analyze_model(n) for n in C.MODELS]
    n_typ = sum(1 for r in results if r["cond_typ"])
    n_non = sum(1 for r in results if r["cond_nonce"])
    n_cov = sum(1 for r in results if r["cond_cov"])
    n_graded = sum(1 for r in results if r["graded_monotone_anim_gt_coll_gt_inan"])

    if n_typ >= 2 and n_non >= 2 and n_cov >= 2:
        panel = "CONFIRM"
    elif n_typ >= 2 and not (n_non >= 2 and n_cov >= 2):
        panel = "SHADOW"
    elif n_typ >= 2:
        panel = "WEAK"
    else:
        panel = "FALSIFY"

    all_rows = []
    for n in C.MODELS:
        all_rows += [{"usage": u} for r in C.read_jsonl(os.path.join(C.RAW, f"probe-{n}.jsonl"))
                     for u in (r.get("usage") or [])]
    billed, have, missing = C.billed_cost([all_rows])

    import hashlib
    out = {
        "panel_verdict": panel,
        "n_models_cond_typ": n_typ, "n_models_cond_nonce": n_non, "n_models_cond_cov": n_cov,
        "n_models_graded_monotone": n_graded,
        "stimuli_sha256": hashlib.sha256(open(os.path.join(HERE, "stimuli.json"), "rb").read()).hexdigest(),
        "freq_control_sha256": hashlib.sha256(open(os.path.join(HERE, "freq_control.json"), "rb").read()).hexdigest(),
        "covariate_corpus_base_rate_s": FREQ["corpus_meta"]["corpus_base_rate_s"],
        "billed_usd": round(billed, 6), "n_cost_have": have, "n_cost_missing": missing,
        "models": results,
    }
    json.dump(out, open(os.path.join(HERE, "analysis.json"), "w"), indent=2)

    print(f"PANEL VERDICT: {panel}  (cond_typ {n_typ}/3, cond_nonce {n_non}/3, cond_cov {n_cov}/3, "
          f"graded {n_graded}/3)")
    print(f"billed ${billed:.5f} ({have} calls, {missing} missing)")
    for r in results:
        print(f"\n[{r['model']}] {r['verdict']}  "
              f"(typ={r['cond_typ']} nonce={r['cond_nonce']} cov={r['cond_cov']})")
        print(f"  TYPICAL shift={r['typical_mean_shift']} CI={r['typical_ci95']} "
              f"pos={r['typical_frames_pos']} sign-p={r['typical_sign_p']}")
        print(f"  NONCE   shift={r['nonce_mean_shift']} CI={r['nonce_ci95']} "
              f"pos={r['nonce_frames_pos']} sign-p={r['nonce_sign_p']}  (the firewall)")
        print(f"  COV-ADJ b0={r['covariate_adjusted_intercept_b0']} CI={r['cov_adj_ci95']} "
              f"| b1={r['covariate_slope_b1']} R2={r['covariate_r2']} propdiff_sd={r['covariate_propdiff_sd']}")
        print(f"  graded (anim,coll,inan)={r['graded_means_anim_coll_inan']} "
              f"monotone={r['graded_monotone_anim_gt_coll_gt_inan']}  default s-pref={r['default_s_pref']}")
        print(f"  data: NA={r['data']['n_NA']} retried={r['data']['n_retried']} "
              f"len-trunc={r['data']['n_length_trunc']} of {r['data']['n_total']}")


if __name__ == "__main__":
    main()
