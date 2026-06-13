#!/usr/bin/env python3
"""AANN inferential v3 — analysis. Implements the FROZEN design + PREREG exactly;
no tunable knobs. Written and committed at freeze time, BEFORE any model call
(probe.py refuses to run if this file is absent); the post-run verifier
recomputes from raw with independent code.

The headline indicator is the AANN-vs-control SHIFT, never the raw AANN rate
(Condition 2). The agreement (was/were) shift is the LOAD-BEARING discriminator
and gates the headline wording (Condition 3). The |FC shift - NLI shift| per
model is a reported named statistic, never averaged away (Condition 7). Tier-0
is a gate with a pre-declared failure consequence (Condition 7). The expected
unification key is EXPERT-STIPULATED (Condition 5); item-level disputed codings
are sensitivity-tested (Condition 6). Under-pressure subset reported separately
(Condition 4). All thresholds frozen pre-run (Condition 8).

FROZEN THRESHOLDS (fixed pre-data; baked here, not tunable):
  - shift threshold TAU = +0.20, INCLUSIVE (>= +0.20 passes).
  - a "positive" shift additionally needs bootstrap 95% CI lower bound > 0
    (STRICT). 10,000 resamples over items, seed 20260613.
  - Tier-0 pass >= 20/24, INCLUSIVE; >25% missing = instrument failure.
  - instrument-disagreement flag: |FC shift - NLI shift| >= 0.30 (INCLUSIVE)
    => mandatory per-model fragility caveat (fed to the instrument-sensitivity
    open question), independent of headline category.
  - VERDICT over Tier-0-passing models only:
      SUPPORTED       >=2 CONVERGENT-POSITIVE
      PARTIAL         >=2 PARAPHRASE-ONLY but <2 CONVERGENT-POSITIVE
      NULL            <2 even PARAPHRASE-ONLY
      INSTRUMENT FAIL <2 Tier-0 passers

Selftest: python3 analyze.py --selftest (synthetic in-memory; no files, no calls).
"""
import argparse
import json
import random
import re
import statistics
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
STIMULI = json.load(open(HERE / "stimuli.json"))
ITEMS = {it["id"]: it for it in STIMULI["items"]}
TIER0 = {p["id"]: p for p in STIMULI["tier0"]}
UNDER_PRESSURE = set(STIMULI["under_pressure_ids"])
DISPUTED = set(STIMULI["key_disputed_ids"])
# Row counts derive from the frozen item count (N base items): paraphrase and
# agreement are {AANN, control} per item (2N); NLI is 2 hypotheses x {AANN,
# control} per item (4N); Tier-0 is the fixed 24 pairs. After the 2026-06-13
# object-class drop N = 23 (was 32): paraphrase/agreement 46, nli 92, tier0 24.
_N = len(ITEMS)
EXPECTED_ROWS = {"paraphrase": 2 * _N, "nli": 4 * _N, "agreement": 2 * _N,
                 "tier0": len(TIER0)}
BOOT = 10000
SEED = 20260613

TAU = 0.20                 # shift threshold, inclusive (>=)
CI_LOWER_MUST_EXCEED = 0.0  # strict (>)
TIER0_MIN = 20             # inclusive (>=), of 24
DISAGREEMENT_MIN = 0.30    # inclusive (>=) => instrument-fragility caveat

PANEL_NAMES = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini",
               "C": "gemini-3.5-flash"}

CHIEF_COST = STIMULI["chief_cost_statement"]
KEY_PROVENANCE = STIMULI["expected_inference_key_provenance"]


# ---------------- statistics ----------------

def shift_ci(per_item_aann, per_item_control, ids, seed=SEED):
    """Paired AANN-vs-control shift = mean(aann_indicator) - mean(control)
    over the items present in BOTH conditions. Bootstrap 95% CI over ITEMS
    (resampling item ids; the shift is paired per item). Returns
    (shift, (ci_lo, ci_hi) | None, n_items). per_item_* map id -> 0/1 (or None
    if missing/absent for that item-condition)."""
    paired = [(i, per_item_aann.get(i), per_item_control.get(i)) for i in ids]
    paired = [(i, a, c) for (i, a, c) in paired if a is not None and c is not None]
    if len(paired) < 2:
        return float("nan"), None, len(paired)
    diffs = {i: a - c for (i, a, c) in paired}
    keys = [i for (i, _, _) in paired]
    shift = statistics.mean(diffs.values())
    rng = random.Random(seed)
    n = len(keys)
    boots = []
    for _ in range(BOOT):
        idx = [rng.randrange(n) for _ in range(n)]
        boots.append(statistics.mean(diffs[keys[j]] for j in idx))
    boots.sort()
    ci = (boots[int(0.025 * BOOT) - 1], boots[int(0.975 * BOOT) - 1])
    return shift, ci, n


