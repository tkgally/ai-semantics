---
type: resource
id: homonym-meaning-dominance-norms
title: "Homonym meaning-dominance norms (British eDom 2016; Spoken-ambiguity dominance norms, J. Cognition 2023) — per-WORD human sense-balance for selecting balanced homonyms"
status: verified
url: https://openpsychologydata.metajnl.com/articles/10.5334/jopd.28
paper: "Maciejewski, G. & Klepousniotou, E. 2016. Relative Meaning Frequencies for 100 Homonyms: British eDom Norms. J. Open Psychology Data 4(1), DOI 10.5334/jopd.28. — Companion: Dominance Norms and Data for Spoken Ambiguous Words in British English, J. Cognition, DOI 10.5334/joc.194 (author list per the article page; cited by DOI)."
license: "CC BY 4.0 (both datasets) — verified verbatim 2026-06-23 from the two article pages."
meaning-senses:
  - referential
  - human-comparison
contingent-on: []
created: 2026-06-23
updated: 2026-07-06
links:
  - rel: depends-on
    target: concept/polysemy
---

# Homonym meaning-dominance norms — per-word human sense-balance

> **Status: verified (scouted 2026-06-23 s92; regraded `scouting → verified` 2026-07-06, s184,
> wiki-coherence campaign P2).** Both datasets' licenses (CC BY 4.0), reachability (OSF +
> open-access journal), and the load-bearing schema facts were verified by direct fetch (s92), and
> both norm CSVs were **downloaded from OSF and used firsthand in session 94, 2026-06-23** to build
> the forced-both v2 frozen subset — so the front-matter now reads `verified`, matching the WordNet
> resource's grade (license + reachability + schema verified from the artifact, and used). *(The
> original s92 wording read "Neither has been fetched/checksummed/mirrored in-repo, and no probe yet
> uses them"; that was superseded s94 — see "Verification status" below — and the front-matter
> `scouting` had lagged it until this P2 regrade.)* They are
> catalogued together because they are the same *kind* of signal — **per-word human meaning-dominance**
> from which a researcher can select *balanced* homonyms — and because that signal is **a better-anchored
> version of the general-usage balance proxy** the session-91 forced-both build attempt used (SemCor tag
> counts), **not** a fix for that attempt's structural blocker (see "what it cannot ground").

## What they are

Two open, human-normed datasets of English **homonym meaning-dominance** — for each homonym, how the
probability mass of "which meaning a person reaches for" is distributed across its meanings:

- **British eDom** (Maciejewski & Klepousniotou 2016, *J. Open Psychology Data*, 10.5334/jopd.28): **100
  homonyms**, normed by **100 native British-English speakers** (plus 30 in a meaning-relatedness
  pre-test). Participants were asked to "estimate, as a percentage, how often each meaning of a homonym
  was implied when they encountered that word" (verbatim). The British counterpart to the original eDom
  norms (Armstrong, Tokowicz & Plaut 2012, 544 US-English homonyms — whose open copy could **not** be
  confirmed fetchable this session; Springer paywalled, KiltHub 403).
- **Spoken-ambiguity dominance norms** (*J. Cognition*, 10.5334/joc.194): **182 words** with ≥100 valid
  responses (243 total), word-association based. Reports a per-word **Dominance** (proportion for the most
  frequent meaning), an information-theoretic **U** value, and a **D** value.

## The human signal — what bears, and its grain

The relevant property: a **per-word, human, model-independent** measure of sense balance, on a continuum
from *dominant* (one meaning carries most of the mass) to *balanced* (mass split evenly). The
spoken-ambiguity norms make the balanced-selector explicit:

> "D values near 0 indicate that the item is balanced, i.e. the two most common meanings are similar in
> frequency. D values near 1 indicate that the item is biased, i.e. the most common (dominant) meaning is
> much more frequent than the next most common meaning." (*J. Cognition* 10.5334/joc.194, verified
> 2026-06-23)

British eDom states the matching use case directly: researchers can "compile and match sets of homonyms
with balanced and unbalanced meaning frequencies" (verbatim). So either set lets a build **select
homonyms that are balanced in general usage**, with a real human anchor — strictly better-grounded than
the SemCor tag-count proxy of the session-91 attempt (which was both too sparse, 1/8 candidates powered,
and US-corpus-bound).

