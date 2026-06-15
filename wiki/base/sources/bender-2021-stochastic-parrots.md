---
type: source
id: bender-2021-stochastic-parrots
title: "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?"
authors:
  - Bender, Emily M.
  - Gebru, Timnit
  - McMillan-Major, Angelina
  - Shmitchell, Shmargaret
year: 2021
venue: "FAccT '21: Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency, pp. 610–623"
doi: "10.1145/3442188.3445922"
url: https://dl.acm.org/doi/10.1145/3442188.3445922
access: open-access
license: "CC BY 4.0"
meaning-senses:
  - distributional
  - grounded
  - relational
status: received
created: 2026-06-15
updated: 2026-06-15
links:
  - rel: supports
    target: concept/deflationary-and-eliminativist-llm-meaning
---

# Bender, Gebru, McMillan-Major & Shmitchell 2021 — On the Dangers of Stochastic Parrots

## What it is

The FAccT '21 paper that coined the phrase **"stochastic parrot."** Four authors as listed on the paper (Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, Shmargaret Shmitchell — "Shmargaret Shmitchell" is widely understood as a pseudonym, the authorship entangled with Google's 2020 dismissal of Gebru; the other three names are the authors' own), published in the *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and Transparency*, pp. 610–623, DOI 10.1145/3442188.3445922, licensed CC BY 4.0. The paper is primarily a **risks-and-harms critique** of ever-larger language models: environmental and financial cost, the inscrutability of web-scale training data, encoded bias and a "hegemonic worldview," and the downstream harms of fluent-but-ungrounded text. Those sections (§2 cost, §3–5 data and bias) are **out of scope for this project** and are noted here only for completeness.

What *is* on-point for this project is **§6 "Stochastic Parrots"** — specifically §6.1 "Coherence in the Eye of the Beholder" — where the authors give the form-without-meaning argument that became the field's shorthand for the **eliminativist / deflationary reading** of "LLM meaning." Their claim is that an LM produces fluent text without any communicative intent or grounding, and that the apparent meaning is an artifact of *human* interpretation, not a property of the system: a *stochastic parrot*. This is the foil that [`concept/deflationary-and-eliminativist-llm-meaning`](../concepts/deflationary-and-eliminativist-llm-meaning.md) defines other positions against, and the slogan whose verbatim wording several in-repo sources reply to.

This is a **philosophical/critical position paper, not a human-annotated resource.** It reports no experiments, treebanks, or annotations; it cannot serve as an `anchors:` resource for any empirical claim. Its role is framing and counterpoint — the canonical statement of the eliminativist pole.

## Summary (the part that bears on this project)

The argument the project cares about is concentrated in §6.1:

1. **What an LM is, in their terms (§2).** An LM is a system trained on *string prediction* — predicting the likelihood of a token given its (preceding or surrounding) context. Nothing in that training signal is communicative intent.

2. **Coherence is in the eye of the beholder (§6.1).** Transformer LMs produce text that is "seemingly" fluent and coherent, but the authors stress *seemingly*: human coherence-judgement derives from recognizing interlocutors' beliefs and intentions in context, and we project that onto LM output even though the LM has no such states.

3. **LM text is not grounded in communicative intent (§6.1).** Because the training data never included "sharing thoughts with a listener," the text cannot be grounded in communicative intent, a model of the world, or a model of the reader's mind. The impression of meaning is "an illusion arising from our singular human understanding of language (independent of the model)."

4. **The "stochastic parrot" definition (§6.1).** The load-bearing sentence: an LM is "a system for haphazardly stitching together sequences of linguistic forms … according to probabilistic information about how they combine, but without any reference to meaning: a stochastic parrot."

The form/meaning structure here is the same one [`source/bender-koller-2020-climbing`](bender-koller-2020-climbing.md) states as a rigorous argument; this paper is the *slogan* form (Bender is a common author), and the concept page is careful to distinguish the rigorous in-principle argument (Bender & Koller) from the slogan (this paper).

## Key passages (verbatim, section locators from the CC BY 4.0 PDF)

**Abstract (opening framing):**

> "The past 3 years of work in NLP have been characterized by the development and deployment of ever larger language models, especially for English. BERT, its variants, GPT-2/3, and others, most recently Switch-C, have pushed the boundaries of the possible both through architectural innovations and through sheer size."

**§2 Background — what they mean by "language model":**

> "Similar to [14], we understand the term language model (LM) to refer to systems which are trained on string prediction tasks: that is, predicting the likelihood of a token (character, word or string) given either its preceding context or (in bidirectional and masked LMs) its surrounding context."

**§6.1 Coherence in the Eye of the Beholder — coherence is projected by the human reader:**

> "We say seemingly coherent because coherence is in fact in the eye of the beholder. Our human understanding of coherence derives from our ability to recognize interlocutors' beliefs [30, 31] and intentions [23, 33] within context [32]."

**§6.1 — LM text is not grounded in communicative intent:**

> "Text generated by an LM is not grounded in communicative intent, any model of the world, or any model of the reader's state of mind. It can't have been, because the training data never included sharing thoughts with a listener, nor does the machine have the ability to do that."

**§6.1 — the "stochastic parrot" definition (the load-bearing quote):**

> "Contrary to how it may seem when we observe its output, an LM is a system for haphazardly stitching together sequences of linguistic forms it has observed in its vast training data, according to probabilistic information about how they combine, but without any reference to meaning: a stochastic parrot."

**§6.1 — the meaning-as-illusion claim (the footnoted sentence just before the definition):**

> "The problem is, if one side of the communication does not have meaning, then the comprehension of the implicit meaning is an illusion arising from our singular human understanding of language (independent of the model)."

