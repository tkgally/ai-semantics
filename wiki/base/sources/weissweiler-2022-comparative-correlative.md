---
type: source
id: weissweiler-2022-comparative-correlative
title: "The better your Syntax, the better your Semantics? Probing Pretrained Language Models for the English Comparative Correlative"
authors:
  - Weissweiler, Leonie
  - Hofmann, Valentin
  - Köksal, Abdullatif
  - Schütze, Hinrich
year: 2022
venue: "Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing (EMNLP 2022), pp. 10859–10882, Abu Dhabi"
arxiv: "2210.13181"
url: https://aclanthology.org/2022.emnlp-main.746/
access: open-access
meaning-senses:
  - constructional
  - functional-vs-formal
  - distributional
status: received
created: 2026-05-29
updated: 2026-05-29
pdf-pages: "ACL Anthology 2022.emnlp-main.746 (PDF, pp. 10859–10882); body section quotes read from ar5iv HTML (ar5iv.labs.arxiv.org/html/2210.13181), cited by section heading/number"
links:
  - rel: supports
    target: concept/constructional-meaning
  - rel: supports
    target: source/weissweiler-2023-cxg-insight
---

# Weissweiler et al. 2022 — The better your Syntax, the better your Semantics? Probing PLMs for the English Comparative Correlative

## What it is

Empirical CxG-probing paper published at EMNLP 2022 (pp. 10859–10882), arXiv 2210.13181. Lead author Leonie Weissweiler (same lead author as [`source/weissweiler-2023-cxg-insight`](weissweiler-2023-cxg-insight.md)), with Valentin Hofmann, Abdullatif Köksal, and Hinrich Schütze. This is the **single-construction empirical precedent** that the 2023 GURT position paper later generalizes into a methodological program: where the 2023 paper argues *why* CxG probing is the right lens, this 2022 paper actually runs the probe on one construction — the English comparative correlative (CC) — and finds a syntax-vs-semantics dissociation.

## Summary

The paper tests whether state-of-the-art pretrained language models (PLMs) — BERT, RoBERTa, and DeBERTa (multiple sizes) — encode the English comparative correlative (CC), e.g. "the more you practice, the better you get". The CC is chosen because it is a heavily studied CxG construction whose form (a two-clause `the X-er ... the Y-er` template) is distinctive while its meaning (a conditional/proportional dependency between two scales) is non-compositional and must be supplied by the construction itself.

The design splits the question into two:
1. **Syntactic probe.** Logistic-regression probing classifiers are trained on PLM embeddings to distinguish CC sentences from non-CC controls, using both artificial (CFG-generated) and corpus-based minimal-pair-style data, layer by layer.
2. **Semantic application task.** A zero-shot task (masked / cloze-style token prediction with calibration to mitigate bias) tests whether the models can actually *use* the proportional meaning the CC encodes to draw the right inference.

Headline result: the PLMs **recognise the structure** of the CC well (the syntactic probe separates positive from negative examples in at least some layers) but **fail to use its meaning** (no model performs above chance on the semantic task). This is a clean dissociation between formal pattern-recognition and functional deployment of constructional meaning, on a single well-chosen construction.

Relation to this project: this is an early, single-construction instance of the program later named by [`source/weissweiler-2023-cxg-insight`](weissweiler-2023-cxg-insight.md). The syntax-recognised-but-meaning-not-used dissociation is a direct precedent for the project's formal-vs-functional wedge and for the Scivetti et al. 2025 generalization gap — and the comparative correlative is itself **one of the 8 constructions** in the later Scivetti benchmark (see [`source/scivetti-2025-beyond-memorization`](scivetti-2025-beyond-memorization.md) and [`resource/scivetti-2025-cxnli-dataset`](../resources/scivetti-2025-cxnli-dataset.md)), making this 2022 study the earliest single-construction probe of the same target the 2025 multi-construction benchmark later re-tests with newer models.

## Key passages

