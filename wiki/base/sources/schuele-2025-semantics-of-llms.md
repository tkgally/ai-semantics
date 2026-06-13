---
type: source
id: schuele-2025-semantics-of-llms
title: On the Semantics of Large Language Models
authors:
  - Schuele, Martin
year: 2024
venue: Intellectica 81, pp. 15-36 (2024); arXiv 2507.05448 (2025 preprint posting)
arxiv: "2507.05448"
url: https://arxiv.org/abs/2507.05448
access: open-access
meaning-senses:
  - referential
  - distributional
status: received
created: 2026-06-12
updated: 2026-06-12
links:
  - rel: refines
    target: concept/referential-meaning
  - rel: refines
    target: concept/distributional-meaning
---

# Schuele 2024/2025 — On the Semantics of Large Language Models

## What it is

Single-author philosophical article: published in *Intellectica* 81, pp. 15–36 (2024), per the arXiv journal reference; posted to arXiv as 2507.05448 (v1, 2025-07-07; subject categories cs.CL, cs.AI). Author listed on arXiv as **Martin Schuele**. The paper narrows the "do LLMs understand?" question to **word- and sentence-level semantics**, gives a concise technical description of how LLMs build distributed vector-space representations, and then runs that description against the classical theories of meaning of **Russell** and **Frege**. The verdict is deliberately split: on a purely referential account LLM representations come out meaningless, but the latent space "shares certain properties with Frege’s notion of sense" — so whether LLMs have semantics depends on which classical notion of meaning one holds fixed. This is the strongest philosophical-track item from the project's 2026-06-12 literature refresh ([`wanted.md`](../wanted.md), "2025–2026 OA finds").

