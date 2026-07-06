---
type: note
id: instrument-disagreement-reanalysis-v1
title: Instrument-disagreement re-analysis — per-model, per-construction NLI vs forced-choice divergence across two existing runs
meaning-senses:
  - constructional
  - inferential
  - functional-vs-formal
status: recorded
contingent-on: []
created: 2026-05-30
updated: 2026-07-06
links:
  - rel: refines
    target: result/conative-minimal-pair-divergence-v1
  - rel: refines
    target: result/argument-structure-coercion-v2
  - rel: supports
    target: open-question/instrument-sensitivity-constructional-inference
  - rel: depends-on
    target: result/conative-minimal-pair-divergence-v1
  - rel: depends-on
    target: result/argument-structure-coercion-v2
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
---

# Result: instrument-disagreement re-analysis v1

> **Reclassified 2026-07-06 (session 185, campaign P3 / program B6): result → note.** A read-only re-analysis across two existing runs (no new API calls, $0) — a structured summary of existing data, not a new experiment. Per the `note` page type (CLAUDE.md) it carries **no new measurement about LLM meaning**; `status: recorded`. History-preserving reclassification — nothing measured, scoped, or decided on this page changes.

A read-only re-analysis of two existing parent runs — **no new API calls, $0.00 spend** — that turns the anecdotal gpt-5.4-mini/conative cross-instrument divergence into a systematic per-model × per-construction **instrument-disagreement statistic**. Design: [`experiments/runs/2026-05-30-instrument-disagreement-reanalysis/`](../../../experiments/runs/2026-05-30-instrument-disagreement-reanalysis/README.md). All numbers in this page are recomputed by `analyze.py` from the committed `raw/results.json` of each parent run.

**Lead caveat:** two parent runs, three models, small item counts (N = 12 verbs / 10 stems per construction), single dates. The instrument-disagreement statistic here is **descriptive, not inferential** — no significance test is computed or claimed. This is a structured summary of existing data, not a new experiment.

**Anchor note:** this page carries an `anchors:` link to [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md), the same resource that anchors the parent conative result. The Scivetti CxNLI conative subset establishes the human-anchored construction contrast (≈0.90/0.83 native-speaker baseline) against which the behavioral panel is read. The instrument-disagreement statistic is computed on behavioral outputs from stimuli in that anchored domain; the resource's grounding role is indirect (via the parent result and the conative verb-class inventory), not item-matched to this re-analysis. Orchestrator note: if this indirect anchor is insufficient, a direct anchor decision should be queued — but the indirect chain is strong enough to avoid fabricating a separate resource.

## What was computed

**Instrument-disagreement statistic**, per model × construction × run:
- **Signed** = NLI_gap − FC_gap (negative = FC shows a larger gap than NLI)
- **Absolute** = |NLI_gap − FC_gap|

