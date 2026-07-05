---
type: result
id: way-construction-traversal-v1
title: The project's own way-construction minimal pairs — all three models draw the path-traversal entailment from non-motion verbs above the ratified bar, with gpt-5.4-mini the conservative outlier on consumption verbs
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
    target: conjecture/way-construction
  - rel: supports
    target: result/caused-motion-minimal-pair-divergence-v1
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: open-question/constructional-vs-frequency-confound
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
---

# Result: way-construction minimal-pair probe v1

The project's **own** test of [`conjecture/way-construction`](../conjectures/way-construction.md) — the third own-design argument-structure minimal-pair probe, completing the set begun by [`result/conative-minimal-pair-divergence-v1`](conative-minimal-pair-divergence-v1.md) (the construction *removes* an entailment) and [`result/caused-motion-minimal-pair-divergence-v1`](caused-motion-minimal-pair-divergence-v1.md) (the construction *adds* a transitive causation-of-motion entailment). The way-construction is the converse-flavoured "add" case: it coerces a **self-motion / path-traversal** entailment onto non-motion verbs — *Mia whistled her way down the hall* entails Mia moved down the hall, though *whistle* denotes no displacement (Goldberg 1995, ch. 9). Design + frozen stimuli: [`design/way-construction-v1`](../../../experiments/designs/way-construction-v1.md); run record: [`experiments/runs/2026-05-29-way-construction-probe-v1/`](../../../experiments/runs/2026-05-29-way-construction-probe-v1/README.md).

