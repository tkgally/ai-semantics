---
type: source
id: milliere-buckner-2024-philosophical-intro-ii
title: "A Philosophical Introduction to Language Models — Part II: The Way Forward"
authors:
  - Millière, Raphaël
  - Buckner, Cameron
year: 2024
venue: arXiv 2405.03207 (preprint, May 2024; no journal reference listed on arXiv at fetch time)
arxiv: "2405.03207"
url: https://arxiv.org/abs/2405.03207
access: open-access
meaning-senses:
  - grounded
  - referential
  - inferential
status: received
created: 2026-06-13
updated: 2026-06-13
links:
  - rel: refines
    target: source/milliere-buckner-2024-philosophical-intro-i
  - rel: refines
    target: concept/grounding
  - rel: refines
    target: concept/compositionality
  - rel: refines
    target: concept/deflationary-and-eliminativist-llm-meaning
---

# Millière & Buckner 2024 — A Philosophical Introduction to Language Models, Part II

## What it is

Two-author survey article (Raphaël Millière, Macquarie; Cameron Buckner, Houston): the **second** of two companion papers, posted to arXiv as 2405.03207 (v1, 2024-05-06 — the only version as of fetch). Where Part I ([`source/milliere-buckner-2024-philosophical-intro-i`](milliere-buckner-2024-philosophical-intro-i.md)) maps the LLM-meaning disputes as *continuations* of classic debates and concludes that behavioral evidence alone cannot settle the semantic questions, Part II is "the way forward": it turns to the **mechanistic** methods Part I deferred and to the **newer** philosophical questions the latest systems raise. The spine is two big chapters plus a closing one: §2 *Mechanistic understanding and intervention methods* (why benchmarks under-determine the constructs they target, what mechanistic explanation and intervention buy, and mechanistic interpretability through three case studies — induction heads, modular addition, and world models / Othello-GPT), §3 *Newer philosophical questions* (§3.1 modular architectures — multimodality and 'agent' systems; §3.2 consciousness; §3.3 secrecy and the reproducibility crisis), and §4 *The status of LLMs as cognitive models*, which returns to the two-paper opening question — are LLMs more than approximate lookup tables? — and answers it "broadly negative" (i.e. they are *more* than lookup tables), with qualifications. The stance, as in Part I, is non-partisan but opinionated: the case-study evidence pushes past the Blockhead null, yet the authors keep the open questions open (notably consciousness, where fluent self-report is held to be no evidence at all).

