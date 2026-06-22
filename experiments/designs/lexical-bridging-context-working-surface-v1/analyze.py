#!/usr/bin/env python3
"""Working-surface re-run analysis (session 79, 2026-06-22).

Applies the SAME frozen reading rule as v1 (experiments/designs/lexical-bridging-context-v1/
analyze.py) to the working-surface raw outputs, and adds:
  (1) a head-to-head DELTA vs v1's committed analysis.json on the commitment axes
      (bridging b_conf, bridging %UNCLEAR, bridging A-entropy) — the witness-seek question, and
  (2) an UPTAKE report per model per framing (median content chars / completion tokens,
      % FINAL-tag present), because essay/output-channel-confound's uptake clause says a
      declined surface is channel-not-taken-up (inconclusive), never a survival.

Bootstrap identical to v1: cluster by LEMMA, 10000 reps, seed 20260622, 95% percentile CIs.

Run: python3 analyze.py    (reads raw/, writes analysis.json, prints verdict + delta + uptake)
"""
import json
import math
import os
import random
import statistics
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OUT = os.path.join(HERE, "analysis.json")
V1_ANALYSIS = os.path.abspath(os.path.join(
    HERE, "..", "lexical-bridging-context-v1", "analysis.json"))
SLOTS = ["A", "B", "C"]
MODEL_OF = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
CLASSES = ["clear-same", "bridging", "clear-different"]
BAND = [40, 60]
N_BOOT = 10000
SEED = 20260622
CONF_HIGH = 70.0
DECLINE_LOW = 0.20


def load(framing, slot):
    p = os.path.join(RAW, f"{framing}_{slot}.json")
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def lemma_root(lemma):
    return lemma.split("_")[0]


def by_class(recs, key):
    out = defaultdict(list)
    for r in recs:
        v = r.get(key)
        if v is None:
            continue
        out[r["bridging_class"]].append((lemma_root(r["lemma"]), v))
    return out


def cluster_means(pairs, rng=None):
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
    samples = []
    for _ in range(N_BOOT):
        boot = {c: cluster_means(p, rng) for c, p in class_pairs.items()}
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
    def stat(m):
        if m.get(c_hi) is None or m.get(c_lo) is None:
            return None
        return m[c_hi] - m[c_lo]
    return ci_of_stat(class_pairs, stat, rng)


def point_means(class_pairs):
    return {c: (round(cluster_means(p), 3) if p else None) for c, p in class_pairs.items()}


def uptake_report(recs):
    """median content chars / completion tokens, % FINAL-tag, % bare(<40 chars)."""
    chars = [r["uptake"]["content_chars"] for r in recs if r.get("uptake")]
    ctoks = [r["uptake"]["completion_tokens"] for r in recs
             if r.get("uptake") and r["uptake"]["completion_tokens"] is not None]
    rtoks = [r["uptake"]["reasoning_tokens"] for r in recs
             if r.get("uptake") and r["uptake"].get("reasoning_tokens") is not None]
    tags = [1 for r in recs if r.get("had_final_tag")]
    return {
        "n": len(recs),
        "median_content_chars": round(statistics.median(chars), 1) if chars else None,
        "median_completion_tokens": round(statistics.median(ctoks), 1) if ctoks else None,
        "median_reasoning_tokens": round(statistics.median(rtoks), 1) if rtoks else None,
        "pct_final_tag": round(100 * len(tags) / len(recs), 1) if recs else None,
        "pct_bare_lt40chars": round(100 * sum(1 for c in chars if c < 40) / len(chars), 1)
        if chars else None,
    }


