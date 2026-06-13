#!/usr/bin/env python3
"""analyze.py — pre-registered analysis for the history-perturbation probe v3.

Implements EXACTLY the design's frozen measures and decision rule
(experiments/designs/relational-history-perturbation-v3.md §Measures / §Decision rule);
the verdict mapper is CODE (verdict() below), not prose, so it cannot be retuned
silently. No quantity outside this file's outputs may be promoted to a finding.

Per model:
- per-cluster manipulation gate (ALL FOUR consistent controls correct — 2 twins x 2
  presentation directions, critic S1);
- PRIMARY: gated rho_chron per presentation direction (chron-last-twin pick rate over
  gated, parsed, in-pair mixed trials), clustered bootstrap CI (10,000 resamples over
  (pair x sample) clusters);
- artifact diagnostic rho_phys (physically-last-line twin);
- the >=k-cluster guard, k = 3, per direction (fix 4), applied symmetrically to every
  CI-bearing clause; degenerate (zero-width) CIs satisfy NO clause;
- trial floors (critic blocker 3): >=24 gated in-pair parsed trials per direction on
  the FALSIFIED and PHYSICAL-POSITION-ARTIFACT clauses; >=36 on null-certification;
- both-directions agreement on every chronology clause (fix 5);
- NA / out-of-pair reporting (out-of-pair over parsed picks; >0.5 -> UNDER-POWERED);
  NA-concentration flag (>25% in any pair x direction cell);
- per-model strict-compliance rate;
- secondary descriptive: clean-switch (XXYY/YYXX) vs interleaved;
- sensitivity cuts (pre-registered, DESCRIPTIVE ONLY, never verdict-bearing — critic
  S5: the verdict is computed on the primary gated pool only): leave-one-pair-out (x3),
  NAs-as-out-of-pair, strict-format-only, pair-level (3-cluster) bootstrap.

Usage (from repo root or this dir):
  python3 analyze.py                          # reads raw/probe-<model>.jsonl
  python3 analyze.py --raw-dir fixtures/raw   # synthetic fixture (sanity check)
Writes <raw-dir>/analysis.json alongside the printed report.
"""
import argparse
import json
import os
import random
import sys
import zlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import read_jsonl  # noqa: E402

MODELS = ("claude", "gpt", "gemini")
N_BOOT = 10000
SEED = 20260613
K_GUARD = 3          # >=k gated clusters per direction (design fix 4)
N_FLOOR_NULL = 36    # >=36 gated in-pair parsed trials per direction for null-cert
N_FLOOR_EFFECT = 24  # >=24 gated in-pair parsed trials per direction for the
                     # FALSIFIED / PHYSICAL-POSITION-ARTIFACT clauses (critic blocker 3)
OOP_MAX = 0.5
CLEAN = {"XXYY", "YYXX"}
DIRS = ("fwd", "rev")


# ---------- mechanics ---------------------------------------------------------------
def rate(trials, key):
    """Fraction of IN-PAIR trials with truthy `key`; (value, n_in_pair)."""
    inp = [r for r in trials if r.get("in_pair")]
    if not inp:
        return None, 0
    return sum(1 for r in inp if r[key]) / len(inp), len(inp)


def cluster_boot(trials, key, cluster_of, seed_label):
    """Percentile 95% CI from N_BOOT cluster resamples (resample clusters with
    replacement; pooled in-pair rate per resample). Deterministic per label.
    Aggregated per cluster for speed — identical to pooling the raw records."""
    agg = {}  # cluster -> [n_true, n_in_pair]
    for r in trials:
        if r.get("in_pair"):
            a = agg.setdefault(cluster_of(r), [0, 0])
            a[0] += 1 if r[key] else 0
            a[1] += 1
    # clusters with zero in-pair trials contribute nothing to the pooled rate but ARE
    # resampling units only if they have in-pair data; keys = clusters with data.
    keys = sorted(agg)
    if not keys:
        return None
    rng = random.Random(SEED ^ zlib.crc32(seed_label.encode()))
    vals = []
    for _ in range(N_BOOT):
        num = den = 0
        for _k in keys:
            c = agg[rng.choice(keys)]
            num += c[0]
            den += c[1]
        if den:
            vals.append(num / den)
    if not vals:
        return None
    vals.sort()
    lo, hi = vals[int(0.025 * len(vals))], vals[int(0.975 * len(vals))]
    degenerate = (lo == hi)  # zero-width CI: carries no inferential weight, no clause
    if degenerate:
        side = None
    elif lo > 0.5:
        side = 1
    elif hi < 0.5:
        side = -1
    else:
        side = 0
    return {"lo": lo, "hi": hi, "degenerate": degenerate, "side": side,
            "n_clusters": len(keys)}


