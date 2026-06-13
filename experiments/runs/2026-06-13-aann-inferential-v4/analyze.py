#!/usr/bin/env python3
"""AANN inferential v4 — analysis. Implements the FROZEN v4 design + PREREG
exactly; no tunable knobs. Written and committed at freeze time, BEFORE any model
call (probe.py refuses to run if this file is absent); the post-run verifier
recomputes from raw with independent code.

v4's single structural change from v3 is the CONTROL GEOMETRY: paraphrase and NLI
now carry THREE premise frames (aann / ddc / lcc), so the headline is a DOUBLE
contrast Δ² that nets out the imported lexical cue. The agreement (was/were) arm
and Tier-0 are UNCHANGED from v3 (two conditions: aann / control bare-plural and
aann / ill-formed respectively).

THE DECISION RULE (baked in, governing decisions:
aann-inferential-default-coincidence §Ratification + aann-inferential-
operationalization §Ratification):

  Headroom-precondition gate (Condition N1), read PRE-HEADLINE, per model:
    P(uni|DDC) on paraphrase. PASS <= 0.30; MARGINAL 0.30-0.50 (caveat);
    HEADROOM-FAIL > 0.50 (excluded from the headline). Whole-design gate: if
    fewer than 2 models clear (PASS/MARGINAL) -> overall HEADROOM-FAIL ->
    OPTION-B NAMED NULL. NLI carries an analogous DDC check, reported alongside,
    NOT gating the primary.

  AANN shift        = P(uni|AANN) - P(uni|DDC)
  lexical-cue shift = P(uni|LCC)  - P(uni|DDC)
  Δ² (headline)     = AANN shift - lexical-cue shift = P(uni|AANN) - P(uni|LCC)
  "positive": Δ² >= TAU (=+0.20) AND item-level bootstrap 95% CI-lower > 0.

  Agreement shift   = P(was|AANN) - P(was|bare-plural control); single contrast,
                      same TAU + bootstrap (unchanged from v3).

  Named disagreement |FC Δ² - NLI Δ²| per model, flag >= 0.30.

  Verdict map (§6): CONVERGENT-POSITIVE / PARAPHRASE-ONLY / LEXICAL-CUE ARTIFACT /
  INSTRUMENT-DISAGREEMENT (caveat) / NULL / HEADROOM-FAIL->Option-B / INSTRUMENT
  FAILURE (<2 pass Tier-0). Overall verdict per §6. Headline-gating: paraphrase-
  positive but agreement-null => "shift WITHOUT the grammaticalized reflex".

FROZEN THRESHOLDS (fixed pre-data; baked here, not tunable):
  - double-contrast threshold TAU = +0.20, INCLUSIVE (Δ² >= +0.20 passes).
  - a "positive" Δ² additionally needs bootstrap 95% CI lower bound > 0 (STRICT).
    10,000 item-level resamples, seed 20260613.
  - headroom gate: PASS P(uni|DDC) <= 0.30; MARGINAL <= 0.50; FAIL > 0.50.
  - Tier-0 pass >= 20/24, INCLUSIVE; >25% missing = instrument failure.
  - instrument-disagreement flag: |FC Δ² - NLI Δ²| >= 0.30 (INCLUSIVE).

Selftest: python3 analyze.py --selftest (synthetic in-memory; no files, no calls).
"""
import argparse
import json
import random
import statistics
import re
from pathlib import Path

HERE = Path(__file__).parent
STIMULI = json.load(open(HERE / "stimuli.json"))
ITEMS = {it["id"]: it for it in STIMULI["items"]}
TIER0 = {p["id"]: p for p in STIMULI["tier0"]}
UNDER_PRESSURE = set(STIMULI["under_pressure_ids"])
DISPUTED = set(STIMULI["key_disputed_ids"])

# Row counts derive from the frozen item count (N base items):
#   paraphrase  : 3 frames (aann/ddc/lcc) per item            -> 3N
#   nli         : 2 hypotheses x 3 frames per item             -> 6N
#   agreement   : 2 conditions (aann/control bare-plural)      -> 2N
#   tier0       : the fixed 24 pairs
# N = 23: paraphrase 69, nli 138, agreement 46, tier0 24.
_N = len(ITEMS)
EXPECTED_ROWS = {"paraphrase": 3 * _N, "nli": 6 * _N, "agreement": 2 * _N,
                 "tier0": len(TIER0)}
BOOT = 10000
SEED = 20260613

TAU = 0.20                 # double-contrast threshold, inclusive (>=)
CI_LOWER_MUST_EXCEED = 0.0  # strict (>)
HEADROOM_TARGET = 0.30     # PASS <= 0.30 (inclusive)
HEADROOM_CEILING = 0.50    # MARGINAL <= 0.50 (inclusive); > 0.50 = HEADROOM-FAIL
TIER0_MIN = 20             # inclusive (>=), of 24
DISAGREEMENT_MIN = 0.30    # inclusive (>=) => instrument-fragility caveat

PANEL_NAMES = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini",
               "C": "gemini-3.5-flash"}

CHIEF_COST = STIMULI["chief_cost_statement"]
KEY_PROVENANCE = STIMULI["expected_inference_key_provenance"]


