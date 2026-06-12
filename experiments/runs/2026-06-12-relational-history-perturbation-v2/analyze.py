#!/usr/bin/env python3
"""analyze.py — pre-registered analysis for the history-perturbation probe (v2).

Implements exactly the PREREG measures (as revised by the pre-run critic before any
finding-bearing call): per-cluster manipulation gate, primary chronological recency-pick
rate rho_chron per presentation direction with clustered bootstrap CIs, the physical-
position diagnostic rho_phys, out-of-pair and NA rates, secondary clean-vs-interleaved
descriptives, and the pre-registered verdict per model. Gemini's 3-cluster CI is
descriptive-only (pre-registered).
"""
import json
import os
import random
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
N_BOOT = 10000
SEED = 20260612
CLEAN = {"XXYY", "YYXX"}


def rate(trials, key):
    inp = [r for r in trials if r.get("in_pair")]
    if not inp:
        return None, 0
    return sum(1 for r in inp if r[key]) / len(inp), len(inp)


def cluster_boot(trials, key, rng):
    clusters = defaultdict(list)
    for r in trials:
        clusters[(r["pair"], r["sample"])].append(r)
    keys = sorted(clusters)
    vals = []
    for _ in range(N_BOOT):
        sample = []
        for _k in keys:
            sample += clusters[rng.choice(keys)]
        v, n = rate(sample, key)
        if v is not None:
            vals.append(v)
    vals.sort()
    if not vals:
        return None, None
    return vals[int(0.025 * len(vals))], vals[int(0.975 * len(vals))]


def fmt(v):
    return "NA" if v is None else f"{v:.3f}"


def ci_side(lo, hi):
    """-1 below 0.5, +1 above 0.5, 0 includes 0.5 (or no CI)."""
    if lo is None:
        return 0
    if lo > 0.5:
        return 1
    if hi < 0.5:
        return -1
    return 0


def main():
    recs = json.load(open(os.path.join(HERE, "raw", "results.json")))
    rng = random.Random(SEED)
    print("clusters gated on their own consistent controls (both twins correct).")
    for m in ("claude", "gpt", "gemini"):
        rs = [r for r in recs if r["model"] == m]
        cons = [r for r in rs if r["kind"] == "consistent"]
        mixed = [r for r in rs if r["kind"] == "mixed"]
        na = sum(1 for r in rs if r["pick_cid"] is None)
        retried = sum(1 for r in rs if r.get("retried"))

        # per-cluster gate (critic B2): both twins' controls correct
        gate_ok = {}
        by_cluster = defaultdict(list)
        for r in cons:
            by_cluster[(r["pair"], r["sample"])].append(r)
        for k, cl in sorted(by_cluster.items()):
            gate_ok[k] = all(r["correct"] for r in cl)
        gacc = sum(1 for r in cons if r["correct"]) / len(cons)
        n_pass = sum(gate_ok.values())

        parsed = [r for r in mixed if r["pick_cid"] is not None]
        oop = (sum(1 for r in parsed if not r["in_pair"]) / len(parsed)) if parsed else 1.0
        gated = [r for r in parsed if gate_ok.get((r["pair"], r["sample"]))]

        print(f"\n[{m}] mixed={len(mixed)} consistent={len(cons)} NA={na} retried={retried}")
        print(f"  GATE: control acc={gacc:.2f}; clusters passing both-twin gate: "
              f"{n_pass}/{len(gate_ok)} {sorted(k for k,v in gate_ok.items() if v)}")
        print(f"  out-of-pair (parsed)={oop:.3f} "
              f"({'FLAG under-powered' if oop > 0.5 else 'ok'})")

        sides = {}
        for label, pool in (("GATED", gated), ("ungated", parsed)):
            for d in ("fwd", "rev"):
                dd = [r for r in pool if r["direction"] == d]
                rc, n = rate(dd, "picked_chron_last")
                lo, hi = cluster_boot(dd, "picked_chron_last", rng)
                rp, _ = rate(dd, "picked_phys_last")
                plo, phi = cluster_boot(dd, "picked_phys_last", rng)
                print(f"  {label:7s} {d}: rho_chron={fmt(rc)} CI[{fmt(lo)},{fmt(hi)}] "
                      f"rho_phys={fmt(rp)} CI[{fmt(plo)},{fmt(phi)}] (in-pair n={n})")
                if label == "GATED":
                    sides[("chron", d)] = ci_side(lo, hi)
                    sides[("phys", d)] = ci_side(plo, phi)
        # secondary descriptives (gated, both directions pooled, chron measure)
        for nm, sel in (("clean", lambda r: r["order"] in CLEAN),
                        ("interleaved", lambda r: r["order"] not in CLEAN)):
            v, n = rate([r for r in gated if sel(r)], "picked_chron_last")
            print(f"  SECONDARY {nm}: rho_chron={fmt(v)} (n={n})")

        # pre-registered verdict
        if n_pass == 0:
            verdict = "METHODOLOGICAL NULL (no cluster passed the manipulation gate)"
        elif oop > 0.5:
            verdict = "UNDER-POWERED (out-of-pair > 0.5 on parsed picks)"
        else:
            c_f, c_r = sides[("chron", "fwd")], sides[("chron", "rev")]
            p_f, p_r = sides[("phys", "fwd")], sides[("phys", "rev")]
            if c_f != 0 and c_f == c_r:
                d = "RECENCY" if c_f > 0 else "PRIMACY"
                verdict = (f"NON-COMMUTATIVE (chronology-tracking, {d}; both presentation "
                           f"arms agree) — falsification clause met")
            elif p_f != 0 and p_f == p_r and not (c_f != 0 and c_f == c_r):
                verdict = ("PHYSICAL-POSITION ARTIFACT (pick follows the physically-last "
                           "line in both arms) — methodological finding, NOT relational; "
                           "conjecture untouched")
            elif c_f == 0 and c_r == 0 and p_f == 0 and p_r == 0:
                verdict = "COMMUTATIVE NULL (all CIs include 0.5; conjecture's bet holds at this power)"
            else:
                verdict = "INCONCLUSIVE/MIXED (arms disagree; report point estimates only)"
        if m == "gemini":
            verdict += "  [DESCRIPTIVE ONLY: 3 clusters — pre-registered CI instability]"
        print(f"  VERDICT: {verdict}")


if __name__ == "__main__":
    main()
