#!/usr/bin/env python3
"""analyze.py — frozen analysis for the POWERED let-alone forced-decomposition re-run
(NO API). Trigger-(g) power-resolution of session 60's partial witness.

Pre-registered questions (PREREG.md):

  Q1 (the headline — vs-baseline residual, anchored/descriptive leg). Under forced
     decomposition, what is each model's let-alone accuracy on the POWERED combined set
     (33 = 24 test + 9 train) and its Wilson 95% CI vs the ≈0.90 human native-speaker
     baseline? comparative-correlative carries the RATIFIED Scivetti anchor; let-alone is
     DESCRIPTIVE from the same human-annotated release (not individually anchored), exactly
     as sessions 57/58/60. The trigger-(g) reading focuses on gpt-5.4-mini: does the
     session-60 below-baseline residual (24-item CI hi 0.755 < 0.90) HOLD at higher power?

  Q1b (internal replication + generalization; internal contrast). Per-split accuracy:
     let-alone TEST (n=24) vs let-alone TRAIN (n=9, disjoint). Does the 24-item test
     accuracy REPRODUCE session 60 (item-by-item agreement reported)? Do the 9 fresh
     disjoint items AGREE in direction (below baseline for gpt)?

  Q2 (ceiling control guard; internal). comp-correlative (n=30) accuracy + Wilson CI.
     PRESERVED iff at/near ceiling (Wilson LB high) — guards "the scaffold broke the
     instrument."

  Q3 (uptake manipulation check — what makes the residual readable as channel-controlled).
     Per model on let-alone: fraction "worked" (>=40 pre-FINAL chars and >=2 numbered step
     markers) and the gpt completion-token distribution. The clean reading requires uptake
     to be INDUCED (as in session 60: gpt 24/24 worked, median 120 tokens). If uptake is
     NOT induced, the run is a method-null on the channel question.

Pre-registered verdict map (frozen) for gpt-5.4-mini let-alone (combined n=33):

  CONFIRMS-RESIDUAL : uptake induced (>=80% worked) AND control PRESERVED AND combined
                      Wilson CI hi < 0.90  -> the below-baseline channel-controlled residual
                      HOLDS at higher power (a cleaner essay/output-channel-confound
                      trigger-(b) case; descriptive + contamination-caveated, NOT "cannot").
  DISSOLVES         : uptake induced AND control PRESERVED AND combined Wilson CI COVERS
                      0.90 -> the residual was a small-N artifact (leans output-channel-
                      artifact, like claude/gemini).
  STAYS-PARTIAL     : uptake induced AND control PRESERVED AND combined point estimate
                      below 0.90 but CI hi >= 0.90 with point < 0.90 already covered by
                      DISSOLVES -> reserved for the genuinely ambiguous case (point near
                      0.90 / CI straddles): power bound sharpened, 33 = the max available
                      human-anchored let-alone N, redirect axis.
  METHOD-NULL       : uptake NOT induced (<80% worked) OR control BROKEN -> channel
                      question not cleanly posed this run.

claude/gemini are the manipulation check: each EXPECTED at/covering baseline (a benign,
non-degrading scaffold), control PRESERVED.

Internal-replication baseline (Q1b): the session-60 24-item forced-decomposition labels at
../2026-06-20-scivetti-let-alone-forced-decomposition/raw/{A,B,C}-labels.json. Matched by
item_id; NO text in any committed artifact.

Anchor: resource/scivetti-2025-cxnli-dataset (ratified 2026-05-29, Tom).

Usage: python3 analyze.py            # reads raw/{A,B,C}-labels.json, writes results.json
       python3 analyze.py --selftest # synthetic checks, no raw needed
"""
import argparse
import json
import math
import statistics
from collections import Counter
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "raw"
S60_RAW = HERE / ".." / "2026-06-20-scivetti-let-alone-forced-decomposition" / "raw"
PANEL_NAMES = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
TARGET = "let-alone"
CONTROL = "comparative-correlative"
RATIFIED = {CONTROL}
HUMAN_BASELINE = 0.90
WORKED_THRESH = 0.80  # >=80% of let-alone items "worked" => uptake induced


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0, 0.0)
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = (z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom
    return (max(0.0, centre - half), min(1.0, centre + half), p)


def acc(rows):
    n = len(rows)
    k = sum(1 for x in rows if x["value"] is not None and int(x["value"]) == x["gold"])
    lo, hi, p = wilson(k, n)
    return {"n": n, "correct": k, "acc": (k / n if n else None),
            "wilson_lo": lo, "wilson_hi": hi}


def load(slot):
    return json.load(open(RAW / f"{slot}-labels.json"))


def load_s60(slot):
    p = S60_RAW / f"{slot}-labels.json"
    return json.load(open(p)) if p.exists() else None


def median_completion(rows):
    toks = [(x.get("usage") or {}).get("completion_tokens") for x in rows]
    toks = [t for t in toks if t is not None]
    return statistics.median(toks) if toks else None


def analyze():
    out = {"human_baseline": HUMAN_BASELINE, "instrument": "forced-decomposition",
           "letalone_combined_n": None, "per_model": {}}
    for slot, name in PANEL_NAMES.items():
        rows = load(slot)
        la = [x for x in rows if x["cxn"] == TARGET]
        la_test = [x for x in la if x["split"] == "test"]
        la_train = [x for x in la if x["split"] == "train"]
        cc = [x for x in rows if x["cxn"] == CONTROL]
        out["letalone_combined_n"] = len(la)

        # uptake (Q3)
        worked = sum(1 for x in la if x["uptake"]["worked"])
        worked_frac = worked / len(la) if la else 0.0
        uptake_induced = worked_frac >= WORKED_THRESH

        # control guard (Q2): PRESERVED iff Wilson LB >= 0.80 (near ceiling)
        cc_stat = acc(cc)
        control_preserved = cc_stat["wilson_lo"] >= 0.80

        # combined vs-baseline (Q1)
        comb = acc(la)
        ci_hi_below = comb["wilson_hi"] < HUMAN_BASELINE
        ci_covers = comb["wilson_lo"] <= HUMAN_BASELINE <= comb["wilson_hi"]

        # per-split (Q1b)
        test_stat = acc(la_test)
        train_stat = acc(la_train)

        # internal replication vs session 60 (24 test items)
        rep = None
        s60 = load_s60(slot)
        if s60:
            s60_la = {x["item_id"]: x for x in s60 if x["cxn"] == TARGET}
            this_la = {x["item_id"]: x for x in la_test}
            shared = sorted(set(s60_la) & set(this_la))
            agree = sum(1 for k in shared
                        if s60_la[k]["value"] == this_la[k]["value"])
            s60_correct = sum(1 for k in shared
                              if s60_la[k]["value"] is not None
                              and int(s60_la[k]["value"]) == s60_la[k]["gold"])
            rep = {"n_shared": len(shared),
                   "label_agreement": agree / len(shared) if shared else None,
                   "s60_test_acc": s60_correct / len(shared) if shared else None,
                   "this_test_acc": test_stat["acc"]}

        # verdict (gpt is the trigger-(g) subject; others are the manipulation check)
        if not uptake_induced or not control_preserved:
            verdict = "METHOD-NULL"
        elif ci_hi_below:
            verdict = "CONFIRMS-RESIDUAL"
        elif ci_covers and comb["acc"] >= HUMAN_BASELINE - 1e-9:
            verdict = "DISSOLVES"
        elif ci_covers:
            verdict = "STAYS-PARTIAL"
        else:
            verdict = "STAYS-PARTIAL"

        out["per_model"][name] = {
            "letalone_combined": comb,
            "letalone_test": test_stat,
            "letalone_train": train_stat,
            "control_cc": cc_stat,
            "control_preserved": control_preserved,
            "uptake_worked": worked, "uptake_worked_frac": round(worked_frac, 4),
            "uptake_induced": uptake_induced,
            "gpt_or_other_completion_median": median_completion(la),
            "vs_baseline": {"ci_hi_below_090": ci_hi_below, "ci_covers_090": ci_covers},
            "internal_replication_vs_s60": rep,
            "verdict": verdict,
            "parse_modes": dict(Counter(x["parse_mode"] for x in rows)),
            "n_missing": sum(1 for x in rows if x["value"] is None),
        }
    return out


def selftest():
    # wilson sanity
    lo, hi, p = wilson(19, 33)
    assert abs(p - 19 / 33) < 1e-9
    assert lo < p < hi
    # a 19/33 (~0.576) accuracy: hi should be < 0.90 (residual confirmed shape)
    assert hi < 0.90, f"expected 19/33 CI hi < 0.90, got {hi}"
    # a 30/33 (~0.909) accuracy: CI should cover 0.90
    lo2, hi2, p2 = wilson(30, 33)
    assert lo2 <= 0.90 <= hi2, "30/33 should cover 0.90"
    # acc() basic
    rows = [{"value": "0", "gold": 0}, {"value": "1", "gold": 0}, {"value": None, "gold": 2}]
    s = acc(rows)
    assert s["correct"] == 1 and s["n"] == 3
    print("selftest PASS")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    out = analyze()
    json.dump(out, open(HERE / "results.json", "w"), indent=2)
    print(f"let-alone combined n = {out['letalone_combined_n']}  (vs human {HUMAN_BASELINE})")
    for name, m in out["per_model"].items():
        c = m["letalone_combined"]
        print(f"\n{name}:")
        print(f"  let-alone COMBINED  {c['correct']}/{c['n']} = {c['acc']:.3f} "
              f"[{c['wilson_lo']:.3f}, {c['wilson_hi']:.3f}]  "
              f"(test {m['letalone_test']['acc']:.3f} / train {m['letalone_train']['acc']:.3f})")
        print(f"  control cc {m['control_cc']['acc']:.3f} "
              f"[{m['control_cc']['wilson_lo']:.3f}, {m['control_cc']['wilson_hi']:.3f}] "
              f"-> {'PRESERVED' if m['control_preserved'] else 'BROKEN'}")
        print(f"  uptake worked {m['uptake_worked']}/{c['n']} "
              f"({m['uptake_worked_frac']:.2f}) induced={m['uptake_induced']} "
              f"median-completion-tokens={m['gpt_or_other_completion_median']}")
        if m["internal_replication_vs_s60"]:
            r = m["internal_replication_vs_s60"]
            print(f"  vs s60 (24 test): label-agreement {r['label_agreement']:.3f} "
                  f"(s60 acc {r['s60_test_acc']:.3f} -> this {r['this_test_acc']:.3f})")
        print(f"  VERDICT: {m['verdict']}")


if __name__ == "__main__":
    main()
