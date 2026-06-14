#!/usr/bin/env python3
"""AANN agreement-reflex generalization v5 — analysis. Implements the FROZEN v5
design + PREREG exactly; no tunable knobs. Written and committed at freeze time,
BEFORE any model call (probe.py refuses to run if this file is absent); a post-run
verifier recomputes from raw with independent code.

THE HEADLINE INSTRUMENT is the v4 agreement arm UNCHANGED: a was/were forced
choice over two conditions per held-out item (aann / bare-plural control). The
indicator is the SINGLE contrast

    agreement shift = P(was|AANN) - P(was|bare-plural control)

per model, with a PREREG-seeded item-level bootstrap CI. This is the same
single-contrast machinery as the v4 agreement arm (single_contrast_ci), just on
fresh HELD-OUT items.

THE FROZEN VERDICT TREE (ordered if/else, baked in below as code; governing
decision: aann-inferential-operationalization §Ratification — the agreement
sub-probe the load-bearing discriminator; v5 reuses that instrument class, NO new
decision):

  Per the reflex-bearing model (gpt-5.4-mini, slot B):
    REPLICATES            if shift >= TAU (=+0.30) AND bootstrap CI-lower > 0
    else FAILS-TO-REPLICATE

  Per claude (A) / gemini (C):
    CEILING-UNINFORMATIVE if control "was"-rate >= CEILING (=0.85)
                          (the discriminator is structurally blind here, as in
                          v3/v4: both AANN and bare-plural pull singular agreement)
    else GENERALIZES-TO-PANEL if shift >= TAU AND CI-lower > 0
    else NO-REFLEX

  Overall verdict (exhaustive, with an explicit final else):
    REFLEX-IS-GPT-SPECIFIC-AND-REPLICATES : gpt REPLICATES and neither other
                                            model GENERALIZES-TO-PANEL
    REFLEX-GENERALIZES-TO-PANEL           : >= 1 of {claude, gemini} GENERALIZES
                                            (whether or not gpt replicates)
    REFLEX-FAILS-TO-REPLICATE             : gpt FAILS-TO-REPLICATE and neither
                                            other model GENERALIZES
    INCONCLUSIVE                          : final else (e.g. a gated-item floor
                                            breach, Tier-0 failure on the
                                            reflex-bearer, or any cell that the
                                            three branches above do not resolve)

The count-noun DIAGNOSTIC arm is DESCRIPTIVE-ONLY and NEVER enters the verdict:
it reports, per model, P(were) on genuine count plurals, to characterise whether
a model that sits at the AANN/quantity ceiling can still pick "were" for an
ordinary count plural (i.e. whether the ceiling is notional-singular-for-quantity
rather than a blanket "always picks was"). analyze.py keeps it out of every
verdict branch by construction.

FROZEN THRESHOLDS (fixed pre-data; baked here, not tunable):
  - replication/generalization bar TAU = +0.30, INCLUSIVE (shift >= +0.30 passes).
  - a positive shift additionally needs bootstrap 95% CI lower bound > 0 (STRICT);
    a degenerate zero-width CI (e.g. all-ceiling cells) carries NO inferential
    weight (it cannot have CI-lower > 0 unless the point shift is itself > 0 with
    spread, so a 0/0 ceiling cell is never "positive").
  - ceiling threshold CEILING = 0.85, INCLUSIVE (control was-rate >= 0.85).
  - bootstrap: 10,000 item-level resamples, seed 20260614, percentile CI.
  - Tier-0 pass >= 10/12 (INCLUSIVE) per model; >25% missing = instrument failure.
  - gated-item floor: each verdict-bearing cell needs >= MIN_ITEMS gated items in
    BOTH conditions; below the floor the cell is INCONCLUSIVE.

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
DIAGNOSTIC = {d["id"]: d for d in STIMULI["diagnostic"]}
TIER0 = {p["id"]: p for p in STIMULI["tier0"]}

_N = len(ITEMS)
EXPECTED_ROWS = {"agreement": 2 * _N, "diagnostic": len(DIAGNOSTIC),
                 "tier0": len(TIER0)}
BOOT = 10000
SEED = 20260614

TAU = 0.30                 # replication / generalization bar, inclusive (>=)
CI_LOWER_MUST_EXCEED = 0.0  # strict (>)
CEILING = 0.85             # control was-rate >= 0.85 => CEILING-UNINFORMATIVE
TIER0_MIN = 10             # inclusive (>=), of 12
MIN_ITEMS = 8              # gated-item floor per verdict-bearing cell (both conds)

PANEL_NAMES = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini",
               "C": "gemini-3.5-flash"}
REFLEX_BEARER = "B"        # gpt-5.4-mini: the +0.74 v3 / +0.65 v4 reflex model

CHIEF_COST = STIMULI["chief_cost_statement"]
KEY_PROVENANCE = STIMULI["expected_agreement_key_provenance"]


# ---------------- statistics ----------------

def single_contrast_ci(aann, control, ids, seed=SEED):
    """Paired AANN-vs-control single shift (the v4 agreement-arm machinery,
    reused unchanged). Bootstrap CI over items present in BOTH conditions.
    Returns (shift, ci, n_items, p_aann, p_control)."""
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
    """A 'positive' shift: value >= TAU (inclusive) AND CI lower bound > 0.
    A degenerate/None CI (e.g. a zero-width all-ceiling cell) is never positive."""
    if value != value:           # NaN
        return False
    return value >= TAU and ci is not None and ci[0] > CI_LOWER_MUST_EXCEED


def rate(per_item):
    vals = [v for v in per_item.values() if v is not None]
    return statistics.mean(vals) if vals else None


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

def chose_was(row):
    """Map the chosen LETTER back to content. 1 = chose "was", 0 = "were",
    None = missing."""
    if row["value"] is None:
        return None
    return 1 if row["value"] == row["was_letter"] else 0


def split_aann_control(rows):
    aann, ctrl = {}, {}
    for r in rows:
        (aann if r["cond"] == "aann" else ctrl)[r["id"]] = chose_was(r)
    return aann, ctrl


# ---------------- Tier-0 ----------------

def chose_grammatical(row):
    """Tier-0 'correct' = picked the letter whose form is the grammatical one."""
    if row["value"] is None:
        return None
    p = TIER0[row["id"]]
    correct_letter = "A" if p["A"] == p["grammatical_form"] else "B"
    return 1 if row["value"] == correct_letter else 0


def analyze_tier0(rows, status):
    res = {"arm_status": status}
    if not rows or status != "ok":
        return res
    ok = sum(1 for r in rows if chose_grammatical(r) == 1)
    miss, gate = miss_gate(rows)
    res.update({"n": len(rows), "correct": ok, "missing": miss,
                "missingness": gate,
                "pass": bool(ok >= TIER0_MIN and gate != "instrument-failure")})
    return res


# ---------------- diagnostic (DESCRIPTIVE-ONLY; NEVER verdict-bearing) ----------------

def analyze_diagnostic(rows, status):
    """Count-noun ceiling diagnostic. Reports P(were) on genuine count plurals.
    DESCRIPTIVE ONLY — this function's output enters NO verdict branch."""
    res = {"arm_status": status, "descriptive_only": True,
           "never_verdict_bearing": True}
    if not rows or status != "ok":
        return res
    were = [1 - chose_was(r) for r in rows if r["value"] is not None]  # were=1-was
    miss, gate = miss_gate(rows)
    res.update({
        "n": len(rows), "missing": miss, "missingness": gate,
        "p_were_count_plural": (round(statistics.mean(were), 4) if were else None),
        "interpretation": ("P(were) on genuine COUNT plurals; high => the model "
                           "CAN pick 'were' for an ordinary count plural, so any "
                           "AANN/quantity ceiling is notional-singular-for-"
                           "quantity, not a blanket 'always picks was'. "
                           "DESCRIPTIVE ONLY — does not bear on the verdict."),
    })
    return res


