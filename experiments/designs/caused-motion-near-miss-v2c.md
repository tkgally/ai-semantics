---
type: design
id: caused-motion-near-miss-v2c
title: caused-motion probe v2c — near-miss form controls (does the causation inference key on the construction form, or a looser "verb happened + object displaced" shape?)
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
    target: design/argument-structure-coercion-v2
  - rel: operationalizes
    target: conjecture/caused-motion-construction
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
---

# Design — caused-motion probe v2c (near-miss form controls)

**The near-miss form-control arm that [`design/argument-structure-coercion-v2`](argument-structure-coercion-v2.md) §3(d) specified and v2/v2b deferred** (v2b README: "the other deferred arms — near-miss form controls and multi-step composition — remain for a later run"). Governed by the same ratified [`decisions/resolved/cc-v2-difficulty-operationalization`](../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md) gate (report-the-rate, internal-contrast-only). **No new decision.** `anchor: pending`, tracked by [`decisions/open/conflicting-cue-human-anchor`](../../wiki/decisions/open/conflicting-cue-human-anchor.md).

## Why

[`result/caused-motion-minimal-pair-divergence-v1`](../../wiki/findings/results/caused-motion-minimal-pair-divergence-v1.md) found the panel affirms the caused-motion construction's causation-of-motion entailment onto **non-motion verbs at ceiling** (90–100%). Its controls were *absent-construction* (no displacement / object moved by another cause). v2c adds the harder **near-miss**: hold the verb + object + displacement **outcome** roughly constant and vary only the **form** between (a) the caused-motion **construction** ("Maria sneezed the napkin off the table") and (b) near-miss frames that report the same verb and end-state **without** construction-licensing the causation — a coordinated *and*-frame and a temporal-*sequence* frame. The construction **entails** that the subject's action caused the motion; the near-miss frames leave the causal link open (the displacement could be coincidental).

This is a sharper `functional-vs-formal` floor than v1: it asks whether the causation inference keys on the **argument-structure form** or on a looser "verb happened + object ended up displaced → caused it" shape (or a Gricean post-hoc-ergo-propter-hoc default).

## Instrument (reused verbatim from the caused-motion v1/v2b harness)

The hypothesis "`<Subj>`'s `<gerund>` caused `<obj>` to move." is **held identical across the three forms within each scene**, so the only thing that varies is the form. NLI 0/1/2; FC "is this statement true: `<hyp>`?" YES/NO/CANT_TELL. Temperature 0, no logprobs → the ratified 3-family panel ([`config/models.md`](../../config/models.md)).

## Arms (8 scenes × 3 forms; difficulty frozen pre-run)

| arm | d | form | example | affirm gold (entailment-correct) |
|---|---|---|---|---|
| `cm-construction` | 1 | the construction | *Maria sneezed the napkin off the table.* | affirm (v1 anchor) |
| `near-coord` | 2 | coordinated *and* | *Maria sneezed, and the napkin ended up off the table.* | withhold |
| `near-seq` | 3 | temporal sequence | *Maria sneezed. Moments later, the napkin was off the table.* | withhold |

Verbs are non-motion bodily/sound/air-displacement verbs (sneeze, cough, blow, laugh, whistle, fan, clap, puff) whose lexical semantics do **not** encode caused motion — so the construction is doing the work.

## Reading rule (ratified report-the-rate; no manufactured pass bar)

- Per-arm affirm-causation rate.
- **Construction-vs-near-miss gap** = `cm-construction` affirm − near-miss affirm, per model per instrument — the internal contrast. A **large** gap ⇒ the causation inference is keyed on the **construction form** (genuine constructional causation, tightening v1's floor). A **small** gap (near-miss affirmed too) ⇒ the v1/v2 ceiling is **not** construction-specific. Either is first-class.

**Gold contestability (disclosed, not retuned):** the near-miss "withhold" gold is the strict *entailment* reading. A Gricean reader may pragmatically infer causation from the coordinated frame, so a model that affirms near-miss is not simply "wrong" — which is exactly why the headline is the within-scene **gap** (report-the-rate), not accuracy against the near-miss gold.

## Human anchor

**Pending / internal-contrast-only.** Scivetti has no coordinated/sequence near-miss coercion items → no in-repo human norm on the near-miss arms. The `cm-construction` arm keeps the v1 phenomenon-level caused-motion anchor ([`resource/scivetti-2025-cxnli-dataset`](../../wiki/base/resources/scivetti-2025-cxnli-dataset.md)). No human label invented.

## Pre-registration

Items frozen + committed **before any probe call** (`items.csv` sha256[:16] `6d0b92e39b2d9eb8`); an `assert` in `build_items.py` checks the hypothesis is identical across the three forms within each scene. An independent read-only adversarial pre-run critique re-derives the affirm-gold direction and the form contrast before the run.