The "gap" is defined to match each parent run's primary statistic:
- Conative run: transitive_affirm − conative_affirm (the conjecture's P1 quantity)
- Coercion v2: canonical_minus_cue_drop (the H-deep vs H-default discriminator)

Sanity-check targets (from parent result pages):
- Conative FC gaps: 42–88 pp in 3/3 models (raw: 41.7, 66.7, 87.5 pp — consistent; 41.7 rounds to 42 pp)
- Conative NLI gaps: 54–67 pp in 2/3; gpt ~−8 pp (raw: 54.2, −8.3, 66.7 pp — consistent)
- All sanity checks **PASSED**; recomputed values reconcile with the parent result pages.

## Results

### Table 1: Conative probe

Instrument disagreement on the transitive−conative gap. NLI_gap = transitive_affirm − conative_affirm under NLI; FC_gap = same under forced-choice.

| model | NLI trans | NLI conative | NLI gap | FC trans | FC conative | FC gap | signed (NLI−FC) | abs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| claude | 100.0% | 45.8% | +54.2 pp | 100.0% | 33.3% | +66.7 pp | −12.5 pp | 12.5 pp |
| gpt | 91.7% | 100.0% | −8.3 pp | 91.7% | 50.0% | +41.7 pp | −50.0 pp | **50.0 pp** |
| gemini | 100.0% | 33.3% | +66.7 pp | 100.0% | 12.5% | +87.5 pp | −20.8 pp | 20.8 pp |

### Table 2: Coercion v2

Instrument disagreement on the canonical−cue drop. NLI_drop = canonical_affirm − cue_affirm under NLI; FC_drop = same under forced-choice.

| model | construction | NLI canon | NLI cue | NLI drop | FC canon | FC cue | FC drop | signed (NLI−FC) | abs |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| claude | caused-motion | 100.0% | 0.0% | +100.0 pp | 100.0% | 0.0% | +100.0 pp | +0.0 pp | 0.0 pp |
| claude | way | 100.0% | 0.0% | +100.0 pp | 100.0% | 10.0% | +90.0 pp | +10.0 pp | 10.0 pp |
| gpt | caused-motion | 80.0% | 0.0% | +80.0 pp | 80.0% | 10.0% | +70.0 pp | +10.0 pp | 10.0 pp |
| gpt | way | 70.0% | 0.0% | +70.0 pp | 80.0% | 20.0% | +60.0 pp | +10.0 pp | 10.0 pp |
| gemini | caused-motion | 100.0% | 0.0% | +100.0 pp | 100.0% | 0.0% | +100.0 pp | +0.0 pp | 0.0 pp |
| gemini | way | 100.0% | 20.0% | +80.0 pp | 100.0% | 20.0% | +80.0 pp | +0.0 pp | 0.0 pp |

### Table 3: Summary (compact)

| model | construction | run | NLI gap | FC gap | abs disagree |
|---|---|---|---:|---:|---:|
| claude | conative | conative-v1 | +54.2 pp | +66.7 pp | 12.5 pp |
| gpt | conative | conative-v1 | −8.3 pp | +41.7 pp | **50.0 pp** |
| gemini | conative | conative-v1 | +66.7 pp | +87.5 pp | 20.8 pp |
| claude | caused-motion | coercion-v2 | +100.0 pp | +100.0 pp | 0.0 pp |
| claude | way | coercion-v2 | +100.0 pp | +90.0 pp | 10.0 pp |
| gpt | caused-motion | coercion-v2 | +80.0 pp | +70.0 pp | 10.0 pp |
| gpt | way | coercion-v2 | +70.0 pp | +60.0 pp | 10.0 pp |
| gemini | caused-motion | coercion-v2 | +100.0 pp | +100.0 pp | 0.0 pp |
| gemini | way | coercion-v2 | +80.0 pp | +80.0 pp | 0.0 pp |

## Headline finding

**Large instrument disagreement (50.0 pp) is confined to gpt-5.4-mini on the conative construction.** All other eight cells — covering claude and gemini on conative, and all three models × both constructions in coercion-v2 — show absolute disagreement of ≤20.8 pp, with the coercion-v2 cells uniformly ≤10 pp (mostly 0 or 10 pp).

**Instrument fragility is not pervasive.** Seven of nine cells show agreement within what is plausibly measurement noise for this item size (≤20.8 pp). The exception is gpt/conative (50 pp), which reproduces the original anecdote and makes it systematic: this is a specific cell, not a general property of the instrument pair or the panel.

**Direction is consistent across the conative run:** the signed statistic is negative in all three conative cells (NLI gap < FC gap), meaning FC systematically elicits a larger conative-vs-transitive contrast than NLI for all three models. The magnitude of this NLI-to-FC underestimation differs radically across models — trivially for claude/gemini (12.5 and 20.8 pp), catastrophically for gpt (50.0 pp, whose NLI gap reverses sign). For coercion-v2, the signed values are 0–10 pp, with no consistent direction.

## Interpretation (modest)

1. **The gpt/conative NLI collapse is not a global instrument artifact.** If NLI systematically depressed all models' conative gaps relative to FC, we would expect large absolute disagreement across the board. We do not. Claude and gemini show modest disagreement (12.5 and 20.8 pp) in the same direction, suggesting a mild NLI-default-toward-contact pull that is model-amplified in gpt. The 50 pp gpt gap is better described as gpt-specific instrument-fragility than as NLI-is-always-worse.

2. **The add-direction constructions (coercion-v2) are instrument-stable across all three models.** Caused-motion and way canonical→cue drops range 70–100 pp under both instruments, with disagreement ≤10 pp in every cell. These constructions are near-ceiling under canonical conditions, and the cue knocks them to near-floor under both instruments — leaving little room for instrument-specific variance. The small absolute disagreements here are consistent with ceiling/floor compression rather than genuine instrument invariance; a harder probe at intermediate difficulty would be a more demanding stability test.

3. **Cancel-direction vs. add-direction asymmetry in instrument sensitivity.** The conative (cancel-direction) shows larger instrument disagreement than the two add-direction constructions (caused-motion, way) in the coercion-v2 run. This is consistent with the open question's hypothesis that cancel-direction constructions are harder and more instrument-sensitive — but the pattern is also consistent with a difficulty × ceiling confound: the add-direction items were already at or near ceiling on both instruments, where disagreement is arithmetically compressed. Whether the asymmetry is structural (cancel is harder and more elicitation-dependent) or artifactual (add items happen to be ceiling) is not resolvable from this data.

4. **The NLI-default-toward-contact interpretation is plausible but not proven.** The conative NLI gap is smaller than the FC gap for all three models (signed always negative). This pattern is consistent with NLI pulling toward a "yes-contact" default (the gpt result is the extreme of this pull). But the direction could also reflect differences in how each instrument frames the judgment rather than a default-bias; distinguishing these interpretations would require a design where the expected direction of instrument bias varies across items.

## What this licenses / does not license

**Licenses:** a project-owned, structured summary stating that instrument disagreement in this panel is **concentrated in one model × construction cell** (gpt/conative, 50 pp), with all other cells showing ≤20.8 pp absolute disagreement. This advances [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md) by supplying the named systematic statistic that page explicitly called for.

**Does NOT license:**
- **A general claim that "NLI understates constructional competence."** Only three models, two runs, two constructions (one cancel, two add); the direction of understatement is consistent within the conative run but that run's add-direction evidence is ceiling-compressed.
- **A causal account of why gpt diverges.** The 50 pp disagreement is a behavioral summary, not an explanation of what internal feature of gpt-5.4-mini makes it instrument-sensitive on the conative. That question remains open.
- **Inferential statistics or significance claims.** No test was run; N is small (12 verbs / 10 stems per construction, single run per parent). The disagreement statistics are descriptive.
- **A model-internal or grounding claim.** Behavioral only.

## Limits

- **Two parent runs, three models, small N.** The coercion-v2 cells each rest on 10 stems per construction; the conative cells on 12 verbs (24 items/frame). Instrument disagreement computed from this N is noisy.
- **Single dates for both parent runs** (both 2026-05-29). No test-retest reliability.
- **Ceiling/floor compression in coercion-v2.** The 0–10 pp disagreement in the add-direction cells partly reflects both instruments returning near-ceiling canonical and near-floor cue rates, which arithmetically bounds the disagreement regardless of whether the instruments genuinely agree.
- **No third instrument.** The two-instrument comparison cannot determine which (if either) is the more valid measure. The open question's framework treats this as an unresolved operationalization question.
- **The coercion-v2 gap metric (canonical→cue drop) is not fully parallel to the conative gap metric (transitive−conative gap).** Both are the parent run's primary discriminator statistic, but they operationalize different things — one measures sensitivity to constructional framing, the other measures cue-respect. Comparing magnitudes across runs is therefore approximate.

## Provenance

- **Data:** committed `raw/results.json` from each parent run (see inputs in [`experiments/runs/2026-05-30-instrument-disagreement-reanalysis/README.md`](../../../experiments/runs/2026-05-30-instrument-disagreement-reanalysis/README.md)).
- **Script:** `experiments/runs/2026-05-30-instrument-disagreement-reanalysis/analyze.py` — stdlib only; every number in this page is reproducible by running it.
- **Parent results:** [`result/conative-minimal-pair-divergence-v1`](../results/conative-minimal-pair-divergence-v1.md) (run commit `acbcdc4`) and [`result/argument-structure-coercion-v2`](../results/argument-structure-coercion-v2.md) (run commit `1f27d92`).
- **Open question advanced:** [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md).

## Status

`status: proposed`. Anchored (indirectly) to [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md) via the parent conative result's constructional domain (see Anchor note above). `contingent-on: []`. Numbers reproducible from committed `analyze.py` + parent `raw/results.json`. Promotion past `proposed` awaits Tom's review. *(Governance note, s183: since the autonomous-era amendment of 2026-06-12 — [`PROJECT.md`](../../../PROJECT.md) §12.3 — promotion runs by autonomous cross-session adversarial review; Tom holds a standing override.)*
