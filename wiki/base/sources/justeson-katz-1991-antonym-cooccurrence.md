---
type: source
id: justeson-katz-1991-antonym-cooccurrence
title: Co-occurrences of Antonymous Adjectives and Their Contexts
authors:
  - Justeson, John S.
  - Katz, Slava M.
year: 1991
venue: Computational Linguistics 17(1), pp. 1-20
url: https://aclanthology.org/J91-1001.pdf
access: open-access
meaning-senses:
  - distributional
status: received
created: 2026-06-29
updated: 2026-06-29
links:
  - rel: supports
    target: essay/antonymy-outlier-distributional-shadow
  - rel: refines
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: concept/distributional-meaning
---

# Justeson & Katz 1991 — Co-occurrences of Antonymous Adjectives and Their Contexts

## What it is

The **primary corpus-linguistic study** of *where* antonyms occur relative to each
other in text (following up, and extending, Charles & Miller's 1989 original co-occurrence counts —
J&K's own first contribution is the syntactic-context / frame analysis, §3, Table 3). John S. Justeson and Slava M. Katz (IBM T. J. Watson Research Center),
"Co-occurrences of Antonymous Adjectives and Their Contexts," *Computational Linguistics* 17(1),
pp. 1-20 (1991). Following up Charles & Miller (1989), the paper tests, on the 1-million-word tagged
**Brown Corpus**, the **co-occurrence hypothesis**: that the lexical association between antonymous
adjectives (e.g. *big–little*, *good–bad*) is formed because antonyms co-occur in the **same
sentence** far more often than chance — *not* (per the rival *substitutability hypothesis*) because
they are freely interchangeable in identical syntactic slots. Its two load-bearing empirical findings:
(1) antonymous adjectives co-occur sententially **much more often than expected by chance**, for all
frequent enough to test; and (2) when they co-occur, they overwhelmingly do so in **syntactically
parallel, lexically (near-)identical contrastive frames** — conjoined phrases ("X and Y") and repeated
phrases with one antonym substituted for the other — rather than scattered independently. This is the
primary source that establishes the *contrastive-frame saturation* of antonym pairs as a measured
corpus fact, not an intuition.

**Scope, stated up front (it bounds every use below):** the study is about **predicative adjectives**
in **one ~1961 American-English written corpus** (Brown), and its theoretical target is the
**psycholinguistics of human word-association acquisition** — *why* antonym pairs are each other's
top word-association responses. It is **pre-LLM** (1991) and says nothing about neural models. It
grounds a fact about the **distribution of antonyms in natural-language text** (the kind of signal a
distributional learner is trained on); it is **not** a human anchor for any LLM behavioral claim, and
its adjectival evidence does not, by itself, license the same claim about nominal relations.

## Provenance

The full text (20 pp.) was read from the open-access scan on the **ACL Anthology**
(`https://aclanthology.org/J91-1001.pdf`, fetched 2026-06-29). The scan carries an embedded OCR text
layer, extracted here with PyMuPDF (`fitz`). All quotes below were checked against that extracted
text; each carries the printed *Computational Linguistics* 17(1) page number read from the scan's
running footers (the first article page is p. 1). OCR/scan artifacts: the extracted layer hyphenates
words across line breaks (e.g. "syntac-" / "tically") and interleaves running headers/footers at page
boundaries; quotes are rendered de-hyphenated and re-joined, with any spanned page break noted. A
citing session quoting at length should re-confirm against the scan image. The article is the ACL/MIT
Press *Computational Linguistics* item; the ACL Anthology copy is the open-access route used.

## The hypothesis tested (verbatim, Abstract, p. 1)

> "Charles and Miller propose that lexical associations between antonymous adjectives are formed via
> their co-occurrences within the same sentence (the co-occurrence hypothesis), rather than via their
> syntactic substitutability (the substitutability hypothesis), and that such co-occurrences must take
> place more often than expected by chance."

And the paper's own headline result (verbatim, Abstract, p. 1):

> "We show that very high co-occurrence rates do appear to characterize all antonymous adjective
> pairs, supporting the precondition for the formation of the association; and we find that the
> syntactic contexts of these co-occurrences raise the intrinsic associability of antonyms when they
> do co-occur."

## Finding 1 — antonyms co-occur far above chance (verbatim, p. 3)

> "This paper confirms that, for all adjectives frequent enough to judge, antonymous adjectives do
> co-occur within the same sentence much more often than is expected by chance. On the other hand,
> something like the substitutability hypothesis must also be involved: when antonyms do co-occur,
> they usually substitute for one another in clausal or phrasal contexts that are otherwise
> word-for-word repetitions of each other, apart from pronominalization or ellipsis in some cases."

(Context: Charles & Miller had argued antonyms are *not* generally interchangeable — "Charles and
Miller (1989) dispute the substitutability of antonymous adjectives, showing that their sentential
contexts normally leave only one member of the pair plausible," p. 2 — so the substitution J&K find is
*within co-occurrence sentences*, not free global interchangeability.)

## Finding 2 — they co-occur in parallel, lexically identical contrastive frames

The structural characterization (verbatim, §3, p. 10):

> "in sentences containing both members of an antonym pair, the antonymic adjectives are usually
> syntactically paired, and in these cases they are commonly found in conjoined phrases that are
> identical or nearly identical, word for word, except for the substitution of one antonym for the
> other"

The trend and its size (verbatim, §3, p. 11; "syntactically" re-joined from the line-break
hyphenation "syntac-/tically"):

> "we find a strong trend for the antonyms to occur in syntactically parallel and usually lexically
> identical structures"

> "63% (139/219) of antonym co-occurrences are in lexically identical structures"

> "Fully 164 (75%) of these 219 co-occurrences appear in conjoined syntactic structures."

The summary of the mechanism (verbatim, §3 close, p. 13):

> "In summary, we have shown that antonyms co-occur sententially mainly by substituting for one
> another in otherwise identical or near-identical phrases."

(J&K's documented frames are **conjunction** of the two adjectives — "adjective conjunction
adjective", e.g. *cold and hot*, *large and small* — and **repeated noun/prepositional/predicate
phrases** with one antonym substituted for the other, optionally with deletion or pronominalization;
Table 3, pp. 11-12. The frame is *conjoined / repeated-and-substituted parallelism*. J&K do **not**
catalogue the specific strings "neither X nor Y" / "from X to Y" / "X versus Y" — those belong to a
later antonym-construction literature not in-repo.)

## The redefinition of antonymy it proposes (verbatim, §4.1, pp. 13-14)

J&K fold the distributional fact into the *definition* of antonymy — a lexical criterion added to the
semantic one (this sentence spans the printed pp. 13-14 page boundary in the scan):

> "we now characterize the co-occurrence phenomenon not simply in terms of its excess over chance
> expectation, but in terms of regular syntactic patterns that they exhibit"

> "To the semantic criterion for antonymy, opposition in meaning, we now add a lexical criterion:
> improbably frequent substitution in nearby, otherwise essentially identical phrases. Together, the
> semantic and lexical criteria define antonymy."

And — bearing directly on the project's *gradience* vocabulary — the lexical criterion is explicitly
graded (verbatim, footnote 13, p. 14):

> "The lexical criterion accommodates such uncertainty and gradability, since improbability and
> co-occurrence rate are graded factors."

## Bearing on this project

- **[`essay/antonymy-outlier-distributional-shadow`](../../findings/essays/antonymy-outlier-distributional-shadow.md)
  — the contrastive-frame premise now has a primary corpus anchor.** The essay's load-bearing
  characterization — "antonym pairs do not merely co-occur; they recur in tight, near-symmetric
  contrastive frames … and they substitute into very nearly identical environments" — was, before this
  page, grounded only in Harris's general form-internal contrast measure
  ([`source/harris-1954-distributional-structure`](harris-1954-distributional-structure.md)) plus the
  essay's own reasoning. J&K supply the *measured* version of exactly that claim: antonyms co-occur far
  above chance, and 63% of those co-occurrences are in lexically identical structures, 75% in conjoined
  structures. This `supports` the deflationary reading — antonymy is the relation most fully *written
  into* parallel contrastive co-occurrence — with a primary corpus study rather than an intuition. It
  fires the essay's **revision trigger (d)** ("a primary antonymy-distribution literature is ingested
  that bears on the contrastive-frame claim") in the **confirming** direction: it strengthens, not
  complicates, the characterization, while sharpening one phrase (see "What it cannot ground").
- **[`theory/lexicon-grammar-continuum`](../../findings/theory/lexicon-grammar-continuum.md) — the
  lexical pole's "maximally Harris-recoverable" gloss.** The continuum's lexical-pole subsection says
  antonym pairs "recur in tight, near-symmetric contrastive frames", reading antonymy as
  "maximally Harris-recoverable". J&K is the primary corpus evidence for the *recur in contrastive
  frames* half of that gloss; it `refines` the page by anchoring the characterization, **without**
  changing the gradient or any panel claim.
- **[`concept/distributional-meaning`](../concepts/distributional-meaning.md).** A concrete, measured
  instance of Harris's "difference of meaning correlates with difference of distribution": antonymy is
  a *contrast* relation that is densely and regularly inscribed in the distribution itself (conjoined
  and repeated-substituted frames), which is why a distributional learner recovers it cheaply.

## What it can ground

- The **corpus fact** that antonymous (predicative) adjectives co-occur in the same sentence far above
  chance, predominantly in conjoined and lexically-identical repeated/parallel contrastive frames with
  mutual substitution (Abstract, p. 1; pp. 3, 10-13) — the training-distribution premise the
  project's distributional-shadow argument leans on.
- The point that antonymy's distributional trace is **both** strong (production/recovery cheap) **and**
  non-discriminating against synonymy at the level of free substitution (Charles & Miller's
  "contexts normally leave only one member plausible", p. 2) — the source-level version of the
  essay's production-vs-discrimination split.
- That the antonymy "lexical criterion" J&K propose is **graded** ("graded factors", fn. 13, p. 14),
  consistent with the project's treatment of relation/sense structure as gradient.

## What it cannot ground

- **Any claim about LLMs, embeddings, or the project's panel.** The paper predates all of it; it
  grounds the *distributional fact a model could exploit*, never a model result. No transfer to
  claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash.
- **Free global substitutability of antonyms.** J&K (with Charles & Miller) explicitly *deny* that
  antonyms are interchangeable in single-member contexts; their substitution finding is **within
  co-occurrence sentences, in otherwise-identical repeated phrases**. The essay phrase "substitute into
  very nearly identical environments" must be read in *that* restricted sense (co-occurrence/repeated-
  frame substitution), not as global slot-interchangeability — a sharpening this source forces.
- **Nominal or non-adjectival relations.** The evidence is on **predicative adjectives** in the Brown
  Corpus. Extending "contrastive-frame saturation" to nominal antonymy (or to hyponymy/meronymy, as
  the continuum gradient does) is plausible but is an *extrapolation beyond J&K's data*, not something
  J&K measured.
- **A human-comparison anchor.** Its human-facing data are word-association response frequencies
  (Deese), used to motivate an acquisition theory — not graded human judgments of an LLM-comparable
  task. It is a theory/corpus source, not a `resource`.

## Known limits

- Single corpus (Brown, ~1M words, ~1961 written American English), adjectives only; the co-occurrence
  rates and the 63%/75% structural proportions are corpus- and POS-specific.
- The locators are printed *Computational Linguistics* 17(1) page numbers from the scan footers,
  reliable for citation; quotes were taken from the embedded OCR layer (hyphenation re-joined, page
  boundaries noted), so a length-sensitive re-quote should be re-checked against the scan image.
- The theoretical framing is a 1991 psycholinguistic-acquisition account ("association", "training",
  "alignment"); mapping its terms onto distributional-semantics or LLM-training vocabulary is
  interpretive and is flagged as the project's reading wherever used, never as a J&K claim.