Provenance: title, authors, submission history, and abstract fetched from the arXiv abs page (https://arxiv.org/abs/2405.03207) on 2026-06-13. The arXiv-native HTML (arxiv.org/html/2405.03207v1) and the WebFetch summarizer both truncate the long body, so all verbatim body text below — including the section locators — was extracted character-for-character from the **ar5iv HTML rendering of v1** (https://ar5iv.labs.arxiv.org/html/2405.03207, fetched and parsed locally 2026-06-13), with section locators from that rendering's structure. Status: **received** (abstract from the abs page; 8 section-level quotes verbatim-verified against the ar5iv rendering of arXiv v1, 2026-06-13).

## Abstract (verbatim, arXiv abs page)

> "In this paper, the second of two companion pieces, we explore novel philosophical questions raised by recent progress in large language models (LLMs) that go beyond the classical debates covered in the first part. We focus particularly on issues related to interpretability, examining evidence from causal intervention methods about the nature of LLMs' internal representations and computations. We also discuss the implications of multimodal and modular extensions of LLMs, recent debates about whether such systems may meet minimal criteria for consciousness, and concerns about secrecy and reproducibility in LLM research. Finally, we discuss whether LLM-like systems may be relevant to modeling aspects of human cognition, if their architectural characteristics and learning scenario are adequately constrained."

(The abstract above is the abs-page text; the ar5iv rendering carries the same wording.)

## Summary of the argument

1. **Benchmarks under-determine constructs (§2.1).** Saturating a benchmark is not, by itself, evidence that a model has the underlying ability the benchmark was meant to measure — the construct-validity gap is the motivation for going mechanistic.
2. **Mechanistic interpretability (§2.2–§2.5).** The proposal is to reverse-engineer internal computations into human-intelligible functional modules at Marr's algorithmic level, illustrated by three case studies: induction heads (§2.5.1), modular addition (§2.5.2), and world models (§2.5.3).
3. **World models via causal intervention (§2.5.3).** The Othello-GPT line is the cleanest existence proof deferred from Part I: a linearly decodable, *causally efficacious* board-state representation, read as support for the linear representation hypothesis — though the authors flag that generalizing this to full LLMs (e.g. GPT-4) remains "sorely lacking."
4. **Newer questions (§3).** Multimodal and modular/agent extensions (§3.1) reframe the LLM as one component of a larger architecture rather than the whole cognitive story; consciousness (§3.2) is treated as a live but unsettled question on which fluent self-report carries no evidential weight; secrecy and non-released weights (§3.3) are flagged as a reproducibility threat to the whole interpretability program.
5. **LLMs as cognitive models (§4).** The closing chapter returns to the two-paper framing question and gives a qualifiedly negative answer to the lookup-table hypothesis — LLMs *do* induce complex mechanisms — while conditioning their relevance as cognitive models on adequately constrained architecture and learning scenario.

## Key passages (verbatim, section locators from the ar5iv rendering of v1)

**§2.1 The trouble with benchmarks — why saturation is not the construct:**

> "However, such success is often marred by independent examples of obvious failures, suggesting that performance saturation is not reliable evidence that LLMs actually surpass humans on the cognitive ability or aptitude (the ‘target construct’) that the benchmark was designed to assess."

**§2.5 Mechanistic interpretability — what it is:**

> "Mechanistic interpretability refers to this concerted effort to reverse engineer the internal computations performed by artificial neural networks."

**§2.5 Mechanistic interpretability — its overarching goal:**

> "The overarching goal of mechanistic interpretability is to open up the ‘black box’ of neural networks by providing human-intelligible descriptions of the functional modules that drive the emergence of model behaviors."

**§2.5.3 Case study 3: World models — the linear representation hypothesis the Othello-GPT result is read as supporting:**

> "These findings align with the linear representation hypothesis, according to which high-level concepts or features are represented linearly as directions in a neural network’s activation space."

**§3.1.2 'Agent' systems — the LLM reframed as one component of a larger agent architecture:**

> "According to this frame, LLMs were an important breakthrough in making DNNs more compositional and in particular allowing them to tackle language-scaffolded effects in thought and action, but they are only one component in a full agent architecture."

**§3.2 Consciousness — fluent self-report is no evidence of experience:**

> "No matter how convincing their fluent mimicry of experience reports might be, it cannot be taken as prima facie evidence that they are conscious."

**§3.3 Secrecy and the reproducibility crisis — the call for a science of machine behavior, with the hard-won cautions of other behavioral sciences:**

> "Much like the brains of humans and animals, LLMs today are large, opaque, and produce strikingly sophisticated behavior; this has led some researchers to suggest that we need a new ‘science of machine behavior’ to develop appropriate instruments and methods of analysis to study them"

— the sentence continues with a citation of Rahwan et al. 2019.

**§4 The status of LLMs as cognitive models — the verdict on the two-paper framing question (lookup-table null):**

> "Our survey of behavioral and mechanistic evidence supports a broadly negative answer (with some qualifications)."

(Note on rendering: quotes preserve the ar5iv typography — curly quotes and apostrophes, spaced en dashes; citation parentheticals inside quoted sentences are reported in prose rather than quoted, as in the Part I page. The §3.3 quote ends just before its inline citation; the truncation is marked.)

## What it grounds / bears on

This is a survey/primer with **no empirical claims of its own** — every experimental result it reports (Othello-GPT and the linear-probe interventions, induction heads, modular addition, the agent architectures, the benchmark-saturation examples) belongs to the cited primary work, which would need its own source page before a finding leans on it. Its value here is as the *survey backbone* for several concept pages and as the published statement of the methodological turn the project itself takes.

- **[`source/milliere-buckner-2024-philosophical-intro-i`](milliere-buckner-2024-philosophical-intro-i.md).** This page completes the two-part survey: the questions Part I leaves open behaviorally (world models, the lookup-table null) are exactly the ones Part II addresses mechanistically. Cite the pair together when invoking either.
- **[`concept/compositionality`](../concepts/compositionality.md).** §4's framing ("LLMs were an important breakthrough in making DNNs more compositional … but they are only one component in a full agent architecture", §3.1.2) is the published current statement of where the compositionality debate has moved — from "can ANNs be compositional at all" toward "compositionality as one capability inside a larger agent picture."
- **[`concept/grounding`](../concepts/grounding.md).** §3.1.1 (multimodality) and the world-models case study (§2.5.3) are the mechanistic complement to Part I's grounding chapter: the existence-proof line for internal world structure that Part I deferred.
- **[`concept/deflationary-and-eliminativist-llm-meaning`](../concepts/deflationary-and-eliminativist-llm-meaning.md).** §4 restates the two-paper framing question — "Are LLMs more than approximate lookup tables?" — and answers the Blockhead/lookup-table null "broadly negative," i.e. the deflationary null is *not* upheld (with qualifications). This is the published verdict on exactly the deflationary pole that concept page maps; cite it as the authors' qualified, survey-level judgement, not as data.
- **Methodological warrant for anchored, mechanistic probes.** §2.1's construct-validity argument (benchmark saturation ≠ the target construct) is a citable published statement of precisely why this project prefers operationalized, anchored probes over verdict-level behavioral claims — and §3.3's secrecy/reproducibility caution (closed weights preclude interpretability by anyone outside the training team) bears on the project's own methods discipline.
- **Consciousness as out-of-scope-but-noted.** §3.2 is the most careful in-repo statement that fluent first-person report from an LLM is *no* prima facie evidence of experience; useful as the citable caution against over-reading model self-ascriptions, not as a positive or negative consciousness claim.

## Known limits

- A survey/primer, explicitly opinionated and the companion to Part I; its framings (Marr's levels for interpretability, the lookup-table question as the two-paper spine) are choices, not consensus.
- **No empirical claims of its own** — see "What it grounds / bears on." The Othello-GPT world-model result, in particular, is reported as the cleanest existence proof but is the cited primary authors' result; the survey itself flags that generalizing it to full state-of-the-art LLMs is "sorely lacking" (§2.5.3, footnote 8), so this page cannot be cited for a world-model claim about any deployed model.
- Preprint only as of fetch (v1, 2024-05-06; no journal reference on arXiv); May 2024 vintage, so its empirical citations stop in early 2024 and pre-date the 2024–2026 literature this project also tracks.
- Provenance caveat: the abstract is from the arXiv abs page; the body quotes are from the **ar5iv LaTeXML rendering of v1**, parsed locally (the arXiv-native HTML and the WebFetch summarizer both truncate this long paper). The PDF was not consulted, so **no PDF page numbers are used as locators** — locators are section/subsection numbers and titles from the ar5iv structure. The §3.3 secrecy quote is reported up to its inline citation only; a sentence first surfaced as footnote 8 of §2.5.3 (the closed-weights point) was not used as a standalone quote to avoid a footnote-vs-prose locator mismatch.
- Part I is already in-repo; with this page the two-part survey is fully catalogued. Conclusions internal to the cited primary work (the case studies) still require their own source pages before any finding relies on them.

## Status in wanted.md

Part II was not previously its own `wanted.md` entry — the Part I page carried it as a Known-limits backlog note ("the mechanistic-interpretability half … remains in the backlog, not yet catalogued"). This page discharges that note; with it, both halves of the Millière & Buckner survey are catalogued as `received`. As with Part I, the role is "useful as a map, not an anchor."
