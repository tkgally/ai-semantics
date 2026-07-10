#!/usr/bin/env python3
"""analyze.py — score the frozen BLiMP forced-choice sweep (A3b, s205). Recomputes every figure from
raw/ only. Thresholds are FROZEN in PREREG.md and copied here as constants; nothing is tuned post-hoc.

Readings (RATIFIED Q1-B/Q2-A/Q3-A + C8):
  R1 (PRIMARY, human-anchored, DESCRIPTIVE/DIRECTIONAL-ONLY per C8+F2): rho_prof(m) = Spearman across the
     40 paradigms of order-averaged accuracy vs human agreement, per model, with bootstrap CI + power.
  R2 (SECONDARY, STRICTLY within-panel): depth gradient — mean acc(shallow=local) vs deep(scope+island),
     F4 floor applied (all 40 pass). Verdict-bearing.
  R2h (human-anchored sub-reading): does the panel's shallow-minus-deep accuracy gap EXCEED the human
     shallow-minus-deep agreement gap? (panel finds deep contrasts disproportionately harder than humans)
  Diagnostics: order-flip / position-lock (instrument-failure guard, Q2-A); F3 saturation/range guard;
     absolute-accuracy dispersion (contamination diagnostic; absolute acc = upper bound).
"""
import json, math, os
from pathlib import Path
import numpy as np

HERE = Path(__file__).parent
RAW = HERE / "raw"
ITEMS = json.load(open(HERE / "items.json"))
PARA = {p["uid"]: p for p in ITEMS["paradigms"]}
UIDS = [p["uid"] for p in ITEMS["paradigms"]]
SLOTS = ["A", "B", "C"]

# ---- FROZEN thresholds (PREREG) ----
PROFILE_ALIGNED = 0.40      # rho_prof > this on >=2/3  -> ALIGNED (directional; non-promotable per C8)
PROFILE_DIVERGES = 0.20     # rho_prof < this on >=2/3  -> DIVERGES; [0.20,0.40] = INCONCLUSIVE band
SATURATION_SD = 0.03        # F3: per-model per-paradigm acc SD below this -> rho INCONCLUSIVE (near-const)
DEPTH_MARGIN = 0.05         # R2: mean acc(shallow)-mean acc(deep) >= this on >=2/3 -> DEPTH-GRADED
R2H_MARGIN = 0.05           # R2h: (panel gap - human gap) > this -> EXCEEDS-HUMAN-DIP
POSLOCK_FAIL = 0.50         # instrument-failure if position-lock > this AND
ANS1_EXTREME = 0.40         #   |P(answer=1) - 0.5| > this
BOOT = 5000
SEED = 20260710
SHALLOW = {"local"}
DEEP = {"scope", "island"}
F4_FLOOR = 0.60             # F4: paradigms below this are dropped from the reading-2 accuracy strata
                            # (contested gold). Inert this run (all 40 clear it) but enforced in code.


def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    def rank(v):
        order = v.argsort()
        r = np.empty(len(v)); r[order] = np.arange(len(v))
        # average ties
        _, inv, cnt = np.unique(v, return_inverse=True, return_counts=True)
        sums = np.zeros(len(cnt)); np.add.at(sums, inv, r)
        avg = sums / cnt
        return avg[inv]
    rx, ry = rank(x), rank(y)
    rx -= rx.mean(); ry -= ry.mean()
    d = math.sqrt((rx @ rx) * (ry @ ry))
    return float(rx @ ry / d) if d else float("nan")


