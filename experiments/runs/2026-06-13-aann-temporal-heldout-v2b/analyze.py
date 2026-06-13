#!/usr/bin/env python3
"""AANN temporal held-out widening (v2b) — analysis. Implements PREREG exactly;
no tunable knobs. Written and committed at freeze time, BEFORE any model call
(probe.py refuses to run if this file is absent — pre-run critic blocker 4);
the post-run verifier recomputes from raw with independent code.

Outputs results.json + a human-readable summary + a single machine-readable
JSON summary block to stdout.

THREE ARMS (pre-run critic 2026-06-13, GO after fixes):
  heldout-temporal (80 items)  — gate-bearing gradient read (primary + secondary)
  tier0 (24 pairs, fresh)      — gate-bearing instrument check, >= 20/24 per
                                 model; failure = instrument failure for that
                                 model -> EXCLUDED from the >=2-of-3 stratum
                                 count (its gradient verdict reported
                                 descriptively, never counted)
  robustness (40-item 4-point) — CAVEAT-bearing only, never gate-bearing:
                                 item-level Spearman 0-100 vs 4-point on the
                                 fixed subsample; rho < 0.50 or NaN => mandatory
                                 instrument-fragility caveat (v2 semantics)

FROZEN BOUNDARY-INCLUSIVITY DECISIONS (fixed pre-data; see also PREREG
"Thresholds are >=/inclusive"):
  - class-cell rho threshold 0.40 is INCLUSIVE  (rho >= 0.40 counts).
  - adjective-grain rho threshold 0.20 is INCLUSIVE (rho >= 0.20 counts).
  - bootstrap CI lower bound vs 0 is STRICT  (ci_lo > 0; ci_lo == 0.0 does
    NOT replicate -- PREREG says "lower bound > 0").
  - FAILS-TO-REPLICATE CI upper bound vs 0.20 is STRICT (ci_hi < 0.20;
    ci_hi == 0.20 is NOT a fail -- PREREG says "upper bound < 0.20").
  - Tier-0 pass >= 20/24 is INCLUSIVE (20 passes; 19 fails). A missing
    (unparseable-after-retry) Tier-0 response cannot match and so counts
    against the pass total.
  - framing-fragility threshold is rho < 0.50 STRICT (rho == 0.50 is NOT
    fragile; NaN from degenerate constant output IS fragile) — v2 semantics.
  - VERDICT PRECEDENCE: REPLICATES is evaluated before FAILS; if both
    branches somehow fire (point estimate outside its own percentile CI --
    a bootstrap pathology), the verdict is STILL-TOO-THIN with a
    contradiction note, per the PREREG catch-all.
  - missingness > 25% on the main arm (instrument failure for the stratum)
    forces that model's verdict to STILL-TOO-THIN.
  - NaN rho from degenerate (constant) output counts as 0 and its CI is
    undefined (None) => STILL-TOO-THIN ("undefined CI"), per PREREG. A NaN
    inside a single bootstrap resample likewise COUNTS AS 0 (zeroed, not
    dropped — same rule applied per-replicate); this NaN-counts-as-0 rule
    applies to GATE statistics too, not only descriptives.
  - TOURISH SENSITIVITY (pre-declared descriptive): the adjective-grain and
    class-cell statistics are recomputed excluding template-2 items (the
    upstream "The tourish stayed ..." typo template); THE GATE STAYS ON ALL
    80 ITEMS; if the verdict category would differ under the exclusion, a
    mandatory caveat sentence attaches to the result. The sensitivity verdict
    reuses the all-80 missingness gate and the same bootstrap seed.

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
TIER0 = {s["id"]: s for s in STIMULI["tier0"]}
SUBSET_IDS = set(STIMULI["robustness_4pt"]["ids"])
EXPECTED_ROWS = {"heldout-temporal": 80, "tier0": 24, "robustness": 40}
BOOT = 10000
SEED = 20260613  # bootstrap seed (= the stimuli seed), declared in the PREREG
TOURISH_TPL = 2  # the upstream-typo template ("The tourish stayed ...")

# PREREG frozen verdict-map thresholds (inclusivity frozen in the docstring).
CELL_RHO_MIN = 0.40     # inclusive (>=)
ADJ_RHO_MIN = 0.20      # inclusive (>=)
CI_LOWER_MUST_EXCEED = 0.0    # strict (>)
FAIL_CI_UPPER_BELOW = 0.20    # strict (<)
TIER0_MIN = 20                # inclusive (>=), of 24
FRAGILITY_RHO_BELOW = 0.50    # strict (<); NaN counts as fragile (v2 semantics)

LATTICE_CAVEAT = ("n=4 class-cells: Spearman lattice is coarse "
                  "({0, +/-0.2, +/-0.4, +/-0.6, +/-0.8, +/-1.0}); read only "
                  "jointly with the adjective-grain secondary statistic (PREREG)")

NOUN_ASYMMETRY_NOTE = (
    "subgroup reads are confounded with item surface: the frozen rotation "
    "gives new adjectives more days/hours items (12/12/8/8/8 over "
    "days/hours/months/weeks/years) and carryovers more months/weeks/years "
    "(4/4/8/8/8), so new-vs-carryover differences are not interpretable as "
    "adjective-set effects alone")

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
    if len(x) < 2:
        return float("nan")
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
    """PREREG: NaN rho from constant output counts as 0 (gate statistics too)."""
    return 0.0 if rho != rho else rho


def framing_fragility_flag(rho):
    """v2 semantics, verbatim: fragile iff rho is NaN (degenerate constant
    output) or rho < 0.50 (strict: 0.50 exactly is NOT fragile)."""
    return bool(rho != rho or rho < FRAGILITY_RHO_BELOW)


# ---------- loading ----------

def load(slot, arm):
    """Full raw files only (.partial files from an abort are never analyzed,
    v2 critic S2). Returns (rows, status): 'ok' | 'wrong-count' | 'absent'."""
    p = HERE / "raw" / f"{slot}-{arm}.json"
    if not p.exists():
        return None, "absent"
    rows = json.load(open(p))
    if len(rows) != EXPECTED_ROWS[arm]:
        return rows, "wrong-count"
    return rows, "ok"


def miss_gate(rows):
    """PREREG missingness rules: >10% caveat, >25% instrument failure."""
    miss = sum(1 for r in rows if r["value"] is None)
    frac = miss / len(rows) if rows else 1.0
    return miss, ("instrument-failure" if frac > 0.25
                  else "caveat" if frac > 0.10 else "ok")


def read_cost_log():
    """Billed-cost bookkeeping from probe.py's raw/cost-log.txt, including the
    missing-cost call count probe.py now logs (critic should-fix 8)."""
    p = HERE / "raw" / "cost-log.txt"
    if not p.exists():
        return {"status": "absent", "lines": [], "total_billed_usd": None}
    lines = [ln for ln in p.read_text().splitlines() if ln.strip()]
    total = sum(float(m.group(1)) for ln in lines
                for m in re.finditer(r"billed=\$([0-9.]+)", ln))
    miss = sum(int(m.group(1)) for ln in lines
               for m in re.finditer(r"missing_cost_calls=(\d+)", ln))
    out = {"status": "ok", "lines": lines, "total_billed_usd": round(total, 4),
           "missing_cost_calls": miss}
    if miss:
        out["missing_cost_caveat"] = (f"{miss} call(s) reported no usage.cost; "
                                      "the billed total UNDERCOUNTS")
    return out


# ---------- per-model analysis ----------

def adjective_means(rows):
    """adj -> mean of its parsed ratings. PREREG missing-value handling:
    means are over AVAILABLE ratings (1 rating if the other is missing); an
    adjective with both items missing is DROPPED and counted/reported."""
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
    as the v2 analyze.py. A NaN inside a single resample (degenerate resample,
    e.g. all-tied draw) COUNTS AS 0 — zeroed, not dropped (frozen rule)."""
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
    the module docstring. PRECEDENCE: REPLICATES evaluated before FAILS;
    contradiction -> STILL-TOO-THIN with note. Returns (verdict, note|None)."""
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
    """PREREG >=2 rule over the COUNTED (Tier-0-passing) models. verdicts:
    the counted models' verdict strings."""
    n_rep = sum(v == "REPLICATES" for v in verdicts)
    n_fail = sum(v == "FAILS-TO-REPLICATE" for v in verdicts)
    if n_rep >= 2 and n_fail == 0:
        return "REPLICATES"
    if n_fail >= 2:
        return "FAILS-TO-REPLICATE"
    return "STILL-TOO-THIN / MIXED"


