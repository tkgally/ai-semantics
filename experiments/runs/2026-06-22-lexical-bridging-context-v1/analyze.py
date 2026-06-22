#!/usr/bin/env python3
"""Lexical bridging-context probe v1 — analysis (separate step; reads probe.py raw/).

Applies the FROZEN per-axis reading rule (instrument.json `reading_rule_frozen`) to the
raw outputs collected by ../../designs/lexical-bridging-context-v1/probe.py. No threshold
is tuned here after the run: every contrast is ordinal with per-lemma-clustered bootstrap
uncertainty (operationalization gate modification 2/3). A (a_forced) is characterizing-only
and never enters the verdict.

Reading rule (verbatim from instrument.json):
  - POSITION (B/b_rel alone): bridging mean relatedness STRICTLY between clear-different
    mean and clear-same mean (per-lemma-clustered bootstrap CI on the two gaps).
  - CONFIDENCE/DISPERSION (B AND C): (B) bridging mean b_conf LOWER than BOTH clear
    classes; AND (C) bridging decline rate (%UNCLEAR) ELEVATED vs BOTH clear classes.
  - prediction4_supported iff position holds AND confidence/dispersion holds on BOTH B and C.
  - B-C disagreement on the confidence axis => MIXED/WEAK (both readings shown), not null.
  - clean null: bridging at clear-item confidence AND clear-item decline rate.
  - CLEAR-CLASS PRECONDITION: interpretable only if the clear classes show high confidence
    (B) and low decline (C); else NO-GO -> collapse to internal-contrast-only.

Run: python3 analyze.py   (reads ../../designs/lexical-bridging-context-v1/raw/)
"""
import json
import math
import os
import random
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.abspath(os.path.join(
    HERE, "..", "..", "designs", "lexical-bridging-context-v1", "raw"))
SLOTS = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
CLASSES = ["clear-different", "bridging", "clear-same"]
BAND = [40, 60]
SEED = 20260622
N_BOOT = 5000


def load(framing, slot):
    with open(os.path.join(RAW, f"{framing}_{slot}.json"), encoding="utf-8") as f:
        return json.load(f)


def by_class(recs, valuefn):
    """Map class -> list of (lemma, value) over recs where valuefn is not None."""
    out = defaultdict(list)
    for r in recs:
        v = valuefn(r)
        if v is not None:
            out[r["bridging_class"]].append((r["lemma"], v))
    return out


def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def cluster_boot_ci(pairs, stat=mean, n=N_BOOT, seed=SEED):
    """Per-lemma-clustered bootstrap CI of `stat` over values. pairs = [(lemma, value)]."""
    if not pairs:
        return (float("nan"), float("nan"), float("nan"))
    rng = random.Random(seed)
    bylem = defaultdict(list)
    for lem, v in pairs:
        bylem[lem].append(v)
    lemmas = list(bylem)
    point = stat([v for _, v in pairs])
    draws = []
    for _ in range(n):
        samp = []
        for _ in range(len(lemmas)):
            samp.extend(bylem[rng.choice(lemmas)])
        draws.append(stat(samp))
    draws.sort()
    lo = draws[int(0.025 * n)]
    hi = draws[int(0.975 * n)]
    return (point, lo, hi)


def diff_boot_ci(pa, pb, stat=mean, n=N_BOOT, seed=SEED):
    """CI of stat(a) - stat(b), clustering each group by its own lemmas."""
    rng = random.Random(seed)
    a_by, b_by = defaultdict(list), defaultdict(list)
    for lem, v in pa:
        a_by[lem].append(v)
    for lem, v in pb:
        b_by[lem].append(v)
    la, lb = list(a_by), list(b_by)
    point = stat([v for _, v in pa]) - stat([v for _, v in pb])
    draws = []
    for _ in range(n):
        sa = [v for _ in la for v in a_by[rng.choice(la)]]
        sb = [v for _ in lb for v in b_by[rng.choice(lb)]]
        draws.append(stat(sa) - stat(sb))
    draws.sort()
    return (point, draws[int(0.025 * n)], draws[int(0.975 * n)])


def entropy2(picks):
    """Shannon entropy (bits) of binary SAME/DIFFERENT picks; None if no valid picks."""
    vals = [p for p in picks if p in ("SAME", "DIFFERENT")]
    if not vals:
        return None
    p = vals.count("SAME") / len(vals)
    if p in (0.0, 1.0):
        return 0.0
    return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))