# ---------------- per-model agreement cell ----------------

def agreement_cell(rows, ids):
    aann, ctrl = split_aann_control(rows)
    shift, ci, n, p_a, p_c = single_contrast_ci(aann, ctrl, ids)
    return {
        "label": "P(was|AANN) - P(was|bare-plural control) [held-out single "
                 "contrast; the v4 agreement arm, unchanged]",
        "shift": None if shift != shift else round(shift, 4),
        "ci95": None if ci is None else [round(ci[0], 4), round(ci[1], 4)],
        "n_items": n,
        "raw_was_rate_aann": None if p_a is None else round(p_a, 4),
        "raw_was_rate_control": None if p_c is None else round(p_c, 4),
        "positive": positive(shift, ci),
        "below_item_floor": n < MIN_ITEMS,
    }


# ---------------- frozen verdict tree (ordered if/else, AS CODE) ----------------

def per_model_verdict(slot, cell, tier0_passed):
    """The frozen per-model branch. Ordered if/else with an explicit final else.

    Reflex-bearer (gpt, slot B): REPLICATES vs FAILS-TO-REPLICATE.
    Others (claude/gemini): CEILING-UNINFORMATIVE / GENERALIZES-TO-PANEL /
    NO-REFLEX. Any floor breach or Tier-0 failure on the cell resolves to
    INCONCLUSIVE-CELL, kept out of the positive branches."""
    # gate: a verdict-bearing cell needs the item floor met in both conditions
    if cell["below_item_floor"]:
        return ("INCONCLUSIVE-CELL",
                f"fewer than {MIN_ITEMS} gated items in both conditions; "
                "the cell carries no inferential weight (PREREG floor)")
    if not tier0_passed:
        return ("INCONCLUSIVE-CELL",
                "model failed Tier-0 (does not read the was/were task at "
                "threshold); its agreement numbers are descriptive only")

    if slot == REFLEX_BEARER:
        # ---- gpt-5.4-mini: replication test ----
        if cell["positive"]:
            return ("REPLICATES",
                    "the singular-agreement reflex replicates on fresh held-out "
                    "items: P(was|AANN) - P(was|control) >= TAU with CI-lower > 0")
        return ("FAILS-TO-REPLICATE",
                "the held-out agreement shift does not clear the pre-registered "
                "bar (>= TAU with CI-lower > 0)")

    # ---- claude / gemini: ceiling, generalization, or no-reflex ----
    cw = cell["raw_was_rate_control"]
    if cw is not None and cw >= CEILING:
        return ("CEILING-UNINFORMATIVE",
                f"control 'was'-rate {cw} >= {CEILING}: the discriminator is "
                "structurally blind (both AANN and bare-plural pull singular "
                "agreement), exactly as in v3/v4 — the contrast has no room to "
                "show, so this is NOT a failure")
    if cell["positive"]:
        return ("GENERALIZES-TO-PANEL",
                "off the ceiling, the held-out agreement shift clears the bar: "
                "the reflex is present in this model too")
    return ("NO-REFLEX",
            "off the ceiling but the held-out agreement shift does not clear the "
            "bar: no singular-agreement reflex in this model")


