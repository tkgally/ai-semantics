---
type: source
id: tarski-1944-semantic-conception-of-truth
title: The Semantic Conception of Truth and the Foundations of Semantics
authors:
  - Tarski, Alfred
year: 1944
venue: "Philosophy and Phenomenological Research 4(3): 341–376"
url: http://www.ditext.com/tarski/tarski.html
access: fair-use-quotes-only
meaning-senses:
  - referential
  - referential.reference
  - constructional
status: received
created: 2026-06-26
updated: 2026-06-26
links:
  - rel: supports
    target: concept/truth-conditional-and-use-meaning
  - rel: supports
    target: concept/compositionality
---

# Tarski 1944 — The Semantic Conception of Truth and the Foundations of Semantics

## What it is

Alfred Tarski's 1944 article "The Semantic Conception of Truth and the Foundations of Semantics," *Philosophy and Phenomenological Research* 4(3): 341–376. It is Tarski's informal, philosophical-audience restatement of the technical theory of truth first published in his 1933 monograph (*Der Wahrheitsbegriff in den formalisierten Sprachen* / "The Concept of Truth in Formalized Languages"). The article supplies, in prose rather than formalism, the apparatus that the project's concept pages mean when they write "Tarski's recursive definition of truth via satisfaction":

- the **material-adequacy condition** (Convention T): an adequate definition of truth must entail every instance of the schema **(T) X is true if, and only if, p** — the canonical illustration being *the sentence "snow is white" is true if, and only if, snow is white* (§4);
- the **semantic conception** of truth: truth as a relation aligned with the Aristotelian intuition, "carefully" deflationary in that the schema, not any one equivalence, fixes the notion, and that truth for a sentence is always truth-in-a-language (§§3, 5);
- the **object-language / meta-language distinction** and the diagnosis that a **semantically closed** language (one containing its own truth predicate plus the names of its own sentences, with the ordinary laws of logic) is inconsistent because it breeds the **Liar antinomy** (§§7–9);
- the recursive definition of truth via **satisfaction** — a sentence is true iff it is satisfied by all objects (§11).

It is a **primary philosophy/logic-of-meaning text** — **not** a human-labeled empirical resource, and so **not a human anchor**: it grounds the *theory* the project's concept pages characterize, never a result about any model. Before this page, [`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md) and [`concept/compositionality`](../concepts/compositionality.md) both cited Tarski only as "(not in-repo; characterization)." This page is the in-repo primary those pages can now point at for the Convention-T schema, the object/meta-language distinction, and truth-via-satisfaction.

## Provenance

The full text of **Part I (the expository part, §§1–13)** was fetched on **2026-06-26** from the open-access hypertext transcription by Andrew Chrucky (1997) hosted at `ditext.com`: the frameset is `http://www.ditext.com/tarski/tarski.html`; the body read for this page is `http://www.ditext.com/tarski/tarski1.html` (§§1–13). The contents file `http://www.ditext.com/tarski/tarski-c.html` supplies the article's section list and is the source of the section titles below. The raw HTML was downloaded with `curl`, tags were stripped, and **every quote below was matched character-for-character against the raw HTML source** (verifying the wording survives the italic/blockquote markup the transcription interleaves).

**Locators.** The article is divided into **23 numbered sections** in two parts — Part I "Exposition" (§§1–13) and Part II "Polemical Remarks" (§§14–23). The Chrucky transcription preserves these section numbers exactly; locators below are **section-level** (e.g. §4), which is the article's own native division. The transcription does **not** preserve the original PPR page numbers (341–376) inline, so no page-level locator is given except where Tarski himself prints one inside the text (his Liar sentence self-refers to "p. 347, l. 31" — that "347" is Tarski's own in-text page reference in the original PPR pagination, quoted verbatim, not a locator this page assigns).

