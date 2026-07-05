---
type: source
id: davidson-1967-truth-and-meaning
title: Truth and Meaning
authors:
  - Davidson, Donald
year: 1967
venue: "Synthese 17(3), Sep. 1967, pp. 304–323"
url: https://www.uh.edu/~garson/Truth%20and%20Meaning.pdf
access: copyright-fair-use
meaning-senses:
  - referential
  - inferential
status: received
created: 2026-06-26
updated: 2026-07-05
links:
  - rel: supports
    target: concept/truth-conditional-and-use-meaning
  - rel: supports
    target: concept/semantic-holism
  - rel: supports
    target: concept/compositionality
---

# Davidson 1967 — Truth and Meaning

## What it is

Donald Davidson's 1967 paper "Truth and Meaning," *Synthese* 17(3), pp. 304–323 (published by D. Reidel, Dordrecht-Holland). It is the founding statement of **truth-conditional theory of meaning for natural language**: Davidson's proposal that a theory of meaning for a language `L` can take the form of a **Tarski-style recursive theory of truth for `L`** — that to give the conditions under which each sentence is true is, in effect, to give its meaning. The paper argues that **meanings-as-entities** do no explanatory work and should be dropped; that a workable theory must be **finitely stated** so that a learner who masters a finite vocabulary and finite rules can produce and understand a potential infinitude of sentences; that the meanings of sentences are **holistically** interdependent ("only in the context of the language does a sentence... have meaning"); and that the criterion an adequate theory must meet is **Tarski's Convention T**, with Tarski's order of explanation *reversed* — truth taken as the illuminating primitive rather than meaning/translation. It is a primary philosophy-of-meaning text — **not** a human-labeled empirical resource, and so **not a human anchor**: it grounds the *theory* the project's concept pages characterize, never a result about any model.

