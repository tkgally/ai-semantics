---
type: resource
id: blimp
title: BLiMP — Benchmark of Linguistic Minimal Pairs for English (Warstadt et al. 2020)
status: catalogued
url: https://github.com/alexwarstadt/blimp
url-note: "Code + data repo. Mirror dataset also at HuggingFace nyu-mll/blimp (license cc-by-4.0). Paper: arXiv 1912.00582 / TACL vol. 8 (2020), https://aclanthology.org/2020.tacl-1.25/. One sample paradigm file fetched + sha256-pinned THIS session (2026-06-21): determiner_noun_agreement_1.jsonl full file 468,642 bytes sha256 f48065fd760d0fd1a895012860d38bdf3c2ac115cd221e521684cc430c0f1855; a committed 10-line sample is sha256 0a05d83fae0e255f0faf3bd7907596079bf82463f283b98403c2d549c114b6e8."
paper: "Warstadt, A., Parrish, A., Liu, H., Mohananey, A., Peng, W., Wang, S.-F., & Bowman, S. R. (2020). BLiMP: The Benchmark of Linguistic Minimal Pairs for English. Transactions of the Association for Computational Linguistics, 8, 377-392."
venue: "Transactions of the Association for Computational Linguistics (TACL), Volume 8 (2020). https://aclanthology.org/2020.tacl-1.25/"
license: "CC-BY (the repo README states 'BLiMP is distributed under a CC-BY license' linking creativecommons.org/licenses/by/4.0/; the HuggingFace mirror nyu-mll/blimp lists 'cc-by-4.0'). VERIFIED 2026-06-21. Note: the GitHub repo has no standalone LICENSE *file* in its tree — the license is asserted in the README prose only."
local-path: "experiments/data/blimp/determiner_noun_agreement_1.sample.jsonl (a SMALL 10-line sample of one paradigm) AND experiments/data/blimp/human_validation_summary.csv (the FULL per-paradigm human-agreement summary, 3,057 bytes, sha256 ea0e7c21de6b9df2fd8a94d0b175e84ea57627e4cbfa1fcba4ef8b3d0fba1b2d, committed 2026-07-10 s204). The full 67,000-pair dataset itself is NOT committed — re-fetchable from the repo's data/ directory."
meaning-senses:
  - constructional
  - human-comparison
contingent-on: []
created: 2026-06-21
updated: 2026-07-10
links:
  - rel: depends-on
    target: concept/distributional-meaning
---

# BLiMP — Benchmark of Linguistic Minimal Pairs for English (Warstadt et al. 2020)

> **Verification status (2026-06-21):** all structural facts below were fetched this
> session from the arXiv abstract page (`arxiv.org/abs/1912.00582`), the ACL Anthology
> TACL entry (`aclanthology.org/2020.tacl-1.25/`), the repo README
> (`raw.githubusercontent.com/alexwarstadt/blimp/master/README.md`), the repo `data/`
> directory listing (the 67 `.jsonl` filenames), and the HuggingFace mirror
> (`huggingface.co/datasets/nyu-mll/blimp`). **One paradigm file
> (`determiner_noun_agreement_1.jsonl`) was downloaded and its JSON field schema
> inspected firsthand**; a 10-line sample is committed and sha256-pinned (see *Where it
> lives*). The full 67,000-pair dataset is **not** committed (re-fetchable, CC-BY).
> This page catalogues BLiMP as the named, **optional, fetch-and-catalogue-first**
> human-acceptability backing for the Posture-2 upgrade of the function-word swap probe
> ([`decisions/resolved/function-word-anchor-design`](../../decisions/resolved/function-word-anchor-design.md)),
> and as a candidate human-acceptability anchor for the grammatical-agreement work
> (determiner-noun agreement bears on the AANN line). The page states precisely what
> BLiMP **can** and **cannot** anchor for those lines.

## What it is

BLiMP is a challenge set of **English minimal pairs** that isolate single grammatical
contrasts. From the TACL abstract (verbatim, `aclanthology.org/2020.tacl-1.25/`):

> "We introduce The Benchmark of Linguistic Minimal Pairs (BLiMP), a challenge set for
> evaluating the linguistic knowledge of language models (LMs) on major grammatical
> phenomena in English. BLiMP consists of 67 individual datasets, each containing 1,000
> minimal pairs—that is, pairs of minimally different sentences that contrast in
> grammatical acceptability and isolate specific phenomenon in syntax, morphology, or
> semantics. We generate the data according to linguist-crafted grammar templates, and
> human aggregate agreement with the labels is 96.4%. We evaluate n-gram, LSTM, and
> Transformer (GPT-2 and Transformer-XL) LMs by observing whether they assign a higher
> probability to the acceptable sentence in each minimal pair."

