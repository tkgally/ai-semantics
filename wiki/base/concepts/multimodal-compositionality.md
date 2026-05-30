---
type: concept
id: multimodal-compositionality
title: Multimodal Compositionality (VLM compositionality and the bags-of-words failure)
meaning-senses:
  - grounded.perceptual
  - constructional
  - distributional
  - human-comparison
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: depends-on
    target: source/thrush-2022-winoground
  - rel: depends-on
    target: source/yuksekgonul-2023-aro
  - rel: refines
    target: concept/grounding
  - rel: refines
    target: concept/constructional-meaning
---

# Multimodal Compositionality

## The core question

Do vision-language models (VLMs) compose the distributional-semantic contributions of individual words — their order, their structural relations, their attribute-binding — across the visual and linguistic modalities, or do they function as **bags of words**: treating each caption as an unordered set of tokens whose combined score is a sum of individual-token contributions, regardless of syntax?

This is the multimodal analogue of the question this project already runs on text-only models: do LLMs track constructional form–meaning pairings, or collapse them to distributional patterns? In both cases the wedge is the same in structure — hold the vocabulary constant, vary the structure, measure whether the model's output tracks the structural difference. In the multimodal case the structure is image-caption compositional matching; in the constructional case it is inference-licensing or surprisal-contrast on minimal pairs. The probe instrument differs (retrieval/matching vs. forced-choice/NLI), but the underlying semantic question — does structure carry meaning beyond the lexical bag? — is shared.

## Empirical baseline: three benchmark papers

**Winoground** ([`source/thrush-2022-winoground`](../sources/thrush-2022-winoground.md), Thrush et al. 2022, CVPR): the first and most influential human-curated VLM compositionality benchmark. Each item consists of two images and two captions sharing an identical word-bag; the captions differ only in word order / syntactic structure. SOTA VLMs — including CLIP and FLAVA — perform near chance (the group-score random baseline is 16.67%; models do not substantially exceed it), establishing that these models fail at visio-linguistic compositional reasoning.

**ARO** ([`source/yuksekgonul-2023-aro`](../sources/yuksekgonul-2023-aro.md), Yuksekgonul et al. 2023, ICLR Oral): decomposes the failure into three sub-dimensions — **attribution** (linking objects to properties), **relation** (directionality of structural relations), and **order** (sensitivity to word order) — using >50,000 test cases. The paper names the mechanism: contrastive pretraining "optimizes for retrieval on datasets with similar shortcuts," so "models do not need to learn to represent compositional information." The fix proposed — composition-aware hard negative mining — significantly improves compositionality scores, showing the failure is at least partially a training-objective artefact, not an architectural inevitability.

**SugarCrepe** (Hsieh et al. 2023, NeurIPS — abstract note in [`source/yuksekgonul-2023-aro`](../sources/yuksekgonul-2023-aro.md); a full dedicated source page is `wanted`): critiques Winoground-style and ARO-style benchmarks for harboring exploitable text-only artefacts. "Blind models with no access to the image outperform state-of-the-art vision-language models" on these benchmarks — meaning the foil captions are lexically distinctive enough to be rejected without looking at the image. SugarCrepe introduces LLM-generated hard negatives with adversarial filtering to remove this bias, and finds that previously reported improvements on compositionality tasks "were hugely overestimated." This complicates the simple reading of Winoground as demonstrating compositional failure: the failure could partly be a benchmark artefact (the near-chance result is real, but the specific deficits attributed to it need the cleaner SugarCrepe eval to adjudicate).

## Connection to this project's constructional wedge

This project's constructional probing line ([`concept/constructional-meaning`](constructional-meaning.md), CxG form–meaning pairings) is a **text-only analogue** of the multimodal compositionality question, operating at the level of argument-structure constructions and inference-licensing rather than image-caption matching. The structural parallel:

| Dimension | Text-only constructional probing | Multimodal compositionality |
|-----------|----------------------------------|----------------------------|
| Vocabulary control | Verb held constant; construction varies | Same words; order / structure varies |
| Meaning variation | Constructional meaning (add/cancel entailment) | Compositional image-caption match |
| Instrument | NLI, forced-choice, surprisal | Retrieval score, matching accuracy |
| Human anchor | Scivetti CxNLI, Mahowald AANN stimuli | Winoground expert-curated labels |
| Failure mode studied | Generalization gap on divergent-form items | Near-chance on word-order variants |

The `constructional` tag applies to both lines because CxG theory treats compositionality as a property of form–meaning pairings at all levels: the claim that VLMs fail at compositionality in the multimodal setting is a `grounded.perceptual` claim with a `constructional` structure. The multimodal case adds the `grounded.perceptual` sub-dimension that the text-only constructional line leaves unaddressed — it is the closest available test of whether cross-modal grounding changes the compositionality picture.

The ARO "bags of words" framing also mirrors the `distributional` shadow that the text-only constructional project tries to beat: a bag-of-words model *is* a distributional model that ignores order, just as the distributional null the constructional line competes against is the model that tracks co-occurrence patterns without tracking structural meaning.

## Gap: discriminative vs. generative evaluation

A key limitation for this project's purposes: all three benchmark papers use **discriminative** (retrieval / matching) evaluation — a model scores whether a given image-caption pair is correct, not whether it generates a compositionally appropriate description. This project's panel uses **generative** models (claude-sonnet, gpt-5.4-mini, gemini-3.5-flash) probed via NLI and forced-choice prompts, not retrieval scoring. The gap between discriminative and generative evaluation is non-trivial:

- A generative model may succeed at compositionality in prompted inference tasks even while a discriminative retrieval model fails at Winoground-style matching, because the task structures recruit different processing pathways.
- Conversely, a generative model may pass VLM compositionality tests by relying on prior knowledge of likely caption-image pairings rather than genuine cross-modal compositional parsing.
- Winoground is an image-text input task; this project's experiments use text-only prompts to language models, sidestepping the visual modality entirely.

**This gap should be flagged whenever multimodal compositionality evidence is cited in support of a finding about this project's generative text-only panel.** The connection is conceptual — both lines test whether model representations support compositional structure beyond the lexical bag — but the behaviours are not identical and should not be equated.

A future extension of this project into multimodal probing (e.g., using Winoground-style stimuli in a prompted VLM) would close this gap and give `grounded.perceptual` its first directly supported finding.

## Meaning-sense usage note

In this page, "compositional meaning" (the sense in which multimodal compositionality benchmarks test meaning) is `constructional` and `grounded.perceptual`: the meaning in question is the semantics carried by syntactic structure (word order, argument structure) as evaluated against visual content. It is not the same as `distributional` meaning (co-occurrence statistics) — the point of all three benchmark papers is precisely that distributional training is insufficient for compositional meaning. Any finding page citing these sources should tag at minimum `grounded.perceptual` and `constructional`, and should avoid the unqualified word "meaning" per the project's lint rule.
