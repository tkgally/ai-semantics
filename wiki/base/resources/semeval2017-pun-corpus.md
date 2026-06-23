---
type: resource
id: semeval2017-pun-corpus
title: "SemEval-2017 Task 7 pun corpus (Miller, Hempelmann & Gurevych 2017) — human-annotated puns with per-item dual WordNet-sense labels on the actual sentence"
status: catalogued
url: "https://alt.qcri.org/semeval2017/task7/data/uploads/semeval2017_task7.tar.xz"
url-note: "Full archive (trial + test data, scorer, task-paper preprint) downloaded 2026-06-23 (session 92), HTTP 200, 748,424 bytes, sha256 70e82d89a102fced7dd1b1db90daa4ead55357d399d23f4d99e888634b4f4d0a (xz/CRC64). Official task page: https://alt.qcri.org/semeval2017/task7/ ; data-and-resources page: https://alt.qcri.org/semeval2017/task7/index.php?id=data-and-resources . Data NOT mirrored in-repo (see License — a CC BY-NC 4.0 subset; the canonical URL + sha256 here make any future re-fetch deterministic)."
paper: "Tristan Miller, Christian F. Hempelmann & Iryna Gurevych (2017). SemEval-2017 Task 7: Detection and Interpretation of English Puns. Proceedings of the 11th International Workshop on Semantic Evaluation (SemEval-2017), pp. 59–69. ACL. https://aclanthology.org/S17-2005/ . ISBN 978-1-945626-00-5."
venue: "SemEval-2017 (ACL)"
license: "MIXED — scorer Apache-2.0; data: individual jokes deemed by the authors too short to be copyrightable, with secured compilation licences CC BY 4.0 for most subsets and CC BY-NC 4.0 for the PunoftheDay.com subset; overall compilation CC BY 4.0 (UKP/TU Darmstadt). See License section for the verbatim LICENCE.md breakdown and the practical implication."
meaning-senses:
  - distributional
  - referential
  - human-comparison
contingent-on: []
created: 2026-06-23
updated: 2026-06-23
links:
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: resource/wordnet-sense-inventory
---

# SemEval-2017 Task 7 pun corpus (Miller, Hempelmann & Gurevych 2017)

> **Verification status (2026-06-23, session 92).** Archive **fetched and inspected firsthand**
> (not scouted from secondary descriptions): downloaded from the official QCRI URL (HTTP 200,
> 748,424 bytes, sha256 above), extracted, and the gold files, DTD, the archive's README and LICENCE
> files, and the task-paper abstract read directly. Counts, annotation format, and licence below are from the
> primary files. The polysemy/homonymy split is a **disclosed proxy I computed** from the WordNet
> sense keys, not a human label — see that section. **Anchor status: RATIFIED (Q4 co-activation
> only).** As of session 93 (2026-06-23) the cross-session adversarial-review pass **adopted** this
> corpus as the gate's **Q4 sense-co-activation** anchor
> ([`decisions/resolved/sense-coactivation-anchor-semeval-puns`](../../decisions/resolved/sense-coactivation-anchor-semeval-puns.md));
> the ratification is scoped to sense **co-presence** and licenses **no** balance/dominance claim
> (Q-B-1: a separate, frozen, not-model-based dominance step is still owed). The run is not
> automatic — a forced-both build still needs a fresh pre-run critic GO + budget.

This page catalogs the SemEval-2017 Task 7 pun corpus as the candidate resource the
[`result/forced-both-lexical-build-attempt-v1`](../../findings/results/forced-both-lexical-build-attempt-v1.md)
page named as the thing that would lift its **Q1-ii wall** — "a released corpus of human-annotated
puns/zeugmas with per-item balance or co-activation labels (none in-repo or on `wanted.md` today)".
It is now in-repo (catalogued) and on [`wanted.md`](../wanted.md) as **RECEIVED**.

## What it is

The corpus underwrote the first shared task on automatic pun detection, location, and
interpretation. The task paper's abstract states verbatim (ACL Anthology S17-2005, fetched
2026-06-23):

