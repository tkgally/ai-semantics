---
type: source
id: weissweiler-2023-cxg-insight
title: "Construction Grammar Provides Unique Insight into Neural Language Models"
authors:
  - Weissweiler, Leonie
  - He, Taiqi
  - Otani, Naoki
  - Mortensen, David R.
  - Levin, Lori
  - Schütze, Hinrich
year: 2023
venue: "GURT 2023 (Georgetown University Round Table on Languages and Linguistics)"
arxiv: "2302.02178"
url: https://arxiv.org/abs/2302.02178
access: open-access
meaning-senses:
  - constructional
  - distributional
created: 2026-05-28
updated: 2026-05-28
links:
  - rel: supports
    target: concept/constructional-meaning
---

# Weissweiler et al. 2023 — Construction Grammar Provides Unique Insight into Neural Language Models

## What it is

Position and survey paper published at GURT 2023 (Georgetown University Round Table), arXiv 2302.02178. The founding methodological statement of the CxG-probing line for neural language models — the research program this project's wedge most directly joins. Not an empirical study of specific constructions, but a theoretical and methodological argument for why Construction Grammar (CxG) is uniquely valuable as a lens on NLM behavior.

## Summary

Weissweiler et al. argue that CxG offers something qualitatively different from standard syntactic or semantic probing: constructions are **form–meaning pairings** at multiple levels of abstractness, and probing NLMs for construction knowledge tests whether models encode the *pairing*, not just the form or just semantic plausibility in isolation. The paper surveys existing probing methodologies, identifies gaps, and frames the research questions the CxG-probing line needs to answer.

Key moves:
1. **CxG as a two-sided test.** Probing for a construction is not probing for a syntactic pattern and separately probing for a semantic preference — it is probing for the form–meaning unity. This makes CxG probes a sharper test of "meaning" tracking than either pure distributional probing or pure acceptability tasks.
2. **Survey of methodologies.** The paper reviews probing methods: (a) probes designed for other purposes (masked prediction, surprisal, NLI) repurposed for constructions; (b) construction-specific probes with minimal-pair designs. It evaluates each against the core question: does a model's behavior reflect the constraint structure of the construction?
3. **Open challenges.** Key challenges identified: (a) confound between construction knowledge and memorization of surface collocations; (b) absence of human-normed data for many constructions (making it hard to ground claims about model behavior against human behavior); (c) difficulty distinguishing formal from functional competence on construction probes.
4. **Relation to this project.** The AANN conjecture, the `way`-construction, and the dative-alternation conjectures in this project are all instances of the program Weissweiler et al. describe. The paper provides the methodological framing that justifies using minimal-pair surprisal probes and grounding them against human acceptability data.

## Key quotes

From abstract and arXiv-accessible text (no page numbers from preprint):

The paper argues that CxG provides "unique insight" into NLMs because constructions are form–meaning pairings whose dual nature cannot be captured by either purely formal or purely semantic probes alone.

Key open challenge (paraphrase from accessible text): distinguishing whether a model tracks a construction's constraint structure vs. simply reproducing collocational patterns from training data.

## What it can ground

- The `constructional` tag on any conjecture or result page — Weissweiler et al. 2023 is the methodological home for that tag as applied to NLM probing.
- The design decision to use minimal pairs with human acceptability anchors: the paper explicitly frames this as the right methodology for CxG probing.
- The confound concern about memorization vs. genuine construction knowledge — any AANN result must address this, and this paper is the source for naming the confound.
- Cross-references with the Weissweiler et al. 2024 empirical papers (`constructions-are-so-difficult`) that follow up with concrete construction probe results.

## What it cannot ground

- Empirical claims about specific construction behavior — this paper makes no empirical claims about what models do with AANN or any other specific construction; it is a methodological argument.
- Human-anchored acceptability claims — no human data in this paper.

## Known limits

- Position/survey paper; explicitly frames itself as a call to action rather than a completed empirical program. Claims here should be cited as methodological framing, not as empirical findings.
- The CxG literature the paper surveys is selective (primarily Goldberg-tradition and related lines). Other CxG traditions (Radical CxG, Sign-Based CxG) are less represented.

## Note on the broader Weissweiler line

Additional empirical papers from the same group (relevant but not yet catalogued in this repo):
- **Weissweiler et al. 2022** (arXiv 2210.13181): "The Better Your Syntax, the Better Your Semantics? Probing Pretrained Language Models for the English Comparative Correlative." EMNLP 2022. Empirical probe of the Comparative Correlative construction.
- **Weissweiler et al. 2024** (arXiv 2403.17760): "Constructions Are So Difficult That Even Large Language Models Get Them Right for the Wrong Reasons." LREC-COLING 2024. Challenge dataset for NLI; finds GPT-4 and Llama 2 fail with strong bias.

These should be catalogued if/when they are directly cited by a finding page.

## Status in wanted.md

Was `wanted (try OA; ACL Anthology likely)`. Now `catalogued` as the primary Weissweiler line entry. Full PDF available at arXiv URL above; page-level quotes should be extracted when a finding page requires verbatim citation.
