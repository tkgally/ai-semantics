---
type: result
id: relational-reference-game-v1
title: The relational pilot — a two-AI reference game; convergence WITHOUT trajectory-dependence (a first-class relational null), and convergence WITHOUT human-like compression
meaning-senses:
  - relational
  - distributional
  - model-internal
  - human-comparison
status: proposed
anchor: resource/hawkins-tangrams
contingent-on:
  - relational-pilot-operationalization
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: anchors
    target: resource/hawkins-tangrams
  - rel: depends-on
    target: open-question/relational-meaning-pilot
  - rel: depends-on
    target: concept/relational-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: the relational pilot — convergence without trajectory-dependence (a first-class null)

> **Status: proposed (2026-05-31), contingent on [`decisions/open/relational-pilot-operationalization`](../../decisions/open/relational-pilot-operationalization.md).**
> The project's **first finding on the relational axis** — the bottom rung of the "second ladder"
> ([`concept/relational-meaning`](../../base/concepts/relational-meaning.md)). Builds + runs the
> two-AI iterated dyadic reference-game pilot ratified GO in
> [`decisions/resolved/relational-pilot-go`](../../decisions/resolved/relational-pilot-go.md)
> ("Decision 9"), per [`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md).
> Run record + frozen `PREREG.md` + `sha256` in
> [`experiments/runs/2026-05-31-relational-reference-game-v1/`](../../../experiments/runs/2026-05-31-relational-reference-game-v1/README.md).
> **864 calls, $0.945 billed, 14 NA (all claude truncations).** Independent pre-run critic (forced
> the opaque-nickname + `coined_only` diagnostic + `reversed` control before any finding-bearing
> call) + independent post-run verifier (every figure reproduced from raw).

## Headline

Two LLM agents of the **same family** (homogeneous dyads) play an iterated reference game over
hard-to-name abstract figures, coin a compressed label, and a fresh matcher then interprets that
opaque coined nickname. The load-bearing question is **trajectory-dependence**: does the matcher's
interpretation depend on the *ordered* interaction history, with the *content* of the prior turns
held byte-identical and only their *order* destroyed?

**It does not — a first-class relational NULL, uniform across all three models.** The history's
**content** is load-bearing (giving the matcher the record lifts accuracy well above the nickname
alone), but its **order** is not (chronological ≈ shuffled ≈ reversed). The coined convention is
recovered from the **set** of prior turns, not their **ordered trajectory**. This is the relational
analogue of "a distributional pass is not a constructional pass": coordination and convention-use are
real, but they are explained by the co-occurrence *content* a next-token predictor conditions on,
which **survives order-scrambling** — coordination, not constitution
([`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md) §"deflationary null";
[`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)). Per the charter's
first-class-negatives commitment and the GO decision, this is **written as the result, not retuned
toward a positive**.

A **second, anchored** finding falls out of the same run: the LLM dyads converge on referential
**success** but do **not compress** their referring expressions the way humans do.

## What ran (frozen design; full detail in `PREREG.md`)

- **Agents:** the 3-family panel ([`config/models.md`](../../../config/models.md)) — `claude-sonnet-4.6`,
  `gpt-5.4-mini`, `gemini-3.5-flash` — as **homogeneous dyads** (same model both roles), so any gap
  cannot be an artifact of two different systems. Cross-family is a deferred arm.
- **Referents:** 6 hard-to-name 8×8 grid figures in 3 confusable near-twin pairs, frozen
  deterministically (`figures.json`, sha256 `a2709582…`) and committed before any finding-bearing call.
- **Per model, 2 games:** a live dyad game (K=6 figures × R=5 reps, real hit/miss feedback) →
  entrainment curve + per-figure convention records; then each figure's director gives a **≤3-word
  opaque coined nickname**; then a **fresh matcher** interprets that nickname under four arms that
  hold the record content byte-identical and vary only order: **coined_only** (no history),
  **ordered**, **reversed** (chronology control), **shuffled** (×3 permutations, the deflationary
  control). A **single-agent monologue** baseline (no partner / no feedback) runs the same probe as
  the bar-(b) floor.
- **Measures:** the order-isolating de-confounded form of the design's "live vs shuffled" contrast.
  All agent memory is serialized into prompt text (stateless calls) so the shuffle is **exact**.

## The numbers (reproduced from raw by the post-run verifier)

**Entrainment (live dyad) vs the human Hawkins curve** — anchored to
[`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md) (human: utterance length
**7.73→4.10 words**, accuracy **0.78→0.94** over repetitions):

| model | accuracy rep1→rep5 | mean words rep1→rep5 |
|-------|--------------------|----------------------|
| claude | 0.67 → 1.00 | 9.17 → 9.08 (flat) |
| gpt    | 0.42 → 0.75 | 8.58 → 8.42 (flat) |
| gemini | 0.92 → 1.00 | 10.67 → 10.83 (flat) |

→ all converge on **success**; **none compresses** expression length. Convergence without entrainment.

**Trajectory probe (dyadic; per-coined-term cluster accuracy, n=12 terms/model):**

| model | coined_only | ordered | reversed | shuffled | history_lift (ord−coined) | **ORDER gap (ord−shuf)** | mono order gap |
|-------|-------------|---------|----------|----------|---------------------------|--------------------------|----------------|
| claude | 0.583 | 0.917 | 0.750 | 0.833 | **+0.333** [0.000, 0.667] | **+0.083** [0.000, 0.222] | −0.056 |
| gpt    | 0.333 | 0.750 | 0.667 | 0.694 | **+0.417** [0.083, 0.750] | **+0.056** [−0.194, 0.278] | +0.056 |
| gemini | 0.667 | 0.917 | 0.750 | 0.806 | **+0.250** [0.000, 0.500] | **+0.111** [0.000, 0.278] | +0.028 |

