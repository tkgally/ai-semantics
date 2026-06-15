#!/usr/bin/env python3
"""analyze.py — frozen analysis for the conative preference/commitment double
contrast (run 2026-06-15-conative-preference-commitment-v1). NO model calls.

Implements experiments/designs/conative-preference-commitment-v1.md §4-§6 exactly;
no tunable knobs. Written + committed at FREEZE TIME, before any model call
(probe.py refuses to run if this file is absent).

THE DECISION RULE (baked in; design §4-§6)
------------------------------------------
Per model, per arm, over the matched item families:
  preference (Arm 1, paraphrase FC):  P(cancel-pref) on conative / resist / transitive
  commitment (Arm 2, NLI):            P(withhold = NLI != 0) on conative / resist / transitive

Component shifts (reported in full, design §4):
  conative shift = P(·|conative) - P(·|transitive_conative)
  resist  shift  = P(·|resist)   - P(·|transitive_resist)

HEADLINE = double contrast Δ² (conative minus resist, net of the bare-at cue):
  Δ²_pref   = P(cancel-pref | conative) - P(cancel-pref | resist)
  Δ²_commit = P(withhold    | conative) - P(withhold    | resist)
A double contrast is "positive" iff Δ² >= TAU (=0.20) AND item-level bootstrap
95% CI lower bound > 0 (10,000 resamples, seed 20260615).

HEADROOM GATE (design §5; conative-translated), pre-headline, per model:
  PASS iff P(NLI=entailment | transitive_conative) >= 0.85
       AND P(paraphrase = D | transitive_conative)  >= 0.85.
  Whole-design: >= 2 of 3 models clear, else HEADROOM-FAIL -> route to Option-B.

VERDICT MAP (design §6), per model:
  CONVERGENT-POSITIVE   Δ²_pref positive AND Δ²_commit positive
  PARAPHRASE-ONLY       Δ²_pref positive, Δ²_commit NOT positive
  COMMITMENT-ONLY       Δ²_commit positive, Δ²_pref NOT positive (anomaly)
  LEXICAL-CUE ARTIFACT  a raw conative shift exists but Δ² not positive on either arm
  NULL                  no shift on either arm
  HEADROOM-FAIL         transitive contact default off-ceiling for that model

Panel-level (design §6): CONFIRM / FALSIFY-convergence / FALSIFY-null / INCONCLUSIVE.

FROZEN THRESHOLDS (fixed pre-data; not tunable):
  TAU = 0.20 (inclusive); CI lower bound strictly > 0; 10,000 resamples seed 20260615;
  headroom ceiling 0.85 (inclusive); whole-design gate >= 2 of 3 clear.

Selftest: python3 analyze.py --selftest (synthetic in-memory; no files, no calls).
"""
import argparse
import json
import random
import re
import statistics
from pathlib import Path

HERE = Path(__file__).parent
STIMULI = json.load(open(HERE / "stimuli.json"))
ITEMS = {it["item_id"]: it for it in STIMULI["items"]}

# stems present in BOTH a transitive and an at-frame family (the minimal-pair keys
# the double contrast resamples over). Conative stems and resist stems are distinct
# pools (verb classes differ by necessity, design §2).
CONATIVE_STEMS = sorted({it["stem"] for it in STIMULI["items"]
                         if it["verb_class"] == "conative"})
RESIST_STEMS = sorted({it["stem"] for it in STIMULI["items"]
                       if it["verb_class"] == "resist"})

BOOT = 10000
SEED = 20260615
TAU = 0.20                  # double-contrast threshold, inclusive (>=)
CI_LOWER_MUST_EXCEED = 0.0  # strict (>)
HEADROOM_MIN = 0.85         # PASS >= 0.85 (inclusive), both indicators
WHOLE_DESIGN_MIN_CLEAR = 2  # >= 2 of 3 models clear, else route-to-Option-B

PANEL_NAMES = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini",
               "C": "gemini-3.5-flash"}

EXPECTED_ROWS = {"paraphrase": len(ITEMS), "nli": len(ITEMS)}  # 40 each


# ---------------- statistics ----------------

