"""Analyze the add-arm headroom calibration. Reads raw/{nli,fc}_{A,B,C}.json, applies the
FROZEN reading rule from PREREG.md, emits raw/results.json. No threshold tuned after data.

affirm = NLI label '0' (entailment) | FC 'YES'. construction arm wants ceiling; control
arm wants off-ceiling. per-verb headroom = construction_affirm - control_affirm.

FROZEN GATE (PREREG.md):
  verb HEADROOM-CLEAN (panel aggregate, NLI primary): construction affirm >= 0.80 AND
    control affirm <= 0.40.
  construction DEMONSTRATES HEADROOM: >= 4/12 verbs headroom-clean in aggregate AND
    >= 1 such verb headroom-clean in >= 2/3 models individually.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
SLOTS = ["A", "B", "C"]
CEIL = 0.80
FLOOR = 0.40
MIN_CLEAN = 4


def affirm(rec, instrument):
    p = rec["pred"]
    if instrument == "nli":
        return 1 if p == "0" else 0
    return 1 if p == "YES" else 0


def load(instrument, slot):
    return json.load(open(os.path.join(RAW, f"{instrument}_{slot}.json")))


def per_model_rates(instrument):
    """{slot: {construction: {stem: {construction_arm: rate, control_arm: rate}}}}"""
    out = {}
    for slot in SLOTS:
        recs = load(instrument, slot)
        d = {}
        for r in recs:
            d.setdefault(r["construction"], {}).setdefault(r["stem"], {})[r["condition"]] = \
                affirm(r, instrument)
        out[slot] = d
    return out


def main():
    results = {"gate": {"ceiling": CEIL, "floor": FLOOR, "min_clean": MIN_CLEAN},
               "by_construction": {}}
    nli = per_model_rates("nli")
    fc = per_model_rates("fc")
    constructions = sorted({c for slot in SLOTS for c in nli[slot]})

    for con in constructions:
        stems = sorted(nli["A"][con])
        verbs = {}
        clean_aggregate = []
        clean_in_2of3 = []
        for stem in stems:
            # panel-aggregate NLI affirm per arm
            con_aff = [nli[s][con][stem].get("construction", 0) for s in SLOTS]
            ctl_aff = [nli[s][con][stem].get("control", 0) for s in SLOTS]
            con_mean = sum(con_aff) / 3
            ctl_mean = sum(ctl_aff) / 3
            headroom = con_mean - ctl_mean
            agg_clean = con_mean >= CEIL and ctl_mean <= FLOOR
            # per-model clean count (a model is clean on this verb if its own
            # construction affirm = 1 and control affirm = 0)
            per_model_clean = sum(1 for i in range(3)
                                  if con_aff[i] == 1 and ctl_aff[i] == 0)
            if agg_clean:
                clean_aggregate.append(stem)
            if per_model_clean >= 2:
                clean_in_2of3.append(stem)
            verbs[stem] = {
                "nli_construction_affirm": con_aff, "nli_control_affirm": ctl_aff,
                "nli_construction_mean": round(con_mean, 3),
                "nli_control_mean": round(ctl_mean, 3),
                "nli_headroom": round(headroom, 3),
                "aggregate_clean": agg_clean, "per_model_clean": per_model_clean,
                "fc_construction_affirm": [fc[s][con][stem].get("construction", 0) for s in SLOTS],
                "fc_control_affirm": [fc[s][con][stem].get("control", 0) for s in SLOTS],
            }
        demonstrates = (len(clean_aggregate) >= MIN_CLEAN
                        and any(v in clean_in_2of3 for v in clean_aggregate))
        # arm-level means
        con_arm = [v["nli_construction_mean"] for v in verbs.values()]
        ctl_arm = [v["nli_control_mean"] for v in verbs.values()]
        results["by_construction"][con] = {
            "n_verbs": len(stems),
            "mean_construction_affirm_nli": round(sum(con_arm) / len(con_arm), 3),
            "mean_control_affirm_nli": round(sum(ctl_arm) / len(ctl_arm), 3),
            "clean_aggregate": clean_aggregate,
            "n_clean_aggregate": len(clean_aggregate),
            "clean_in_2of3_models": clean_in_2of3,
            "DEMONSTRATES_HEADROOM": demonstrates,
            "verbs": verbs,
        }

    json.dump(results, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    # console summary
    for con, r in results["by_construction"].items():
        print(f"\n=== {con} ===")
        print(f"  mean construction affirm (NLI): {r['mean_construction_affirm_nli']}")
        print(f"  mean control affirm (NLI):      {r['mean_control_affirm_nli']}")
        print(f"  headroom-clean verbs (>= {CEIL} con & <= {FLOOR} ctl): "
              f"{r['n_clean_aggregate']}/{r['n_verbs']}  {r['clean_aggregate']}")
        print(f"  clean in >= 2/3 models: {r['clean_in_2of3_models']}")
        print(f"  DEMONSTRATES HEADROOM (>= {MIN_CLEAN} clean & >=1 robust): "
              f"{r['DEMONSTRATES_HEADROOM']}")
        for stem, v in r["verbs"].items():
            print(f"    {stem:9s} con={v['nli_construction_mean']:.2f} "
                  f"ctl={v['nli_control_mean']:.2f} headroom={v['nli_headroom']:+.2f} "
                  f"{'CLEAN' if v['aggregate_clean'] else ''}")


if __name__ == "__main__":
    main()