def load(slot):
    """Return per-paradigm stats for one model from raw/{slot}-{uid}.json."""
    out = {}
    ans1 = poslock_num = poslock_den = 0
    for uid in UIDS:
        f = RAW / f"{slot}-{uid}.json"
        rows = json.load(open(f))
        by_pair = {}
        for r in rows:
            if r["choice"] == 1:
                ans1 += 1
            by_pair.setdefault(r["pairID"], {})[r["order"]] = r
        oa, cons = [], []          # order-averaged correct, consistency (correct both orders)
        for pid, od in by_pair.items():
            gf, gs = od.get("gf"), od.get("gs")
            cs = [x["correct"] for x in (gf, gs) if x and x["correct"] is not None]
            if cs:
                oa.append(sum(cs) / len(cs))
            if gf and gs and gf["choice"] is not None and gs["choice"] is not None:
                cons.append(1.0 if (gf["correct"] and gs["correct"]) else 0.0)
                poslock_den += 1
                if gf["choice"] == gs["choice"]:   # same DIGIT in both orders -> position-locked
                    poslock_num += 1
        out[uid] = {"acc": float(np.mean(oa)) if oa else float("nan"),
                    "consistency": float(np.mean(cons)) if cons else float("nan"),
                    "n_pairs": len(by_pair), "human": PARA[uid]["human_agreement"],
                    "stratum": PARA[uid]["stratum"]}
    n_calls = sum(len(json.load(open(RAW / f"{slot}-{uid}.json"))) for uid in UIDS)
    diag = {"ans1_rate": ans1 / n_calls, "poslock_rate": poslock_num / poslock_den if poslock_den else float("nan"),
            "n_calls": n_calls}
    return out, diag


def strat_mean(per, keys):
    # F4: only paradigms clearing the 0.60 human-agreement floor enter the reading-2 accuracy strata.
    v = [per[u]["acc"] for u in UIDS
         if per[u]["stratum"] in keys and PARA[u]["human_agreement"] >= F4_FLOOR]
    return float(np.mean(v)), len(v)