def _mean(vals):
    present = [v for v in vals if v is not None]
    return statistics.mean(present) if present else None


def family_rate(per_item):
    """Mean of present 0/1 indicators in a {stem: 0/1/None} map (a family rate)."""
    return _mean(list(per_item.values()))


def double_contrast_ci(target, control, t_stems, c_stems, seed=SEED):
    """Δ² = P(·|target/conative) - P(·|control/resist).

    The conative and resist verb pools are DISJOINT (different verbs by necessity,
    design §2), so the resample is a TWO-SAMPLE item-level bootstrap: resample the
    conative stems and the resist stems independently and take the difference of
    their family means. Returns delta2, ci95, the two family rates, and n's."""
    tvals = {s: target.get(s) for s in t_stems if target.get(s) is not None}
    cvals = {s: control.get(s) for s in c_stems if control.get(s) is not None}
    nt, nc = len(tvals), len(cvals)
    if nt < 2 or nc < 2:
        return {"delta2": float("nan"), "ci95": None,
                "p_target": (statistics.mean(tvals.values()) if tvals else None),
                "p_control": (statistics.mean(cvals.values()) if cvals else None),
                "n_target": nt, "n_control": nc}
    p_t = statistics.mean(tvals.values())
    p_c = statistics.mean(cvals.values())
    delta2 = p_t - p_c
    tk, ck = list(tvals), list(cvals)
    rng = random.Random(seed)
    boots = []
    for _ in range(BOOT):
        bt = statistics.mean(tvals[tk[rng.randrange(nt)]] for _ in range(nt))
        bc = statistics.mean(cvals[ck[rng.randrange(nc)]] for _ in range(nc))
        boots.append(bt - bc)
    boots.sort()
    ci = (boots[int(0.025 * BOOT) - 1], boots[int(0.975 * BOOT) - 1])
    return {"delta2": delta2, "ci95": ci, "p_target": p_t, "p_control": p_c,
            "n_target": nt, "n_control": nc}


def positive(value, ci):
    """Positive contrast: value >= TAU (inclusive) AND CI lower bound > 0 (strict)."""
    if value != value:  # NaN
        return False
    return value >= TAU and ci is not None and ci[0] > CI_LOWER_MUST_EXCEED


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

def paraphrase_chose_cancel(row):
    """1 = chose the cancel reading C, 0 = default D, None = missing.
    Maps the chosen LETTER back to content via the item's cancel_letter."""
    if row["value"] is None:
        return None
    return 1 if row["value"] == row["cancel_letter"] else 0


def paraphrase_chose_default(row):
    """1 = chose the default reading D (the headroom indicator), 0 = cancel."""
    if row["value"] is None:
        return None
    return 1 if row["value"] == row["default_letter"] else 0


def nli_withhold(row):
    """1 = withholds the contact entailment (NLI != 0), 0 = affirms (NLI == 0)."""
    if row["value"] is None:
        return None
    return 1 if row["value"] != "0" else 0


def nli_entailment(row):
    """1 = NLI == 0 (entailment / affirms contact), the headroom indicator."""
    if row["value"] is None:
        return None
    return 1 if row["value"] == "0" else 0


def by_family(rows, indicator):
    """rows -> {family: {stem: indicator}}."""
    out = {}
    for r in rows:
        out.setdefault(r["family"], {})[r["stem"]] = indicator(r)
    return out


# ---------------- per-arm double-contrast block ----------------

