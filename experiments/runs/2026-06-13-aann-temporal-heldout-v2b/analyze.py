#!/usr/bin/env python3
"""AANN temporal held-out widening (v2b) — analysis. Implements PREREG exactly;
no tunable knobs. Written and committed at freeze time, BEFORE any model call
(PREREG-draft disclosure 5); the post-run verifier recomputes from raw with
independent code.

Outputs results.json + a human-readable summary + a single machine-readable
JSON summary block to stdout.

FROZEN BOUNDARY-INCLUSIVITY DECISIONS (fixed pre-data; see also PREREG
"Thresholds are >=/inclusive"):
  - class-cell rho threshold 0.40 is INCLUSIVE  (rho >= 0.40 counts).
  - adjective-grain rho threshold 0.20 is INCLUSIVE (rho >= 0.20 counts).
  - bootstrap CI lower bound vs 0 is STRICT  (ci_lo > 0; ci_lo == 0.0 does
    NOT replicate -- PREREG says "lower bound > 0").
  - FAILS-TO-REPLICATE CI upper bound vs 0.20 is STRICT (ci_hi < 0.20;
    ci_hi == 0.20 is NOT a fail -- PREREG says "upper bound < 0.20").
  - REPLICATES is evaluated before FAILS; if both branches somehow fire
    (point estimate outside its own percentile CI -- a bootstrap pathology),
    the verdict is STILL-TOO-THIN with a contradiction note, per the PREREG
    catch-all ("grains disagree without CI resolution").
  - missingness > 25% (instrument failure for the stratum) forces that
    model's verdict to STILL-TOO-THIN: unreliable data can neither
    confidently replicate nor confidently exclude the band.
  - NaN rho from degenerate (constant) output counts as 0 and its CI is
    undefined (None) => STILL-TOO-THIN ("undefined CI"), per PREREG. A NaN
    inside a single bootstrap resample likewise counts as 0 (same rule,
    applied per-replicate).

Selftest: python3 analyze.py --selftest  (synthetic in-memory data; no files
written, no model calls).
"""
import argparse
import json
import random
import re
import statistics
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
STIMULI = json.load(open(HERE / "stimuli.json"))
ITEMS = {s["id"]: s for s in STIMULI["items"]}
HUMAN = {c: v["mean"] for c, v in STIMULI["human_temporal_class_means"].items()}
ARM = "heldout-temporal"
EXPECTED_ROWS = 80
BOOT = 10000
SEED = 20260613  # = the stimuli seed; reported in the output (PREREG secondary)

# PREREG frozen verdict-map thresholds (inclusivity frozen in the docstring).
CELL_RHO_MIN = 0.40     # inclusive (>=)
ADJ_RHO_MIN = 0.20      # inclusive (>=)
CI_LOWER_MUST_EXCEED = 0.0    # strict (>)
FAIL_CI_UPPER_BELOW = 0.20    # strict (<)

LATTICE_CAVEAT = ("n=4 class-cells: Spearman lattice is coarse "
                  "({0, +/-0.2, +/-0.4, +/-0.8, +/-1.0}); read only jointly "
                  "with the adjective-grain secondary statistic (PREREG)")

PANEL_NAMES = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini",
               "C": "gemini-3.5-flash"}


# ---------- statistics (verbatim conventions from the v2 analyze.py) ----------

def ranks(xs):
    """Average ranks (tie handling per PREREG)."""
    idx = sorted(range(len(xs)), key=lambda i: xs[i])
    r = [0.0] * len(xs)
    i = 0
    while i < len(xs):
        j = i
        while j + 1 < len(xs) and xs[idx[j + 1]] == xs[idx[i]]:
            j += 1
        avg = (i + j) / 2 + 1
        for k in range(i, j + 1):
            r[idx[k]] = avg
        i = j + 1
    return r


def spearman(x, y):
    rx, ry = ranks(x), ranks(y)
    mx, my = statistics.mean(rx), statistics.mean(ry)
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    dx = sum((a - mx) ** 2 for a in rx) ** 0.5
    dy = sum((b - my) ** 2 for b in ry) ** 0.5
    return num / (dx * dy) if dx and dy else float("nan")


