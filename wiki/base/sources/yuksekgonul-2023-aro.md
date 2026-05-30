---
type: source
id: yuksekgonul-2023-aro
title: "When and Why Vision-Language Models Behave like Bags-of-Words, and What to Do About It?"
authors:
  - Yuksekgonul, Mert
  - Bianchi, Federico
  - Kalluri, Pratyusha
  - Jurafsky, Dan
  - Zou, James
year: 2023
venue: "Proceedings of the Eleventh International Conference on Learning Representations (ICLR 2023) — Oral (notable top-5%)"
arxiv: "2210.01936"
url: https://arxiv.org/abs/2210.01936
access: open-access
meaning-senses:
  - grounded.perceptual
  - constructional
  - distributional
status: received
created: 2026-05-30
updated: 2026-05-30
pdf-pages: "arXiv 2210.01936v3 abstract page (verbatim abstract fetched 2026-05-30); ICLR 2023 virtual poster page (key finding paraphrases confirmed 2026-05-30). Body section quotes not yet extracted from full PDF."
links:
  - rel: supports
    target: concept/multimodal-compositionality
  - rel: refines
    target: source/thrush-2022-winoground

---

# Yuksekgonul et al. 2023 — When and Why Vision-Language Models Behave like Bags-of-Words

## What it is

