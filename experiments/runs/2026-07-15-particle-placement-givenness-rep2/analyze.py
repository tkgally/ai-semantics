#!/usr/bin/env python3
"""analyze.py -- pre-registered analysis for the VERB-PARTICLE-PLACEMENT object-givenness probe.

Resampling unit = the FRAME (a fixed verb+particle+object-head-noun). Per model:

Arm 1 -- DEFINITENESS shift (anchor-exact, CONFOUNDABLE, NOT decisive):
    shift1(frame) = mean(split-pref | definite) - mean(split-pref | indefinite)   [over A/B]
  Human direction (Kim et al. 2016 / Gries 1999): definite -> split, shift1 > 0. Role (R4): a
  CONSISTENCY check only (directional consistency required; a REVERSAL blocks CONFIRM), NOT a hard CI gate.

Arm 2 -- DISCOURSE-GIVENNESS FIREWALL (byte-identical scored strings; LOAD-BEARING; carries the CONFIRM):
    DECISIVE = 'given_minus_newment' (Option A): shift2 = mean(split-pref|GIVEN) - mean(split-pref|NEW-MENTIONED)
       -- holds object-noun lexical priming/recency constant, isolates REFERENTIAL givenness (B-crit-1/R2).
    descriptive: given_minus_new = mean(split-pref|GIVEN) - mean(split-pref|NEW).
  Because the scored strings are byte-identical across GIVEN/NEW-MENTIONED/NEW, any scored-string reader
  yields shift2 = 0 by construction; a positive shift2 comes only from integrating the discourse context.

Arm 3 -- LENGTH (convergent-validity leg, SECONDARY, non-gating -- R5):
    shift3(frame) = mean(split-pref | short) - mean(split-pref | long).  Human dir: short -> split, > 0.
  Feeds the WEAK adjudication only; never enters the CONFIRM gate and is not blended into the givenness legs.

COVARIATE (corroboration only; R1/R7 near-vacuous) -- Arm-1 definiteness shift residual over the frozen
  per-(verb+particle) marginal SPLIT-order rate: OLS shift1(frame) = b0 + b1*split_rate(frame). b0 = the
  definiteness shift not attributable to the verb+particle's baseline split propensity. analyze.py reports
  the covariate's OWN predictive validity (b1, R^2); if it barely predicts the shift, partialling it out is
  near-vacuous and the reading rests on Arm 2 -- stated plainly. (Particle-verb tokens are sparse in UD-EWT.)

PRE-REGISTERED ASYMMETRIC VERDICT (R4; symmetric -- a null is first-class). Per model:
    cond_fw       : firewall shift2 (DECISIVE) > 0 AND bootstrap 95% lower bound > 0     [necessary+primary]
    arm1_consistent : shift1 point estimate > 0 (human direction)                        [directional only]
    arm1_reversal : shift1 point estimate < 0                                            [blocks CONFIRM]
    cond_fw_strong: shift1 > 0 AND bootstrap 95% lower bound > 0                          [full vs firewall-borne]
    cond_len      : shift3 > 0 AND bootstrap 95% lower bound > 0                          [convergent leg]
  Panel (>=2/3 models):
    CONFIRM  : cond_fw (>=2/3) AND arm1_consistent (>=2/3) AND NOT arm1_reversal (>=2/3).
               'full CONFIRM' if cond_fw_strong (>=2/3) too; else 'CONFIRM, firewall-borne'.
    SHADOW   : shift1 > 0 (>=2/3) but cond_fw FAILS (<2/3) -> the definiteness effect is a surface/lexical
               shadow, not information structure (a first-class negative).
    WEAK     : cond_fw (>=2/3) but cond_len FAILS (<2/3) -> firewall positive without the convergent leg.
    FALSIFY  : cond_fw fails AND shift1 not > 0 at >=2/3 (or Arm 1 reverses at >=2/3).
"""
import json
import math
import os

import numpy as np

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
STIM = json.load(open(os.path.join(HERE, "stimuli.json")))
FREQ = json.load(open(os.path.join(HERE, "freq_control.json")))
RNG = np.random.default_rng(20260714)

FRAMES = STIM["frames"]

# DECISIVE firewall leg -- set at freeze from the independent certifier verdict:
#   'given_minus_newment' = Option A (three-condition; the ratified default), decisive GIVEN-NEW-MENTIONED
#   'given_minus_new'     = Option B fallback (two-condition; rescoped claim) if NEW-MENTIONED uncertifiable
DECISIVE = "given_minus_newment"

VERB_LEMMA = {
    "picked": "pick", "put": "put", "took": "take", "threw": "throw", "pulled": "pull",
    "wiped": "wipe", "hung": "hang", "locked": "lock", "folded": "fold", "rolled": "roll",
    "packed": "pack", "wrapped": "wrap", "carried": "carry", "set": "set", "lifted": "lift",
    "handed": "hand", "cleared": "clear", "shut": "shut", "brought": "bring", "turned": "turn",
    "cut": "cut", "hauled": "haul",
}


