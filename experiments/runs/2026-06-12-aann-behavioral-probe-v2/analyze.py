#!/usr/bin/env python3
"""AANN behavioral probe v2 — analysis. Implements PREREG.md exactly; no tunable knobs.

Outputs results.json + a human-readable summary to stdout.
"""
import json, random, statistics
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
STIMULI = json.load(open(HERE / "stimuli.json"))
ITEMS = {s["id"]: s for s in STIMULI["anchored"] + STIMULI["held_out"]}
BOOT = 10000
SEED = 20260612


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
    """Spearman of x,y controlling z via rank residualization (PREREG)."""
    rx, ry, rz = ranks(x), ranks(y), ranks(z)

    def resid(a, b):
        ma, mb = statistics.mean(a), statistics.mean(b)
        beta = (sum((p - ma) * (q - mb) for p, q in zip(a, b))
                / max(sum((q - mb) ** 2 for q in b), 1e-12))
        return [p - ma - beta * (q - mb) for p, q in zip(a, b)]

    return spearman(resid(rx, rz), resid(ry, rz))


EXPECTED_ROWS = {"anchored": 408, "robustness": 102, "heldout": 60, "tier0": 24}


def load(slot, arm):
    """Full raw files only (S2: .partial files from an abort are never analyzed).
    Returns (rows, status): status is 'ok', 'wrong-count', or 'absent'."""
    p = HERE / "raw" / f"{slot}-{arm}.json"
    if not p.exists():
        return None, "absent"
    rows = json.load(open(p))
    if len(rows) != EXPECTED_ROWS[arm]:
        return rows, "wrong-count"
    return rows, "ok"


def miss_gate(rows):
    """PREREG missingness rules: >10% caveat, >25% arm instrument failure."""
    miss = sum(1 for r in rows if r["value"] is None)
    frac = miss / len(rows) if rows else 1.0
    return miss, ("instrument-failure" if frac > 0.25
                  else "caveat" if frac > 0.10 else "ok")


def human_cells():
    cells = {}
    for row in open(HERE / "human_cell_means.csv").read().splitlines()[1:]:
        adj, adjclass, nc, n, mean = row.split(",")
        cells[(adj, nc)] = (adjclass, float(mean))
    return cells


def within_nounclass_mean(per_cell_model, human, key_nc, min_cells=4):
    """Mean Spearman within each noun-class stratum (pre-run critic B2 guard).
    NaN within a stratum (constant model values: the noun-class-only confound)
    counts as 0. Returns (mean, per_stratum_dict)."""
    strata = defaultdict(list)
    for c in per_cell_model:
        strata[key_nc(c)].append(c)
    per = {}
    for nc, cs in sorted(strata.items()):
        if len(cs) < min_cells:
            continue
        rho = spearman([per_cell_model[c] for c in cs], [human[c] for c in cs])
        per[nc] = 0.0 if rho != rho else round(rho, 4)  # NaN -> 0
    mean = statistics.mean(per.values()) if per else 0.0
    return round(mean, 4), per


def human_class_cells():
    cells = {}
    for row in open(HERE / "human_class_means.csv").read().splitlines()[1:]:
        ac, nc, n, mean = row.split(",")
        cells[(ac, nc)] = float(mean)
    return cells


