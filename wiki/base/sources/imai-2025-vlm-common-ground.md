---
type: source
id: imai-2025-vlm-common-ground
title: Measuring How (Not Just Whether) VLMs Build Common Ground
authors:
  - Imai, Saki
  - İnan, Mert
  - Sicilia, Anthony
  - Alikhani, Malihe
year: 2025
venue: arXiv preprint
arxiv: "2509.03805"
url: https://arxiv.org/abs/2509.03805
access: open-access
meaning-senses:
  - relational
  - distributional
  - human-comparison
status: received
created: 2026-06-12
updated: 2026-06-12
links:
  - rel: refines
    target: concept/relational-meaning
---

# Imai et al. 2025 — Measuring How (Not Just Whether) VLMs Build Common Ground

## What it is

arXiv preprint (submitted 2025-09-04), no journal/conference venue stated on the abs page at retrieval. The closest existing empirical neighbor to the project's relational pilot: it runs **model–model self-play dyads in an iterated referential game** (PhotoBook, five rounds, MS COCO images) and evaluates them **against a large human-dyad corpus** with a four-metric suite — grounding efficiency, content alignment, **lexical adaptation** (the conceptual-pacts measure), and human-likeness. The headline: VLM dyads succeed at the task while *failing to ground the way humans do* — in particular, they do not form human-like conceptual pacts.

Provenance: abstract verbatim from the arXiv abs page; all body quotes below verified character-for-character against the arXiv HTML v1 full text (fetched 2026-06-12), with section locators.

Note on the word "grounding": throughout this paper "grounding" is **Clark-style conversational grounding** (building common ground in dialogue), *not* symbol grounding in the Harnad sense — do not conflate with [`concept/symbol-grounding-problem`](../concepts/symbol-grounding-problem.md) or [`concept/grounding`](../concepts/grounding.md).

## Summary

- **Task.** PhotoBook: dyads must discover which of three visually similar images they share. Three proprietary VLM dyads (GPT4.1, GPT4o-mini, Claude3.5-Haiku), 50 games each (150 sessions), compared with the released human–human PhotoBook corpus.
- **Metrics.** Grounding efficiency (task success vs. effort over rounds); content alignment (CLIPScore-based image–utterance alignment); lexical adaptation (Word Novelty Rate — do partners reuse each other's established expressions?); human-likeness (distributional energy distance from human dialogues).
- **Findings.** All three models diverge from human patterns on at least three of the four metrics. Humans compress referring expressions from round 2 on (the classic entrainment curve); VLMs stay verbose and keep coining new descriptions instead of reusing established shorthand. Task success does not indicate successful grounding — a case study shows GPT4.1 inflating its score by sycophantically mirroring its partner.

## Key passages

Locators are section numbers/titles in the arXiv HTML v1.

**Abstract — headline finding:**

> "All three models diverge from human patterns on at least three metrics, while GPT4o-mini is the closest overall."

**Introduction (fn. 1) — the Clark-lineage frame:**

> "Following Clark (1996), we use common ground to mean the set of propositions that all interlocutors mutually believe, know that the others believe, and recognize as a basis for subsequent action."

**Introduction — the conceptual-pacts research question (RQ3, labeled "lexical adaptation"):**

> "Do VLM pairs form human-like conceptual pacts, reusing each other's terms and pruning redundant detail over rounds?"

**§3.1 The PhotoBook Task — the game:**

> "PhotoBook is a five round referential game in which two conversational partners must discover which of three images they share, and which are unique to each speaker"

**§3.1 Human corpus — the human-comparison baseline:**

> "The released dataset contains 2,506 human–human dialogues (164,615 utterances, 130,322 actions and spans a vocabulary of 11,805 unique tokens)."

**§5.3 Lexical adaptation — the conceptual-pacts result:**

> "These metrics show that VLM pairs do not fully replicate human strategies of lexical adaptation." … "While some VLMs, such as Claude, exhibit partial human-like adaptation in lexical choices, GPT-4 models struggle to stabilize and reuse previously grounded referring expressions."

**Discussion — the compression failure:**

> "VLMs tend to produce unnecessarily long utterances and rarely reuse previously established shorthand."

## What this bears on in-repo

- **Independent convergence on the pilot's discipline.** [`open-question/relational-meaning-pilot`](../../findings/open-questions/relational-meaning-pilot.md) insists that coordination success is the *floor*, not the finding, and that the comparison must be against independent human dyadic data, never model-agreement. This paper independently enacts both commitments — "how, not just whether" is its title-level thesis, and its human baseline is corpus-grade — which corroborates the pilot's methodological stance from outside the project.
- **Direct bearing on the pilot's measured non-compression.** [`result/relational-reference-game-v1`](../../findings/results/relational-reference-game-v1.md) reports "convergence WITHOUT human-like compression" in its title; this paper's §5.3 and Discussion findings (verbose utterances, little reuse of established shorthand, contrast with the human round-2 compression curve) are the same phenomenon found independently in VLM dyads on a different game with a far larger human baseline. The two results support each other at the level of *pattern*; note they used different models and modalities, so the support is qualitative.
- **What it does NOT test: trajectory-dependence.** Like Ashery et al. ([`source/ashery-2025-llm-conventions`](ashery-2025-llm-conventions.md)), there is no order-scramble / shuffled-history control: lexical adaptation (WNR) measures *reuse*, which the deflationary distributional story ([`concept/distributional-meaning`](../concepts/distributional-meaning.md)) predicts from content alone. So the paper sharpens but does not answer the constitution question of [`concept/relational-meaning`](../concepts/relational-meaning.md); the live-vs-shuffled discriminator and the aggregation/constitution distinction of [`conjecture/commutative-convention`](../../findings/conjectures/commutative-convention.md) remain the project's own wedge.
- **Human anchor lineage.** The paper cites and operationalizes exactly the human literature the project ratified as its relational anchor line (Clark & Wilkes-Gibbs 1986; Brennan & Clark 1996; Pickering & Garrod 2004; Krauss & Weinheimer 1964 — all named in its Introduction/Related Work), and its human corpus plays the same calibration role the Hawkins tangrams corpus ([`resource/hawkins-tangrams`](../resources/hawkins-tangrams.md)) plays in-repo.

## What it can ground

- The claim that current model dyads achieve referential coordination without human-like conceptual-pact formation (verbatim §5.3 / Discussion quotes above).
- The methodological claim that task success is a poor proxy for grounding quality in interactive settings.
- Calibration expectations for what human entrainment/compression looks like in a five-round reference game (via the PhotoBook human-corpus statistics).

## What it cannot ground

- Any meaning-constitution claim — reuse/adaptation metrics are order-insensitive in design; no trajectory control.
- Claims about the project's own panel models — the paper tests GPT4.1, GPT4o-mini, Claude3.5-Haiku, none of which is in [`config/models.md`](../../../config/models.md)'s panel.
- Strong text-only conclusions — PhotoBook is image-referential; effects may differ for text-only referents.

## Known limits

- Preprint; not peer-reviewed at retrieval (2026-06-12). No stated venue.
- 50 games per model pair; round-level patterns (e.g. the round-2 word-count increase in GPT4o-mini and Claude) are reported without the project's preferred uncertainty discipline everywhere.
- "Human-likeness" is a distributional energy distance over dialogue features — divergence from it is not by itself a semantic deficit; the paper itself notes Claude3.5 matches humans on lexical adaptation while diverging in overall style.

## Status in wanted.md

Was not previously listed. Catalogued 2026-06-12 as the second relational-axis source (dyadic / conceptual-pacts side, complementing the population-scale Ashery et al. page); noted there.
