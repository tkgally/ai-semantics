---
type: source
id: lewis-1970-general-semantics
title: General Semantics
authors:
  - Lewis, David
year: 1970
venue: "Synthese 22(1–2), 1970, pp. 18–67 (D. Reidel, Dordrecht-Holland)"
url: https://www.andrewmbailey.com/dkl/General_Semantics.pdf
access: copyright-fair-use
meaning-senses:
  - referential
  - constructional
status: received
created: 2026-06-26
updated: 2026-06-26
links:
  - rel: refines
    target: concept/compositionality
  - rel: supports
    target: concept/truth-conditional-and-use-meaning
---

# Lewis 1970 — General Semantics

## What it is

David Lewis's 1970 paper "General Semantics," *Synthese* 22(1–2), pp. 18–67 (D. Reidel, Dordrecht-Holland). It is a foundational text of **intensional, model-theoretic, compositional semantics for natural language**, and it carries two strands this project needs.

First, the **"Markerese" argument** (pp. 18–19): translating a natural-language sentence into a formal symbolic markup language ("Semantic Markerese" — the semantic-marker apparatus of Katz & Postal) is *not by itself* a semantics, because one can know the Markerese translation of an English sentence "without knowing the first thing about the meaning of the English sentence: namely, the conditions under which it would be true." A translation from one symbol system into another stays inside symbols; it never touches "the relations between symbols and the world of non-symbols — that is... genuinely semantic relations" (p. 19). This is the load-bearing passage for the project: it is the classic statement that **form-to-form translation is not yet meaning**, and a semantics with no treatment of truth-conditions is not a semantics.

Second, Lewis's **intensions-as-functions / compositional categorial-grammar semantics** (§§II–IV, pp. 22–33): a meaning for a sentence is "something that determines the conditions under which the sentence is true or false" (p. 22); an *intension* is a function from indices (possible world plus contextual coordinates) to extensions (truth-values for sentences, things for names, sets for common nouns) (pp. 23–24); and full *meanings* are "semantically interpreted phrase markers" — finite ordered trees with a category and an intension at each node, built up part-from-part so that a compound's meaning is computed from its constituents' (pp. 31–33). This is a primary statement of compositional, intension-based semantics that [`concept/compositionality`](../concepts/compositionality.md) characterizes (the "Montague tradition" it cites as not-in-repo; Lewis 1970 is a sibling primary of that tradition, explicitly drawing on Montague 1968 and Scott 1970, p. 24).

It is a primary philosophy-of-language / formal-semantics text — **not** a human-labeled empirical resource, and so **not a human anchor**: it predates LLMs by half a century and grounds the *theory* a model may or may not instantiate, never a result about any model.

## Provenance

