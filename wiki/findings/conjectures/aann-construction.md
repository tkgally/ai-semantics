---
type: conjecture
id: aann-construction
title: LLMs treat the AANN ("a beautiful three days") construction as a unit, not a syntactic accident
meaning-senses:
  - constructional
  - functional-vs-formal
status: proposed
contingent-on: []
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: refines
    target: open-question/relational-meaning-pilot
---

# Conjecture: LLMs treat the AANN construction as a productive unit

## Statement

The **AANN construction** — *a* + Adjective + Numeral + Plural-Noun, as in *a beautiful three days*, *a remarkable five miles*, *a long six months* — is a marked English construction where the indefinite article scopes over a plural NP, and it carries a characteristic meaning: the measured quantity is presented as a coherent, unified, often evaluated stretch. This is the canonical CxG-probing target in the Weissweiler / Tayyar Madabushi line.

The conjecture: current LLMs treat AANN as a **productive construction** in Goldberg's sense — they generalize it to held-out lexical material in a way that tracks the construction's characteristic semantics (unification + evaluation), not merely the surface pattern.

## Why this is interesting

- AANN is the cleanest existing CxG-probing target, and the recent literature gives a ready-made human-anchor inventory of licit and illicit AANN instantiations.
- It splits cleanly along `functional-vs-formal`: the *form* (a + Adj + Num + N.PL) is learnable from a small number of training examples; the *function* (unification + evaluation) is what would make this `constructional` meaning rather than memorized template.
- It is the right size for a first-pass loop turn: one construction, one probe family, multiple panel models.

## Predictions

1. LLMs assign higher continuation likelihood to AANN with **evaluatively-loaded** adjectives (*beautiful*, *gruelling*, *remarkable*) than with **neutral measure-modifying** adjectives (*approximate*, *roughly*), even controlling for unigram frequency — because the construction's meaning is partly evaluative.
2. LLMs distinguish licit AANN from minimally-different illicit variants (*a three beautiful days*; *the beautiful three days*) at a level consistent with construction-specific learning rather than n-gram coverage.
3. Panel divergence: models with more code/structured-text in training will show *less* AANN sensitivity (it's a marked colloquial construction); this is itself informative about whether constructional meaning is uniformly recoverable from text.

## What would confirm / falsify

- **Confirm:** AANN-licit vs. illicit surprisal contrast on held-out lexical items tracks the human-rated licit/illicit distinction from the Weissweiler line, in ≥2 of 3 panel models.
- **Weak:** contrast exists for items that appeared in training (memorization) but does not generalize to held-out adjectives.
- **Falsify:** flat or inverse contrast pattern; or contrast that tracks unigram frequency of adjective alone, not the construction.

## Human anchor (pending)

The Weissweiler et al. AANN stimulus sets are the natural anchor; the recent papers include rated item lists. Catalogue the specific stimulus list as a `resource` page when this conjecture is moved to design.

→ Open decision queued: `decisions/open/aann-stimulus-source.md` (to be written at design time).

## Notes / caveats

- Memorization is the main confound; the held-out lexical-item check is the main defense.
- The Weissweiler line has done a version of this; the project's contribution is the **meaning-sense tagging** and the **cross-model decorrelation** angle, not novel probing of AANN per se.
