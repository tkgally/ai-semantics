# PREREG — C2 privative-modifier category-default B2 calibration (frozen before any probe call)

**Date:** 2026-06-28 (session 137)
**Step:** STEP 1b of the frozen build instruction in [`decisions/resolved/monotonicity-cancel-arm-redesign`](../../../wiki/decisions/resolved/monotonicity-cancel-arm-redesign.md) (ratified s136). Reached because **STEP 1 (C1 telic-completion) was a B2 NO-GO** ([`result/monotonicity-c1-completion-calibration-v1`](../../../wiki/findings/results/monotonicity-c1-completion-calibration-v1.md)). **M2 applied first:** the conjecture's scope was broadened in writing (nominal/adjectival privative cancel arm admitted; verbal-only abstraction relaxed; add-verbal/cancel-nominal domain mismatch a live caveat) — see [`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md), the "M2" blockquote.
**Frozen items:** `experiments/data/monotonicity-c2-privative-calibration/items.csv`, sha256[:16] **`39598ee7ad97f33d`** (emitted by `build_items.py`, committed before any API call).
**What this is:** a **calibration only** — measures whether a bare head noun's *category-membership* default is a model-held entailment **at the B2 ceiling**, BEFORE any matched asymmetry battery is built or run. Tests nothing about the conjecture; decides only whether the C2 cancel direction *can be built at matched ceiling*.
**Human anchor:** **none asserted — `internal-contrast-only`** (ratified, [`decisions/resolved/conflicting-cue-human-anchor`](../../../wiki/decisions/resolved/conflicting-cue-human-anchor.md)). No human-comparison claim; no human label invented.

## The C2 cancel direction (privative-modifier cancellation)

| cell | example | hypothesis | role |
|---|---|---|---|
| **default** (calibrated here) | "Sam bought a gun." | "Sam bought a weapon." | the category default the STEP-2 cancel arm would suppress — must sit at ceiling on the bare frame (B2) |
| **construction** (held OUT; built only on GO in STEP 2) | "Sam bought a fake gun." | (same) | privative modifier cancels category membership (nominal analogue of the imperfective paradox) |
| **cue** (STEP 2 only) | "…a fake gun, but it was a real weapon." | (same) | explicit re-assertion of the cancelled category |

Only the **default** cell is run in this calibration. The cancel **construction** (suppression) cell is held **out** (anti-cheat: the asymmetry magnitude must not be computable at the gate). Each item's frozen privative modifier (for STEP 2) is recorded in `items.csv`.

**Frozen category-hypothesis phrasing:** `"<Subject> <verb> a/an <category>."` — the premise frame with the head noun replaced by its superordinate category, uniform across all eight items.

**Noun pool (8):** gun, diamond, rose, tiger, apple, pearl, sword, violin — each a clean taxonomic (bare noun ⊨ category) entailment, cancellable by a standard privative modifier (fake / artificial / toy / imitation / plastic). Categories: weapon (×2), gemstone, flower, animal, fruit, jewel, musical instrument.

8 default items × 2 instruments (NLI primary + forced-choice) × 3 models = **48 calls**.

## FROZEN B2 gate (decision STEP 1b, NOT relaxable)

Read **panel NLI primary**; "≥2/3 models" = the per-model value clears the bar in ≥2 of 3.

> **Category-membership default affirm ("a gun" → "a weapon") ≥ 0.80 in ≥2/3 models, strict NLI (label 0 = entailment), temperature 0.**

- **GO →** STEP 2: build the matched C2 cancel arm in the conflicting-cue paradigm, reuse the frozen B2-passing resultative ADD arm verbatim (items sha `80bd4b60b55a3e60`), re-run the full B2 gate, obtain an independent pre-run-critic GO, run the full battery, read by the frozen s134 thresholds (asymmetry 20 pp; fragility 10 pp; cue 0.70). The **add-verbal/cancel-nominal domain mismatch is a live caveat** on the result (M2).
- **NO-GO →** **STEP 3 principled-limit closure** (M3): both C1 and C2 failed → record, as a first-class result, that the matched-difficulty cancel arm is **un-instrumentable at ceiling on the strict-NLI panel** without a categorically-held lexical-entailment default. Do **not** relax the bar.

## Anti-cheat (binding)

- Items **frozen + sha256-hashed and committed before the first probe call**; no item/noun added, dropped, or re-binned after.
- The gate threshold is **frozen before any data** (the ratified decision's STEP 1b floor, unchanged); the verdict is read mechanically by `analyze_calib.py`. No threshold tuned post-hoc.
- **Gate-before-anything:** an **independent fresh-agent pre-run critic** reviews this frozen calibration set + this PREREG against the decision's STEP 1b spec and returns GO/NO-GO *before* the probe runs.
- **Post-run**, an independent fresh agent recomputes every number from `raw_calib/*.json`.
- This session **runs** the calibration; it ratifies nothing and re-tunes no threshold.

## Known limits (stated before data)

- **Small N, panel-as-subjects, single run.** 8 nouns × 3 models; a feasibility gate, not a magnitude or a human comparison.
- **`internal-contrast-only`.** No human baseline; the gate certifies the category default is at ceiling *for these models*, not for people.
- **Domain mismatch (M2 live caveat).** A C2 battery pairs a *verbal* ADD arm with a *nominal/adjectival* CANCEL arm; any C2 asymmetry is across a domain difference, not a clean within-verbal contrast — to be stated prominently on any C2 result.
- **A C2 NO-GO is the principled-limit trigger**, not a conjecture falsification — it is a fact about the instrument (no categorically-held lexical-entailment default reaches ceiling on this panel).
