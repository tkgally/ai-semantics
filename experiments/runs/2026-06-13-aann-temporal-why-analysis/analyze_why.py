#!/usr/bin/env python3
"""
analyze_why.py  --  $0 read-only re-analysis: WHY does the temporal noun class
fail to replicate the AANN held-out acceptability gradient?

NO model API calls. Reads only existing on-disk artifacts from two frozen runs:
  - 2026-06-13-aann-temporal-heldout-v2b/  (the temporal-only widened run; the finding)
  - 2026-06-12-aann-behavioral-probe-v2/   (the parent run; object/distance/temporal classes)

It adjudicates four candidate explanations for the temporal held-out failure
(see the unit brief / NEXT.md item 3):

  H1  Compressed human gradient   -- is the temporal human class gradient FLATTER
                                     than the object/distance ones it is compared against?
  H2  Small temporal noun inventory -- how many Mahowald nouns / class-cells does
                                     temporal admit, and does that cap precision?
  H3  Frequency artifact          -- do temporal AANN strings differ in Zipf by class?
  H4  Genuine model-side hole     -- residual: if H1-H3 don't account for it.

Everything is recomputed from raw. The script first REPRODUCES the published v2b
temporal cell-grain Spearman values (provenance sanity check) before drawing any
new conclusion. Spearman conventions are copied verbatim from the frozen
analyze.py files so the reproduction is byte-faithful.

Run:  python3 analyze_why.py        # prints a report, writes findings.json
"""
import json
import statistics
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
ROOT = HERE.parent.parent.parent  # repo root
V2B = ROOT / "experiments/runs/2026-06-13-aann-temporal-heldout-v2b"
V2 = ROOT / "experiments/runs/2026-06-12-aann-behavioral-probe-v2"

PANELS = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
# The 4 adjective classes the temporal noun class admits in Mahowald Exp-2.
TEMPORAL_ADJCLASSES = ["ambig", "neg", "pos", "quant"]


# ---------- statistics (verbatim convention from the frozen analyze.py files) ----------
def ranks(xs):
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


def load_raw(path):
    """Frozen raw files are JSON arrays of {id, value, ...} records."""
    return json.load(open(path))


# ============================================================================
# Load stimuli + human anchors
# ============================================================================
V2B_STIM = json.load(open(V2B / "stimuli.json"))
V2B_ITEMS = {s["id"]: s for s in V2B_STIM["items"]}
# v2b human temporal class means (the yardstick the v2b temporal arm replicates)
HUMAN_TEMP = {c: v["mean"] for c, v in V2B_STIM["human_temporal_class_means"].items()}

# Full per-(adjclass, nounclass) human cell means -- the cross-class table H1 needs.
HUMAN_CELLS = {}  # (adjclass, nounclass) -> (n, mean)
for row in (V2 / "human_class_means.csv").read_text().splitlines()[1:]:
    adjclass, nounclass, n, mean = row.split(",")
    HUMAN_CELLS[(adjclass, nounclass)] = (int(n), float(mean))


# ============================================================================
# PROVENANCE CHECK: reproduce the published v2b temporal cell-grain Spearman
# ============================================================================
def v2b_cell_spearman_per_model():
    """Per-model Spearman of the 4 held-out temporal class-cell model means
    against the human temporal class means -- the v2b PRIMARY figure."""
    out = {}
    for slot, model in PANELS.items():
        recs = load_raw(V2B / "raw" / f"{slot}-heldout-temporal.json")
        per_class = defaultdict(list)
        for r in recs:
            if r["value"] is None:
                continue
            per_class[V2B_ITEMS[r["id"]]["adjclass"]].append(r["value"])
        classes = sorted(per_class)  # ambig, neg, pos, quant
        cell_means = {c: statistics.mean(per_class[c]) for c in classes}
        rho = spearman([cell_means[c] for c in classes],
                       [HUMAN_TEMP[c] for c in classes])
        out[model] = {
            "n_records": sum(len(per_class[c]) for c in classes),
            "cell_means": {c: round(cell_means[c], 4) for c in classes},
            "cell_grain_spearman": round(rho, 4),
        }
    return out