def arm_block(rows, cancel_ind, default_ind, label):
    """Compute, for one arm: the per-family rates, the component shifts, the
    headline Δ² (conative - resist) + CI, and the headroom indicator on
    transitive_conative (P(default-reading | transitive_conative))."""
    fam_cancel = by_family(rows, cancel_ind)
    fam_default = by_family(rows, default_ind)

    p_conative = family_rate(fam_cancel.get("conative", {}))
    p_resist = family_rate(fam_cancel.get("resist", {}))
    p_tc = family_rate(fam_cancel.get("transitive_conative", {}))
    p_tr = family_rate(fam_cancel.get("transitive_resist", {}))

    conative_shift = (None if p_conative is None or p_tc is None
                      else p_conative - p_tc)
    resist_shift = (None if p_resist is None or p_tr is None
                    else p_resist - p_tr)

    dc = double_contrast_ci(fam_cancel.get("conative", {}),
                            fam_cancel.get("resist", {}),
                            CONATIVE_STEMS, RESIST_STEMS)

    # headroom indicator for this arm = default-reading rate on transitive_conative
    headroom_rate = family_rate(fam_default.get("transitive_conative", {}))

    return {
        "label": label,
        "p_cancelpref_conative": _round(p_conative),
        "p_cancelpref_resist": _round(p_resist),
        "p_cancelpref_transitive_conative": _round(p_tc),
        "p_cancelpref_transitive_resist": _round(p_tr),
        "conative_shift": _round(conative_shift),
        "resist_shift": _round(resist_shift),
        "delta2": _round(dc["delta2"]),
        "ci95": (None if dc["ci95"] is None
                 else [round(dc["ci95"][0], 4), round(dc["ci95"][1], 4)]),
        "n_conative": dc["n_target"], "n_resist": dc["n_control"],
        "delta2_positive": positive(dc["delta2"], dc["ci95"]),
        "headroom_default_rate_transitive_conative": _round(headroom_rate),
    }


def _round(x):
    if x is None:
        return None
    if x != x:  # NaN
        return None
    return round(x, 4)


# ---------------- headroom gate (design §5) ----------------

def headroom_status(p_nli_entail_tc, p_para_default_tc):
    """PASS iff BOTH >= 0.85 (inclusive). Else HEADROOM-FAIL."""
    if p_nli_entail_tc is None or p_para_default_tc is None:
        return "NA"
    if p_nli_entail_tc >= HEADROOM_MIN and p_para_default_tc >= HEADROOM_MIN:
        return "PASS"
    return "HEADROOM-FAIL"


# ---------------- per-model verdict (design §6) ----------------

def per_model_verdict(pref, commit):
    """The §6 per-model category. Assumes the model cleared headroom (gated in
    assemble()). LEXICAL-CUE ARTIFACT = a raw conative shift exists but neither Δ²
    is positive; NULL = no raw conative shift on either arm either."""
    pref_pos = pref["delta2_positive"]
    commit_pos = commit["delta2_positive"]
    if pref_pos and commit_pos:
        return ("CONVERGENT-POSITIVE",
                "the conative shifts BOTH the paraphrase preference and the NLI "
                "commitment more than the matched anomalous at-string (Δ² positive "
                "on both arms)")
    if pref_pos and not commit_pos:
        return ("PARAPHRASE-ONLY",
                "preference without commitment: the conative shifts paraphrase "
                "selection (Δ²_pref positive) but NOT the NLI commitment; reported "
                "as 'preference without commitment', never as 'draws the inference'")
    if commit_pos and not pref_pos:
        return ("COMMITMENT-ONLY",
                "ANOMALY: the conative shifts the NLI commitment (Δ²_commit "
                "positive) but NOT the paraphrase preference; reported as an "
                "anomaly, not folded into a confirm")
    # neither Δ² positive: artifact (raw conative shift exists) vs null (no shift)
    raw_shift = (_nonzero(pref["conative_shift"]) or _nonzero(commit["conative_shift"]))
    if raw_shift:
        return ("LEXICAL-CUE ARTIFACT",
                "a raw conative shift exists but the double contrast (net of the "
                "anomalous at-string) is not positive on either arm: the bare-at "
                "cue, not the licensed conative, moved the reading")
    return ("NULL",
            "no shift on either arm: the conative reads like its transitive; the "
            "antecedent for a dissociation is absent")


def _nonzero(x, eps=1e-9):
    return x is not None and abs(x) > eps


# ---------------- per-model assembly ----------------