def positive(shift, ci):
    """A 'positive' shift: shift >= TAU (inclusive) AND CI lower bound > 0
    (strict)."""
    if shift != shift:           # NaN
        return False
    return shift >= TAU and ci is not None and ci[0] > CI_LOWER_MUST_EXCEED


# ---------------- loading ----------------

def load(slot, arm):
    p = HERE / "raw" / f"{slot}-{arm}.json"
    if not p.exists():
        return None, "absent"
    rows = json.load(open(p))
    if len(rows) != EXPECTED_ROWS[arm]:
        return rows, "wrong-count"
    return rows, "ok"


def miss_gate(rows):
    miss = sum(1 for r in rows if r["value"] is None)
    frac = miss / len(rows) if rows else 1.0
    return miss, ("instrument-failure" if frac > 0.25
                  else "caveat" if frac > 0.10 else "ok")


def read_cost_log():
    p = HERE / "raw" / "cost-log.txt"
    if not p.exists():
        return {"status": "absent", "total_billed_usd": None}
    lines = [ln for ln in p.read_text().splitlines() if ln.strip()]
    total = sum(float(m.group(1)) for ln in lines
                for m in re.finditer(r"billed=\$([0-9.]+)", ln))
    miss = sum(int(m.group(1)) for ln in lines
               for m in re.finditer(r"missing_cost_calls=(\d+)", ln))
    out = {"status": "ok", "total_billed_usd": round(total, 4),
           "missing_cost_calls": miss}
    if miss:
        out["missing_cost_caveat"] = (f"{miss} call(s) reported no usage.cost; "
                                      "the billed total UNDERCOUNTS")
    return out


# ---------------- per-arm indicators (content recovered from counterbalanced letter) ----------------

def paraphrase_chose_unification(row):
    """Map the chosen LETTER back to content (Condition 1/2: block position
    bias at the stimulus level). 1 = chose unification paraphrase, 0 = chose
    distributive, None = missing."""
    if row["value"] is None:
        return None
    uni_letter = row["unification_letter"]
    return 1 if row["value"] == uni_letter else 0


def agreement_chose_was(row):
    """1 = chose singular 'was', 0 = chose 'were', None = missing."""
    if row["value"] is None:
        return None
    return 1 if row["value"] == row["was_letter"] else 0


def nli_affirm(row):
    """1 = YES (affirm), 0 = NO (withhold), None = missing."""
    if row["value"] is None:
        return None
    return 1 if row["value"] == "YES" else 0


def split_by_cond(rows, indicator):
    """rows -> {id: indicator} for aann and for control separately."""
    aann, ctrl = {}, {}
    for r in rows:
        v = indicator(r)
        (aann if r["cond"] == "aann" else ctrl)[r["id"]] = v
    return aann, ctrl


# ---------------- Tier-0 ----------------

def analyze_tier0(rows, status):
    res = {"arm_status": status}
    if not rows or status != "ok":
        return res
    ok = sum(1 for r in rows if r["value"] == TIER0[r["id"]]["aann_position"])
    miss, gate = miss_gate(rows)
    res.update({"n": len(rows), "aann_preferred": ok, "missing": miss,
                "missingness": gate,
                "pass": bool(ok >= TIER0_MIN and gate != "instrument-failure")})
    return res


# ---------------- per-model ----------------