**The decisive limit, stated up front:** both measure **general per-word** balance, elicited in
**isolation / word-association without sentence context** — "Word association is typically used as the
test because it provides a measure of the participants' interpretation in the absence of any biasing,
pre-determined context" (*J. Cognition* 10.5334/joc.194, verified verbatim 2026-06-23).

## What they can / cannot ground

- **Can:** selection of **general-usage-balanced homonyms** with a per-word human anchor (a CC BY 4.0
  upgrade over SemCor for that purpose); a human-anchored balance/dominance variable for any probe that
  needs one at the **word** grain. Potentially relevant to the matched-ambiguity sibling's reserved
  Option-A homonym sense-anchor
  ([`decisions/resolved/matched-ambiguity-kind-cross-level`](../../decisions/resolved/matched-ambiguity-kind-cross-level.md),
  Q2-a) for *balance* (not for same/different sense labels).
- **Cannot:** certify the **in-item** balance of a **specific sentence** — which is exactly the
  forced-both gate's Q1-ii requirement. A homonym balanced in **general usage** can still **lean in its
  specific sentence**, because (per the session-91 attempt's structural finding) a co-predication frame's
  in-item balance "is set by the *relative pull of the two complements*"
  ([`result/forced-both-lexical-build-attempt-v1`](../../findings/results/forced-both-lexical-build-attempt-v1.md)),
  which no general-usage statistic sees. So these norms **soften but do not eliminate** the Q1-ii gap;
  they re-supply, with a better anchor, the general-balance proxy that attempt already judged
  insufficient. They are **not** a co-activation resource (use
  [`resource/semeval2017-pun-corpus`](semeval2017-pun-corpus.md) for that) and carry no same/different
  per-item sense label.

## License (verbatim) and where they live

> "CC BY 4.0" (both article pages, verified 2026-06-23).

CC BY 4.0 — permissive, attribution-only; reuse and adaptation permitted (commercial included). No NC
restriction (unlike [`resource/semeval2017-pun-corpus`](semeval2017-pun-corpus.md)).

- British eDom: article https://openpsychologydata.metajnl.com/articles/10.5334/jopd.28 ; data OSF
  `osf.io/7k3eh` (verified reachable; **not yet fetched in-repo** *[stale — fetched + used firsthand
  session 94; see "Verification status" below]*).
- Spoken-ambiguity dominance norms: article DOI 10.5334/joc.194 ; data OSF `osf.io/uy47w` (verified
  reachable; **not yet fetched in-repo** *[stale — fetched + used firsthand session 94; see
  "Verification status" below]*).

## Verification status (honest)

- **Verified session 92 by direct fetch:** both CC BY 4.0 licenses; the item/rater counts (British eDom
  100/100; spoken-ambiguity 182 words); the D-value "near 0 = balanced" definition; the eDom "estimate …
  how often each meaning … was implied" instruction; the "balanced and unbalanced" matching statement;
  the word-association-in-isolation method.
- **Data files DOWNLOADED + USED firsthand (session 94, 2026-06-23).** The two norm CSVs were fetched
  from OSF this session — `British eDom norms - Norms File.csv` (OSF node `7k3eh`, file `pmbkm`, 19,219
  bytes) and `RoddGilbert_WA_Dominance_Norms.csv` (OSF node `uy47w`, file `2mduw`, 72,571 bytes; the
  spoken set is **Rodd & Gilbert**, author names now confirmed from the filenames) — and used to compute
  the [`result/forced-both-lexical-build-attempt-v2`](../../findings/results/forced-both-lexical-build-attempt-v2.md)
  frozen subset. They were not mirrored in-repo (CC BY 4.0 permits it, but only the *derived* balance
  values are committed, in the design's `frozen_subset.json`).
- **Cross-norm disagreement noted (session 94).** On the 5 words present in *both* sets within the v2
  pun intersection (`calf`, `fan`, `mail`, `plot`, `pupil` → 11 items), the two human word-grain
  instruments **disagree on the balanced/biased classification 11/11** (e.g. `calf` eDom min/total 0.476
  = balanced but spoken D 0.605 = biased). The two norms measure related-but-distinct things (an
  isolation-percentage estimate vs a word-association dominance) on different populations, so some
  divergence is expected — but it bounds how much weight a *single* word-grain balance flag can carry,
  and reinforces the "word-grain, not sentence-grain" limit below.
- **Reported but not re-verified verbatim in-repo:** the original (US) eDom 544-homonym norms' open
  fetchability (could **not** be confirmed session 92; not retried session 94, the British set sufficed).
