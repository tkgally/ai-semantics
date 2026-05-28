---
type: conjecture
id: aann-construction
title: LLMs treat the AANN ("a beautiful three days") construction as a unit, not a syntactic accident
meaning-senses:
  - constructional
  - functional-vs-formal
status: designed
contingent-on:
  - aann-stimulus-source
  - aann-operationalization
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: refines
    target: open-question/relational-meaning-pilot
  - rel: operationalizes
    target: design/aann-construction-v1
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
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

- **Confirm:** AANN-licit vs. illicit surprisal contrast on held-out lexical items tracks the human-rated acceptability gradient in `resource/mahowald-2023-aann-stimuli`, in ≥2 of 3 panel models. Concrete threshold per `decisions/open/aann-operationalization.md` (provisional default T1).
- **Weak:** contrast exists for items that appeared in training (memorization) but does not generalize to held-out adjectives.
- **Falsify:** flat or inverse contrast pattern; or contrast that tracks unigram frequency of adjective alone, not the construction.

## Human anchor

Catalogued as `resource/mahowald-2023-aann-stimuli` (status: `external-only` until a future run mirrors the released repo). Mahowald 2023 (EACL) — templatic AANN stimulus generator plus MTurk acceptability ratings — supersedes the earlier "Weissweiler line" pointer in the bootstrap version of this conjecture; the Weissweiler CxG-probing papers remain a candidate secondary anchor and are tracked in `decisions/open/aann-stimulus-source.md`.

→ Open decisions queued:

- `decisions/open/aann-stimulus-source.md` — confirm Mahowald-as-primary anchor vs. adding Weissweiler as secondary.
- `decisions/open/aann-operationalization.md` — what counts as "tracks the construction" (indicator + threshold + held-out items).

## Status note

This conjecture is `designed` as of 2026-05-28: `experiments/designs/aann-construction-v1.md` operationalizes it. It is **not** `tested` and may not be promoted to a claim until both `contingent-on` decisions are ratified by Tom and the probe is run.

## Notes / caveats

- Memorization is the main confound; the held-out lexical-item check is the main defense.
- The Weissweiler line has done a version of this; the project's contribution is the **meaning-sense tagging** and the **cross-model decorrelation** angle, not novel probing of AANN per se.