So the structure is:

- **67 paradigms** ("sub-datasets" / "individual datasets"), each isolating one contrast.
- **1,000 minimal pairs per paradigm** → **67,000 minimal pairs total**.
- Each pair is `(sentence_good, sentence_bad)`: a grammatically **acceptable** vs an
  **unacceptable** sentence differing minimally.
- Data is **template-generated** from "linguist-crafted grammar templates" (also phrased
  "expert-crafted grammars" in the arXiv abstract) — i.e. **synthetic**, not naturally
  occurring text.

### Field schema (inspected firsthand this session)

The fetched `determiner_noun_agreement_1.jsonl` is one JSON object per line with these keys
(confirmed by parsing the file): `sentence_good`, `sentence_bad`, `field`
(one of morphology / syntax / syntax-semantics / semantics), `linguistics_term` (the
phenomenon category), `UID` (paradigm id), `pairID` (0–999), and the LM-scoring-method
booleans `simple_LM_method`, `one_prefix_method`, `two_prefix_method`, plus
`lexically_identical` and (for one-prefix paradigms) `one_prefix_prefix` /
`one_prefix_word_good` / `one_prefix_word_bad`. Example line (verbatim from the fetched
file):

> `{"sentence_good": "Raymond is selling this sketch.", "sentence_bad": "Raymond is selling this sketches.", ... "field": "morphology", "linguistics_term": "determiner_noun_agreement", "UID": "determiner_noun_agreement_1", ... "pairID": "0"}`

### The 12 phenomenon categories

The repo README states the `linguistics_term` field "has 12 possible values, discussed in
the paper." The paper groups the 67 paradigms under **12 high-level phenomenon
categories**: anaphor agreement, argument structure, binding, control/raising,
determiner-noun agreement, ellipsis, filler-gap dependency, irregular forms, island
effects, NPI licensing, quantifiers, and subject-verb agreement. *(The 12-category names
are as standardly reported and corroborated by the 67 fetched `.jsonl` filenames below;
the exact **per-category paradigm counts** were not independently re-derived this session
— treat the category list as verified and per-category counts as not-yet-verified.)*

The 67 paradigm filenames (fetched verbatim from the repo `data/` directory this session)
make the mapping concrete; a sample by category:

- **determiner-noun agreement** — `determiner_noun_agreement_1/2`,
  `determiner_noun_agreement_irregular_1/2`, `determiner_noun_agreement_with_adjective_1`,
  `determiner_noun_agreement_with_adj_2`, `determiner_noun_agreement_with_adj_irregular_1/2`
  (8 paradigms; **the category most directly relevant to the AANN article+adjective+noun line**).
- **subject-verb agreement** — `regular_plural_subject_verb_agreement_1/2`,
  `irregular_plural_subject_verb_agreement_1/2`,
  `distractor_agreement_relational_noun`, `distractor_agreement_relative_clause`.
- **NPI licensing** — `npi_present_1/2`, `only_npi_licensor_present`, `only_npi_scope`,
  `matrix_question_npi_licensor_present`, `sentential_negation_npi_licensor_present`,
  `sentential_negation_npi_scope`.
- **quantifiers** — `existential_there_quantifiers_1/2`, `superlative_quantifiers_1/2`.
- **argument structure** — `causative`, `inchoative`, `intransitive`, `transitive`,
  `drop_argument`, `passive_1/2`, `animate_subject_passive`, `animate_subject_trans`.
- **island effects** — `adjunct_island`, `complex_NP_island`, `wh_island`,
  `sentential_subject_island`, `coordinate_structure_constraint_*`, `left_branch_island_*`.
- **filler-gap** — `wh_questions_*`, `wh_vs_that_*`.
- **binding** — `principle_A_*`.
- **control/raising** — `tough_vs_raising_1/2`, `existential_there_*_raising`,
  `expletive_it_object_raising`.
- **anaphor agreement** — `anaphor_gender_agreement`, `anaphor_number_agreement`.
- **irregular forms** — `irregular_past_participle_adjectives`,
  `irregular_past_participle_verbs`.
- **ellipsis** — `ellipsis_n_bar_1/2`.

