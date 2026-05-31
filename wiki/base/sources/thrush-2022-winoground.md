---
type: source
id: thrush-2022-winoground
title: "Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality"
authors:
  - Thrush, Tristan
  - Jiang, Ryan
  - Bartolo, Max
  - Singh, Amanpreet
  - Williams, Adina
  - Kiela, Douwe
  - Ross, Candace
year: 2022
venue: "Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022)"
arxiv: "2204.03162"
url: https://arxiv.org/abs/2204.03162
access: open-access
meaning-senses:
  - grounded.perceptual
  - constructional
  - human-comparison
status: received
created: 2026-05-30
updated: 2026-05-31
pdf-pages: "arXiv 2204.03162 abstract page (verbatim abstract fetched 2026-05-30); CVPR 2022 Open Access HTML (abstract confirmed verbatim 2026-05-30); HuggingFace dataset page for random-baseline quote (fetched 2026-05-30). Body quotes (four-annotator curation §3.1, ten-annotator labeling §4.3, dataset size §3.1, per-model scores Table 3) verified verbatim from the ar5iv HTML rendering (ar5iv.labs.arxiv.org/html/2204.03162, fetched 2026-05-31, re-confirmed 2026-05-31); HTML carries no page numbers, so body quotes are cited by section/table. No inter-annotator agreement statistic exists in the source (verified absent)."
links:
  - rel: supports
    target: concept/multimodal-compositionality
---

# Thrush et al. 2022 — Winoground: Probing VLMs for Visio-Linguistic Compositionality

## What it is

