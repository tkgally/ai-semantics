---
type: source
id: pustejovsky-1991-generative-lexicon
title: "Pustejovsky, \"The Generative Lexicon\" (Computational Linguistics 17(4), 1991) — logical polysemy vs. contrastive (accidental) ambiguity, type coercion / logical metonymy, qualia structure, and why some senses are co-active (complementary) rather than rival (contrastive)"
authors:
  - Pustejovsky, James
year: 1991
venue: "Computational Linguistics 17 (4), 409–441 (1991)"
acl-anthology: J91-4003
url: https://aclanthology.org/J91-4003.pdf
access: open-access
meaning-senses:
  - distributional
  - referential
status: received
created: 2026-06-23
updated: 2026-06-23
links:
  - rel: supports
    target: concept/polysemy
  - rel: supports
    target: essay/layer-specialness-vs-always-resolvability
---

# Pustejovsky 1991 — "The Generative Lexicon"

## What it is

The 1991 *Computational Linguistics* article (vol. 17, no. 4, pp. 409–441) by **James Pustejovsky** (Computer Science Department, Brandeis University) — the founding statement of the **Generative Lexicon** (GL) program. It proposes that word senses should not be exhaustively *enumerated* in the lexicon but **generated** by a small set of mechanisms — **qualia structure** (the Constitutive, Formal, Telic, and Agentive roles of a lexical item), **type coercion**, and **cocompositionality** — operating over richly typed lexical entries. The paper is the canonical source for the linguistic distinction this project needs: **logical (regular, complementary) polysemy** — where senses are systematically related and can be *co-active* — versus **contrastive / accidental ambiguity (homonymy)** — where the readings are *rival* and exactly one is operative.

This is a source about **human language and its formal/computational representation**. It makes **no claim about LLMs** and supplies **no human-annotated dataset**. The project uses it only as an a-priori interpretive frame (see *What it grounds*).

**Open-access basis.** The verbatim text below was extracted from the ACL Anthology full-text PDF (`https://aclanthology.org/J91-4003.pdf`; ACL Anthology id `J91-4003`), which is openly and freely available. The PDF carries an embedded text layer (OCR of the original two-column print); page locators below are the **printed page numbers** read from the running heads of that PDF (even pages head "James Pustejovsky"; odd pages head "Computational Linguistics / Volume 17, Number 4").

## Why it bears on this project (the forced-both / co-predication gap)

The essay [`essay/layer-specialness-vs-always-resolvability`](../../findings/essays/layer-specialness-vs-always-resolvability.md) flags as its **weakest point** the distinction between a *genuinely-unresolvable / rival* lexical item (a balanced homonym, where one reading wins on resolution) and a *forced-both* case (pun / zeugma / co-predication, where two senses are *jointly required*). Its provenance note asks for "a future ingest of a semantics/lexicography source on regular/systematic polysemy, zeugma, and co-predication (the linguistic literature on 'logical polysemy' and the pun/zeugma diagnostics)." This source supplies the **theoretical backbone** of exactly that distinction:

