---
type: resource
id: subtlex-us-frequency
title: SUBTLEX-US word-frequency norm (Brysbaert & New 2009)
status: catalogued
url: https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus
url-note: "Landing page lists multiple format downloads; the plain-text 74,286-word list used here is subtlexus2.zip -> SUBTLEXus74286wordstextversion.txt. Fetched + checksummed THIS session (2026-06-21): 3,298,971 bytes, sha256 c5f86f065fc5d057fbf366433b8c5ca550aa7c24e128362dea4394f2b29c86e4. The old crr.ugent.be/papers/... path now 404s; the ugent.be landing page is the live source."
paper: "Brysbaert, M., & New, B. (2009). Moving beyond Kucera and Francis: A critical evaluation of current word frequency norms and the introduction of a new and improved word frequency measure for American English. Behavior Research Methods, 41(4), 977-990."
venue: "Behavior Research Methods 41(4): 977-990 (2009)"
license: "No formal license string (no CC/GPL stamp) is attached on the source page; the data is distributed openly for research use with the request to cite Brysbaert & New (2009). Recipe-not-corpus posture adopted: full list gitignored + sha256-pinned, only prep.py + a small derived seed table committed."
local-path: "experiments/data/subtlex-us/function-word-seed-frequencies.csv (small derived seed table only; full 74,286-word list gitignored, sha256-pinned, re-downloadable via experiments/data/subtlex-us/prep.py)"
meaning-senses:
  - distributional
  - human-comparison
contingent-on: []
created: 2026-06-21
updated: 2026-06-21
links:
  - rel: depends-on
    target: concept/distributional-meaning
---

# SUBTLEX-US word-frequency norm (Brysbaert & New 2009)

> **Verification status (2026-06-21):** the plain-text 74,286-word list was **downloaded
> and checksummed this session** — `SUBTLEXus74286wordstextversion.txt`, 3,298,971 bytes,
> sha256 `c5f86f065fc5d057fbf366433b8c5ca550aa7c24e128362dea4394f2b29c86e4`, from
> `subtlexus2.zip` on the Ghent University landing page. The column schema, the
> function-word swap-target frequencies, and a candidate content-control band were inspected
> firsthand and emitted to the committed derived table (see *Where it lives*). **No formal
> license string was found** on the source page; the norm is distributed openly for research
> with a citation request — handled here under the project's recipe-not-corpus posture (full
> list gitignored, derived seed table committed). This page catalogs SUBTLEX-US as the
> **frequency-matching norm (Q1)** for the function-word-vs-content-word swap probe,
> [`conjecture/function-word-substitutability`](../../findings/conjectures/function-word-substitutability.md),
> per the ratified decision [`decisions/resolved/function-word-anchor-design`](../../decisions/resolved/function-word-anchor-design.md).

## What it is

SUBTLEX-US is a word-frequency norm for American English built from a **51-million-word
corpus of film and television subtitles**. Brysbaert & New (2009) introduced it as a
replacement for the dated Kučera-Francis (1967) and CELEX norms, showing it accounts for
**substantially more variance in lexical-decision reaction times and accuracies** (from the
English Lexicon Project) than either predecessor — i.e. it is the frequency measure that
best predicts human word-processing behavior among the standard options. It is one of the
most widely used stimulus-matching norms in psycholinguistics.

The plain-text list covers **74,286 word forms**, each with the columns (tab-separated):

- `Word` — the orthographic word form.
- `FREQcount` — raw occurrence count in the 51M-word corpus.
- `CDcount` — contextual diversity: number of the 8,388 films/programs the word appears in.
- `FREQlow`, `Cdlow` — counts restricted to lowercase occurrences.
- `SUBTLWF` — frequency **per million words** (the standard reportable frequency).
- **`Lg10WF`** — `log10(FREQcount + 1)` — **the matching variable this project uses** (log
  frequency is the psycholinguistically standard scale on which frequency effects are linear).
- `SUBTLCD`, `Lg10CD` — the contextual-diversity analogues.

### How it was made