def compute(mixed, gate_ok, label, na_as_oop=False,
            cluster_of=lambda r: (r["pair"], r["sample"])):
    """All pre-registered quantities for one view of one model's mixed trials."""
    parsed = [r for r in mixed if r.get("pick_cid") is not None]
    nas = [r for r in mixed if r.get("pick_cid") is None]
    if na_as_oop:  # sensitivity cut: NAs scored as out-of-pair picks
        parsed = parsed + [{**r, "in_pair": False, "picked_chron_last": None,
                            "picked_phys_last": None} for r in nas]
        nas = []
    n_oop = sum(1 for r in parsed if not r.get("in_pair"))
    oop = (n_oop / len(parsed)) if parsed else 1.0
    gated = [r for r in parsed if gate_ok.get((r["pair"], r["sample"]))]
    out = {"label": label, "n_mixed": len(mixed), "n_parsed": len(parsed),
           "n_na": len(nas), "oop": oop, "dirs": {}}
    for d in DIRS:
        dd = [r for r in gated if r["direction"] == d]
        inp = [r for r in dd if r.get("in_pair")]
        res = {"n_in_pair": len(inp),
               "n_gated_clusters": len({cluster_of(r) for r in inp})}
        for nm, key in (("chron", "picked_chron_last"), ("phys", "picked_phys_last")):
            v, _ = rate(dd, key)
            res[f"rho_{nm}"] = v
            res[f"ci_{nm}"] = cluster_boot(dd, key, cluster_of, f"{label}:{d}:{nm}")
        # ungated, descriptive
        ud = [r for r in parsed if r["direction"] == d]
        res["rho_chron_ungated"], _ = rate(ud, "picked_chron_last")
        out["dirs"][d] = res
    out["guard_ok"] = all(out["dirs"][d]["n_gated_clusters"] >= K_GUARD for d in DIRS)
    out["floor24_ok"] = all(out["dirs"][d]["n_in_pair"] >= N_FLOOR_EFFECT for d in DIRS)
    out["floor36_ok"] = all(out["dirs"][d]["n_in_pair"] >= N_FLOOR_NULL for d in DIRS)
    # secondary descriptive (gated, both directions pooled)
    out["secondary"] = {}
    for nm, sel in (("clean", lambda r: r["order"] in CLEAN),
                    ("interleaved", lambda r: r["order"] not in CLEAN)):
        v, n = rate([r for r in gated if sel(r)], "picked_chron_last")
        out["secondary"][nm] = {"rho_chron": v, "n": n}
    return out


