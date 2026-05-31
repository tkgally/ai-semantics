---
type: result
id: coercion-implicit-cue-v2b
title: Implicit-cue caused-motion v2b — decoders affirm a physically-impossible coercion at near-ceiling from an implicit world-knowledge cue, and only floor under an explicit outcome denial; so the v2 cue-sensitivity is explicit-outcome parsing, not world-model integration
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: refines
    target: result/argument-structure-coercion-v2
  - rel: supports
    target: conjecture/caused-motion-construction
  - rel: supports
    target: open-question/instrument-sensitivity-constructional-inference
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: concept/coercion
---

# Result: caused-motion implicit-cue probe v2b

The v2b the add-direction v2 deferred. Design + frozen stimuli: [`design/coercion-implicit-cue-v2b`](../../../experiments/designs/coercion-implicit-cue-v2b.md); governing operationalization (ratified): [`decisions/resolved/cc-v2-difficulty-operationalization`](../../decisions/resolved/cc-v2-difficulty-operationalization.md); run record: [`experiments/runs/2026-05-30-coercion-implicit-cue-probe-v2b/`](../../../experiments/runs/2026-05-30-coercion-implicit-cue-probe-v2b/README.md).

## What it tests

[`result/argument-structure-coercion-v2`](argument-structure-coercion-v2.md) showed the caused-motion ceiling drops to floor under an **explicit** outcome denial ("…off the table, **but the napkin never moved**") and read that as **H-deep** (the model computes the inference and withholds it under a resolving cue). But an explicit clause contradicts the hypothesis **in the premise**. v2b asks the harder question: does the model block a **physically impossible** coercion (a sneeze moving an immovable object) from **world knowledge alone**, with **no outcome stated** — or does it need the explicit statement?

Three conditions, verb + path held constant, object varied: `canonical` (light object → coerced motion plausible), `implicit-wk` (immovable object via an in-premise descriptor — *bolted-down bust*, *cast-iron anvil* — **no outcome stated**), `explicit` (immovable object **+** an explicit outcome denial). Indicator: affirm-caused-motion rate (FC YES / NLI entailment), both instruments, the 3-family panel.

## One-line finding

**The models do NOT block the impossible coercion from world knowledge alone — they need the explicit outcome statement.** With only the in-premise immovability descriptor, affirm-caused-motion stays at **near-ceiling (implicit-wk 90–100%; the lone exception is gpt-5.4-mini under FC at 40%)**; only the **explicit** outcome denial drives it to **floor (0%, gpt-5.4-mini FC 10%)**. So the v2 cue-sensitivity is **explicit-outcome parsing, not world-model integration** — a finding that **bounds the v2 H-deep reading**: respecting an explicit denial is a weaker competence than computing-and-world-checking the inference.

## Numbers

Affirm-caused-motion rate (%), 10 scenes × {canonical, implicit-wk, explicit}, 0 NA / 180 calls:

| model | instr | canonical | implicit-wk (world-knowledge) | explicit (outcome denial) | implicit − explicit |
|---|---|---|---|---|---|
| claude-sonnet-4.6 | NLI | 100.0 | 100.0 | 0.0 | 100.0 |
| claude-sonnet-4.6 | FC | 100.0 | 90.0 | 0.0 | 90.0 |
| gpt-5.4-mini | NLI | 100.0 | 90.0 | 0.0 | 90.0 |
| gpt-5.4-mini | FC | 60.0 | 40.0 | 10.0 | 30.0 |
| gemini-3.5-flash | NLI | 100.0 | 100.0 | 0.0 | 100.0 |
| gemini-3.5-flash | FC | 100.0 | 100.0 | 0.0 | 100.0 |

The discriminator is **implicit-wk vs explicit**: a model that blocked the impossible coercion from world knowledge alone would show **low** implicit-wk affirm; instead implicit-wk is near-ceiling and the explicit cell is floor → the explicit outcome statement, not the world-knowledge conflict, is what the models respond to.

## Instrument note (reported, not corrected)

Under **NLI** the implicit-wk premise *asserts* the caused motion; the conflict is only with **external** world knowledge about "bolted-down", so high NLI affirm is partly premise-internal reasoning (taking the premise's little world at face value). The decisive cells are therefore the **FC** ones, where the question ("is it true that …") more naturally engages world knowledge — and there **claude (90%) and gemini (100%) still affirm the impossible coercion**, while **only gpt-5.4-mini partially engages world knowledge** (implicit-wk 40%, explicit 10%, and a depressed canonical 60%). So the negative is robust to the instrument worry for 2/3 models. The NLI-vs-FC split on the implicit-wk cell is itself a first-class datum for [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md).

## A unifying observation with the CC result

Read alongside [`result/comparative-correlative-covariation-v2`](comparative-correlative-covariation-v2.md), a consistent disposition appears: **the panel takes the construction's stated content at face value and does not override it with world knowledge.** In the CC conflicting-cue arm that is *correct* (the construction explicitly asserts the covariation direction, so following it against world knowledge is right — ~100% follow-construction). Here it is *questionable* (the construction asserts a physically impossible event, and following it ignores world knowledge). Only an **explicit in-premise denial of the outcome** flips the caused-motion judgment. "Follow the stated construction over world knowledge" is one disposition that is right in one case and wrong in the other.

## Caveats (lead first)

- **The implicit-wk gold is contestable.** A sentence can *assert* an impossible event; whether the right answer is "affirm (the premise says so)" or "withhold (it can't happen)" is genuinely unsettled for humans too. This is why the arm is **internal-contrast-only** with **no human baseline** (`anchor: internal-contrast-only`, [`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)); the result is read as the implicit-vs-explicit *contrast*, not as a below-human error rate. No human label invented.
- **Small N** (10 scenes × 3 conditions × 3 models); direction-of-effect, not precise magnitude.
- **canonical anchor.** The `canonical` arm keeps the v1/v2 phenomenon-level caused-motion anchor ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)); pre-run critique fixed propulsive verbs (huff/puff) so the canonical YES is genuinely coerced, not literal.
- **Scope.** Only the world-knowledge cue axis ran; near-miss form controls and multi-step composition remain for a later run (documented, not retuned).

## Bearing

**Refines** [`result/argument-structure-coercion-v2`](argument-structure-coercion-v2.md) by bounding its H-deep reading to "respects explicit outcome statements" rather than "integrates world knowledge." Feeds [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md) (the coercion-cancellation competence is shallower than v2 alone suggested). Internal-contrast-only by ratified decision ([`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md), 2026-05-31). Cost **$0.158 billed** (token-estimate $0.039 undercounts; see [`config/budget.md`](../../../config/budget.md)); 0 NA / 180 calls.