def arm_shift(rows, indicator, ids, label):
    """Compute the AANN-vs-control shift + CI for one arm over the given ids."""
    aann, ctrl = split_by_cond(rows, indicator)
    shift, ci, n = shift_ci(aann, ctrl, ids)
    return {"label": label,
            "shift": None if shift != shift else round(shift, 4),
            "ci95": None if ci is None else [round(ci[0], 4), round(ci[1], 4)],
            "n_items": n, "positive": positive(shift, ci),
            "raw_aann_rate": (round(statistics.mean([v for v in aann.values()
                                                     if v is not None]), 4)
                              if any(v is not None for v in aann.values())
                              else None),
            "raw_control_rate": (round(statistics.mean([v for v in ctrl.values()
                                                        if v is not None]), 4)
                                 if any(v is not None for v in ctrl.values())
                                 else None)}


def headline(para_pos, agr_pos, convergent_positive):
    """Condition 3 headline-gating rule, mechanical.
    - convergent_positive: A + B + agreement all positive.
    - PARAPHRASE-ONLY: A positive but agreement null -> the cautious headline.
    - else NULL."""
    if convergent_positive:
        return ("CONVERGENT-POSITIVE",
                "the construction shifts inferential behaviour, including the "
                "grammaticalized singular reflex, in the direction the published "
                "semantics predicts")
    if para_pos and not agr_pos:
        return ("PARAPHRASE-ONLY",
                "shift in paraphrase selection WITHOUT the grammaticalized "
                "reflex (NOT 'draws the unification inference')")
    if para_pos and agr_pos:
        # A + agreement positive but B (NLI) not -> still cautious, not full
        # convergence; report as paraphrase+reflex, flagged for the NLI gap.
        return ("PARAPHRASE-PLUS-REFLEX-NO-NLI",
                "paraphrase and agreement shift positive but the NLI convergent "
                "arm did not confirm; not full convergence (see disagreement)")
    return ("NULL", "no AANN-vs-control shift at this instrument")


def analyze_model(slot, para, para_st, nli, nli_st, agr, agr_st, t0, t0_st):
    res = {"slot": slot, "model": PANEL_NAMES[slot],
           "arm_status": {"paraphrase": para_st, "nli": nli_st,
                          "agreement": agr_st, "tier0": t0_st}}
    res["tier0"] = analyze_tier0(t0, t0_st)
    if not all(st == "ok" for st in (para_st, nli_st, agr_st)):
        return res

    all_ids = list(ITEMS)

    # ---- ARM A: paraphrase forced choice (PRIMARY), full set + under-pressure
    res["paraphrase"] = arm_shift(para, paraphrase_chose_unification, all_ids,
                                  "P(unification|AANN) - P(unification|control)")
    res["paraphrase_under_pressure"] = arm_shift(
        para, paraphrase_chose_unification, list(UNDER_PRESSURE),
        "under-pressure subset (distributive locally-fluent): paraphrase shift")
    # disputed-coding sensitivity (Condition 6): headline arm excluding flags
    res["paraphrase_excl_disputed"] = arm_shift(
        para, paraphrase_chose_unification,
        [i for i in all_ids if i not in DISPUTED],
        "paraphrase shift excluding item-level disputed-key items")

    # ---- ARM B: NLI (CONVERGENT) — unification + whole-eval hypotheses only
    nli_uw = [r for r in nli if r["hyp_key"] in ("unification_hyp",
                                                 "whole_eval_hyp")]
    res["nli"] = arm_shift(nli_uw, nli_affirm, all_ids,
                           "affirm-rate shift AANN vs control "
                           "(unification + whole-evaluation hypotheses)")

    # ---- AGREEMENT sub-probe (LOAD-BEARING DISCRIMINATOR)
    res["agreement"] = arm_shift(agr, agreement_chose_was, all_ids,
                                 "P(was|AANN) - P(was|control) [singular reflex]")

    # ---- named disagreement statistic |FC shift - NLI shift| (Condition 7)
    fc, nl = res["paraphrase"]["shift"], res["nli"]["shift"]
    disagree = (None if fc is None or nl is None else round(abs(fc - nl), 4))
    res["instrument_disagreement"] = {
        "statistic": "|FC shift - NLI shift|",
        "value": disagree,
        "flag": bool(disagree is not None and disagree >= DISAGREEMENT_MIN),
        "fed_to": "open-question/instrument-sensitivity-constructional-inference",
    }
    if res["instrument_disagreement"]["flag"]:
        res["instrument_fragility_caveat"] = (
            f"mandatory: |FC shift - NLI shift| = {disagree} >= "
            f"{DISAGREEMENT_MIN}; this model's inferential read is "
            f"instrument-fragile (fed to the instrument-sensitivity open "
            f"question), never averaged away (PREREG)")

    # ---- convergence category (Condition 3 + 7), gated on Tier-0 handled at stratum
    para_pos = res["paraphrase"]["positive"]
    agr_pos = res["agreement"]["positive"]
    nli_pos = res["nli"]["positive"]
    convergent_positive = bool(para_pos and nli_pos and agr_pos)
    cat, note = headline(para_pos, agr_pos, convergent_positive)
    res["category"] = cat
    res["headline"] = note
    res["convergent_positive"] = convergent_positive

    # disputed-coding category sensitivity (Condition 6)
    para_pos_excl = res["paraphrase_excl_disputed"]["positive"]
    res["disputed_sensitivity"] = {
        "n_disputed_excluded": len(DISPUTED),
        "paraphrase_positive_all_items": para_pos,
        "paraphrase_positive_excl_disputed": para_pos_excl,
        "category_changes": para_pos != para_pos_excl,
    }
    if para_pos != para_pos_excl:
        res["disputed_sensitivity"]["mandatory_caveat"] = (
            "MANDATORY CAVEAT: excluding the item-level disputed-key items "
            "changes the paraphrase-arm positivity; the expert-stipulated key "
            "is not settled where flagged (Condition 6); result page must carry "
            "this sentence.")
    return res