def analyze_model(slot):
    res = {"slot": slot}
    hc = human_cells()
    hcc = human_class_cells()

    # ---- Tier-0
    t0, t0_status = load(slot, "tier0")
    res["arm_status"] = {"tier0": t0_status}
    if t0 and t0_status == "ok":
        t0map = {s["id"]: s for s in STIMULI["tier0"]}
        ok = sum(1 for r in t0 if r["value"] == t0map[r["id"]]["aann_position"])
        miss, gate = miss_gate(t0)
        bypos = {"A": sum(1 for r in t0 if r["value"] == "A"),
                 "B": sum(1 for r in t0 if r["value"] == "B")}
        res["tier0"] = {"n": len(t0), "aann_preferred": ok, "missing": miss,
                        "missingness": gate, "by_position": bypos,
                        "pass": bool(ok >= 20 and gate != "instrument-failure")}

    # ---- anchored
    an, an_status = load(slot, "anchored")
    res["arm_status"]["anchored"] = an_status
    if an and an_status == "ok":
        per_cell = defaultdict(list)
        item_pairs = []
        for r in an:
            if r["value"] is None:
                continue
            it = ITEMS[r["id"]]
            per_cell[(it["adj"], it["nounclass"])].append((r["value"], it["zipf"]))
            item_pairs.append((r["value"], it["human_rating"]))
        cells = sorted(c for c in per_cell if c in hc)
        m = [statistics.mean(v for v, _ in per_cell[c]) for c in cells]
        h = [hc[c][1] for c in cells]
        z = [per_cell[c][0][1] for c in cells]  # zipf is per-adjective, constant within cell
        rho = spearman(m, h)
        rng = random.Random(SEED)
        boots = []
        n = len(cells)
        for _ in range(BOOT):
            idx = [rng.randrange(n) for _ in range(n)]
            boots.append(spearman([m[i] for i in idx], [h[i] for i in idx]))
        boots.sort()
        ci = (boots[int(0.025 * BOOT) - 1], boots[int(0.975 * BOOT) - 1])
        partial = partial_spearman(m, h, z)
        miss, gate = miss_gate(an)
        # B2 guard: within-noun-class Spearman (noun-class-only confound scores ~0 here)
        pcm = {c: statistics.mean(v for v, _ in per_cell[c]) for c in cells}
        hum = {c: hc[c][1] for c in cells}
        wnc_mean, wnc_per = within_nounclass_mean(pcm, hum, key_nc=lambda c: c[1],
                                                  min_cells=10)
        res["anchored"] = {
            "n_items": len(an), "missing": miss, "missingness": gate, "n_cells": n,
            "cell_spearman": round(rho, 4), "ci95": [round(ci[0], 4), round(ci[1], 4)],
            "partial_spearman_zipf": round(partial, 4),
            "within_nounclass_mean_spearman": wnc_mean,
            "within_nounclass_per_stratum": wnc_per,
            "item_spearman_descriptive_only": round(
                spearman([a for a, _ in item_pairs], [b for _, b in item_pairs]), 4),
            "raw_pass": bool(rho >= 0.40 and ci[0] > 0),
            "freq_guard_pass": bool(partial >= 0.20),
            "nounclass_guard_pass": bool(wnc_mean >= 0.25),
        }
        res["anchored"]["pass"] = bool(res["anchored"]["raw_pass"]
                                       and res["anchored"]["freq_guard_pass"]
                                       and res["anchored"]["nounclass_guard_pass"]
                                       and gate != "instrument-failure")
        # secondary grain: 28 class-cells
        per_cc = defaultdict(list)
        for r in an:
            if r["value"] is None:
                continue
            it = ITEMS[r["id"]]
            per_cc[(it["adjclass"], it["nounclass"])].append(r["value"])
        ccs = sorted(c for c in per_cc if c in hcc)
        res["anchored"]["class_cell_spearman"] = round(
            spearman([statistics.mean(per_cc[c]) for c in ccs], [hcc[c] for c in ccs]), 4)

    # ---- held-out (gradient replication vs HUMAN anchored class-cells)
    ho, ho_status = load(slot, "heldout")
    res["arm_status"]["heldout"] = ho_status
    if ho and ho_status == "ok":
        per_cc = defaultdict(list)
        for r in ho:
            if r["value"] is None:
                continue
            it = ITEMS[r["id"]]
            per_cc[(it["adjclass"], it["nounclass"])].append(r["value"])
        ccs = sorted(c for c in per_cc if c in hcc)
        mcc = {c: statistics.mean(per_cc[c]) for c in ccs}
        rho = spearman([mcc[c] for c in ccs], [hcc[c] for c in ccs])
        miss, gate = miss_gate(ho)
        wnc_mean, wnc_per = within_nounclass_mean(mcc, hcc, key_nc=lambda c: c[1],
                                                  min_cells=4)
        res["heldout"] = {"n_items": len(ho), "missing": miss, "missingness": gate,
                          "n_class_cells": len(ccs),
                          "class_cell_spearman_vs_human_anchored": round(rho, 4),
                          "within_nounclass_mean_spearman": wnc_mean,
                          "within_nounclass_per_stratum": wnc_per,
                          "nounclass_guard_pass": bool(wnc_mean >= 0.30),
                          "pass": bool(rho >= 0.50 and wnc_mean >= 0.30
                                       and gate != "instrument-failure")}
        if rho >= 0.50 and wnc_mean < 0.30:
            res["heldout"]["note"] = ("not separable from noun-class main effect "
                                      "(overall rho passed, within-class mean did not)")

    # ---- framing robustness
    rb, rb_status = load(slot, "robustness")
    res["arm_status"]["robustness"] = rb_status
    if rb and rb_status == "ok" and an and an_status == "ok":
        v100 = {r["id"]: r["value"] for r in an if r["value"] is not None}
        pairs = [(r["value"], v100[r["id"]]) for r in rb
                 if r["value"] is not None and r["id"] in v100]
        rho = spearman([a for a, _ in pairs], [b for _, b in pairs])
        nan = rho != rho
        res["robustness"] = {"n_pairs": len(pairs),
                             "missing": sum(1 for r in rb if r["value"] is None),
                             "framing_spearman": None if nan else round(rho, 4),
                             # S5: NaN (degenerate constant output) => flagged fragile
                             "fragility_flag": bool(nan or rho < 0.50)}
    return res


