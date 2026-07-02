---
type: essay
id: presupposition-environment-gated
title: "The presupposition corner is environment-gated in both directions — one distributional shape, two signatures"
meaning-senses:
  - inferential
  - distributional
status: draft
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-02
updated: 2026-07-02
links:
  - rel: refines
    target: essay/projection-defeasible-by-frame
  - rel: supports
    target: conjecture/presupposition-environment-gated-both-directions
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: result/projection-trigger-inventory-v1
  - rel: depends-on
    target: result/presupposition-accommodation-v1
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
---

# The presupposition corner is environment-gated in both directions

**Thesis.** At the presupposition corner, what a semantic theory treats as an *inferential*
competence — a represented presupposition/assertion split that ought to hold **invariantly** across
embeddings and contexts — presents behaviorally, across **both** of its classic signatures, as
sensitivity to the *licensing environment*. **Projection** is gated by the embedding **frame** (the
presupposition survives negation, collapses under the conditional antecedent); **accommodation** is
gated by **context support** (the unmet presupposition is supplied in a neutral context, attenuated
under explicit contradiction). One distributional description — *follow the surface cue; its
reliability is set by the environment* — predicts both. The sibling essay
[`essay/projection-defeasible-by-frame`](projection-defeasible-by-frame.md) argued this for
projection alone. This essay's contribution is narrower and more structural: the **same** shape
appears in the *other* signature too, so environment-gating is better read as a property of how these
text-trained decoders handle the phenomenon than as an artifact of one embedding manipulation.

This is a philosophical reading of two within-model results, each at `internal-contrast-only`
strength. It reads a *description*, not a mechanism; it claims no access to what the models internally
compute, and it makes no human comparison — none was measured. It is weak evidence at one grammatical
corner, and it is written to be knocked down.

## Two signatures, two results

The presupposition corner has two behavioral signatures the SEP survey keeps distinct
([`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md),
§1.2 projection, §5 accommodation). The project has now probed both within-model.

**Projection is frame-gated.** Across eight trigger families
([`result/presupposition-projection-v1`](../results/presupposition-projection-v1.md),
[`result/projection-trigger-inventory-v1`](../results/projection-trigger-inventory-v1.md)) the panel
gives the textbook survival under **negation** — the cleanest cell, where two of three models endorse
the presupposition on every item while the matched entailment cancels completely — and the
presupposition **collapses under the conditional antecedent** for every model. In the first run
presupposition-survival under the conditional frame is **0.42 / 0.17 / 0.17**, at or near the
matched-entailment leg; the trigger-inventory run reproduces the collapse on four brand-new families
at **0.25 / 0.17 / 0.00**. The failure tracks the *embedding frame*, not the item or trigger — the
load-bearing observation the sibling essay is built on.

**Accommodation is context-gated.** Across four trigger families
([`result/presupposition-accommodation-v1`](../results/presupposition-accommodation-v1.md), verdict
GATED-ACCOMMODATION 3/3) the unmet presupposition is supplied near-ceiling in a **neutral** context
(neutral-endorse **1.00 / 0.92 / 1.00**) and substantially withheld under **explicit contradiction**
(contradicting-endorse **0.33 / 0.58 / 0.42**), clearing the frozen gating bar
(accommodation-gap **+0.67 / +0.33 / +0.58**). The endorsement tracks *context support*.

In both lines the panel does **not** behave the way a frame-/context-invariant semantic
representation would: it does not endorse (or withhold) the presuppositional inference uniformly
regardless of the environment. It endorses where the licensing environment permits and withholds
where the environment resists. That common shape — sensitivity to the environment rather than
invariance across it — is this essay's object.

## Why "environment-gated in both directions" is one shape, not two coincidences

It would be possible to read the two results as unrelated facts: one about how embeddings scope
inferences, the other about how discourse context licenses accommodation. The claim here is that they
are **two instances of one description**, and the reason is that the two "gates" are the same kind of
thing pointed at different axes of the design.

The projection probe holds a presupposition fixed and varies the **embedding**; the accommodation
probe holds the trigger sentence fixed and varies the **context**. In each, the question the model
faces is the same at the level of surface cues: *does the licensing environment leave the trigger's
presuppositional cue unopposed, or does it place a competing cue on the surface?* Under **negation**,
"X didn't stop Y-ing" co-occurs in text with the continued truth of "X used to Y" — the
presupposition rides the surface string with high reliability, and it survives. Under the
**conditional antecedent**, the same backgrounded content sits in the frame where — per the source —
projection is independently hardest: "Presuppositions typically project, but often do not"
([`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md),
§1.3). The surface cue is weakest there, and it collapses. On the accommodation side the mechanics
are parallel: a **neutral** context leaves the trigger's own cue unopposed → supplied; a
**contradicting** context places an explicit ¬P on the surface → attenuated.

