---
type: source
id: brennan-clark-1996-conceptual-pacts
title: Conceptual Pacts and Lexical Choice in Conversation
authors:
  - Brennan, Susan E.
  - Clark, Herbert H.
year: 1996
venue: "Journal of Experimental Psychology: Learning, Memory, and Cognition, Vol. 22, No. 6, 1482-1493"
url: https://profgerhard.de/sfs/lehre/ws0708/spieltheorie/Brennan&Clark_96.pdf
access: author/course-site mirror (publisher paywalled)
meaning-senses:
  - relational
  - referential
  - human-comparison
status: received
created: 2026-06-12
updated: 2026-06-12
links:
  - rel: refines
    target: concept/relational-meaning
---

# Brennan & Clark 1996 — Conceptual Pacts and Lexical Choice in Conversation

## What it is

The canonical experimental paper on **conceptual pacts**: three matching-task experiments showing that lexical entrainment in human conversation is **historical** (driven by precedents built up in the interaction) and **partner-specific** (indexed to the particular addressee with whom a conceptualization was grounded), not merely a by-product of informativeness, lexical availability, or salience. This is the human-side result the project's relational-meaning axis contrasts LLM dyad behavior against; it was queued at P2 in [`base/wanted.md`](../wanted.md) as the anchor IOU named by the commutative-convention conjecture.

## Provenance

- Fetched 2026-06-12 from the long-standing course-site mirror noted in [`base/wanted.md`](../wanted.md): `https://profgerhard.de/sfs/lehre/ws0708/spieltheorie/Brennan&Clark_96.pdf` (1.4 MB scanned-typeset PDF; the APA publisher route is paywalled).
- Verified against the PDF masthead: title **"Conceptual Pacts and Lexical Choice in Conversation"**; authors **Susan E. Brennan** (State University of New York at Stony Brook) and **Herbert H. Clark** (Stanford University); journal line "Journal of Experimental Psychology: Learning, Memory, and Cognition, 1996, Vol. 22, No. 6, 1482-1493"; copyright 1996 American Psychological Association. This is the JEP:LMC paper, **not** Brennan 1996 "Lexical entrainment in spontaneous dialog" (the distinct conference paper wanted.md warned about) — both authors, the journal header, and the 1482–1493 pagination are all present in the document itself.
- Text extracted with `pdftotext`; all quotes below were checked against that extraction, with page locators taken from the journal's printed page numbers. Two transcription caveats: (a) the extraction occasionally drops spaces around italic ligatures (e.g. "morefirmlyestablished" for "more firmly established"); such obvious extraction artifacts are repaired in the quotes; (b) the print's italics on example terms (*the loafer*, *fish*) are not preserved by extraction and are not reconstructed here.

## Abstract (verbatim, p. 1482)

> When people in conversation refer repeatedly to the same object, they come to use the same terms. This phenomenon, called lexical entrainment, has several possible explanations. Ahistorical accounts appeal only to the informativeness and availability of terms and to the current salience of the object's features. Historical accounts appeal in addition to the recency and frequency of past references and to partner-specific conceptualizations of the object that people achieve interactively. Evidence from 3 experiments favors a historical account and suggests that when speakers refer to an object, they are proposing a conceptualization of it, a proposal their addressees may or may not agree to. Once they do establish a shared conceptualization, a conceptual pact, they appeal to it in later references even when they could use simpler references. Over time, speakers simplify conceptual pacts and, when necessary, abandon them for new conceptualizations.

## Summary

- **Task.** Pairs (director + matcher) repeatedly match cards depicting objects across trial blocks A, B, C; card sets manipulate whether targets are lone exemplars of their basic-level category (so a bare basic-level term suffices) or have within-category competitors (so subordinate or modified terms are needed).
- **Experiment 1** compares an ahistorical informativeness model against historical models (recency alone vs. recency + frequency). **Experiment 2** alternates the director/matcher roles, testing whether a partner-introduced conceptualization is as effective a precedent as a self-introduced one (it is — pacts are "accessible to both speakers and addressees," p. 1492), and tracks hedging (*kind of*, *sort of*) as a mark of provisionality. **Experiment 3** switches the matcher mid-task: directors continuing with the same matcher keep using established (even overinformative) terms; directors facing a new matcher revert toward bare basic-level terms.
- **Headline numbers (Exp. 3, p. 1491):** directors used the same terms in trial C1 as in B4 48% of the time with the same matcher vs. 18% after a matcher switch; unadorned basic-level terms rose only 15→23% over C trials with the same partner but 20→55% with a new partner.
- **Conclusion:** a historical, interactive model — speakers and addressees jointly establish provisional, partner-indexed agreements ("conceptual pacts") on how a referent is to be conceptualized, and later lexical choice appeals to those pacts.

## Key passages (verbatim, with page locators)

**The definition of a conceptual pact (§Partner Specificity, p. 1484):**

> "The idea is that when speakers and addressees ground a reference, they are creating a conceptual pact, a temporary agreement about how the referent is to be conceptualized."

**Lexical entrainment defined as a consequence of pacts (General Discussion, p. 1491):**

