---
type: source
id: grindrod-2024-linguistic-intentionality
title: Large language models and linguistic intentionality
authors:
  - Grindrod, Jumbly
year: 2024
venue: "Synthese 204: 71 (2024); arXiv 2404.09576 (v1 2024-04-15; v2 2024-09-16)"
arxiv: "2404.09576"
doi: 10.1007/s11229-024-04723-8
url: https://arxiv.org/abs/2404.09576
access: open-access
meaning-senses:
  - referential
  - distributional
  - inferential
status: received
created: 2026-06-14
updated: 2026-06-14
links:
  - rel: refines
    target: concept/referential-meaning
  - rel: refines
    target: concept/distributional-meaning
  - rel: refines
    target: concept/deflationary-and-eliminativist-llm-meaning
---

# Grindrod 2024 — Large language models and linguistic intentionality

## What it is

Single-author philosophy-of-language article (Jumbly Grindrod, University of Reading), published in *Synthese* 204: 71 (2024), DOI 10.1007/s11229-024-04723-8, also posted to arXiv as 2404.09576 (cs.CL; cs.AI). Its question is the project's own framing question put in metasemantic terms: do LLMs *meaningfully use* the words they produce, or are they "merely clever prediction machines, simulating language use by producing statistically plausible text"? Grindrod's distinctive move is to **shift the level of the question**. Most prior attempts (he focuses on Coelho Mollo & Millière 2023) ask whether LLMs satisfy a *mental* metasemantics — the conditions under which a *mental state* has content. Grindrod argues that is the wrong target: we should ask whether LLMs satisfy a **linguistic** metasemantics — the conditions under which a *linguistic item* has content. He then applies two such theories — **Gareth Evans' (1982) account of naming practices** and **Ruth Millikan's (1984, 2004, 2005) teleosemantics** — and argues that on both, LLM outputs come out **meaningful**, because linguistic intentionality (unlike mental intentionality) is constitutively *dependent on a pre-existing linguistic system*, which the model inherits from its training corpus. The verdict is hedged-positive: meaningful usage is plausible, with communicative intentions flagged as the remaining open question.

This is a **philosophical map and counterpoint, not a human-annotated resource.** Its evidence base is conceptual analysis over a survey-level description of transformer LLMs; this project's is behavioral black-box probing. The boundary is stated under "What it cannot ground." It is the most directly on-point philosophical item from the Grindrod backlog entry in [`wanted.md`](../wanted.md) (P1), which named only "[check current title]"; the title and venue are now verified.

