---
type: conjecture
id: genitive-alternation-animacy
title: LLMs track the possessor-animacy constraint on the English genitive alternation
meaning-senses:
  - constructional
  - inferential
  - distributional
status: tested
contingent-on: []
created: 2026-07-13
updated: 2026-07-13
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: resource/genitive-animacy-human-anchor
  - rel: depends-on
    target: source/dubois-2023-genitive-animacy
---

> **Proposed 2026-07-13 (session 217); ratified + tested 2026-07-13 (session 218).** The second
> sibling of the program A5 production-side alternation battery — extending the dative pattern
> ([`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md),
> a human-direction-anchored production-preference positive) to the **genitive alternation**, with a
> **human-comparison anchor** ([`resource/genitive-animacy-human-anchor`](../../base/resources/genitive-animacy-human-anchor.md);
> Dubois et al. 2023, 25 native-speaker acceptability ratings, CC BY 4.0). The operationalization gates
> ([`decisions/resolved/genitive-alternation-anchor-and-indicator`](../../decisions/resolved/genitive-alternation-anchor-and-indicator.md):
> Q1 possessor animacy / Q2 graded forced-choice + nonce-arm & covariate shadow controls / Q3
> human-anchored on the direction) were **ratified s218** (adversarial review + non-Anthropic vote,
> convergent) and the probe **frozen + run s218** →
> [`result/genitive-alternation-animacy-v1`](../results/genitive-alternation-animacy-v1.md). See that
> result for the verdict.
>
> **→ REPLICATED s220, PROMOTED s221.** The line replicated on fresh disjoint items
> ([`result/genitive-alternation-animacy-rep2`](../results/genitive-alternation-animacy-rep2.md), CONFIRM
> 3/3 again) and the cross-session promotion review then promoted it **direction-only** →
> [`claim/genitive-alternation-animacy`](../claims/genitive-alternation-animacy.md) (`status: supported`).
> The conjecture's confirm branch (human-direction shift + surviving the shadow control) is realized;
> predictions 2 (smooth graded ramp) and the magnitude remain fenced (animate/non-animate binary; magnitude
> deferred to an owed powered re-run). `status: tested` stands.

# Conjecture: LLMs track the possessor-animacy constraint on the genitive alternation

## Statement

The English genitive alternation — the **s-genitive** (*the judge's decision*, possessor first) vs the
**of-genitive** (*the decision of the court*, possessum first) — is constrained by **possessor
animacy**: animate possessors favour the s-genitive, inanimate possessors favour the of-genitive
(Dubois et al. 2023; "animacy is normally the strongest constraint of the genitive alternation",
Rosenbach 2014). The conjecture: production-style genitive preferences in current panel LLMs are
sensitive to this animacy constraint **in the human-rated direction**, and the sensitivity is not
merely a shadow of the higher surface frequency of animate-possessor s-genitive strings.

## Why this is interesting

The genitive alternation is, with the dative, one of the two canonical probabilistic-grammar
alternations of the Bresnan school, but it turns on a **different** primary constraint (possessor
animacy, a semantic/referential property) rather than information structure (givenness). A second
human-anchored alternation row lets the shadow-depth table
([`theory/shadow-depth-table-v2`](../theory/shadow-depth-table-v2.md)) carry a *production-side*
measured residual against a *named human direction* for a construction whose driving factor is
semantic rather than discourse-structural — testing whether "the panel tracks the soft constraint in
the human direction" generalizes across the two flagship alternations or is specific to information
structure. The sharpest form of the question: **does the animacy effect survive a surface-frequency
control**, or is animate→s-genitive just the model reading off which genitive string it has seen more
often? That is the distributional-shadow question in production-preference clothing.

## Predictions

1. In a graded forced-choice production-preference probe (distribute 100 points by naturalness between
   the s-genitive and of-genitive phrasings of the *same* possessive proposition, possessum held
   fixed), the panel prefers the **s-genitive more when the possessor is animate** than when it is
   inanimate — the human-rated direction — with possessor/possessum length and final sibilancy held
   constant.
2. The effect is **graded**, not categorical: preference strength tracks the animacy level (animate >
   collective > inanimate, the source's scale) rather than flipping at a hard boundary.
3. The animacy shift **survives the surface-frequency shadow control**: it holds on an **atypical arm of
   rare/nonce possessor lemmas** (where the model has no per-lemma genitive statistic and must read
   animacy off the possessor *category*) and its animacy coefficient survives partialling out the frozen
   **possessor-lemma marginal genitive-propensity** covariate. If the shift is fully explained by the
   possessor's marginal s-genitive propensity, that is the shadow reading, not a constructional one.
   *(The naive "novel possessor–possessum pairings on common possessors" control is insufficient — it
   leaves the marginal-propensity channel intact; s217 pre-run critic B1.)*
4. Effect size decorrelates across models in a way that need not track overall benchmark performance
   (the dative and CC pattern: a concordant panel direction can hide an order-of-magnitude spread).

## What would confirm / falsify

*(These are provisional pending ratification of the open decision, which fixes the indicator, the
shadow control, and the anchor posture. Symmetric — a null is first-class.)*

- **Confirm (human-direction, primary):** the panel's s-genitive preference **shifts in the human
  direction** across the animacy manipulation (animate → more s-genitive), possessor length +
  sibilancy held constant, with the shift's bootstrap lower bound clear of zero in ≥2/3 models, **AND**
  the pre-registered independence rule holds (animacy CI still excludes zero with the marginal
  possessor-propensity covariate included, and the rare/nonce-possessor atypical-arm shift clears zero,
  each ≥2/3). → a human-anchored production-side animacy positive.
- **Shadow / attenuated:** a positive animacy shift exists but its animacy coefficient collapses once the
  marginal possessor-propensity covariate is included, or it does not clear zero on the rare/nonce-
  possessor atypical arm → the effect is a distributional shadow of the possessor's genitive propensity,
  not animacy tracking; recorded as such.
- **Weak:** the shift exists but does not track the graded animacy scale (prediction 2 fails).
- **Falsify:** no animate→s-genitive shift under the controlled manipulation, or the shift reverses.

## Human anchor

[`resource/genitive-animacy-human-anchor`](../../base/resources/genitive-animacy-human-anchor.md) —
the native-speaker acceptability direction (animate → s-genitive) from Dubois et al. (2023), a genuine
human-comparison leg. A **per-item** human gradient (per-item ratings or the TLC corpus production
surface) would be a stronger secondary anchor but is **not yet license-verified** (TLC is a controlled
corpus); adopting one is a queued scout, not a precondition — the direction anchor is the adopted
primary, mirroring the dative line's corpus-vs-ratings resolution.

## Notes / caveats

- The construction is **English-specific** in this exact form; bracket cross-linguistic ambition.
- Final **sibilancy** of the possessor is an independent phonological constraint on the s-genitive
  (*the boss's / the church's* is dispreferred) — it must be matched across animacy conditions or it
  confounds the shift.
- Watch the operationalization-tuning failure mode (charter §8): the item set and the shadow control
  are frozen before any spend and not retuned after seeing model outputs.
