#!/usr/bin/env python3
"""build_trials.py — freeze the v3 trial set (stimuli.json) from CERTIFIED descriptions.

No API calls. Adapted from v2 build_stimuli.py with the v3 design changes
(experiments/designs/relational-history-perturbation-v3.md):

- descriptions come from certification_report.json (freshly harvested + per-description
  certified, fix 2), NOT from v1 live-game raw;
- 3 description samples per pair -> 9 (pair x sample) clusters per model per direction
  (fix 3), unless a recorded shortfall reduced a model's sample count;
- fresh frozen nonces PLOVNEK / SKARMIL / VANTREX (no v2 carryover);
- v1 discipline retained: ONE frozen matcher figure-array permutation per cluster,
  constant across that cluster's 12 mixed cells + 2 controls (v2 critic S1) — now frozen
  INTO stimuli.json (the artifact fully determines the probe);
- MIXED: 2 certified descriptions of X + 2 of Y, uniform positive feedback, all 6 orders
  of {X,X,Y,Y} x 2 presentation directions; content multiset byte-identical across the 12
  cells of a cluster;
- CONSISTENT: 4 controls per cluster — one per twin x BOTH presentation directions
  (critic S1, 2026-06-13: a rev-direction control checks instruction-following under the
  rev framing, sharpening the position-vs-direction artifact diagnosis), retained on top
  of certification as defense in depth. 36 controls/model; totals 144/model, 432.
- SAMPLE PARTITION (pre-registered, critic S4): sample s in {0, 1, 2} takes roster
  positions 2s and 2s+1 of the frozen first-6-certified-in-harvest-order roster
  (`roster[2s:2s+2]` below) — fully deterministic given certification_report.json.

Freeze discipline: the printed sha256 of stimuli.json goes into PREREG.md; NO
finding-bearing probe call before that hash is committed (probe.py enforces this).

Usage (from repo root or this dir):
  python3 build_trials.py
  python3 build_trials.py --report fixtures/certification_report.fixture.json \
                          --out fixtures/stimuli.fixture.json     # dry-run geometry check
"""
import argparse
import hashlib
import json
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import (MODELS, MODEL_SEED_OFFSET, SEED0, ORDERS, DIRECTIONS, NONCE,  # noqa: E402
                    FIGURES_SHA256, load_figures, figure_pairs)


def cluster_p_order(mname, pair, sample, canon):
    """Deterministic matcher array per (model, pair, sample) cluster — v2 formula, v3 seed."""
    rng = random.Random(SEED0 + MODEL_SEED_OFFSET[mname] + 100 * pair + 10 * sample)
    ids = list(canon)
    rng.shuffle(ids)
    return [[f"P{i+1}", cid] for i, cid in enumerate(ids)]


