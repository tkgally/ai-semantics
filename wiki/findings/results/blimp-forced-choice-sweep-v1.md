---
type: result
id: blimp-forced-choice-sweep-v1
title: "BLiMP forced-choice sweep — the panel's grammatical difficulty profile TRACKS the human one (PROFILE-ALIGNED 3/3, descriptive) and error concentrates on the structurally-deep paradigms (DEPTH-GRADED 3/3, within-panel), by roughly the human margin (TRACKS-DIP): a broad grammar-side shadow-depth gradient, human-anchored"
meaning-senses:
  - constructional
  - human-comparison
  - measurement-epistemic
status: proposed
anchor: resource/blimp
contingent-on: []
created: 2026-07-10
updated: 2026-07-10
links:
  - rel: operationalizes
    target: design/blimp-forced-choice-sweep-v1
  - rel: operationalizes
    target: essay/shadow-depth-cross-cuts-grain
  - rel: anchors
    target: resource/blimp
  - rel: depends-on
    target: source/mahowald-2024-dissociating
  - rel: supports
    target: claim/formal-competence-aann-ceiling
  - rel: depends-on
    target: theory/lexicon-grammar-continuum-v2
---

# Result — BLiMP forced-choice sweep (program A3b)

> **Status: proposed · `anchor: resource/blimp` (HUMAN-COMPARISON, not internal-contrast-only) · 40-paradigm
> observed on-axis set · n = 3 models, orderings not coefficients · behavioral 2AFC, not logprob.**
> Ratified + frozen + run + verifier-checked this session (s205; design
> [`design/blimp-forced-choice-sweep-v1`](../../../experiments/designs/blimp-forced-choice-sweep-v1.md),
> gates [`decisions/resolved/blimp-forced-choice-sweep-design`](../../decisions/resolved/blimp-forced-choice-sweep-design.md)
> Q1-B/Q2-A/Q3-A + C8). PREREG + reviews:
> [`experiments/runs/2026-07-10-blimp-forced-choice-sweep/`](../../../experiments/runs/2026-07-10-blimp-forced-choice-sweep/).
>
> **Two headline readings, one caveated:**
> - **R2 (VERDICT-BEARING, strictly within-panel): DEPTH-GRADED 3/3.** Forced-choice error concentrates
>   on the structurally-deep paradigms (islands, scope/NPI, long-distance filler-gap; accuracy ≈0.81–0.92)
>   relative to shallow-local agreement (adjacent determiner–noun / regular subject–verb; ≈0.98–0.99).
>   Shallow-minus-deep accuracy gap **+0.111 / +0.168 / +0.070** (claude / gpt / gemini), all ≥ the
>   pre-registered +0.05 margin. A broad **grammar-side shadow-depth gradient** at the construction grain.
> - **R1 (human-anchored, DESCRIPTIVE/DIRECTIONAL ONLY — non-promotable this run per C8): PROFILE-ALIGNED
>   3/3.** Per-model Spearman of per-paradigm forced-choice accuracy against BLiMP's per-paradigm human
>   agreement is clearly positive on all three: ρ_prof **+0.606 [+0.357,+0.795] / +0.543 [+0.260,+0.736] /
>   +0.628 [+0.368,+0.799]** (all CIs exclude 0; n=40 ⇒ p<0.05 at |ρ|≈0.31). The panel is hard **where
>   people are hard** — the models' grammatical difficulty structure lines up with the human one.
> - **R2h (human-anchored sub-reading): TRACKS-DIP 2/3.** The panel's shallow-minus-deep accuracy gap is
>   *comparable to* the human shallow-minus-deep agreement gap (+0.065), not disproportionately larger:
>   (panel − human) = +0.046 / **+0.103** / +0.005 — only gpt EXCEEDS (+0.103 > +0.05); claude and gemini
>   TRACK. So the panel finds deep contrasts harder by **roughly the margin humans do**, not beyond it.
>
> **No contamination-saturation (F3), no instrument-failure.** Absolute accuracy 0.915 / 0.870 / 0.942 is
> a **contamination upper bound** (BLiMP is synthetic, 2019, widely trained on) and is **never** the
> headline; the load-bearing readings are the *relative* profile (R1) and *within-panel* gradient (R2),
> both robust to a roughly-uniform memorization boost.