The corpus was assembled from American film and TV subtitles (8,388 films/programs); raw
word-form counts were taken over the 51M tokens, then transformed to per-million and log10
measures. The signal is a **corpus frequency count**, not a human rating task — its human
bearing is that it is compiled from human-produced language and is **validated against human
lexical-processing latencies** (the variance-accounted-for tables in Brysbaert & New 2009).

## What it can ground

This is the section that matters (charter rule: cite a resource by the *feature* that bears).

**SUBTLEX-US grounds the frequency-matching control (Q1) of the function-word swap probe.**
The conjecture's whole risk is that "frequency-matched" can be gamed to manufacture a
function > content asymmetry; the ratified decision makes a single fetched unigram norm the
**floor** on which the function-swap words and the content-swap controls are matched, frozen,
and hashed before any model output is seen. SUBTLEX-US's `Lg10WF` column is that norm. It
supplies:

- A **per-word-form log-frequency** value for every swap target and every candidate control,
  so the function-swap set and the content-swap set can be matched on the dimension that, if
  uncontrolled, would by itself drive a behavior shift (the `distributional` control variable).
- The **within-pair frequency gaps** of the named function-word swap partners, computed
  firsthand this session and committed to the seed table — which concretely document the
  decision's Q1-C concern that several swap partners are *not* pair-level frequency-matchable:
  `because` (Lg10WF 4.74) → `although` (3.33) is a **1.41 log-unit (~25×)** gap;
  `some` (4.94) → `every` (4.45) is 0.50; `the` (6.18) → `a` (6.02) is 0.16;
  `will` (5.03) → `would` (4.96) is 0.08. So pair-level matching is satisfiable for the
  modal pair, marginal for the determiner pair, and **infeasible** for the subordinator and
  quantifier pairs — exactly the build-session constraint the decision flagged.
- A **candidate open-class content-control band** within ±0.10 Lg10WF of each mid-band
  function word (would/some/every/because), from which the build session draws its
  certified, frozen control set. The committed candidate pool shows solid matches exist
  (e.g. *man, take, time, father, girl, leave, thing, people, give* all within ~0.01–0.05
  Lg10WF of a function-word anchor) **and** that the raw band carries discourse junk
  (interjections, contraction fragments, capitalized names) the build session must curate —
  the candidate pool is explicitly **NOT** the frozen set.

In the optional **Posture-2 upgrade** (a human-comparison claim, see the decision Q3), the
norm's human-validated status — it is the frequency measure best predicting human RTs — is
what would let a function/content asymmetry be referred to a human-behavior baseline; but the
default result posture is `internal-contrast-only` and does **not** require this.

## What it cannot ground

The limits are sharp and worth stating so no later session over-reads it:

- **It is a frequency norm, not a function/content classification.** SUBTLEX-US does not
  label words as function vs content. The function-word swap targets are a **hand-enumerated
  closed class** (determiners, modals, subordinators, quantifiers); the norm only supplies
  their frequencies, not their grammatical category.
- **The plain-text 2009 list carries no part-of-speech.** Selecting frequency-matched *content*
  controls by PoS would need the separate "SUBTLEX-US with PoS information" file (Brysbaert,
  New & Keuleers 2012), which is **not fetched** — the closed-class stoplist used to keep the
  candidate pool open-class is a convenience filter, not a PoS annotation.
- **Word-form frequency aggregates over senses and PoS.** A single `Lg10WF` per orthographic
  form mixes, e.g., *will* the modal with *will* the noun/verb. The build session must treat
  these as form-level frequencies, not lemma- or sense-level.
- **It is not an acceptability or entailment resource.** SUBTLEX-US says nothing about whether
  a swap is grammatical, natural, or inference-altering. It cannot anchor the **indicator**
  (Q2, entailment-flip / forced-choice) — that needs BLiMP/NLI (a separate, not-yet-fetched
  fetch-and-catalogue-first resource) and is only the optional Posture-2 upgrade.
- **Subtitle-corpus register.** Frequencies reflect conversational film/TV English; very
  formal or technical vocabulary is under-counted relative to a balanced corpus.

