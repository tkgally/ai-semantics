---
type: source
id: scivetti-2025-beyond-memorization
title: "Beyond Memorization: Assessing Semantic Generalization in Large Language Models Using Phrasal Constructions"
authors:
  - Scivetti, Wesley
  - Torgbi, Melissa
  - Shichman, Mollie
  - Pellegrin, Taylor
  - Blodgett, Austin
  - Bonial, Claire
  - Tayyar Madabushi, Harish
year: 2025
venue: "Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (IJCNLP-AACL 2025), pp. 1184–1201"
arxiv: "2501.04661"
url: https://aclanthology.org/2025.ijcnlp-long.65/
access: open-access
meaning-senses:
  - constructional
  - inferential
  - human-comparison
status: received
created: 2026-05-29
updated: 2026-05-29
pdf-pages: "ACL Anthology 2025.ijcnlp-long.65 (PDF, pp. 1184–1201); arXiv 2501.04661 v1 HTML for body section quotes"
links:
  - rel: supports
    target: concept/constructional-meaning
---

# Scivetti et al. 2025 — Beyond Memorization: Assessing Semantic Generalization in LLMs Using Phrasal Constructions

## What it is

Empirical CxG-probing paper, published at IJCNLP-AACL 2025 (pp. 1184–1201), arXiv 2501.04661. Lead author Wesley Scivetti (Georgetown); senior author Harish Tayyar Madabushi (University of Bath); other authors at the U.S. Army Research Lab and Bath. This single paper covers **both** P2 wanted entries — "Scivetti et al. (recent constructional probing)" and "Tayyar Madabushi et al. on … constructional probing" — since Tayyar Madabushi is its senior author.

Note on title/version drift: arXiv v1 (8 Jan 2025) was titled "Assessing Language Comprehension in Large Language Models Using Construction Grammar"; v2 (13 Aug 2025) and the published ACL version were retitled "Beyond Memorization: Assessing Semantic Generalization in Large Language Models Using Phrasal Constructions." This page uses the published title/venue as the citable record; the body section quotes below were read from the arXiv **v1** HTML and are labelled as such.

## Summary

The paper builds a diagnostic evaluation that uses Construction Grammar (CxG) to separate LLM competence on cases well-represented in pretraining data from genuine generalization to out-of-domain instances. The design rests on a property of phrasal constructions: human speakers abstract over commonplace instantiations to understand and produce creative ones (e.g. atypical lexical fillers in a familiar constructional slot). The authors test 8 unique constructions on natural language inference and reasoning tasks, comparing LLM behavior with human behavior.

Two questions structure the evaluation:
1. Can models understand the semantics of sentences whose instantiations are rarer in pretraining data but intuitive for people?
2. Can LLMs deploy the appropriate constructional semantics when constructions are **syntactically identical but semantically divergent** — i.e., when the same form carries different constructional meaning?

Headline result (published version): state-of-the-art models including GPT-o1 show a performance drop of **over 40%** on the second task — a failure to generalize over syntactically identical forms to arrive at distinct constructional meanings the way humans do. The framing: LLMs process constructional semantics "up to a point," and the challenge sets locate the "breaking point of understanding."

Relation to this project: this is the most directly on-target recent empirical instance of the CxG-probing program described by [`source/weissweiler-2023-cxg-insight`](weissweiler-2023-cxg-insight.md). It operationalizes the memorization-vs-construction-knowledge confound that Weissweiler et al. name, using out-of-distribution lexical fillers as the lever, and it carries explicit human comparison data — relevant to any AANN or argument-structure conjecture in this repo that needs a human-anchored generalization test.

## Key passages

