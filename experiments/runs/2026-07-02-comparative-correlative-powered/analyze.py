"""Analyze the POWERED CC re-run (A2a, 2026-07-02) — magnitudes WITH intervals.

Same quantities as the frozen v1 analyzer (assertion-rate T1 gap, inverse-flip rate,
typical-vs-atypical robustness, NLI cc-vs-ctrl gap) PLUS the thing the v1 run could not give
and the claim explicitly defers to this run: a 95% confidence INTERVAL on each magnitude.

Intervals are CLUSTER bootstrap over scale PAIRS (2000 resamples, fixed seed): the four item
forms of a pair are not independent, so we resample whole pairs with replacement and recompute
each statistic. This is the honest interval for a nested item design; a naive item-level
bootstrap would understate width. The frozen thresholds (T1>=30pp / T2>=70% / T3 within 15pp)
are reported for continuity with v1 but the deliverable here is the point estimate + CI, not a
pass/fail gate.

Emits results.json (machine) and prints a human table. No item-level cherry-picking; no retuning.
"""
import json, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
PANEL = ["A", "B", "C"]
MODELS = {"A": "anthropic/claude-sonnet-4.6",
          "B": "openai/gpt-5.4-mini",
          "C": "google/gemini-3.5-flash"}
B_BOOT = 2000
SEED = 20260702


def load(arm, slot):
    return json.load(open(os.path.join(RAW, f"{arm}_{slot}.json")))


# ---- point statistics computed over a LIST of records ----

def _asrt(recs):
    """assertion rate: fraction predicting a direction (increase/decrease), among parsed."""
    p = [r for r in recs if r["pred"] is not None]
    if not p:
        return None
    return sum(1 for r in p if r["pred"] in ("increase", "decrease")) / len(p)


def _acc(recs, pred_key, gold_key):
    p = [r for r in recs if r[pred_key] is not None]
    if not p:
        return None
    return sum(1 for r in p if str(r[pred_key]) == str(r[gold_key])) / len(p)


def _flip(recs):
    """inverse-CC direction-flip: fraction of cc-inverse items answered 'decrease'."""
    inv = [r for r in recs if r["form"] == "cc-inverse" and r["pred"] is not None]
    if not inv:
        return None
    return sum(1 for r in inv if r["pred"] == "decrease") / len(inv)


def _posinc(recs):
    pos = [r for r in recs if r["form"] == "cc-positive" and r["pred"] is not None]
    if not pos:
        return None
    return sum(1 for r in pos if r["pred"] == "increase") / len(pos)


# statistics that take (fc_recs, nli_recs) and return a scalar (or None)
def stat_t1_gap(fc, nli):
    cc = [r for r in fc if r["form"] in ("cc-positive", "cc-inverse")]
    ctrl = [r for r in fc if r["form"] in ("ctrl-two", "ctrl-single")]
    a, b = _asrt(cc), _asrt(ctrl)
    return None if a is None or b is None else (a - b) * 100


def stat_flip(fc, nli):
    v = _flip(fc)
    return None if v is None else v * 100


def stat_posinc(fc, nli):
    v = _posinc(fc)
    return None if v is None else v * 100


def stat_typ_minus_atyp(fc, nli):
    cc = [r for r in fc if r["form"] in ("cc-positive", "cc-inverse")]
    typ = _acc([r for r in cc if r["typicality"] == "typical"], "pred", "fc_gold")
    aty = _acc([r for r in cc if r["typicality"] == "atypical"], "pred", "fc_gold")
    return None if typ is None or aty is None else (typ - aty) * 100


def stat_atyp_assert(fc, nli):
    cc_aty = [r for r in fc if r["form"] in ("cc-positive", "cc-inverse")
              and r["typicality"] == "atypical"]
    v = _asrt(cc_aty)
    return None if v is None else v * 100


def stat_nli_gap(fc, nli):
    cc = _acc([r for r in nli if r["form"] in ("cc-positive", "cc-inverse")], "pred", "nli_gold")
    ctrl = _acc([r for r in nli if r["form"] in ("ctrl-two", "ctrl-single")], "pred", "nli_gold")
    return None if cc is None or ctrl is None else (cc - ctrl) * 100


def stat_fc_cc_accuracy(fc, nli):
    """FC covariation-direction accuracy on CC items (headline deployment rate)."""
    v = _acc([r for r in fc if r["form"] in ("cc-positive", "cc-inverse")], "pred", "fc_gold")
    return None if v is None else v * 100