def analyze_slot(slot, scope_filter, rng):
    b_rel = [r for r in load("b_rel", slot) if scope_filter(r)]
    b_conf = [r for r in load("b_conf", slot) if scope_filter(r)]
    c_third = [r for r in load("c_third", slot) if scope_filter(r)]
    topic = [r for r in load("topic", slot) if scope_filter(r)]
    a_raw = load("a_forced", slot)
    a_forced = [r for r in a_raw if scope_filter(r)] if a_raw else []

    rel_pairs = by_class(b_rel, "pred")
    rel_means = point_means(rel_pairs)
    pos_hi_gap = gap_ci(rel_pairs, "clear-same", "bridging", rng)
    pos_lo_gap = gap_ci(rel_pairs, "bridging", "clear-different", rng)
    pos_between = (None not in (rel_means["clear-same"], rel_means["bridging"], rel_means["clear-different"])
                   and rel_means["clear-same"] > rel_means["bridging"] > rel_means["clear-different"])
    pos_ci_strict = bool(pos_hi_gap and pos_lo_gap and pos_hi_gap[0] > 0 and pos_lo_gap[0] > 0)
    brid_in_band = (rel_means["bridging"] is not None and BAND[0] <= rel_means["bridging"] <= BAND[1])

    conf_pairs = by_class(b_conf, "pred2")
    conf_means = point_means(conf_pairs)
    conf_gap_cs = gap_ci(conf_pairs, "clear-same", "bridging", rng)
    conf_gap_cd = gap_ci(conf_pairs, "clear-different", "bridging", rng)
    conf_lower = (None not in (conf_means["bridging"], conf_means["clear-same"], conf_means["clear-different"])
                  and conf_means["bridging"] < conf_means["clear-same"]
                  and conf_means["bridging"] < conf_means["clear-different"])
    conf_ci_strict = bool(conf_gap_cs and conf_gap_cd and conf_gap_cs[0] > 0 and conf_gap_cd[0] > 0)

    dec_pairs = defaultdict(list)
    for r in c_third:
        if r.get("pred") is None:
            continue
        dec_pairs[r["bridging_class"]].append((lemma_root(r["lemma"]),
                                               1.0 if r["pred"] == "UNCLEAR" else 0.0))
    dec_means = point_means(dec_pairs)
    dec_gap_cs = gap_ci(dec_pairs, "bridging", "clear-same", rng)
    dec_gap_cd = gap_ci(dec_pairs, "bridging", "clear-different", rng)
    dec_elevated = (None not in (dec_means["bridging"], dec_means["clear-same"], dec_means["clear-different"])
                    and dec_means["bridging"] > dec_means["clear-same"]
                    and dec_means["bridging"] > dec_means["clear-different"])
    dec_ci_strict = bool(dec_gap_cs and dec_gap_cd and dec_gap_cs[0] > 0 and dec_gap_cd[0] > 0)

    disp_pairs = defaultdict(list)
    for r in a_forced:
        picks = [p for p in r["picks"] if p in ("SAME", "DIFFERENT")]
        if not picks:
            continue
        p_same = picks.count("SAME") / len(picks)
        ent = 0.0
        for p in (p_same, 1 - p_same):
            if p > 0:
                ent -= p * math.log2(p)
        disp_pairs[r["bridging_class"]].append((lemma_root(r["lemma"]), ent))
    disp_means = point_means(disp_pairs)

    topic_by_item = {r["item_id"]: r["pred"] for r in topic if r.get("pred") is not None}
    rel_by_item = {r["item_id"]: r["pred"] for r in b_rel if r.get("pred") is not None}
    brid_ids = [r["item_id"] for r in b_rel if r["bridging_class"] == "bridging"]
    xy = [(topic_by_item[i], rel_by_item[i]) for i in brid_ids
          if i in topic_by_item and i in rel_by_item]
    q3_corr = pearson([x for x, _ in xy], [y for _, y in xy]) if len(xy) >= 3 else None

    pre_conf_ok = (None not in (conf_means["clear-same"], conf_means["clear-different"])
                   and conf_means["clear-same"] >= CONF_HIGH and conf_means["clear-different"] >= CONF_HIGH)
    pre_dec_ok = (None not in (dec_means["clear-same"], dec_means["clear-different"])
                  and dec_means["clear-same"] <= DECLINE_LOW and dec_means["clear-different"] <= DECLINE_LOW)
    pre_rel_ok = (None not in (rel_means["clear-same"], rel_means["clear-different"])
                  and rel_means["clear-same"] >= 70.0 and rel_means["clear-different"] <= 40.0)
    precondition_met = pre_conf_ok and pre_dec_ok and pre_rel_ok

    def psucc(recs, key):
        return [sum(1 for r in recs if r.get(key) is not None), len(recs)]

    out = {
        "model": MODEL_OF[slot],
        "n_items": {c: sum(1 for r in b_rel if r["bridging_class"] == c) for c in CLASSES},
        "parse_success": {"b_rel": psucc(b_rel, "pred"), "b_conf_conf": psucc(b_conf, "pred2"),
                          "c_third": psucc(c_third, "pred"), "topic": psucc(topic, "pred")},
        "uptake": {fr: uptake_report([r for r in load(fr, slot) if scope_filter(r)])
                   for fr in ["b_rel", "b_conf", "c_third", "topic"]},
        "position": {"b_rel_means": rel_means, "brid_in_band_40_60": brid_in_band,
                     "gap_clearsame_minus_bridging_ci": pos_hi_gap,
                     "gap_bridging_minus_cleardiff_ci": pos_lo_gap,
                     "between_pointwise": pos_between, "between_ci_strict": pos_ci_strict},
        "confidence": {"b_conf_means": conf_means,
                       "gap_clearsame_minus_bridging_ci": conf_gap_cs,
                       "gap_cleardiff_minus_bridging_ci": conf_gap_cd,
                       "lower_pointwise": conf_lower, "lower_ci_strict": conf_ci_strict},
        "decline": {"pct_unclear": dec_means,
                    "gap_bridging_minus_clearsame_ci": dec_gap_cs,
                    "gap_bridging_minus_cleardiff_ci": dec_gap_cd,
                    "elevated_pointwise": dec_elevated, "elevated_ci_strict": dec_ci_strict},
        "dispersion_A_characterizing_only": {"entropy_bits_means": disp_means,
                                             "present": bool(a_forced)},
        "q3_topic_control": {"n_bridging_pairs": len(xy),
                             "pearson_topic_vs_brel_on_bridging": q3_corr},
        "precondition": {"conf_ok": pre_conf_ok, "decline_ok": pre_dec_ok,
                         "rel_poles_ok": pre_rel_ok, "met": precondition_met},
    }
    return out


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
    if not a["precondition"]["met"]:
        return "PRECONDITION-UNMET -> internal-contrast-only (collapse)"
    pos = a["position"]["between_ci_strict"]
    conf = a["confidence"]["lower_ci_strict"]
    dec = a["decline"]["elevated_ci_strict"]
    if pos and conf and dec:
        return "PREDICTION-4 SUPPORTED (position + confidence(B) + decline(C))"
    if conf != dec:
        return (f"MIXED/WEAK — B(confidence) and C(decline) disagree (B_lower={conf}, "
                f"C_elevated={dec}; position={pos}) — both readings shown, NOT the null")
    if pos and not conf and not dec:
        return ("PARTIAL — position graded (B) but confidence/decline at clear-item level: "
                "graded SCALE with ungraded COMMITMENT (within-item discreteness)")
    if not pos and not conf and not dec:
        return ("CLEAN NULL — bridging at clear-item position, confidence, and decline "
                "(graded scale + ungraded commitment)")
    return f"PARTIAL/OTHER (position={pos}, confidence_lower={conf}, decline_elevated={dec})"


