---
type: source
id: davis-2024-implicature-sep
title: "Davis, \"Implicature\" (Stanford Encyclopedia of Philosophy) — scalar vs. conventional implicature and the what-is-said / what-is-implicated divide"
authors:
  - Davis, Wayne
year: 2024
venue: "The Stanford Encyclopedia of Philosophy (Fall 2025 Edition), Edward N. Zalta & Uri Nodelman (eds.)"
url: https://plato.stanford.edu/archives/fall2025/entries/implicature/
access: open-access
meaning-senses:
  - inferential
  - referential
status: received
created: 2026-06-21
updated: 2026-06-21
links: []
---

# Davis 2024 — "Implicature" (Stanford Encyclopedia of Philosophy)

## What it is

The Stanford Encyclopedia of Philosophy (SEP) survey entry on **implicature**, by **Wayne Davis** (Georgetown University). First published Fri May 6, 2005; substantive revision Wed Jan 10, 2024. SEP is **open-access** (free to read, no paywall). It is a reference-quality survey of Grice's notion of implicature: the gap between *what a speaker says* and *what the speaker thereby means or implies*, the species of that gap (conversational vs. conventional implicature, with generalized/scalar implicature as a sub-case), and the standard properties used to tell them apart (cancelability, calculability, and relation to entailment / truth-conditional content).

This is a philosophy-of-language / linguistics source about **human language and speakers' meaning**. It makes no claim about LLMs. The project uses it only as an a-priori interpretive frame; see *What it grounds*.

**Provenance.** All quotes below were verified verbatim against the dated archived edition (a frozen snapshot) at
`https://plato.stanford.edu/archives/fall2025/entries/implicature/` (retrieved 2026-06-21). Section names are the locators; SEP entries are not paginated. Italicized words in the original are marked with underscores. Author name and citation form confirmed against the entry's "Author and Citation Information" page (`https://plato.stanford.edu/cgi-bin/encyclopedia/archinfo.cgi?entry=implicature`), which gives the preferred citation "Davis, Wayne, "Implicature", _The Stanford Encyclopedia of Philosophy_ ... ". The Fall 2025 archived edition carries the same Jan 10, 2024 substantive-revision text as the live entry.

## The typology it provides

### What is said vs. what is implicated

Grice's foundational distinction: the truth-conditional content a speaker asserts (*what is said*) versus the further content the speaker conveys without asserting it (*what is implicated*).

**§1 Speaker Implicature — the technical terms:**

> "Grice introduced the technical terms _implicate_ and _implicature_ for the case in which what the speaker said is distinct from what the speaker thereby meant or implied."

The entry fixes a notational convention used throughout (and below): parentheses name sentences, brackets name what those sentences express.

**§2 Conversational and Conventional Implicature — the convention:**

> "We will use parentheses to refer to the sentences in an example like (3), and brackets to refer to what the sentences express. So (3c) is the sentence "Being brave follows from being English" and [3c] is the proposition that being brave follows from being English."

### Conversational implicature (including generalized / scalar)

Conversational implicatures are inferred from the speaker's observance of the Cooperative Principle and its maxims. The entry gives the standard diagnostics:

**Cancelability — §2:**

> "Following Grice (1975: 39), it is widely accepted that generalized conversational implicatures differ from semantic implicatures in being _cancelable,_ either explicitly or implicitly (contextually)."

**Not (in general) entailed by what is said — §2 (the load-bearing point):**

> "Whereas semantic implicatures are generally entailed by what is said, many believe that conversational implicatures cannot be."

The entry immediately qualifies this with a hedge worth keeping (the claim is "typically", and is itself contested):

> "As (1), (2), (5), and (6) illustrate, conversational implicatures are _typically_ not entailments. But exceptions have been noted."

**The scalar `some`/`all` case — §2.** The entry uses the existential `some` to illustrate a generalized (scalar) conversational implicature. Example (5) is presented as:

> "(5)
>
> a. Some athletes smoke.
>
> b. Not all athletes smoke."

and the upper-bounding implicate [5b] is shown to be **cancelable** — which (3a)'s conventional implicate [3c] is not:

> "Whereas (3a) cannot be asserted without implicating [3c], (5a) can be asserted without implicating [5b]. The speaker may do this explicitly by adding "Indeed, all do" after uttering "Some athletes smoke"."

So uttering "Some athletes smoke" generates the upper-bounding scalar implicature "Not all athletes smoke", but a speaker can cancel it ("Indeed, all do") without contradiction — the hallmark of a conversational, not semantic, implicature.

### Conventional implicature

Conventional implicatures are tied to the conventional (lexical) meaning of particular words rather than to conversational reasoning; in the standard telling they are *implied rather than said*, i.e. not part of the at-issue truth-conditional content. The entry's worked example is (3a) "The queen is English and therefore brave":

**§2 — implied rather than said:**

> "By using (3a) to say and mean [3a], speakers implicate [3c]. That is, by using (3a) to say and mean that the queen is English and therefore brave, speakers implicate that being brave follows from being English. They _imply_ rather than _say_ that being brave follows from being English."

**§2 — the trigger words:**

> "Other words "triggering" conventional implicatures are _but, even, too, still, yet, already, again, stop, start, know,_ and _regret_."

