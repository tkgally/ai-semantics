---
type: claim
id: aann-behavioral-gradient
title: The AANN acceptability gradient is a powered, frequency- and noun-class-guarded behavioral positive, cross-date replicated on fresh disjoint items (graded gradient, rep2) — all three panel models' prompted AANN acceptability rank-tracks the human Exp-2 MTurk gradient (cell-level ρ 0.68–0.75, CIs exclude 0), survives a Zipf word-frequency partial (the distributional shadow-beater) and a noun-class marginal guard, and generalizes to frequency-matched held-out adjectives at the overall grain (0.75–0.83) — but that held-out productivity is noun-class-dependent and FAILS in the temporal stratum (v2b, uniformly negative), and one model's coarse Tier-0 form-preference can wobble at the margin (rep2). Tier-2 gradient tracking, NOT the Tier-0 form ceiling and NOT the Tier-4 inferential line
meaning-senses:
  - constructional
  - distributional
  - functional-vs-formal
  - human-comparison
status: supported
anchor: resource/mahowald-2023-aann-stimuli
contingent-on: []
created: 2026-07-04
updated: 2026-07-05
links:
  - rel: anchors
    target: resource/mahowald-2023-aann-stimuli
  - rel: depends-on
    target: result/aann-behavioral-gradient-v2
  - rel: depends-on
    target: result/aann-behavioral-gradient-rep2
  - rel: depends-on
    target: result/aann-temporal-heldout-v2b
  - rel: supports
    target: conjecture/aann-construction
  - rel: supports
    target: theory/shadow-depth-table-v1
  - rel: refines
    target: claim/formal-competence-aann-ceiling
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: concept/constructional-meaning
---

# Claim: the AANN acceptability gradient tracks the human MTurk gradient net of a frequency shadow, and generalizes to held-out adjectives — noun-class-dependently

> **Status: supported (2026-07-04, session 176).** Cross-session, independent, adversarial
> claims-promotion review ([`PROTOCOL.md §3`](../../../PROTOCOL.md); program item B1) of the AANN
> behavioral-gradient line — [`result/aann-behavioral-gradient-v2`](../results/aann-behavioral-gradient-v2.md)
> (session's single pre-registered run, verdict SUPPORTED, independent post-run verifier **0
> mismatches**) with its named follow-up [`result/aann-temporal-heldout-v2b`](../results/aann-temporal-heldout-v2b.md)
> (a second date that powers-up and confirms the temporal hole). The reviewer did not produce
> either result. Promotion **fixes the yardstick, never the result** (see *Anti-cheat*).
>
> *(Decorrelation note, [`PROTOCOL.md §3`](../../../PROTOCOL.md)/§2: the owed non-Anthropic panel vote
> was routed via the probe REST path — `openai/gpt-5.4-mini`, cutoff-aware preamble — and returned
> **PROMOTE-SCOPED**, converging with this fresh-agent verdict on the same single-run, frequency-guarded,
> temporal-stratum-qualified scope.)*
>
> **Update (2026-07-04, session 178) — the single-run lead caveat is DISCHARGED for the graded
> gradient (cross-date, fresh items).** The owed A2a second-date powered re-run landed:
> [`result/aann-behavioral-gradient-rep2`](../results/aann-behavioral-gradient-rep2.md) — the
> **byte-identical frozen v2 instrument** on **408 fresh anchored items drawn disjoint from v2 (0
> shared)**, against the **byte-identical human anchor**, 1,782 calls, $0.3092, 0 missing; fresh-agent
> pre-run critic GO + non-Anthropic vote GO-WITH-CONDITIONS + fresh-agent post-run verifier
> **REPRODUCED (0 discrepancies)**. **The frequency- and noun-class-guarded anchored gradient
> replicates for all three models** — cell ρ **0.692 [0.603,0.762] / 0.702 [0.617,0.770] / 0.735
> [0.658,0.795]**, every CI overlapping v2's, partial-ρ\|Zipf 0.687/0.690/0.722 — so the claim's
> core (graded gradient net of frequency) now stands on **two dates and disjoint items, 3/3**, not one
> run. The conjecture-level **SUPPORTED verdict also replicates**, but **via A+C**: on this occasion
> **gpt-5.4-mini's Tier-0 manipulation check dropped to 18/24** (genuine, clean single-letter misses,
> all on the marginal *objects + negative-evaluative* items — "gruesome three paintings", "ugly three
> desks"), so B is **Tier-0-excluded from the support count even though its graded gradient is
> undiminished** (0.702, CI overlaps v2). This *sharpens* the scope, it does not weaken it: the
> **graded gradient-tracking** statement (what `supported` attaches to) is robust across dates and
> items for all three; the coarse **binary form-ceiling** can wobble at the margin for one model. The
> held-out overall positive also re-passed 3/3 (same frozen items, second date) and the temporal hole
> reproduced for A and C. See *Bounds* (first bullet, amended).
>
> **This promotion is deliberately SCOPED.** Unlike its two sibling claims —
> [`claim/comparative-correlative-covariation`](comparative-correlative-covariation.md) (three runs + a powered re-run) and
> [`claim/dative-information-structure-givenness`](dative-information-structure-givenness.md) (three
> runs) — the positive AANN gradient rests on a **single measurement occasion**. What earns the
> promotion at that single occasion, and what bounds it, is stated explicitly in *Grounds*,
> *Held-out generalization*, and *Bounds*: the run is already at **powered N** (204 human cells over
> 3,600 ratings; 408 anchored model items), it carries the **shadow-beater controls** the flagship
> table requires (frequency partial + noun-class guard), and its **within-run held-out arm** is a
> genuine fresh-items replication of the class gradient — but that within-run replication is
> **partial** (the temporal noun class fails), and there is **no second-date replication of the
> overall positive**. The claim is scoped to exactly that. *(This last bound was the promotion-time
> state; it is **discharged for the graded gradient** by the 2026-07-04 update box above —
> [`result/aann-behavioral-gradient-rep2`](../results/aann-behavioral-gradient-rep2.md) supplies the
> second-date fresh-item replication, 3/3 with overlapping CIs.)*

