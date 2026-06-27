---
type: source
id: janssen-zimmermann-montague-semantics-sep
title: "Janssen & Zimmermann, \"Montague Semantics\" (Stanford Encyclopedia of Philosophy) — compositionality as a syntax-to-semantics homomorphism, the model-theoretic/intensional core, and the rule-to-rule hypothesis"
authors:
  - Janssen, Theo M. V.
  - Zimmermann, Thomas Ede
year: 2025
venue: "The Stanford Encyclopedia of Philosophy (Spring 2025 Edition), Edward N. Zalta & Uri Nodelman (eds.)"
url: https://plato.stanford.edu/entries/montague-semantics/
access: open-access
meaning-senses:
  - referential
  - inferential
  - constructional
status: received
created: 2026-06-27
updated: 2026-06-27
links:
  - rel: depends-on
    target: concept/compositionality
  - rel: depends-on
    target: concept/truth-conditional-and-use-meaning
  - rel: depends-on
    target: source/frege-1892-sense-and-reference
  - rel: depends-on
    target: source/tarski-1944-semantic-conception-of-truth
  - rel: depends-on
    target: source/davidson-1967-truth-and-meaning
  - rel: depends-on
    target: source/lewis-1970-general-semantics
---

# Janssen & Zimmermann 2025 — "Montague Semantics" (Stanford Encyclopedia of Philosophy)

## What it is

The Stanford Encyclopedia of Philosophy (SEP) survey entry on **Montague semantics**, by **Theo M. V. Janssen** and **Thomas Ede Zimmermann**. First published Mon Nov 7, 2011; substantive revision Wed Feb 5, 2025. SEP is **open-access** (free to read, no paywall). It is a reference-quality survey of Richard Montague's program for the semantics of natural language: treating a fragment of a natural language as a formal language with a **model-theoretic, denotational** interpretation, built so that the meaning of a complex expression is computed from the meanings of its parts and their mode of syntactic combination — the **principle of compositionality** in its sharpest, algebraic form.

This is a philosophy-of-language / formal-semantics source about **human language**. It makes no claim about LLMs and provides no human-annotated dataset. The project uses it only as an a-priori interpretive frame; see *What it grounds*.

## Secondary source carrying primary locators (read this first)

