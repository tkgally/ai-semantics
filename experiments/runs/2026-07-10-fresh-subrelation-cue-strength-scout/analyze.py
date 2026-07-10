#!/usr/bin/env python3
"""analyze.py — per-relation contrastive-frame cue-strength of the FRESH noun sub-relations, and the
C2-DISSOCIATION feasibility read (s202 scout).

cue-strength per relation = mean 𝒮(control top-3 FRAME candidates, gold) over the relation's cues —
the SAME quantity s186/s193 called cue-strength (soundness = Cao precision-over-produced). We also
report hit@3 (gold-size-robust) because the fresh direct-gold sets are small (median 1–2), which caps
precision; the C2 read must survive on BOTH measures. A frequency-matched-subset pass checks the
ordering is not a Lg10WF artifact.

C2-DISSOCIATION QUESTION (feasibility only — NO empirical claim about model behavior; recovery is
a-priori-PREDICTED here from the s193 coarse hit@3, not measured):
  conjecture/decoupling-relation-inventory-shape needs, for a within-noun forward test, a matched pair
  of sub-inventories that dissociate C2 (tail-alignment) — one C2-SATISFYING (worst-recovered
  relations OFF the cue-strength floor, like the coarse noun set) and one C2-VIOLATING (worst-recovered
  relations AT the floor, like the verbs where the decoupling broke) — plus a C1 head disaligner
  (low-cue/high-recovery; the fresh candidate is instance_hypernymy). Whether such a pair is
  ASSEMBLABLE turns on the fresh sub-types' cue-strengths, which this measures. It does NOT confirm or
  weaken the bet; it decides constructibility of a route.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RELS = ["member_meronymy", "part_meronymy", "substance_meronymy",
        "member_holonymy", "part_holonymy", "substance_holonymy",
        "instance_hypernymy", "instance_hyponymy"]

# A-PRIORI predicted recovery band, inherited from the s193 COARSE noun hit@3 (NEXT.md carry):
#   antonymy ~0.95 / hypernymy ~0.69 / synonymy ~0.47 / hyponymy ~0.42 / holonymy ~0.32 / meronymy ~0.32.
# These are PREDICTIONS from the coarse parent, NOT measured on the fresh sub-types.
PREDICTED_RECOVERY = {
    "member_meronymy": ("LOW", 0.32), "part_meronymy": ("LOW", 0.32),
    "substance_meronymy": ("LOW", 0.32),
    "member_holonymy": ("LOW", 0.32), "part_holonymy": ("LOW", 0.32),
    "substance_holonymy": ("LOW", 0.32),
    "instance_hypernymy": ("HIGH", 0.69),   # C1 candidate head disaligner (taxonomic centrality)
    "instance_hyponymy": ("MID", 0.42),
}
# s193 coarse frame cue-strength reference (for context; NOT a within-experiment comparison — coarse
# used unions/closures, the fresh sub-types use direct gold):
S193_COARSE_CUE = {"hypernymy": 0.008, "synonymy": 0.006, "meronymy": 0.019,
                   "holonymy": 0.031, "hyponymy": 0.036, "antonymy": 0.149}


def soundness(produced, gold):
    if not produced:
        return None
    return sum(1 for w in produced if w in gold) / len(produced)


def hit(produced, gold):
    if not produced:
        return None
    return 1.0 if any(w in gold for w in produced) else 0.0


def load():
    items = json.load(open(os.path.join(HERE, "items.json")))
    ctrl = json.load(open(os.path.join(HERE, "control.json")))["cues"]
    gold, order, lg10wf = {}, {}, {}
    for r in RELS:
        order[r] = [it["cue"] for it in items["items"][r]]
        for it in items["items"][r]:
            gold[(r, it["cue"])] = set(it["gold"])
            lg10wf[(r, it["cue"])] = it["lg10wf"]
    return items, ctrl, gold, order, lg10wf


def per_rel(order, gold, ctrl, cues_subset=None):
    """cue_strength (soundness frame/sent) + hit@3 (frame) per relation, over cues (optionally subset)."""
    out = {}
    for r in RELS:
        cs_frame, cs_sent, h_frame = [], [], []
        for cue in order[r]:
            if cues_subset is not None and cue not in cues_subset:
                continue
            g = gold[(r, cue)]
            fr = [v for v, gg, o in ctrl.get(cue, {}).get("frame", [])]
            se = [v for v, gg, o in ctrl.get(cue, {}).get("sent", [])]
            sf, ss, hf = soundness(fr, g), soundness(se, g), hit(fr, g)
            if sf is not None:
                cs_frame.append(sf)
            if ss is not None:
                cs_sent.append(ss)
            if hf is not None:
                h_frame.append(hf)
        n = len(cs_frame)
        out[r] = {
            "n": n,
            "cue_strength_frame": round(sum(cs_frame) / n, 4) if n else None,
            "cue_strength_sent": round(sum(cs_sent) / len(cs_sent), 4) if cs_sent else None,
            "hit3_frame": round(sum(h_frame) / len(h_frame), 4) if h_frame else None,
        }
    return out


def freq_matched_subset(items, order, lg10wf, bin_w=0.25, seed=20260710):
    """Match all relations to a common Lg10WF profile = the sparsest relation's per-bin counts, by
    seeded per-bin subsampling. Returns a set of retained cues (union across relations)."""
    import random
    rng = random.Random(seed)
    def binof(w):
        return int((w - 2.0) / bin_w)
    # sparsest relation by n
    anchor = min(RELS, key=lambda r: len(order[r]))
    anchor_bins = {}
    for cue in order[anchor]:
        anchor_bins[binof(lg10wf[(anchor, cue)])] = anchor_bins.get(binof(lg10wf[(anchor, cue)]), 0) + 1
    keep = set()
    for r in RELS:
        by_bin = {}
        for cue in order[r]:
            by_bin.setdefault(binof(lg10wf[(r, cue)]), []).append(cue)
        for b, want in anchor_bins.items():
            pool = sorted(by_bin.get(b, []))
            take = pool if len(pool) <= want else rng.sample(pool, want)
            keep.update(take)
    return anchor, keep


def main():
    items, ctrl, gold, order, lg10wf = load()
    prof = items["profile"]

    primary = per_rel(order, gold, ctrl)
    anchor, keep = freq_matched_subset(items, order, lg10wf)
    matched = per_rel(order, gold, ctrl, cues_subset=keep)

    # ---- assemble the table, sorted by frame cue-strength (the floor axis) ----
    rows = []
    for r in RELS:
        pr = primary[r]
        band, prec = PREDICTED_RECOVERY[r]
        rows.append({
            "relation": r, "n": pr["n"], "predicted_recovery": band, "pred_hit3": prec,
            "cue_strength_frame": pr["cue_strength_frame"],
            "hit3_frame": pr["hit3_frame"],
            "cue_strength_sent": pr["cue_strength_sent"],
            "cue_strength_frame_matched": matched[r]["cue_strength_frame"],
            "gold_size_mean": prof[r].get("gold_size_mean"),
            "lg10wf_median": prof[r].get("lg10wf_median"),
        })
    rows.sort(key=lambda x: (x["cue_strength_frame"] if x["cue_strength_frame"] is not None else 9))

    # ---- C2-dissociation read (feasibility) ----
    csf = {r: primary[r]["cue_strength_frame"] for r in RELS}
    floor = min(v for v in csf.values() if v is not None)
    ceil = max(v for v in csf.values() if v is not None)
    span = ceil - floor
    low_rels = [r for r in RELS if PREDICTED_RECOVERY[r][0] == "LOW"]
    low_csf = {r: csf[r] for r in low_rels}
    low_floor = min(low_csf.values())
    low_ceil = max(low_csf.values())
    # a C2 dissociation needs LOW-recovery relations that SPAN the cue-strength range: some AT the
    # inventory floor (=> a C2-VIOLATING arm) and some clearly OFF it (=> a C2-SATISFYING arm).
    # threshold for "clearly off the floor": >= floor + 25% of the full span (heuristic, reported).
    off_floor_gap = 0.25 * span if span > 0 else 0.0
    low_at_floor = [r for r in low_rels if csf[r] <= floor + 1e-9 + off_floor_gap * 0.5]
    low_off_floor = [r for r in low_rels if csf[r] >= floor + off_floor_gap]
    head = "instance_hypernymy"
    head_csf = csf[head]
    head_at_low = head_csf <= floor + off_floor_gap   # C1 vehicle sits at low cue-strength?

    dissociable = bool(low_at_floor) and bool(low_off_floor) and head_at_low

    report = {
        "Nsent": json.load(open(os.path.join(HERE, "control.json")))["Nsent"],
        "freq_matched_anchor": anchor, "freq_matched_kept_cues": len(keep),
        "table_sorted_by_frame_cue_strength": rows,
        "cue_strength_floor": round(floor, 4), "cue_strength_ceil": round(ceil, 4),
        "cue_strength_span": round(span, 4),
        "low_recovery_relations": low_rels,
        "low_recovery_cue_strength": {r: round(low_csf[r], 4) for r in low_rels},
        "low_at_floor": low_at_floor, "low_off_floor": low_off_floor,
        "head_disaligner": head, "head_cue_strength": round(head_csf, 4),
        "head_at_low_cue_strength": head_at_low,
        "C2_dissociating_pair_assemblable": dissociable,
        "s193_coarse_cue_reference": S193_COARSE_CUE,
    }
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(report, f, indent=1)

    # ---- print ----
    print(f"\nN sentences streamed: {report['Nsent']:,}")
    print(f"\nfresh sub-relation cue-strength (sorted by frame; floor={floor:.4f} ceil={ceil:.4f}):")
    print(f"{'relation':20s} {'n':>3s} {'pred':>5s} {'frame':>7s} {'match':>7s} {'hit@3':>6s} {'sent':>7s} {'gold':>5s} {'lgWF':>5s}")
    for x in rows:
        print(f"{x['relation']:20s} {x['n']:3d} {x['predicted_recovery']:>5s} "
              f"{x['cue_strength_frame']:7.4f} "
              f"{(x['cue_strength_frame_matched'] if x['cue_strength_frame_matched'] is not None else 0):7.4f} "
              f"{(x['hit3_frame'] if x['hit3_frame'] is not None else 0):6.3f} "
              f"{(x['cue_strength_sent'] if x['cue_strength_sent'] is not None else 0):7.4f} "
              f"{(x['gold_size_mean'] if x['gold_size_mean'] is not None else 0):5.2f} "
              f"{(x['lg10wf_median'] if x['lg10wf_median'] is not None else 0):5.2f}")
    print(f"\nLOW-recovery (predicted) sub-types cue-strength: "
          f"{ {r: round(low_csf[r],4) for r in low_rels} }")
    print(f"  at floor:  {low_at_floor}")
    print(f"  off floor: {low_off_floor}")
    print(f"C1 head disaligner {head}: cue-strength {head_csf:.4f}  at-low={head_at_low}")
    print(f"\n==> C2-DISSOCIATING within-noun pair ASSEMBLABLE: {dissociable}")


if __name__ == "__main__":
    main()
