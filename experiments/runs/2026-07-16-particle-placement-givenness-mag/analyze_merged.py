#!/usr/bin/env python3
"""analyze_merged.py -- the NEW pre-registered POOLED MAGNITUDE analysis for the verb-particle placement
object-givenness FIREWALL shift (program A5 / A2a; session 238).

The frozen analyze.py computes a single-run VERDICT; this run's finding is a POOLED within-model MAGNITUDE
of the load-bearing firewall shift, so the analysis is new (frozen here, before any model call, alongside
stimuli.json). It reuses the byte-frozen INDICATOR (probe.py/common.py) and the byte-frozen firewall
computation (shift2 = mean(split-pref|GIVEN) - mean(split-pref|NEW-MENTIONED), decisive Option A).

Resampling unit = the FRAME (a fixed verb+particle+object-head-noun), keyed by (run, frame_id) so the three
runs' frames pool as mutually-disjoint independent units:
    v1 (40) + rep2 (48) + mag (48 fresh-disjoint) = 136 pooled firewall frames.

Per model, the within-frame firewall shift shift2(frame) = mean(split-pref|given) - mean(split-pref|newment).

PRIMARY (headline) -- POOLED magnitude. Per model: the pooled-frame mean shift2 = the within-model
magnitude, with a nonparametric bootstrap 95% CI over the 136 frames + a one-sided sign test.

REPORTED ALONGSIDE (honesty; the genitive-MAG discipline) -- the FRESH-48-only estimate (the magnitude on
the never-seen mag items alone = the blind check) and the PRIOR-88-only estimate (v1 + rep2), so the reader
sees that the pooled interval reuses prior data and can read the fresh-only magnitude on its own.

PRE-REGISTERED READOUT (symmetric; a null/weak result is first-class). The claim is scoped 2/3: the
firewall positive covers CLAUDE + GEMINI; GPT is a persistent, replicated SHADOW (fence a/b). So the
magnitude attaches to claude + gemini and gpt is a displayed SHADOW, never averaged:

  MAGNITUDE ATTACHED iff:
    (gate 1, standalone blind) the FRESH-48 mag arm clears CI-LB>0 for BOTH claude and gemini
      -- the same bar each prior firewall arm cleared for the two confirming models -- AND
    (gate 2, pooled) the POOLED-136 CI-LB>0 for BOTH claude and gemini.
    Then the magnitude the claim carries = the per-model POOLED point shift2 + intervals for claude+gemini,
    reported as a conditional update, WITH the fresh-48-only and prior-88-only estimates shown alongside;
    gpt's pooled estimate is reported as a displayed SHADOW (CI expected to include 0).

  PARTIAL / PROVISIONAL if the pooled-136 CI-LB>0 for both claude+gemini but the FRESH-48 blind arm is
    positive yet does not clear its own CI-LB for both (48 frames underpowered for a tight fresh interval):
    report the pooled magnitude as PROVISIONAL, the fresh arm shown, and fence (j) softened but not fully
    discharged -- a larger fully-fresh arm still owed.

  NO-LIFT if the FRESH-48 arm reverses or is non-positive for either of claude/gemini, or the pooled CI-LB
    <=0 for either -- the claim stays direction-only-no-magnitude and the note records why.

  gpt is NOT part of any gate; its estimate is reported. If gpt's pooled firewall UNEXPECTEDLY clears
    CI-LB>0, that is a first-class disclosure (the SHADOW would have lifted at pooled N) -- reported, not
    folded into the 2/3 headline without a fresh cross-session look.

The DIRECTION + firewall-survival are NOT re-adjudicated here (a promoted claim); this run estimates the
SIZE and decides, on the fresh blind arm's standalone behaviour first, whether to attach it.
"""
import hashlib
import json
import math
import os

import numpy as np

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.dirname(HERE)
RUN_DIRS = {
    "v1":   os.path.join(RUNS, "2026-07-14-particle-placement-givenness"),
    "rep2": os.path.join(RUNS, "2026-07-15-particle-placement-givenness-rep2"),
    "mag":  HERE,
}
RNG = np.random.default_rng(20260716)


def firewall_frame_shifts(run_dir, model, hi="given", lo="newment"):
    """Per (run,frame) firewall shift2 = mean(split_pref|hi) - mean(split_pref|lo) for one model+run."""
    rows = C.read_jsonl(os.path.join(run_dir, "raw", f"probe-{model}.jsonl"))
    frames = sorted({r["frame"] for r in rows if r["arm"] == "firewall"})
    out = {}
    for fid in frames:
        def cell(cond):
            vals = [r["split_pref"] for r in rows if r["arm"] == "firewall"
                    and r["frame"] == fid and r["condition"] == cond and r["split_pref"] is not None]
            return float(np.mean(vals)) if vals else None
        a, b = cell(hi), cell(lo)
        if a is not None and b is not None:
            out[fid] = a - b
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
    nn, k = len(vals), int((np.asarray(vals) > 0).sum())
    if not nn:
        return float("nan")
    return sum(math.comb(nn, i) for i in range(k, nn + 1)) / (2 ** nn)


