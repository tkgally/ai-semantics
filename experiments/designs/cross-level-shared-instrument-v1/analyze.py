#!/usr/bin/env python3
"""Cross-level shared-instrument analysis -- the FROZEN cross-level reading rule.

Built at the same time as the frozen instrument (2026-06-22); reads raw/ which does NOT
yet exist (no probe has run). Applies instrument.json -> reading_rule_frozen with no
threshold tuned after any output. Encodes, per the resolved gate's binding conditions:

  C1 (decline load-bearing): the moment pole is decided by the categorical DECLINE rate
     (%UNCLEAR), NOT the 0-100 confidence. Confidence may CORROBORATE but never, on its
     own, flips a moment-axis verdict.
  C3 (clear-class precondition -> NO-GO per level): a level is interpretable only if its
     clear classes show HIGH confidence AND LOW decline. A failing level collapses to
     weak / internal-contrast-only and contributes NO moment verdict.
  C4 (channel-sensitivity guard): a confidence shift on the ambiguous class WITHOUT a
     matching decline shift is reported as a SELF-REPORT effect, not graded-moment evidence.
  Q2 verdict map: CONFIRM (>=2 levels show the two-axis dissociation under the one frozen
     instrument, same model) / DISSOLVE (first-class null) / WEAK.

Per level the ambiguous class is: lexical 'bridging' | constructional 'ambiguous' |
relational 'ambiguous-midrecord'. The clear classes are the level's two clear-* classes.

Bootstrap: cluster by ITEM-SET where sets exist (constructional set / relational set), by
LEMMA for lexical; 10000 reps, seed 20260622, 95% percentile CIs on class-rate gaps.
Direction-of-effect only; small clustered N -> wide CIs, no coverage claim. NO human
comparison: lexical capped to usage-similarity; constructional+relational internal-contrast-only.

Run (after a probe run): python3 analyze.py   (reads raw/, writes analysis.json, prints table)
"""
import json
import os
import random
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
INSTRUMENT = os.path.join(HERE, "instrument.json")
SEED = 20260622
REPS = 10000

# per-level (ambiguous_class, [clear_classes], cluster_key)
LEVELS = {
    "lexical": ("bridging", ["clear-same", "clear-different"], "lemma"),
    "constructional": ("ambiguous", ["clear-reading1", "clear-reading2"], "set"),
    "relational": ("ambiguous-midrecord",
                   ["clear-determinate", "clear-other-determinate"], "set"),
}
# C3 precondition thresholds (frozen, ordinal -- a level interpretable only if clear classes
# clear these). Decline LOW = clear-class %UNCLEAR small; confidence HIGH = clear-class mean
# confidence well above the [40,60] mid-band. These are NECESSARY-condition gates, not pass
# bars for the conjecture; documented as preconditions in the gate (C3).
CLEAR_DECLINE_MAX = 0.20   # clear classes must decline on < 20% of items
CLEAR_CONF_MIN = 70        # clear-class mean confidence must exceed 70 (above mid-band 60)


def load_level(level, slot):
    p = os.path.join(RAW, f"{level}_{slot}.json")
    if not os.path.exists(p):
        return None
    return json.load(open(p, encoding="utf-8"))


def cluster_key(rec, level):
    if level == "lexical":
        return rec.get("lemma") or rec["item_id"]
    return rec["item_id"][:-1]  # set id = item_id minus trailing letter


def rates(recs):
    """decline rate (%UNCLEAR) and mean confidence over valid records."""
    n = len(recs)
    if n == 0:
        return None, None, 0
    decl = sum(1 for r in recs if (r.get("call") or "").upper() == "UNCLEAR") / n
    confs = [r["conf"] for r in recs if r.get("conf") is not None]
    mconf = sum(confs) / len(confs) if confs else None
    return decl, mconf, n


def clustered_bootstrap_gap(amb, clear, level, stat):
    """95% CI on (amb_stat - clear_stat) resampling CLUSTERS with replacement."""
    rng = random.Random(SEED)
    amb_c, clear_c = defaultdict(list), defaultdict(list)
    for r in amb:
        amb_c[cluster_key(r, level)].append(r)
    for r in clear:
        clear_c[cluster_key(r, level)].append(r)
    ak, ck = list(amb_c), list(clear_c)
    if not ak or not ck:
        return None
    gaps = []
    for _ in range(REPS):
        a = [x for k in (rng.choice(ak) for _ in ak) for x in amb_c[k]]
        c = [x for k in (rng.choice(ck) for _ in ck) for x in clear_c[k]]
        sa, sc = stat(a), stat(c)
        if sa is None or sc is None:
            continue
        gaps.append(sa - sc)
    if not gaps:
        return None
    gaps.sort()
    lo = gaps[int(0.025 * len(gaps))]
    hi = gaps[int(0.975 * len(gaps)) - 1]
    return round(lo, 4), round(hi, 4)