def gradient_stats(rows):
    """Primary (class-cell) + secondary (adjective-grain) statistics over a
    set of parsed rows. Used for the all-80 gate read AND the pre-declared
    tourish (template-2-excluded) sensitivity recompute (same code path, same
    bootstrap seed). Returns a dict of raw pieces."""
    per_class = defaultdict(list)
    for r in rows:
        if r["value"] is None:
            continue
        per_class[ITEMS[r["id"]]["adjclass"]].append(r["value"])
    classes = sorted(c for c in per_class if c in HUMAN)
    cell_means = {c: statistics.mean(per_class[c]) for c in classes}
    cell_rho_raw = (spearman([cell_means[c] for c in classes],
                             [HUMAN[c] for c in classes])
                    if len(classes) >= 2 else float("nan"))
    amean = adjective_means(rows)
    adjs = sorted(amean)
    adj_class = {s["adj"]: s["adjclass"] for s in STIMULI["items"]}
    hmean = {a: HUMAN[adj_class[a]] for a in adjs}
    adj_rho_raw = (spearman([amean[a] for a in adjs], [hmean[a] for a in adjs])
                   if len(adjs) >= 2 else float("nan"))
    adj_degenerate = adj_rho_raw != adj_rho_raw
    ci = None if adj_degenerate else bootstrap_ci(adjs, amean, hmean, SEED)
    return {"classes": classes, "cell_means": cell_means,
            "cell_rho_raw": cell_rho_raw,
            "cell_degenerate": cell_rho_raw != cell_rho_raw,
            "cell_rho": nan_to_zero(cell_rho_raw),
            "amean": amean, "adjs": adjs, "hmean": hmean,
            "adj_rho": nan_to_zero(adj_rho_raw),
            "adj_degenerate": adj_degenerate, "ci": ci,
            "dropped": sorted(set(adj_class) - set(adjs))}


