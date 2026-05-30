"""Lexical v2 — polysemy vs homonymy re-analysis (2026-05-30). Pure-Python (no numpy).

Tests conjecture/lexical-sense-gradience clause (b) / prediction 2 — the conjecture's
*distinctive* still-untested bet:

  "there is an INTERMEDIATE REGIME for related-but-distinct (polysemous) usages that is
   ABSENT for homonyms (homonym pairs sit at the 'different' floor with little intermediate
   mass)."

NO NEW API SPEND. It re-uses the ALREADY-COLLECTED lexical-v1 model ratings
(experiments/runs/2026-05-30-lexical-sense-gradience-probe-v1/raw/{durel,cont}_{A,B,C}.json)
joined to the v1 manifest (item_id -> lemma, human_median), split by a FROZEN
etymology-grounded polysemy/homonymy stratification of the 43 DWUG EN lemmas
(stratification.csv, committed + sha256-frozen BEFORE this script is run; built from
etymological sources ALONE, blind to the per-pair model ratings — see README + the design
page for the no-retuning discipline and its honest limits).

Pre-registered reading (report-the-number; NO pass bar that manufactures a result):

  (b1) WITHIN-STRATUM monotonicity: Spearman(model sense, human DURel) computed separately
       for HOMONYM-lemma pairs and POLYSEMY-lemma pairs. Does the v1 monotonicity hold in
       BOTH regimes? (A sanity/decomposition of the v1 positive.)

  (b2) THE CLAUSE-(b) CONTRAST — discreteness/floor concentration. The conjecture predicts
       homonym pairs are treated more DISCRETELY ("different" floor) and polysemy pairs keep
       more INTERMEDIATE mass. Operationalized two ways, both matched on the HUMAN signal so
       a raw "homonyms are just more unrelated" difference is not mistaken for discreteness:
         - mean model rating per (stratum x human-level) cell, and the homonym - polysemy
           gap within each human level (negative => homonyms more floored at matched human
           relatedness = the predicted discreteness);
         - among LOW-human pairs (human_median <= LOW_CUT) the %-at-model-floor and mean
           model rating by stratum (homonym predicted lower mean / more floor mass).

  (b3) INTERMEDIATE-MASS precondition (item structure, model-free): the human DURel
       distribution by stratum. Clause (b) presupposes homonym lemmas are more BIMODAL
       (mass at 1 and 4, thin middle) than polysemy lemmas. Reported as the share of each
       stratum's pairs in the intermediate human band (2..3) vs the extremes.

  Uncertainty on the headline (b2) stratum gap: a label-permutation test (shuffle the
  stratum labels across lemmas, keep cluster structure by permuting WHOLE lemmas) gives a
  null distribution for the matched-human homonym-polysemy mean-rating gap.

Honest limits (stated in the result): the v1 ratings were already seen (this is a re-analysis,
not a fresh pre-registration); the discipline is that the STRATIFICATION is etymology-driven
and frozen before this pass, and the statistics here are fixed before computing. N per stratum
is small (esp. homonym pairs); treat as direction-of-effect, write the null first-class.
"""
import csv
import json
import math
import os
import random
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
V1 = os.path.abspath(os.path.join(HERE, "..", "2026-05-30-lexical-sense-gradience-probe-v1"))
V1_RAW = os.path.join(V1, "raw")
V1_MANIFEST = os.path.join(V1, "manifest.csv")
STRAT = os.path.join(HERE, "stratification.csv")
PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}

LOW_CUT = 2.0            # "low-human / unrelated end" = human_median <= 2.0
INTERMED_BAND = (2.0, 3.0)  # inclusive human-level band counted as "intermediate"
FLOOR = {"durel": 1, "cont": 20}  # model-floor threshold per framing (durel: exact 1)
SEED = 20260530
N_PERM = 5000


def ranks(z):
    order = sorted(range(len(z)), key=lambda i: z[i])
    r = [0.0] * len(z)
    i = 0
    while i < len(z):
        j = i
        while j + 1 < len(z) and z[order[j + 1]] == z[order[i]]:
            j += 1
        avg = (i + j) / 2 + 1
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def pearson(x, y):
    n = len(x)
    if n < 3:
        return None
    mx, my = sum(x) / n, sum(y) / n
    cov = sum((a - mx) * (b - my) for a, b in zip(x, y))
    vx = math.sqrt(sum((a - mx) ** 2 for a in x))
    vy = math.sqrt(sum((b - my) ** 2 for b in y))
    return cov / (vx * vy) if vx and vy else 0.0