def partial_spearman(x, y, z):
    """Spearman of x,y controlling z via rank residualization (v2 convention)."""
    rx, ry, rz = ranks(x), ranks(y), ranks(z)

    def resid(a, b):
        ma, mb = statistics.mean(a), statistics.mean(b)
        beta = (sum((p - ma) * (q - mb) for p, q in zip(a, b))
                / max(sum((q - mb) ** 2 for q in b), 1e-12))
        return [p - ma - beta * (q - mb) for p, q in zip(a, b)]

    return spearman(resid(rx, rz), resid(ry, rz))


def nan_to_zero(rho):
    """PREREG: NaN rho from constant output counts as 0."""
    return 0.0 if rho != rho else rho


# ---------- loading ----------

def load(slot):
    """Full raw files only (.partial files from an abort are never analyzed,
    v2 critic S2). Returns (rows, status): 'ok' | 'wrong-count' | 'absent'."""
    p = HERE / "raw" / f"{slot}-{ARM}.json"
    if not p.exists():
        return None, "absent"
    rows = json.load(open(p))
    if len(rows) != EXPECTED_ROWS:
        return rows, "wrong-count"
    return rows, "ok"


def miss_gate(rows):
    """PREREG missingness rules: >10% caveat, >25% instrument failure."""
    miss = sum(1 for r in rows if r["value"] is None)
    frac = miss / len(rows) if rows else 1.0
    return miss, ("instrument-failure" if frac > 0.25
                  else "caveat" if frac > 0.10 else "ok")


def read_cost_log():
    """Billed-cost bookkeeping from probe.py's raw/cost-log.txt."""
    p = HERE / "raw" / "cost-log.txt"
    if not p.exists():
        return {"status": "absent", "lines": [], "total_billed_usd": None}
    lines = [ln for ln in p.read_text().splitlines() if ln.strip()]
    total = sum(float(m.group(1)) for ln in lines
                for m in re.finditer(r"billed=\$([0-9.]+)", ln))
    return {"status": "ok", "lines": lines,
            "total_billed_usd": round(total, 4)}


# ---------- per-model analysis ----------

def adjective_means(rows):
    """adj -> (mean of its parsed ratings, adjclass). PREREG: adjective mean =
    mean of that adjective's 2 ratings; an adjective with both items NA is
    dropped (and reported)."""
    vals = defaultdict(list)
    for r in rows:
        if r["value"] is None:
            continue
        it = ITEMS[r["id"]]
        vals[it["adj"]].append(r["value"])
    return {a: statistics.mean(v) for a, v in vals.items()}


def bootstrap_ci(adjs, amean, hmean, seed):
    """10,000-resample percentile bootstrap 95% CI over the adjectives
    (resampling adjectives; PREREG secondary). Seeded; same index convention
    as the v2 analyze.py. NaN replicates count as 0 (frozen rule above)."""
    rng = random.Random(seed)
    n = len(adjs)
    boots = []
    for _ in range(BOOT):
        idx = [rng.randrange(n) for _ in range(n)]
        boots.append(nan_to_zero(spearman([amean[adjs[i]] for i in idx],
                                          [hmean[adjs[i]] for i in idx])))
    boots.sort()
    return (boots[int(0.025 * BOOT) - 1], boots[int(0.975 * BOOT) - 1])


def model_verdict(cell_rho, adj_rho, ci, missingness):
    """PREREG frozen verdict map, mechanical. Boundary inclusivity frozen in
    the module docstring. Returns (verdict, note-or-None)."""
    if missingness == "instrument-failure":
        return "STILL-TOO-THIN", "instrument failure (>25% missing): cannot replicate or confidently fail"
    replicates = (cell_rho >= CELL_RHO_MIN
                  and adj_rho >= ADJ_RHO_MIN
                  and ci is not None and ci[0] > CI_LOWER_MUST_EXCEED)
    fails = ci is not None and ci[1] < FAIL_CI_UPPER_BELOW
    if replicates and fails:
        return "STILL-TOO-THIN", ("contradictory gates (point estimate outside "
                                  "its own percentile CI); per PREREG catch-all")
    if replicates:
        return "REPLICATES", None
    if fails:
        return "FAILS-TO-REPLICATE", None
    return "STILL-TOO-THIN", None


