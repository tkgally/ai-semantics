#!/usr/bin/env python3
"""Lexical bridging-context probe v1 analysis (run session 2026-06-22).

Applies the FROZEN reading rule (instrument.json -> reading_rule_frozen) to the raw
outputs probe.py collected. No threshold is tuned after the run: every contrast is the
ordinal one named in the frozen rule, with per-lemma-clustered bootstrap CIs.

Per model (panel.A claude / panel.B gpt / panel.C gemini), per class
(clear-same / bridging / clear-different):

  POSITION axis (B/b_rel, alone):   bridging mean relatedness strictly BETWEEN the
                                    clear-different mean and the clear-same mean.
                                    Absolute descriptor: bridging mean within [40,60].
  CONFIDENCE axis (B/b_conf):       bridging mean confidence LOWER than BOTH clear classes.
  DECLINE axis (C/c_third %UNCLEAR):bridging decline rate ELEVATED vs BOTH clear classes.
  -> confidence/dispersion axis is certified by BOTH B (confidence) and C (decline).
  prediction4_supported iff position holds (B) AND confidence/dispersion holds on BOTH.
  mixed_weak: B-C disagree on the confidence/dispersion axis (both readings shown).
  clean_null: bridging at clear-item confidence AND clear-item decline rate.

  CLEAR-CLASS PRECONDITION (gate): clear classes must show high confidence (high mean
  b_conf, saturated b_rel at the poles) AND low decline (%UNCLEAR). If unmet even with
  the WiC pole supplement -> NO-GO -> the result collapses to internal-contrast-only.

  A (a_forced) dispersion is CHARACTERIZING-ONLY: reported, never enters the verdict.
  Q3 (topic) control: on bridging items, the sense signal's relation to the model's own
  topic-similarity rating, to show within-item uncertainty tracks SENSE not mere context.

Bootstrap: cluster by LEMMA (resample lemmas with replacement within each class), 10000
reps, seed 20260622, 95% percentile CIs on the class-mean gaps. Direction-of-effect only;
small lemma-clustered N -> wide CIs, no coverage claim.

Run: python3 analyze.py    (reads raw/, writes analysis.json, prints the verdict table)
"""
import json
import math
import os
import random
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "analysis.json")
SLOTS = ["A", "B", "C"]
MODEL_OF = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
CLASSES = ["clear-same", "bridging", "clear-different"]
BAND = [40, 60]
N_BOOT = 10000
SEED = 20260622
CONF_HIGH = 70.0     # precondition: clear-class mean b_conf must clear this
DECLINE_LOW = 0.20   # precondition: clear-class %UNCLEAR must be at/under this


def load(framing, slot):
    p = os.path.join(RAW, f"{framing}_{slot}.json")
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def lemma_root(lemma):
    return lemma.split("_")[0]


def by_class(recs, key):
    """{class: [(lemma_root, value), ...]} for records whose key value is not None."""
    out = defaultdict(list)
    for r in recs:
        v = r.get(key)
        if v is None:
            continue
        out[r["bridging_class"]].append((lemma_root(r["lemma"]), v))
    return out


def cluster_means(pairs, rng=None):
    """Mean over (lemma, value) pairs; if rng given, resample LEMMAS with replacement."""
    if not pairs:
        return None
    if rng is None:
        return sum(v for _, v in pairs) / len(pairs)
    by_lemma = defaultdict(list)
    for lem, v in pairs:
        by_lemma[lem].append(v)
    lemmas = list(by_lemma)
    picks = [lemmas[rng.randrange(len(lemmas))] for _ in range(len(lemmas))]
    vals = [v for lem in picks for v in by_lemma[lem]]
    return sum(vals) / len(vals) if vals else None


def ci_of_stat(class_pairs, stat_fn, rng):
    """95% percentile CI of a scalar stat over cluster-bootstrap resamples."""
    samples = []
    for _ in range(N_BOOT):
        boot = {c: None for c in class_pairs}
        for c, pairs in class_pairs.items():
            boot[c] = cluster_means(pairs, rng)
        s = stat_fn(boot)
        if s is not None:
            samples.append(s)
    if not samples:
        return None
    samples.sort()
    lo = samples[int(0.025 * len(samples))]
    hi = samples[min(len(samples) - 1, int(0.975 * len(samples)))]
    return [round(lo, 4), round(hi, 4)]


