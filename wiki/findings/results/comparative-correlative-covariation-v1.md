---
type: result
id: comparative-correlative-covariation-v1
title: The form/meaning dissociation Weissweiler 2022 found for encoder PLMs on the comparative correlative does not appear in the 2026 decoder panel — covariation inference is at ceiling, including inverse-direction and absurd-pair items
meaning-senses:
  - constructional
  - inferential
  - functional-vs-formal
  - human-comparison
status: proposed
contingent-on: []
created: 2026-05-29
updated: 2026-07-05
links:
  - rel: depends-on
    target: design/comparative-correlative-v1
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: supports
    target: conjecture/comparative-correlative-construction
  - rel: contradicts
    target: conjecture/comparative-correlative-construction
  - rel: depends-on
    target: source/weissweiler-2022-comparative-correlative
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: supports
    target: claim/comparative-correlative-covariation
---

# Result: comparative-correlative covariation-inference probe v1

This is the project's **first probe of its own design to run end-to-end** (charter §5.4 "Run"). It executes [`design/comparative-correlative-v1`](../../../experiments/designs/comparative-correlative-v1.md) under the ratified operationalization, against the ratified panel, with the [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md) CC subset as the human-comparison anchor. The run record (prompts, raw outputs, code, costs) is at [`experiments/runs/2026-05-29-comparative-correlative-probe-v1/`](../../../experiments/runs/2026-05-29-comparative-correlative-probe-v1/README.md).

**One-line finding:** on this probe, the panel's deployment of the comparative correlative's proportional-covariation meaning is **at or near ceiling** — including the discriminating manipulations (inverse-direction flip; deliberately absurd scale pairs) — and matches the Scivetti native-speaker baseline. This is a **positive result that overshoots the conjecture**: the conjecture bet "narrows but does not close" the form/meaning dissociation [`source/weissweiler-2022-comparative-correlative`](../../base/sources/weissweiler-2022-comparative-correlative.md) found for encoder PLMs; the probe instead shows **no residual dissociation** detectable by this instrument. The headline caveat travels with that overshoot: ceiling on an easy instrument is weak evidence for the strong reading, and the result's main load-bearing limit is exactly that (see *Limits*).

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A), `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C). Temperature 0. Gemini required reasoning enabled (the endpoint rejects `reasoning.enabled=false`); A and B answered with a bare token.
- **Three arms**, all zero-shot, read-only:
  1. **Forced-choice** covariation-direction (INCREASE / DECREASE / UNDETERMINED) on 80 project-authored items.
  2. **NLI** (entailment/neutral/contradiction → 0/1/2) on the same 80 items.
  3. **Human-comparison**: the same NLI instrument on the **30 real Scivetti CC items**, scored against the released per-item gold labels + the aggregate native-speaker baseline (≈0.90).
- **Item set** (frozen before the run, [`items.csv`](../../../experiments/data/comparative-correlative/items.csv)): 20 scale pairs (14 typical + 6 deliberately absurd "atypical") × 4 forms = 80 items. The four forms reuse the *same scalar lexical material*: `cc-positive` (*the more X, the more Y*), `cc-inverse` (*the more X, the less Y*), `ctrl-two` (two independent declaratives), `ctrl-single` (one comparative clause). Atypical pairs (e.g. *the rounder the pebble, the longer the meeting ran*) are constructed so covariation direction can come **only** from the construction, not from world knowledge.
- **No logprobs.** The ratified panel chat models expose no token logprobs on OpenRouter (verified 2026-05-29). The design's ratified fallback (temperature-0 greedy completion + string parse) was used. Parsing was clean: **0 NA across all 570 calls.**
- **Cost** (actual, from token usage): **$0.124** total. Well under the $5 single-run flag ([`config/budget.md`](../../../config/budget.md)).

## Results

Thresholds are the frozen ones from [`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md): **T1** CC-vs-control covariation-assertion gap ≥ 30 pp; **T2** inverse-CC direction-flip rate ≥ 70%; **T3** atypical-pair covariation rate within 15 pp of typical. A clause is supported only if met in ≥ 2 of 3 panel models.

| model | CC assertion | ctrl assertion | **T1 gap** | **T2** inv-flip | pos-incr | typical | atypical | **T3** | NLI CC acc | **Scivetti acc** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| claude-sonnet-4.6 | 100% | 12% | **+87.5 pp** | 100% | 100% | 100% | 100% | ✓ | 100% | **100%** (30/30) |
| gpt-5.4-mini | 100% | 10% | **+90.0 pp** | 100% | 100% | 100% | 100% | ✓ | 98% | **93%** (28/30) |
| gemini-3.5-flash | 100% | 20% | **+80.0 pp** | 95% | 100% | 96% | 100% | ✓ | 95% | **100%** (30/30) |

**Gate outcomes (≥ 2/3 required):** T1 **3/3** · T2 **3/3** · T3 **3/3**. Human-comparison: panel NLI accuracy on the 30 real Scivetti CC items is **93–100%**, at or above the aggregate native-speaker baseline (≈0.90).

Reading the columns:

