#!/usr/bin/env python3
"""analyze.py — scoring + H1/H2 verdict for the FRESH relation-recovery / taxonomic-proxy probe.

Recomputes everything from raw/ + items.json + control.json + hearst.json. No threshold is tuned
after seeing results (anti-cheat); the verdict map is the one frozen in PREREG.md.

RATIFIED gates (s193) + six freeze-time conditions honored here:
- Q1-C / condition 1: the ACROSS-RELATION (n=6) result is the SOLE VERDICT OF RECORD for H1 and H2.
  The item-level cue-depth regression is DESCRIPTIVE/ROBUSTNESS-ONLY (reported, flagged non-decisive,
  can never fire H2 or upgrade an across-relation H2-loss).
- condition 2: exhaustive, mutually-exclusive H1 bands (no uncovered middle) + a NUMERIC H2 margin.
- condition 5 / Q3-A: IS-A depth PRIMARY (predicted sign NEGATIVE); the corpus Hearst proxy SECONDARY
  (predicted sign POSITIVE); a Hearst-only H2 win is reported QUALIFIED/WEAKER, never equal-status.

Recovery 𝒮 (per relation) = mean raw SOUNDNESS (Cao precision-over-produced) over the relation's cues
— the exact quantity the essay's clause 2 and the pilot use (the −0.086 pipeline). HIT@3 is the
gold-size-insensitive CO-PRIMARY carried from s186. Across-relation Spearman is TIE-NAIVE, matching
the authoritative s186 pipeline (the pilot notes tie-corrected gives a slightly larger |ρ|; tie-naive
is the s186 figure of record). n=3 models, orderings not coefficients; nouns only.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
RELS = ["antonymy", "synonymy", "hypernymy", "hyponymy", "holonymy", "meronymy"]
SLOTS = ["A", "B", "C"]

# ---- FROZEN verdict thresholds (PREREG; condition 2) ----
H1_REPL_MAX = 0.30     # rho_cue <= 0.30  -> DECOUPLING-REPLICATES (near-zero or negative)
H1_BREAK_MIN = 0.50    # rho_cue >  0.50  -> DECOUPLING-BREAKS (cue-strength clearly recovers)
# (0.30, 0.50]         -> H1-PARTIAL/AMBIGUOUS  (exhaustive, mutually exclusive; pre-named)
H2_MARGIN = 0.20       # |rho_proxy| - |rho_cue| >= 0.20 AND predicted direction -> proxy wins
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
    """TIE-NAIVE Spearman (byte-identical to s186 analyze.py — the authoritative −0.086 pipeline)."""
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
    gold, order, depth = {}, {}, {}
    for r in RELS:
        order[r] = [it["cue"] for it in items["items"][r]]
        for it in items["items"][r]:
            gold[(r, it["cue"])] = set(it["gold"])
            depth[(r, it["cue"])] = it["is_a_depth"]
    return items, gold, order, depth


def control_soundness_per_rel(order, gold):
    """cue-strength per relation = mean 𝒮(control top-3, frame variant) — s186 clause-2 quantity."""
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


def model_scores(gold, order):
    """per (slot, rel): mean raw soundness, mean hit, per-cue soundness dict, empties."""
    S, H, per_cue_S, miss = {}, {}, {}, {}
    for slot in SLOTS:
        for r in RELS:
            f = HERE / "raw" / f"{slot}-{r}-neutral.json"
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
    items, gold, order, depth = load_items()
    cs = control_soundness_per_rel(order, gold)
    hearst = json.load(open(HERE / "hearst.json"))["hearst_density"]
    S, H, per_cue_S, miss = model_scores(gold, order)

    # predictor vectors (frozen BEFORE recovery; per relation)
    cue_strength = [cs["frame"][r] for r in RELS]           # H1 predictor
    isa_depth = [items["profile"][r]["mean_is_a_depth"] for r in RELS]   # H2 primary proxy
    hearst_dens = [sum(hearst[c] for c in order[r]) / len(order[r]) for r in RELS]  # H2 second arm

    rep = {"relations": RELS, "n_per_rel": {r: len(order[r]) for r in RELS},
           "corpus": "C4 (allenai/c4 en, shards 00000-00002, ODC-BY)",
           "predictors": {"cue_strength_frame": dict(zip(RELS, [round(x, 4) for x in cue_strength])),
                          "isa_depth": dict(zip(RELS, [round(x, 3) for x in isa_depth])),
                          "hearst_density": dict(zip(RELS, [round(x, 4) for x in hearst_dens]))},
           "cue_strength_sent": {r: round(cs["sent"][r], 4) for r in RELS}}

    # recovery vectors per model (SOUNDNESS primary, HIT co-primary)
    rep["recovery_soundness"] = {slot: {r: round(S[(slot, r)], 4) for r in RELS} for slot in SLOTS}
    rep["recovery_hit"] = {slot: {r: round(H[(slot, r)], 4) for r in RELS} for slot in SLOTS}
    rep["empties"] = {slot: {r: miss.get((slot, r), 0) for r in RELS} for slot in SLOTS}

    # ---- across-relation correlations, per model (PRIMARY = soundness recovery) ----
    def rhos(recov):
        return {"rho_cue": round(spearman(recov, cue_strength), 3),
                "rho_depth": round(spearman(recov, isa_depth), 3),
                "rho_hearst": round(spearman(recov, hearst_dens), 3)}
    corr_S, corr_H = {}, {}
    for slot in SLOTS:
        corr_S[slot] = rhos([S[(slot, r)] for r in RELS])
        corr_H[slot] = rhos([H[(slot, r)] for r in RELS])
    rep["across_relation_soundness"] = corr_S
    rep["across_relation_hit"] = corr_H

    # ---- H1 verdict (exhaustive bands; condition 2) on PRIMARY (soundness) ----
    def band(rc):
        if rc <= H1_REPL_MAX:
            return "REPLICATES"
        if rc > H1_BREAK_MIN:
            return "BREAKS"
        return "PARTIAL"
    h1_bands = {slot: band(corr_S[slot]["rho_cue"]) for slot in SLOTS}
    n_repl = sum(1 for s in SLOTS if h1_bands[s] == "REPLICATES")
    n_break = sum(1 for s in SLOTS if h1_bands[s] == "BREAKS")
    if n_repl >= MAJ:
        H1 = "DECOUPLING-REPLICATES"
    elif n_break >= MAJ:
        H1 = "DECOUPLING-BREAKS"
    else:
        H1 = "H1-PARTIAL/AMBIGUOUS"

    # ---- H2 verdict (numeric margin; IS-A depth PRIMARY neg; Hearst SECONDARY pos) ----
    def proxy_wins(c, proxy, sign):
        rp = c[f"rho_{proxy}"]
        dir_ok = (rp < 0) if sign == "neg" else (rp > 0)
        return dir_ok and (abs(rp) - abs(c["rho_cue"]) >= H2_MARGIN)
    depth_win = {slot: proxy_wins(corr_S[slot], "depth", "neg") for slot in SLOTS}
    hearst_win = {slot: proxy_wins(corr_S[slot], "hearst", "pos") for slot in SLOTS}
    n_depth = sum(1 for s in SLOTS if depth_win[s])
    n_hearst = sum(1 for s in SLOTS if hearst_win[s])
    if n_depth >= MAJ:
        H2 = "TAXONOMIC-PROXY-WINS (IS-A depth, primary)"
    elif n_hearst >= MAJ:
        H2 = "TAXONOMIC-PROXY-WINS-QUALIFIED (Hearst only; IS-A depth did not win — weaker)"
    else:
        H2 = "TAXONOMIC-PROXY-LOSES"

    # ---- item-level SECONDARY (Q1-C / condition 1): DESCRIPTIVE/ROBUSTNESS-ONLY, NON-DECISIVE ----
    # within-cue: does a cue's own IS-A depth predict its own recovery? pooled across relations.
    item_level = {}
    for slot in SLOTS:
        xs, ys = [], []
        for r in RELS:
            pcs = per_cue_S[(slot, r)]
            for c in order[r]:
                d = depth[(r, c)]
                s = pcs.get(c)
                if d is not None and s is not None:
                    xs.append(d); ys.append(s)
        item_level[slot] = {"n": len(xs),
                            "rho_depth_recovery": round(spearman(xs, ys), 3) if len(xs) > 2 else None}
    rep["item_level_secondary"] = {
        "NOTE": "DESCRIPTIVE/ROBUSTNESS-ONLY per Q1-C + freeze-condition 1 — NON-DECISIVE; "
                "cannot fire H2 or upgrade an across-relation H2-loss.",
        "per_model_rho_depth_vs_recovery": item_level}

    rep["headline"] = {
        "H1": H1, "H1_bands_per_model": h1_bands,
        "H1_rho_cue_per_model": {s: corr_S[s]["rho_cue"] for s in SLOTS},
        "H2": H2,
        "H2_rho_depth_per_model": {s: corr_S[s]["rho_depth"] for s in SLOTS},
        "H2_rho_hearst_per_model": {s: corr_S[s]["rho_hearst"] for s in SLOTS},
        "H2_depth_win_per_model": depth_win, "H2_hearst_win_per_model": hearst_win,
        "level_divergence": None,  # filled below
        "thresholds": {"H1_REPL_MAX": H1_REPL_MAX, "H1_BREAK_MIN": H1_BREAK_MIN,
                       "H2_MARGIN": H2_MARGIN, "MAJ": MAJ},
    }
    # level-divergence flag (condition 1: a first-class outcome, reported not resolved)
    il = [item_level[s]["rho_depth_recovery"] for s in SLOTS if item_level[s]["rho_depth_recovery"] is not None]
    across_depth_neg = sum(1 for s in SLOTS if corr_S[s]["rho_depth"] < 0) >= MAJ
    item_depth_neg = sum(1 for v in il if v is not None and v < 0) >= MAJ
    rep["headline"]["level_divergence"] = (across_depth_neg != item_depth_neg)

    json.dump(rep, open(HERE / "results.json", "w"), indent=1)
    _print(rep)


def _print(rep):
    print("=" * 74)
    print("H1:", rep["headline"]["H1"], "| bands:", rep["headline"]["H1_bands_per_model"])
    print("   rho_cue per model:", rep["headline"]["H1_rho_cue_per_model"])
    print("H2:", rep["headline"]["H2"])
    print("   rho_depth per model:", rep["headline"]["H2_rho_depth_per_model"], "(predicted NEG)")
    print("   rho_hearst per model:", rep["headline"]["H2_rho_hearst_per_model"], "(predicted POS)")
    print("   depth-wins:", rep["headline"]["H2_depth_win_per_model"],
          "| hearst-wins:", rep["headline"]["H2_hearst_win_per_model"])
    print("   level-divergence (across vs item-level depth sign):", rep["headline"]["level_divergence"])
    print("\nPredictors per relation:")
    print("   cue-strength(frame):", rep["predictors"]["cue_strength_frame"])
    print("   IS-A depth:         ", rep["predictors"]["isa_depth"])
    print("   Hearst density:     ", rep["predictors"]["hearst_density"])
    print("\nRecovery (soundness) per model per relation:")
    for slot in SLOTS:
        print(f"   {slot}:", rep["recovery_soundness"][slot])
    print("Recovery (HIT@3) per model per relation:")
    for slot in SLOTS:
        print(f"   {slot}:", rep["recovery_hit"][slot])
    print("\nitem-level SECONDARY (descriptive/non-decisive):",
          {s: rep["item_level_secondary"]["per_model_rho_depth_vs_recovery"][s]["rho_depth_recovery"]
           for s in SLOTS})
    print("empties per model/rel:", rep["empties"])
    print("HIT co-primary across-relation rho_cue:",
          {s: rep["across_relation_hit"][s]["rho_cue"] for s in SLOTS})
    print("\nresults.json written.")


if __name__ == "__main__":
    main()
