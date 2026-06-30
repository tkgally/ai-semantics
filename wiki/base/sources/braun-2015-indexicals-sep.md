---
type: source
id: braun-2015-indexicals-sep
title: "Braun, \"Indexicals\" (Stanford Encyclopedia of Philosophy) — Kaplan's character/content distinction and context-dependent reference"
authors:
  - Braun, David
year: 2015
venue: "The Stanford Encyclopedia of Philosophy (Spring 2024 Edition), Edward N. Zalta & Uri Nodelman (eds.)"
url: https://plato.stanford.edu/archives/spr2024/entries/indexicals/
access: open-access
meaning-senses:
  - referential
  - distributional
  - grounded
status: received
created: 2026-06-30
updated: 2026-06-30
links: []
---

# Braun 2015 — "Indexicals" (Stanford Encyclopedia of Philosophy)

## What it is

The Stanford Encyclopedia of Philosophy (SEP) survey entry on **indexicals**, by **David Braun** (University at Buffalo). First published Fri Sep 14, 2001; substantive revision Fri Jan 16, 2015 (Copyright © 2015 by David Braun). SEP is **open-access** (free to read, no paywall). It is a reference-quality survey of the semantics of indexical and demonstrative expressions — words whose reference shifts with the context of utterance — organized around **David Kaplan's** theory and its `character`/`content` distinction, with later sections on indexical belief and on alternatives/criticisms.

This is a philosophy-of-language source about **human language and the semantics of context-dependence**. It makes no claim about LLMs. The project uses it only as an a-priori interpretive frame; see *What it grounds*.

**Provenance.** All quotes below were verified verbatim against the dated archived edition (a frozen snapshot) at
`https://plato.stanford.edu/archives/spr2024/entries/indexicals/` (retrieved 2026-06-30). Section names are the locators; SEP entries are not paginated. The entry uses **typographic single quotes** (‘ ’) around mentioned expressions; these are reproduced as written. Italicized words in the original are marked with underscores. Author name, citation form, and the substantive-revision date were confirmed against the entry's header and "Author and Citation Information" page (`https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=indexicals`), which gives the preferred citation "Braun, David, "Indexicals", _The Stanford Encyclopedia of Philosophy_ ... ". The Spring 2024 archived edition carries the Jan 16, 2015 substantive-revision text.

## The typology it provides

### What an indexical is

The entry's opening characterization (Introduction):

> "An indexical is, roughly speaking, a linguistic expression whose reference can shift from context to context."

The paradigm cases it studies are a **grammatical** mix — pronouns, adverbs, adjectives (§1.1, "Some Further Examples of Indexicals, Some Terminology, and a Contrast with Ambiguity"):

> "The indexicals that philosophers have studied most are the pronouns ‘I’, ‘he’, ‘she’, ‘it’, ‘this’, and ‘that’; the adverbs ‘here’, ‘now’, ‘today’, ‘yesterday’, ‘tomorrow’, and ‘actually’; and the adjectives ‘my’, ‘his’, ‘her’, ‘present’, ‘past’, and ‘actual’."

### Kaplan's character / content distinction

The load-bearing distinction the project imports. From **§3.1 ("An Example (Again) and Kaplan's Distinctions")**:

> "Kaplan (1989a) proposes a distinction between two kinds of meaning, _character_ and _content_. The sentence ‘I am a philosopher’ has a single character, but has different contents with respect to different contexts. Kaplan usually identifies character with linguistic meaning, which is a kind of meaning fixed by linguistic convention."

So **character** is the standing, convention-fixed side of an indexical's meaning (one rule, identified with linguistic meaning); **content** is what the expression contributes at a particular context (it varies across contexts while the character stays fixed). Note the hedge — Kaplan "_usually_" identifies character with linguistic meaning — which the project carries forward rather than smoothing over.

### Content is fixed by the context of utterance

From **§3.2 ("Some Basics of Kaplan's Theory")** — content is relativized to a context, and a context is a structured object with an agent, a time, a location, and a world:

> "On Kaplan's (1989a) theory, indexicals have contents _in_, or _with respect to_, _contexts_. Each context has associated with it at least an agent, time, location, and possible world. The content of ‘I’ with respect to a context \(c\) is the agent of \(c\). The content of ‘here’ is the location of \(c\). The content of ‘now’ is the time of \(c\)."

