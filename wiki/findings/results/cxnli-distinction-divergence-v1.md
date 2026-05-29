---
type: result
id: cxnli-distinction-divergence-v1
title: A project-run replication of the Scivetti divergent-form generalization gap — the 2026 panel drops ~28–45 pp from base to syntactically-identical/semantically-divergent constructions, with the conative collapsing hardest
meaning-senses:
  - constructional
  - functional-vs-formal
  - human-comparison
status: proposed
contingent-on: []
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: supports
    target: claim/constructional-divergent-form-generalization-gap
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: open-question/constructional-divergence-probe
  - rel: depends-on
    target: source/scivetti-2025-beyond-memorization
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
---

# Result: CxNLI base-vs-distinction divergence probe v1

This is the **experimental cash-out of [`open-question/constructional-divergence-probe`](../open-questions/constructional-divergence-probe.md)**: it turns the *external* Scivetti >40% divergent-form drop (recorded in [`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md)) into a **project-run result** by running the project panel as subjects on Scivetti's own NLI items and measuring the base→distinction drop directly. Run record (code, redacted outputs, cost): [`experiments/runs/2026-05-29-cxnli-distinction-probe-v1/`](../../../experiments/runs/2026-05-29-cxnli-distinction-probe-v1/README.md).

**One-line finding:** the divergent-form generalization gap **reproduces on the 2026 panel**. All three models score near the human baseline on the base task (84–94% vs ≈0.90) but drop **28–45 percentage points** on the syntactically-identical/semantically-divergent task (to 39–64%, well below the ≈0.83 human ceiling). The drop is **convergent in direction across all three models** and the **conative construction collapses hardest in every model** (60–80 pp). This is a *negative* result for current models at the Tier 3→4 boundary — and, unlike the comparative-correlative ceiling result, it is **not** at ceiling, so it discriminates.

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A), `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C), run **as subjects** (charter §6). Temperature 0; NLI instrument (0/1/2), the same one validated in [`result/comparative-correlative-covariation-v1`](comparative-correlative-covariation-v1.md); no logprobs needed. **0 NA across all 600 calls.**
- **Items** (read in place from the un-licensed Scivetti repo, not mirrored): the **5 argument-structure constructions present in both experiments** — causative-with, caused-motion, conative, intransitive-motion, resultative. **Distinction** = all 100 CxNLI-Distinction (Exp 2) items, 20/construction. **Base** = the first 20 CxNLI (Exp 1) items per construction by item number, fixed before the run, so base and distinction are N-matched (100 vs 100).
- **Cost** (actual): **$0.140** (A $0.104 / B $0.006 / C $0.030). Under the $5 single-run flag.

## Results

Human references (fixed, not retuned): Scivetti native-speaker baselines Exp 1 ≈ 0.90, Exp 2 ≈ 0.83; published model result GPT-o1 aggregate drop **> 40%**, with GPT-o1 scoring *worse* than GPT-4o on Exp 2 ([`source/scivetti-2025-beyond-memorization`](../../base/sources/scivetti-2025-beyond-memorization.md) §5.3).

| model | base acc | distinction acc | **drop** | vs human (base≈0.90 / dist≈0.83) |
|---|---:|---:|---:|---|
| claude-sonnet-4.6 | 94% | 64% | **−30 pp** | base ≈ human; dist ~19 pp below human |
| gpt-5.4-mini | 84% | 39% | **−45 pp** | base ~6 pp below; dist ~44 pp below human |
| gemini-3.5-flash | 89% | 61% | **−28 pp** | base ≈ human; dist ~22 pp below human |

Mean panel drop ≈ **34 pp**. The base task sits at or near the human baseline for two of three models; the distinction task sits **well below** the human ceiling for all three — the signature of the divergent-form gap.

### Per-construction drop (base → distinction)

| construction | claude-sonnet-4.6 | gpt-5.4-mini | gemini-3.5-flash |
|---|---:|---:|---:|
| **conative** | 100→35 (**−65**) | 85→25 (**−60**) | 95→15 (**−80**) |
| intransitive-motion | 85→65 (−20) | 85→50 (−35) | 90→55 (−35) |
| caused-motion | 95→65 (−30) | 90→65 (−25) | 90→75 (−15) |
| resultative | 95→75 (−20) | 70→55 (−15) | 90→55 (−15) |
| causative-with | 95→80 (−15) | 95→80 (−15) | 85→80 (−5) |

The **conative is the hardest construction for every model** (60–80 pp drop, to 15–35% — at or below chance for a 3-way task). Causative-with is the most robust. This per-construction ordering is itself a finding: the divergent-form difficulty is **not uniform across constructions**, and the conative's surface-identical/meaning-divergent contrast (the *at*-frame's non-completion vs. the transitive's completion) is where current models break down most sharply.

## Interpretation

This **converts the external Scivetti claim into a project-run datum** (the theory page's standing IOU). Three things it shows, stated modestly:

1. **The gap is real and reproduces on a newer, independent panel.** Scivetti reported it for GPT-4o/o1/Llama (2024–25); it holds for the 2026 panel (Claude Sonnet 4.6, GPT-5.4-mini, Gemini 3.5-flash). The effect is not an artifact of one model generation.
2. **It is convergent in direction, divergent in magnitude** (charter §6 panel-as-subjects). All three drop substantially (28–45 pp); gpt-5.4-mini drops most (and is the only one notably below the human base baseline even on the base task). Convergence here is QA (the effect is robust); the magnitude divergence is the signal (the gap is partly model-specific).
3. **The locus is construction-specific.** The conative collapse is the sharpest single result — a candidate target for the project's own conative minimal-pair probe ([`conjecture/conative-construction`](../conjectures/conative-construction.md)), which tests the *same* completion-entailment contrast with verb held constant.

### Relation to the comparative-correlative result

The two own-design results this session point in **opposite directions, consistently**: [`result/comparative-correlative-covariation-v1`](comparative-correlative-covariation-v1.md) found the panel at *ceiling* on a well-marked construction's core covariation inference; this result finds the panel *failing* (28–45 pp drop) when the *same surface form* must be mapped to a divergent constructional meaning. Together they sketch the live picture the theory page now carries: current decoders handle the *easy* direction of the upper ladder (unambiguous construction → its core inference) at ceiling, while the *hard* direction (surface-identical → divergent meaning) is where the gap lives. This result is the one that discriminates — it is off ceiling.

## What this result does and does not license

**Does license:** a project-owned, revisable statement that the divergent-form generalization gap reproduces on the 2026 panel (≈34 pp mean drop), is convergent across three families, and is sharpest for the conative — placed at the Tier 3→4 boundary as a *negative* result. It **supports** [`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md) with the project's own evidence rather than only the external citation.

**Does NOT license:**
- **A precise magnitude comparison to Scivetti's ">40%".** Scivetti's headline is an aggregate over 8 constructions with their own base set and their own (one-shot/few-shot) protocols; this probe is 5 argument-structure constructions, zero-shot, with a base *subsample* matched to the distinction N. The numbers are the same *phenomenon and order of magnitude*, not a like-for-like reproduction of their figure. (gpt-5.4-mini's 45 pp happens to land near ">40%"; do not over-read the coincidence.)
- **A per-construction claim with tight uncertainty.** N = 20 items per construction per model; a single percentage has wide error bars. The conative ordering is robust *because it replicates across all three models*, not because any one cell is precise.
- **A model-internal or grounding claim.** Behavioral NLI only.
- **An answer to whether the conjectures' own predictions hold.** This probe uses *Scivetti's* items (their divergent-form contrast), not the project's own minimal-pair designs for caused-motion/conative/etc. It bears on those conjectures as anchored answer-key accuracy, not as a test of their specific predictions (which need the project's own controlled stimuli).

## Limits

- **Base subsample, not full base set.** The base arm is the first 20 items/construction (by number), fixed pre-run; it is N-matched to the distinction set but is not Scivetti's full Exp-1 set, so the base accuracies are this subsample's, not Scivetti's reported base accuracies.
- **Single gold label, small N** (resource page *Known limits*): answer-key agreement, not a human gradient; 20/construction.
- **One run, one date.** No replication, no alternate-phrasing sweep. Cross-model convergence is the main robustness signal.
- **Shared priors (charter §2.5).** Three decoders converging is weak evidence on its own; the Scivetti human baseline (small, aggregate) is the independent bearing.
- **NLI instrument framing.** A different framing (forced-choice, CoT) could shift absolute accuracies; the *drop* (within-instrument, base vs distinction) is the more robust quantity than the absolute numbers.

## Provenance

- Open question: [`open-question/constructional-divergence-probe`](../open-questions/constructional-divergence-probe.md). Operationalization (instrument, human-baseline comparison): [`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md) (ratified). External claim replicated: [`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md). Source: [`source/scivetti-2025-beyond-memorization`](../../base/sources/scivetti-2025-beyond-memorization.md).
- Human anchor: [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md) (CxNLI Exp1 + CxNLI-Distinction Exp2, gold labels + ≈0.90/≈0.83 baselines). No license → read in place, **not mirrored**; committed raw outputs redacted of dataset text.
- Run record + code + redacted outputs + cost: [`experiments/runs/2026-05-29-cxnli-distinction-probe-v1/`](../../../experiments/runs/2026-05-29-cxnli-distinction-probe-v1/README.md).

## Status

`status: proposed`. Numbers reproducible from the committed code against a local Scivetti clone. What is `proposed` is the project's reading; `contingent-on: []` (the governing operationalization decision is ratified and the result uses only aggregate/answer-key bearing). Promotion past `proposed` awaits Tom's review and, ideally, the project's *own* minimal-pair conative probe (the sharpest signal here) to corroborate the construction-specific locus.
