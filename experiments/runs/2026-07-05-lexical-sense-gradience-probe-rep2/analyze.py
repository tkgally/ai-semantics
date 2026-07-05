"""Analyze the lexical-sense-gradience v1 probe (2026-05-30). Pure-Python stats (no numpy).

P1 monotonicity: Spearman rho between the model's sense-relatedness rating and the human DURel
median, per model, per framing (durel 1-4, cont 0-100).
P3 context control (clause c): partial Spearman of (model sense, human DURel) controlling for
  (a) lexical overlap [independent, surface] and (b) the model's own topic-similarity rating
  [semantic, model-internal]. If the monotonicity survives both partials, that supports
  graded-sense tracking over a context-similarity shadow.
Also: Spearman(model sense, model topic) = how much the sense rating conflates with topic;
per-human-level mean ratings (the monotonic table); bootstrap 95% CI on the headline rho.
Joins committed raw preds to manifest.csv (gold + overlap covariate) by item_id. No tuning.
"""
import csv
import json
import math
import os
import random
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
MANIFEST = os.path.join(HERE, "manifest.csv")
PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}


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
    return pearson(ranks(x), ranks(y))


def partial(rxy, rxz, ryz):
    d = (1 - rxz ** 2) * (1 - ryz ** 2)
    return (rxy - rxz * ryz) / math.sqrt(d) if d > 0 else None


def boot_ci(x, y, n_boot=2000, seed=20260530):
    rng = random.Random(seed)
    n = len(x)
    rs = []
    for _ in range(n_boot):
        idx = [rng.randrange(n) for _ in range(n)]
        rs.append(spearman([x[i] for i in idx], [y[i] for i in idx]))
    rs.sort()
    return round(rs[int(0.025 * n_boot)], 3), round(rs[int(0.975 * n_boot)], 3)


def main():
    man = {r["item_id"]: {"overlap": float(r["overlap_jaccard"]),
                          "human": float(r["human_median"]), "human_n": int(r["human_n"])}
           for r in csv.DictReader(open(MANIFEST))}
    out = {"per_model": {}, "n_items": len(man),
           "reading_rule": "P1 Spearman(model sense, human DURel); P3 partial Spearman "
           "controlling for lexical overlap and model topic-similarity; report-the-correlation"}
    print(f"\n===== LEXICAL-SENSE-GRADIENCE v1 — monotonicity + context controls (n={len(man)}) =====\n")
    for slot, name in PANEL.items():
        preds = {}
        for fr in ("durel", "cont", "topic"):
            preds[fr] = {r["item_id"]: r["pred"]
                         for r in json.load(open(os.path.join(RAW, f"{fr}_{slot}.json")))}
        m = {"model": name}
        topic_map = preds["topic"]
        for sense_fr in ("durel", "cont"):
            ids = [i for i in man
                   if preds[sense_fr].get(i) is not None
                   and topic_map.get(i) is not None]
            sense = [preds[sense_fr][i] for i in ids]
            human = [man[i]["human"] for i in ids]
            overlap = [man[i]["overlap"] for i in ids]
            topic = [topic_map[i] for i in ids]
            r_sh = spearman(sense, human)
            r_so, r_ho = spearman(sense, overlap), spearman(human, overlap)
            r_st, r_ht = spearman(sense, topic), spearman(human, topic)
            ci = boot_ci(sense, human)
            # S3 robustness: rho on the higher-reliability subset (>=3 annotators)
            ids3 = [i for i in ids if man[i]["human_n"] >= 3]
            r_sh3 = (round(spearman([preds[sense_fr][i] for i in ids3],
                                    [man[i]["human"] for i in ids3]), 3)
                     if len(ids3) >= 10 else None)
            cell = {"n": len(ids), "rho_sense_human": round(r_sh, 3), "rho_ci95": ci,
                    "partial_ctrl_overlap": round(partial(r_sh, r_so, r_ho), 3),
                    "partial_ctrl_topic": round(partial(r_sh, r_st, r_ht), 3),
                    "rho_sense_topic": round(r_st, 3),
                    "rho_sense_human_n>=3": r_sh3, "n_ge3": len(ids3),
                    "na": sum(1 for i in man if preds[sense_fr].get(i) is None)}
            # per-human-level mean sense rating (monotonic table)
            bylvl = defaultdict(list)
            for i in ids:
                bylvl[man[i]["human"]].append(preds[sense_fr][i])
            cell["mean_by_human_level"] = {f"{lvl:.1f}": round(sum(v) / len(v), 2)
                                           for lvl, v in sorted(bylvl.items())}
            m[sense_fr] = cell
        out["per_model"][slot] = m
        for fr in ("durel", "cont"):
            c = m[fr]
            print(f"[{name:<18} {fr:<5}] rho(sense,human)={c['rho_sense_human']} "
                  f"CI{c['rho_ci95']}  | partial|overlap={c['partial_ctrl_overlap']} "
                  f"partial|topic={c['partial_ctrl_topic']}  rho(sense,topic)={c['rho_sense_topic']}  n={c['n']} na={c['na']}")
            print(f"        mean {fr} by human level: {c['mean_by_human_level']}")
        print()
    print("--- headline: P1 rho(sense,human) per model ---")
    for fr in ("durel", "cont"):
        vals = [out["per_model"][s][fr]["rho_sense_human"] for s in PANEL]
        pov = [out["per_model"][s][fr]["partial_ctrl_overlap"] for s in PANEL]
        ptp = [out["per_model"][s][fr]["partial_ctrl_topic"] for s in PANEL]
        print(f"  {fr:<5}: rho={vals}  partial|overlap={pov}  partial|topic={ptp}")
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
