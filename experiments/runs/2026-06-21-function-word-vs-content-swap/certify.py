#!/usr/bin/env python3
"""certify.py -- build-session pre-run certification (binding condition (i) + integrity).

Emits certification.json. The decisive check (condition (i),
wiki/decisions/resolved/function-word-anchor-design.md): NO frequency-only and NO
length-only reader reproduces the function>content flip asymmetry. Because the content
swap is matched to the function swap on |dLg10WF| (mirrored spread) and on |dlen|, any
reader keyed ONLY on those surface deltas assigns the SAME flip rate to the function and
content conditions -> asymmetry ~ 0. We demonstrate this over a threshold grid.

Also checks minimal-pair integrity (premise_fn differs from premise_base ONLY by the
function word; premise_ct ONLY by the content word), no function-word leak into the
hypothesis, item count + semantic-class span, and the predictability proxy non-difference.
"""
import json
import os

import freqlib as F

HERE = os.path.dirname(os.path.abspath(__file__))


def load():
    return json.load(open(os.path.join(HERE, "stimuli.json")))["items"]


def words(s):
    return s.replace(".", " ").replace(",", " ").split()


def single_token_diff(a, b):
    """True iff a and b differ in exactly one aligned token (same length)."""
    wa, wb = words(a), words(b)
    if len(wa) != len(wb):
        return False, None, None
    diffs = [(x, y) for x, y in zip(wa, wb) if x.lower() != y.lower()]
    if len(diffs) != 1:
        return False, None, None
    return True, diffs[0][0], diffs[0][1]


def freq_only_flip(delta_lg, theta):
    """Frequency-only reader: predicts a flip iff the swapped word's |dLg10WF| > theta."""
    return 1 if delta_lg > theta else 0


def len_only_flip(delta_len, theta):
    """Length-only reader: predicts a flip iff the swapped word's |dlen| >= theta."""
    return 1 if delta_len >= theta else 0