- **T1 (the construction isolates the inference).** On forced choice, all three models assert a covariation direction for ~100% of CC items but for only 10–20% of the matched non-CC controls that reuse the *same words*. The 80–90 pp gap is direct evidence that the **construction**, not the scalar vocabulary, drives the inference. (The few control "assertions" are mostly the two-clause control, where a model occasionally reads an implied dependency into juxtaposed declaratives — itself a minor, interpretable divergence.)
- **T2 (direction, not just template).** Inverse-CC items (*the more X, the **less** Y*) flip the asserted direction to "decrease" 95–100% of the time. A model merely recognising the CC *template* would not reliably flip; this is the discriminating indicator Weissweiler 2022 designed the encoder semantic task around, and the panel passes it cleanly.
- **T3 (not an n-gram effect).** The covariation inference holds at ~100% even on the deliberately absurd pairs (*the greener the wallpaper, the louder the applause*), within 0–4 pp of the typical pairs. A frequency/memorisation account predicts collapse here; there is none.
- **Human-comparison.** On the actual Scivetti CC gold items the panel matches or slightly exceeds the ≈0.90 human aggregate. The two gpt-5.4-mini misses are both on *contradiction*-labelled items (gold=2), not on the basic positive-covariation cases — i.e. the model under-detected a directional contradiction twice. (The Scivetti CC subset is balanced 10/10/10 across entailment/neutral/contradiction, so this is not a label-imbalance artifact.)

### A measurement note recorded before interpreting (charter §8)

The design's T1 names a "CC-vs-control gap." There are two distinct quantities the raw data can yield, and **both were computable before the run**: (a) a *covariation-assertion* gap (does the model assert any covariation for CC but withhold it for controls), and (b) an *accuracy* difference (CC-correct rate minus control-correct rate). The design's stated *purpose* for T1 — "isolates the construction, not the words, as the source of the inference" — is quantity (a); the analysis uses (a) as the primary T1 number. Quantity (b) is near-zero here (~10–17 pp) only because *both* CC and control accuracy are at ceiling (the controls are correctly answered "undetermined"), which is itself consistent with the finding, not against it.

**Stated bluntly, so the choice is not buried:** read as the design's *literal subtraction* (covariation-inference rate = "fraction correct," so control-correct = correctly saying "undetermined"), T1 is the accuracy difference of ~10–17 pp and **would not clear the 30 pp threshold**. The gap clears 30 pp only under the *assertion-rate* reading (a). These diverge *only because the controls came out correct at ceiling*. We use reading (a) because it is the design's stated purpose and the more natural reading of "the rate on controls" (a control has no covariation, so "control covariation rate" most sensibly means the rate at which controls wrongly *assert* one) — but we flag the divergence explicitly rather than silently selecting the passing number. Both quantities are committed to [`raw/results.json`](../../../experiments/runs/2026-05-29-comparative-correlative-probe-v1/raw/results.json) (`fc_cc_vs_ctrl_gap_pp` vs `fc_cc_vs_ctrl_accuracy_diff_pp`) so a reader can apply either definition; the design's §2 carries the same two-reading ambiguity and a v2/erratum should tighten its wording.

## Interpretation against the conjecture

[`conjecture/comparative-correlative-construction`](../conjectures/comparative-correlative-construction.md) staked a directional bet: decoder LLMs **use** the CC's covariation meaning, **narrowing** the form-recognised-but-meaning-not-used dissociation Weissweiler 2022 found for encoder PLMs, **but not closing it** (remaining measurably below the human baseline).

This probe returns the conjecture's explicitly-flagged **"stronger (closes)" outcome**, not its central "narrows-but-not-closes" bet:

- The panel does not merely beat the encoder-PLM chance baseline; it reaches **ceiling** on covariation inference, including inverse-direction and atypical items.
- It does not sit **measurably below** the human baseline; it **matches** it (93–100% vs ≈90%) on the actual Scivetti items.

Per the conjecture's own falsification table, this outcome "would *refine* the conjecture's 'not closing' clause toward retirement (gap is construction-/generation-specific)." The result is therefore linked to the conjecture as **both** `supports` (the "decoder LLMs use the CC's covariation meaning" core) **and** `contradicts` (the "does not close / remains below human" clause). The honest summary: the *use* claim is supported strongly; the *narrows-but-not-closes* qualifier is not supported by this instrument and should be softened in the conjecture (done in this revision — the conjecture is moved to `tested` with the clause flagged).

## What this result does and does not license (modesty, charter §1/§2.6, CLAUDE.md rule 6)

**Does license**, narrowly and provisionally:
- For *this instrument, this panel, this date*, current instruction-tuned decoder LLMs deploy the comparative correlative's proportional-covariation meaning at human-comparable rates, and the deployment is driven by the construction (T1), tracks direction (T2), and survives an n-gram control (T3). On the [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md) evidence ladder *(superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md) — cited here as the edition this result fed)* this is a **positive Tier-4 (inference-licensing) result with a Tier-3 (generalization/atypical) control passed** — the first positive upper-ladder result of the project's own design.