Benchmark paper, published at CVPR 2022; arXiv 2204.03162. Lead author Tristan Thrush (Meta AI); co-authors Ryan Jiang, Max Bartolo, Amanpreet Singh, Adina Williams, Douwe Kiela, Candace Ross — multiple affiliations including Meta AI and NYU. The dataset is available at [https://huggingface.co/datasets/facebook/winoground](https://huggingface.co/datasets/facebook/winoground).

Winoground is the foundational human-curated compositionality benchmark for vision-language models (VLMs): the first widely-adopted test to isolate **word-order / compositional-structure sensitivity** in the image-text matching setting, by using pairs of captions with identical word inventories in different orders. Its near-chance SOTA result established the headline empirical claim that the VLM field mobilized around: these models fail at visio-linguistic compositionality.

## Summary

The paper presents a task and dataset in which a model is given two images and two captions. Both captions share exactly the same words; only the order differs (e.g., *"a dog chases a cat"* vs. *"a cat chases a dog"*). The model must correctly pair each image to its caption. Success requires genuine compositional interpretation; a bag-of-words (order-insensitive) strategy scores at chance. The dataset was hand-curated by expert annotators and tagged with fine-grained linguistic and visual categories to enable analysis.

The headline result: across a diverse range of SOTA vision-language models probed, none performed substantially better than chance on the Winoground task, demonstrating that these models fail at the core visio-linguistic compositional reasoning the task targets.

**Human-curation relevance.** The dataset is fully human-curated: both the image-caption pairs and the fine-grained tags were produced by expert annotators rather than generated from templates or mined automatically. The paper states (§3.1, verbatim, ar5iv HTML, re-confirmed 2026-05-31) that "The Winoground dataset was hand-curated by four expert annotators with extensive experience in vision and language research as well as computational linguistics." This makes Winoground a plausible human-anchored resource: the ground truth reflects human compositional judgments, not a formal rule system. **Inter-annotator agreement caveat:** the paper does **not** report any inter-annotator agreement statistic (no kappa or agreement rate appears anywhere in the body text as fetched via ar5iv on 2026-05-31, re-confirmed 2026-05-31). What it does report (§4.3, "Human Performance", verbatim) is the labeling depth: "All 1600 combinations of images and captions are labeled by at least ten annotators." So a downstream claim cannot cite a Winoground IAA figure — none exists in the source — but it can cite the four-expert-annotator curation procedure, the ten-annotator labeling depth, and the human (MTurk) baseline scores reported in Table 3 (see below).

## Key passages

Abstract quoted verbatim from **arXiv 2204.03162 abstract page** (https://arxiv.org/abs/2204.03162v2, fetched 2026-05-30) and cross-checked against the **CVPR 2022 Open Access HTML** (https://openaccess.thecvf.com/content/CVPR2022/html/Thrush_Winoground_Probing_Vision_and_Language_Models_for_Visio-Linguistic_Compositionality_CVPR_2022_paper.html, fetched 2026-05-30).

**Abstract (verbatim):**

> "We present a novel task and dataset for evaluating the ability of vision and language models to conduct visio-linguistic compositional reasoning, which we call Winoground. Given two images and two captions, the goal is to match them correctly - but crucially, both captions contain a completely identical set of words, only in a different order. The dataset was carefully hand-curated by expert annotators and is labeled with a rich set of fine-grained tags to assist in analyzing model performance. We probe a diverse range of state-of-the-art vision and language models and find that, surprisingly, none of them do much better than chance. Evidently, these models are not as skilled at visio-linguistic compositional reasoning as we might have hoped. We perform an extensive analysis to obtain insights into how future work might try to mitigate these models' shortcomings. We aim for Winoground to serve as a useful evaluation set for advancing the state of the art and driving further progress in the field."

**Random-baseline clarification (verbatim, HuggingFace dataset page, https://huggingface.co/datasets/facebook/winoground, fetched 2026-05-30):**

> "Why is the group score for a random model equal to 16.67%?"
> "We can conclude that the probability of a group score of 1 is 4/24 = 0.166..."

This establishes that the "near chance" result means near **16.67%**, not 50% — the group-score metric requires correctly matching both images in a pair, so random guessing gives 1 in 6 probability, not 1 in 2. The models probed do not substantially exceed this floor.

**Dataset size (verbatim, §3.1, ar5iv HTML, fetched 2026-05-31):**

> "Our dataset has 1600 image-text pairs in total, with 800 correct and 800 incorrect pairings. These comprise 400 examples, with 800 unique captions and images."

The headline unit is therefore **400 examples** (each example pairs two images with two captions).

**Per-model and baseline scores (verbatim selection, Table 3, ar5iv HTML, fetched 2026-05-31).** Table 3 reports Text / Image / Group scores. The random-chance row reads **"25.00, 25.00, 16.67"** and the human row reads **"MTurk Human: 89.50, 88.50, 85.50"**, confirming the chance floor for the group metric (16.67) and the high human ceiling. Representative model rows (Text / Image / Group): "VinVL: 37.75, 17.75, 14.50"; "UNITERlarge: 38.00, 14.00, 10.50"; "CLIP (ViT-B/32): 30.75, 10.50, 8.00". These confirm the "none do much better than chance" headline on the group metric while humans score 85.50. (Locator is Table 3; the table number is verified — earlier drafts that referred to "Table 1" were mistaken, as Table 1 in this paper holds linguistic/visual tag counts, not model scores.)

## What it can ground

- The `grounded.perceptual` tag on findings about VLMs and image-text alignment — this paper is the canonical benchmark paper establishing that VLMs fail at cross-modal compositional matching.
- The existence of a human-curated compositionality benchmark as a candidate human anchor for multimodal VLM claims. Annotation procedure is verified from the source (four expert annotators curated; each of the 1600 combinations labeled by at least ten annotators, §4.3); no inter-annotator agreement statistic is reported (verified absent), so none can be cited.
- The "bags of words" or order-insensitivity failure mode in VLMs as an empirical baseline finding — the paper is the widely-cited origin point for this framing in the VLM literature.
- The concept that compositional structure is not automatically captured by multimodal contrastive training (see [`concept/multimodal-compositionality`](../concepts/multimodal-compositionality.md)).

## What it cannot ground

- Claims about any specific model's score on Winoground beyond the representative Table 3 rows transcribed here; the full 12-configuration table lives in the paper's Table 3.
- The mechanisms behind the failure — Winoground is behavioral (image-text matching), not a probing of internal representations.
- Generative VLM behavior — the task is a discriminative image-caption matching task, not a generation task. This is a non-trivial gap for any project that uses generative panels.
- Claims specifically about text-only LLMs — the task requires multimodal input; the failure cannot be attributed to the text encoder alone without isolation.

## Known limits

- Behavioral benchmark only; does not access internal representations.
- Discriminative (matching) task, not generative: the near-chance result holds for image-text retrieval/matching, not for free-form captioning or question answering.
- The dataset is small and specialized (400 examples / 1600 image-text pairs as of the published paper, verified §3.1), which limits statistical power for fine-grained sub-analysis.
- Subsequent work has disputed whether some Winoground items are genuinely compositional (some require pragmatic and world-knowledge reasoning, not only syntactic compositionality); this complicates interpreting the "near chance" result as purely a compositionality failure.
- Per-model Text/Image/Group scores are now verified verbatim from Table 3 (ar5iv HTML, 2026-05-31); a representative selection is transcribed above rather than the full 12-row table. The paper reports **no** inter-annotator agreement statistic (verified absent), so no IAA figure can be cited from this source.
