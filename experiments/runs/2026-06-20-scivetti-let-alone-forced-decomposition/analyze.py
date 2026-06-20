#!/usr/bin/env python3
"""analyze.py — frozen analysis for the let-alone FORCED-DECOMPOSITION probe (NO API).

Three questions, pre-registered (PREREG.md):

  Q1 (anchored leg). Under forced decomposition, what is each model's per-construction
      accuracy vs the per-item gold and the human ~0.90 native-speaker baseline?
      comparative-correlative carries the RATIFIED Scivetti anchor (ceiling control);
      let-alone is DESCRIPTIVE from the same human-annotated release (not individually
      anchored), exactly as sessions 57/58.

  Q2 (the headline uptake contrast; internal-contrast-only). Does FORCING the working
      steps CHANGE the label on the SAME items vs the session-58 OFFERED working surface
      (which gpt largely declined)? Within-item paired comparison vs session 58:
        b = offered-WRONG -> forced-decomp-RIGHT (gains)
        c = offered-RIGHT -> forced-decomp-WRONG (losses)
      one-sided exact binomial (sign) test on the b+c discordant pairs. Pre-registered
      per-(model,construction) verdict:
        LIFTS     : fd_acc > offered_acc AND P(X>=b | n=b+c, 0.5) < 0.05
        DROPS     : fd_acc < offered_acc AND P(X>=c | n=b+c, 0.5) < 0.05
        UNCHANGED : otherwise.

  Q3 (the UPTAKE MANIPULATION CHECK — what makes the (b) test clean). Did forced
      decomposition actually INDUCE uptake? Per model on let-alone: fraction "worked"
      (>=40 pre-FINAL chars and >=2 numbered step markers) and the completion-token
      distribution, reported alongside session 58's offered-surface uptake. The clean
      trigger-(b) reading for gpt requires uptake to have RISEN (session 58: 16/24 bare,
      median 8 completion tokens). If gpt now works AND still fails -> a serial negative
      surviving a genuinely-exercised wide channel (essay/output-channel-confound trigger
      (b) FIRES). If gpt works AND lifts -> the let-alone failure was channel non-uptake
      for gpt too (an output-channel artifact, like claude/gemini).

Paired baseline (Q2): ../2026-06-20-scivetti-let-alone-working-surface/raw/{A,B,C}-labels.json
  (session 58 OFFERED working surface). Forced baseline (descriptive, Q1 context):
  ../2026-06-20-scivetti-cxnli-answer-key/raw/{A,B,C}-nli.json (session 57). Matched by
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
OFFERED_RAW = HERE / ".." / "2026-06-20-scivetti-let-alone-working-surface" / "raw"
FORCED_RAW = HERE / ".." / "2026-06-20-scivetti-cxnli-answer-key" / "raw"
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


def paired(fd_rows, base_rows, cxn):
    """Within-item paired comparison on construction `cxn` vs a baseline. Match by id.
    b = base-WRONG -> fd-RIGHT (gains); c = base-RIGHT -> fd-WRONG (losses)."""
    base = {r["item_id"]: r for r in base_rows if r["cxn"] == cxn}
    fd = {r["item_id"]: r for r in fd_rows if r["cxn"] == cxn}
    ids = sorted(set(base) & set(fd))
    a = b = c = d = 0
    for i in ids:
        bc = correct(base[i])
        fc = correct(fd[i])
        if bc and fc:
            a += 1
        elif (not bc) and fc:
            b += 1
        elif bc and (not fc):
            c += 1
        else:
            d += 1
    n_disc = b + c
    fd_acc = (a + b) / len(ids) if ids else 0.0
    base_acc = (a + c) / len(ids) if ids else 0.0
    p_lift = binom_tail_ge(b, n_disc)
    p_drop = binom_tail_ge(c, n_disc)
    if fd_acc > base_acc and p_lift < 0.05:
        verdict = "LIFTS"
    elif fd_acc < base_acc and p_drop < 0.05:
        verdict = "DROPS"
    else:
        verdict = "UNCHANGED"
    return {"n_paired": len(ids), "both_right": a, "gains_wrong_to_right": b,
            "losses_right_to_wrong": c, "both_wrong": d,
            "base_acc": round(base_acc, 4), "fd_acc": round(fd_acc, 4),
            "acc_delta": round(fd_acc - base_acc, 4),
            "p_lift_one_sided": round(p_lift, 5), "p_drop_one_sided": round(p_drop, 5),
            "verdict": verdict}


def control_guard(fd_cc, base_rows):
    base_cc = [r for r in base_rows if r["cxn"] == CONTROL]
    fk = sum(1 for r in base_cc if correct(r))
    base_acc = fk / len(base_cc) if base_cc else 0.0
    contains = fd_cc["wilson_lo"] <= base_acc <= fd_cc["wilson_hi"]
    return {"base_acc": round(base_acc, 4), "fd_acc": fd_cc["acc"],
            "fd_ci": [fd_cc["wilson_lo"], fd_cc["wilson_hi"]],
            "status": "PRESERVED" if contains else "FLAG-degraded-or-changed"}


def completion_tokens(rows, cxn):
    cts = []
    for r in rows:
        if r["cxn"] != cxn:
            continue
        u = r.get("usage") or {}
        ct = u.get("completion_tokens")
        if ct is not None:
            cts.append(ct)
    if not cts:
        return None
    return {"n": len(cts), "min": min(cts), "median": statistics.median(cts),
            "max": max(cts)}


def uptake_summary(fd_rows, offered_rows, cxn):
    """Q3 manipulation check on the TARGET: did forcing decomposition induce uptake?
    'worked' for THIS run comes from the committed `uptake` field; for session 58
    (offered, no uptake field) we proxy with completion_tokens >= 30 (its bare answers
    were ~8 tokens, its worked answers 200+)."""
    fd = [r for r in fd_rows if r["cxn"] == cxn]
    fd_worked = sum(1 for r in fd if r.get("uptake", {}).get("worked"))
    off = [r for r in offered_rows if r["cxn"] == cxn]
    off_worked = 0
    for r in off:
        ct = (r.get("usage") or {}).get("completion_tokens")
        if ct is not None and ct >= 30:
            off_worked += 1
    return {"n": len(fd),
            "forced_decomp_worked": fd_worked,
            "forced_decomp_worked_frac": round(fd_worked / len(fd), 4) if fd else None,
            "forced_decomp_completion_tokens": completion_tokens(fd_rows, cxn),
            "offered_worked_proxy_ge30tok": off_worked,
            "offered_completion_tokens": completion_tokens(offered_rows, cxn)}


def analyze():
    out = {"human_baseline_exp1": HUMAN_BASELINE,
           "anchor": "resource/scivetti-2025-cxnli-dataset (ratified 2026-05-29, Tom)",
           "design": ("uptake-inducing (offered working surface -> FORCED decomposition); "
                      "items byte-identical to sessions 57/58"),
           "paired_baseline": "session 58 (offered working surface)",
           "models": {}}
    for slot, name in PANEL_NAMES.items():
        f = RAW / f"{slot}-labels.json"
        off_f = OFFERED_RAW / f"{slot}-labels.json"
        forced_f = FORCED_RAW / f"{slot}-nli.json"
        if not f.exists():
            print(f"  (missing {f.name}; skipping {name})")
            continue
        fd_rows = json.load(open(f))
        offered_rows = json.load(open(off_f)) if off_f.exists() else []
        forced_rows = json.load(open(forced_f)) if forced_f.exists() else []
        unparseable = sum(1 for r in fd_rows if r["value"] is None)
        modes = dict(Counter(r["parse_mode"] for r in fd_rows))
        m = {"unparseable": unparseable, "parse_modes": modes,
             "per_construction_fd": {}, "paired_vs_offered": {},
             "forced_acc_s57": {}}
        for cxn in (TARGET, CONTROL):
            cc = per_cxn_acc(fd_rows, cxn)
            cc["baseline_verdict"] = baseline_verdict(cc["wilson_lo"], cc["wilson_hi"])
            cc["ratified_anchor"] = cxn in RATIFIED
            m["per_construction_fd"][cxn] = cc
            if offered_rows:
                m["paired_vs_offered"][cxn] = paired(fd_rows, offered_rows, cxn)
            if forced_rows:
                fr = [r for r in forced_rows if r["cxn"] == cxn]
                k = sum(1 for r in fr if correct(r))
                m["forced_acc_s57"][cxn] = round(k / len(fr), 4) if fr else None
        if offered_rows:
            m["control_guard_comp_correlative"] = control_guard(
                m["per_construction_fd"][CONTROL], offered_rows)
            m["uptake_target"] = uptake_summary(fd_rows, offered_rows, TARGET)
        out["models"][name] = m
    out["target_summary"] = {
        "construction": TARGET,
        "per_model_verdict_vs_offered": {
            name: m["paired_vs_offered"].get(TARGET, {}).get("verdict")
            for name, m in out["models"].items() if m.get("paired_vs_offered")},
        "per_model_fd_acc": {
            name: m["per_construction_fd"][TARGET]["acc"]
            for name, m in out["models"].items()},
    }
    json.dump(out, open(HERE / "results.json", "w"), indent=2)
    print(f"wrote results.json ({len(out['models'])} models)")
    for name, m in out["models"].items():
        print(f"\n{name}: unparseable {m['unparseable']}, parse_modes {m['parse_modes']}")
        for cxn in (TARGET, CONTROL):
            c = m["per_construction_fd"][cxn]
            tag = " *anchor" if c["ratified_anchor"] else " (descriptive)"
            s57 = m["forced_acc_s57"].get(cxn)
            print(f"  {cxn:24s} forced(s57)={s57} -> fd_acc={c['acc']:.3f} "
                  f"[{c['wilson_lo']:.3f},{c['wilson_hi']:.3f}] "
                  f"vs human {HUMAN_BASELINE}->{c['baseline_verdict']}{tag}")
            if cxn in m["paired_vs_offered"]:
                pr = m["paired_vs_offered"][cxn]
                print(f"     PAIRED vs OFFERED: {pr['base_acc']:.3f} -> {pr['fd_acc']:.3f} "
                      f"(Δ{pr['acc_delta']:+.3f}); gains {pr['gains_wrong_to_right']} "
                      f"losses {pr['losses_right_to_wrong']} "
                      f"p_lift={pr['p_lift_one_sided']:.4f} => {pr['verdict']}")
        if "control_guard_comp_correlative" in m:
            print(f"     CONTROL GUARD: {m['control_guard_comp_correlative']['status']}")
        if "uptake_target" in m:
            u = m["uptake_target"]
            print(f"     UPTAKE (let-alone): forced-decomp worked "
                  f"{u['forced_decomp_worked']}/{u['n']} "
                  f"(ct {u['forced_decomp_completion_tokens']}) | "
                  f"offered worked~{u['offered_worked_proxy_ge30tok']}/{u['n']} "
                  f"(ct {u['offered_completion_tokens']})")
    print(f"\nTARGET ({TARGET}) verdict vs offered: "
          f"{out['target_summary']['per_model_verdict_vs_offered']}")
    print(f"TARGET fd_acc: {out['target_summary']['per_model_fd_acc']}")
    return out


def selftest():
    assert abs(binom_tail_ge(0, 0) - 1.0) < 1e-12
    assert abs(binom_tail_ge(5, 5) - 0.5**5) < 1e-12
    lo, hi, p = wilson(24, 24)
    assert p == 1.0 and hi == 1.0 and lo < 1.0
    # paired: all base-wrong -> fd-right is a clean LIFT
    base = [{"item_id": f"let-alone#{i}", "cxn": "let-alone", "gold": 0,
             "value": 1} for i in range(8)]
    fd = [{"item_id": f"let-alone#{i}", "cxn": "let-alone", "gold": 0,
           "value": 0, "parse_mode": "tagged",
           "uptake": {"worked": True}} for i in range(8)]
    pr = paired(fd, base, "let-alone")
    assert pr["gains_wrong_to_right"] == 8 and pr["losses_right_to_wrong"] == 0
    assert pr["verdict"] == "LIFTS" and pr["p_lift_one_sided"] < 0.05, pr
    # paired: no change -> UNCHANGED
    fd2 = [{"item_id": f"let-alone#{i}", "cxn": "let-alone", "gold": 0,
            "value": 1, "parse_mode": "tagged"} for i in range(8)]
    pr2 = paired(fd2, base, "let-alone")
    assert pr2["verdict"] == "UNCHANGED" and pr2["gains_wrong_to_right"] == 0
    # control guard: fd CI contains base acc -> PRESERVED
    base_cc = [{"item_id": f"comparative-correlative#{i}", "cxn": CONTROL, "gold": 0,
                "value": 0} for i in range(30)]
    fd_cc = per_cxn_acc([{"item_id": f"comparative-correlative#{i}", "cxn": CONTROL,
                          "gold": 0, "value": 0} for i in range(30)], CONTROL)
    cg = control_guard(fd_cc, base_cc)
    assert cg["status"] == "PRESERVED", cg
    # uptake: worked counts from the uptake field; offered proxy from tokens
    fd_u = [{"cxn": "let-alone", "uptake": {"worked": True},
             "usage": {"completion_tokens": 200}} for _ in range(8)]
    off_u = [{"cxn": "let-alone", "usage": {"completion_tokens": 8}} for _ in range(8)]
    us = uptake_summary(fd_u, off_u, "let-alone")
    assert us["forced_decomp_worked"] == 8 and us["offered_worked_proxy_ge30tok"] == 0, us
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