def gap_ci(class_pairs, c_hi, c_lo, rng):
    """CI of (mean[c_hi] - mean[c_lo])."""
    def stat(m):
        if m.get(c_hi) is None or m.get(c_lo) is None:
            return None
        return m[c_hi] - m[c_lo]
    return ci_of_stat(class_pairs, stat, rng)


def point_means(class_pairs):
    return {c: (round(cluster_means(p), 3) if p else None) for c, p in class_pairs.items()}


def analyze_slot(slot, scope_filter, rng):
    """scope_filter(rec) -> bool selects which items count (e.g. DWUG-only vs +WiC)."""
    b_rel = [r for r in load("b_rel", slot) if scope_filter(r)]
    b_conf = [r for r in load("b_conf", slot) if scope_filter(r)]
    c_third = [r for r in load("c_third", slot) if scope_filter(r)]
    topic = [r for r in load("topic", slot) if scope_filter(r)]
    a_forced = [r for r in load("a_forced", slot) if scope_filter(r)]

    # ---- POSITION (b_rel) ----
    rel_pairs = by_class(b_rel, "pred")
    rel_means = point_means(rel_pairs)
    # bridging strictly between: (clear-same - bridging) > 0 AND (bridging - clear-different) > 0
    pos_hi_gap = gap_ci(rel_pairs, "clear-same", "bridging", rng)      # >0 expected
    pos_lo_gap = gap_ci(rel_pairs, "bridging", "clear-different", rng)  # >0 expected
    pos_between = (rel_means["clear-same"] is not None and rel_means["bridging"] is not None
                   and rel_means["clear-different"] is not None
                   and rel_means["clear-same"] > rel_means["bridging"] > rel_means["clear-different"])
    pos_ci_strict = (pos_hi_gap and pos_lo_gap and pos_hi_gap[0] > 0 and pos_lo_gap[0] > 0)
    brid_in_band = (rel_means["bridging"] is not None
                    and BAND[0] <= rel_means["bridging"] <= BAND[1])

    # ---- CONFIDENCE (b_conf pred2) ----
    conf_pairs = by_class(b_conf, "pred2")
    conf_means = point_means(conf_pairs)
    conf_gap_cs = gap_ci(conf_pairs, "clear-same", "bridging", rng)        # >0 expected
    conf_gap_cd = gap_ci(conf_pairs, "clear-different", "bridging", rng)   # >0 expected
    conf_lower = (conf_means["bridging"] is not None
                  and conf_means["clear-same"] is not None
                  and conf_means["clear-different"] is not None
                  and conf_means["bridging"] < conf_means["clear-same"]
                  and conf_means["bridging"] < conf_means["clear-different"])
    conf_ci_strict = (conf_gap_cs and conf_gap_cd and conf_gap_cs[0] > 0 and conf_gap_cd[0] > 0)

    # ---- DECLINE (c_third %UNCLEAR) ----
    dec_pairs = defaultdict(list)
    for r in c_third:
        if r.get("pred") is None:
            continue
        dec_pairs[r["bridging_class"]].append((lemma_root(r["lemma"]),
                                               1.0 if r["pred"] == "UNCLEAR" else 0.0))
    dec_means = point_means(dec_pairs)
    dec_gap_cs = gap_ci(dec_pairs, "bridging", "clear-same", rng)         # >0 expected
    dec_gap_cd = gap_ci(dec_pairs, "bridging", "clear-different", rng)    # >0 expected
    dec_elevated = (dec_means["bridging"] is not None
                    and dec_means["clear-same"] is not None
                    and dec_means["clear-different"] is not None
                    and dec_means["bridging"] > dec_means["clear-same"]
                    and dec_means["bridging"] > dec_means["clear-different"])
    dec_ci_strict = (dec_gap_cs and dec_gap_cd and dec_gap_cs[0] > 0 and dec_gap_cd[0] > 0)

    # ---- A dispersion (characterizing-only) ----
    disp_pairs = defaultdict(list)
    for r in a_forced:
        picks = [p for p in r["picks"] if p in ("SAME", "DIFFERENT")]
        if not picks:
            continue
        p_same = picks.count("SAME") / len(picks)
        # Shannon entropy (bits) of the binary pick distribution
        ent = 0.0
        for p in (p_same, 1 - p_same):
            if p > 0:
                ent -= p * math.log2(p)
        disp_pairs[r["bridging_class"]].append((lemma_root(r["lemma"]), ent))
    disp_means = point_means(disp_pairs)

    # ---- Q3 topic control (bridging items): relation of topic rating to sense signal ----
    topic_by_item = {r["item_id"]: r["pred"] for r in topic if r.get("pred") is not None}
    rel_by_item = {r["item_id"]: r["pred"] for r in b_rel if r.get("pred") is not None}
    brid_ids = [r["item_id"] for r in b_rel if r["bridging_class"] == "bridging"]
    xy = [(topic_by_item[i], rel_by_item[i]) for i in brid_ids
          if i in topic_by_item and i in rel_by_item]
    q3_corr = pearson([x for x, _ in xy], [y for _, y in xy]) if len(xy) >= 3 else None

    # ---- precondition ----
    pre_conf_ok = (conf_means["clear-same"] is not None and conf_means["clear-different"] is not None
                   and conf_means["clear-same"] >= CONF_HIGH
                   and conf_means["clear-different"] >= CONF_HIGH)
    pre_dec_ok = (dec_means["clear-same"] is not None and dec_means["clear-different"] is not None
                  and dec_means["clear-same"] <= DECLINE_LOW
                  and dec_means["clear-different"] <= DECLINE_LOW)
    # saturated b_rel poles: clear-same high, clear-different low
    pre_rel_ok = (rel_means["clear-same"] is not None and rel_means["clear-different"] is not None
                  and rel_means["clear-same"] >= 70.0 and rel_means["clear-different"] <= 40.0)
    precondition_met = pre_conf_ok and pre_dec_ok and pre_rel_ok

    # ---- parse success ----
    def psucc(recs, key):
        n = len(recs)
        ok = sum(1 for r in recs if r.get(key) is not None)
        return [ok, n]

    return {
        "model": MODEL_OF[slot],
        "n_items": {c: sum(1 for r in b_rel if r["bridging_class"] == c) for c in CLASSES},
        "parse_success": {
            "b_rel": psucc(b_rel, "pred"), "b_conf_conf": psucc(b_conf, "pred2"),
            "c_third": psucc(c_third, "pred"), "topic": psucc(topic, "pred"),
        },
        "position": {
            "b_rel_means": rel_means, "brid_in_band_40_60": brid_in_band,
            "gap_clearsame_minus_bridging_ci": pos_hi_gap,
            "gap_bridging_minus_cleardiff_ci": pos_lo_gap,
            "between_pointwise": pos_between, "between_ci_strict": pos_ci_strict,
        },
        "confidence": {
            "b_conf_means": conf_means,
            "gap_clearsame_minus_bridging_ci": conf_gap_cs,
            "gap_cleardiff_minus_bridging_ci": conf_gap_cd,
            "lower_pointwise": conf_lower, "lower_ci_strict": conf_ci_strict,
        },
        "decline": {
            "pct_unclear": dec_means,
            "gap_bridging_minus_clearsame_ci": dec_gap_cs,
            "gap_bridging_minus_cleardiff_ci": dec_gap_cd,
            "elevated_pointwise": dec_elevated, "elevated_ci_strict": dec_ci_strict,
        },
        "dispersion_A_characterizing_only": {"entropy_bits_means": disp_means},
        "q3_topic_control": {"n_bridging_pairs": len(xy),
                             "pearson_topic_vs_brel_on_bridging": q3_corr},
        "precondition": {
            "conf_ok": pre_conf_ok, "decline_ok": pre_dec_ok, "rel_poles_ok": pre_rel_ok,
            "met": precondition_met,
            "thresholds": {"conf_high": CONF_HIGH, "decline_low": DECLINE_LOW,
                           "rel_clearsame_min": 70.0, "rel_cleardiff_max": 40.0},
        },
    }