# ---------------- statistics ----------------

def rate(per_item):
    """Mean of the present (non-None) 0/1 indicators in a {id: 0/1/None} map."""
    vals = [v for v in per_item.values() if v is not None]
    return statistics.mean(vals) if vals else None


def double_contrast_ci(aann, lcc, ddc, ids, seed=SEED):
    """Item-level bootstrap on the DOUBLE contrast Δ² = P(uni|AANN) - P(uni|LCC),
    over items present in ALL THREE frames. Δ² algebraically equals
    (AANN shift) - (lexical-cue shift); the resample is on the per-item AANN-LCC
    difference (the headline), which is the construction's net contribution.
    Also returns the component shifts (vs DDC) for the verdict map.
    Returns dict with delta2, ci, component shifts, n."""
    paired = [(i, aann.get(i), lcc.get(i), ddc.get(i)) for i in ids]
    paired = [(i, a, l, d) for (i, a, l, d) in paired
              if a is not None and l is not None and d is not None]
    n = len(paired)
    if n < 2:
        return {"delta2": float("nan"), "ci95": None, "n_items": n,
                "aann_shift": float("nan"), "lexical_cue_shift": float("nan"),
                "p_uni_aann": None, "p_uni_lcc": None, "p_uni_ddc": None}
    keys = [i for (i, _, _, _) in paired]
    a_map = {i: a for (i, a, _, _) in paired}
    l_map = {i: l for (i, _, l, _) in paired}
    d_map = {i: d for (i, _, _, d) in paired}
    p_a = statistics.mean(a_map.values())
    p_l = statistics.mean(l_map.values())
    p_d = statistics.mean(d_map.values())
    delta2 = p_a - p_l                      # = AANN shift - lexical-cue shift
    aann_shift = p_a - p_d
    lex_shift = p_l - p_d
    diffs = {i: a_map[i] - l_map[i] for i in keys}  # per-item Δ² contribution
    rng = random.Random(seed)
    boots = []
    for _ in range(BOOT):
        idx = [rng.randrange(n) for _ in range(n)]
        boots.append(statistics.mean(diffs[keys[j]] for j in idx))
    boots.sort()
    ci = (boots[int(0.025 * BOOT) - 1], boots[int(0.975 * BOOT) - 1])
    return {"delta2": delta2, "ci95": ci, "n_items": n,
            "aann_shift": aann_shift, "lexical_cue_shift": lex_shift,
            "p_uni_aann": p_a, "p_uni_lcc": p_l, "p_uni_ddc": p_d}


def single_contrast_ci(aann, control, ids, seed=SEED):
    """Paired AANN-vs-control single shift (the agreement arm, unchanged from
    v3). Bootstrap CI over items present in BOTH conditions."""
    paired = [(i, aann.get(i), control.get(i)) for i in ids]
    paired = [(i, a, c) for (i, a, c) in paired if a is not None and c is not None]
    n = len(paired)
    if n < 2:
        return float("nan"), None, n, None, None
    diffs = {i: a - c for (i, a, c) in paired}
    keys = [i for (i, _, _) in paired]
    p_a = statistics.mean(a for (_, a, _) in paired)
    p_c = statistics.mean(c for (_, _, c) in paired)
    shift = statistics.mean(diffs.values())
    rng = random.Random(seed)
    boots = []
    for _ in range(BOOT):
        idx = [rng.randrange(n) for _ in range(n)]
        boots.append(statistics.mean(diffs[keys[j]] for j in idx))
    boots.sort()
    ci = (boots[int(0.025 * BOOT) - 1], boots[int(0.975 * BOOT) - 1])
    return shift, ci, n, p_a, p_c


def positive(value, ci):
    """A 'positive' contrast: value >= TAU (inclusive) AND CI lower bound > 0."""
    if value != value:           # NaN
        return False
    return value >= TAU and ci is not None and ci[0] > CI_LOWER_MUST_EXCEED


def headroom_status(p_uni_ddc):
    """Condition N1, pre-headline. PASS <= 0.30; MARGINAL <= 0.50; FAIL > 0.50."""
    if p_uni_ddc is None or p_uni_ddc != p_uni_ddc:
        return "NA"
    if p_uni_ddc <= HEADROOM_TARGET:
        return "PASS"
    if p_uni_ddc <= HEADROOM_CEILING:
        return "MARGINAL"
    return "HEADROOM-FAIL"


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


# ---------------- per-arm indicators ----------------

def paraphrase_chose_unification(row):
    """Map the chosen LETTER back to content. 1 = chose unification, 0 =
    distributive, None = missing."""
    if row["value"] is None:
        return None
    return 1 if row["value"] == row["unification_letter"] else 0


def agreement_chose_was(row):
    if row["value"] is None:
        return None
    return 1 if row["value"] == row["was_letter"] else 0


def nli_affirm(row):
    if row["value"] is None:
        return None
    return 1 if row["value"] == "YES" else 0


def split_by_frame(rows, indicator):
    """rows -> {frame: {id: indicator}} for cond in {aann, ddc, lcc}."""
    out = {"aann": {}, "ddc": {}, "lcc": {}}
    for r in rows:
        out[r["cond"]][r["id"]] = indicator(r)
    return out


