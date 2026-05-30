---
type: design
id: coercion-implicit-cue-v2b
title: caused-motion v2b — does the model block an impossible coercion from an implicit world-knowledge cue, or does it need the explicit outcome statement?
meaning-senses:
  - constructional
  - inferential
  - distributional
  - human-comparison
status: provisional
anchor: pending
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: refines
    target: result/argument-structure-coercion-v2
  - rel: operationalizes
    target: conjecture/caused-motion-construction
  - rel: depends-on
    target: design/argument-structure-coercion-v2
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
---

# Experiment design v2b — caused-motion, implicit (world-knowledge) cue

> **Status: provisional.** The **v2b** the add-direction v2 explicitly deferred (its README: "the cue is an *explicit verbal denial* … a subtler world-knowledge cue is v2b"). Governed by the **same ratified gate** ([`decisions/resolved/cc-v2-difficulty-operationalization`](../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md): conflicting-cue primary + graded ladder + report-the-rate) — **no new decision**; `contingent-on: []`.

## Why — what the explicit-cue v2 left open

[`result/argument-structure-coercion-v2`](../../wiki/findings/results/argument-structure-coercion-v2.md) showed the caused-motion / way ceilings are cue-sensitive: under an **explicit** outcome denial ("…off the table, **but the napkin never moved**") all three models drop to floor (H-deep over H-default). But the explicit clause directly contradicts the hypothesis **in the premise**; it does not test whether the model integrates **world knowledge** to block a *physically impossible* coercion when **no outcome is stated**. That is the subtler, more demanding cue.

## Manipulation (verb + path held constant; object + cue type varied)

Hypothesis: *"&lt;subj&gt;'s &lt;gerund&gt; caused &lt;obj&gt; to move."*

| condition | difficulty | example | affirm-motion gold |
|---|---|---|---|
| `canonical` | 1 | Maria sneezed the dust off the pedestal. | YES (light object; the v1/v2 ceiling anchor) |
| `implicit-wk` | 2 | Maria sneezed the **bolted-down bust** off the pedestal. | NO — world knowledge (bolted-down) blocks it; **no outcome stated** (contestable, see anchor) |
| `explicit` | 3 | Maria sneezed the bolted-down bust off the pedestal, **but it never budged.** | NO — outcome stated (the v2-style cue, here as the within-experiment calibration) |

**Key discriminator: implicit-wk affirm vs explicit affirm.** If they are comparably low, the model blocks the impossible coercion **from world knowledge alone** (a stronger H-deep signal than v2 established). If implicit-wk affirm is much higher, the model **needs the explicit outcome statement** — the v2 cue-sensitivity was outcome-parsing, not world-model integration.

## Instrument note (reported, not corrected)

Under **NLI** the implicit-wk premise *asserts* the caused motion; the conflict is only with **external** world knowledge about "bolted-down", so a premise-internal NLI reading may affirm. Under **FC** ("is it true that …") world knowledge is more naturally engaged. The **NLI-vs-FC gap on the implicit-wk cell is itself a first-class datum** (cf. [`open-question/instrument-sensitivity-constructional-inference`](../../wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md)); both instruments are kept and reported separately, as ratified.

## Indicator, reading rule, anchor

Indicator: affirm-caused-motion rate per condition (FC YES / NLI entailment), temperature 0, logprob-free, both instruments. **Reading rule (ratified report-the-rate):** report the implicit-vs-explicit gap and the two canonical→cue drops per instrument; no manufactured pass bar; either reading is first-class. **Human anchor: pending / internal-contrast-only** (Option-4 logic, same as v2) — Scivetti has no conflicting-cue / impossible-coercion items and the "correct" reading of a physically-impossible coercion is contestable for humans, so **no human-level claim** on the cue cells; no human label invented. The `canonical` arm keeps the v1/v2 phenomenon-level caused-motion anchor ([`resource/scivetti-2025-cxnli-dataset`](../../wiki/base/resources/scivetti-2025-cxnli-dataset.md)).

## Scope (documented, not retuned)

This v2b runs the **world-knowledge cue** axis only (the headline piece v2 deferred). The other deferred arms — **near-miss form controls** and **multi-step composition** — remain for a later run; running the most-discriminating axis in full (10 scenes × {canonical, implicit-wk, explicit}) is a scope choice fixed before the build, not a retune.

## Harness / freeze / budget

Reuses the v2 harness verbatim. Items frozen before any probe call (`items.csv` sha256[:16] `9aad20a22d183402`, after the pre-run critique verb fixes; 30 items = 10 scenes × 3 conditions). 30 × 2 instruments × 3 models = 180 calls; expected ≈ $0.03–0.05 (cf. v1 caused-motion $0.044). Pre-flight per [`config/budget.md`](../../config/budget.md).