- It names the **contrastive vs. complementary** axis (citing Weinreich 1972) and aligns it with **homonymy (accidental) vs. logical polysemy**.
- It treats logical polysemy as **systematic** and **generable by lexical rule** rather than listed, which is what makes the related senses *co-available* rather than *competing*.
- Its **qualia structure** for nouns like *novel* / *dictionary* (both `Form: book, disk`) is the GL machinery later used (in GL's 1995 book and the copredication literature it spawned) to explain why a single noun can host two senses (e.g. physical-object vs. informational-content) that a predicate can pick out — the *forced-both* / dot-object phenomenon.

A complementary in-repo ingest, [`source/falkum-vicente-2015-polysemy`](falkum-vicente-2015-polysemy.md), grounds the **regular/logical vs. irregular/accidental** carving from the survey side and records that logical polysemy is "operationally defined as polysemy which passes the **conjunction and anaphoric reference tests**" — i.e. the **copredication diagnostics**. This Pustejovsky source grounds the *generative mechanism* behind that carving and is itself the locus classicus that the Falkum & Vicente survey cites for it.

**Important honesty note on scope.** The *term* "copredication" and the explicit **dot-object / dot-type** apparatus are developed in Pustejovsky's later work (the 1995 book *The Generative Lexicon* and subsequent type-theoretic literature), **not in this 1991 article**. What the 1991 paper supplies is (a) the contrastive-vs-complementary / homonymy-vs-logical-polysemy distinction, (b) qualia structure and type coercion / logical metonymy, and (c) the *novel*/*dictionary* `book/disk` qualia that the dot-object account later builds on. The page below quotes only what the 1991 text actually says and flags the 1995 attributions as such.

## Provenance and what was verified

The bibliographic block (author, affiliation, venue *Computational Linguistics* 17(4), pp. 409–441) was read from the article header and running heads of the fetched PDF. The verbatim passages below were extracted from the embedded text layer of `https://aclanthology.org/J91-4003.pdf`. **Whitespace normalization (declared):** the source is a two-column print whose OCR text layer renders inter-word gaps as single-or-double spaces and inserts mid-sentence line breaks; every quote below has had runs of whitespace (spaces + newlines) collapsed to a single space and line-break hyphenation rejoined; **no words were added, removed, or reordered.** Example numbers, italics, and the asterisk-marked variable notation (`*x*`) are reproduced as they appear in the text layer.

## Key passages (verbatim, whitespace-normalized as declared)

**The ambiguity test, distinguishing homonymy/accidental from logical ambiguity, with the `bank` (river / financial institution) example (Section 2, p. 411):**

> "Test for the ambiguity of a word. Distinguish between homonymy and polysemy, (cf. Hirst 1987; Wilks 1975b); that is, from the accidental and logical aspects of ambiguity. For example, the homonymy between the two senses of bank in Example 6 is accidental."

with Example 6 (p. 411):

> "a. the bank of the river"
> "b. the richest bank in the city"

**The contrastive vs. complementary alignment (footnote 2, p. 411) — the load-bearing locator for the rival-vs-co-active axis:**

> "Cf. Weinreich (1972) distinguishes between contrastive and complementary polysemy, essentially covering this same distinction. See Section 4 for discussion."

**By contrast, the polysemous (complementary) `bank` — institution vs. building (Section 2, pp. 411–412):**

> "In contrast, the senses in Example 7 exhibit a polysemy (cf. Weinreich 1972; Lakoff 1987)."

with Example 7:

> "a. The bank raised its interest rates yesterday (i.e. the institution)."
> "b. The store is next to the new bank (i.e. the building)."

**Logical polysemy named as systematic and rule-explicable (Section 4, p. 415):**

> "Yet, something about the systematicity of such ambiguity suggests that a more general and simpler explanation should be possible. By relaxing the conditions on how the meaning of a complex expression is derived from its parts, I will, in fact, propose a very straightforward explanation for these cases of logical polysemy."

**Type coercion defined — the mechanism behind reference shift / logical metonymy (p. 423):**

> "Type Coercion: A semantic operation that converts an argument to the type that is expected by a function, where it would otherwise result in a type error."

**Logical metonymy, with the "Mary enjoyed the book" example (Example 33a, p. 423; analysis p. 424):**

> "a. Mary enjoyed the book."

> "In 33(a), the book is enjoyed only by virtue of some event or process that involves the book, performed by Mary. It might furthermore be reasonable to assume that the semantic structure of book specifies what the artifact is used for; i.e. reading. Such a coercion results in a word sense for the NP that I will call logical metonymy."

**Qualia structure carrying two co-present "aspects" of a noun — `novel` and `dictionary` both `Form: book, disk` (Examples 40–41, pp. 426–427):**

For *novel* (Example 40, p. 426):

> "Const: narrative(*x*)"
> "Form: book(*x*), disk(*x*)"
> "Telic: read(T,y,*x*)"
> "Agentive: artifact(*x*), write(T,z,*x*)"

with the gloss:

> "This structures our basic knowledge about the object: it is a narrative; typically in the form of a book; for the purpose of reading (whose event type is a transition); and is an artifact created by a transition event of writing."

For *dictionary* (Example 41, p. 427):

> "Form: book(*x*), disk(*x*)"

**Degrees of prototypicality / salience of a predication (Section, p. 432) — the gradience the project should carry forward:**

> "Both of these sentences are obviously well-formed syntactically, but there is a definite sense that the predication in 58(a) is "tighter" or more prototypical than that in 58(b)."

## What it grounds in this project (relevance)

- **[`essay/layer-specialness-vs-always-resolvability`](../../findings/essays/layer-specialness-vs-always-resolvability.md) — grounds the rival-vs-forced-both distinction the essay flagged as its weakest point.** The essay's "genuinely-unresolvable balanced homonym" (one reading operative on resolution) corresponds to Pustejovsky's **contrastive / accidental homonymy** (the *bank* river/institution case); its "forced-both" case (two senses jointly required) corresponds to the **complementary / logical-polysemy** pole, whose generative basis is qualia structure and type coercion. The source grounds the *framing* of this distinction (and supplies, in the qualia for *novel*/*dictionary*, the apparatus the later copredication / dot-object literature uses), **not** any empirical re-reading of model behavior.
- **[`concept/polysemy`](../concepts/polysemy.md) — adds the generative-lexicon account of logical (complementary) polysemy and the type-coercion mechanism.** It sharpens the page's "related senses" into "senses systematically related by lexical rule and co-encoded in qualia structure," and supplies the contrastive (homonymy) contrast pole. It complements [`source/falkum-vicente-2015-polysemy`](falkum-vicente-2015-polysemy.md), which gives the survey-level regular/irregular carving and the copredication-diagnostic definition (conjunction + anaphora tests) that this article's machinery underwrites.
- **A forthcoming forced-both operationalization decision.** When the project operationalizes "forced-both," this source is the principled basis for the *rival* (homonym; exactly one reading wins) vs. *co-active* (logical polysemy; both readings jointly required) contrast, and points (via Falkum & Vicente) to the **conjunction / anaphoric-reference (copredication) tests** as the operational diagnostic.

## What it cannot ground

- **Any empirical claim about LLMs.** A human-language / formal-semantics theory paper with no labeled resource. It cannot serve as the `anchors:` resource for any claim or result.
- **A graded measurement instrument.** It supplies the *conceptual* carving (contrastive vs. complementary; qualia; coercion) and notes that predication has "degrees of prototypicality," but it provides no human-rated scale or annotations.
- **The explicit copredication / dot-object diagnostics by name.** Those are developed in Pustejovsky's *later* work (GL 1995) and the subsequent type-theoretic literature; this 1991 article supplies the antecedent machinery (qualia, coercion, the contrastive/complementary distinction), not the dot-type formalism or the term "copredication" itself. Do not cite this page for the 1995 apparatus.

## Map/reference, not a human anchor

This page is a **reference/theory source**. It grounds *framing* — the contrastive (rival/homonymy) vs. complementary (co-active/logical-polysemy) distinction, qualia structure, and type coercion / logical metonymy — that the project's forced-both wedge and the layer-specialness essay presuppose. It makes **no empirical claim about LLMs**, supplies **no human-annotated resource**, and **cannot** serve as the `anchors:` resource for any claim or result.