## What was run

A behavioral 2-alternative forced-choice sweep of **40 BLiMP paradigms** — every paradigm in the on-axis
`linguistics_term` categories (determiner–noun agreement; the local + `distractor_` split of subject–verb
agreement; NPI licensing; quantifiers; island effects; filler-gap dependency), selected on **structural
criteria only, human-agreement-blind** (F6; the freeze critic verified `paradigm_meta.json` carries no
human values and `prep.py` never reads `total_mean` to select). 30 fresh seeded minimal pairs/paradigm,
**both presentation orders** per pair (position-bias netted, Q2-A), temperature 0, zero-shot. Prompt:
*"Which of these two sentences is the more grammatically acceptable sentence of standard written English?
… Answer with ONLY the single digit 1 or 2."* A pick is correct iff the model selects `sentence_good`.
**7,200 calls, 0 unparsed**, $1.3349 billed. Panel = [`config/models.md`](../../../config/models.md)
`panel.A/.B/.C`.

**Anchor.** BLiMP's per-paradigm human agreement (`total_mean`), committed + sha256-pinned
(`experiments/data/blimp/human_validation_summary.csv`, `ea0e7c21…`), catalogued in
[`resource/blimp`](../../base/resources/blimp.md): *"human aggregate agreement with the labels is 96.4%"*
(TACL abstract), with the per-paradigm profile ranging **0.47–0.99**. This is a genuine human difficulty
profile — the reason R1 is a **human-comparison** line, not a within-model contrast.

## The numbers (per model, order-averaged accuracy)

| | claude-sonnet-4.6 (A) | gpt-5.4-mini (B) | gemini-3.5-flash (C) | human |
|---|---|---|---|---|
| absolute acc (SD, range) — **upper bound** | 0.915 (0.12, .57–1.0) | 0.870 (0.15, .53–1.0) | 0.942 (0.11, .47–1.0) | 0.964 agg |
| **ρ_prof (vs human agreement)** | **+0.606** [.357,.795] | **+0.543** [.260,.736] | **+0.628** [.368,.799] | — |
| shallow-local acc | 0.987 | 0.981 | 0.989 | 0.930 |
| medium (distractor) acc | 0.975 | 0.967 | 0.950 | 0.833 |
| deep (scope+island) acc | 0.877 | 0.812 | 0.919 | 0.866 |
| **depth-gap (shallow−deep)** | **+0.111** | **+0.168** | **+0.070** | +0.065 |
| consistency acc (both orders) | 0.847 | 0.789 | 0.914 | — |
| position-lock / ans1-rate | 0.14 / 0.44 | 0.16 / 0.48 | 0.06 / 0.49 | — |

**Per-category accuracy (freeze-vote condition — is one category carrying R2?).** No: the deep dip appears
across islands, quantifiers, and filler-gap for the weaker models, not a single category. claude:
det–noun 1.00, subj–verb 0.97, NPI 0.92, filler-gap 0.93, quantifiers 0.85, **islands 0.81**. gpt:
det–noun 0.98, subj–verb 0.97, NPI 0.94, filler-gap 0.78, **quantifiers 0.74, islands 0.76**. gemini:
uniformly 0.91–0.99 (the smallest gradient). NPI licensing stays high for all three — its cue is more
locally detectable than islands/quantifier-scope.

## Reading the result