So the same one-line account — *follow the surface cue; its reliability is set by the environment* —
predicts frame-gating in one signature and context-gating in the other. The two axes (which
embedding, which context) differ, but the gating relation is identical: endorsement is high exactly
where the environment makes the presuppositional inference surface-reliable, and it falls exactly
where the environment makes it unreliable or puts a conflicting cue on the surface. That a single
description reaches across both signatures is what makes environment-gating look like a property of
the *phenomenon-handling*, not a property of the one manipulation the sibling essay studied.

## Why the distributional description fits the shape better than "computes the split"

Read the shape through [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md).
A next-token learner reproduces the surface regularities in which triggers and their continuations
co-occur, without that tracking having to encode the presupposition as a represented semantic object
(the "extent of the construction" confound that concept page flags from Weissweiler et al.). Such a
learner is *predicted* to endorse a presuppositional inference exactly where the environment makes it
surface-reliable and to withhold it where the environment makes it unreliable — which is the
two-directional gating the results show.

Now put beside it the description a semantic theory would license. A system that had computed a
**presupposition/assertion split** — a genuine representation of what a sentence backgrounds versus
what it asserts — would carry that split *through* the licensing environment, because the whole point
of the split is that backgrounded content is not in the operator's scope and is not answerable to the
local discourse. That description predicts **invariance**: projection roughly frame-invariant across
negation, question, and conditional; accommodation roughly context-invariant in whether the
backgrounded content is treated as given. Neither invariance is what the panel does. Its projection is
frame-conditioned; its accommodation is context-conditioned. So the ostensibly **inferential**
competence ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)) — where the
indicator is which inference is licensed, not co-occurrence — comes out, at this corner and in *both*
of its signatures, looking **distributional**.

This is the co-tagged tension [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)
keeps live — the two senses are entangled in a next-token learner, and here the entanglement resolves,
across both signatures of one corner, on the distributional side. The sibling essay resolved it for
projection; the generalization is that the resolution does not depend on the projection manipulation.
It is still one data point, at one grammatical corner, and it does not generalize to the project's
other inference-licensing results — several of which show strong, frame-robust inference-preservation.
It is a case, not a verdict.

## What this essay does *not* claim

- **No mechanism.** "Better described as distributional" is a claim about which *description* fits the
  behavioral pattern, not about what the models compute internally. Endorsing (or declining) a
  presuppositional inference off a forced-choice answer is text-consistent-with a description; it is
  not a read of internal representation. The essay asserts nothing about internal representation,
  either way — and in particular does not claim the models *lack* a represented split.
- **No human comparison.** Both underlying lines are within-model contrasts, each
  `internal-contrast-only` (the projection line ratified in sessions 159/161, the accommodation line
  in session 163). Nothing here compares the panel to human projection or accommodation judgments;
  none were measured. The SEP material enters only as an a-priori map of *where in the grammar* each
  signature is environment-sensitive, never as a baseline. This matters especially because the source
  records that even the *human* pattern is defeasible at the conditional antecedent (§1.3), so the
  collapse is not by itself a "the model is wrong" finding.
