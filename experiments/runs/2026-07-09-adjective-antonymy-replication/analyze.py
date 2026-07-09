#!/usr/bin/env python3
"""analyze.py — scoring + verdict for the ADJECTIVE-antonymy replication probe (H1 + antonymy-shadow).

Recomputes everything from raw/ + items.json + control.json. No threshold is tuned after seeing
results (anti-cheat); the verdict map is the one frozen in PREREG.md. Gates RATIFIED s196 (Q1-C /
Q2-A / Q3 internal-contrast-only) + eight freeze-time conditions honored here:

- Q1-C: the ANTONYMY-SHADOW clause is the registered PRIMARY; the across-relation decoupling (H1) is a
  CO-PRIMARY reported at its true low power (<=4 relations); the item-level cue-strength->recovery arm
  is a POWERED SECONDARY, DESCRIPTIVE/ROBUSTNESS-ONLY (C7 — can never on its own fire/break H1).
- Q2-A: NO H2 / no structural proxy (adjectives have no IS-A taxonomy).
- C1 + C8: the antonymy FRAME-ABLATION arm is the corpus-free hedge, with its OWN pre-registered
  numeric decision rule (Δ on HIT@3 under frame-suppression).
- C2: exhaustive, mutually-exclusive H1 bands (no uncovered dead-zone).
- C3: a NUMERIC calibration floor on mean control-frame soundness; below it the antonymy-shadow
  RESIDUAL arm is DESCRIPTIVE-ONLY and weight shifts to the frame-ablation arm + H1.
- C6: HIT@3 (gold-size-insensitive) is the scorer of record for the antonymy-shadow PRIMARY (antonymy
  gold ~= 1); a relation-agnostic, pre-registered largest-vs-smallest RANK+MARGIN decision rule.

Recovery = model relatum production, one NEUTRAL (frame-suppressed) arm over all 4 relations + a
FRAME-present arm for antonymy only (the frame-ablation arm). Soundness 𝒮 = Cao precision-over-
produced; HIT@3 = gold-size-insensitive co-primary. n=3 models, orderings not coefficients,
ADJECTIVES only — never pooled with the noun probes.
"""
import json
import random
from pathlib import Path

HERE = Path(__file__).parent
RELS = ["antonymy", "synonymy", "similar", "alsosee"]
SLOTS = ["A", "B", "C"]
B_BOOT = 2000
BOOT_SEED = 20260709

# ---- FROZEN verdict thresholds (PREREG; C2/C3/C6/C8) ----
H1_REPL_MAX = 0.30      # rho_cue <= 0.30 -> DECOUPLING-REPLICATES (byte-identical to s193)
H1_BREAK_MIN = 0.50     # rho_cue >  0.50 -> DECOUPLING-BREAKS (byte-identical to s193)
# (0.30, 0.50] -> H1-PARTIAL/AMBIGUOUS (exhaustive, mutually exclusive; pre-named)
CALIB_FLOOR = 0.05      # C3: mean control-frame soundness floor (s186 value); below -> residual descriptive-only
ANT_NEARZERO = 0.10     # C6: antonymy-shadow near-zero band for the residual (HIT@3)
DELTA_ABLATE = 0.15     # C8: antonym recovery "survives" frame suppression iff HIT@3(neutral) >= HIT@3(frame) - DELTA
MAJ = 2                 # >=2/3 models


def soundness(produced, gold):
    if not produced:
        return None
    return sum(1 for w in produced if w in gold) / len(produced)


def hit(produced, gold):
    if not produced:
        return None
    return 1.0 if any(w in gold for w in produced) else 0.0


def spearman(a, b):
    """TIE-NAIVE Spearman (byte-identical to s186/s193 — the authoritative pipeline)."""
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


def load_items():
    items = json.load(open(HERE / "items.json"))
    gold, order = {}, {}
    for r in RELS:
        order[r] = [it["cue"] for it in items["items"][r]]
        for it in items["items"][r]:
            gold[(r, it["cue"])] = set(it["gold"])
    return items, gold, order


