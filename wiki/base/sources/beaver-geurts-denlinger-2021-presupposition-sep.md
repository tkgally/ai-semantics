---
type: source
id: beaver-geurts-denlinger-2021-presupposition-sep
title: "Beaver, Geurts & Denlinger, \"Presupposition\" (Stanford Encyclopedia of Philosophy) — backgrounded content, triggers, and the projection diagnostic"
authors:
  - Beaver, David I.
  - Geurts, Bart
  - Denlinger, Kristie
year: 2021
venue: "The Stanford Encyclopedia of Philosophy (Fall 2024 Edition), Edward N. Zalta & Uri Nodelman (eds.)"
url: https://plato.stanford.edu/archives/fall2024/entries/presupposition/
access: open-access
meaning-senses:
  - inferential
  - distributional
status: received
created: 2026-07-01
updated: 2026-07-01
links: []
---

# Beaver, Geurts & Denlinger 2021 — "Presupposition" (Stanford Encyclopedia of Philosophy)

## What it is

The Stanford Encyclopedia of Philosophy (SEP) survey entry on **presupposition**, by **David I. Beaver** (University of Texas at Austin), **Bart Geurts** (Radboud University Nijmegen), and **Kristie Denlinger**. First published Fri Apr 1, 2011; substantive revision Thu Jan 7, 2021 (Copyright © 2021 by David I. Beaver, Bart Geurts, and Kristie Denlinger). SEP is **open-access** (free to read, no paywall). It is a reference-quality survey of **presupposition** — the family of linguistic phenomena in which a speaker marks some information as taken for granted rather than asserted — organized around the phenomenon's characterization (triggers, projection, cancellability), the Frege–Strawson tradition, pragmatic accounts, dynamic/local-context theories, accommodation, and open puzzles.

This is a philosophy-of-language / linguistic-semantics source about **human language**. It makes no claim about LLMs. The project uses it only as an a-priori interpretive frame and as the scoping source for a fresh grammatical corner; see *What it grounds*.

**Provenance.** All quotes below were verified verbatim against the dated archived edition (a frozen snapshot) at `https://plato.stanford.edu/archives/fall2024/entries/presupposition/` (retrieved 2026-07-01), whose body carries the Thu Jan 7, 2021 substantive-revision text. Section names are the locators; SEP entries are not paginated. The entry uses **typographic quotation marks** (" ") around mentioned expressions and an arrow (→) to display an inference from a sentence to its presupposition; these are reproduced as written, and italicized words in the original are marked with underscores. The full author list and preferred citation were confirmed against the entry's "Author and Citation Information" page (`https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=presupposition`), which gives the preferred citation "Beaver, David I., Bart Geurts, and Kristie Denlinger, 'Presupposition', _The Stanford Encyclopedia of Philosophy_ …"; the footer copyright line "Copyright © 2021 by David I. Beaver … Bart Geurts … Kristie Denlinger" was verified against the archived page directly, fixing the substantive-revision year at **2021** (hence this page's id/year).

## The typology it provides

### What presupposition is

The entry's own characterization (§1.1, "Introduction"):

> "We discuss presupposition, the phenomenon whereby speakers mark linguistically information as being taken for granted, rather than being part of the main propositional content of a speech act. Expressions and constructions carrying presuppositions are called "presupposition triggers", forming a large class including definites and factive verbs."

So a presupposition is **backgrounded** information — marked as taken for granted rather than asserted as the main point — and it is carried by identifiable **triggers**.

### The triggers it lists

From **§1.1 ("Introduction")** — "at least the following lexical classes and constructions are widely agreed to be presupposition triggers" — the entry gives a labelled list, each with an example sentence and the inference (→) it carries. Verbatim, in the entry's order:

> "_factives_ (Kiparsky and Kiparsky, 1970)
> Berlusconi knows that he is signing the end of Berlusconism.
> → Berlusconi is signing the end of Berlusconism.
> _aspectual verbs_ ("stop, continue") (Simons, 2001; Abusch, 2002; Lorenz, 1992)
> China has stopped stockpiling metals.
> → China used to stockpile metals."

and, continuing the same list:

> "_cleft sentences_ (Delin, 1995; Prince, 1986)
> It was Jesus who set me free.
> → Somebody set me free."

> "_definite descriptions_ (Strawson, 1950)
> The Prime Minister of Trinidad and Tobago stood up and wagged his finger.
> → Trinidad and Tobago have a (unique) prime minister."

The list continues with temporal clauses ("before", "after", "since"), manner adverbs, sortally restricted predicates ("bachelor"), quantifiers, names, and intonation (focus, contrast) — each with a comparable trigger → presupposition schema.

### The projection diagnostic

The load-bearing behavioral signature the project imports. From **§1.2 ("Projection")** — the presupposition, unlike the ordinary entailment, **survives embedding**. Given a base sentence (2) "It's the knave that stole the tarts", presuppositions (3) and ordinary entailments (4), the entry contrasts what survives when (2) is embedded under negation (5a), a conditional antecedent (5b), a question (5c), and modals (5d–e):

