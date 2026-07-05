---
type: resource
id: mahowald-2023-aann-stimuli
title: Mahowald 2023 AANN stimulus suite and MTurk acceptability ratings
status: catalogued
url: https://github.com/mahowak/aann-public
license: MIT (LICENSE file verified in the mirrored repo, 2026-06-12; "Copyright (c) 2024 Kyle Mahowald")
paper: https://arxiv.org/abs/2301.12564
venue: EACL 2023
created: 2026-05-28
updated: 2026-07-05
links:
  - rel: anchors
    target: conjecture/aann-construction
  - rel: anchors
    target: claim/formal-competence-aann-ceiling
  - rel: anchors
    target: claim/aann-behavioral-gradient
---

# Mahowald 2023 — AANN stimulus suite and human acceptability ratings

## What it is

The data and code accompanying Mahowald (2023), *A Discerning Several Thousand Judgments: GPT-3 Rates the Article + Adjective + Numeral + Noun Construction* (EACL). The paper templatically constructs AANN sentences (e.g. *a beautiful three days*) along multiple linguistic dimensions, elicits acceptability ratings from both GPT-3 and human MTurk raters, and compares them against constraints proposed in the CxG / formal-semantics literature on AANN.

The release at `github.com/mahowak/aann-public` contains, per the README and the paper:

- `generate_sentence_templates/` — CSV files that combine with `aann_experiments.py` to generate the actual sentence stimuli used in each experiment.
- `aann-sents/` — the generated sentences themselves.
- `mturk_data/` — human MTurk ratings on the 1–10 acceptability scale, across Experiments 1–3.
- `mturk_generation/` — HTML templates and input CSVs to regenerate the MTurk surveys.
- `gpt3_data/` — GPT-3 ratings (text-davinci-002) for the same items.

**Mirrored and inspected 2026-06-12** (upstream commit `c8095a0008cd6538717de5cc937f90ce5944e688`,
2024-06-12; cloned to `experiments/data/aann-public/`, gitignored under the recipe-not-corpus
posture — MIT license permits redistribution, but the 69 MB raw mirror is re-clonable and only
derived tables are committed). Inspection confirmed the structure summarized below, and
specifically the anchor-bearing files: `mturk_data/adjexp_turk.csv` (7,200 rating rows, 3,600
non-filler over item ids of the form `{adjective}-{numeral}-{noun}-sent-{nounclass}-{template}` —
the Experiment 2 adjective×noun gradient), `mturk_data/mainexp_turk.csv` (3,740 rows, 756
non-filler over AANN/default/degenerate-variant conditions — Experiment 1; the 756 counts every
rated item across all conditions, a superset of the 378 critical-sentence ratings the Known
limits section cites), and
`mturk_data/adjorder_turk.csv` (1,320 rows — the order experiment). Ratings are on the 1–10
acceptability scale in the `answer` column; sentences are reconstructible from
`generate_sentence_templates/` (template `first`/`second` strings + slot fillers). Hence
`status: catalogued`. The paper's Table 1 (page 2) gives the superset of slot fillers used to
generate the templates, which is what this page summarizes below.

## Stimulus structure (from Mahowald 2023, Table 1, p. 2)

The stimuli are templatic. A sentence is built from a template, an adjective, a numeral, and a noun, with cross-cutting type constraints (a human-template only takes a human noun, etc.).

- **Templates**: 6 noun-category-keyed template families (temporal, objects, human, art, distance, unitlike), each with three template strings — e.g. temporal: *"The family spent X in London"*, *"The diplomat worked X in Nairobi"*, *"The tourist stayed X in Papua New Guinea"*, where *X* is the AANN phrase.
- **Adjective categories** (≈10 per category): `ambig` (astonishing, incredible, impressive, disappointing, surprising, devastating, pathetic, remarkable, mediocre, unsatisfying); `qualitative` (lovely, beautiful, enchanting, soothing, charming, disgusting, uninviting, haunting, hideous, ugly); `quant` (mere, staggering, whopping, hefty, paltry, meager, extra, measly, substantial, record-setting); `stubborn` (large, big, small, round, tall); `color` (blue, green, red, yellow, orange); `human-adj` (lucky, talented, graceful, fancy, friendly, collegial, hopeful, shy, bold, grinning).
- **Noun categories**: human (soldiers, students, …); objects (desks, marbles, …); art (movies, paintings, …); temporal (days, weeks, months, years, hours); distance (meters, feet, yards, blocks, steps); unit_like (pages, acts, paragraphs, awards, meals).
- **Numerals**: three, five, six, eight, ten, twenty, fifty, 500, 1000, 10000, 21, 51, 512, 1429, 21234 — with *three* and *five* used for the bulk of the human experiments.

