#!/usr/bin/env python3
"""replication_check.py -- the FROZEN rep2-vs-v1 replication predicate (s250).

Consumes this run's analysis.json (rep2, produced by the byte-frozen analyze.py) and the committed
s248 analysis.json (v1). Does NOT recompute any statistic -- it only compares the two frozen outputs
against the replication predicate pinned in PREREG.md BEFORE any model call (anti-cheat, PROTOCOL §B).

The promotable leg is the Arm-A verb-bias rho (the s248 result's "What it feeds" + the design's Q3).
The definiteness surface (Arm B within-length) is a null-leaning LENGTH-ONLY dissociation, NOT
promotable; its replication is REPORTED (does the dissociation hold up?) but never gates promotion.

FROZEN Arm-A verb-bias REPLICATION predicate (per model, then >=2/3):
  (R1) rep2 matched-rho CI-LB > 0                 -- the correlation exists on fresh items
  (R2) rep2 alternating-only rho CI-LB > 0        -- the B2 control survives (not merely the
                                                     alternating/non-alternating lexical split)
  (R3) rep2 matched-rho POINT ESTIMATE lies within v1's 95% CI -- consistent magnitude. This is the
                                                     documented sense-gradience-rep2 standard ("every
                                                     base rho within v1's CI"), and is strictly tighter
                                                     than a CI-overlap test (which the s250 freeze-vote
                                                     flagged as gameable by two wide intervals). ci_overlap
                                                     and v1-point-in-rep2-CI are kept as DESCRIPTIVE fields.
  VERB-BIAS-REPLICATES := (R1 >=2/3) and (R2 >=2/3) and (R3 >=2/3).

A VERB-BIAS-REPLICATES verdict only LICENSES a SEPARATE, precommitted cross-session promotion review; it
does NOT itself promote and does NOT automatically unlock a claim. That review (fresh reviewer + one
non-Anthropic vote) is an independent adjudication that MAY DECLINE even when VERB-BIAS-REPLICATES holds
(e.g. if the contamination caveat is judged to bar a scoped claim). Anything short of the predicate =>
report the divergence, no promotion. The overall instrument band (analyze.py::decide) is also reported:
whether the s248 LENGTH-ONLY dissociation itself replicates.
"""
import json
import os

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
V1 = os.path.abspath(os.path.join(HERE, "..", "2026-07-18-dais-option-b"))


def overlap(ci_a, ci_b):
    return not (ci_a[1] < ci_b[0] or ci_b[1] < ci_a[0])


def main():
    rep2 = json.load(open(os.path.join(HERE, "analysis.json")))
    v1 = json.load(open(os.path.join(V1, "analysis.json")))
    models = list(C.MODELS)

    rows = []
    for m in models:
        r2, r1 = rep2["arm_A"][m], v1["arm_A"][m]
        R1 = bool(r2["ci_lb_gt0"])
        R2 = bool(r2["alt_ci_lb_gt0"])
        # R3 (binding): rep2 point estimate within v1's 95% CI (sense-gradience-rep2 standard).
        R3 = bool(r1["ci_matched"][0] <= r2["rho_matched"] <= r1["ci_matched"][1])
        rows.append({
            "model": m,
            "v1_rho_matched": r1["rho_matched"], "v1_ci": r1["ci_matched"],
            "rep2_rho_matched": r2["rho_matched"], "rep2_ci": r2["ci_matched"],
            "rep2_rho_alt": r2["rho_alternating_only"], "rep2_alt_ci": r2["ci_alt"],
            "R1_ci_lb_gt0": R1, "R2_alt_ci_lb_gt0": R2, "R3_rep2_point_in_v1_ci": R3,
            # descriptive (not gating):
            "desc_ci_overlap": overlap(r2["ci_matched"], r1["ci_matched"]),
            "desc_v1_point_in_rep2_ci": bool(r2["ci_matched"][0] <= r1["rho_matched"] <= r2["ci_matched"][1]),
            "all_three": R1 and R2 and R3,
        })

    n = lambda k: sum(1 for r in rows if r[k])
    verb_bias_replicates = (n("R1_ci_lb_gt0") >= 2 and n("R2_alt_ci_lb_gt0") >= 2
                            and n("R3_rep2_point_in_v1_ci") >= 2)

    out = {
        "promotable_leg": "Arm-A verb-bias rho (matched + alternating-only B2 control)",
        "per_model": rows,
        "counts": {"R1_ci_lb_gt0": n("R1_ci_lb_gt0"), "R2_alt_ci_lb_gt0": n("R2_alt_ci_lb_gt0"),
                   "R3_rep2_point_in_v1_ci": n("R3_rep2_point_in_v1_ci")},
        "VERB_BIAS_REPLICATES": verb_bias_replicates,
        "licenses_promotion_review": verb_bias_replicates,
        "instrument_band_v1": v1["verdict"]["band"],
        "instrument_band_rep2": rep2["verdict"]["band"],
        "length_only_dissociation_replicates": (
            rep2["verdict"]["band"] == v1["verdict"]["band"] == "LENGTH-ONLY"),
    }
    json.dump(out, open(os.path.join(HERE, "replication.json"), "w"), indent=2)

    print(f"=== Arm-A VERB-BIAS-REPLICATES: {verb_bias_replicates} "
          f"(licenses promotion review: {verb_bias_replicates}) ===")
    print(f"counts (of 3): R1 ci-lb>0={out['counts']['R1_ci_lb_gt0']}  "
          f"R2 alt-ctrl={out['counts']['R2_alt_ci_lb_gt0']}  "
          f"R3 point-in-v1-CI={out['counts']['R3_rep2_point_in_v1_ci']}")
    for r in rows:
        print(f"  {r['model']}: v1 rho={r['v1_rho_matched']:+.3f} CI[{r['v1_ci'][0]:+.3f},"
              f"{r['v1_ci'][1]:+.3f}] | rep2 rho={r['rep2_rho_matched']:+.3f} "
              f"CI[{r['rep2_ci'][0]:+.3f},{r['rep2_ci'][1]:+.3f}] | alt={r['rep2_rho_alt']:+.3f} "
              f"| R1={r['R1_ci_lb_gt0']} R2={r['R2_alt_ci_lb_gt0']} R3={r['R3_rep2_point_in_v1_ci']}")
    print(f"\ninstrument band: v1={out['instrument_band_v1']}  rep2={out['instrument_band_rep2']}  "
          f"(LENGTH-ONLY dissociation replicates: {out['length_only_dissociation_replicates']})")


if __name__ == "__main__":
    main()
