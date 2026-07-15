#!/usr/bin/env python3
"""analyze_swap_c4.py — score the frozen BLiMP C4-MATCHED swap arm (A3b, s232). Recomputes every figure
from raw/ + the frozen instrument only. Thresholds FROZEN in PREREG.md, copied here as constants; nothing
tuned post-hoc. The BLIND-SCORING LOCK (BLOCKER 4): this scoring code + the exclusion criteria + the
four-outcome decision table are frozen BEFORE any re-run; the run verifier attests no human-readable
intermediate output was inspected until the whole batch was scored.

VERDICT — the FOUR-OUTCOME decision table (BLOCKER 4; the disambiguation map):
  0. G-C4-match-adequacy FIRST (BLOCKER 3; blind, build-time, pre-model-call): signed set-mean C4 gap
     g_C4 = mean over all subs of (c4log(orig) - c4log(swap)), at the C4_NUM_SHARDS stream scale.
     if |g_C4| > MAX_SETMEAN_C4_GAP (0.05)  -> STILL-INCONCLUSIVE-BY-MATCH-FAILURE  (no DROPS/STABLE read;
        the +0.204 confound was NOT demonstrably closed at this band/stream).
  Else read the inherited G-metric (signed-CI TOST equivalence, per model, per DEEP stratum, ±0.05 bands):
  1. DEEP-STILL-DROPS   iff the whole deep Δ̄ CI ≤ -0.05 (i.e. Δ̄ ≤ -0.05 AND the CI upper bound ≤ -0.05) on ≥2/3 -> cleaner exact-string memorization,
        R1 refused promotion more firmly (a first-class negative).
  2. DEEP-SWAP-STABLE   iff Δ̄ CI ⊂ [-0.05,+0.05] on BOTH strata for ≥2/3 -> the s210 drop WAS the C4
        confound; with s208 SURVIVES-COVARIATE, R1 is a bounded promotion-review CANDIDATE (cross-session).
  3. STILL-INCONCLUSIVE otherwise.
G-coverage: a paradigm below the 0.50 coverage floor is flagged weak and EXCLUDED from the stratum verdict.
G-power / S1 attrition (SHOULD-FIX 7): a DEEP paradigm below USABLE_FLOOR=60 usable pairs is dropped; if
  ≥2 deep paradigms remain -> re-verdict on deep-2; if <2 remain -> ATTRITION-INCONCLUSIVE (pre-registered,
  never a post-hoc choice).
Diagnostics: position-lock / ans1_rate (INSTRUMENT-FAILURE guard); achieved SUBTLEX gap (G-freq, inherited);
  achieved per-word AND set-mean C4 gap + a soft directional-cancellation check (SHOULD-FIX 6).

  python3 analyze_swap_c4.py
"""
import json, math, os, sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).parent
RAW = HERE / "raw"
ITEMS = json.load(open(HERE / "items_swap_c4.json"))
SEL = json.load(open(HERE / "selection_c4.json"))
UIDS = ITEMS["selected"]
STRATA = ITEMS["strata"]                      # uid -> 'shallow'|'deep'
SLOTS = ["A", "B", "C"]

# FROZEN (PREREG s232)
MARGIN = 0.05                     # G-metric ±0.05 equivalence band (inherited)
COV_FLOOR = 0.50                  # G-coverage (inherited)
USABLE_FLOOR = 60                 # G-power / S1 attrition (inherited)
MAX_SETMEAN_C4_GAP = 0.05         # BLOCKER 3: |signed set-mean C4 gap| ≤ 0.05 or MATCH-FAILURE
PERWORD_C4_TIGHT = 0.15           # SHOULD-FIX 6: fraction of subs within this tighter per-word C4 band (report)
BOOT = 5000
SEED = 20260715
POSLOCK_FAIL = 0.50
ANS1_EXTREME = 0.40


def load(slot):
    per = {}
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


def usable_pairs(per, uid):
    return [pid for pid, rec in per[uid].items()
            if rec.get("orig") is not None and rec.get("swap") is not None]