def overall_verdict(per_model_cats):
    """Exhaustive overall verdict with an explicit final else. per_model_cats is
    {slot: category}."""
    gpt = per_model_cats.get(REFLEX_BEARER)
    others = [per_model_cats[s] for s in ("A", "C") if s in per_model_cats]
    any_generalizes = any(c == "GENERALIZES-TO-PANEL" for c in others)

    if any_generalizes:
        return ("REFLEX-GENERALIZES-TO-PANEL",
                "at least one of claude/gemini shows the held-out agreement "
                "reflex off the ceiling; the reflex is not gpt-specific")
    if gpt == "REPLICATES":
        return ("REFLEX-IS-GPT-SPECIFIC-AND-REPLICATES",
                "gpt-5.4-mini's reflex replicates on fresh held-out items, and "
                "neither claude nor gemini generalizes (both at ceiling or "
                "no-reflex): the reflex is gpt-specific and robust to held-out "
                "items")
    if gpt == "FAILS-TO-REPLICATE":
        return ("REFLEX-FAILS-TO-REPLICATE",
                "gpt-5.4-mini's reflex does not replicate on fresh held-out "
                "items, and neither other model generalizes")
    return ("INCONCLUSIVE",
            "the reflex-bearer's cell did not resolve to REPLICATES or "
            "FAILS-TO-REPLICATE (e.g. Tier-0 failure or item-floor breach on "
            "gpt-5.4-mini), and no other model generalizes; no verdict")


