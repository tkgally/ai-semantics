---
type: conjecture
id: presupposition-environment-gated-both-directions
title: "Presuppositional inference in current decoders is environment-gated in BOTH of its signatures — projection by embedding frame, accommodation by context support — a two-directional distributional signature"
meaning-senses:
  - inferential
  - distributional
status: proposed
contingent-on: []
created: 2026-07-01
updated: 2026-07-02
links:
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: result/projection-trigger-inventory-v1
  - rel: depends-on
    target: result/presupposition-accommodation-v1
  - rel: depends-on
    target: essay/projection-defeasible-by-frame
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
---

# Conjecture: presuppositional inference is environment-gated in both directions

**The bet (one sentence).** Current text-trained decoders' handling of presupposition is
**environment-gated in both of the phenomenon's behavioral signatures** — *projection* (whether a
presupposition survives an embedding) is gated by the **embedding frame**, and *accommodation*
(whether an unmet presupposition is supplied) is gated by **context support** — and this
two-directional sensitivity to the *licensing environment* is better described as a distributional
surface-cue regularity (endorse the presuppositional inference where the environment makes it
surface-reliable, withhold it where the environment makes it unreliable or contradicts it) than as
the output of a system that carries a frame- and context-invariant presupposition/assertion split.

This is a **proposed synthesis**, not a demonstrated fact. It generalizes across two behavioral lines
that the project has now measured within-model; it is weak evidence, at one grammatical corner, and it
inherits every scope limit of the results it rests on. It is stated so it can be **falsified**.

## What it rests on (both measured within-model, no human comparison)

The presupposition corner has two classic behavioral signatures (SEP survey
[`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md),
§1.2 projection, §5 accommodation). The project has now probed both:

- **Projection is frame-gated.** Across eight trigger families
  ([`result/presupposition-projection-v1`](../results/presupposition-projection-v1.md),
  [`result/projection-trigger-inventory-v1`](../results/projection-trigger-inventory-v1.md)) the
  presupposition survives near-perfectly under **negation** and **collapses under the conditional
  antecedent** for every model — the failure tracks the *embedding frame*, not the item or trigger
  ([`essay/projection-defeasible-by-frame`](../essays/projection-defeasible-by-frame.md)).
- **Accommodation is context-gated.** Across four trigger families
  ([`result/presupposition-accommodation-v1`](../results/presupposition-accommodation-v1.md), verdict
  GATED-ACCOMMODATION 3/3) the unmet presupposition is supplied near-ceiling in a **neutral** context
  and substantially withheld under **explicit contradiction** — the endorsement tracks *context
  support*.

In both lines the model does **not** behave the way a frame-/context-invariant semantic representation
would: it does not endorse (or withhold) the presuppositional inference uniformly regardless of the
environment. It endorses **where the licensing environment permits** and withholds **where the
environment resists**. That common shape — sensitivity to the environment rather than invariance
across it — is the conjecture's object.

## Why the distributional description fits the common shape

Read through [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md): a
next-token learner reproduces the surface regularities in which triggers and their continuations
co-occur, without that tracking having to encode the presupposition as a represented semantic object.
Such a learner is predicted to endorse a presuppositional inference exactly where the *environment
makes the inference surface-reliable*, and to withhold it where the environment makes it unreliable or
puts a conflicting cue on the surface:

- **Projection:** "X didn't stop Y-ing" co-occurs in text with the continued truth of "X used to Y"
  (surface-reliable) → survives; a conditional antecedent is the frame where projection is
  independently graded and the surface cue weakest → collapses.
- **Accommodation:** a neutral context leaves the trigger's own presuppositional cue unopposed on the
  surface → supplied; a contradicting context places an explicit ¬P on the surface → attenuated.

So the *same* distributional account — "follow the surface cue; its reliability is set by the
environment" — predicts frame-gating in one signature and context-gating in the other. The two
results are two instances of one description. An ostensibly **inferential** competence
([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)) — presupposition is
about which inference survives / is licensed, not co-occurrence — comes out, at this corner, looking
**distributional** in both of its signatures.

## What it does NOT claim

- **No mechanism.** "Better described as distributional" is a claim about which *description* fits the
  behavioral pattern, not about what the models compute internally. No internal-representation claim,
  either way.
- **No human comparison.** Both underlying results are within-model contrasts, each
  `internal-contrast-only` (ratified for the projection line in sessions 159/161, and for the
  accommodation line in session 163).
  Nothing here compares the panel to human projection or accommodation judgments; none were measured.
  The SEP material enters only as an a-priori map of *where in the grammar* each signature is
  environment-sensitive, never as a baseline.
- **Not exhaustive.** Two signatures, one panel of three 2026 models, small synthetic item sets. The
  bet is a description of a shape, offered as the better-fitting one — not a demonstrated property of
  language models in general.

## Confirmation / falsification criteria

**Confirming** evidence (would strengthen the bet):
- A probe that varies **surface-cue reliability** while holding the trigger's semantic status fixed,
  and finds endorsement tracks the *cue reliability* rather than the semantic status — in either
  signature.
- Accommodation's partial gate turning out to be **graded by cue strength** (a stronger surface
  contradiction gates harder), paralleling projection's graded frame effect.

**Falsifying** evidence (would break the bet):
- **Environment-invariance in either direction.** If projection turned out frame-invariant (the
  presupposition survives, or fails, uniformly across negation / question / conditional), or
  accommodation turned out context-invariant (P supplied — or withheld — regardless of
  supported/neutral/contradicting), the "environment-gated" description would be wrong.
- **Gating that tracks the semantic presupposition/assertion split *invariantly*** — i.e. the model
  endorses exactly the backgrounded content and only it, stably across frames and contexts, in a way a
  surface-cue account cannot reconstruct. That would favor the "computes the split" description over
  the distributional one.
- The residual **yes-bias pocket** (gpt-5.4-mini endorses the cleft existential even under
  contradiction;
  [`result/presupposition-accommodation-v1`](../results/presupposition-accommodation-v1.md))
  turning out to dominate rather than be a localized exception — if endorsement is mostly
  environment-*insensitive* yes-bias, "gated" is the wrong word.

A cue-strength probe testing exactly this is now designed and frozen (unrun) —
[`experiments/runs/2026-07-02-accommodation-cue-strength/`](../../../experiments/runs/2026-07-02-accommodation-cue-strength/README.md),
awaiting a pre-run-critic GO and a run session. Until it runs, this conjecture stays **proposed**: a
synthesis that fits the two measured signatures, calibrated to their `internal-contrast-only`
strength, and written to be knocked down.