def pearson(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    if sxx == 0 or syy == 0:
        return None
    return round(sxy / math.sqrt(sxx * syy), 4)


def verdict(a):
    """Apply the frozen verdict map to one slot's analysis (under the precondition)."""
    if not a["precondition"]["met"]:
        return "PRECONDITION-UNMET -> internal-contrast-only (collapse)"
    pos = a["position"]["between_ci_strict"]
    conf = a["confidence"]["lower_ci_strict"]
    dec = a["decline"]["elevated_ci_strict"]
    if pos and conf and dec:
        return "PREDICTION-4 SUPPORTED (position + confidence(B) + decline(C))"
    # confidence/dispersion axis needs BOTH B and C
    if conf != dec:
        return ("MIXED/WEAK — B(confidence) and C(decline) disagree on the "
                f"confidence/dispersion axis (B_lower={conf}, C_elevated={dec}; "
                f"position={pos}) — both readings shown, NOT the null")
    if pos and not conf and not dec:
        return ("PARTIAL — position graded (B) but confidence/decline at clear-item "
                "level: graded SCALE with ungraded COMMITMENT (within-item discreteness)")
    if not pos and not conf and not dec:
        return ("CLEAN NULL — bridging handled at clear-item position, confidence, and "
                "decline (graded scale + ungraded commitment)")
    return (f"PARTIAL/OTHER (position={pos}, confidence_lower={conf}, decline_elevated={dec})")


def main():
    rng = random.Random(SEED)
    scopes = {
        "dwug_plus_wic": lambda r: True,
        "dwug_only": lambda r: r.get("source") == "dwug",
    }
    out = {"_meta": {"n_boot": N_BOOT, "seed": SEED, "band": BAND,
                     "precondition_thresholds": {"conf_high": CONF_HIGH,
                                                 "decline_low": DECLINE_LOW}},
           "scopes": {}}
    for scope_name, filt in scopes.items():
        out["scopes"][scope_name] = {}
        for slot in SLOTS:
            a = analyze_slot(slot, filt, rng)
            a["verdict"] = verdict(a)
            out["scopes"][scope_name][slot] = a

    json.dump(out, open(OUT, "w"), indent=1)

    for scope_name in scopes:
        print(f"\n{'='*78}\nSCOPE: {scope_name}\n{'='*78}")
        for slot in SLOTS:
            a = out["scopes"][scope_name][slot]
            print(f"\n--- panel.{slot} {a['model']}  (n {a['n_items']}) ---")
            print(f"  b_rel means     : {a['position']['b_rel_means']}  "
                  f"brid_in_[40,60]={a['position']['brid_in_band_40_60']}")
            print(f"    position between(pt)={a['position']['between_pointwise']} "
                  f"ci_strict={a['position']['between_ci_strict']} "
                  f"(cs-br {a['position']['gap_clearsame_minus_bridging_ci']}, "
                  f"br-cd {a['position']['gap_bridging_minus_cleardiff_ci']})")
            print(f"  b_conf means    : {a['confidence']['b_conf_means']}  "
                  f"lower(pt)={a['confidence']['lower_pointwise']} "
                  f"ci_strict={a['confidence']['lower_ci_strict']}")
            print(f"  %UNCLEAR (C)    : {a['decline']['pct_unclear']}  "
                  f"elevated(pt)={a['decline']['elevated_pointwise']} "
                  f"ci_strict={a['decline']['elevated_ci_strict']}")
            print(f"  A entropy(bits) : {a['dispersion_A_characterizing_only']['entropy_bits_means']} (char-only)")
            print(f"  Q3 topic~brel(brid): r={a['q3_topic_control']['pearson_topic_vs_brel_on_bridging']} "
                  f"(n={a['q3_topic_control']['n_bridging_pairs']})")
            print(f"  precondition    : {a['precondition']['met']} "
                  f"(conf_ok={a['precondition']['conf_ok']}, "
                  f"decline_ok={a['precondition']['decline_ok']}, "
                  f"rel_poles_ok={a['precondition']['rel_poles_ok']})")
            print(f"  VERDICT         : {a['verdict']}")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