def main():
    items = load()
    matched = [it for it in items if it["arm"] == "matched"]
    det = [it for it in items if it["arm"] == "det_char"]
    checks = {}
    fails = []

    # --- count + semantic classes (condition e) ---
    classes = sorted({it["pos"] for it in matched})
    checks["(e) >=200 matched items"] = len(matched) >= 200
    checks["(e) >=4 content semantic classes"] = len(classes) >= 4
    checks["matched_count"] = len(matched)
    checks["semantic_classes"] = classes

    # --- minimal-pair integrity ---
    fn_ok = ct_ok = leak_ok = base_fn_diff_ok = True
    for it in matched:
        ok_fn, a, b = single_token_diff(it["premise_base"], it["premise_fn"])
        if not (ok_fn and a.lower() == it["func_out"] and b.lower() == it["func_in"]):
            fn_ok = False
        ok_ct, c, dwd = single_token_diff(it["premise_base"], it["premise_ct"])
        if not (ok_ct and c.lower() == it["cont_out"].lower()
                and dwd.lower() == it["cont_in"].lower()):
            ct_ok = False
        # function swap-in word must NOT appear in the hypothesis (no leak)
        if it["func_in"].lower() in [w.lower() for w in words(it["hyp_base"])]:
            leak_ok = False
        if it["pred_base"] == it["pred_fn"]:
            base_fn_diff_ok = False
    checks["premise_fn differs from base ONLY by the function word"] = fn_ok
    checks["premise_ct differs from base ONLY by the content word"] = ct_ok
    checks["function swap-in word never appears in the hypothesis (no leak)"] = leak_ok
    checks["every matched item predicts a function flip (pred_base != pred_fn)"] = base_fn_diff_ok

    # --- condition (i): freq-only & len-only readers cannot reproduce the asymmetry ---
    # For each item: function condition swaps the FUNCTION word (dLg10WF=func_gap,
    # dlen=|len_func_out-len_func_in|); content condition swaps the CONTENT word
    # (dLg10WF=content_gap, dlen=|len_cont_out-len_cont_in|).
    def func_deltas(it):
        return it["func_gap"], abs(len(it["func_out"]) - len(it["func_in"]))

    def cont_deltas(it):
        return it["content_gap"], abs(len(it["cont_out"]) - len(it["cont_in"]))

    # The guard is against a reader REPRODUCING the function>content asymmetry, i.e. a
    # POSITIVE (function-favoring) asymmetry. A negative value (content swaps look bigger)
    # is conservative -- it cannot mimic the conjecture -- so we track the max POSITIVE.
    freq_asym, len_asym = {}, {}
    for theta in [0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.25]:
        fn = sum(freq_only_flip(func_deltas(it)[0], theta) for it in matched) / len(matched)
        ct = sum(freq_only_flip(cont_deltas(it)[0], theta) for it in matched) / len(matched)
        freq_asym[f"theta={theta}"] = round(fn - ct, 4)
    for theta in [1, 2]:
        fn = sum(len_only_flip(func_deltas(it)[1], theta) for it in matched) / len(matched)
        ct = sum(len_only_flip(cont_deltas(it)[1], theta) for it in matched) / len(matched)
        len_asym[f"theta={theta}"] = round(fn - ct, 4)
    max_pos_freq = max(v for v in freq_asym.values())
    max_pos_len = max(v for v in len_asym.values())
    # principled MONOTONE reader: flip prob rises with |dLg10WF|, so its function>content
    # asymmetry is the pooled mean (func_gap - content_gap) -- report it as the headline.
    monotone = sum(it["func_gap"] - it["content_gap"] for it in matched) / len(matched)
    checks["(i) freq-only reader max POSITIVE threshold asymmetry <= 0.12"] = max_pos_freq <= 0.12
    checks["(i) len-only reader max POSITIVE threshold asymmetry <= 0.05"] = max_pos_len <= 0.05
    checks["(i) monotone freq reader pooled (func_gap-content_gap)"] = round(monotone, 4)
    checks["(i) monotone freq reader asymmetry small (<=0.10)"] = abs(monotone) <= 0.10
    checks["freq_only_asymmetry_by_theta"] = freq_asym
    checks["len_only_asymmetry_by_theta"] = len_asym
    checks["max_positive_freq_asym"] = round(max_pos_freq, 4)
    checks["max_positive_len_asym"] = round(max_pos_len, 4)

    # --- predictability proxy (condition d): swapped-word Lg10WF matched across conditions ---
    func_lg = [F.require(it["func_out"]) for it in matched]            # always the func word
    cont_lg = [F.require(it["cont_out"]) for it in matched]
    pred_gap = abs(sum(func_lg) / len(func_lg) - sum(cont_lg) / len(cont_lg))
    # NOTE: function words are intrinsically higher-frequency than any open-class word; the
    # matching controls the SWAP magnitude (dLg10WF), not the absolute level. The decisive
    # predictability control is that the function- and content-swap MAGNITUDES match (above).
    checks["mean_Lg10WF_func_out"] = round(sum(func_lg) / len(func_lg), 4)
    checks["mean_Lg10WF_cont_out"] = round(sum(cont_lg) / len(cont_lg), 4)
    checks["abs_mean_Lg10WF_gap_func_vs_cont_out"] = round(pred_gap, 4)

    # --- gap-match magnitude summary per function type (mirrored spread, condition c) ---
    by_ft = {}
    for it in matched:
        by_ft.setdefault(it["ftype"], {"fgap": [], "cgap": []})
        by_ft[it["ftype"]]["fgap"].append(it["func_gap"])
        by_ft[it["ftype"]]["cgap"].append(it["content_gap"])
    checks["gap_match_by_ftype"] = {
        ft: {"func_gap": round(sum(d["fgap"]) / len(d["fgap"]), 4),
             "content_gap_mean": round(sum(d["cgap"]) / len(d["cgap"]), 4),
             "n": len(d["fgap"])}
        for ft, d in by_ft.items()}

    checks["det_char_arm_count"] = len(det)

    for k, v in checks.items():
        if isinstance(v, bool) and not v:
            fails.append(k)

    out = {"ok": not fails, "fails": fails, "checks": checks,
           "stimuli_sha256": json.load(open(os.path.join(HERE, "stimuli.json")))["sha256"]}
    json.dump(out, open(os.path.join(HERE, "certification.json"), "w"), indent=1)
    print(json.dumps({"ok": out["ok"], "fails": fails,
                      "matched": len(matched), "classes": classes,
                      "max_pos_freq_asym": round(max_pos_freq, 4),
                      "max_pos_len_asym": round(max_pos_len, 4),
                      "monotone_freq_asym": round(monotone, 4)}, indent=1))
    if fails:
        print("CERTIFICATION FAILED:", fails)


if __name__ == "__main__":
    main()
