---
type: claim
id: comparative-correlative-covariation
title: The 2026 decoder panel reliably tracks the comparative correlative's covariation structure and direction on the tested instruments — a robust, construction-driven directional result, not a magnitude or general human-level-competence claim
meaning-senses:
  - constructional
  - inferential
  - functional-vs-formal
  - human-comparison
status: supported
contingent-on: []
created: 2026-07-02
updated: 2026-07-02
links:
  - rel: supports
    target: conjecture/comparative-correlative-construction
  - rel: depends-on
    target: result/comparative-correlative-covariation-v1
  - rel: depends-on
    target: result/comparative-correlative-covariation-v2
  - rel: depends-on
    target: result/comparative-correlative-covariation-v3
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
---

# Claim: the decoder panel reliably tracks the comparative correlative's covariation structure and direction on the tested instruments

## Statement

Across three replicated, controlled runs on the ratified 3-family panel (`claude-sonnet-4.6`, `gpt-5.4-mini`, `gemini-3.5-flash`), current instruction-tuned decoder LLMs **reliably deploy the English comparative correlative's proportional-covariation reading on the tested items** — they treat *the more X, the more/less Y* as licensing the inference that a change along the first scale goes with a fixed-direction change along the second, and they do so **because of the construction, not the scalar vocabulary**. The result is **directional/ordering-level and robust across a graded battery of stress manipulations**:

- the inference is **isolated to the construction**: the panel asserts a covariation direction for ~100% of comparative-correlative (CC) items but for only 10–20% of matched non-CC controls that reuse the *same words* (v1 forced-choice gap +80.0 to +90.0 pp, 3/3 models — see *Grounds*, and the measurement caveat in *Bounds*);
- it **tracks direction, not a surface template**: inverse CCs (*the more X, the **less** Y*) flip the asserted direction (v1 inverse-flip 95–100%, 3/3; v3 `baseline-inv` 100% on both instruments, 3/3);
- it is **not an n-gram/memorization effect**: the inference persists at ~100% on deliberately absurd scale pairs whose direction can come only from the construction (v1 T3, within 0–4 pp of typical pairs, 3/3);
- it **follows the construction over conflicting world knowledge** (v2 conflicting-cue: NLI 100% 3/3; forced-choice 100/83.3/83.3) and **composes two-step covariation chains**, including the diagnostic negative×negative→positive case a single-clause heuristic would fail (v2 multi-step 100%, both instruments, 3/3);
- for **2 of 3 models** it further **survives an in-sentence operator that cancels or suspends the assertion** — sentential negation and epistemic hedging (v3: `claude-sonnet-4.6` and `gemini-3.5-flash` at/near ceiling on every embedded arm), so the robustness is not a bare *"the-more…the-more → increase"* template.

On the **single human-comparison arm the project has for this construction** — the 30 real Scivetti CC NLI items, scored against the released per-item gold answer key and the aggregate ≈0.90 native-speaker baseline — the panel **matches or slightly exceeds** the human answer-key baseline (v1 NLI accuracy 93–100%). This human-comparison leg is narrow and single-run (see *Human-comparison leg* and *Bounds*).

This claim is deliberately **scoped to a direction/ordering statement about performance on the tested instruments**. It does **not** assert a precise magnitude with an interval (the runs are founding-N; a powered re-run is owed — *Bounds*), and it does **not** assert general human-level CC semantic competence or that the human-vs-model meaning gap is closed (*What this claim does not say*).

## Grounds

Three own-design results, all replicating the direction on disjoint item sets and escalating difficulty. Read the **orderings and rates** below, not fitted coefficients: n = 3 models, and per-arm cells rest on small item counts, so single items move a cell by 5–33 pp.

### v1 — construction isolation, direction, n-gram robustness, and the human arm
[`result/comparative-correlative-covariation-v1`](../results/comparative-correlative-covariation-v1.md). 80 project-authored items (20 scale pairs × 4 forms, 20 per cell) + the 30 real Scivetti CC items; both forced-choice and NLI instruments; 0 NA / 570 calls; cost $0.124.

| model | T1 CC-vs-ctrl assertion gap | T2 inverse-flip | T3 atypical | Scivetti NLI acc |
|---|---:|---:|---:|---:|
| claude-sonnet-4.6 | +87.5 pp | 100% | ✓ (100% vs 100%) | 100% (30/30) |
| gpt-5.4-mini | +90.0 pp | 100% | ✓ (100% vs 100%) | 93% (28/30) |
| gemini-3.5-flash | +80.0 pp | 95% | ✓ (100% vs 96%) | 100% (30/30) |