def carryover_vs_v2(slot, amean_v2b):
    """Descriptive only (no gate): CARRYOVER CONSISTENCY — the 16 carryover
    adjectives' v2b means vs their v2 single-item temporal ratings (from the
    committed v2 raw/*-heldout.json). Statistic (named in the PREREG):
    Spearman + mean signed difference (v2b minus v2). This is a CONSISTENCY
    number, not test-retest: v2 rated 1 item per adjective, v2b averages 2
    different items. If the v2 artifacts are unreadable, emit the v2b-side
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
        msd = statistics.mean(amean_v2b[a] - v2mean[a] for a in common)
        # v2 temporal-stratum class means (from the 4 carryover adjs per class)
        # vs the v2b carryover-subgroup class means, same adjectives.
        percls_v2, percls_v2b = defaultdict(list), defaultdict(list)
        for a in common:
            percls_v2[v2class[a]].append(v2mean[a])
            percls_v2b[v2class[a]].append(amean_v2b[a])
        return {"statistic": ("consistency (Spearman + mean signed difference, "
                              "v2b minus v2), not test-retest: v2 rated 1 item "
                              "per adjective, v2b averages 2 different items"),
                "n_adjectives": len(common),
                "spearman_v2b_mean_vs_v2_single": round(rho, 4),
                "mean_signed_diff_v2b_minus_v2": round(msd, 4),
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


def analyze_tier0(rows, status):
    """Fresh Tier-0 instrument check (critic blocker 1). GATE on the
    last-standalone-token parse (rows' 'value'); the v2-style first-token
    parse ('value_first_token') is reported DESCRIPTIVELY for continuity.
    Pass >= 20/24 (inclusive); failure = instrument failure for the model
    (excluded from the stratum count; gradient verdict reported only
    descriptively)."""
    res = {"arm_status": status}
    if not rows or status != "ok":
        return res
    ok = sum(1 for r in rows if r["value"] == TIER0[r["id"]]["aann_position"])
    ok_first = sum(1 for r in rows
                   if r.get("value_first_token") == TIER0[r["id"]]["aann_position"])
    miss, gate = miss_gate(rows)
    bypos = {"A": sum(1 for r in rows if r["value"] == "A"),
             "B": sum(1 for r in rows if r["value"] == "B")}
    res.update({
        "n": len(rows), "aann_preferred": ok,
        "aann_preferred_first_token_v2_descriptive": ok_first,
        "missing": miss, "missingness": gate, "by_position": bypos,
        "pass": bool(ok >= TIER0_MIN and gate != "instrument-failure"),
    })
    return res


def analyze_model(slot, rows, status, t0_rows=None, t0_status="absent",
                  rb_rows=None, rb_status="absent", with_v2_carryover=True):
    """All PREREG statistics for one model. Pure function of (rows, stimuli);
    no file writes (selftest runs it on synthetic rows)."""
    res = {"slot": slot, "model": PANEL_NAMES[slot],
           "arm_status": {"heldout-temporal": status, "tier0": t0_status,
                          "robustness": rb_status}}

    # ---- TIER-0 (gate-bearing instrument check; independent of the main arm)
    res["tier0"] = analyze_tier0(t0_rows, t0_status)

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

    # ---- PRIMARY + SECONDARY (all-80 gate read)
    g = gradient_stats(rows)
    res["primary"] = {
        "n_class_cells": len(g["classes"]),
        "model_class_cell_means": {c: round(g["cell_means"][c], 4)
                                   for c in g["classes"]},
        "human_class_cell_means": {c: HUMAN[c] for c in g["classes"]},
        "class_cell_spearman": round(g["cell_rho"], 4),
        "degenerate": g["cell_degenerate"],
        "lattice_caveat": LATTICE_CAVEAT,
    }
    amean, adjs, hmean, ci = g["amean"], g["adjs"], g["hmean"], g["ci"]
    res["secondary"] = {
        "n_adjectives": len(adjs), "adjectives_dropped_all_na": g["dropped"],
        "adjective_spearman": round(g["adj_rho"], 4),
        "degenerate": g["adj_degenerate"],
        "ci95": None if ci is None else [round(ci[0], 4), round(ci[1], 4)],
        "bootstrap_resamples": BOOT, "bootstrap_seed": SEED,
    }

    # ---- VERDICT (mechanical; PREREG frozen map; gate on ALL 80 items)
    verdict, note = model_verdict(g["cell_rho"], g["adj_rho"], ci, gate)
    res["verdict"] = verdict
    if note:
        res["verdict_note"] = note
    if g["adj_degenerate"] or g["cell_degenerate"]:
        res["degenerate_output_caveat"] = ("mandatory (constant model output: "
                                           "NaN rho counted as 0, CI undefined)")

    # ---- TOURISH-TEMPLATE SENSITIVITY (pre-declared MANDATORY descriptive;
    #      the gate stays on all 80 items)
    rows_no_t2 = [r for r in rows if ITEMS[r["id"]]["template"] != TOURISH_TPL]
    gs = gradient_stats(rows_no_t2)
    verdict_excl, _ = model_verdict(gs["cell_rho"], gs["adj_rho"], gs["ci"], gate)
    sens = {
        "excluded_template": TOURISH_TPL,
        "excluded_template_text": "The tourish stayed ... in Papua New Guinea",
        "n_items_remaining": len(rows_no_t2),
        "class_cell_spearman_excl_t2": round(gs["cell_rho"], 4),
        "adjective_spearman_excl_t2": round(gs["adj_rho"], 4),
        "n_adjectives": len(gs["adjs"]),
        "ci95_excl_t2": (None if gs["ci"] is None
                         else [round(gs["ci"][0], 4), round(gs["ci"][1], 4)]),
        "verdict_if_t2_excluded": verdict_excl,
        "verdict_category_differs": verdict_excl != verdict,
        "note": ("descriptive only; the gate stays on all 80 items (PREREG); "
                 "all-80 missingness gate and bootstrap seed reused"),
    }
    if verdict_excl != verdict:
        sens["mandatory_caveat"] = (
            f"MANDATORY CAVEAT: excluding the upstream-typo ('tourish') "
            f"template-2 items changes this model's verdict category "
            f"({verdict} on all 80 items vs {verdict_excl} on the {len(rows_no_t2)} "
            f"non-template-2 items); the gate remains on all 80 items per "
            f"PREREG, and the result page must carry this sentence.")
    res["tourish_sensitivity"] = sens

    # ---- DESCRIPTIVES (no gates)
    adj_class = {s["adj"]: s["adjclass"] for s in STIMULI["items"]}
    adj_zipf = {s["adj"]: s["zipf"] for s in STIMULI["items"]}
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
    # new-only adjective-grain rho (descriptive; critic should-fix 6)
    new_adjs = [a for a in adjs if src[a] == "new"]
    new_only_rho = (nan_to_zero(spearman([amean[a] for a in new_adjs],
                                         [hmean[a] for a in new_adjs]))
                    if len(new_adjs) >= 2 else None)
    res["descriptives"] = {
        "item_spearman_pooled_n": len(item_pairs),
        "item_spearman_pooled": round(pooled, 4),
        "partial_spearman_zipf_adjective_grain": round(partial, 4),
        "per_class_adjective_spread_sd": spread,
        "new_only_adjective_spearman": (None if new_only_rho is None
                                        else round(new_only_rho, 4)),
        "new_only_n_adjectives": len(new_adjs),
        "new_vs_carryover": {
            "new_adjective_mean": round(statistics.mean(sub["new"]), 4)
            if sub.get("new") else None,
            "carryover_adjective_mean": round(statistics.mean(sub["v2-carryover"]), 4)
            if sub.get("v2-carryover") else None,
            "per_class": {f"{s}/{c}": round(statistics.mean(v), 4)
                          for (s, c), v in sorted(subcls.items())},
            "noun_asymmetry_note": NOUN_ASYMMETRY_NOTE,
        },
        "carryover_vs_v2": (carryover_vs_v2(
            slot, {a: amean[a] for a in adjs if src[a] == "v2-carryover"})
            if with_v2_carryover else {"todo": "skipped (selftest)"}),
    }

    # ---- 4-POINT FRAMING ROBUSTNESS (caveat-bearing, never gate-bearing;
    #      critic blocker 2, v2 fragility semantics verbatim)
    if rb_rows is not None and rb_status == "ok":
        v100 = {r["id"]: r["value"] for r in rows if r["value"] is not None}
        pairs = [(r["value"], v100[r["id"]]) for r in rb_rows
                 if r["value"] is not None and r["id"] in v100]
        rho = (spearman([a for a, _ in pairs], [b for _, b in pairs])
               if len(pairs) >= 2 else float("nan"))
        nan = rho != rho
        flag = framing_fragility_flag(rho)
        res["robustness_4pt"] = {
            "n_pairs": len(pairs),
            "missing": sum(1 for r in rb_rows if r["value"] is None),
            "framing_spearman": None if nan else round(rho, 4),
            "fragility_flag": flag,
        }
        if flag:
            res["instrument_fragility_caveat"] = (
                "mandatory (item-level 0-100 vs 4-point Spearman on the "
                "40-item subsample is "
                + ("undefined/NaN" if nan else f"{rho:.4f} < 0.50")
                + "): the temporal-stratum read for this model is "
                  "framing-fragile; caveat-bearing only, the gradient gate "
                  "is unchanged (PREREG)")
    return res


# ---------- assembly ----------

def assemble(per_model_results):
    """Global result object incl. stratum verdict. PREREG: ANY arm absent or
    partial (all three arms are required to run) => INCOMPLETE, no substantive
    verdict. Tier-0 failure for a model => that model EXCLUDED from the
    stratum count (gradient verdict reported descriptively); fewer than 2
    Tier-0 passers => INSTRUMENT FAILURE, no substantive stratum verdict."""
    incomplete = [f"{s}/{arm}:{st}" for s, r in per_model_results.items()
                  for arm, st in r["arm_status"].items() if st != "ok"]
    out = {
        "run": "2026-06-13-aann-temporal-heldout-v2b",
        "arms": list(EXPECTED_ROWS),
        "prereg": "PREREG.md (frozen from PREREG-draft.md)",
        "seed": SEED,
        "thresholds": {
            "cell_rho_min_inclusive": CELL_RHO_MIN,
            "adj_rho_min_inclusive": ADJ_RHO_MIN,
            "ci_lower_strictly_above": CI_LOWER_MUST_EXCEED,
            "fail_ci_upper_strictly_below": FAIL_CI_UPPER_BELOW,
            "tier0_min_inclusive_of_24": TIER0_MIN,
            "fragility_rho_strictly_below": FRAGILITY_RHO_BELOW,
        },
        "models": per_model_results,
        "cost": read_cost_log(),
    }
    if incomplete:
        out["stratum_verdict"] = "INCOMPLETE (required arm missing/partial)"
        out["incomplete_arms"] = incomplete
        return out
    passers = [s for s in ("A", "B", "C")
               if per_model_results[s]["tier0"].get("pass")]
    excluded = [s for s in ("A", "B", "C") if s not in passers]
    out["tier0_passers"] = passers
    if excluded:
        out["tier0_excluded_models"] = excluded
        out["tier0_exclusion_note"] = (
            "Tier-0 failure = instrument failure for the model: its gradient "
            "verdict is reported descriptively only and is excluded from the "
            ">=2-of-3 stratum count (PREREG)")
    if len(passers) < 2:
        out["stratum_verdict"] = ("INSTRUMENT FAILURE (fewer than 2 Tier-0 "
                                  "passers; no substantive stratum verdict)")
    else:
        out["stratum_verdict"] = stratum_verdict(
            [per_model_results[s]["verdict"] for s in passers])
    return out


def report(out):
    print("== AANN temporal held-out widening (v2b) — PREREG analysis ==")
    for s in ("A", "B", "C"):
        r = out["models"].get(s, {})
        st = r.get("arm_status", {})
        if any(v != "ok" for v in st.values()):
            print(f"  {s} ({PANEL_NAMES[s]}): arm status {st}")
            continue
        bk, pr, se, t0 = (r["bookkeeping"], r["primary"], r["secondary"],
                          r["tier0"])
        print(f"  {s} ({r['model']}): tier0 {t0['aann_preferred']}/24 "
              f"({'PASS' if t0['pass'] else 'FAIL -> excluded from stratum count'};"
              f" v2-parse descriptive {t0['aann_preferred_first_token_v2_descriptive']}/24)")
        print(f"     main: parsed {bk['n_parsed']}/{bk['n_rows']}"
              f" (NA {bk['n_missing']}, gate {bk['missingness']};"
              f" cells>5%NA {bk['cells_over_5pct_na'] or 'none'})")
        print(f"     primary 4-cell rho = {pr['class_cell_spearman']}"
              f"  [{pr['lattice_caveat']}]")
        print(f"     secondary adjective rho = {se['adjective_spearman']}"
              f" (n={se['n_adjectives']}), 95% CI {se['ci95']}"
              f" (boot {se['bootstrap_resamples']}, seed {se['bootstrap_seed']})")
        ts = r["tourish_sensitivity"]
        print(f"     tourish sensitivity (excl t2): adj rho "
              f"{ts['adjective_spearman_excl_t2']}, verdict-if-excluded "
              f"{ts['verdict_if_t2_excluded']}"
              + ("  ** MANDATORY CAVEAT: category differs **"
                 if ts["verdict_category_differs"] else ""))
        rb = r.get("robustness_4pt", {})
        print(f"     4-point framing: rho {rb.get('framing_spearman')} "
              f"(n_pairs {rb.get('n_pairs')}; fragile: {rb.get('fragility_flag')})")
        print(f"     verdict: {r['verdict']}"
              + (f"  [{r['verdict_note']}]" if r.get("verdict_note") else ""))
    print(f"  STRATUM VERDICT: {out['stratum_verdict']}")
    cost = out["cost"]
    print(f"  billed cost: {cost['total_billed_usd']} ({cost['status']}"
          + (f"; {cost.get('missing_cost_calls')} calls missing usage.cost"
             if cost.get("missing_cost_calls") else "") + ")")
    print("\n=== MACHINE-READABLE JSON SUMMARY ===")
    print(json.dumps(out, indent=1))


def main():
    per_model = {}
    for slot in ("A", "B", "C"):
        rows, status = load(slot, "heldout-temporal")
        t0_rows, t0_status = load(slot, "tier0")
        rb_rows, rb_status = load(slot, "robustness")
        per_model[slot] = analyze_model(slot, rows, status, t0_rows, t0_status,
                                        rb_rows, rb_status)
    out = assemble(per_model)
    json.dump(out, open(HERE / "results.json", "w"), indent=1)
    report(out)


# ---------- selftest (synthetic, in-memory, no files written, no calls) ----------

def _synthetic_rows(level_by_class, jitter_seed=None, constant=None,
                    na_ids=(), only_template=None, base_constant=None):
    """Build 80 synthetic main-arm rows from the frozen stimuli. If
    only_template is given, items of that template get the class level and
    every other item gets base_constant (tourish-sensitivity scenario)."""
    rng = random.Random(jitter_seed)
    rows = []
    for s in STIMULI["items"]:
        if s["id"] in na_ids:
            v = None
        elif constant is not None:
            v = constant
        elif only_template is not None:
            v = (level_by_class[s["adjclass"]]
                 if s["template"] == only_template else base_constant)
        else:
            v = level_by_class[s["adjclass"]] + rng.randrange(-2, 3)
        rows.append({"id": s["id"], "arm": "heldout-temporal", "raw": str(v),
                     "value": v, "usage": None, "error": None})
    return rows


def _synthetic_tier0(n_correct, n_missing=0, first_token_correct=None):
    """24 synthetic tier0 rows: the first n_missing are None, the next
    n_correct match aann_position, the rest are wrong. value_first_token
    matches aann_position for the first first_token_correct rows (defaults
    to mirroring value)."""
    rows = []
    for i, s in enumerate(STIMULI["tier0"]):
        if i < n_missing:
            val = None
        elif i < n_missing + n_correct:
            val = s["aann_position"]
        else:
            val = "A" if s["aann_position"] == "B" else "B"
        if first_token_correct is None:
            vft = val
        else:
            vft = (s["aann_position"] if i < first_token_correct
                   else ("A" if s["aann_position"] == "B" else "B"))
        rows.append({"id": s["id"], "arm": "tier0", "raw": str(val),
                     "value": val, "value_first_token": vft,
                     "usage": None, "error": None})
    return rows


def _synthetic_robustness(main_rows, mode="monotone"):
    """40 synthetic 4-point rows on the frozen subsample, derived from the
    main rows: monotone (high agreement), reversed (negative rho), or
    constant (degenerate -> NaN -> fragile)."""
    v100 = {r["id"]: r["value"] for r in main_rows}
    rows = []
    for sid in STIMULI["robustness_4pt"]["ids"]:
        v = v100.get(sid)
        if v is None:
            val = None
        elif mode == "monotone":
            val = min(4, max(1, 1 + round(3 * v / 100)))
        elif mode == "reversed":
            val = min(4, max(1, 4 - round(3 * v / 100)))
        else:  # constant
            val = 2
        rows.append({"id": sid, "arm": "robustness", "raw": str(val),
                     "value": val, "usage": None, "error": None})
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
    check("contradictory gates -> STILL-TOO-THIN (precedence rule)",
          v(0.80, 0.25, (0.01, 0.19), "ok") == "STILL-TOO-THIN")
    # ---- stratum rule (over counted models)
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

    # ---- 2. tier0 gate edge cases (critic blocker 1)
    t = analyze_tier0(_synthetic_tier0(20), "ok")
    check("tier0 exactly 20/24 passes (inclusive)", t["pass"] and t["aann_preferred"] == 20)
    t = analyze_tier0(_synthetic_tier0(19), "ok")
    check("tier0 19/24 fails", not t["pass"])
    t = analyze_tier0(_synthetic_tier0(24), "ok")
    check("tier0 24/24 passes", t["pass"])
    t = analyze_tier0(_synthetic_tier0(17, n_missing=7), "ok")
    check("tier0 >25% missing = instrument failure even if it could not reach 20",
          not t["pass"] and t["missingness"] == "instrument-failure")
    t = analyze_tier0(_synthetic_tier0(24, first_token_correct=10), "ok")
    check("tier0 v2 first-token score is descriptive only (gate unaffected)",
          t["pass"] and t["aann_preferred"] == 24
          and t["aann_preferred_first_token_v2_descriptive"] == 10)

    # ---- 3. fragility flag edge cases (critic blocker 2; v2 semantics)
    check("fragility: rho exactly 0.50 is NOT fragile (strict <)",
          not framing_fragility_flag(0.50))
    check("fragility: rho 0.4999 IS fragile", framing_fragility_flag(0.4999))
    check("fragility: NaN IS fragile", framing_fragility_flag(float("nan")))

    # ---- 4. full pipeline on synthetic data
    # A: class levels in the human anchored order (quant>ambig>pos>neg),
    #    well separated -> REPLICATES; 2 NAs in the neg cell exercise the
    #    report-and-exclude path and the per-cell >5% NA flag; monotone
    #    4-point arm -> not fragile; tier0 24/24 pass.
    neg_ids = [s["id"] for s in STIMULI["items"] if s["adjclass"] == "neg"][:2]
    rows_a = _synthetic_rows({"quant": 90, "ambig": 80, "pos": 70, "neg": 60},
                             jitter_seed=1, na_ids=neg_ids)
    # B: reversed order -> strongly negative adjective rho -> FAILS;
    #    reversed 4-point arm (still |rho| high but negative -> fragile).
    rows_b = _synthetic_rows({"quant": 60, "ambig": 70, "pos": 80, "neg": 90},
                             jitter_seed=2)
    # C: constant output -> degenerate -> STILL-TOO-THIN; constant 4-point
    #    arm -> NaN -> fragile.
    rows_c = _synthetic_rows(None, constant=50)
    per_model = {
        "A": analyze_model("A", rows_a, "ok", _synthetic_tier0(24), "ok",
                           _synthetic_robustness(rows_a, "monotone"), "ok",
                           with_v2_carryover=False),
        "B": analyze_model("B", rows_b, "ok", _synthetic_tier0(22), "ok",
                           _synthetic_robustness(rows_b, "reversed"), "ok",
                           with_v2_carryover=False),
        "C": analyze_model("C", rows_c, "ok", _synthetic_tier0(20), "ok",
                           _synthetic_robustness(rows_c, "constant"), "ok",
                           with_v2_carryover=False),
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
    check("A monotone 4-point arm: not fragile, no caveat",
          not ra["robustness_4pt"]["fragility_flag"]
          and "instrument_fragility_caveat" not in ra)
    check("A tourish sensitivity: same category, no mandatory caveat",
          not ra["tourish_sensitivity"]["verdict_category_differs"]
          and "mandatory_caveat" not in ra["tourish_sensitivity"])
    check("A new-only descriptive rho present; both-items-NA adjective "
          "('depressing') dropped and reported (n=23)",
          ra["descriptives"]["new_only_n_adjectives"] == 23
          and ra["descriptives"]["new_only_adjective_spearman"] is not None
          and ra["secondary"]["adjectives_dropped_all_na"] == ["depressing"]
          and ra["secondary"]["n_adjectives"] == 39)
    check("B new-only descriptive rho over the full n=24",
          rb["descriptives"]["new_only_n_adjectives"] == 24
          and rb["descriptives"]["new_only_adjective_spearman"] is not None)
    check("noun-asymmetry note attached to the subgroup read",
          "noun_asymmetry_note" in ra["descriptives"]["new_vs_carryover"])
    check("B fails-to-replicate on reversed synthetic data",
          rb["verdict"] == "FAILS-TO-REPLICATE")
    check("B primary 4-cell rho == -1.0",
          rb["primary"]["class_cell_spearman"] == -1.0)
    check("B reversed 4-point arm: fragile flag + mandatory caveat",
          rb["robustness_4pt"]["fragility_flag"]
          and "instrument_fragility_caveat" in rb)
    check("C degenerate: rho 0, CI undefined, STILL-TOO-THIN",
          rc["verdict"] == "STILL-TOO-THIN"
          and rc["secondary"]["adjective_spearman"] == 0.0
          and rc["secondary"]["ci95"] is None
          and rc["secondary"]["degenerate"])
    check("C constant 4-point arm: NaN -> fragile + mandatory caveat",
          rc["robustness_4pt"]["framing_spearman"] is None
          and rc["robustness_4pt"]["fragility_flag"]
          and "instrument_fragility_caveat" in rc)
    check("stratum verdict on R/F/T (all tier0 passers) is MIXED",
          out["stratum_verdict"] == "STILL-TOO-THIN / MIXED"
          and out["tier0_passers"] == ["A", "B", "C"])
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

    # ---- 5. tier0 exclusion + instrument-failure stratum paths
    # C fails tier0 (19/24); its gradient verdict must not count.
    rc_fail = analyze_model("C", rows_b, "ok", _synthetic_tier0(19), "ok",
                            _synthetic_robustness(rows_b, "monotone"), "ok",
                            with_v2_carryover=False)
    ra2 = analyze_model("A", rows_a, "ok", _synthetic_tier0(24), "ok",
                        _synthetic_robustness(rows_a, "monotone"), "ok",
                        with_v2_carryover=False)
    rb2 = analyze_model("B", rows_a, "ok", _synthetic_tier0(24), "ok",
                        _synthetic_robustness(rows_a, "monotone"), "ok",
                        with_v2_carryover=False)
    out2 = assemble({"A": ra2, "B": rb2, "C": rc_fail})
    check("tier0-failing model excluded: 2 passing replicators -> REPLICATES "
          "despite excluded model's FAILS gradient",
          out2["stratum_verdict"] == "REPLICATES"
          and out2["tier0_excluded_models"] == ["C"]
          and rc_fail["verdict"] == "FAILS-TO-REPLICATE")
    out3 = assemble({"A": ra2,
                     "B": analyze_model("B", rows_a, "ok",
                                        _synthetic_tier0(19), "ok",
                                        _synthetic_robustness(rows_a, "monotone"),
                                        "ok", with_v2_carryover=False),
                     "C": rc_fail})
    check("fewer than 2 tier0 passers -> INSTRUMENT FAILURE stratum verdict",
          out3["stratum_verdict"].startswith("INSTRUMENT FAILURE"))

    # ---- 6. tourish-sensitivity mandatory caveat fires when category differs
    # All non-template-2 items constant 50; template-2 items carry the entire
    # (correct) ordering -> all-80 read REPLICATES, excl-t2 read degenerate
    # (STILL-TOO-THIN) -> categories differ -> mandatory caveat.
    rows_t2 = _synthetic_rows({"quant": 100, "ambig": 90, "pos": 80, "neg": 60},
                              only_template=TOURISH_TPL, base_constant=50)
    rt2 = analyze_model("A", rows_t2, "ok", _synthetic_tier0(24), "ok",
                        _synthetic_robustness(rows_t2, "monotone"), "ok",
                        with_v2_carryover=False)
    check("tourish scenario: all-80 verdict REPLICATES",
          rt2["verdict"] == "REPLICATES")
    check("tourish scenario: excl-t2 verdict STILL-TOO-THIN (degenerate)",
          rt2["tourish_sensitivity"]["verdict_if_t2_excluded"]
          == "STILL-TOO-THIN")
    check("tourish scenario: mandatory caveat sentence attached",
          rt2["tourish_sensitivity"]["verdict_category_differs"]
          and "mandatory_caveat" in rt2["tourish_sensitivity"])

    # ---- 7. INCOMPLETE paths (any required arm absent)
    out_inc = assemble({"A": {"slot": "A", "model": PANEL_NAMES["A"],
                              "arm_status": {"heldout-temporal": "absent",
                                             "tier0": "ok",
                                             "robustness": "ok"},
                              "tier0": {"arm_status": "ok"}},
                        "B": rb, "C": rc})
    check("absent main arm -> INCOMPLETE, no substantive verdict",
          out_inc["stratum_verdict"].startswith("INCOMPLETE"))
    ra_norb = dict(ra2)
    ra_norb["arm_status"] = {"heldout-temporal": "ok", "tier0": "ok",
                             "robustness": "absent"}
    out_inc2 = assemble({"A": ra_norb, "B": rb2, "C": rc_fail})
    check("absent robustness arm -> INCOMPLETE (all three arms required)",
          out_inc2["stratum_verdict"].startswith("INCOMPLETE"))
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
