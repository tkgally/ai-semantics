#!/usr/bin/env python3
"""analyze.py — frozen analysis for the REPEATED-RUNS temp-0 jitter measurement (NO API).

Characterizes the run-to-run label jitter that session 62 surfaced (~12% from a single
s60->s62 pair) by scoring the byte-identical forced-decomposition instrument K times at
temperature 0 over the SAME frozen 63-item set. This is a MEASUREMENT, not a pass/fail probe:
the frozen output is the jitter distribution, not a verdict on the let-alone residual.

Pre-registered questions (PREREG.md):

  Q1 (per-run accuracy spread — the jitter on the headline number). For each model and each
     cell (let-alone combined n=33 / let-alone test n=24 / let-alone train n=9 / comp-corr
     n=30), the K per-run accuracies and their {mean, min, max, range=max-min, sample SD}.
     The across-run RANGE and SD ARE the jitter on a single-run point estimate.

  Q2 (per-item label stability — what drives the jitter). For each model and cell: per-item
     label counts over the K runs, the modal label, whether the item is CONSTANT (all K
     equal), the churn rate (fraction non-constant), and the mean pairwise label agreement
     across the C(K,2) run-pairs (the symmetric generalization of s62's "21/24 agreement").

  Q3 (trigger (a) — does jitter shrink at the ceiling?). Contrast the let-alone churn/range
     against the comp-corr (ceiling control) churn/range. essay/point-estimate-is-a-draw
     revision trigger (a) FIRES if jitter is concentrated at the hard near-chance let-alone
     and is negligible at the comp-corr ceiling (narrowing the essay from "single-run point
     estimates are draws" to "...on hard, near-chance, functional instruments are draws").

  Q4 (the de-noised / pinned estimate). Majority-vote accuracy (per-item modal label vs gold)
     and its Wilson CI per model+cell: the best single de-noised estimate the K runs support.
     For gpt let-alone combined, does the across-run MAX accuracy still stay below the 0.90
     human baseline? (Pins the residual magnitude the session-62 result left at ~±0.12.)

  Q5 (uptake + ceiling guard). Every run must have uptake INDUCED on let-alone (>=80% worked)
     and the comp-corr control at/near ceiling; a run that breaks either is flagged (it would
     contaminate the jitter read with a scaffold failure, not measure label noise).

  Q6 (cross-session corroboration; honest framing). The K runs are SAME-SESSION, so their
     spread is a within-session figure and may UNDERESTIMATE true run-to-run jitter. The
     s60 draw (24 LA test + 30 CC) and the s62 draw (all 63) are CROSS-SESSION (different
     days). Report s60/s62 accuracies per cell and the extended (K + historical) per-item
     label distribution, and whether the cross-session spread exceeds the within-session one.

Frozen reporting map (Q3, descriptive — no result is retuned):
  TRIGGER-A-FIRES   : let-alone combined across-run RANGE > 0 AND comp-corr across-run RANGE
                      ~ 0 (<=0.034, i.e. <=1 item on n=30) AND let-alone churn > comp-corr
                      churn -> jitter concentrates at near-chance, negligible at ceiling.
  JITTER-FLAT       : let-alone range ~ comp-corr range (both small) -> the s62 ~12% was a
                      high draw; essay/point-estimate-is-a-draw SOFTENS (jitter smaller, and
                      not specially concentrated at near-chance). (trigger (a) does not fire.)
  JITTER-EVERYWHERE : comp-corr also jitters materially (range > 0.034) -> jitter is NOT
                      ceiling-protected; essay's "barely bites at ceilings" clause needs
                      revision. (Unexpected; would itself be the finding.)
  GUARD-FAIL        : any run with uptake NOT induced or control broken -> that run flagged;
                      jitter read restricted to clean runs (reported).

Internal-replication anchors: s60 raw at
  ../2026-06-20-scivetti-let-alone-forced-decomposition/raw/{A,B,C}-labels.json (24 LA test +
  30 CC) and s62 raw at ../2026-06-20-scivetti-let-alone-powered-rerun/raw/{A,B,C}-labels.json
  (all 63). Matched by item_id; NO text in any committed artifact.

Anchor: resource/scivetti-2025-cxnli-dataset (ratified 2026-05-29, Tom). comp-corr carries the
ratified anchor; let-alone is descriptive from the same human-annotated release. This run makes
NO new human-comparison claim beyond pinning the magnitude of an already-reported residual; its
force is a within-model MEASUREMENT of instrument jitter.

Usage: python3 analyze.py            # reads raw/run*-{A,B,C}-labels.json, writes results.json
       python3 analyze.py --selftest # synthetic checks, no raw needed
"""
import argparse
import itertools
import json
import math
import statistics
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "raw"
S60_RAW = HERE / ".." / "2026-06-20-scivetti-let-alone-forced-decomposition" / "raw"
S62_RAW = HERE / ".." / "2026-06-20-scivetti-let-alone-powered-rerun" / "raw"
PANEL_NAMES = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
TARGET = "let-alone"
CONTROL = "comparative-correlative"
HUMAN_BASELINE = 0.90
WORKED_THRESH = 0.80
CEILING_RANGE_EPS = 0.034  # <=1 item on n=30 (1/30 = 0.0333) counts as "~0 range"
K = 5


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0, 0.0)
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = (z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom
    return (max(0.0, centre - half), min(1.0, centre + half), p)


def correct(row):
    return row["value"] is not None and int(row["value"]) == row["gold"]


def acc_of(rows):
    n = len(rows)
    k = sum(1 for x in rows if correct(x))
    return k / n if n else None


def cell_rows(rows, cxn, split=None):
    out = [x for x in rows if x["cxn"] == cxn]
    if split is not None:
        out = [x for x in out if x.get("split", "test") == split]
    return out


def load_runs(slot):
    """Return {run_idx: [rows]} for every committed run file for this slot."""
    runs = {}
    for p in sorted(RAW.glob(f"run*-{slot}-labels.json")):
        idx = int(p.name.split("-")[0].replace("run", ""))
        runs[idx] = json.load(open(p))
    return runs


def load_hist(raw_dir, slot):
    p = raw_dir / f"{slot}-labels.json"
    return json.load(open(p)) if p.exists() else None


def spread(values):
    vals = [v for v in values if v is not None]
    if not vals:
        return {"n_runs": 0}
    return {"n_runs": len(vals), "per_run": vals, "mean": statistics.mean(vals),
            "min": min(vals), "max": max(vals), "range": max(vals) - min(vals),
            "sd": statistics.stdev(vals) if len(vals) > 1 else 0.0}


def item_stability(runs, cxn, split=None):
    """Per-item label distribution across the K runs. Returns per-item records + summary."""
    # index each run's cell rows by item_id
    by_run = {idx: {r["item_id"]: r for r in cell_rows(rows, cxn, split)}
              for idx, rows in runs.items()}
    item_ids = sorted({iid for d in by_run.values() for iid in d})
    items = []
    for iid in item_ids:
        labels = [by_run[idx][iid]["value"] for idx in sorted(by_run) if iid in by_run[idx]]
        gold = next(by_run[idx][iid]["gold"] for idx in sorted(by_run) if iid in by_run[idx])
        cnt = Counter(labels)  # includes None if any missing
        nonnull = [l for l in labels if l is not None]
        modal = Counter(nonnull).most_common(1)[0][0] if nonnull else None
        items.append({"item_id": iid, "gold": gold, "labels": labels,
                      "label_counts": dict(cnt),
                      "modal": modal,
                      "constant": len(set(labels)) == 1,
                      "modal_correct": modal is not None and int(modal) == gold})
    n = len(items)
    n_const = sum(1 for it in items if it["constant"])
    # mean pairwise label agreement across C(K,2) run-pairs, averaged over items
    pair_aggs = []
    run_idxs = sorted(by_run)
    for a, b in itertools.combinations(run_idxs, 2):
        shared = [iid for iid in item_ids if iid in by_run[a] and iid in by_run[b]]
        if shared:
            agree = sum(1 for iid in shared
                        if by_run[a][iid]["value"] == by_run[b][iid]["value"])
            pair_aggs.append(agree / len(shared))
    maj_correct = sum(1 for it in items if it["modal_correct"])
    lo, hi, p = wilson(maj_correct, n)
    return {
        "n_items": n,
        "n_constant": n_const,
        "churn_rate": (n - n_const) / n if n else None,
        "mean_pairwise_agreement": statistics.mean(pair_aggs) if pair_aggs else None,
        "n_pairs": len(pair_aggs),
        "majority_vote_correct": maj_correct,
        "majority_vote_acc": maj_correct / n if n else None,
        "majority_vote_wilson": [lo, hi],
        "items": items,
    }


CELLS = [("letalone_combined", TARGET, None),
         ("letalone_test", TARGET, "test"),
         ("letalone_train", TARGET, "train"),
         ("compcorr", CONTROL, None)]


def analyze():
    out = {"K": K, "human_baseline": HUMAN_BASELINE, "instrument": "forced-decomposition",
           "ceiling_range_eps": CEILING_RANGE_EPS, "per_model": {}}
    for slot, name in PANEL_NAMES.items():
        runs = load_runs(slot)
        n_runs = len(runs)
        s60 = load_hist(S60_RAW, slot)
        s62 = load_hist(S62_RAW, slot)
        model = {"name": name, "n_runs_committed": n_runs, "cells": {},
                 "guard": {}, "cross_session": {}}

        # Q5 guard: per run, uptake induced on let-alone + comp-corr at/near ceiling
        guard_rows = []
        for idx, rows in sorted(runs.items()):
            la = cell_rows(rows, TARGET)
            cc = cell_rows(rows, CONTROL)
            worked = sum(1 for x in la if x["uptake"]["worked"])
            worked_frac = worked / len(la) if la else 0.0
            cc_acc = acc_of(cc)
            cc_lo = wilson(sum(1 for x in cc if correct(x)), len(cc))[0]
            n_missing = sum(1 for x in rows if x["value"] is None)
            guard_rows.append({"run": idx, "worked_frac": worked_frac,
                               "uptake_induced": worked_frac >= WORKED_THRESH,
                               "cc_acc": cc_acc, "cc_wilson_lo": cc_lo,
                               "control_preserved": cc_lo >= 0.80,
                               "n_missing": n_missing})
        model["guard"]["per_run"] = guard_rows
        model["guard"]["all_clean"] = all(
            g["uptake_induced"] and g["control_preserved"] and g["n_missing"] == 0
            for g in guard_rows) if guard_rows else False

        for key, cxn, split in CELLS:
            per_run_acc = [acc_of(cell_rows(rows, cxn, split))
                           for _, rows in sorted(runs.items())]
            sp = spread(per_run_acc)
            stab = item_stability(runs, cxn, split)
            model["cells"][key] = {"spread": sp, "stability": stab}

        # Q6 cross-session: s60 (LA test + CC) and s62 (all 63) draws per cell
        def hist_acc(hist, cxn, split=None):
            if hist is None:
                return None
            rs = cell_rows(hist, cxn, split)
            return acc_of(rs) if rs else None
        model["cross_session"] = {
            "s60": {"letalone_test": hist_acc(s60, TARGET, "test"),
                    "compcorr": hist_acc(s60, CONTROL)},
            "s62": {"letalone_combined": hist_acc(s62, TARGET),
                    "letalone_test": hist_acc(s62, TARGET, "test"),
                    "letalone_train": hist_acc(s62, TARGET, "train"),
                    "compcorr": hist_acc(s62, CONTROL)},
        }
        # extended within+cross-session per-run accuracy band for LA combined and CC
        la_runs = [a for a in model["cells"]["letalone_combined"]["spread"].get("per_run", [])]
        la_ext = list(la_runs) + [v for v in [model["cross_session"]["s62"]["letalone_combined"]]
                                  if v is not None]
        cc_runs = [a for a in model["cells"]["compcorr"]["spread"].get("per_run", [])]
        cc_ext = list(cc_runs) + [v for v in [model["cross_session"]["s60"]["compcorr"],
                                              model["cross_session"]["s62"]["compcorr"]]
                                  if v is not None]
        model["cross_session"]["extended_band"] = {
            "letalone_combined": spread(la_ext), "compcorr": spread(cc_ext)}
        out["per_model"][slot] = model

    # Q3 trigger-(a) reading map (frozen)
    reads = {}
    for slot in PANEL_NAMES:
        la = out["per_model"][slot]["cells"]["letalone_combined"]["spread"]
        cc = out["per_model"][slot]["cells"]["compcorr"]["spread"]
        la_churn = out["per_model"][slot]["cells"]["letalone_combined"]["stability"]["churn_rate"]
        cc_churn = out["per_model"][slot]["cells"]["compcorr"]["stability"]["churn_rate"]
        clean = out["per_model"][slot]["guard"]["all_clean"]
        la_r = la.get("range")
        cc_r = cc.get("range")
        if not clean:
            verdict = "GUARD-FAIL"
        elif cc_r is not None and cc_r > CEILING_RANGE_EPS:
            verdict = "JITTER-EVERYWHERE"
        elif la_r is not None and la_r > 0 and cc_r is not None and cc_r <= CEILING_RANGE_EPS \
                and (la_churn or 0) > (cc_churn or 0):
            verdict = "TRIGGER-A-FIRES"
        else:
            verdict = "JITTER-FLAT"
        reads[slot] = {"name": PANEL_NAMES[slot], "verdict": verdict,
                       "letalone_range": la_r, "compcorr_range": cc_r,
                       "letalone_churn": la_churn, "compcorr_churn": cc_churn}
    out["trigger_a_read"] = reads
    return out


def selftest():
    # synthetic: 2 runs, 2 items; run1 labels [0,1], run2 labels [0,2]; gold [0,0]
    assert abs(wilson(1, 2)[2] - 0.5) < 1e-9
    runs = {1: [{"run": 1, "item_id": "x#1", "cxn": "let-alone", "split": "test",
                 "gold": 0, "value": "0", "uptake": {"worked": True}, "usage": {}},
                {"run": 1, "item_id": "x#2", "cxn": "let-alone", "split": "test",
                 "gold": 0, "value": "1", "uptake": {"worked": True}, "usage": {}}],
            2: [{"run": 2, "item_id": "x#1", "cxn": "let-alone", "split": "test",
                 "gold": 0, "value": "0", "uptake": {"worked": True}, "usage": {}},
                {"run": 2, "item_id": "x#2", "cxn": "let-alone", "split": "test",
                 "gold": 0, "value": "2", "uptake": {"worked": True}, "usage": {}}]}
    st = item_stability(runs, "let-alone", "test")
    assert st["n_items"] == 2
    assert st["n_constant"] == 1  # item x#1 constant (0,0), x#2 not (1,2)
    assert abs(st["churn_rate"] - 0.5) < 1e-9
    # modal of x#2 is min-most_common -> Counter([1,2]).most_common(1) deterministic by count
    # both appear once; most_common returns insertion order -> "1"; modal_correct False
    assert st["majority_vote_correct"] == 1  # x#1 modal 0 correct; x#2 modal not 0
    # pairwise agreement: x#1 agrees, x#2 disagrees -> 0.5
    assert abs(st["mean_pairwise_agreement"] - 0.5) < 1e-9
    sp = spread([0.5, 0.0, 1.0])
    assert sp["range"] == 1.0 and sp["min"] == 0.0 and sp["max"] == 1.0
    assert sp["n_runs"] == 3
    print("selftest PASS")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    res = analyze()
    json.dump(res, open(HERE / "results.json", "w"), indent=1)
    # human-readable summary
    print(f"K={res['K']} runs; instrument={res['instrument']}; baseline={res['human_baseline']}")
    for slot, m in res["per_model"].items():
        print(f"\n== {m['name']} ({slot}) — {m['n_runs_committed']} runs committed, "
              f"all_clean={m['guard']['all_clean']} ==")
        for key in ("letalone_combined", "compcorr"):
            sp = m["cells"][key]["spread"]
            stab = m["cells"][key]["stability"]
            print(f"  {key:18s} per-run acc {[round(a,3) for a in sp.get('per_run',[])]} "
                  f"range={sp.get('range'):.3f} sd={sp.get('sd'):.3f} "
                  f"churn={stab['churn_rate']:.3f} mvote={stab['majority_vote_acc']:.3f} "
                  f"pairAgree={stab['mean_pairwise_agreement']:.3f}")
        r = res["trigger_a_read"][slot]
        print(f"  trigger-(a) read: {r['verdict']} "
              f"(LA range {r['letalone_range']:.3f} churn {r['letalone_churn']:.3f} | "
              f"CC range {r['compcorr_range']:.3f} churn {r['compcorr_churn']:.3f})")
    print("\nwrote results.json")


if __name__ == "__main__":
    main()