def stratum_verdict(verdicts):
    """PREREG >=2-of-3 rule. verdicts: list of the 3 per-model verdict strings."""
    n_rep = sum(v == "REPLICATES" for v in verdicts)
    n_fail = sum(v == "FAILS-TO-REPLICATE" for v in verdicts)
    if n_rep >= 2 and n_fail == 0:
        return "REPLICATES"
    if n_fail >= 2:
        return "FAILS-TO-REPLICATE"
    return "STILL-TOO-THIN / MIXED"


def carryover_vs_v2(slot, amean_v2b):
    """Descriptive only (no gate): the 16 carryover adjectives' v2b means vs
    their v2 single-item temporal ratings, recomputed from the committed v2
    raw/*-heldout.json. If the v2 artifacts are unreadable, emit the v2b-side
    means and a TODO note instead of fragile guesswork."""
    try:
        v2dir = HERE.parent / "2026-06-12-aann-behavioral-probe-v2"
        v2items = {s["id"]: s
                   for s in json.load(open(v2dir / "stimuli.json"))["held_out"]}
        rows = json.load(open(v2dir / "raw" / f"{slot}-heldout.json"))
        v2vals = defaultdict(list)   # adj -> v2 temporal ratings (1 per adj)
        v2class = {}
        for r in rows:
            it = v2items.get(r["id"])
            if it and it["nounclass"] == "temporal" and r["value"] is not None:
                v2vals[it["adj"]].append(r["value"])
                v2class[it["adj"]] = it["adjclass"]
        v2mean = {a: statistics.mean(v) for a, v in v2vals.items()}
        common = sorted(a for a in v2mean if a in amean_v2b)
        if len(common) < 3:
            raise ValueError(f"only {len(common)} carryover adjectives matched")
        rho = nan_to_zero(spearman([amean_v2b[a] for a in common],
                                   [v2mean[a] for a in common]))
        # v2 temporal-stratum class means (from the 4 carryover adjs per class)
        # vs the v2b carryover-subgroup class means, same adjectives.
        percls_v2, percls_v2b = defaultdict(list), defaultdict(list)
        for a in common:
            percls_v2[v2class[a]].append(v2mean[a])
            percls_v2b[v2class[a]].append(amean_v2b[a])
        return {"n_adjectives": len(common),
                "spearman_v2b_mean_vs_v2_single": round(rho, 4),
                "v2_temporal_class_means": {c: round(statistics.mean(v), 4)
                                            for c, v in sorted(percls_v2.items())},
                "v2b_carryover_class_means": {c: round(statistics.mean(v), 4)
                                              for c, v in sorted(percls_v2b.items())}}
    except Exception as e:  # brittle-format fallback declared in the task
        return {"todo": ("v2 raw recompute skipped (" + repr(e) + "); v2b-side "
                         "carryover means are in new_vs_carryover; post-run "
                         "verifier should recompute v2 side independently"),
                "v2b_carryover_adjective_means": {
                    a: round(m, 4) for a, m in sorted(amean_v2b.items())}}