### Character as a function from contexts to contents

From **§3.4 ("Character")** — character is formally a function on contexts:

> "Kaplan (1989a, p. 505) says that he represents the character of an expression with a function on contexts whose value at any context is the expression's content at that context."

and the worked case:

> "So the character of ‘I’ is a function on contexts whose value at any context \(c\) is the agent of \(c\)."

## What it grounds in this project (relevance)

This source supplies an **a-priori** semantic frame for a grammatical corner the project had not yet touched: **indexicality / deixis** (the meaning of ‘I’, ‘you’, ‘here’, ‘now’, ‘this’, ‘today’, …). Its specific use is to license a *structural* distinction the project's essay [`essay/indexical-character-learnable-content-supplied`](../../findings/essays/indexical-character-learnable-content-supplied.md) draws between the two halves of an indexical's meaning:

- **Character** is, in Kaplan's own telling here, "linguistic meaning … fixed by linguistic convention" (§3.1) — a standing rule, a function on contexts (§3.4). The essay argues this is the side of indexical meaning a distributional / next-token learner is *structurally suited* to acquire (see [`concept/distributional-meaning`](../concepts/distributional-meaning.md)): convention-fixed regularities over context **types** are exactly what such an objective models.
- **Content** is the value at *this* context — the agent/time/location/world of the context of utterance (§3.2). The essay argues that for a text-only model there is no such context it *occupies* (no live agent, clock-time, or location it is anchored to), so the content of an indexical can only be **supplied by the described context in the text**, never read off an occupied one. The essay *argues* this generalizes the project's [`essay/reference-as-premise-bound`](../../findings/essays/reference-as-premise-bound.md) diagnosis from referring expressions to the whole indexical apparatus — a structural argument at survey strength, not an extended finding.

The frame is a-priori: it tells the project where, in the architecture of indexical meaning, distributional comfort and grounding strain fall, *before* any probe. The essay owns that application.

**Honest bounds (these matter):**

1. **This is a survey of human-language semantics, not a claim about LLMs.** Braun's entry concerns the semantics of context-dependence for human speakers; it says nothing about machine systems. The project applies Kaplan's distinction as an interpretive frame only; the essay owns the application and makes **no human-vs-LLM empirical claim**.
2. **Survey strength, not primary.** The character/content distinction is Kaplan's (Kaplan 1989a, "Demonstratives"); this entry reports and organizes it. Kaplan's primary is **not** open-access and stays on the wish-list ([`wanted.md`](../wanted.md)); the distinction is therefore carried at *reliable-survey* strength, and the "character = linguistic meaning" identification is reported with Braun's own hedge ("_usually_").
3. **The Kaplanian factorization is itself contested in the literature.** The entry's later sections survey criticisms of Kaplan's theory and rival treatments (relativist and contextualist alternatives, the status of ‘actually’, complex demonstratives, quasi-indicators). The clean two-level character/content factorization is the *standard* frame the project leans on, not a settled theorem; cite it as a well-motivated a-priori frame.

## What it cannot ground

- Any claim that a particular model *computes* an indexical's character or content (vs. producing text consistent with one). The entry is about human-language semantics; the label-/text-consistency-is-not-mechanism caution lives in the findings pages, not here.
- Any human acceptability or human-meaning-judgment baseline — this is a survey article, not a human-anchored dataset; it provides no labeled resource.
- The empirical magnitude or direction of any model effect.

## Known limits

- A reference survey, not primary research: it reports and organizes the literature (Kaplan and successors), and where the field disagrees it says so rather than deciding. Treat the typology as a frame, not a verdict.
- The page-level citation "Kaplan (1989a, p. 505)" is Braun's citation to Kaplan's primary, reproduced here for fidelity; the project has not verified it against Kaplan's text (the primary is not in-repo and not OA).

## Status in wanted.md

New ingestion (2026-06-30). Author (David Braun), edition (Spring 2024 archived snapshot), and substantive-revision date (Fri Jan 16, 2015) verified; all body quotes verified verbatim against the archived edition URL recorded above. Open-access confirmed. **Kaplan 1989a ("Demonstratives") remains a wish-list primary** (not OA); see [`wanted.md`](../wanted.md).