## Statement

On the ratified 3-family panel (`claude-sonnet-4.6`, `gpt-5.4-mini`, `gemini-3.5-flash`), each
model's **prompted graded acceptability (0–100, temperature 0) for AANN sentences rank-tracks the
human MTurk acceptability gradient** over the Mahowald Experiment-2 adjective-class × noun-class
space, at **cell grain**: Spearman ρ **0.7017 / 0.6843 / 0.7505** across the 204 (adjective × noun-class)
cells, each with a bootstrap 95% CI (**0.61–0.77 / 0.60–0.75 / 0.68–0.81**) that excludes 0. The
tracking is **not a distributional-frequency shadow**: it survives partialling out the adjective's
Zipf word-frequency (partial ρ **0.6919 / 0.6607 / 0.7363**) and a noun-class marginal guard
(within-noun-class mean ρ **0.630 / 0.659 / 0.654**) that a zero-adjective-information responder
would fail. And the **class gradient generalizes to frequency-matched held-out adjectives the human
raters never saw** — at the overall grain, held-out class-cell ρ **0.8336 / 0.8143 / 0.7525**.

The claim is **scoped and qualified**, never panel-uniform-competence:

- **Held-out productivity is noun-class-dependent, and the temporal stratum FAILS.** The overall
  held-out positive is carried by the object and distance classes; the **temporal noun class is
  uniformly negative** (cell-grain ρ **−0.20 / −0.40 / −0.40**, adjective-grain **−0.139 / −0.028 /
  −0.046** at powered widening — see *Held-out generalization*). Productivity is real at the overall
  grain and **uneven by noun class**; this is a load-bearing qualifier, not a footnote.
  *(Update 2026-07-06, s189: the temporal stratum's negative sign is now understood to be an **inventory
  artifact**, not a quant-class property. A widened K=20 quantity-modifier probe
  ([`result/aann-quant-temporal-inversion-v1`](../results/aann-quant-temporal-inversion-v1.md), VERDICT
  NULL) found the quant×temporal cell rises to 2nd of four classes for all three models once the modifier
  set is widened; only the thin held-out sample's low-frequency large-magnitude items [towering/colossal/
  ample] invert. This does **not** widen the claim's scope — it narrows the temporal caveat to
  "sensitive to a few marginal low-frequency adjectives," not "quantity adjectives invert." The v2b
  held-out temporal negatives above are faithful to that specific sample.)*