def verdict(stats):
    """THE pre-registered verdict mapper (design §Decision rule) — mechanical, an
    ORDERED, EXHAUSTIVE if/else tree with an explicit final else (critic blocker 1).

    Pre-registered precedence: METHODOLOGICAL NULL > UNDER-POWERED > the CI clauses
    (FALSIFIED > PHYSICAL-POSITION ARTIFACT > COMMUTATIVE-NULL-CERTIFIED > the named
    gap sub-label "INCONCLUSIVE — null pattern, certification floor unmet") > final
    else INCONCLUSIVE-MIXED. Degenerate (zero-width) CIs have side=None and satisfy no
    clause. Every CI clause requires agreement in BOTH presentation directions. Trial
    floors (critic blocker 3): the effect clauses (FALSIFIED, ARTIFACT) require >=24
    gated in-pair parsed trials per direction; null-certification keeps the stricter
    >=36 floor.
    """
    # 1. METHODOLOGICAL NULL — the >=k-cluster guard outranks everything below.
    if not stats["guard_ok"]:
        return ("METHODOLOGICAL NULL", f"< {K_GUARD} gated clusters in some direction "
                "(whatever the point estimates say)")
    # 2. UNDER-POWERED — outranks every CI clause.
    if stats["oop"] > OOP_MAX:
        return ("UNDER-POWERED", f"out-of-pair {stats['oop']:.3f} > {OOP_MAX} on parsed picks")
    side = {}
    for nm in ("chron", "phys"):
        for d in DIRS:
            ci = stats["dirs"][d][f"ci_{nm}"]
            side[(nm, d)] = None if ci is None else ci["side"]
    c_f, c_r = side[("chron", "fwd")], side[("chron", "rev")]
    p_f, p_r = side[("phys", "fwd")], side[("phys", "rev")]
    chron_pattern = (c_f is not None and c_r is not None and c_f != 0 and c_f == c_r)
    phys_pattern = (p_f is not None and p_r is not None and p_f != 0 and p_f == p_r)
    all_null = all(side[(nm, d)] == 0 for nm in ("chron", "phys") for d in DIRS)
    # 3. FALSIFIED — rho_chron CI pattern + the >=24-trial effect floor.
    if chron_pattern and stats["floor24_ok"]:
        d = "RECENCY" if c_f > 0 else "PRIMACY"
        return ("FALSIFIED", f"non-commutative, chronology-tracking ({d}); rho_chron CI "
                "excludes 0.5 on the same side in BOTH presentation directions, with "
                f">= {N_FLOOR_EFFECT} gated in-pair parsed trials per direction")
    # 4. PHYSICAL-POSITION ARTIFACT — reached only if FALSIFIED did not fire.
    if phys_pattern and stats["floor24_ok"]:
        return ("PHYSICAL-POSITION ARTIFACT", "rho_phys CI excludes 0.5 on the same side "
                "in both directions while the rho_chron clause is unmet, with "
                f">= {N_FLOOR_EFFECT} gated in-pair parsed trials per direction — "
                "position-following or direction-instruction neglect, observationally "
                "equivalent here; methodological, not relational")
    # 5. COMMUTATIVE-NULL-CERTIFIED — all four CIs null + the stricter >=36 floor.
    if all_null and stats["floor36_ok"]:
        return ("COMMUTATIVE-NULL-CERTIFIED", "all four CIs include 0.5 (non-degenerate) "
                f"and >= {N_FLOOR_NULL} gated in-pair parsed trials per direction")
    # 6. The NAMED GAP SUB-LABEL (critic blocker 1): guard holds, out-of-pair <= 0.5,
    #    all four CIs include 0.5 (non-degenerate), but the >=36 certification floor is
    #    unmet — no clause fires.
    if all_null:
        return ("INCONCLUSIVE — null pattern, certification floor unmet",
                "guard holds, out-of-pair <= 0.5, all four CIs include 0.5 "
                f"(non-degenerate), but < {N_FLOOR_NULL} gated in-pair parsed trials in "
                "some direction — the absence claim may not be certified on this n")
    # 7. FINAL ELSE — INCONCLUSIVE-MIXED, exhaustively everything not caught above.
    if (chron_pattern or phys_pattern) and not stats["floor24_ok"]:
        return ("INCONCLUSIVE-MIXED", "a both-directions CI pattern is present but "
                f"< {N_FLOOR_EFFECT} gated in-pair parsed trials in some direction — "
                "no effect clause may fire; point estimates only")
    return ("INCONCLUSIVE-MIXED", "arms disagree (one CI-clean, the other not, opposite "
            "sides, or a degenerate CI) — point estimates only, no substantive label")


# ---------- reporting ----------------------------------------------------------------
def fmt(v):
    return "NA" if v is None else f"{v:.3f}"


def fmt_ci(ci):
    if ci is None:
        return "CI[--,--]"
    tag = " DEGEN" if ci["degenerate"] else ""
    return f"CI[{fmt(ci['lo'])},{fmt(ci['hi'])}]{tag}"