def main():
    results = {s: analyze_model(s) for s in ["A", "B", "C"]}
    # S1: any verdict-bearing arm absent/partial => INCOMPLETE, no substantive verdict
    incomplete = [(s, a, st) for s in results
                  for a, st in results[s].get("arm_status", {}).items() if st != "ok"]
    if incomplete:
        out = {"results": results, "verdict": "INCOMPLETE (verdict-bearing arm missing/partial)",
               "incomplete_arms": [f"{s}/{a}:{st}" for s, a, st in incomplete]}
        json.dump(out, open(HERE / "results.json", "w"), indent=1)
        print(json.dumps(out, indent=1))
        return
    # PREREG verdict map
    t0_passers = [s for s in results if results[s].get("tier0", {}).get("pass")]
    anchored_passers = [s for s in t0_passers
                        if results[s].get("anchored", {}).get("pass")]
    heldout_ok = [s for s in anchored_passers
                  if results[s].get("heldout", {}).get("pass")]
    confounded = [s for s in t0_passers
                  if results[s].get("anchored", {}).get("raw_pass")
                  and not results[s].get("anchored", {}).get("freq_guard_pass")]
    if len(anchored_passers) >= 2 and len(heldout_ok) == len(anchored_passers):
        verdict = "SUPPORTED"
    elif len(anchored_passers) >= 2:
        verdict = "PARTIAL (memorization-like: held-out replication failed for a passer)"
    elif len(t0_passers) >= 2 and len(anchored_passers) < 2:
        nominal = [s for s in t0_passers if results[s].get("anchored", {}).get("raw_pass")]
        if not nominal or all(s in confounded for s in nominal):
            verdict = ("FALSIFIED (current form)" if not nominal
                       else "FALSIFIED (current form: all passes frequency-confounded)")
        else:
            verdict = "PARTIAL (form-without-gradient)"
    else:
        verdict = "INSTRUMENT FAILURE (fewer than 2 Tier-0 passers)"
    out = {"results": results, "tier0_passers": t0_passers,
           "anchored_passers": anchored_passers, "heldout_ok": heldout_ok,
           "frequency_confounded": confounded, "verdict": verdict}
    json.dump(out, open(HERE / "results.json", "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
