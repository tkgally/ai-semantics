# PREREG — BLiMP R1 content-word-swap arm (A3b, s210, C8 promotion-prep)

**Frozen before any model call.** Ratified s210 (autonomous cross-session adversarial review + one
non-Anthropic decorrelation vote): **Q1-A / Q2-B / Q3-A + noun-only swap (conditional on G-coverage) +
G-margin-justification** ([`decisions/resolved/blimp-swap-arm-design`](../../../wiki/decisions/resolved/blimp-swap-arm-design.md);
design [`design/blimp-swap-arm-v1`](../../designs/blimp-swap-arm-v1.md)). This document + `build_swap.py` are
the frozen recipe; the swap-build is independently reproduced by a fresh-agent verifier from this recipe
**before any item is scored** (G5-plus). Because the swapped-condition accuracies are **unknown at freeze**,
the swap arm carries **no known-accuracy exposure**; its only DoF is the build, fenced here.

## Question

Reading **R1 = PROFILE-ALIGNED** of [`result/blimp-forced-choice-sweep-v1`](../../../wiki/findings/results/blimp-forced-choice-sweep-v1.md)
(per-model Spearman of per-paradigm forced-choice accuracy vs BLiMP per-paradigm human agreement, ρ_prof
+0.606 / +0.543 / +0.628, n=40) survived the s208 corpus-frequency **covariate** arm (SURVIVES-COVARIATE
3/3). Per **G8**, a human-comparison **promotion** of R1 also requires the **content-word-swap** arm: does
the panel's per-paradigm grammatical-difficulty profile **survive replacing the exact BLiMP surface strings
with novel, frequency-matched content words** (holding the grammatical minimal contrast constant)? If yes,
the profile is not driven by **exact-string / lexical-item memorization** of the BLiMP items.

## Panel & elicitation (the s205 instrument, carried verbatim)

Panel = the three [`config/models.md`](../../../config/models.md) slots (`panel.A/.B/.C`), temperature 0,
zero-shot, single-turn, **both presentation orders** per pair, `google/*` reasoning suppressed
(`reasoning={"effort":"minimal"}`). The **exact s205 forced-choice prompt** (frozen in
`../2026-07-10-blimp-forced-choice-sweep/probe.py`): *"Which of these two sentences is the more
grammatically acceptable sentence of standard written English? … Answer with ONLY the single digit 1 or
2."* A pick is CORRECT if the model selects the grammatical member. `usage.cost` recorded via
[`experiments/lib/openrouter.py`](../../lib/openrouter.py). `ABORT_USD = 1.60` per model in `probe.py`.

## Q1-A — paradigm & item selection (accuracy-blind AND human-agreement-blind)

- **6 frame-safe paradigms**, 3 shallow (local) + 3 deep (scope), selected by a deterministic
  **swappability score** = mean count of swappable open-class positions/item over a fixed seeded sample
  (`SEL_SEED=77770711`, `SEL_N=80`), ties by UID alphabetical, computed **blind to accuracy and human
  agreement** (`build_swap.py:swappability_score`). Candidate sets:
  - shallow (frame-safe regular): `determiner_noun_agreement_1/_2`, `regular_plural_subject_verb_agreement_1/_2`.
  - deep (closed-class licensor → frame-safe): `npi_licensing` ∪ `quantifiers` (11 paradigms).
  - **EXCLUDED (G-frame):** `island_effects` / `filler_gap_dependency` (a POS-preserving verb swap can
    break the gap-licensing subcategorization frame) and every `irregular_*` paradigm (irregular morphology
    carries the contrast). The **deep-pole generality cost** — the swap covers the **scope-deep** pole, not
    the **island-deep** pole where the models were weakest — is reported and travels into candidacy.
- **Selected this freeze** (scores in `selection.json`): **shallow** = `determiner_noun_agreement_2`
  (2.125), `determiner_noun_agreement_1` (1.738), `regular_plural_subject_verb_agreement_1` (1.387);
  **deep** = `sentential_negation_npi_scope` (3.038), `only_npi_scope` (2.888), `superlative_quantifiers_1`
  (1.962).
- **ORIGINAL condition = a FRESH seeded ≈100-pair subsample re-run this session** (`SEED=20260711`,
  `SAMPLE_N=130` drawn, first `TARGET_N=100` usable kept), **not** the s205 frozen accuracies — so
  `Δacc = acc_swap − acc_orig` is a **within-run paired** quantity with **no known-accuracy exposure** (the
  anti-cheat advantage). Usable-pair floor `USABLE_FLOOR=60`; below it a paradigm is dropped and power
  re-stated (G-power).

## Q2-B — the swap operationalization (the crux): POS from the published 2012 file, frequency = SUBTLEX-US Lg10WF

