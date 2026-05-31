"""Coercion-as-sense-modulation v2 analysis (2026-05-31). Pure-Python.

Reads raw/{durel,cont}_{A,B,C}.json (the reused lexical relatedness instrument on the v2 stimuli).
Reports per model x framing the per-arm mean relatedness and the diagnostic gaps. Report-the-number;
no pass bar; reading rule fixed pre-run (design v2). Internal-contrast-only.

Arms: coerced-way / transitive-ctrl / elab-ctrl / polysemy-anchor.

Diagnostic gaps:
  coercion_gap   = mean(elab-ctrl)       - mean(coerced-way)   [v1 replication: coercion lowers relatedness vs a bare elaboration]
  ISOLATION_gap  = mean(transitive-ctrl) - mean(coerced-way)   [THE DECISIVE v2 contrast: both arms add argument structure,
                                                                so a POSITIVE isolation gap => the drop is SENSE-specific, not
                                                                a mere added-structure artifact (settles v1's I1 confound)]
  surface_effect = mean(elab-ctrl)       - mean(transitive-ctrl) [does adding a CONVENTIONAL object alone lower relatedness?
                                                                  ~0 => adding structure per se does not drive the drop]
  within-verb isolation sign: # verbs with transitive-ctrl > coerced-way (of 8)
Predicted ordering (pre-committed): elab-ctrl >= transitive-ctrl >= coerced-way >= polysemy-anchor.
"""
import csv
import json
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
ITEMS = os.path.join(HERE, "items.csv")
PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
FRAMINGS = ("durel", "cont")
ARMS = ("elab-ctrl", "transitive-ctrl", "coerced-way", "polysemy-anchor")


def mean(v):
    return sum(v) / len(v) if v else None


def main():
    meta = {r["item_id"]: r for r in csv.DictReader(open(ITEMS))}
    out = {"reading": "isolation_gap = transitive-ctrl - coerced-way is the decisive contrast "
                       "(both add argument structure; positive => sense-specific, settles v1 I1). "
                       "Internal-contrast-only; report-the-number.",
           "per_model": {}}
    for slot, name in PANEL.items():
        m = {"model": name}
        for fr in FRAMINGS:
            recs = json.load(open(os.path.join(RAW, f"{fr}_{slot}.json")))
            by_arm = defaultdict(list)
            by_verb_arm = defaultdict(dict)
            for r in recs:
                if r["pred"] is None:
                    continue
                by_arm[r["arm"]].append(r["pred"])
                by_verb_arm[r["verb"]][r["arm"]] = r["pred"]
            arm_mean = {a: (round(mean(by_arm[a]), 2) if by_arm[a] else None) for a in ARMS}
            cg = (round(arm_mean["elab-ctrl"] - arm_mean["coerced-way"], 2)
                  if arm_mean["elab-ctrl"] is not None and arm_mean["coerced-way"] is not None else None)
            iso = (round(arm_mean["transitive-ctrl"] - arm_mean["coerced-way"], 2)
                   if arm_mean["transitive-ctrl"] is not None and arm_mean["coerced-way"] is not None else None)
            surf = (round(arm_mean["elab-ctrl"] - arm_mean["transitive-ctrl"], 2)
                    if arm_mean["elab-ctrl"] is not None and arm_mean["transitive-ctrl"] is not None else None)
            # within-verb isolation sign: transitive > coerced
            iso_pos = iso_tot = 0
            for verb, d in by_verb_arm.items():
                if "transitive-ctrl" in d and "coerced-way" in d:
                    iso_tot += 1
                    if d["transitive-ctrl"] > d["coerced-way"]:
                        iso_pos += 1
            ordering_ok = (arm_mean["elab-ctrl"] >= arm_mean["transitive-ctrl"] >=
                           arm_mean["coerced-way"] >= arm_mean["polysemy-anchor"]) \
                if all(arm_mean[a] is not None for a in ARMS) else None
            m[fr] = {"arm_mean": arm_mean, "coercion_gap(elab-coerced)": cg,
                     "ISOLATION_gap(trans-coerced)": iso, "surface_effect(elab-trans)": surf,
                     "within_verb_isolation_sign": f"{iso_pos}/{iso_tot}",
                     "ordering_elab>=trans>=coerced>=poly": ordering_ok}
        out["per_model"][slot] = m
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)

    print("===== coercion-as-sense-modulation v2 (non-coercing transitive control) =====")
    for slot, name in PANEL.items():
        print(f"\n[{name}]")
        for fr in FRAMINGS:
            c = out["per_model"][slot][fr]
            am = c["arm_mean"]
            print(f"  {fr:5s} elab={am['elab-ctrl']} trans={am['transitive-ctrl']} "
                  f"coerced={am['coerced-way']} poly={am['polysemy-anchor']}")
            print(f"        ISOLATION_gap(trans-coerced)={c['ISOLATION_gap(trans-coerced)']} "
                  f"surface(elab-trans)={c['surface_effect(elab-trans)']} "
                  f"coercion_gap={c['coercion_gap(elab-coerced)']} "
                  f"iso_sign={c['within_verb_isolation_sign']} "
                  f"order_ok={c['ordering_elab>=trans>=coerced>=poly']}")
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
