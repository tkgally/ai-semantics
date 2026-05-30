---
type: design
id: coercion-as-sense-modulation-v1
title: coercion as lexical sense modulation — does constructional coercion register as a verb-sense shift in the DWUG-style relatedness instrument? (the lexicon–grammar bridge probe)
meaning-senses:
  - constructional
  - referential
  - inferential
status: ready
anchor: pending
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: operationalizes
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: result/caused-motion-near-miss-v2c
---

# Design — coercion as lexical sense modulation (v1, the lexicon–grammar bridge)

**The empirical bridge proposed by [`theory/lexicon-grammar-continuum`](../../wiki/findings/theory/lexicon-grammar-continuum.md).** It reuses the **lexical** sense-relatedness instrument built for [`result/lexical-sense-gradience-v1`](../../wiki/findings/results/lexical-sense-gradience-v1.md) on **constructional** (coercion) stimuli, so a result speaks to both wedges at once. Internal-contrast-only (`anchor: pending` — no in-repo human relatedness rating for constructed coercion pairs; same status as the off-ceiling constructional probes, tracked by [`decisions/open/conflicting-cue-human-anchor`](../../wiki/decisions/open/conflicting-cue-human-anchor.md)). Operationalization fixed under Tom's standing delegation (rigorous, no new gated decision — it reuses ratified instruments).

## The bet

Constructional coercion ([`concept/coercion`](../../wiki/base/concepts/coercion.md)) — the caused-motion construction making *sneeze* contribute causation-of-motion in *she sneezed the napkin off the table* — **is** a grammar-induced shift in the verb's sense. If a model registers coercion *as sense modulation*, then asking (with the DWUG-style relatedness rating) how related the **verb's** meaning is between its bare use and its coerced use should yield a **lower** relatedness than between its bare use and a length-matched **non-coercing** elaboration. Coercion would then show up *inside the lexical instrument* — the join the two wedges never tested together.

## Instrument (reused verbatim from the lexical v1 probe)

The same target-marked, two-framing relatedness rating: `durel` (4-point: 4 Identical / 3 Closely Related / 2 Distantly Related / 1 Unrelated) + `cont` (0–100). The **target is the verb**, marked with «guillemets» in both sentences. Temperature 0, logprob-free → the 3-family panel ([`config/models.md`](../../config/models.md)). (No `topic` framing here — the contrast is within-verb, frame-controlled.)

## Arms (each item = one verb, two sentences; sentence 1 is the bare/neutral use, sentence 2 varies)

| arm | sentence 2 relative to the bare use | predicted relatedness |
|---|---|---|
| `coerced-cm` | the **caused-motion** coercion (*…sneezed the napkin off the table*) | **lower** (sense shifted) |
| `coerced-way` | the **way-construction** coercion (*…sneezed her way down the hall*) | **lower** (self-traversal sense added) |
| `control-elab` | a **length-matched non-coercing** elaboration of the same verb (*…sneezed all through the lecture*) | **high** (same sense, just more context) |
| `polysemy-anchor` | a genuine lexical **sense shift** of a polysemous verb (*ran a race* → *ran a company*) | **low** (calibration: the instrument can detect a real sense shift) |

The `control-elab` arm is the key control: it matches the coerced arm for "sentence 2 adds material / is longer," so a coerced-vs-control gap isolates the *coercion*, not mere elaboration. `polysemy-anchor` calibrates the low end (the instrument must register an uncontested sense shift as low-related, else a null on the coerced arm is uninterpretable).

## Reading rule (report-the-rate; no pass bar; internal-contrast)

Per model per framing: mean relatedness per arm, and the **coercion sense-shift gap** = relatedness(`control-elab`) − relatedness(`coerced-cm`/`coerced-way`). A **positive** gap (coerced rated less sense-related than the matched elaboration) = the model registers constructional coercion as lexical sense modulation; a **null** gap (coerced ≈ control) = it does not, treating the coerced verb as the same sense. Either is first-class. `polysemy-anchor` must read low for the run to be interpretable. No threshold tuned post-run.

## Human anchor

**Pending / internal-contrast-only.** No in-repo human relatedness rating exists for constructed coercion pairs; the result makes no human-comparison claim. The DWUG-anchored *instrument* is validated by [`result/lexical-sense-gradience-v1`](../../wiki/findings/results/lexical-sense-gradience-v1.md) (it tracks human DURel), but these specific items are the project's own, with no human gold — so the headline is the within-verb arm contrast, not accuracy.

## Pre-registration

Own constructed stimuli, frozen + committed (sha256) before any probe call; verbs drawn from the caused-motion / way set already used (so the coercion is independently evidenced by [`result/caused-motion-near-miss-v2c`](../../wiki/findings/results/caused-motion-near-miss-v2c.md) / [`result/way-construction-traversal-v1`](../../wiki/findings/results/way-construction-traversal-v1.md)). Independent read-only pre-run critique of the stimuli (are the control elaborations genuinely non-coercing and length-matched? is the polysemy anchor a real sense shift?) before the run; independent post-run number verification.