- **Frequency norm (match):** SUBTLEX-US `Lg10WF = log10(FREQcount+1)` — the human-validated log-frequency
  scale — computed from `FREQcount` in the **2012 "SUBTLEX-US frequency list with PoS and Zipf information"**
  file (Q2-B). Each replacement matched **within ±0.10 `Lg10WF`** of the original form (`BAND=0.10`, the
  band the resource page already names). The 2012 file is fetched + **sha256-pinned** (zip
  `458128f9…d15090`; inner xlsx `3a8cb93a…4167a7`), handled recipe-not-corpus (gitignored; only the recipe
  + derived pool sizes/sha committed), license posture identical to the in-repo 2009 file
  ([`resource/subtlex-us-frequency`](../../../wiki/base/resources/subtlex-us-frequency.md), extended this
  session). Fallback to Q2-A (2009 file + rule POS) only if the 2012 fetch/license fails — **it did not**.
- **POS (published, not curated — Q2-B):** `Dom_PoS_SUBTLEX` from the 2012 file supplies the part of speech
  (Name / Noun / Adjective / …), removing the last build DoF (G-lexicon-determinism). Pool membership
  (`build_pools`): dominant-POS ≥ **0.75**, alphabetic length ≥ 3, no `-ing`/`-ed`, minus a small profanity
  junk list; **singular-noun** pool additionally requires the isolated form to nltk-tag `NN` (excludes
  irregular plurals men/children/feet/data that a Dom_PoS='Noun' filter alone would admit). The **only DoF
  is membership**; substitute selection is seeded-deterministic from the **full eligible in-band set**
  (`pick()`), never per-item hand-assignment.
- **Swap categories (BUILD RULING, ratified):** replace **common nouns + proper names + attributive
  adjectives** — the frame-safe open-class categories that carry **no subcategorization frame**. **Main
  verbs and adverbs are held fixed** (verbs carry valence; adverbs are often the contrast locus or
  licensing-sensitive). This is the noun-only ruling; its perturbation bound is measured by **G-coverage**.
- **Substitution recipe (`build_swap.py:swap_pair`):** per pair `(good, bad)` — (1) locate the contrast
  locus = token(s) differing between good and bad (**never swapped**, EXCEPT the det-noun carve-out below);
  (2) a common noun is swappable only in an **NP-internal left context** (preceded by det/adj/prep/
  possessive/number/noun — this excludes bare sentence-final main verbs that a POS tagger mis-tags as
  nouns); a proper name only if title-case alphabetic; an adjective only if **attributive** (followed by a
  noun/adj); (3) replace with a novel same-POS in-band substitute, **number/inflection preserved** (plural
  nouns → rule-pluralized substitute, verified corpus-attested); closed-class `a/an` re-normalized to the
  following word's phonology.
- **det-noun carve-out:** where the contrast IS the head noun's number, the locus noun's **lemma** is
  swapped with each member's number feature preserved (good/bad keep their sg/pl); a pair whose contrast
  noun is **irregular** (neither member is the regular plural of the other) is **dropped** (G-frame).
- **sv subject guard:** in subject–verb paradigms a proper name **before** the agreement locus is the
  subject (ambiguous number → could flip agreement) and is **held fixed**; objects (after the verb) stay
  swappable.

## Q3-A — mechanical re-validation (no human subjects) + bounded candidacy

- **Mechanical admission (drop, never repair; `build_swap.py`):** (i) ≥1 swap; (ii/iv) the good/bad
  contrast survives with the **same number of differing token-positions** as the original (no collapsed or
  new contrast); (iii) no `a/an`-before-vowel error introduced; every substitute is a real in-band attested
  form of the matched POS/number; (v) frame-preservation is structural (only frame-free categories swapped;
  island/filler-gap + irregular_* excluded at Q1). A dropped pair is **logged and reported**
  (`selection.json → build_report`); a paradigm below `USABLE_FLOOR=60` is dropped and power re-stated.
- **Researcher spot-audit (not a human-subject task, rule 4):** the lead reviews `build_report`'s audit
  sample of admitted pairs for gross selectional anomaly, as the researcher running the instrument;
  systematic anomaly is reported as a limitation, never silently fixed. **Note:** the 2AFC asks which of
  the *two* members is more acceptable and both members share the identical swapped content, so semantic
  oddity of a substitute **cancels in the forced choice** — it cannot bias `Δacc`.
- **Promotion scope (bounded):** SWAP-STABLE ∧ (s208) SURVIVES-COVARIATE → R1 becomes a **bounded
  promotion-review CANDIDATE** — a later, separate, cross-session adversarial review writes the `claim`
  (this run earns candidacy, never ratifies). SWAP-DROPS → R1 refused; the shadow-depth table's form-(iv)
  row keeps only its within-panel DEPTH-GRADED sibling.

## Metric + verdict map (G-metric — signed-CI equivalence, PINNED; not mean-of-absolutes)

Let `acc_C(m,p)` = model m's order-averaged 2AFC accuracy on paradigm p under condition C ∈ {orig, swap},
both conditions **re-run fresh**, both orders, position-bias-netted. Per pairID, `Δ_pair = acc_swap_pair −
acc_orig_pair` (order-averaged per member; the orig and swap sentences of the same pairID are the paired
unit). **Per model, per stratum**, `Δ̄ = mean Δ_pair` over the stratum's 3 paradigms' pairs; a percentile
**bootstrap CI** (`BOOT=5000`, `SEED=20260711`) is taken by resampling pairs.

