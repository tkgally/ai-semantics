---
type: result
id: caused-motion-minimal-pair-divergence-v1
title: The project's own caused-motion minimal pairs — all three models affirm the construction's causation-of-motion entailment onto non-motion verbs at ceiling, and correctly withhold it when another cause is present
meaning-senses:
  - constructional
  - inferential
  - distributional
  - human-comparison
status: proposed
contingent-on: []
created: 2026-05-29
updated: 2026-07-05
links:
  - rel: supports
    target: conjecture/caused-motion-construction
  - rel: supports
    target: result/conative-minimal-pair-divergence-v1
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: open-question/constructional-vs-frequency-confound
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
---

# Result: caused-motion minimal-pair probe v1

The project's **own** test of [`conjecture/caused-motion-construction`](../conjectures/caused-motion-construction.md) — the companion to [`result/conative-minimal-pair-divergence-v1`](conative-minimal-pair-divergence-v1.md). Where the conative tests whether the construction *removes* an entailment (completed contact), this tests whether it **adds** one: Goldberg's canonical case that *Maria sneezed the napkin off the table* entails the napkin moved and her sneezing caused it, even though *sneeze* is intransitive and denotes no motion. Design + frozen stimuli: [`design/caused-motion-construction-v1`](../../../experiments/designs/caused-motion-construction-v1.md); run record: [`experiments/runs/2026-05-29-caused-motion-minimal-pair-probe-v1/`](../../../experiments/runs/2026-05-29-caused-motion-minimal-pair-probe-v1/README.md).