The full text was fetched on **2026-06-26** from the **author-estate self-archive** at andrewmbailey.com (https://www.andrewmbailey.com/dkl/General_Semantics.pdf), the David K. Lewis papers collection (`andrewmbailey.com/dkl/`), an open-access posting of Lewis's published articles. The PDF (50 pages, scan of the *Synthese* original) was downloaded with `curl` and its text extracted with `pdftotext`; every quote below was matched character-for-character against that extracted text. (A second OA copy — a University of Maryland course PDF, `terpconnect.umd.edu/~pietro/.../Lewis_GeneralSemantics.pdf` — was found in the same search but failed to download in this environment with a TLS/connection error, exit 35; the Bailey copy is the one actually read. The Springer *Synthese* version of record, link.springer.com/article/10.1007/BF00413598, is paywalled and was **not** used.)

**Pagination.** The scan preserves the **original *Synthese* journal pagination (pp. 18–67)**: the first text page carries the footer "Synthese 22 (1970) 18-67 ... Copyright © 1970 by D. Reidel Publishing Company, Dordrecht-Holland" (OCR'd as "1). Reidel", flagged below), and the running heads print the page number on each page ("GENERAL SEMANTICS / 19", "/ 23", "/ 25", ... on odd pages; "24 / DAVID LEWIS" on even pages). The locators below are these original journal page numbers, read directly from the running-head numerals, and match the conventional citation pagination (pp. 18–67). This is the *Synthese* original pagination, **not** a reprint — the article was later reprinted in Davidson & Harman (eds.), *Semantics of Natural Language* (1972) and in Lewis's *Philosophical Papers* vol. I (1983) with different pagination; those reprints were **not** consulted, and no locator below refers to them.

**OCR normalization (flagged).** The `pdftotext` extraction carries scan artifacts: mid-sentence line breaks, end-of-line hyphenation (e.g. "semantic interpreta-/tion", "extension-/determining"), and a handful of mis-rendered glyphs — notably "finitude" OCR'd as "]initude" (p. 19), "D. Reidel" as "1). Reidel" (footer, p. 18), "note" for "node" (p. 31), and "Carnap" footnote section signs. In the quotes below, **line-break hyphenation has been closed up**; no words were added, removed, or reordered. Where a quoted span would contain an OCR-mangled glyph it is **flagged inline** and the corrected reading given in brackets. A session quoting these at length should re-verify against the journal scan.

**Access / license.** The *work* is **under copyright** (© 1970 D. Reidel / Springer; Lewis died 2001). It is **not public domain**. This page therefore quotes only **short fair-use passages** from an open-access self-archive, with the copyright status flagged here and in Known limits, and reproduces no wholesale text — the same posture this project takes for its other in-copyright primaries (Davidson, Putnam, Bender & Koller, etc.).

## Key passages (verbatim, with *Synthese* page locators)

### 1. The Markerese argument — form-to-form translation is not yet a semantics (pp. 18–19)

This is the load-bearing passage. Lewis targets the Katz–Postal "semantic marker" apparatus, dubbing the marker vocabulary "Semantic Markerese":

> "Semantic markers are symbols: items in the vocabulary of an artificial language we may call Semantic Markerese. Semantic interpretation by means of them amounts merely to a translation algorithm from the object language to the auxiliary language Markerese. But we can know the Markerese translation of an English sentence without knowing the first thing about the meaning of the English sentence: namely, the conditions under which it would be true. Semantics with no treatment of truth conditions is not semantics. Translation into Markerese is at best a substitute for real semantics, relying either on our tacit competence (at some future date) as speakers of Markerese or on our ability to do real semantics at least for the one language Markerese." (pp. 18–19; line-break hyphenation closed up)

The diagnosis of *why* the translation-into-symbols move fails — it never leaves the realm of symbols:

> "The Markerese method is attractive in part just because it deals with nothing but symbols: finite combinations of entities of a familiar sort out of a finite set of elements by finitely many applications of finitely many rules. There is no risk of alarming the ontologically parsimonious. But it is just this pleasing finitude that prevents Markerese semantics from dealing with the relations between symbols and the world of non-symbols — that is, with genuinely semantic relations." (p. 19; **"finitude" is OCR'd "]initude" in the scan**, corrected here; the em-dash before "that is" renders as a line break in the scan)

The two sentences carrying the most weight for this project's form-vs-meaning line: *"we can know the Markerese translation of an English sentence without knowing the first thing about the meaning of the English sentence: namely, the conditions under which it would be true"* and *"Semantics with no treatment of truth conditions is not semantics"* (both p. 18) — both verified character-for-character.

### 2. A meaning determines truth-conditions (pp. 22–23)

Opening §III, Lewis fixes what a meaning must *do* before asking what it *is* — the truth-conditional starting point:

> "In order to say what a meaning is, we may first ask what a meaning does, and then find something that does that." (p. 22)

> "A meaning for a sentence is something that determines the conditions under which the sentence is true or false. It determines the truth-value of the sentence in various possible states of affairs, at various times, at various places, for various speakers, and so on." (pp. 22–23)

### 3. Intensions as functions from indices to extensions (pp. 23–24)

The intension machinery: meanings (in part) are functions from an *index* (a package of world plus contextual coordinates) to extensions.

> "We will call such an input package of relevant factors an index; and we will call any function from indices to appropriate extensions for a sentence, name, or common noun an intension." (p. 23)

> "Thus an appropriate intension for a sentence is any function from indices to truth-values; an appropriate intension for a name is any function from indices to things; an appropriate intension for a common noun is any function from indices to sets. The plan to construe intensions as extension-determining functions originated with Carnap." (pp. 23–24; "intension for" prints solid in the scan as "intensionfor", separated here; "extension-/determining" hyphenation closed up)

Lewis is explicit that intensions are *not yet* full meanings, because they are too coarse — they cannot distinguish logically equivalent sentences:

> "Intensions, our functions from indices to extensions, are designed to do part of what meanings do. Yet they are not meanings; for there are differences in meaning unaccompanied by differences in intension. It would be absurd to say that all tautologies have the same meaning, but they have the same intension; the constant function having at every index the value truth. Intensions are part of the way to meanings, however..." (p. 25)

### 4. Meanings as compositional, semantically-interpreted phrase markers (pp. 31–33)

The compositional core: full meanings are finite trees carrying a category and an intension at each node, so that a compound's meaning decomposes into — and is built from — its constituents' meanings.

> "It is natural, therefore, to identify meanings with semantically interpreted phrase markers minus their terminal nodes: finite ordered trees having at each node a category and an appropriate intension. If we associate a meaning of this sort with an expression, we are given the category and intension of the expression; and if the expression is compound, we are given also the categories and intensions of its constituent parts, their constituent parts, and so on down." (pp. 31–32; **"node" OCR'd "note"** in the first sentence, corrected here)

> "A meaning may be a tree with a single node; call such meanings simple and other meanings compound. Compound meanings are, as it were, built up from simple meanings by steps in which several meanings (simple or compound) are combined as sub-trees under a new node, analogously to the way in which expressions are built up by concatenating shorter expressions." (p. 33)

This is the part-to-whole construction — a compound meaning is a function of its constituent meanings under the categorial mode of combination — that makes Lewis's a **compositional** semantics in the strict sense [`concept/compositionality`](../concepts/compositionality.md) owns.

## Bearing on this project

- **The form-vs-meaning line (the Markerese argument).** The project's central wedge is whether a symbol-manipulating system has *meaning* or only *form* — the Bender & Koller form/meaning distinction ([`source/bender-koller-2020-climbing`](bender-koller-2020-climbing.md)) and the [`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md) truth-conditional pole. Lewis 1970 is a clean, early primary for one half of that line: a system that maps a sentence to a formal symbolic representation has thereby done a *translation*, not a *semantics*, because one can possess the translation "without knowing the first thing about the meaning... namely, the conditions under which it would be true" (p. 18). Stated against an LLM: producing a symbolic transform of a sentence (a paraphrase, a logical form, a token sequence) is, on Lewis's argument, not *ipso facto* grasping its meaning — the truth-conditional / world-relation is the thing the symbol-shuffling leaves untouched ("the relations between symbols and the world of non-symbols," p. 19). This sharpens the project's recurring **distributional null**: a model's competence at form-to-form mapping does not by itself establish that it tracks truth-conditions. (Honest two-sidedness, kept here: Lewis's "real semantics" *is* the truth-conditional pole; a meaning-as-use or inferentialist reading — [`concept/inferential-meaning`](../concepts/inferential-meaning.md), Piantadosi & Hill's "meaning without reference" — would resist Lewis's premise that truth-conditions are *the* thing missing. Lewis grounds the truth-conditional formulation of the form/meaning gap, not an uncontested one.)
- **[`concept/compositionality`](../concepts/compositionality.md).** That page characterizes the Montague/model-theoretic tradition of compositional, intension-based semantics as *not-in-repo*. Lewis 1970 is an in-repo primary *of that tradition* (Lewis cites Montague 1968 and Scott 1970, p. 24): the intension-as-function-from-indices construction (pp. 23–24) and the meanings-as-interpreted-phrase-markers tree construction (pp. 31–33) are the verbatim source for "the meaning of a compound is built up from the meanings of its constituent parts" via a homomorphism from a categorial syntax to a semantics. Caveat to carry forward: Lewis's full *meanings* are trees (interpreted phrase markers), a *finer* grain than intensions; his intensions alone are explicitly **too coarse** to be meanings (p. 25). Cite Lewis for the compositional, intension-based construction, not for an identification of meaning with intension.
- **Meaning-senses.** Tagged `referential` (Lewis's "real semantics" is the truth-conditional / world-relation pole — meaning as a function to truth-values and extensions, the `Bedeutung` lineage in [`meaning-senses.md`](../../meaning-senses.md); the Markerese argument's whole force is that form-to-form translation never reaches the symbol-to-world relation) and `constructional` (the part-to-whole, category-driven composition of interpreted phrase markers — form–meaning pairings combined under categorial rules). It does **not** bear on `distributional`, `grounded`, or `inferential` directly, except as the truth-conditional foil those poles are contrasted against.

## What it can ground

- The verbatim **Markerese argument** (pp. 18–19) — that translation of a sentence into a formal symbolic markup is not a semantics absent a treatment of truth-conditions — for any page needing the founding statement of the form-to-form-is-not-meaning point rather than a paraphrase.
- The verbatim **intension** construction (functions from indices to extensions, pp. 23–24), the **meaning-determines-truth-conditions** starting point (pp. 22–23), the **intensions-are-not-yet-meanings** caveat (p. 25), and the **compositional interpreted-phrase-marker / tree** construction (pp. 31–33) — for any page needing the founding formulation of intensional, compositional, model-theoretic semantics rather than a paraphrase.
- The historical-conceptual point that on Lewis's picture **meaning is, at its core, a truth-conditional world-relation built up compositionally** — the referential/truth-conditional pole the project contrasts against distributional and use accounts.

## What it cannot ground

- **Any claim about LLMs, embeddings, or neural models.** The paper predates all of it by half a century; it grounds the *theory* a model may or may not instantiate, never a result about a model. The Markerese argument is suggestive *for* the project's form-vs-meaning question, but Lewis is arguing about a *theory of semantics* (Katz–Postal markers), not about any computational system's internal states; transferring his conclusion to "an LLM that maps text to tokens therefore lacks meaning" is an **interpretive application by this project, not a claim Lewis makes**, and it inherits the contested premise that truth-conditions are the missing ingredient.
- **It is not an `anchors:` resource** — it is not a human-labeled empirical asset (no treebank, sense inventory, acceptability norm, or annotation), and it grounds no claim about any model.
- **A human-comparison anchor.** A `source` page supplies theory/provenance, not a human yardstick; citing it does not discharge any empirical claim's human-anchor obligation.
- **An uncontested form/meaning verdict.** Lewis's "real semantics" is specifically *truth-conditional*; the page grounds the truth-conditional statement of the form-vs-meaning gap, which a use-theoretic or inferentialist account would resist (see Bearing, above). Do not cite it as settling that meaning *requires* truth-conditions.

## Known limits

- **In copyright; short fair-use quotes only.** © 1970 D. Reidel / Springer. This page quotes only short passages and reproduces no wholesale text; a citing session must respect the same limit.
- **OCR/scan provenance.** Quotes come from a `pdftotext` extraction of a scan (via the andrewmbailey.com author-estate self-archive), not a born-digital text. Line-break hyphenation was closed up and several mis-OCR'd glyphs flagged and corrected inline ("]initude" → "finitude" p. 19; "1). Reidel" → "D. Reidel" footer p. 18; "note" → "node" p. 31; "intensionfor" separated p. 23). Re-verify against the journal scan before quoting at length.
- **Page locators are the *Synthese* original pagination (18–67)**, read from the running-head numerals in the scan; they match the conventional citation pagination. The 1972 (*Semantics of Natural Language*) and 1983 (*Philosophical Papers* I) reprints have different pagination and were **not** consulted.
- The paper's bulk — the categorial base and its transformational extension (§IV ff.), the treatment of non-declaratives / mood / performatives (§VIII), intensions for derived categories, the appendix on indices — is summarized only in passing here; this page captures the Markerese argument, the intension construction, the truth-conditional starting point, and the compositional interpreted-phrase-marker core (pp. 18–33), not the full grammar.