def split_aann_control(rows, indicator):
    """rows -> (aann{id:ind}, control{id:ind}) for the two-condition arms."""
    aann, ctrl = {}, {}
    for r in rows:
        (aann if r["cond"] == "aann" else ctrl)[r["id"]] = indicator(r)
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


# ---------------- per-arm double-contrast block ----------------

def double_arm(rows, indicator, ids, label):
    """Compute the headroom (P(uni|DDC)), the component shifts, Δ², and CI for a
    three-frame arm over the given ids."""
    frames = split_by_frame(rows, indicator)
    dc = double_contrast_ci(frames["aann"], frames["lcc"], frames["ddc"], ids)
    return {
        "label": label,
        "p_uni_aann": (None if dc["p_uni_aann"] is None
                       else round(dc["p_uni_aann"], 4)),
        "p_uni_ddc": (None if dc["p_uni_ddc"] is None
                      else round(dc["p_uni_ddc"], 4)),
        "p_uni_lcc": (None if dc["p_uni_lcc"] is None
                      else round(dc["p_uni_lcc"], 4)),
        "aann_shift": (None if dc["aann_shift"] != dc["aann_shift"]
                       else round(dc["aann_shift"], 4)),
        "lexical_cue_shift": (None if dc["lexical_cue_shift"]
                              != dc["lexical_cue_shift"]
                              else round(dc["lexical_cue_shift"], 4)),
        "delta2": (None if dc["delta2"] != dc["delta2"]
                   else round(dc["delta2"], 4)),
        "ci95": (None if dc["ci95"] is None
                 else [round(dc["ci95"][0], 4), round(dc["ci95"][1], 4)]),
        "n_items": dc["n_items"],
        "delta2_positive": positive(dc["delta2"], dc["ci95"]),
        "aann_shift_clears_tau": (dc["aann_shift"] == dc["aann_shift"]
                                  and dc["aann_shift"] >= TAU),
    }


def single_arm(rows, indicator, ids, label):
    """Compute the AANN-vs-control single shift + CI (agreement arm)."""
    aann, ctrl = split_aann_control(rows, indicator)
    shift, ci, n, p_a, p_c = single_contrast_ci(aann, ctrl, ids)
    return {"label": label,
            "shift": None if shift != shift else round(shift, 4),
            "ci95": None if ci is None else [round(ci[0], 4), round(ci[1], 4)],
            "n_items": n, "positive": positive(shift, ci),
            "raw_aann_rate": None if p_a is None else round(p_a, 4),
            "raw_control_rate": None if p_c is None else round(p_c, 4)}


# ---------------- verdict (per model) ----------------

def lexical_cue_artifact(para):
    """LEXICAL-CUE ARTIFACT (Condition N2): the AANN shift clears τ but Δ² < τ
    (or its CI straddles 0) BECAUSE the lexical-cue shift accounts for it.
    Operationally: AANN shift >= τ AND lexical-cue shift >= (AANN shift - τ),
    so the net Δ² fails."""
    a = para["aann_shift"]
    lx = para["lexical_cue_shift"]
    if a is None or lx is None:
        return False
    if para["delta2_positive"]:
        return False                      # the construction's net shift survived
    return a >= TAU and lx >= (a - TAU)


def per_model_verdict(para, agr, nli, headroom):
    """The §6 per-model category, over a Tier-0-passing, headroom-clearing
    model. Headroom gating is applied in assemble(); here we assume the model
    cleared (PASS/MARGINAL)."""
    para_pos = para["delta2_positive"]
    agr_pos = agr["positive"]
    nli_pos = nli["delta2_positive"]
    artifact = lexical_cue_artifact(para)

    if para_pos and nli_pos and agr_pos:
        return ("CONVERGENT-POSITIVE",
                "the construction shifts inferential behaviour, including the "
                "grammaticalized singular reflex, relative to a matched control, "
                "in the direction the published semantics predicts")
    if para_pos and not agr_pos:
        return ("PARAPHRASE-ONLY",
                "shift in paraphrase selection WITHOUT the grammaticalized "
                "reflex (NOT 'draws the unification inference')")
    if para_pos and agr_pos and not nli_pos:
        return ("PARAPHRASE-PLUS-REFLEX-NO-NLI",
                "paraphrase double-contrast and agreement shift positive but the "
                "NLI convergent arm did not confirm; not full convergence")
    if artifact:
        return ("LEXICAL-CUE ARTIFACT",
                "AANN shift clears tau but the double-contrast Δ² does not: the "
                "lexical cue alone accounts for the movement; the paraphrase arm "
                "cannot carry the headline (the imported itemizing cue, not the "
                "AANN construction, moved the reading)")
    return ("NULL",
            "no AANN double-contrast shift off the distributive-default control "
            "at this instrument")


# ---------------- per-model assembly ----------------

