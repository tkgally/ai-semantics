---
type: claim
id: dative-pronominality-partial-reach
title: Recipient pronominality — the largest information-structure factor in the human dative — cannot be cleanly isolated as a primary within-model behavioral effect under pure autonomy; it is a documented partial-reach (Option C), reported only via the human corpus production surface
meaning-senses:
  - constructional
  - distributional
  - human-comparison
status: supported
anchor: human-anchored
contingent-on: []
created: 2026-06-20
updated: 2026-06-20
links:
  - rel: anchors
    target: resource/languageR-dative-corpus
  - rel: depends-on
    target: result/dative-information-structure-v1
  - rel: depends-on
    target: result/dative-information-structure-v2
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: theory/constructional-meaning-in-llms
---

# Claim: recipient pronominality is a documented partial-reach on the dative line (Option C)

> **Status: supported (2026-06-20, session 56).** Realizes **Option C** of the ratified decision
> [`decisions/resolved/dative-pronominality-operationalization`](../../decisions/resolved/dative-pronominality-operationalization.md)
> (ADOPT OTHER, autonomous adversarial review — opened session 55, ratified session 56). This is a
> **reachability** result in the project's "text alone cannot reach this" family, **not** a behavioral
> finding about how a model handles pronominality: **no probe was run** ($0). It records what the
> dative instrument can and cannot reach, and why, and it cites the human corpus to fix the size of
> the factor left unreached.

## One-line claim

The dative line's information-structure result is reached for **givenness**
([`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md),
[`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md), replicated)
but **cannot be cleanly extended to recipient pronominality** — the *largest* information-structure
factor in the human corpus — as a primary within-model behavioral effect, because under pure autonomy
(no prompt logprobs) there is **no controlled forced-choice minimal pair that isolates pronominality
from length and givenness by construction**. Pronominality is therefore reported only on the human
side (where it is real and large) and left as a documented partial-reach, not a behavioral claim.

## Why the clean test does not exist (the substance of the closure)

The dative givenness result earns its rigour from one trick: the two phrasings the model scores (DOC vs.
PD) are **byte-identical across an item's two discourse contexts**, so the finding-bearing within-item
shift is **immune by construction** to every length-only, position-only, order-only, always-DOC,
always-PD, shorter-first, or longer-first reader (each yields shift = 0; certified at build and
re-derived by the v1/v2 pre-run critics). Pronominality cannot inherit this trick, for three structural
reasons — confirmed by the ratifying independent review against the frozen instrument:

1. **Pronominality is a property of the *test sentence*, not the swappable context.** Givenness is
   manipulated while holding the sentence fixed ("the customer" is given in one context, new in another).
   A pronoun is *in the sentence* ("…gave **him** the book" vs. "…gave **the customer** the book"). To
   vary it you must change the scored sentence, so the within-item, length-immune-by-construction measure
   **collapses into a between-item contrast whose sentences differ** — the immunity is gone.
2. **A pronoun is intrinsically the shorter constituent** (`him` = 1 word; corpus `LengthOfRecipient`
   ranges 1–31, mean 1.84), so a "pronominal recipient → DOC" effect is **confounded with the
   short-before-long end-weight heuristic** — the precise confound the ratified control architecture
   exists to neutralize. Worse, the design's dissociation cell (the *given* constituent made the
   *longer* one, so information structure and end-weight oppose) **cannot be built for a pronoun at
   all**, because a pronoun is never the longer constituent.
3. **Pronominality is near-collinear with givenness.** One pronominalizes a referent *because* it is
   given; pronoun and given travel together in natural use and in the corpus. Crediting a shift to
   pronominality *over and above* givenness is exactly what a controlled, under-powered, minimal-pair
   behavioral probe cannot do for free — it is what the corpus's multiple regression does across 3263
   attested rows with natural length variation.

