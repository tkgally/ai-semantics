#!/usr/bin/env python3
"""analyze.py — frozen analysis for the Scivetti CxNLI answer-key probe (NO API calls).

Scores panel NLI labels against the per-item gold labels:
  * overall accuracy + Wilson 95% CI per model, vs the human native-speaker baseline
    0.90 (Exp 1) -> per-model verdict {ABOVE / MATCHES / BELOW the human baseline};
  * per-construction accuracy + Wilson CI + n (all 8; the 4 ratified-anchor ones flagged);
  * 3x3 gold-vs-pred confusion; unparseable/missing count (never dropped silently);
  * DESCRIPTIVE add-vs-cancel contrast (caused-motion+way-manner vs conative) for
    conjecture/constructional-monotonicity-asymmetry — reported with the explicit
    caveat that this is baseline-difficulty-CONFOUNDED, NOT the matched-difficulty
    confirm test the conjecture requires.

Human anchor: resource/scivetti-2025-cxnli-dataset (ratified 2026-05-29, Tom).

Usage: python3 analyze.py            # reads raw/{A,B,C}-nli.json, writes results.json
       python3 analyze.py --selftest # synthetic checks, no raw needed
"""
import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "raw"
PANEL_NAMES = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
RATIFIED = {"caused-motion", "conative", "way-manner", "comparative-correlative"}
ADD = {"caused-motion", "way-manner"}
CANCEL = {"conative"}
HUMAN_BASELINE = 0.90  # native-speaker accuracy, Exp 1 (Scivetti et al. 2025)


