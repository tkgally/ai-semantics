---
type: source
id: freiesleben-2026-construct-validity-llm-benchmarks
title: Establishing Construct Validity in LLM Capability Benchmarks Requires Nomological Networks
authors:
  - Freiesleben, Timo
year: 2026
venue: "arXiv:2603.15121v1 [cs.LG]"
url: https://arxiv.org/abs/2603.15121
access: open-access
meaning-senses:
  - measurement-epistemic
status: received
created: 2026-06-24
updated: 2026-07-06
links: []
---

# Freiesleben 2026 — Establishing Construct Validity in LLM Capability Benchmarks Requires Nomological Networks

## What it is

A single-author **philosophy-of-measurement / methodology position paper** (Timo Freiesleben, Munich Center for Mathematical Philosophy, LMU Munich), posted as arXiv:2603.15121v1 [cs.LG], submitted 16 March 2026. It asks which framework of **construct validity** machine-learning researchers should adopt when they attribute human-like capabilities — reasoning, theory of mind, morality — to large language models on the basis of **benchmark performance**, and argues that the **nomological-network account** of Cronbach & Meehl (1955) is the best available choice. It compares three rival accounts of construct validity — the **causal/realist** account (Borsboom 2004), the **inferential** account (Messick 1989, refined by Kane 2013), and the **nomological** account (Cronbach & Meehl 1955) — and concludes that the nomological account avoids the over-strong ontological commitments of the causal account while supplying a more substantive theory of construct meaning than the inferential account. It then works the implications through a concrete case (assessing reasoning in LLMs, via the Cattell–Horn–Carroll psychometric model).

This is a **theory/methodology + peer-positioning source, NOT a human-comparison anchor.** It reports no experiment, no model panel, and no human-labeled dataset; it is an argument about *how* LLM capability claims should be validated, not a measurement of any model. Its bearing on this project is twofold and methodological: it is (a) an independent peer who, in the LLM domain specifically, reaches the conclusion this project reconstructed from scratch — that **nomological-net construct validity is the right frame** for behavioral capability claims when no single accepted criterion is available; and (b) a citable *secondary* engagement with Messick's and Borsboom's accounts of validity, neither of which the project has ingested as a primary text. The match to the project's own discipline is unusually close: §3.1's "design nomological networks prior to benchmarks" rhymes with the project's *freeze-before-run* gate, and §3.4's treatment of theory–measurement conflict echoes Cronbach & Meehl's three-way charge of negative evidence that the project already leans on. The honest scope limits — preprint, single-author, secondary characterizations, no human anchor — are spelled out under "What it cannot ground" and "Known limits."

## Provenance

The body text was extracted from the **arXiv HTML rendering** of arXiv:2603.15121v1 (LaTeXML conversion) and the section structure read from its HTML table of contents. The abstract block is labelled **"Zusammenfassung"** in the HTML (the arXiv German LaTeX template), but the abstract text itself is in English; it is reproduced verbatim below. The HTML is **not paginated**, so **section headings are the quote locators**. Every quote below was matched character-for-character with `grep -F` against the extracted text before inclusion; the HTML strip collapses runs of whitespace, so quotes are reproduced with single spaces between words. The text preserves the source's typographic punctuation (curly quotation marks, the en-dash in "Duhem–Quine" and "theoretical–empirical"); these are reproduced as they appear. Inline citation markers that the strip left in the running text (e.g. `[ cronbach1955construct ]`, reference keys) are **omitted** from inside quoted spans; no bracketed reference key appears inside any quote below.

The **HTML body was complete**: all sections from §1 Introduction through §4 Conclusion (including §§2.1–2.3 and §§3.1–3.4) are present in the extracted text; nothing needed was missing, and nothing was dropped for lack of verification.

**Access / license honesty.** This is an **arXiv preprint**; the listed license is "arXiv.org perpetual non-exclusive license." **Peer-review status is unconfirmed** — treat it as a preprint, not a refereed publication. Corresponding author: timo.freiesleben@lmu.de (LMU Munich). Access recorded as `open-access` (arXiv).

## Section structure (verbatim headings, in order)

1. Introduction
2. The nomological account is the best available framework for conceptualizing LLM capabilities
   - 2.1 The causal account is ontologically demanding for LLMs
   - 2.2 The inferential account provides limited resources to theorize LLM capabilities
   - 2.3 Nomological Networks as a middle ground between causal realism and pure pragmatism
3. Implications of the nomological account for LLM benchmark design
   - 3.1 Researchers should design nomological networks prior to benchmarks
   - 3.2 Task benchmarks require empirical and theoretical validation
   - 3.3 Capability benchmarks should undergo convergent and discriminant analysis
   - 3.4 Resolving conflicts between theory and measurement is difficult
4. Conclusion

## Key passages (verbatim, with section locators)

**§"Zusammenfassung" (abstract) — the thesis and the three-way contrast:**