def analyze_model(slot, para, para_st, nli, nli_st, agr, agr_st, t0, t0_st):
    res = {"slot": slot, "model": PANEL_NAMES[slot],
           "arm_status": {"paraphrase": para_st, "nli": nli_st,
                          "agreement": agr_st, "tier0": t0_st}}
    res["tier0"] = analyze_tier0(t0, t0_st)
    if not all(st == "ok" for st in (para_st, nli_st, agr_st)):
        return res

    all_ids = list(ITEMS)

    # ---- ARM A: paraphrase double contrast (PRIMARY), full set ----
    res["paraphrase"] = double_arm(
        para, paraphrase_chose_unification, all_ids,
        "Δ² = P(uni|AANN) - P(uni|LCC) [double contrast, net of lexical cue]")
    # under-pressure subset (distributive locally-fluent), separate
    res["paraphrase_under_pressure"] = double_arm(
        para, paraphrase_chose_unification, list(UNDER_PRESSURE),
        "under-pressure subset (distributive locally-fluent): paraphrase Δ²")
    # disputed-coding sensitivity (Condition I6): headline excluding flags
    res["paraphrase_excl_disputed"] = double_arm(
        para, paraphrase_chose_unification,
        [i for i in all_ids if i not in DISPUTED],
        "paraphrase Δ² excluding item-level disputed-key items")

    # ---- HEADROOM-PRECONDITION GATE (Condition N1, read PRE-HEADLINE) ----
    p_uni_ddc = res["paraphrase"]["p_uni_ddc"]
    res["headroom"] = {
        "p_uni_ddc": p_uni_ddc,
        "status": headroom_status(p_uni_ddc),
        "target_le": HEADROOM_TARGET, "ceiling_le": HEADROOM_CEILING,
        "note": ("PASS: DDC reads distributive at baseline, AANN has headroom"
                 if headroom_status(p_uni_ddc) == "PASS"
                 else "MARGINAL: reduced-headroom caveat mandatory"
                 if headroom_status(p_uni_ddc) == "MARGINAL"
                 else "HEADROOM-FAIL: DDC still reads unification at/near "
                      "ceiling; the v3 cause is NOT removed for this model; "
                      "paraphrase/NLI numbers reported descriptively only and "
                      "EXCLUDED from the headline"),
    }

    # ---- ARM B: NLI double contrast (CONVERGENT), unification + whole-eval ----
    nli_uw = [r for r in nli if r["hyp_key"] in ("unification_hyp",
                                                 "whole_eval_hyp")]
    res["nli"] = double_arm(
        nli_uw, nli_affirm, all_ids,
        "NLI Δ² = affirm(AANN) - affirm(LCC) [unification + whole-eval hyps]")
    # NLI's own DDC-baseline check (reported alongside; NOT gating the primary)
    res["nli_headroom"] = {
        "affirm_ddc": res["nli"]["p_uni_ddc"],
        "status": headroom_status(res["nli"]["p_uni_ddc"]),
        "note": "reported alongside; the FC headroom gate governs the primary",
    }

    # ---- AGREEMENT sub-probe (LOAD-BEARING; control = BARE PLURAL, N4) ----
    res["agreement"] = single_arm(
        agr, agreement_chose_was, all_ids,
        "P(was|AANN) - P(was|bare-plural control) [singular reflex; single "
        "contrast]")

    # ---- named disagreement |FC Δ² - NLI Δ²| (Condition I7) ----
    fc, nl = res["paraphrase"]["delta2"], res["nli"]["delta2"]
    disagree = (None if fc is None or nl is None else round(abs(fc - nl), 4))
    res["instrument_disagreement"] = {
        "statistic": "|FC Δ² - NLI Δ²|",
        "value": disagree,
        "flag": bool(disagree is not None and disagree >= DISAGREEMENT_MIN),
        "fed_to": "open-question/instrument-sensitivity-constructional-inference",
    }
    if res["instrument_disagreement"]["flag"]:
        res["instrument_fragility_caveat"] = (
            f"mandatory: |FC Δ² - NLI Δ²| = {disagree} >= {DISAGREEMENT_MIN}; "
            f"this model's inferential read is instrument-fragile (fed to the "
            f"instrument-sensitivity open question), never averaged away "
            f"(PREREG)")

    # ---- per-model category (verdict map §6) ----
    cat, note = per_model_verdict(res["paraphrase"], res["agreement"],
                                  res["nli"], res["headroom"])
    res["category"] = cat
    res["headline"] = note
    res["convergent_positive"] = bool(cat == "CONVERGENT-POSITIVE")

    # ---- disputed-coding category sensitivity (Condition I6) ----
    para_pos = res["paraphrase"]["delta2_positive"]
    para_pos_excl = res["paraphrase_excl_disputed"]["delta2_positive"]
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
            "is not settled where flagged (Condition I6); result page must carry "
            "this sentence.")
    return res


# ---------------- overall verdict ----------------

def stratum_verdict(categories):
    """Over Tier-0-passing, headroom-clearing models. PREREG frozen §6 map."""
    n_conv = sum(c == "CONVERGENT-POSITIVE" for c in categories)
    n_para = sum(c in ("PARAPHRASE-ONLY", "PARAPHRASE-PLUS-REFLEX-NO-NLI",
                       "CONVERGENT-POSITIVE")
                 for c in categories)
    n_artifact = sum(c == "LEXICAL-CUE ARTIFACT" for c in categories)
    if n_conv >= 2:
        return ("SUPPORTED (inferential half)",
                ">=2 models CONVERGENT-POSITIVE")
    if n_para >= 2:
        return ("PARTIAL (paraphrase/constructional shift without full "
                "convergence)",
                ">=2 reach paraphrase double-contrast positivity but <2 "
                "CONVERGENT-POSITIVE")
    if n_artifact >= 2:
        return ("LEXICAL-CUE ARTIFACT",
                ">=2 models LEXICAL-CUE ARTIFACT: the apparent shift is the "
                "imported cue, not the construction; the double contrast did "
                "its job. A first-class outcome.")
    return ("NULL (no AANN double-contrast inferential shift at this instrument)",
            "<2 models reach even paraphrase positivity and not a lexical-cue "
            "artifact; a first-class null.")