**One-line finding:** the conjecture's confirm bar is **met by all three models on both instruments** — way rate **77.8–100%**, gap (way − location control) **77.7–100 pp**, in **3/3 models**, and the anti-motion stress category (the predicted verb-reading weak spot) **holds at or near ceiling for every model**. Two models (claude, gemini) are at/near ceiling; **gpt-5.4-mini is the conservative outlier** — its only non-affirms (4–5 items: *hum, eat, chat*, and under forced-choice *snack*) it reads as "may or may not have moved." The over-generalization guard (idiomatic *way*) sits at **0%** for all models and the location control near **floor**, so this is not surface-string detection. Lead caveat (as for the CC and caused-motion results): **ceiling on relatively easy controls is weak evidence for any strong "deep processing" reading.**

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): claude-sonnet-4.6 (A), gpt-5.4-mini (B), gemini-3.5-flash (C), as subjects. Both instruments (NLI 0/1/2 + forced-choice YES/NO/CANT_TELL); temperature 0; the ratified divergence operationalization. **0 NA across all 360 calls.**
- **Stimuli** (project's own, frozen pre-run; `items.csv` sha256[:16] `536977843dff18a5`): 18 non-motion verbs (6 manner, 6 activity, 6 anti-motion) × 3 forms — **way** (construction), **ctrl-loc** (same verb, locative of the same scene; the discriminating control), **ctrl-motion** (motion lexicalized in a "*walked …, V-ing*" frame; the positive floor) — plus 6 **idiomatic** over-generalization guards (*talked her way out of trouble*). Indicator = **affirm path-traversal rate** (FC YES, or NLI entailment) on "*&lt;Subj&gt; moved from one place to another.*"
- **Cost** (actual): **$0.072** (A $0.052 / B $0.003 / C $0.016). Well under the $5 flag.

## Results

Affirm path-traversal rate (%). Confirm bar: way ≥70%, gap ≥30 pp vs. the location control, in ≥2/3 models, holding for the anti-motion category.

| model | instr. | way | ctrl-loc | ctrl-motion | idiom | **gap** | manner / activity / anti | verbs way-yes |
|---|---|---:|---:|---:|---:|---:|:--:|:--:|
| claude-sonnet-4.6 | NLI | 100% | 0% | 100% | 0% | **+100** | 100 / 100 / 100 | 18/18 |
| claude-sonnet-4.6 | FC | 100% | 0% | 100% | 0% | **+100** | 100 / 100 / 100 | 18/18 |
| gpt-5.4-mini | NLI | 83.3% | 5.6% | 100% | 0% | **+77.7** | 83.3 / 66.7 / 100 | 15/18 |
| gpt-5.4-mini | FC | 77.8% | 0% | 100% | 0% | **+77.8** | 83.3 / 50.0 / 100 | 14/18 |
| gemini-3.5-flash | NLI | 100% | 11.1% | 100% | 0% | **+88.9** | 100 / 100 / 100 | 18/18 |
| gemini-3.5-flash | FC | 94.4% | 0% | 100% | 0% | **+94.4** | 100 / 100 / 83.3 | 17/18 |

- **Confirm bar met by all three models on both instruments** (way ≥77.8%, gap ≥77.7 pp). claude and gemini affirm the traversal entailment for essentially every verb (18/18; gemini 17/18 under FC); gpt-5.4-mini for 14–15/18.
- **ctrl-loc near floor (0–11.1%):** when the same verb appears with a plain locative ("*Mia whistled in the hall*") instead of the construction, no model reads path-traversal. This is the discriminating control and the floor of the gap.
- **ctrl-motion = 100% everywhere (the positive floor):** when motion is lexicalized ("*Mia walked down the hall, whistling*"), every model affirms traversal. This validates the indicator — a low way rate would mean "not reading the construction," not "doesn't understand the question."
- **idiomatic guard = 0% everywhere:** for bleached/metaphorical *way* with a non-spatial goal ("*talked her way out of trouble*", "*worked his way up the company*"), no model affirms literal traversal. So the way-form affirmations are **not** mere detection of the surface string "*POSS way*."
- **P3 (verb-reading guard):** the anti-motion category — the predicted collapse point for a model reading the *verb* rather than the construction — is at ceiling for claude and gemini-NLI (100%) and **100% for gpt-5.4-mini on both instruments**. No model shows the verb-reading failure mode. gemini's single anti-motion FC non-affirm is *waited his way up the queue* (CANT_TELL) — the most marginal item in the set.

### gpt-5.4-mini's misses are scattered, not the anti-motion stress items

gpt-5.4-mini's only way-form non-affirms are **hum, eat, chat** (NLI) and **hum, eat, chat, snack** (FC) — all judged *neutral / CANT_TELL*. They do **not** form a clean semantic class: *hum* is a manner-of-sound verb (categorized `manner`), while *eat, chat, snack* are `activity` verbs. For *eat/chat/snack* a metaphorical "made progress through" reading is genuinely available alongside the literal-traversal one (one can plausibly *eat across a buffet* without walking its length), so CANT_TELL there is defensible caution; *hum* (*hummed his way through the crowd*) has a clearly physical path, so its non-affirm is closer to arbitrary conservatism. The unifying point is **not** a tidy verb-class effect but that gpt applies a **more conservative entailment bar** — crucially, **not** the predicted verb-reading failure: it affirms the *anti-motion* items (*waited/rested/knelt his way*) at **100%**, where the literal reading is the only one available. This mirrors gpt-5.4-mini's role as the divergent, instrument-sensitive model in the [`result/conative-minimal-pair-divergence-v1`](conative-minimal-pair-divergence-v1.md) probe.

## Interpretation (modest)

1. **The way-construction's path-traversal entailment is drawn off the construction, above the ratified bar by all three models.** With the (non-motion) verb held constant and toggled against a plain locative, all three models read the self-motion inference from the *construction*, not the verb. This **confirms** the conjecture at its stated bar — the conjecture's three predictions (prediction 1 — way ≥70%; prediction 2 — gap ≥30 pp vs. controls; prediction 3 — robust to verb semantics, i.e. anti-motion holds) are all met, and the *added* over-generalization guard (idiomatic *way* → low) — not one of the conjecture's stated predictions but a design-level robustness check — also passes.
2. **It is the construction, not the surface "*way*" string.** The idiomatic guard (surface *POSS way* + non-spatial goal) is at 0% for all models, and the location control near floor — two independent ways the result rules out a surface-string heuristic. Together with ctrl-motion at ceiling (the indicator fires when motion is lexical), the contrast is clean.
3. **The set of three argument-structure probes now sketches a consistent picture.** Across conative (cancel an entailment — harder, instrument-fragile), caused-motion (add a causation-of-motion entailment — ceiling), and now way (add a self-motion entailment — above bar, near ceiling): current decoders **license a construction-contributed inference readily** and **suppress a lexically-default one less readily**. The way-construction is an "add" case and patterns with caused-motion (easy direction), consistent with the asymmetry flagged in [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md). *(superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md) — cited here as the edition this page engaged.)*
4. **The one cross-model split is interpretively benign.** gpt-5.4-mini's 4–5 non-affirms are scattered across the manner and activity categories (not a clean verb class); for the *eat/chat/snack* subset a real metaphorical-progress alternative makes CANT_TELL cautious-not-wrong, and it affirms the harder anti-motion items at 100%. The divergence is itself data (charter §6) but does not undercut the confirm.