### Calculability (conversational implicature is worked out, not asserted)

The mark that distinguishes conversational implicature is that it can be *derived* from the Cooperative Principle plus the literal content and context — it is pragmatic inference, not a truth-conditional component of the sentence.

**§6 Gricean Theory:**

> "Conversational implicatures must be capable of being worked out."

> "To work out an implicature is to infer it in a specific way from the Cooperative Principle using particular facts about the meaning of the sentence uttered and the context of utterance."

## What it grounds in this project (relevance)

This source supplies an **a-priori** semantics/pragmatics typology of closed-class meaning — Davis's survey of what is *said* vs. what is *conversationally / conventionally implicated* — that the project's function-word swap line can use to **predict, rather than read off post hoc**, which closed-class swaps a *truth-conditional / entailment* instrument should register versus miss. The relevant in-repo work is the swap result [`result/function-word-swap-run-v2`](../../findings/results/function-word-swap-run-v2.md), its quantifier-reading refinement [`result/function-word-few-many-split`](../../findings/results/function-word-few-many-split.md), and the essay [`essay/function-words-not-one-category`](../../findings/essays/function-words-not-one-category.md); the underlying construct (truth-conditions vs. use) is owned by [`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md).

The frame is simple. A 3-way NLI instrument is a **truth-conditional / entailment** instrument: it tracks *what is said* (at-issue truth-conditional content), so by Davis's typology it should **register** a swap that changes at-issue content and should be **blind** to content whose force is carried by a *conversational (scalar) implicature*, since on the standard view "many believe that conversational implicatures cannot be" entailed by what is said (§2). This lines up with the empirical split:

- `some`→`every` (existential→universal) changes the **at-issue quantificational truth-conditions** of what is said. An entailment instrument should register it — and it does (strong, panel-consistent flips).
- `few`→`many` turns on the **upper bound** of the multal quantifier ("many, *but not all*"), which Davis classifies as a cancelable, generalized **scalar** conversational implicature, not an entailment. An entailment instrument has no obligation to register it — and the result is exactly the panel split [`result/function-word-few-many-split`](../../findings/results/function-word-few-many-split.md) reports: one model's labels behave as if the upper bound is in force (so "Many X → All X" contradicts), the others' as if only the lower bound is at-issue (so it is neutral). Davis's typology predicts *a priori* that this is the arm where a truth-conditional instrument can legitimately diverge, because the contested content here is implicature, not what-is-said.

**Honest bounds (these matter):**

1. **This is a typology about human language, not a claim about LLMs.** Davis's entry concerns speakers' meaning and the semantics/pragmatics interface. The project applies it as an interpretive frame only; the essay [`essay/function-words-not-one-category`](../../findings/essays/function-words-not-one-category.md) owns that application, and the swap results themselves are `internal-contrast-only` (within-/across-model contrasts, no human comparison). **Nothing on this page asserts any human-vs-LLM empirical claim** — it is a source summary.
2. **The typology is itself contested in places.** The entry repeatedly flags live debate ("many believe", "But exceptions have been noted"). The non-entailment of conversational implicature is the *standard* view Davis reports, not a settled theorem; the project should cite it as a well-motivated a-priori frame, not as ground truth about what entailment must do.
3. **Flag only (not resolved here): the `because`→`although` arm is not a pure implicature case.** Concessive `although` adds an implicature-like contrast/concession layer, but `because` also carries an **at-issue causal assertion** — so a strong flip on that arm is consistent with a truth-conditional change in *what is said*, and does not need the implicature frame to explain it. This page does not adjudicate where the concessive layer sits relative to truth-conditional content; it marks the case as mixed so the swap line does not over-read it as a clean implicature contrast.

## What it cannot ground

- Any claim about whether a particular model *computes* a scalar implicature (vs. merely producing labels consistent with one). The entry characterizes implicature in human language; the label-consistency-is-not-mechanism caution lives in the result pages, not here.
- Any human acceptability or human-meaning-judgment baseline for the swap arms — this is a survey article, not a human-anchored dataset; it provides no labeled resource.
- The empirical magnitude or direction of any model effect — those come from the run, not from Davis.

## Known limits

- A reference survey, not primary research: it reports and organizes the literature (Grice and successors), and where the field disagrees it says so rather than deciding. Treat the typology as a frame, not a verdict.
- One verbatim quote was **dropped for lack of a clean source sentence**: the orchestrator's brief asked for a single sentence stating that a conventional implicature's truth is a *precondition for proper assertion* but that the host sentence can be *true even when the implicature is false*. The entry does not present this as one verbatim sentence; the nearest verified text is "Because [3c] is false, on the other hand, the use of (3a) to make a statement is _infelicitous_ and _improper_ as well as misleading" (§2), which establishes infelicity-on-falsity but not the truth-while-implicature-false half. The verified say-vs-imply passage above (quote on (3a)) is used instead, which makes the conventional-implicature point — *implied rather than said* — without overstating the truth-conditional claim.

## Status in wanted.md

New ingestion (2026-06-21). Author (Wayne Davis), edition (Fall 2025 archived snapshot), and substantive-revision date (Wed Jan 10, 2024) verified; all body quotes verified verbatim against the archived edition URL recorded above. Open-access confirmed.
