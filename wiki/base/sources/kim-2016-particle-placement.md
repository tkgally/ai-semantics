---
type: source
id: kim-2016-particle-placement
title: "Kim, Lee & Lee (2016) — A correlation analysis of English particle placement (native ICE-GB + East-Asian EFL writing; the definiteness and length direction facts)"
url: https://aclanthology.org/Y16-3005/
pdf: https://aclanthology.org/Y16-3005.pdf
license: "CC BY 4.0 (Creative Commons Attribution 4.0 International; ACL Anthology: \"Materials published in or after 2016 are licensed on a Creative Commons Attribution 4.0 International License\" — verified firsthand on the article landing page, 2026-07-14)"
citation: "Kim, H.-E., Lee, G.-H. & Lee, Y. (2016). A Correlation Analysis of English Particle Placement of Three East Asian EFL Learners' Writings. In Proceedings of the 30th Pacific Asia Conference on Language, Information and Computation (PACLIC 30): Posters, 347–354. Seoul, Korea. https://aclanthology.org/Y16-3005/"
created: 2026-07-14
updated: 2026-07-14
links:
  - rel: supports
    target: resource/particle-placement-givenness-human-anchor
---

# Source: Kim, Lee & Lee (2016) — English particle placement (definiteness + length direction facts)

**Ingested 2026-07-14 (session 224)** for the A5 production-side alternation battery (third sibling,
verb-particle placement). The ACL Anthology version was fetched firsthand (PDF, 8 pp., ~34 k characters
extracted with `pdfminer`); every quote below is verbatim from that extract (curly quotes rendered
straight; pdfminer line-break whitespace collapsed; one original typo kept `[sic]`). **License: CC BY
4.0**, verified firsthand on the landing page (the ACL Anthology blanket policy for 2016+ materials:
"Materials published in or after 2016 are licensed on a Creative Commons Attribution 4.0 International
License"), so it is in-scope for quotation and for anchoring an in-repo resource.

## What the paper is

A monofactorial **correlation study** of the English verb-particle (particle-placement) alternation,
comparing East-Asian EFL learners' writing (three slices of the TOEFL11 corpus) against a native-speaker
corpus (ICE-GB). From the abstract, the alternation itself — its example (1):

> "a. John picked up the book.
> b. John picked the book up."

And the design:

> "This paper examines the English particle placements of EFL learners' writings in three East Asian
> countries (Chinese, Japan, and Korea). Three parts of the TOEFL11 corpus were chosen, and all the
> sentences with particles were extracted. The ICE-GB was chosen as a native speakers' English. Then,
> eleven linguistic factors were manually encoded."

The native-speaker reference:

> "the ICE-GB corpus (the British component of the International Corpus of English; Nelson et al., 2002)
> was chosen for the native speakers' counterparts."

## The two constructions (the alternation mapping — load-bearing)

> "Here, construction0 refers to the sentences with the order of 'verb + particle + DO' as in (1a),
> while construction1 refers to the sentences with the order of 'verb + DO + particle' as in (1b)."

So **construction0 = the JOINED / continuous order** (V-Prt-DO, *picked up the book*) and
**construction1 = the SPLIT / discontinuous order** (V-DO-Prt, *picked the book up*). This mapping is
what makes the direction quotes below unambiguous.

## The direction facts (what this source anchors)

The paper states the native-speaker direction of two robust particle-placement constraints. Both are the
paper's own CC BY text, explicitly **summarizing Gries (1999:33)**'s synthesis of the prior descriptive /
corpus literature:

> "Gries (1999:33) closely investigated the claims in previous studies and summarized them as in Table 1."

**Definiteness of the direct object (the focal constraint for this probe):**

> "The factor DET, the fifth factor, refers to the determiner of the DO. If the determiner of DO is
> indefinite (such as a or an), native speakers tend to choose construction0 rather than construction1.
> If the determiner of DO is definite (such as the), native speakers prefer to use construction1 rather
> than construction0."

→ **indefinite / new object → JOINED (V-Prt-DO); definite object → SPLIT (V-DO-Prt).** Definiteness is
the grammaticalized marker of the object's discourse-givenness / identifiability, so this is the
information-structural direction: a **discourse-given / definite object favours the split order**.

**Length / weight of the direct object (the second, convergent-validity constraint):**

> "LENGTHW (the first factor in Table 1) refers to the length of DO in words. If the DO is long, native
> speakers tend to choose construction0 rather than construction1. If the DO is short, however, the
> native speakers tend to use construction1 rather tahn [sic] construction0."

→ **long / heavy object → JOINED; short object → SPLIT.** (The end-weight / domain-minimization
constraint — Lohse, Hawkins & Wasow 2004; here a second named human direction the panel can be checked
against.)

## The factor inventory (what a clean design must hold constant, and what discourse factors exist)

Table 1 (from Gries 1999) enumerates 18 factors; those the paper encodes include the object's **length**,
**determiner (definiteness)**, **type** (lexical / pronominal), **concreteness**, **animacy**,
**idiomaticity** of the VP, and a family of **discourse-mention** factors — "Distance to last mention of
the DO", "Times of preceding mention of the DO", "Last mention of the DO", "Cohesiveness of the DO to the
preceding discourse". So the discourse-givenness factors are catalogued in the same inventory as
definiteness; a probe isolating information-status must hold **object length, type (avoid pronouns —
pronominal objects are near-categorically split, not a graded contrast), concreteness, animacy, and VP
idiomaticity** constant across its given/new conditions.

## What this source can and cannot ground (for the probe)

- **Can ground** the *direction* of the definiteness / givenness constraint as a **license-verified,
  native-speaker-attributed fact**: a definite / discourse-given direct object favours the split
  (V-DO-Prt) order; an indefinite / new object favours the joined (V-Prt-DO) order. And the second
  convergent direction: a short object favours split, a long object favours joined. This is the asset
  catalogued as
  [`resource/particle-placement-givenness-human-anchor`](../resources/particle-placement-givenness-human-anchor.md).
- **Cannot ground** a **per-item human gradient** to regress the panel against. The paper reports
  aggregate monofactorial correlation coefficients on writing corpora, not a per-item human-rated
  gradient, and it releases no openly-licensed per-item data file. A per-item gradient is a **secondary**
  measure contingent on a separate license-verified dataset scout (verified null 2026-07-14: the classic
  particle-placement gradient corpora — Gries 2003; Grafmiller & Szmrecsanyi 2018 — are paywalled / carry
  no verifiable open license and are **not** adopted).
- **Cannot ground** any claim about model *representations* — only a behavioural probe.

## Provenance / honesty note

Unlike the genitive anchor ([`source/dubois-2023-genitive-animacy`](dubois-2023-genitive-animacy.md),
a fresh 25-native-speaker **rating experiment**), this paper is an **EFL-learner monofactorial corpus
study** whose stated native-speaker *directions* are a restatement of Gries (1999)'s synthesis of the
descriptive literature, corroborated by the paper's own native-speaker (ICE-GB) corpus. The direction it
supplies is **textbook-robust and uncontroversial** (definite / short → split is one of the most
established findings in the particle-placement literature), so it is a sound **direction anchor** for the
*sign* of the effect — but it is a restatement, not a novel human-rating dataset. This modesty-of-
provenance is recorded here and carried into the resource page and the open design decision as a caveat
the ratification must weigh; it is exactly why the probe is anchored on the **direction only**, with no
per-item human-gradient or human-level claim. Quotes verified verbatim 2026-07-14 from the extracted
ACL Anthology PDF; page numbers 347–354 per the Anthology landing metadata.