> "A pun is a form of wordplay in which a word suggests two or more meanings by exploiting
> polysemy, homonymy, or phonological similarity to another word, for an intended humorous or
> rhetorical effect. Though a recurrent and expected feature in many discourse types, puns stymie
> traditional approaches to computational lexical semantics because they violate their
> one-sense-per-context assumption. This paper describes the first competitive evaluation for the
> automatic detection, location, and interpretation of puns. We describe the motivation for these
> tasks, the evaluation methods, and the manually annotated data set. Finally, we present an
> overview and discussion of the participating systems' methodologies, resources, and results."

The load-bearing property, for this project, is the clause **"they violate their
one-sense-per-context assumption"**: a pun is by construction an item in which **two senses are
jointly operative** in one short context — i.e. it is exactly the **forced-both lexical item** the
discriminating test of
[`essay/layer-specialness-vs-always-resolvability`](../../findings/essays/layer-specialness-vs-always-resolvability.md)
needs, and which the build attempt could not *certify* from author-constructed sentences.

Two pun types are distinguished:
- **Homographic** puns — one *written word form* with two meanings (polysemy or homonymy). **This
  is the relevant subset** for the single-form lexical line.
- **Heterographic** puns — the punned word is *phonologically* similar to a different target word
  (different spelling). Out of scope for a single-form lexical commit probe, but kept here for the
  record.

## Annotation format — the per-item dual-sense gold (the crux)

The interpretation subtask (subtask 3) gold supplies, **per pun item, the two WordNet senses the
pun evokes**. From the archive's README file (verbatim):

> "For subtask 3, each line consists of three fields separated by horizontal whitespace (a single
> tab or space character). The first field is the ID of a pun word. The second field is a
> semicolon-delimited list of WordNet 3.1 sense keys that match one meaning of the pun. The third
> field is a semicolon-delimited list of WordNet 3.1 sense keys that match the other meaning of the
> pun."
>
> "The order of the two meanings is not significant, nor is the order of the sense keys within each
> meaning."

So each item carries a **human-curated, item-specific annotation that two distinct senses are both
in play in that very sentence**. Example gold lines (homographic test, read directly):

```
hom_2_9    save%2:40:02::    save%2:41:02::
hom_3_7    sting%1:26:01::   sting%1:04:01::
hom_8_17   vault%1:06:02::   vault%1:04:00::
```

The stimuli themselves are in the paired XML files (`<text>`/`<word>` tokens, with the pun word
marked `senses="2"`); the DTD is `data/test/puns.dtd`. Sense keys are **WordNet 3.1** — see
[`resource/wordnet-sense-inventory`](wordnet-sense-inventory.md).

**Why this is the right shape and the SemCor route was not.** The build attempt's structural defect
was that a SemCor *general-usage* balance ratio "does not measure the balance of the *specific
constructed co-predication sentence*" — general frequency cannot see the in-item pull of a
constructed frame. Here the annotation is **on the actual pun sentence**: humans labelled the two
senses *of this item*, not of the word in general. That is precisely the in-item evidence the
SemCor proxy could not give.

## Counts (read directly from the gold/XML files, 2026-06-23)

| split | homographic | heterographic |
|---|---:|---:|
| test — subtask 1 (detection, all texts) | 2250 | — |
| test — subtask 3 (interpretation, pun texts w/ gold dual senses) | **1298** | **1098** |

(Trial data is also present under `data/trial/` for all three subtasks and both pun types.) The
1298/1298 match between the homographic subtask-3 XML `<text>` count and its gold line count was
verified.

## Polysemy vs. homonymy mix — a DISCLOSED PROXY (not a human label)

The forced-both line specifically wants **homonyms** (discrete, *unrelated* senses), while the
sibling [`concept/polysemy`](../concepts/polysemy.md) cares about the polysemy/homonymy split
itself. The corpus does **not** tag items as polysemy vs. homonymy. As a **rough, disclosed proxy**
I computed (session 92) whether the two gold senses fall in **different WordNet lexicographer
files** (`lexfile`, the broad semantic-field number in the sense key) — a coarse stand-in for
"unrelated sense":

