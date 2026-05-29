"""Analyze the CC probe outputs against the frozen thresholds (2026-05-29).

Thresholds are fixed by the ratified constructional-divergence-operationalization
decision and the design (NOT retuned after seeing results):
  T1  CC-vs-control covariation gap >= 30 pp           (primary indicator)
  T2  inverse-CC direction-flip rate >= 70%            (discriminating indicator)
  T3  atypical-pair rate within 15 pp of typical-pair  (generalization indicator)
A finding "supports" the conjecture's clause only if met in >= 2 of 3 panel models.

Emits results.json (machine) and prints a human table. No item-level cherry-picking.
"""
import json, os, glob

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
PANEL = ["A", "B", "C"]
MODELS = {"A": "anthropic/claude-sonnet-4.6",
          "B": "openai/gpt-5.4-mini",
          "C": "google/gemini-3.5-flash"}


def load(arm, slot):
    p = os.path.join(RAW, f"{arm}_{slot}.json")
    return json.load(open(p))


def rate(recs, pred_key, gold_key, filt=None):
    """fraction correct among parseable; returns (rate, n, n_na)."""
    sel = [r for r in recs if (filt is None or filt(r))]
    parsed = [r for r in sel if r[pred_key] is not None]
    na = len(sel) - len(parsed)
    if not parsed:
        return None, 0, na
    correct = sum(1 for r in parsed if str(r[pred_key]) == str(r[gold_key]))
    return correct / len(parsed), len(parsed), na


def by_form(recs, form):
    return [r for r in recs if r["form"] == form]


def analyze_slot(slot):
    nli = load("constructed-nli", slot)
    fc = load("constructed-fc", slot)
    sci = load("scivetti-nli", slot)
    out = {"model": MODELS[slot]}

    # --- Forced-choice arm: grounds direction indicators (closest to semantic task) ---
    fc_cc = [r for r in fc if r["form"] in ("cc-positive", "cc-inverse")]
    fc_ctrl = [r for r in fc if r["form"] in ("ctrl-two", "ctrl-single")]

    # (i) covariation-CORRECT rate: pred == fc_gold. For CC, gold is a direction; for
    #     controls, gold is "undetermined". So this is ACCURACY, near-ceiling for both,
    #     and its CC-minus-control difference is NOT the design's T1 intent.
    cc_rate, cc_n, cc_na = rate(fc_cc, "pred", "fc_gold")
    ctrl_rate, ctrl_n, ctrl_na = rate(fc_ctrl, "pred", "fc_gold")
    out["fc_cc_accuracy"] = cc_rate
    out["fc_ctrl_accuracy"] = ctrl_rate

    # (ii) covariation-ASSERTION rate: fraction asserting a direction (increase/decrease)
    #      rather than "undetermined". This is the design's T1 quantity — it "isolates
    #      the construction as the source of the inference": CC should assert, matched
    #      controls (same words, no CC syntax) should NOT.
    def assert_rate(recs):
        p = [r for r in recs if r["pred"] is not None]
        if not p:
            return None
        return sum(1 for r in p if r["pred"] in ("increase", "decrease")) / len(p)
    cc_assert = assert_rate(fc_cc)
    ctrl_assert = assert_rate(fc_ctrl)
    out["fc_cc_assertion_rate"] = (None if cc_assert is None else round(cc_assert, 3))
    out["fc_ctrl_assertion_rate"] = (None if ctrl_assert is None else round(ctrl_assert, 3))
    out["fc_cc_vs_ctrl_gap_pp"] = (None if cc_assert is None or ctrl_assert is None
                                   else round((cc_assert - ctrl_assert) * 100, 1))
    # keep the accuracy-difference too, clearly labelled, for transparency
    out["fc_cc_vs_ctrl_accuracy_diff_pp"] = (None if cc_rate is None or ctrl_rate is None
                                             else round((cc_rate - ctrl_rate) * 100, 1))
    # backward-compat aliases used by the table
    out["fc_cc_rate"] = cc_rate
    out["fc_ctrl_rate"] = ctrl_rate

    # direction-flip on inverse CC: fraction of inverse items answered "decrease"
    inv = by_form(fc, "cc-inverse")
    inv_p = [r for r in inv if r["pred"] is not None]
    out["fc_inverse_flip_rate"] = (None if not inv_p else
        round(sum(1 for r in inv_p if r["pred"] == "decrease") / len(inv_p), 3))
    pos = by_form(fc, "cc-positive")
    pos_p = [r for r in pos if r["pred"] is not None]
    out["fc_positive_increase_rate"] = (None if not pos_p else
        round(sum(1 for r in pos_p if r["pred"] == "increase") / len(pos_p), 3))

    # atypical vs typical (CC items, fc covariation-correct)
    typ_rate, _, _ = rate([r for r in fc_cc if r["typicality"] == "typical"], "pred", "fc_gold")
    aty_rate, _, _ = rate([r for r in fc_cc if r["typicality"] == "atypical"], "pred", "fc_gold")
    out["fc_typical_rate"] = typ_rate
    out["fc_atypical_rate"] = aty_rate
    out["fc_typ_minus_atyp_pp"] = (None if typ_rate is None or aty_rate is None
                                   else round((typ_rate - aty_rate) * 100, 1))

    # --- NLI arm on constructed items (parallel, for cross-instrument read) ---
    nli_cc = [r for r in nli if r["form"] in ("cc-positive", "cc-inverse")]
    nli_ctrl = [r for r in nli if r["form"] in ("ctrl-two", "ctrl-single")]
    out["nli_cc_rate"], _, _ = rate(nli_cc, "pred", "nli_gold")
    out["nli_ctrl_rate"], _, _ = rate(nli_ctrl, "pred", "nli_gold")
    if out["nli_cc_rate"] is not None and out["nli_ctrl_rate"] is not None:
        out["nli_cc_vs_ctrl_gap_pp"] = round((out["nli_cc_rate"] - out["nli_ctrl_rate"]) * 100, 1)
    else:
        out["nli_cc_vs_ctrl_gap_pp"] = None

    # --- Human-comparison arm: NLI accuracy on the 30 real Scivetti CC items ---
    sci_rate, sci_n, sci_na = rate(sci, "pred", "gold")
    out["scivetti_nli_accuracy"] = sci_rate
    out["scivetti_n"] = sci_n
    out["scivetti_na"] = sci_na

    # NA bookkeeping
    out["na"] = {"nli": sum(1 for r in nli if r["pred"] is None),
                 "fc": sum(1 for r in fc if r["pred"] is None),
                 "scivetti": sci_na}
    return out


