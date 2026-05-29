"""Analyze the caused-motion minimal-pair probe v1 (2026-05-29).

Primary indicator: "affirm caused-motion rate" (FC YES, or NLI label 0 = entailment) on
the hypothesis "<Subj>'s <gerund> caused <obj> to move."
Conjecture confirm bar: cm rate >=70%, with a >=30pp gap vs. controls, in >=2/3 models,
holding for held-out/low-frequency (atypical) verbs. P3: cm rate for atypical verbs
within 15pp of typical verbs. Two controls: ctrl-loc (object stayed; no motion) and
ctrl-sep (object moved by ANOTHER cause; causation-specific control).

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
    out = {"per_model": {}, "thresholds": {"cm_rate_min": 70, "gap_pp": 30,
                                           "atypical_within_pp": 15}}
    print("\n===== CAUSED-MOTION MINIMAL-PAIR PROBE v1 — affirm caused-motion rate =====")
    print("Predicted (confirm): cm >=70%, gap >=30pp vs controls, atypical within 15pp.\n")
    for slot, name in PANEL.items():
        m = {"model": name}
        for arm in ("nli", "fc"):
            recs = json.load(open(os.path.join(RAW, f"{arm}_{slot}.json")))
            for r in recs:
                r["affirm"] = affirm(arm, r["pred"])
            byform = {f: [r for r in recs if r["form"] == f]
                      for f in ("cm", "ctrl-loc", "ctrl-sep")}
            cm, cm_n = rate(byform["cm"])
            loc, _ = rate(byform["ctrl-loc"])
            sep, _ = rate(byform["ctrl-sep"])
            ctrl_max = None if loc is None or sep is None else max(loc, sep)
            gap = None if cm is None or ctrl_max is None else round(cm - ctrl_max, 1)
            cm_typ, _ = rate([r for r in byform["cm"] if r["typicality"] == "typical"])
            cm_atyp, _ = rate([r for r in byform["cm"] if r["typicality"] == "atypical"])
            cm_inan, _ = rate([r for r in byform["cm"] if r["animacy"] == "inanimate"])
            cm_anim, _ = rate([r for r in byform["cm"] if r["animacy"] == "animate"])
            # per-verb cm affirm (replication)
            verbs = sorted(set(r["verb"] for r in byform["cm"]))
            pv = {v: rate([r for r in byform["cm"] if r["verb"] == v])[0] for v in verbs}
            n_cm_yes = sum(1 for v in pv.values() if v is not None and v >= 50)
            m[arm] = {"cm_rate": cm, "ctrl_loc_rate": loc, "ctrl_sep_rate": sep,
                      "gap_vs_worst_ctrl_pp": gap, "cm_n": cm_n,
                      "cm_typical": cm_typ, "cm_atypical": cm_atyp,
                      "cm_inanimate": cm_inan, "cm_animate": cm_anim,
                      "atypical_minus_typical_pp": None if cm_typ is None or cm_atyp is None
                          else round(cm_atyp - cm_typ, 1),
                      "verbs_cm_majority_yes": f"{n_cm_yes}/{len(verbs)}",
                      "per_verb_cm": pv,
                      "na": sum(1 for r in recs if r["pred"] is None)}
        out["per_model"][slot] = m
        for arm in ("nli", "fc"):
            a = m[arm]
            print(f"[{name:<18} {arm.upper():<3}] cm={a['cm_rate']}%  "
                  f"ctrl-loc={a['ctrl_loc_rate']}%  ctrl-sep={a['ctrl_sep_rate']}%  "
                  f"GAP={a['gap_vs_worst_ctrl_pp']}pp  (typ {a['cm_typical']} / atyp "
                  f"{a['cm_atypical']}; inan {a['cm_inanimate']} / anim {a['cm_animate']}; "
                  f"verbs cm-yes {a['verbs_cm_majority_yes']}; NA {a['na']})")
        print()
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    print(f"wrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
