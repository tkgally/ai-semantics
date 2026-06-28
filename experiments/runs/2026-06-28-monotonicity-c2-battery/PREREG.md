# PREREG — C2 matched-difficulty add-vs-cancel monotonicity battery (frozen before any probe call)

**Date:** 2026-06-28 (session 137)
**Step:** STEP 2 of [`decisions/resolved/monotonicity-cancel-arm-redesign`](../../../wiki/decisions/resolved/monotonicity-cancel-arm-redesign.md) (ratified s136), reached because STEP 1 (C1) was a B2 NO-GO and **STEP 1b (C2 privative) was a B2 GO** ([`result/monotonicity-c2-privative-calibration-v1`](../../../wiki/findings/results/monotonicity-c2-privative-calibration-v1.md)). **M2 applied first** ([`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md), the "M2" blockquote): scope broadened to a nominal/adjectival privative cancel arm; verbal-only abstraction relaxed; add-verbal/cancel-nominal domain mismatch a live caveat.
**Frozen items:** `experiments/data/monotonicity-c2-battery/items.csv`, sha256[:16] **`4b823d3d48422eaf`** (emitted by `build_items.py`, committed before any API call). **54 items** = 30 ADD (verbatim s135) + 24 CANCEL (C2 privative).
**Tests:** [`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md) — its decisive matched-difficulty add-vs-cancel test, **as broadened by M2**.
**Yardstick fixed by (ratified):** the s134 operationalization (thresholds) + the s136 re-design (cancel coercion). This session **builds + runs**; it re-tunes nothing.
**Human anchor:** **none — `internal-contrast-only`** (ratified [`decisions/resolved/conflicting-cue-human-anchor`](../../../wiki/decisions/resolved/conflicting-cue-human-anchor.md)).

## The frozen pair (STEP 2)

| arm | construction | example | hypothesis | discriminating cell |
|---|---|---|---|---|
| **ADD** (verbatim s135, sha `80bd4b60b55a3e60`) | resultative | "Tomas hammered the metal flat." | "The metal became flat." | construction affirm = **add_no_cue** (license; want ceiling) |
| **CANCEL** (C2 privative, M2) | privative modifier | "Sam bought a fake gun." | "Sam bought a weapon." | **cancel_no_cue** = 1 − construction affirm (suppress; want high) |

**ADD verb pool (10, reused verbatim):** beat, boil, cut, hammer, kick, paint, push, scrub, squeeze, wipe — the s135 frozen resultative arm, read byte-for-byte (a sha self-check in `build_items.py` refuses to build unless the source is `80bd4b60b55a3e60`).
**CANCEL noun pool (8, C2):** gun, diamond, rose, tiger, apple, pearl, sword, violin — each a taxonomic (noun ⊨ category) entailment cancelled by a privative modifier (fake/artificial/toy/imitation/plastic). Identical to the STEP-1b GO calibration (sha `39598ee7ad97f33d`); privatives now used.

Each arm × 3 conditions (the matched conflicting-cue paradigm):
- **ADD:** `control` (bare) / `construction` (resultative; licensing-no-cue) / `cue` (explicit **denial**: "…flat, but the metal did not become flat" → follow-cue = **withhold**).
- **CANCEL:** `default` (bare noun; category default) / `construction` (privative; **suppression**) / `cue` (explicit **re-assertion**: "…a fake gun, but it was a real weapon" → follow-cue = **affirm**).

54 items × 2 instruments × 3 models = **324 calls** for the full battery; the B2 calibration subset (12 items: add {cut,hammer,kick,push} × {control,construction} + cancel {gun,diamond,tiger,apple} × {default}) is a separate, prior probe.

## FROZEN thresholds (ratified s134, UNTOUCHED)

All read **panel NLI primary**; "≥2/3 models" = the per-model value clears the bar in ≥2 of 3.

**B2 blocking ceiling gate** — on the calib subset, **before** the main read. Admit only if:
1. **Add headroom:** construction affirm **≥ 0.80** AND bare control affirm **≤ 0.40**, in ≥2/3.
2. **Cancel default:** category-membership affirm **≥ 0.80**, in ≥2/3. *(Already GO at STEP 1b; re-run on the frozen combined set per the decision.)*
The cancel **suppression** (construction) cell is held **out** of calib, so the asymmetry is not computable at the gate.

**Asymmetry (20 pp).** On the no-cue cell: `add_no_cue − cancel_no_cue ≥ 0.20` (≥2/3) → **CONFIRMS** (leg 1); `|·| < 0.20` (≥2/3) → **SYMMETRIC** (falsifies); `≤ −0.20` (≥2/3) → **REVERSAL** (falsifies).

**Instrument-fragility (10 pp).** Cancel NLI-vs-FC disagreement on the no-cue cell must exceed the add arm's by **≥ 0.10** in ≥2/3 (leg 2).

**Cue-arm rule (inherited):** ≥ 0.70 follow-cue in ≥2/3 = robust; else informative partial-null.

## Pre-registered outcomes (all first-class; falsify arms LIVE)

- **Confirms:** asymmetry ≥ 20 pp (≥2/3) **and** cancel more fragile (≥10 pp, ≥2/3) → the asymmetry generalizes to the (M2-broadened) pair; conjecture → `tested` (supported on this leg, `internal-contrast-only`, **domain-mismatch caveat**).
- **Symmetric → falsifies:** add and cancel no-cue indistinguishable (<20 pp, ≥2/3).
- **Reversal → falsifies:** cancel easy / add hard (≥20 pp the other way, ≥2/3).
- A symmetric/reversal result is a **clean falsification** (M3: the principled-limit closure is **not** triggered by an asymmetry result — only by measured B2 NO-GOs, which did not occur). No re-pairing/re-tuning after outputs.

## M1 / M2 (binding on the result page)

- **M1:** the B2 default-at-ceiling pass (category membership 1.00, 3/3 at STEP 1b) is what licenses reading a cancel **suppression failure** as **defeasance** — the gate certifies the cancelled default is a real model-held entailment, closing the s135 "the inference was never an entailment" confound.
- **M2 live caveat:** the ADD arm is **verbal** (resultative) and the CANCEL arm is **nominal/adjectival** (privative), so any asymmetry is across a **domain difference**, not a clean within-verbal contrast — a broadened, weaker version of the original bet. State prominently.

## Anti-cheat (binding)

- Items **frozen + sha256-hashed (`4b823d3d48422eaf`) and committed before the first probe call**; the ADD arm is reused **verbatim** (byte-for-byte, sha-self-checked); no item added/dropped/re-binned after.
- All thresholds **frozen before any data** (ratified s134); verdicts read mechanically by `analyze_calib.py` (gate) and `analyze.py` (asymmetry/fragility/cue). No threshold tuned post-hoc.
- **Two-phase, gate-before-run:** (1) `probe.py --calib` → `analyze_calib.py` B2 gate; (2) on GO, an **independent fresh-agent pre-run critic** reviews the frozen full set + this PREREG + the gate; (3) on GO, `probe.py` runs the full battery.
- **Post-run**, an independent fresh agent recomputes every number from `raw/*.json`.

## Known limits (stated before data)

- **Small N, panel-as-subjects, single run.** 10 add + 8 cancel stems × 3 conditions × 3 models; a direction-of-effect signal, not a magnitude or a human comparison.
- **`internal-contrast-only`.** No human baseline on any arm.
- **Domain mismatch (M2).** The headline caveat: add-verbal vs cancel-nominal.
- **Cue arms are deliberately contradictory sentences** (anomalous); they test cue-following, secondary to the no-cue headline.
