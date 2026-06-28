"""B2 BLOCKING CEILING GATE for the monotonicity-generalization battery (session 135).

Reads raw_calib/{nli,fc}_{A,B,C}.json, applies the FROZEN B2 gate from PREREG.md (and the
ratified decision prereq 2). NLI primary. No threshold tuned after data. Emits
raw_calib/gate.json.

FROZEN B2 GATE (admit the PAIR only if ALL hold):
  ADD arm has real headroom:
    construction (licensing-no-cue) affirm >= 0.80 AND bare control affirm <= 0.40,
    each in >= 2/3 models.
  CANCEL arm has a real default to suppress (MOD-3, contestable default):
    lexical-default affirm ("only once") >= 0.80, in >= 2/3 models.
A NO-GO on either -> reject/re-pair the pair BEFORE the main run (do NOT relax the bar).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw_calib")
SLOTS = ["A", "B", "C"]
ADD_CEIL = 0.80      # add construction licensing-no-cue floor
ADD_CTRL = 0.40      # add bare-control ceiling
CAN_CEIL = 0.80      # cancel default floor
MIN_MODELS = 2       # ">= 2/3 models"


def affirm(rec, instrument):
    p = rec["pred"]
    return (1 if p == "0" else 0) if instrument == "nli" else (1 if p == "YES" else 0)


def load(instrument, slot):
    return json.load(open(os.path.join(RAW, f"{instrument}_{slot}.json")))


def rate(recs, arm, condition, instrument):
    vals = [affirm(r, instrument) for r in recs
            if r["arm"] == arm and r["condition"] == condition]
    return (sum(vals) / len(vals)) if vals else None


def main():
    per_model = {}
    for slot in SLOTS:
        nli = load("nli", slot)
        per_model[slot] = {
            "add_construction_nli": rate(nli, "add", "construction", "nli"),
            "add_control_nli": rate(nli, "add", "control", "nli"),
            "cancel_default_nli": rate(nli, "cancel", "default", "nli"),
            "add_construction_fc": rate(load("fc", slot), "add", "construction", "fc"),
            "add_control_fc": rate(load("fc", slot), "add", "control", "fc"),
            "cancel_default_fc": rate(load("fc", slot), "cancel", "default", "fc"),
        }
    # gate counts (NLI primary)
    add_head_ok = sum(1 for s in SLOTS
                      if per_model[s]["add_construction_nli"] is not None
                      and per_model[s]["add_construction_nli"] >= ADD_CEIL
                      and per_model[s]["add_control_nli"] <= ADD_CTRL)
    can_def_ok = sum(1 for s in SLOTS
                     if per_model[s]["cancel_default_nli"] is not None
                     and per_model[s]["cancel_default_nli"] >= CAN_CEIL)
    add_pass = add_head_ok >= MIN_MODELS
    can_pass = can_def_ok >= MIN_MODELS
    verdict = "GO" if (add_pass and can_pass) else "NO-GO"
    out = {
        "gate": {"add_ceiling": ADD_CEIL, "add_control_max": ADD_CTRL,
                 "cancel_ceiling": CAN_CEIL, "min_models": MIN_MODELS},
        "per_model_nli_primary": per_model,
        "add_headroom_models_ok": add_head_ok, "add_pass": add_pass,
        "cancel_default_models_ok": can_def_ok, "cancel_pass": can_pass,
        "VERDICT": verdict,
    }
    json.dump(out, open(os.path.join(RAW, "gate.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))
    print(f"\nB2 GATE VERDICT: {verdict}")
    if verdict == "NO-GO":
        print("  -> re-pair before spend (MOD-3 / decision prereq 2). Do NOT relax the bar.")


if __name__ == "__main__":
    main()
