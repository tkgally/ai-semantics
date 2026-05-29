"""Analyze the way-construction minimal-pair probe v1 (2026-05-29).

Primary indicator: "affirm path-traversal rate" (FC YES, or NLI label 0 = entailment) on
the hypothesis "<Subj> moved from one place to another."
Conjecture confirm bar: way rate >=70%, with a >=30pp gap vs the ctrl-loc (location) control,
in >=2/3 models, holding for the anti-motion verb category (P3 / verb-reading guard).
Forms: way (construction), ctrl-loc (locative; discriminating control),
ctrl-motion (motion lexicalized; positive floor), idiomatic (over-generalization guard).

No threshold retuning: raw rates reported; result page interprets against the fixed bar.
"""
import csv, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}


def affirm(arm, pred):
    if pred is None:
        return None
    return pred == "0" if arm == "nli" else pred == "YES"


def rate(recs):
    vals = [r["affirm"] for r in recs if r["affirm"] is not None]
    return (round(sum(vals) / len(vals) * 100, 1), len(vals)) if vals else (None, 0)


def main():
    out = {"per_model": {}, "thresholds": {"way_rate_min": 70, "gap_pp": 30,
                                           "anti_motion_holds": True}}
    print("\n===== WAY-CONSTRUCTION MINIMAL-PAIR PROBE v1 — affirm path-traversal rate =====")
    print("Predicted (confirm): way >=70%, gap >=30pp vs ctrl-loc, holds for anti-motion.\n")
    for slot, name in PANEL.items():
        m = {"model": name}
        for arm in ("nli", "fc"):
            recs = json.load(open(os.path.join(RAW, f"{arm}_{slot}.json")))
            for r in recs:
                r["affirm"] = affirm(arm, r["pred"])
            byform = {f: [r for r in recs if r["form"] == f]
                      for f in ("way", "ctrl-loc", "ctrl-motion", "idiomatic")}
            way, way_n = rate(byform["way"])
            loc, _ = rate(byform["ctrl-loc"])
            mot, _ = rate(byform["ctrl-motion"])
            idi, _ = rate(byform["idiomatic"])
            gap = None if way is None or loc is None else round(way - loc, 1)
            # way rate by verb category (P3)
            bycat = {}
            for cat in ("manner", "activity", "anti-motion"):
                bycat[cat] = rate([r for r in byform["way"] if r["category"] == cat])[0]
            # per-verb way affirm (replication)
            verbs = sorted(set(r["verb"] for r in byform["way"]))
            pv = {v: rate([r for r in byform["way"] if r["verb"] == v])[0] for v in verbs}
            n_way_yes = sum(1 for v in pv.values() if v is not None and v >= 50)
            m[arm] = {"way_rate": way, "ctrl_loc_rate": loc, "ctrl_motion_rate": mot,
                      "idiomatic_rate": idi, "gap_way_minus_loc_pp": gap, "way_n": way_n,
                      "way_manner": bycat["manner"], "way_activity": bycat["activity"],
                      "way_antimotion": bycat["anti-motion"],
                      "verbs_way_majority_yes": f"{n_way_yes}/{len(verbs)}",
                      "per_verb_way": pv,
                      "na": sum(1 for r in recs if r["pred"] is None)}
        out["per_model"][slot] = m
        for arm in ("nli", "fc"):
            a = m[arm]
            print(f"[{name:<18} {arm.upper():<3}] way={a['way_rate']}%  "
                  f"loc={a['ctrl_loc_rate']}%  motion={a['ctrl_motion_rate']}%  "
                  f"idiom={a['idiomatic_rate']}%  GAP={a['gap_way_minus_loc_pp']}pp  "
                  f"(manner {a['way_manner']} / activity {a['way_activity']} / "
                  f"anti {a['way_antimotion']}; verbs way-yes {a['verbs_way_majority_yes']}; "
                  f"NA {a['na']})")
        print()
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    print(f"wrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