Empirical benchmark + analysis paper, published at ICLR 2023 as an **Oral** (notable top-5%); arXiv 2210.01936. Lead author Mert Yuksekgonul (Stanford); co-authors Federico Bianchi, Pratyusha Kalluri, Dan Jurafsky, James Zou — Stanford affiliation. Repository: [https://github.com/mertyg/vision-language-models-are-bows](https://github.com/mertyg/vision-language-models-are-bows).

This paper names and diagnoses the **bags-of-words failure mode** in VLMs, introducing the ARO (**A**ttribution, **R**elation, **O**rder) benchmark to decompose compositionality into three sub-dimensions, and proposes a training-time fix (composition-aware hard negative mining). It is the direct mechanistic complement to Winoground: where Winoground showed the behavioral failure (near chance), ARO explains *why* it happens (contrastive pretraining creates retrieval shortcuts that do not require compositionality) and *where* it happens (attribution, relation, and order sensitivity are each separately deficient).

## Summary

The paper makes three interlocking contributions:

1. **Diagnosis.** State-of-the-art VLMs (CLIP and successors) fail on compositional tasks because contrastive pretraining on large datasets can be solved via lexical shortcuts — there is no training signal that forces the model to encode order or structural relations. The models behave like bag-of-words encoders: they recognize which words appear but not how they are combined.

2. **Benchmark (ARO).** A systematic decomposition of compositionality into three sub-dimensions:
   - *Visual Genome Attribution* — tests whether models correctly link objects to their attributes (e.g., distinguishing *"a red car"* from *"a blue car"* in a matching task).
   - *Visual Genome Relation* — tests relational understanding (e.g., *"a dog chasing a cat"* vs. *"a cat chasing a dog"*).
   - *COCO-Order & Flickr30k-Order* — tests sensitivity to word order by contrasting a caption with a word-order-shuffled foil.
   ARO contains more than 50,000 test cases, making it substantially larger than Winoground (400 items).

3. **Fix.** Composition-aware hard negative mining during contrastive learning — a training-time modification that significantly improves compositionality scores without other changes to architecture.

## Key passages

Abstract quoted verbatim from **arXiv 2210.01936v3 abstract page** (https://arxiv.org/abs/2210.01936v3, fetched 2026-05-30).

**Abstract (verbatim):**

> "Despite the success of large vision and language models (VLMs) in many downstream applications, it is unclear how well they encode compositional information. Here, we create the Attribution, Relation, and Order (ARO) benchmark to systematically evaluate the ability of VLMs to understand different types of relationships, attributes, and order. ARO consists of Visual Genome Attribution, to test the understanding of objects' properties; Visual Genome Relation, to test for relational understanding; and COCO & Flickr30k-Order, to test for order sensitivity. ARO is orders of magnitude larger than previous benchmarks of compositionality, with more than 50,000 test cases. We show where state-of-the-art VLMs have poor relational understanding, can blunder when linking objects to their attributes, and demonstrate a severe lack of order sensitivity. VLMs are predominantly trained and evaluated on large datasets with rich compositional structure in the images and captions. Yet, training on these datasets has not been enough to address the lack of compositional understanding, and evaluating on these datasets has failed to surface this deficiency. To understand why these limitations emerge and are not represented in the standard tests, we zoom into the evaluation and training procedures. We demonstrate that it is possible to perform well on retrieval over existing datasets without using the composition and order information. Given that contrastive pretraining optimizes for retrieval on datasets with similar shortcuts, we hypothesize that this can explain why the models do not need to learn to represent compositional information. This finding suggests a natural solution: composition-aware hard negative mining. We show that a simple-to-implement modification of contrastive learning significantly improves the performance on tasks requiring understanding of order and compositionality."

**Note on body/results quotes:** Specific per-model per-task accuracy numbers and section-level body passages are not verified here — the arXiv HTML version was unavailable (404) and the PDF was binary. The abstract is verified verbatim; detailed results live in the paper's Table 1 and section 3. A full PDF ingestion or arXiv HTML fetch when available would supply section-level quotes with page numbers.

## SugarCrepe (Hsieh et al. 2023, NeurIPS) — brief note

SugarCrepe (arXiv 2306.14610) is a directly related paper that *critiques* benchmarks like ARO and Winoground for harboring exploitable text-only artifacts, introduces an LLM-generated hard-negative benchmark to address this, and re-evaluates prior claims of improvement. Its **abstract** (verified verbatim from the NeurIPS 2023 proceedings page https://proceedings.neurips.cc/paper_files/paper/2023/hash/63461de0b4cb760fc498e85b18a7fe81-Abstract-Datasets_and_Benchmarks.html and OpenReview https://openreview.net/forum?id=Jsc7WSCZd4, both fetched 2026-05-30) reads:

> "In the last year alone, a surge of new benchmarks to measure compositional understanding of vision-language models have permeated the machine learning ecosystem. Given an image, these benchmarks probe a model's ability to identify its associated caption amongst a set of compositional distractors. Surprisingly, we find significant biases in all these benchmarks rendering them hackable. This hackability is so dire that blind models with no access to the image outperform state-of-the-art vision-language models. To remedy this rampant vulnerability, we introduce SugarCrepe, a new benchmark for vision-language compositionality evaluation. We employ large language models, instead of rule-based templates used in previous benchmarks, to generate fluent and sensical hard negatives, and utilize an adversarial refinement mechanism to maximally reduce biases. We re-evaluate state-of-the-art models and recently proposed compositionality inducing strategies, and find that their improvements were hugely overestimated, suggesting that more innovation is needed in this important direction."

Authors: Cheng-Yu Hsieh, Jieyu Zhang, Zixian Ma, Aniruddha Kembhavi, Ranjay Krishna (University of Washington / AI2 / Cornell). Venue: *Advances in Neural Information Processing Systems 36* (NeurIPS 2023), Datasets and Benchmarks Track. arXiv: 2306.14610.

**What SugarCrepe adds:** The core finding is that "blind models with no access to the image outperform state-of-the-art vision-language models" on prior compositionality benchmarks — i.e., the hard-negative foils in Winoground-style benchmarks are lexically distinctive enough that text-only classifiers exploit the artifact without accessing the image. SugarCrepe replaces rule-based foil generation with LLM-generated fluent negatives plus adversarial filtering, producing a benchmark that cannot be short-circuited this way. The re-evaluation finds that previously reported improvements on ARO-style tasks were "hugely overestimated." **Body-section quotes and per-model numbers from SugarCrepe are not verified here** — only the abstract (from NeurIPS proceedings and OpenReview) is confirmed verbatim. A dedicated source page (`source/hsieh-2023-sugarcrepe`) is warranted if findings page citations need more than abstract-level support from this paper; it is listed as `wanted` in this session's return.

## What it can ground

- The `grounded.perceptual` tag on findings about cross-modal compositional failure — this paper provides the mechanistic explanation and systematic sub-decomposition of the failure (attribution / relation / order).
- The "bags of words" framing as a named, diagnosable pathology of contrastive VLM training: the model compresses image-text co-occurrence without encoding structural relations.
- The claim that compositional deficiency is invisible on standard retrieval benchmarks (a null-on-standard-eval, positive-on-targeted-probe pattern that mirrors this project's own surprisal-contrast vs. standard-NLI results).
- The proposition that training-time fixes (composition-aware hard negatives) can improve compositional sensitivity — useful context for interpreting improvement claims.

## What it cannot ground

- Claims about generative VLMs — the paper tests discriminative (retrieval/matching) models, primarily CLIP variants.
- Claims about specific modern generative models (GPT-4V, Gemini, etc.) probed in this project's panel — those are outside the paper's scope.
- The exact magnitude of each failure by sub-dimension (needs Table 1 from the full PDF).
- Claims that compositionality is fully fixed by hard negative mining — SugarCrepe (Hsieh et al. 2023) shows improvements were overestimated.

## Known limits

- Behavioral evaluation; does not probe internal representations.
- Discriminative task (image-text retrieval) — failure mode may not transfer to generative or prompted evaluation settings used by this project.
- The "bags of words" framing was developed for contrastively trained CLIP-style models; its applicability to instruction-tuned generative VLMs is a separate empirical question.
- Body quotes and numerical results are abstract-verified only; Table 1 per-model numbers are unverified.
