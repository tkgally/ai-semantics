---
type: resource
id: dais-dative-ratings
title: DAIS — graded human dative-alternation preference ratings (Hawkins, Yamakoshi, Griffiths & Goldberg 2020)
status: catalogued
url: https://github.com/taka-yamakoshi/neural_constructions
data: https://raw.githubusercontent.com/taka-yamakoshi/neural_constructions/master/DAIS/data/experiment_output/data_cleaned.zip
docs: https://aclanthology.org/2020.emnlp-main.376/
preregistration: https://osf.io/rtzv4
license: CC BY 4.0 (verified firsthand against the repository's raw LICENSE file, 2026-07-17 — genuine standard Creative Commons Attribution 4.0 International text; permits sharing and adaptation, including commercial, with attribution)
citation: Hawkins, R. D., Yamakoshi, T., Griffiths, T. L. & Goldberg, A. E. (2020) Investigating representations of verb bias in neural language models. Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP), pp. 4653-4663. DOI 10.18653/v1/2020.emnlp-main.376; arXiv 2010.02375.
created: 2026-07-17
updated: 2026-07-17
links:
  - rel: anchors
    target: conjecture/dative-alternation-information-structure
  - rel: supports
    target: resource/languageR-dative-corpus
---

# DAIS — graded human dative-alternation preference ratings

> **Catalogued s244 (license-VERIFIED, firsthand-inspected); ADOPTED s245 as a scoped SECONDARY
> graded-acceptability companion anchor** (cross-session adversarial review,
> [`decisions/resolved/dais-dative-rating-anchor`](../../decisions/resolved/dais-dative-rating-anchor.md);
> fresh-reviewer ADOPT-A-WITH-MODIFICATION + a convergent non-Anthropic vote). A cataloguing scout
> (charter §12.4, pure autonomy) had opened the DAIS release firsthand, verified its **CC BY 4.0**
> license against the repository's raw LICENSE file, mirrored (gitignored) and inspected the
> 50,136-row human-ratings CSV, and committed two derived tables. The s245 ratification adopts DAIS as
> a **companion** to `languageR::dative`, grounding the verb/argument **definiteness/length preference
> surface** and the dative conjecture's graded-acceptability clause — explicitly **NOT** the
> discourse-context givenness shift the tested claim measures. **No claim-level `anchors:` link was
> added** ([`claim/dative-information-structure-givenness`](../../findings/claims/dative-information-structure-givenness.md)
> keeps its anchor leg = Bresnan production, direction-only): a blunt front-matter edge would read as
> DAIS anchoring the tested shift, the exact over-claim the decision fenced off. DAIS's adoption edge
> targets the **conjecture** ([`conjecture/dative-alternation-information-structure`](../../findings/conjectures/dative-alternation-information-structure.md)),
> where its graded-acceptability surface honestly belongs. `status:` stays `catalogued` (as
> `languageR::dative` did post-ratification — a resource's `status` field is not the adoption record;
> this blockquote + the resolved decision are). The **Cao `ProbeResponses` precedent** governed the
> catalogue-then-ratify separation.

## What it is

**DAIS** (*Dative Alternation and Information Structure*) is the human-ratings benchmark released with
Hawkins, Yamakoshi, Griffiths & Goldberg (2020), *Investigating representations of verb bias in neural
language models* (EMNLP 2020, pp. 4653-4663; arXiv 2010.02375). Per the paper's abstract, verified
char-for-char against the arXiv PDF (extracted locally with PyMuPDF):

> "Here we introduce DAIS, a large benchmark dataset containing 50K human judgments for 5K distinct
> sentence pairs in the English dative alternation. This dataset includes 200 unique verbs and
> systematically varies the definiteness and length of arguments."

And §3 (verified char-for-char):

> "The DAIS dataset contains 50,136 human preference judgments for 5,000 sentence pairs … we
> collected the 100 most frequent verbs influentially classified by Levin (1993) as alternating
> (i.e. acceptably appearing in both PO and DO constructions), as well as the 100 most frequent verbs
> classified as 'non-alternating' (appearing only in the PO construction)."