def stratum_verdict(passing_categories):
    """Over Tier-0-passing models. PREREG frozen verdict map."""
    n_conv = sum(c == "CONVERGENT-POSITIVE" for c in passing_categories)
    # PARAPHRASE-ONLY and PARAPHRASE-PLUS-REFLEX-NO-NLI both count as
    # "reached paraphrase positivity but not full convergence"
    n_para = sum(c in ("PARAPHRASE-ONLY", "PARAPHRASE-PLUS-REFLEX-NO-NLI",
                       "CONVERGENT-POSITIVE")
                 for c in passing_categories)
    if n_conv >= 2:
        return "SUPPORTED (inferential half)"
    if n_para >= 2:
        return "PARTIAL (paraphrase/constructional shift without full convergence)"
    return "NULL (no AANN-vs-control inferential shift at this instrument)"


def assemble(per_model):
    incomplete = [f"{s}/{arm}:{st}" for s, r in per_model.items()
                  for arm, st in r["arm_status"].items() if st != "ok"]
    out = {
        "run": "2026-06-13-aann-inferential-v3",
        "design": "experiments/designs/aann-construction-v3-inferential.md",
        "anchor": "internal-contrast-only",
        "chief_cost_statement": CHIEF_COST,
        "expected_inference_key_provenance": KEY_PROVENANCE,
        "primary_instrument": "A (paraphrase forced-choice)",
        "thresholds": {"tau_shift_inclusive": TAU,
                       "ci_lower_strictly_above": CI_LOWER_MUST_EXCEED,
                       "tier0_min_inclusive_of_24": TIER0_MIN,
                       "disagreement_flag_min_inclusive": DISAGREEMENT_MIN},
        "models": per_model,
        "cost": read_cost_log(),
    }
    if incomplete:
        out["verdict"] = "INCOMPLETE (required arm missing/partial)"
        out["incomplete_arms"] = incomplete
        return out
    passers = [s for s in ("A", "B", "C") if per_model[s]["tier0"].get("pass")]
    excluded = [s for s in ("A", "B", "C") if s not in passers]
    out["tier0_passers"] = passers
    if excluded:
        out["tier0_excluded_models"] = excluded
        out["tier0_exclusion_note"] = (
            "Tier-0 failure = instrument failure for the model: its inferential "
            "category is reported descriptively only and is EXCLUDED from the "
            ">=2-of-3 stratum count (Condition 7)")
    if len(passers) < 2:
        out["verdict"] = ("INSTRUMENT FAILURE (fewer than 2 Tier-0 passers; no "
                          "substantive inferential verdict)")
    else:
        out["verdict"] = stratum_verdict(
            [per_model[s]["category"] for s in passers])
    return out


