---
type: conjecture
id: dative-alternation-information-structure
title: LLMs track the information-structure constraint on dative alternation
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
contingent-on: []
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: concept/constructional-meaning
# Note: a `resource` anchor (e.g. Bresnan et al. dative rating data) will be
# added when this conjecture is promoted to a design — see body for candidates.
---

# Conjecture: LLMs track the information-structure constraint on dative alternation

## Statement

The English dative alternation — *Mary gave John the book* (double object, DOC) vs. *Mary gave the book to John* (prepositional dative, PD) — is constrained by information structure (Bresnan & Nikitina 2009 and downstream work): given/discourse-old material tends to precede new material; pronominal recipients strongly prefer DOC. The conjecture: production-style preferences in current LLMs are sensitive to this information-structure constraint, not merely to surface-form frequency.

## Why this is interesting

The DOC/PD choice is one of the most-studied form-meaning pairings in English. The meaning side is partly **constructional** (the two constructions have weakly different semantics — DOC favors a "successful transfer / recipient affectedness" reading) and partly an **inferential** consequence of information structure (what is given vs. new). If LLMs respect the information-structure side without respecting the constructional-semantic side (or vice versa), that is a sharper diagnostic than the usual coarse "do LLMs know syntax" framing.

## Predictions

1. In a minimal-pair production-preference probe (continuation likelihood for DOC vs. PD given a controlled discourse context), LLMs prefer DOC when the recipient is given/pronominal and the theme is new, and prefer PD when the theme is given/pronominal and the recipient is new.
2. The effect is **graded**, not categorical: surprisal differences should track human acceptability ratings on parallel items rather than flipping at a hard threshold.
3. Effect size will vary cross-model in a way that decorrelates from surface accuracy — i.e., two models with similar overall benchmark performance can differ in how cleanly they track information structure here.

## What would confirm / falsify

- **Confirm:** monotonic relationship between human acceptability scores (anchor) and LLM surprisal contrast across at least 30 controlled minimal-pair items, in at least two of three panel models.
- **Weak:** the preference exists but does not track human gradient acceptability — the model has surface preference but not information-structure sensitivity.
- **Falsify:** preference flips with shallow lexical confounds (recipient/theme length, animacy of theme) but not with information-structure manipulation when length and animacy are controlled.

## Human anchor (pending)

Needs a sourced human-acceptability dataset for dative alternation by information-structure condition. Candidates:

- Bresnan et al. (2007) "Predicting the dative alternation" corpus study + the follow-up rating data.
- The MIT/Harvard psycholinguistic norming work that uses these stimuli.

→ Open decision queued: `decisions/open/dative-anchor-choice.md` (to be written when this conjecture is moved to design).

## Notes / caveats

- The construction is **English-specific** in this exact form. A cross-linguistic version is more ambitious; bracket it.
- Information structure is itself underdetermined without a discourse model; control discourse explicitly in the stimulus.
- Watch for the operationalization-tuning failure mode: do not refine the stimulus set after seeing the first batch of model outputs (charter §8).
