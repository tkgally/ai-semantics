---
type: source
id: dubois-2023-genitive-animacy
title: "Dubois, Grafmiller, Paquot & Szmrecsanyi (2023) — Animacy effects in the English genitive alternation (native-speaker ratings vs corpus)"
url: https://doi.org/10.1017/langcog.2023.51
pdf: https://pure-oai.bham.ac.uk/ws/portalfiles/portal/214001831/animacy-effects-in-the-english-genitive-alternation-comparing-native-speakers-and-efl-learner-judgments-with-corpus-data.pdf
license: CC BY 4.0 (Creative Commons Attribution; "© The Author(s), 2023. Published by Cambridge University Press. This is an Open Access article, distributed under the terms of the Creative Commons Attribution licence (http://creativecommons.org/licenses/by/4.0)")
citation: "Dubois, T., Grafmiller, J., Paquot, M. & Szmrecsanyi, B. (2023). Animacy effects in the English genitive alternation: comparing native speakers and EFL learner judgments with corpus data. Language and Cognition (2023), 1–23. https://doi.org/10.1017/langcog.2023.51"
created: 2026-07-13
updated: 2026-07-13
links:
  - rel: supports
    target: resource/genitive-animacy-human-anchor
---

# Source: Dubois et al. (2023) — animacy in the English genitive alternation

**Ingested 2026-07-13 (session 217)** for the A5 production-side alternation battery (genitive
sibling). The publisher's version of record (Cambridge University Press, *Language and Cognition*)
was fetched from the University of Birmingham open repository and the body text extracted firsthand
(`pdfminer`); every quote below is verbatim from that extract. **License: CC BY 4.0** (stated on the
article's first page — see front matter), so it is in-scope for quotation and for anchoring an
in-repo resource.

## What the paper is

A rating-task experiment comparing native-speaker and EFL-learner acceptability intuitions about the
English genitive alternation against corpus-based production models. From the abstract (p. 1):

> "In this study, we investigate this interface further by conducting a rating task experiment on the
> intuitions of 25 native speakers and 101 low–intermediate to advanced learners of English as a
> Foreign Language regarding the acceptability of the genitive variants (the beauty of nature/nature's
> beauty) in different contexts. These ratings were then compared against existing corpus-based
> statistical models that predict which variant is most likely in spoken language use with two
> mixed-effects linear regression models."

The two genitive variants (their examples 1–2, p. 2):

> "(1) the people's<sub>possessor</sub> mentality<sub>possessum</sub> (TLC:2_IN_11)
> (2) the mentality<sub>possessum</sub> of the people<sub>possessor</sub> (TLC:2_6_ME_69)"

— i.e. the **s-genitive** (*the people's mentality*, possessor first) vs the **of-genitive** (*the
mentality of the people*, possessum first).

## The direction of the animacy effect (the load-bearing fact this source anchors)

> "Both native speakers and learners are also sensitive to possessor animacy, which captures the
> tendency for animate possessors to favour the s-genitive and inanimate possessors to prefer the
> of-genitive."

So the human-rated direction is: **animate possessor → s-genitive** (*the judge's decision*),
**inanimate possessor → of-genitive** (*the decision of the court*). Animacy is the paper's focal
constraint, and it names it the strongest one in the alternation literature:

> "While animacy is normally the strongest constraint of the genitive alternation (Rosenbach, 2014),
> Dubois et al. (2023) found that B1 speakers are more likely than native speakers to use the
> s-genitive when the possessor is inanimate, whereas B2 speakers are more likely than native speakers
> to use the of-genitive when the possessor is animate…"

The animacy coding scheme (five levels, from Zaenen et al. 2004):

> "Dubois et al. (2023) originally distinguished between five animacy levels based on the coding scheme
> of Zaenen and colleagues (Zaenen et al., 2004; see also Wolk et al., 2013), namely animate,
> collective, inanimate, locative, and temporal possessors. Animate possessors 'mostly concern humans
> or entities represented as humans and animals' (e.g. god's plan)…"

## The other constraints (what a clean animacy probe must hold constant)

Native speakers and learners are, in the corpus model, jointly sensitive to a battery of constraints;
a probe isolating **animacy** must neutralize the rest:

> "…both are sensitive to structural persistence (e.g. Bock, 1982; Szmrecsanyi, 2006), the length of
> the possessor and the possessum, the final sibilancy of the possessor, and the lexical density of
> the surrounding context (Dubois et al., 2023, p. 443)."

And, in the rating-experiment write-up:

> "According to the reference corpus model, the choice of genitive variant is also influenced by the
> definiteness and the final sibilancy of the possessor, the length of the possessor and the possessum,
> the lexical density of the [surrounding context]…"

So the named covariates to control are: **possessor length**, **possessum length**, **final sibilancy
of the possessor** (a possessor ending in a sibilant — *the boss's*, *the church's* — independently
disfavours the s-genitive), **definiteness**, structural persistence (priming), and lexical density.

## The human anchor's shape (a graded acceptability rating, midpoint 50)

The native-speaker task rated variant acceptability on a scale whose neutral midpoint is **50**:

> "…we compared to what extent the ratings of A2/B1, B2, and native speakers deviated from the middle
> point of the rating scale, namely 50. For example, if a learner gave a rating of 75 for the
> s-genitive, the deviation from 50 is 25."

Fifteen target experimental items were used:

> "After the 15 target experimental items, participants answered the remaining 35 items from the Oxford
> Quick Placement Test."

## Human ratings track the corpus production surface (the concordance)

> "Overall, the intuitions from the participants in the experiment correlate with the patterns of
> language use of the speakers in the corpus, which provides additional evidence that the participants
> are sensitive to the significant probabilistic constraints included in the reference c[orpus model]."

The corpus reference is the Trinity Lancaster Corpus (TLC):

> "…they collected 2302 genitive observations in the Trinity Lancaster Corpus (TLC, Gablasova et al.,
> 2019), a three-million-word corpus consisting of transcribed recordings from an official spoken
> language examination…"

## What this source can and cannot ground (for the probe)

- **Can ground** the *direction* of the animacy effect as a **human-rated fact** (25 native speakers,
  graded acceptability, midpoint-50 scale): animate possessor → s-genitive, inanimate → of-genitive.
  This is a genuine human-comparison anchor (like the AANN acceptability gradient), not a within-model
  contrast. It is the asset catalogued as
  [`resource/genitive-animacy-human-anchor`](../resources/genitive-animacy-human-anchor.md).
- **Cannot ground, from the paper alone,** a **per-item human gradient** to regress the panel against:
  the paper reports the aggregate rating-vs-corpus concordance and mixed-effects coefficients, and its
  per-item native-speaker ratings / the TLC corpus rows are **not** shown to be openly licensed here
  (TLC is a controlled research corpus). A per-item corpus-production or per-item rating gradient is a
  **secondary** measure contingent on a separate license-verified dataset scout (see the resource
  page's "what it cannot ground" and the open design decision).
- **Cannot ground** any claim about model *representations* — only a behavioural probe.

## Provenance note

Quotes verified verbatim 2026-07-13 from the extracted publisher PDF (485 KB, 83 k characters of body
text; the University of Birmingham repository "General rights" boilerplate is superseded by the CC BY
licence explicitly displayed above it — "Where a licence is displayed above, please note the terms and
conditions of the licence govern your use of this document"). Page numbers are given where the running
header made them unambiguous; several quotes are from the un-paginated online-first extract and are
located by section instead.
