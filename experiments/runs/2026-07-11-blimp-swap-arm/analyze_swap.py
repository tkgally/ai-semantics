#!/usr/bin/env python3
"""analyze_swap.py — score the frozen BLiMP swap arm (A3b, s210). Recomputes every figure from raw/ +
the frozen instrument only. Thresholds FROZEN in PREREG.md, copied here as constants; nothing tuned post-hoc.

Verdict (G-metric — signed-CI TOST equivalence, per model, per stratum):
  Δ_pair = acc_swap_pair − acc_orig_pair (order-averaged per member; orig/swap of the same pairID paired).
  Δ̄(m,stratum) = mean Δ_pair over the stratum's pairs; percentile bootstrap CI over pairs (BOOT, SEED).
  SWAP-STABLE  iff Δ̄ CI ⊂ [−0.05, +0.05] on BOTH strata for ≥2/3 models.
  SWAP-DROPS   iff Δ̄ ≤ −0.05 with CI excluding 0 within a stratum on ≥2/3.
  else SWAP-INCONCLUSIVE.
G-coverage: a paradigm below the 0.50 coverage floor is flagged weak and EXCLUDED from the stratum verdict.
Diagnostics: position-lock / ans1_rate (INSTRUMENT-FAILURE guard); achieved freq-match gap (G-freq).

  python3 analyze_swap.py           # the verdict + coverage + freq-match (from raw/)
  python3 analyze_swap.py --c4      # ALSO the G-freq-pretraining C4 unigram diagnostic ($0, bounded stream)
"""
import argparse, json, math, os, sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).parent
RAW = HERE / "raw"
ITEMS = json.load(open(HERE / "items_swap.json"))
SEL = json.load(open(HERE / "selection.json"))
UIDS = ITEMS["selected"]
STRATA = ITEMS["strata"]                      # uid -> 'shallow'|'deep'
SLOTS = ["A", "B", "C"]

# FROZEN (PREREG)
MARGIN = 0.05
COV_FLOOR = 0.50
BOOT = 5000
SEED = 20260711
POSLOCK_FAIL = 0.50
ANS1_EXTREME = 0.40


def load(slot):
    """Return per-pair order-averaged accuracy per condition, per paradigm, + diagnostics."""
    per = {}                                  # uid -> pairID -> {'orig':acc,'swap':acc}
    ans1 = plock_n = plock_d = ncall = 0
    for uid in UIDS:
        rows = json.load(open(RAW / f"{slot}-{uid}.json"))
        d = {}
        for r in rows:
            ncall += 1
            if r["choice"] == 1: ans1 += 1
            d.setdefault(r["pairID"], {}).setdefault(r["cond"], {})[r["order"]] = r
        pd = {}
        for pid, conds in d.items():
            rec = {}
            for cond, od in conds.items():
                cs = [x["correct"] for x in od.values() if x["correct"] is not None]
                rec[cond] = (sum(cs) / len(cs)) if cs else None
                gf, gs = od.get("gf"), od.get("gs")
                if gf and gs and gf["choice"] is not None and gs["choice"] is not None:
                    plock_d += 1
                    if gf["choice"] == gs["choice"]: plock_n += 1
            pd[pid] = rec
        per[uid] = pd
    diag = {"ans1_rate": ans1 / ncall, "poslock_rate": plock_n / plock_d if plock_d else float("nan"),
            "n_calls": ncall}
    return per, diag


def stratum_deltas(per, stratum, cov_ok):
    """List of Δ_pair over the stratum's coverage-passing paradigms."""
    ds = []
    for uid in UIDS:
        if STRATA[uid] != stratum or not cov_ok[uid]:
            continue
        for pid, rec in per[uid].items():
            if rec.get("orig") is not None and rec.get("swap") is not None:
                ds.append(rec["swap"] - rec["orig"])
    return np.array(ds, float)


