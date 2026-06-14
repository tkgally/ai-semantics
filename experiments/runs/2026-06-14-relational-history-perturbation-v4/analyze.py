#!/usr/bin/env python3
"""analyze.py — pre-registered analysis for the history-perturbation probe v4.

Implements EXACTLY the design's frozen measures and decision rule
(experiments/designs/relational-history-perturbation-v4.md §"The exact contrast" /
§"Frozen analysis plan"); the verdict mapper is CODE (verdict() below), an ordered,
exhaustive if/else tree with an explicit final else, so it cannot be retuned silently.

The v4 headline pair, both centered at 0.5 over gated, parsed, in-pair mixed trials:
- **Delta_chron = rho(pick = chronologically-latest twin) - 0.5** — the CLAST twin (the
  twin owning the two latest round stamps R3,R4). A chronology/stamp reader -> Delta_chron
  CI-clean off 0.5; a content-only reader -> CI includes 0.5.
- **Delta_pos = rho(pick = physically-last-line twin) - 0.5** — the twin whose description
  is the last LINE of the rendered record. A text-position reader -> Delta_pos CI-clean off
  0.5 while Delta_chron is null; this is the diagnostic v3 could only get by reversing the
  whole record, obtained here WITHIN one arm.

Because CLAST and the physically-last twin are crossed orthogonally (asserted at build),
the JOINT reading of (Delta_chron, Delta_pos) separates the three readers cleanly:
  (chron clean, pos null) -> chronology-tracking (non-commutative; conjecture FALSIFIED);
  (pos clean, chron null) -> TEXT-POSITION ARTIFACT (methodological; says nothing relational);
  (both null)             -> COMMUTATIVE-NULL (conjecture's bet, strengthened);
  (both clean) / disagree -> INCONCLUSIVE/MIXED.

The v4-specific STAMP-RESPECT control gates the Delta_chron reading: a model that cannot
decode a single-twin record whose stamps are non-monotonic vs text order is stamp-blind ->
METHODOLOGICAL NULL on the chronology question (its picks reduce to text-position).

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
from common import read_jsonl, MODELS as PANEL_MODELS  # noqa: E402

MODELS = tuple(PANEL_MODELS)          # ("claude", "gemini")
N_BOOT = 10000
SEED = 20260614
K_GUARD = 3                # >= k gated clusters (design guard)
N_FLOOR_NULL = 36          # >= 36 gated in-pair parsed trials per (clast x dpos) cell for null-cert
N_FLOOR_EFFECT = 24        # >= 24 for the FALSIFIED / TEXT-POSITION-ARTIFACT clauses
OOP_MAX = 0.5
STAMP_RESPECT_MIN = 0.75   # model-level stamp-respect accuracy floor; below -> stamp-blind
CELLS = [("X", "late"), ("X", "early"), ("Y", "late"), ("Y", "early")]


def rate(trials, key):
    inp = [r for r in trials if r.get("in_pair")]
    if not inp:
        return None, 0
    return sum(1 for r in inp if r[key]) / len(inp), len(inp)


def cluster_boot(trials, key, cluster_of, seed_label):
    """Percentile 95% CI from N_BOOT cluster resamples. Verbatim machinery from v3."""
    agg = {}
    for r in trials:
        if r.get("in_pair"):
            a = agg.setdefault(cluster_of(r), [0, 0])
            a[0] += 1 if r[key] else 0
            a[1] += 1
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
    degenerate = (lo == hi)
    side = None if degenerate else (1 if lo > 0.5 else (-1 if hi < 0.5 else 0))
    return {"lo": lo, "hi": hi, "degenerate": degenerate, "side": side,
            "n_clusters": len(keys)}


def compute(mixed, gate_ok, label, na_as_oop=False,
            cluster_of=lambda r: (r["pair"], r["sample"])):
    """All pre-registered quantities for one view of one model's mixed trials."""
    parsed = [r for r in mixed if r.get("pick_cid") is not None]
    nas = [r for r in mixed if r.get("pick_cid") is None]
    if na_as_oop:
        parsed = parsed + [{**r, "in_pair": False, "picked_chron_last": None,
                            "picked_phys_last": None} for r in nas]
        nas = []
    n_oop = sum(1 for r in parsed if not r.get("in_pair"))
    oop = (n_oop / len(parsed)) if parsed else 1.0
    gated = [r for r in parsed if gate_ok.get((r["pair"], r["sample"]))]
    inp = [r for r in gated if r.get("in_pair")]
    out = {"label": label, "n_mixed": len(mixed), "n_parsed": len(parsed),
           "n_na": len(nas), "oop": oop,
           "n_in_pair": len(inp),
           "n_gated_clusters": len({cluster_of(r) for r in inp})}
    for nm, key in (("chron", "picked_chron_last"), ("pos", "picked_phys_last")):
        v, _ = rate(gated, key)
        out[f"rho_{nm}"] = v
        out[f"delta_{nm}"] = (None if v is None else v - 0.5)
        out[f"ci_{nm}"] = cluster_boot(gated, key, cluster_of, f"{label}:{nm}")
    # per (clast x dpos) cell counts (the floor is checked on the MIN cell)
    cell_n = {}
    for clast, dpos in CELLS:
        cell = [r for r in inp if r["clast"] == clast and r["dpos"] == dpos]
        cell_n[f"{clast}:{dpos}"] = len(cell)
    out["cell_n_in_pair"] = cell_n
    out["min_cell_n"] = min(cell_n.values()) if cell_n else 0
    # descriptive: Delta_chron and Delta_pos at each level of the other factor
    out["by_dpos"] = {}
    for dpos in ("late", "early"):
        dd = [r for r in gated if r["dpos"] == dpos]
        rc, _ = rate(dd, "picked_chron_last")
        rp, _ = rate(dd, "picked_phys_last")
        out["by_dpos"][dpos] = {"rho_chron": rc, "rho_pos": rp,
                                "n": len([r for r in dd if r.get("in_pair")])}
    out["guard_ok"] = out["n_gated_clusters"] >= K_GUARD
    out["floor24_ok"] = out["min_cell_n"] >= N_FLOOR_EFFECT
    out["floor36_ok"] = out["min_cell_n"] >= N_FLOOR_NULL
    return out


