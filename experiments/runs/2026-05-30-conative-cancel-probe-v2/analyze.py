"""Analyze the off-ceiling CANCEL-DIRECTION conative v2 probe (2026-05-30).

Indicator: affirm-CONTACT rate (FC YES, or NLI label 0 = entailment) on the hypothesis
"<subj> made contact with <obj>".

Per model x instrument, conative-class verbs:
  transitive_affirm  (expect high / ~ceiling -> the lexical default; licensing baseline)
  conative_affirm    (LOW = good suppression; the v1 off-ceiling quantity)
  cue_affirm         (does the explicit contact-consequence re-license contact, overriding
                      the conative? high = cue-respecting / updates under cue)
DERIVED (the de-confounding measures, matched to the add-direction v2):
  suppression_no_cue = 100 - conative_affirm   (construction-following, no cue;
                       COMPARE to add-direction CANONICAL affirm = licensing-no-cue)
  cue_following      = cue_affirm               (COMPARE to add cue-following = 100 - cue_affirm)
  conative_to_cue_shift = cue_affirm - conative_affirm  (how far the cue moves the model)
Control (non-alternating) verbs:
  transitive_affirm  (ceiling anchor) ; resist_affirm (anomalous conative; report rate)

Reading rule (RATIFIED cc-v2-difficulty-operationalization, report-the-rate; no pass bar):
  - suppression and cue-following reported as rates with CIs implicit in N; the headline is
    the CROSS-DIRECTION comparison against the committed add-direction v2 numbers
    (2026-05-29-argument-structure-coercion-probe-v2/raw/results.json), NOT a threshold.
  - A clean symmetric pattern (both directions follow the cue; only the no-cue canonical
    differs) => the v1 add/cancel asymmetry was canonical-difficulty, de-confound it.
  - Cancel staying harder than add even with the cue arm => asymmetry is about direction.
No threshold tuned after the run.
"""
import json, os

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
    out = {"per_model": {}, "indicator": "affirm-contact rate on '<subj> made contact with <obj>'",
           "reading_rule": "report-the-rate; headline = cross-direction comparison vs the "
           "add-direction v2 (de-confound add/cancel asymmetry from ceiling), not a pass bar"}
    print("\n===== CANCEL-DIRECTION CONATIVE v2 — affirm-CONTACT rate =====")
    print("transitive=lexical default (ceiling anchor); conative=suppression (LOW=good); "
          "cue=re-licensing under explicit contact consequence.\n")
    for slot, name in PANEL.items():
        m = {"model": name}
        for arm in ("nli", "fc"):
            recs = json.load(open(os.path.join(RAW, f"{arm}_{slot}.json")))
            for r in recs:
                r["affirm"] = affirm(arm, r["pred"])
            con = [r for r in recs if r["construction"] == "conative"]
            ctl = [r for r in recs if r["construction"] == "conative-control"]
            t, _ = rate([r for r in con if r["condition"] == "transitive"])
            c, _ = rate([r for r in con if r["condition"] == "conative"])
            cue, _ = rate([r for r in con if r["condition"] == "cue"])
            ct_t, _ = rate([r for r in ctl if r["condition"] == "transitive"])
            ct_r, _ = rate([r for r in ctl if r["condition"] == "resist"])
            supp = None if c is None else round(100 - c, 1)
            shift = None if (cue is None or c is None) else round(cue - c, 1)
            m[arm] = {"transitive": t, "conative": c, "cue": cue,
                      "suppression_no_cue": supp, "cue_following": cue,
                      "conative_to_cue_shift": shift,
                      "ctrl_transitive": ct_t, "ctrl_resist": ct_r}
        out["per_model"][slot] = m
        for arm in ("nli", "fc"):
            a = m[arm]
            print(f"[{name:<18} {arm.upper():<3}] trans={a['transitive']}%  "
                  f"conative={a['conative']}%  cue={a['cue']}%  | suppression(no-cue)="
                  f"{a['suppression_no_cue']}pp  cue-following={a['cue_following']}%  "
                  f"shift={a['conative_to_cue_shift']}pp  || ctrl: trans={a['ctrl_transitive']}% "
                  f"resist={a['ctrl_resist']}%")
        print()
    # cross-model summaries of the two de-confounding quantities
    print("--- de-confounding quantities (cancel direction), per instrument ---")
    for arm in ("nli", "fc"):
        supp = [out["per_model"][s][arm]["suppression_no_cue"] for s in PANEL]
        cf = [out["per_model"][s][arm]["cue_following"] for s in PANEL]
        print(f"  {arm.upper():<3}: suppression-no-cue (100-conative) = {supp}  | "
              f"cue-following (cue affirm) = {cf}")
    print("\nCompare against add-direction v2 (committed): "
          "../2026-05-29-argument-structure-coercion-probe-v2/raw/results.json")
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    print(f"wrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
