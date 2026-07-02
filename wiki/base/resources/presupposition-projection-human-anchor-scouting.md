---
type: resource
id: presupposition-projection-human-anchor-scouting
title: "Presupposition/projection human-anchor scouting — feasibility catalog for a HUMAN projection-variability signal to re-anchor the projection line"
meaning-senses:
  - inferential
  - human-comparison
  - distributional
status: scouting
created: 2026-07-02
updated: 2026-07-02
links:
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: result/conditional-projection-rescue-v1
  - rel: depends-on
    target: result/projection-trigger-inventory-v1
---

# Presupposition/projection human-anchor scouting — a HUMAN projection-variability signal for the projection line

**Scouted:** 2026-07-02 (session 168, program item A3a). **Purpose:** a $0 license-check
feasibility catalog of candidate **human** projection-variability datasets that could re-anchor the
project's presupposition/projection line from a within-model contrast to a **model-vs-human**
comparison. This is a **scouting** note in the mould of
[`base/resources/multimodal-anchor-scouting.md`](multimodal-anchor-scouting.md) and
[`base/resources/scalar-implicature-anchor-scouting.md`](scalar-implicature-anchor-scouting.md);
it **adopts nothing**. The project's standing rule applies: a resource may be cited only by the
*specific human-produced feature* that bears on a claim, never by existence alone. **No `anchors:`
link is asserted here** — nothing below is ratified as the anchor; this records only what was checked,
honestly, including where a license could not be verified.