def stratum_deltas(per, stratum, cov_ok, keep):
    ds = []
    for uid in UIDS:
        if STRATA[uid] != stratum or not cov_ok[uid] or not keep[uid]:  # F1: exclude below-floor paradigms (S7)
            continue
        for pid in usable_pairs(per, uid):
            ds.append(per[uid][pid]["swap"] - per[uid][pid]["orig"])
    return np.array(ds, float)


def boot_ci(ds, rng):
    if len(ds) == 0: return (float("nan"), float("nan"))
    bs = [ds[rng.integers(0, len(ds), len(ds))].mean() for _ in range(BOOT)]
    return tuple(np.percentile(bs, [2.5, 97.5]))


def c4_adequacy():
    """G-C4-match-adequacy (BLOCKER 3) + per-word report + soft cancellation check (SHOULD-FIX 6).
    Reads the per-sub [c4log(orig), c4log(swap)] recorded by build_swap_c4.py (blind, build-time)."""
    signed = []                                   # per-sub (orig - swap): >0 => swap rarer in C4
    for uid in UIDS:
        for p in ITEMS["items"][uid]:
            for oc, nc in p.get("sub_c4", []):
                signed.append(oc - nc)
    a = np.array(signed) if signed else np.array([0.0])
    set_mean = float(a.mean())
    perword_abs = np.abs(a)
    # soft cancellation check: does a small set-mean hide large within-band per-word gaps of both signs?
    frac_pos = float((a > 0).mean()); frac_neg = float((a < 0).mean())
    cancellation_flag = bool(abs(set_mean) <= MAX_SETMEAN_C4_GAP
                             and float(perword_abs.mean()) > 2 * MAX_SETMEAN_C4_GAP
                             and min(frac_pos, frac_neg) > 0.30)
    return {"n_subs": int(len(signed)),
            "signed_set_mean_gap": round(set_mean, 4),
            "abs_set_mean_gap": round(abs(set_mean), 4),
            "adequate": bool(abs(set_mean) <= MAX_SETMEAN_C4_GAP),
            "threshold": MAX_SETMEAN_C4_GAP,
            "perword_mean_abs_gap": round(float(perword_abs.mean()), 4),
            "perword_max_abs_gap": round(float(perword_abs.max()), 4),
            "perword_p95_abs_gap": round(float(np.percentile(perword_abs, 95)), 4),
            "frac_within_perword_tight": round(float((perword_abs <= PERWORD_C4_TIGHT + 1e-9).mean()), 4),
            "perword_tight_band": PERWORD_C4_TIGHT,
            "frac_swap_rarer": round(frac_pos, 4), "frac_swap_commoner": round(frac_neg, 4),
            "directional_cancellation_flag": cancellation_flag,
            "c4_num_shards": SEL.get("c4_num_shards"), "c4_sentences": SEL.get("c4_sentences_streamed")}