def spearman(x, y):
    if len(x) < 3:
        return None
    return pearson(ranks(x), ranks(y))


def mean(v):
    return sum(v) / len(v) if v else None


def matched_human_gap(items, stratum_of, framing_key):
    """Mean (homonym - polysemy) model-rating gap, averaged over shared human levels
    (equal weight per level => matched on the human signal). Returns (gap, per_level)."""
    by = defaultdict(lambda: {"H": [], "P": []})
    for it in items:
        s = stratum_of.get(it["lemma"])
        if s not in ("HOMONYM", "POLYSEMY"):
            continue
        by[it["human"]]["H" if s == "HOMONYM" else "P"].append(it[framing_key])
    per_level = {}
    diffs = []
    for lvl in sorted(by):
        h, p = by[lvl]["H"], by[lvl]["P"]
        if h and p:
            d = mean(h) - mean(p)
            per_level[f"{lvl:.1f}"] = {"homonym_mean": round(mean(h), 2),
                                       "polysemy_mean": round(mean(p), 2),
                                       "gap": round(d, 2), "n_h": len(h), "n_p": len(p)}
            diffs.append(d)
    return (round(mean(diffs), 3) if diffs else None), per_level


def main():
    # ---- load frozen stratification ----
    strat_rows = list(csv.DictReader(open(STRAT)))
    stratum_of = {r["lemma"]: r["stratum"].strip().upper() for r in strat_rows}
    strat_counts = defaultdict(int)
    for s in stratum_of.values():
        strat_counts[s] += 1

    # ---- load v1 manifest (gold) ----
    man = {r["item_id"]: {"lemma": r["lemma"], "human": float(r["human_median"]),
                          "human_n": int(r["human_n"])}
           for r in csv.DictReader(open(V1_MANIFEST))}

    out = {"strat_counts": dict(strat_counts),
           "n_lemmas_classified": len(stratum_of),
           "n_items_total": len(man),
           "params": {"LOW_CUT": LOW_CUT, "INTERMED_BAND": INTERMED_BAND,
                      "FLOOR": FLOOR, "N_PERM": N_PERM, "SEED": SEED},
           "reading": "b1 within-stratum Spearman; b2 matched-human homonym-polysemy gap "
                      "(neg => homonyms more floored = discreteness) + low-end floor mass; "
                      "b3 human-DURel distribution by stratum (intermediate-mass precondition); "
                      "report-the-number, no pass bar",
           "per_model": {}}

    # items per stratum (model-free counts)
    items_by_strat = defaultdict(list)
    for iid, m in man.items():
        items_by_strat[stratum_of.get(m["lemma"], "UNCLASSIFIED")].append(m)

    # ---- b3 precondition: human-DURel structure by stratum (model-free) ----
    def human_struct(ms):
        levels = [m["human"] for m in ms]
        lo = sum(1 for x in levels if x <= LOW_CUT)
        hi = sum(1 for x in levels if x >= 3.5)
        mid = sum(1 for x in levels if INTERMED_BAND[0] <= x <= INTERMED_BAND[1])
        dist = defaultdict(int)
        for x in levels:
            dist[f"{x:.1f}"] += 1
        return {"n": len(ms), "mean_human": round(mean(levels), 2) if ms else None,
                "frac_low(<=2)": round(lo / len(ms), 3) if ms else None,
                "frac_intermediate(2..3)": round(mid / len(ms), 3) if ms else None,
                "frac_high(>=3.5)": round(hi / len(ms), 3) if ms else None,
                "human_dist": dict(sorted(dist.items()))}
    out["b3_human_structure_by_stratum"] = {
        s: human_struct(items_by_strat[s]) for s in ("HOMONYM", "POLYSEMY")
        if items_by_strat[s]}

    # ---- per model: load preds, build joined items ----
    rng = random.Random(SEED)
    for slot, name in PANEL.items():
        preds = {}
        for fr in ("durel", "cont"):
            preds[fr] = {r["item_id"]: r["pred"]
                         for r in json.load(open(os.path.join(V1_RAW, f"{fr}_{slot}.json")))
                         if r.get("pred") is not None}
        m = {"model": name}
        for fr in ("durel", "cont"):
            items = [{"lemma": man[i]["lemma"], "human": man[i]["human"], fr: preds[fr][i]}
                     for i in man if i in preds[fr]
                     and stratum_of.get(man[i]["lemma"]) in ("HOMONYM", "POLYSEMY")]
            cell = {"n_used": len(items)}

            # b1 within-stratum Spearman + overall
            for s in ("HOMONYM", "POLYSEMY"):
                sub = [it for it in items if stratum_of[it["lemma"]] == s]
                sense = [it[fr] for it in sub]
                human = [it["human"] for it in sub]
                rho = spearman(sense, human)
                cell[f"rho_{s.lower()}"] = (round(rho, 3) if rho is not None else None)
                cell[f"n_{s.lower()}"] = len(sub)

            # b2 matched-human gap
            gap, per_level = matched_human_gap(items, stratum_of, fr)
            cell["matched_human_gap(H-P)"] = gap
            cell["gap_per_human_level"] = per_level

            # b2 low-end floor mass
            for s in ("HOMONYM", "POLYSEMY"):
                low = [it[fr] for it in items
                       if stratum_of[it["lemma"]] == s and it["human"] <= LOW_CUT]
                if low:
                    fl = sum(1 for v in low if (v == FLOOR["durel"] if fr == "durel"
                                                else v <= FLOOR["cont"]))
                    cell[f"low_{s.lower()}"] = {"n": len(low), "mean": round(mean(low), 2),
                                                "frac_at_floor": round(fl / len(low), 3)}

            # b2 permutation null for the matched-human gap (permute WHOLE lemmas' labels)
            if gap is not None:
                lemmas = sorted(set(it["lemma"] for it in items))
                labels = [stratum_of[l] for l in lemmas]
                n_h = labels.count("HOMONYM")
                ge = 0
                valid = 0
                for _ in range(N_PERM):
                    perm = labels[:]
                    rng.shuffle(perm)
                    pmap = dict(zip(lemmas, perm))
                    g, _pl = matched_human_gap(items, pmap, fr)
                    if g is not None:
                        valid += 1
                        if abs(g) >= abs(gap):
                            ge += 1
                cell["perm_two_sided_p"] = round(ge / valid, 4) if valid else None
                cell["perm_n_homonym_lemmas"] = n_h

            m[fr] = cell
        out["per_model"][slot] = m

    json.dump(out, open(os.path.join(HERE, "raw", "results.json"), "w"), indent=1)

    # ---- console summary ----
    print(f"\n===== LEXICAL v2 — polysemy vs homonymy (clause b) =====")
    print(f"stratification: {dict(strat_counts)}  ({len(stratum_of)} lemmas)")
    print(f"b3 human structure by stratum:")
    for s, d in out["b3_human_structure_by_stratum"].items():
        print(f"  {s:9s} n={d['n']:3d}  mean_human={d['mean_human']}  "
              f"low={d['frac_low(<=2)']} mid={d['frac_intermediate(2..3)']} "
              f"high={d['frac_high(>=3.5)']}")
    for slot, name in PANEL.items():
        print(f"\n[{name}]")
        for fr in ("durel", "cont"):
            c = out["per_model"][slot][fr]
            print(f"  {fr:5s} n={c['n_used']:3d}  "
                  f"rho_homonym={c['rho_homonym']}(n={c['n_homonym']}) "
                  f"rho_polysemy={c['rho_polysemy']}(n={c['n_polysemy']})  "
                  f"matched_gap(H-P)={c['matched_human_gap(H-P)']} "
                  f"perm_p={c.get('perm_two_sided_p')}")
            if c.get("low_homonym") and c.get("low_polysemy"):
                lh, lp = c["low_homonym"], c["low_polysemy"]
                print(f"        low-end(<= {LOW_CUT}): homonym mean={lh['mean']} "
                      f"floor={lh['frac_at_floor']}(n={lh['n']}) | "
                      f"polysemy mean={lp['mean']} floor={lp['frac_at_floor']}(n={lp['n']})")
    print(f"\nwrote {os.path.join(HERE, 'raw', 'results.json')}")


if __name__ == "__main__":
    main()