> "It contrasts three influential frameworks: the nomological account developed by Cronbach and Meehl, the inferential account proposed by Messick and refined by Kane, and Borsboom's causal account. I argue that the nomological account provides the most suitable foundation for current LLM capability research. It avoids the strong ontological commitments of the causal account while offering a more substantive framework for articulating construct meaning than the inferential account."

**§1 (Introduction) — the thesis restated as the §2 heading-claim, with the reasons against each rival:**

> "In this paper, I argue that the nomological account developed by Cronbach and Meehl provides the most suitable theoretical framework for current LLM capability research. Compared to Borsboom's causal account, it avoids strong ontological commitments about the real existence of constructs, commitments that are difficult to defend in the case of LLMs. Unlike the inferential account, it offers concrete guidance on how to theorize complex constructs."

**§2.1 ("The causal account is ontologically demanding for LLMs") — Borsboom's two conditions, as this paper characterizes them:**

> "For a measurement to validly measure a construct, two conditions must be satisfied: the construct must exist , and variations in measurement outcomes must be caused by variations in the state of that construct"

**§2.1 — why the realist stance is rejected for LLMs:**

> "For LLMs, however, this realist stance is difficult to defend. It is unclear what it would mean for a model to possess reasoning, theory of mind, or morality as internal attributes, rather than merely to exhibit behavioral patterns that resemble those associated with these constructs in humans."

**§2.2 ("The inferential account provides limited resources to theorize LLM capabilities") — how this paper characterizes the Messick/Kane account, and its central limitation:**

> "Rather than asking the ontological question whether a measurement is caused by a latent but real construct, they focus on the epistemological question whether inferences drawn from a measurement are warranted."

> "More importantly, the inferential account offers limited resources for even theorizing the construct. Because it focuses primarily on downstream inferences, the question of what exactly is being measured remains comparatively undertheorized."

**§2.2 — the paper's note that even an inferentialist (Kane) routes theoretical constructs through nomological networks:**

> "Kane distinguishes between observable attributes and theoretical constructs, noting that inferences about theoretical constructs typically require nomological networks (introduced in Section 2.3) as their theoretical foundation."

**§2.3 ("Nomological Networks as a middle ground between causal realism and pure pragmatism") — the relational definition of a construct:**

> "On this view, a construct is defined neither by its real-world referent, as in the causal account, nor by isolated inferential claims, as in the inferential account, but by its position within a coherent system of laws, correlations, and theoretical expectations."

**§2.3 — Borsboom's standing objection to the nomological account, quoted by this paper (a secondary quotation of Borsboom):**

> "He argues that this project is bound to fail because \"Few, if any, theoretical terms in psychology can be unambiguously identified in this way.\""

**§2.3 — the summary verdict (the "middle ground"):**

> "In sum, Cronbach and Meehl's nomological network account offers a compelling middle ground for LLM capability testing. It avoids Borsboom's strong realist commitments while preserving a substantive notion of construct meaning that goes beyond Messick and Kane's inferentialism."

**§3 (Implications, opening) — design the net before the benchmark:**

> "To prevent construct underrepresentation, the nomological account recommends first designing a nomological network before constructing any test."

**§3.3 ("Capability benchmarks should undergo convergent and discriminant analysis") — aggregation is not enough; the Campbell-&-Fiske-style vocabulary applied to benchmarks:**

> "Aggregation alone does not secure construct validity."

> "Convergent analysis checks whether reasoning scores correlate positively/negatively with theoretically related capabilities such as working memory. Discriminant analysis checks that reasoning scores are uncorrelated with capabilities that are theoretically distinct, such as social intelligence."

**§3.4 ("Resolving conflicts between theory and measurement is difficult") — the Duhem–Quine / three-way ambiguity of a theory–measurement mismatch:**

> "We are confronted with a version of the Duhem–Quine problem: as Simms puts it, it remains unclear whether \"(i) the measure does not adequately measure the target construct, (ii) the theory requires modification, or (iii) some combination of both.\""

**§3.4 — where the author thinks doubt should fall first in the LLM case:**

> "In the context of LLM research, I believe that initial doubt should often fall on the benchmarks."

**§4 (Conclusion) — the upshot the project shares:**

> "By embedding benchmarks within a theoretically articulated network of interrelated capabilities, we move from isolated performance scores to empirically constrained claims about LLM capabilities, as illustrated through the example of reasoning."

## What this grounds

