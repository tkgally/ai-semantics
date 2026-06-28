# PREREG — monotonicity-generalization battery (frozen before any probe call)

**Date:** 2026-06-28 (session 135)
**Frozen items:** `experiments/data/monotonicity-generalization-battery/items.csv`, sha256[:16] **`80bd4b60b55a3e60`** (emitted by `build_items.py`, committed before any API call).
**Tests:** [`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md) — its **sole decisive test**, the matched-difficulty add-vs-cancel generalization battery.
**Yardstick fixed by (ratified):** [`decisions/resolved/constructional-monotonicity-generalization-operationalization`](../../../wiki/decisions/resolved/constructional-monotonicity-generalization-operationalization.md) (ADOPT-WITH-MODS, s134 autonomous adversarial review). This session **builds + runs**; it re-tunes nothing.
**Paradigm template:** [`result/conative-cancel-direction-v2`](../../../wiki/findings/results/conative-cancel-direction-v2.md) (the matched conflicting-cue design).
**Human anchor:** **none asserted — `internal-contrast-only`** (ratified, [`decisions/resolved/conflicting-cue-human-anchor`](../../../wiki/decisions/resolved/conflicting-cue-human-anchor.md)). No human-comparison claim; no human label invented. A3's anchored leg was **dropped** (prereq 4).

## The frozen pair (prereq 3) — a genuinely NEW add/cancel pair

| arm | construction | example | hypothesis | discriminating cell |
|---|---|---|---|---|
| **ADD** | resultative | "Maria hammered the metal flat." | "The metal became flat." | construction affirm = **add_no_cue** (license; want ceiling) |
| **CANCEL** | *for*-durative aspectual coercion of a semelfactive | "The light flashed for ten minutes." | "The light flashed only once." | **cancel_no_cue** = 1 − construction affirm (suppress; want high) |

**ADD verb pool (10):** beat, boil, cut, hammer, kick, paint, push, scrub, squeeze, wipe — the s133 calibration's headroom-clean resultative verbs, **excluding** trap verbs `freeze`, `sharpen` (telic; control at ceiling).
**CANCEL verb pool (7):** flash, knock, tap, blink, jump, cough, nod — semelfactive/punctual; **disjoint** from the add pool (MOD-1: `kick`, `bounce` removed) and de-duplicated (MOD-2: `blink` once).

Each arm × 3 conditions (the matched conflicting-cue paradigm):

- **ADD:** `control` (bare: "hammered the metal") / `construction` (resultative: "hammered the metal flat") / `cue` (explicit **denial**: "…flat, but the metal did not become flat" → follow-cue = **withhold**).
- **CANCEL:** `default` (bare: "The light flashed") / `construction` (*for*-durative: "…for ten minutes") / `cue` (explicit **re-assertion**: "…for ten minutes, but the light flashed only once" → follow-cue = **affirm**).

The add cue **denies** the licensed inference; the cancel cue **re-asserts** the suppressed default — mirror images, both deliberately internally-conflicting (as cc-v2's cue arm was).

51 items × 2 instruments (NLI primary + forced-choice) × 3 models (claude-sonnet-4.6 A, gpt-5.4-mini B, gemini-3.5-flash C) = **306 calls** for the full battery; the B2 calibration subset (12 items) is a separate, prior probe.

## FROZEN thresholds (prereq 2; set in the ratified decision before any data, NOT tunable after)

All read **panel NLI primary**; "≥2/3 models" = the per-model value clears the bar in ≥2 of 3.

**B2 blocking ceiling gate** — run on the frozen **calib subset** (4 add verbs {cut, hammer, kick, push} × {control, construction} + 4 cancel verbs {cough, flash, jump, nod} × {default}; `calib==1`), **before** the main read. The pair is **admitted** only if:
1. **Add headroom:** construction licensing-no-cue affirm **≥ 0.80** AND bare control affirm **≤ 0.40**, in ≥2/3 models.
2. **Cancel default (MOD-3, contestable):** lexical-default affirm ("only once") **≥ 0.80**, in ≥2/3 models.
A **NO-GO** on either → **re-pair the pair/coercion before spend** (do not relax the bar). The cancel suppression (construction) cell is held **out** of calib, so the asymmetry magnitude is not computable until the main run.

**Asymmetry direction (the "cliff" analogue, 20 pp).** On the no-cue cell:
- `add_no_cue − cancel_no_cue ≥ 0.20` in ≥2/3 → **CONFIRMS** (confirm-leg 1);
- `|add_no_cue − cancel_no_cue| < 0.20` in ≥2/3 → **SYMMETRIC** → falsifies;
- `cancel_no_cue − add_no_cue ≥ 0.20` in ≥2/3 → **REVERSAL** → falsifies.

**Instrument-fragility (confirm-leg 2, 10 pp).** The cancel arm's NLI-vs-FC disagreement on the no-cue cell must exceed the add arm's by **≥ 0.10** in ≥2/3 models.

**Cue-arm reading rule (inherited cc-v2, unchanged):** ≥ 0.70 follow-cue in ≥2/3 models = robust; ~chance / construction-following = informative partial-null. (Reported, not part of the headline asymmetry verdict.)

## Pre-registered outcomes (all first-class; the falsify arms are LIVE)

- **Confirms:** add_no_cue − cancel_no_cue ≥ 20 pp (≥2/3) **and** cancel more instrument-fragile (≥10 pp, ≥2/3) → the monotonicity asymmetry **generalizes** to the new pair; conjecture advances to `tested` (supported on this leg, `internal-contrast-only`).
- **Symmetric → falsifies:** once difficulty is matched, add and cancel no-cue are indistinguishable (<20 pp in ≥2/3).
- **Reversal → falsifies:** the new pair's cancel is easy / add hard (≥20 pp the other way in ≥2/3).
- A symmetric/reversal result is recorded as a **clean falsification** — **no re-pairing or re-tuning after seeing outputs** (the only legitimate re-pair is a B2 NO-GO, decided before the main read).

## Anti-cheat (binding)

- Items **frozen + sha256-hashed (`80bd4b60b55a3e60`) and committed before the first probe call**; no item/verb added, dropped, or re-binned after.
- All thresholds **frozen before any data** (in the ratified decision); verdicts read mechanically by `analyze_calib.py` (gate) and `analyze.py` (asymmetry / fragility / cue). No threshold tuned post-hoc.
- **Two-phase, gate-before-run:** (1) `probe.py --calib` → `analyze_calib.py` applies the B2 gate; (2) on GO, an **independent fresh-agent pre-run critic** reviews the frozen full set + this PREREG + the gate result and returns GO/NO-GO; (3) on GO, `probe.py` runs the full battery, read by the frozen thresholds.
- **Post-run**, an independent fresh agent recomputes every number from `raw/*.json` (separate from `analyze.py`).
- This session **runs** the battery; it ratifies nothing and re-tunes no threshold (the decision was ratified s134).

## Known limits (stated before data)

- **Small N, panel-as-subjects, single run.** 10 add + 7 cancel verbs × 3 conditions × 3 models; wide per-cell uncertainty. A direction-of-effect signal, not a magnitude or a human comparison.
- **`internal-contrast-only`.** No human baseline on any arm; the cancel "only once" default is contestable for humans → no human-level claim (the B2 gate is exactly what certifies the default is at ceiling *for these models*, not for people).
- **The cue arms are deliberately contradictory sentences** (anomalous); they test cue-following, not naturalistic inference, and are secondary to the no-cue headline.
- **Cancel marginality flagged:** `blink`/`nod`/`tap`/`knock` `for ten minutes` are grammatical but less natural than `flash`/`cough`/`jump`; the B2 gate (cancel default ≥ 0.80) is the pre-data check that the default is real, and the verdict reads the arm aggregate.