## Where it lives — download and in-repo handling

- **Source (live):** the Ghent University landing page
  `https://www.ugent.be/pp/experimentele-psychologie/en/research/documents/subtlexus` lists
  the downloads. The plain-text list is `subtlexus2.zip` → `SUBTLEXus74286wordstextversion.txt`.
  (The older `crr.ugent.be/papers/SUBTLEX-US_frequency_list_with_PoS_information_text_version.zip`
  path now returns 404.)
- **Fetched + verified this session:** 3,298,971 bytes, sha256
  `c5f86f065fc5d057fbf366433b8c5ca550aa7c24e128362dea4394f2b29c86e4`.
- **In-repo handling (recipe-not-corpus):** the full 74,286-word list is **gitignored**
  (`experiments/data/subtlex-us/.gitignore`); committed are `prep.py` (the download + sha256
  + derive recipe) and `function-word-seed-frequencies.csv` (the ~56-row derived seed table:
  the 8 swap targets + within-pair gaps + the candidate content band). No wholesale corpus
  text is committed.

## Known limits / scope

- **License: no formal string; open-for-research + citation request.** Recipe-not-corpus
  posture adopted (gitignore the list, commit only the recipe + small derived table). This is
  the conservative handling used for other no-explicit-license resources in the catalog.
- **Frequency norm only.** Grounds the Q1 matching control; does **not** ground the Q2
  indicator or any acceptability/entailment claim.
- **No PoS in the fetched file; aggregates over senses.** Form-level frequencies only.

## Verified / Unverified / Open breakdown

| Item | Status | Source |
|------|--------|--------|
| Citation (Brysbaert & New 2009, BRM 41(4):977–990) | **VERIFIED** | Source landing page references; standard citation |
| 51M-word subtitle corpus; 74,286 word forms | **VERIFIED** | Landing page text + list line count (74,286 rows) |
| Column schema (Word/FREQcount/CDcount/FREQlow/Cdlow/SUBTLWF/Lg10WF/SUBTLCD/Lg10CD) | **VERIFIED** | File header, inspected this session |
| Accounts for more RT/Acc variance than Kučera-Francis & CELEX | **VERIFIED** | Landing page variance tables (SUBTL WF 30.1/62.3 vs KF 19.6/57.7) |
| Function-word swap-target frequencies + within-pair gaps | **VERIFIED (computed this session)** | `function-word-seed-frequencies.csv` |
| File: 3,298,971 bytes, sha256 c5f86f06… | **VERIFIED (downloaded this session)** | curl from subtlexus2.zip, 2026-06-21 |
| Formal license (CC/GPL) | **NONE FOUND** | No license string on the landing page |
| Part-of-speech per word | **NOT IN FETCHED FILE** | Needs the separate 2012 "with PoS" file (not fetched) |
| Sense- or lemma-level frequency | **NOT PROVIDED** | Word-form counts aggregate over senses/PoS |

## Pointer for next visit

1. **Use as the Q1 matching norm now.** The seed table is committed; the build session draws
   the frozen, hashed function-vs-content minimal-pair set to the ratified scheme (frequency
   floor + length/predictability tightening + pair-level where feasible), under an independent
   pre-run critic — **no item added/dropped after the first probe call**.
2. **Respect the pair-level infeasibility.** `because→although` and `some→every` cannot be
   pair-level frequency-matched; the build session matches the *content control's* frequency
   to each function word individually and reports the achieved gap distribution, rather than
   forcing a within-pair match that would drop the most diagnostic items.
3. **Do not over-reach to the indicator.** SUBTLEX-US cannot anchor the entailment-flip /
   forced-choice indicator (Q2). A BLiMP/NLI human backing is the separate, optional,
   fetch-and-catalogue-first Posture-2 upgrade — it never blocks the within-model run.
4. **PoS upgrade if needed.** If auditable PoS-based content-control selection is wanted,
   fetch the 2012 "SUBTLEX-US with PoS information" file and extend this page.