**One-line finding:** the conjecture's confirm bar is met **decisively, at ceiling**. All three models affirm the causation-of-motion entailment for non-motion verbs at **90–100%** (cm rate), with a **70–100 pp gap** over controls, in **3/3 models**, replicating across **9–10 of 10 verbs**, holding for **atypical / low-frequency-in-construction verbs** (within 15 pp). Crucially, the **causation-specific control passes**: when the object moves *but by another cause* (ctrl-sep), the panel **withholds** the verb-causation attribution (0–20% affirm) — so this is not merely "the path-PP implies motion." Lead caveat (as with the comparative correlative): **ceiling on relatively easy controls is weak evidence for any strong "deep processing" reading.**

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): claude-sonnet-4.6 (A), gpt-5.4-mini (B), gemini-3.5-flash (C), as subjects. Both instruments (NLI 0/1/2 + forced-choice YES/NO/CANT_TELL); temperature 0; the ratified divergence operationalization. **0 NA across all 180 calls.**
- **Stimuli** (project's own, frozen pre-run; `items.csv` sha256[:16] `ebb37ae501d455ca`): 10 non-motion verbs × 3 forms — **cm** (caused-motion frame), **ctrl-loc** (object stated to stay put), **ctrl-sep** (object moves by another cause). Indicator = **affirm caused-motion rate** (FC YES, or NLI entailment) on "*&lt;Subj&gt;'s &lt;gerund&gt; caused &lt;obj&gt; to move.*"
- **Cost** (actual): **$0.044** (A $0.027 / B $0.002 / C $0.015). Well under the $5 flag.

## Results

Affirm caused-motion rate (%). Confirm bar: cm ≥70%, gap ≥30 pp vs. worst control, in ≥2/3 models, holding for atypical verbs.

| model | instr. | cm | ctrl-loc | ctrl-sep | **gap** | typ / atyp | inan / anim | verbs cm-yes |
|---|---|---:|---:|---:|---:|:--:|:--:|:--:|
| claude-sonnet-4.6 | NLI | 100% | 0% | 10% | **+90** | 100 / 100 | 100 / 100 | 10/10 |
| claude-sonnet-4.6 | FC | 100% | 0% | 10% | **+90** | 100 / 100 | 100 / 100 | 10/10 |
| gpt-5.4-mini | NLI | 90% | 0% | 20% | **+70** | 100 / 80 | 100 / 80 | 9/10 |
| gpt-5.4-mini | FC | 90% | 0% | 10% | **+80** | 100 / 80 | 100 / 80 | 9/10 |
| gemini-3.5-flash | NLI | 100% | 0% | 0% | **+100** | 100 / 100 | 100 / 100 | 10/10 |
| gemini-3.5-flash | FC | 100% | 0% | 0% | **+100** | 100 / 100 | 100 / 100 | 10/10 |

- **Confirm bar met by all three models on both instruments** (cm ≥90%, gap ≥70 pp). The effect replicates across essentially every verb (10/10 for claude and gemini; 9/10 for gpt).
- **ctrl-loc = 0% everywhere:** when the verb is intransitive and the object is stated to stay put, no model affirms caused-motion. Trivially correct, and the floor of the gap.
- **ctrl-sep = 0–20%** (the causation-specific control): when the object *does* move but by an overt other cause, the panel correctly does **not** attribute the motion to the verb. This is the load-bearing control — it shows the panel tracks *causal attribution* contributed by the construction, not merely the presence of motion or of a path-PP.
- **P3 (frequency/memorization):** atypical (low-frequency-in-construction) verbs are within 15 pp of typical in every cell (claude/gemini 100/100; gpt 100/80). The construction coerces caused-motion even onto verbs that essentially never appear in the frame — not a memorized-string effect.

### gpt-5.4-mini's two misses are both animate-object items

gpt-5.4-mini's only cm non-affirms are *shudder* (NLI, → neutral) and *snore* (FC, → NO) — both **animate-object** items (a spider/kitten as a volitional self-mover responding to the verb), which the design pre-registered as a *softer* caused-motion reading (the agent could refuse). Its inanimate-propulsion core is 100%. This is the predicted weak spot, not a failure of the construction reading.

## Interpretation (modest)

1. **The caused-motion construction's added entailment is tracked at ceiling.** With clean stimuli holding the (non-motion) verb's lexical inability to license motion constant, all three models read the causation-of-motion inference off the *construction*. This **confirms** the conjecture at its stated bar.
2. **It is genuine causal attribution, not motion detection.** The ctrl-sep control (motion present, other cause) is the result's strongest feature: models withhold the inference precisely when the construction is absent even though motion occurred. A pure "path-PP ⇒ motion" or "any motion ⇒ yes" heuristic would fail this; the panel passes it.
3. **An asymmetry with the conative** (the two own-design argument-structure probes together): **adding** a salient entailment (caused-motion) is *easy* — ceiling for all three models, both instruments — while **cancelling** a default entailment (the conative's completed-contact) was *harder* and instrument-fragile (gpt-5.4-mini failed it under NLI). Notably gpt-5.4-mini handles caused-motion fine under **both** instruments (90%), so its conative-NLI failure is specific to entailment-*cancellation*, not a general inability. The tentative reading: current decoders more readily license a construction-contributed inference than suppress a lexically-default one.

This places caused-motion alongside the comparative correlative as an upper-ladder **positive at ceiling** (Tier 4 inference-licensing, with the Tier-3 atypical control passed), complementing the conative's positive-with-divergence and the distinction probe's negative.

## What this licenses / does not license

**Licenses:** a project-owned statement that current decoders track the caused-motion construction's causation-of-motion entailment onto non-motion verbs at ceiling, with the causal-attribution and frequency controls passed — promoting [`conjecture/caused-motion-construction`](../conjectures/caused-motion-construction.md) to `tested` (supported).

**Does NOT license:**
- **A strong "deep constructional processing" claim.** Like the CC result, this is **ceiling on relatively easy controls** (ctrl-loc explicitly says "stayed"; the cm frames are well-formed canonical coercions). Ceiling discriminates poorly — a harder instrument (coercion-resisting verbs, conflicting cues) could separate the models. The calibrated reading is "the construction-contributed inference is reliably available," not "the model has deep causal semantics."
- **A tight magnitude or item-matched human comparison.** N=10 verbs, single run; the Scivetti anchor is answer-key/aggregate and these are the project's own items (phenomenon-level comparison: caused-motion is a real construction with a ≈0.90/0.83 native baseline).
- **A model-internal or grounding claim.** Behavioral only.

## Limits

- **Ceiling result** — the main caution; harder controls are the natural v2. *[Update, s183: the
  harder controls ran — [`result/argument-structure-coercion-v2`](argument-structure-coercion-v2.md)
  (same day, 2026-05-29: the ceiling survived a conflicting cue, cue-sensitive not a brittle
  template) and [`result/caused-motion-near-miss-v2c`](caused-motion-near-miss-v2c.md) (2026-05-30:
  the causation inference is genuinely form-keyed, withheld for near-miss frames carrying the same
  content).]*
- **N=10 verbs, single run/date, both instruments.** Cross-model + cross-instrument convergence is the robustness signal.
- **Animate-object cm items** (laugh/whistle/yawn/snore/shudder) are a softer caused-motion (volitional self-mover); reported split — the inanimate-propulsion core is the crisp case. **shudder/shiver verbs themselves denote body-motion**, so a positive cm there is less diagnostic of pure constructional coercion (kept for the atypical arm, not load-bearing).
- **ctrl-sep changes two things at once** (construction absent *and* a salient competing cause present); it isolates causal attribution but not the construction in pure isolation.
- **Shared priors (charter §2.5):** three decoders are not three independent witnesses; the independent bearing is the Goldberg/Scivetti human anchor.

## Provenance

- Conjecture: [`conjecture/caused-motion-construction`](../conjectures/caused-motion-construction.md). Operationalization: [`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md) (ratified). Anchor: [`decisions/resolved/caused-motion-anchor`](../../decisions/resolved/caused-motion-anchor.md) → [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md). Inventory: Goldberg (1995, ch. 7).
- Companion: [`result/conative-minimal-pair-divergence-v1`](conative-minimal-pair-divergence-v1.md).
- Run record + code + full (own-stimuli) outputs + cost: [`experiments/runs/2026-05-29-caused-motion-minimal-pair-probe-v1/`](../../../experiments/runs/2026-05-29-caused-motion-minimal-pair-probe-v1/README.md). Every number reproducible from the committed `raw/results.json`.

## Status

`status: proposed`. Numbers reproducible from committed code + `raw/results.json`. `contingent-on: []`. Promotion past `proposed` awaits Tom's review. *(Governance note, s183: since the autonomous-era amendment of 2026-06-12 — [`PROJECT.md`](../../../PROJECT.md) §12.3 — promotion runs by autonomous cross-session adversarial review; Tom holds a standing override.)* The standing caveat is the ceiling: this confirms the conjecture's prediction but a harder instrument is needed to probe the strength of the underlying competence.