def cell_pref(rows, frame_id, arm, condition):
    vals = [r["split_pref"] for r in rows
            if r["frame"] == frame_id and r["arm"] == arm and r["condition"] == condition
            and r["split_pref"] is not None]
    return float(np.mean(vals)) if vals else None


def frame_shifts(rows, arm, hi, lo):
    out = {}
    for fr in FRAMES:
        a, b = cell_pref(rows, fr["id"], arm, hi), cell_pref(rows, fr["id"], arm, lo)
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


def split_rate(frame):
    lemma = VERB_LEMMA[frame["verb"]]
    return FREQ["per_pair"][f"{lemma}+{frame['prt'].lower()}"]["marginal_split_rate_smoothed"]


def covariate_adjust(shift1):
    """OLS shift1 = b0 + b1*split_rate over frames. Bootstrap CI on b0. Returns (b0,lo,hi,b1,r2,x_sd)."""
    fmap = {f["id"]: f for f in FRAMES}
    fr_ids = list(shift1.keys())
    x = np.array([split_rate(fmap[i]) for i in fr_ids])
    y = np.array([shift1[i] for i in fr_ids])
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


def level_mean(rows, arm, condition):
    vals = [cell_pref(rows, fr["id"], arm, condition) for fr in FRAMES]
    vals = [v for v in vals if v is not None]
    return float(np.mean(vals)) if vals else None


def analyze_model(name):
    rows = C.read_jsonl(os.path.join(C.RAW, f"probe-{name}.jsonl"))
    n_total = len(rows)
    n_na = sum(1 for r in rows if r["split_pref"] is None)
    n_retried = sum(1 for r in rows if r.get("retried"))
    n_len = sum(1 for r in rows if r.get("finish_reason") == "length")

    sh1 = frame_shifts(rows, "definiteness", "definite", "indefinite")
    sh2_gm = frame_shifts(rows, "firewall", "given", "newment")   # Option A decisive
    sh2_gn = frame_shifts(rows, "firewall", "given", "new")       # descriptive / Option B decisive
    sh3 = frame_shifts(rows, "length", "short", "long")
    sh2 = sh2_gm if DECISIVE == "given_minus_newment" else sh2_gn

    s1_m, s1_lo, s1_hi = boot_ci(list(sh1.values()))
    fw_m, fw_lo, fw_hi = boot_ci(list(sh2.values()))
    gm_m, gm_lo, gm_hi = boot_ci(list(sh2_gm.values()))
    gn_m, gn_lo, gn_hi = boot_ci(list(sh2_gn.values()))
    l_m, l_lo, l_hi = boot_ci(list(sh3.values()))
    b0, b0_lo, b0_hi, b1, r2, x_sd = covariate_adjust(sh1)

    cond_fw = fw_m > 0 and fw_lo > 0
    arm1_consistent = s1_m > 0
    arm1_reversal = s1_m < 0
    cond_fw_strong = s1_m > 0 and s1_lo > 0
    cond_len = l_m > 0 and l_lo > 0

    # per-model verdict (asymmetric, R4)
    if cond_fw and arm1_consistent and not arm1_reversal:
        verdict = "CONFIRM" if cond_fw_strong else "CONFIRM-firewall-borne"
    elif (not cond_fw) and arm1_consistent:
        verdict = "SHADOW"
    elif cond_fw and not cond_len:
        verdict = "WEAK"
    else:
        verdict = "FALSIFY"

    # per-condition mean split-pref (context calibration)
    calib = {arm: {c: level_mean(rows, arm, c) for c in
                   (["definite", "indefinite"] if arm == "definiteness"
                    else ["given", "newment", "new"] if arm == "firewall"
                    else ["short", "long"])}
             for arm in ("definiteness", "firewall", "length")}

    return {
        "model": name, "verdict": verdict,
        "cond_fw": cond_fw, "arm1_consistent": arm1_consistent, "arm1_reversal": arm1_reversal,
        "cond_fw_strong": cond_fw_strong, "cond_len": cond_len,
        "definiteness_shift1": round(s1_m, 4), "definiteness_ci95": [round(s1_lo, 4), round(s1_hi, 4)],
        "definiteness_frames_pos": f"{int((np.array(list(sh1.values())) > 0).sum())}/{len(sh1)}",
        "definiteness_sign_p": round(sign_test_p(list(sh1.values())), 5),
        "firewall_decisive_leg": DECISIVE,
        "firewall_shift2": round(fw_m, 4), "firewall_ci95": [round(fw_lo, 4), round(fw_hi, 4)],
        "firewall_frames_pos": f"{int((np.array(list(sh2.values())) > 0).sum())}/{len(sh2)}",
        "firewall_sign_p": round(sign_test_p(list(sh2.values())), 5),
        "given_minus_newment": round(gm_m, 4), "given_minus_newment_ci95": [round(gm_lo, 4), round(gm_hi, 4)],
        "given_minus_new_desc": round(gn_m, 4), "given_minus_new_ci95": [round(gn_lo, 4), round(gn_hi, 4)],
        "length_shift3": round(l_m, 4), "length_ci95": [round(l_lo, 4), round(l_hi, 4)],
        "length_frames_pos": f"{int((np.array(list(sh3.values())) > 0).sum())}/{len(sh3)}",
        "covariate_adj_b0": round(b0, 4), "covariate_adj_ci95": [round(b0_lo, 4), round(b0_hi, 4)],
        "covariate_slope_b1": round(b1, 4), "covariate_r2": round(r2, 4), "covariate_x_sd": round(x_sd, 5),
        "calibration_mean_split_pref": {a: {c: (round(v, 4) if v is not None else None)
                                            for c, v in d.items()} for a, d in calib.items()},
        "data": {"n_total": n_total, "n_NA": n_na, "n_retried": n_retried, "n_length_trunc": n_len},
        "per_frame_definiteness_shift": {k: round(v, 3) for k, v in sh1.items()},
        "per_frame_firewall_shift": {k: round(v, 3) for k, v in sh2.items()},
        "per_frame_length_shift": {k: round(v, 3) for k, v in sh3.items()},
    }