(The PDF renders apostrophes typographically (it's, can't, reader's); reproduced as in the source. Bracketed numerals like [14], [30, 31] are the paper's own in-text citation markers, reproduced verbatim. No page numbers are attached to the §6.1 quotes — the extraction was section-level; the article spans pp. 610–623 in the proceedings, and §6 falls around pp. 616–617 in that range, but the locators above are given as section headings to avoid asserting a page number not directly verified.)

## Provenance (what was fetched and what was verified)

Fetched via WebFetch on 2026-06-15 from the open-access mirror `https://s10251.pcdn.co/pdf/2021-bender-parrots.pdf` (a publicly mirrored copy of the FAccT '21 PDF; the paper is CC BY 4.0, license line "This work is licensed under a Creative Commons Attribution International 4.0 License." present in the PDF). The ACM version of record (`https://dl.acm.org/doi/10.1145/3442188.3445922`, and its epdf form) returned HTTP 403 to automated fetch and was not parsed directly; the DOI and pp. 610–623 pagination are from the ACM citation metadata and the PDF's own ACM Reference Format block. The PDF binary was saved by the harness and its text extracted locally with `pdfminer` (109,475 characters). **All six body quotes above were verified character-for-character against that extracted text**, with section locators from the paper's own numbered headings (§2 "BACKGROUND", §6 "STOCHASTIC PARROTS", §6.1 "Coherence in the Eye of the Beholder"). The famous definition wording matches the canonical citation exactly. No quote here is weaker than section-level; the only thing deliberately *not* asserted is a per-quote page number for the §6.1 passages (locators are section-level by choice, see note above).

## Bearing on this project

- **[`concept/deflationary-and-eliminativist-llm-meaning`](../concepts/deflationary-and-eliminativist-llm-meaning.md) — the principal connection.** This paper *is* the origin of the "stochastic parrot" slogan that names the eliminativist pole of that page's spectrum. It now backs, with the verbatim definition, the sentence that page previously carried as a characterization. Note the page's own careful distinction: the *slogan* (this paper) versus the *rigorous in-principle argument* (Bender & Koller 2020). The link is `supports` (it supplies the verbatim source for the eliminativist pole the page maps).
- **[`source/bender-koller-2020-climbing`](bender-koller-2020-climbing.md).** The two pair tightly (shared author): Bender & Koller give the argued form-only-training impossibility result; this paper gives the memorable slogan and the "coherence in the eye of the beholder" / "not grounded in communicative intent" framing. Cite Bender & Koller for the *argument*, this paper for the *phrase* and the projected-meaning point.
- **[`source/lyre-2024-semantic-grounding`](lyre-2024-semantic-grounding.md), [`source/piantadosi-hill-2022-meaning-without-reference`](piantadosi-hill-2022-meaning-without-reference.md), [`source/grindrod-2024-linguistic-intentionality`](grindrod-2024-linguistic-intentionality.md).** Each defines itself *against* the stochastic-parrot reading (Lyre: "neither stochastic parrots nor semantic zombies"; Piantadosi & Hill: against "claims that LLMs possess no meaning whatsoever"; Grindrod: against "merely clever prediction machines"). This page is the in-repo home of the position they push back on, so those replies can now cite the foil verbatim rather than by paraphrase.

## What it can ground

- The verbatim "stochastic parrot" definition, and the §6.1 form-without-meaning / coherence-in-the-eye-of-the-beholder / not-grounded-in-communicative-intent passages, as the canonical statement of the **eliminativist / slogan reading** the project's concept page maps — cited as one position in the debate, not as a result the project endorses.
- The authors' own minimal definition of "language model" (string prediction; §2), useful when a page needs a sourced statement of the deflationary "it's just next-token prediction" baseline.
- The point that apparent meaning in LM output can be a projection of the human interpreter — a citable framing for why the project installs the distributional structure as the *null to beat* rather than as evidence of meaning.

## What it cannot ground

- **Any empirical claim about any model.** No experiments, probes, or measurements; it cannot be an `anchors:` resource. Its force is rhetorical/critical and conceptual.
- **A settled verdict that LLMs have no meaning.** The project's stance is descriptivist ("describe, don't litigate"); this paper is the *eliminativist pole*, one bound of the axis the concept page declines to adjudicate. Cite it as that pole, not as the project's conclusion.
- **The rigorous in-principle argument.** That is Bender & Koller 2020's (the M ⊆ E × I relation, the octopus). This paper states the slogan and the projected-meaning point; do not attribute the formal impossibility result to it.
- **Anything about the project's own constructions, gradience, or methodology.** The paper predates and does not treat AANN, dative alternation, graded word sense, or acceptability methodology.

## Known limits

- **Critical position paper.** Peer-reviewed conference paper at a venue (FAccT) focused on fairness/accountability, not philosophy of language; its meaning-relevant content is §6.1, a few paragraphs, not a developed semantic theory. Report it as the influential *slogan* and its accompanying intuition, not as an argued metasemantics.
- **Section-level locators.** Quotes are pinned to section headings, not page numbers (provenance note above); the proceedings pagination pp. 610–623 is from citation metadata.
- **Scope mismatch.** Most of the paper is about environmental/financial cost, data documentation, and bias — out of scope here and not catalogued; only the §6 form-without-meaning material is summarized.

## Status in wanted.md

Listed in [`wanted.md`](../wanted.md) as "[P2] Bender, E.M., Gebru, T., McMillan-Major, A. & Shmitchell, S. 2021. 'On the Dangers of Stochastic Parrots.' FAccT." (status: wanted). Now `received`: section-level verbatim quotes verified locally from the CC BY 4.0 PDF (2026-06-15). The orchestrating session should flip that entry to received.