def analyze_model(slot, para, para_st, nli, nli_st):
    res = {"slot": slot, "model": PANEL_NAMES[slot],
           "arm_status": {"paraphrase": para_st, "nli": nli_st}}
    if para_st != "ok" or nli_st != "ok":
        return res

    pm, pgate = miss_gate(para)
    nm, ngate = miss_gate(nli)
    res["missingness"] = {"paraphrase": {"missing": pm, "gate": pgate},
                          "nli": {"missing": nm, "gate": ngate}}

    # Arm 1: paraphrase preference (cancel-pref) double contrast
    res["preference"] = arm_block(
        para, paraphrase_chose_cancel, paraphrase_chose_default,
        "Δ²_pref = P(cancel-pref|conative) - P(cancel-pref|resist)")
    # Arm 2: NLI commitment (withhold) double contrast
    res["commitment"] = arm_block(
        nli, nli_withhold, nli_entailment,
        "Δ²_commit = P(withhold|conative) - P(withhold|resist)")

    # ---- HEADROOM GATE (design §5), pre-headline, per model ----
    p_nli_entail_tc = res["commitment"]["headroom_default_rate_transitive_conative"]
    p_para_default_tc = res["preference"]["headroom_default_rate_transitive_conative"]
    res["headroom"] = {
        "p_nli_entailment_transitive_conative": p_nli_entail_tc,
        "p_paraphrase_default_transitive_conative": p_para_default_tc,
        "min_inclusive": HEADROOM_MIN,
        "status": headroom_status(p_nli_entail_tc, p_para_default_tc),
        "note": ("PASS: the transitive contact default is at ceiling on both "
                 "instruments; the conative has room to suppress it"),
    }
    if res["headroom"]["status"] != "PASS":
        res["headroom"]["note"] = (
            "HEADROOM-FAIL: the transitive contact default is NOT at ceiling "
            "(< 0.85 on NLI-entailment and/or paraphrase-default); no room to "
            "read a construction effect; this model's headline is uninterpretable")

    # ---- per-model category (verdict map §6) ----
    cat, note = per_model_verdict(res["preference"], res["commitment"])
    res["category"] = cat
    res["headline"] = note
    res["convergent_positive"] = bool(cat == "CONVERGENT-POSITIVE")
    res["paraphrase_only"] = bool(cat == "PARAPHRASE-ONLY")
    return res


# ---------------- panel-level verdict (design §6) ----------------

def panel_verdict(categories):
    """Over headroom-clearing models. Design §6 symmetric confirm/falsify."""
    n_conv = sum(c == "CONVERGENT-POSITIVE" for c in categories)
    n_para = sum(c == "PARAPHRASE-ONLY" for c in categories)
    n_null = sum(c == "NULL" for c in categories)
    n = len(categories)

    # FALSIFY (convergence): ALL models CONVERGENT-POSITIVE
    if n >= 1 and n_conv == n:
        return ("FALSIFY-convergence",
                "all headroom-clearing models CONVERGENT-POSITIVE (full "
                "cross-instrument convergence): the AANN preference-without-"
                "commitment dissociation does NOT reproduce on the conative; the "
                "dissociation is plausibly AANN-specific")
    # FALSIFY (null): ALL models NULL
    if n >= 1 and n_null == n:
        return ("FALSIFY-null",
                "all headroom-clearing models NULL (no preference shift to "
                "dissociate from): the antecedent is absent for the conative; the "
                "instance falls, the conceptual point survives un-instanced")
    # CONFIRM: the qualitative AANN shape — >=1 CONVERGENT-POSITIVE AND >=1 PARAPHRASE-ONLY
    if n_conv >= 1 and n_para >= 1:
        return ("CONFIRM",
                "the AANN shape reproduces: >=1 model CONVERGENT-POSITIVE and >=1 "
                "PARAPHRASE-ONLY (preference broad, commitment a minority); the "
                "preference-without-commitment dissociation generalizes to the "
                "conative")
    return ("INCONCLUSIVE",
            "the panel does not cleanly match a confirm/falsify shape (no "
            "CONVERGENT-POSITIVE + PARAPHRASE-ONLY pair, and not unanimously "
            "convergent or null)")


