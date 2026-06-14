#!/usr/bin/env python3
"""build_trials.py — freeze the v4 trial set (stimuli.json) from CERTIFIED descriptions.

No API calls. Implements the v4 design's ONE structural change
(experiments/designs/relational-history-perturbation-v4.md §"The mechanism"): a
non-adjacent perturbation point that dissociates chronology (an explicit per-line round
STAMP) from text-position (line order) WITHIN a single arm.

GEOMETRY (the 2x2, frozen here; integers pinned in PREREG.md):
Per (model, pair, sample) cluster, over the byte-identical 4-description multiset
{x1, x2, y1, y2} (2 certified X-descriptions + 2 certified Y-descriptions), v4 crosses:

  - CLAST in {X, Y}  : the chronologically-latest twin = the twin whose two descriptions
                       carry the two LATEST round stamps (R3, R4). The decisive line is R4.
                       The OTHER twin's descriptions carry the earlier stamps (R1, R2) —
                       this is the "reassignment" (term attached to one twin first, then to
                       the other), encoded purely by the stamps.
  - DPOS in {late, early} : where the decisive (R4) line sits PHYSICALLY.
       late  -> R4 is the last line of text; the physically-last-line twin == CLAST.
       early -> R4 sits NON-TERMINALLY (position 1 or 2), followed in the text by
                chronologically-earlier lines, so the physically-last-line twin == the
                OTHER twin (not CLAST). This is the non-adjacent perturbation point.
  - VARIANT in 0..N_VARIANTS-1 : frozen line-orderings within each (clast, dpos) cell, to
       cancel serial-position (primacy/recency-of-reading) confounds and to serve as the
       within-arm "robust-to-reordering" convergent check that v4 substitutes for v3's
       presentation-direction factor (now subsumed, since physical position is a
       MANIPULATED factor in v4, not the chronology carrier — flagged for the pre-run
       critic in PREREG §"Adaptations of the frozen design").

This makes the two channels ORTHOGONAL within one arm:
  - chronologically-latest twin (CLAST) is balanced X/Y across the cell set;
  - physically-last-line twin (P) is balanced X/Y across the cell set;
  - and CLAST and P are uncorrelated (cov 0; asserted in fixtures).
So Delta_chron = P(pick = CLAST twin) - 0.5 and Delta_pos = P(pick = physically-last twin)
- 0.5 separate the chronology-reader, the text-position-reader, and the content-only
(commutative) reader, which a single rho on v3's collinear record could not.

CONTROLS per cluster (gating, on top of per-description certification):
  - CONSISTENT (monotonic stamps): 1 per twin, all 4 lines that twin, stamps ascending in
    physical order. Tests solo decodability under the stamped format.
  - STAMP-RESPECT (shuffled physical order, correct stamps): 1 per twin, all 4 lines that
    twin, stamps NON-monotonic vs physical order. The v4-specific control (design
    §Conditions): verifies a model is not derailed by non-monotonic stamp/position layout
    (which the DPOS=early mixed cells create). A model that cannot decode a shuffled-stamp
    single-twin record is read as stamp-blind -> METHODOLOGICAL NULL on the chronology
    question (its mixed picks would reduce to text-position). NECESSARY, not sufficient,
    for stamp-reading — flagged as such in PREREG.
  Manipulation gate = ALL FOUR controls correct.

SAMPLE PARTITION (pre-registered, carried from v3 critic S4): sample s in 0..N_SAMPLES-1
takes roster positions 2s and 2s+1 of the frozen first-DESCS_PER_FIG-certified roster.

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
from common import (MODELS, MODEL_SEED_OFFSET, SEED0, CLAST, DPOS, N_VARIANTS,  # noqa: E402
                    NONCE, FIGURES_SHA256, load_figures, figure_pairs)

# Frozen line-orderings (lists of round numbers in PHYSICAL/display order). N_VARIANTS each.
# LATE: R4 (decisive) physically last -> physically-last-line twin == CLAST.
LATE_ORDERS = [[1, 2, 3, 4], [2, 3, 1, 4], [3, 1, 2, 4], [2, 1, 3, 4]]
# EARLY: R4 non-terminal AND physically-last line in {R1, R2} (the OTHER twin's earlier
# block) -> physically-last-line twin == NOT-CLAST. Balanced: 2 end on R1, 2 end on R2.
EARLY_ORDERS = [[4, 3, 2, 1], [3, 4, 2, 1], [4, 3, 1, 2], [3, 4, 1, 2]]
assert len(LATE_ORDERS) == N_VARIANTS and len(EARLY_ORDERS) == N_VARIANTS
assert all(o[-1] == 4 for o in LATE_ORDERS), "LATE: decisive R4 must be physically last"
assert all(o[-1] in (1, 2) and o.index(4) != 3 for o in EARLY_ORDERS), \
    "EARLY: decisive R4 non-terminal and last line in the earlier (other-twin) block"


def round_assignment(clast, a, b, dx, dy):
    """Rounds 1..4 -> (description, figure_id). The earlier block (R1,R2) is the NOT-clast
    twin; the later block (R3,R4) is the CLAST twin; R4 is the decisive line."""
    if clast == "Y":          # clast twin = b (Y); other = a (X)
        return {1: (dx[0], a), 2: (dx[1], a), 3: (dy[0], b), 4: (dy[1], b)}, b
    else:                     # clast == "X": clast twin = a; other = b (Y)
        return {1: (dy[0], b), 2: (dy[1], b), 3: (dx[0], a), 4: (dx[1], a)}, a


def cluster_p_order(mname, pair, sample, canon):
    """Deterministic matcher array per (model, pair, sample) cluster — v3 formula, v4 seed."""
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
                dx, dy = ra[2 * s:2 * s + 2], rb[2 * s:2 * s + 2]
                assert len(dx) == 2 and len(dy) == 2, "roster shorter than n_samples implies"
                ckey = f"{m}:{pid}:{s}"
                clusters[ckey] = cluster_p_order(m, pid, s, canon)
                # ---- MIXED cells: the 2x2 x variants ----
                for clast in CLAST:
                    rmap, clast_cid = round_assignment(clast, a, b, dx, dy)
                    for dpos in DPOS:
                        orders = LATE_ORDERS if dpos == "late" else EARLY_ORDERS
                        for v, ordering in enumerate(orders):
                            stamped = [[k, rmap[k][0]] for k in ordering]  # physical order
                            last_round = ordering[-1]
                            last_cid = rmap[last_round][1]
                            trials[m].append({
                                "kind": "mixed", "pair": pid, "X": a, "Y": b,
                                "sample": s, "cluster": ckey, "nonce": NONCE[pid],
                                "clast": clast, "clast_cid": clast_cid,
                                "dpos": dpos, "variant": v,
                                "decisive_round": 4, "decisive_cid": clast_cid,
                                "last_round": last_round, "last_cid": last_cid,
                                "stamped": stamped,   # [[round, desc], ...] physical order
                            })
                # ---- CONTROLS: consistent (monotonic) + stamp-respect (shuffled) ----
                for fid, dd in ((a, dx), (b, dy)):
                    # consistent: 4 lines that twin, stamps ascending in physical order
                    cons = [[1, dd[0]], [2, dd[1]], [3, dd[0]], [4, dd[1]]]
                    trials[m].append({
                        "kind": "consistent", "pair": pid, "X": a, "Y": b, "sample": s,
                        "cluster": ckey, "nonce": NONCE[pid], "target": fid,
                        "stamped": cons})
                    # stamp-respect: same lines, NON-monotonic physical order vs stamps
                    rmap_c = {1: dd[0], 2: dd[1], 3: dd[0], 4: dd[1]}
                    sr_order = [3, 1, 4, 2]
                    sr = [[k, rmap_c[k]] for k in sr_order]
                    trials[m].append({
                        "kind": "stamp_respect", "pair": pid, "X": a, "Y": b, "sample": s,
                        "cluster": ckey, "nonce": NONCE[pid], "target": fid,
                        "stamped": sr})
    return {"seed": SEED0, "clast_levels": CLAST, "dpos_levels": DPOS,
            "n_variants": N_VARIANTS, "late_orders": LATE_ORDERS,
            "early_orders": EARLY_ORDERS, "nonce": {str(k): v for k, v in NONCE.items()},
            "figures_content_sha256": FIGURES_SHA256,
            "figures": figs, "pairs": pairs, "clusters": clusters, "trials": trials,
            "certification_census": report.get("census", []),
            "anti_null_bias_disclosure": report.get("anti_null_bias_disclosure", "")}


def assert_geometry(out):
    """The byte-identical-multiset + orthogonality/balance asserts the design requires."""
    for m in MODELS:
        n_cl = sum(1 for k in out["clusters"] if k.startswith(m + ":"))
        mixed = [t for t in out["trials"][m] if t["kind"] == "mixed"]
        cons = [t for t in out["trials"][m] if t["kind"] == "consistent"]
        sr = [t for t in out["trials"][m] if t["kind"] == "stamp_respect"]
        # per cluster: 2 clast x 2 dpos x N_VARIANTS mixed; 2 consistent; 2 stamp-respect
        assert len(mixed) == 2 * 2 * N_VARIANTS * n_cl, "mixed geometry violation"
        assert len(cons) == 2 * n_cl and len(sr) == 2 * n_cl, "control geometry violation"
        by_cl = {}
        for t in mixed:
            by_cl.setdefault(t["cluster"], []).append(t)
        for ck, cells in by_cl.items():
            # byte-identical DESCRIPTION multiset across all mixed cells of the cluster
            msets = {tuple(sorted(d for _, d in t["stamped"])) for t in cells}
            assert len(msets) == 1, f"multiset drift in {ck}"
            assert len(cells) == 2 * 2 * N_VARIANTS, f"cell count in {ck}"
            # CLAST balanced, P (last-line twin) balanced, and CLAST _|_ P (cov 0)
            xs = [1 if t["clast_cid"] == t["Y"] else 0 for t in cells]   # code by twin
            ps = [1 if t["last_cid"] == t["Y"] else 0 for t in cells]
            n = len(cells)
            assert sum(xs) == n // 2, f"CLAST not balanced in {ck}"
            assert sum(ps) == n // 2, f"physically-last twin not balanced in {ck}"
            cov = sum(x * p for x, p in zip(xs, ps)) / n - (sum(xs) / n) * (sum(ps) / n)
            assert abs(cov) < 1e-12, f"CLAST and physical-last twin not orthogonal in {ck}"
            # decisive (R4) line non-terminal in every EARLY cell, terminal in every LATE
            for t in cells:
                rounds_phys = [k for k, _ in t["stamped"]]
                if t["dpos"] == "early":
                    assert rounds_phys[-1] != 4 and t["last_cid"] != t["clast_cid"], \
                        f"early cell not decoupled in {ck}"
                else:
                    assert rounds_phys[-1] == 4 and t["last_cid"] == t["clast_cid"], \
                        f"late cell not aligned in {ck}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", default=os.path.join(HERE, "certification_report.json"))
    ap.add_argument("--out", default=os.path.join(HERE, "stimuli.json"))
    args = ap.parse_args()
    if not os.path.exists(args.report):
        sys.exit(f"no {args.report} — run harvest.py + certify.py first "
                 f"(or pass --report fixtures/certification_report.fixture.json).")
    report = json.load(open(args.report))
    figs = load_figures()
    out = build(report, figs)
    assert_geometry(out)
    with open(args.out, "w") as f:
        json.dump(out, f, indent=2)
    h = hashlib.sha256(open(args.out, "rb").read()).hexdigest()
    n = {m: len(out["trials"][m]) for m in MODELS}
    total = sum(n.values())
    per_cluster = 2 * 2 * N_VARIANTS + 4
    print(f"{os.path.basename(args.out)} written: trials/model {n} (total {total}; "
          f"{per_cluster}/cluster = {2*2*N_VARIANTS} mixed + 4 controls)\nsha256={h}")
    for m in MODELS:
        n_cl = sum(1 for k in out["clusters"] if k.startswith(m + ":"))
        print(f"  {m}: {n_cl} clusters")
    print("FREEZE: record this sha256 in PREREG.md (frozen post-critic) before any "
          "finding-bearing call; probe.py refuses `preflight`/`full` until it matches.")


if __name__ == "__main__":
    main()