**What was read.** Only **Part I (§§1–13)** of the **1944 PPR article** was fetched and quoted. Part II (§§14–23, the polemical remarks) was not needed for the passages this page captures and is not quoted. The **1933 monograph was NOT consulted**; where the full satisfaction recursion lives in technical detail is the 1933 work, and §11 here is Tarski's own *outline* of it — this page quotes the 1944 outline and says so, and makes no claim about the 1933 formalism beyond what §11 states.

**Access / copyright.** The 1944 article is **© 1944 (Philosophy and Phenomenological Research; rights now with Wiley)** and is **not public domain** (Tarski died 1983; the venue is a still-published journal). The ditext transcription carries **no copyright notice of its own** and presents the text as a scholarly reproduction. This page therefore treats the work like the project's Putnam/Burge pages: **short fair-use quotes only**, from an open-access mirror, with the copyright status flagged here and in Known limits. Access status is recorded as `fair-use-quotes-only`.

**One transcription artifact, flagged.** In §5 the ditext transcription prints "snow satisfies the sentential function (the condition) **"2 is white"**" — the "2" is an OCR/transcription error in the mirror for the intended **"x is white"** (the very function §11 uses, "x is white," with "snow" as the object that satisfies it). The §5 designation/satisfaction examples are therefore **paraphrased, not quoted**, below to avoid propagating the typo; the §11 satisfaction passages (which read "x is white" correctly) are quoted verbatim.

## Key passages (verbatim, with section locators)

### 1. The Aristotelian intuition the definition must honor (§3)

Tarski anchors the "classical Aristotelian conception" with Aristotle's *Metaphysics* formulation, then notes the "correspondence" gloss:

> "To say of what is that it is not, or of what is not that it is, is false, while to say of what is that it is, or of what is not that it is not, is true." (§3, Tarski quoting Aristotle's *Metaphysics*)

> "The truth of a sentence consists in its agreement with (or correspondence to) reality. (For a theory of truth which is to be based upon the latter formulation the term "correspondence theory" has been suggested.)" (§3)

Tarski immediately flags these formulations as imprecise — "none of them can be considered a satisfactory definition of truth" (§3) — which is why the material-adequacy criterion of §4 is needed. Note also the **language-relativity** of truth he insists on in §2:

> "we must always relate the notion of truth, like that of a sentence, to a specific language; for it is obvious that the same expression which is a true sentence in one language can be false or meaningless in another." (§2)

### 2. The snow-is-white example and the schema (T) (§4)

The concrete equivalence the definition must imply, quoted verbatim:

> "The sentence "snow is white" is true if, and only if, snow is white." (§4)

Tarski generalizes by replacing the sentence with `p` and its name with `X`:

> "(T) X is true if, and only if, p." (§4)

> "We shall call any such equivalence (with 'p' replaced by any sentence of the language to which the word "true" refers, and 'X' replaced by a name of this sentence) an "equivalence of the form (T)."" (§4)

### 3. The material-adequacy condition (Convention T) (§4)

The load-bearing definition of adequacy — an adequate truth-definition must entail *all* equivalences of form (T):

> "we wish to use the term "true" in such a way that all equivalences of the form (T) can be asserted, and we shall call a definition of truth "adequate" if all these equivalences follow from it." (§4)

And the careful, deflationary-flavored caveat that the schema itself is **not** the definition — each instance is only a *partial* definition:

> "neither the expression (T) itself (which is not a sentence, but only a schema of a sentence) nor any particular instance of the form (T) can be regarded as a definition of truth." (§4)

> "every equivalence of the form (T) obtained by replacing 'p' by a particular sentence, and 'X' by a name of this sentence, may be considered a partial definition of truth ... The general definition has to be, in a certain sense, a logical conjunction of all these partial definitions." (§4)

The §4 quotation-marks discussion is also where Tarski states the **use/mention** point that on the left of (T) stands *the name of the sentence*, not the sentence: "if we wish to say something about a sentence, for example, that it is true, we must use the name of this sentence, and not the sentence itself" (§4).

### 4. Truth as a semantic concept (§5)

Tarski names the conception and locates truth among the **semantic** relations (designation, satisfaction, definition):

> "Semantics is a discipline which, speaking loosely, deals with certain relations between expressions of a language and the objects (or "states of affairs") "referred to" by those expressions." (§5)

Truth differs from designation/satisfaction in being a property, not a relation, yet is grounded *via* a relation — satisfaction:

> "the simplest and the most natural way of obtaining an exact definition of truth is one which involves the use of other semantic notions, e.g., the notion of satisfaction." (§5)

(The §5 examples — "the father of his country" designates George Washington; snow satisfies the function "x is white"; the equation defining ½ — are **paraphrased here, not quoted**, because the mirror misprints the satisfaction example as "2 is white"; see the transcription-artifact note in Provenance.)

### 5. The object-language / meta-language distinction (§9)

The apparatus the project's concept pages mean by "Tarski's … definition of truth":

> "We shall refer to the first language as "the object language," and to the second as "the meta-language."" (§9)

> "every sentence which occurs in the object-language must also occur in the meta-language; in other words, the meta-language must contain the object-language as a part." (§9)

Tarski stresses the relativity and the resulting **hierarchy of languages**: "these terms "object-language" and "meta-language" have only a relative sense … In this way we arrive at a whole hierarchy of languages." (§9). Truth is **defined in the meta-language**, and the meta-language must be (§10) "essentially richer" than the object-language for the definition to succeed:

> "the condition of "essential richness" is necessary for the possibility of a satisfactory definition of truth in the meta-language." (§10)

### 6. Semantic closure and the Liar antinomy (§§7–8)

Tarski derives the Liar from the (T)-equivalence for a self-referential sentence `s` ("The sentence printed in this paper on p. 347, l. 31, is not true"), reaching:

> "(3) 's' is true if, and only if, 's' is not true." (§7)

> "In this way we have arrived at an obvious contradiction." (§7)

He then isolates the property of the language that produces it — **semantic closure** — and concludes such languages are to be rejected:

> "We have implicitly assumed that the language in which the antinomy is constructed contains, in addition to its expressions, also the names of these expressions, as well as semantic terms such as the term "true" referring to sentences of this language; we have also assumed that all sentences which determine the adequate usage of this term can be asserted in the language. A language with these properties will be called "semantically closed."" (§8)

> "Since every language which satisfies both of these assumptions is inconsistent, we must reject at least one of them" (§8)

> "we decide not to use any language which is semantically closed in the sense given." (§8)

This is exactly why truth cannot be defined for a single universal/everyday language that talks about its own truth — the reason the object/meta-language split is forced. Tarski adds about everyday language: "We may at best only risk the guess that a language whose structure has been exactly specified and which resembles our everyday language as closely as possible would be inconsistent." (§8)

### 7. Truth via satisfaction, recursively (§11)

Truth is defined from **satisfaction**, itself defined by a recursive procedure over sentential functions:

> "A definition of truth can be obtained in a very simple way from that of another semantic notion, namely, of the notion of satisfaction." (§11)

> "Satisfaction is a relation between arbitrary objects and certain expressions called "sentential functions." These are expressions like "x is white," "x is greater than y," etc." (§11)

The recursion bottoms out, and truth falls out as satisfaction-by-all-objects:

> "for a sentence only two cases are possible: a sentence is either satisfied by all objects, or by no objects. Hence we arrive at a definition of truth and falsehood simply by saying that a sentence is true if it is satisfied by all objects, and false otherwise." (§11)

This §11 passage is Tarski's **1944 outline** of the satisfaction recursion; the fully formal recursion (satisfaction by infinite sequences, the clauses for each connective and quantifier) is in the 1933 monograph, **which this page did not consult**.

## Bearing on this project

- **[`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md).** That page's pole (a) writes: "Tarski's recursive definition of truth for a formalized language (1933/1944) made "is true" a precise, compositional notion via satisfaction." This page supplies the in-repo verbatim primary for exactly that — Convention T (§4), truth-via-satisfaction (§11), and the object/meta-language machinery (§9). The page's "Honest gaps" lists Tarski among the not-in-repo truth-conditional lineage; this closes the **Tarski** leg (Davidson, Montague remain not-in-repo).
- **[`concept/compositionality`](../concepts/compositionality.md).** That page describes the Montague-tradition homomorphism that "lets that machinery run." Tarski's truth-via-satisfaction is the **compositional / recursive** half: §11's recursive construction (simplest functions first, then "operations by means of which compound functions can be constructed from simpler ones") is the precise sense in which "is true" is built up systematically from the structure of expressions — the satisfaction recursion mirrors the syntactic build-up. The compositionality-relevant content here is the *recursive* definition, not a "function of the meanings of the parts" slogan (Tarski states a recursion over satisfaction, not a meaning-of-the-whole principle). This page is tagged `constructional` for that part–whole recursion, since the controlled vocabulary in [`meaning-senses.md`](../../meaning-senses.md) has no separate `compositional` tag.
- **The `referential` pole.** [`meaning-senses.md`](../../meaning-senses.md) defines `referential` as the relation between an expression and something in the world (or a model). Tarski's semantics is the disciplined version of that relation for the truth predicate: truth grounded in satisfaction, "relations between expressions of a language and the objects … "referred to" by those expressions" (§5). It is the referential pole the project contrasts against distributional and use accounts — and a *deflationary-careful* version: the schema (T), not a metaphysics of correspondence, fixes the notion.

## What it can ground

- The verbatim Convention-T schema (§4), the snow-is-white equivalence (§4), the material-adequacy condition (§4), the Aristotelian/correspondence framing and language-relativity of truth (§§2–3), the object/meta-language distinction and language hierarchy (§9), the semantic-closure / Liar-antinomy diagnosis (§§7–8), and truth-via-satisfaction-by-all-objects (§11) — for any page needing Tarski's own formulation rather than a paraphrase.
- The historical-conceptual point that, on the Tarskian picture, **"is true" is a precise relation between a sentence and the world via satisfaction, defined only relative to a language and only from a richer meta-language** — the referential, truth-conditional anchor the project sets against distributional and use-based accounts of meaning.

## What it cannot ground

- **Any claim about LLMs, embeddings, or neural models.** The article predates all of it; it grounds the *theory* a model may or may not instantiate, never a result about a model. **It is not an `anchors:` resource** — it is not a human-labeled empirical asset (no treebank, sense inventory, acceptability norm, or annotation), and citing it **grounds no claim about any model** and **discharges no empirical claim's human-anchor obligation**.
- **The full formal satisfaction recursion.** §11 is Tarski's *outline*; the detailed recursion (satisfaction by sequences, per-connective/quantifier clauses) is in the **1933 monograph, not consulted here**. Cite this page for the 1944 outline and the Convention-T apparatus, not for the 1933 formalism.
- **A "meaning of the whole is a function of the meanings of the parts" slogan.** What is verbatim here is a *recursive* definition of truth via satisfaction (§11) and the material-adequacy condition (§4) — not a compositionality principle in the textbook slogan form; that systematization is Montague-tradition, not Tarski's wording.

## Known limits

- **Copyright / fair-use.** The 1944 PPR article is © 1944 (Wiley/PPR) and **not public domain**; this page quotes short passages under fair use from an open-access transcription. A citing session quoting at length should re-verify against the journal original or a licensed copy and keep quotations minimal.
- **Transcription, not page image.** Quotes are matched against the Chrucky hypertext transcription, not the PPR scan; locators are **section-level** (the article's native division), and original PPR page numbers (341–376) are **not** carried (except Tarski's own in-text "p. 347" self-reference). One mirror typo ("2 is white" for "x is white" in §5) is flagged and quarantined above by paraphrasing the affected §5 examples.
- **Part I only; 1933 not read.** Only the expository §§1–13 of the 1944 article were fetched; the polemical Part II (§§14–23) and the 1933 monograph were not consulted. Any reading of Tarski's *replies to objections* (e.g. on whether the conception is "correspondence," on epistemology) would need Part II, which this page does not cover.