def assemble(per_model):
    incomplete = [f"{s}/{arm}:{st}" for s, r in per_model.items()
                  for arm, st in r["arm_status"].items() if st != "ok"]
    out = {
        "run": "2026-06-15-conative-preference-commitment-v1",
        "design": "experiments/designs/conative-preference-commitment-v1.md",
        "anchor": {"nli_conative": "human-anchored (resource/scivetti-2025-cxnli-"
                   "dataset; CxNLI conative gold = non-entailment)",
                   "paraphrase_arm": "internal-contrast-only",
                   "resist_lcc_arm": "internal-contrast-only"},
        "primary_discriminator": "Arm 2 NLI commitment (Δ²_commit); paraphrase is "
                                 "the weaker preference signal",
        "headline_statistics": ["Δ²_pref = P(cancel-pref|conative) - "
                                "P(cancel-pref|resist)",
                                "Δ²_commit = P(withhold|conative) - "
                                "P(withhold|resist)"],
        "thresholds": {"tau_delta2_inclusive": TAU,
                       "ci_lower_strictly_above": CI_LOWER_MUST_EXCEED,
                       "bootstrap_resamples": BOOT, "bootstrap_seed": SEED,
                       "headroom_min_inclusive": HEADROOM_MIN,
                       "whole_design_min_clear_of_3": WHOLE_DESIGN_MIN_CLEAR},
        "models": per_model,
        "cost": read_cost_log(),
    }
    if incomplete:
        out["verdict"] = "INCOMPLETE (required arm missing/partial)"
        out["incomplete_arms"] = incomplete
        return out

    # ---- HEADROOM WHOLE-DESIGN GATE (design §5), pre-headline ----
    clearing = [s for s in ("A", "B", "C")
                if per_model[s]["headroom"]["status"] == "PASS"]
    failed = [s for s in ("A", "B", "C")
              if per_model[s]["headroom"]["status"] != "PASS"]
    out["headroom_clearing_models"] = clearing
    out["headroom_failed_models"] = failed
    out["headroom_summary"] = {s: per_model[s]["headroom"]["status"]
                               for s in ("A", "B", "C")}
    if len(clearing) < WHOLE_DESIGN_MIN_CLEAR:
        out["verdict"] = (
            "HEADROOM-FAIL -> route-to-Option-B: fewer than 2 of 3 models clear "
            "the conative-translated headroom precondition (transitive contact "
            "default off-ceiling). The design's headline does not stand; route to "
            "the Option-B named fallback (way/caused-motion near-miss variant) per "
            "the ratified decision. No retuning.")
        out["option_b_redirect"] = (
            "decisions/resolved/fresh-construction-inferential-generalization "
            "names the Option-B fallback; the inferential question moves there.")
        return out

    # ---- panel verdict over headroom-clearing models only ----
    cats = [per_model[s]["category"] for s in clearing]
    verdict, basis = panel_verdict(cats)
    out["verdict"] = verdict
    out["verdict_basis"] = basis
    out["verdict_over_models"] = clearing
    out["per_model_categories"] = {s: per_model[s]["category"] for s in clearing}
    # the pre-registered anti-cheat note (design §7)
    out["gpt_scoring_note"] = (
        "design §7 (binding anti-cheat): gpt-5.4-mini's PRE-EXISTING conative NLI "
        "fragility must NOT be retrofitted as new confirmation; the converging "
        "model's identity is read from THIS run's data. A genuine CONFIRM needs a "
        "model OTHER than gpt-5.4-mini to converge.")
    return out