- **Not exhaustive.** Two signatures, one panel of three 2026 commercial models, small synthetic item
  sets (12 project-authored scenarios per line). No coverage claim; direction-of-effect only. The
  essay offers the distributional description as the better-fitting one at this corner, not as a
  demonstrated property of language models in general.

## The counter-texture that could break the reading

An honest reading has to carry the friction, and there is real friction on the accommodation side.

First, the gate is **partial, not clean**. Contradicting-endorse is **0.33 / 0.58 / 0.42**, not near
zero: the models still endorse an explicitly-denied presupposition a third to a half of the time. The
trigger's cue and the discourse's denial *both* pull, and the denial only partly wins. "Gated" names a
within-panel attenuation, not an on/off block.

Second, there is a **residual yes-bias pocket**, and it is located rather than hypothetical:
gpt-5.4-mini endorses the cleft existential **100% of the time even under explicit contradiction**
("The memo was never leaked to anyone. It was the intern who leaked the memo." → YES). For that model
on that family the gate is fully open. The panel-level gating verdict is carried by the other
families; one model has a trigger family where accommodation is indiscriminate. If that pocket turned
out to *dominate* rather than be localized — if endorsement were mostly environment-*insensitive*
yes-bias — then "gated" would be the wrong word and the environment-sensitivity reading would fail.

Third, and most fundamental: the accommodation "gate" **cannot behaviorally separate** genuine
accommodation-*blocking* from generic contradiction-detection plus a yes-bias. A model that says NO in
the contradicting condition may be blocking accommodation, or it may simply be detecting the explicit
¬P on the surface (a *never / no one / nothing* or a lexical antonym) and reporting the contradiction.
The result page fences this openly, and the `internal-contrast-only` framing is exactly what keeps the
finding to the *within-model contrast between contexts* rather than a claim that the model *computes*
accommodation. For this essay the point cuts a specific way: the alternative reading — surface
contradiction-detection plus yes-bias — is *itself a distributional story*, so it does not rescue the
"computes the split" description; but it does mean the accommodation leg is weaker evidence for
*environment-gating specifically* than the clean neutral-vs-contradicting gap makes it look. The essay
owns that the accommodation signature is the softer of the two.

## Revision triggers (the essay's own puncture test)

An essay in this project must name what evidence revises or retracts it. These are the punctures.

- **If a queued cue-strength probe shows accommodation's gate is *not* graded by contradiction
  strength** — i.e. a stronger surface contradiction does not gate harder, and the gate is on/off
  rather than graded — then the "graded distributional cue" gloss on the accommodation leg is strained.
  Revise toward a cleaner contradiction-detection reading of that signature (which is still
  distributional, but no longer the same *graded environment-reliability* story that unifies it with
  projection).
- **If either signature turns out environment-*invariant*** — projection frame-invariant (the
  presupposition survives, or fails, uniformly across negation / question / conditional), or
  accommodation context-invariant (P supplied — or withheld — regardless of
  supported / neutral / contradicting) — then **retract** "environment-gated in both directions." The
  whole shape depends on the gating being real on each axis.
- **If the yes-bias pocket turns out to dominate rather than be localized** — if endorsement across
  families is mostly environment-insensitive yes-bias with a few gated exceptions, rather than the
  reverse — then "gated" is the wrong word for the accommodation signature and the parallel breaks.
- **If a probe isolates a frame-/context-invariant presupposition/assertion split** — the model
  endorsing exactly the backgrounded content and only it, stably across frames and contexts, in a way
  a surface-cue account cannot reconstruct — then the balance tips toward "computes the split" over the
  distributional reading, in at least the signature where the invariance shows up.
- **If either underlying result's numbers move on re-run**, the empirical premises above move with
  them and this reading is re-examined here in-page.

Until such probes are run, this stays a **draft** synthesis: a reading that fits the two measured
signatures, calibrated to their `internal-contrast-only` strength, generalizing the sibling essay's
frame-shaped claim to the corner's other signature, and written so a single environment-invariant
result could knock it down.
