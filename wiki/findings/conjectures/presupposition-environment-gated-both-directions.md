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
updated: 2026-07-05
links:
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: result/projection-trigger-inventory-v1
  - rel: depends-on
    target: result/presupposition-accommodation-v1
  - rel: depends-on
    target: result/accommodation-cue-strength-v1
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

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The corner's owed matched surface-cue
> control has since run (session 173):
> [`result/presupposition-doppelganger-control-v1`](../results/presupposition-doppelganger-control-v1.md)
> returns **BEATS-DOPPELGANGER** (pooled residual +0.78 / +0.47 / +0.94, 3/3; the clean FLAT null did
> not obtain) — **but BEATS is the under-licensed outcome**: the residual is keyed to the trigger
> **word-form** and remains reconstructable by a verb-sensitive surface-cue follower, so it does not
> move the corner to the beater side. The result's anchor was ratified `internal-contrast-only` in
> session 174, and the line remains the last unpromoted B1 candidate — B1 has promoted 5 of its 6
> candidate lines (s168–s177); this one's promotion review is still owed, and given the
> under-licensing a written refusal would be a legitimate outcome.
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

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
  contradiction gates harder), paralleling projection's graded frame effect. **✓ Confirmed within-model
  (session 164):** [`result/accommodation-cue-strength-v1`](../results/accommodation-cue-strength-v1.md)
  split v1's single contradiction into a hedged (weak) and an emphatic (strong) denial of the same P
  and found **GRADED-GATE (3/3)** — every model endorses the denied P more under the hedged denial than
  the emphatic one (strength-gradient +0.33 / +0.17 / +0.67, all ≥ 0.15; B robustness-checked). A pure
  contradiction-detector would gate weak and strong equally; the graded drop is the cue-strength
  signature. This strengthens (does not prove) the bet, within the `internal-contrast-only` fence; the
  softest margin (B, +0.17) and the family non-uniformity are carried on the result page.

**A related within-model probe that is deliberately NOT counted as confirming evidence (session 166).**
The commitment-framing decomposition
([`result/commitment-framing-model-difference-v1`](../results/commitment-framing-model-difference-v1.md),
verdict PARTIAL) held the conditional sentence fixed and varied only the *metalinguistic question
wording* (from "everything the speaker takes for granted" to "only … the main point"), finding that
one model's (claude's) presupposition-endorsement is strongly movable by that wording while another's
(gpt's) is not. It is tempting to read this as another instance of "endorsement follows the surface
cue" — but it is **not** logged as a confirming arm, and the reason is a discipline this conjecture
should state: the two anchor wordings are *elicitation-designed to separate*, so a system that
genuinely **computed** a presupposition/assertion split would *also* answer the backgrounding question
high and the at-issue question low. A metalinguistic question that names "what is taken for granted"
versus "the main point" therefore cannot, on its own, discriminate the distributional description from
the semantic one — unlike the confirming criteria above, which vary the *licensing environment*
(embedding frame, context support, cue strength) while holding the trigger's semantic status fixed. The
s166 result does, however, bear on the projection line's *model-level texture*: it retires the
"gpt reads 'committed' restrictively" reading (gpt keeps projection low under every framing, a general
floor, not a narrow reading — see [`essay/projection-defeasible-by-frame`](../essays/projection-defeasible-by-frame.md)),
which removes one alternative story but neither confirms nor falsifies this bet.

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

The cue-strength probe testing exactly this **has now run** (session 164) —
[`experiments/runs/2026-07-02-accommodation-cue-strength/`](../../../experiments/runs/2026-07-02-accommodation-cue-strength/README.md),
verdict **GRADED-GATE (3/3)** ([`result/accommodation-cue-strength-v1`](../results/accommodation-cue-strength-v1.md)),
confirming the cue-strength arm. This conjecture stays **proposed** — one confirmed arm at one
grammatical corner is a strengthening, not a demonstration — a synthesis that fits the measured
signatures, calibrated to their `internal-contrast-only` strength, and still written to be knocked
down (the falsifying criteria above remain live).