The provisional default had been a by-construction "length-matched pronoun vs. 1-word name" contrast
(Option A). The independent review **rejected it**: even at equal word count a pronoun is *prosodically
lighter* than a name (not dissociable by construction), and a re-mentioned name in a given context
incurs a **repeated-name penalty** that pushes in the *same direction* as the predicted pronominality
effect — so an Option-A "positive" could be the confound, not the factor. Adopting A as primary would
have made a confounded positive *easier* to obtain, not harder; the rigorous move is to decline the
primary behavioral test. (Option B — modelling length as a statistical covariate — was rejected as the
assumption-laden control the project consistently declines, on an item-N far too thin to support it.)

## What the human corpus says about the unreached factor

The closure is about the **instrument's reach**, not the factor's reality. On the human side the factor
is real and large. The firsthand `languageR::dative` logistic fit
([`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md);
`corpus_inspection.json`, in-sample accuracy 0.887, predicting P(PP), NP=DOC the 0 class) gives the
recipient-pronominality coefficient as **−1.48** — a pronominal recipient pushes strongly toward DOC,
and in magnitude this is the **largest of the information-structure predictors**: larger than the
given-recipient effect the reached probe tests (−0.93), and larger than pronominal-theme (+1.37) and
given-theme (+1.33). (Only the non-information-structure `AnimacyOfRec_inanimate` term, +1.62, is
larger.) The resource codes pronominality as its own factor — `PronomOfRec`, "a factor with levels
`nonpronominal` and `pronominal` coding the pronominality of the recipient" — orthogonal to
accessibility (`AccessOfRec`) and definiteness (`DefinOfRec`). So the human dative weights pronominality
most heavily among the discourse factors; the dative probe simply has no clean behavioral mirror for it.

The v1/v2 secondary corpus-gradient analysis currently holds the `PronomOfRec` dummy **fixed** at the
nonpronominal reference level (`analyze.py`: "Pronom reference = nonpronominal (dropped) → … constant
across cells"), because every v1/v2 recipient is a nonpronominal full NP. A future arm *could* add a
varying `PronomOfRec` term to the human production surface (it would genuinely bring the −1.48 coefficient
into the gradient rather than restate an existing correlation), but only on **fresh stimuli that include
pronominal recipients**, and only as a **non-decisive secondary** measure — never a primary within-model
claim, and never overwriting the as-published v1/v2 ρ values. That extension is not run here; it is named
as the only honest behavioral residue, and it is optional.

## Scope and limits (binding)

- **This is a reachability/closure claim, not a behavioral finding.** It says the controlled primary test
  is not buildable under pure autonomy; it makes **no** claim that any model does or does not track
  pronominality. The "model can't" box stays empty, exactly as the project's negative-results discipline
  requires.
- **Pure-autonomy scope.** The closure is relative to the available instrument (logprob-free graded
  forced-choice, synthetic minimal pairs). It is **not** a claim that pronominality is unreachable in
  principle — with prompt logprobs, or a different anchor, a cleaner isolation might exist. The closure is
  honest about *which* tool cannot reach it, analogous to the relational line's transcript-ceiling closure
  and the third-construction headroom closure.
- **The reached result is untouched.** The replicated givenness positive (v1/v2: claude + gemini robust
  across disjoint item sets, gpt fragile) stands exactly as published; this claim neither strengthens nor
  weakens it. It bounds the dative line's *extent*, marking pronominality as the documented edge of what
  the instrument reaches.
- **Anti-cheat.** The closure makes a confounded pronominality positive *impossible* (no probe, no
  behavioral measure to confound) rather than merely harder — the conservative direction. Surfacing and
  declining the test was chosen *over* a design that could have manufactured a positive; ratification fixed
  the yardstick, never a result.

## Provenance

- Governing decision: [`decisions/resolved/dative-pronominality-operationalization`](../../decisions/resolved/dative-pronominality-operationalization.md)
  (ADOPT OTHER — Option C; autonomous adversarial review, session 56).
- Human anchor: [`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md)
  (Bresnan et al. 2007; `languageR::dative`; the `PronomOfRec` factor and the −1.48 coefficient are in the
  firsthand fit, `experiments/runs/2026-06-20-dative-information-structure/corpus_inspection.json`).
- Reached results bounded by this closure:
  [`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md),
  [`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md).
- **Cost: $0** — no probe, no API call. A governance + closure session.
