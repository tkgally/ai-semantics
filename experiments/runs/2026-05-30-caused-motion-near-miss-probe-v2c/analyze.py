"""Analyze the caused-motion near-miss form-control probe (v2c, 2026-05-30).

Indicator: affirm-causation rate per arm (FC YES / NLI entailment 0). The hypothesis
"<Subj>'s <gerund> caused <obj> to move" is held identical across the 3 forms within each
scene, so the only thing that varies is the FORM (construction vs near-miss).

Headline quantities (ratified report-the-rate; no manufactured pass bar):
  - per-arm affirm-causation rate (cm-construction / near-coord / near-seq).
  - CONSTRUCTION-vs-NEAR-MISS GAP = cm-construction affirm minus the near-miss affirm rate,
    per model per instrument. A large gap => the causation inference is keyed on the
    CONSTRUCTION FORM (genuine constructional causation, tightening v1's floor). A small gap
    (near-miss affirmed too) => the v1/v2 ceiling is NOT construction-specific (a looser
    "verb happened + object displaced -> caused it" shape / Gricean default). Either is
    first-class.
No threshold tuned after the run. The near-miss "withhold" gold labels the entailment-correct
direction only; the headline is the within-scene gap, not accuracy against the (pragmatically
contestable) near-miss gold.
"""
import json
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
ARMS = ["cm-construction", "near-coord", "near-seq"]


def is_affirm(arm_kind, pred):
    if pred is None:
        return None
    return (pred == "0") if arm_kind == "nli" else (pred == "YES")


def rate(vals):
    v = [x for x in vals if x is not None]
    return (round(sum(v) / len(v) * 100, 1), len(v)) if v else (None, 0)


def main():
    out = {"per_model": {}, "reading_rule": "affirm-causation rate per arm; headline = "
           "construction-vs-near-miss GAP per model per instrument (report-the-rate, ratified)"}
    print("\n===== CAUSED-MOTION near-miss v2c — affirm-causation rate per arm =====")
    print("cm-construction(d1)=the construction | near-coord(d2)=and-frame | "
          "near-seq(d3)=temporal-sequence. hypothesis identical across forms within a scene.\n")
    for slot, name in PANEL.items():
        m = {"model": name}
        for arm_kind in ("nli", "fc"):
            recs = json.load(open(os.path.join(RAW, f"{arm_kind}_{slot}.json")))
            byarm = defaultdict(list)
            for r in recs:
                byarm[r["arm"]].append(r)
            for arm in ARMS:
                ar, n = rate([is_affirm(arm_kind, r["pred"]) for r in byarm[arm]])
                m[f"{arm}_{arm_kind}"] = {"affirm": ar, "n": n}
            cm = m[f"cm-construction_{arm_kind}"]["affirm"]
            nm = rate([is_affirm(arm_kind, r["pred"])
                       for arm in ("near-coord", "near-seq") for r in byarm[arm]])[0]
            m[f"gap_{arm_kind}"] = (round(cm - nm, 1)
                                    if cm is not None and nm is not None else None)
            m[f"near_miss_affirm_{arm_kind}"] = nm
        out["per_model"][slot] = m
        for arm_kind in ("nli", "fc"):
            cells = [f"{a}={m[f'{a}_{arm_kind}']['affirm']}%" for a in ARMS]
            print(f"[{name:<18} {arm_kind.upper():<3}] " + "  ".join(cells) +
                  f"  | construction-vs-near-miss gap={m[f'gap_{arm_kind}']}pp")
        print()
    print("--- headline gaps per instrument (across models) ---")
    for arm_kind in ("nli", "fc"):
        cm = [out["per_model"][s][f"cm-construction_{arm_kind}"]["affirm"] for s in PANEL]
        nm = [out["per_model"][s][f"near_miss_affirm_{arm_kind}"] for s in PANEL]
        gap = [out["per_model"][s][f"gap_{arm_kind}"] for s in PANEL]
        print(f"  {arm_kind.upper():<3}: construction={cm}  near-miss={nm}  gap(pp)={gap}")
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