This places the way-construction alongside the comparative correlative and caused-motion as an upper-ladder **positive at/near ceiling** (Tier 4 inference-licensing, with the Tier-3 anti-motion / frequency-stress control passed).

## What this licenses / does not license

**Licenses:** a project-owned statement that current decoders draw the way-construction's path-traversal entailment onto non-motion verbs above the ratified bar (3/3 models, both instruments), with the location control, the over-generalization guard, and the anti-motion verb-reading guard all passed — promoting [`conjecture/way-construction`](../conjectures/way-construction.md) to `tested` (supported).

**Does NOT license:**
- **A strong "deep constructional processing" claim.** Like the CC and caused-motion results, this is **ceiling on relatively easy controls** (ctrl-loc is a plain locative; the way items are well-formed canonical or marked-but-interpretable coercions). Ceiling discriminates poorly — a harder instrument (conflicting cues; verbs that *contradict* motion in a fully resolved context) could separate the models. The calibrated reading is "the construction-contributed traversal inference is reliably available," not "the model has deep motion-event semantics."
- **A tight item-matched human comparison.** N=18 verbs, single run; the Scivetti anchor is answer-key/aggregate and these are the project's own items (phenomenon-level comparison: the way-construction is a real construction with a ≈0.90/0.83 native baseline in Scivetti's CxNLI).
- **A model-internal or grounding claim.** Behavioral only.

## Limits

- **Ceiling result** — the main caution; a coercion-resisting / conflicting-cue v2 is the natural follow-up (queued).
- **N=18 verbs, single run/date, both instruments.** Cross-model + cross-instrument convergence is the robustness signal; the one divergence (gpt-5.4-mini on consumption verbs) is reported in full.
- **Directional-PP vs locative confound (documented, not tuned away):** the *way* form uses a directional PP ("*down the hall*") and ctrl-loc a locative ("*in the hall*"). The bare directional form ("*\*Mia whistled down the hall*") is **ungrammatical** for these non-motion verbs *without* the construction — which is itself the construction's signature, but means the way-vs-loc gap is not a pure "*way*"-string toggle. The idiomatic guard (surface *way*, non-spatial goal → 0%) bounds the "is it just the string?" worry; full reasoning in the run's `build_items.py` header.
- **Anti-motion items are deliberately marked.** *Waited/rested/knelt/crouched/paused/lingered his way* are marginal way-constructions; each path-PP is spatial so the traversal gold holds *if* the string is parsed as a way-construction at all. That all three models affirm them at/near ceiling is itself the prediction-3 result.
- **Shared priors (charter §2.5):** three decoders are not three independent witnesses; the independent bearing is the Goldberg/Scivetti human anchor.

## Provenance

- Conjecture: [`conjecture/way-construction`](../conjectures/way-construction.md). Operationalization: [`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md) (ratified). Anchor: [`decisions/resolved/way-construction-anchor`](../../decisions/resolved/way-construction-anchor.md) → [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md). Inventory seed: Goldberg (1995, ch. 9).
- Companions: [`result/conative-minimal-pair-divergence-v1`](conative-minimal-pair-divergence-v1.md), [`result/caused-motion-minimal-pair-divergence-v1`](caused-motion-minimal-pair-divergence-v1.md).
- Run record + code + full (own-stimuli) outputs + cost: [`experiments/runs/2026-05-29-way-construction-probe-v1/`](../../../experiments/runs/2026-05-29-way-construction-probe-v1/README.md). Every number reproducible from the committed `raw/results.json`.

## Status

`status: proposed`. Numbers reproducible from committed code + `raw/results.json`. `contingent-on: []`. Promotion past `proposed` awaits Tom's review. *(Governance note, s183: since the autonomous-era amendment of 2026-06-12 — [`PROJECT.md`](../../../PROJECT.md) §12.3 — promotion runs by autonomous cross-session adversarial review; Tom holds a standing override.)* The standing caveat is the ceiling: this confirms the conjecture's prediction but a harder instrument is needed to probe the strength of the underlying competence.