## What it can ground

Specifically:

- Claims about whether a model assigns higher acceptability to the AANN construction (*a beautiful three days*) than to its degenerate variants — the four contrasts Mahowald defines: switched numeral/adjective order (*a three beautiful days*), no modifier (*a three days*), singular noun (*a beautiful three day*), no article (*beautiful three days*).
- Claims about whether a model's acceptability *gradient* tracks the proposed semantic/syntactic constraints on AANN: adjective-type sensitivity (quantitative > ambiguous > qualitative > stubborn / color on canonical predictions); noun-type sensitivity (measure / temporal nouns most acceptable); numeral sensitivity.
- Cross-model comparison of behavior on **the same templatic item set**, with human MTurk ratings as the common reference.

What it **cannot** ground:

- Claims about model *representations* of the construction — Mahowald uses behavioral acceptability only.
- Claims about constructional meaning beyond English AANN.
- Claims about productivity on items wholly outside the slot-filler superset — held-out generalization requires extending the templates, which is a downstream design decision (see [`decisions/resolved/aann-operationalization`](../../decisions/resolved/aann-operationalization.md)).

## Known limits

- **Crowdsourced raters**: MTurk, US-IP, with exclusion criteria (rate good fillers ≥ 1 point higher than bad on the 1–10 scale; no duplicate submissions). 126 raters × 3 critical sentences each in Experiment 1 (378 ratings). Not a balanced linguistic-expert panel.
- **Prompted GPT-3 judgments, not surprisal**. Mahowald elicits "good"/"bad" probabilities from `text-davinci-002` via a prompt validated on CoLA. A reimplementation against the current panel either reuses that prompt (apples-to-apples) or switches to surprisal-based contrasts (cleaner but different measure) — the operationalization gate.
- **Coverage of the literature is not exhaustive**: the AANN-licensing literature names additional fine-grained constraints (Solt 2007 on unit-coercion; Dalrymple & King 2019 LFG; Bylinina & Nouwen 2018 on quantitative semantics) that the stimulus set partially probes but does not exhaustively dissociate.

## Features most likely to be cited

The AANN probes have now run (behavioral v2, 2026-06-12; cross-date replication rep2, session 178, 2026-07-04 — the earlier surprisal instrument was retired by the ratified behavioral operationalization), and the citations landed where expected:

- **Exp. 1 contrasts** (AANN vs. default vs. four degenerate variants) — the cleanest baseline.
- **Adjective-type × noun-type interaction** (Mahowald Fig. 3 and Exp. 2) — for the prediction in the conjecture that *evaluative* adjectives behave differently from *neutral measure* adjectives; this Exp-2 cell space is exactly what the ran probes regress against.
- The **human MTurk ratings** as the gradient anchor — consumed by the *behavioral* (prompted 0–100 acceptability) instrument rather than the originally-envisaged surprisal contrast: [`claim/aann-behavioral-gradient`](../../findings/claims/aann-behavioral-gradient.md) (promoted session 176; rep2 discharged its single-run caveat, session 178) records all three panel models rank-tracking the human Exp-2 gradient at cell grain (ρ 0.68–0.75, CIs excluding 0), surviving a Zipf-frequency partial.

## Pointer for next visit

~~Clone, inspect, re-confirm license~~ — **done 2026-06-12** (see the mirror note above): repo
cloned to `experiments/data/aann-public/`, `mturk_data/` and `aann-sents/` inspected and found to
match the summary here, license verified MIT, page promoted `external-only` → `catalogued`. The
instrument that consumes this anchor is governed by
[`decisions/resolved/aann-behavioral-operationalization`](../../decisions/resolved/aann-behavioral-operationalization.md)
(ratified 2026-06-12; the earlier surprisal instrument is retired).