- **1074 / 1298 (83%)** homographic items have the two senses in **different** lexfiles (homonymy
  proxy — e.g. `vault%1:06:02` *artifact* vs `vault%1:04:00` *act*).
- **224 / 1298 (17%)** have them in the **same** lexfile (related-sense / polysemy proxy — e.g.
  `hit%1:04:00` vs `hit%1:04:02`).
- 1060 / 1298 have both senses sharing the same lemma (the rest pair lemma variants, e.g.
  `pin_on` / `pin`).

**This is a proxy, not ground truth.** Lexicographer-file difference over- and under-counts
homonymy (WordNet's file structure is not a homonymy oracle); it is offered only to show the corpus
contains **a large pool of candidate unrelated-sense items** *and* a native polysemy-vs-homonymy
contrast — both useful, neither certified by it. A real homonymy split would still need a
dictionary etymology step or human labels on top.

## What it can ground

The key section (charter rule: cite a resource by the *feature* that bears).

**Sense CO-ACTIVATION on the actual item — human, per-item.** Each homographic subtask-3 item is a
human-curated context in which **two distinct senses are both intended**, with the two senses named
(WordNet keys). This is the direct ground for the gate's **Q4** anchor target, which names "sense
**co-activation**" specifically (the gate held Q4 at `internal-contrast-only` precisely "unless a
sense-co-activation resource is separately cross-session ratified"). It is also the
[`matched-ambiguity-kind-cross-level`](../../decisions/resolved/matched-ambiguity-kind-cross-level.md)
**Option-A** homonym sense-anchor that was held in reserve.

**Pre-built, human-validated forced-both stimuli.** ~1298 homographic items are real puns vetted by
the task organisers (contexts whose two meanings are not both in WordNet were removed — task paper);
they are *attested* forced-both items, stronger than author-constructed co-predication sentences
because the joint-sense requirement is what makes the pun work, not an author's stipulation.

**A stat-powered N.** Unlike the SemCor route (1/8 candidates powered), this is ~1298 + ~1098 items
— ample for a per-model behavioral pattern if the gate's other questions are met.

## What it cannot ground

- **A graded BALANCE / dominance score.** This is the honest limit and the heart of the open
  decision. The gold certifies that **both senses are present** (co-activation); it does **not**
  give a numeric "neither sense dominates" rating. In many puns one reading is the surface/expected
  one and the other the surprise — co-presence is guaranteed, *equal salience is not measured*. The
  gate's **Q1-ii** asked for an independent check that "neither sense **dominates**." Whether
  human-annotated co-activation **suffices** for Q1-ii, or whether a separate dominance measure is
  still required, is exactly what the queued decision must adjudicate — **not settled here**.
- **A zeugma / co-predication structural frame.** The gate's frozen **Q1-iii** default was a
  *zeugma/co-predication* frame (one token yoked to two complements). A pun is a **different**
  forced-both device (one context simultaneously evoking both senses, often without two explicit
  complements). Using attested puns as stimuli is a *design variant* of the frozen frame; whether
  it satisfies the forced-both structural criterion, or whether puns supply only the anchor while
  author-built zeugma items remain the stimuli, is part of the open decision.
- **Heterographic puns for a single-form probe.** The ~1098 heterographic items turn on
  *phonological* similarity to a *different* spelled word — not one form with two senses — so they
  do not instantiate the single-form lexical commit object.
- **Reference / extension.** Like every in-repo resource, it carries no human-agreed extension; it
  bears on `referential.sense`, not `referential.reference`.
- **Sense granularity vs. a full inventory.** It does not adjudicate model sense-splitting against
  WordNet; that needs SemCor/OntoNotes.

## License

From the archive's `LICENCE.md` (verbatim excerpts):

> "The scoring software is licensed under the Apache License, Version 2.0."

> "To the best of our knowledge, the individual punning jokes in the data are short enough that they
> are not eligible for copyright. … However, copyright may persist in the overall compilation … Out
> of an abundance of caution, we have undertaken to secure licences for certain of the copyrights
> possibly persisting …"

The secured compilation licences are **CC BY 4.0** for the Don Hauptman, Stan Kegel, Beatrice
Santorini, Daniel Austin, and Hempelmann/Bell/Crossley subsets and for the **overall** compilation
(UKP/TU Darmstadt), and **CC BY-NC 4.0** for the PunoftheDay.com subset (verbatim: "licensed under
the terms of the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)
licence"). LICENCE.md adds: "If you wish to redistribute the data in whole or in part, verbatim or
modified, then you should abide by the terms of these licences."

**Practical implication for this project (non-commercial research):**
- **Permitted:** downloading and running analysis on the data (this is use, not redistribution).
- **Care needed on redistribution:** because one subset is CC BY-NC 4.0, **bulk-committing the raw
  corpus into this public repo is avoided** (the DWUG precedent for redistribution caution —
  [`resource/dwug-usage-graphs`](dwug-usage-graphs.md)). Instead this page records the **canonical
  URL + sha256** so any future session re-fetches the identical archive deterministically; a
  derived **item-id list / stratification layer** (not the joke text) may be committed if a probe
  is built, with attribution.
- Citation required (CC BY): cite Miller, Hempelmann & Gurevych 2017 in any use.

## Fetchability

- **Confirmed reachable 2026-06-23 (session 92):** `curl` of
  `https://alt.qcri.org/semeval2017/task7/data/uploads/semeval2017_task7.tar.xz` → HTTP 200,
  748,424 bytes, **sha256 `70e82d89a102fced7dd1b1db90daa4ead55357d399d23f4d99e888634b4f4d0a`**.
- Mirrors exist (e.g. the `Zhijun-Xu/PunEval` GitHub repo bundles the SemEval-2017 Task 7 data);
  the QCRI original is canonical and was the one fetched.

## Pointer for next visit

> **Build attempted under the anchor — NO-GO (session 94, 2026-06-23).** A v2 forced-both build used
> this corpus as the Q4 co-activation anchor and froze a **43-item balanced-homonym subset** (homonym
> proxy + the word-grain dominance norms). The sha256 above was **re-verified** (deterministic
> re-fetch, identical hash). A fresh pre-run critic ruled **NO-GO → trigger (c)**: the corpus
> discharges co-activation but **cannot** supply the Q-B-1 in-item dominance step, the pun genre
> directionally installs an in-item lean, and an attested pun affords a pickable surface reading (so it
> is not the fork's "no-reading-to-pick" object). The anchor is sound *for what it certifies*
> (co-presence); the wall is the separate balance premise →
> [`result/forced-both-lexical-build-attempt-v2`](../../findings/results/forced-both-lexical-build-attempt-v2.md).

1. **The anchor is RATIFIED for co-activation (Q4) only** (session 93, 2026-06-23). Read
   [`decisions/resolved/sense-coactivation-anchor-semeval-puns`](../../decisions/resolved/sense-coactivation-anchor-semeval-puns.md);
   the adopted posture is Q-A (adopt as Q4 anchor) + Q-B-1 (co-activation does NOT discharge Q1-ii —
   a separate dominance step is owed) + Q-C-1 (attested homographic puns may serve as forced-both
   stimuli, homonym subset, sha256-frozen). A forced-both result may now lift off
   `internal-contrast-only` **for the co-activation claim only**.
2. **Co-activation ratified, balance NOT.** The cleanest first design uses the corpus as the **Q4
   co-activation anchor** while still meeting Q1-ii by a separate, pre-registered dominance step
   (e.g. the word-grain [`resource/homonym-meaning-dominance-norms`](homonym-meaning-dominance-norms.md)
   plus a frozen, *argued* transfer-to-item step — Q-B-1). Do not relax the balance band to force a
   runnable item.
3. **To build a probe,** freeze a homographic-item subset (id list + the homonymy criterion) and
   the reading rule under the existing forced-both gate *before* any model call (charter §8); commit
   only the id list / stratification, not the joke text.
4. **Re-fetch deterministically** with the URL + sha256 above; verify the hash before use.
