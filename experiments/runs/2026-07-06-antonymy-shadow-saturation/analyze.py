#!/usr/bin/env python3
"""analyze.py — scoring + verdict for the A1b antonymy shadow-saturation probe.

Recomputes everything from raw/ + items.json + control.json. No threshold is tuned after
seeing results (anti-cheat); the verdict map is the one frozen in PREREG.md.

Two per-cue scorers, both frozen (Q2-A + the gold-size-insensitive companion the pre-run
reviews required):
- SOUNDNESS 𝒮 = (produced words in gold)/(words produced)  — Cao precision-over-produced.
- HIT@k       = 1 if any produced word is in gold else 0     — gold-size-insensitive (a hit is
                a hit regardless of over-production; neutralizes the antonymy-ceiling confound
                the reviewers flagged: gold size 1 caps 𝒮 at 1/3 when the model volunteers 3).

residual(rel, model, scorer) = score(model, neutral) − score(control), paired per cue, bootstrap
95% CI over cues. Controls: frame-G² (mechanism-specific) + sent-G² (relation-agnostic, the
neutral baseline). Size-matched view = frame control on cues |gold|≤GOLD_CAP.

Verdict is taken over multiple views (dual-control × two scorers × size-matched); the headline is
CONFIRMS-ROBUST / CONFIRMS-FRAME-SPECIFIC / SHADOW-SATURATED-FLAT / INVERTED / MIXED, plus a
calibration gate (if residual just reproduces raw recovery, report descriptive-only). n=3 models,
orderings not coefficients.
"""
import json
import random
from pathlib import Path

HERE = Path(__file__).parent
RELS = ["antonymy", "synonymy", "hypernymy", "hyponymy", "holonymy", "meronymy"]
SLOTS = ["A", "B", "C"]
B_BOOT = 2000
BOOT_SEED = 20260706
GOLD_CAP = 5


def soundness(produced, gold):
    if not produced:
        return None
    return sum(1 for w in produced if w in gold) / len(produced)


def hit(produced, gold):
    if not produced:
        return None
    return 1.0 if any(w in gold for w in produced) else 0.0


def load_items():
    items = json.load(open(HERE / "items.json"))
    gold, order = {}, {}
    for r in RELS:
        order[r] = [it["cue"] for it in items["items"][r]]
        for it in items["items"][r]:
            gold[(r, it["cue"])] = set(it["gold"])
    return items, gold, order


def control_scores(order, gold, scorer):
    ctrl = json.load(open(HERE / "control.json"))["cues"]
    out = {}
    for r in RELS:
        for variant in ("frame", "sent"):
            d = {}
            for cue in order[r]:
                cand = [v for v, g, o in ctrl.get(cue, {}).get(variant, [])]
                d[cue] = scorer(cand, gold[(r, cue)])
            out[(r, variant)] = d
    return out


def model_scores(gold, order, scorer):
    out, miss = {}, {}
    for slot in SLOTS:
        for r in RELS:
            for arm in (("neutral", "frame") if r == "antonymy" else ("neutral",)):
                f = HERE / "raw" / f"{slot}-{r}-{arm}.json"
                if not f.exists():
                    continue
                rows = json.load(open(f))
                d = {}
                empt = 0
                for row in rows:
                    if not row["words"]:
                        empt += 1
                    d[row["cue"]] = scorer(row["words"], gold[(r, row["cue"])])
                out[(slot, r, arm)] = d
                miss[(slot, r, arm)] = empt
    return out, miss


def mean_ci(vals):
    v = [x for x in vals if x is not None]
    if not v:
        return None, None, None, 0
    m = sum(v) / len(v)
    rng = random.Random(BOOT_SEED)
    n = len(v)
    boots = sorted(sum(v[rng.randrange(n)] for _ in range(n)) / n for _ in range(B_BOOT))
    return m, boots[int(0.025 * B_BOOT)], boots[int(0.975 * B_BOOT)], n


