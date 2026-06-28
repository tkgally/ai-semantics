---
type: result
id: monotonicity-c2-privative-calibration-v1
title: C2 privative B2 calibration — GO; bare-head-noun category membership IS a categorical entailment at ceiling (3/3 models, 1.00), unlike the s135/C1 defaults, so a privative cancel arm can be built at matched ceiling
meaning-senses:
  - constructional
  - inferential
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-28
updated: 2026-06-28
links:
  - rel: depends-on
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: refines
    target: result/monotonicity-c1-completion-calibration-v1
  - rel: depends-on
    target: concept/coercion
---

# Result: C2 privative-modifier B2 calibration — GO

> **Design-feasibility calibration, `internal-contrast-only`.** This records **STEP 1b**
> of the ratified cancel-arm re-design ([`decisions/resolved/monotonicity-cancel-arm-redesign`](../../decisions/resolved/monotonicity-cancel-arm-redesign.md)),
> reached on the C1 NO-GO ([`result/monotonicity-c1-completion-calibration-v1`](monotonicity-c1-completion-calibration-v1.md))
> after the **M2** conjecture-scope amendment. A fresh **B2 default-at-ceiling gate** on the
> **C2 privative** cancel direction: does a bare head noun entail its superordinate category
> ("Sam bought a gun" → "Sam bought a weapon")? The gate is a clean **GO** — affirm **1.00 in
> 3/3 models** under strict NLI. So a privative cancel arm **can** be built at matched ceiling,
> unblocking **STEP 2** (the matched asymmetry battery). Makes **no human-comparison claim**.
> Pre-registration, run record, every number:
> [`experiments/runs/2026-06-28-monotonicity-c2-privative-calibration/`](../../../experiments/runs/2026-06-28-monotonicity-c2-privative-calibration/README.md).

## Why this ran