def main():
    results = [analyze_model(n) for n in C.MODELS]
    n_fw = sum(1 for r in results if r["cond_fw"])
    n_a1 = sum(1 for r in results if r["arm1_consistent"])
    n_rev = sum(1 for r in results if r["arm1_reversal"])
    n_fw_strong = sum(1 for r in results if r["cond_fw_strong"])
    n_len = sum(1 for r in results if r["cond_len"])
    n_s1pos = sum(1 for r in results if r["definiteness_shift1"] > 0)

    if n_fw >= 2 and n_a1 >= 2 and n_rev < 2:
        panel = "CONFIRM" if n_fw_strong >= 2 else "CONFIRM-firewall-borne"
    elif n_s1pos >= 2 and n_fw < 2:
        panel = "SHADOW"
    elif n_fw >= 2 and n_len < 2:
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
        "panel_verdict": panel, "decisive_firewall_leg": DECISIVE,
        "n_models_cond_fw": n_fw, "n_models_arm1_consistent": n_a1, "n_models_arm1_reversal": n_rev,
        "n_models_cond_fw_strong": n_fw_strong, "n_models_cond_len": n_len,
        "n_models_definiteness_pos": n_s1pos,
        "stimuli_sha256": hashlib.sha256(open(os.path.join(HERE, "stimuli.json"), "rb").read()).hexdigest(),
        "freq_control_sha256": hashlib.sha256(open(os.path.join(HERE, "freq_control.json"), "rb").read()).hexdigest(),
        "covariate_corpus_base_split_rate": FREQ["corpus_meta"]["corpus_base_split_rate"],
        "billed_usd": round(billed, 6), "n_cost_have": have, "n_cost_missing": missing,
        "models": results,
    }
    json.dump(out, open(os.path.join(HERE, "analysis.json"), "w"), indent=2)

    print(f"PANEL VERDICT: {panel}  (decisive leg: {DECISIVE})")
    print(f"  cond_fw {n_fw}/3, arm1_consistent {n_a1}/3, arm1_reversal {n_rev}/3, "
          f"fw_strong {n_fw_strong}/3, cond_len {n_len}/3, definiteness>0 {n_s1pos}/3")
    print(f"billed ${billed:.5f} ({have} calls, {missing} missing)")
    for r in results:
        print(f"\n[{r['model']}] {r['verdict']}  "
              f"(fw={r['cond_fw']} a1_consist={r['arm1_consistent']} a1_rev={r['arm1_reversal']} "
              f"fw_strong={r['cond_fw_strong']} len={r['cond_len']})")
        print(f"  DEFINITENESS shift1={r['definiteness_shift1']} CI={r['definiteness_ci95']} "
              f"pos={r['definiteness_frames_pos']} sign-p={r['definiteness_sign_p']}  (consistency check)")
        print(f"  FIREWALL     shift2={r['firewall_shift2']} CI={r['firewall_ci95']} "
              f"pos={r['firewall_frames_pos']} sign-p={r['firewall_sign_p']}  (DECISIVE {r['firewall_decisive_leg']})")
        print(f"    given-newment={r['given_minus_newment']} {r['given_minus_newment_ci95']} | "
              f"given-new(desc)={r['given_minus_new_desc']} {r['given_minus_new_ci95']}")
        print(f"  LENGTH       shift3={r['length_shift3']} CI={r['length_ci95']} "
              f"pos={r['length_frames_pos']}  (convergent leg)")
        print(f"  COV-ADJ b0={r['covariate_adj_b0']} CI={r['covariate_adj_ci95']} | "
              f"b1={r['covariate_slope_b1']} R2={r['covariate_r2']} x_sd={r['covariate_x_sd']}")
        print(f"  calib split-pref: {r['calibration_mean_split_pref']}")
        print(f"  data: NA={r['data']['n_NA']} retried={r['data']['n_retried']} "
              f"len-trunc={r['data']['n_length_trunc']} of {r['data']['n_total']}")


if __name__ == "__main__":
    main()