def residual_ci(model_d, ctrl_d, keep=None):
    diffs = []
    for cue in model_d:
        if keep is not None and cue not in keep:
            continue
        mv, cv = model_d[cue], ctrl_d.get(cue)
        if mv is None or cv is None:
            continue
        diffs.append(mv - cv)
    if not diffs:
        return None, None, None, 0
    m = sum(diffs) / len(diffs)
    rng = random.Random(BOOT_SEED)
    n = len(diffs)
    boots = sorted(sum(diffs[rng.randrange(n)] for _ in range(n)) / n for _ in range(B_BOOT))
    return m, boots[int(0.025 * B_BOOT)], boots[int(0.975 * B_BOOT)], n


def spearman(a, b):
    def rank(x):
        idx = sorted(range(len(x)), key=lambda i: x[i])
        r = [0] * len(x)
        for pos, i in enumerate(idx):
            r[i] = pos
        return r
    ra, rb = rank(a), rank(b)
    n = len(a)
    d2 = sum((ra[i] - rb[i]) ** 2 for i in range(n))
    return 1 - 6 * d2 / (n * (n * n - 1))


def resid_table(mod, ctrl, scorer_name, order=None, keep_by_rel=None):
    """{slot: {rel: {mean,ci,n}}} for the frame control (+sent stored separately)."""
    out = {}
    for variant in ("frame", "sent"):
        out[variant] = {}
        for slot in SLOTS:
            out[variant][slot] = {}
            for r in RELS:
                md = mod.get((slot, r, "neutral"), {})
                keep = keep_by_rel[r] if keep_by_rel else None
                m, lo, hi, n = residual_ci(md, ctrl[(r, variant)], keep=keep)
                out[variant][slot][r] = {"mean": m, "ci": [lo, hi], "n": n}
    return out


def ant_smallest_count(view):
    c = 0
    for slot in SLOTS:
        vals = {r: view[slot][r]["mean"] for r in RELS if view[slot][r]["mean"] is not None}
        if vals and min(vals, key=vals.get) == "antonymy":
            c += 1
    return c


def smallest_per_model(view):
    out = {}
    for slot in SLOTS:
        vals = {r: view[slot][r]["mean"] for r in RELS if view[slot][r]["mean"] is not None}
        out[slot] = min(vals, key=vals.get) if vals else None
    return out