Provenance and what was verified: title, author, abstract, subject categories, the journal reference (*Synthese* 204: 71), the DOI, and the two arXiv submission dates were fetched from the arXiv abs page (https://arxiv.org/abs/2404.09576) on 2026-06-14. The **full accepted-version PDF** (https://arxiv.org/pdf/2404.09576, the author's "Published in Synthese / Please cite published version" manuscript) was downloaded and its text extracted locally with `pdfminer` (88,757 characters); **all body quotes below were verified character-for-character against that extracted text**, with section locators from the paper's own numbered headings. The CentAUR version of record (https://centaur.reading.ac.uk/117589/3/117589%20VoR.pdf) was confirmed to exist as a second OA route but was not separately parsed. One provenance wrinkle, recorded honestly: the arXiv abs-page rendering of the abstract opened "like Chat-GPT or LLaMa," whereas the accepted-version PDF reads "like Chat-GPT or Claude" — a version difference between the abs-page metadata and the manuscript text. The abstract is quoted below **from the PDF** (the authoritative full text verified locally), and this discrepancy is flagged. The *Synthese* published HTML behind the Springer paywall was not consulted; no journal page numbers are used as locators (the article is numbered 71, not paginated in the quotes).

## Abstract (verbatim, from the accepted-version PDF)

> "Do large language models like Chat-GPT or Claude meaningfully use the words they produce? Or are they merely clever prediction machines, simulating language use by producing statistically plausible text? There have already been some initial attempts to answer this question by showing that these models meet the criteria for entering meaningful states according to metasemantic theories of mental content. In this paper, I will argue for a different approach – that we should instead consider whether language models meet the criteria given by our best metasemantic theories of linguistic content. In that vein, I will illustrate how this can be done by applying two such theories to the case of language models: Gareth Evans' (1982) account of naming practices and Ruth Millikan's (1984, 2004, 2005) teleosemantics. In doing so, I will argue that it is a mistake to think that the failure of LLMs to meet plausible conditions for mental intentionality thereby renders their outputs meaningless, and that a distinguishing feature of linguistic intentionality – dependency on a pre-existing linguistic system – allows for the plausible result that LLM outputs are meaningful."

(The PDF uses en-dashes `–`; reproduced as in the source. The keywords line gives: "metasemantics; large language models; distributional semantics; intentionality".)

## Section structure (verbatim numbered headings, from the PDF)

1. The question of meaningful usage
2. The construction and theoretical background of large language models
3. Mental metasemantic theories and large language models
4. Linguistic metasemantics and large language models
5. Conclusion: context, content, and intentions

## Key passages (verbatim, section locators from the PDF)

**§1 — the mental/linguistic metasemantics distinction (the paper's organizing move):**

> "We can draw a broad distinction between two types of metasemantics: one that captures how a mental state has meaning (what I will call a mental metasemantics) and one that captures how a linguistic item has meaning (what I will call a linguistic metasemantics)."

**§1 — the roadmap, on the distributional grounding and on rejecting the mental-metasemantics route (the paper's own section preview):**

> "I will argue that it is not plausible that LLMs can be treated as sources of mental intentionality. In section 4, I will then make the case that LLMs are better understood through the lens of linguistic metasemantic theories. After all, such theories attempt to capture meaningful language usage, and this is precisely what we are considering in asking the meaningful usage question. I will make the case that LLMs are meaningful language users by applying two distinct metasemantic theories: Evans' (1982) account of naming practices and Millikan's (1984, 2004, 2005) teleosemantic theory of linguistic meaning."

**§2 — distributional semantics as the theoretical background, with the distributional hypothesis stated:**

> "LLMs have their origins within an approach to meaning known as distributional semantics (Erk, 2012; Lenci, 2018; Boleda, 2020; Grindrod 2023). This approach has a history stretching back to the likes of John Firth (1957) and Zellig Harris (1954) and is underpinned by the so-called distributional hypothesis: that the meaning of a word can be represented by its distribution across a text or corpus."

**§5 Conclusion — the load-bearing claim: linguistic intentionality presupposes a pre-existing linguistic system, which is what makes the positive result available:**

> "That LLMs look to stand a better chance of meeting the conditions of a linguistic metasemantics partly reflects a difference across the two types of metasemantics in their explananda. Instances of linguistic intentionality are reliant on a pre-existing linguistic system in a way that instances of mental intentionality need not be. Indeed, this is a feature of language that is made much of by both metasemantic theories considered: in Evans' notion that the meaning of name partly consists in the naming practice that circulates around the community, and in Millikan's notion that the meaning of a linguistic item is understood in terms of its history of reproduction."

**§5 Conclusion — the hedge that keeps the verdict modest (communicative intentions left open):**

> "As such, there is a sense in which generating an instance of linguistic intentionality is less demanding. At the same time, we have also seen that there is some plausibility to the idea that communicative intentions might play some necessary role on the production of a meaningful token. Ultimately, a great deal of further work will need to be done to defend a positive answer to the meaningful usage question."

(The PDF renders apostrophes typographically (Evans', Millikan's); reproduced as in the source. "the meaning of name" in the §5 passage is verbatim — the indefinite article appears to be dropped in the original.)

## Bearing on this project

- **[`concept/referential-meaning`](../concepts/referential-meaning.md) — the principal connection.** Evans' naming-practices account and Millikan's teleosemantics are both *externalist, content-fixing* theories — exactly the externalist pole that concept page carries (Evans appears there already as a characterized want; Millikan is the teleosemantics line). Grindrod's paper is a worked, citable application of those theories *to LLMs*, with a non-obvious result: the very externalism that grounds reference also supplies the "pre-existing linguistic system" the model inherits, so the externalist machinery is used here to license meaning **without** the model itself being a source of mental/referential content. A finding that turns on "the model inherits content from a public language rather than fixing it" can cite this rather than asserting it. Link is `refines` (it sharpens the externalist application).
- **[`concept/distributional-meaning`](../concepts/distributional-meaning.md).** §2 grounds LLMs explicitly in the Firth/Harris distributional tradition and the distributional hypothesis — the same lineage that concept page rests on — and Grindrod uses that grounding to *defuse* a class of skeptical arguments ("merely statistically plausible text") rather than to settle the meaning question by itself. This is a philosophy-side statement of why distributional structure is the right starting description while being silent, on its own, about content — the boundary [`meaning-senses.md`](../../meaning-senses.md) flags for the `distributional` tag. `refines`.
- **[`concept/deflationary-and-eliminativist-llm-meaning`](../concepts/deflationary-and-eliminativist-llm-meaning.md).** The paper is an explicit, published *push against* the "merely clever prediction machines" deflationary reading, arguing it is "a mistake to think that the failure of LLMs to meet plausible conditions for mental intentionality thereby renders their outputs meaningless." It pairs naturally with [`source/beckmann-queloz-2025-mechanistic-indicators`](beckmann-queloz-2025-mechanistic-indicators.md) (anti-deflation from the *mechanistic* side) as an anti-deflation argument from the *metasemantic/philosophy-of-language* side — but, as with that page, the project's own stance is **descriptivist ("describe, don't litigate")**, so cite this as one position in the debate, not as a result the project has established. `refines`.
- **[`source/piantadosi-hill-2022-meaning-without-reference`](piantadosi-hill-2022-meaning-without-reference.md) and [`source/schuele-2025-semantics-of-llms`](schuele-2025-semantics-of-llms.md).** Grindrod sits in a clear triangle with these two. Piantadosi & Hill argue *meaning without reference* (conceptual-role/inferential route); Schuele argues LLM latent space is *Fregean sense* without reference; Grindrod argues meaningful *linguistic* usage via inherited public-language content without the model being a source of *mental* intentionality. All three reach a qualified-positive verdict by relocating "meaning" off the bare model-fixes-reference picture, but by three different routes (inferential role / Fregean sense / externalist metasemantics of public language). This makes the page a useful third in-repo articulation of the "yes, but not the way you'd assume" position.
- **[`source/bender-koller-2020-climbing`](bender-koller-2020-climbing.md).** Grindrod's "merely statistically plausible text" foil is the form-only-training worry Bender & Koller crystallize; his response is not to deny the form-only training but to argue the model inherits a *public* language whose items already carry content — a distinct reply from the octopus-thought-experiment debate, worth recording as another in-repo move against the form/meaning gap.

## What it can ground

- Citations for the **semantic / metasemantic** and **mental / linguistic metasemantics** distinctions, and for the position that the LLM meaningful-usage question is better posed at the *linguistic*-metasemantic level — as a published philosophical proposal (Grindrod 2024), not a result this project has reproduced.
- Citations for the specific argument that **linguistic intentionality's dependency on a pre-existing linguistic system** is what makes a positive verdict for LLM outputs available — i.e. the model inherits content from a public language rather than originating it.
- The framing that **failure of mental intentionality does not entail meaninglessness** of LLM outputs — a citable anti-deflation argument from the philosophy-of-language side.
- A worked in-repo instance of **Evans' naming practices** and **Millikan's teleosemantics** applied to LLMs (useful if a later finding needs to pin either externalist theory to the LLM case).

## What it cannot ground

- **Any empirical claim about any model.** The paper reports no experiments, probes, or measurements; its description of transformer internals (§2) is survey-level. It cannot serve as the `anchors:` resource for a claim or result — it is not a human-labeled resource (no treebank, sense inventory, acceptability norm, or annotation). Its role is philosophical framing and counterpoint.
- **A settled verdict that LLMs "understand" or have mental content.** Grindrod explicitly *denies* that LLMs are sources of *mental* intentionality, and his positive verdict is for *linguistic* meaningful usage, hedged on communicative intentions ("a great deal of further work will need to be done"). Do not cite it as establishing LLM understanding or mental content.
- **Anything about lexical gradience or Construction Grammar specifically.** The analysis stays at the level of word/sentence meaningful usage and metasemantic theory; it does not treat graded word sense, constructional form–meaning pairing, or acceptability methodology — the project's own probe-level questions.
- **The relational/between-agents axis.** The account is about a single model's relation to an inherited public language (an aggregation-style, model-and-its-corpus picture), not about meaning constituted between agents; it should not be cited on between-agent constitution.

## Known limits

- **Position paper, single author.** Peer-reviewed (*Synthese* is an established philosophy journal), so its standing is "published philosophical article"; the verdict is the author's argued position, not a consensus.
- **Survey-level model description.** §2's account of transformers/distributional semantics is general; the argument is not sensitive to architecture-level differences between specific models.
- **Verdict is conditional and hedged.** The positive result depends on accepting Evans' and/or Millikan's metasemantics and is explicitly left open on the role of communicative intentions; it should be reported with that conditionality intact.
- **Abstract version discrepancy (recorded above).** arXiv abs-page metadata says "LLaMa"; the accepted-version PDF says "Claude." Body quotes are all from the PDF; cite the PDF/published text as authoritative.
- **Published HTML not consulted.** Only the arXiv abs page and the accepted-version PDF were read; the Springer version of record behind the paywall was not. No page numbers are used as quote locators.

## Status in wanted.md

Listed in [`wanted.md`](../wanted.md) at P1 ("Grindrod, J. … 2024–25 monograph on LLMs and language … check actual title and pull intro + relevant chapters"). The backlog entry's tentative titles were not this paper; the actual on-point item is this *Synthese* 2024 article, now verified and catalogued. The wanted.md Grindrod entry should be updated to `RECEIVED` (this paper) by the orchestrating session — note that Grindrod's *Philosophical Studies* 2026 "Modelling Language using Large Language Models" and the *Communicating with AI* chapter (with J.D. Porter and Nat Hansen) remain separate, uncatalogued items if a later finding needs them.