def main():
    rng = np.random.default_rng(SEED)
    result = {"per_model": {}, "readings": {}}
    accs, humans = {}, np.array([PARA[u]["human_agreement"] for u in UIDS])

    for slot in SLOTS:
        per, diag = load(slot)
        acc = np.array([per[u]["acc"] for u in UIDS])
        accs[slot] = acc
        rho = spearman(acc, humans)
        # bootstrap CI over paradigms
        boots = []
        for _ in range(BOOT):
            idx = rng.integers(0, len(UIDS), len(UIDS))
            boots.append(spearman(acc[idx], humans[idx]))
        lo, hi = np.percentile(boots, [2.5, 97.5])
        acc_sd = float(acc.std(ddof=1))
        saturated = acc_sd < SATURATION_SD
        sh, nsh = strat_mean(per, SHALLOW)
        dp, ndp = strat_mean(per, DEEP)
        md, nmd = strat_mean(per, {"medium"})
        mean_cons = float(np.nanmean([per[u]["consistency"] for u in UIDS]))
        # per-category means (freeze-vote condition: show whether one category carries R2)
        cats = sorted({PARA[u]["category"] for u in UIDS})
        by_cat = {c: round(float(np.mean([per[u]["acc"] for u in UIDS if PARA[u]["category"] == c])), 4)
                  for c in cats}
        result["per_model"][slot] = {
            "rho_prof": rho, "rho_ci": [float(lo), float(hi)], "acc_sd": acc_sd,
            "saturated_F3": saturated,
            "mean_abs_acc": float(acc.mean()), "acc_min": float(acc.min()), "acc_max": float(acc.max()),
            "mean_consistency_acc": mean_cons,
            "shallow_acc": sh, "deep_acc": dp, "medium_acc": md,
            "depth_gap": sh - dp,
            "ans1_rate": diag["ans1_rate"], "poslock_rate": diag["poslock_rate"],
            "n_calls": diag["n_calls"],
            "per_category_acc": by_cat,
            "per_paradigm": {u: round(per[u]["acc"], 4) for u in UIDS},
        }

    # human shallow/deep gap (fixed, model-independent)
    hsh = float(np.mean([PARA[u]["human_agreement"] for u in UIDS if PARA[u]["stratum"] in SHALLOW]))
    hdp = float(np.mean([PARA[u]["human_agreement"] for u in UIDS if PARA[u]["stratum"] in DEEP]))
    human_gap = hsh - hdp

    def maj(pred):  # >=2/3 models
        return sum(1 for s in SLOTS if pred(s)) >= 2

    pm = result["per_model"]
    # R1 (directional; per C8 non-promotable this run)
    aligned = maj(lambda s: (not pm[s]["saturated_F3"]) and pm[s]["rho_prof"] > PROFILE_ALIGNED)
    diverges = maj(lambda s: (not pm[s]["saturated_F3"]) and pm[s]["rho_prof"] < PROFILE_DIVERGES)
    r1 = "PROFILE-ALIGNED" if aligned else ("PROFILE-DIVERGES" if diverges else "PROFILE-INCONCLUSIVE")
    # R2 within-panel depth
    graded = maj(lambda s: pm[s]["depth_gap"] >= DEPTH_MARGIN)
    r2 = "DEPTH-GRADED" if graded else "DEPTH-FLAT"
    # R2h human-anchored excess
    exceeds = maj(lambda s: (pm[s]["depth_gap"] - human_gap) > R2H_MARGIN)
    tracks = maj(lambda s: abs(pm[s]["depth_gap"] - human_gap) <= R2H_MARGIN)
    r2h = "EXCEEDS-HUMAN-DIP" if exceeds else ("TRACKS-DIP" if tracks else "BELOW-HUMAN-DIP")
    # instrument-failure guard
    instr_fail = maj(lambda s: pm[s]["poslock_rate"] > POSLOCK_FAIL and abs(pm[s]["ans1_rate"] - 0.5) > ANS1_EXTREME)

    # per-category human agreement (observed-set context for R1)
    cats = sorted({PARA[u]["category"] for u in UIDS})
    human_by_cat = {c: round(float(np.mean([PARA[u]["human_agreement"] for u in UIDS
                                            if PARA[u]["category"] == c])), 4) for c in cats}
    result["readings"] = {
        "observed_set_note": ("R1/R2/R2h are over the 40-paradigm OBSERVED on-axis set, not full BLiMP; "
                              "verdicts scope to THIS frozen panel, not a universal depth law (freeze-vote "
                              "condition)."),
        "human_by_category": human_by_cat,
        "human_shallow_acc": hsh, "human_deep_acc": hdp, "human_gap": human_gap,
        "R1_profile_alignment": r1 + " (DESCRIPTIVE/DIRECTIONAL ONLY — non-promotable this run per C8)",
        "R1_rho_by_model": {s: [round(pm[s]["rho_prof"], 3)] + [round(x, 3) for x in pm[s]["rho_ci"]] for s in SLOTS},
        "R1_power_note": f"n=40 paradigms; two-sided p<0.05 at |rho|~0.31; PROFILE_ALIGNED band {PROFILE_ALIGNED} is above that.",
        "R2_depth_gradient_within_panel": r2,
        "R2_depth_gap_by_model": {s: round(pm[s]["depth_gap"], 4) for s in SLOTS},
        "R2h_vs_human_dip": r2h,
        "instrument_failure": instr_fail,
        "contamination_diag_abs_acc": {s: [round(pm[s]["mean_abs_acc"], 4), round(pm[s]["acc_sd"], 4)] for s in SLOTS},
    }
    json.dump(result, open(HERE / "results.json", "w"), indent=1)

    print("=== BLiMP forced-choice sweep — results (s205) ===")
    print(f"human: shallow(local) {hsh:.3f}  deep(scope+island) {hdp:.3f}  gap {human_gap:+.3f}")
    for s in SLOTS:
        m = pm[s]
        print(f"\n[{s}] n_calls={m['n_calls']}  abs_acc {m['mean_abs_acc']:.3f} (SD {m['acc_sd']:.3f}, "
              f"{m['acc_min']:.2f}-{m['acc_max']:.2f}){'  <F3-SATURATED>' if m['saturated_F3'] else ''}")
        print(f"     rho_prof {m['rho_prof']:+.3f}  CI[{m['rho_ci'][0]:+.3f},{m['rho_ci'][1]:+.3f}]")
        print(f"     acc shallow {m['shallow_acc']:.3f} / medium {m['medium_acc']:.3f} / deep {m['deep_acc']:.3f}"
              f"  depth-gap {m['depth_gap']:+.3f}   consistency {m['mean_consistency_acc']:.3f}")
        print(f"     per-category: " + "  ".join(f"{c}={v:.2f}" for c, v in m["per_category_acc"].items()))
        print(f"     ans1_rate {m['ans1_rate']:.3f}  poslock {m['poslock_rate']:.3f}")
    r = result["readings"]
    print("\n--- VERDICTS ---")
    print("R1 profile:", r["R1_profile_alignment"])
    print("R2 depth (within-panel):", r["R2_depth_gradient_within_panel"], r["R2_depth_gap_by_model"])
    print("R2h vs human dip:", r["R2h_vs_human_dip"])
    print("instrument-failure:", r["instrument_failure"])


if __name__ == "__main__":
    main()
