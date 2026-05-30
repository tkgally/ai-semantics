---
type: design
id: comparative-correlative-v3
title: comparative-correlative probe v3 — embedded CC under negation / epistemic modality (operator-scope wedge)
meaning-senses:
  - constructional
  - inferential
  - functional-vs-formal
status: provisional
anchor: pending
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: refines
    target: design/comparative-correlative-v2
  - rel: operationalizes
    target: conjecture/comparative-correlative-construction
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
---

# Design — comparative-correlative probe v3 (embedded CC / operator scope)

**The embedded-CC arm the [`design/comparative-correlative-v2`](comparative-correlative-v2.md) deferred.** Governed by the ratified [`decisions/resolved/cc-v2-difficulty-operationalization`](../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md) (which unified the v2 difficulty gate and said explicitly "...defer embedded-CC to v3..."). **No new decision.** Internal-contrast-only (`anchor: pending`, tracked by [`decisions/open/conflicting-cue-human-anchor`](../../wiki/decisions/open/conflicting-cue-human-anchor.md)).

## Why

[`result/comparative-correlative-covariation-v1`](../../wiki/findings/results/comparative-correlative-covariation-v1.md) and [`result/comparative-correlative-covariation-v2`](../../wiki/findings/results/comparative-correlative-covariation-v2.md) found the CC's proportional-covariation reading robust at/above ceiling — including multi-step composition and following the construction against conflicting world knowledge. Both probed the CC as an **asserted** relation. v3 asks the sharper *meaning-vs-template* question: when the identical `the more X, the more Y` is placed **under an operator that cancels or suspends its assertion** — sentential **negation** ("it is not the case that…") or **epistemic hedging** ("it remains unproven whether…") — does the model track the operator scope (withhold the bare covariation direction), or fire a surface "the-more…the-more → INCREASE" template regardless?

A template-firer affirms the positive direction everywhere. A model deploying the covariation *meaning* + operator scope withholds it under negation/modality. This is a cleaner probe of `functional-vs-formal` competence than the v2 conflicting-cue arm: there the cue was world knowledge (extra-linguistic); here the cancelling operator is **inside the sentence**, so the test is purely compositional-semantic.

## Instrument (reused verbatim from v1/v2)

NLI hypothesis is **always** the positive covariation "As `<dim1>` increases, `<dim2>` increases."; FC asks INCREASE / DECREASE / UNDETERMINED for `<dim2>` as `<dim1>` increases. Temperature 0, no logprobs → existing 3-family behavioral panel ([`config/models.md`](../../config/models.md)).

## Arms (graded ladder; golds frozen pre-run in `build_items.py`)

| arm | d | what it tests | FC gold | NLI gold |
|---|---|---|---|---|
| `baseline-pos` | 1 | plain positive CC, asserted (ceiling anchor) | INCREASE | 0 |
| `baseline-inv` | 1 | plain inverse CC, asserted — **direction anchor**, guards against an INCREASE-bias readout (the gap v2's set lacked) | DECREASE | 2 |
| `negation` | 2 | **the key manipulation** — negated positive CC; the positive covariation is denied | UNDETERMINED | 2 |
| `modal-epistemic` | 2 | epistemically-hedged positive CC; relation merely possible, not asserted | UNDETERMINED | 1 |
| `negation-inv` | 3 | negated *inverse* CC — **control vs a flat "see 'not' → UNDETERMINED" rule** (negating a decrease does not entail an increase) | UNDETERMINED | 1 |

The two golds are decoupled per arm (the embedded arms separate them). FC gold = UNDETERMINED is uniform across embedded arms — the least gold-contestable readout, so **FC is the primary instrument** for the embedded arms; NLI is secondary (its finer 2/1/1 encoding is defensible but pragmatically debatable — flagged for the pre-run critic).

## Reading rule (ratified report-the-rate; no manufactured pass bar)

- **Embedding-cancellation rate** — over the embedded arms, fraction where the model does *not* answer the bare positive direction (FC ≠ INCREASE / NLI ≠ 0): the off-template signal.
- Per-arm operator-correct rate.
- Degradation shape across d1<d2<d3.

No threshold tuned after the run. The discriminating cross-cut: a "the-more…the-more → INCREASE" template-firer passes `baseline-pos` but fails `baseline-inv`/`negation`/`modal`/`negation-inv`; a flat "any 'not' → UNDETERMINED" heuristic fails `baseline-inv` (no "not") and the `negation` NLI gold (2, not 1).

## Human anchor

**Pending / internal-contrast-only.** The Scivetti CC subset has no negated / hedged CC items → no in-repo human norm on the embedded arms → no human-level claim. The baseline arms keep the v1/v2 phenomenon-level Scivetti CC anchor. No human label invented.

## Pre-registration

Items frozen + committed **before any probe call** (`items.csv` sha256[:16] `98d1fd150e36fe30`); per-arm golds cross-checked against `ARM_NLI`/`ARM_FC` by an `assert` in `build_items.py`. An independent read-only adversarial pre-run critique re-derives every gold from the sentence text before the run.