def control_per_cue(order, gold, scorer):
    """per (rel,variant): {cue: scorer(control top-3, gold)}."""
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


def model_per_cue(gold, order, scorer):
    """per (slot,rel,arm): {cue: scorer(words, gold)}; arm in {neutral, frame(antonymy only)}."""
    out, miss = {}, {}
    for slot in SLOTS:
        for r in RELS:
            for arm in (("neutral", "frame") if r == "antonymy" else ("neutral",)):
                f = HERE / "raw" / f"{slot}-{r}-{arm}.json"
                if not f.exists():
                    continue
                rows = json.load(open(f))
                d, empt = {}, 0
                for row in rows:
                    if not row["words"]:
                        empt += 1
                    d[row["cue"]] = scorer(row["words"], gold[(r, row["cue"])])
                out[(slot, r, arm)] = d
                miss[(slot, r, arm)] = empt
    return out, miss


def mean_of(d, keep=None):
    v = [x for c, x in d.items() if x is not None and (keep is None or c in keep)]
    return sum(v) / len(v) if v else 0.0


def residual_ci(model_d, ctrl_d):
    diffs = []
    for cue in model_d:
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


def main():
    items, gold, order = load_items()
    ctrlS = control_per_cue(order, gold, soundness)
    ctrlH = control_per_cue(order, gold, hit)
    mS, missS = model_per_cue(gold, order, soundness)
    mH, missH = model_per_cue(gold, order, hit)

    # ---- per-relation recovery + cue-strength (neutral arm) ----
    recS = {(s, r): mean_of(mS[(s, r, "neutral")]) for s in SLOTS for r in RELS if (s, r, "neutral") in mS}
    recH = {(s, r): mean_of(mH[(s, r, "neutral")]) for s in SLOTS for r in RELS if (s, r, "neutral") in mH}
    cueS = {r: mean_of(ctrlS[(r, "frame")]) for r in RELS}     # H1 predictor (frame-G² soundness)
    cueS_sent = {r: mean_of(ctrlS[(r, "sent")]) for r in RELS}
    cueH = {r: mean_of(ctrlH[(r, "frame")]) for r in RELS}     # control HIT (for antonymy-shadow residual)

    rep = {"relations": RELS, "n_per_rel": {r: len(order[r]) for r in RELS}, "pos": "adjective",
           "corpus": "C4 (allenai/c4 en, shards 00000-00002, ODC-BY)",
           "cue_strength_frame_soundness": {r: round(cueS[r], 4) for r in RELS},
           "cue_strength_sent_soundness": {r: round(cueS_sent[r], 4) for r in RELS},
           "recovery_soundness": {s: {r: round(recS.get((s, r), 0.0), 4) for r in RELS} for s in SLOTS},
           "recovery_hit": {s: {r: round(recH.get((s, r), 0.0), 4) for r in RELS} for s in SLOTS},
           "empties_neutral": {s: {r: missS.get((s, r, "neutral"), 0) for r in RELS} for s in SLOTS}}

    # ---- H1 across-relation decoupling (CO-PRIMARY, reported at true low power; C2 bands) ----
    def rho_cue(recov):
        return spearman([recov[r] for r in RELS], [cueS[r] for r in RELS])
    corr = {s: round(rho_cue({r: recS.get((s, r), 0.0) for r in RELS}), 3) for s in SLOTS}
    corrH = {s: round(rho_cue({r: recH.get((s, r), 0.0) for r in RELS}), 3) for s in SLOTS}

    def band(rc):
        if rc <= H1_REPL_MAX:
            return "REPLICATES"
        if rc > H1_BREAK_MIN:
            return "BREAKS"
        return "PARTIAL"
    h1_bands = {s: band(corr[s]) for s in SLOTS}
    n_repl = sum(1 for s in SLOTS if h1_bands[s] == "REPLICATES")
    n_break = sum(1 for s in SLOTS if h1_bands[s] == "BREAKS")
    H1 = ("DECOUPLING-REPLICATES" if n_repl >= MAJ else
          "DECOUPLING-BREAKS" if n_break >= MAJ else "H1-PARTIAL/AMBIGUOUS")

    # ---- calibration gate (C3): mean control-frame soundness over ALL cues ----
    all_ctrl_frame_S = []
    for r in RELS:
        all_ctrl_frame_S += [x for x in ctrlS[(r, "frame")].values() if x is not None]
    mean_ctrl_frame_S = sum(all_ctrl_frame_S) / len(all_ctrl_frame_S) if all_ctrl_frame_S else 0.0
    calib_fired = mean_ctrl_frame_S < CALIB_FLOOR   # True -> residual arm DESCRIPTIVE-ONLY

    # ---- antonymy-shadow PRIMARY (C6): HIT@3 residual per relation (neutral - control-frame) ----
    resid_hit = {}   # (slot, rel) -> (mean, lo, hi, n)
    for s in SLOTS:
        for r in RELS:
            if (s, r, "neutral") in mH:
                resid_hit[(s, r)] = residual_ci(mH[(s, r, "neutral")], ctrlH[(r, "frame")])
    # relation-agnostic RANK+MARGIN decision rule per model
    def ant_verdict(s):
        rv = {r: (resid_hit[(s, r)][0] if (s, r) in resid_hit else None) for r in RELS}
        if any(v is None for v in rv.values()):
            return "INCOMPLETE"
        vals = sorted(rv.values())
        med = (vals[1] + vals[2]) / 2.0            # median of 4
        ant = rv["antonymy"]
        is_min = ant <= min(rv[r] for r in RELS if r != "antonymy")
        if ant >= ANT_NEARZERO and ant >= med:
            return "CLEARS"                        # among the largest, clears the control
        if ant < ANT_NEARZERO and is_min:
            return "SATURATES"                     # near-zero AND the smallest — control reconstructs it
        return "MIDDLING"
    ant_per_model = {s: ant_verdict(s) for s in SLOTS}
    n_clear = sum(1 for s in SLOTS if ant_per_model[s] == "CLEARS")
    n_sat = sum(1 for s in SLOTS if ant_per_model[s] == "SATURATES")
    ANT = ("ANT-CLEARS-CONTROL" if n_clear >= MAJ else
           "ANT-SATURATES" if n_sat >= MAJ else "ANT-MIDDLING/MIXED")

    # ---- frame-ablation arm (C1 + C8): antonym HIT@3, neutral vs frame-present ----
    ablate = {}
    for s in SLOTS:
        nH = mean_of(mH[(s, "antonymy", "neutral")]) if (s, "antonymy", "neutral") in mH else None
        fH = mean_of(mH[(s, "antonymy", "frame")]) if (s, "antonymy", "frame") in mH else None
        survives = (nH is not None and fH is not None and nH >= fH - DELTA_ABLATE)
        ablate[s] = {"neutral_hit": round(nH, 4) if nH is not None else None,
                     "frame_hit": round(fH, 4) if fH is not None else None,
                     "survives_suppression": survives}
    n_survive = sum(1 for s in SLOTS if ablate[s]["survives_suppression"])
    ABLATE = "SURVIVES-SUPPRESSION" if n_survive >= MAJ else "FRAME-DEPENDENT"

    # ---- item-level SECONDARY (C7): pooled cue-strength(frame-G² soundness) -> recovery, per model ----
    item_level = {}
    for s in SLOTS:
        xs, ys = [], []
        for r in RELS:
            cf = ctrlS[(r, "frame")]
            mv = mS.get((s, r, "neutral"), {})
            for c in order[r]:
                cs, rs = cf.get(c), mv.get(c)
                if cs is not None and rs is not None:
                    xs.append(cs); ys.append(rs)
        item_level[s] = {"n": len(xs),
                         "rho_cuestrength_recovery": round(spearman(xs, ys), 3) if len(xs) > 2 else None}

    rep["headline"] = {
        "PRIMARY_antonymy_shadow": ANT,
        "antonymy_verdict_per_model": ant_per_model,
        "antonymy_hit_residual_per_model": {s: {r: (round(resid_hit[(s, r)][0], 4)
                                                    if (s, r) in resid_hit else None) for r in RELS} for s in SLOTS},
        "calibration_gate_fired": calib_fired, "mean_control_frame_soundness": round(mean_ctrl_frame_S, 4),
        "CALIB_FLOOR": CALIB_FLOOR,
        "frame_ablation": ABLATE, "frame_ablation_per_model": ablate,
        "H1_coprimary": H1, "H1_bands_per_model": h1_bands,
        "H1_rho_cue_soundness_per_model": corr, "H1_rho_cue_hit_per_model": corrH,
        "item_level_secondary_rho": {s: item_level[s]["rho_cuestrength_recovery"] for s in SLOTS},
        "thresholds": {"H1_REPL_MAX": H1_REPL_MAX, "H1_BREAK_MIN": H1_BREAK_MIN,
                       "CALIB_FLOOR": CALIB_FLOOR, "ANT_NEARZERO": ANT_NEARZERO,
                       "DELTA_ABLATE": DELTA_ABLATE, "MAJ": MAJ},
    }
    rep["antonymy_shadow_residual_ci"] = {
        s: {r: {"mean": round(resid_hit[(s, r)][0], 4), "lo": round(resid_hit[(s, r)][1], 4),
                "hi": round(resid_hit[(s, r)][2], 4), "n": resid_hit[(s, r)][3]}
            for r in RELS if (s, r) in resid_hit} for s in SLOTS}
    rep["item_level_secondary"] = {
        "NOTE": "DESCRIPTIVE/ROBUSTNESS-ONLY per Q1-C + C7 — NON-DECISIVE; cannot fire/break H1.",
        "per_model": item_level}

    json.dump(rep, open(HERE / "results.json", "w"), indent=1)
    _print(rep)