def analyze_model(slot, rows, status, with_v2_carryover=True):
    """All PREREG statistics for one model. Pure function of (rows, stimuli);
    no file writes (selftest runs it on synthetic rows)."""
    res = {"slot": slot, "model": PANEL_NAMES[slot], "arm_status": status}
    if status != "ok" or not rows:
        return res

    # ---- bookkeeping: n parsed / n NA, arm-level gate, per-cell >5% NA flag
    miss, gate = miss_gate(rows)
    per_cell_n = defaultdict(lambda: [0, 0])   # class -> [n_total, n_missing]
    for r in rows:
        c = ITEMS[r["id"]]["adjclass"]
        per_cell_n[c][0] += 1
        if r["value"] is None:
            per_cell_n[c][1] += 1
    cells_over_5pct = sorted(c for c, (n, m) in per_cell_n.items()
                             if n and m / n > 0.05)
    res["bookkeeping"] = {
        "n_rows": len(rows), "n_parsed": len(rows) - miss, "n_missing": miss,
        "missing_frac": round(miss / len(rows), 4), "missingness": gate,
        "per_cell_na": {c: {"n": n, "missing": m, "na_frac": round(m / n, 4)}
                        for c, (n, m) in sorted(per_cell_n.items())},
        "cells_over_5pct_na": cells_over_5pct,   # report-and-exclude flag
    }

    # ---- PRIMARY: 4 class-cell means vs human anchored class-cell means
    per_class = defaultdict(list)
    for r in rows:
        if r["value"] is None:
            continue
        per_class[ITEMS[r["id"]]["adjclass"]].append(r["value"])
    classes = sorted(c for c in per_class if c in HUMAN)
    cell_means = {c: statistics.mean(per_class[c]) for c in classes}
    cell_rho_raw = spearman([cell_means[c] for c in classes],
                            [HUMAN[c] for c in classes])
    cell_degenerate = cell_rho_raw != cell_rho_raw
    cell_rho = nan_to_zero(cell_rho_raw)
    res["primary"] = {
        "n_class_cells": len(classes),
        "model_class_cell_means": {c: round(cell_means[c], 4) for c in classes},
        "human_class_cell_means": {c: HUMAN[c] for c in classes},
        "class_cell_spearman": round(cell_rho, 4),
        "degenerate": cell_degenerate,
        "lattice_caveat": LATTICE_CAVEAT,
    }

    # ---- SECONDARY: 40 adjective means vs class-assigned human means,
    #      percentile bootstrap over adjectives (seeded)
    amean = adjective_means(rows)
    adjs = sorted(amean)
    adj_class = {}
    adj_zipf = {}
    for s in STIMULI["items"]:
        adj_class[s["adj"]] = s["adjclass"]
        adj_zipf[s["adj"]] = s["zipf"]      # zipf is per-adjective (asserted in prep)
    hmean = {a: HUMAN[adj_class[a]] for a in adjs}
    dropped = sorted(set(adj_class) - set(adjs))
    adj_rho_raw = spearman([amean[a] for a in adjs], [hmean[a] for a in adjs])
    adj_degenerate = adj_rho_raw != adj_rho_raw
    adj_rho = nan_to_zero(adj_rho_raw)
    if adj_degenerate:
        ci = None   # PREREG: degenerate constant output -> CI undefined
    else:
        ci = bootstrap_ci(adjs, amean, hmean, SEED)
    res["secondary"] = {
        "n_adjectives": len(adjs), "adjectives_dropped_all_na": dropped,
        "adjective_spearman": round(adj_rho, 4),
        "degenerate": adj_degenerate,
        "ci95": None if ci is None else [round(ci[0], 4), round(ci[1], 4)],
        "bootstrap_resamples": BOOT, "bootstrap_seed": SEED,
    }

    # ---- VERDICT (mechanical; PREREG frozen map)
    verdict, note = model_verdict(cell_rho, adj_rho, ci, gate)
    res["verdict"] = verdict
    if note:
        res["verdict_note"] = note
    if adj_degenerate or cell_degenerate:
        res["degenerate_output_caveat"] = ("mandatory (constant model output: "
                                           "NaN rho counted as 0, CI undefined)")

    # ---- DESCRIPTIVES (no gates)
    item_pairs = [(r["value"], HUMAN[ITEMS[r["id"]]["adjclass"]])
                  for r in rows if r["value"] is not None]
    pooled = nan_to_zero(spearman([a for a, _ in item_pairs],
                                  [b for _, b in item_pairs]))
    partial = nan_to_zero(partial_spearman([amean[a] for a in adjs],
                                           [hmean[a] for a in adjs],
                                           [adj_zipf[a] for a in adjs]))
    spread = {}
    by_class = defaultdict(list)
    for a in adjs:
        by_class[adj_class[a]].append(amean[a])
    for c, v in sorted(by_class.items()):
        spread[c] = round(statistics.stdev(v), 4) if len(v) > 1 else None
    src = {s["adj"]: s["source"] for s in STIMULI["items"]}
    sub = defaultdict(list)
    subcls = defaultdict(list)
    for a in adjs:
        sub[src[a]].append(amean[a])
        subcls[(src[a], adj_class[a])].append(amean[a])
    res["descriptives"] = {
        "item_spearman_pooled_n": len(item_pairs),
        "item_spearman_pooled": round(pooled, 4),
        "partial_spearman_zipf_adjective_grain": round(partial, 4),
        "per_class_adjective_spread_sd": spread,
        "new_vs_carryover": {
            "new_adjective_mean": round(statistics.mean(sub["new"]), 4)
            if sub.get("new") else None,
            "carryover_adjective_mean": round(statistics.mean(sub["v2-carryover"]), 4)
            if sub.get("v2-carryover") else None,
            "per_class": {f"{s}/{c}": round(statistics.mean(v), 4)
                          for (s, c), v in sorted(subcls.items())},
        },
        "carryover_vs_v2": (carryover_vs_v2(
            slot, {a: amean[a] for a in adjs if src[a] == "v2-carryover"})
            if with_v2_carryover else {"todo": "skipped (selftest)"}),
    }
    return res


