---
type: essay
id: projection-defeasible-by-frame
title: "Projection is defeasible by frame, not by item — a distributional signature"
meaning-senses:
  - inferential
  - distributional
status: draft
contingent-on: []
created: 2026-07-01
updated: 2026-07-01
links:
  - rel: refines
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
---

# Projection is defeasible by frame, not by item — a distributional signature

**Thesis.** The conditional-antecedent collapse in the s158 projection probe is not item-scattered
noise but a **frame-shaped** regularity — near-total under one embedding environment and near-absent
under another, consistently across every model and trigger family — and that shape is better
described as a **frame-conditioned distributional regularity** than as the output of a system that
*computes* a presupposition/assertion split, making it weak evidence against a "the model represents
presupposition semantically" reading and for a distributional one.

This is a philosophical reading of a single result at `internal-contrast-only` strength. It reads a
*description*, not a mechanism; the essay disclaims any access to what the models internally compute
and does not upgrade behavioral text-consistency into evidence of internal representation either way.

## The pattern the result hands us

The probe ([`result/presupposition-projection-v1`](../results/presupposition-projection-v1.md))
returns a pre-registered verdict of **PROJECTION** — two of three models pass the sanity floor and
endorse a base sentence's presupposition under entailment-cancelling frames far more than a matched
ordinary entailment (per-model gaps **+0.64** and **+0.72**; the third shows the same direction at
**+0.36** but falls just under the survival floor). But the headline number pools frames, and the
per-frame breakdown is where the interesting structure lives. Reading the result's own per-frame
table, presupposition-survival splits sharply by *which* embedding environment does the cancelling:

- **Negation** is the cleanest cell: two models give the textbook pattern — presupposition survives
  on all items, matched entailment cancels completely.
- **Question** projects strongly (presupposition-survival 0.83–1.00), with the matched entailment
  surviving somewhat more here because a question does not assert the entailment's negation.
- **Conditional antecedent** *collapses for every model*: presupposition-survival is
  **0.42 / 0.17 / 0.17**, at or near the matched-entailment leg (for one model, equal to it).

The result page states the shape plainly: "projection is **near-perfect under negation and strong
under questions, and COLLAPSES under the conditional antecedent for all three models**." The collapse
is **not** confined to one model, and per the result's per-family table every trigger family shows a
positive pooled projection-gap — so it is "not an artifact of one trigger type." The failure is
organized by the *embedding frame*, not scattered across items or triggers.

## Why "frame-shaped, not item-scattered" is the load-bearing observation

Two failure profiles are compatible with the same pooled survival number, and they license opposite
readings.

If the presupposition failed to survive on a *scattered* handful of items — some factives here, an
it-cleft there, no relation to the embedding environment — that would look like ordinary noise: a
system with a genuine but imperfect presupposition representation, misfiring idiosyncratically. It
would say little about the *kind* of competence in play.

What the result shows instead is the other profile. The failure is **aligned to one axis of the
design** — the embedding environment — and is near-total on that axis (conditional) while near-absent
on a parallel one (negation), holding across three independently trained models and four trigger
families. A failure that tracks the *frame* rather than the *item* is the signature that asks to be
explained by a property of the frame, not by per-item difficulty.

Here is the philosophical move. A system that had computed a **presupposition/assertion split** — a
genuine semantic representation of what the sentence backgrounds versus what it asserts — would carry
that split *through* the entailment-cancelling operators uniformly, because the whole point of the
split is that the backgrounded content is not in the operator's scope. Projection would look roughly
frame-invariant across negation, question, and conditional antecedent, because the represented object
(the presupposition) is the same in each. That is not what the panel does. Its projection is
**frame-conditioned**: strong exactly where the surface signal for projection is most reliable, weak
exactly where it is least.

## The distributional expectation, and why the collapse matches it

Now read the same pattern through [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md).
A next-token learner reproduces a **construction-conditioned surface regularity**: it tracks the
distributions in which triggers appear and the continuations they license, without that tracking
having to encode "the extent of the construction" or the projection as a represented semantic object
(the confound that concept page flags from Weissweiler et al.). If that is what is happening, one
predicts strength exactly where projection is *surface-reliable* and weakness exactly where the
environment makes the surface signal weakest.

The environments line up. Under **negation**, "X didn't stop Y-ing" overwhelmingly co-occurs, in
text, with the continued truth of "X used to Y" — the presupposition rides along on the surface
string with high reliability, so a distributional learner endorses it near-perfectly. Under a
**conditional antecedent**, the same backgrounded content is exactly where — per the SEP source —
projection is hardest and most defeasible: the source is explicit that "Presuppositions typically
project, but often do not" ([`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md), §1.3), and the
whole "projection problem" is the task of saying *when* they project and when they do not. The
conditional antecedent is a frame where the human pattern is graded and the surface cue is weakest;
it is exactly there that a distributional learner, tracking the surface regularity, would be expected
to fail. Reading the raw answers, the result reports the models "overwhelmingly return **UNCLEAR** (or
NO)" to the conditional's presupposition, "treating the whole conditional as merely hypothetical and
declining to extract the antecedent's backgrounded content."

