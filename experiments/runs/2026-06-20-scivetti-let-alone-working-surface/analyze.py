#!/usr/bin/env python3
"""analyze.py — frozen analysis for the let-alone working-surface format probe (NO API).

Two questions, pre-registered (PREREG.md):

  Q1 (anchored leg). Under the working surface, what is each model's per-construction
      accuracy vs the per-item gold and the human ~0.90 native-speaker baseline?
      comparative-correlative carries the RATIFIED Scivetti anchor (ceiling control);
      let-alone is DESCRIPTIVE from the same human-annotated release (not individually
      anchored), exactly as in session 57.

  Q2 (the headline format contrast; internal-contrast-only). Does the working surface
      CHANGE the label on the SAME items vs the session-57 forced single-token format?
      Within-item paired comparison: for each model and construction, count
        b = forced-WRONG -> working-surface-RIGHT (gains)
        c = forced-RIGHT -> working-surface-WRONG (losses)
      and a one-sided exact binomial (sign) test on the b+c discordant pairs.
      Pre-registered per-(model,construction) verdict:
        LIFTS     : ws_acc > forced_acc AND P(X>=b | n=b+c, 0.5) < 0.05
        DROPS     : ws_acc < forced_acc AND P(X>=c | n=b+c, 0.5) < 0.05
        UNCHANGED : otherwise.
      Control guard (comp-correlative): PRESERVED if its ws_acc Wilson CI contains the
      forced-format acc (the working surface did not break the instrument), else FLAG.

Paired baseline: ../2026-06-20-scivetti-cxnli-answer-key/raw/{A,B,C}-nli.json
  (committed; item_id + cxn + gold + value, NO text). Matched by item_id.

Anchor: resource/scivetti-2025-cxnli-dataset (ratified 2026-05-29, Tom).

Usage: python3 analyze.py            # reads raw/{A,B,C}-labels.json, writes results.json
       python3 analyze.py --selftest # synthetic checks, no raw needed
"""
import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "raw"
BASELINE_RAW = HERE / ".." / "2026-06-20-scivetti-cxnli-answer-key" / "raw"
PANEL_NAMES = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
TARGET = "let-alone"
CONTROL = "comparative-correlative"
RATIFIED = {CONTROL}
HUMAN_BASELINE = 0.90


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 1.0, 0.0)
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = (z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / denom
    return (max(0.0, centre - half), min(1.0, centre + half), p)


def baseline_verdict(lo, hi):
    if lo > HUMAN_BASELINE:
        return "ABOVE-HUMAN-BASELINE"
    if hi < HUMAN_BASELINE:
        return "BELOW-HUMAN-BASELINE"
    return "MATCHES-HUMAN-BASELINE"


def binom_tail_ge(b, n, p=0.5):
    """One-sided exact: P(X >= b) for X ~ Binomial(n, p)."""
    if n == 0:
        return 1.0
    return sum(math.comb(n, k) * p**k * (1 - p)**(n - k) for k in range(b, n + 1))


def correct(row):
    return row["value"] is not None and int(row["value"]) == int(row["gold"])


def per_cxn_acc(rows, cxn):
    rs = [r for r in rows if r["cxn"] == cxn]
    k = sum(1 for r in rs if correct(r))
    lo, hi, p = wilson(k, len(rs))
    return {"n": len(rs), "correct": k, "acc": round(p, 4),
            "wilson_lo": round(lo, 4), "wilson_hi": round(hi, 4)}


def paired(ws_rows, base_rows, cxn):
    """Within-item paired comparison on construction `cxn`. Match by item_id."""
    base = {r["item_id"]: r for r in base_rows if r["cxn"] == cxn}
    ws = {r["item_id"]: r for r in ws_rows if r["cxn"] == cxn}
    ids = sorted(set(base) & set(ws))
    a = b = c = d = 0  # both-right / forced-wrong->ws-right / forced-right->ws-wrong / both-wrong
    for i in ids:
        bc = correct(base[i])
        wc = correct(ws[i])
        if bc and wc:
            a += 1
        elif (not bc) and wc:
            b += 1
        elif bc and (not wc):
            c += 1
        else:
            d += 1
    n_disc = b + c
    ws_acc = (a + b) / len(ids) if ids else 0.0
    forced_acc = (a + c) / len(ids) if ids else 0.0
    p_lift = binom_tail_ge(b, n_disc)   # gains exceed losses?
    p_drop = binom_tail_ge(c, n_disc)   # losses exceed gains?
    if ws_acc > forced_acc and p_lift < 0.05:
        verdict = "LIFTS"
    elif ws_acc < forced_acc and p_drop < 0.05:
        verdict = "DROPS"
    else:
        verdict = "UNCHANGED"
    return {"n_paired": len(ids), "both_right": a, "gains_wrong_to_right": b,
            "losses_right_to_wrong": c, "both_wrong": d,
            "forced_acc": round(forced_acc, 4), "ws_acc": round(ws_acc, 4),
            "acc_delta": round(ws_acc - forced_acc, 4),
            "p_lift_one_sided": round(p_lift, 5), "p_drop_one_sided": round(p_drop, 5),
            "verdict": verdict}


def control_guard(ws_cc, base_rows):
    """comp-correlative: did the working surface break the instrument? PRESERVED if the
    ws Wilson CI contains the forced-format acc."""
    base_cc = [r for r in base_rows if r["cxn"] == CONTROL]
    fk = sum(1 for r in base_cc if correct(r))
    forced_acc = fk / len(base_cc) if base_cc else 0.0
    contains = ws_cc["wilson_lo"] <= forced_acc <= ws_cc["wilson_hi"]
    return {"forced_acc": round(forced_acc, 4), "ws_acc": ws_cc["acc"],
            "ws_ci": [ws_cc["wilson_lo"], ws_cc["wilson_hi"]],
            "status": "PRESERVED" if contains else "FLAG-degraded-or-changed"}


def analyze():
    out = {"human_baseline_exp1": HUMAN_BASELINE,
           "anchor": "resource/scivetti-2025-cxnli-dataset (ratified 2026-05-29, Tom)",
           "design": "format-only (forced single token -> working surface); items byte-identical to session 57",
           "models": {}}
    for slot, name in PANEL_NAMES.items():
        f = RAW / f"{slot}-labels.json"
        bf = BASELINE_RAW / f"{slot}-nli.json"
        if not f.exists():
            print(f"  (missing {f.name}; skipping {name})")
            continue
        ws_rows = json.load(open(f))
        base_rows = json.load(open(bf)) if bf.exists() else []
        unparseable = sum(1 for r in ws_rows if r["value"] is None)
        modes = dict(Counter(r["parse_mode"] for r in ws_rows))
        m = {"unparseable": unparseable, "parse_modes": modes,
             "per_construction_ws": {}, "paired": {}}
        for cxn in (TARGET, CONTROL):
            cc = per_cxn_acc(ws_rows, cxn)
            cc["baseline_verdict"] = baseline_verdict(cc["wilson_lo"], cc["wilson_hi"])
            cc["ratified_anchor"] = cxn in RATIFIED
            m["per_construction_ws"][cxn] = cc
            if base_rows:
                m["paired"][cxn] = paired(ws_rows, base_rows, cxn)
        if base_rows:
            m["control_guard_comp_correlative"] = control_guard(
                m["per_construction_ws"][CONTROL], base_rows)
        out["models"][name] = m
    # cross-model summary on the TARGET
    out["target_summary"] = {
        "construction": TARGET,
        "per_model_verdict": {name: m["paired"].get(TARGET, {}).get("verdict")
                              for name, m in out["models"].items() if m.get("paired")},
    }
    json.dump(out, open(HERE / "results.json", "w"), indent=2)
    print(f"wrote results.json ({len(out['models'])} models)")
    for name, m in out["models"].items():
        print(f"\n{name}: unparseable {m['unparseable']}, parse_modes {m['parse_modes']}")
        for cxn in (TARGET, CONTROL):
            c = m["per_construction_ws"][cxn]
            tag = " *anchor" if c["ratified_anchor"] else " (descriptive)"
            print(f"  {cxn:24s} ws_acc={c['acc']:.3f} "
                  f"[{c['wilson_lo']:.3f},{c['wilson_hi']:.3f}] "
                  f"vs human {HUMAN_BASELINE}->{c['baseline_verdict']}{tag}")
            if cxn in m["paired"]:
                pr = m["paired"][cxn]
                print(f"     PAIRED forced {pr['forced_acc']:.3f} -> ws {pr['ws_acc']:.3f} "
                      f"(Δ{pr['acc_delta']:+.3f}); gains {pr['gains_wrong_to_right']} "
                      f"losses {pr['losses_right_to_wrong']} "
                      f"p_lift={pr['p_lift_one_sided']:.4f} => {pr['verdict']}")
        if "control_guard_comp_correlative" in m:
            print(f"     CONTROL GUARD: {m['control_guard_comp_correlative']['status']}")
    print(f"\nTARGET ({TARGET}) per-model verdict: {out['target_summary']['per_model_verdict']}")
    return out


def selftest():
    # binom tail
    assert abs(binom_tail_ge(0, 0) - 1.0) < 1e-12
    assert abs(binom_tail_ge(5, 5) - 0.5**5) < 1e-12
    assert abs(binom_tail_ge(0, 4) - 1.0) < 1e-12
    # wilson sanity
    lo, hi, p = wilson(24, 24)
    assert p == 1.0 and hi == 1.0 and lo < 1.0
    # paired: all forced-wrong -> ws-right is a clean LIFT
    base = [{"item_id": f"let-alone#{i}", "cxn": "let-alone", "gold": 0,
             "value": 1} for i in range(8)]  # all wrong
    ws = [{"item_id": f"let-alone#{i}", "cxn": "let-alone", "gold": 0,
           "value": 0, "parse_mode": "tagged"} for i in range(8)]  # all right
    pr = paired(ws, base, "let-alone")
    assert pr["gains_wrong_to_right"] == 8 and pr["losses_right_to_wrong"] == 0
    assert pr["verdict"] == "LIFTS", pr
    assert pr["p_lift_one_sided"] < 0.05
    # paired: no change -> UNCHANGED
    ws2 = [{"item_id": f"let-alone#{i}", "cxn": "let-alone", "gold": 0,
            "value": 1, "parse_mode": "tagged"} for i in range(8)]
    pr2 = paired(ws2, base, "let-alone")
    assert pr2["verdict"] == "UNCHANGED" and pr2["gains_wrong_to_right"] == 0
    # control guard: ws CI contains forced acc -> PRESERVED
    base_cc = [{"item_id": f"comparative-correlative#{i}", "cxn": CONTROL, "gold": 0,
                "value": 0} for i in range(30)]  # forced acc 1.0
    ws_cc = per_cxn_acc([{"item_id": f"comparative-correlative#{i}", "cxn": CONTROL,
                          "gold": 0, "value": 0} for i in range(30)], CONTROL)  # ws 1.0
    cg = control_guard(ws_cc, base_cc)
    assert cg["status"] == "PRESERVED", cg
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