def summ(vals):
    m, lo, hi = boot_ci(vals)
    pos = int((np.asarray(vals, float) > 0).sum())
    return {"shift2": round(m, 4), "ci95": [round(lo, 4), round(hi, 4)],
            "frames_pos": f"{pos}/{len(vals)}", "sign_p": round(sign_test_p(vals), 5),
            "cond_lb_gt0": bool(m > 0 and lo > 0)}


def analyze_model(model, decisive="given_minus_newment"):
    hi, lo = ("given", "newment") if decisive == "given_minus_newment" else ("given", "new")
    per_run = {r: firewall_frame_shifts(d, model, hi, lo) for r, d in RUN_DIRS.items()}
    fresh = list(per_run["mag"].values())
    prior = list(per_run["v1"].values()) + list(per_run["rep2"].values())
    pooled = fresh + prior
    # descriptive given-new (for the record)
    per_run_gn = {r: firewall_frame_shifts(d, model, "given", "new") for r, d in RUN_DIRS.items()}
    fresh_gn = list(per_run_gn["mag"].values())
    return {
        "model": model,
        "fresh_48_given_minus_newment": summ(fresh),
        "prior_88_given_minus_newment": summ(prior),
        "pooled_136_given_minus_newment": summ(pooled),
        "fresh_48_given_minus_new_desc": summ(fresh_gn),
        "n_frames": {r: len(v) for r, v in per_run.items()},
    }


def main():
    models = list(C.MODELS)
    results = {m: analyze_model(m) for m in models}

    # gates (claude + gemini are the 2 confirming models; gpt is a displayed SHADOW, not gated)
    conf = ["claude", "gemini"]
    gate1 = all(results[m]["fresh_48_given_minus_newment"]["cond_lb_gt0"] for m in conf)
    gate2 = all(results[m]["pooled_136_given_minus_newment"]["cond_lb_gt0"] for m in conf)
    fresh_pos = all(results[m]["fresh_48_given_minus_newment"]["shift2"] > 0 for m in conf)
    pooled_lb = all(results[m]["pooled_136_given_minus_newment"]["cond_lb_gt0"] for m in conf)

    if gate1 and gate2:
        verdict = "MAGNITUDE-ATTACHED"
    elif gate2 and fresh_pos and not gate1:
        verdict = "PARTIAL-PROVISIONAL"
    elif not (fresh_pos and pooled_lb):
        verdict = "NO-LIFT"
    else:
        verdict = "PARTIAL-PROVISIONAL"

    gpt_shadow_lifts = results["gpt"]["pooled_136_given_minus_newment"]["cond_lb_gt0"]

    # billed cost of the mag run (the finding-bearing spend this run)
    all_rows = []
    for m in models:
        all_rows += [{"usage": u} for r in C.read_jsonl(os.path.join(HERE, "raw", f"probe-{m}.jsonl"))
                     for u in (r.get("usage") or [])]
    billed, have, missing = C.billed_cost([all_rows])

    out = {
        "verdict": verdict,
        "decisive_firewall_leg": "given_minus_newment",
        "scope": "magnitude attaches to claude+gemini (the 2 firewall-confirming models); gpt is a "
                 "displayed, replicated SHADOW (not gated). Claim particle-placement-givenness fence (j).",
        "gate1_fresh48_claude_and_gemini_lb_gt0": bool(gate1),
        "gate2_pooled136_claude_and_gemini_lb_gt0": bool(gate2),
        "gpt_shadow_lifts_at_pooled_N": bool(gpt_shadow_lifts),
        "stimuli_sha256": hashlib.sha256(open(os.path.join(HERE, "stimuli.json"), "rb").read()).hexdigest(),
        "freq_control_sha256": hashlib.sha256(open(os.path.join(HERE, "freq_control.json"), "rb").read()).hexdigest(),
        "billed_usd_mag_run": round(billed, 6), "n_cost_have": have, "n_cost_missing": missing,
        "models": results,
    }
    json.dump(out, open(os.path.join(HERE, "analysis_merged.json"), "w"), indent=2)

    print(f"VERDICT: {verdict}   (gate1 fresh48 {gate1}, gate2 pooled136 {gate2}; "
          f"gpt-shadow-lifts {gpt_shadow_lifts})")
    print(f"billed (mag run) ${billed:.5f} ({have} calls, {missing} missing)\n")
    for m in models:
        r = results[m]
        f, p, pl = (r["fresh_48_given_minus_newment"], r["prior_88_given_minus_newment"],
                    r["pooled_136_given_minus_newment"])
        tag = "SHADOW(not gated)" if m == "gpt" else "confirming"
        print(f"[{m}] ({tag})  n_frames={r['n_frames']}")
        print(f"   FRESH-48 : shift2={f['shift2']} CI={f['ci95']} pos={f['frames_pos']} "
              f"sign-p={f['sign_p']} LB>0={f['cond_lb_gt0']}")
        print(f"   PRIOR-88 : shift2={p['shift2']} CI={p['ci95']} pos={p['frames_pos']}")
        print(f"   POOLED136: shift2={pl['shift2']} CI={pl['ci95']} pos={pl['frames_pos']} "
              f"LB>0={pl['cond_lb_gt0']}")


if __name__ == "__main__":
    main()