Frozen thresholds from [`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md) (T1 gap ≥ 30 pp; T2 flip ≥ 70%; T3 atypical within 15 pp of typical; a clause supported only if met in ≥ 2/3). **All three gates: 3/3.** The two `gpt-5.4-mini` Scivetti misses are both on contradiction-labelled items (under-detected a directional contradiction), not on basic positive covariation.

### v2 — conflicting cue and composition (off-ceiling stress)
[`result/comparative-correlative-covariation-v2`](../results/comparative-correlative-covariation-v2.md). 19 items across 4 arms (baseline / conflicting-cue / paraphrase / multi-step), both instruments; 0 NA / 114 calls; `anchor: internal-contrast-only`; cost $0.109 billed. **Conflicting-cue** (construction states the covariation whose real-world direction is the *opposite*): follow-construction NLI 100% 3/3, FC 100/83.3/83.3 — the panel privileges the stated construction over plausibility, with a single 1-in-6 FC slip toward world knowledge for `gpt-5.4-mini` and `gemini`. **Multi-step** composition 100% everywhere, including the `multi-bears` negative×negative→positive item, and the arm mixes sign products (+×+, +×−, −×−, −×+) so it is not an "always assert increase" bias.

### v3 — operator embedding (negation / epistemic hedging)
[`result/comparative-correlative-covariation-v3`](../results/comparative-correlative-covariation-v3.md). 16 items × 5 arms (asserted positive / asserted inverse / negation / modal-epistemic / negated-inverse), both instruments; 96 calls, 1 NA (a truncation artifact); `anchor: internal-contrast-only`; cost $0.09326 billed. `claude-sonnet-4.6` and `gemini-3.5-flash` withhold the covariation direction under negation and hedging at/near ceiling (gemini 100% on every arm and instrument); `baseline-inv` is 100% everywhere, confirming genuine direction-tracking, not an increase-bias. **`gpt-5.4-mini` cracks under forced-choice specifically** via an excluded-middle *over*-inference (treats ¬(X decreases) as entailing X increases: `negation-inv` FC 0%; one `negation` flip to decrease; one epistemic hedge read as asserted) — over-inference, not template-firing, and instrument-localized (its NLI is far stronger). This is a genuine non-uniformity of the panel, carried explicitly in *Bounds*.

### The controls that isolate the construction
The claim's "construction-driven, not lexical" force rests on the matched controls, not on the raw high rates: v1's T1 non-CC controls reuse the *same scalar words* in a non-CC syntax (the gap is the construction's contribution); v1's T2/`baseline-inv` inverse items guard against an increase-bias readout; v1's T3 absurd pairs guard against memorization; v2's conflicting-cue arm separates the construction from world knowledge; v2's multi-step composition separates real composition from last-clause matching; v3's in-sentence operators test compositional scope rather than extra-linguistic cues.

## Human-comparison leg (narrow — v1 only, answer-key not gradient)
The **only** human anchor for this construction in-repo is the Scivetti CxNLI CC subset ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md); ratified [`decisions/resolved/comparative-correlative-anchor`](../../decisions/resolved/comparative-correlative-anchor.md)). Inspection (2026-05-29) confirmed it delivers a **single adjudicated gold label per item plus an aggregate ≈0.90 native-speaker baseline — an answer key, NOT a per-item multi-rater gradient.** So the human-comparison statement here is **answer-key agreement on 30 CC items on one run (v1)**: panel NLI accuracy 93–100% at or above ≈0.90. The v2/v3 hard arms (conflicting-cue, composition, negated/hedged CC) have **no in-repo human norm** and are `internal-contrast-only` by ratified decision ([`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)); **no human-comparison claim is made for them.**

## Where it sits on the evidence ladder
On the ladder in [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md) this is a **Tier-4 (inference-licensing) positive with a Tier-3 (atypical/generalization) control passed**, stress-tested for conflicting-cue, multi-step composition, and operator scope. It is the project's **most robust constructional positive** and patterns with the theory's recurring observation that current decoders handle the **add / easy direction** of the upper ladder at ceiling. The theory page's standing caution travels with it unchanged: this is the "easy direction," and ceiling on a modest instrument bounds how deep a reading it licenses.

