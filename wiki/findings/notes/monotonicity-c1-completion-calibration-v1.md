---
type: note
id: monotonicity-c1-completion-calibration-v1
title: C1 telic-completion B2 calibration — NO-GO; the completion default of a simple-past accomplishment is read as defeasible-not-categorical under strict NLI (0/3 models at ceiling), so even completion cannot anchor a matched cancel arm
meaning-senses:
  - constructional
  - inferential
status: recorded
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-28
updated: 2026-07-06
links:
  - rel: depends-on
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: refines
    target: note/monotonicity-generalization-b2-nogo-v1
  - rel: depends-on
    target: concept/coercion
---

# Result: C1 telic-completion B2 calibration — NO-GO

> **Reclassified 2026-07-06 (session 185, campaign P3 / program B6): result → note.** A design-feasibility B2 calibration (NO-GO); no asymmetry was read and it makes no human-comparison claim — a gate record. Per the `note` page type (CLAUDE.md) it carries **no new measurement about LLM meaning**; `status: recorded`. History-preserving reclassification — nothing measured, scoped, or decided on this page changes.

> **Design-feasibility calibration, `internal-contrast-only`.** This records **STEP 1**
> of the ratified cancel-arm re-design ([`decisions/resolved/monotonicity-cancel-arm-redesign`](../../decisions/resolved/monotonicity-cancel-arm-redesign.md)):
> a fresh **B2 default-at-ceiling gate** on the proposed **C1 telic-completion** cancel
> direction, run **before** any matched asymmetry battery is built. The gate is a
> **NO-GO**: the completion default of a simple-past accomplishment ("Maria built the
> house" → "Maria finished building the house") is **not** affirmed at the ≥ 0.80 ceiling
> under strict NLI in any of the three panel models. Per the frozen instruction this does
> **not** relax the bar; it routes to **STEP 1b (C2 privative)** after a written
> conjecture-scope amendment. Makes **no human-comparison claim** (within-model affirm
> rates only). Pre-registration, run record, every number:
> [`experiments/runs/2026-06-28-monotonicity-c1-completion-calibration/`](../../../experiments/runs/2026-06-28-monotonicity-c1-completion-calibration/README.md).

## Why this ran

The s135 B2 gate was a NO-GO on the ratified *for*-durative/semelfactive cancel arm:
the "only once" default floored at 0.00 in 3/3 models because single-occurrence is a
defeasible Gricean *implicature*, not a lexical entailment
([`note/monotonicity-generalization-b2-nogo-v1`](monotonicity-generalization-b2-nogo-v1.md)).
An independent adversarial review **ratified** a re-design
([`decisions/resolved/monotonicity-cancel-arm-redesign`](../../decisions/resolved/monotonicity-cancel-arm-redesign.md)):
**ADOPT C1 (telic-completion) conditional on its own B2 calibration**, with C2 (privative)
as the pre-authorized fallback and a principled-limit closure if both fail. The decision's
crux was that *completion* is a materially stronger default than single-occurrence — closer
to an aspectual entailment encoded in the predicate's event structure — **but is itself
somewhat defeasible** under strict NLI, so its default-at-ceiling is unverified and **must
be measured, not assumed** (the s135 lesson, one rung up). STEP 1 is exactly that
measurement.

## What was measured

The frozen calibration (items.csv sha256[:16] **`4e8c3935af154c46`**, committed before
any API call): **8 incremental-theme accomplishment verbs** — build, write, read, bake,
knit, mow, draw, dig — each with a quantized definite object, **disjoint** from the
resultative ADD pool. Default sentence = bare simple past ("Maria built the house");
frozen completion hypothesis = `"<Subject> finished <gerund> the <object>."` The
cancelling *for*-durative construction cell was held **out** (anti-cheat: the asymmetry
magnitude is not computable at the gate). NLI primary + forced-choice, temperature 0, the
panel claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash. 8 items × 2 instruments × 3
models = **48 calls**.

**Frozen gate (STEP 1, not relaxable):** completion default affirm ("finished V-ing")
**≥ 0.80 in ≥ 2/3 models**, strict NLI (label 0 = entailment).

An independent fresh-agent **pre-run critic** returned **GO** on the frozen design before
the probe ran; an independent fresh-agent **post-run verifier** recomputed every cell from
`raw_calib/*.json` after.

## One-line finding

**The gate is a NO-GO: the simple-past accomplishment's completion entailment is affirmed
at only 0.25 / 0.375 / 0.75 (claude / gpt-mini / gemini) under strict NLI — 0/3 models
reach the ≥ 0.80 ceiling. Even completion — a far stronger default than the s135 "only
once" — is read as defeasible-not-categorical under strict NLI, so it cannot anchor a
matched cancel arm.** (The failure is softer than s135's uniform floor, not a uniform
floor: gemini nearly clears, and the split is informative — see below.)

## Numbers (verified)

Completion-default affirm rate (NLI primary, n = 8 items per model); independently
recomputed by the post-run verifier — exact match to `raw_calib/gate.json`, 48/48 priced,
0 parse failures, 0 errors.

| model | NLI affirm | FC affirm | gate target (NLI) | pass? |
|---|---|---|---|---|
| A — claude-sonnet-4.6 | **0.25** | 0.25 | ≥ 0.80 | ✗ |
| B — gpt-5.4-mini | **0.375** | 0.125 | ≥ 0.80 | ✗ |
| C — gemini-3.5-flash | **0.75** | 0.75 | ≥ 0.80 | ✗ |
| | | | **models ok: 0/3** | **NO-GO** |

Per-model NLI **label distribution** (0 = entailment, 1 = neutral, 2 = contradiction),
verifier-recomputed:

| model | label 0 (entail) | label 1 (neutral) | label 2 (contradiction) |
|---|---|---|---|
| A — claude | 2 (bake, mow) | 4 (build, read, knit, draw) | **2 (write, dig)** |
| B — gpt-mini | 3 (build, bake, draw) | 5 (write, read, knit, mow, dig) | 0 |
| C — gemini | 6 (build, write, bake, knit, mow, draw) | 2 (read, dig) | 0 |

- **claude is the strictest:** it treats completion as a *non-entailment* for 6/8 verbs and
  as an active **contradiction** for 2 ("wrote the letter" ⊭⊨ "finished writing the
  letter"; same for "dug the tunnel") — reading the explicit *finish* predicate as adding a
  culmination event the bare past does not force.
- **gemini is the most permissive** (0.75), affirming completion for 6/8, but still short of
  ceiling and not at ceiling on read/dig.
- **gpt-mini sits in between on NLI (0.375) but drops to 0.125 on forced-choice** — the only
  model whose FC affirm falls *below* its NLI affirm here.

## Why this is a real result, not a bad verb pool

The pre-run critic confirmed all eight are genuine telic accomplishments with quantized
definite objects whose simple past plausibly entails culmination; the weak items (large
objects like *house*/*tunnel* that invite a "was building" coercion) bias affirm **down**,
which is conservative, never inflating. The split is **not** a verb artifact: it is a
cross-model disagreement about whether simple-past accomplishment culmination is a strict
entailment. Standard event semantics says a quantized accomplishment in the simple past
*does* entail culmination (the imperfective paradox is precisely that the **progressive**
does not), but these models — claude especially — decline to treat the bare past →
"finished V-ing" step as forced. The completion entailment is **defeasible-not-categorical
for the panel under strict NLI**, exactly the trap the decision flagged "one rung up."

## What this does and does not license

- **Does:** establish, with a clean verified gate, that **C1 (telic-completion) cannot
  anchor a matched cancel arm** on the project's strict-NLI panel — its default does not
  sit at ceiling. It discharges the decision's STEP-1 condition (a measured NO-GO) and
  routes to **STEP 1b (C2 privative)**.
- **Does:** sharpen a recurring pattern bearing on the conjecture's own framing
  (weigh-question 4 of the ratified decision; the thesis of
  [`essay/nothing-to-cancel`](../essays/nothing-to-cancel.md)): the cancel-side defaults the
  project has reached for — single-occurrence (s135) and now completion — are **inferences
  the panel does not hold as categorical entailments**. The "cancel side is hard" pattern is
  partly that there is *less held entailment to cancel* than a human-semantics intuition
  expects. This is a fact about the **instrument** (strict NLI) and the **models**, not yet
  about defeasance competence.
- **Does not:** test [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md).
  No asymmetry was read; the suppression cell was held out and no battery ran. The
  conjecture stays **`proposed`**.
- **Does not** make any human comparison (`internal-contrast-only`), nor re-open or re-tune
  any ratified threshold (the 0.80 floor is the decision's own STEP-1 gate, unchanged).

## What happens next (frozen by the decision)

The decision pre-authorized the C1-NO-GO path: **STEP 1b — C2 privative-modifier
cancellation**, but only **after M2**: a *written* amendment to the conjecture's scope
(broaden to include a nominal/adjectival privative cancel arm; relax the verbal-only
abstraction; flag the add-verbal/cancel-nominal domain mismatch as a live caveat). Then a
frozen privative B2 calibration ("a gun" ⊨ "a weapon"; "a fake gun" cancels it) under the
**same** ≥ 0.80 gate. A C2 GO unblocks STEP 2 (the matched battery, reusing the frozen
B2-passing resultative ADD arm, sha `80bd4b60b55a3e60`); a second NO-GO triggers the
**principled-limit closure** (the matched cancel arm is un-instrumentable at ceiling on a
strict-NLI panel without a categorically-held lexical-entailment default).

*[Pointer, s183: this path ran the same day — [`note/monotonicity-c2-privative-calibration-v1`](monotonicity-c2-privative-calibration-v1.md)
GO (s137), [`result/monotonicity-c2-battery-v1`](../results/monotonicity-c2-battery-v1.md) WEAK CONFIRM (s137),
then [`result/monotonicity-within-verbal-battery-v1`](../results/monotonicity-within-verbal-battery-v1.md)
CONFIRM 3/3 (s141, M2 discharged).]*

## Provenance

- Every figure is reproduced verbatim from
  [`raw_calib/gate.json`](../../../experiments/runs/2026-06-28-monotonicity-c1-completion-calibration/README.md)
  and independently recomputed from the per-call `raw_calib/*.json` by a read-only post-run
  verifier (exact match; 48/48 priced, 0 missing, 0 parse failures).
- The s135 floor (0.00, 3/3) and the resultative add-arm ceiling (1.00 / 0.00) are quoted
  from [`note/monotonicity-generalization-b2-nogo-v1`](monotonicity-generalization-b2-nogo-v1.md).
  The C1-conditional-on-calibration structure and the NO-GO → C2 routing are the ratified
  decision's own STEP 1.
- Spend: **$0.01151 billed** (UTC 2026-06-28), the calibration probe only; no battery run.