def main():
    items, gold, order = load_items()
    ctrl_S = control_scores(order, gold, soundness)
    ctrl_H = control_scores(order, gold, hit)
    modS, missS = model_scores(gold, order, soundness)
    modH, _ = model_scores(gold, order, hit)

    rep = {"n_per_rel": items["n_per_rel"], "relations": RELS}

    # gold sizes + %gold-in-V + small subset
    vocab = set(json.load(open(HERE / "vocab.json"))["vocab"])
    rep["gold_size"], small = {}, {}
    for r in RELS:
        sizes = sorted(len(gold[(r, c)]) for c in order[r])
        in_v = [sum(1 for w in gold[(r, c)] if w in vocab) / max(1, len(gold[(r, c)]))
                for c in order[r]]
        rep["gold_size"][r] = {"mean": round(sum(sizes) / len(sizes), 2),
                               "median": sizes[len(sizes) // 2], "max": sizes[-1],
                               "n_le_cap": sum(1 for s in sizes if s <= GOLD_CAP),
                               "pct_gold_in_V": round(sum(in_v) / len(in_v), 3)}
        small[r] = {c for c in order[r] if len(gold[(r, c)]) <= GOLD_CAP}

    # raw model soundness + hit; control soundness + hit
    rep["raw_soundness"], rep["raw_hit"] = {}, {}
    for slot in SLOTS:
        rep["raw_soundness"][slot], rep["raw_hit"][slot] = {}, {}
        for r in RELS:
            m, lo, hi, n = mean_ci(list(modS.get((slot, r, "neutral"), {}).values()))
            rep["raw_soundness"][slot][r] = {"mean": m, "ci": [lo, hi], "n": n,
                                             "empty": missS.get((slot, r, "neutral"), 0)}
            m2, l2, h2, n2 = mean_ci(list(modH.get((slot, r, "neutral"), {}).values()))
            rep["raw_hit"][slot][r] = {"mean": m2, "ci": [l2, h2], "n": n2}
    rep["control_soundness"], rep["control_hit"] = {}, {}
    for variant in ("frame", "sent"):
        rep["control_soundness"][variant], rep["control_hit"][variant] = {}, {}
        for r in RELS:
            m, lo, hi, n = mean_ci(list(ctrl_S[(r, variant)].values()))
            rep["control_soundness"][variant][r] = {"mean": m, "ci": [lo, hi], "n": n}
            m2, l2, h2, n2 = mean_ci(list(ctrl_H[(r, variant)].values()))
            rep["control_hit"][variant][r] = {"mean": m2, "ci": [l2, h2], "n": n2}

    # residual tables: soundness + hit (full) and size-matched (both scorers, frame)
    rep["residual_soundness"] = resid_table(modS, ctrl_S, "soundness")
    rep["residual_hit"] = resid_table(modH, ctrl_H, "hit")
    rep["residual_soundness_sizematched"] = resid_table(
        modS, ctrl_S, "soundness", keep_by_rel=small)["frame"]
    rep["residual_hit_sizematched"] = resid_table(
        modH, ctrl_H, "hit", keep_by_rel=small)["frame"]

    # frame-ablation (antonymy): 𝒮(frame) − 𝒮(neutral), + hit
    rep["frame_ablation"] = {}
    for slot in SLOTS:
        for label, md in (("soundness", modS), ("hit", modH)):
            nd = md.get((slot, "antonymy", "neutral"), {})
            fd = md.get((slot, "antonymy", "frame"), {})
            diffs = [fd[c] - nd[c] for c in nd if c in fd and nd[c] is not None and fd[c] is not None]
            if diffs:
                m = sum(diffs) / len(diffs)
                rng = random.Random(BOOT_SEED)
                n = len(diffs)
                bs = sorted(sum(diffs[rng.randrange(n)] for _ in range(n)) / n for _ in range(B_BOOT))
                rep["frame_ablation"].setdefault(slot, {})[label] = {
                    "mean_delta": round(m, 4), "ci": [round(bs[int(0.025*B_BOOT)], 4),
                                                      round(bs[int(0.975*B_BOOT)], 4)], "n": n,
                    "neutral": round(sum(v for v in nd.values() if v is not None)/max(1, sum(1 for v in nd.values() if v is not None)), 4),
                    "frame": round(sum(v for v in fd.values() if v is not None)/max(1, sum(1 for v in fd.values() if v is not None)), 4)}

    # clause-2: raw ranking vs corpus cue-strength (control 𝒮), reported for BOTH controls
    rep["clause2"] = {}
    for cvar in ("frame", "sent"):
        cue_strength = [rep["control_soundness"][cvar][r]["mean"] or 0.0 for r in RELS]
        top_cs = RELS[max(range(6), key=lambda i: cue_strength[i])]
        per = {}
        for slot in SLOTS:
            raw = [rep["raw_soundness"][slot][r]["mean"] or 0.0 for r in RELS]
            per[slot] = {"rho": round(spearman(raw, cue_strength), 3),
                         "antonymy_top_raw": RELS[max(range(6), key=lambda i: raw[i])] == "antonymy"}
        rep["clause2"][cvar] = {"cue_strength_top": top_cs, "per_model": per,
                                "antonymy_top_cue_strength": top_cs == "antonymy"}

    # ------- headline verdict over views (frozen logic) -------
    def visibly_larger(view, slot):
        """antonymy residual CI-separated-below meronymy AND/OR hyponymy for this model."""
        a = view[slot]["antonymy"]
        if a["mean"] is None:
            return False
        for r in ("meronymy", "hyponymy"):
            o = view[slot][r]
            if o["mean"] is not None and a["ci"][1] < o["ci"][0]:
                return True
        return False

    def flat_count(view):
        c = 0
        for slot in SLOTS:
            a = view[slot]["antonymy"]
            if a["mean"] is None:
                continue
            ov = sum(1 for r in RELS if r != "antonymy" and view[slot][r]["mean"] is not None
                     and not (a["ci"][1] < view[slot][r]["ci"][0] or view[slot][r]["ci"][1] < a["ci"][0]))
            if ov == 5:
                c += 1
        return c

    # measured weakly-cued relations = bottom-2 by frame cue-strength (SHOULD-FIX 5)
    cs_frame = [(r, rep["control_soundness"]["frame"][r]["mean"] or 0.0) for r in RELS]
    weak = {r for r, _ in sorted(cs_frame, key=lambda x: x[1])[:2]}
    rep["weakly_cued_relations"] = sorted(weak)

    views = {
        "soundness_frame": rep["residual_soundness"]["frame"],
        "soundness_sent": rep["residual_soundness"]["sent"],
        "soundness_sizematched": rep["residual_soundness_sizematched"],
        "hit_frame": rep["residual_hit"]["frame"],
        "hit_sent": rep["residual_hit"]["sent"],
        "hit_sizematched": rep["residual_hit_sizematched"],
    }
    ant_counts = {k: ant_smallest_count(v) for k, v in views.items()}
    smalls = {k: smallest_per_model(v) for k, v in views.items()}
    vlarge = {k: sum(1 for s in SLOTS if visibly_larger(v, s)) for k, v in views.items()}
    inverted = {k: sum(1 for s in SLOTS if smalls[k][s] in weak) for k, v in views.items()}

    # calibration: does residual just reproduce raw ranking? (frame, soundness)
    calib = {}
    for slot in SLOTS:
        raw = [rep["raw_soundness"][slot][r]["mean"] or 0.0 for r in RELS]
        resid = [rep["residual_soundness"]["frame"][slot][r]["mean"] or 0.0 for r in RELS]
        calib[slot] = round(spearman(raw, resid), 3)
    mean_ctrl_S = sum(rep["control_soundness"]["frame"][r]["mean"] or 0 for r in RELS) / 6

    frame_views = ["soundness_frame", "hit_frame", "soundness_sizematched", "hit_sizematched"]
    sent_views = ["soundness_sent", "hit_sent"]
    # round-2 critic condition 1: CONFIRMS requires antonymy-smallest AND meronymy/hyponymy
    # CI-separated-larger (visibly_larger) on >=2/3, per frame view — not a bare argmin.
    robust_frame = all(ant_counts[v] >= 2 and vlarge[v] >= 2 for v in frame_views)
    robust_sent = all(ant_counts[v] >= 2 for v in sent_views)
    if robust_frame and robust_sent:
        headline = "CONFIRMS-ROBUST"
    elif robust_frame:
        headline = "CONFIRMS-FRAME-SPECIFIC"
    elif flat_count(rep["residual_hit"]["frame"]) >= 2:
        headline = "SHADOW-SATURATED-FLAT"
    elif inverted["hit_frame"] >= 2:
        headline = "INVERTED"
    else:
        headline = "MIXED/NO-MAJORITY"

    # locked calibration gate: descriptive-only iff control explains ~nothing AND residual
    # merely reproduces raw recovery (PREREG: mean 𝒮(control,frame)<0.05 AND median Spearman>=0.90)
    calib_median = sorted(calib.values())[len(calib) // 2] if calib else 0.0
    descriptive_only = (mean_ctrl_S < 0.05) and (calib_median >= 0.90)

    rep["headline"] = {
        "verdict": headline,
        "residual_descriptive_only": descriptive_only,
        "calibration_median_spearman": calib_median,
        "antonymy_smallest_counts": ant_counts,
        "smallest_per_model": smalls,
        "visibly_larger_counts": vlarge,
        "inverted_counts": inverted,
        "flat_count_hit_frame": flat_count(rep["residual_hit"]["frame"]),
        "calibration_spearman_resid_vs_raw": calib,
        "mean_control_soundness_frame": round(mean_ctrl_S, 4),
        "note": ("CONFIRMS requires antonymy-smallest on >=2/3 under all 4 frame views "
                 "(soundness+hit, full+sizematched); ROBUST adds both sent views. If calibration "
                 "Spearman ~1 and mean control soundness negligible, the residual arm is "
                 "descriptive-only and weight shifts to clause-2 + frame-ablation (PREREG gate).")}

    json.dump(rep, open(HERE / "results.json", "w"), indent=1)
    _print(rep, views, ant_counts, smalls)


def _print(rep, views, ant_counts, smalls):
    print("=" * 74)
    print("HEADLINE:", rep["headline"]["verdict"])
    print("antonymy-smallest counts (/3) per view:", ant_counts)
    print("smallest-residual per model per view:")
    for k in views:
        print(f"   {k:26s} {smalls[k]}")
    print("calibration Spearman(resid,raw) per model:", rep["headline"]["calibration_spearman_resid_vs_raw"])
    print("mean control soundness (frame):", rep["headline"]["mean_control_soundness_frame"])
    print("\nPRIMARY residual — HIT@3, frame control  (𝒮hit(model)−𝒮hit(control)):")
    for slot in SLOTS:
        v = rep["residual_hit"]["frame"][slot]
        print(f"  {slot}: " + "  ".join(
            f"{r[:4]}={v[r]['mean']:+.2f}[{v[r]['ci'][0]:+.2f},{v[r]['ci'][1]:+.2f}]"
            for r in RELS if v[r]["mean"] is not None))
    print("\nSoundness residual, frame control:")
    for slot in SLOTS:
        v = rep["residual_soundness"]["frame"][slot]
        print(f"  {slot}: " + "  ".join(f"{r[:4]}={v[r]['mean']:+.2f}" for r in RELS if v[r]["mean"] is not None))
    print("\nRaw recovery (soundness) + control cue-strength per relation:")
    for r in RELS:
        cs = rep["control_soundness"]["frame"][r]["mean"]
        raws = [rep["raw_soundness"][s][r]["mean"] for s in SLOTS]
        print(f"   {r:12s} raw 𝒮 A/B/C={['%.2f'%x if x is not None else 'NA' for x in raws]}  "
              f"ctrl-frame 𝒮={cs:.3f}")
    print("\nClause-2:", {k: rep["clause2"][k]["antonymy_top_cue_strength"] for k in rep["clause2"]},
          "| per-model rho (frame):", {s: rep["clause2"]["frame"]["per_model"][s]["rho"] for s in SLOTS})
    print("Frame-ablation (antonymy):")
    for slot in SLOTS:
        fa = rep["frame_ablation"].get(slot, {})
        if fa:
            s = fa.get("soundness", {}); h = fa.get("hit", {})
            print(f"   {slot}: 𝒮 {s.get('neutral')}→{s.get('frame')} (Δ{s.get('mean_delta'):+}) | "
                  f"hit {h.get('neutral')}→{h.get('frame')} (Δ{h.get('mean_delta'):+})")
    print("\nGold sizes / %gold-in-V:")
    for r in RELS:
        g = rep["gold_size"][r]
        print(f"   {r:12s} mean={g['mean']:5.1f} median={g['median']:3d} max={g['max']:3d} "
              f"|gold|<={GOLD_CAP}:{g['n_le_cap']:3d}  %gold-in-V={g['pct_gold_in_V']}")
    print("weakly-cued (bottom-2 cue-strength):", rep["weakly_cued_relations"])
    print("\nresults.json written.")


if __name__ == "__main__":
    main()