def delta_vs_v1(ws_scopes):
    """Bridging commitment metrics: working-surface minus v1 (dwug_plus_wic scope)."""
    if not os.path.exists(V1_ANALYSIS):
        return {"error": f"v1 analysis missing at {V1_ANALYSIS}"}
    v1 = json.load(open(V1_ANALYSIS, encoding="utf-8"))
    out = {}
    for slot in SLOTS:
        v1a = v1["scopes"]["dwug_plus_wic"][slot]
        wsa = ws_scopes["dwug_plus_wic"][slot]
        def g(a, *path):
            x = a
            for p in path:
                x = x.get(p) if isinstance(x, dict) else None
                if x is None:
                    return None
            return x
        v1_conf = g(v1a, "confidence", "b_conf_means", "bridging")
        ws_conf = g(wsa, "confidence", "b_conf_means", "bridging")
        v1_dec = g(v1a, "decline", "pct_unclear", "bridging")
        ws_dec = g(wsa, "decline", "pct_unclear", "bridging")
        out[slot] = {
            "model": MODEL_OF[slot],
            "bridging_b_conf": {"v1": v1_conf, "ws": ws_conf,
                                "delta": round(ws_conf - v1_conf, 3)
                                if None not in (v1_conf, ws_conf) else None},
            "bridging_pct_unclear": {"v1": v1_dec, "ws": ws_dec,
                                     "delta": round(ws_dec - v1_dec, 4)
                                     if None not in (v1_dec, ws_dec) else None},
            "v1_verdict": v1a.get("verdict"), "ws_verdict": wsa.get("verdict"),
        }
    return out