- **An independent peer reaching this project's own conclusion, in the LLM domain specifically.** The project arrived, from scratch, at the position that with criterion-oriented validation removed by design, the only available form of validation for a behavioral probe is **nomological-net construct validity** (see [`source/cronbach-meehl-1955-construct-validity`](cronbach-meehl-1955-construct-validity.md) and [`essay/construct-validity-without-a-criterion`](../../findings/essays/construct-validity-without-a-criterion.md)). Freiesleben argues the same — that for "capabilities" attributed to LLMs from benchmark scores, Cronbach & Meehl's nomological account "provides the most suitable foundation," over both Borsboom's causal/realist account and the Messick/Kane inferential account. This is external corroboration of the project's *framing choice*, now made by a measurement philosopher writing about LLMs. It is a convergence of *direction*, not an empirical result the project can borrow.
- **A citable secondary engagement with Messick's and Borsboom's accounts** — two primary texts the project has *not* ingested. The page records this paper's characterizations: that Borsboom's causal account requires that "the construct must exist" and that measurement variation "must be caused by variations in the state of that construct"; that the Messick/Kane inferential account asks "whether inferences drawn from a measurement are warranted" rather than the ontological question, but "offers limited resources for even theorizing the construct." These are usable as **this paper's reading** of those accounts — a secondary source to cite when the project needs to situate its own position against the causal and inferential alternatives, **always flagged as Freiesleben's characterization**, never as a primary statement from Messick or Borsboom. (Messick has a parallel source page being created this same wave; the orchestrator will linkify the reference. Borsboom and Messick primaries remain uncatalogued wants.)
- **A benchmark-design rhyme with the project's freeze-before-run discipline.** §3.1's recommendation to "design a nomological network before constructing any test" is, structurally, the project's *freeze-the-instrument-before-the-run* gate transposed to benchmark design: fix the theoretical net of relations first, so that what the test measures is not chosen post hoc. §3.3's "convergent and discriminant analysis" imports the multitrait-style vocabulary (a construct earns its identity by correlating with its theoretical neighbors and *not* correlating with theoretically distinct constructs) into LLM benchmarking — useful framing for the project's discipline of locating a probe in a net of contrasts rather than certifying it against a single self-chosen standard.
- **A confirmation that the negative-evidence ambiguity is structural.** §3.4 frames a theory–measurement conflict as a Duhem–Quine problem — the mismatch may indict the measure, the theory, or both — which is the same three-way charge Cronbach & Meehl make in "Implications of Negative Evidence" and which the project already cites to refuse reading a single probe's null as instrument-invalidity. Freiesleben's added wrinkle (that for *LLM* benchmarks "initial doubt should often fall on the benchmarks," because ML benchmark design is immature) is his domain judgment, recorded as such, not a project commitment.

## What it cannot ground

- **Any claim about any model the project tests.** It reports no model panel, no benchmark run, and no measurement; it licenses no statement about claude-, gemini-, or gpt-class models, nor about any LLM's reasoning, theory of mind, or other capability. It is a methodology argument, not data.
- **A human-comparison anchor.** It contains no human-labeled dataset — no treebank, sense inventory, acceptability norm, or annotation — and so **cannot be an `anchors:` resource** for any claim or result. Its role is methodology/peer-positioning framing only; citing it does not discharge the human-anchor obligation on any empirical claim.
- **A primary statement of Messick's or Borsboom's views.** The page's renderings of the inferential and causal accounts are **this paper's secondary characterizations**. They must be cited as "Freiesleben's reading of Messick/Borsboom," never quoted as if from Messick or Borsboom themselves; the project has not read those primaries. The one direct Borsboom string here ("Few, if any, theoretical terms…", "correlations are not enough…") is a *quotation embedded in Freiesleben's text*, reproduced at that strength.
- **Anything about lexical or constructional meaning directly.** The paper is about validating capability constructs (reasoning, theory of mind) via benchmarks; it says nothing about word sense, form–meaning pairing, gradience, or Construction Grammar. Its bearing on the project is at the validity-methodology layer only.

## Known limits

- **arXiv preprint; peer-review status unconfirmed.** Cite as "Freiesleben 2026 (arXiv:2603.15121v1)," a preprint, not a refereed paper.
- **Single-author position paper.** It argues a thesis (nomological account is best for LLMs) and acknowledges live objections (Borsboom's "correlations are not enough"; the question of whether a human psychometric model such as Cattell–Horn–Carroll transfers to LLMs at all). It is one philosopher's considered position, not a consensus statement.
- **Its characterizations of Messick and Borsboom are secondary.** The project has not ingested Messick (1989/1995), Kane (2013), or Borsboom (2004/2005) as primary texts; treat the inferential- and causal-account descriptions as Freiesleben's reading until those primaries are read.
- **HTML-rendering extraction.** Quotes are taken from the LaTeXML HTML conversion and verified against the extracted text; locators are section headings (the HTML is unpaginated). The body was complete in the extraction, but a stray rendering artifact (e.g. the German template label "Zusammenfassung," `Section ˜ N` tildes, bracketed reference keys) appears around — never inside — the quoted spans.

## Status in wanted.md

Catalogued this session as a methodology / peer-positioning source for the project's construct-validity line — the LLM-domain companion to [`source/cronbach-meehl-1955-construct-validity`](cronbach-meehl-1955-construct-validity.md) and direct support for [`essay/construct-validity-without-a-criterion`](../../findings/essays/construct-validity-without-a-criterion.md). This subagent created only this page and edited no shared files; the orchestrating session should wire it into `wiki/index.md`, the relevant essay(s), and `wanted.md`, and linkify the Messick source page (created in parallel this wave). The **Messick (1989/1995), Kane (2013), and Borsboom (2004/2005)** primaries remain uncatalogued wants if a later finding needs them at primary strength.