Abstract quoted verbatim from the **published ACL Anthology page** (https://aclanthology.org/2025.ijcnlp-long.65/, fetched 2026-05-29, HTML). Body section quotes read verbatim from the **arXiv v1 HTML** rendering (https://arxiv.org/html/2501.04661v1, fetched 2026-05-29); sections cited by heading/number as printed in v1.

**Abstract (verbatim, published ACL version) — design and headline result:**

> "The web-scale of pretraining data has created an important evaluation challenge: to disentangle linguistic competence on cases well-represented in pretraining data from generalization to out-of-domain language, specifically the dynamic, real-world instances less common in pretraining data. To this end, we construct a diagnostic evaluation to systematically assess natural language understanding in LLMs by leveraging Construction Grammar (CxG). CxG provides a psycholinguistically grounded framework for testing generalization, as it explicitly links syntactic forms to abstract, non-lexical meanings. Our novel inference evaluation dataset consists of English phrasal constructions, for which speakers are known to be able to abstract over commonplace instantiations in order to understand and produce creative instantiations. Our evaluation dataset uses CxG to evaluate two central questions: first, if models can \"understand\" the semantics of sentences for instances that are likely to appear in pretraining data less often, but are intuitive and easy for people to understand. Second, if LLMs can deploy the appropriate constructional semantics given constructions that are syntactically identical but with divergent meanings. Our results demonstrate that state-of-the-art models, including GPT-o1, exhibit a performance drop of over 40% on our second task, revealing a failure to generalize over syntactically identical forms to arrive at distinct constructional meanings in the way humans do. We make our novel dataset and associated experimental data, including prompts and model responses, publicly available."

**§2.1 Construction Grammars (verbatim, arXiv v1 HTML) — CxG as form–meaning pairs:**

> "CxG encompasses a family of linguistic theories which posit that morphemes, words, idioms, and even schematic structures in language can be represented as simple form-meaning pairs, or constructions (Cxns), at different levels of granularity and abstraction."

**§3 Theory-Informed Experimental Design (verbatim, arXiv v1 HTML) — the open generalization question:**

> "However, it is not clear the extent to which LLMs can recognize and generalize over the formal properties of language in order to ascribe shared semantics to novel usages"

**§9 Conclusions and Future Work (verbatim, arXiv v1 HTML) — the "breaking point of understanding":**

> "Thus, our targeted series of experiments demonstrated that LLMs do process constructional semantics up to a point, yet our challenge datasets revealed the breaking point of understanding—where speakers are able to generalize the appropriate semantics to constructional slots filled by pragmatically atypical lexical items, but LLMs are much less proficient at this generalization."

## What it can ground

- The `constructional` tag on conjecture/result pages that test argument-structure or phrasal constructions via inference rather than acceptability — this paper is a recent empirical exemplar with public data.
- The memorization-vs-construction-knowledge confound (named by Weissweiler 2023): this paper operationalizes it concretely by constructing examples "unlikely to appear in pre-training data" with pragmatically atypical lexical fillers. Any AANN result that must rule out memorization can cite this as a method precedent.
- A `human-comparison` anchor pattern: the design compares LLM behavior with human behavior on the same 8 constructions, and the public dataset (prompts + model responses) is a candidate resource for a `wiki/base/resources/` page if a finding needs it.
- The specific empirical claim that even GPT-o1 drops >40% when the same syntactic form carries divergent constructional meaning — a concrete supported data point for the `functional-vs-formal` / generalization-failure line.

## What it cannot ground

- Claims about AANN specifically — this paper tests 8 phrasal constructions, and the public summary/sections read do not single out the Article + Adjective + Numeral + Noun construction. Do not cite it as AANN evidence without confirming the construction inventory in the full PDF.
- Mechanistic / representational claims — the evaluation is behavioral (NLI + reasoning task accuracy), not probing of internal representations, so it does not ground `model-internal` claims.
- Exact per-construction numbers or the human-baseline figures — those need the full PDF (pp. 1184–1201); only the abstract-level >40% figure and the section-level framing quotes above are verified here.

## Known limits

- Behavioral evaluation; results are task accuracies, not direct evidence about what models represent.
- Title and framing shifted between arXiv v1 ("Assessing Language Comprehension … Using Construction Grammar") and the published version ("Beyond Memorization … Using Phrasal Constructions"); the v1 body quotes here are from the earlier framing. If precise published-version wording of body passages is needed, the ACL PDF must be consulted.
- The body section quotes are from the arXiv v1 HTML, not the camera-ready PDF; page-level provenance for body passages is pending PDF ingestion.

## Status in wanted.md

Was `wanted` under both "Tayyar Madabushi et al. on AANN and constructional probing" and "Scivetti et al. (recent constructional probing work)" (P2). Now `received`: full abstract verbatim from the published ACL Anthology page, plus three section-level body quotes verbatim from arXiv v1 HTML (both fetched 2026-05-29). One paper resolves both wanted entries (Tayyar Madabushi is senior author). Full PDF (ACL, pp. 1184–1201) available for per-construction and human-baseline numbers if a finding needs them.
