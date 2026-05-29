"""Analyze the CxNLI base-vs-distinction probe (2026-05-29).

Per-construction and overall:
  - base accuracy (Exp1 subsample)  vs  distinction accuracy (Exp2)
  - the DROP (base - distinction) — the quantity Scivetti reports as >40% for GPT-o1
Compares to the Scivetti human baselines (Exp1 ~0.90, Exp2 ~0.83) and the published
GPT-o1 >40% aggregate drop. No threshold retuning: the ratified divergence threshold
machinery (constructional-divergence-operationalization) governs interpretation;
here we report the raw drop and let the result page interpret against the fixed
human/published references.
"""
import json, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
CXNS = ["causative-with-CxN", "caused-motion", "conative", "intransitive-motion", "resultative"]


def load(arm, slot):
    return json.load(open(os.path.join(RAW, f"{arm}_{slot}.json")))


def acc(recs, cxn=None):
    sel = [r for r in recs if cxn is None or r["cxn"] == cxn]
    p = [r for r in sel if r["pred"] is not None]
    if not p:
        return None, 0
    return sum(1 for r in p if str(r["pred"]) == str(r["gold"])) / len(p), len(p)


def main():
    out = {"per_model": {}, "references": {
        "scivetti_human_exp1": 0.90, "scivetti_human_exp2": 0.83,
        "scivetti_gpt_o1_drop": ">40% (aggregate, published)"}}
    print("\n========== CxNLI BASE vs DISTINCTION — project-run replication ==========")
    print("Human baselines: Exp1(base)~0.90  Exp2(distinction)~0.83  |  GPT-o1 published drop >40%\n")
    print(f"{'model':<20}{'baseAcc':>8}{'distAcc':>8}{'DROP pp':>9}   per-construction drop (base->dist)")
    agg = {}
    for slot, name in PANEL.items():
        b = load("base", slot); d = load("distinction", slot)
        ba, bn = acc(b); da, dn = acc(d)
        drop = None if ba is None or da is None else round((ba - da) * 100, 1)
        percx = {}
        for cxn in CXNS:
            bca, _ = acc(b, cxn); dca, _ = acc(d, cxn)
            percx[cxn] = {"base": bca, "dist": dca,
                          "drop_pp": None if bca is None or dca is None else round((bca - dca) * 100, 1)}
        out["per_model"][slot] = {"model": PANEL[slot], "base_acc": ba, "dist_acc": da,
                                  "drop_pp": drop, "base_n": bn, "dist_n": dn,
                                  "na": {"base": sum(1 for r in b if r["pred"] is None),
                                         "dist": sum(1 for r in d if r["pred"] is None)},
                                  "per_construction": percx}
        agg[slot] = drop
        cxstr = "  ".join(f"{c.split('-')[0][:4]}:{percx[c]['drop_pp']}" for c in CXNS)
        print(f"{name:<20}{ba*100:7.0f}%{da*100:7.0f}%{drop:>8}pp   {cxstr}")
    print(f"\nmean drop across panel: {sum(agg.values())/len(agg):.1f} pp "
          f"(Scivetti GPT-o1 published: >40%)")
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
