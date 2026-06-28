# PREREG — C1 telic-completion DEFAULT B2 calibration (frozen before any probe call)

**Date:** 2026-06-28 (session 137)
**Step:** STEP 1 of the frozen build instruction in [`decisions/resolved/monotonicity-cancel-arm-redesign`](../../../wiki/decisions/resolved/monotonicity-cancel-arm-redesign.md) (ratified s136: **ADOPT C1 telic-completion CONDITIONAL on its own B2 calibration**, C2 privative fallback, principled-limit closure if both fail, MODS M1–M3).
**Frozen items:** `experiments/data/monotonicity-c1-completion-calibration/items.csv`, sha256[:16] **`4e8c3935af154c46`** (emitted by `build_items.py`, committed before any API call).
**What this is:** a **calibration only** — it measures whether the *completion default* of a simple-past accomplishment is a model-held entailment **at the B2 ceiling**, BEFORE any matched asymmetry battery is built or run. It tests nothing about the [`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md); it decides only whether the C1 cancel direction *can be built at matched ceiling*.
**Human anchor:** **none asserted — `internal-contrast-only`** (ratified, [`decisions/resolved/conflicting-cue-human-anchor`](../../../wiki/decisions/resolved/conflicting-cue-human-anchor.md)). No human-comparison claim; no human label invented.

## The C1 cancel direction (telic-completion accomplishment cancellation)

| cell | example | hypothesis | role |
|---|---|---|---|
| **default** (calibrated here) | "Maria built the house." | "Maria finished building the house." | the completion default that STEP 2's cancel arm would suppress — must sit at ceiling on the bare frame (B2, MOD-3) |
| **construction** (held OUT; built only on GO in STEP 2) | "Maria built the house for two hours." | (same) | *for*-durative/atelic frame coerces a non-culminating reading (imperfective paradox) → cancels completion |
| **cue** (STEP 2 only) | "…for two hours, but she did not finish building it." | (same) | explicit re-assertion of the cancellation |

Only the **default** cell is run in this calibration. The cancel **construction** (suppression) cell is held out, exactly as s135 held its cancel-suppression cell out of calib — anti-cheat: the asymmetry magnitude must not be computable at the gate.

**Frozen completion-hypothesis phrasing** (decision STEP 1: "pick one phrasing, freeze it"): `"<Subject> finished <gerund> the <object>."` — the standard accomplishment-culmination diagnostic, uniform across all eight verbs.

**Accomplishment verb pool (8):** build, write, read, bake, knit, mow, draw, dig — incremental-theme accomplishments with a quantized definite object, whose bare simple-past plausibly entails culmination. **Disjoint** from the resultative ADD pool {beat, boil, cut, hammer, kick, paint, push, scrub, squeeze, wipe} (decision STEP 1; `paint` is in the add pool → no accomplishment item is a resultative). Verified by a disjointness self-check in `build_items.py`.

8 default items × 2 instruments (NLI primary + forced-choice) × 3 models (claude-sonnet-4.6 A, gpt-5.4-mini B, gemini-3.5-flash C) = **48 calls**.

## FROZEN B2 gate (decision STEP 1, NOT relaxable)

Read **panel NLI primary**; "≥2/3 models" = the per-model value clears the bar in ≥2 of 3.

> **Completion default affirm ("…finished V-ing…") ≥ 0.80 in ≥2/3 models, strict NLI (label 0 = entailment), temperature 0.**

- **GO →** STEP 2: build the matched C1 cancel arm in the conflicting-cue paradigm, reuse the frozen B2-passing resultative ADD arm verbatim (items sha `80bd4b60b55a3e60`), re-run the full B2 gate, obtain an independent pre-run-critic GO, run the full battery, read by the frozen s134 thresholds (asymmetry 20 pp; fragility 10 pp; cue 0.70). The conjecture's scope is unchanged.
- **NO-GO →** do **not** relax the bar or re-pair completion verbs within the frame (a NO-GO is structural, like s135). Record a verified C1-NO-GO result (a weigh-question-4-bearing finding: completion, too, reads as defeasible-not-categorical under strict NLI), then STEP 1b (C2 privative, **after** M2's written conjecture-scope amendment).

## Anti-cheat (binding)

- Items **frozen + sha256-hashed and committed before the first probe call**; no item/verb added, dropped, or re-binned after.
- The gate threshold is **frozen before any data** (it is the ratified decision's STEP 1 floor, unchanged); the verdict is read mechanically by `analyze_calib.py`. No threshold tuned post-hoc.
- **Gate-before-anything:** an **independent fresh-agent pre-run critic** reviews this frozen calibration set + this PREREG against the decision's STEP 1 spec and returns GO/NO-GO *before* the probe runs.
- **Post-run**, an independent fresh agent recomputes every number from `raw_calib/*.json` (separate from `analyze_calib.py`).
- This session **runs** the calibration; it ratifies nothing and re-tunes no threshold (the yardstick was ratified s134/s136).

## Known limits (stated before data)

- **Small N, panel-as-subjects, single run.** 8 verbs × 3 models; this is a feasibility gate, not a magnitude or a human comparison.
- **`internal-contrast-only`.** No human baseline; completion is contestable for humans too. The gate certifies the default is at ceiling *for these models*, not for people.
- **A C1 NO-GO is not a falsification of the conjecture** — it is a fact about the *instrument* (completion read as defeasible-not-categorical under strict NLI), and it routes to C2, not to a conjecture verdict.
