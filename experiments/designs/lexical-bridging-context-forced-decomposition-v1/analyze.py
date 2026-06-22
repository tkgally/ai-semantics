#!/usr/bin/env python3
"""Analyze the gpt-only forced-decomposition follow-up against the FROZEN v1 reading rule.

Reports, for gpt-5.4-mini:
  1. UPTAKE manipulation check (the crux): forced vs OFFERED (recomputed from the committed
     working-surface raw) -- median completion tokens, % bare, % worked (>=40 pre-FINAL chars
     AND >=2 numbered steps), median reasoning tokens (expect 0).
  2. Clear-class precondition (dwug+wic): poles separated on b_rel, clear-class confidence high,
     clear-class decline low (the internal benign-scaffold check).
  3. The three axes (dwug+wic; n clear-same 29 / bridging 24 / clear-different 35) with
     per-lemma-clustered bootstrap 95% CIs (10000 reps, seed 20260622, as v1/ws):
       position (b_rel), confidence (b_conf pred2), decline (c_third %UNCLEAR).
  4. Head-to-head deltas vs gpt OFFERED + the per-axis verdict (the frozen rule, per model).

No API. Run AFTER probe.py and BEFORE sanitize_raw.py (uses only parsed fields, no corpus text).
"""
import json
import os
import random
import statistics as st

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
OFFERED_RAW = os.path.abspath(os.path.join(
    HERE, "..", "lexical-bridging-context-working-surface-v1", "raw"))
SLOT = "B"  # gpt-5.4-mini
REPS, SEED = 10000, 20260622
MIDBAND = (40, 60)
CLASSES = ["clear-different", "bridging", "clear-same"]


def load(raw_dir, framing, slot):
    p = os.path.join(raw_dir, f"{framing}_{slot}.json")
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else None


def by_class_pairs(recs, value_key):
    """{class: [(lemma, value), ...]} over records with a non-None value."""
    out = {c: [] for c in CLASSES}
    for r in recs:
        v = r.get(value_key)
        if v is None or r["bridging_class"] not in out:
            continue
        out[r["bridging_class"]].append((r["lemma"], float(v)))
    return out


def boot_ci(pairs, reps=REPS, seed=SEED):
    """Lemma-clustered bootstrap mean + 95% CI. Resample lemmas (clusters) with replacement."""
    if not pairs:
        return None, None, None, 0
    rng = random.Random(seed)
    by_lemma = {}
    for lemma, v in pairs:
        by_lemma.setdefault(lemma, []).append(v)
    lemmas = list(by_lemma)
    vals = [v for _, v in pairs]
    point = st.mean(vals)
    means = []
    for _ in range(reps):
        drawn = [rng.choice(lemmas) for _ in lemmas]
        pool = [v for lm in drawn for v in by_lemma[lm]]
        if pool:
            means.append(st.mean(pool))
    means.sort()
    lo = means[int(0.025 * len(means))]
    hi = means[int(0.975 * len(means)) - 1]
    return round(point, 1), round(lo, 1), round(hi, 1), len(lemmas)


def rate_unclear(recs):
    """{class: (%unclear, n)} for c_third."""
    out = {}
    for c in CLASSES:
        sub = [r for r in recs if r["bridging_class"] == c and r.get("pred") is not None]
        n = len(sub)
        u = sum(1 for r in sub if r["pred"] == "UNCLEAR")
        out[c] = (round(100 * u / n, 1) if n else None, n)
    return out


def uptake_row(recs):
    # UPTAKE GATE = genuine reasoning volume before the answer (>=40 pre-FINAL chars), robust
    # to format: gpt sometimes externalizes the 3 steps in PROSE rather than "1./2./3." markers,
    # so numbered-step compliance is reported SEPARATELY (pct_numbered), not as the uptake gate.
    ct = [r["uptake"]["completion_tokens"] for r in recs
          if r.get("uptake") and r["uptake"].get("completion_tokens") is not None]
    cc = [r["uptake"]["content_chars"] for r in recs if r.get("uptake")]
    pf = [r["uptake"].get("pre_final_chars") or 0 for r in recs if r.get("uptake")]
    worked = [x for x in pf if x >= 40]
    numbered = [r for r in recs if r.get("uptake") and (r["uptake"].get("n_steps") or 0) >= 2]
    bare = [c for c in cc if c < 40]
    rt = [r["uptake"].get("reasoning_tokens") or 0 for r in recs if r.get("uptake")]
    n = len(recs)
    return {"median_completion_tokens": round(st.median(ct), 1) if ct else None,
            "median_pre_final_chars": round(st.median(pf), 1) if pf else None,
            "pct_bare_lt40chars": round(100 * len(bare) / n, 1) if n else None,
            "pct_worked_ge40_prefinal_chars": round(100 * len(worked) / n, 1) if n else None,
            "pct_numbered_ge2_steps": round(100 * len(numbered) / n, 1) if n else None,
            "median_reasoning_tokens": round(st.median(rt), 1) if rt else None,
            "n": n}