- **SWAP-STABLE (TOST-style equivalence)** iff the per-model per-stratum `Δ̄` bootstrap CI **sits within
  ±0.05** on **both** the shallow and deep strata for **≥2/3 models** — the profile is statistically
  equivalent-to-unchanged under swap (does not depend on exact-string memorization).
- **SWAP-DROPS** iff `Δ̄ ≤ −0.05` with its CI **excluding 0** within a stratum on **≥2/3** — the exact
  strings were load-bearing (a first-class negative).
- **SWAP-INCONCLUSIVE** otherwise (a CI that neither fits within ±0.05 nor clears −0.05 — the honest
  under-power landing).
- **Combined promotion verdict (G8, inherited):** candidacy requires **SURVIVES-COVARIATE (s208) ∧
  SWAP-STABLE (this run)**. A SWAP-DROPS refuses promotion.

**G-margin-justification.** The ±0.05 margin is a **pre-registered practical-equivalence threshold**, not a
convenience cutoff: it matches the s205 `DEPTH_MARGIN` (0.05, the smallest per-model depth gap the parent
design treats as a real difference) and the s205 human shallow−deep agreement gap scale, so "within ±0.05"
means "smaller than the smallest grammatical-difficulty difference the parent instrument is designed to
resolve." At N≈100 fresh paired items/paradigm the per-paradigm Δ SE ≈ 0.03 and the per-stratum (≈300 pairs)
`Δ̄` SE is smaller, so the equivalence test is adequately powered to place the CI inside ±0.05 under a true
Δ≈0; the shallow stratum sits near ceiling (s205 local acc 0.98–0.99) so **the deep-3 carry the real test**.

## G-coverage (mandatory — the noun-only perturbation is measured and gated)

`build_swap.py` reports, per paradigm, **swap coverage** = mean(fraction of swap-eligible-category tokens
actually replaced) and **mean nsub** (mean tokens changed/item, the token-level surface edit distance).
**Coverage floor = 0.50** (pre-registered): a paradigm below it has a **weak/uninformative** perturbation
and its SWAP-STABLE is **flagged and EXCLUDED from the ≥2/3 stratum verdict**. Selected paradigms this
freeze all clear it (shallow 0.70–0.98; deep 0.97–0.98). **Perturbation bound recorded:** SWAP-STABLE means
"stable under frequency-matched replacement of content nouns / proper names / attributive adjectives,
holding the closed-class skeleton, main verbs, and adverbs fixed" — **not** under full open-class
replacement (verb/adverb swapping with a subcategorization guard is a deferred stronger-perturbation
sensitivity arm).

## Diagnostics

- **Instrument-failure guard (Q2-A, carried verbatim from s205):** if position-lock rate > **0.50** AND
  |ans1_rate − 0.5| > **0.40** on ≥2/3 models, the 2AFC has collapsed to position-answering →
  **INSTRUMENT-FAILURE** voids the accuracy readings (reported, not silently dropped). Reported per model.
- **G-freq (achieved match):** the per-word `Lg10WF` gap distribution of orig→swap substitutes (≤0.10 by
  construction; reported).
- **G-freq-pretraining (the seam between the two arms — $0 model cost):** `analyze_swap.py` streams the
  frozen s208 C4 adapter (`build_cooc_c4.py:stream_sentences`) over a **bounded** prefix (pinned
  `C4_MAX_SENTENCES`) to compare the **swap-set vs original-set unigram C4 (pretraining-proxy)
  log-frequency**. A material gap (swap set materially rarer in C4 than the originals) is a **load-bearing
  limitation on any SWAP-DROPS reading** (a Δacc could be a pretraining-frequency drop, not memorization)
  and travels into candidacy alongside G3′.

## Pre-named outcomes (symmetric — the anti-cheat guarantee)

SWAP-STABLE, SWAP-DROPS (first-class negative), SWAP-INCONCLUSIVE, an INSTRUMENT-FAILURE void, a paradigm
dropped for too-many broken-pair drops, and a coverage-floor exclusion are **all pre-registered**. Bands are
identical for SWAP-STABLE and SWAP-DROPS. `predictions.md` bet registered at this freeze.

## Scope caps (carry into any citation)

1. Controls **R1 only**, and only the **exact-string / lexical-item memorization** sub-confound; does not
   control **construction frequency** or template difficulty (G3′), does not touch R2/R2h.
2. SWAP-STABLE means "not driven by memorizing the exact BLiMP strings," **never** "grammatical competence";
   absolute accuracy stays a contamination upper bound.
3. Frequency match is only as good as SUBTLEX-US `Lg10WF` + the ±0.10 band; residual per-word gap reported.
4. Deep-pole generality cost (scope-deep covered, island-deep not); perturbation bound (nouns/names/adjs
   only). 5. n=3 models; per-model, per-stratum Δ, never pooled.