def assemble(per_model):
    incomplete = [f"{s}/{arm}:{st}" for s, r in per_model.items()
                  for arm, st in r["arm_status"].items() if st != "ok"]
    out = {
        "run": "2026-06-13-aann-inferential-v4",
        "design": "experiments/designs/aann-construction-v4-inferential.md",
        "anchor": "internal-contrast-only",
        "chief_cost_statement": CHIEF_COST,
        "expected_inference_key_provenance": KEY_PROVENANCE,
        "primary_instrument": "A (paraphrase forced-choice, double contrast Δ²)",
        "headline_statistic": "Δ² = P(uni|AANN) - P(uni|LCC)",
        "thresholds": {"tau_delta2_inclusive": TAU,
                       "ci_lower_strictly_above": CI_LOWER_MUST_EXCEED,
                       "headroom_pass_le": HEADROOM_TARGET,
                       "headroom_ceiling_le": HEADROOM_CEILING,
                       "tier0_min_inclusive_of_24": TIER0_MIN,
                       "disagreement_flag_min_inclusive": DISAGREEMENT_MIN},
        "models": per_model,
        "cost": read_cost_log(),
    }
    if incomplete:
        out["verdict"] = "INCOMPLETE (required arm missing/partial)"
        out["incomplete_arms"] = incomplete
        return out

    # ---- Tier-0 stratum ----
    passers = [s for s in ("A", "B", "C") if per_model[s]["tier0"].get("pass")]
    excluded_t0 = [s for s in ("A", "B", "C") if s not in passers]
    out["tier0_passers"] = passers
    if excluded_t0:
        out["tier0_excluded_models"] = excluded_t0
        out["tier0_exclusion_note"] = (
            "Tier-0 failure = instrument failure for the model: its inferential "
            "category is reported descriptively only and is EXCLUDED from the "
            ">=2-of-3 stratum count (Condition I7)")
    if len(passers) < 2:
        out["verdict"] = ("INSTRUMENT FAILURE (fewer than 2 Tier-0 passers; no "
                          "substantive inferential verdict)")
        return out

    # ---- HEADROOM WHOLE-DESIGN GATE (Condition N1/N6), read PRE-HEADLINE ----
    # Among Tier-0 passers, which clear the headroom precondition (PASS/MARGINAL)?
    headroom_clearing = [s for s in passers
                         if per_model[s]["headroom"]["status"]
                         in ("PASS", "MARGINAL")]
    headroom_failed = [s for s in passers
                       if per_model[s]["headroom"]["status"] == "HEADROOM-FAIL"]
    out["headroom_clearing_models"] = headroom_clearing
    out["headroom_failed_models"] = headroom_failed
    out["headroom_summary"] = {s: per_model[s]["headroom"]["status"]
                               for s in passers}
    if len(headroom_clearing) < 2:
        out["verdict"] = (
            "HEADROOM-FAIL -> OPTION-B NAMED NULL: fewer than 2 Tier-0-passing "
            "models clear the headroom precondition (P(uni|DDC) off-ceiling). "
            "The distributive-default control did NOT give the construction "
            "headroom at this instrument; the v3 cause is NOT removed. Record "
            "the inferential half as terminally untestable-at-paraphrase-"
            "instrument for AANN and REDIRECT to Option B (the cancel-direction "
            "/ conative route), per the governing decision's binding fallback.")
        out["option_b_redirect"] = (
            "result/conative-minimal-pair-divergence-v1 shows the "
            "cancel-direction route works; the inferential question moves there.")
        return out

    # ---- substantive verdict over headroom-clearing models only ----
    cats = [per_model[s]["category"] for s in headroom_clearing]
    verdict, basis = stratum_verdict(cats)
    out["verdict"] = verdict
    out["verdict_basis"] = basis
    out["verdict_over_models"] = headroom_clearing
    # carry the marginal-headroom caveat into the verdict if any clearing model
    # is MARGINAL
    marg = [s for s in headroom_clearing
            if per_model[s]["headroom"]["status"] == "MARGINAL"]
    if marg:
        out["marginal_headroom_caveat"] = (
            f"models {marg} cleared the headroom precondition only MARGINALLY "
            f"(0.30 < P(uni|DDC) <= 0.50); their numbers carry a mandatory "
            f"reduced-headroom caveat (Condition N1).")
    return out