- **Single run for the positive gradient.** The anchored gradient and its overall held-out
  replication come from one pre-registered occasion; the only second date in the line
  ([`result/aann-temporal-heldout-v2b`](../results/aann-temporal-heldout-v2b.md)) replicates and
  sharpens the *temporal hole*, not the positive. What substitutes, in part, for a cross-date
  replication is the **within-run held-out arm** (fresh lexical material), which is the
  memorization/productivity defense — but it shares every nuisance factor of its run.
- **Cell-averaging is load-bearing, and pre-declared.** The headline is at cell grain; item-level
  correlations against **single** human ratings are **0.49 / 0.45 / 0.45** — the honest descriptive
  floor. Cell grain was declared primary *before* any model output (single-rater item noise
  attenuates item-level ρ), which is legitimate, but the item-level floor is stated, not buried.

## Grounds

One own-design result, pre-registered and frozen before any finding-bearing call, with an
independent pre-run critic and an independent post-run verifier
([`result/aann-behavioral-gradient-v2`](../results/aann-behavioral-gradient-v2.md); 1,782 calls,
$0.3125 billed, **zero missing responses in every arm**; frozen design
[`design/aann-construction-v2`](../../../experiments/designs/aann-construction-v2.md)). Read the
**rank correlations and their intervals** below; the pre-registered SUPPORTED map required "≥ 2 of 3
Tier-0-passing models achieve the anchored-arm pass, AND each of those models also passes held-out
replication" — **all three** models pass every gate.

| Gate (frozen pre-run) | claude-sonnet-4.6 | gpt-5.4-mini | gemini-3.5-flash |
|---|---:|---:|---:|
| Tier-0 manipulation check (≥ 20/24) | 23/24 | 23/24 | 24/24 |
| Anchored cell-level Spearman, 204 cells (≥ 0.40) | **0.7017** | **0.6843** | **0.7505** |
| bootstrap 95% CI (excludes 0) | 0.61–0.77 | 0.60–0.75 | 0.68–0.81 |
| Zipf frequency guard, partial ρ (≥ 0.20) | 0.6919 | 0.6607 | 0.7363 |
| Noun-class guard, within-class mean ρ (≥ 0.25) | 0.630 | 0.659 | 0.654 |
| Held-out replication vs human class-cells (≥ 0.50) | 0.8336 | 0.8143 | 0.7525 |
| Held-out within-noun-class mean (≥ 0.30) | 0.4585 | 0.4476 | 0.4394 |
| Framing robustness, 0–100 vs 4-point ρ (≥ 0.50) | 0.9288 | 0.8168 | 0.8215 |

Secondary grain (28 adjective-class × noun-class cells, descriptive): ρ = 0.85 / 0.84 / 0.92.
Item-level against single human ratings (descriptive floor; single-rater noise): 0.49 / 0.45 / 0.45.

What the result page states in its own words:

> "All three panel models' prompted graded acceptability (0–100, temperature 0) **rank-tracks the
> human MTurk acceptability gradient** over the Mahowald Exp-2 adjective × noun-class space, and the
> adjective-class gradient **replicates on frequency-matched held-out adjectives the human raters
> never saw**" ([`result/aann-behavioral-gradient-v2`](../results/aann-behavioral-gradient-v2.md)).

And the reading it explicitly licenses — the one this claim promotes — is: *"their graded ratings
reproduce the shape of the human acceptability gradient (which adjective classes license AANN more,
in which noun-class environments), survive a frequency control, survive a noun-class-marginal
control, and generalize the class gradient to novel adjectives … That is behavior consistent with a
productive form–meaning pairing, not a memorized template inventory."*