# ---------------- per-model assembly ----------------

def analyze_model(slot, agr, agr_st, diag, diag_st, t0, t0_st):
    res = {"slot": slot, "model": PANEL_NAMES[slot],
           "arm_status": {"agreement": agr_st, "diagnostic": diag_st,
                          "tier0": t0_st}}
    res["tier0"] = analyze_tier0(t0, t0_st)
    res["diagnostic"] = analyze_diagnostic(diag, diag_st)  # descriptive only
    if agr_st != "ok":
        return res
    res["agreement"] = agreement_cell(agr, list(ITEMS))
    cat, note = per_model_verdict(slot, res["agreement"],
                                  bool(res["tier0"].get("pass")))
    res["category"] = cat
    res["category_note"] = note
    return res


def assemble(per_model):
    incomplete = [f"{s}/{arm}:{st}" for s, r in per_model.items()
                  for arm, st in r["arm_status"].items()
                  if arm == "agreement" and st != "ok"]
    out = {
        "run": "2026-06-14-aann-agreement-reflex-v5",
        "design": "experiments/designs/aann-agreement-reflex-generalization-v5.md",
        "anchor": "internal-contrast-only",
        "chief_cost_statement": CHIEF_COST,
        "expected_agreement_key_provenance": KEY_PROVENANCE,
        "headline_instrument": "agreement (was/were FC) single contrast; the v4 "
                               "agreement arm unchanged, on fresh held-out items",
        "headline_statistic": "P(was|AANN) - P(was|bare-plural control)",
        "thresholds": {"tau_shift_inclusive": TAU,
                       "ci_lower_strictly_above": CI_LOWER_MUST_EXCEED,
                       "ceiling_control_was_rate_inclusive": CEILING,
                       "tier0_min_inclusive_of_12": TIER0_MIN,
                       "item_floor_per_cell": MIN_ITEMS,
                       "bootstrap_resamples": BOOT, "bootstrap_seed": SEED},
        "diagnostic_arm_note": "DESCRIPTIVE-ONLY count-noun ceiling diagnostic; "
                               "NEVER verdict-bearing (see per-model 'diagnostic').",
        "models": per_model,
        "cost": read_cost_log(),
    }
    if incomplete:
        out["verdict"] = "INCOMPLETE (agreement arm missing/partial)"
        out["incomplete_arms"] = incomplete
        return out

    cats = {s: per_model[s]["category"] for s in ("A", "B", "C")
            if "category" in per_model[s]}
    out["per_model_categories"] = cats
    verdict, basis = overall_verdict(cats)
    out["verdict"] = verdict
    out["verdict_basis"] = basis
    # surface (descriptively) any model whose Tier-0 failed or floor breached
    out["tier0_summary"] = {s: per_model[s]["tier0"].get("pass")
                            for s in ("A", "B", "C")}
    return out