def print_stats(stats, indent="  "):
    print(f"{indent}{stats['label']}: mixed={stats['n_mixed']} parsed={stats['n_parsed']} "
          f"NA={stats['n_na']} oop={stats['oop']:.3f} guard_ok={stats['guard_ok']} "
          f"floor24_ok={stats['floor24_ok']} floor36_ok={stats['floor36_ok']}")
    for d in DIRS:
        r = stats["dirs"][d]
        print(f"{indent}  {d}: rho_chron={fmt(r['rho_chron'])} {fmt_ci(r['ci_chron'])} "
              f"rho_phys={fmt(r['rho_phys'])} {fmt_ci(r['ci_phys'])} "
              f"(in-pair n={r['n_in_pair']}, gated clusters={r['n_gated_clusters']}, "
              f"ungated rho_chron={fmt(r['rho_chron_ungated'])})")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw-dir", default=os.path.join(HERE, "raw"))
    args = ap.parse_args()
    report = {}
    for m in MODELS:
        path = os.path.join(args.raw_dir, f"probe-{m}.jsonl")
        recs = read_jsonl(path)
        if not recs:
            print(f"[{m}] no records at {path} — skipped")
            continue
        mixed = [r for r in recs if r["kind"] == "mixed"]
        cons = [r for r in recs if r["kind"] == "consistent"]

        # manipulation gate: ALL FOUR consistent controls correct (2 twins x 2
        # directions, critic S1), per (pair, sample) cluster
        gate_ok, by_cluster = {}, {}
        for r in cons:
            by_cluster.setdefault((r["pair"], r["sample"]), []).append(r)
        for k, cl in sorted(by_cluster.items()):
            gate_ok[k] = all(c.get("correct") for c in cl)
        gacc = sum(1 for r in cons if r.get("correct")) / len(cons) if cons else 0.0
        n_pass = sum(gate_ok.values())

        strict_rate = sum(1 for r in recs if r.get("parse_mode") == "strict") / len(recs)
        retried = sum(1 for r in recs if r.get("retried"))

        # NA concentration flag: > 25% NA in any pair x direction cell (the v2 pathology)
        na_flags = []
        for p in sorted({r["pair"] for r in mixed}):
            for d in DIRS:
                cell = [r for r in mixed if r["pair"] == p and r["direction"] == d]
                if cell:
                    f = sum(1 for r in cell if r.get("pick_cid") is None) / len(cell)
                    if f > 0.25:
                        na_flags.append({"pair": p, "direction": d, "na_rate": f})

        print(f"\n[{m}] mixed={len(mixed)} consistent={len(cons)} "
              f"strict-compliance={strict_rate:.3f} retried={retried}")
        print(f"  GATE: control acc={gacc:.2f}; clusters passing both-twin gate: "
              f"{n_pass}/{len(gate_ok)} {sorted(k for k, v in gate_ok.items() if v)}")
        if na_flags:
            print(f"  NA-CONCENTRATION FLAG (>25% in a pair x direction cell): {na_flags}")

        primary = compute(mixed, gate_ok, "PRIMARY")
        print_stats(primary)
        v, why = verdict(primary)
        print(f"  VERDICT: {v} — {why}")
        for nm, sec in primary["secondary"].items():
            print(f"  SECONDARY {nm}: rho_chron={fmt(sec['rho_chron'])} (n={sec['n']})")

        # ---- pre-registered sensitivity cuts — DESCRIPTIVE ONLY, never verdict-bearing
        # (critic S5: the verdict above is computed on the primary gated pool only;
        # "verdict-under-cut" is a descriptive robustness readout, not a verdict) ----
        cuts = {}
        cut_views = [("strict-only",
                      [r for r in mixed if r.get("parse_mode") == "strict"], False),
                     ("NAs-as-out-of-pair", mixed, True)]
        for p in sorted({r["pair"] for r in mixed}):
            cut_views.append((f"leave-out-pair-{p}",
                              [r for r in mixed if r["pair"] != p], False))
        for label, view, na_oop in cut_views:
            st = compute(view, gate_ok, label, na_as_oop=na_oop)
            cv, cwhy = verdict(st)
            st["verdict_descriptive_only"] = cv
            cuts[label] = st
            print_stats(st, indent="  CUT ")
            print(f"  CUT {label}: verdict-under-cut (descriptive only, never "
                  f"verdict-bearing) = {cv}")
        # pair-level (3-cluster) bootstrap — descriptive cross-check only, NO verdict
        pl = compute(mixed, gate_ok, "pair-level-bootstrap (descriptive only)",
                     cluster_of=lambda r: r["pair"])
        print_stats(pl, indent="  XCHK ")
        cuts["pair-level-bootstrap"] = pl

        report[m] = {"gate": {"control_acc": gacc, "n_pass": n_pass,
                              "clusters": {f"{k[0]}:{k[1]}": v
                                           for k, v in sorted(gate_ok.items())}},
                     "strict_compliance": strict_rate, "retried": retried,
                     "na_concentration_flags": na_flags,
                     "primary": primary, "verdict": v, "verdict_reason": why,
                     "sensitivity_cuts": cuts}
    out_path = os.path.join(args.raw_dir, "analysis.json")
    json.dump(report, open(out_path, "w"), indent=2, default=str)
    print(f"\nanalysis.json written to {out_path}")


if __name__ == "__main__":
    main()