def main():
    rng = random.Random(SEED)
    scopes = {"dwug_plus_wic": lambda r: True,
              "dwug_only": lambda r: r.get("source") == "dwug"}
    out = {"_meta": {"n_boot": N_BOOT, "seed": SEED, "band": BAND, "variant": "working-surface",
                     "compares_to": "experiments/designs/lexical-bridging-context-v1/analysis.json"},
           "scopes": {}}
    for scope_name, filt in scopes.items():
        out["scopes"][scope_name] = {}
        for slot in SLOTS:
            a = analyze_slot(slot, filt, rng)
            a["verdict"] = verdict(a)
            out["scopes"][scope_name][slot] = a
    out["delta_vs_v1"] = delta_vs_v1(out["scopes"])
    json.dump(out, open(OUT, "w"), indent=1)

    for scope_name in scopes:
        print(f"\n{'='*78}\nSCOPE: {scope_name}\n{'='*78}")
        for slot in SLOTS:
            a = out["scopes"][scope_name][slot]
            print(f"\n--- panel.{slot} {a['model']}  (n {a['n_items']}) ---")
            print(f"  b_rel means : {a['position']['b_rel_means']}  in[40,60]={a['position']['brid_in_band_40_60']} "
                  f"between_ci={a['position']['between_ci_strict']}")
            print(f"  b_conf means: {a['confidence']['b_conf_means']}  lower_ci={a['confidence']['lower_ci_strict']}")
            print(f"  %UNCLEAR(C) : {a['decline']['pct_unclear']}  elevated_ci={a['decline']['elevated_ci_strict']}")
            print(f"  A entropy   : {a['dispersion_A_characterizing_only']['entropy_bits_means']} "
                  f"(present={a['dispersion_A_characterizing_only']['present']})")
            print(f"  Q3 r        : {a['q3_topic_control']['pearson_topic_vs_brel_on_bridging']} "
                  f"(n={a['q3_topic_control']['n_bridging_pairs']})")
            print(f"  precond     : {a['precondition']['met']}")
            if scope_name == "dwug_plus_wic":
                up = a["uptake"]["b_conf"]
                print(f"  uptake(b_conf): median_chars={up['median_content_chars']} "
                      f"median_ctoks={up['median_completion_tokens']} "
                      f"final_tag%={up['pct_final_tag']} bare%={up['pct_bare_lt40chars']}")
            print(f"  VERDICT     : {a['verdict']}")

    print(f"\n{'='*78}\nDELTA vs v1 (bridging commitment; dwug_plus_wic)\n{'='*78}")
    for slot in SLOTS:
        d = out["delta_vs_v1"][slot]
        print(f"  {d['model']}: b_conf {d['bridging_b_conf']}  %UNCLEAR {d['bridging_pct_unclear']}")
        print(f"     v1: {d['v1_verdict']}\n     ws: {d['ws_verdict']}")
    print(f"\nwrote {OUT}")


if __name__ == "__main__":
    main()
