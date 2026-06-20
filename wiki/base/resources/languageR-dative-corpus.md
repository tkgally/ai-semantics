---
type: resource
id: languageR-dative-corpus
title: Bresnan et al. (2007) dative-alternation corpus (languageR::dative)
status: external-only
url: https://cran.r-project.org/web/packages/languageR/
data: https://cran.r-project.org/src/contrib/languageR_1.6.tar.gz
docs: https://rdrr.io/cran/languageR/man/dative.html
license: GPL-2 | GPL-3 (the languageR package; verified on CRAN 2026-06-20, version 1.6, 2025-06-10)
citation: Bresnan, J., Cueni, A., Nikitina, T. and Baayen, R. H. (2007) Predicting the dative alternation, in Bouma, G. and Kraemer, I. and Zwarts, J. (eds.), Cognitive Foundations of Interpretation, Royal Netherlands Academy of Sciences, 33 pages, in press.
created: 2026-06-20
updated: 2026-06-20
links:
  - rel: anchors
    target: conjecture/dative-alternation-information-structure
---

# Bresnan et al. (2007) dative-alternation corpus — `languageR::dative`

## What it is

The `dative` data frame shipped with the R package **languageR** (Baayen; CRAN
version 1.6, 2025-06-10; license GPL-2 | GPL-3). Per the package documentation
([rdrr.io mirror](https://rdrr.io/cran/languageR/man/dative.html), fetched and
verified verbatim 2026-06-20):

> "Data describing the realization of the dative as NP or PP in the Switchboard
> corpus and the Treebank Wall Street Journal collection."

> "A data frame with 3263 observations on the following 15 variables."

So each row is **one attested ditransitive clause** (spoken Switchboard or written
WSJ), hand-coded for a set of explanatory factors plus the **outcome** — whether
the speaker/writer realized the recipient as an NP (the double-object construction,
*Mary gave John the book*) or as a PP (the prepositional dative, *Mary gave the book
to John*). This is **human production data** (attested choices in natural
discourse), not per-item acceptability ratings (for the rating complement see the
"Companion rating anchor" note below).

## The 15 variables (from the package documentation)

Transcribed faithfully from the package `Format` block (identifiers set in code
font for readability; wording and factor levels unchanged):

- `Speaker` — "a factor coding speaker; available only for the subset of spoken English."
- `Modality` — "a factor with levels `spoken`, `written`."
- `Verb` — "a factor with the verbs as levels."
- `SemanticClass` — "a factor with levels `a` (abstract: 'give it some thought'), `c` (communication: 'tell, give me your name'), `f` (future transfer of possession: 'owe, promise'), `p` (prevention of possession: 'cost, deny'), and `t` (transfer of possession: 'give an armband, send')."
- `LengthOfRecipient` — "a numeric vector coding the number of words comprising the recipient."
- `AnimacyOfRec` — "a factor with levels `animate` and `inanimate` for the animacy of the recipient."
- `DefinOfRec` — "a factor with levels `definite` and `indefinite` coding the definiteness of the recipient."
- `PronomOfRec` — "a factor with levels `nonpronominal` and `pronominal` coding the pronominality of the recipient."
- `LengthOfTheme` — "a numeric vector coding the number of words comprising the theme."
- `AnimacyOfTheme` — "a factor with levels `animate` and `inanimate` coding the animacy of the theme."
- `DefinOfTheme` — "a factor with levels `definite` and `indefinite` coding the definiteness of the theme."
- `PronomOfTheme` — "a factor with levels `nonpronominal` and `pronominal` coding the pronominality of the theme."
- `RealizationOfRecipient` — "a factor with levels `NP` and `PP` coding the realization of the dative." **(the outcome variable)**
- `AccessOfRec` — "a factor with levels `accessible`, `given`, and `new` coding the accessibility of the recipient."
- `AccessOfTheme` — "a factor with levels `accessible`, `given`, and `new` coding the accessibility of the theme."

## What it can ground

The conjecture [`conjecture/dative-alternation-information-structure`](../../findings/conjectures/dative-alternation-information-structure.md)
predicts that panel LLMs' dative-realization preferences are sensitive to
**information structure** (given/old before new; pronominal recipients favor the
double-object form), not merely to surface frequency. This dataset supplies the
exact human-side signal that prediction needs:

- The **information-structure factors** are coded directly: `AccessOfRec` /
  `AccessOfTheme` (given / accessible / new), `PronomOfRec` / `PronomOfTheme`,
  `DefinOfRec` / `DefinOfTheme`.
- The **confounds the design must control** are coded too: `LengthOfRecipient` /
  `LengthOfTheme` (the length-vs-givenness confound — given material tends to be
  shorter), `AnimacyOfRec` / `AnimacyOfTheme`.
- The **human outcome** is `RealizationOfRecipient` (NP=DOC vs PP=PD). The
  canonical Bresnan et al. (2007) result is a logistic-regression model that
  predicts this outcome from the factors above with high accuracy — so the human
  "gradient" available from this corpus is the **model-predicted probability of
  PP/NP per factor configuration**, i.e. an aggregate production-probability
  surface, *not* a direct per-item naturalness rating.

What it **cannot** ground on its own:

- A claim that the model's preferences match **graded per-item human acceptability**
  — that is the rating anchor's job (see below), not the corpus's. The corpus
  grounds production *probability*, which is a different (if correlated) human
  signal. Conflating the two is the operationalization trap the open decision
  fences off.
- Anything about **model representations** — the conjecture's behavioral probe is
  the only thing this resource can back.
- Anything cross-linguistic — the dative alternation in this exact NP/PP form is
  English-specific.

## Known limits / cautions

- **Production, not judgment.** Corpus realization is the speaker's *choice in
  context*, shaped by processing and discourse pressures; it is the right anchor
  for "does the model's production preference track the human production surface",
  the wrong anchor for "does the model rate sentences the way humans rate them".
- **Length and givenness are correlated in the corpus** (given/pronominal material
  is typically shorter). A probe that wants to attribute a preference shift to
  *information structure* rather than to *length* must dissociate them in its
  stimuli — this is the load-bearing control, surfaced in the open decision.
- **Memorization / contamination risk.** The attested corpus sentences (especially
  WSJ) may sit in the panel models' training data. A clean probe should use
  **synthetic minimal pairs** built to the corpus's factor structure rather than
  lifting corpus sentences verbatim; the corpus then anchors the *factor → outcome*
  relationship, not specific items.
- **GPL data, recipe-not-corpus posture.** Like the other in-repo anchors, the
  build session should mirror the package tarball to `experiments/data/` (gitignored),
  inspect/checksum the `dative.rda` (requires R or a librdata reader), and commit
  only derived tables. Reading the `.rda` is a build-time step (no R in the
  cataloguing environment, 2026-06-20).

## Companion rating anchor (option, not yet verified)

Bresnan & Ford (2010), "Predicting Syntax: Processing Dative Constructions in
American and Australian Varieties of English" (*Language* 86.1), ran a **gradient
sentence-rating** experiment: native speakers distribute 100 points across the two
dative variants by perceived naturalness, and Bresnan et al. report that these
human gradient ratings correlate well with the corpus-model probabilities. *(This
description is characterized from secondary summaries and the paper's abstract; the
paper PDF could not be text-extracted in the cataloguing environment, so no body
quotes are recorded here — verbatim verification is deferred to whichever session
adopts the rating anchor.)* If its per-item data proves fetchable and licensed, it
is the more direct anchor for the conjecture's *graded-acceptability* clause; this
is one arm of the open operationalization decision
([`decisions/open/dative-anchor-and-indicator`](../../decisions/open/dative-anchor-and-indicator.md)).

## Pointer for next visit

- Status `external-only`: documented and license-verified from the authoritative
  CRAN package, tarball fetchability confirmed (HTTP 200, 2026-06-20), but the data
  rows are **not yet mirrored or inspected firsthand**. The build session promotes
  this to `catalogued` after mirroring + row inspection (3263 × 15 confirmed
  firsthand, factor levels confirmed).
- The instrument that will consume this anchor is governed by
  [`decisions/open/dative-anchor-and-indicator`](../../decisions/open/dative-anchor-and-indicator.md)
  — ratifiable, at the earliest, the session after the one that opened it.