def report(out):
    print("== AANN agreement-reflex generalization v5 — FROZEN PREREG analysis ==")
    print(f"   anchor: {out['anchor']} | headline: {out['headline_statistic']}")
    for s in ("A", "B", "C"):
        r = out["models"].get(s, {})
        t0 = r.get("tier0", {})
        dg = r.get("diagnostic", {})
        ag = r.get("agreement")
        flag = "" if not s == REFLEX_BEARER else " [REFLEX-BEARER]"
        if ag is None:
            print(f"  {s} ({PANEL_NAMES[s]}){flag}: agreement arm "
                  f"{r.get('arm_status', {}).get('agreement')}")
            continue
        print(f"  {s} ({r['model']}){flag}: tier0 {t0.get('correct')}/12 "
              f"({'PASS' if t0.get('pass') else 'FAIL'})")
        print(f"     agreement shift = {ag['shift']} CI {ag['ci95']} "
              f"(pos={ag['positive']}); was-rate AANN/control = "
              f"{ag['raw_was_rate_aann']}/{ag['raw_was_rate_control']} "
              f"(n={ag['n_items']})")
        print(f"     DIAGNOSTIC (descriptive-only): P(were|count plural) = "
              f"{dg.get('p_were_count_plural')}")
        print(f"     category: {r['category']}  -> {r['category_note']}")
    print(f"  VERDICT: {out['verdict']}")
    print(f"     basis: {out.get('verdict_basis')}")
    print(f"  cost: {out['cost'].get('total_billed_usd')} "
          f"({out['cost'].get('status')})")
    print("\n=== MACHINE-READABLE JSON SUMMARY ===")
    print(json.dumps(out, indent=1))


def main():
    per = {}
    for slot in ("A", "B", "C"):
        agr, ags = load(slot, "agreement")
        diag, ds = load(slot, "diagnostic")
        t0, t0s = load(slot, "tier0")
        per[slot] = analyze_model(slot, agr, ags, diag, ds, t0, t0s)
    out = assemble(per)
    json.dump(out, open(HERE / "results.json", "w"), indent=1)
    report(out)


# ---------------- selftest (synthetic; no files, no calls) ----------------

def _agr_rows(was_aann, was_ctrl, na_aann=()):
    """Synthetic agreement rows over the two conditions. was_* are 0/1 rates
    applied deterministically per item (so the shift is exact)."""
    rows = []
    for it in STIMULI["items"]:
        was_letter = it["agreement"]["agr_letter_was"]
        for cond, w in (("aann", was_aann), ("control", was_ctrl)):
            if it["id"] in na_aann and cond == "aann":
                val = None
            else:
                val = was_letter if w else ("B" if was_letter == "A" else "A")
            rows.append({"id": it["id"], "arm": "agreement", "cond": cond,
                         "was_letter": was_letter, "raw": str(val),
                         "value": val, "usage": None, "error": None})
    return rows


def _diag_rows(were_rate):
    rows = []
    for d in STIMULI["diagnostic"]:
        was_letter = d["diagnostic"]["agr_letter_was"]
        chose_were = 1 if were_rate else 0
        # chose 'were' => the letter that is NOT the was_letter
        val = (("B" if was_letter == "A" else "A") if chose_were else was_letter)
        rows.append({"id": d["id"], "arm": "diagnostic", "cond": "count_control",
                     "was_letter": was_letter, "expected": d["diagnostic"]["expected"],
                     "raw": str(val), "value": val, "usage": None, "error": None})
    return rows


def _tier0_rows(n_correct, n_missing=0):
    rows = []
    for i, p in enumerate(STIMULI["tier0"]):
        correct_letter = "A" if p["A"] == p["grammatical_form"] else "B"
        if i < n_missing:
            val = None
        elif i < n_missing + n_correct:
            val = correct_letter
        else:
            val = "A" if correct_letter == "B" else "B"
        rows.append({"id": p["id"], "arm": "tier0",
                     "was_letter": p["agr_letter_was"],
                     "grammatical_form": p["grammatical_form"],
                     "raw": str(val), "value": val, "usage": None, "error": None})
    return rows