# ---------- assembly ----------

def assemble(per_model_results):
    """Global result object incl. stratum verdict. PREREG: arm absent/partial
    => INCOMPLETE, no substantive verdict (matches the v2 analyze.py)."""
    incomplete = [f"{s}:{r['arm_status']}" for s, r in per_model_results.items()
                  if r["arm_status"] != "ok"]
    out = {
        "run": "2026-06-13-aann-temporal-heldout-v2b",
        "arm": ARM,
        "prereg": "PREREG.md (frozen from PREREG-draft.md)",
        "seed": SEED,
        "thresholds": {
            "cell_rho_min_inclusive": CELL_RHO_MIN,
            "adj_rho_min_inclusive": ADJ_RHO_MIN,
            "ci_lower_strictly_above": CI_LOWER_MUST_EXCEED,
            "fail_ci_upper_strictly_below": FAIL_CI_UPPER_BELOW,
        },
        "models": per_model_results,
        "cost": read_cost_log(),
    }
    if incomplete:
        out["stratum_verdict"] = "INCOMPLETE (verdict-bearing arm missing/partial)"
        out["incomplete_arms"] = incomplete
    else:
        out["stratum_verdict"] = stratum_verdict(
            [per_model_results[s]["verdict"] for s in ("A", "B", "C")])
    return out


def report(out):
    print("== AANN temporal held-out widening (v2b) — PREREG analysis ==")
    for s in ("A", "B", "C"):
        r = out["models"].get(s, {})
        if r.get("arm_status") != "ok":
            print(f"  {s} ({PANEL_NAMES[s]}): arm {r.get('arm_status')}")
            continue
        bk, pr, se = r["bookkeeping"], r["primary"], r["secondary"]
        print(f"  {s} ({r['model']}): parsed {bk['n_parsed']}/{bk['n_rows']}"
              f" (NA {bk['n_missing']}, gate {bk['missingness']};"
              f" cells>5%NA {bk['cells_over_5pct_na'] or 'none'})")
        print(f"     primary 4-cell rho = {pr['class_cell_spearman']}"
              f"  [{pr['lattice_caveat']}]")
        print(f"     secondary adjective rho = {se['adjective_spearman']}"
              f" (n={se['n_adjectives']}), 95% CI {se['ci95']}"
              f" (boot {se['bootstrap_resamples']}, seed {se['bootstrap_seed']})")
        print(f"     verdict: {r['verdict']}"
              + (f"  [{r['verdict_note']}]" if r.get("verdict_note") else ""))
    print(f"  STRATUM VERDICT: {out['stratum_verdict']}")
    cost = out["cost"]
    print(f"  billed cost: {cost['total_billed_usd']} ({cost['status']})")
    print("\n=== MACHINE-READABLE JSON SUMMARY ===")
    print(json.dumps(out, indent=1))