def report(out):
    print("== AANN inferential v4 — FROZEN PREREG analysis (double contrast) ==")
    print(f"   anchor: {out['anchor']} | primary: {out['primary_instrument']}")
    print(f"   headline: {out['headline_statistic']}")
    for s in ("A", "B", "C"):
        r = out["models"].get(s, {})
        st = r.get("arm_status", {})
        t0 = r.get("tier0", {})
        if any(v != "ok" for v in st.values()):
            print(f"  {s} ({PANEL_NAMES[s]}): arm status {st}"
                  f" | tier0 {t0.get('aann_preferred')}/24 "
                  f"({'PASS' if t0.get('pass') else 'FAIL/NA'})")
            continue
        p = r["paraphrase"]
        hr = r["headroom"]
        print(f"  {s} ({r['model']}): tier0 {t0['aann_preferred']}/24 "
              f"({'PASS' if t0['pass'] else 'FAIL -> excluded'})")
        print(f"     HEADROOM (pre-headline): P(uni|DDC) = {hr['p_uni_ddc']} "
              f"-> {hr['status']}")
        print(f"     A paraphrase: P(uni) AANN/DDC/LCC = {p['p_uni_aann']}/"
              f"{p['p_uni_ddc']}/{p['p_uni_lcc']}")
        print(f"       AANN shift {p['aann_shift']}, lexical-cue shift "
              f"{p['lexical_cue_shift']}, Δ² = {p['delta2']} CI {p['ci95']} "
              f"(pos={p['delta2_positive']})")
        print(f"       under-pressure Δ² = "
              f"{r['paraphrase_under_pressure']['delta2']} "
              f"(n={r['paraphrase_under_pressure']['n_items']})")
        print(f"     B NLI Δ² = {r['nli']['delta2']} CI {r['nli']['ci95']} "
              f"(pos={r['nli']['delta2_positive']})")
        print(f"     AGREEMENT shift = {r['agreement']['shift']} "
              f"CI {r['agreement']['ci95']} (pos={r['agreement']['positive']}) "
              f"[load-bearing discriminator]")
        print(f"     |FC Δ² - NLI Δ²| = {r['instrument_disagreement']['value']} "
              f"(flag={r['instrument_disagreement']['flag']})")
        print(f"     category: {r['category']}  -> {r['headline']}")
    print(f"  HEADROOM summary: {out.get('headroom_summary')}")
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

def _para_rows(p_uni_aann, p_uni_ddc, p_uni_lcc, na_aann=()):
    """Synthetic paraphrase rows over the 3 frames. Rates are deterministic 0/1
    per item (so shifts are exact); content mapped through the frozen letter."""
    rows = []
    for it in STIMULI["items"]:
        for cond, rate_ in (("aann", p_uni_aann), ("ddc", p_uni_ddc),
                            ("lcc", p_uni_lcc)):
            if it["id"] in na_aann and cond == "aann":
                val = None
            else:
                uni_letter = it["fc_letter_unification"]
                val = uni_letter if rate_ else ("B" if uni_letter == "A"
                                                else "A")
            rows.append({"id": it["id"], "arm": "paraphrase", "cond": cond,
                         "unification_letter": it["fc_letter_unification"],
                         "raw": str(val), "value": val, "usage": None,
                         "error": None})
    return rows


