#!/usr/bin/env python3
"""analyze.py -- pre-registered analysis for the DATIVE information-structure probe.

PRIMARY (corpus-licensed, decision-bearing). Per model, the WITHIN-ITEM preference shift
    shift(item) = mean(DOC-pref | recipient-given) - mean(DOC-pref | theme-given)
averaged over the A/B counterbalancing. Human prediction: shift > 0 (a given recipient
favours DOC; a given theme favours PD). Reported with a nonparametric bootstrap 95% CI
over items and a one-sided sign test (items with shift>0). Per-model verdict:
    CONFIRM    : mean shift > 0 AND bootstrap 95% lower bound > 0 (the human direction,
                 length+animacy held constant by construction).
    WEAK       : mean shift > 0 but CI includes 0 (a directional hint that does not clear).
    FALSIFY    : mean shift <= 0 (no shift, or the wrong direction).
Panel verdict: CONFIRM if >=2/3 models CONFIRM.

CONTROL arm (condition (b)): the same shift on the 12 control items, whose dissociating
cells pit information structure against end-weight (the given constituent is the LONGER
one). A shift that SURVIVES here cannot be a short-before-long artifact. (The within-item
shift is already length-immune by construction -- the control arm is the stronger,
absolute-order-level check.)

NEUTRAL baseline: mean DOC-pref in the both-new context -> the model's default.

SECONDARY (anchor-dependent, NON-decisive -- ratification modification 2). Spearman
correlation between each model's per-cell DOC-pref and the corpus-model predicted
P(NP=DOC) for that cell's factor configuration (computed from the firsthand-inspected
languageR::dative logistic fit, corpus_inspection.json). May STRENGTHEN a confirm or
characterize a weak result; may NOT convert weak->confirm nor rescue a failed primary.
"""
import json
import math
import os

import numpy as np

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
STIM = json.load(open(os.path.join(HERE, "stimuli.json")))
FIT = json.load(open(os.path.join(HERE, "corpus_inspection.json")))["corpus_model"]
RNG = np.random.default_rng(20260620)

# ---- per-item animacy coding for the SECONDARY corpus-gradient only (pre-registered;
# does not touch the frozen stimuli). Recipients are animate people/roles EXCEPT the
# institutional recipients of the long-theme control items (coded inanimate, conservative).
# Themes are all inanimate. ----
INANIMATE_REC_ITEMS = {"tlong1", "tlong2", "tlong3", "tlong4", "tlong5", "tlong6"}


def corpus_p_np(item, context_kind):
    """Corpus-model predicted P(NP=DOC) for this cell's factor configuration.

    Applies the firsthand languageR::dative logistic fit (predicts P(PP); we return
    P(NP)=1-P(PP)). Factor mapping: givenness from the context; pronominality constant
    (nonpronominal full NPs); definiteness from the NP article; animacy as coded above;
    log length difference from the item's recipient/theme word counts."""
    coef = FIT["coefficients"]
    rec, thm = item["rec"], item["thm"]
    rl, tl = len(rec.split()), len(thm.split())
    access = {"rec_given": ("given", "new"),
              "thm_given": ("new", "given"),
              "neutral": ("accessible", "accessible")}[context_kind]
    rec_def = "definite" if rec.lower().startswith("the ") else "indefinite"
    thm_def = "definite" if thm.lower().startswith("the ") else "indefinite"
    rec_anim = "inanimate" if item["id"] in INANIMATE_REC_ITEMS else "animate"

    z = coef["const"]
    z += coef["log_theme_minus_rec_len"] * (math.log(tl) - math.log(rl))
    # treatment-coded dummies (reference = first alpha level, dropped). Add the coef only
    # when the cell is at the non-reference level.
    def add(name, level):
        nonlocal z
        key = f"{name}_{level}"
        if key in coef:
            z += coef[key]
    add("AccessOfRec", access[0]); add("AccessOfTheme", access[1])
    # Pronom reference = nonpronominal (dropped) -> add nothing (constant across cells).
    add("DefinOfRec", rec_def); add("DefinOfTheme", thm_def)
    add("AnimacyOfRec", rec_anim); add("AnimacyOfTheme", "inanimate")
    p_pp = 1.0 / (1.0 + math.exp(-z))
    return 1.0 - p_pp   # P(NP = double object = DOC)


def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    def rank(v):
        order = v.argsort()
        r = np.empty_like(order, float)
        r[order] = np.arange(len(v))
        # average ties
        _, inv, cnt = np.unique(v, return_inverse=True, return_counts=True)
        means = np.zeros(len(cnt))
        sums = np.zeros(len(cnt)); counts = np.zeros(len(cnt))
        np.add.at(sums, inv, r); np.add.at(counts, inv, 1)
        means = sums / counts
        return means[inv]
    rx, ry = rank(x), rank(y)
    if rx.std() == 0 or ry.std() == 0:
        return float("nan")
    return float(np.corrcoef(rx, ry)[0, 1])


def cell_pref(rows, item_id, ctx):
    vals = [r["doc_pref"] for r in rows
            if r["item"] == item_id and r["context_kind"] == ctx and r["doc_pref"] is not None]
    return float(np.mean(vals)) if vals else None