def build(report, figs):
    pairs = figure_pairs(figs)
    canon = sorted(figs)
    trials = {m: [] for m in MODELS}
    clusters = {}
    for m in MODELS:
        md = report["models"][m]
        for pid, (a, b) in sorted(pairs.items()):
            pmeta = md["pairs"][str(pid)]
            assert (pmeta["X"], pmeta["Y"]) == (a, b), "pair/report mismatch"
            n_samples = pmeta["n_samples"]
            ra = md["figures"][a]["roster"]
            rb = md["figures"][b]["roster"]
            for s in range(n_samples):
                # pre-registered deterministic partition (critic S4): sample s = roster
                # positions 2s, 2s+1 (first-6-certified-in-harvest-order roster)
                dx, dy = ra[2 * s:2 * s + 2], rb[2 * s:2 * s + 2]
                assert len(dx) == 2 and len(dy) == 2, "roster shorter than n_samples implies"
                ckey = f"{m}:{pid}:{s}"
                clusters[ckey] = cluster_p_order(m, pid, s, canon)
                for order in ORDERS:
                    ix, iy, lines = 0, 0, []
                    for ch in order:
                        if ch == "X":
                            lines.append(dx[ix]); ix += 1
                        else:
                            lines.append(dy[iy]); iy += 1
                    for direction in DIRECTIONS:
                        trials[m].append({
                            "kind": "mixed", "pair": pid, "X": a, "Y": b,
                            "order": order, "direction": direction, "sample": s,
                            "nonce": NONCE[pid], "lines": lines, "cluster": ckey,
                            "last": a if order[-1] == "X" else b,   # chron-last twin
                            "first": a if order[0] == "X" else b,   # chron-first twin
                        })
                # consistent controls: all 4 lines describe ONE twin, run in BOTH
                # presentation directions (critic S1) -> 4 controls per cluster
                for fid, dd in ((a, dx), (b, dy)):
                    for direction in DIRECTIONS:
                        trials[m].append({
                            "kind": "consistent", "pair": pid, "X": a, "Y": b,
                            "order": None, "direction": direction, "sample": s,
                            "nonce": NONCE[pid], "target": fid, "cluster": ckey,
                            "lines": [dd[0], dd[1], dd[0], dd[1]],
                        })
    return {"seed": SEED0, "orders": ORDERS, "directions": DIRECTIONS,
            "nonce": {str(k): v for k, v in NONCE.items()},
            "figures_content_sha256": FIGURES_SHA256,
            "figures": figs, "pairs": pairs, "clusters": clusters, "trials": trials,
            "certification_census": report.get("census", []),
            "anti_null_bias_disclosure": report.get("anti_null_bias_disclosure", "")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", default=os.path.join(HERE, "certification_report.json"))
    ap.add_argument("--out", default=os.path.join(HERE, "stimuli.json"))
    args = ap.parse_args()
    if not os.path.exists(args.report):
        sys.exit(f"no {args.report} — run harvest.py + certify.py first "
                 f"(or pass --report fixtures/certification_report.fixture.json).")
    report = json.load(open(args.report))
    figs = load_figures()  # hash-checked against the frozen v1 set
    out = build(report, figs)

    # geometry assertions (design: 9 clusters -> 108 mixed + 36 controls per model;
    # controls = 2 twins x 2 directions per cluster, critic S1)
    for m in MODELS:
        n_cl = sum(1 for k in out["clusters"] if k.startswith(m + ":"))
        mixed = [t for t in out["trials"][m] if t["kind"] == "mixed"]
        cons = [t for t in out["trials"][m] if t["kind"] == "consistent"]
        assert len(mixed) == 12 * n_cl and len(cons) == 4 * n_cl, "geometry violation"
        assert all(sum(1 for t in cons if t["direction"] == d) == 2 * n_cl
                   for d in DIRECTIONS), "controls not balanced across directions"
        # byte-identical multiset within every cluster's 12 mixed cells
        by_cl = {}
        for t in mixed:
            by_cl.setdefault(t["cluster"], []).append(tuple(sorted(t["lines"])))
        for ck, msets in by_cl.items():
            assert len(set(msets)) == 1 and len(msets) == 12, f"multiset drift in {ck}"
        if n_cl < 9:
            print(f"  NOTE: {m} has {n_cl}/9 clusters (recorded shortfall) — record the "
                  f"reduced count in PREREG.md before the freeze.")
    with open(args.out, "w") as f:
        json.dump(out, f, indent=2)
    h = hashlib.sha256(open(args.out, "rb").read()).hexdigest()
    n = {m: len(out["trials"][m]) for m in MODELS}
    total = sum(n.values())
    print(f"{os.path.basename(args.out)} written: trials/model {n} (total {total}; "
          f"design nominal 144/model, 432 total)\nsha256={h}")
    print("FREEZE: record this sha256 in PREREG.md (frozen post-critic) before any "
          "finding-bearing call; probe.py refuses `preflight`/`full` until it matches.")


if __name__ == "__main__":
    main()