def g_freq_report():
    """G-freq (inherited): achieved per-word |Lg10WF(orig) − Lg10WF(sub)| over the frozen subs."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("build_swap_c4", HERE / "build_swap_c4.py")
    bs = importlib.util.module_from_spec(spec); spec.loader.exec_module(bs)
    lex = bs.load_lexicon()
    gaps, name_unmatched, n_subs = [], 0, 0
    by_type = {}
    for uid in UIDS:
        for p in ITEMS["items"][uid]:
            for sub in p["subs"]:
                typ, orig, new = sub[0], sub[1].lower(), sub[2].lower()
                n_subs += 1
                lo = lex.get(orig, {}).get("lg"); ln = lex.get(new, {}).get("lg")
                if typ == "name" and lo is None:
                    name_unmatched += 1; continue
                if lo is not None and ln is not None:
                    g = abs(lo - ln); gaps.append(g); by_type.setdefault(typ, []).append(g)
    gaps = np.array(gaps) if gaps else np.array([0.0])
    return {"n_subs": n_subs, "n_gaps_measured": int(len(gaps)),
            "mean_abs_gap": round(float(gaps.mean()), 4), "max_abs_gap": round(float(gaps.max()), 4),
            "p95_abs_gap": round(float(np.percentile(gaps, 95)), 4),
            "frac_within_0.10": round(float((gaps <= 0.10 + 1e-9).mean()), 4),
            "name_orig_unmatched": name_unmatched,
            "mean_gap_by_type": {t: round(float(np.mean(v)), 4) for t, v in by_type.items()}}


def main():
    rng = np.random.default_rng(SEED)
    cov = {r["uid"]: r["mean_coverage"] for r in SEL["build_report"]}
    cov_ok = {uid: cov[uid] >= COV_FLOOR for uid in UIDS}

    # ---- G-C4-match-adequacy FIRST (BLOCKER 3) — gates whether any DROPS/STABLE verdict is read ----
    adeq = c4_adequacy()

    # ---- per-model, per-stratum deltas + S1 attrition fallback (SHOULD-FIX 7) ----
    result = {"per_model": {}, "coverage": cov, "coverage_ok": cov_ok, "readings": {}}
    per_by_slot = {}
    for slot in SLOTS:
        per, diag = load(slot); per_by_slot[slot] = (per, diag)

    # attrition: a paradigm is 'kept' iff usable pairs ≥ USABLE_FLOOR on ALL slots
    keep = {}
    n_usable = {}
    for uid in UIDS:
        mins = min(len(usable_pairs(per_by_slot[s][0], uid)) for s in SLOTS)
        n_usable[uid] = mins
        keep[uid] = mins >= USABLE_FLOOR
    deep_kept = [u for u in UIDS if STRATA[u] == "deep" and keep[u] and cov_ok[u]]
    attrition_inconclusive = len(deep_kept) < 2

    for slot in SLOTS:
        per, diag = per_by_slot[slot]
        acc = {uid: {c: float(np.mean([per[uid][pid][c] for pid in per[uid] if per[uid][pid].get(c) is not None]))
                     for c in ("orig", "swap")} for uid in UIDS}
        strat = {}
        for st in ("shallow", "deep"):
            ds = stratum_deltas(per, st, cov_ok, keep)
            lo, hi = boot_ci(ds, rng)
            strat[st] = {"delta_mean": float(ds.mean()) if len(ds) else float("nan"),
                         "ci": [float(lo), float(hi)], "n_pairs": int(len(ds)),
                         "within_margin": bool((not math.isnan(lo)) and -MARGIN <= lo and hi <= MARGIN),
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
    drops = maj(lambda s: pm[s]["stratum"]["deep"]["drops"])
    instr_fail = maj(lambda s: pm[s]["poslock_rate"] > POSLOCK_FAIL and abs(pm[s]["ans1_rate"] - 0.5) > ANS1_EXTREME)

    # ---- FOUR-OUTCOME decision table (BLOCKER 4) ----
    if not adeq["adequate"]:
        verdict = "STILL-INCONCLUSIVE-BY-MATCH-FAILURE"
        reading = ("the achieved |signed set-mean C4 gap| %.4f exceeds the ±%.2f adequacy threshold; the "
                   "+0.204 s210 confound was NOT demonstrably closed at this band/stream, so no "
                   "DROPS/STABLE verdict is read." % (adeq["abs_set_mean_gap"], MAX_SETMEAN_C4_GAP))
    elif attrition_inconclusive:
        verdict = "ATTRITION-INCONCLUSIVE"
        reading = ("<2 deep paradigms cleared USABLE_FLOOR=%d after dual-band attrition (deep kept: %s); "
                   "pre-registered attrition landing, no deep-stratum verdict read." % (USABLE_FLOOR, deep_kept))
    elif drops:
        verdict = "DEEP-STILL-DROPS"
        reading = ("the whole deep Δ̄ CI ≤ −%.2f (Δ̄ and CI-upper both ≤ −0.05) on ≥2/3 under a two-frequency-channel-matched swap → "
                   "a CLEANER exact-string / lexical-item memorization signal than s210; R1 refused promotion "
                   "MORE firmly (a first-class negative)." % MARGIN)
    elif stable:
        verdict = "DEEP-SWAP-STABLE"
        reading = ("deep + shallow Δ̄ CI ⊂ ±%.2f on ≥2/3 → the s210 deep drop WAS the C4 confound; with the "
                   "s208 SURVIVES-COVARIATE, R1 is a BOUNDED promotion-review CANDIDATE (bounded to 'not "
                   "exact-string memorization, not the surface freq proxy, not the pretraining-proxy freq "
                   "gap'; STILL NOT construction-frequency-controlled; a later cross-session review writes/"
                   "refuses the claim)." % MARGIN)
    else:
        verdict = "STILL-INCONCLUSIVE"
        reading = ("neither a ≥2/3 deep drop nor a ≥2/3 both-strata equivalence; even a two-confound-clean "
                   "swap did not resolve the deep-scope alignment at this N (a candid ceiling).")

    result["g_freq"] = g_freq_report()
    result["c4_adequacy"] = adeq
    result["attrition"] = {"n_usable_min_over_slots": n_usable, "kept": keep, "deep_kept": deep_kept,
                           "usable_floor": USABLE_FLOOR, "attrition_inconclusive": attrition_inconclusive}
    result["readings"] = {
        "verdict": verdict, "reading": reading,
        "instrument_failure": instr_fail,
        "coverage_floor": COV_FLOOR, "coverage_excluded": [u for u in UIDS if not cov_ok[u]],
        "margin": MARGIN, "adequacy_threshold": MAX_SETMEAN_C4_GAP,
        "n_per_stratum": {st: {s: pm[s]["stratum"][st]["n_pairs"] for s in SLOTS} for st in ("shallow", "deep")},
        "note": "four-outcome table; adequacy gate FIRST; deep stratum carries the test; shallow near ceiling.",
    }
    json.dump(result, open(HERE / "results.json", "w"), indent=1)

    print("=== BLiMP C4-matched swap arm — results (s232) ===")
    print(f"build mode: {ITEMS.get('mode')}  |  C4 stream: {adeq['c4_sentences']} sent ({adeq['c4_num_shards']} shards)")
    print(f"G-C4-match-adequacy: signed set-mean gap {adeq['signed_set_mean_gap']:+.4f} "
          f"(|·| {adeq['abs_set_mean_gap']:.4f} vs ≤{MAX_SETMEAN_C4_GAP}) -> "
          f"{'ADEQUATE' if adeq['adequate'] else 'MATCH-FAILURE'}  "
          f"[per-word mean|gap| {adeq['perword_mean_abs_gap']:.3f}, within±{PERWORD_C4_TIGHT}={adeq['frac_within_perword_tight']}, "
          f"cancellation_flag={adeq['directional_cancellation_flag']}]")
    print(f"coverage: " + "  ".join(f"{u.split('_')[0][:6]}={cov[u]:.2f}" for u in UIDS) +
          f"   (floor {COV_FLOOR}; excluded {[u for u in UIDS if not cov_ok[u]] or 'NONE'})")
    print(f"attrition: deep kept {result['attrition']['deep_kept']} (floor {USABLE_FLOOR}); "
          f"{'ATTRITION-INCONCLUSIVE' if attrition_inconclusive else 'ok'}")
    for s in SLOTS:
        m = pm[s]
        print(f"\n[{s}] ans1={m['ans1_rate']:.3f} poslock={m['poslock_rate']:.3f} n_calls={m['n_calls']}")
        for st in ("shallow", "deep"):
            x = m["stratum"][st]
            print(f"    {st:7s} Δ̄={x['delta_mean']:+.4f} CI[{x['ci'][0]:+.4f},{x['ci'][1]:+.4f}] "
                  f"n={x['n_pairs']}  within±{MARGIN}={x['within_margin']} drops={x['drops']}")
    r = result["readings"]
    print("\n--- VERDICT ---")
    print(r["verdict"])
    print(r["reading"])
    print("instrument-failure:", r["instrument_failure"])


if __name__ == "__main__":
    main()