So the very frame that a *semantic* representation would project through unchanged is the frame where
a *distributional* learner would be expected to break — and it is the frame that breaks. The
collapse is not a random shortfall; it is the collapse the distributional description predicts.
**Frame-shaped defeasibility is a distributional signature.**

Note the direction of the inference carefully. The SEP source records that even the *human* pattern
is defeasible at the conditional antecedent — projection there is graded, not a clean survival rule.
So the collapse is not, by itself, a "the model is wrong" finding; a graded human pattern makes a
graded model pattern unsurprising. The essay's claim is narrower and about *description*: given that
the model's grading tracks the *frame's* surface-reliability rather than being frame-invariant, the
distributional description fits the observed shape better than the "computes a presupposition/assertion
split" description does. That is consistent with the source's own "typically project, but often do
not," and it is the reading this essay argues for.

## The inferential-competence that turns out distributional

This is a small but pointed instance of the tension the concept pages keep live. Projection is,
on its face, an **inferential** competence: it is about which inference a construction licenses to
survive under embedding, a matter of inference-preservation rather than co-occurrence
([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)). The projection
diagnostic is precisely the kind of behavioral wedge that page and the source treat as *inferential*,
not distributional — "survival under embedding … not a distributional similarity."

Yet on this evidence the competence is better described in **distributional** terms. The panel does
not behave as though it holds a frame-invariant inferential object and reports whether it survives;
it behaves as though it tracks a frame-conditioned surface regularity that happens to be reliable
under negation and unreliable under the conditional antecedent. An ostensibly inferential competence,
probed at one grammatical corner, comes out looking distributional. That is exactly the co-tagged
tension [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md) names — the two senses are entangled in a next-token learner,
and here the entanglement resolves, for this frame, on the distributional side. It is one data point,
at one corner, and it does not generalize to the project's other inference-licensing results (several
of which show strong, frame-robust inference-preservation); it is a case, not a verdict.

## What this essay does *not* claim

- **No mechanism.** "Better described as distributional" is a claim about which *description* fits the
  behavioral pattern, not about what the model computes internally. Endorsing (or declining) a
  projected inference off a forced-choice answer is text-consistent-with a description; it is not a
  read of internal representation. The essay has no access to mechanism and asserts none.
- **No human comparison.** The result is `internal-contrast-only` (ratified by an independent
  session-159 adversarial review,
  [`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../decisions/resolved/presupposition-projection-internal-contrast-anchor.md)) — a
  within-model contrast between the presupposition leg and the matched-entailment leg. Nothing here
  compares the panel to human projection judgments; none were measured. The SEP material enters only
  as an a-priori interpretive frame for *where in the grammar* projection is defeasible, never as a
  human baseline.
- **No over-reach past the result.** Every empirical number above is the result page's own; the essay
  adds a reading, not data. The "distributional signature" claim is weak evidence, one result, one
  corner — offered as the better-fitting description, not a demonstrated fact about the models.

## Revision triggers (the essay's own puncture test)

A live follow-up probe this session tests whether the conditional-antecedent collapse is *rescued* by
reframing: (a) a speaker-commitment framing, (b) moving the trigger out of the antecedent, or (c) a
speaker-belief framing. The outcome is not asserted here — it may be unknown when this is written —
and there is as yet no result page for it; it is referred to only as a `conditional-antecedent rescue
probe`. It is this essay's puncture test, and it cuts both ways:

- **If a rescue framing RESTORES conditional projection** → the collapse was a surface-cue artifact
  rather than a deep limit, which *strengthens* the "frame-conditioned distributional regularity"
  reading (the model's projection is exactly as strong as the surface framing makes it, and a better
  framing restores the surface cue). Revise toward that reading, and toward calling the collapse a
  cue-sensitivity rather than a limit.
- **If the collapse is ROBUST to all three rescue framings** → the failure is not a mere surface-cue
  artifact but a genuine limit of the text-trained projection behavior at this frame. Revise toward
  the "genuine limit" reading; the distributional description still fits, but the collapse would be a
  standing boundary of the behavior rather than a rescuable cue effect.

Either way the essay's *core* description — projection here is frame-shaped, not item-scattered —
survives; what the rescue probe adjudicates is whether the specific conditional collapse is a
rescuable cue effect or a fixed limit. A third trigger: if the underlying result's numbers move on
re-run, this essay's empirical premises move with them and the reading is re-examined here in-page.