def verdict(stats, stamp_respect_acc):
    """THE pre-registered verdict mapper (design §"Frozen analysis plan" verdict map) —
    mechanical, ORDERED, EXHAUSTIVE, explicit final else. Precedence:
    METHODOLOGICAL NULL > UNDER-POWERED > FALSIFIED > TEXT-POSITION ARTIFACT >
    COMMUTATIVE-NULL-CERTIFIED > named-gap sub-label > INCONCLUSIVE/MIXED.
    Degenerate (zero-width) CIs satisfy no clause."""
    # 1. METHODOLOGICAL NULL — stamp-blind, or the >=k-cluster guard fails.
    if stamp_respect_acc is not None and stamp_respect_acc < STAMP_RESPECT_MIN:
        return ("METHODOLOGICAL NULL", f"stamp-blind: stamp-respect control accuracy "
                f"{stamp_respect_acc:.2f} < {STAMP_RESPECT_MIN} — the model cannot decode "
                "a single-twin record with non-monotonic stamps, so its mixed picks reduce "
                "to text-position and no Delta_chron reading is licensed")
    if not stats["guard_ok"]:
        return ("METHODOLOGICAL NULL", f"< {K_GUARD} gated clusters with in-pair data "
                "(whatever the point estimates say)")
    # 2. UNDER-POWERED.
    if stats["oop"] > OOP_MAX:
        return ("UNDER-POWERED", f"out-of-pair {stats['oop']:.3f} > {OOP_MAX} on parsed picks")
    cc = stats["ci_chron"]
    cp = stats["ci_pos"]
    chron_clean = cc is not None and cc["side"] in (1, -1)
    pos_clean = cp is not None and cp["side"] in (1, -1)
    chron_null = cc is not None and cc["side"] == 0
    pos_null = cp is not None and cp["side"] == 0
    # 3. FALSIFIED — chronology clean, position null, >=24 floor.
    if chron_clean and pos_null and stats["floor24_ok"]:
        d = "RECENCY" if cc["side"] > 0 else "PRIMACY"
        return ("FALSIFIED", f"non-commutative, chronology-tracking ({d}): Delta_chron CI "
                "excludes 0.5 while Delta_pos CI includes 0.5, with "
                f">= {N_FLOOR_EFFECT} gated in-pair parsed trials in every (clast x dpos) cell")
    # 4. TEXT-POSITION ARTIFACT — position clean, chronology null, >=24 floor.
    if pos_clean and chron_null and stats["floor24_ok"]:
        d = "last-line" if cp["side"] > 0 else "first-line"
        return ("TEXT-POSITION ARTIFACT", f"Delta_pos CI excludes 0.5 ({d}-following) while "
                "Delta_chron CI includes 0.5, with "
                f">= {N_FLOOR_EFFECT} gated in-pair parsed trials in every cell — a "
                "methodological finding about prompt geometry / stamp neglect; says nothing "
                "relational")
    # 5. COMMUTATIVE-NULL-CERTIFIED — both null, >=36 floor.
    if chron_null and pos_null and stats["floor36_ok"]:
        return ("COMMUTATIVE-NULL-CERTIFIED", "both Delta_chron and Delta_pos CIs include "
                f"0.5 (non-degenerate) with >= {N_FLOOR_NULL} gated in-pair parsed trials "
                "in every cell — neither stamped chronology nor text position moves the pick")
    # 6. Named gap — both null but the >=36 floor unmet.
    if chron_null and pos_null:
        return ("INCONCLUSIVE — null pattern, certification floor unmet",
                "both CIs include 0.5 (non-degenerate) but "
                f"< {N_FLOOR_NULL} gated in-pair parsed trials in some cell — the absence "
                "claim may not be certified on this n")
    # 7. FINAL ELSE — everything else (both clean; one clean one not in a non-paired way;
    #    a clean pattern below the >=24 floor; a degenerate CI).
    if (chron_clean or pos_clean) and not stats["floor24_ok"]:
        return ("INCONCLUSIVE-MIXED", "a CI excludes 0.5 but "
                f"< {N_FLOOR_EFFECT} gated in-pair parsed trials in some cell — no effect "
                "clause may fire; point estimates only")
    if chron_clean and pos_clean:
        return ("INCONCLUSIVE-MIXED", "both Delta_chron and Delta_pos CIs exclude 0.5 — "
                "the two channels are confounded in the picks; point estimates only")
    return ("INCONCLUSIVE-MIXED", "neither a clean single-channel effect nor a certified "
            "null (a degenerate CI or a mixed pattern) — point estimates only")