def flip(picks):
    vals = [p for p in picks if p in ("SAME", "DIFFERENT")]
    if not vals:
        return None
    return min(vals.count("SAME"), vals.count("DIFFERENT")) / len(vals)


def analyze_slot(slot):
    b_rel = load("b_rel", slot)
    b_conf = load("b_conf", slot)
    c_third = load("c_third", slot)
    topic = load("topic", slot)
    a_forced = load("a_forced", slot)

    # --- per-class collections ---
    rel = by_class(b_rel, lambda r: r.get("pred"))
    conf = by_class(b_conf, lambda r: r.get("pred2") if r.get("pred") in ("SAME", "DIFFERENT") else None)
    # decline rate: per rec 1 if UNCLEAR else 0 (over parsed recs)
    decl = by_class(c_third, lambda r: (1.0 if r.get("pred") == "UNCLEAR" else 0.0) if r.get("pred") in ("SAME", "DIFFERENT", "UNCLEAR") else None)
    top = by_class(topic, lambda r: r.get("pred"))
    ent = by_class(a_forced, lambda r: entropy2(r.get("picks", [])))

    # parse-integrity
    parse = {
        "b_rel_parsed": sum(1 for r in b_rel if r.get("pred") is not None),
        "b_rel_total": len(b_rel),
        "b_conf_call_parsed": sum(1 for r in b_conf if r.get("pred") in ("SAME", "DIFFERENT")),
        "c_third_parsed": sum(1 for r in c_third if r.get("pred") in ("SAME", "DIFFERENT", "UNCLEAR")),
        "topic_parsed": sum(1 for r in topic if r.get("pred") is not None),
        "errors": sum(1 for r in (b_rel + b_conf + c_third + topic) if r.get("error")),
    }

    def cls_stat(d, stat=mean):
        return {c: cluster_boot_ci(d.get(c, []), stat=stat) for c in CLASSES}

    res = {
        "slot": slot, "model": SLOTS[slot], "parse": parse,
        "n_by_class": {c: len(rel.get(c, [])) for c in CLASSES},
        "position_b_rel": cls_stat(rel),
        "confidence_b_conf": cls_stat(conf),
        "decline_c_third": cls_stat(decl),
        "topic_q3": cls_stat(top),
        "dispersion_entropy_a": cls_stat(ent),
    }

    # --- reading-rule contrasts (with CIs on the gaps) ---
    # POSITION: bridging strictly between the two clear poles.
    res["gap_bridging_minus_cd_rel"] = diff_boot_ci(rel.get("bridging", []), rel.get("clear-different", []))
    res["gap_cs_minus_bridging_rel"] = diff_boot_ci(rel.get("clear-same", []), rel.get("bridging", []))
    bm = res["position_b_rel"]["bridging"][0]
    res["position_holds"] = (
        res["gap_bridging_minus_cd_rel"][1] > 0 and res["gap_cs_minus_bridging_rel"][1] > 0)
    res["bridging_in_band"] = (BAND[0] <= bm <= BAND[1]) if not math.isnan(bm) else False

    # CONFIDENCE (B): bridging lower than BOTH clear classes.
    res["conf_bridging_minus_cs"] = diff_boot_ci(conf.get("bridging", []), conf.get("clear-same", []))
    res["conf_bridging_minus_cd"] = diff_boot_ci(conf.get("bridging", []), conf.get("clear-different", []))
    res["confidence_B_holds"] = (
        res["conf_bridging_minus_cs"][2] < 0 and res["conf_bridging_minus_cd"][2] < 0)

    # DECLINE (C): bridging elevated vs BOTH clear classes.
    res["decl_bridging_minus_cs"] = diff_boot_ci(decl.get("bridging", []), decl.get("clear-same", []))
    res["decl_bridging_minus_cd"] = diff_boot_ci(decl.get("bridging", []), decl.get("clear-different", []))
    res["decline_C_holds"] = (
        res["decl_bridging_minus_cs"][1] > 0 and res["decl_bridging_minus_cd"][1] > 0)

    # --- clear-class precondition (report; DWUG poles vs WiC poles separated) ---
    def pole_conf_decl(src_filter):
        cf = defaultdict(list)
        dc = defaultdict(list)
        for r in b_conf:
            if src_filter(r) and r.get("pred") in ("SAME", "DIFFERENT") and r["bridging_class"] in ("clear-same", "clear-different"):
                cf[r["bridging_class"]].append(r.get("pred2"))
        for r in c_third:
            if src_filter(r) and r.get("pred") in ("SAME", "DIFFERENT", "UNCLEAR") and r["bridging_class"] in ("clear-same", "clear-different"):
                dc[r["bridging_class"]].append(1.0 if r["pred"] == "UNCLEAR" else 0.0)
        return ({c: round(mean(cf[c]), 1) if cf[c] else None for c in ("clear-same", "clear-different")},
                {c: round(mean(dc[c]), 3) if dc[c] else None for c in ("clear-same", "clear-different")})
    res["precond_all"] = pole_conf_decl(lambda r: True)
    res["precond_dwug"] = pole_conf_decl(lambda r: r.get("source") == "dwug")
    res["precond_wic"] = pole_conf_decl(lambda r: r.get("source") == "wic")

    # --- per-model verdict per the frozen rule ---
    conf_disp = res["confidence_B_holds"] and res["decline_C_holds"]
    if res["position_holds"] and conf_disp:
        verdict = "PREDICTION-4 SUPPORTED (position + confidence/dispersion on both B and C)"
    elif res["confidence_B_holds"] != res["decline_C_holds"]:
        verdict = "MIXED/WEAK (B-C disagree on the confidence/dispersion axis)"
    elif res["position_holds"] and not conf_disp:
        verdict = "CLEAN NULL on confidence (graded scale, ungraded commitment); position-only"
    elif (not res["position_holds"]) and conf_disp:
        verdict = "confidence/dispersion without certified position (report both)"
    else:
        verdict = "CLEAN NULL (bridging handled at clear-item confidence and decline)"
    res["verdict"] = verdict
    return res


