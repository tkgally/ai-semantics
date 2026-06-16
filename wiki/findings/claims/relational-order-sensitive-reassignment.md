---
type: claim
id: relational-order-sensitive-reassignment
title: LLM referential conventions are order-sensitive (non-commutative) when the history carries disambiguating recency information — both models recover a reassigned term by its most-recent binding
meaning-senses:
  - relational
  - model-internal
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-16
updated: 2026-06-16
links:
  - rel: depends-on
    target: result/relational-spontaneous-recency-a
  - rel: contradicts
    target: conjecture/commutative-convention
  - rel: refines
    target: concept/relational-meaning
  - rel: depends-on
    target: result/relational-stamp-comprehension-b
---

# Claim: LLM referential conventions are order-sensitive (non-commutative) when the history disambiguates by recency

> **Status: supported (2026-06-16).** Promoted from the clean positive in
> [`result/relational-spontaneous-recency-a`](../results/relational-spontaneous-recency-a.md)
> (Option A of the ratified relational-v5 staged design; independent pre-run critic GO,
> independent post-run verifier REPRODUCED). It is the positive the conjecture's own falsification
> clause said to promote when a clean order effect appears. `anchor: internal-contrast-only` —
> a within-model behavioural contrast over byte-identical content; **no human-comparison claim.**

## The claim (scoped exactly)

When a coined referential term is **reassigned** to different referents across an explicitly
stamped interaction history — so that the *content-set* of the history is symmetric (every
candidate referent has been "called" by the term) and **only the recency ordering disambiguates**
— both panel models (`claude-sonnet-4.6`, `gemini-3.5-flash`) recover the term by its
**most-recent binding**, *spontaneously* (the query asks only which referent the term picks out,
never mentioning recency). The recovered convention is therefore a function of the **order**, not
of the content-set: it is **order-sensitive / non-commutative** in this regime.

The supporting effect is a ceiling, identical across both separately-trained models: SPONT
latest-binding rate **1.000** (Wilson-95 [0.926, 1.000]), first-binding rate 0.000,
physical-position-following at exactly chance (0.250), with a DIRECT on-demand manipulation check
at **1.000** in both directions and 0 NA. The design is shortcut-proof by construction (every
position/lexical/frequency strategy scores exactly 1/K, proven at build and on idealized-reader
fixtures and re-derived by an independent critic), so the above-chance rate can only come from
spontaneously weighting the round stamp.

## What it refines and what it contradicts

- **Contradicts [`conjecture/commutative-convention`](../conjectures/commutative-convention.md).**
  The conjecture bet that LLM referential conventions are *commutative* (order-invariant,
  set-based). This claim shows they are **not**, in the regime where order carries disambiguating
  information. The conjecture is **retired**; its v1/v4 nulls are preserved as bounded observations
  for framings where order carried no disambiguating signal (v1) or was confounded with physical
  position (v4). Commutativity is thus **operationalization-dependent**, not a property of LLM
  convention-recovery as such.
- **Refines [`concept/relational-meaning`](../../base/concepts/relational-meaning.md).** It places
  the models on the *order-sensitive* side of the aggregation/constitution distinction in this
  setting — but at its **bottom rung**: order-sensitivity here is consistent with a thin
  **latest-binding-wins / convention-update** rule and does **not** establish a convention
  *constituted between* agents through the live trajectory. The claim is order-sensitivity, not
  constitution.

## Binding scope limits (do not over-cite)

1. **Internal-contrast-only.** A within-model contrast; it makes **no** claim about humans. The
   conjecture's predicted human/LLM contrast is *not* settled by this result — human
   order-sensitivity at this grain remains unanchored in-repo.
2. **One operationalization.** Reassignment-of-a-term is one way to make order disambiguating;
   generality (image referents, cross-family dyads, non-overwrite repairs) is untested.
3. **Thin, not rich.** "Latest-binding-wins" may be a shallow update heuristic; this claim does not
   separate thin order-sensitivity from deep path-dependence.
4. **Spontaneous = query-not-directed, not cue-free.** The framing flags that the term was
   reassigned (a choice among bindings is required); the models resolve that choice by **recency**
   without the query asking them to — which is the content of "spontaneous" here.

## Revision triggers

- A framing in which order disambiguates but the models **do not** track it (a commutative result
  in an order-disambiguating setting) would **bound** this claim to the reassignment frame.
- Evidence that the latest-binding-wins behaviour is a **surface artifact** of the explicit
  "was reassigned" wording (e.g. it vanishes when reassignment is implicit) would narrow it.
- A human order-perturbation anchor becoming available would let the within-model claim be tested
  against the predicted human contrast (a new, currently-undischargeable anchor question).
