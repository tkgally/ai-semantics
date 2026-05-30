"""Analyze the embedded-CC (operator-scope) comparative-correlative v3 probe (2026-05-30).

Indicator: operator-correct rate per arm (pred == the per-arm, per-instrument gold frozen in
items.csv). The NLI hypothesis is always the POSITIVE covariation, so:
  baseline-pos -> entail(0)/INCREASE ; baseline-inv -> contradiction(2)/DECREASE ;
  embedded arms -> FC=UNDETERMINED uniformly, NLI = 2 (negation) / 1 (modal, negation-inv).

Headline quantities (ratified report-the-rate; no manufactured pass bar):
  - EMBEDDING-CANCELLATION rate = over the embedded arms (negation+modal+negation-inv),
    fraction where the model does NOT answer the bare positive direction (FC != INCREASE /
    NLI != 0) -- the off-template signal that the operator scope is tracked.
  - per-arm operator-correct rate.
  - degradation SHAPE across d1<d2<d3.
FC is primary for the embedded arms (UNDETERMINED gold is least gold-contestable); NLI
secondary. No threshold tuned after the run.
"""
import json
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
ARMS = ["baseline-pos", "baseline-inv", "negation", "modal-epistemic", "negation-inv"]
EMBEDDED = {"negation", "modal-epistemic", "negation-inv"}


def rate(vals):
    v = [x for x in vals if x is not None]
    return (round(sum(v) / len(v) * 100, 1), len(v)) if v else (None, 0)


def main():
    out = {"per_model": {}, "reading_rule": "operator-correct rate per arm; headline = "
           "embedding-cancellation rate (off bare-positive on embedded arms) + per-arm "
           "operator-correct + degradation shape (report-the-rate, ratified)"}
    print("\n===== COMPARATIVE-CORRELATIVE v3 — operator-correct rate per arm =====")
    print("baseline-pos(d1)=entail/INCREASE  baseline-inv(d1)=contra/DECREASE  "
          "negation(d2)/modal(d2)/negation-inv(d3) embedded=UNDETERMINED(FC), 2/1/1(NLI)\n")
    for slot, name in PANEL.items():
        m = {"model": name}
        cancel_hits = defaultdict(list)  # arm_kind -> list of off-template bools (embedded)
        for arm_kind, goldkey in (("nli", "nli_gold"), ("fc", "fc_gold")):
            recs = json.load(open(os.path.join(RAW, f"{arm_kind}_{slot}.json")))
            byarm = defaultdict(list)
            for r in recs:
                byarm[r["arm"]].append(r)
            for arm in ARMS:
                rs = byarm[arm]
                cr, n = rate([(r["pred"] == r[goldkey]) if r["pred"] is not None else None
                              for r in rs])
                m[f"{arm}_{arm_kind}"] = {"correct": cr, "n": n}
                if arm in EMBEDDED:
                    bare = "0" if arm_kind == "nli" else "INCREASE"
                    for r in rs:
                        if r["pred"] is None:
                            cancel_hits[arm_kind].append(None)
                        else:
                            cancel_hits[arm_kind].append(r["pred"] != bare)
        for arm_kind in ("nli", "fc"):
            cancr, cann = rate(cancel_hits[arm_kind])
            m[f"embedding_cancellation_{arm_kind}"] = {"rate": cancr, "n": cann}
        out["per_model"][slot] = m
        for arm_kind in ("nli", "fc"):
            cells = [f"{a}={m[f'{a}_{arm_kind}']['correct']}%" for a in ARMS]
            canc = m[f"embedding_cancellation_{arm_kind}"]
            print(f"[{name:<18} {arm_kind.upper():<3}] " + "  ".join(cells) +
                  f"  | embed-cancel={canc['rate']}% (n={canc['n']})")
        print()
    print("--- headline quantities per instrument (across models) ---")
    for arm_kind in ("nli", "fc"):
        canc = [out["per_model"][s][f"embedding_cancellation_{arm_kind}"]["rate"] for s in PANEL]
        bp = [out["per_model"][s][f"baseline-pos_{arm_kind}"]["correct"] for s in PANEL]
        bi = [out["per_model"][s][f"baseline-inv_{arm_kind}"]["correct"] for s in PANEL]
        neg = [out["per_model"][s][f"negation_{arm_kind}"]["correct"] for s in PANEL]
        mod = [out["per_model"][s][f"modal-epistemic_{arm_kind}"]["correct"] for s in PANEL]
        ni = [out["per_model"][s][f"negation-inv_{arm_kind}"]["correct"] for s in PANEL]
        print(f"  {arm_kind.upper():<3}: base-pos={bp} base-inv={bi} | "
              f"negation={neg} modal={mod} negation-inv={ni} | embed-cancel={canc}")
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