def offered_uptake_row(framing):
    o = load(OFFERED_RAW, framing, SLOT)
    if not o:
        return None
    # offered raw lacks pre_final_chars/n_steps -> worked computed from content_chars only
    ct = [r["uptake"]["completion_tokens"] for r in o
          if r.get("uptake") and r["uptake"].get("completion_tokens") is not None]
    cc = [r["uptake"]["content_chars"] for r in o if r.get("uptake")]
    bare = [c for c in cc if c < 40]
    n = len(o)
    return {"median_completion_tokens": round(st.median(ct), 1) if ct else None,
            "pct_bare_lt40chars": round(100 * len(bare) / n, 1) if n else None, "n": n}


def axis(recs, value_key):
    pairs = by_class_pairs(recs, value_key)
    return {c: dict(zip(("mean", "ci_lo", "ci_hi", "n_lemmas"), boot_ci(pairs[c])))
            for c in CLASSES}


def main():
    out = {"model": "openai/gpt-5.4-mini", "scope": "dwug+wic", "reps": REPS, "seed": SEED}

    # ---- uptake (the crux) ----
    up = {}
    for fr in ["b_rel", "b_conf", "c_third", "topic"]:
        recs = load(RAW, fr, SLOT)
        if recs:
            up[fr] = {"forced": uptake_row(recs), "offered": offered_uptake_row(fr)}
    out["uptake_manipulation_check"] = up

    # ---- axes ----
    b_rel = load(RAW, "b_rel", SLOT)
    b_conf = load(RAW, "b_conf", SLOT)
    c_third = load(RAW, "c_third", SLOT)
    topic = load(RAW, "topic", SLOT)

    if b_rel:
        out["position_b_rel"] = axis(b_rel, "pred")
        br = out["position_b_rel"]
        out["position_verdict"] = {
            "bridging_in_midband": MIDBAND[0] <= (br["bridging"]["mean"] or -1) <= MIDBAND[1],
            "pointwise_between": (br["clear-different"]["mean"] < br["bridging"]["mean"]
                                  < br["clear-same"]["mean"]),
            "ci_strict_between": (br["bridging"]["ci_lo"] > br["clear-different"]["mean"]
                                  and br["bridging"]["ci_hi"] < br["clear-same"]["mean"]),
        }
    if b_conf:
        out["confidence_b_conf"] = axis(b_conf, "pred2")
        bc = out["confidence_b_conf"]
        bridge_hi = bc["bridging"]["ci_hi"]
        out["confidence_verdict"] = {
            "bridging_pointwise_lower_than_both": (bc["bridging"]["mean"] < bc["clear-different"]["mean"]
                                                   and bc["bridging"]["mean"] < bc["clear-same"]["mean"]),
            "bridging_ci_strict_lower_than_both": (bridge_hi < bc["clear-different"]["mean"]
                                                   and bridge_hi < bc["clear-same"]["mean"]),
        }
    if c_third:
        out["decline_c_third_pct_unclear"] = {c: rate_unclear(c_third)[c] for c in CLASSES}
        d = out["decline_c_third_pct_unclear"]
        out["decline_verdict"] = {
            "bridging_elevated_vs_both": (d["bridging"][0] is not None
                                          and d["bridging"][0] > d["clear-different"][0]
                                          and d["bridging"][0] > d["clear-same"][0]),
        }
    if topic:
        out["topic_control_b_rel_vs_topic"] = axis(topic, "pred")

    # ---- clear-class precondition (benign-scaffold check) ----
    if b_rel and b_conf and c_third:
        br, bc = out["position_b_rel"], out["confidence_b_conf"]
        dec = out["decline_c_third_pct_unclear"]
        out["clear_class_precondition"] = {
            "poles_separated_b_rel": br["clear-same"]["mean"] - br["clear-different"]["mean"],
            "clear_same_conf": bc["clear-same"]["mean"], "clear_diff_conf": bc["clear-different"]["mean"],
            "clear_same_pct_unclear": dec["clear-same"][0], "clear_diff_pct_unclear": dec["clear-different"][0],
        }

    # ---- per-axis verdict (frozen v1 rule, gpt) ----
    if b_rel and b_conf and c_third:
        pos_ok = out["position_verdict"]["pointwise_between"] and out["position_verdict"]["bridging_in_midband"]
        conf_crack = out["confidence_verdict"]["bridging_ci_strict_lower_than_both"]
        dec_crack = out["decline_verdict"]["bridging_elevated_vs_both"]
        if conf_crack and dec_crack:
            commit = "GRADED commitment under forced surface (B and C both crack)"
        elif not conf_crack and not dec_crack:
            commit = "UNGRADED commitment (null holds) -- channel-controlled for gpt"
        else:
            commit = "MIXED/WEAK (B and C disagree) -- per modification 3, not the null, not a clean positive"
        out["verdict"] = {"position_graded": pos_ok, "commitment": commit}

    json.dump(out, open(os.path.join(HERE, "analysis.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