The **rating task** (§3, verified char-for-char):

> "We collected judgments from 1011 participants on Amazon Mechanical Turk. Each participant was shown
> 50 dative alternation pairs (DO vs. PO) using unique verbs, balanced across the possible recipient
> and theme conditions. On each trial, participants used a continuous slider to indicate the strength
> of their preference for the DO or the PO, with the midpoint used to indicate they were 'about the
> same'".

So each judgment is a **graded, per-item, comparative naturalness preference** between the two dative
phrasings of the *same* proposition — a 0–100 slider where 0 = strong prepositional-object (PO/PD)
preference, 100 = strong double-object (DO/DOC) preference, and 50 = "about the same". This is exactly
the **per-item human acceptability/preference gradient** the project's dative claim
([`claim/dative-information-structure-givenness`](../../findings/claims/dative-information-structure-givenness.md))
explicitly notes it lacks — it is anchored only to the Bresnan et al. (2007) **production** corpus
([`resource/languageR-dative-corpus`](languageR-dative-corpus.md)) on its *direction* leg, with "**no**
per-item human acceptability rating and **no** human effect-*size* anchor."

## The data file (firsthand inspection, 2026-07-17)

The released file `DAIS/data/experiment_output/data_cleaned.zip → data_cleaned.csv` was mirrored to the
gitignored `experiments/data/dais/` (sha256 pinned below) and inspected firsthand. Confirmed
**50,136 rows** (one human judgment each; matches the paper's stated 50,136 exactly), **14 columns**:

| column | firsthand content |
|---|---|
| `rt` | reaction time (ms) |
| `set_id` | item-set id (100 distinct sets) |
| `participant_id` | Mechanical Turk worker id (**1,011 distinct participants** — matches the paper) |
| `theme_type` | `def` / `indef` / `something` (theme definiteness) |
| `recipient_id` | `pronoun` / `shortDefinite` / `shortIndefinite` / `longDefinite` / `longIndefinite` (the 5 recipient length×definiteness conditions of paper ex. 3: *him / the man / a man / the man from work / a man from work*) |
| `verb_id` | 1–200 (**200 distinct verbs**) |
| `theme_id` | 5 theme slots per verb |
| `DOsentence` | the double-object phrasing (e.g. "Alice took him the blanket") |
| `PDsentence` | the prepositional-dative phrasing (e.g. "Alice took the blanket to him") |
| `frequency_rank` | verb frequency rank |
| `classification` | `alternating` (25,177 rows) / `non-alternating` (24,959 rows) |
| `trial_index` | trial position within participant |
| `DOpreference` | **the human rating** — 0–100 continuous slider (min 0, max 100, mean 26.48, median 17) |
| `verb` | the verb string |

**5,000 distinct (DO, PD) sentence pairs**, ~**10.03 judgments per pair** (min 4, max 14). The
`DOpreference` distribution is right-skewed toward PO (mean 26.5) because the 200-verb set is half
non-alternating (PO-only) verbs, which humans rate low on the DO slider.

### Firsthand sanity reproduction of two published qualitative results

Two of the paper's own reported directions reproduce from the raw rows firsthand (derived table
`experiments/runs/2026-07-17-dais-license-scout/inspection_manifest.json`):

- **Alternating > non-alternating on the DO slider.** Mean `DOpreference` is **33.97** for `alternating`
  verbs vs **18.92** for `non-alternating` — a **15.05-point** gap. The paper reports the same contrast:
  *"verbs in the 'alternating' class were indeed rated more acceptable on average in the DO than
  'non-alternating' verbs (b = −15.0, t = −46.5, p < 0.001)"* — the firsthand mean-difference (15.05)
  matches the reported coefficient (−15.0) to within rounding.
