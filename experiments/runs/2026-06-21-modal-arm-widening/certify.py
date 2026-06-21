#!/usr/bin/env python3
"""certify.py -- pre-run certification for the MODAL-ARM-WIDENING set (session 71).

The shortcut-reader + minimal-pair-integrity checks are BYTE-IDENTICAL in logic to run-v2's
certify.py (the anti-confound core): NO frequency-only and NO length-only reader can reproduce
the function>content flip asymmetry, premise_fn/premise_ct are single-token swaps, no function
leak into the hypothesis, predictability proxy reported, gap-match per arm. These are the
scientifically binding checks and are UNCHANGED.

The ONLY difference from run-v2 is the count gate. run-v2 enforced the CONJECTURE-confirm bar
(>=200 matched items) because it tested wiki/findings/conjectures/function-word-substitutability.md.
THIS probe does not re-test that conjecture (already `tested`); it is a focused per-arm
characterization of MODAL behavior testing essay revision trigger (a). Its statistical unit is
the per-arm flip rate, so the gate is PER-ARM POWER (>= ARM_MIN items per function arm) plus the
unchanged >=4-content-semantic-class span. This relaxation is surfaced in README.md + PREREG.md
and is for the independent pre-run critic to rule on ("no new decision owed" -- the instrument and
matching discipline are both ratified, the inventory-widening method is ratified, and the result is
internal-contrast-only with no new human claim).
"""
import json
import os

import freqlib as F

HERE = os.path.dirname(os.path.abspath(__file__))
ARM_MIN = 15   # per-arm minimum (power gate); replaces run-v2's >=200 conjecture-confirm bar.


def load():
    return json.load(open(os.path.join(HERE, "stimuli.json")))["items"]


def words(s):
    return s.replace(".", " ").replace(",", " ").split()


def single_token_diff(a, b):
    wa, wb = words(a), words(b)
    if len(wa) != len(wb):
        return False, None, None
    diffs = [(x, y) for x, y in zip(wa, wb) if x.lower() != y.lower()]
    if len(diffs) != 1:
        return False, None, None
    return True, diffs[0][0], diffs[0][1]


def freq_only_flip(delta_lg, theta):
    return 1 if delta_lg > theta else 0


def len_only_flip(delta_len, theta):
    return 1 if delta_len >= theta else 0