def analyze_model(name):
    rows = C.read_jsonl(os.path.join(C.RAW, f"probe-{name}.jsonl"))
    n_total = len(rows)
    n_na = sum(1 for r in rows if r["doc_pref"] is None)
    n_retried = sum(1 for r in rows if r.get("retried"))
    n_len = sum(1 for r in rows if r.get("finish_reason") == "length")
    items = {it["id"]: it for it in STIM["items"]}

    def shifts(arm):
        out = {}
        for it in STIM["items"]:
            if it["arm"] != arm:
                continue
            rg = cell_pref(rows, it["id"], "rec_given")
            tg = cell_pref(rows, it["id"], "thm_given")
            if rg is not None and tg is not None:
                out[it["id"]] = rg - tg
        return out

    main_shifts = shifts("main")
    ctrl_shifts = shifts("control")
    sv = np.array(list(main_shifts.values()))

    # bootstrap 95% CI of the mean shift over items
    if len(sv):
        boot = np.array([RNG.choice(sv, len(sv), replace=True).mean() for _ in range(10000)])
        lo, hi = np.percentile(boot, [2.5, 97.5])
        mean_shift = float(sv.mean())
        n_pos = int((sv > 0).sum()); n_items = len(sv)
        # one-sided sign test p = P(>= n_pos successes | p=0.5)
        p_sign = sum(math.comb(n_items, k) for k in range(n_pos, n_items + 1)) / (2 ** n_items)
    else:
        lo = hi = mean_shift = float("nan"); n_pos = n_items = 0; p_sign = float("nan")

    if len(sv) and mean_shift > 0 and lo > 0:
        verdict = "CONFIRM"
    elif len(sv) and mean_shift > 0:
        verdict = "WEAK"
    else:
        verdict = "FALSIFY"

    # neutral baseline
    neut = [cell_pref(rows, it["id"], "neutral") for it in STIM["items"] if it["arm"] == "main"]
    neut = [v for v in neut if v is not None]
    neutral_default = float(np.mean(neut)) if neut else None

    # SECONDARY: corpus gradient correlation (rec_given + thm_given cells, all items)
    xs, ys = [], []
    for it in STIM["items"]:
        for ctx in ("rec_given", "thm_given"):
            mp = cell_pref(rows, it["id"], ctx)
            if mp is not None:
                xs.append(corpus_p_np(items[it["id"]], ctx)); ys.append(mp)
    rho = spearman(xs, ys) if len(xs) > 2 else float("nan")

    ctrl_arr = np.array(list(ctrl_shifts.values()))
    return {
        "model": name, "verdict": verdict,
        "n_total": n_total, "n_NA": n_na, "n_retried": n_retried, "n_length_trunc": n_len,
        "main_mean_shift": round(mean_shift, 4),
        "main_shift_ci95": [round(float(lo), 4), round(float(hi), 4)],
        "main_items_positive": f"{n_pos}/{n_items}", "sign_test_p_onesided": round(p_sign, 5),
        "control_mean_shift": round(float(ctrl_arr.mean()), 4) if len(ctrl_arr) else None,
        "control_items_positive": (f"{int((ctrl_arr>0).sum())}/{len(ctrl_arr)}"
                                   if len(ctrl_arr) else None),
        "neutral_baseline_doc_pref": round(neutral_default, 4) if neutral_default is not None else None,
        "secondary_spearman_rho_vs_corpus_gradient": round(rho, 4),
        "per_item_main_shift": {k: round(v, 3) for k, v in main_shifts.items()},
        "per_item_control_shift": {k: round(v, 3) for k, v in ctrl_shifts.items()},
    }


def main():
    results = [analyze_model(n) for n in C.MODELS]
    n_confirm = sum(1 for r in results if r["verdict"] == "CONFIRM")
    panel = "CONFIRM" if n_confirm >= 2 else ("WEAK" if any(r["verdict"] != "FALSIFY" for r in results) else "FALSIFY")

    # cost from the per-model jsonl usage fields
    all_rows = []
    for n in C.MODELS:
        all_rows += [{"usage": u} for r in C.read_jsonl(os.path.join(C.RAW, f"probe-{n}.jsonl"))
                     for u in (r.get("usage") or [])]
    billed, have, missing = C.billed_cost([all_rows])

    out = {"panel_verdict": panel, "n_models_confirm": n_confirm,
           "stimuli_sha256": __import__("hashlib").sha256(
               open(os.path.join(HERE, "stimuli.json"), "rb").read()).hexdigest(),
           "billed_usd": round(billed, 6), "n_cost_have": have, "n_cost_missing": missing,
           "models": results}
    json.dump(out, open(os.path.join(HERE, "analysis.json"), "w"), indent=2)

    print(f"PANEL VERDICT: {panel} ({n_confirm}/3 models CONFIRM)")
    print(f"billed ${billed:.5f} ({have} calls, {missing} missing cost)")
    for r in results:
        print(f"\n[{r['model']}] {r['verdict']}")
        print(f"  main shift={r['main_mean_shift']} CI95={r['main_shift_ci95']} "
              f"pos={r['main_items_positive']} sign-p={r['sign_test_p_onesided']}")
        print(f"  control shift={r['control_mean_shift']} pos={r['control_items_positive']}")
        print(f"  neutral DOC-pref={r['neutral_baseline_doc_pref']}")
        print(f"  secondary Spearman rho vs corpus gradient={r['secondary_spearman_rho_vs_corpus_gradient']}")
        print(f"  data: NA={r['n_NA']} retried={r['n_retried']} length-trunc={r['n_length_trunc']} of {r['n_total']}")


if __name__ == "__main__":
    main()