STEP 1 (C1 telic-completion) was a measured B2 NO-GO: even simple-past accomplishment
completion is read as defeasible-not-categorical under strict NLI (0/3 models at ceiling).
The ratified decision pre-authorized the fallback: **C2 = privative-modifier cancellation**
("a gun" ⊨ "a weapon"; "a fake gun" cancels it) — "the cleanest, most ceiling-likely lexical
default" — but only **after M2**, a deliberate *written* broadening of the conjecture's scope
to admit a nominal/adjectival cancel arm and to record the add-verbal/cancel-nominal **domain
mismatch** as a live caveat. M2 was applied first
([`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md),
the "M2" blockquote). This is STEP 1b: calibrate the category default before building the
battery — measure, don't assume.

## What was measured

The frozen calibration (items.csv sha256[:16] **`39598ee7ad97f33d`**, committed before any
API call): **8 noun→category taxonomic entailments** — gun→weapon, diamond→gemstone,
rose→flower, tiger→animal, apple→fruit, pearl→jewel, sword→weapon, violin→musical
instrument. Default sentence = a bare-noun frame ("Sam bought a gun"); frozen category
hypothesis = the same frame with the head noun replaced by its category ("Sam bought a
weapon"). Each item's cancelling privative modifier (fake / artificial / toy / imitation /
plastic) was **frozen for STEP 2 but held out** of this calibration (anti-cheat). NLI primary
+ forced-choice, temperature 0, the panel claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash.
8 × 2 × 3 = **48 calls**.

**Frozen gate (STEP 1b, not relaxable):** category default affirm ≥ **0.80 in ≥2/3 models**,
strict NLI. An independent fresh-agent **pre-run critic** returned **GO** (and verified the M2
precondition was present and deliberate); an independent fresh-agent **post-run verifier**
recomputed every cell.

## One-line finding

**The gate is a clean GO: bare-head-noun category membership is affirmed at 1.00 in 3/3
models under strict NLI — every one of the 24 NLI category-default judgements is "entailment"
(label 0). Category membership IS a categorical entailment for the panel, in sharp contrast to
the s135 "only once" implicature (0.00, 3/3) and the C1 completion default (0.25 / 0.375 /
0.75). So a privative cancel arm can anchor a matched cancel arm at ceiling.**

## Numbers (verified)

Category-default affirm rate (n = 8 items per model); independently recomputed by the
post-run verifier — exact match to `raw_calib/gate.json`, 48/48 priced, 0 missing, 0 parse
failures, 0 errors.

| model | NLI affirm | FC affirm | gate target (NLI) | pass? |
|---|---|---|---|---|
| A — claude-sonnet-4.6 | **1.00** | 1.00 | ≥ 0.80 | ✓ |
| B — gpt-5.4-mini | **1.00** | 1.00 | ≥ 0.80 | ✓ |
| C — gemini-3.5-flash | **1.00** | 0.875 | ≥ 0.80 | ✓ |
| | | | **models ok: 3/3** | **GO** |

NLI label distribution: **label 0 (entailment) = 8/8 for every model**; no neutral, no
contradiction, anywhere. The single non-affirm across all 48 calls is gemini's
**forced-choice** "CANT_TELL" on *pearl* (NLI on the same item is entailment) — irrelevant to
the NLI-primary gate.

## The contrast this sharpens (bears on the conjecture's framing)

This is the third cancel-side default the project has now B2-calibrated, and the three line
up into a clean ranking of **which defaults these models hold as categorical entailments**:

| cancel default | what kind of inference | affirm (NLI, 3 models) | held at ceiling? |
|---|---|---|---|
| single-occurrence ("flashed" → "only once"), s135 | Gricean quantity **implicature** | 0.00 / 0.00 / 0.00 | no |
| completion ("built the house" → "finished building it"), C1 | aspectual default (defeasible) | 0.25 / 0.375 / 0.75 | no |
| category membership ("a gun" → "a weapon"), C2 | taxonomic **lexical entailment** | 1.00 / 1.00 / 1.00 | **yes** |

This is exactly the by-product the companion essay [`essay/nothing-to-cancel`](../essays/nothing-to-cancel.md)
anticipated: the recurring cancel-arm trouble has been **a map of which defaults the panel
holds as entailments** — and only the genuinely taxonomic one (category membership) sits at
ceiling. It vindicates the B2 gate's necessity: a fair cancel test needs a *held entailment*
as its target, and C2 is the first cancel direction to supply one at ceiling.

## What this does and does not license

- **Does:** establish, with a verified gate, that **C2 (privative) can anchor a matched
  cancel arm** at ceiling on the strict-NLI panel. It discharges STEP 1b and **unblocks
  STEP 2** (the matched asymmetry battery, reusing the frozen B2-passing resultative ADD arm,
  sha `80bd4b60b55a3e60`).
- **Does not:** test [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md).
  No asymmetry was read; the suppression (privative) cell was held out and no battery ran. The
  conjecture stays **`proposed`**.
- **Carries forward a live caveat (M2):** the C2 battery will pair a *verbal* ADD arm with a
  *nominal/adjectival* CANCEL arm, so any C2 asymmetry is across a **domain difference**, not a
  clean within-verbal contrast. Any STEP-2 result must state this prominently; the asymmetry it
  could show is between *constructional inference types across domains*, a broadened (and
  weaker) version of the original verbal-only bet.
- **Does not** make any human comparison (`internal-contrast-only`), nor re-tune any ratified
  threshold (the 0.80 floor is the decision's own STEP-1b gate, unchanged).

## What happens next (frozen by the decision)

**STEP 2** (only-on-GO, now reached): reuse the s135 frozen resultative ADD arm verbatim;
build the matched C2 privative cancel arm (default / construction / cue) in the same
conflicting-cue paradigm; freeze + sha256-hash the full set; re-run the full B2 gate on the
main-item calibration subset; obtain a fresh independent pre-run-critic GO; run the full
battery; read by the frozen s134 thresholds (asymmetry 20 pp; instrument-fragility ≥ 10 pp;
cue ≥ 0.70); post-run verifier recomputes. **M1:** the STEP-2 result must state that this B2
pass is what licenses reading any suppression failure as defeasance. The conjecture advances to
`tested` only after that battery runs.

## Provenance

- Every figure is reproduced verbatim from
  [`raw_calib/gate.json`](../../../experiments/runs/2026-06-28-monotonicity-c2-privative-calibration/README.md)
  and independently recomputed from the per-call `raw_calib/*.json` by a read-only post-run
  verifier (exact match; 48/48 priced, 0 missing, 0 parse failures).
- The s135 floor (0.00, 3/3) and C1 numbers (0.25 / 0.375 / 0.75) are quoted from
  [`result/monotonicity-generalization-b2-nogo-v1`](monotonicity-generalization-b2-nogo-v1.md)
  and [`result/monotonicity-c1-completion-calibration-v1`](monotonicity-c1-completion-calibration-v1.md).
  The C2 fallback, the M2 precondition, and the GO → STEP 2 routing are the ratified decision's
  own STEP 1b.
- Spend: **$0.01087 billed** (UTC 2026-06-28), the calibration probe only; no battery run.