- **The recipient information-structure gradient.** Mean `DOpreference` falls monotonically across the
  five recipient conditions: **pronoun 37.7 > shortDefinite 30.5 > shortIndefinite 25.2 >
  longDefinite 20.8 > longIndefinite 18.3** — i.e. pronominal / short / definite (given-like) recipients
  raise DO preference, exactly the human information-structure direction the project's dative claim
  attests via the Bresnan production corpus. DAIS supplies this direction **with a graded magnitude**
  (a ~20-point slider swing pronoun→longIndefinite), which the production corpus cannot.

## What it can ground

As adopted (s245, a scoped *secondary* companion — see the resolved decision below), DAIS supplies the two
things the dative line's human-anchor leg was explicitly missing, **scoped to the definiteness/length
preference surface and the conjecture's graded-acceptability clause, not the tested claim's givenness shift**:

- **A graded, per-item human *acceptability/preference* rating** (not production) — the complement to
  the `languageR::dative` production surface. Where the corpus grounds "does the model's *production
  preference* track the human *production* surface," DAIS grounds "does the model's stated preference
  track *graded per-item human naturalness preference*."
- **A human *effect-size* gradient** — the per-condition and per-verb mean `DOpreference` (committed
  derived table `verb_recipient_means.csv`: 200 verbs × 5 recipient conditions) gives a human-side
  magnitude a model's within-item shift could be *correlated against* (Spearman ρ over items/verbs), not
  merely a direction. This is the anchor the claim's "no human effect-*size*" gap names.

## What it CANNOT ground (honest limits)

- **Not the same instrument as the project's own probe.** DAIS is a *bare* slider preference between two
  isolated sentences; the project's dative probe manipulates **discourse-context givenness** on
  byte-identical phrasings. DAIS varies recipient/theme **definiteness and length**, which are *cues to*
  information status, but it does **not** carry the project's discourse-context given/new manipulation.
  So DAIS anchors the *graded verb/argument-definiteness preference surface*, **not** the project's
  context-driven within-item givenness shift directly. **Resolved s245:** DAIS grounds that
  definiteness/length surface + the conjecture's graded-acceptability clause, and is deliberately **not**
  wired as an `anchors:` link on [`claim/dative-information-structure-givenness`](../../findings/claims/dative-information-structure-givenness.md)
  (whose tested force is the givenness shift DAIS does not measure) — see
  [`decisions/resolved/dais-dative-rating-anchor`](../../decisions/resolved/dais-dative-rating-anchor.md).
- **A different measure from the corpus.** Slider *preference* ≠ corpus *production probability*; the two
  are correlated (the paper reports it) but not identical. Conflating them is the operationalization trap
  the sibling resource's open-decision fenced off, and it recurs here.
- **Not a human anchor for anything cross-linguistic, representational, or lexical-sense** — English
  dative alternation only; behavioral human ratings only.
- **Contamination caution.** DAIS is public since 2020 and may sit in the panel models' training data; a
  probe that *uses* DAIS items verbatim inherits a memorization risk. The clean use is to anchor the
  *factor → rating* relationship (verb class, recipient definiteness/length → graded preference), not to
  lift DAIS sentences as probe stimuli.

## Mirror / provenance (recipe-not-corpus posture)

- **License: CC BY 4.0**, verified firsthand 2026-07-17 against the repository's raw `LICENSE` file
  (`raw.githubusercontent.com/taka-yamakoshi/neural_constructions/master/LICENSE` — genuine standard
  Creative Commons Attribution 4.0 International text). The README adds: *"If you use the DAIS judgments,
  please cite the EMNLP 2020 paper … and this dataset."* CC BY 4.0 permits analysis and mirroring with
  attribution — so, unlike the GPL `languageR` and license-null tangrams cases, mirroring is explicitly
  licensed; the recipe-not-corpus posture below is a **repo-hygiene** choice (keep the 50k raw rows out
  of git), not a licensing necessity.
- **Mirror:** `experiments/data/dais/` (gitignored). `data_cleaned.zip` sha256
  `f3860b93c6e7d5a7065ea3b7256360c8d1227112f340c790d3a00a192cc1c652`; extracted `data_cleaned.csv` sha256
  `01ee1b163003e354cddf1c6c6be1b386123cbbce3424163bf198e9fbc4c251f9`.
