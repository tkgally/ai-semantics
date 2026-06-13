---
type: source
id: milliere-buckner-2024-philosophical-intro-i
title: "A Philosophical Introduction to Language Models — Part I: Continuity with Classic Debates"
authors:
  - Millière, Raphaël
  - Buckner, Cameron
year: 2024
venue: arXiv 2401.03910 (preprint, January 2024; no journal reference listed on arXiv at fetch time)
arxiv: "2401.03910"
url: https://arxiv.org/abs/2401.03910
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
    target: concept/grounding
  - rel: refines
    target: concept/symbol-grounding-problem
  - rel: refines
    target: concept/deflationary-and-eliminativist-llm-meaning
  - rel: refines
    target: concept/compositionality
  - rel: refines
    target: concept/inferential-meaning
  - rel: refines
    target: concept/referential-meaning
---

# Millière & Buckner 2024 — A Philosophical Introduction to Language Models, Part I

## What it is

Two-author survey article (Raphaël Millière, Macquarie; Cameron Buckner, Houston): the first of two companion papers, posted to arXiv as 2401.03910 (v1, 2024-01-08 — the only version as of fetch). It is the standard map of the LLM-meaning disputes as *continuations* of classic debates in philosophy of cognitive science, AI, and linguistics: a technical primer on Transformer LLMs (§2), then five debate chapters (§3.1 compositionality, §3.2 nativism and language acquisition, §3.3 language understanding and grounding, §3.4 world models, §3.5 transmission of cultural knowledge), framed throughout by Block's "Blockhead" thought experiment taken as the null hypothesis to beat. The stance is deliberately non-partisan but opinionated: behavioral successes genuinely erode several long-held anti-connectionist predictions, yet behavioral evidence alone cannot settle the semantic questions — that requires the mechanistic methods deferred to Part II (arXiv 2405.03207, **not yet catalogued** in this repo). Queued in [`wanted.md`](../wanted.md) ("2025–2026 OA finds", P2) as "useful as a map, not an anchor" — this page catalogues it in exactly that role.