def _print(rep):
    h = rep["headline"]
    print("=" * 78)
    print("PRIMARY  antonymy-shadow:", h["PRIMARY_antonymy_shadow"], "| per model:", h["antonymy_verdict_per_model"])
    print("   antonymy HIT@3 residual per model:", h["antonymy_hit_residual_per_model"])
    print("   calibration gate fired:", h["calibration_gate_fired"],
          f"(mean control-frame 𝒮 ={h['mean_control_frame_soundness']}, floor {h['CALIB_FLOOR']})")
    print("   -> if fired, antonymy-shadow RESIDUAL arm is DESCRIPTIVE-ONLY; weight -> frame-ablation + H1")
    print("FRAME-ABLATION (corpus-free hedge):", h["frame_ablation"])
    for s in SLOTS:
        print(f"   {s}:", h["frame_ablation_per_model"][s])
    print("H1 co-primary (decoupling, <=4 relations — reported at true low power):", h["H1_coprimary"])
    print("   bands:", h["H1_bands_per_model"], "| rho_cue(soundness):", h["H1_rho_cue_soundness_per_model"],
          "| rho_cue(HIT):", h["H1_rho_cue_hit_per_model"])
    print("\nCue-strength (frame-G² 𝒮) per relation:", rep["cue_strength_frame_soundness"])
    print("Recovery (soundness) per model:")
    for s in SLOTS:
        print(f"   {s}:", rep["recovery_soundness"][s])
    print("Recovery (HIT@3) per model:")
    for s in SLOTS:
        print(f"   {s}:", rep["recovery_hit"][s])
    print("item-level SECONDARY (descriptive/non-decisive) rho:", h["item_level_secondary_rho"])
    print("empties (neutral) per model/rel:", rep["empties_neutral"])
    print("\nresults.json written.")


if __name__ == "__main__":
    main()
