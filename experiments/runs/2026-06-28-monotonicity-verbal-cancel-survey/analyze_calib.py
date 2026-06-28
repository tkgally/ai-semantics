"""PER-FAMILY B2 DEFAULT-AT-CEILING GATE for the within-verbal cancel-default survey
(session 139).

Reads raw_calib/{nli,fc}_{A,B,C}.json, applies the FROZEN B2 gate (same bar as the
C1/C2 STEP-1b calibrations) INDEPENDENTLY to each candidate verbal family. NLI primary.
No threshold tuned after data. Emits raw_calib/gate.json.

FROZEN B2 GATE per family (NOT relaxable):
  default affirm >= 0.80 in >= 2/3 models, strict NLI (label 0 = entailment).
  A family that PASSES is a candidate B2-passing NEW verbal default -> the result
  scrutinizes whether it admits a clean *constructional* cancel (vs a lexical swap)
  before any battery is flagged. A family that FLOORS feeds the principled-limit closure.
  No gate is relaxed after data.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw_calib")
SLOTS = ["A", "B", "C"]
CEIL = 0.80          # default-at-ceiling floor (frozen, same as C1/C2 STEP 1b)
MIN_MODELS = 2       # ">= 2/3 models"
FAMILIES = ["implicative", "factive", "causative-inchoative"]


def affirm(rec, instrument):
    p = rec["pred"]
    return (1 if p == "0" else 0) if instrument == "nli" else (1 if p == "YES" else 0)


def load(instrument, slot):
    return json.load(open(os.path.join(RAW, f"{instrument}_{slot}.json")))


def rate(recs, family, instrument):
    vals = [affirm(r, instrument) for r in recs if r["family"] == family]
    return (sum(vals) / len(vals)) if vals else None


def main():
    per_family = {}
    for fam in FAMILIES:
        per_model = {}
        for slot in SLOTS:
            nli = load("nli", slot)
            fc = load("fc", slot)
            per_model[slot] = {"default_nli": rate(nli, fam, "nli"),
                               "default_fc": rate(fc, fam, "fc")}
        models_ok = sum(1 for s in SLOTS
                        if per_model[s]["default_nli"] is not None
                        and per_model[s]["default_nli"] >= CEIL)
        per_family[fam] = {"per_model_nli_primary": per_model,
                           "models_ok": models_ok,
                           "VERDICT": "GO" if models_ok >= MIN_MODELS else "NO-GO"}
    out = {
        "gate": {"ceiling": CEIL, "min_models": MIN_MODELS,
                 "instrument": "NLI primary, label 0 = entailment"},
        "per_family": per_family,
        "summary": {fam: per_family[fam]["VERDICT"] for fam in FAMILIES},
    }
    json.dump(out, open(os.path.join(RAW, "gate.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))
    print("\nPER-FAMILY B2 SURVEY VERDICTS:")
    for fam in FAMILIES:
        print(f"  {fam}: {per_family[fam]['VERDICT']} "
              f"(models_ok {per_family[fam]['models_ok']}/3)")


if __name__ == "__main__":
    main()
