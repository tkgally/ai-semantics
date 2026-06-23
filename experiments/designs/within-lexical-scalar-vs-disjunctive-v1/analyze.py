#!/usr/bin/env python3
"""Within-lexical scalar-vs-disjunctive analysis -- the FROZEN reading rule (NO API).

Built with the frozen instrument (2026-06-23); reads raw/ (does NOT exist until a probe runs).
Applies instrument.json -> reading_rule_frozen with no threshold tuned after any output.

Per model, per arm (scalar / disjunctive):
  - decline rate (%UNCLEAR) on the AMBIGUOUS class (scalar: bridging; disjunctive: disjunctive)
    vs the pooled CLEAR classes (clear-same + clear-different);
  - mean confidence (corroborates only, C1);
  - C3 clear-class precondition (clear decline < 0.20 AND clear conf > 70);
  - WITHIN-ARM clustered-bootstrap CI on the decline gap (ambiguous - clear).
Cross-arm: clustered-bootstrap CI on (disjunctive arm decline - scalar bridging decline), the
two arms resampled as independent groups (clusters: lemma for scalar, homonym surface for arm2).

Per-model SURVIVAL vs COLLAPSE (frozen, gate Q3):
  COLLAPSE  : disjunctive within-arm decline-gap CI lower bound > 0 (decline elevated over its
              own clear controls).  [within-arm; robust to the Arm1-vs-Arm2 register residual]
  SURVIVAL  : disjunctive within-arm gap CI lower bound NOT > 0  AND  cross-arm gap CI includes 0
              AND disjunctive decline near-zero.  [higher bar: both within- and cross-arm]
  MIXED/INCONCLUSIVE : anything else, or C3 fails for an arm, or N too thin.

Bootstrap: 10000 reps, seed 20260623, 95% percentile CIs. Direction-of-effect only; small
clustered N -> wide CIs, no coverage claim. NO human comparison: scalar capped to
usage-similarity; disjunctive internal-contrast-only.

Run (after a probe run): python3 analyze.py   (reads raw/, writes analysis.json, prints table)
"""
import json
import os
import random
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
SEED = 20260623
REPS = 10000

ARMS = {  # arm -> (ambiguous_class, [clear_classes])
    "scalar": ("bridging", ["clear-same", "clear-different"]),
    "disjunctive": ("disjunctive", ["clear-same", "clear-different"]),
}
CLEAR_DECLINE_MAX = 0.20
CLEAR_CONF_MIN = 70
NEAR_ZERO_DECLINE = 0.10  # "near-zero" point estimate for the survival criterion

# PRE-REGISTERED clean subset (declared BEFORE any model output, on linguistic grounds only, by
# the independent pre-run critic 2026-06-23). The critic judged 8/12 disjunctive balanced ctx1
# contexts genuinely two-way and flagged 4 as leaning toward one sense (mole/punch/club mild,
# pupil strong). Because each balanced ctx1 is paired with a sense-fixed ctx2, a lean in EITHER
# direction suppresses UNCLEAR and biases TOWARD survival -> leaners erode the collapse signal.
# So the within-arm collapse statistic is reported on BOTH all-12 and this clean-8 subset. This
# is a fixed linguistic partition fixed pre-run, NOT a post-hoc re-selection against model
# confidence (no model output existed when it was declared); items_arm2.json is unchanged.
CLEAN_SUBSET = {"bank", "crane", "file", "organ", "trunk", "tank", "plot", "ring"}
LEANING_DISCLOSED = {"mole": "toward spy (B)", "punch": "toward drink (B)",
                     "club": "toward heirloom-stick (B)", "pupil": "toward student (B), strong"}


