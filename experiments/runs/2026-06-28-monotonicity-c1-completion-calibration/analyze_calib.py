"""B2 DEFAULT-AT-CEILING GATE for the C1 telic-completion calibration (session 137).

Reads raw_calib/{nli,fc}_{A,B,C}.json, applies the FROZEN B2 gate from STEP 1 of
decisions/resolved/monotonicity-cancel-arm-redesign. NLI primary. No threshold tuned
after data. Emits raw_calib/gate.json.

FROZEN B2 GATE (NOT relaxable):
  completion default affirm ("<Subj> finished <gerund> the <object>") >= 0.80
  in >= 2/3 models, strict NLI (label 0 = entailment).
  GO    -> STEP 2 (build matched C1 cancel arm, reuse frozen B2-passing ADD arm).
  NO-GO -> record a verified C1-NO-GO result, then STEP 1b (C2 privative, after M2).
A NO-GO does NOT relax the bar or re-pair completion verbs within the frame
(a NO-GO is structural, like s135).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw_calib")
SLOTS = ["A", "B", "C"]
CAN_CEIL = 0.80      # completion default floor (frozen STEP 1)
MIN_MODELS = 2       # ">= 2/3 models"


def affirm(rec, instrument):
    p = rec["pred"]
    return (1 if p == "0" else 0) if instrument == "nli" else (1 if p == "YES" else 0)


def load(instrument, slot):
    return json.load(open(os.path.join(RAW, f"{instrument}_{slot}.json")))


def rate(recs, condition, instrument):
    vals = [affirm(r, instrument) for r in recs if r["condition"] == condition]
    return (sum(vals) / len(vals)) if vals else None


def main():
    per_model = {}
    for slot in SLOTS:
        nli = load("nli", slot)
        fc = load("fc", slot)
        per_model[slot] = {
            "completion_default_nli": rate(nli, "default", "nli"),
            "completion_default_fc": rate(fc, "default", "fc"),
        }
    can_def_ok = sum(1 for s in SLOTS
                     if per_model[s]["completion_default_nli"] is not None
                     and per_model[s]["completion_default_nli"] >= CAN_CEIL)
    verdict = "GO" if can_def_ok >= MIN_MODELS else "NO-GO"
    out = {
        "gate": {"completion_ceiling": CAN_CEIL, "min_models": MIN_MODELS,
                 "instrument": "NLI primary, label 0 = entailment"},
        "per_model_nli_primary": per_model,
        "completion_default_models_ok": can_def_ok,
        "VERDICT": verdict,
    }
    json.dump(out, open(os.path.join(RAW, "gate.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))
    print(f"\nB2 C1-COMPLETION GATE VERDICT: {verdict}")
    if verdict == "NO-GO":
        print("  -> C1 NO-GO. Record verified result, then STEP 1b (C2 privative, "
              "after M2). Do NOT relax the bar.")


if __name__ == "__main__":
    main()
