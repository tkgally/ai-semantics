#!/usr/bin/env python3
"""Lancaster perceptual-strength moderation of the lexical-v1 monotonicity result.

Pure stdlib (no numpy/scipy — project constraint). Reads the frozen lexical-v1 raw
ratings + manifest + the lemma_perceptual.csv join table; writes raw/results.json.

Tests (see PREREG.md):
  T1  median-split stratified Spearman rho(model, human), Delta = HIGH - LOW,
      cluster-bootstrap CI (resample lemmas).
  T2  lemma-level Spearman rho(MAE, perceptual strength) across 42 lemmas.
  T3  same with Visual.mean.
"""
import csv, json, os, random, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
V1RAW = os.path.join(ROOT, "experiments/runs/2026-05-30-lexical-sense-gradience-probe-v1/raw")
JOIN = os.path.join(HERE, "lemma_perceptual.csv")

MODELS = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
FRAMINGS = ["durel", "cont"]
SCALE = {"durel": (1.0, 4.0), "cont": (0.0, 100.0)}  # model-pred scale per framing (T2 norm)
HUMAN_SCALE = (1.0, 4.0)  # B1 fix: human gold is ALWAYS the DURel median on 1-4, every framing
SEED = 20260530
NBOOT = 10000


# ---------- statistics (stdlib) ----------
def rankdata(xs):
    """Average-rank (ties shared)."""
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(xs):
        j = i
        while j + 1 < len(xs) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def pearson(xs, ys):
    n = len(xs)
    if n < 2:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    sx = sum((x - mx) ** 2 for x in xs)
    sy = sum((y - my) ** 2 for y in ys)
    if sx == 0 or sy == 0:
        return None
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return cov / (sx ** 0.5 * sy ** 0.5)


def spearman(xs, ys):
    if len(xs) < 2:
        return None
    return pearson(rankdata(xs), rankdata(ys))


def pct(vals, p):
    vals = sorted(vals)
    if not vals:
        return None
    k = (len(vals) - 1) * p
    lo, hi = int(k), min(int(k) + 1, len(vals) - 1)
    return vals[lo] + (vals[hi] - vals[lo]) * (k - lo)


# ---------- load ----------
def load():
    # join table
    perc = {}
    for r in csv.DictReader(open(JOIN, newline="")):
        if r["covered"] == "1":
            perc[r["lemma"]] = {
                "Max_strength.perceptual": float(r["Max_strength.perceptual"]),
                "Visual.mean": float(r["Visual.mean"]),
            }
    # ratings: item_id -> {model -> {framing -> pred}} ; plus human + lemma
    items = {}
    for fr in FRAMINGS:
        for code in MODELS:
            data = json.load(open(os.path.join(V1RAW, f"{fr}_{code}.json")))
            for row in data:
                it = items.setdefault(row["item_id"], {
                    "lemma": row["lemma"], "human": float(row["human_median"]),
                    "human_n": int(row["human_n"]), "pred": {}})
                it["pred"].setdefault(code, {})[fr] = float(row["pred"])
    return perc, items


# ---------- analysis ----------
def stratified(items, perc, moderator, code, fr, min_n=1):
    """Return (rho_high, rho_low, n_high, n_low, med) pooled within median-split strata."""
    covered = {lem: v[moderator] for lem, v in perc.items()}
    med = statistics.median(sorted(covered.values()))
    hi_m, hi_h, lo_m, lo_h = [], [], [], []
    for it in items.values():
        lem = it["lemma"]
        if lem not in covered:
            continue
        if code not in it["pred"] or fr not in it["pred"][code]:
            continue
        if it.get("human_n", 99) < min_n:
            continue
        m, h = it["pred"][code][fr], it["human"]
        if covered[lem] > med:
            hi_m.append(m); hi_h.append(h)
        else:
            lo_m.append(m); lo_h.append(h)
    return (spearman(hi_m, hi_h), spearman(lo_m, lo_h), len(hi_m), len(lo_m), med)


