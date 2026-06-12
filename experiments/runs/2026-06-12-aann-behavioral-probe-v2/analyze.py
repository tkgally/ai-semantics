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


def load(slot, arm):
    p = HERE / "raw" / f"{slot}-{arm}.json"
    return json.load(open(p)) if p.exists() else None


def human_cells():
    cells = {}
    for row in open(HERE / "human_cell_means.csv").read().splitlines()[1:]:
        adj, adjclass, nc, n, mean = row.split(",")
        cells[(adj, nc)] = (adjclass, float(mean))
    return cells


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
    t0 = load(slot, "tier0")
    if t0:
        t0map = {s["id"]: s for s in STIMULI["tier0"]}
        ok = sum(1 for r in t0 if r["value"] == t0map[r["id"]]["aann_position"])
        res["tier0"] = {"n": len(t0), "aann_preferred": ok,
                        "missing": sum(1 for r in t0 if r["value"] is None),
                        "pass": ok >= 20}

    # ---- anchored
    an = load(slot, "anchored")
    if an:
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
        ci = (boots[int(0.025 * BOOT)], boots[int(0.975 * BOOT)])
        partial = partial_spearman(m, h, z)
        miss = sum(1 for r in an if r["value"] is None)
        res["anchored"] = {
            "n_items": len(an), "missing": miss, "n_cells": n,
            "cell_spearman": round(rho, 4), "ci95": [round(ci[0], 4), round(ci[1], 4)],
            "partial_spearman_zipf": round(partial, 4),
            "item_spearman": round(spearman([a for a, _ in item_pairs],
                                            [b for _, b in item_pairs]), 4),
            "raw_pass": bool(rho >= 0.40 and ci[0] > 0),
            "freq_guard_pass": bool(partial >= 0.20),
        }
        res["anchored"]["pass"] = (res["anchored"]["raw_pass"]
                                   and res["anchored"]["freq_guard_pass"])
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
    ho = load(slot, "heldout")
    if ho:
        per_cc = defaultdict(list)
        for r in ho:
            if r["value"] is None:
                continue
            it = ITEMS[r["id"]]
            per_cc[(it["adjclass"], it["nounclass"])].append(r["value"])
        ccs = sorted(c for c in per_cc if c in hcc)
        rho = spearman([statistics.mean(per_cc[c]) for c in ccs], [hcc[c] for c in ccs])
        res["heldout"] = {"n_items": len(ho),
                          "missing": sum(1 for r in ho if r["value"] is None),
                          "n_class_cells": len(ccs),
                          "class_cell_spearman_vs_human_anchored": round(rho, 4),
                          "pass": bool(rho >= 0.50)}

    # ---- framing robustness
    rb = load(slot, "robustness")
    if rb and an:
        v100 = {r["id"]: r["value"] for r in an if r["value"] is not None}
        pairs = [(r["value"], v100[r["id"]]) for r in rb
                 if r["value"] is not None and r["id"] in v100]
        rho = spearman([a for a, _ in pairs], [b for _, b in pairs])
        res["robustness"] = {"n_pairs": len(pairs),
                             "missing": sum(1 for r in rb if r["value"] is None),
                             "framing_spearman": round(rho, 4),
                             "fragility_flag": bool(rho < 0.50)}
    return res


def main():
    results = {s: analyze_model(s) for s in ["A", "B", "C"]}
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