# Published v2b primary figures (from the result page table; for the sanity check).
V2B_PUBLISHED_CELL_RHO = {
    "claude-sonnet-4.6": -0.20,
    "gpt-5.4-mini": -0.40,
    "gemini-3.5-flash": -0.40,
}


# ============================================================================
# H1: human gradient SPREAD per noun class (compressed-gradient hypothesis)
# ============================================================================
def human_spread_by_nounclass():
    """For each noun class, the within-class spread of the human anchored-half
    class-cell means over the 4 temporal-admissible adjclasses (ambig/neg/pos/quant).
    A *flatter* gradient -> a near-tie ranking -> a Spearman that tracks noise."""
    out = {}
    # Noun classes that have all 4 of the temporal adjclasses present:
    nounclasses = sorted({nc for (ac, nc) in HUMAN_CELLS
                          if ac in TEMPORAL_ADJCLASSES})
    for nc in nounclasses:
        means = {}
        for ac in TEMPORAL_ADJCLASSES:
            if (ac, nc) in HUMAN_CELLS:
                means[ac] = HUMAN_CELLS[(ac, nc)][1]
        if len(means) < 4:
            out[nc] = {"complete": False, "present_adjclasses": sorted(means)}
            continue
        vals = list(means.values())
        out[nc] = {
            "complete": True,
            "class_means": {ac: round(means[ac], 4) for ac in TEMPORAL_ADJCLASSES},
            "range": round(max(vals) - min(vals), 4),
            "sd": round(statistics.pstdev(vals), 4),
            # ordering of the 4 classes by human mean (low->high):
            "human_order_low_to_high": [ac for ac, _ in
                                        sorted(means.items(), key=lambda kv: kv[1])],
        }
    return out


# ============================================================================
# H1 (cross-class behavior): the v2 held-out per-noun-class Spearman.
# Did object/distance track POSITIVE while temporal went NEGATIVE -- and is
# that explained by their human spread, or do they track positive DESPITE a
# similar/compressed spread?
# ============================================================================
def v2_heldout_per_stratum():
    res = json.load(open(V2 / "results.json"))["results"]
    out = {}
    for slot, model in PANELS.items():
        out[model] = res[slot]["heldout"]["within_nounclass_per_stratum"]
    return out


# ============================================================================
# H2: temporal noun inventory + class-cell count
# ============================================================================
def temporal_inventory():
    nouns = sorted({s["noun"] for s in V2B_STIM["items"]})
    adjclasses = sorted({s["adjclass"] for s in V2B_STIM["items"]})
    # cells = adjclass x nounclass; temporal is one noun class -> #cells = #adjclasses
    return {
        "n_temporal_nouns": len(nouns),
        "temporal_nouns": nouns,
        "n_adjclasses": len(adjclasses),
        "adjclasses": adjclasses,
        "n_class_cells": len(adjclasses),  # 4: the structural maximum
        "spearman_lattice_n4": "{0, +/-0.2, +/-0.4, +/-0.6, +/-0.8, +/-1.0}",
        "note": ("with only 4 class-cells the cell-grain Spearman can take "
                 "11 discrete values; a single swapped pair moves rho by 0.2-0.4"),
    }


# ============================================================================
# H3: frequency artifact -- Zipf by noun class
# ============================================================================
def zipf_by_class():
    """The v2 held-out items carry a per-ADJECTIVE wordfreq Zipf. Temporal and
    distance share the SAME adjective set, so any class difference in held-out
    Zipf is driven by the noun class's adjective inventory, not by string freq."""
    d2 = json.load(open(V2 / "stimuli.json"))
    by = defaultdict(list)
    adj_by = defaultdict(set)
    for it in d2["held_out"]:
        if it.get("zipf") is not None:
            by[it["nounclass"]].append(it["zipf"])
            adj_by[it["nounclass"]].add(it["adj"])
    out = {}
    for nc in sorted(by):
        out[nc] = {
            "n_items": len(by[nc]),
            "zipf_median": round(statistics.median(by[nc]), 4),
            "zipf_mean": round(statistics.mean(by[nc]), 4),
            "n_unique_adjs": len(adj_by[nc]),
        }
    # v2b temporal items (the widened set)
    zt = [it["zipf"] for it in V2B_STIM["items"] if it.get("zipf") is not None]
    out["temporal_v2b"] = {
        "n_items": len(zt),
        "zipf_median": round(statistics.median(zt), 4),
        "zipf_mean": round(statistics.mean(zt), 4),
        "n_unique_adjs": len({it["adj"] for it in V2B_STIM["items"]}),
    }
    # the freq audit already proves per-adjclass freq-match within the temporal set
    out["v2b_freq_audit_all_pass"] = all(a["pass"] for a in V2B_STIM["freq_audit"])
    # do temporal and distance share the held-out adjective set? (key for H3)
    out["temporal_distance_same_adjset_in_v2"] = (
        adj_by.get("temporal") == adj_by.get("distance"))
    return out