> "The hallmark of presuppositions, as well as the most thoroughly studied presuppositional phenomenon, is _projection_ (Langendoen and Savin, 1971)."

> "In all these examples, sentence (2) is embedded under various operators. What is notable is that whereas the statements in (4) do not follow from any of these embeddings (and would not be expected to follow according to classical logics), the presuppositions do follow. We say that the presuppositions are _projected_."

The embedding operators are enumerated in (5) with the entry's own labels — "(_negation_)", "(_antecedent of a conditional_)", "(_question_)", "(_possibility modal_)", "(_evidential modal, probability adverb_)", "(_belief operator_)". The entry names negation as the canonical test but warns to vary the embedding:

> "Projection from embeddings, especially negation, is standardly used as a diagnostic for presupposition (hence the term "negation test"). However it is important to try several types of embedding when testing for presupposition …"

And it is explicit that projection is defeasible, not absolute — the "projection problem" is exactly *when* presuppositions project and when they are cancelled (§1.3, "Cancellability"):

> "Presuppositions typically project, but often do not, and most of the empirical and theoretical work on presupposition since the 1970s has been taken up with the task of describing and explaining when presuppositions project, and when they don't."

## What it grounds in this project (relevance)

This source supplies an **a-priori** semantic frame for a grammatical corner the project has not yet worked: **presupposition and projection**. Its specific use is to license the scoping open-question [`open-question/presupposition-projection-corner`](../../findings/open-questions/presupposition-projection-corner.md), which sketches (does not run) a minimal-pair probe of whether a model treats a triggered presupposition as *surviving* an entailment-cancelling embedding (negation / question / conditional antecedent) while a matched ordinary entailment does not.

- The projection contrast is a clean **behavioral** wedge: the diagnostic is *survival under embedding*, a forced-choice or inference judgment, not a distributional similarity. It therefore falls under [`concept/inferential-meaning`](../concepts/inferential-meaning.md) (which inferences a construction licenses to and from) — and, because triggers have characteristic distributions a next-token learner is well suited to, it sits against the [`concept/distributional-meaning`](../concepts/distributional-meaning.md) null (a model may reproduce the trigger's *distribution* without treating its presupposition as projecting).
- The frame is a-priori: it tells the project *where* in the grammar the projection signature lives (a fixed inventory of triggers, a fixed set of entailment-cancelling environments) **before** any probe. The open-question owns the application and makes **no** human-vs-LLM empirical claim.

**Honest bounds (these matter):**

1. **This is a survey of human-language semantics, not a claim about LLMs.** The entry concerns presupposition for human speakers; it says nothing about machine systems. The project applies the projection diagnostic as an interpretive frame only.
2. **Survey strength, not primary.** The entry reports and organizes a large literature (Frege, Strawson, Karttunen, Stalnaker, Heim, van der Sandt, and others); the primaries are not in-repo. Carry the typology at *reliable-survey* strength.
3. **Theories of presupposition are themselves contested.** The entry surveys competing **semantic vs. pragmatic** accounts, dynamic/local-context and satisfaction theories, and accommodation, and is explicit that the **projection problem is unsettled** ("most of the empirical and theoretical work on presupposition since the 1970s has been taken up with … when presuppositions project, and when they don't", §1.3). The clean trigger/projection description is the *standard frame* the project leans on, not a settled theorem.
4. **Not a human anchor.** This is a survey article, not a human-annotated dataset; it provides no labeled resource and grounds no human acceptability or presupposition-judgment baseline.

## What it cannot ground

- Any claim that a particular model *computes* projection (vs. producing text consistent with a projected presupposition). The entry is about human-language semantics; the text-consistency-is-not-mechanism caution lives on the findings pages, not here.
- Any human presupposition/projection judgment baseline — no labeled resource is provided.
- The empirical magnitude or direction of any model effect; projection is itself defeasible in the source (§1.3), so even the human pattern is graded, not a clean survival-under-all-embeddings rule.

## Known limits

- A reference survey, not primary research: where the field disagrees (semantic vs. pragmatic presupposition, the projection problem, accommodation), it reports the disagreement rather than deciding it. Treat the typology as a frame, not a verdict.
- The bibliographic pointers accompanying each trigger (e.g. "Kiparsky and Kiparsky, 1970", "Strawson, 1950") are Beaver, Geurts & Denlinger's citations, reproduced for fidelity; the project has not verified them against those primaries (not in-repo, not necessarily OA).

## Status in wanted.md

New ingestion (2026-07-01). Authors (David I. Beaver, Bart Geurts, Kristie Denlinger), edition (Fall 2024 archived snapshot, carrying the Jan 7, 2021 substantive-revision text), and substantive-revision year (2021) verified against the entry header, the "Author and Citation Information" page, and the footer copyright line; all body quotes verified verbatim against the archived edition URL recorded above. Open-access confirmed. The primary sources the entry cites (Karttunen, Stalnaker, Heim, van der Sandt, Strawson, etc.) are **not** in-repo and are not added to the wish-list by this ingestion.