def fmt(v):
    return "NA" if v is None else f"{v:.3f}"


def fmt_ci(ci):
    if ci is None:
        return "CI[--,--]"
    tag = " DEGEN" if ci["degenerate"] else ""
    return f"CI[{fmt(ci['lo'])},{fmt(ci['hi'])}]{tag}"


def print_stats(stats, indent="  "):
    print(f"{indent}{stats['label']}: mixed={stats['n_mixed']} parsed={stats['n_parsed']} "
          f"NA={stats['n_na']} oop={stats['oop']:.3f} in_pair={stats['n_in_pair']} "
          f"gated_clusters={stats['n_gated_clusters']} min_cell_n={stats['min_cell_n']} "
          f"guard={stats['guard_ok']} floor24={stats['floor24_ok']} "
          f"floor36={stats['floor36_ok']}")
    print(f"{indent}  rho_chron={fmt(stats['rho_chron'])} {fmt_ci(stats['ci_chron'])} | "
          f"rho_pos={fmt(stats['rho_pos'])} {fmt_ci(stats['ci_pos'])}")
    print(f"{indent}  cells={stats['cell_n_in_pair']}")
    print(f"{indent}  by_dpos={ {k: {'chron': fmt(v['rho_chron']), 'pos': fmt(v['rho_pos']), 'n': v['n']} for k, v in stats['by_dpos'].items()} }")


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
        sr = [r for r in recs if r["kind"] == "stamp_respect"]

        # manipulation gate: ALL FOUR controls correct per (pair, sample) cluster
        gate_ok, by_cluster = {}, {}
        for r in cons + sr:
            by_cluster.setdefault((r["pair"], r["sample"]), []).append(r)
        for k, cl in sorted(by_cluster.items()):
            gate_ok[k] = all(c.get("correct") for c in cl)
        gacc = (sum(1 for r in cons + sr if r.get("correct")) / len(cons + sr)
                if (cons + sr) else 0.0)
        sr_acc = (sum(1 for r in sr if r.get("correct")) / len(sr)) if sr else None
        cons_acc = (sum(1 for r in cons if r.get("correct")) / len(cons)) if cons else None
        n_pass = sum(gate_ok.values())

        strict_rate = sum(1 for r in recs if r.get("parse_mode") == "strict") / len(recs)
        retried = sum(1 for r in recs if r.get("retried"))

        # NA concentration flag: > 25% NA in any (clast x dpos) cell
        na_flags = []
        for clast, dpos in CELLS:
            cell = [r for r in mixed if r["clast"] == clast and r["dpos"] == dpos]
            if cell:
                f = sum(1 for r in cell if r.get("pick_cid") is None) / len(cell)
                if f > 0.25:
                    na_flags.append({"cell": f"{clast}:{dpos}", "na_rate": f})

        print(f"\n[{m}] mixed={len(mixed)} consistent={len(cons)} stamp_respect={len(sr)} "
              f"strict-compliance={strict_rate:.3f} retried={retried}")
        print(f"  GATE: control acc={gacc:.2f} (consistent={fmt(cons_acc)}, "
              f"stamp_respect={fmt(sr_acc)}); clusters passing all-4-control gate: "
              f"{n_pass}/{len(gate_ok)} {sorted(k for k, v in gate_ok.items() if v)}")
        if sr_acc is not None and sr_acc < STAMP_RESPECT_MIN:
            print(f"  STAMP-BLIND FLAG: stamp_respect acc {sr_acc:.2f} < {STAMP_RESPECT_MIN} "
                  "-> METHODOLOGICAL NULL on the chronology question")
        if na_flags:
            print(f"  NA-CONCENTRATION FLAG (>25% in a cell): {na_flags}")

        primary = compute(mixed, gate_ok, "PRIMARY")
        print_stats(primary)
        v, why = verdict(primary, sr_acc)
        print(f"  VERDICT: {v} — {why}")

        # ---- pre-registered sensitivity cuts — DESCRIPTIVE ONLY, never verdict-bearing ----
        cuts = {}
        cut_views = [("strict-only",
                      [r for r in mixed if r.get("parse_mode") == "strict"], False),
                     ("NAs-as-out-of-pair", mixed, True),
                     ("late-only", [r for r in mixed if r["dpos"] == "late"], False),
                     ("early-only", [r for r in mixed if r["dpos"] == "early"], False)]
        for p in sorted({r["pair"] for r in mixed}):
            cut_views.append((f"leave-out-pair-{p}",
                              [r for r in mixed if r["pair"] != p], False))
        for label, view, na_oop in cut_views:
            st = compute(view, gate_ok, label, na_as_oop=na_oop)
            cv, cwhy = verdict(st, sr_acc)
            st["verdict_descriptive_only"] = cv
            cuts[label] = st
            print_stats(st, indent="  CUT ")
            print(f"  CUT {label}: verdict-under-cut (descriptive only) = {cv}")
        pl = compute(mixed, gate_ok, "pair-level-bootstrap (descriptive only)",
                     cluster_of=lambda r: r["pair"])
        print_stats(pl, indent="  XCHK ")
        cuts["pair-level-bootstrap"] = pl

        report[m] = {"gate": {"control_acc": gacc, "consistent_acc": cons_acc,
                              "stamp_respect_acc": sr_acc, "n_pass": n_pass,
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