## What this claim does NOT say
- **No precise magnitude.** n = 3 models, founding-N per arm (20/cell in v1's constructed set; 3–6 items per arm in v2/v3); the numbers are orderings and rates with wide per-cell uncertainty, not estimates with intervals. A magnitude+CI is **owed to the A2a powered re-run** and is out of scope here.
- **No general human-level CC competence claim.** The human-comparison leg is a single-run, 30-item, answer-key agreement at ceiling — it cannot distinguish robust competence from task-easiness. "Reliably tracks CC covariation on the tested instruments" is **not** "understands comparative correlatives like humans."
- **The human-vs-model gap is not shown "closed."** The v1 arm shows the panel *matching* the ≈0.90 answer-key baseline on 30 easy items; that contradicts the conjecture's "narrows-but-does-not-close" bet on this one instrument (see *Bounds*), but it is **not** a general closure claim — it is answer-key parity on one small ceiling arm.
- **Not uniform across the panel.** `gpt-5.4-mini` cracks under forced-choice operator embedding (v3); the claim covers the panel *including* that crack, it does not paper over it.
- **No model-internal or grounding claim.** Behavioral only; silent on representations and on grounding in Bender & Koller's sense (Tier-4 is the ceiling of text-internal evidence).

## Bounds
- **Ceiling instrument (the lead caveat).** Every run is at or near ceiling; when a task saturates it stops discriminating, so these results cannot separate "robust constructional competence" from "the task was easy for these models." This is the single most important limit and is why the claim is scoped to a directional/ordering statement on the tested instruments, not to a depth-of-processing verdict.
- **Founding-N; powered re-run owed.** v1's constructed set is 20 items per cell; v2/v3 arms rest on 3–6 items each (a single item moves a v3 cell 25–33 pp). Under [`PROTOCOL.md`](../../../PROTOCOL.md) §4 a claim-carrying *magnitude* needs ~100–150 items. The program's **A2a powered re-run is owed** to attach a magnitude+interval; until it runs, this claim states direction/ordering only.
- **A measurement ambiguity in v1's T1.** T1 clears 30 pp only under the *assertion-rate* reading of "CC-vs-control gap"; under the literal *accuracy-difference* reading it is ~10–17 pp and **would not clear** the threshold — the two diverge only because the controls are correctly answered at ceiling. The result page commits both quantities to its raw data and uses the assertion-rate reading (the design's stated purpose); the claim inherits that reading and flags it here rather than burying it.
- **`gpt-5.4-mini` FC over-inference under operator embedding.** The panel is non-uniform at the operator-scope frontier (v3): the directional robustness holds for 2/3 models on both instruments, but `gpt-5.4-mini`'s forced-choice reading of negated/hedged CCs is a specific excluded-middle over-inference. The claim's "for 2 of 3 models" scoping on the operator-embedding leg is load-bearing. (For symmetry: `claude-sonnet-4.6` is not perfectly uniform either — its one embedded-arm slip is a single forced-choice miss on the hardest, doubly-recoded `negi-alarm` item, which the v3 page reads as noise rather than a mechanism; the "at/near ceiling" phrasing above covers it. The non-uniformity that is a *mechanism* is gpt-5.4-mini's.)
- **The conjecture's "narrows-but-not-closes" clause is contradicted on the v1 instrument.** [`conjecture/comparative-correlative-construction`](../conjectures/comparative-correlative-construction.md) bet the panel would stay measurably below the human baseline; on the v1 Scivetti arm it *matched* it — the conjecture's explicitly-flagged "stronger (closes)" outcome, on that one small ceiling instrument. This claim records that as answer-key parity on an easy arm, not as a general closure.
- **Single date, single panel, cross-model shared priors.** Three decoder LLMs converging is weak evidence on its own; the Scivetti human anchor is what gives the v1 arm independent bearing, and it is small (30 items, answer-key). No temperature sweep beyond the two framings; no independent-dataset replication.

## Anchor
This claim carries a resource `anchors:` link to [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md) because it makes a (narrow) **human-comparison** statement — the v1 answer-key parity on the 30 real Scivetti CC items. That link grounds only the human-comparison leg. The **internal-contrast legs** (construction isolation, direction, n-gram robustness, conflicting-cue, composition, operator scope) draw their force from within-model contrasts and carry no human claim — consistent with the ratified `internal-contrast-only` status of the v2/v3 hard arms ([`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)). The claim is therefore **not** marked `anchor: internal-contrast-only`: it does lean, in part, on the Scivetti human comparison, and states that leg at exactly its (single-run, answer-key, ceiling) strength.

## Status
`status: supported`. What is supported is the **scoped directional/ordering claim**: the finding is replicated across three controlled runs on disjoint item sets, survives its matched controls and a graded stress battery, and carries a ratified human anchor on its (narrow) human-comparison leg. `supported` attaches to the direction and the construction-isolation, **not** to any magnitude and **not** to a general human-level-competence reading — both of which are explicitly disclaimed above. The three underlying results remain `status: proposed` (the promotion consolidates them; it does not restate their per-run readings). `contingent-on: []` — every governing decision (anchor, operationalization, conflicting-cue anchor, v2 difficulty gate) is ratified.