def report(out):
    print("== AANN inferential v3 — FROZEN PREREG analysis ==")
    print(f"   anchor: {out['anchor']} | primary: {out['primary_instrument']}")
    for s in ("A", "B", "C"):
        r = out["models"].get(s, {})
        st = r.get("arm_status", {})
        t0 = r.get("tier0", {})
        if any(v != "ok" for v in st.values()):
            print(f"  {s} ({PANEL_NAMES[s]}): arm status {st}"
                  f" | tier0 {t0.get('aann_preferred')}/24 "
                  f"({'PASS' if t0.get('pass') else 'FAIL/NA'})")
            continue
        print(f"  {s} ({r['model']}): tier0 {t0['aann_preferred']}/24 "
              f"({'PASS' if t0['pass'] else 'FAIL -> excluded'})")
        print(f"     A paraphrase shift = {r['paraphrase']['shift']} "
              f"CI {r['paraphrase']['ci95']} "
              f"(pos={r['paraphrase']['positive']}; raw AANN "
              f"{r['paraphrase']['raw_aann_rate']} vs ctrl "
              f"{r['paraphrase']['raw_control_rate']})")
        print(f"       under-pressure subset shift = "
              f"{r['paraphrase_under_pressure']['shift']} "
              f"(n={r['paraphrase_under_pressure']['n_items']})")
        print(f"     B NLI shift = {r['nli']['shift']} CI {r['nli']['ci95']} "
              f"(pos={r['nli']['positive']})")
        print(f"     AGREEMENT shift = {r['agreement']['shift']} "
              f"CI {r['agreement']['ci95']} (pos={r['agreement']['positive']}) "
              f"[load-bearing discriminator]")
        print(f"     |FC-NLI| = {r['instrument_disagreement']['value']} "
              f"(flag={r['instrument_disagreement']['flag']})")
        print(f"     category: {r['category']}  -> {r['headline']}")
    print(f"  VERDICT: {out['verdict']}")
    print(f"  cost: {out['cost'].get('total_billed_usd')} "
          f"({out['cost'].get('status')})")
    print("\n=== MACHINE-READABLE JSON SUMMARY ===")
    print(json.dumps(out, indent=1))


def main():
    per = {}
    for slot in ("A", "B", "C"):
        para, ps = load(slot, "paraphrase")
        nli, ns = load(slot, "nli")
        agr, ags = load(slot, "agreement")
        t0, t0s = load(slot, "tier0")
        per[slot] = analyze_model(slot, para, ps, nli, ns, agr, ags, t0, t0s)
    out = assemble(per)
    json.dump(out, open(HERE / "results.json", "w"), indent=1)
    report(out)


# ---------------- selftest (synthetic; no files, no calls) ----------------

def _para_rows(p_uni_aann, p_uni_ctrl, na_ids=()):
    """Synthetic paraphrase rows: chose-unification with prob 1 if rate==1,
    0 if rate==0 (deterministic per item for testable shifts). Maps content
    back through the frozen counterbalanced letter."""
    rows = []
    for it in STIMULI["items"]:
        for cond, rate in (("aann", p_uni_aann), ("control", p_uni_ctrl)):
            if it["id"] in na_ids and cond == "aann":
                val = None
            else:
                chose_uni = rate
                uni_letter = it["fc_letter_unification"]
                val = uni_letter if chose_uni else ("B" if uni_letter == "A"
                                                    else "A")
            rows.append({"id": it["id"], "arm": "paraphrase", "cond": cond,
                         "unification_letter": it["fc_letter_unification"],
                         "raw": str(val), "value": val, "usage": None,
                         "error": None})
    return rows


def _nli_rows(affirm_aann, affirm_ctrl):
    rows = []
    for it in STIMULI["items"]:
        for hyp_key in ("unification_hyp", "whole_eval_hyp"):
            for cond, aff in (("aann", affirm_aann), ("control", affirm_ctrl)):
                rows.append({"id": it["id"], "arm": "nli", "cond": cond,
                             "hyp_key": hyp_key,
                             "raw": "YES" if aff else "NO",
                             "value": "YES" if aff else "NO",
                             "usage": None, "error": None})
    return rows


def _agr_rows(was_aann, was_ctrl):
    rows = []
    for it in STIMULI["items"]:
        for cond, w in (("aann", was_aann), ("control", was_ctrl)):
            was_letter = it["agreement"]["agr_letter_was"]
            val = was_letter if w else ("B" if was_letter == "A" else "A")
            rows.append({"id": it["id"], "arm": "agreement", "cond": cond,
                         "was_letter": was_letter, "raw": str(val),
                         "value": val, "usage": None, "error": None})
    return rows