def selftest():
    failures = []
    n = [0]

    def check(name, cond):
        n[0] += 1
        print(("PASS " if cond else "FAIL ") + name)
        if not cond:
            failures.append(name)

    # ---- single-contrast math + positivity
    cell = agreement_cell(_agr_rows(1, 0), list(ITEMS))
    check("clean shift +1 (AANN was, control were)", cell["shift"] == 1.0)
    check("shift +1 positive", cell["positive"])
    check("was-rate AANN 1.0 / control 0.0",
          cell["raw_was_rate_aann"] == 1.0
          and cell["raw_was_rate_control"] == 0.0)

    # ceiling cell: both conditions pick 'was' at 1.0 -> shift 0, control >= CEILING
    cell_ceil = agreement_cell(_agr_rows(1, 1), list(ITEMS))
    check("ceiling cell shift 0, not positive",
          cell_ceil["shift"] == 0.0 and not cell_ceil["positive"])
    check("ceiling cell control was-rate 1.0 >= CEILING",
          cell_ceil["raw_was_rate_control"] >= CEILING)

    # below-TAU shift: small positive that does not clear 0.30
    # 5/30 items shift -> 0.1667 < TAU
    def _agr_partial(k_aann_was):
        rows = []
        for j, it in enumerate(STIMULI["items"]):
            wl = it["agreement"]["agr_letter_was"]
            for cond in ("aann", "control"):
                w = 1 if (cond == "aann" and j < k_aann_was) else 0
                val = wl if w else ("B" if wl == "A" else "A")
                rows.append({"id": it["id"], "arm": "agreement", "cond": cond,
                             "was_letter": wl, "raw": str(val), "value": val,
                             "usage": None, "error": None})
        return rows
    cell_small = agreement_cell(_agr_partial(5), list(ITEMS))
    check("shift 5/30 (~0.167) < TAU not positive",
          not cell_small["positive"] and cell_small["shift"] < TAU)

    # ---- thresholds
    check("positive() needs CI-lower > 0", not positive(0.5, (0.0, 0.9)))
    check("positive() at exactly TAU with good CI",
          positive(0.30, (0.05, 0.55)))
    check("positive() rejects NaN", not positive(float("nan"), (0.1, 0.2)))

    # ---- Tier-0 gate
    check("tier0 10/12 passes", analyze_tier0(_tier0_rows(10), "ok")["pass"])
    check("tier0 9/12 fails", not analyze_tier0(_tier0_rows(9), "ok")["pass"])
    check("tier0 >25% missing = instrument failure",
          analyze_tier0(_tier0_rows(8, 4), "ok")["missingness"]
          == "instrument-failure"
          and not analyze_tier0(_tier0_rows(8, 4), "ok")["pass"])

    # ---- diagnostic descriptive-only, never verdict-bearing
    dg = analyze_diagnostic(_diag_rows(1), "ok")
    check("diagnostic P(were)=1.0 reported", dg["p_were_count_plural"] == 1.0)
    check("diagnostic flagged descriptive-only + never-verdict-bearing",
          dg["descriptive_only"] and dg["never_verdict_bearing"])

    # ---- per-model verdict branches --------------------------------------
    # gpt REPLICATES (clean +1 shift, tier0 pass)
    perB_rep = analyze_model("B", _agr_rows(1, 0), "ok", _diag_rows(1), "ok",
                             _tier0_rows(12), "ok")
    check("gpt clean shift -> REPLICATES",
          perB_rep["category"] == "REPLICATES")
    # gpt FAILS-TO-REPLICATE (small shift)
    perB_fail = analyze_model("B", _agr_partial(5), "ok", _diag_rows(1), "ok",
                              _tier0_rows(12), "ok")
    check("gpt small shift -> FAILS-TO-REPLICATE",
          perB_fail["category"] == "FAILS-TO-REPLICATE")
    # gpt tier0 fail -> INCONCLUSIVE-CELL
    perB_t0 = analyze_model("B", _agr_rows(1, 0), "ok", _diag_rows(1), "ok",
                            _tier0_rows(9), "ok")
    check("gpt tier0 fail -> INCONCLUSIVE-CELL",
          perB_t0["category"] == "INCONCLUSIVE-CELL")

    # claude CEILING-UNINFORMATIVE (both at ceiling)
    perA_ceil = analyze_model("A", _agr_rows(1, 1), "ok", _diag_rows(1), "ok",
                              _tier0_rows(12), "ok")
    check("claude both-ceiling -> CEILING-UNINFORMATIVE",
          perA_ceil["category"] == "CEILING-UNINFORMATIVE")
    # claude GENERALIZES (off ceiling, clean shift)
    perA_gen = analyze_model("A", _agr_rows(1, 0), "ok", _diag_rows(1), "ok",
                             _tier0_rows(12), "ok")
    check("claude off-ceiling clean shift -> GENERALIZES-TO-PANEL",
          perA_gen["category"] == "GENERALIZES-TO-PANEL")
    # gemini NO-REFLEX (off ceiling, small shift)
    perC_no = analyze_model("C", _agr_partial(5), "ok", _diag_rows(0), "ok",
                            _tier0_rows(12), "ok")
    check("gemini off-ceiling small shift -> NO-REFLEX",
          perC_no["category"] == "NO-REFLEX")

    # ---- overall verdict branches ----------------------------------------
    out_gpt = assemble({"A": perA_ceil, "B": perB_rep, "C": perA_ceil})
    check("gpt REPLICATES + others ceiling -> GPT-SPECIFIC-AND-REPLICATES",
          out_gpt["verdict"] == "REFLEX-IS-GPT-SPECIFIC-AND-REPLICATES")
    out_panel = assemble({"A": perA_gen, "B": perB_rep, "C": perA_ceil})
    check("a model GENERALIZES -> REFLEX-GENERALIZES-TO-PANEL",
          out_panel["verdict"] == "REFLEX-GENERALIZES-TO-PANEL")
    out_fail = assemble({"A": perA_ceil, "B": perB_fail, "C": perC_no})
    check("gpt FAILS + no generalize -> REFLEX-FAILS-TO-REPLICATE",
          out_fail["verdict"] == "REFLEX-FAILS-TO-REPLICATE")
    out_inc = assemble({"A": perA_ceil, "B": perB_t0, "C": perA_ceil})
    check("gpt INCONCLUSIVE-CELL + no generalize -> INCONCLUSIVE",
          out_inc["verdict"] == "INCONCLUSIVE")
    # generalize OUTRANKS a gpt failure (panel finding stands)
    out_panel2 = assemble({"A": perA_gen, "B": perB_fail, "C": perC_no})
    check("generalize outranks gpt-fail -> REFLEX-GENERALIZES-TO-PANEL",
          out_panel2["verdict"] == "REFLEX-GENERALIZES-TO-PANEL")

    # ---- INCOMPLETE path (agreement arm absent)
    out_missing = assemble({
        "A": {"slot": "A", "model": PANEL_NAMES["A"],
              "arm_status": {"agreement": "absent", "diagnostic": "ok",
                             "tier0": "ok"},
              "tier0": {"arm_status": "ok"}, "diagnostic": {"arm_status": "ok"}},
        "B": perB_rep, "C": perA_ceil})
    check("absent agreement arm -> INCOMPLETE",
          out_missing["verdict"].startswith("INCOMPLETE"))

    # ---- diagnostic never appears in any verdict text
    check("diagnostic kept out of verdict (no count-plural in verdict basis)",
          "count" not in out_panel.get("verdict_basis", "").lower())

    # ---- determinism + serializable
    c1 = single_contrast_ci({i: 1 for i in ITEMS}, {i: 0 for i in ITEMS},
                            list(ITEMS))[1]
    c2 = single_contrast_ci({i: 1 for i in ITEMS}, {i: 0 for i in ITEMS},
                            list(ITEMS))[1]
    check("bootstrap CI deterministic under frozen seed", c1 == c2)
    check("summary JSON-serializable", bool(json.dumps(out_panel)))

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