**Honesty up front.** All four datasets came back with **no verifiable data license** this session —
no `LICENSE` file in the repository, and no license/terms-of-use statement on the paper or project
page that could be quoted. That is an honest, expected scouting outcome, recorded as such. Where a
license *string* appears (NOPE's arXiv posting), it covers the **paper**, not the released corpus, and
is flagged as such. **Nothing below is assumed permissive.** The recommendation at the end is
calibrated to this null.

---

## What the projection line currently is, and what a human anchor would change

The project's presupposition/projection results are all **`anchor: internal-contrast-only`** — they
measure a **within-model** contrast (a base sentence's presupposition leg survives an
entailment-cancelling frame more than a *matched ordinary entailment* leg, within the same model),
and make **no human comparison** (ratified via
[`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../decisions/resolved/presupposition-projection-internal-contrast-anchor.md)
and its siblings). The striking finding —
[`result/presupposition-projection-v1`](../../findings/results/presupposition-projection-v1.md) and
[`result/conditional-projection-rescue-v1`](../../findings/results/conditional-projection-rescue-v1.md) —
is that **the conditional-antecedent frame COLLAPSES projection across all three models** (presupposition
survival 0.42 / 0.17 / 0.17), robustly, while negation and questions preserve it; and
[`result/projection-trigger-inventory-v1`](../../findings/results/projection-trigger-inventory-v1.md)
finds the within-model asymmetry generalizes in direction across trigger families but clears the bar
for only 1/3 (verdict MIXED).

A **license-clean human projection-variability dataset** would let a later session convert this into a
quantified **model-vs-human** comparison — interesting in *either* direction:

- **Humans dip too** under the conditional antecedent (or on the same trigger families) → the panel
  *tracks* human projection variability, a convergence result.
- **Humans do not dip** where the models collapse → a **quantified divergence** — the panel fails to
  reproduce human projection exactly where the semantics literature says projection is most robust or
  most defeasible.

Either outcome would upgrade the projection line from a within-model contrast to a
`human-comparison`-tagged finding. That is the prize this scout is checking the price of. **The price,
this session, is an unverified license on every candidate.**

---

## What a fit-for-purpose anchor would look like

To upgrade the projection line, the project needs a human resource supplying, per item (ideally per
trigger and per embedding environment): a **graded human projection judgment** — the rate or degree to
which people take a speaker to be committed to the embedded/backgrounded content when it sits under an
entailment-cancelling operator (negation, question, modal, **conditional antecedent**). The
**conditional-antecedent environment** is the load-bearing cell: the project's headline is the
conditional collapse, so a dataset that includes conditional-antecedent (or antecedent-of-conditional)
items with human judgments is worth more than one that only covers negation/question. The signal must
be human-produced, released, and licensed for at least analysis + short verbatim quotation.

---

## Candidate 1: CommitmentBank (de Marneffe, Simons & Tonhauser 2019) — projection under entailment-cancelling operators, the closest environment match

**What it is (verified from the repo + paper page).** de Marneffe, Simons & Tonhauser (2019), "The
CommitmentBank: Investigating projection in naturally occurring discourse," *Proceedings of Sinn und
Bedeutung 23*. A corpus of **1,200 naturally-occurring discourses** whose final sentence contains a
**clause-embedding predicate under an entailment-cancelling operator (question, modal, negation,
antecedent of conditional)**. The human signal is a **projection judgment on a 7-point Likert scale**
(from the speaker is certain the embedded content is true, through uncertain, to certain false), i.e.
how strongly annotators take the speaker to be committed to the embedded clause. Repository:
`https://github.com/mcdm/CommitmentBank` (data file `CommitmentBank-All.csv`). A 3-way-labelled subset
is also the **CB** task in **SuperGLUE**.

**Why it is the best environment fit.** It is the only candidate whose design *explicitly includes the
antecedent of a conditional* among its entailment-cancelling operators — the exact environment where
the project's panel collapses
([`result/conditional-projection-rescue-v1`](../../findings/results/conditional-projection-rescue-v1.md)).
It also covers negation, question, and modal, so it spans the project's frame set. This is the
directly on-target human projection signal.

**License: UNVERIFIED (no license found).** The GitHub repository has **no `LICENSE` file** (raw
`https://raw.githubusercontent.com/mcdm/CommitmentBank/master/LICENSE` returned **HTTP 404** this
session) and the README carries **no license, terms-of-use, or data-use statement** that could be
quoted (WebFetch of the repo page confirmed "no explicit license statement"). Additional layer: the
discourses are drawn from pre-existing corpora (the naturally-occurring source texts) whose own terms
would need checking before redistribution — **that source provenance was not verified this session**
and must not be assumed open. Treat the CommitmentBank data as **license-unverified**; do not assume
permissive terms. (The SuperGLUE redistribution of CB may carry its own terms — also unverified here.)

**What it could anchor (if licensed).** A human projection-rate baseline per embedding operator —
crucially **antecedent-of-conditional** — against which the panel's conditional collapse could be
scored directly. It is the single most on-target candidate for
[`result/conditional-projection-rescue-v1`](../../findings/results/conditional-projection-rescue-v1.md)
and the frame-asymmetry in
[`result/presupposition-projection-v1`](../../findings/results/presupposition-projection-v1.md).

**What it cannot anchor.** Its items are **naturally-occurring** clause-embedding-predicate discourses,
not the project's authored matched-P-vs-E minimal pairs, so any comparison is at the *aggregate
projection-rate* grain, not item-matched to the project's stimuli. It does not carry the project's
matched-*entailment* control leg. And it is **clause-embedding-predicate-centric** — it does not cover
the definite-description / it-cleft / aspectual trigger families the project's inventory
([`result/projection-trigger-inventory-v1`](../../findings/results/projection-trigger-inventory-v1.md))
also spans.

---

## Candidate 2: MegaVeridicality (White & Rawlins 2018) — veridicality/projection over many clause-embedding predicates

**What it is (verified from the project page).** The MegaVeridicality dataset (White & Rawlins 2018),
part of the **MegaAttitude** project. It collects human judgments about whether an embedded clause's
content projects (is inferred true) in **positive and negative** syntactic contexts, across a very
large predicate inventory. Two versions (verified from `megaattitude.io`): **v1 — 1,088 sentences,
517 predicates, 2 frames**; **v2.1 — 3,938 sentences, 773 predicates, 9 frames**. The human signal is
an ordinal veridicality/inference judgment per predicate-frame. Home:
`https://megaattitude.io/projects/mega-veridicality/`; also listed at `https://rawlins.io/data/`.
Distributed as downloadable zip files.

**License: UNVERIFIED (no license found).** Neither the MegaVeridicality project page nor the Rawlins
data index (`https://rawlins.io/data/`) states **any** license, Creative Commons designation, or
data-use policy (both fetched this session; both returned "no explicit licensing information"). No
`LICENSE` in an associated repository was located. Treat as **license-unverified**.

**What it could anchor (if licensed).** A human veridicality/projection signal over a **broad
clause-embedding-predicate inventory** — the natural anchor for the **factive family** leg of
[`result/projection-trigger-inventory-v1`](../../findings/results/projection-trigger-inventory-v1.md)
(factive realize/discover/know) and for a predicate-level model-vs-human veridicality comparison. Its
positive/negative-context design bears on the negation cell of the project's frame set.

**What it cannot anchor.** It covers **positive and negative** contexts (and finite/non-finite frames),
**not the antecedent-of-conditional** — so it does **not** directly bear on the project's headline
conditional collapse. It is predicate-veridicality, not the presupposition-of-definite-descriptions or
it-cleft triggers. Its unit is predicate-frame veridicality, not item-matched to the project's authored
scenarios.

---

## Candidate 3: Degen & Tonhauser projection-variability datasets (2021 "Prior beliefs modulate projection"; the "How Projective is Projective Content?" norming line)

**What it is (verified from the repo).** The Stanford ALPS-lab projection-variability line: Degen &
Tonhauser (2021), "Prior beliefs modulate projection" (*Open Mind* 5: 59–70), and the associated
norming studies (Tonhauser, Beaver & Degen, "How Projective is Projective Content? Gradience in
Projectivity and At-issueness," *Journal of Semantics*). The repository
`https://github.com/judith-tonhauser/projective-probability` holds (verified via fetch) experimental
materials, human projection-rating data, and R analyses for the Degen & Tonhauser 2021 projection
experiments, plus re-analyses of CommitmentBank, MegaVeridicality and VerbVeridicality. The human
signal is **graded projection ratings** ("how certain is the speaker that ...") measuring
**by-participant projection variability** — the finding is that *gradient prior beliefs* predict
projection, i.e. projection is graded and variable across people and content. This is the candidate
whose *construct name* is literally "projection variability."

**License: UNVERIFIED (no license found).** The repository has **no `LICENSE` file** (raw
`https://raw.githubusercontent.com/judith-tonhauser/projective-probability/master/LICENSE` returned
**HTTP 404** this session) and the README states **no license or terms of use** (WebFetch confirmed).
Treat as **license-unverified**.

**What it could anchor (if licensed).** The **graded, by-item and by-participant projection-variability
signal** — the closest match to the project's *variability* framing
([`result/projection-trigger-inventory-v1`](../../findings/results/projection-trigger-inventory-v1.md)'s
MIXED, family-dependent picture; the essay
[`essay/projection-defeasible-by-frame`](../../findings/essays/projection-defeasible-by-frame.md)).
Because its whole point is that human projection is *graded and context/prior-sensitive*, it is the
natural human comparator for a "does the panel's frame-dependent projection track human graded
projection?" question.

**What it cannot anchor.** Its experiments primarily norm projection out-of-the-blue and under
question/negation-style diagnostics; **antecedent-of-conditional coverage was not verified** this
session, so it should not be assumed to bear on the conditional collapse without checking the actual
materials. Its predicates overlap CommitmentBank/MegaVeridicality (clause-embedding predicates),
narrower than the project's full trigger inventory.

---

## Candidate 4: NOPE (Naturally-Occurring Presuppositions in English; Parrish et al. 2021, CoNLL)

**What it is (verified from the paper page + repo).** NOPE (Kabbara/Parrish et al. 2021, "NOPE: A
Corpus of Naturally-Occurring Presuppositions in English," *CoNLL 2021*; arXiv 2109.06987). A
broad-coverage dataset of sentences with naturally-occurring presupposition triggers: **2,386
annotated main examples + 346 adversarial examples**, covering **10 types of presupposition triggers**.
The human signal is inference ratings (a Likert-style human judgment of whether the presupposition is
inferred). The paper's headline (verified from the abstract/summary) is **considerable human-rating
variability across items for two trigger classes — clause-embedding predicates (know/think) and
implicatives (manage to / fail to)** — while other triggers show lower contextual variability, and
that transformer models fail to capture the minority of exceptional context-sensitive cases.
Repository: `https://github.com/nyu-mll/nope` (also reached as `nyu-mll/presupposition_dataset`), with
a `human_results` directory.

**License: UNVERIFIED for the corpus (paper-only CC found).** No `LICENSE` file was found in the
repository under either name/branch tried (raw `.../nope/master/LICENSE`,
`.../presupposition_dataset/main/LICENSE`, `.../presupposition_dataset/master/LICENSE` all returned
**HTTP 404** this session), and the README states no data-use terms. The **arXiv posting** of the
paper shows a Creative Commons icon linking to
`http://creativecommons.org/licenses/by-sa/4.0/` — i.e. **CC BY-SA 4.0** — but that license covers the
**paper text on arXiv**, *not* the released corpus/annotations, and must not be read as a data license.
Additional layer: NOPE's sentences are drawn from a pre-existing text source whose own terms were
**not verified** this session. Treat the **corpus license as UNVERIFIED**. *(Flagged quote-provenance
note: the CC BY-SA 4.0 string is verified as the arXiv paper license only; I could not pin any license
to the corpus data files.)*

**What it could anchor (if licensed).** A human presupposition-inference-rate signal across **10
trigger types** with **explicit per-item human variability** — the broadest trigger coverage of the
four, and a direct comparator for the project's **trigger-inventory** line
([`result/projection-trigger-inventory-v1`](../../findings/results/projection-trigger-inventory-v1.md))
and its family-decomposition finding. Its documented human variability for clause-embedding predicates
and implicatives is exactly the kind of graded human signal a model-vs-human comparison needs.

**What it cannot anchor.** It targets presupposition-inference in (largely single-sentence) natural
contexts, not a systematic negation/question/**conditional** frame crossing — so it does **not**
cleanly isolate the antecedent-of-conditional environment behind the project's headline collapse. It
is presupposition-trigger-centric (definite descriptions, factives, implicatives, etc.), overlapping
but not identical to the project's authored trigger set.

---

## What this could and could not anchor (summary)

**Could anchor (pending a verified license):**

- **The conditional collapse** ([`result/conditional-projection-rescue-v1`](../../findings/results/conditional-projection-rescue-v1.md))
  — best served by **CommitmentBank** (the only candidate whose design includes the *antecedent of a
  conditional* as an entailment-cancelling operator with human projection judgments).
- **The factive/predicate leg** of the trigger inventory
  ([`result/projection-trigger-inventory-v1`](../../findings/results/projection-trigger-inventory-v1.md))
  — best served by **MegaVeridicality** (broad clause-embedding-predicate veridicality) and the
  **Degen & Tonhauser** graded projection norms.
- **The variability framing** — best served by **NOPE** (10 trigger types, explicit per-item human
  variability) and **Degen & Tonhauser** (by-participant graded projection).

**Could NOT anchor (in every case):**

- **Item-matched** comparison to the project's *authored matched-P-vs-E minimal pairs*. Every candidate
  is either naturally-occurring (CommitmentBank, NOPE) or predicate-norming (MegaVeridicality, Degen &
  Tonhauser); none carries the project's matched-entailment control leg. Any anchor would be an
  **aggregate projection-rate** comparison (human rate per operator/trigger vs. panel rate), not an
  item-level key. That is a legitimate `human-comparison` upgrade but a coarser one than the project's
  internal contrast — and must be scoped as such if adopted.
- **The full frame crossing.** Only CommitmentBank spans conditional + negation + question + modal;
  MegaVeridicality is positive/negative only; NOPE and Degen & Tonhauser do not cleanly isolate the
  conditional antecedent (unverified this session).

---

## Recommendation

**No license-verified human projection-variability dataset was found this session.** All four
candidates — **CommitmentBank, MegaVeridicality, Degen & Tonhauser projective-probability, NOPE** —
have **no verifiable data license** (no `LICENSE` file; no quotable terms-of-use on paper or project
page). NOPE's only verifiable license string (arXiv CC BY-SA 4.0) covers the paper, not the corpus.

The honest posture is therefore: **the human-comparison upgrade for the projection line stays
un-anchored for now, and `internal-contrast-only` remains the calibrated status** of
[`result/presupposition-projection-v1`](../../findings/results/presupposition-projection-v1.md),
[`result/conditional-projection-rescue-v1`](../../findings/results/conditional-projection-rescue-v1.md),
and [`result/projection-trigger-inventory-v1`](../../findings/results/projection-trigger-inventory-v1.md)
until a license is verified.

Ranked, for a *future* session that wants to pursue the anchor and can verify a license by a route this
scout could not (e.g. emailing an author for terms, or finding a deposit with an explicit license):

1. **Most on-target environment, license unverified: CommitmentBank.** The only candidate covering the
   **antecedent-of-conditional** with human projection judgments — the exact environment behind the
   project's headline. If its terms can be verified (and the underlying source-text terms cleared), it
   is the first-choice anchor for the conditional-collapse comparison.
2. **Broadest trigger coverage + explicit human variability, license unverified: NOPE.** Ten trigger
   types, per-item human variability; best comparator for the trigger-inventory line. arXiv paper is
   CC BY-SA 4.0 but the **corpus** license must be verified separately.
3. **Broadest predicate coverage, license unverified: MegaVeridicality**, and **the projection-variability
   construct itself: Degen & Tonhauser projective-probability** — both strong for the factive/predicate
   and variability legs, both license-unverified.

**Bottom line.** The projection line's human-comparison upgrade has **no clean open anchor available
now**. The most on-target dataset (CommitmentBank, conditional-antecedent human judgments) is
license-unverified; the broadest (NOPE) is license-unverified beyond its paper-only CC BY-SA; the two
predicate/variability norms (MegaVeridicality, Degen & Tonhauser) are license-unverified. So
`internal-contrast-only` stays the honest posture, and the anchor question is opened — not ratified —
in [`decisions/open/presupposition-projection-human-anchor`](../../decisions/open/presupposition-projection-human-anchor.md).

---

## Verification ledger for this scout

| Candidate | What it measures / unit | Size (verified) | URL | License verdict | How checked / what stays unverified |
|-----------|-------------------------|-----------------|-----|-----------------|-------------------------------------|
| CommitmentBank | projection judgments (7-pt Likert) under Q/modal/negation/**conditional antecedent** | 1,200 discourses | github.com/mcdm/CommitmentBank | **UNVERIFIED** | raw `LICENSE` → HTTP 404; README no license (fetched); underlying source-text terms **not** verified |
| MegaVeridicality | veridicality/projection judgments (positive/negative frames) | v1 1,088 sent / 517 pred / 2 frames; v2.1 3,938 sent / 773 pred / 9 frames | megaattitude.io/projects/mega-veridicality/ | **UNVERIFIED** | project page + rawlins.io/data both state no license (fetched); no repo LICENSE located |
| Degen & Tonhauser (projective-probability) | graded projection ratings; by-participant projection variability | not counted this session | github.com/judith-tonhauser/projective-probability | **UNVERIFIED** | raw `LICENSE` → HTTP 404; README no license (fetched); conditional-antecedent coverage **not** verified |
| NOPE | presupposition-inference ratings over 10 trigger types; per-item human variability | 2,386 main + 346 adversarial; 10 trigger types | github.com/nyu-mll/nope | **UNVERIFIED (corpus)** | raw `LICENSE` → HTTP 404 (both repo names/branches); **arXiv paper** = CC BY-SA 4.0 (paper only, not data); text-source terms **not** verified |

**Fetches / facts NOT verified this scout (stated honestly):**
- No `LICENSE` file exists in any of the four repositories on the branches/names tried (HTTP 404 on
  every raw-LICENSE URL). This is evidence of *absence of a stated license*, not of any particular
  permissive or restrictive term.
- The **underlying source-text provenance and terms** for CommitmentBank (naturally-occurring
  discourses) and NOPE (naturally-occurring sentences) were **not** verified — an additional license
  layer beyond the annotation release.
- NOPE's **CC BY-SA 4.0** string is verified only as the **arXiv paper** license; it could **not** be
  pinned to any corpus data file. Do not read it as a data license.
- The GitHub MCP is scoped to this project's repo only, so authoritative repo-metadata license fields
  (the GitHub API `license` object) could **not** be read; verdicts rest on raw-file 404s + fetched
  README/page prose.
- Antecedent-of-conditional coverage in the Degen & Tonhauser materials was **not** confirmed by
  reading the item files.
