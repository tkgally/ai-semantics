---
type: source
id: harris-1954-distributional-structure
title: Distributional Structure
authors:
  - Harris, Zellig S.
year: 1954
venue: Word 10(2-3), pp. 146-162
url: https://www.its.caltech.edu/~matilde/ZelligHarrisDistributionalStructure1954.pdf
access: open-access
meaning-senses:
  - distributional
status: received
created: 2026-06-24
updated: 2026-06-24
links:
  - rel: refines
    target: concept/distributional-meaning
---

# Harris 1954 — Distributional Structure

## What it is

The paper that states the **distributional hypothesis** formally. Zellig S. Harris, "Distributional Structure," published in *Word* 10(2-3), pp. 146-162 (1954). Harris argues that the elements of a language can be described, exhaustively and exactly, through their *distribution* — the positions in which each element occurs relative to other elements — and that this distributional structure is not a separate optional level but the structure of language itself. The paper's most-cited move is the claim that **difference of meaning correlates with difference of distribution**: the more two elements differ in the company they keep, the more they differ in meaning. This is the structuralist source-statement that the next-token objective and word-embedding methods later operationalize at scale; it is one of the two founding statements of distributional semantics (the other being [`source/firth-1957-synopsis`](firth-1957-synopsis.md)).

Provenance: the full text was read character-for-character from a freely accessible scan hosted on Matilde Marcolli's faculty page at Caltech (https://www.its.caltech.edu/~matilde/ZelligHarrisDistributionalStructure1954.pdf, fetched 2026-06-24; 17-page scan of the *Word* original, with the original journal pagination 146-162 visible as running-header page numbers). All quotes below were verified against the extracted text of that scan, and each carries the original *Word* page number read directly from that page's header. This is a scan of the primary; the primary text was consulted (not a secondary reproduction). The article is also the official-of-record Taylor & Francis item (DOI 10.1080/00437956.1954.11659520), which is paywalled; the Caltech scan is the open-access route used here.

## Opening statement (verbatim, p. 146)

> "1. Does language have a distributional structure? For the purposes of the present discussion, the term structure will be used in the following non-rigorous sense: A set of phonemes or a set of data is structured in respect to some feature, to the extent that we can form in terms of that feature some organized system of statements which describes the members of the set and their interrelations (at least up to some limit of complexity). In this sense, language can be structured in respect to various independent features."

## The central claim (verbatim, p. 156)

The hypothesis that names the tradition. Read at the bottom of p. 156 (immediately preceding the page-157 header in the scan); the surrounding context is Harris's point (b), that the non-arbitrariness of class co-selection can be used as a *measure of meaning difference*:

> "More than that: if we consider words or morphemes A and B to be more different in meaning than A and C, then we will often find that the distributions of A and B are more different than the distributions of A and C. In other words, difference of meaning correlates with difference of distribution."

## All elements are distributionally describable (verbatim, p. 146)

The claim that distribution is not a partial or optional description but covers every element:

> "All elements in a language can be grouped into classes whose relative occurrence can be stated exactly. However, for the occurrence of a particular member of one class relative to a particular member of another class it would be necessary to speak in terms of probability, based on the frequency of that occurrence in a sample."

## The oculist / eye-doctor / lawyer worked example (verbatim, pp. 156-157)

Harris's illustration of how distributional overlap tracks synonymy and meaning difference — the passage NLP retells as the intuition behind embeddings:

> "If we consider oculist and eye-doctor we find that, as our corpus of actually occurring utterances grows, these two occur in almost the same environments, except for such sentences as An oculist is just an eye-doctor under a fancier name [...]. In contrast, there are many sentence environments in which oculist occurs but lawyer does not [...]."

And the rule he draws from it (verbatim, p. 157):

> "If A and B have almost identical environments except chiefly for sentences which contain both, we say they are synonyms: oculist and eye-doctor. If A and B have some environments in common and some not (e.g. oculist and lawyer) we say that they have different meanings, the amount of meaning difference corresponding roughly to the amount of difference in their environments."

(Note: the footnote attached to this example records that the oculist/eye-doctor pair was suggested by Y. Bar-Hillel, "who however considers that distributional correlates of meaning differences cannot be established" — p. 156, footnote 17, verbatim. Harris himself thus flags the contested status of the correlation in the founding paper.)

## Bearing on this project

- **[`concept/distributional-meaning`](../concepts/distributional-meaning.md).** This source is the primary the concept page names as "Harris (1954) supplies the formal distributional hypothesis." Before this page the concept cited Harris only as "not in-repo"; the concept page can now point at a read primary for "difference of meaning correlates with difference of distribution" rather than asserting the formulation second-hand.
- **The `distributional` tag's caveat.** The [`meaning-senses.md`](../../meaning-senses.md) entry for `distributional` calls it "The Firth/Harris tradition" and warns that distributional structure is "by itself, silent on reference and on truth." Harris's own framing is consistent with that caveat in a precise way: his correlation is between *meaning difference* and *distribution difference*, a within-language contrast, not a theory of how expressions hook onto the world. The Bar-Hillel footnote is the founding paper conceding that the correlation's evidential force is exactly what is contestable — which is the project's live tension, stated at the source.
- **Operationalization lineage.** Harris's "measure how similar are the selection approximations of any two words" (p. 157, in-text) is, read forward, the vector-space neighborhood / substitution-similarity measure the project uses as a distributional indicator. Citing Harris lets a probe that measures substitution behavior or neighborhood structure name its theoretical ancestor precisely rather than gesturing at "the distributional hypothesis."

## What it can ground

- The verbatim source-statement of the distributional hypothesis ("difference of meaning correlates with difference of distribution," p. 156) and Harris's claim that all linguistic elements are exhaustively describable by distribution (p. 146), for any page that needs the founding formulation rather than a paraphrase.
- The historical-conceptual point that distributional *meaning* in this tradition is a within-language contrast measure (meaning *difference* via distribution *difference*), not a reference- or truth-involving notion.
- The oculist/eye-doctor synonymy intuition as the canonical illustration, with Harris's own hedge (Bar-Hillel footnote) that the correlation may not be establishable as a law.

## What it cannot ground

- Any claim about LLMs, embeddings, or neural models: the paper predates all of it. It grounds the *theory* a model may instantiate, never a result about a model.
- Any reference- or truth-conditional claim: Harris's correlation is explicitly silent on whether distribution fixes what an expression refers to or whether a sentence is true.
- A claim that the distribution-meaning correlation is a settled empirical law: the paper itself records the contrary view (Bar-Hillel, footnote 17) and presents the correlation as something we "often find," not as proven.

## Known limits

- The locators here are the original *Word* page numbers (146-162) read from the scan's running headers; they are reliable for citation, but the scan is of the journal original, not the Taylor & Francis re-typeset of-record PDF, so a citing reader using the paywalled version should re-confirm a quote against their copy if exact line context matters.
- OCR/scan transcription: quotes were taken from text extracted from the scan. Long em-dashes, bracketed elisions, and the dropping of the footnote-reference superscript in the oculist passage are editorial (marked with [...] where material is omitted); the wording itself was checked against the extracted text but a citing session quoting at length should re-verify against the scan image.
- This is a 1954 structuralist paper in its own theoretical idiom ("selection," "environment," "morpheme class"); mapping its terms onto modern distributional-semantics vocabulary is interpretive and should be done explicitly, not silently.