1. **A grammar-side shadow-depth gradient exists, within the panel (R2).** The construction grain shows
   the same internal split the lexical pole shows: structurally-deep contrasts (island constraints,
   quantifier/NPI scope, long-distance filler-gap — dependencies the local co-occurrence window
   under-determines) are harder than adjacent agreement (n-gram/local-window detectable). This is the
   direct grammar-side realization of the depth axis in
   [`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md) —
   measured, not asserted, across 40 paradigms.
2. **But that gradient TRACKS the human one (R1 + R2h), it is not a model-specific pathology.** Humans
   *also* find the deep contrasts harder (human depth-gap +0.065), and the panel's per-paradigm difficulty
   profile aligns with the human profile (ρ_prof +0.54–0.63, 3/3). The panel's excess difficulty on deep
   contrasts is **comparable to** the human dip (TRACKS-DIP 2/3), not disproportionately larger (gpt the
   lone EXCEEDS). So the honest reading is *shared* difficulty structure — the models are hard roughly
   where, and roughly as much as, people are hard — **not** "the panel fails structurally-deep grammar in
   a way humans don't."
3. **Why R1 is descriptive-only this run (C8).** A positive ρ_prof could in principle be inflated by a
   training-frequency artifact rather than shared grammatical-difficulty structure: frequent
   local-agreement constructions are plausibly *both* human-easy *and* the most memorized; rare
   island/scope contrasts *both* human-harder *and* less memorized. The F3 saturation guard rules out the
   ceiling case (no model is F3-saturated: SD 0.12/0.15/0.11), but it does **not** rule out a
   moderate-variance frequency-driven ordering. Per the s205 ratification's binding **C8**, R1 is
   therefore reported **descriptively / directionally** and is **non-promotable to a `claim` on this run
   alone**; promotion waits on a later session that adds the pre-registered training-frequency control
   (an F7 content-word-swap arm, or a corpus-frequency covariate partialled from ρ_prof). The same power
   status is fixed symmetrically at freeze — a PROFILE-DIVERGES null would have been reported the same
   descriptive way.

## Scope caps (LOAD-BEARING — read before citing)

- **Absolute accuracy is a contamination upper bound**, never a headline (0.87–0.94, all near ceiling —
  BLiMP is synthetic, 2019, widely trained on). The load-bearing readings are the *relative* profile (R1)
  and the *within-panel* gradient (R2).
- **Acceptability, not inference.** BLiMP contrasts grammatical well-formedness only; nothing here bears
  on truth-conditional / entailment / implicature relations ([`resource/blimp`](../../base/resources/blimp.md)).
- **Behavioral 2AFC, not BLiMP's original logprob scoring** — a different measurement; panel accuracy is
  not comparable to the paper's published LM logprob accuracies. Position bias controlled (both orders;
  position-lock 0.06–0.16, ans1-rate 0.44–0.49 — no bias; consistency 0.79–0.91).
- **40-paradigm selected observed set, not full 67**; verdicts scope to **this frozen panel**, not a
  universal depth law (freeze-vote condition). Two low-agreement paradigms (0.514, 0.47) had no data file
  on master (404) and were excluded for data-availability, mildly conservative for R1.
- **n = 3 models; orderings, not pooled coefficients.** ρ_prof reported per model with its CI.

## What this feeds

- **[`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md):** a
  broad, human-anchored grammar-side depth gradient (R2 DEPTH-GRADED 3/3) corroborating "the grammatical
  pole is *also* internally graded by shadow-depth" — now with a 40-paradigm measurement, not only the CC
  beater + presupposition corner. No revision trigger fires *against*; the placement is supported and
  sharpened (the gradient tracks the human profile — a shared axis, not a model deficit).
- **[`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md):**
  broadens the formal-competence evidence from one construction (AANN) to a depth-stratified sweep, with a
  per-paradigm human anchor the AANN line lacked at this granularity (`supports`).
- **Promotion (deferred, C8):** if a later session adds the training-frequency control and R1 replicates,
  the PROFILE-ALIGNED human-comparison line is a promotion-review candidate — the program's first broad
  human-anchored grammatical-competence claim. Not promotable on this run.
- **[`predictions.md`](../../predictions.md):** the s205 freeze bet — R2 DEPTH-GRADED **fires-for**; the
  R2h EXCEEDS-HUMAN-DIP leg does **not** obtain (TRACKS-DIP, not EXCEEDS) — recorded there.

## Verification

Independent post-run verifier (fresh agent) recomputed every headline figure from the 7,200 raw records
without importing the scorer — see
[`REVIEW-verify-s205.md`](../../../experiments/runs/2026-07-10-blimp-forced-choice-sweep/REVIEW-verify-s205.md).
Pre-run: fresh-agent critic GO + non-Anthropic vote GO-WITH-CONDITIONS
([`REVIEW-freeze-s205.md`](../../../experiments/runs/2026-07-10-blimp-forced-choice-sweep/REVIEW-freeze-s205.md));
gates ratified s205 ([`REVIEW-ratify-s205.md`](../../../experiments/runs/2026-07-10-blimp-forced-choice-sweep/REVIEW-ratify-s205.md)).