This page summarizes the **SEP survey entry**, a *secondary* source. **All quotes below are reproduced as they appear in the SEP entry by Janssen & Zimmermann.** Most are the survey authors' own characterizing prose; a few are short primary quotations the survey itself embeds (e.g. the §1.1 "in my opinion ... no important theoretical difference" sentence is Montague's own words, quoted *by* the survey). Either way the project records them at *secondary* strength — at the strength of a reference survey reporting and selecting Montague, **not** as a primary ingestion of Montague's own texts. The primary texts the survey is about — above all Montague's **"The Proper Treatment of Quantification in Ordinary English" (PTQ, 1973)**, and the companion papers **"Universal Grammar" (1970, the survey's "Montague 1970c")** and **"English as a Formal Language" (1970)** — are book-/proceedings-walled and are **not in-repo**. So the syntax-to-semantics-homomorphism formulation, the model-theoretic core, and the rule-to-rule hypothesis are recorded here at the strength of *a reference survey reporting Montague*, with §-locators into the SEP entry, **not** at the strength of Montague's primary prose. This mirrors how the project has handled other SEP entries ([`source/davis-2024-implicature-sep`](davis-2024-implicature-sep.md), [`source/sennet-2021-ambiguity-sep`](sennet-2021-ambiguity-sep.md)) and Cruse-style secondary-only ingestions: the entry discharges the *characterization* gap, it does not stand in for the primary text.

This ingestion exists to discharge a gap flagged in two concept pages: both [`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md) (its *Honest gaps* section: "Only **Montague (PTQ 1973)** remains **not in-repo** of the truth-conditional lineage") and [`concept/compositionality`](../concepts/compositionality.md) (§1: the homomorphism-from-a-syntactic-algebra-to-a-semantic-algebra picture is attributed to "the Montague tradition ... *not in-repo; characterization*"). With this page, those references now rest on a citable in-repo source (the survey), though the *primary* PTQ text remains wanted.

## Provenance and what was verified

Author names (Theo M. V. Janssen and Thomas Ede Zimmermann), first-published date (Mon Nov 7, 2011), and substantive-revision date (Wed Feb 5, 2025) were read from the entry. The **ten key passages** below were fetched from the live entry (`https://plato.stanford.edu/entries/montague-semantics/`) and then **re-fetched from the dated Spring 2025 archived edition** (`https://plato.stanford.edu/archives/spr2025/entries/montague-semantics/`, a frozen independent URL) on 2026-06-27; **every sentence quoted below came back character-for-character identical across both URLs (double-fetch-confirmed).** SEP entries are not paginated; section numbers/names are the locators. The single-quote marks around `'rule-to-rule hypothesis'` are reproduced as they appear.

## Key passages (verbatim, double-fetch-confirmed)

### (a) Compositionality — the principle, and its algebraic (homomorphism) form

The principle, stated plainly (**§1.2 Basic Aspects**):

> "The meaning of a compound expression is a function of the meanings of its parts and of the way they are syntactically combined."

The sharp algebraic statement the [`concept/compositionality`](../concepts/compositionality.md) page attributes to the Montague tradition (**§3.2 Compositionality**):

> "Syntax is an algebra, semantics is an algebra, and meaning is a homomorphism between them"

### (b) The model-theoretic / denotational core

The aim of the semantics is truth-in-a-model and entailment (**§1.1 Background**):

> "The basic aim of semantics is to characterize the notion of a true sentence (under a given interpretation) and of entailment"

Expressions interpreted as elements of a set-theoretic model (**§1.2 Basic Aspects**):

> "using constructions from set theory, a model is defined, and that natural language expressions are interpreted as elements (or sets, or functions) in this universe."

Entailment defined over all models (**§1.2 Basic Aspects**):

> "Sentence A entails sentence B if in all models in which the interpretation of A is true, also the interpretation of B is true."

Montague's own methodological identification of natural language with a formal language — the first sentence is **Montague's own words, quoted in the survey**; the second is the **survey authors' gloss** (**§1.1 Background**):

> "There is in my opinion no important theoretical difference between natural languages and the artificial languages of logicians"

> "Montague held the view that natural language was a formal language very much in the same sense as predicate logic was a formal language. As such, in Montague's view, the study of natural language belonged to mathematics, and not to psychology"

### (c) The rule-to-rule / syntax–semantics correspondence

The pairing of each syntactic rule with a semantic rule (**§1.2 Basic Aspects**):

> "each syntactic rule must be accompanied by a semantic rule which says how the meaning of the compound is obtained."

Named as the "rule-to-rule hypothesis" (**§2.3 Logic and Translation**):

> "For each syntactic construction (operation plus rule, in the terminology of Montague 1970c) there is a semantic rule that combines the corresponding representations of the meanings. Bach (1976) aptly called this interpretive strategy the 'rule-to-rule hypothesis'."

### (d) Contrast with use-based / pragmatic pictures — what the program brackets

Context-dependence assigned to pragmatics, kept out of the truth-conditional core (**§3.4 Pragmatics**):

> "Montague (1970c, 68) followed Bar-Hillel 1954 in treating context dependence as part of pragmatics."

The §1.1 "mathematics, not psychology" passage quoted above is the other half of this contrast: Montague's program locates meaning in a *world-relation* (truth-in-a-model), not in patterns of use or speaker psychology — the truth-conditional pole of [`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md).

## What it grounds in this project (relevance)

- **[`concept/compositionality`](../concepts/compositionality.md) — the principal connection.** §1 of that page describes the "homomorphism from a syntactic algebra to a semantic algebra" with the Montague tradition marked *not in-repo; characterization*. This source supplies the citable, open-access statement of exactly that: the plain principle (§1.2), the homomorphism formulation (§3.2), and the rule-to-rule pairing (§1.2, §2.3). The concept page's *productivity/systematicity* motivation is already in-repo via Davidson's finitude argument; the Montague entry adds the algebraic engine ("syntax is an algebra ... meaning is a homomorphism") the concept page's prose presupposes.
- **[`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md) — discharges the named Montague gap.** That page's *Honest gaps* records Frege, Tarski, Davidson, and Wittgenstein as in-repo and singles out Montague as the last not-in-repo leg of the truth-conditional lineage. This source removes the "no in-repo source at all" status for the Montague characterization: the model-theoretic core (§1.1, §1.2) and the natural-language-as-formal-language stance (§1.1) are now quotable with locators. **It does not replace the PTQ primary** (still wanted) — it is the survey, secondary-strength.
- **Sibling truth-conditional sources.** The entry sits with [`source/frege-1892-sense-and-reference`](frege-1892-sense-and-reference.md) (sense/reference, sentence-reference-as-truth-value), [`source/tarski-1944-semantic-conception-of-truth`](tarski-1944-semantic-conception-of-truth.md) (the truth-via-satisfaction recursion Montague's model theory presupposes), [`source/davidson-1967-truth-and-meaning`](davidson-1967-truth-and-meaning.md) (truth-conditions-as-meaning, finitude), and [`source/lewis-1970-general-semantics`](lewis-1970-general-semantics.md) (the contemporaneous categorial/intensional program). Montague completes the standard textbook lineage of the truth-conditional pole.

## What it cannot ground

- **Any empirical claim about LLMs.** A formal-semantics survey of human language, with no labeled resource — it cannot serve as the `anchors:` resource for any claim or result, and it bears on the *framing* of compositionality and the truth-conditional pole, not on any model behavior.
- **Montague's primary text.** The PTQ / "Universal Grammar" / "English as a Formal Language" primaries are not in-repo; this page carries the survey's characterization of them, not their own prose. Any claim needing Montague *verbatim* (rather than Janssen & Zimmermann reporting Montague) still requires the primary, which stays on the wanted backlog.
- **A verdict on whether LLM behavior is "compositional" in Montague's sense.** The entry defines compositionality for a formal fragment; whether a model's behavior realizes a homomorphism rather than a distributional shortcut is the project's own open question ([`concept/compositionality`](../concepts/compositionality.md) §4), not something this source settles.

## Known limits

- **A reference survey, not primary research, and secondary-only here.** It reports and organizes Montague's program (and its descendants); treat every quote as the survey's characterization, not Montague's own words.
- **No clean verbatim sentence on productivity/learnability *as a Montague achievement*.** The brief asked for systematicity/productivity/learnability text. The entry discusses learnability mainly in *critique* of an alternative (the §3.1 remark that a Fregean sense-hierarchy raises "serious learnability issues"), and does not state, in one clean verbatim sentence, that Montague semantics *solves* productivity or learnability. That motivation is therefore **not** quoted here as a Montague claim; the project's productivity/learnability grounding stays with Davidson's finitude argument ([`source/davidson-1967-truth-and-meaning`](davidson-1967-truth-and-meaning.md), p. 304), already in-repo and cited by [`concept/compositionality`](../concepts/compositionality.md) §1.
- **The use/distributional contrast is *implicit*, by what the program brackets.** The entry does not stage an explicit Montague-vs-use-theory or Montague-vs-distributional debate; the contrast is read off the §3.4 pragmatics passage (context-dependence pushed to pragmatics) and the §1.1 "mathematics, not psychology" stance. The §1.2 limitation noted by commentators — that "Montague only considered sentences in isolation" and "the sentence boundary was a serious limitation for the approach" — was returned by the live fetch but is **paraphrased, not quoted as double-confirmed verbatim** here (it was not part of the nine-sentence double-fetch verification set); it is reported as the survey's characterization only.

## Status in wanted.md

New ingestion (2026-06-27), discharging the Montague leg flagged in [`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md) and [`concept/compositionality`](../concepts/compositionality.md). Authors (Theo M. V. Janssen, Thomas Ede Zimmermann), edition (Spring 2025 archived snapshot), first-published (Mon Nov 7, 2011) and substantive-revision (Wed Feb 5, 2025) dates verified; the ten key quotes above are double-fetch-confirmed verbatim across the live and Spring-2025-archived URLs. Open-access confirmed. The **PTQ 1973 primary** (and the 1970 companion papers) remain **not in-repo** and stay on the backlog; this survey is secondary-strength and does not replace them.