def report(out):
    print("== conative preference/commitment v1 — FROZEN analysis (double "
          "contrast Δ²) ==")
    print(f"   anchor: nli={out['anchor']['nli_conative']}")
    print(f"   primary discriminator: {out['primary_discriminator']}")
    for s in ("A", "B", "C"):
        r = out["models"].get(s, {})
        st = r.get("arm_status", {})
        if any(v != "ok" for v in st.values()):
            print(f"  {s} ({PANEL_NAMES[s]}): arm status {st}")
            continue
        pr, cm, hr = r["preference"], r["commitment"], r["headroom"]
        print(f"  {s} ({r['model']}):")
        print(f"     HEADROOM (pre-headline): NLI-entail|trans={hr['p_nli_entailment_transitive_conative']} "
              f"para-default|trans={hr['p_paraphrase_default_transitive_conative']} "
              f"-> {hr['status']}")
        print(f"     PREF  : cancel-pref conative/resist = "
              f"{pr['p_cancelpref_conative']}/{pr['p_cancelpref_resist']} | "
              f"Δ²_pref = {pr['delta2']} CI {pr['ci95']} (pos={pr['delta2_positive']})")
        print(f"     COMMIT: withhold conative/resist = "
              f"{cm['p_cancelpref_conative']}/{cm['p_cancelpref_resist']} | "
              f"Δ²_commit = {cm['delta2']} CI {cm['ci95']} (pos={cm['delta2_positive']})")
        print(f"     category: {r.get('category')}  -> {r.get('headline')}")
    print(f"  HEADROOM summary: {out.get('headroom_summary')}")
    print(f"  VERDICT: {out['verdict']}")
    if out.get("verdict_basis"):
        print(f"           {out['verdict_basis']}")
    print(f"  cost: {out['cost'].get('total_billed_usd')} "
          f"({out['cost'].get('status')})")


def main():
    per = {}
    for slot in ("A", "B", "C"):
        para, ps = load(slot, "paraphrase")
        nli, ns = load(slot, "nli")
        per[slot] = analyze_model(slot, para, ps, nli, ns)
    out = assemble(per)
    json.dump(out, open(HERE / "results.json", "w"), indent=1)
    report(out)


# ---------------- selftest (synthetic; no files, no calls) ----------------

def _para_rows(p_cancel_conative, p_default_trans_con, p_cancel_resist,
               p_default_trans_res):
    """Synthetic paraphrase rows. Rates are deterministic per item (so shifts are
    exact). p_default_trans_* gives the DEFAULT-reading rate on the transitive
    families (the headroom indicator); p_cancel_* gives the CANCEL-reading rate on
    the at-frame families. Content mapped through the frozen counterbalance letter."""
    rows = []
    for it in STIMULI["items"]:
        fam = it["family"]
        if fam == "conative":
            cancel_rate = p_cancel_conative
        elif fam == "resist":
            cancel_rate = p_cancel_resist
        elif fam == "transitive_conative":
            cancel_rate = 1 - p_default_trans_con  # default-rate -> cancel-rate
        else:  # transitive_resist
            cancel_rate = 1 - p_default_trans_res
        val = it["cancel_letter"] if cancel_rate >= 0.5 else it["default_letter"]
        rows.append({"item_id": it["item_id"], "family": fam,
                     "verb_class": it["verb_class"], "stem": it["stem"],
                     "arm": "paraphrase", "cancel_letter": it["cancel_letter"],
                     "default_letter": it["default_letter"],
                     "raw": val, "value": val, "usage": None, "error": None})
    return rows


def _nli_rows(p_withhold_conative, p_entail_trans_con, p_withhold_resist,
              p_entail_trans_res):
    """Synthetic NLI rows. value '0' = entailment (affirm contact), '1' = neutral
    (withhold). Withhold-rate -> emit '1'; affirm -> '0'. For the transitives,
    p_entail_* is the entailment (affirm) rate."""
    rows = []
    for it in STIMULI["items"]:
        fam = it["family"]
        if fam == "conative":
            withhold = p_withhold_conative
        elif fam == "resist":
            withhold = p_withhold_resist
        elif fam == "transitive_conative":
            withhold = 1 - p_entail_trans_con
        else:
            withhold = 1 - p_entail_trans_res
        val = "1" if withhold >= 0.5 else "0"
        rows.append({"item_id": it["item_id"], "family": fam,
                     "verb_class": it["verb_class"], "stem": it["stem"],
                     "arm": "nli", "raw": val, "value": val,
                     "usage": None, "error": None})
    return rows