(CIs = clustered bootstrap over coined terms.) **history_lift is clearly positive for all three**
(history content helps — coined_only is well below ordered), so the order test is interpretable, not
a methodological artifact. **The ORDER gap is small and no model's CI excludes 0**; the `reversed`
(coherent reverse-chronological) arm is **no better than — sometimes worse than — random `shuffled`**
(claude reversed 0.750 < shuffled 0.833; gemini 0.750 < 0.806), so even the small positive order-gap
point estimates are not a chronology-specific trajectory effect but order-insensitive noise around a
content-driven baseline. The pre-registered positive bar (order-gap CI>0 **and** chronology-specific
**and** above the monologue floor) is met by **no model**.

## Interpretation — coordination, not constitution

The pilot's own evidential bar ([`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md))
required, for a relational *positive*, that live-dialogue interpretation of a coined term differ
reliably from shuffled-history replay with content held constant. It does not. The convention is
**computed from the content bag and aggregated**, not constituted in the ordered interaction — the
relational deflation the open question names as a first-class negative. The deflationary alternative
there is explicitly a `distributional` story (two next-token predictors converging from overlapping
co-occurrence content, a convergence that survives order-scrambling); this result is that story
holding. The **second ladder's bottom rung is not climbed** by this pilot: it shows what relational
convergence looks like *without* trajectory-dependence.

This is a **null about constitution, not about coordination**. The agents do coordinate (accuracy
rises), do use the coined convention (history content lifts matcher accuracy +0.25 to +0.42), and a
fresh agent does recover the convention from the record — all of which the deflationary distributional
story predicts. Only the order-sensitivity that would separate "constituted between" from "computed
within and aggregated" is absent.

## The anchored secondary finding — convergence without human-like compression

Across all three models the dyads reach near-ceiling referential **accuracy** within a few
repetitions but keep their referring expressions at roughly constant length (~8.5–10.8 words),
whereas the human Hawkins dyads **compress** from 7.73 to 4.10 words over repetitions while accuracy
rises. So the panel reproduces the human *accuracy* convergence but **not** the human *entrainment /
compression* curve. This is the run's one **human-comparison** claim and the only measure
[`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md) anchors. (Honest scope: a
≤12-word director budget caps the ceiling, and the elicited final nickname is short by construction;
the finding is about the *trajectory* of the in-dialogue expressions, which stays flat.)

## Anchor discipline (read this before citing)

- The **load-bearing trajectory measure is an INTERNAL within-model contrast** (ordered vs shuffled,
  same model both arms) and is **NOT anchored by Hawkins** — the live-vs-shuffled control is novel to
  the LLM probe and unanchored by any human resource, exactly as ratified in
  [`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md)
  and stated in [`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md) §"What it
  CANNOT ground". No human-comparison claim is made for the null.
- The **entrainment curve is the only human-comparison measure** and carries the page's single
  `anchors` link to [`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md).
- The page is `contingent-on`
  [`decisions/open/relational-pilot-operationalization`](../../decisions/open/relational-pilot-operationalization.md):
  the *yardstick* (text-grid referents; order-isolating headline; monologue floor) is provisional
  until Tom ratifies. A null does not over-claim, so it stands as a first-class negative regardless;
  ratification would only fix the yardstick, not the result.

## Caveats (the null is bounded, not strong)

1. **Pilot scale.** n=12 coined terms/model, 2 games, 6 figures. The pilot detects only **large,
   consistent** order effects; a moderate real trajectory effect could read as this null. The honest
   claim is *direction and absence-of-large-effect*, not a precise zero.
2. **A possibly-too-easy probe.** `coined_only` accuracy is already 0.33–0.67 and `ordered` 0.75–0.92
   — there is headroom (not a ceiling artifact), but the opaque-nickname probe may simply not be a
   setting where ordered history *can* carry disambiguating information beyond its content. The
   `coined_only` diagnostic was added precisely so this is visible: history **does** help, order does
   not. A sharper test (the deferred **perturbation arm** — reassign a coined term mid-trajectory and
   test position-sensitivity) is the natural v2.
3. **14 claude truncations** (chatty replies overrunning the 64-token matcher cap) scored as wrong,
   spread across arms; the verifier recomputed claude's order gap with them dropped and the null held.
4. **Gemini at `reasoning: effort=minimal`** (required on this endpoint) — constant across all gemini
   arms, so a within-gemini condition, not a cross-arm confound; cross-*model* comparison is already
   family-confounded by the homogeneous-dyad design.
5. **Labeling refinement disclosed:** the analysis distinguishes a *methodological* null (history not
   load-bearing) from this *deflationary* null (history loads, order does not) by the history_lift
   **point** estimate (>0.10); the frozen **positive** bar (order-gap CI>0) is untouched and unmet by
   every model. This affects only how the two null-flavours are named, not the headline.

## What it licenses

A **first-class relational negative**: at pilot scale, homogeneous LLM dyads coordinate and use coined
conventions, but their conventions are **order-insensitive** — recovered from the content set, not the
ordered trajectory — so the pilot finds **no evidence of relational meaning-constitution** and a
positive demonstration that the deflationary distributional story survives order-scrambling. It does
**not** define a positive bottom rung of the second ladder; it characterises the floor the ladder
would have to rise above. The theory page absorbs it as: the relational axis now has its first
*finding* (a null), no longer only an IOU. Natural next steps (deferred): the **perturbation arm**
(sharper trajectory test), **image referents**, and **cross-family dyads** — see
[`decisions/open/relational-pilot-operationalization`](../../decisions/open/relational-pilot-operationalization.md).