def analyze_level(level, slot):
    amb_class, clear_classes, _ = LEVELS[level]
    recs = load_level(level, slot)
    if not recs:
        return None
    by_class = defaultdict(list)
    for r in recs:
        by_class[r.get("class")].append(r)
    amb = by_class.get(amb_class, [])
    clear = [r for cc in clear_classes for r in by_class.get(cc, [])]
    a_decl, a_conf, a_n = rates(amb)
    c_decl, c_conf, c_n = rates(clear)

    # C3 precondition: clear classes high confidence AND low decline
    precond_ok = (c_decl is not None and c_decl <= CLEAR_DECLINE_MAX
                  and c_conf is not None and c_conf >= CLEAR_CONF_MIN)

    # decline stat = %UNCLEAR; the LOAD-BEARING moment-axis signal (C1)
    def decline_stat(rs):
        return rates(rs)[0]

    def conf_stat(rs):
        return rates(rs)[1]

    decl_gap_ci = clustered_bootstrap_gap(amb, clear, level, decline_stat)
    conf_gap_ci = clustered_bootstrap_gap(amb, clear, level, conf_stat)

    # moment pole (C1): "discrete/uncommitted on the moment" holds iff decline is NOT
    # elevated on the ambiguous class vs clear classes (CI on the decline gap does not
    # clear 0 positive). Elevated decline => graded-on-the-moment.
    decline_elevated = decl_gap_ci is not None and decl_gap_ci[0] > 0
    conf_lower = conf_gap_ci is not None and conf_gap_ci[1] < 0  # amb conf < clear conf

    # C4 guard: confidence dropped but decline did not rise => SELF-REPORT effect only
    c4_self_report_only = conf_lower and not decline_elevated

    if not precond_ok:
        moment_verdict = "NO-GO (C3 clear-class precondition failed) -> weak/internal-contrast-only"
    elif decline_elevated:
        moment_verdict = "GRADED-ON-MOMENT (decline elevated on ambiguous class)"
    else:
        moment_verdict = ("DISCRETE/UNCOMMITTED-ON-MOMENT (decline not elevated; C1 load-bearing)"
                          + (" [C4: confidence-only softening noted as self-report, NOT moment evidence]"
                             if c4_self_report_only else ""))

    return {
        "level": level, "model": slot,
        "ambiguous": {"class": amb_class, "n": a_n, "decline_rate": a_decl,
                      "mean_conf": a_conf},
        "clear": {"classes": clear_classes, "n": c_n, "decline_rate": c_decl,
                  "mean_conf": c_conf},
        "decline_gap_ci_amb_minus_clear": decl_gap_ci,
        "conf_gap_ci_amb_minus_clear": conf_gap_ci,
        "C3_precondition_ok": precond_ok,
        "C4_confidence_only_self_report": c4_self_report_only,
        "moment_verdict": moment_verdict,
    }


def cross_level_verdict(per_level_per_model):
    """Q2 map. CONFIRM iff the SAME model shows DISCRETE-on-moment at >=2 C3-passing levels
    (the aggregate axis is documented separately per level; here the moment-pole dissociation
    is the cross-level test). DISSOLVE iff levels go graded/divergent under the shared
    instrument. WEAK if too few interpretable levels."""
    out = {}
    by_model = defaultdict(dict)
    for r in per_level_per_model:
        by_model[r["model"]][r["level"]] = r
    for model, levels in by_model.items():
        interpretable = {lv: r for lv, r in levels.items() if r["C3_precondition_ok"]}
        discrete = [lv for lv, r in interpretable.items()
                    if r["moment_verdict"].startswith("DISCRETE")]
        graded = [lv for lv, r in interpretable.items()
                  if r["moment_verdict"].startswith("GRADED")]
        if len(interpretable) < 2:
            v = "WEAK (fewer than 2 levels passed the C3 precondition / are interpretable)"
        elif len(discrete) >= 2 and not graded:
            scope = ("3-level" if len(discrete) >= 3 else
                     "2-level instrument-equalized regularity (R2 over levels tested; "
                     "if relational excluded, scope per reporting_nuance)")
            v = f"CONFIRM ({scope}): discrete-on-moment at {sorted(discrete)}"
        elif graded:
            v = (f"DISSOLVE (first-class null): moment pole GRADED under the shared "
                 f"instrument at {sorted(graded)} -> the equalized instrument kills the "
                 f"shape there; deflationary default stands")
        else:
            v = "DISSOLVE/divergent: no coherent >=2-level discrete-on-moment pattern"
        out[model] = {"interpretable_levels": sorted(interpretable),
                      "discrete_on_moment": sorted(discrete),
                      "graded_on_moment": sorted(graded), "verdict": v}
    return out


def main():
    if not os.path.isdir(RAW) or not os.listdir(RAW):
        print("raw/ is empty -- no probe has run yet. This is expected at build time. "
              "analyze.py is frozen and ready; run probe.py (in a later, cleared session) "
              "first.")
        return
    per = []
    slots = ["A", "B", "C"]
    for slot in slots:
        for level in LEVELS:
            r = analyze_level(level, slot)
            if r:
                per.append(r)
                print(json.dumps(r, indent=1))
    verdicts = cross_level_verdict(per)
    print("\n=== CROSS-LEVEL VERDICTS (Q2) ===")
    print(json.dumps(verdicts, indent=1))
    json.dump({"per_level": per, "cross_level": verdicts,
               "scope_cap": "NO human comparison; lexical capped to usage-similarity; "
                            "constructional+relational internal-contrast-only."},
              open(os.path.join(HERE, "analysis.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