def cluster_bootstrap_delta(items, perc, moderator, code, fr, med):
    """Resample lemmas with replacement; recompute Delta rho = rho_high - rho_low."""
    covered = {lem: v[moderator] for lem, v in perc.items()}
    # group pairs by lemma
    bylem = {}
    for it in items.values():
        lem = it["lemma"]
        if lem not in covered:
            continue
        if code not in it["pred"] or fr not in it["pred"][code]:
            continue
        bylem.setdefault(lem, []).append((it["pred"][code][fr], it["human"]))
    lemmas = list(bylem.keys())
    rng = random.Random(SEED)
    deltas = []
    for _ in range(NBOOT):
        samp = [lemmas[rng.randrange(len(lemmas))] for _ in lemmas]
        hi_m, hi_h, lo_m, lo_h = [], [], [], []
        for lem in samp:
            tgt_m, tgt_h = (hi_m, hi_h) if covered[lem] > med else (lo_m, lo_h)
            for m, h in bylem[lem]:
                tgt_m.append(m); tgt_h.append(h)
        rh, rl = spearman(hi_m, hi_h), spearman(lo_m, lo_h)
        if rh is not None and rl is not None:
            deltas.append(rh - rl)
    return pct(deltas, 0.025), pct(deltas, 0.975), len(deltas)


def lemma_level_mae(items, perc, moderator, code, fr, min_n=1):
    """T2: Spearman(lemma MAE, lemma perceptual strength) across covered lemmas.

    B1 fix: the model pred is normalized on its framing's scale (SCALE[fr]); the human
    gold is ALWAYS normalized on the DURel (1,4) scale (HUMAN_SCALE), because the gold is
    the DURel median on 1-4 in every framing. min_n filters to pairs with >= min_n raters.
    """
    mlo, mhi = SCALE[fr]
    hlo, hhi = HUMAN_SCALE

    def mnorm(v):
        return (v - mlo) / (mhi - mlo)

    def hnorm(v):
        return (v - hlo) / (hhi - hlo)

    bylem = {}
    for it in items.values():
        lem = it["lemma"]
        if lem not in perc:
            continue
        if code not in it["pred"] or fr not in it["pred"][code]:
            continue
        if it.get("human_n", 99) < min_n:
            continue
        err = abs(mnorm(it["pred"][code][fr]) - hnorm(it["human"]))
        bylem.setdefault(lem, []).append(err)
    xs, ys, rows = [], [], []
    for lem, errs in bylem.items():
        mae = sum(errs) / len(errs)
        ps = perc[lem][moderator]
        xs.append(ps); ys.append(mae)
        rows.append({"lemma": lem, "n": len(errs), "perc": ps, "mae": round(mae, 4)})
    return spearman(xs, ys), len(xs), rows


def confounds(items, perc):
    """Input-only confound checks (no model outputs): does the moderator track pairs/lemma,
    annotator count, human spread, or its own Visual sibling? (critic S1/S4/N1)."""
    bylem = {}
    for it in items.values():
        lem = it["lemma"]
        if lem not in perc:
            continue
        d = bylem.setdefault(lem, {"n": 0, "hn": [], "hvals": []})
        d["n"] += 1
        d["hn"].append(it["human_n"])
        d["hvals"].append(it["human"])
    lems = list(bylem.keys())
    pv = [perc[l]["Max_strength.perceptual"] for l in lems]
    npairs = [bylem[l]["n"] for l in lems]
    mean_hn = [sum(bylem[l]["hn"]) / len(bylem[l]["hn"]) for l in lems]
    spread = [(statistics.pstdev(bylem[l]["hvals"]) if len(bylem[l]["hvals"]) > 1 else 0.0)
              for l in lems]
    vis = [perc[l]["Visual.mean"] for l in lems]
    n_identical = sum(1 for l in lems
                      if abs(perc[l]["Max_strength.perceptual"] - perc[l]["Visual.mean"]) < 1e-9)
    return {
        "n_lemmas": len(lems),
        "rho_perc_vs_npairs": round(spearman(pv, npairs), 4),
        "rho_perc_vs_mean_human_n": round(spearman(pv, mean_hn), 4),
        "rho_perc_vs_human_spread": round(spearman(pv, spread), 4),
        "rho_perc_vs_visual": round(spearman(pv, vis), 4),
        "n_lemmas_perc_eq_visual": n_identical,
    }