def load_arm(arm, slot):
    p = os.path.join(RAW, f"{arm}_{slot}.json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None


def rates(recs):
    n = len(recs)
    if n == 0:
        return None, None, 0
    decl = sum(1 for r in recs if (r.get("call") or "").upper() == "UNCLEAR") / n
    confs = [r["conf"] for r in recs if r.get("conf") is not None]
    mconf = sum(confs) / len(confs) if confs else None
    return decl, mconf, n


def decline_stat(rs):
    return rates(rs)[0]


def conf_stat(rs):
    return rates(rs)[1]


def clustered_gap(group_a, group_b, stat):
    """95% CI on (stat(a) - stat(b)) resampling CLUSTERS (rec['cluster']) with replacement."""
    rng = random.Random(SEED)
    ca, cb = defaultdict(list), defaultdict(list)
    for r in group_a:
        ca[r.get("cluster") or r["item_id"]].append(r)
    for r in group_b:
        cb[r.get("cluster") or r["item_id"]].append(r)
    ak, bk = list(ca), list(cb)
    if not ak or not bk:
        return None
    gaps = []
    for _ in range(REPS):
        a = [x for k in (rng.choice(ak) for _ in ak) for x in ca[k]]
        b = [x for k in (rng.choice(bk) for _ in bk) for x in cb[k]]
        sa, sb = stat(a), stat(b)
        if sa is None or sb is None:
            continue
        gaps.append(sa - sb)
    if not gaps:
        return None
    gaps.sort()
    return round(gaps[int(0.025 * len(gaps))], 4), round(gaps[int(0.975 * len(gaps)) - 1], 4)


def analyze_arm(arm, slot):
    amb_class, clear_classes = ARMS[arm]
    recs = load_arm(arm, slot)
    if not recs:
        return None
    by_class = defaultdict(list)
    for r in recs:
        by_class[r.get("class")].append(r)
    amb = by_class.get(amb_class, [])
    clear = [r for cc in clear_classes for r in by_class.get(cc, [])]
    a_decl, a_conf, a_n = rates(amb)
    c_decl, c_conf, c_n = rates(clear)
    precond_ok = (c_decl is not None and c_decl <= CLEAR_DECLINE_MAX
                  and c_conf is not None and c_conf >= CLEAR_CONF_MIN)
    decl_gap = clustered_gap(amb, clear, decline_stat)
    conf_gap = clustered_gap(amb, clear, conf_stat)
    decline_elevated = decl_gap is not None and decl_gap[0] > 0
    conf_lower = conf_gap is not None and conf_gap[1] < 0
    c4_self_report_only = conf_lower and not decline_elevated
    return {"arm": arm, "model": slot, "ambiguous_class": amb_class,
            "ambiguous": {"n": a_n, "decline_rate": a_decl, "mean_conf": a_conf},
            "clear": {"n": c_n, "decline_rate": c_decl, "mean_conf": c_conf},
            "within_arm_decline_gap_ci_amb_minus_clear": decl_gap,
            "within_arm_conf_gap_ci_amb_minus_clear": conf_gap,
            "C3_precondition_ok": precond_ok,
            "decline_elevated_within_arm": decline_elevated,
            "C4_confidence_only_self_report": c4_self_report_only,
            "_amb_recs": amb, "_clear_recs": clear}  # carried for gaps; stripped before json dump


def per_model_verdict(slot, scalar, disj):
    if not (scalar and disj):
        return {"verdict": "WEAK (an arm is missing)"}
    cross = clustered_gap(disj["_amb_recs"], scalar["_amb_recs"], decline_stat)  # disj - bridging
    # within-arm collapse statistic ALSO on the pre-registered clean-8 subset (robustness)
    clean_amb = [r for r in disj["_amb_recs"] if r.get("cluster") in CLEAN_SUBSET]
    clean_clear = [r for r in disj["_clear_recs"] if r.get("cluster") in CLEAN_SUBSET]
    clean_gap = clustered_gap(clean_amb, clean_clear, decline_stat)
    clean_decl = rates(clean_amb)[0]
    out = {"model": slot,
           "scalar_C3_ok": scalar["C3_precondition_ok"],
           "disjunctive_C3_ok": disj["C3_precondition_ok"],
           "disjunctive_decline_all12": disj["ambiguous"]["decline_rate"],
           "disjunctive_decline_clean8": clean_decl,
           "scalar_bridging_decline": scalar["ambiguous"]["decline_rate"],
           "within_arm_disj_gap_ci_all12": disj["within_arm_decline_gap_ci_amb_minus_clear"],
           "within_arm_disj_gap_ci_clean8": clean_gap,
           "cross_arm_disj_minus_bridging_ci": cross,
           "leaning_items_disclosed": LEANING_DISCLOSED}
    if not disj["C3_precondition_ok"]:
        out["verdict"] = "WEAK (disjunctive arm fails C3 clear-class precondition)"
        return out
    within_elevated = disj["decline_elevated_within_arm"]
    cross_includes_0 = cross is not None and cross[0] <= 0 <= cross[1]
    near_zero = (disj["ambiguous"]["decline_rate"] is not None
                 and disj["ambiguous"]["decline_rate"] <= NEAR_ZERO_DECLINE)
    if within_elevated:
        out["verdict"] = ("COLLAPSE: disjunctive decline elevated over its own clear controls "
                          "(within-arm CI lower bound > 0) -> kind-reading supported; the lexical "
                          "commit-without-hedging was an artifact of the softer scalar stimulus")
    elif (not within_elevated) and cross_includes_0 and near_zero:
        out["verdict"] = ("SURVIVAL: disjunctive decline near-zero, NOT elevated within-arm, AND "
                          "indistinguishable from scalar bridging (cross-arm CI includes 0) -> "
                          "lexical commit-without-hedging survives a genuine disjunction (HIGHER "
                          "bar met); register residual cuts toward survival -- led with")
    else:
        out["verdict"] = ("MIXED/INCONCLUSIVE: not within-arm elevated, but the survival "
                          "conjunction is not fully met (cross-arm distinguishable or decline not "
                          "near-zero) -> no clean survival/collapse for this model")
    return out


def main():
    if not os.path.isdir(RAW) or not os.listdir(RAW):
        print("raw/ is empty -- no probe has run yet. analyze.py is frozen and ready; run "
              "probe.py (in a later, cleared session) first.")
        return
    per, verdicts = [], {}
    for slot in ["A", "B", "C"]:
        sc = analyze_arm("scalar", slot)
        dj = analyze_arm("disjunctive", slot)
        verdicts[slot] = per_model_verdict(slot, sc, dj)
        for r in (sc, dj):
            if r:
                r.pop("_amb_recs", None)
                r.pop("_clear_recs", None)
                per.append(r)
                print(json.dumps(r, indent=1))
    print("\n=== PER-MODEL SURVIVAL/COLLAPSE VERDICTS ===")
    print(json.dumps(verdicts, indent=1))
    json.dump({"per_arm": per, "per_model_verdict": verdicts,
               "scope_cap": "NO human comparison; scalar capped to usage-similarity; "
                            "disjunctive internal-contrast-only. Behavioural, n=3 commercial "
                            "models, small clustered N, direction-of-effect only."},
              open(os.path.join(HERE, "analysis.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