**Does NOT license:**
- **Ceiling is weak evidence for the strong reading.** When a task saturates, it stops discriminating; a ceiling result cannot distinguish "robust constructional competence" from "the task was too easy for these models." The probe shows the 2022 encoder dissociation is *not reproduced by this instrument on these models* — it does **not** show the construction is processed in any particular deep way. This is the single most important limit.
- **Not interchangeable with Weissweiler 2022.** That was a masked/cloze semantic-application task on encoder PLMs; this is a zero-shot NLI/forced-choice task on decoder LLMs. The "dissociation gone" statement is a *cross-instrument, cross-generation* observation, not a controlled within-instrument longitudinal measurement. The two numbers are not directly comparable (the design and conjecture both forbid equating them); the claim is only that the *phenomenon* (form recognised, meaning at chance) does not recur here.
- **No model-internal claim.** Behavioral only; says nothing about representations.
- **No grounding claim.** Tier-4 inference-licensing is the ceiling of text-internal evidence; this result is silent on grounding in Bender & Koller's sense (theory page, "Open tensions" 2).

## Limits

- **Ceiling / discrimination floor.** See above — the dominant limit. A v2 should raise difficulty (multi-step covariation chains, conflicting lexical-vs-constructional cues, longer-distance scale pairs) to find where, if anywhere, the panel breaks.
- **Small N.** 80 constructed items + 30 Scivetti items; per-cell counts are 20 (constructed) and 30 (Scivetti). Wide uncertainty on any single percentage; the gpt-5.4-mini 28/30 vs 30/30 differences are within noise.
- **Item authorship.** The 80 constructed items are the project's own (the design requires this for the matched-control and atypical manipulations the Scivetti set does not contain). They were frozen before the run and built to a pre-stated schema, but they are not human-normed; only the 30 Scivetti items carry a human gold label. The constructed-item gaps (T1/T2/T3) are *internal* contrasts; the *human-comparison* claim rests only on the Scivetti arm.
- **Single gold label, not a gradient.** The Scivetti anchor is an answer key + aggregate baseline, not a per-item multi-rater distribution (resource page, *Known limits*). The "matches human" statement is answer-key agreement, not a graded-judgment regression.
- **One run, one date, one panel.** No replication, no temperature sensitivity, no alternate-phrasing sweep beyond the two framings. Cross-model divergence was minor (gemini's one inverse-flip miss; gpt-5.4-mini's two Scivetti misses) — informative only as a hint that the effect is convergent, not idiosyncratic.
- **Cross-model shared priors (charter §2.5).** Three decoder LLMs converging is *weak* evidence on its own (the AI-internal ceiling); the Scivetti human anchor is what gives the result independent bearing, and it is small.

## Provenance

- Conjecture: [`conjecture/comparative-correlative-construction`](../conjectures/comparative-correlative-construction.md). Design: [`design/comparative-correlative-v1`](../../../experiments/designs/comparative-correlative-v1.md). Operationalization: [`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md); anchor: [`decisions/resolved/comparative-correlative-anchor`](../../decisions/resolved/comparative-correlative-anchor.md).
- Encoder-PLM precedent: [`source/weissweiler-2022-comparative-correlative`](../../base/sources/weissweiler-2022-comparative-correlative.md) (BERT/RoBERTa/DeBERTa recognise the CC's form but score at chance on its meaning).
- Human anchor: [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md) (CC subset, 30 items, gold labels + ≈0.90 baseline). The dataset repo carries no license; it was **read in place** from a local clone and **not** mirrored into this repo (only aggregate numbers and short verbatim example items are recorded).
- Run record + raw outputs + code + cost ledger: [`experiments/runs/2026-05-29-comparative-correlative-probe-v1/`](../../../experiments/runs/2026-05-29-comparative-correlative-probe-v1/README.md).

## Status

`status: proposed`. The numbers are recorded and reproducible from the committed code + frozen items; what is `proposed` is the project's reading of them. The result is **not** promoted past `proposed` pending: (i) a harder v2 that escapes the ceiling, and (ii) Tom's review of the overshoot relative to the conjecture's "not closing" clause. `contingent-on: []` — both governing decisions are ratified.

> **Update (2026-07-05, session 183 — wiki-coherence pass).** Both pendings landed long ago: the
> harder v2 **and** v3 ran 2026-05-30 (see
> [`result/comparative-correlative-covariation-v2`](comparative-correlative-covariation-v2.md),
> [`result/comparative-correlative-covariation-v3`](comparative-correlative-covariation-v3.md)),
> and promotion — autonomous cross-session review since the 2026-06-12 amendment
> ([`PROJECT.md`](../../../PROJECT.md) §12.3), not a Tom gate — happened s168:
> [`claim/comparative-correlative-covariation`](../claims/comparative-correlative-covariation.md)
> (`supported`, direction-scoped), with the powered magnitude attached s169
> ([`result/comparative-correlative-covariation-powered`](comparative-correlative-covariation-powered.md):
> 136 fresh disjoint items, gap ≈87pp [lb ≈78], 3/3). *(Back-annotation: this page's numbers and
> reading stand unchanged.)*