def main():
    perc, items = load()
    out = {"n_items_total": len(items),
           "n_lemmas_covered": len(perc),
           "moderators": ["Max_strength.perceptual", "Visual.mean"],
           "primary_cell": "Max_strength.perceptual x durel x {A,B,C}, T1 (all else exploratory)",
           "confounds": confounds(items, perc),
           "T1": {}, "T2": {},
           "robustness_n_ge_3": {}}
    for moderator in ["Max_strength.perceptual", "Visual.mean"]:
        out["T1"][moderator] = {}
        out["T2"][moderator] = {}
        for fr in FRAMINGS:
            for code, name in MODELS.items():
                rh, rl, nh, nl, med = stratified(items, perc, moderator, code, fr)
                clo, chi, nboot = cluster_bootstrap_delta(items, perc, moderator, code, fr, med)
                out["T1"][moderator][f"{name}|{fr}"] = {
                    "rho_high": round(rh, 4), "rho_low": round(rl, 4),
                    "delta": round(rh - rl, 4), "n_high": nh, "n_low": nl,
                    "median_split": round(med, 4),
                    "delta_ci95": [round(clo, 4), round(chi, 4)], "nboot": nboot,
                }
                rho, nlem, lemrows = lemma_level_mae(items, perc, moderator, code, fr)
                out["T2"][moderator][f"{name}|{fr}"] = {
                    "rho_mae_perc": round(rho, 4), "n_lemmas": nlem,
                }
                if moderator == "Max_strength.perceptual" and fr == "durel" and code == "C":
                    out["T2"]["_example_lemma_rows_gemini_durel"] = sorted(
                        lemrows, key=lambda r: -r["perc"])

    # robustness: primary cell-set restricted to pairs with >=3 annotators (critic S4)
    for fr in FRAMINGS:
        for code, name in MODELS.items():
            rh, rl, nh, nl, med = stratified(items, perc, "Max_strength.perceptual",
                                             code, fr, min_n=3)
            rho, nlem, _ = lemma_level_mae(items, perc, "Max_strength.perceptual",
                                           code, fr, min_n=3)
            out["robustness_n_ge_3"][f"{name}|{fr}"] = {
                "T1_rho_high": round(rh, 4) if rh is not None else None,
                "T1_rho_low": round(rl, 4) if rl is not None else None,
                "T1_delta": round(rh - rl, 4) if (rh is not None and rl is not None) else None,
                "n_high": nh, "n_low": nl,
                "T2_rho_mae_perc": round(rho, 4) if rho is not None else None,
                "n_lemmas": nlem,
            }
    os.makedirs(os.path.join(HERE, "raw"), exist_ok=True)
    json.dump(out, open(os.path.join(HERE, "raw/results.json"), "w"), indent=1)
    # console summary
    print(f"items {out['n_items_total']}  covered lemmas {out['n_lemmas_covered']}")
    for moderator in out["moderators"]:
        print(f"\n=== moderator: {moderator} ===")
        print(f"{'model|framing':28}{'rhoHI':>7}{'rhoLO':>7}{'Δ':>7}  {'Δ CI95':>18}   {'T2 rho(MAE,perc)':>17}")
        for k in out["T1"][moderator]:
            t1 = out["T1"][moderator][k]; t2 = out["T2"][moderator][k]
            ci = f"[{t1['delta_ci95'][0]:+.2f},{t1['delta_ci95'][1]:+.2f}]"
            print(f"{k:28}{t1['rho_high']:7.3f}{t1['rho_low']:7.3f}{t1['delta']:+7.3f}  {ci:>18}   {t2['rho_mae_perc']:+17.3f}")


if __name__ == "__main__":
    main()