def main():
    per_model = {}
    for slot in ("A", "B", "C"):
        rows, status = load(slot)
        per_model[slot] = analyze_model(slot, rows, status)
    out = assemble(per_model)
    json.dump(out, open(HERE / "results.json", "w"), indent=1)
    report(out)


# ---------- selftest (synthetic, in-memory, no files written, no calls) ----------

def _synthetic_rows(level_by_class, jitter_seed=None, constant=None,
                    na_ids=()):
    """Build 80 synthetic raw rows from the frozen stimuli."""
    rng = random.Random(jitter_seed)
    rows = []
    for s in STIMULI["items"]:
        if s["id"] in na_ids:
            v = None
        elif constant is not None:
            v = constant
        else:
            v = level_by_class[s["adjclass"]] + rng.randrange(-2, 3)
        rows.append({"id": s["id"], "arm": ARM, "raw": str(v), "value": v,
                     "usage": None, "error": None})
    return rows


def selftest():
    failures = []
    n_checks = [0]

    def check(name, cond):
        n_checks[0] += 1
        print(("PASS " if cond else "FAIL ") + name)
        if not cond:
            failures.append(name)

    # ---- 1. verdict-mapper edge cases (boundary inclusivity frozen above)
    v = lambda *a: model_verdict(*a)[0]
    check("cell rho exactly 0.40 is inclusive (REPLICATES)",
          v(0.40, 0.50, (0.10, 0.80), "ok") == "REPLICATES")
    check("cell rho just below 0.40 -> STILL-TOO-THIN",
          v(0.3999, 0.90, (0.50, 1.0), "ok") == "STILL-TOO-THIN")
    check("adjective rho exactly 0.20 is inclusive (REPLICATES)",
          v(0.80, 0.20, (0.01, 0.40), "ok") == "REPLICATES")
    check("CI lower exactly 0 does NOT replicate (strict >)",
          v(0.80, 0.50, (0.0, 0.80), "ok") == "STILL-TOO-THIN")
    check("CI upper exactly 0.20 is NOT a fail (strict <)",
          v(0.0, 0.05, (-0.30, 0.20), "ok") == "STILL-TOO-THIN")
    check("CI upper just below 0.20 -> FAILS-TO-REPLICATE",
          v(0.0, 0.05, (-0.30, 0.1999), "ok") == "FAILS-TO-REPLICATE")
    check("undefined CI (degenerate) -> STILL-TOO-THIN",
          v(0.0, 0.0, None, "ok") == "STILL-TOO-THIN")
    check("instrument failure forces STILL-TOO-THIN",
          v(1.0, 1.0, (0.90, 1.0), "instrument-failure") == "STILL-TOO-THIN")
    check("contradictory gates -> STILL-TOO-THIN",
          v(0.80, 0.25, (0.01, 0.19), "ok") == "STILL-TOO-THIN")
    # ---- stratum rule
    check("stratum 2R+1T -> REPLICATES",
          stratum_verdict(["REPLICATES", "REPLICATES", "STILL-TOO-THIN"])
          == "REPLICATES")
    check("stratum 2R+1F -> MIXED (none-fails clause)",
          stratum_verdict(["REPLICATES", "REPLICATES", "FAILS-TO-REPLICATE"])
          == "STILL-TOO-THIN / MIXED")
    check("stratum 2F+1R -> FAILS-TO-REPLICATE",
          stratum_verdict(["FAILS-TO-REPLICATE", "FAILS-TO-REPLICATE",
                           "REPLICATES"]) == "FAILS-TO-REPLICATE")
    check("stratum 1R+2T -> MIXED",
          stratum_verdict(["REPLICATES", "STILL-TOO-THIN", "STILL-TOO-THIN"])
          == "STILL-TOO-THIN / MIXED")

    # ---- 2. full pipeline on synthetic data
    # A: class levels in the human anchored order (quant>ambig>pos>neg),
    #    well separated -> REPLICATES; 2 NAs in the neg cell exercise the
    #    report-and-exclude path and the per-cell >5% NA flag.
    neg_ids = [s["id"] for s in STIMULI["items"] if s["adjclass"] == "neg"][:2]
    rows_a = _synthetic_rows({"quant": 90, "ambig": 80, "pos": 70, "neg": 60},
                             jitter_seed=1, na_ids=neg_ids)
    # B: reversed order -> strongly negative adjective rho -> FAILS.
    rows_b = _synthetic_rows({"quant": 60, "ambig": 70, "pos": 80, "neg": 90},
                             jitter_seed=2)
    # C: constant output -> degenerate -> STILL-TOO-THIN.
    rows_c = _synthetic_rows(None, constant=50)
    per_model = {
        "A": analyze_model("A", rows_a, "ok", with_v2_carryover=False),
        "B": analyze_model("B", rows_b, "ok", with_v2_carryover=False),
        "C": analyze_model("C", rows_c, "ok", with_v2_carryover=False),
    }
    out = assemble(per_model)
    ra, rb, rc = per_model["A"], per_model["B"], per_model["C"]
    check("A replicates on order-preserving synthetic data",
          ra["verdict"] == "REPLICATES")
    check("A primary 4-cell rho == 1.0",
          ra["primary"]["class_cell_spearman"] == 1.0)
    check("A NA bookkeeping: 2 missing, gate ok",
          ra["bookkeeping"]["n_missing"] == 2
          and ra["bookkeeping"]["missingness"] == "ok")
    check("A per-cell >5% NA flag fires for neg (2/20 = 10%)",
          ra["bookkeeping"]["cells_over_5pct_na"] == ["neg"])
    check("B fails-to-replicate on reversed synthetic data",
          rb["verdict"] == "FAILS-TO-REPLICATE")
    check("B primary 4-cell rho == -1.0",
          rb["primary"]["class_cell_spearman"] == -1.0)
    check("C degenerate: rho 0, CI undefined, STILL-TOO-THIN",
          rc["verdict"] == "STILL-TOO-THIN"
          and rc["secondary"]["adjective_spearman"] == 0.0
          and rc["secondary"]["ci95"] is None
          and rc["secondary"]["degenerate"])
    check("stratum verdict on R/F/T is MIXED",
          out["stratum_verdict"] == "STILL-TOO-THIN / MIXED")
    check("all 40 adjectives present for B",
          rb["secondary"]["n_adjectives"] == 40)
    # ---- bootstrap determinism (seeded)
    amean = adjective_means(rows_b)
    adj_class = {s["adj"]: s["adjclass"] for s in STIMULI["items"]}
    adjs = sorted(amean)
    hmean = {a: HUMAN[adj_class[a]] for a in adjs}
    ci1 = bootstrap_ci(adjs, amean, hmean, SEED)
    ci2 = bootstrap_ci(adjs, amean, hmean, SEED)
    check("bootstrap CI is deterministic under the frozen seed", ci1 == ci2)
    check("B CI matches direct recompute",
          [round(ci1[0], 4), round(ci1[1], 4)] == rb["secondary"]["ci95"])
    # ---- INCOMPLETE path
    out_inc = assemble({"A": {"slot": "A", "model": PANEL_NAMES["A"],
                              "arm_status": "absent"},
                        "B": rb, "C": rc})
    check("absent arm -> INCOMPLETE, no substantive verdict",
          out_inc["stratum_verdict"].startswith("INCOMPLETE"))
    # ---- JSON summary serializes
    check("summary JSON-serializable", bool(json.dumps(out)))

    if failures:
        raise SystemExit(f"SELFTEST FAILED: {failures}")
    print(f"SELFTEST OK ({n_checks[0]} checks)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true",
                    help="run the synthetic in-memory pipeline test (no files "
                         "written, no model calls)")
    args = ap.parse_args()
    if args.selftest:
        selftest()
    else:
        main()
