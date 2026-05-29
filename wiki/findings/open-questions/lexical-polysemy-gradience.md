---
type: open-question
id: lexical-polysemy-gradience
title: Does LLM lexical-sense behavior exhibit the graded polysemy lexicographers document, or collapse to discrete senses?
meaning-senses:
  - distributional
  - referential
  - human-comparison
status: open
created: 2026-05-29
updated: 2026-05-29
links:
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
---

# Open question: graded polysemy vs. discrete sense in LLMs

## The question

Every finding in this project so far is **grammatical / constructional**. The charter scopes the project to "lexical *and* grammatical meaning" ([`PROJECT.md`](../../../PROJECT.md) §1) and names a standing asset the field underuses: "a lexicographer's tolerance for fine-grained polysemy and sense-distinction … The debate tends to be coarse; the gradiness is the point." The lexical axis is currently empty. This question opens it on exactly that asset.

Lexicographers treat word sense as **graded**: the senses of a polysemous word (*paper* = material / newspaper / academic article; *run* across dozens of related uses) shade into one another, with bridging contexts where two senses are co-present and judgments are genuinely intermediate — unlike homonymy (*bank* = riverside / financial), where senses are discrete and unrelated. The question: **does an LLM's in-context sense behavior reproduce this gradience, or does it collapse polysemy toward discreteness (treating related senses as either identical or as sharply separate as homonyms)?** And does the model's implicit sense inventory align with, over-split, or under-split a human sense inventory?

This is a `distributional`-vs-`referential.sense` question: distributional structure gives sense-in-context for free (different contexts → different neighborhoods), but whether that structure carries the *graded* sense relations a lexicographer documents — Frege's `Sinn` at fine grain — is exactly the contested boundary ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md), [`concept/referential-meaning`](../../base/concepts/referential-meaning.md)).

## Why it matters

- It is the project's first **lexical** wedge, complementing the constructional wedge, and the one place the lexicographer asset the charter highlights is directly in play.
- It is tractable with existing human-annotated resources (below), so it does not require new human-subject data (charter §8).
- The gradience framing is a genuine contribution angle: most LLM word-sense work uses *discrete* sense inventories (WordNet synsets) and asks for classification accuracy; the lexicographically interesting question — whether the model tracks **graded** relatedness and bridging contexts — is comparatively under-probed.

## What a serious answer would look like

A design that distinguishes three hypotheses:
1. **Graded-sense tracking** — the model's same-sense / different-sense behavior is *monotonic in human-rated sense relatedness*: intermediate for bridging/polysemous contexts, high for same-sense, low for homonyms. (The lexicographer's picture.)
2. **Discrete-sense collapse** — behavior is near-binary, with polysemous-but-related uses treated as sharply same or different, no intermediate regime distinguishing polysemy from homonymy.
3. **Distributional shadow** — apparent sense-tracking reduces to context-similarity (the two contexts' overall lexical overlap), not to sense relatedness per se — the lexical analogue of the constructional `distributional` null that runs through this repo.

Discriminating moves: hold context-similarity roughly constant while varying sense relatedness (polysemy vs. homonymy vs. same-sense) so hypothesis 3 is separable from 1; include **bridging contexts** (engineered to be sense-ambiguous) and test for an intermediate regime; compare the model's induced sense splits against a human sense inventory for over-/under-splitting.

## Human anchors (candidates; none in-repo yet)

Public, human-annotated lexical-sense resources that could ground this — several are already on the resources shortlist ([`base/resources/index.md`](../../base/resources/index.md)):

- **WiC — Word-in-Context** (Pilehvar & Camacho-Collados 2019): human binary same-sense/different-sense judgments for a target word across two contexts. The cleanest candidate for the same/different-sense behavioral contrast; public.
- **Graded word-sense / usage-similarity data** (e.g. Erk, McCarthy & Gaylord usage-similarity (Usim) ratings; SemEval graded-sense / lexical-substitution sets): human *graded* relatedness judgments — the resource type that bears directly on hypothesis 1 (gradience), which a binary set like WiC cannot fully ground.
- **WordNet** (sense inventory) and **SemCor / OntoNotes** (sense-tagged corpora): for the over-/under-splitting comparison against a human sense inventory. On the resources shortlist.

A future run that picks this up would catalogue the chosen resource as a `resource` page (checking it actually bears on the *gradience* question, not just sense existence — the charter's verify-content-not-existence rule), and queue an anchor decision then. **This page does not open that decision** — it is an open question, not yet a design.

## Relation to the existing wedge

- It is the **lexical counterpart** of the constructional `distributional`-vs-`constructional` tension ([`open-question/constructional-vs-frequency-confound`](constructional-vs-frequency-confound.md)): there the null is n-gram frequency; here it is context-similarity. Both ask whether a `distributional` shadow explains apparent meaning-tracking.
- It does **not** touch the relational axis ([`open-question/relational-meaning-pilot`](relational-meaning-pilot.md)); it is `model-internal` plus `human-comparison`.
- If pursued, it would likely spawn the project's first lexical `conjecture` (e.g., "LLM same/different-sense behavior is monotonic in human-rated sense relatedness, with an intermediate regime for polysemy absent for homonymy").

## Why this is queued, not active

It needs the word-sense-disambiguation / usage-similarity literature read first (WiC, Usim, the graded-sense line, the CoarseWSD / WSD-as-classification critiques) to confirm the gradience probe is not already a solved or trivial measurement, and to pick the anchor whose annotations are *graded* rather than discrete. Framing the question — fixing the three hypotheses and the context-similarity control — is the deliverable here; resolving it is a later loop turn gated on the reading and a fetched, gradience-bearing anchor.

## Pointers for the next visit

- Confirm which candidate anchor carries **graded** (not binary) human sense-relatedness judgments — that is the load-bearing property for hypothesis 1; WiC alone (binary) underdetermines it.
- Decide the locus: behavioral (prompted same/different-sense + confidence) on the panel, or the small-model lane (representation-similarity / probe) for a graded signal — note the instrument is an operationalization gate to queue before running.
- This is the seed for broadening beyond the grammatical wedge; keep it from sprawling — one tractable polysemy-gradience probe, anchored, before any wider lexical-semantics program.