def _nli_rows(aff_aann, aff_ddc, aff_lcc):
    rows = []
    for it in STIMULI["items"]:
        for hyp_key in ("unification_hyp", "whole_eval_hyp"):
            for cond, aff in (("aann", aff_aann), ("ddc", aff_ddc),
                              ("lcc", aff_lcc)):
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

    # ---- double-contrast math + positivity
    dc = double_contrast_ci({i: 1 for i in ITEMS}, {i: 0 for i in ITEMS},
                            {i: 0 for i in ITEMS}, list(ITEMS))
    check("clean Δ²=+1 (AANN 1, LCC 0, DDC 0)",
          abs(dc["delta2"] - 1.0) < 1e-9 and dc["n_items"] == len(ITEMS))
    check("Δ²=+1 positive", positive(dc["delta2"], dc["ci95"]))
    check("AANN shift +1, lexical-cue shift 0 -> Δ²=+1 net",
          abs(dc["aann_shift"] - 1.0) < 1e-9
          and abs(dc["lexical_cue_shift"]) < 1e-9)
    # lexical-cue-artifact case: AANN moves a lot, but the LCC moves just as much
    dc2 = double_contrast_ci({i: 1 for i in ITEMS}, {i: 1 for i in ITEMS},
                             {i: 0 for i in ITEMS}, list(ITEMS))
    check("artifact shape: AANN 1, LCC 1, DDC 0 -> Δ²=0, not positive",
          abs(dc2["delta2"]) < 1e-9 and not positive(dc2["delta2"], dc2["ci95"])
          and abs(dc2["aann_shift"] - 1.0) < 1e-9
          and abs(dc2["lexical_cue_shift"] - 1.0) < 1e-9)
    # small Δ² below TAU
    half = list(ITEMS)
    n_below = int(TAU * len(half))   # floor(0.20*23)=4 -> 4/23=0.174 < TAU
    a = {i: (1 if k2 < n_below else 0) for k2, i in enumerate(half)}
    l = {i: 0 for i in half}
    d = {i: 0 for i in half}
    dcs = double_contrast_ci(a, l, d, half)
    check(f"Δ² {n_below}/{len(half)} (~{n_below/len(half):.3f}) < TAU not pos",
          not positive(dcs["delta2"], dcs["ci95"]))

    # ---- headroom gate
    check("headroom PASS at 0.30", headroom_status(0.30) == "PASS")
    check("headroom PASS at 0.10", headroom_status(0.10) == "PASS")
    check("headroom MARGINAL at 0.45", headroom_status(0.45) == "MARGINAL")
    check("headroom FAIL at 0.60", headroom_status(0.60) == "HEADROOM-FAIL")
    check("headroom FAIL at 0.51", headroom_status(0.51) == "HEADROOM-FAIL")

    # ---- lexical-cue-artifact detector
    para_art = double_arm(_para_rows(1, 0, 1), paraphrase_chose_unification,
                          list(ITEMS), "x")
    check("lexical_cue_artifact() fires on AANN1/DDC0/LCC1",
          lexical_cue_artifact(para_art))
    para_clean = double_arm(_para_rows(1, 0, 0), paraphrase_chose_unification,
                            list(ITEMS), "x")
    check("lexical_cue_artifact() does NOT fire on a clean Δ²",
          not lexical_cue_artifact(para_clean))

    # ---- Tier-0 gate (unchanged from v3)
    check("tier0 20/24 passes", analyze_tier0(_tier0_rows(20), "ok")["pass"])
    check("tier0 19/24 fails", not analyze_tier0(_tier0_rows(19), "ok")["pass"])
    check("tier0 >25% missing = instrument failure",
          not analyze_tier0(_tier0_rows(17, 7), "ok")["pass"]
          and analyze_tier0(_tier0_rows(17, 7), "ok")["missingness"]
          == "instrument-failure")

    # ---- SCENARIO (i): clean CONVERGENT-POSITIVE -------------------------------
    # high P(uni|AANN), low DDC (headroom PASS), low LCC, big agreement shift.
    perA = analyze_model(
        "A", _para_rows(1, 0, 0), "ok", _nli_rows(1, 0, 0), "ok",
        _agr_rows(1, 0), "ok", _tier0_rows(24), "ok")
    check("(i) A headroom PASS (DDC=0)", perA["headroom"]["status"] == "PASS")
    check("(i) A paraphrase Δ²=+1 positive",
          perA["paraphrase"]["delta2"] == 1.0
          and perA["paraphrase"]["delta2_positive"])
    check("(i) A NLI Δ²=+1 positive", perA["nli"]["delta2_positive"])
    check("(i) A agreement +1 positive (discriminator)",
          perA["agreement"]["positive"])
    check("(i) A category CONVERGENT-POSITIVE",
          perA["category"] == "CONVERGENT-POSITIVE")

    # PARAPHRASE-ONLY: clean Δ² but agreement null
    perB = analyze_model(
        "B", _para_rows(1, 0, 0), "ok", _nli_rows(0, 0, 0), "ok",
        _agr_rows(0, 0), "ok", _tier0_rows(22), "ok")
    check("B agreement null -> not positive", not perB["agreement"]["positive"])
    check("B category PARAPHRASE-ONLY (agreement gates headline)",
          perB["category"] == "PARAPHRASE-ONLY"
          and "WITHOUT the grammaticalized reflex" in perB["headline"])

    # LEXICAL-CUE ARTIFACT model
    perART = analyze_model(
        "C", _para_rows(1, 0, 1), "ok", _nli_rows(1, 0, 1), "ok",
        _agr_rows(0, 0), "ok", _tier0_rows(24), "ok")
    check("artifact model: headroom PASS but Δ²=0",
          perART["headroom"]["status"] == "PASS"
          and perART["paraphrase"]["delta2"] == 0.0)
    check("artifact model category LEXICAL-CUE ARTIFACT",
          perART["category"] == "LEXICAL-CUE ARTIFACT")

    # NULL model: AANN doesn't move off DDC at all
    perNULL = analyze_model(
        "C", _para_rows(0, 0, 0), "ok", _nli_rows(0, 0, 0), "ok",
        _agr_rows(0, 0), "ok", _tier0_rows(24), "ok")
    check("null model category NULL", perNULL["category"] == "NULL")

    # ---- stratum: 2 convergent-positive -> SUPPORTED
    out_supported = assemble({"A": perA, "B": analyze_model(
        "B", _para_rows(1, 0, 0), "ok", _nli_rows(1, 0, 0), "ok",
        _agr_rows(1, 0), "ok", _tier0_rows(24), "ok"), "C": perNULL})
    check("(i) stratum 2 convergent-positive -> SUPPORTED",
          out_supported["verdict"].startswith("SUPPORTED")
          and out_supported["headroom_clearing_models"] == ["A", "B", "C"])

    # ---- SCENARIO (ii): HEADROOM-FAIL (DDC P(uni) > 0.5) -----------------------
    # DDC reads unification at ceiling for every model -> whole-design gate fires.
    perHF_A = analyze_model(
        "A", _para_rows(1, 1, 1), "ok", _nli_rows(1, 1, 1), "ok",
        _agr_rows(1, 0), "ok", _tier0_rows(24), "ok")
    perHF_B = analyze_model(
        "B", _para_rows(1, 1, 1), "ok", _nli_rows(1, 1, 1), "ok",
        _agr_rows(1, 0), "ok", _tier0_rows(24), "ok")
    perHF_C = analyze_model(
        "C", _para_rows(1, 1, 1), "ok", _nli_rows(1, 1, 1), "ok",
        _agr_rows(1, 0), "ok", _tier0_rows(24), "ok")
    check("(ii) per-model headroom = HEADROOM-FAIL (DDC=1.0)",
          perHF_A["headroom"]["status"] == "HEADROOM-FAIL")
    out_hf = assemble({"A": perHF_A, "B": perHF_B, "C": perHF_C})
    check("(ii) whole-design HEADROOM-FAIL -> OPTION-B NAMED NULL",
          out_hf["verdict"].startswith("HEADROOM-FAIL")
          and "OPTION-B" in out_hf["verdict"]
          and "option_b_redirect" in out_hf)
    check("(ii) all three Tier-0 passers but 0 clear headroom",
          out_hf["tier0_passers"] == ["A", "B", "C"]
          and out_hf["headroom_clearing_models"] == [])

    # ---- MARGINAL headroom path: DDC ~0.43 (>0.30, <=0.50) -> caveat carried
    # build a DDC rate between thresholds: set 10/23 items uni in DDC ~0.435
    def _para_marginal():
        rows = []
        for k, it in enumerate(STIMULI["items"]):
            ddc_uni = 1 if k < 10 else 0     # 10/23 ~ 0.435 -> MARGINAL
            for cond, r_ in (("aann", 1), ("ddc", ddc_uni), ("lcc", 0)):
                uni_letter = it["fc_letter_unification"]
                val = uni_letter if r_ else ("B" if uni_letter == "A" else "A")
                rows.append({"id": it["id"], "arm": "paraphrase", "cond": cond,
                             "unification_letter": uni_letter, "raw": str(val),
                             "value": val, "usage": None, "error": None})
        return rows
    perMARG = analyze_model("A", _para_marginal(), "ok", _nli_rows(1, 0, 0), "ok",
                            _agr_rows(1, 0), "ok", _tier0_rows(24), "ok")
    check("MARGINAL headroom status (0.30<P(uni|DDC)<=0.50)",
          perMARG["headroom"]["status"] == "MARGINAL")
    out_marg = assemble({"A": perMARG, "B": perA, "C": perNULL})
    check("MARGINAL model still counts toward verdict + caveat carried",
          "marginal_headroom_caveat" in out_marg
          and "A" in out_marg["headroom_clearing_models"])

    # ---- INSTRUMENT FAILURE: <2 Tier-0 passers
    out_if = assemble({"A": analyze_model("A", _para_rows(1, 0, 0), "ok",
                                          _nli_rows(1, 0, 0), "ok",
                                          _agr_rows(1, 0), "ok",
                                          _tier0_rows(19), "ok"),
                       "B": perB,
                       "C": analyze_model("C", _para_rows(0, 0, 0), "ok",
                                          _nli_rows(0, 0, 0), "ok",
                                          _agr_rows(0, 0), "ok",
                                          _tier0_rows(19), "ok")})
    check("<2 tier0 passers -> INSTRUMENT FAILURE",
          out_if["verdict"].startswith("INSTRUMENT FAILURE"))

    # ---- INCOMPLETE path
    out_inc = assemble({"A": {"slot": "A", "model": PANEL_NAMES["A"],
                              "arm_status": {"paraphrase": "absent", "nli": "ok",
                                             "agreement": "ok", "tier0": "ok"},
                              "tier0": {"arm_status": "ok"}},
                        "B": perB, "C": perNULL})
    check("absent arm -> INCOMPLETE", out_inc["verdict"].startswith("INCOMPLETE"))

    # ---- |FC - NLI| disagreement flag
    perDIS = analyze_model(
        "A", _para_rows(1, 0, 0), "ok", _nli_rows(0, 0, 0), "ok",
        _agr_rows(1, 0), "ok", _tier0_rows(24), "ok")
    check("|FC Δ² - NLI Δ²| = 1.0 flags disagreement + caveat",
          perDIS["instrument_disagreement"]["value"] == 1.0
          and perDIS["instrument_disagreement"]["flag"]
          and "instrument_fragility_caveat" in perDIS)

    # ---- under-pressure subset + disputed sensitivity present
    check("under-pressure Δ² computed (n matches stimuli)",
          perA["paraphrase_under_pressure"]["n_items"] == len(UNDER_PRESSURE))
    check("disputed sensitivity block present",
          "disputed_sensitivity" in perA
          and perA["disputed_sensitivity"]["n_disputed_excluded"]
          == len(DISPUTED))

    # ---- determinism + serializable
    c1 = double_contrast_ci({i: 1 for i in ITEMS}, {i: 0 for i in ITEMS},
                            {i: 0 for i in ITEMS}, list(ITEMS))["ci95"]
    c2 = double_contrast_ci({i: 1 for i in ITEMS}, {i: 0 for i in ITEMS},
                            {i: 0 for i in ITEMS}, list(ITEMS))["ci95"]
    check("bootstrap CI deterministic under frozen seed", c1 == c2)
    check("summary JSON-serializable", bool(json.dumps(out_supported)))

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