### Human agreement / validation (what the 96.4% measures)

The reported human number is **aggregate human agreement with the labels = 96.4%**
(abstract, verbatim above). This is a **validation/agreement** figure: human annotators
were asked, per item, to pick the acceptable member of the minimal pair, and 96.4% is the
aggregate rate at which their forced choice agreed with the template-assigned `good`/`bad`
label. The repo also ships "Full human validation judgments" in its `raw_results` folder
(per the README). The figure functions as a **human ceiling / baseline** against which LM
forced-choice accuracy is read.

#### Per-paradigm human agreement (committed + verified firsthand 2026-07-10, s204)

The aggregate 96.4% is not the only human signal BLiMP ships: the repo's
`raw_results/summary/human_validation_summary.csv` carries a **per-paradigm** human-agreement rate.
That file was fetched, inspected, and **committed to this repo** this session
(`experiments/data/blimp/human_validation_summary.csv`, 3,057 bytes, sha256
`ea0e7c21de6b9df2fd8a94d0b175e84ea57627e4cbfa1fcba4ef8b3d0fba1b2d`; **69 per-condition rows**). Its
columns are **`Condition,accepted,total_mean,count`** — `Condition` = the per-paradigm UID; `total_mean`
= the per-paradigm human agreement rate; `count` ≈ 97–100 human judgments per paradigm. Per-paradigm
human agreement **ranges from 0.47 to 0.99** across the 69 conditions:

- **Lowest (humans themselves divided):** `wh_questions_object_gap_long_distance` **0.47**,
  `coordinate_structure_constraint_subject_extraction` **0.514**, `sentential_subject_island` **0.606**,
  `only_npi_scope` **0.72**, `wh_island` **0.73** — long-distance / island / NPI-scope contrasts.
- **Highest (near-unanimous):** `transitive` / `left_branch_island_simple_question` /
  `irregular_past_participle_adjectives` / `anaphor_number_agreement` **0.99**,
  `wh_questions_subject_gap` **0.98**.
- **Local agreement (mid-high):** `determiner_noun_agreement_1` **0.958**,
  `determiner_noun_agreement_with_adjective_1` **0.95**, `regular_plural_subject_verb_agreement_1`
  **0.95**; distractor agreement **0.81** (`..._relational_noun`) / **0.857** (`..._relative_clause`);
  `npi_present_1` **0.83**, `sentential_negation_npi_scope` **0.81**, `existential_there_quantifiers_1`
  **0.94**, `adjunct_island` **0.94** (all values verbatim from the committed CSV).

**What this grounds (and what it does not).** The per-paradigm `total_mean` is a genuine **human
difficulty profile** across grammatical phenomena — a real human-comparison anchor for "are models hard
where humans are hard" (the profile the A3b forced-choice sweep design measures against;
[`design/blimp-forced-choice-sweep-v1`](../../../experiments/designs/blimp-forced-choice-sweep-v1.md)).
Two honest limits: (i) **it is an agreement rate, not a graded acceptability norm** — `total_mean` is
the fraction of human validators who endorsed the template's `good`/`bad` label, so a low value
(e.g. 0.514, near chance) means the **gold label itself is contested**, not that the contrast is
"hard" in a graded sense — any use of a sub-~0.6-agreement paradigm as a model-accuracy gold must flag
that the key is shaky; (ii) **the summary has 69 rows, not the paper's 67 paradigms** — the two extra
`Condition` rows are noted but not reconciled here (use the committed CSV as the operative per-UID
source, and re-derive counts before quoting a paradigm total).

The Mahowald-2024 source in this repo cites the aggregate figure as a baseline —
"86% on BLiMP (cf. human baseline of 89%)" in that paper refers to a model's score vs a
human baseline (note: 89% is the figure that source quotes; the original BLiMP paper's own
aggregate human-agreement figure is 96.4% — the two numbers come from different
measurements and should not be conflated). See
[`source/mahowald-2024-dissociating`](../sources/mahowald-2024-dissociating.md).

## What it can ground

**BLiMP grounds a human-acceptability, forced-choice minimal-pair signal for English
grammatical phenomena** — "which member of the pair is the acceptable one," with a
human-agreement baseline (96.4%). Concretely, for in-repo grammatical-axis work:

- **For the function-word swap probe (the Posture-2 upgrade named in
  [`decisions/resolved/function-word-anchor-design`](../../decisions/resolved/function-word-anchor-design.md)):**
  BLiMP can supply a **human-acceptability backing** for whether a function-word swap lands
  where humans find the swap most *disruptive to grammatical acceptability*. Several BLiMP
  categories overlap the probe's swap targets: **determiner-noun agreement** (the `the`/`a`,
  determiner-agreement family), **quantifiers** (the `some`/`every` family), **NPI
  licensing**, and **subject-verb agreement**. If the probe's flip-rate asymmetry is to be
  referred to a human signal, BLiMP's acceptability judgments on the relevant grammatical
  contrasts are a legitimate human reference. Per the decision, this is an **optional
  upgrade that never blocks the within-model run** (the result posture stays
  `internal-contrast-only` by default).
- **For the AANN line:** BLiMP's **determiner-noun agreement** paradigms (8 of them,
  including the `with_adjective` variants) bear on the article+adjective+numeral+noun
  agreement structure probed by
  [`resource/mahowald-2023-aann-stimuli`](mahowald-2023-aann-stimuli.md) and
  [`conjecture/aann-construction`](../../findings/conjectures/aann-construction.md). BLiMP
  is **not** an AANN-specific stimulus set (it has no article+adjective+numeral+plural-noun
  construction), but it offers an independent human-validated agreement baseline on adjacent
  determiner-noun agreement contrasts.
- **General:** a cross-model **forced-choice accuracy** comparison on the same 67,000
  template items, with a shared human-agreement reference — the same forced-choice logic
  the panel can run logprob-free (present each member, record which the model prefers).

## What it cannot ground

The limits are sharp and stated so no later session over-reads BLiMP:

- **It is ACCEPTABILITY (grammatical well-formedness), not entailment/inference.** BLiMP
  pairs contrast *grammaticality*, not truth-conditional or inferential relations. It does
  **not** anchor the function-word probe's **entailment-flip indicator** (Q2(i) of
  [`decisions/resolved/function-word-anchor-design`](../../decisions/resolved/function-word-anchor-design.md))
  against human *entailment* labels — that wants a human **NLI** set (separate,
  not-yet-fetched). BLiMP can back the *acceptability* reading of a swap's disruption, not
  the *inferential* reading.
- **Not implicature / not "which reading humans favor."** BLiMP says nothing about scalar
  implicature or preferred interpretations; its quantifier/NPI paradigms are
  acceptability contrasts, not pragmatic-reading preferences. It cannot ground a
  "which reading humans favor" claim.
- **Not sense-similarity.** It is silent on lexical sense, polysemy, or graded
  similarity (those are the province of WiC / DWUG / WordNet resources in the catalog).
- **Template-generated → contamination + naturalness caveat.** Items are synthetic,
  published since 2019, and **very widely used in LM training and evaluation**, so BLiMP
  sentences are plausibly in the training data of the panel models; and template-generated
  sentences are less natural than corpus text. Any use as an anchor must flag the
  contamination risk (this is the same caveat the decision raised against *lifting*
  function-word minimal pairs from BLiMP rather than building synthetic ones — see the Q3
  "Stimulus source" discussion in the decision page).
- **English only; agreement-heavy coverage.** All 67 paradigms are English; the category
  balance is weighted toward agreement/morphosyntax. It cannot ground cross-lingual or
  non-grammatical-meaning claims.

## Where it lives — download and in-repo handling

- **Source (live):** repo `https://github.com/alexwarstadt/blimp`; per-paradigm data at
  `https://raw.githubusercontent.com/alexwarstadt/blimp/master/data/<paradigm>.jsonl`
  (67 files). HuggingFace mirror: `huggingface.co/datasets/nyu-mll/blimp` (license
  `cc-by-4.0`). Paper: arXiv `1912.00582`; TACL `aclanthology.org/2020.tacl-1.25/`.
- **Fetched + verified this session:** `determiner_noun_agreement_1.jsonl` —
  full file 468,642 bytes, 1,000 lines, sha256
  `f48065fd760d0fd1a895012860d38bdf3c2ac115cd221e521684cc430c0f1855`. Its field schema was
  parsed and confirmed firsthand.