- **Committed derived artifacts** (under `experiments/runs/2026-07-17-dais-license-scout/`): `prep.py`
  (the sha-pinned fetch + inspect recipe), `inspection_manifest.json` (counts + column list + sanity
  aggregates), and `verb_recipient_means.csv` (the 200×5 human-gradient table). **Never the 50,136 raw
  judgment rows.**
- Author list corrected on cataloguing: the s243 `wanted.md` entry (surfaced via the Rakshit & Goldberg
  2025 secondary) recorded the authors as "Hawkins, Nguyen, Goldberg, Frank & Goodman" and pages
  "4707–4718" — **both wrong**. Firsthand: **Hawkins, Yamakoshi, Griffiths & Goldberg**, **pp. 4653-4663**
  (verified against the arXiv abstract, the ACL Anthology landing page, and the PDF). A cautionary
  instance of the firsthand-verification rule.

## Pointer for next visit

- Status `catalogued` (license-verified + firsthand-inspected). **Adoption RATIFIED s245** as a scoped
  *secondary* graded-acceptability companion — see
  [`decisions/resolved/dais-dative-rating-anchor`](../../decisions/resolved/dais-dative-rating-anchor.md)
  (ADOPT-A-WITH-MODIFICATION). DAIS may be cited as the human resource for the **definiteness/length
  graded-preference surface** and the conjecture's graded-acceptability clause — **not** as an anchor for
  the tested discourse-context givenness shift (which stays anchored to `languageR::dative` production,
  direction-only). Any human-vs-model *magnitude comparison* on DAIS is a separate, powered, pre-critiqued
  probe (Option B), not licensed by adoption alone.
- **Option B RAN s248** ([`result/dais-graded-preference-correlation-v1`](../../findings/results/dais-graded-preference-correlation-v1.md),
  `anchors: → resource/dais-dative-ratings`): the first human-effect-size comparison on this surface. **VERDICT
  LENGTH-ONLY** — the panel tracks the human graded verb-bias magnitude (matched ρ +0.61/+0.76/+0.63,
  alternating-only control survives 3/3) and reproduces the raw recipient gradient, but the within-length
  definiteness control fails 3/3 at long length (end-weight-dominated), so its recipient gradient is not cleanly
  a definiteness surface. Scoped to the definiteness/length + verb-bias surface, NOT the givenness shift; single
  run → `proposed`.
- **Option-B REPLICATION RAN s250** ([`result/dais-graded-preference-correlation-rep2`](../../findings/results/dais-graded-preference-correlation-rep2.md),
  fresh disjoint fillers, verifier REPRODUCED): the **verb-bias leg REPLICATED 3/3** (VERB-BIAS-REPLICATES;
  matched ρ +0.68/+0.82/+0.70 each inside the s248 CI; alternating-only control survives) and was **promoted**
  to [`claim/dative-verb-bias-graded-correspondence`](../../findings/claims/dative-verb-bias-graded-correspondence.md)
  — a scoped **ordering** correspondence (not a magnitude match; contamination-vulnerable) that carries an
  `anchors: → resource/dais-dative-ratings` edge for the **verb-bias per-verb gradient** (the first supported
  claim this resource anchors). **The definiteness/length band did NOT replicate** — it flipped LENGTH-ONLY →
  TRACKS-HUMAN-SURFACE on fresh fillers, so that surface is **filler-unstable** and stays `proposed`,
  unpromoted. So DAIS now grounds one supported claim (verb-bias ordering) and one unstable dissociation
  (definiteness/length).
- The `anchors: → conjecture/dative-alternation-information-structure` front-matter link records DAIS's
  *adopted role* (s245) to strengthen the dative line's graded-acceptability clause, mirroring the
  identical edge on `languageR::dative`; the load-bearing adoption targets the **conjecture**, never the
  tested claim.
