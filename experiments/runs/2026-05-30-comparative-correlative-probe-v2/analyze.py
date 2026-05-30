"""Analyze the off-ceiling comparative-correlative v2 probe (2026-05-30).

Indicator: construction-correct rate per arm (pred matches the STATED/composed direction).
  NLI: 0=increase, 2=decrease, 1=undetermined ; FC: INCREASE/DECREASE/UNDETERMINED.

Per model x instrument x arm (baseline d1, conflicting-cue d2, paraphrase d2, multi-step d3):
  correct rate = fraction matching the construction/composition gold.
Headline quantities (ratified report-the-rate; no manufactured pass bar):
  - conflicting-cue FOLLOW-CONSTRUCTION rate = correct rate on the conflicting-cue arm
    (the model follows the STATED direction against world knowledge). Its complement splits
    into follow-world-knowledge (the opposite direction) vs undetermined.
  - multi-step COMPOSITION rate = correct rate on the 2-step chains.
  - degradation SHAPE across difficulty d1<d2<d3: graceful (monotone, shallow) vs brittle cliff.
No threshold tuned after the run.
"""
import json, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
ARMS = ["baseline", "conflicting-cue", "paraphrase", "multi-step"]
NLI_DIR = {"0": "increase", "2": "decrease", "1": "undetermined"}


def correct(arm_kind, pred, gold):
    if pred is None:
        return None
    if arm_kind == "nli":
        return NLI_DIR.get(pred) == gold
    return pred == {"increase": "INCREASE", "decrease": "DECREASE",
                    "undetermined": "UNDETERMINED"}[gold]


def pred_dir(arm_kind, pred):
    if pred is None:
        return None
    return NLI_DIR.get(pred) if arm_kind == "nli" else pred.lower()


def rate(vals):
    v = [x for x in vals if x is not None]
    return (round(sum(v) / len(v) * 100, 1), len(v)) if v else (None, 0)


def main():
    out = {"per_model": {}, "reading_rule": "construction-correct rate per arm; headline = "
           "conflicting-cue follow-construction + multi-step composition + degradation shape "
           "(report-the-rate, ratified)"}
    print("\n===== COMPARATIVE-CORRELATIVE v2 — construction-correct rate per arm =====")
    print("baseline(d1) clear CC | conflicting-cue(d2) construction vs world | "
          "paraphrase(d2) non-`the` form | multi-step(d3) 2-step composition.\n")
    for slot, name in PANEL.items():
        m = {"model": name}
        for arm_kind in ("nli", "fc"):
            recs = json.load(open(os.path.join(RAW, f"{arm_kind}_{slot}.json")))
            byarm = defaultdict(list)
            for r in recs:
                byarm[r["arm"]].append(r)
            for arm in ARMS:
                rs = byarm[arm]
                cr, n = rate([correct(arm_kind, r["pred"], r["direction_gold"]) for r in rs])
                cell = {"correct": cr, "n": n}
                if arm == "conflicting-cue":
                    # split the non-correct mass into follow-world vs undetermined
                    fw = fu = 0
                    for r in rs:
                        pd = pred_dir(arm_kind, r["pred"])
                        if pd is None or pd == r["direction_gold"]:
                            continue
                        if pd == "undetermined":
                            fu += 1
                        else:
                            fw += 1  # the opposite stated direction = world-knowledge-following
                    cell["follow_world_pct"] = round(fw / n * 100, 1) if n else None
                    cell["undetermined_pct"] = round(fu / n * 100, 1) if n else None
                m[f"{arm}_{arm_kind}"] = cell
        out["per_model"][slot] = m
        for arm_kind in ("nli", "fc"):
            cells = [f"{a}={m[f'{a}_{arm_kind}']['correct']}%" for a in ARMS]
            cc = m[f"conflicting-cue_{arm_kind}"]
            print(f"[{name:<18} {arm_kind.upper():<3}] " + "  ".join(cells) +
                  f"  | conf-cue follow-world={cc.get('follow_world_pct')}% "
                  f"undet={cc.get('undetermined_pct')}%")
        print()
    print("--- headline quantities per instrument (across models) ---")
    for arm_kind in ("nli", "fc"):
        cc = [out["per_model"][s][f"conflicting-cue_{arm_kind}"]["correct"] for s in PANEL]
        ms = [out["per_model"][s][f"multi-step_{arm_kind}"]["correct"] for s in PANEL]
        bl = [out["per_model"][s][f"baseline_{arm_kind}"]["correct"] for s in PANEL]
        print(f"  {arm_kind.upper():<3}: baseline={bl}  conflicting-cue(follow-constr)={cc}  "
              f"multi-step(composition)={ms}")
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