# ============================================================================
# H4 support check: per-noun model behavior on the v2b temporal items.
# Is the negative sign carried by a systematic inversion, or by near-ties /
# one or two noisy cells? Inspect the per-noun, per-adjclass model means.
# ============================================================================
def v2b_per_noun_behavior():
    out = {}
    for slot, model in PANELS.items():
        recs = load_raw(V2B / "raw" / f"{slot}-heldout-temporal.json")
        cell = defaultdict(list)   # (adjclass) -> values  (model gradient)
        noun_adj = defaultdict(list)  # (noun, adjclass) -> values
        for r in recs:
            if r["value"] is None:
                continue
            it = V2B_ITEMS[r["id"]]
            cell[it["adjclass"]].append(r["value"])
            noun_adj[(it["noun"], it["adjclass"])].append(r["value"])
        model_order = [ac for ac, _ in sorted(
            ((ac, statistics.mean(v)) for ac, v in cell.items()),
            key=lambda kv: kv[1])]
        # per-noun cell-grain spearman (does ANY single noun track positive?)
        per_noun_rho = {}
        nouns = sorted({n for (n, _) in noun_adj})
        for n in nouns:
            ms = {ac: statistics.mean(noun_adj[(n, ac)])
                  for ac in TEMPORAL_ADJCLASSES if (n, ac) in noun_adj}
            if len(ms) == 4:
                per_noun_rho[n] = round(spearman(
                    [ms[ac] for ac in TEMPORAL_ADJCLASSES],
                    [HUMAN_TEMP[ac] for ac in TEMPORAL_ADJCLASSES]), 4)
        # localization probe: does dropping the quant cell flip the sign positive?
        cl3 = ["ambig", "neg", "pos"]
        rho_no_quant = spearman(
            [statistics.mean(cell[c]) for c in cl3],
            [HUMAN_TEMP[c] for c in cl3])
        out[model] = {
            "model_class_means": {ac: round(statistics.mean(cell[ac]), 4)
                                  for ac in TEMPORAL_ADJCLASSES},
            "model_order_low_to_high": model_order,
            "human_order_low_to_high": [ac for ac, _ in sorted(
                HUMAN_TEMP.items(), key=lambda kv: kv[1])],
            "per_noun_cell_spearman": per_noun_rho,
            "n_nouns_positive": sum(1 for v in per_noun_rho.values() if v > 0),
            "n_nouns_total": len(per_noun_rho),
            # quant is rated HIGHEST by humans (8.45) but LOWEST by every model:
            "quant_is_human_highest": (max(HUMAN_TEMP, key=HUMAN_TEMP.get) == "quant"),
            "quant_is_model_lowest": (model_order[0] == "quant"),
            "cell_grain_spearman_dropping_quant": round(rho_no_quant, 4),
        }
    return out


