"""B2 DEFAULT-AT-CEILING GATE for the C2 privative calibration (session 137).

Reads raw_calib/{nli,fc}_{A,B,C}.json, applies the FROZEN B2 gate from STEP 1b of
decisions/resolved/monotonicity-cancel-arm-redesign. NLI primary. No threshold tuned
after data. Emits raw_calib/gate.json.

FROZEN B2 GATE (NOT relaxable):
  category-membership default affirm ("a gun" -> "a weapon") >= 0.80 in >= 2/3 models,
  strict NLI (label 0 = entailment).
  GO    -> STEP 2 (build matched C2 cancel arm; reuse frozen B2-passing ADD arm; amended
           conjecture scope; add-verbal/cancel-nominal domain mismatch a live caveat).
  NO-GO -> STEP 3 principled-limit closure (M3: triggered ONLY by a measured B2 NO-GO).
A NO-GO does NOT relax the bar.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw_calib")
SLOTS = ["A", "B", "C"]
CAN_CEIL = 0.80      # category-membership default floor (frozen STEP 1b)
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
            "category_default_nli": rate(nli, "default", "nli"),
            "category_default_fc": rate(fc, "default", "fc"),
        }
    can_def_ok = sum(1 for s in SLOTS
                     if per_model[s]["category_default_nli"] is not None
                     and per_model[s]["category_default_nli"] >= CAN_CEIL)
    verdict = "GO" if can_def_ok >= MIN_MODELS else "NO-GO"
    out = {
        "gate": {"category_ceiling": CAN_CEIL, "min_models": MIN_MODELS,
                 "instrument": "NLI primary, label 0 = entailment"},
        "per_model_nli_primary": per_model,
        "category_default_models_ok": can_def_ok,
        "VERDICT": verdict,
    }
    json.dump(out, open(os.path.join(RAW, "gate.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))
    print(f"\nB2 C2-PRIVATIVE GATE VERDICT: {verdict}")
    if verdict == "NO-GO":
        print("  -> C2 NO-GO. Both C1 and C2 failed -> STEP 3 principled-limit closure "
              "(M3). Do NOT relax the bar.")


if __name__ == "__main__":
    main()