def main():
    items = load()
    matched = [it for it in items if it["arm"] == "matched"]
    det = [it for it in items if it["arm"] == "det_char"]
    checks = {}
    fails = []

    # --- count + semantic classes (condition e, per-arm power gate) ---
    classes = sorted({it["pos"] for it in matched})
    by_ft = {}
    for it in matched:
        by_ft[it["ftype"]] = by_ft.get(it["ftype"], 0) + 1
    checks["(e) every function arm >= ARM_MIN items"] = all(n >= ARM_MIN for n in by_ft.values())
    checks["(e) >=4 content semantic classes"] = len(classes) >= 4
    checks["matched_count"] = len(matched)
    checks["arm_min"] = ARM_MIN
    checks["counts_by_arm"] = by_ft
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
        if it["func_in"].lower() in [w.lower() for w in words(it["hyp_base"])]:
            leak_ok = False
        if it["pred_base"] == it["pred_fn"]:
            base_fn_diff_ok = False
    checks["premise_fn differs from base ONLY by the function word"] = fn_ok
    checks["premise_ct differs from base ONLY by the content word"] = ct_ok
    checks["function swap-in word never appears in the hypothesis (no leak)"] = leak_ok
    checks["every matched item predicts a function flip (pred_base != pred_fn)"] = base_fn_diff_ok

    # --- condition (i): freq-only & len-only readers cannot reproduce the asymmetry ---
    def func_deltas(it):
        return it["func_gap"], abs(len(it["func_out"]) - len(it["func_in"]))

    def cont_deltas(it):
        return it["content_gap"], abs(len(it["cont_out"]) - len(it["cont_in"]))

    EPS = 1e-9
    gaps = sorted({round(func_deltas(it)[0], 6) for it in matched}
                  | {round(cont_deltas(it)[0], 6) for it in matched})
    thetas = sorted({0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.25}
                    | {g - EPS for g in gaps} | {g for g in gaps})
    freq_asym, len_asym = {}, {}
    for theta in thetas:
        fn = sum(freq_only_flip(func_deltas(it)[0], theta) for it in matched) / len(matched)
        ct = sum(freq_only_flip(cont_deltas(it)[0], theta) for it in matched) / len(matched)
        freq_asym[f"theta={round(theta, 6)}"] = round(fn - ct, 4)
    for theta in [1, 2]:
        fn = sum(len_only_flip(func_deltas(it)[1], theta) for it in matched) / len(matched)
        ct = sum(len_only_flip(cont_deltas(it)[1], theta) for it in matched) / len(matched)
        len_asym[f"theta={theta}"] = round(fn - ct, 4)
    max_pos_freq = max(v for v in freq_asym.values())
    max_pos_len = max(v for v in len_asym.values())
    monotone = sum(it["func_gap"] - it["content_gap"] for it in matched) / len(matched)
    checks["(i) freq-only reader max POSITIVE threshold asymmetry <= 0.12"] = max_pos_freq <= 0.12
    checks["(i) len-only reader max POSITIVE threshold asymmetry <= 0.05"] = max_pos_len <= 0.05
    checks["(i) monotone freq reader pooled (func_gap-content_gap)"] = round(monotone, 4)
    checks["(i) monotone freq reader asymmetry small (<=0.10)"] = abs(monotone) <= 0.10
    checks["freq_only_asymmetry_by_theta"] = freq_asym
    checks["len_only_asymmetry_by_theta"] = len_asym
    checks["max_positive_freq_asym"] = round(max_pos_freq, 4)
    checks["max_positive_len_asym"] = round(max_pos_len, 4)

    # --- predictability proxy (condition d) ---
    func_lg = [F.require(it["func_out"]) for it in matched]
    cont_lg = [F.require(it["cont_out"]) for it in matched]
    pred_gap = abs(sum(func_lg) / len(func_lg) - sum(cont_lg) / len(cont_lg))
    checks["mean_Lg10WF_func_out"] = round(sum(func_lg) / len(func_lg), 4)
    checks["mean_Lg10WF_cont_out"] = round(sum(cont_lg) / len(cont_lg), 4)
    checks["abs_mean_Lg10WF_gap_func_vs_cont_out"] = round(pred_gap, 4)

    # --- gap-match magnitude summary per function type (mirrored spread, condition c) ---
    by_ft_gap = {}
    for it in matched:
        by_ft_gap.setdefault(it["ftype"], {"fgap": [], "cgap": []})
        by_ft_gap[it["ftype"]]["fgap"].append(it["func_gap"])
        by_ft_gap[it["ftype"]]["cgap"].append(it["content_gap"])
    checks["gap_match_by_ftype"] = {
        ft: {"func_gap": round(sum(d["fgap"]) / len(d["fgap"]), 4),
             "content_gap_mean": round(sum(d["cgap"]) / len(d["cgap"]), 4),
             "n": len(d["fgap"])}
        for ft, d in by_ft_gap.items()}

    checks["det_char_arm_count"] = len(det)

    for k, v in checks.items():
        if isinstance(v, bool) and not v:
            fails.append(k)

    out = {"ok": not fails, "fails": fails, "checks": checks,
           "stimuli_sha256": json.load(open(os.path.join(HERE, "stimuli.json")))["sha256"]}
    json.dump(out, open(os.path.join(HERE, "certification.json"), "w"), indent=1)
    print(json.dumps({"ok": out["ok"], "fails": fails,
                      "matched": len(matched), "by_arm": by_ft, "classes": classes,
                      "max_pos_freq_asym": round(max_pos_freq, 4),
                      "max_pos_len_asym": round(max_pos_len, 4),
                      "monotone_freq_asym": round(monotone, 4)}, indent=1))
    if fails:
        print("CERTIFICATION FAILED:", fails)


if __name__ == "__main__":
    main()
