---
type: conjecture
id: function-word-substitutability
title: Function-word swaps produce sharper meaning shifts than matched content-word swaps in LLM behavior
meaning-senses:
  - constructional
  - distributional
  - inferential
status: proposed
contingent-on: []
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Conjecture: function-word swaps produce sharper meaning shifts than content-word swaps

## Statement

For matched-frequency minimal pairs, swapping a **function word** (e.g., *the* → *a*; *will* → *would*; *because* → *although*; *some* → *every*) produces a **larger downstream change in LLM behavior** (entailment, paraphrase preference, continuation distribution) than swapping a content word of comparable surface frequency. The intuition: function words encode constructional/grammatical meaning whose downstream consequences are systematic; content-word swaps shift topic but often leave inferential structure intact.

## Why this is interesting

- Function words are exactly where lexicography is historically thinnest and meaning-theory is most underdeveloped — yet they carry the constructional load.
- The frequency-controlled comparison is the cleanest possible probe of the `constructional` vs. `distributional` distinction: the distributional theory predicts comparable behavior shifts for comparable frequency; a substantially larger shift on function-word swaps is evidence for constructional meaning being computed beyond surface co-occurrence.
- It is the most *general* of the four founding conjectures — any LLM, any matched corpus, any inferential probe; the conjecture survives or fails across many specific stimulus sets.

## Predictions

1. KL divergence (or similar) on continuation distributions is larger after function-word swaps than after frequency-matched content-word swaps.
2. Entailment / inference behavior flips more often after function-word swaps.
3. The gap is robust across panel models and across content-word semantic classes — i.e., it is not driven by a few outlier categories.

## What would confirm / falsify

- **Confirm:** statistically robust gap (effect size meaningfully > 0) on a corpus of ≥200 matched minimal pairs, replicated in ≥2 of 3 panel models.
- **Weak:** gap present but small and inconsistent across models — function-word effects are real but not dominant over distributional.
- **Falsify:** flat or inverse pattern — content-word swaps move behavior at least as much as function-word swaps, after frequency control. Would be a strong (and surprising) finding for the distributional camp; write it.

## Human anchor (pending)

A frequency-controlled function-vs-content swap inventory does not, to current knowledge, exist as a single resource. The conjecture probably first needs:

- A frequency-matched word-pair list drawn from BNC / COCA / a UD treebank.
- An NLI / acceptability backing (BLiMP / SyntaxGym have partial coverage of function-word minimal pairs).

→ Queue `decisions/open/function-word-anchor-design.md` at design time. This is the **operationalization gate** for this conjecture — what counts as a "frequency-matched" pair is the place a loop can quietly cheat by selecting items that bias the result.

## Notes / caveats

- This is the most *abstract* of the founding conjectures and so the most vulnerable to operationalization tuning. Lock the matched-pair set **before** seeing model outputs.
- A null here is a positive result for the distributional position, not a failure — write it as such.
