"""Analyze the monotonicity-generalization battery (session 135). Reads raw/{nli,fc}_{A,B,C}
.json, applies the FROZEN reading rule from PREREG.md / the ratified decision (prereq 2),
emits raw/results.json. NLI primary. No threshold tuned after data.

KEY QUANTITIES (rates in [0,1]; affirm = NLI '0' | FC 'YES'):
  add_no_cue        = add CONSTRUCTION affirm  (licensing the added inference, no cue)
  add_control       = add CONTROL affirm       (bare default; B2 de-confounder)
  cancel_default    = cancel DEFAULT affirm    ("only once" on the bare frame)
  cancel_no_cue     = 1 - cancel CONSTRUCTION affirm  (SUPPRESSION with no cue; cc-v2 defn:
                      100 - construction_affirm)
  asymmetry         = add_no_cue - cancel_no_cue   (the discriminating no-cue contrast)
  add_cuefollow     = 1 - add CUE affirm       (cue DENIES; follow-cue = withhold)
  cancel_cuefollow  = cancel CUE affirm        (cue RE-ASSERTS; follow-cue = affirm)

FROZEN VERDICTS (>= 2/3 models; thresholds set before data):
  ASYMMETRY (20 pp):  add_no_cue - cancel_no_cue >= 0.20 -> CONFIRMS (leg 1)
                      |.| < 0.20 -> SYMMETRIC (falsifies);  <= -0.20 -> REVERSAL (falsifies)
  FRAGILITY (10 pp):  cancel no-cue NLI-vs-FC disagreement - add's >= 0.10 -> CONFIRMS leg 2
  CUE (inherited):    >= 0.70 follow-cue in >= 2/3 = robust; else informative partial-null
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
SLOTS = ["A", "B", "C"]
ASYM = 0.20      # 20 pp asymmetry margin
FRAG = 0.10      # 10 pp instrument-fragility margin
CUE = 0.70       # inherited cc-v2 cue-following robustness bar
MIN_MODELS = 2


def affirm(rec, instrument):
    p = rec["pred"]
    return (1 if p == "0" else 0) if instrument == "nli" else (1 if p == "YES" else 0)


def load(instrument, slot):
    return json.load(open(os.path.join(RAW, f"{instrument}_{slot}.json")))


def rate(recs, arm, condition, instrument):
    vals = [affirm(r, instrument) for r in recs
            if r["arm"] == arm and r["condition"] == condition]
    return (sum(vals) / len(vals)) if vals else None


def cells(slot, instrument):
    recs = load(instrument, slot)
    add_con = rate(recs, "add", "construction", instrument)
    can_con = rate(recs, "cancel", "construction", instrument)
    return {
        "add_no_cue": add_con,
        "add_control": rate(recs, "add", "control", instrument),
        "add_cuefollow": 1 - rate(recs, "add", "cue", instrument),
        "cancel_default": rate(recs, "cancel", "default", instrument),
        "cancel_no_cue": 1 - can_con,
        "cancel_cuefollow": rate(recs, "cancel", "cue", instrument),
    }


def main():
    per_model = {s: {"nli": cells(s, "nli"), "fc": cells(s, "fc")} for s in SLOTS}

    # per-model derived margins (NLI primary)
    asym_by_model, frag_by_model = {}, {}
    add_cue_ok, can_cue_ok = 0, 0
    for s in SLOTS:
        n, f = per_model[s]["nli"], per_model[s]["fc"]
        asym_by_model[s] = n["add_no_cue"] - n["cancel_no_cue"]
        add_disagree = abs(n["add_no_cue"] - f["add_no_cue"])
        can_disagree = abs(n["cancel_no_cue"] - f["cancel_no_cue"])
        frag_by_model[s] = {"add_disagree": round(add_disagree, 3),
                            "cancel_disagree": round(can_disagree, 3),
                            "cancel_minus_add": round(can_disagree - add_disagree, 3)}
        if n["add_cuefollow"] >= CUE:
            add_cue_ok += 1
        if n["cancel_cuefollow"] >= CUE:
            can_cue_ok += 1

    confirm_models = sum(1 for s in SLOTS if asym_by_model[s] >= ASYM)
    symmetric_models = sum(1 for s in SLOTS if abs(asym_by_model[s]) < ASYM)
    reversal_models = sum(1 for s in SLOTS if asym_by_model[s] <= -ASYM)
    if confirm_models >= MIN_MODELS:
        asym_verdict = "CONFIRMS (add easy / cancel hard, leg 1)"
    elif reversal_models >= MIN_MODELS:
        asym_verdict = "FALSIFIES — REVERSAL"
    elif symmetric_models >= MIN_MODELS:
        asym_verdict = "FALSIFIES — SYMMETRIC"
    else:
        asym_verdict = "INDETERMINATE (no direction in >=2/3 models)"

    frag_models = sum(1 for s in SLOTS if frag_by_model[s]["cancel_minus_add"] >= FRAG)
    frag_verdict = ("CONFIRMS leg 2 (cancel more instrument-fragile)"
                    if frag_models >= MIN_MODELS else
                    "leg 2 NOT met (cancel not reliably more fragile)")

    # aggregate (mean of 3 models), NLI primary, for the headline table
    agg = {k: round(sum(per_model[s]["nli"][k] for s in SLOTS) / 3, 3)
           for k in per_model["A"]["nli"]}
    agg["asymmetry_add_minus_cancel"] = round(agg["add_no_cue"] - agg["cancel_no_cue"], 3)

    results = {
        "thresholds": {"asymmetry_pp": ASYM, "fragility_pp": FRAG, "cue_bar": CUE,
                       "min_models": MIN_MODELS},
        "per_model": {s: {"nli": {k: round(v, 3) for k, v in per_model[s]["nli"].items()},
                          "fc": {k: round(v, 3) for k, v in per_model[s]["fc"].items()}}
                      for s in SLOTS},
        "aggregate_nli": agg,
        "asymmetry_by_model_nli": {s: round(asym_by_model[s], 3) for s in SLOTS},
        "asymmetry_confirm_models": confirm_models,
        "asymmetry_symmetric_models": symmetric_models,
        "asymmetry_reversal_models": reversal_models,
        "ASYMMETRY_VERDICT": asym_verdict,
        "fragility_by_model": frag_by_model,
        "fragility_confirm_models": frag_models,
        "FRAGILITY_VERDICT": frag_verdict,
        "add_cuefollow_robust_models": add_cue_ok,
        "cancel_cuefollow_robust_models": can_cue_ok,
    }
    json.dump(results, open(os.path.join(RAW, "results.json"), "w"), indent=1)

    print("=== aggregate (NLI primary, mean of 3 models) ===")
    for k, v in agg.items():
        print(f"  {k:32s} {v}")
    print("\n=== per-model NLI asymmetry (add_no_cue - cancel_no_cue) ===")
    for s in SLOTS:
        n = per_model[s]["nli"]
        print(f"  {s}: add_no_cue={n['add_no_cue']:.3f} cancel_no_cue={n['cancel_no_cue']:.3f}"
              f"  asym={asym_by_model[s]:+.3f}")
    print(f"\nASYMMETRY (>= {ASYM} in >= {MIN_MODELS}/3): {results['ASYMMETRY_VERDICT']}"
          f"  [confirm={confirm_models} sym={symmetric_models} rev={reversal_models}]")
    print(f"FRAGILITY (cancel-add disagreement >= {FRAG} in >= {MIN_MODELS}/3): "
          f"{results['FRAGILITY_VERDICT']}  [models={frag_models}]")
    print(f"CUE-FOLLOW robust (>= {CUE} in >= {MIN_MODELS}/3): "
          f"add={add_cue_ok}/3  cancel={can_cue_ok}/3")


if __name__ == "__main__":
    main()