def stat_nli_cc_accuracy(fc, nli):
    """NLI covariation-reading accuracy on CC items (cross-instrument deployment rate)."""
    v = _acc([r for r in nli if r["form"] in ("cc-positive", "cc-inverse")], "pred", "nli_gold")
    return None if v is None else v * 100


STATS = {
    "fc_cc_accuracy_pct": stat_fc_cc_accuracy,
    "fc_T1_assertion_gap_pp": stat_t1_gap,
    "fc_inverse_flip_pct": stat_flip,
    "fc_positive_increase_pct": stat_posinc,
    "fc_typ_minus_atyp_pp": stat_typ_minus_atyp,
    "fc_atypical_assertion_pct": stat_atyp_assert,
    "nli_cc_accuracy_pct": stat_nli_cc_accuracy,
    "nli_cc_vs_ctrl_gap_pp": stat_nli_gap,
}


def cluster_bootstrap(fc, nli, statfn):
    """Resample whole scale pairs with replacement; recompute statfn each draw."""
    pairs = sorted({r["scale_pair"] for r in fc})
    fc_by = {p: [r for r in fc if r["scale_pair"] == p] for p in pairs}
    nli_by = {p: [r for r in nli if r["scale_pair"] == p] for p in pairs}
    rng = random.Random(SEED)
    vals = []
    n = len(pairs)
    for _ in range(B_BOOT):
        draw = [pairs[rng.randrange(n)] for _ in range(n)]
        fcs, nlis = [], []
        for p in draw:
            fcs.extend(fc_by[p])
            nlis.extend(nli_by[p])
        v = statfn(fcs, nlis)
        if v is not None:
            vals.append(v)
    if not vals:
        return None, None
    vals.sort()
    lo = vals[int(0.025 * len(vals))]
    hi = vals[min(len(vals) - 1, int(0.975 * len(vals)))]
    return round(lo, 1), round(hi, 1)


def analyze_slot(slot):
    fc = load("constructed-fc", slot)
    nli = load("constructed-nli", slot)
    out = {"model": MODELS[slot], "n_fc": len(fc), "n_nli": len(nli),
           "na": {"fc": sum(1 for r in fc if r["pred"] is None),
                  "nli": sum(1 for r in nli if r["pred"] is None)},
           "point": {}, "ci95": {}}
    for name, fn in STATS.items():
        pt = fn(fc, nli)
        out["point"][name] = None if pt is None else round(pt, 1)
        out["ci95"][name] = cluster_bootstrap(fc, nli, fn)
    return out


def main():
    res = {slot: analyze_slot(slot) for slot in PANEL}

    # frozen-threshold gates (continuity with v1; not the deliverable)
    T1 = sum(1 for s in PANEL if (res[s]["point"]["fc_T1_assertion_gap_pp"] or -999) >= 30)
    T2 = sum(1 for s in PANEL if (res[s]["point"]["fc_inverse_flip_pct"] or -1) >= 70)
    T3 = sum(1 for s in PANEL if res[s]["point"]["fc_typ_minus_atyp_pp"] is not None
             and abs(res[s]["point"]["fc_typ_minus_atyp_pp"]) <= 15
             and (res[s]["point"]["fc_atypical_assertion_pct"] or 0) > 50)
    gates = {"T1_ge_30pp": f"{T1}/3", "T2_flip_ge_70pct": f"{T2}/3",
             "T3_atypical_within_15pp": f"{T3}/3", "confirm": ">=2/3 each"}

    print("\n========= COMPARATIVE-CORRELATIVE POWERED RE-RUN (A2a) — MAGNITUDES + 95% CI =========")
    print("34 fresh scale pairs x 4 forms = 136 items; cluster bootstrap over pairs, B=2000, seed fixed.\n")
    for name in STATS:
        print(f"--- {name} ---")
        for s in PANEL:
            pt = res[s]["point"][name]
            lo, hi = res[s]["ci95"][name]
            ptxt = "  NA" if pt is None else f"{pt:6.1f}"
            citxt = "" if lo is None else f"  [{lo:.1f}, {hi:.1f}]"
            print(f"  {MODELS[s][:26]:<26} {ptxt}{citxt}")
        print()
    print("Frozen-threshold gates (continuity with v1; not the deliverable):")
    for k, v in gates.items():
        print(f"  {k}: {v}")

    out = {"per_model": res, "gates": gates,
           "meta": {"b_boot": B_BOOT, "seed": SEED, "n_pairs": 34, "n_items": 136,
                    "bootstrap": "cluster over scale_pair"}}
    with open(os.path.join(RAW, "results.json"), "w") as f:
        json.dump(out, f, indent=1)
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