def fmt(x, scale=False):
    if x is None:
        return "  NA"
    if scale:
        return f"{x*100:4.0f}%"
    return f"{x:5.1f}"


def main():
    res = {slot: analyze_slot(slot) for slot in PANEL}

    # threshold gates (>= 2 of 3 models)
    T1 = sum(1 for s in PANEL if (res[s]["fc_cc_vs_ctrl_gap_pp"] or -999) >= 30)
    T2 = sum(1 for s in PANEL if (res[s]["fc_inverse_flip_rate"] or -1) >= 0.70)
    T3 = sum(1 for s in PANEL if res[s]["fc_typ_minus_atyp_pp"] is not None
             and abs(res[s]["fc_typ_minus_atyp_pp"]) <= 15
             and (res[s]["fc_atypical_rate"] or 0) > 0.5)
    gates = {"T1_cc_vs_ctrl_ge_30pp": f"{T1}/3",
             "T2_inverse_flip_ge_70pct": f"{T2}/3",
             "T3_atypical_within_15pp": f"{T3}/3",
             "confirm_requires": ">=2/3 on each"}

    print("\n================ COMPARATIVE-CORRELATIVE PROBE v1 — RESULTS ================")
    print("Scivetti human baseline (aggregate, Exp1): native-speaker accuracy ~0.90")
    print("T1 gap = CC covariation-ASSERTION rate minus control assertion rate (design intent)\n")
    hdr = ("model", "ccAssert", "ctlAssert", "T1gapPP", "invFlip", "posInc", "typ%", "atyp%",
           "nliCC%", "sciAcc", "NA")
    print("{:<26}{:>9}{:>10}{:>8}{:>9}{:>8}{:>7}{:>8}{:>8}{:>8}{:>5}".format(*hdr))
    for s in PANEL:
        r = res[s]
        print("{:<26}{:>9}{:>10}{:>8}{:>9}{:>8}{:>7}{:>8}{:>8}{:>8}{:>5}".format(
            r["model"][:26],
            fmt(r["fc_cc_assertion_rate"], True), fmt(r["fc_ctrl_assertion_rate"], True),
            fmt(r["fc_cc_vs_ctrl_gap_pp"]),
            fmt(r["fc_inverse_flip_rate"], True), fmt(r["fc_positive_increase_rate"], True),
            fmt(r["fc_typical_rate"], True), fmt(r["fc_atypical_rate"], True),
            fmt(r["nli_cc_rate"], True),
            fmt(r["scivetti_nli_accuracy"], True),
            sum(r["na"].values())))
    print("\nGATES (>=2/3 to support a clause):")
    for k, v in gates.items():
        print(f"  {k}: {v}")

    out = {"per_model": res, "gates": gates}
    with open(os.path.join(RAW, "results.json"), "w") as f:
        json.dump(out, f, indent=1)
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