Before this page, [`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md) cited Davidson (1967) only as "(not in-repo; characterization)" in its truth-conditional lineage, and [`concept/semantic-holism`](../concepts/semantic-holism.md) characterized Davidson's holism without a quoted primary. This page is the in-repo primary those two concept pages can now point at for the truth-conditions-as-meaning move, the rejection of meanings-as-entities, the learnability/finitude motivation, the holism line, and the Convention-T dependence.

## Provenance

The full text was fetched on **2026-06-26** from an open-access course mirror at the University of Houston (https://www.uh.edu/~garson/Truth%20and%20Meaning.pdf), a scan of the JSTOR digitization of the *Synthese* original (the file's own cover page reads "Source: *Synthese*, Vol. 17, No. 3 ... (Sep., 1967), pp. 304–323" and "Stable URL: http://www.jstor.org/stable/20114563"). The PDF was downloaded locally and its text extracted with `pypdf`; every quote below was matched against that extracted text.

**Pagination.** The locators below are the **original *Synthese* journal page numbers (304–323)**, read directly from the page-footer numerals preserved in the scan (each journal page's text block terminates in its printed number: "304", "305", ... "323"). These are the conventional citation pages. The page assignment of every quote below was verified programmatically against those footer markers.

**OCR normalization (flagged).** The extracted text carries OCR artifacts: mid-sentence line breaks, end-of-line hyphenation (e.g. "lan-/guage", "ob-/jection"), and mis-rendered punctuation — Davidson's typographic quotes around metavariables come out as stray glyphs (the printed `'is T'` extracts as `'is T9`; `'s'` as `V`; `'p'` as `'p9`). In the quotes below, **line-break hyphenation has been closed up and the mis-OCR'd metavariable quotes restored to plain ASCII quotes** (`'is T'`, `'s'`, `'p'`); no words were added, removed, or reordered. A session quoting these at length should re-verify against the journal scan, especially around the formula `(T)` and the `'s' / 'p'` metavariables. One verbatim oddity is preserved as printed: the scan reads "meaning ; in the same vein" with a space before the semicolon (kept below).

**Access / license.** The *work* is **under copyright** (© 1967 D. Reidel Publishing Co. / Springer; Davidson died 2003). It is **not public domain**. This page therefore quotes only **short fair-use passages** from an open-access mirror, with the copyright status flagged here and in Known limits, and reproduces no wholesale text — the same posture this project takes for its other in-copyright primaries (Putnam, Burge, Bender & Koller, etc.).

## Key passages (verbatim, with *Synthese* page locators)

### 1. The learnability / finitude motivation (p. 304)

The paper opens on the demand that fixes the whole project — a theory must explain how a finite endowment yields an unbounded competence:

> "Unless such an account could be supplied for a particular language, it is argued, there would be no explaining the fact that we can learn the language: no explaining the fact that, on mastering a finite vocabulary and a finitely stated set of rules, we are prepared to produce and to understand any of a potential infinitude of sentences." (p. 304; line-break hyphenation in "lan-/guage" closed up)

This is the recursion / finite-account motivation the project's concept pages attribute to Davidson. A footnote ties it to his earlier learnability argument: "Elsewhere I have urged that it is a necessary condition, if a language is to be learnable, that it have only a finite number of semantical primitives" (note 1, p. 321, citing his "Theories of Meaning and Learnable Languages," 1965).

### 2. Why meanings-as-entities fail — the regress and "no demonstrated use" (pp. 304, 307)

Davidson rejects the proposal to assign "some entity as meaning to each word." Assigning entities and a relation of "participating in or instantiating" to concatenation, he notes, only starts a regress:

> "Viewing concatenation as a significant piece of syntax, we may assign to it the relation of participating in or instantiating; however, it is obvious that we have here the start of an infinite regress." (p. 304)

His diagnosis is not that meaning-entities are abstract or ill-individuated but that they earn nothing:

> "My objection to meanings in the theory of meaning is not that they are abstract or that their identity conditions are obscure, but that they have no demonstrated use." (p. 307; "ob-/jection" closed up)

He had already proposed rephrasing the demand so as "not to suggest that individual words must have meanings at all, in any sense that transcends the fact that they have a systematic effect on the meanings of the sentences in which they occur" (p. 305) — the move from word-meanings to *systematic contribution*.

### 3. The holism thread (p. 308)

The line [`concept/semantic-holism`](../concepts/semantic-holism.md) wants for the Davidson leg — meanings of sentences are interdependent, and a word's meaning is an abstraction from the totality of sentences it figures in:

> "If sentences depend for their meaning on their structure, and we understand the meaning of each item in the structure only as an abstraction from the totality of sentences in which it features, then we can give the meaning of any sentence (or word) only by giving the meaning of every sentence (and word) in the language. Frege said that only in the context of a sentence does a word have meaning ; in the same vein he might have added that only in the context of the language does a sentence (and therefore a word) have meaning." (p. 308; "meaning ;" printed with the space before the semicolon, kept verbatim)

Davidson calls this "a certain holistic view of meaning" (p. 308) and notes it "was already implicit in the suggestion that an adequate theory of meaning must entail all sentences of the form 's means m'" (p. 308).

### 4. The core proposal: the (T) schema and truth-conditions as meaning (pp. 309–310)

Sweeping away the intensional "means that," Davidson arrives at the schema and the requirement on a theory:

> "(T) s is T if and only if p." (p. 309)

> "What we require of a theory of meaning for a language L is that without appeal to any (further) semantical notions it place enough restrictions on the predicate 'is T' to entail all sentences got from schema T when 's' is replaced by a structural description of a sentence of L and 'p' by that sentence." (p. 309; OCR-mangled metavariable quotes restored to `'is T'`, `'s'`, `'p'`)

The conclusion, stated in his own summary:

> "a theory of meaning for a language L shows 'how the meanings of sentences depend upon the meanings of words' if it contains a (recursive) definition of truth-in-L." (p. 310)

And the explicit identification of truth-conditions with meaning — the formulation the project most needs:

> "the definition works by giving necessary and sufficient conditions for the truth of every sentence, and to give truth conditions is a way of giving the meaning of a sentence. To know the semantic concept of truth for a language is to know what it is for a sentence — any sentence — to be true, and this amounts, in one good sense we can give to the phrase, to understanding the language." (p. 310)

### 5. Convention T, and the reversal of Tarski (pp. 309–310)

Davidson borrows Tarski's adequacy criterion as the test his own theory must meet:

> "the condition we have placed on satisfactory theories of meaning is in essence Tarski's Convention T that tests the adequacy of a formal semantical definition of truth." (pp. 309–310)

And he frames his own contribution as defending the *philosophical* role of the semantic concept of truth — taking truth as the foundation that illuminates meaning (where Tarski's own enterprise had presupposed meaning/translation in order to define truth):

> "I hope that what I am doing may be described in part as defending the philosophical importance of Tarski's semantical concept of truth." (p. 310)

> "It is a misfortune that dust from futile and confused battles ... has prevented those with a theoretical interest in language ... from recognizing in the semantical concept of truth (under whatever name) the sophisticated and powerful foundation of a competent theory of meaning." (p. 310)

(The *reversal* is Davidson's order of explanation: Tarski defined truth on the assumption that translation/meaning was already understood, whereas Davidson takes a truth theory meeting Convention T as the thing that *illuminates* meaning. Davidson states the borrowing and the foundational role verbatim above; the "reversal" gloss is the standard reading of that move, made explicit here as interpretation, not as a phrase Davidson quotes.)

### 6. Testability and the empirical character (pp. 310–312)

Davidson stresses the theory is empirical and testable case-by-case against truth-conditions:

> "A theory of meaning (in my mildly perverse sense) is an empirical theory, and its ambition it to account for the workings of a natural language." (pp. 310–311; "ambition it" printed thus — apparent typo for "is," kept verbatim)

> "A typical test case might involve deciding whether the sentence 'Snow is white' is true if and only if snow is white." (p. 311)

He also concedes the program's open problems at the close: counterfactuals, causal and probabilistic sentences, adverbs, attributive adjectives, mass terms, belief/perception/intention, and non-declaratives "that seem not to have truth values at all" (p. 320).

## Bearing on this project

- **[`concept/truth-conditional-and-use-meaning`](../concepts/truth-conditional-and-use-meaning.md).** That page's pole (a) states: "Davidson (1967) proposed that a Tarski-style truth theory could serve as a theory of *meaning* for a natural language — in the standard slogan-form of his proposal, to give a sentence's meaning is, in effect, to state its truth-conditions." This page supplies the verbatim primary: "to give truth conditions is a way of giving the meaning of a sentence" (p. 310) and the (T) schema (p. 309). The concept page's "Honest gaps" listed Davidson (1967) among the not-in-repo truth-conditional lineage; that gap is now closed for Davidson (Tarski 1933/1944 and Montague PTQ 1973 remain not-in-repo). *(Correction, 2026-07-05, s183: Tarski 1944 is in-repo — [`source/tarski-1944-semantic-conception-of-truth`](tarski-1944-semantic-conception-of-truth.md), ingested session 116, the same session as this page — and the Montague characterization entered at secondary strength via the SEP survey [`source/janssen-zimmermann-montague-semantics-sep`](janssen-zimmermann-montague-semantics-sep.md), session 124; only the Tarski 1933 monograph and the Montague PTQ primary remain not-in-repo, per [`wanted.md`](../wanted.md).)*
- **[`concept/semantic-holism`](../concepts/semantic-holism.md).** That page characterizes Davidson as carrying confirmation holism "into the theory of interpretation and the mental: belief and meaning are fixed together, holistically" (citing *Inquiries into Truth and Interpretation*, 1984, not in-repo). This 1967 paper is the earlier, in-repo primary for the **holism of sentence-meaning**: "only in the context of the language does a sentence (and therefore a word) have meaning" (p. 308), plus the radical-translation passage where "there is no completely disentangling questions of what the alien means from questions of what he believes... We do not know what someone means unless we know what he believes; we do not know what someone believes unless we know what he means" (p. 312). Caveat to carry forward: the 1967 paper does not state the *full* belief-meaning interdependence thesis of the 1984 book; cite it for the sentence-meaning holism and the radical-translation circle, not for the mature interpretation theory.
- **[`concept/compositionality`](../concepts/compositionality.md).** Davidson frames the whole task as showing "how the meanings of sentences depend upon the meanings of words" (p. 304, p. 310) via a *recursive* truth definition — a compositional requirement (structure-driven, finitely-stated). The page can cite this for the *recursion/finitude* face of compositionality. Caveat: Davidson explicitly drops word-*meanings* as entities (p. 305, p. 307), so his is compositionality of **truth-conditional contribution**, not of word-meanings-as-objects; cite carefully.
- **Meaning-senses.** Tagged `referential` (the truth-conditional / world-relation pole — meaning as truth-in-a-model, Frege's `Bedeutung` lineage, [`meaning-senses.md`](../../meaning-senses.md)) and `inferential` (the holism thread: a sentence/word has its content only via its place in the whole language's pattern of truths, which is an inferential-role-adjacent, web-of-sentences picture). It does **not** bear on `distributional`, `grounded`, or `constructional` directly.

## What it can ground

- The verbatim truth-conditions-as-meaning proposal (p. 310), the (T) schema (p. 309), the recursive-truth-definition conclusion (p. 310), the rejection of meanings-as-entities (pp. 304, 307), the learnability/finitude motivation (p. 304), the holism line (p. 308), and the Convention-T dependence (pp. 309–310) — for any page needing the founding formulation rather than a paraphrase.
- The historical-conceptual point that on Davidson's picture a **theory of meaning is a theory of truth**: meaning is approached through truth-conditions, with no commitment to meanings as objects — the referential/truth-conditional pole the project contrasts against distributional and use accounts.

## What it cannot ground

- **Any claim about LLMs, embeddings, or neural models.** The paper predates all of it; it grounds the *theory* a model may or may not instantiate, never a result about a model. **It is not an `anchors:` resource** — it is not a human-labeled empirical asset (no treebank, sense inventory, acceptability norm, or annotation), and it grounds no claim about any model.
- **A human-comparison anchor.** A `source` page supplies theory/provenance, not a human yardstick; citing it does not discharge any empirical claim's human-anchor obligation.
- **The mature Davidsonian interpretation theory.** This is the 1967 paper, not *Inquiries into Truth and Interpretation* (1984); the full belief-meaning holism, radical interpretation, and the principle of charity are only seeded here (the charity/radical-translation passage, p. 312), not developed.

## Known limits

- **In copyright; short fair-use quotes only.** © 1967 D. Reidel / Springer. This page quotes only short passages and reproduces no wholesale text; a citing session must respect the same limit.
- **OCR/scan provenance.** Quotes come from a `pypdf` text extraction of a JSTOR scan of the journal original (via the UH open-access mirror), not from a born-digital text. Line-break hyphenation was closed up and mis-OCR'd metavariable quotes (`'is T9` → `'is T'`, `V` → `'s'`, `'p9` → `'p'`) restored, as flagged in Provenance; one printed oddity ("meaning ;" with the pre-semicolon space) and one apparent typo ("ambition it to account") are kept verbatim. Re-verify against the journal scan before quoting at length, especially around the `(T)` formula and the `'s' / 'p'` metavariables.
- **Page locators are the *Synthese* footer numerals (304–323)**, read from the scan; they match the conventional citation pagination but were read off a digitized scan, not a typeset born-digital edition.
- **Tarski-reversal is partly interpretation.** Davidson's borrowing of Convention T and his "foundation of a competent theory of meaning" framing are quoted verbatim (pp. 309–310); the gloss that this *reverses* Tarski's order of explanation (Tarski presupposing meaning to define truth; Davidson presupposing truth to illuminate meaning) is the standard reading, flagged as interpretation, not a phrase quoted from the paper.
- The paper's later technical sections (radical translation and charity, pp. 312–313; the semantic paradoxes and Tarski's pessimism, pp. 313–314; attributive adjectives, pp. 316–317; demonstratives/indexicals and truth-relativized-to-speaker-and-time, pp. 318–320) are summarized only in passing here; this page captures the truth-conditions-as-meaning core, the anti-entity and finitude motivations, the holism line, and the Convention-T dependence.