def selftest():
    failures = []
    n = [0]

    def check(name, cond):
        n[0] += 1
        print(("PASS " if cond else "FAIL ") + name)
        if not cond:
            failures.append(name)

    # ---- double-contrast math + positivity (two-sample)
    tgt = {s: 1 for s in CONATIVE_STEMS}
    ctl = {s: 0 for s in RESIST_STEMS}
    dc = double_contrast_ci(tgt, ctl, CONATIVE_STEMS, RESIST_STEMS)
    check("clean Δ²=+1 (conative 1, resist 0)",
          abs(dc["delta2"] - 1.0) < 1e-9)
    check("Δ²=+1 positive", positive(dc["delta2"], dc["ci95"]))
    dc0 = double_contrast_ci({s: 1 for s in CONATIVE_STEMS},
                             {s: 1 for s in RESIST_STEMS},
                             CONATIVE_STEMS, RESIST_STEMS)
    check("Δ²=0 (conative 1, resist 1) not positive",
          abs(dc0["delta2"]) < 1e-9 and not positive(dc0["delta2"], dc0["ci95"]))
    # below TAU
    nlow = max(1, int(TAU * len(CONATIVE_STEMS) - 1e-9))
    tlow = {s: (1 if k < nlow else 0) for k, s in enumerate(CONATIVE_STEMS)}
    dcl = double_contrast_ci(tlow, {s: 0 for s in RESIST_STEMS},
                             CONATIVE_STEMS, RESIST_STEMS)
    check(f"Δ² {nlow}/{len(CONATIVE_STEMS)} < TAU not positive",
          not positive(dcl["delta2"], dcl["ci95"]))

    # ---- headroom gate
    check("headroom PASS at 0.85/0.85", headroom_status(0.85, 0.85) == "PASS")
    check("headroom FAIL at 0.84/1.0", headroom_status(0.84, 1.0) == "HEADROOM-FAIL")
    check("headroom FAIL at 1.0/0.5", headroom_status(1.0, 0.5) == "HEADROOM-FAIL")

    # ---- SCENARIO (a): clean PARAPHRASE-ONLY -----------------------------------
    # preference Δ² positive (conative cancel-pref high, resist low; transitives at
    # ceiling default), but commitment Δ² null (NLI does not withhold for conative).
    perPO = analyze_model(
        "A",
        _para_rows(p_cancel_conative=1, p_default_trans_con=1,
                   p_cancel_resist=0, p_default_trans_res=1), "ok",
        _nli_rows(p_withhold_conative=0, p_entail_trans_con=1,
                  p_withhold_resist=0, p_entail_trans_res=1), "ok")
    check("(a) PARAPHRASE-ONLY headroom PASS", perPO["headroom"]["status"] == "PASS")
    check("(a) PARAPHRASE-ONLY Δ²_pref positive",
          perPO["preference"]["delta2_positive"])
    check("(a) PARAPHRASE-ONLY Δ²_commit NOT positive",
          not perPO["commitment"]["delta2_positive"])
    check("(a) category == PARAPHRASE-ONLY",
          perPO["category"] == "PARAPHRASE-ONLY")

    # ---- SCENARIO (b): CONVERGENT-POSITIVE -------------------------------------
    perCP = analyze_model(
        "B",
        _para_rows(1, 1, 0, 1), "ok",
        _nli_rows(p_withhold_conative=1, p_entail_trans_con=1,
                  p_withhold_resist=0, p_entail_trans_res=1), "ok")
    check("(b) CONVERGENT headroom PASS", perCP["headroom"]["status"] == "PASS")
    check("(b) Δ²_pref positive", perCP["preference"]["delta2_positive"])
    check("(b) Δ²_commit positive", perCP["commitment"]["delta2_positive"])
    check("(b) category == CONVERGENT-POSITIVE",
          perCP["category"] == "CONVERGENT-POSITIVE")

    # ---- SCENARIO (c): NULL ----------------------------------------------------
    perNULL = analyze_model(
        "C",
        _para_rows(0, 1, 0, 1), "ok",
        _nli_rows(0, 1, 0, 1), "ok")
    check("(c) NULL headroom PASS", perNULL["headroom"]["status"] == "PASS")
    check("(c) Δ²_pref not positive", not perNULL["preference"]["delta2_positive"])
    check("(c) Δ²_commit not positive", not perNULL["commitment"]["delta2_positive"])
    check("(c) category == NULL", perNULL["category"] == "NULL")

    # ---- COMMITMENT-ONLY anomaly
    perCO = analyze_model(
        "A", _para_rows(0, 1, 0, 1), "ok", _nli_rows(1, 1, 0, 1), "ok")
    check("COMMITMENT-ONLY anomaly category",
          perCO["category"] == "COMMITMENT-ONLY")

    # ---- LEXICAL-CUE ARTIFACT: conative AND resist both shift -> Δ² ~ 0
    perART = analyze_model(
        "A", _para_rows(1, 1, 1, 1), "ok", _nli_rows(1, 1, 1, 1), "ok")
    check("artifact: Δ²_pref ~0", abs(perART["preference"]["delta2"]) < 1e-9)
    check("artifact category == LEXICAL-CUE ARTIFACT",
          perART["category"] == "LEXICAL-CUE ARTIFACT")

    # ---- HEADROOM-FAIL: transitive default off-ceiling
    perHF = analyze_model(
        "A", _para_rows(1, 0, 0, 1), "ok", _nli_rows(1, 0, 0, 1), "ok")
    check("headroom-fail status",
          perHF["headroom"]["status"] == "HEADROOM-FAIL")

    # ---- PANEL: CONFIRM (>=1 convergent + >=1 paraphrase-only, all clear headroom)
    out_confirm = assemble({"A": perCP, "B": perPO, "C": perNULL})
    check("panel CONFIRM (convergent + paraphrase-only present)",
          out_confirm["verdict"] == "CONFIRM"
          and out_confirm["headroom_clearing_models"] == ["A", "B", "C"])

    # ---- PANEL: FALSIFY-convergence (all convergent)
    out_fc = assemble({"A": perCP,
                       "B": analyze_model("B", _para_rows(1, 1, 0, 1), "ok",
                                          _nli_rows(1, 1, 0, 1), "ok"),
                       "C": analyze_model("C", _para_rows(1, 1, 0, 1), "ok",
                                          _nli_rows(1, 1, 0, 1), "ok")})
    check("panel FALSIFY-convergence (all convergent)",
          out_fc["verdict"] == "FALSIFY-convergence")

    # ---- PANEL: FALSIFY-null (all null)
    out_fn = assemble({"A": perNULL,
                       "B": analyze_model("B", _para_rows(0, 1, 0, 1), "ok",
                                          _nli_rows(0, 1, 0, 1), "ok"),
                       "C": analyze_model("C", _para_rows(0, 1, 0, 1), "ok",
                                          _nli_rows(0, 1, 0, 1), "ok")})
    check("panel FALSIFY-null (all null)", out_fn["verdict"] == "FALSIFY-null")

    # ---- PANEL: HEADROOM-FAIL whole-design (only 1 clears)
    out_hf = assemble({"A": perCP, "B": perHF,
                       "C": analyze_model("C", _para_rows(1, 0, 0, 1), "ok",
                                          _nli_rows(1, 0, 0, 1), "ok")})
    check("panel HEADROOM-FAIL -> route-to-Option-B",
          out_hf["verdict"].startswith("HEADROOM-FAIL")
          and "option_b_redirect" in out_hf)

    # ---- INCOMPLETE path
    out_inc = assemble({"A": {"slot": "A", "model": PANEL_NAMES["A"],
                              "arm_status": {"paraphrase": "absent", "nli": "ok"}},
                        "B": perPO, "C": perNULL})
    check("absent arm -> INCOMPLETE", out_inc["verdict"].startswith("INCOMPLETE"))

    # ---- determinism + serializable
    c1 = double_contrast_ci(tgt, ctl, CONATIVE_STEMS, RESIST_STEMS)["ci95"]
    c2 = double_contrast_ci(tgt, ctl, CONATIVE_STEMS, RESIST_STEMS)["ci95"]
    check("bootstrap CI deterministic under frozen seed", c1 == c2)
    check("summary JSON-serializable", bool(json.dumps(out_confirm)))

    if failures:
        raise SystemExit(f"SELFTEST FAILED: {failures}")
    print(f"selftest PASS ({n[0]} checks)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
    else:
        main()