- **In-repo handling (recipe-not-corpus for the pair data; full summary for the human anchor):**
  the **minimal-pair data** keeps its recipe-not-corpus posture — only a **10-line sample** is
  committed (`experiments/data/blimp/determiner_noun_agreement_1.sample.jsonl`, 4,702 bytes, sha256
  `0a05d83fae0e255f0faf3bd7907596079bf82463f283b98403c2d549c114b6e8`; the full 67,000-pair dataset is
  **not** committed, CC-BY, trivially re-fetchable from `data/`). The **per-paradigm human-agreement
  summary is committed in full** (it is a small 3 KB summary, not the corpus, and it is the load-bearing
  human anchor): `experiments/data/blimp/human_validation_summary.csv`, **3,057 bytes, 69 rows, sha256
  `ea0e7c21de6b9df2fd8a94d0b175e84ea57627e4cbfa1fcba4ef8b3d0fba1b2d`** (fetched + committed 2026-07-10,
  s204; CC-BY, attribution to Warstadt et al. 2020).

## Known limits / scope

- **License: CC-BY (README prose + HuggingFace `cc-by-4.0`); no standalone LICENSE file in
  the GitHub tree.** Attribution-only — redistribution permitted with credit. Handled here
  under the recipe-not-corpus posture (sample only committed).
- **Acceptability only.** Grounds a grammatical forced-choice signal; does **not** ground
  entailment, implicature, or sense claims.
- **Synthetic, widely-trained-on.** Contamination + naturalness caveats apply to any
  anchoring use.
- **Per-category paradigm counts not independently re-derived this session** — the
  12-category *names* are verified and corroborated by filenames; exact counts per category
  should be re-confirmed from the paper before being cited as numbers.

## Verified / Unverified / Open breakdown

| Item | Status | Source |
|------|--------|--------|
| Title, full author list (Warstadt, Parrish, Liu, Mohananey, Peng, Wang, Bowman) | **VERIFIED** | arXiv 1912.00582 abstract page + ACL Anthology 2020.tacl-1.25 |
| Venue: TACL vol. 8 (2020) | **VERIFIED** | ACL Anthology 2020.tacl-1.25 |
| 67 paradigms × 1,000 pairs = 67,000 minimal pairs | **VERIFIED** | TACL abstract + repo `data/` (67 `.jsonl` files) + HF nyu-mll/blimp |
| Each pair = acceptable vs unacceptable sentence; template-generated | **VERIFIED** | Abstract + fetched file inspection |
| JSON field schema (sentence_good/bad, field, linguistics_term, UID, pairID, method flags) | **VERIFIED (firsthand)** | Parsed `determiner_noun_agreement_1.jsonl` this session |
| Human aggregate agreement = 96.4% (forced choice of acceptable member) | **VERIFIED** | TACL abstract |
| Per-paradigm human agreement (`total_mean`, range 0.47–0.99, 69 rows) | **VERIFIED (firsthand; committed)** | `human_validation_summary.csv` fetched + committed s204, sha256 `ea0e7c21…` |
| 12 phenomenon categories exist; category names | **VERIFIED (names corroborated by filenames)** | README "12 possible values"; 67 filenames map onto the 12 |
| Per-category paradigm counts; 67-vs-69 summary-row discrepancy | **NOT RE-DERIVED / NOT RECONCILED** | Paper states 67; the committed summary CSV has 69 `Condition` rows — flagged, not reconciled |
| License: CC-BY / cc-by-4.0 | **VERIFIED** | Repo README prose + HF nyu-mll/blimp license field |
| Standalone LICENSE file in repo tree | **NOT PRESENT** | README-prose assertion only (GitHub tree shows no LICENSE file) |
| "89% human baseline" (Mahowald 2024) vs 96.4% (BLiMP paper) | **BOTH VERIFIED, DISTINCT** | mahowald-2024-dissociating quote vs BLiMP abstract — different measurements |

## Pointer for next visit

1. **Use as the optional Posture-2 acceptability backing only.** Per
   [`decisions/resolved/function-word-anchor-design`](../../decisions/resolved/function-word-anchor-design.md),
   BLiMP backs the *acceptability* reading of function-word-swap disruption (determiner,
   quantifier, NPI, subject-verb agreement categories) — it is an **upgrade that never
   blocks** the within-model `internal-contrast-only` run.
2. **Do not use it for the entailment-flip indicator.** The Q2(i) entailment-flip test
   wants human *entailment* labels — fetch an NLI set for that; BLiMP is acceptability only.
3. **Flag contamination on any anchoring use.** Synthetic + widely-trained-on; the
   decision's preference for *synthetic-built* over *BLiMP-lifted* minimal pairs stands.
4. **Re-derive per-category counts before quoting them as numbers.** Pull the paper's
   table (or count UIDs over all 67 files) rather than asserting counts from memory.