def boot_ci(ds, rng):
    if len(ds) == 0: return (float("nan"), float("nan"))
    bs = [ds[rng.integers(0, len(ds), len(ds))].mean() for _ in range(BOOT)]
    return tuple(np.percentile(bs, [2.5, 97.5]))


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--c4", action="store_true"); args = ap.parse_args()
    rng = np.random.default_rng(SEED)

    # coverage (G-coverage) from the frozen build
    cov = {r["uid"]: r["mean_coverage"] for r in SEL["build_report"]}
    cov_ok = {uid: cov[uid] >= COV_FLOOR for uid in UIDS}

    result = {"per_model": {}, "coverage": cov, "coverage_ok": cov_ok, "readings": {}}
    for slot in SLOTS:
        per, diag = load(slot)
        acc = {uid: {c: float(np.mean([per[uid][pid][c] for pid in per[uid] if per[uid][pid].get(c) is not None]))
                     for c in ("orig", "swap")} for uid in UIDS}
        strat = {}
        for st in ("shallow", "deep"):
            ds = stratum_deltas(per, st, cov_ok)
            lo, hi = boot_ci(ds, rng)
            strat[st] = {"delta_mean": float(ds.mean()) if len(ds) else float("nan"),
                         "ci": [float(lo), float(hi)], "n_pairs": int(len(ds)),
                         "within_margin": bool(-MARGIN <= lo and hi <= MARGIN),
                         "drops": bool((not math.isnan(lo)) and hi <= -MARGIN and lo <= -MARGIN)}
        result["per_model"][slot] = {
            "per_paradigm_acc": {uid: {c: round(acc[uid][c], 4) for c in ("orig", "swap")} for uid in UIDS},
            "per_paradigm_delta": {uid: round(acc[uid]["swap"] - acc[uid]["orig"], 4) for uid in UIDS},
            "stratum": {st: {**strat[st], "delta_mean": round(strat[st]["delta_mean"], 4),
                             "ci": [round(x, 4) for x in strat[st]["ci"]]} for st in strat},
            "ans1_rate": round(diag["ans1_rate"], 4), "poslock_rate": round(diag["poslock_rate"], 4),
            "n_calls": diag["n_calls"]}

    def maj(pred): return sum(1 for s in SLOTS if pred(s)) >= 2
    pm = result["per_model"]
    stable = maj(lambda s: pm[s]["stratum"]["shallow"]["within_margin"] and pm[s]["stratum"]["deep"]["within_margin"])
    drops = maj(lambda s: pm[s]["stratum"]["shallow"]["drops"] or pm[s]["stratum"]["deep"]["drops"])
    verdict = "SWAP-STABLE" if stable else ("SWAP-DROPS" if drops else "SWAP-INCONCLUSIVE")
    instr_fail = maj(lambda s: pm[s]["poslock_rate"] > POSLOCK_FAIL and abs(pm[s]["ans1_rate"] - 0.5) > ANS1_EXTREME)

    # G-freq achieved match gap (from the frozen subs: |Lg10WF(orig) − Lg10WF(sub)| where both known)
    result["readings"] = {
        "verdict": verdict,
        "combined_promotion": ("CANDIDATE (SURVIVES-COVARIATE ∧ SWAP-STABLE) — a later cross-session review writes the claim"
                               if verdict == "SWAP-STABLE" else
                               ("REFUSED (SWAP-DROPS)" if verdict == "SWAP-DROPS" else "NEITHER (SWAP-INCONCLUSIVE)")),
        "instrument_failure": instr_fail,
        "coverage_floor": COV_FLOOR, "coverage_excluded": [u for u in UIDS if not cov_ok[u]],
        "margin": MARGIN, "n_per_stratum": {st: {s: pm[s]["stratum"][st]["n_pairs"] for s in SLOTS} for st in ("shallow", "deep")},
        "note": "per-model, per-stratum signed Δ̄ with bootstrap CI; ≥2/3 rule; scope-deep carries the test (shallow near ceiling).",
    }
    json.dump(result, open(HERE / "results.json", "w"), indent=1)

    print("=== BLiMP swap arm — results (s210) ===")
    print(f"selected shallow={ITEMS['selected'][:3]}  deep={ITEMS['selected'][3:]}")
    print(f"coverage: " + "  ".join(f"{u.split('_')[0]}..={cov[u]:.2f}" for u in UIDS) +
          f"   (floor {COV_FLOOR}; excluded {[u for u in UIDS if not cov_ok[u]] or 'NONE'})")
    for s in SLOTS:
        m = pm[s]
        print(f"\n[{s}] ans1={m['ans1_rate']:.3f} poslock={m['poslock_rate']:.3f} n_calls={m['n_calls']}")
        for st in ("shallow", "deep"):
            x = m["stratum"][st]
            print(f"    {st:7s} Δ̄={x['delta_mean']:+.4f} CI[{x['ci'][0]:+.4f},{x['ci'][1]:+.4f}] "
                  f"n={x['n_pairs']}  within±{MARGIN}={x['within_margin']} drops={x['drops']}")
        print("    per-paradigm Δacc: " + "  ".join(f"{u.split('_')[0][:6]}={m['per_paradigm_delta'][u]:+.3f}" for u in UIDS))
    r = result["readings"]
    print("\n--- VERDICT ---")
    print("SWAP:", r["verdict"], "|", r["combined_promotion"])
    print("instrument-failure:", r["instrument_failure"])

    if args.c4:
        c4_diagnostic()