def _tier0_rows(n_correct, n_missing=0):
    rows = []
    for i, p in enumerate(STIMULI["tier0"]):
        if i < n_missing:
            val = None
        elif i < n_missing + n_correct:
            val = p["aann_position"]
        else:
            val = "A" if p["aann_position"] == "B" else "B"
        rows.append({"id": p["id"], "arm": "tier0",
                     "aann_position": p["aann_position"], "raw": str(val),
                     "value": val, "usage": None, "error": None})
    return rows


def selftest():
    failures = []
    n = [0]

    def check(name, cond):
        n[0] += 1
        print(("PASS " if cond else "FAIL ") + name)
        if not cond:
            failures.append(name)

    # ---- shift math + positivity
    s, ci, k = shift_ci({i: 1 for i in ITEMS}, {i: 0 for i in ITEMS},
                        list(ITEMS))
    check("full +1 shift computed", abs(s - 1.0) < 1e-9 and k == len(ITEMS))
    check("+1 shift is positive (>=TAU, CI>0)", positive(s, ci))
    s0, ci0, _ = shift_ci({i: 1 for i in ITEMS}, {i: 1 for i in ITEMS},
                          list(ITEMS))
    check("zero shift not positive", not positive(s0, ci0))
    check("zero-shift CI is degenerate (0,0)", ci0 == (0.0, 0.0))
    # small shift below TAU: pick a one-count strictly under TAU*N (TAU*23=4.6,
    # so 4/23 ~ 0.174 < 0.20). Keep it robust to the item count.
    half = list(ITEMS)
    n_below = int(TAU * len(half))   # floor(0.20*23) = 4 -> 4/23 = 0.174 < TAU
    a = {i: (1 if k2 < n_below else 0) for k2, i in enumerate(half)}
    c = {i: 0 for i in half}
    ss, sci, _ = shift_ci(a, c, half)
    check(f"shift {n_below}/{len(half)} (~{n_below/len(half):.3f}) < TAU "
          "not positive", not positive(ss, sci))

    # ---- Tier-0 gate
    check("tier0 20/24 passes (inclusive)",
          analyze_tier0(_tier0_rows(20), "ok")["pass"])
    check("tier0 19/24 fails", not analyze_tier0(_tier0_rows(19), "ok")["pass"])
    check("tier0 >25% missing = instrument failure",
          not analyze_tier0(_tier0_rows(17, 7), "ok")["pass"]
          and analyze_tier0(_tier0_rows(17, 7), "ok")["missingness"]
          == "instrument-failure")

    # ---- headline gating (Condition 3)
    check("convergent-positive headline",
          headline(True, True, True)[0] == "CONVERGENT-POSITIVE")
    check("paraphrase-only (agreement null) -> cautious headline",
          headline(True, False, False)[0] == "PARAPHRASE-ONLY"
          and "WITHOUT the grammaticalized reflex" in headline(True, False,
                                                               False)[1])
    check("null headline when paraphrase not positive",
          headline(False, True, False)[0] == "NULL")

    # ---- full pipeline: A convergent-positive, B paraphrase-only, C null
    perA = analyze_model(
        "A", _para_rows(1, 0), "ok", _nli_rows(1, 0), "ok",
        _agr_rows(1, 0), "ok", _tier0_rows(24), "ok")
    check("A: paraphrase shift +1, positive",
          perA["paraphrase"]["shift"] == 1.0 and perA["paraphrase"]["positive"])
    check("A: agreement shift +1, positive (discriminator)",
          perA["agreement"]["positive"])
    check("A: NLI shift +1, positive", perA["nli"]["positive"])
    check("A: category CONVERGENT-POSITIVE", perA["category"]
          == "CONVERGENT-POSITIVE")
    check("A: raw rates recorded but not the headline (Condition 2)",
          perA["paraphrase"]["raw_aann_rate"] == 1.0
          and perA["paraphrase"]["raw_control_rate"] == 0.0)
    # B: paraphrase shift positive, but agreement NULL (was_aann==was_ctrl)
    perB = analyze_model(
        "B", _para_rows(1, 0), "ok", _nli_rows(0, 0), "ok",
        _agr_rows(0, 0), "ok", _tier0_rows(22), "ok")
    check("B: agreement shift 0 -> not positive",
          not perB["agreement"]["positive"])
    check("B: category PARAPHRASE-ONLY (agreement null gates headline)",
          perB["category"] == "PARAPHRASE-ONLY")
    # C: null everywhere
    perC = analyze_model(
        "C", _para_rows(0, 0), "ok", _nli_rows(0, 0), "ok",
        _agr_rows(0, 0), "ok", _tier0_rows(20), "ok")
    check("C: category NULL", perC["category"] == "NULL")

    # ---- |FC - NLI| disagreement flag
    perD = analyze_model(
        "A", _para_rows(1, 0), "ok", _nli_rows(0, 0), "ok",
        _agr_rows(1, 0), "ok", _tier0_rows(24), "ok")
    check("|FC-NLI| = 1.0 flags disagreement + mandatory caveat",
          perD["instrument_disagreement"]["value"] == 1.0
          and perD["instrument_disagreement"]["flag"]
          and "instrument_fragility_caveat" in perD)

    # ---- stratum verdicts
    out = assemble({"A": perA, "B": perB, "C": perC})
    check("stratum: 1 convergent + paraphrase-only + null -> PARTIAL",
          out["verdict"].startswith("PARTIAL"))
    out2 = assemble({"A": perA, "B": analyze_model(
        "B", _para_rows(1, 0), "ok", _nli_rows(1, 0), "ok",
        _agr_rows(1, 0), "ok", _tier0_rows(24), "ok"), "C": perC})
    check("stratum: 2 convergent-positive -> SUPPORTED",
          out2["verdict"].startswith("SUPPORTED")
          and out2["tier0_passers"] == ["A", "B", "C"])
    out3 = assemble({"A": perA, "B": perB,
                     "C": analyze_model("C", _para_rows(0, 0), "ok",
                                        _nli_rows(0, 0), "ok", _agr_rows(0, 0),
                                        "ok", _tier0_rows(19), "ok")})
    check("tier0-failing model excluded from count",
          out3.get("tier0_excluded_models") == ["C"])
    out4 = assemble({"A": analyze_model("A", _para_rows(1, 0), "ok",
                                        _nli_rows(1, 0), "ok", _agr_rows(1, 0),
                                        "ok", _tier0_rows(19), "ok"),
                     "B": perB,
                     "C": analyze_model("C", _para_rows(0, 0), "ok",
                                        _nli_rows(0, 0), "ok", _agr_rows(0, 0),
                                        "ok", _tier0_rows(19), "ok")})
    check("fewer than 2 tier0 passers -> INSTRUMENT FAILURE",
          out4["verdict"].startswith("INSTRUMENT FAILURE"))

    # ---- INCOMPLETE path
    out5 = assemble({"A": {"slot": "A", "model": PANEL_NAMES["A"],
                           "arm_status": {"paraphrase": "absent", "nli": "ok",
                                          "agreement": "ok", "tier0": "ok"},
                           "tier0": {"arm_status": "ok"}},
                     "B": perB, "C": perC})
    check("absent arm -> INCOMPLETE", out5["verdict"].startswith("INCOMPLETE"))

    # ---- under-pressure subset + disputed sensitivity present
    check("under-pressure subset computed (n matches stimuli)",
          perA["paraphrase_under_pressure"]["n_items"] == len(UNDER_PRESSURE))
    check("disputed sensitivity block present",
          "disputed_sensitivity" in perA
          and perA["disputed_sensitivity"]["n_disputed_excluded"]
          == len(DISPUTED))
    # ---- determinism
    s1 = shift_ci({i: 1 for i in ITEMS}, {i: 0 for i in ITEMS}, list(ITEMS))[1]
    s2 = shift_ci({i: 1 for i in ITEMS}, {i: 0 for i in ITEMS}, list(ITEMS))[1]
    check("bootstrap CI deterministic under frozen seed", s1 == s2)
    check("summary JSON-serializable", bool(json.dumps(out2)))

    if failures:
        raise SystemExit(f"SELFTEST FAILED: {failures}")
    print(f"SELFTEST OK ({n[0]} checks)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
    else:
        main()