> "Once they establish a conceptual pact, either partner can appeal to it in referring to the shoe a second, third, or fourth time. One consequence is lexical entrainment, the repeated use of the same or closely related terms in referring to an object on successive occasions."

**Partner-specificity — the Experiment 3 result (p. 1491):**

> "In summary, Experiment 3 shows a partner-specific effect on repeated referring. Speakers with continuing addressees appeal to conceptual pacts they have already established, even when these are overinformative. Speakers faced with new addressees sometimes begin by proposing the conceptualizations they have established with previous addressees, but they rapidly accommodate to their new addressees."

**The historical-over-ahistorical verdict (General Discussion, p. 1492):**

> "What we have shown, then, is that lexical entrainment in conversation is better accounted for by conceptual pacts than by informativeness or by recency alone. In our proposal, people establish, track, and update conceptual pacts (i.e., provisional agreements about how they are to conceptualize things)."

**The shape of the history-dependence — frequency over recency (General Discussion point 3, p. 1492):**

> "We have assumed that the more times two people refer to an object, the stronger any resulting conceptual pact is likely to be. So the more firmly two partners establish a pact, the more likely they are to appeal to it later, and to appeal to it with confidence. Frequency of use better explains our data than does simple recency."

## What this bears on in-repo

- **Converts the human leg of the conceptual-pact contrast from characterization to citable ground.** [`essay/aggregation-not-constitution`](../../findings/essays/aggregation-not-constitution.md) and [`conjecture/commutative-convention`](../../findings/conjectures/commutative-convention.md) both flagged Brennan & Clark 1996 as "characterized, not read in-repo," with an explicit revision trigger: fetching it must replace the hedges with quotes. The quotes are now in-repo. The characterization holds up **on partner-specificity**: *who* a term was fixed with demonstrably matters to later lexical choice (Exp. 3, p. 1491 quote above), and pacts are established **jointly and interactively** — "establishing a precedent in conversation requires interaction" (p. 1484) — exactly the interaction-borne texture [`concept/relational-meaning`](../concepts/relational-meaning.md) asks about.
- **A precision the conjecture page must absorb: this paper grounds historicity and partner-indexing, not order/path-dependence in the project's commutativity sense.** The paper never scrambles or reorders an interaction history; its historical variables are *frequency* of establishment (number of A/B trials) and *recency*, and it explicitly finds "Frequency of use better explains our data than does simple recency" (p. 1492). Frequency is an order-insensitive statistic of the record. So the predicted human/LLM contrast in [`conjecture/commutative-convention`](../../findings/conjectures/commutative-convention.md) — "humans non-commutative, LLM dyads commutative" — is now grounded on the **partner axis** (a fresh human partner really does reset the pact, the direct analogue of the pilot's fresh-matcher design) but remains **ungrounded on the trajectory-scrambling axis**: no human experiment in this paper tests whether the *order* of a fixed set of prior references matters. If anything, frequency-over-recency mildly cautions against assuming strong sequence-position effects in humans. Per the essay's standing trigger, the human-contrast clause should be rewritten to claim partner-specificity (citable here) rather than order-sensitivity (still untested on the human side).
- **Grounds the entrainment/shortening baseline lineage.** The paper's framing — "With partners, but not with tape recorders, repeated references tend to become shorter and more efficient" (p. 1484, citing Krauss & Weinheimer 1964, 1966) — is the same compression phenomenon the pilot's anchored secondary finding measures against [`resource/hawkins-tangrams`](../resources/hawkins-tangrams.md), and the same human curve that [`source/imai-2025-vlm-common-ground`](imai-2025-vlm-common-ground.md) finds VLM dyads failing to reproduce. The two model-side results (no compression, little reuse of established shorthand) can now be stated against the original pact account rather than a paraphrase of it.
- **Provisionality and joint establishment as observables.** Hedging as a mark of provisional conceptualization (Exp. 2; General Discussion point 2, pp. 1491–1492) and ratify/modify/solicit moves in grounding (p. 1484) are concrete, human-documented interaction behaviors a future dyad probe could code for — candidate operationalizations for the "pact-like texture" the relational axis currently lacks on the model side.

## What it can ground

- Human partner-specificity of referential precedents (Exp. 3 figures and quote, p. 1491).
- Human reliance on established pacts even when overinformative (loafer kept where shoe would do), and reversion to basic-level terms with new partners (Table 5, p. 1491).
- The joint, interactive establishment of conceptualizations (General Discussion point 1, p. 1491), and the frequency-graded strength of pacts (point 3, p. 1492).

## What it cannot ground

- Any claim about **order/trajectory-scrambling** in humans — no such manipulation exists in the paper; the live-vs-shuffled discriminator remains the project's own, humanly unanchored, wedge.
- Corpus-scale or population-scale convention claims — dyads in a laboratory matching task, mostly student participants, English only.
- Any model-side claim, obviously; it is purely human data from 1996.

## Known limits

- Scanned-typeset PDF via a third-party course mirror; quotes were verified against `pdftotext` extraction of that scan, with extraction-spacing artifacts repaired as noted under Provenance. Page locators use the journal's printed pagination (1482–1493).
- The paper's own statistics are 1990s ANOVA-by-subjects/items; effect sizes by modern standards are not recoverable from the reported F-tests alone.