def wilson(k, n, z=1.96):
    """Wilson score 95% CI for a binomial proportion. Returns (lo, hi, point)."""
    if n == 0:
        return (0.0, 1.0, 0.0)
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = (z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom
    return (max(0.0, centre - half), min(1.0, centre + half), p)


def baseline_verdict(lo, hi):
    """Where does the human 0.90 baseline sit relative to the model's 95% CI?"""
    if lo > HUMAN_BASELINE:
        return "ABOVE-HUMAN-BASELINE"
    if hi < HUMAN_BASELINE:
        return "BELOW-HUMAN-BASELINE"
    return "MATCHES-HUMAN-BASELINE"


def score_model(rows):
    """rows: list of {cxn, gold, value}. value may be None (unparseable). A None is
    scored as WRONG for accuracy (and counted separately as unparseable)."""
    n = len(rows)
    unparseable = sum(1 for r in rows if r["value"] is None)
    correct = sum(1 for r in rows if r["value"] is not None and int(r["value"]) == int(r["gold"]))
    lo, hi, p = wilson(correct, n)
    per_cxn = {}
    by_cxn = defaultdict(list)
    for r in rows:
        by_cxn[r["cxn"]].append(r)
    for cxn, rs in sorted(by_cxn.items()):
        k = sum(1 for r in rs if r["value"] is not None and int(r["value"]) == int(r["gold"]))
        clo, chi, cp = wilson(k, len(rs))
        per_cxn[cxn] = {"n": len(rs), "correct": k, "acc": round(cp, 4),
                        "wilson_lo": round(clo, 4), "wilson_hi": round(chi, 4),
                        "ratified_anchor": cxn in RATIFIED}
    # 3x3 confusion (gold rows, pred cols); None preds bucketed as "NA".
    conf = Counter()
    for r in rows:
        pred = "NA" if r["value"] is None else str(int(r["value"]))
        conf[(str(int(r["gold"])), pred)] += 1
    confusion = {f"gold{g}_pred{p2}": conf[(g, p2)]
                 for g in "012" for p2 in ["0", "1", "2", "NA"]}
    # add vs cancel (descriptive; confounded)
    def acc_over(cxset):
        rs = [r for r in rows if r["cxn"] in cxset]
        k = sum(1 for r in rs if r["value"] is not None and int(r["value"]) == int(r["gold"]))
        l2, h2, p2 = wilson(k, len(rs))
        return {"n": len(rs), "correct": k, "acc": round(p2, 4),
                "wilson_lo": round(l2, 4), "wilson_hi": round(h2, 4)}
    add = acc_over(ADD)
    cancel = acc_over(CANCEL)
    # macro across the four ratified constructions
    rat_accs = [per_cxn[c]["acc"] for c in RATIFIED if c in per_cxn]
    return {
        "n": n, "correct": correct, "unparseable": unparseable,
        "overall_acc": round(p, 4), "wilson_lo": round(lo, 4), "wilson_hi": round(hi, 4),
        "baseline_verdict": baseline_verdict(lo, hi),
        "macro_acc_ratified4": round(sum(rat_accs) / len(rat_accs), 4) if rat_accs else None,
        "per_construction": per_cxn,
        "confusion": confusion,
        "add_caused-motion+way-manner": add,
        "cancel_conative": cancel,
        "add_minus_cancel_acc": round(add["acc"] - cancel["acc"], 4),
    }


def analyze():
    out = {"human_baseline_exp1": HUMAN_BASELINE,
           "anchor": "resource/scivetti-2025-cxnli-dataset (ratified 2026-05-29, Tom)",
           "models": {}}
    for slot, name in PANEL_NAMES.items():
        f = RAW / f"{slot}-nli.json"
        if not f.exists():
            print(f"  (missing {f.name}; skipping {name})")
            continue
        rows = json.load(open(f))
        out["models"][name] = score_model(rows)
    json.dump(out, open(HERE / "results.json", "w"), indent=2)
    print(f"wrote results.json ({len(out['models'])} models)")
    for name, m in out["models"].items():
        print(f"\n{name}: overall {m['overall_acc']:.3f} "
              f"[{m['wilson_lo']:.3f},{m['wilson_hi']:.3f}] vs human {HUMAN_BASELINE} "
              f"-> {m['baseline_verdict']}  (unparseable {m['unparseable']})")
        print(f"   ratified-4 macro {m['macro_acc_ratified4']}; "
              f"ADD {m['add_caused-motion+way-manner']['acc']:.3f} vs "
              f"CANCEL {m['cancel_conative']['acc']:.3f} "
              f"(gap {m['add_minus_cancel_acc']:+.3f}, CONFOUNDED)")
        for cxn, c in m["per_construction"].items():
            tag = " *anchor" if c["ratified_anchor"] else ""
            print(f"     {cxn:24s} n={c['n']:3d} acc={c['acc']:.3f} "
                  f"[{c['wilson_lo']:.3f},{c['wilson_hi']:.3f}]{tag}")
    return out


def selftest():
    # Build synthetic rows: 36 caused-motion all-correct, 78 conative half-correct,
    # 33 way-manner all-correct, 30 comparative-correlative all-wrong, plus filler.
    rows = []
    def add_rows(cxn, n, correct_frac, gold=0):
        for i in range(n):
            ok = i < round(n * correct_frac)
            rows.append({"cxn": cxn, "gold": gold, "value": gold if ok else (gold + 1) % 3})
    add_rows("caused-motion", 36, 1.0)
    add_rows("way-manner", 33, 1.0)
    add_rows("conative", 78, 0.5)
    add_rows("comparative-correlative", 30, 0.0)
    rows.append({"cxn": "let-alone", "gold": 1, "value": None})  # one unparseable
    m = score_model(rows)
    assert m["per_construction"]["caused-motion"]["acc"] == 1.0
    assert m["per_construction"]["comparative-correlative"]["acc"] == 0.0
    assert m["unparseable"] == 1
    # add = (36+33)/(36+33) = 1.0; cancel = 39/78 = 0.5; gap = +0.5
    assert m["add_caused-motion+way-manner"]["acc"] == 1.0
    assert abs(m["cancel_conative"]["acc"] - 0.5) < 1e-9
    assert abs(m["add_minus_cancel_acc"] - 0.5) < 1e-9
    # wilson sanity: 0/30 -> lo 0, point 0; 36/36 -> hi 1
    lo, hi, p = wilson(36, 36)
    assert p == 1.0 and hi == 1.0 and lo < 1.0
    lo, hi, p = wilson(45, 90)
    assert abs(p - 0.5) < 1e-9 and lo < 0.5 < hi
    # baseline verdict logic
    assert baseline_verdict(0.91, 0.95) == "ABOVE-HUMAN-BASELINE"
    assert baseline_verdict(0.50, 0.70) == "BELOW-HUMAN-BASELINE"
    assert baseline_verdict(0.85, 0.95) == "MATCHES-HUMAN-BASELINE"
    # confusion totals == n
    assert sum(m["confusion"].values()) == len(rows)
    print("selftest PASS")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
    else:
        analyze()


if __name__ == "__main__":
    main()