Provenance: title, authors, abstract, and submission history fetched from the arXiv abs page (https://arxiv.org/abs/2401.03910) on 2026-06-13. The arXiv-native HTML rendering (arxiv.org/html/2401.03910) returns 404; all verbatim text below — including the abstract — was instead verified character-for-character against the **ar5iv HTML rendering of v1** (https://ar5iv.labs.arxiv.org/html/2401.03910, LaTeXML build of 2024-02-27, fetched 2026-06-13), with section locators from that rendering's structure. Status: **received** (abstract + 7 section-level quotes verbatim-verified against the ar5iv rendering of arXiv v1, 2026-06-13).

## Abstract (verbatim, ar5iv rendering of v1)

> "Large language models like GPT-4 have achieved remarkable proficiency in a broad spectrum of language-based tasks, some of which are traditionally associated with hallmarks of human intelligence. This has prompted ongoing disagreements about the extent to which we can meaningfully ascribe any kind of linguistic or cognitive competence to language models. Such questions have deep philosophical roots, echoing longstanding debates about the status of artificial neural networks as cognitive models. This article–the first part of two companion papers–serves both as a primer on language models for philosophers, and as an opinionated survey of their significance in relation to classic debates in the philosophy cognitive science, artificial intelligence, and linguistics. We cover topics such as compositionality, language acquisition, semantic competence, grounding, world models, and the transmission of cultural knowledge. We argue that the success of language models challenges several long-held assumptions about artificial neural networks. However, we also highlight the need for further empirical investigation to better understand their internal mechanisms. This sets the stage for the companion paper (Part II), which turns to novel empirical methods for probing the inner workings of language models, and new philosophical questions prompted by their latest developments."

(The phrase "the philosophy cognitive science" is as in the source — both the abs page and the ar5iv rendering carry it; the abs page renders the dashes as `--`.)

## Summary of the argument

1. **Null hypothesis (§1, §4).** The skeptical position — LLMs as sophisticated mimics, Blockhead-style lookup — is treated as the null; the paper asks what evidence could reject it, and concludes the rejection cannot be completed behaviorally.
2. **Compositionality (§3.1).** The Fodor–Pylyshyn dilemma (ANNs either fail at systematicity or merely implement a classical architecture) is re-run against Transformer results on SCAN/CFQ/COGS, meta-learning (Lake & Baroni 2023), and Smolensky's continuity principle: compositional generalization without built-in rules now looks achievable, but whether that is implementation of a language of thought or a non-classical alternative is left open — behavioral evidence cannot arbitrate.
3. **Understanding and grounding (§3.3).** The chapter disentangles three skeptical strands — the Bender–Koller form-only argument, the Harnad grounding problem extended to vector representations, and the missing-communicative-intentions worry — then deliberately drops the word "understanding" for Marconi's split of semantic competence into **inferential** and **referential** aspects. Verdict: substantial inferential competence is plausible (the Piantadosi–Hill conceptual-role line); referential competence is "more controversial" but externalism (Putnam/Kripke, via Mandelkern & Linzen) opens a route through causal chains in the training corpus, and RLHF may supply world-involving functions (Mollo & Millière 2023). Communicative intentions remain the weakest link.
4. **World models (§3.4).** Whether next-token predictors represent world dynamics is empirically open; Andreas's compression argument says efficient prediction may force encoding of the latent variables (beliefs, intentions, situations) that generated the text; the cleanest existence proofs (board-game toy models) are deferred to Part II.
5. **Cultural transmission (§3.5).** Tomasello's ratchet: LLMs show local-to-broad task generalization but their participation in cumulative cultural learning would require the communicative intentions and causal world models the earlier sections found wanting.

## Key passages (verbatim, section locators from the ar5iv rendering of v1)

**§3.3 Language understanding and grounding — the Bender–Koller argument as the authors reconstruct it:**

> "Since, on their view, meaning cannot be learned from linguistic form alone, it follows that language models are constitutively unable to grasp the meaning of language."

**§3.3 — the deflationary slogan, stated to be examined:**

> "On this view, LLMs are mere “stochastic parrots” haphazardly regurgitating linguistic strings without grasping what they mean"

— citing Bender et al. 2021; a footnote there wryly notes that actual parrots are sophisticated learners, "not merely parrots in this sense."

**§3.3 — the chapter's key reframing, from "understanding" to two-component semantic competence:**

> "Following Marconi (1997), we can further distinguish between inferential and referential aspects of semantic competence."

**§3.3 — the externalist route to reference for text-only models:**

> "Indeed, if reference can be determined by a word’s history of use within a linguistic community, then LLMs may inherit referential abilities by being appropriately linked to the causal chain of meaningful word use reflected in their training data."

**§3.3 — where the skeptic keeps the strongest card (communicative intentions):**

> "LLMs arguably do not mean to communicate anything, in the sense that they lack stable intentions to convey meaning to particular audiences with linguistic utterances, driven by broader intrinsic goals and agential autonomy."

**§3.1 Compositionality — the verdict on the classicist challenge:**

> "The achievements of Transformer models on compositional generalization benchmarks provide tentative evidence that built-in rigid compositional rules may not be needed to emulate the structure-sensitive operations of cognition."

**§3.4 World models — the Andreas compression argument for latent world/author variables:**

> "The most efficient compression of these texts may involve encoding values of the hidden variables that generated them: namely, the syntactic knowledge, semantic beliefs, and communicative intentions of the text’s human author(s)."

(Note on rendering: quotes preserve the ar5iv typography — curly quotes and apostrophes, unspaced en dashes for the LaTeX `--`; citation parentheticals inside quoted sentences are reported in prose rather than quoted, as elsewhere in this repo.)

## Bearing on this project

- **[`concept/grounding`](../concepts/grounding.md) and [`source/bender-koller-2020-climbing`](bender-koller-2020-climbing.md).** §3.3 is the most careful published taxonomy of the form-vs-meaning dispute the project has in-repo: it separates the Bender–Koller constitutive argument, the Harnad grounding problem, and the communicative-intentions worry into three distinct skeptical strands that the slogan "no understanding" runs together. Findings that engage the octopus argument can cite this decomposition rather than re-deriving it.
- **[`concept/symbol-grounding-problem`](../concepts/symbol-grounding-problem.md) and [`source/harnad-1990-symbol-grounding`](harnad-1990-symbol-grounding.md).** The paper explicitly extends Harnad's problem from discrete symbols to vector representations ("an analogous problem arises for modern LLMs trained on text only" — §3.3, the sentence continuing with a citation of Mollo & Millière 2023) and canvasses the RLHF world-involving-functions reply — a published bridge between the classic statement and the LLM case, complementing the gradualist picture in [`source/lyre-2024-semantic-grounding`](lyre-2024-semantic-grounding.md).
- **[`concept/deflationary-and-eliminativist-llm-meaning`](../concepts/deflationary-and-eliminativist-llm-meaning.md).** The "stochastic parrots" position is stated, sourced (Bender et al. 2021 — still not itself in-repo; see [`wanted.md`](../wanted.md)), and treated as a serious null hypothesis rather than a straw man; the Blockhead framing gives the deflationary pole a second canonical form (lookup-table mimicry) distinct from the parroting form.
- **[`concept/compositionality`](../concepts/compositionality.md).** §3.1 updates the Fodor–Pylyshyn dilemma against current evidence (SCAN/COGS, meta-learning, the continuity principle) and states the residual underdetermination — implementational vs. revisionist connectionism — that behavioral results cannot resolve. This is the citable current state of exactly the debate that concept page maps.
- **[`concept/inferential-meaning`](../concepts/inferential-meaning.md) and [`concept/referential-meaning`](../concepts/referential-meaning.md).** Marconi's inferential/referential split of semantic competence is the published analogue of the boundary this project's `inferential` vs. `referential` tags draw (see [`meaning-senses.md`](../../meaning-senses.md)); the paper's verdict structure — inferential competence plausible via conceptual-role considerations ([`source/piantadosi-hill-2022-meaning-without-reference`](piantadosi-hill-2022-meaning-without-reference.md) is its named exhibit), referential competence contested but externalism-permeable — is a map the project's findings can locate themselves on.
- **Communicative intentions and the relational axis.** §3.3's closing discussion (no stable, hierarchical, rationally integrated intentions; session-to-session inconsistency; the GPT-4/TaskRabbit anecdote as a possible limit case) bears on the `relational` axis as the strongest *skeptical* statement in-repo about model-side participation in communication — useful as the foil position for the relational program, though it is argument, not data.

## What it can ground

- Citations for the historical-continuity framing: each LLM-meaning dispute (form-vs-meaning, grounding, compositionality, world models) as the continuation of a named classic debate, with the original positions and current evidence laid out.
- The three-way decomposition of the "no understanding" criticism (form-only learning; ungrounded representations; absent communicative intentions) and the Marconi inferential/referential split as a citable alternative to the word "understanding."
- The stated underdetermination results: behavioral evidence alone settles neither the compositionality dilemma (§3.1) nor the world-model question (§3.4) — a published warrant for this project's insistence on anchored, operationalized probes over verdict-level claims.

## What it cannot ground

- Any empirical claim about any model: it is a survey; every empirical result it reports (SCAN, COGS, Lake & Baroni 2023, Wang et al. 2023, the TaskRabbit anecdote) belongs to the cited primary work, which would need its own source page before a finding leans on it.
- A positive verdict that LLMs have referential competence, grounded representations, or world models — the paper deliberately leaves all three open pending the mechanistic evidence of Part II.
- Claims about lexical gradience or constructional form–meaning pairing: the survey does not treat Construction Grammar, graded sense structure, or acceptability-judgment methodology at all.

## Known limits

- A survey/primer, explicitly "opinionated": its framings (Blockhead as null hypothesis, Marconi's split) are choices, not consensus; cite them as the authors' framing.
- Preprint only as of fetch (v1, 2024-01-08; no journal reference on arXiv); the abstract carries an uncorrected typo ("the philosophy cognitive science"), confirming light copyediting.
- January 2024 vintage: pre-dates the 2024–2026 empirical literature this project also tracks (e.g. the convention-emergence and VLM-dyad work); its empirical citations stop at late 2023.
- Part II (arXiv 2405.03207) — the mechanistic-interpretability half, where the existence proofs for world models and the novel philosophical questions live — remains in the backlog, not yet catalogued; conclusions deferred there should not be cited from this page.
- Only the ar5iv LaTeXML rendering of v1 was read; the PDF was not consulted, so no PDF page numbers are used as locators.

## Status in wanted.md

Listed in [`wanted.md`](../wanted.md) under "2025–2026 OA finds" at P2 ("the standard survey connecting LLM-meaning disputes to the classic debates the project's concept pages characterize; useful as a map, not an anchor" — only the landing page had been seen as of 2026-06-12). Catalogued 2026-06-13; the wanted.md entry is flipped to `RECEIVED` in the same wave. Part II is not yet a wanted.md entry of its own; it stays in the backlog via this page's Known limits note.