def c4_diagnostic():
    """G-freq-pretraining: swap-set vs orig-set unigram C4 (pretraining-proxy) log-freq, bounded stream."""
    import importlib.util, re as _re
    COOC = HERE / ".." / "2026-07-08-relation-recovery-taxonomic-proxy" / "build_cooc_c4.py"
    spec = importlib.util.spec_from_file_location("build_cooc_c4", COOC)
    cooc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cooc)
    C4_MAX_SENTENCES = 3_000_000       # FROZEN bound (PREREG): enough for a word-set distributional compare
    # collect orig vs swap open-class substitute words from the frozen build
    orig_w, swap_w = set(), set()
    for uid in UIDS:
        for p in ITEMS["items"][uid]:
            for sub in p["subs"]:
                orig_w.add(sub[1].lower()); swap_w.add(sub[2].lower())
    targets = orig_w | swap_w
    counts = {w: 0 for w in targets}
    seen = 0
    for toks in cooc.stream_sentences():
        for t in toks:
            if t in counts: counts[t] += 1
        seen += 1
        if seen >= C4_MAX_SENTENCES: break
    def lg(ws): return [math.log10(counts[w] + 1) for w in ws if w.isalpha()]
    lo, ls = lg(orig_w), lg(swap_w)
    out = {"c4_sentences": seen, "n_orig_words": len(orig_w), "n_swap_words": len(swap_w),
           "orig_mean_log_c4": round(float(np.mean(lo)), 4), "swap_mean_log_c4": round(float(np.mean(ls)), 4),
           "gap_orig_minus_swap": round(float(np.mean(lo) - np.mean(ls)), 4),
           "orig_zero_rate": round(sum(1 for w in orig_w if counts[w] == 0) / len(orig_w), 4),
           "swap_zero_rate": round(sum(1 for w in swap_w if counts[w] == 0) / len(swap_w), 4)}
    json.dump(out, open(HERE / "c4_pretraining_diag.json", "w"), indent=1)
    print("\n--- G-freq-pretraining (C4 pretraining-proxy, %d sentences) ---" % seen)
    print(f"  orig mean log-C4 {out['orig_mean_log_c4']}  swap {out['swap_mean_log_c4']}  "
          f"gap(orig−swap) {out['gap_orig_minus_swap']:+.4f}  (zero-rate orig {out['orig_zero_rate']} / swap {out['swap_zero_rate']})")


if __name__ == "__main__":
    main()