Abstract quoted verbatim from the ACL Anthology page (https://aclanthology.org/2022.emnlp-main.746/) and cross-checked against the arXiv abs page (https://arxiv.org/abs/2210.13181); both fetched 2026-05-29 and identical. Body section quotes read verbatim from the ar5iv HTML rendering (https://ar5iv.labs.arxiv.org/html/2210.13181, fetched 2026-05-29; re-verified character-for-character 2026-05-31); no pagination in HTML, so sections are cited by heading/number as printed. On re-verification all three body quotes matched exactly and were located at: quote 1 — §1 Introduction (second paragraph); quote 2 — §1 Introduction (final paragraph); quote 3 — §6 Conclusion (first sentence). (An earlier status note had mislabelled quote 2 as "§4.2"; the correct locator is §1 Introduction.)

**Abstract (verbatim, ACL Anthology / arXiv abs) — design and the central finding (the title's question):**

> "Construction Grammar (CxG) is a paradigm from cognitive linguistics emphasising the connection between syntax and semantics. Rather than rules that operate on lexical items, it posits constructions as the central building blocks of language, i.e., linguistic units of different granularity that combine syntax and semantics. As a first step towards assessing the compatibility of CxG with the syntactic and semantic knowledge demonstrated by state-of-the-art pretrained language models (PLMs), we present an investigation of their capability to classify and understand one of the most commonly studied constructions, the English comparative correlative (CC). We conduct experiments examining the classification accuracy of a syntactic probe on the one hand and the models' behaviour in a semantic application task on the other, with BERT, RoBERTa, and DeBERTa as the example PLMs. Our results show that all three investigated PLMs are able to recognise the structure of the CC but fail to use its meaning. While human-like performance of PLMs on many NLP tasks has been alleged, this indicates that PLMs still suffer from substantial shortcomings in central domains of linguistic knowledge."

**§1 Introduction (verbatim, ar5iv HTML) — the CC as a CxG test case:**

> "the CC is one of the most commonly studied constructions in construction grammar (CxG), a usage-based syntax paradigm from cognitive linguistics"

**§1 Introduction (verbatim, ar5iv HTML) — the semantic-side failure, previewed in the intro:**

> "none of the PLMs we investigate perform above chance level, indicating that they are not able to understand and apply the CC in a measurable way in this context."

**§6 Conclusion (verbatim, ar5iv HTML) — the dissociation as takeaway:**

> "they do not seem to be able to extract the meaning it conveys and use it in context"

## What it can ground

- The `constructional` tag for the **comparative correlative specifically** — this is the in-repo empirical source for what PLMs do (and do not do) with the CC, the same construction later folded into the Scivetti et al. 2025 8-construction benchmark.
- A precedent for the **syntax-vs-semantics dissociation** in CxG probing: a model recognising a construction's form does not entail it can deploy the construction's meaning. Directly relevant to this project's `functional-vs-formal` wedge and to the memorization/generalization gap the Scivetti benchmark probes.
- A **methodology line**: layer-wise probing classifiers (logistic regression on embeddings) for the form side, plus a separate zero-shot semantic application task for the meaning side, with artificial CFG-generated and corpus-based data and calibration for bias. A precedent for separating "encodes the pattern" from "uses the meaning" in a probe design.

## What it cannot ground

- Claims about **constructions other than the comparative correlative** — the empirical scope is the single CC construction; do not cite it for AANN, the `way`-construction, dative alternation, or any other construction's behavior.
- Claims about **newer generative LLMs** — the models tested are encoder PLMs (BERT, RoBERTa, DeBERTa), not GPT-class or instruction-tuned models; the syntax/semantics dissociation is established only for these encoders. (The Scivetti 2025 benchmark is where GPT-4o / GPT-o1 / Llama re-test the CC and related constructions.)
- **Mechanistic / representational-theory** claims beyond probe accuracy — the syntactic side is a behavioral probing-classifier result on embeddings (probe accuracy can reflect probe expressivity, not just model knowledge) and the semantic side is a behavioral task; neither is a causal/mechanistic representation claim.
- **Human-anchored** acceptability or inference norms — the paper compares to chance and to a structural baseline, not to a human-normed dataset of CC inference judgements.

## Known limits

- Behavioral / probing-classifier evidence, not representational: probe accuracy on the syntactic side is subject to the usual probing-confound caveats; the semantic side is a zero-shot task with calibration, so absolute scores depend on the task framing.
- Encoder-PLM era (2022): the specific models are BERT/RoBERTa/DeBERTa; the dissociation may or may not transfer to later decoder LLMs — which is precisely why the later multi-construction benchmark re-runs the question.
- Single construction: a clean finding on the CC, but generalization to "constructions in general" is exactly the step the 2023 position paper argues for rather than something this study establishes.
- Body section quotes were read from the ar5iv HTML rendering, not the camera-ready ACL PDF; page-level provenance for body passages is pending PDF ingestion (the abstract is verified against both ACL Anthology and arXiv abs).

## Status in wanted.md

Noted on [`source/weissweiler-2023-cxg-insight`](weissweiler-2023-cxg-insight.md) ("Note on the broader Weissweiler line") as a paper to catalogue if/when cited by a finding. Now `received`: title, authors, venue (EMNLP 2022, pp. 10859–10882), and arXiv id (2210.13181) verified against the ACL Anthology page and arXiv; full abstract verbatim from ACL Anthology (identical to arXiv abs); three section-level body quotes verbatim from ar5iv HTML (§1 ×2, §6), fetched 2026-05-29 and re-verified character-for-character 2026-05-31. Full ACL PDF (pp. 10859–10882) available for page-level provenance and exact per-layer/per-model numbers if a finding needs them.
