"""Analyze the WITHIN-VERBAL matched ADD-vs-CANCEL monotonicity battery (session 141).
Reads raw/{nli,fc}_{A,B,C}.json, applies the FROZEN ratified s134 reading rule, emits
raw/results.json. NLI primary. No threshold tuned after data.

ORDER (anti-cheat, committed in PREREG): the B2 GATE is read FIRST (from the same run);
the ASYMMETRY verdict is only meaningful if B2 passes (M1: the B2 default-at-ceiling pass
is what licenses reading a cancel suppression failure as DEFEASANCE).

KEY QUANTITIES (rates in [0,1]; affirm = NLI '0' | FC 'YES'):
  add_no_cue     = add CONSTRUCTION affirm  (licensing the added inference, no cue)
  add_control    = add CONTROL affirm       (bare default; B2 de-confounder)
  cancel_default = cancel DEFAULT affirm    (result entailment on the bare past; B2 anchor)
  cancel_no_cue  = 1 - cancel CONSTRUCTION affirm  (SUPPRESSION with no cue; cc-v2 defn)
  asymmetry      = add_no_cue - cancel_no_cue   (the discriminating no-cue contrast)
  add_cuefollow  = 1 - add CUE affirm       (cue DENIES; follow-cue = withhold)
  cancel_cuefollow = cancel CUE affirm      (cue RE-ASSERTS; follow-cue = affirm)

FROZEN B2 GATE (s134; calib subset, calib=='1'): add construction >= 0.80 AND add control
  <= 0.40; cancel default >= 0.80; each in >= 2/3 models.
FROZEN VERDICTS (>= 2/3 models):
  ASYMMETRY (20 pp):  add_no_cue - cancel_no_cue >= 0.20 -> CONFIRMS (leg 1)
                      |.| < 0.20 -> SYMMETRIC (falsifies);  <= -0.20 -> REVERSAL (falsifies)
  FRAGILITY (10 pp):  cancel no-cue NLI-vs-FC disagreement - add's >= 0.10 -> leg 2
  CUE (inherited):    >= 0.70 follow-cue in >= 2/3 = robust
M2 DISCHARGED: both arms VERBAL -> a positive asymmetry is a CLEAN WITHIN-VERBAL confirm.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
SLOTS = ["A", "B", "C"]
ASYM, FRAG, CUE, MIN_MODELS = 0.20, 0.10, 0.70, 2
B2_CON, B2_CTRL, B2_DEF = 0.80, 0.40, 0.80


def affirm(rec, instrument):
    p = rec["pred"]
    return (1 if p == "0" else 0) if instrument == "nli" else (1 if p == "YES" else 0)


def load(instrument, slot):
    return json.load(open(os.path.join(RAW, f"{instrument}_{slot}.json")))


def rate(recs, arm, condition, instrument, calib_only=False):
    vals = [affirm(r, instrument) for r in recs
            if r["arm"] == arm and r["condition"] == condition
            and (not calib_only or r["calib"] == "1")]
    return (sum(vals) / len(vals)) if vals else None


def cells(slot, instrument):
    recs = load(instrument, slot)
    return {
        "add_no_cue": rate(recs, "add", "construction", instrument),
        "add_control": rate(recs, "add", "control", instrument),
        "add_cuefollow": 1 - rate(recs, "add", "cue", instrument),
        "cancel_default": rate(recs, "cancel", "default", instrument),
        "cancel_no_cue": 1 - rate(recs, "cancel", "construction", instrument),
        "cancel_cuefollow": rate(recs, "cancel", "cue", instrument),
    }


def b2_gate():
    """Read the frozen B2 gate from the calib subset of the same run (NLI primary)."""
    per = {}
    for s in SLOTS:
        recs = load("nli", s)
        per[s] = {
            "add_construction": rate(recs, "add", "construction", "nli", calib_only=True),
            "add_control": rate(recs, "add", "control", "nli", calib_only=True),
            "cancel_default": rate(recs, "cancel", "default", "nli", calib_only=True),
        }
    con_ok = sum(1 for s in SLOTS if per[s]["add_construction"] is not None
                 and per[s]["add_construction"] >= B2_CON)
    ctrl_ok = sum(1 for s in SLOTS if per[s]["add_control"] is not None
                  and per[s]["add_control"] <= B2_CTRL)
    def_ok = sum(1 for s in SLOTS if per[s]["cancel_default"] is not None
                 and per[s]["cancel_default"] >= B2_DEF)
    verdict = "GO" if (con_ok >= MIN_MODELS and ctrl_ok >= MIN_MODELS
                       and def_ok >= MIN_MODELS) else "NO-GO"
    return {"per_model": per, "add_con_models_ok": con_ok,
            "add_ctrl_models_ok": ctrl_ok, "cancel_def_models_ok": def_ok,
            "VERDICT": verdict}


def cancel_construction_by_verb():
    """Per-verb cancel-construction affirm (suppression visibility; PER-VERB discipline)."""
    out = {}
    for s in SLOTS:
        for arm_name, inst in (("nli", "nli"), ("fc", "fc")):
            recs = load(inst, s)
            d = {r["stem"]: affirm(r, inst) for r in recs
                 if r["arm"] == "cancel" and r["condition"] == "construction"}
            out[f"{s}_{arm_name}"] = d
    return out


def main():
    b2 = b2_gate()
    per_model = {s: {"nli": cells(s, "nli"), "fc": cells(s, "fc")} for s in SLOTS}

    asym_by_model, frag_by_model = {}, {}
    add_cue_ok, can_cue_ok = 0, 0
    for s in SLOTS:
        n, f = per_model[s]["nli"], per_model[s]["fc"]
        asym_by_model[s] = n["add_no_cue"] - n["cancel_no_cue"]
        add_d = abs(n["add_no_cue"] - f["add_no_cue"])
        can_d = abs(n["cancel_no_cue"] - f["cancel_no_cue"])
        frag_by_model[s] = {"add_disagree": round(add_d, 3),
                            "cancel_disagree": round(can_d, 3),
                            "cancel_minus_add": round(can_d - add_d, 3)}
        if n["add_cuefollow"] >= CUE:
            add_cue_ok += 1
        if n["cancel_cuefollow"] >= CUE:
            can_cue_ok += 1

    confirm = sum(1 for s in SLOTS if asym_by_model[s] >= ASYM)
    symmetric = sum(1 for s in SLOTS if abs(asym_by_model[s]) < ASYM)
    reversal = sum(1 for s in SLOTS if asym_by_model[s] <= -ASYM)
    if confirm >= MIN_MODELS:
        asym_verdict = "CONFIRMS (add easy / cancel hard, leg 1) — WITHIN-VERBAL"
    elif reversal >= MIN_MODELS:
        asym_verdict = "FALSIFIES — REVERSAL"
    elif symmetric >= MIN_MODELS:
        asym_verdict = "FALSIFIES — SYMMETRIC"
    else:
        asym_verdict = "INDETERMINATE (no direction in >=2/3 models)"

    frag_models = sum(1 for s in SLOTS if frag_by_model[s]["cancel_minus_add"] >= FRAG)
    frag_verdict = ("CONFIRMS leg 2 (cancel more instrument-fragile)"
                    if frag_models >= MIN_MODELS else
                    "leg 2 NOT met (cancel not reliably more fragile)")

    agg = {k: round(sum(per_model[s]["nli"][k] for s in SLOTS) / 3, 3)
           for k in per_model["A"]["nli"]}
    agg["asymmetry_add_minus_cancel"] = round(agg["add_no_cue"] - agg["cancel_no_cue"], 3)

    results = {
        "thresholds": {"asymmetry_pp": ASYM, "fragility_pp": FRAG, "cue_bar": CUE,
                       "min_models": MIN_MODELS, "b2": {"add_con": B2_CON,
                       "add_ctrl": B2_CTRL, "cancel_def": B2_DEF}},
        "B2_GATE": b2,
        "per_model": {s: {"nli": {k: round(v, 3) for k, v in per_model[s]["nli"].items()},
                          "fc": {k: round(v, 3) for k, v in per_model[s]["fc"].items()}}
                      for s in SLOTS},
        "aggregate_nli": agg,
        "asymmetry_by_model_nli": {s: round(asym_by_model[s], 3) for s in SLOTS},
        "asymmetry_confirm_models": confirm,
        "asymmetry_symmetric_models": symmetric,
        "asymmetry_reversal_models": reversal,
        "ASYMMETRY_VERDICT": asym_verdict,
        "fragility_by_model": frag_by_model,
        "fragility_confirm_models": frag_models,
        "FRAGILITY_VERDICT": frag_verdict,
        "add_cuefollow_robust_models": add_cue_ok,
        "cancel_cuefollow_robust_models": can_cue_ok,
        "cancel_construction_by_verb": cancel_construction_by_verb(),
    }
    json.dump(results, open(os.path.join(RAW, "results.json"), "w"), indent=1)

    print(f"=== B2 GATE (frozen; calib subset, NLI primary): {b2['VERDICT']} ===")
    for s in SLOTS:
        p = b2["per_model"][s]
        print(f"  {s}: add_con={p['add_construction']} add_ctrl={p['add_control']} "
              f"cancel_def={p['cancel_default']}")
    print(f"  models_ok: add_con={b2['add_con_models_ok']} add_ctrl={b2['add_ctrl_models_ok']}"
          f" cancel_def={b2['cancel_def_models_ok']}  (need >= {MIN_MODELS})\n")
    print("=== aggregate (NLI primary, mean of 3 models) ===")
    for k, v in agg.items():
        print(f"  {k:32s} {v}")
    print("\n=== per-model NLI asymmetry (add_no_cue - cancel_no_cue) ===")
    for s in SLOTS:
        n = per_model[s]["nli"]
        print(f"  {s}: add_no_cue={n['add_no_cue']:.3f} cancel_no_cue={n['cancel_no_cue']:.3f}"
              f"  asym={asym_by_model[s]:+.3f}")
    print(f"\nB2 GATE: {b2['VERDICT']}  (asymmetry meaningful only on GO)")
    print(f"ASYMMETRY (>= {ASYM} in >= {MIN_MODELS}/3): {results['ASYMMETRY_VERDICT']}"
          f"  [confirm={confirm} sym={symmetric} rev={reversal}]")
    print(f"FRAGILITY (cancel-add disagreement >= {FRAG} in >= {MIN_MODELS}/3): "
          f"{results['FRAGILITY_VERDICT']}  [models={frag_models}]")
    print(f"CUE-FOLLOW robust (>= {CUE} in >= {MIN_MODELS}/3): "
          f"add={add_cue_ok}/3  cancel={can_cue_ok}/3")


if __name__ == "__main__":
    main()