## Human-comparison leg (the anchored-half cell gradient — magnitude of alignment, not of an effect)

The human anchor is the Mahowald 2023 Experiment-2 MTurk rating corpus
([`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md);
ratified [`decisions/resolved/aann-behavioral-operationalization`](../../decisions/resolved/aann-behavioral-operationalization.md)),
which the resource page documents at the cell it grounds:

> "`mturk_data/adjexp_turk.csv` (7,200 rating rows, 3,600 non-filler over item ids of the form
> `{adjective}-{numeral}-{noun}-sent-{nounclass}-{template}` — the Experiment 2 adjective×noun
> gradient) … Ratings are on the 1–10 acceptability scale in the `answer` column."

The resource page states exactly what this can ground — a **gradient** comparison, not a
representation or an expert-panel comparison:

> "Claims about whether a model's acceptability *gradient* tracks the proposed semantic/syntactic
> constraints on AANN: adjective-type sensitivity … noun-type sensitivity (measure / temporal nouns
> most acceptable) …"

The 3,600 non-filler single-rating items are aggregated (per the frozen design, Condition 1) into
"`human_cell_means.csv` (204 adjective × noun-class cells, n = 6–28 ratings each, median 18)" — the
human side of the cell-level ρ. So the human-comparison statement is exactly: **on a single run, each
model's per-cell acceptability ordering aligns with the human per-cell MTurk ordering at ρ ≈ 0.68–0.75,
net of word-frequency.** This is alignment with a human *gradient*, at cell grain — it is **not** a
per-item human comparison (item-level ρ is 0.45–0.49) and **not** a human effect-*size* comparison.

**The held-out arm carries no independent human claim.** Its evidential type, declared pre-run, is
*gradient replication*: the model's held-out class ordering is scored against the human
**anchored-half** ordering, because — as the resource page states — "held-out generalization requires
extending the templates," so those adjectives **have no human ratings by construction**. The
held-out arm therefore anchors to the resource **only via the anchored-half gradient it must
reproduce**, and makes no measurement of new human behavior.

## The control that earns the rigor (the distributional shadow-beater)

The claim's "tracks the gradient, not the frequency shadow" force rests on the controls, not on the
raw ρ. This is what makes the AANN row a **beater** in the flagship
[`theory/shadow-depth-table-v1`](../theory/shadow-depth-table-v1.md) (form ii, partialled
correlation): a model–human gradient correlation that **survives partialling out a distributional
covariate**.

- **Zipf word-frequency partial.** Partialling the adjective's Zipf frequency out of both the model
  and human cell means leaves the alignment essentially intact (raw ρ 0.702 / 0.684 / 0.751 → partial
  ρ 0.692 / 0.661 / 0.736). The rank information about the human gradient the model carries is
  therefore *over and above* what unigram frequency supplies. This is the ladder's discipline made
  concrete: per [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)
  *(superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md)
  — cited here as the edition this page engaged.)*,
  "A Tier-2 evaluative-adjective effect is only evidence for meaning *if* unigram frequency is
  controlled; otherwise it collapses back to Tier 1." Here it does not collapse.
- **Noun-class marginal guard.** The pre-run critic added this gate precisely because "a degenerate
  responder emitting only the human noun-class marginal (zero adjective information) scores ρ = 0.466
  on the 204 cells — above the 0.40 threshold." Requiring within-noun-class mean ρ ≥ 0.25 (met at
  0.630 / 0.659 / 0.654) forces the alignment to carry **adjective-level** rank information, not just
  the coarse noun-class ordering. A degenerate-responder pass is thereby excluded by construction.

Together these two controls are why the alignment is read as **gradient tracking of the AANN
form–meaning pairing** (unification/evaluation graded by adjective class in a noun-class environment),
not as a distributional or noun-class-marginal artifact.

## Held-out generalization — real at the overall grain, absent in the temporal stratum

The held-out arm (60 items over 24 frequency-matched held-out adjectives, none in Mahowald's 50,
each class median Zipf within ±0.5 of the Mahowald class median) is the **memorization defense** the
conjecture names as central. At the overall grain it passes cleanly (class-cell ρ 0.8336 / 0.8143 /
0.7525, above the 0.50 gate) — the gradient generalizes to lexical material the human raters never
saw.

**But held-out productivity is noun-class-dependent, and the temporal noun class fails.** The result
page's own caveat 2 flags "the **temporal stratum is ≈ −0.2 for all three models**." The named
follow-up widened that stratum 5× (16 → 80 items) under the identical ratified instrument
([`result/aann-temporal-heldout-v2b`](../results/aann-temporal-heldout-v2b.md), a **second date**,
independent pre-run critic + independent post-run verifier, 0 mismatches) and confirmed it was real:

> "the temporal stratum is uniformly NEGATIVE at every grain for all three models … held-out AANN
> productivity is **noun-class-dependent**, and the temporal class is where it fails."

Widened cell-grain ρ **−0.20 / −0.40 / −0.40**; adjective-grain ρ **−0.139 / −0.028 / −0.046** (all
≤ 0; the new-only, non-carryover subgroup also negative for all three). The v2b page is explicit that
this **does not overturn** the v2 overall SUPPORTED verdict — "It **sharpens caveat 2 into a
finding**: AANN held-out productivity … is **noun-class-dependent**, strong for the object/distance
classes that carried v2's positive and absent for the temporal class." This claim therefore states
generalization **and** its limit in the same breath: the gradient generalizes to held-out adjectives
in the object/distance environments and **not** in the temporal one.

## Relation to the Tier-0 form-ceiling claim (distinct diagnostic, no overlap)

This claim is the **separate meaning-diagnostic** that the Tier-0 form-acceptability claim
([`claim/formal-competence-aann-ceiling`](formal-competence-aann-ceiling.md)) explicitly declined to
make and named as owing separate treatment. The Tier-0 claim covers the licit-vs-degenerate **form**
contrast (a beautiful three days vs its four degenerate variants) and says:

> "It does not cover the adjective-type gradient or noun-type sensitivity measures, which are mixed
> formal/semantic probes and require separate treatment … [the graded probe] must be identified as
> the separate meaning-diagnostic that it is."

In this run, the Tier-0 form contrast is the **manipulation check** (23/24, 23/24, 24/24) — a
precondition, not the finding. The finding is the **graded** adjective-class × noun-class gradient
*above* that form ceiling. So the two claims are disjoint: the Tier-0 claim asserts formal competence
(the model knows which strings are well-formed); this claim asserts **graded gradient-tracking** (the
model's acceptability behavior reproduces the human ordering of *how* acceptable, by adjective class
and noun environment, net of frequency). This claim `refines` the Tier-0 claim by supplying the
diagnostic its carve-out named; it does **not** restate or overlap the form-ceiling result.

## Where it sits on the evidence ladder

On the ladder in [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)
this is a **Tier-2 (gradient semantic tracking) positive, frequency- and noun-class-guarded, with a
Tier-3 (held-out generalization) control passed at the overall grain but noun-class-dependent** — the
theory page places it in exactly those terms ("cell-level ρ 0.68–0.75, frequency- and noun-class-guarded
— Tier 2 … replicate the class gradient on a locked, frequency-matched held-out adjective list
(0.75–0.83 — Tier 3, with the honest caveat that replication is uneven by noun class: the temporal
stratum comes out negative)"). It sits **above** Tier 0 (the form ceiling, the separate claim) and
**below** Tier 4 (inference-licensing). It is human-anchored, and it is the AANN line's Tier-2/Tier-3
positive — patterning with the project's recurring observation that current decoders track a
well-described soft constraint in the human direction cleanly.

It does **not** reach **Tier 4 (inference-licensing)**, and this claim makes no Tier-4 statement. The
separate AANN inferential line ([`result/aann-inferential-v3`](../results/aann-inferential-v3.md)
through v6) is a **PARTIAL** — a construction effect fully convergent in only one of three models
(gpt-5.4-mini), paraphrase-level in the other two — and is explicitly out of scope here. The
`inferential` sense-tag is **not** claimed; the `functional-vs-formal` tag marks that this is the
graded *semantic* sensitivity beyond the formal ceiling, not that the construction licenses an
inference.

## What this claim does NOT say

- **No representation claim.** Behavioral acceptability only. As the resource page states, Mahowald
  "uses behavioral acceptability only"; the result's bounds add that "a high gradient correlation
  shows the models' acceptability behavior *tracks* the human gradient; it does **not** show the
  construction's meaning is *represented*." Silent on internal structure.
- **No inference-licensing claim (Tier 4).** Whether the model *draws* the unified-stretch/evaluative
  inference is a different indicator, tested separately and returning **PARTIAL** (one of three
  models convergent). Nothing here bears on it.
- **No panel-uniform human-level-competence claim.** Three decoders converging on a single run is
  weak evidence on its own; the human MTurk gradient is what gives the run independent bearing, and
  it is a crowdsourced, not expert, anchor (below). "Rank-tracks the human gradient net of frequency"
  is **not** "understands the AANN construction like humans."
- **No claim of uniform held-out productivity.** Generalization is **noun-class-dependent**; the
  temporal stratum is uniformly negative (v2b). The over-read "the gradient generalizes to novel
  adjectives" (full stop) is exactly what the temporal failure refuses.
- **No item-level parity claim.** The headline is cell-grain; item-level ρ against single ratings is
  0.45–0.49, stated as the descriptive floor.
- **No cross-construction or beyond-English generality.** AANN-scoped, per the resource's limits
  ("Claims about constructional meaning beyond English AANN" are outside what it can ground) and the
  ratified construction scope.

## Bounds

- **The graded gradient now replicates cross-date on fresh items (2026-07-04, amended — was "single
  run for the positive gradient").** The anchored gradient was originally supported on one
  pre-registered occasion (2026-06-12, v2). The owed second-date powered re-run
  ([`result/aann-behavioral-gradient-rep2`](../results/aann-behavioral-gradient-rep2.md), 2026-07-04)
  **replicates it on 408 fresh items drawn disjoint from v2 (0 shared), against the same human anchor,
  3/3 with overlapping CIs** — so the graded-gradient statement no longer rests on a single occasion.
  The one dimension the replication did **not** fully reproduce is the **binary Tier-0 form-ceiling**
  for one model: gpt-5.4-mini fell to 18/24 on the marginal objects/evaluative items this occasion,
  Tier-0-excluding it from the *conjecture-level* verdict (which is SUPPORTED via A+C) while leaving
  its *graded gradient* intact. Read the discharge precisely: it is the **gradient** (the claim's
  target) that is now two-date-and-fresh-item replicated; the coarse form-preference can wobble at the
  margin. The temporal held-out hole ([`result/aann-temporal-heldout-v2b`](../results/aann-temporal-heldout-v2b.md))
  is unchanged; the within-run held-out arm remains the productivity defense as before.
- **Powered N is already in hand (unlike the founding-N sibling promotions).** The human side is 204
  cells over 3,600 ratings (n = 6–28 per cell, median 18); the model side is 408 anchored + 60
  held-out items. So this claim states a **magnitude with intervals now**, not a threshold-pass
  deferred to a later powered run — the dimension it lacks is cross-date replication, not power.
- **Held-out productivity is noun-class-dependent; the temporal stratum is negative.** Load-bearing,
  from v2b (powered, second date). Read "generalizes to held-out adjectives" **only** as
  "object/distance yes, temporal no."
- **Cell-averaging is load-bearing.** Item-level ρ is 0.45–0.49; cell grain was pre-declared primary
  because single human ratings are rater-noise-dominated — legitimate, but the item-level floor
  binds the depth of any reading.
- **Crowdsourced, not expert, human anchor.** The resource is MTurk: "US-IP, with exclusion criteria
  … Not a balanced linguistic-expert panel." The anchor's known limits carry onto every human-comparison
  statement here.
- **Behavioral not representational; scale-use calibration differs by model** (rank correlation
  mitigates, does not eliminate); an upstream stimulus typo faithfully reproduced (human raters saw
  the identical string, so the comparison stays apples-to-apples); response quantization is uneven by
  model (ties depress rather than inflate ρ). All disclosed on the result page; none change the
  verdict.
- **Single lab, three specific model versions, cross-model shared priors.** Three decoder LLMs
  converging is weak on its own; the human MTurk gradient supplies the independent bearing.

## Anchor

This claim carries `anchor: resource/mahowald-2023-aann-stimuli` with an `anchors:` link to
[`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md) because it
makes a **human-comparison** statement: each model's per-cell AANN acceptability ordering aligns with
the human Exp-2 MTurk per-cell gradient (204 cells, cell-level ρ 0.68–0.75, net of Zipf frequency).
That link grounds the **anchored-half cell gradient**. The **held-out arm** carries **no independent
human claim** — it is gradient replication against the anchored-half human ordering, on adjectives with
no human ratings by construction. The claim is therefore **human-anchored, not
`internal-contrast-only`**: it leans, in full, on a human gradient comparison, and states that leg at
exactly its (single-run, cell-grain, crowdsourced, frequency-partialled) strength.

## Anti-cheat

Promotion fixes the **yardstick** — the empirical Exp-2 MTurk cell gradient and the pre-registered
gate map (ρ ≥ 0.40, CI excludes 0, frequency partial ≥ 0.20, noun-class guard ≥ 0.25, held-out
≥ 0.50) — never the result. That map was frozen before any model call (verified against git history;
the anti-cheat diff of PREREG / analyze / stimuli / human tables between freeze and analysis was
**empty**), no predicted class ordering was hardcoded in the scoring path (scoring is against empirical
cell means only), and the panel roster was the standing ratified one. The reviewer did not produce the
result. The claim states no more than the single run and its within-run controls license: on one
powered, pre-registered occasion all three models' AANN acceptability rank-tracks the human gradient
net of frequency and net of the noun-class marginal, and the class gradient generalizes to held-out
adjectives at the overall grain — with the temporal stratum a measured, powered exception. The
exciting over-reads — "LLMs represent the AANN construction's meaning," "LLMs generalize AANN
productively" (unqualified), or "LLMs match human AANN competence" — are exactly what the
representation disclaimer, the noun-class-dependent temporal failure, the single-run bound, and the
crowdsourced-anchor limit refuse. Nothing here outruns the two result pages it consolidates.

## Status

`status: supported`, **scoped**. What is supported: on a single pre-registered, powered,
independently-verified run, the panel's prompted AANN acceptability **rank-tracks the human Exp-2
MTurk gradient at cell grain** (ρ 0.7017 / 0.6843 / 0.7505, CIs excluding 0), the tracking **survives
a Zipf frequency partial** (0.6919 / 0.6607 / 0.7363) **and a noun-class marginal guard** (0.630 /
0.659 / 0.654) — the distributional shadow-beater — and the class gradient **generalizes to
frequency-matched held-out adjectives at the overall grain** (0.8336 / 0.8143 / 0.7525). `supported`
attaches to that Tier-2 gradient-tracking statement and its Tier-3 held-out control, **with the
load-bearing qualifiers** that held-out productivity is **noun-class-dependent** (the temporal stratum
is uniformly negative, v2b) and that — post the 2026-07-04 update box — the graded gradient is now
**cross-date replicated on fresh disjoint items** (rep2, 3/3, CIs overlap v2), with the residual
single-occasion note applying to the *overall Tier-0-passing composition* (rep2's conjecture-level
SUPPORTED rests on A+C, gpt Tier-0-excluded that occasion) rather than to the graded gradient itself. It
does **not** attach to a representation claim, a Tier-4 inference-licensing claim, a panel-uniform
human-level-competence reading, or an item-level parity claim — all explicitly disclaimed above. The
two underlying results remain `status: proposed` (this promotion consolidates them). `contingent-on:
[]` — the governing operationalization
([`decisions/resolved/aann-behavioral-operationalization`](../../decisions/resolved/aann-behavioral-operationalization.md))
is ratified.