def fmt(t):
    return f"{t[0]:.1f} [{t[1]:.1f}, {t[2]:.1f}]"


def main():
    out = {"slots": {}, "classes": CLASSES, "band": BAND}
    for slot in ("A", "B", "C"):
        try:
            out["slots"][slot] = analyze_slot(slot)
        except FileNotFoundError as e:
            out["slots"][slot] = {"error": f"raw missing: {e}"}
    with open(os.path.join(HERE, "analysis.json"), "w") as f:
        json.dump(out, f, indent=1)

    for slot in ("A", "B", "C"):
        r = out["slots"][slot]
        if "error" in r:
            print(f"\n=== panel.{slot}: {r['error']}")
            continue
        print(f"\n=== panel.{slot} {r['model']} ===")
        print(f"  n_by_class: {r['n_by_class']}  parse: {r['parse']}")
        print(f"  POSITION b_rel  cd={fmt(r['position_b_rel']['clear-different'])} "
              f"br={fmt(r['position_b_rel']['bridging'])} "
              f"cs={fmt(r['position_b_rel']['clear-same'])}")
        print(f"     gaps: br-cd={fmt(r['gap_bridging_minus_cd_rel'])} "
              f"cs-br={fmt(r['gap_cs_minus_bridging_rel'])}  "
              f"position_holds={r['position_holds']} in_band={r['bridging_in_band']}")
        print(f"  CONF b_conf     cd={fmt(r['confidence_b_conf']['clear-different'])} "
              f"br={fmt(r['confidence_b_conf']['bridging'])} "
              f"cs={fmt(r['confidence_b_conf']['clear-same'])}  "
              f"B_holds={r['confidence_B_holds']}")
        print(f"  DECLINE %UNCL   cd={fmt(r['decline_c_third']['clear-different'])} "
              f"br={fmt(r['decline_c_third']['bridging'])} "
              f"cs={fmt(r['decline_c_third']['clear-same'])}  "
              f"C_holds={r['decline_C_holds']}")
        print(f"  TOPIC q3        cd={fmt(r['topic_q3']['clear-different'])} "
              f"br={fmt(r['topic_q3']['bridging'])} "
              f"cs={fmt(r['topic_q3']['clear-same'])}")
        print(f"  DISP entropy(A) cd={fmt(r['dispersion_entropy_a']['clear-different'])} "
              f"br={fmt(r['dispersion_entropy_a']['bridging'])} "
              f"cs={fmt(r['dispersion_entropy_a']['clear-same'])}")
        print(f"  PRECOND conf/decline  all={r['precond_all']}")
        print(f"          dwug={r['precond_dwug']}  wic={r['precond_wic']}")
        print(f"  >>> VERDICT: {r['verdict']}")


if __name__ == "__main__":
    main()