Provenance: title, author, journal reference, and abstract fetched from the arXiv abs page (https://arxiv.org/abs/2507.05448) on 2026-06-12; the abstract below is verbatim from that page. All body quotes below were verified character-for-character against the arXiv HTML v1 full text (https://arxiv.org/html/2507.05448, fetched 2026-06-12), with section locators from that rendering's structure (§1 Introduction; §2 What are LLMs?, §2.1–2.5; §3 Semantic Theories, §3.1.1 Russell, §3.1.2 Frege; §4 Discussion; §5 Conclusion). The *Intellectica* journal version itself was **not** consulted; the pp. 15–36 range comes from the arXiv metadata, and no journal page numbers are used as quote locators.

## Abstract (verbatim)

> "Large Language Models (LLMs) such as ChatGPT demonstrated the potential to replicate human language abilities through technology, ranging from text generation to engaging in conversations. However, it remains controversial to what extent these systems truly understand language. We examine this issue by narrowing the question down to the semantics of LLMs at the word and sentence level. By examining the inner workings of LLMs and their generated representation of language and by drawing on classical semantic theories by Frege and Russell, we get a more nuanced picture of the potential semantic capabilities of LLMs."

## Summary of the argument

1. **Technical ground (§2).** LLMs are probabilistic, connectionist language models whose core semantic-relevant object is the **distributed representation**: tokens as points in a high-dimensional latent space, where a single point is meaningless and only relations among points (and the decoding mechanism that puts them to use) carry content.
2. **Classical theories (§3).** Russell: meaning via reference, logical analysis, knowledge by acquaintance/description, a referential theory of truth. Frege: the sense/reference (Sinn/Bedeutung) distinction — sense as objective, shareable mode of presentation; sentence reference as truth value; indirect reference in indirect speech.
3. **Against Russell (§4).** Text-based LLMs fail the referential requirements: no logical decomposition, no acquaintance (no perception), no description-checking against the facts. But Russell's **context principle** survives in distributional form: a word gains its standing only in the context of other words and ultimately of the whole training distribution.
4. **With Frege (§4).** The latent space shares several properties with Fregean sense: objective and shareable, possible without reference, compositional in the sense that word-representations determine sentence representations, and residing at a level between signs and world. LLMs treat words "always as if they have an indirect reference" — reference to other words/representations, as in Frege's indirect-speech scheme. Sense, on this reading, results from use across the totality of training.
5. **Verdict (§5).** Engaging Bender & Koller's octopus test directly: whether LLMs have semantics "depends on how meaning is defined by Frege and Russell." Reference-only: meaningless. Reference-plus-sense: LLM representations "can carry that kind of semantics." The paper flags that truth (sentence-level reference, for Frege) remains the unresolved hard part, for LLMs as for us, and that an analysis in terms of intentions, beliefs, or consciousness might come out differently.

## Key passages (verbatim, section locators from the arXiv HTML v1)

**§2.5 Summary — a single representation is not meaningful; relations are:**

> "Now, a point, a single vector representation, is not inherently meaningful; it is just a bunch of numbers. Only in relation to other points in that space we gain a meaningful and context-sensitive representation."

**§4 Discussion — the referential failure, and the Bender–Koller inference it licenses:**

> "Text-based LLMs, quite obviously, lack reference; based on this it has been concluded that these systems cannot possess or learn meaning" — citing Bender & Koller 2020; the paper immediately offers two responses, citing Piantadosi & Hill 2022 ("reference may not be the only kind of meaning involved here") and Mollo & Millière 2023 (indirect referential grounding).

**§4 Discussion — Russell's context principle, distributionalized:**

> "Second, and more generally, Russell’s contextual principle appears to also apply to LLMs, though not in the logical form per Russell. A word gains meaning only in the context of other words; more generally, words and sentences represent in relation to the overall context of the entire training data and model training."

**§4 Discussion — the central claim:**

> "The latent space, i.e., the vector space representation of language in LLMs, which is a core element in the deep learning approach to language, shares certain properties with Frege’s notion of sense."

**§4 Discussion — sense from the totality of training, ultimately from use:**

> "In LLMs, it’s the totality of words and sentences, and their myriad interrelations, contextualized in many ways, as experienced through the dataset and training, that essentially gives a word its sense. Ultimately, sense results from the use of language."

**§5 Conclusion — the split verdict:**

> "If meaning is solely based on reference, that is, some referential capability, LLM-generated representations are meaningless, because the text-based LLMs representation do not directly refer to the world unless the reference is somehow indirectly induced."

> "If meaning however is associated with another kind of meaning such as Frege’s sense in addition to reference, it can be argued that LLM representations can carry that kind of semantics."

(Note on rendering: quotes are taken from the arXiv HTML, whose in-text citations render as "(Author, Year )"; citation parentheticals inside quoted sentences are reported in prose rather than quoted, and typographic apostrophes are preserved as in the source.)

## Bearing on this project

- **[`concept/referential-meaning`](../concepts/referential-meaning.md).** This is the project's first in-repo source that applies the Frege/Russell apparatus *directly to LLM internals* rather than to LLM behavior. Its mapping — latent space ≈ Fregean `Sinn` (the `referential.sense` sub-tag), reference and truth still missing (the `referential.reference` sub-tag) — is a worked, citable version of exactly the sense-vs-reference split the concept page carries; a finding that turns on "LLM tracks sense but not reference" can now cite a published argument for that framing rather than asserting it.
- **The `referential`/`distributional` boundary.** The paper's positive claim sits precisely on the contested line the [`meaning-senses.md`](../../meaning-senses.md) caveat for `distributional` names ("by itself, distributional structure is silent on reference and on truth"): Schuele argues the distributional object (the latent space) *is* a sense-like semantic object while conceding it is silent on reference and truth. That is the boundary stated as a position, from the referential side — a useful counterweight to [`source/piantadosi-hill-2022-meaning-without-reference`](piantadosi-hill-2022-meaning-without-reference.md), which approaches the same line from conceptual-role semantics (and which Schuele cites approvingly as one response to the no-reference objection).
- **[`source/bender-koller-2020-climbing`](bender-koller-2020-climbing.md).** The Conclusion engages the octopus test by name and answers it with a distinction rather than a denial: trained-on-form-only is conceded; what is contested is whether *meaning* is exhausted by reference. This gives the project a third position in the triangle with Bender–Koller (no reference, so no meaning) and Piantadosi–Hill (meaning without reference): reference-meaning absent, sense-meaning arguably present.
- **[`concept/symbol-grounding-problem`](../concepts/symbol-grounding-problem.md) and [`source/harnad-1990-symbol-grounding`](harnad-1990-symbol-grounding.md).** §4 names Harnad's symbol grounding problem and canvasses indirect-grounding routes (memorized referring text; Frege-style indirect reference, with an Eco/Peirce infinite-semiosis worry; multimodal models as mediated, task-driven access) — a compact philosophical companion to the gradual-grounding picture in [`source/lyre-2024-semantic-grounding`](lyre-2024-semantic-grounding.md), though Schuele's distinctive twist is that what needs grounding is *sentences* (truth), not word-representations.
- **[`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md).** The closing move — sense "results from the use of language," while truth-as-sentence-reference remains the open obligation — lands the paper between the two poles that concept page maps; it is a citable instance of a Fregean account sliding toward use-based vocabulary when applied to LLMs.
- **Model-internal, aggregation-style account.** Schuele's story locates sense in one model's relation-structure over the *totality* of training experience — a model-internal, aggregation-flavored picture consonant with (though entirely independent of) the relational-axis verdict argued in [`essay/aggregation-not-constitution`](../../findings/essays/aggregation-not-constitution.md); nothing in the paper bears on between-agent constitution, and it should not be cited on that question.

## What it can ground

- Citations for the position "LLM latent-space representations share properties with Fregean sense while lacking reference and truth" — as a published philosophical analysis (Intellectica 2024 / arXiv 2025), not as an empirical result.
- The framing that the LLM-understanding question decomposes by *theory of meaning held fixed*, with Russell-referential and Frege-sense verdicts coming apart.
- The observation that Russell's context principle, stripped of its logical form, is the distributional hypothesis's philosophical cousin.

## What it cannot ground

- Any empirical claim about any model: the paper reports no experiments, probes, or measurements; it is conceptual analysis over a textbook-level description of LLM architecture.
- Claims about lexical gradience, constructional meaning, or any of this project's probe-level questions — the analysis stays at the level of "the latent space" generically.
- A settled identification of latent space with Fregean sense: the paper itself hedges ("This does not mean that we find exactly Frege’s sense here; inter alia Frege could not possibly have this in mind" — §4 Discussion, verbatim).

## Known limits

- Position paper by a single author; the *Intellectica* venue is a French cognitive-science journal, and the project has not independently verified its review process — treat the paper's standing as "published philosophical article," no stronger.
- The technical description (§2) is at survey level (BERT-era probing results, generic transformer description); the paper's claims would not be sensitive to architecture-level differences between models.
- The paper explicitly brackets intentions, beliefs, and consciousness (§5): its split verdict holds only within the classical, objectivist theory of meaning it adopts.
- Only the arXiv v1 HTML was read; the published *Intellectica* text may differ.

## Status in wanted.md

Listed in [`wanted.md`](../wanted.md) under "2025–2026 OA finds" at P2, where the pre-catalogue status line called it the strongest queued philosophical candidate (abstract verified there 2026-06-12). Catalogued 2026-06-12; the wanted.md entry was flipped to `RECEIVED` by the orchestrating session in the same wave.
