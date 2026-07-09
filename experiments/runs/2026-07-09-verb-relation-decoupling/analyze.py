#!/usr/bin/env python3
"""analyze.py — scoring + H-verb-1 / H-verb-2 verdict for the VERB-relation decoupling probe.

Recomputes everything from raw/ + items.json + control.json. No threshold is tuned after seeing
results (anti-cheat); the verdict map is the one frozen in PREREG.md.

RATIFIED gates (s199) + conditions honored here:
- Q1-C: the ACROSS-RELATION result is the SOLE VERDICT OF RECORD for H1 (decoupling) and H2 (depth).
  The item-level cue/depth regression is DESCRIPTIVE/ROBUSTNESS-ONLY (reported, non-decisive).
- Q2-A: troponymy-depth (min_depth of the cue's first verb synset) is the SINGLE H2 proxy, predicted
  sign NEGATIVE. No corpus Hearst arm (Q2-C rejected).
- B1/B2 (the s199 ratifier's binding conditions): the depth-degeneracy verdict is frozen in items.json
  (b1_depth_spread.depth_degenerate, on the NON-antonymy CORE-4 mean-depth range vs DEGEN_MAX_RANGE).
  If DEGENERATE, H2 is under-powered SYMMETRICALLY: a DEPTH-FAILS is NON-falsifying/under-powered AND a
  DEPTH-OUT-PREDICTS is flagged under-powered, NOT banked as mechanistically equivalent to the noun H2.

Recovery 𝒮 (per relation) = mean raw SOUNDNESS (Cao precision-over-produced). HIT@3 the gold-size-
insensitive co-primary. Across-relation Spearman is TIE-NAIVE (the s186/s193 authoritative pipeline).
n=3 models, orderings not coefficients; VERBS only, never pooled across POS.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
ITEMS = json.load(open(HERE / "items.json"))
RELS = ITEMS["relations"]
SLOTS = ["A", "B", "C"]

# ---- FROZEN verdict thresholds (PREREG) ----
H1_REPL_MAX = 0.30     # rho_cue <= 0.30  -> DECOUPLING-REAPPEARS (near-zero or negative; the noun band)
H1_BREAK_MIN = 0.50    # rho_cue >  0.50  -> DECOUPLING-BREAKS (cue-strength recovers; the adjective band)
# (0.30, 0.50]         -> H1-INCONCLUSIVE (exhaustive, mutually exclusive; pre-named)
H2_MARGIN = 0.20       # |rho_depth| - |rho_cue| >= 0.20 AND predicted (negative) direction -> depth wins
MAJ = 2                # >=2/3 models


def soundness(produced, gold):
    if not produced:
        return None
    return sum(1 for w in produced if w in gold) / len(produced)


def hit(produced, gold):
    if not produced:
        return None
    return 1.0 if any(w in gold for w in produced) else 0.0


def spearman(a, b):
    """TIE-NAIVE Spearman (byte-identical to s186/s193 analyze.py)."""
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
    gold, order, depth = {}, {}, {}
    for r in RELS:
        order[r] = [it["cue"] for it in ITEMS["items"][r]]
        for it in ITEMS["items"][r]:
            gold[(r, it["cue"])] = set(it["gold"])
            depth[(r, it["cue"])] = it["trop_depth"]
    return gold, order, depth


def control_soundness_per_rel(order, gold):
    """cue-strength per relation = mean 𝒮(control top-3, frame variant) — the s186 clause-2 quantity."""
    ctrl = json.load(open(HERE / "control.json"))["cues"]
    out = {"frame": {}, "sent": {}}
    for variant in ("frame", "sent"):
        for r in RELS:
            vals = []
            for cue in order[r]:
                cand = [v for v, g, o in ctrl.get(cue, {}).get(variant, [])]
                s = soundness(cand, gold[(r, cue)])
                if s is not None:
                    vals.append(s)
            out[variant][r] = sum(vals) / len(vals) if vals else 0.0
    return out


def model_scores(gold, order, arm="neutral"):
    S, H, per_cue_S, miss = {}, {}, {}, {}
    for slot in SLOTS:
        for r in RELS:
            f = HERE / "raw" / f"{slot}-{r}-{arm}.json"
            if not f.exists():
                continue
            rows = json.load(open(f))
            sv, hv, pcs, empt = [], [], {}, 0
            for row in rows:
                if not row["words"]:
                    empt += 1
                s = soundness(row["words"], gold[(r, row["cue"])])
                h = hit(row["words"], gold[(r, row["cue"])])
                pcs[row["cue"]] = s
                if s is not None:
                    sv.append(s)
                if h is not None:
                    hv.append(h)
            S[(slot, r)] = sum(sv) / len(sv) if sv else 0.0
            H[(slot, r)] = sum(hv) / len(hv) if hv else 0.0
            per_cue_S[(slot, r)] = pcs
            miss[(slot, r)] = empt
    return S, H, per_cue_S, miss


def main():
    gold, order, depth = load_items()
    cs = control_soundness_per_rel(order, gold)
    S, H, per_cue_S, miss = model_scores(gold, order)

    b1 = ITEMS["b1_depth_spread"]
    depth_degenerate = b1["depth_degenerate"]

    # predictor vectors (frozen BEFORE recovery; per relation)
    cue_strength = [cs["frame"][r] for r in RELS]                                 # H1 predictor
    trop_depth = [ITEMS["profile"][r]["mean_trop_depth"] for r in RELS]           # H2 proxy

    rep = {"relations": RELS, "n_per_rel": {r: len(order[r]) for r in RELS},
           "corpus": "C4 (allenai/c4 en, shards 00000-00002, ODC-BY)",
           "cause_included": ITEMS["cause_included"], "cause_achieved_n": ITEMS["cause_achieved_n"],
           "b1_depth_spread": b1,
           "predictors": {"cue_strength_frame": dict(zip(RELS, [round(x, 4) for x in cue_strength])),
                          "mean_trop_depth": dict(zip(RELS, [round(x, 3) for x in trop_depth]))},
           "cue_strength_sent": {r: round(cs["sent"][r], 4) for r in RELS}}

    rep["recovery_soundness"] = {slot: {r: round(S[(slot, r)], 4) for r in RELS} for slot in SLOTS}
    rep["recovery_hit"] = {slot: {r: round(H[(slot, r)], 4) for r in RELS} for slot in SLOTS}
    rep["empties"] = {slot: {r: miss.get((slot, r), 0) for r in RELS} for slot in SLOTS}

    # ---- across-relation correlations, per model (PRIMARY = soundness recovery) ----
    def rhos(recov):
        return {"rho_cue": round(spearman(recov, cue_strength), 3),
                "rho_depth": round(spearman(recov, trop_depth), 3)}
    corr_S, corr_H = {}, {}
    for slot in SLOTS:
        corr_S[slot] = rhos([S[(slot, r)] for r in RELS])
        corr_H[slot] = rhos([H[(slot, r)] for r in RELS])
    rep["across_relation_soundness"] = corr_S
    rep["across_relation_hit"] = corr_H

    # ---- H1 verdict (exhaustive bands) on PRIMARY (soundness) ----
    def band(rc):
        if rc <= H1_REPL_MAX:
            return "REAPPEARS"
        if rc > H1_BREAK_MIN:
            return "BREAKS"
        return "INCONCLUSIVE"
    h1_bands = {slot: band(corr_S[slot]["rho_cue"]) for slot in SLOTS}
    n_repl = sum(1 for s in SLOTS if h1_bands[s] == "REAPPEARS")
    n_break = sum(1 for s in SLOTS if h1_bands[s] == "BREAKS")
    if n_repl >= MAJ:
        H1 = "DECOUPLING-REAPPEARS"
    elif n_break >= MAJ:
        H1 = "DECOUPLING-BREAKS"
    else:
        H1 = "H1-INCONCLUSIVE"

    # ---- H2 verdict (numeric margin; troponymy-depth predicted NEGATIVE) ----
    def depth_wins(c):
        rp = c["rho_depth"]
        return (rp < 0) and (abs(rp) - abs(c["rho_cue"]) >= H2_MARGIN)
    depth_win = {slot: depth_wins(corr_S[slot]) for slot in SLOTS}
    n_depth = sum(1 for s in SLOTS if depth_win[s])
    if n_depth >= MAJ:
        H2_raw = "DEPTH-OUT-PREDICTS"
    else:
        H2_raw = "DEPTH-FAILS"

    # ---- B1/B2 symmetric under-power gate ----
    if depth_degenerate:
        if H2_raw == "DEPTH-OUT-PREDICTS":
            H2 = ("DEPTH-OUT-PREDICTS (UNDER-POWERED — depth spread degenerate per B1; NOT banked as "
                  "mechanistically equivalent to the noun H2; possibly antonymy/cause-driven)")
        else:
            H2 = ("DEPTH-FAILS (UNDER-POWERED / NON-FALSIFYING per B1 — the non-antonymy CORE-4 depth "
                  "spread is degenerate; this does NOT fire conjecture-falsifier-2)")
    else:
        H2 = H2_raw + " (depth spread NON-degenerate; a real test)"

    # ---- item-level SECONDARY (Q1-C): DESCRIPTIVE/ROBUSTNESS-ONLY, NON-DECISIVE ----
    item_level = {}
    for slot in SLOTS:
        xs_c, ys, xs_d = [], [], []
        for r in RELS:
            pcs = per_cue_S[(slot, r)]
            for c in order[r]:
                s = pcs.get(c)
                d = depth[(r, c)]
                if s is None:
                    continue
                ys.append(s); xs_d.append(d if d is not None else 0)
        item_level[slot] = {"n": len(ys),
                            "rho_depth_recovery": round(spearman(xs_d, ys), 3) if len(ys) > 2 else None}
    rep["item_level_secondary"] = {
        "NOTE": "DESCRIPTIVE/ROBUSTNESS-ONLY per Q1-C — NON-DECISIVE; cannot fire H2 or upgrade an "
                "across-relation H2 result.",
        "per_model_rho_depth_vs_recovery": item_level}

    # ---- antonymy frame-ablation arm (descriptive hedge; condition 7) ----
    Sf, Hf, _, missf = model_scores(gold, order, arm="frame")
    ant_frame = {}
    for slot in SLOTS:
        if (slot, "antonymy") in Sf:
            ant_frame[slot] = {"neutral_soundness": round(S.get((slot, "antonymy"), 0.0), 4),
                               "frame_soundness": round(Sf[(slot, "antonymy")], 4)}
    rep["antonymy_frame_ablation"] = {
        "NOTE": "descriptive hedge (condition 7); frame-present vs neutral antonymy soundness — bears on "
                "the local antonymy-shadow reading, not on H1/H2.",
        "per_model": ant_frame}

    # calibration note (H1/H2 rank tests are corpus-control-independent; the residual arm was dropped)
    mean_ctrl_frame = round(sum(cs["frame"][r] for r in RELS) / len(RELS), 4)
    rep["calibration_note"] = {"mean_control_frame_soundness": mean_ctrl_frame,
                               "note": "H1/H2 are RANK tests over per-relation control soundness — well "
                                       "defined regardless of the residual-arm calibration floor."}

    rep["headline"] = {
        "H1": H1, "H1_bands_per_model": h1_bands,
        "H1_rho_cue_per_model": {s: corr_S[s]["rho_cue"] for s in SLOTS},
        "H2": H2, "H2_raw": H2_raw, "depth_degenerate": depth_degenerate,
        "H2_rho_depth_per_model": {s: corr_S[s]["rho_depth"] for s in SLOTS},
        "H2_depth_win_per_model": depth_win,
        "thresholds": {"H1_REPL_MAX": H1_REPL_MAX, "H1_BREAK_MIN": H1_BREAK_MIN,
                       "H2_MARGIN": H2_MARGIN, "MAJ": MAJ,
                       "DEGEN_MAX_RANGE": b1["degen_max_range"]},
    }

    json.dump(rep, open(HERE / "results.json", "w"), indent=1)
    _print(rep)


def _print(rep):
    print("=" * 74)
    print("H1:", rep["headline"]["H1"], "| bands:", rep["headline"]["H1_bands_per_model"])
    print("   rho_cue per model:", rep["headline"]["H1_rho_cue_per_model"])
    print("H2:", rep["headline"]["H2"])
    print("   rho_depth per model:", rep["headline"]["H2_rho_depth_per_model"], "(predicted NEG)")
    print("   depth-wins:", rep["headline"]["H2_depth_win_per_model"],
          "| depth spread degenerate (B1):", rep["headline"]["depth_degenerate"])
    print("\nPredictors per relation:")
    print("   cue-strength(frame):", rep["predictors"]["cue_strength_frame"])
    print("   troponymy-depth:    ", rep["predictors"]["mean_trop_depth"])
    print("\nRecovery (soundness) per model per relation:")
    for slot in SLOTS:
        print(f"   {slot}:", rep["recovery_soundness"][slot])
    print("Recovery (HIT@3) per model per relation:")
    for slot in SLOTS:
        print(f"   {slot}:", rep["recovery_hit"][slot])
    print("\nitem-level SECONDARY (descriptive/non-decisive):",
          {s: rep["item_level_secondary"]["per_model_rho_depth_vs_recovery"][s]["rho_depth_recovery"]
           for s in SLOTS})
    print("antonymy frame-ablation:", rep["antonymy_frame_ablation"]["per_model"])
    print("empties per model/rel:", rep["empties"])
    print("HIT co-primary across-relation rho_cue:",
          {s: rep["across_relation_hit"][s]["rho_cue"] for s in SLOTS})
    print("\nresults.json written.")


if __name__ == "__main__":
    main()