# ============================================================================
def main():
    findings = {}

    # --- provenance check ---
    repro = v2b_cell_spearman_per_model()
    sanity = {}
    for model, pub in V2B_PUBLISHED_CELL_RHO.items():
        got = repro[model]["cell_grain_spearman"]
        sanity[model] = {"published": pub, "recomputed": got,
                         "match": abs(got - pub) < 1e-6}
    findings["provenance_check_v2b_cell_grain_spearman"] = {
        "recomputed": repro, "vs_published": sanity,
        "all_match": all(s["match"] for s in sanity.values()),
    }

    # --- H1 ---
    spreads = human_spread_by_nounclass()
    strata = v2_heldout_per_stratum()
    findings["H1_human_gradient_spread_by_nounclass"] = spreads
    findings["H1_v2_heldout_spearman_per_stratum"] = strata
    # cross-class comparison summary
    temp_range = spreads.get("temporal", {}).get("range")
    cmp = {}
    for nc, s in spreads.items():
        if s.get("complete"):
            cmp[nc] = {"range": s["range"], "sd": s["sd"]}
    findings["H1_spread_comparison"] = {
        "temporal_range": temp_range,
        "by_nounclass": cmp,
        "temporal_is_narrowest": (
            temp_range is not None
            and temp_range == min(v["range"] for v in cmp.values())),
    }

    # --- H2 ---
    findings["H2_temporal_inventory"] = temporal_inventory()

    # --- H3 ---
    findings["H3_zipf_by_class"] = zipf_by_class()

    # --- H4 ---
    findings["H4_per_noun_model_behavior"] = v2b_per_noun_behavior()

    json.dump(findings, open(HERE / "findings.json", "w"), indent=1)

    # ---- human-readable report ----
    print("=" * 72)
    print("PROVENANCE CHECK -- v2b temporal cell-grain Spearman reproduces?")
    for m, s in sanity.items():
        print(f"  {m:20s} published {s['published']:+.2f}  "
              f"recomputed {s['recomputed']:+.4f}  "
              f"{'MATCH' if s['match'] else 'MISMATCH'}")
    print(f"  ALL MATCH: {findings['provenance_check_v2b_cell_grain_spearman']['all_match']}")

    print("=" * 72)
    print("H1 -- human gradient spread (range over ambig/neg/pos/quant), per noun class")
    for nc, s in sorted(spreads.items()):
        if s.get("complete"):
            print(f"  {nc:10s} range {s['range']:.3f}  sd {s['sd']:.3f}  "
                  f"order {s['human_order_low_to_high']}")
        else:
            print(f"  {nc:10s} INCOMPLETE (have {s['present_adjclasses']})")
    print(f"  temporal narrowest? {findings['H1_spread_comparison']['temporal_is_narrowest']}")
    print("  v2 held-out per-stratum Spearman (object/distance POSITIVE, temporal NEGATIVE):")
    for m, st in strata.items():
        print(f"    {m:20s} {st}")

    print("=" * 72)
    print("H2 -- temporal inventory")
    inv = findings["H2_temporal_inventory"]
    print(f"  {inv['n_temporal_nouns']} nouns: {inv['temporal_nouns']}")
    print(f"  {inv['n_class_cells']} class-cells (structural max) -> {inv['spearman_lattice_n4']}")

    print("=" * 72)
    print("H3 -- Zipf (per-adjective wordfreq) by noun class")
    z = findings["H3_zipf_by_class"]
    for nc in ["temporal", "distance", "objects", "temporal_v2b"]:
        if nc in z:
            print(f"  {nc:14s} median {z[nc]['zipf_median']:.3f}  "
                  f"mean {z[nc]['zipf_mean']:.3f}  n_adj {z[nc]['n_unique_adjs']}")
    print(f"  temporal & distance share held-out adjective set: "
          f"{z['temporal_distance_same_adjset_in_v2']}")
    print(f"  v2b per-adjclass freq audit all pass: {z['v2b_freq_audit_all_pass']}")

    print("=" * 72)
    print("H4 -- per-noun model behavior on v2b temporal (any noun track positive?)")
    for m, b in findings["H4_per_noun_model_behavior"].items():
        print(f"  {m}")
        print(f"    model order  {b['model_order_low_to_high']}")
        print(f"    human order  {b['human_order_low_to_high']}")
        print(f"    per-noun rho {b['per_noun_cell_spearman']}")
        print(f"    nouns positive: {b['n_nouns_positive']}/{b['n_nouns_total']}")
        print(f"    quant human-highest & model-lowest: "
              f"{b['quant_is_human_highest']} & {b['quant_is_model_lowest']}  "
              f"-> rho dropping quant = {b['cell_grain_spearman_dropping_quant']:+.3f}")

    print("=" * 72)
    print("findings.json written.")


if __name__ == "__main__":
    main()
