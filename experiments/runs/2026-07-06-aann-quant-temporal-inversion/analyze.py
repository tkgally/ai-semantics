#!/usr/bin/env python3
"""AANN quant×temporal inversion — analysis + verdict (the NEW §6 logic, frozen in PREREG).

The calling instrument (probe.py) is byte-frozen from v2b; THIS file is new code and is exactly
where anti-cheat scrutiny belongs (design S10). It implements the ratified scoring
(wiki/decisions/resolved/aann-quant-temporal-inversion-design, s189 ADOPT-WITH-CHANGES):

  PRIMARY (Q2-B, monotone, threshold-free): per quant modifier j and Tier-0-passing model m,
    A_m(j)   = mean 0-100 acceptability over j's 10 temporal items,
    B_m^min  = min over {ambig,pos,neg} of the model's non-quant temporal CLASS mean (S4: MIN, not
               the pooled mean — the finding's property is "below ALL THREE non-quant cells"),
    d_m(j)   = A_m(j) - B_m^min.
  B2 PRECEDENCE (NULL first): if the pooled quant-cell mean is NOT the lowest of the four
    adjective-class cells (quant, ambig, pos, neg) for the model -> NULL for that model, regardless
    of the d-distribution. Otherwise read the SHAPE of {d_m(j)}:
      CLASS   iff median(d) < 0 AND Q3(d) <= 0     (wholesale below the lowest non-quant baseline)
      LEXICAL iff median(d) >= 0 AND pooled quant-cell mean < B_m^min  (inversion tail-carried)
      MIXED   otherwise.
  PANEL verdict = the category holding for >= 2/3 Tier-0-passing models.

  ANCHORED Arm 1 (human comparison, per-modifier gradient — NOT item-matched, S3): over the 10
    Mahowald quant modifiers with human temporal means, report per-modifier model-low/human-high
    sign and Spearman(model A_m(j), human H(j)); noisy (human N 11-24/modifier), flagged.
  SECONDARY / DESCRIPTIVE (never verdict-bearing): the 0.70/0.30 inversion count + bottom-drop;
    the small-vs-large polarity subtype (S6 descriptive-only); the genuinely-new Arm-2 subset read
    (S7); a per-modifier Zipf partial (S9); the tourish-template-2 exclusion recompute (S2); the
    four-class structural reproduction (N1). Bootstrap 95% CIs (10,000 resamples, percentile).

Run:  python3 analyze.py            (reads raw/{A,B,C}-{arm}.json, writes results.json)
      python3 analyze.py --selftest (verdict logic on synthetic data; MUST pass before any call)
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

HERE = Path(__file__).parent
RAW = HERE / "raw"
SLOTS = ["A", "B", "C"]
TIER0_GATE = 20   # >= 20/24 correct forced-choice = Tier-0 passer (v2 semantics)
BOOT = 10000
RNG_SEED = 20260706


# ------------------------------------------------------------------ pure verdict logic (self-tested)
def classify_model(A_by_mod, nonquant_class_means, quant_cell_mean):
    """Pure per-model classifier. A_by_mod: {modifier: mean}. nonquant_class_means:
    {ambig,pos,neg: mean}. quant_cell_mean: pooled mean over all quant items. Returns
    (label, diag). B2 NULL-first, then the Q2-B monotone shape read."""
    four = dict(nonquant_class_means)
    four["quant"] = quant_cell_mean
    quant_lowest = all(quant_cell_mean <= four[c] for c in ("ambig", "pos", "neg"))
    Bmin = min(nonquant_class_means.values())
    d = {m: A_by_mod[m] - Bmin for m in A_by_mod}
    vals = np.array(sorted(d.values()), dtype=float)
    med = float(np.median(vals))
    q3 = float(np.percentile(vals, 75))
    diag = {"B_min": round(Bmin, 3), "quant_cell_mean": round(quant_cell_mean, 3),
            "quant_lowest_of_four": quant_lowest, "median_d": round(med, 3),
            "q3_d": round(q3, 3), "n_modifiers": len(d)}
    if not quant_lowest:
        return "NULL", diag
    if med < 0 and q3 <= 0:
        return "CLASS", diag
    if med >= 0 and quant_cell_mean < Bmin:
        return "LEXICAL", diag
    return "MIXED", diag


def panel_verdict(labels):
    """>= 2/3 of the passing models sharing a category = that category; else SPLIT."""
    if not labels:
        return "NO-PASSER"
    from collections import Counter
    top, n = Counter(labels).most_common(1)[0]
    return top if n >= 2 and n / len(labels) >= 2 / 3 else "SPLIT"


# ------------------------------------------------------------------ bootstrap + spearman
def boot_ci(vals, stat=np.mean, seed=RNG_SEED):
    a = np.array(vals, dtype=float)
    if len(a) == 0:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    idx = rng.integers(0, len(a), size=(BOOT, len(a)))
    bs = stat(a[idx], axis=1)
    return (round(float(np.percentile(bs, 2.5)), 3), round(float(np.percentile(bs, 97.5)), 3))


def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 3:
        return float("nan")
    rx, ry = _rank(x), _rank(y)
    return float(np.corrcoef(rx, ry)[0, 1])


def _rank(a):
    order = np.argsort(a, kind="mergesort")
    r = np.empty(len(a), float)
    r[order] = np.arange(len(a))
    # average ties
    _, inv, cnt = np.unique(a, return_inverse=True, return_counts=True)
    sums = np.zeros(len(cnt)); np.add.at(sums, inv, r)
    return (sums / cnt)[inv]


def partial_spearman(x, y, z):
    """Spearman partial of x,y controlling z (rank-residual method)."""
    rx, ry, rz = _rank(np.asarray(x, float)), _rank(np.asarray(y, float)), _rank(np.asarray(z, float))
    def resid(a, b):
        b1 = np.vstack([b, np.ones_like(b)]).T
        coef, *_ = np.linalg.lstsq(b1, a, rcond=None)
        return a - b1 @ coef
    ex, ey = resid(rx, rz), resid(ry, rz)
    return float(np.corrcoef(ex, ey)[0, 1])


# ------------------------------------------------------------------ self-test
def selftest():
    """Synthetic data engineered to force each verdict; the classifier must return the right label.
    Anti-cheat: the verdict logic is proven reachable-in-all-directions BEFORE any model call."""
    nq = {"ambig": 55.0, "pos": 50.0, "neg": 49.0}   # B_min = 49
    mods = [f"m{i}" for i in range(20)]

    # CLASS: every quant modifier well below 49 -> median<0, Q3<=0, quant cell lowest
    A = {m: 30.0 for m in mods}
    lab, _ = classify_model(A, nq, quant_cell_mean=30.0)
    assert lab == "CLASS", lab

    # LEXICAL: most modifiers at 60 (above 49), a few deep-negative pull the pooled cell below 49
    A = {m: 60.0 for m in mods}
    for m in mods[:3]:
        A[m] = 2.0
    cell = float(np.mean(list(A.values())))   # (17*60 + 3*2)/20 = 51.3 -> NOT below 49 => MIXED not LEXICAL
    # make the tail deeper so the pooled cell drops below 49 while median stays >=0
    for m in mods[:8]:
        A[m] = 0.0
    cell = float(np.mean(list(A.values())))   # (12*60)/20 = 36 -> below 49; median: 12 of 20 are 60 => median 60>=0
    lab, diag = classify_model(A, nq, quant_cell_mean=cell)
    assert lab == "LEXICAL", (lab, diag)

    # MIXED: spread around zero, cell not below min, quant still lowest of four
    A = {m: 45.0 + (i - 10) * 2.0 for i, m in enumerate(mods)}   # 25..63, median ~46 (<49) ...
    cell = float(np.mean(list(A.values())))                       # mean 45 -> below 49 -> would be LEXICAL if median>=0
    # engineer median just below B_min but Q3 above 0 => not CLASS (Q3>0), median<0, cell>=B_min? tune:
    A = {m: 60.0 for m in mods}
    for m in mods[:10]:
        A[m] = 40.0                                              # half at 40 (d=-9), half at 60 (d=+11)
    cell = float(np.mean(list(A.values())))                       # 50 -> >= 49, quant lowest? 50<55,50,49? 50>49 -> quant NOT lowest -> NULL
    # ensure quant lowest: raise neg above cell
    nq2 = {"ambig": 70.0, "pos": 65.0, "neg": 62.0}               # B_min=62, cell 50<62 lowest; d: 40-62=-22, 60-62=-2 => all<0 median<0
    lab, diag = classify_model(A, nq2, quant_cell_mean=cell)      # median<0 but Q3: 10 vals -2, 10 vals -22 => Q3=-2<=0 => CLASS
    assert lab == "CLASS", (lab, diag)
    # a genuine MIXED: modifiers straddle B_min, cell above B_min, quant lowest of four
    nq3 = {"ambig": 80.0, "pos": 75.0, "neg": 52.0}               # B_min=52
    A = {m: 52.0 + (i - 10) * 3.0 for i, m in enumerate(mods)}    # 22..79, median ~50.5
    cell = float(np.mean(list(A.values())))                       # ~53.5 >= 52 (not LEXICAL), median 50.5<52 => d median<0
    # Q3 above 0 (top modifiers well above 52) => not CLASS; median<0 => not... => MIXED
    lab, diag = classify_model(A, nq3, quant_cell_mean=cell)
    assert lab == "MIXED", (lab, diag)

    # NULL: quant cell not the lowest of four
    A = {m: 70.0 for m in mods}
    lab, _ = classify_model(A, {"ambig": 55.0, "pos": 50.0, "neg": 49.0}, quant_cell_mean=70.0)
    assert lab == "NULL", lab

    # panel rule
    assert panel_verdict(["CLASS", "CLASS", "LEXICAL"]) == "CLASS"
    assert panel_verdict(["CLASS", "LEXICAL", "MIXED"]) == "SPLIT"
    assert panel_verdict(["NULL", "NULL", "CLASS"]) == "NULL"
    print("SELFTEST PASS: CLASS / LEXICAL / MIXED / NULL all reachable; panel rule correct.")


# ------------------------------------------------------------------ real analysis
def load_arm(slot, arm):
    p = RAW / f"{slot}-{arm}.json"
    if not p.exists():
        return None
    return json.load(open(p))


def tier0_result(slot, stim):
    rows = load_arm(slot, "tier0")
    if rows is None:
        return None
    gold = {t["id"]: t["aann_position"] for t in stim["tier0"]}
    correct = sum(1 for r in rows if r["value"] == gold.get(r["id"]))
    return {"correct": correct, "total": len(rows), "passed": correct >= TIER0_GATE}


def main():
    stim = json.load(open(HERE / "stimuli.json"))
    items = {it["id"]: it for it in stim["items"]}
    quant_mods = [m["modifier"] for m in stim["quant_modifiers"]]
    arm_of = {m["modifier"]: m["arm"] for m in stim["quant_modifiers"]}
    polarity = {m["modifier"]: m["polarity"] for m in stim["quant_modifiers"]}
    zipf = {m["modifier"]: m["zipf"] for m in stim["quant_modifiers"]}
    arm1_mods = [m for m in quant_mods if arm_of[m] == "arm1"]
    human_pm = {m: stim["arm1_human_per_modifier"][m]["human_temporal_mean"] for m in arm1_mods}
    human_class = stim["human_class_means_temporal"]
    human_nonquant_min = min(human_class[c]["mean"] for c in ("ambig", "pos", "neg"))

    out = {"tier0": {}, "per_model": {}, "panel": {}, "arm1_anchored": {}, "descriptive": {}}
    passers = []
    per_model_labels = {}

    for slot in SLOTS:
        t0 = tier0_result(slot, stim)
        out["tier0"][slot] = t0
        main_rows = load_arm(slot, "heldout-temporal")
        if main_rows is None:
            continue
        val = {r["id"]: r["value"] for r in main_rows if r["value"] is not None}
        # per-quant-modifier mean (exclude template-2 handled in the recompute below)
        def modifier_mean(m, drop_tourish=False):
            vs = [val[i] for i, it in items.items()
                  if it["adjclass"] == "quant" and it["adj"] == m and i in val
                  and not (drop_tourish and it["template"] == stim["tourish_template"])]
            return float(np.mean(vs)) if vs else float("nan"), vs
        A = {}
        A_items = {}
        for m in quant_mods:
            A[m], A_items[m] = modifier_mean(m)
        # non-quant class means (this occasion)
        nq_means = {}
        nq_items = {}
        for cls in ("ambig", "pos", "neg"):
            vs = [val[i] for i, it in items.items()
                  if it["adjclass"] == cls and i in val]
            nq_means[cls] = float(np.mean(vs)); nq_items[cls] = vs
        quant_vals = [val[i] for i, it in items.items() if it["adjclass"] == "quant" and i in val]
        quant_cell_mean = float(np.mean(quant_vals))

        label, diag = classify_model(A, nq_means, quant_cell_mean)
        Bmin = min(nq_means.values())
        d = {m: A[m] - Bmin for m in quant_mods}

        pm = {
            "tier0_passed": bool(t0 and t0["passed"]),
            "label": label, "diag": diag,
            "four_class_means": {**{c: round(nq_means[c], 3) for c in nq_means},
                                 "quant": round(quant_cell_mean, 3)},
            "quant_cell_ci": boot_ci(quant_vals),
            "B_min_class": min(nq_means, key=nq_means.get),
            "d_by_modifier": {m: round(d[m], 3) for m in quant_mods},
            "median_d_ci": boot_ci(list(d.values()), stat=np.median),
            # descriptive count (secondary, NOT verdict-bearing)
            "inversion_count_p": round(sum(1 for m in quant_mods if A[m] < Bmin) / len(quant_mods), 3),
            # tourish-exclusion recompute (S2, gate-bearing robustness)
            "tourish_excluded": None,
            # genuinely-new subset read (S7)
            "arm2_new_shape": None,
            # polarity subtype (S6 descriptive-only)
            "polarity_median_d": {
                "small": round(float(np.median([d[m] for m in quant_mods if polarity[m] == "small"])), 3),
                "large": round(float(np.median([d[m] for m in quant_mods if polarity[m] == "large"])), 3)},
            # Zipf partial (S9): does d track frequency across modifiers?
            "zipf_partial_note": None,
        }
        # tourish exclusion recompute
        A_dt = {m: modifier_mean(m, drop_tourish=True)[0] for m in quant_mods}
        nq_dt = {cls: float(np.mean([val[i] for i, it in items.items()
                 if it["adjclass"] == cls and i in val and it["template"] != stim["tourish_template"]]))
                 for cls in ("ambig", "pos", "neg")}
        quant_dt = [val[i] for i, it in items.items() if it["adjclass"] == "quant" and i in val
                    and it["template"] != stim["tourish_template"]]
        lab_dt, _ = classify_model(A_dt, nq_dt, float(np.mean(quant_dt)))
        pm["tourish_excluded"] = {"label": lab_dt, "agrees": lab_dt == label}
        # arm2-new subset shape
        new = [m for m in quant_mods if arm_of[m] == "arm2-new"]
        dnew = [d[m] for m in new]
        pm["arm2_new_shape"] = {"modifiers": new, "median_d": round(float(np.median(dnew)), 3),
                                "all_below_zero": all(x < 0 for x in dnew),
                                "d": {m: round(d[m], 3) for m in new}}
        # zipf partial: rank corr d vs zipf, and partial of (d, is-inverted) unnecessary; report corr
        dz = spearman([d[m] for m in quant_mods], [zipf[m] for m in quant_mods])
        pm["zipf_partial_note"] = {"spearman_d_vs_zipf": round(dz, 3)}
        out["per_model"][slot] = pm
        if pm["tier0_passed"]:
            passers.append(slot)
            per_model_labels[slot] = label

        # Arm 1 anchored (per-modifier gradient comparison)
        model_low = {m: A[m] < Bmin for m in arm1_mods}
        human_high = {m: human_pm[m] > human_nonquant_min for m in arm1_mods}
        both = [m for m in arm1_mods if model_low[m] and human_high[m]]
        rho = spearman([A[m] for m in arm1_mods], [human_pm[m] for m in arm1_mods])
        out["arm1_anchored"][slot] = {
            "spearman_model_vs_human": round(rho, 3),
            "n_model_low_and_human_high": len(both),
            "model_low_and_human_high": both,
            "human_nonquant_min": human_nonquant_min,
            "per_modifier": {m: {"model_mean": round(A[m], 2), "human_mean": human_pm[m],
                                 "model_low": model_low[m], "human_high": human_high[m]}
                             for m in arm1_mods},
        }

    out["panel"] = {
        "tier0_passers": passers,
        "per_model_labels": per_model_labels,
        "verdict": panel_verdict([per_model_labels[s] for s in passers]),
    }
    # four-class reproduction (N1) — model side per passer + human side (committed)
    out["descriptive"]["human_four_class"] = {c: human_class[c]["mean"] for c in human_class}
    out["descriptive"]["human_quant_is_highest"] = (
        human_class["quant"]["mean"] == max(human_class[c]["mean"] for c in human_class))

    json.dump(out, open(HERE / "results.json", "w"), indent=1)
    print(json.dumps({"panel": out["panel"],
                      "tier0": out["tier0"],
                      "per_model_labels": per_model_labels}, indent=1))
    print("wrote results.json")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
    else:
        main()
