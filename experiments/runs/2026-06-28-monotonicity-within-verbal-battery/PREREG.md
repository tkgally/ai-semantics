# PREREG — within-verbal matched ADD-vs-CANCEL monotonicity battery (2026-06-28, session 141)

**Frozen before any API call.** The decisive **within-verbal** generalization test of
[`conjecture/constructional-monotonicity-asymmetry`](../../../wiki/findings/conjectures/constructional-monotonicity-asymmetry.md):
both arms are **verbal**, so a positive asymmetry is the clean within-verbal confirm that
**discharges the M2 domain mismatch** the weak C2 confirm carries. Governed by the **ratified
operationalization** ([`decisions/resolved/constructional-monotonicity-generalization-operationalization`](../../../wiki/decisions/resolved/constructional-monotonicity-generalization-operationalization.md))
and the **frozen s134 thresholds** — no new decision is opened, the yardstick is fixed.
`internal-contrast-only`.

## Why this is the test (and what makes it within-verbal)

The s137 C2 battery confirmed the asymmetry only across a **verbal-add / nominal-cancel domain
mismatch** (M2) — its cancel default was taxonomic ("a gun" ⊨ "a weapon"). Sessions 139–140
removed that compromise: s139 B2-confirmed a **verbal** held default (causative-inchoative result,
NLI 1.00 3/3), and s140 showed the **progressive** genuinely suppresses it (NLI cancel_no_cue
66.7/66.7/33.3 pp; cue re-licenses). So this battery pairs the frozen **verbal** resultative ADD
arm with the **verbal** progressive CANCEL arm — a clean within-verbal contrast.

## Frozen design

- **Frozen item set:** `experiments/data/monotonicity-within-verbal-battery/items.csv`, sha256[:16]
  **`2c0d4f70f28bb1c4`**. 48 items = **30 add (verbatim s135, sha `80bd4b60b55a3e60`, self-checked)
  + 18 cancel** (6 s140 causative-inchoative verbs × default/construction/cue, identical strings to
  the s140 frozen calibration sha `5ba8a996fa70cf55`).
- **Matched conflicting-cue paradigm** (template conative-cancel-v2 / the s137 C2 battery):
  - **ADD**: control "Maria beat the cream." / construction "Maria beat the cream stiff."
    (licensing = `add_no_cue`) / cue "…stiff, but the cream did not become stiff." (explicit DENIAL).
  - **CANCEL**: default "Sam broke the vase." (B2 anchor) / construction "Sam was breaking the
    vase." (suppression; `cancel_no_cue` = 1 − affirm) / cue "…the vase, and the pieces scattered
    across the floor." (explicit RE-ASSERTION).
- **Instruments:** NLI (primary) + FC, temperature 0, the ratified panel. 48 × 2 × 3 = **288 calls**.

## Frozen thresholds (ratified s134, UNTOUCHED — not tunable here)

- **B2 gate** (calib subset, read first, NLI primary): add construction ≥ **0.80** AND add control
  ≤ **0.40**; cancel default ≥ **0.80**; each in ≥ 2/3 models. (M1: the cancel default-at-ceiling
  pass licenses reading a suppression failure as **defeasance**.)
- **Asymmetry** (leg 1): `add_no_cue − cancel_no_cue` ≥ **0.20** in ≥ 2/3 → **CONFIRMS**;
  |·| < 0.20 → **SYMMETRIC** (falsifies); ≤ −0.20 → **REVERSAL** (falsifies).
- **Instrument-fragility** (leg 2): cancel NLI-vs-FC disagreement − add's ≥ **0.10** in ≥ 2/3.
- **Cue**: ≥ **0.70** follow-cue in ≥ 2/3 = robust.

## Pre-stated expectation (honest; the run decides)

The s140 numbers predict a CONFIRM (add licensing ~ceiling from s137's 1.00; cancel suppression
NLI 66.7/66.7/33.3 pp → asymmetry ~0.33/0.33/0.67, ≥ 0.20 in 3/3). But a **symmetric** or
**reversal** outcome is a live **falsification** arm and would be reported as such. The
**per-verb** cancel breakdown is reported (s140 found `shattered`/`melted` resist; `dissolved`
clean) — **not averaged away**, and **no verb is dropped** to inflate suppression (that would be
operationalization-tuning, PROTOCOL §8).

## Anti-cheat

- CSV frozen + sha256-hashed before any call; the ADD arm is byte-for-byte verbatim (the build
  asserts the source sha `80bd4b60b55a3e60`).
- Thresholds are the **frozen ratified s134** set — not set or tuned by this session.
- **Design note (disclosed):** unlike the C2 battery's two-stage build (separate B2 calib with the
  suppression cell held out), this runs all cells in one pass; the analyzer reads the **B2 gate
  first** and the asymmetry is meaningful only on a B2 GO. This is safe because the thresholds are
  frozen and the reading rule is committed here before the run; nothing is tuned after data. The B2
  cells are the same strings already B2-confirmed in s139/s135/s137.

## Procedure

1. `python3 build_items.py` — freeze + hash. ✅ (sha `2c0d4f70f28bb1c4`)
2. Independent fresh-agent **pre-run critic** GO/NO-GO (verify ADD verbatim by diff, thresholds
   un-tuned, per-verb discipline, M2-discharge logic).
3. On GO: `OPENROUTER_API_KEY=… python3 probe.py` (288 calls), then `python3 analyze.py` →
   `raw/results.json`.
4. Independent fresh-agent **post-run verifier** recomputes B2 + asymmetry + fragility + cue +
   per-verb, and runs a **leave-one-out** over the 6 cancel verbs.
5. Write [`result/monotonicity-within-verbal-battery-v1`](../../../wiki/findings/results/monotonicity-within-verbal-battery-v1.md);
   advance the conjecture per the frozen rule (M2 discharge stated).

## Human anchor

None. Within-model matched contrast, `internal-contrast-only`; no human-comparison claim.
