---
type: result
id: aann-behavioral-gradient-v2
title: AANN behavioral gradient v2 — all three models' prompted acceptability tracks the human Exp-2 MTurk gradient (ρ 0.68–0.75 at cell grain) and replicates it on frequency-matched held-out adjectives; SUPPORTED on the pre-registered map
meaning-senses:
  - constructional
  - distributional
  - functional-vs-formal
  - human-comparison
status: proposed
contingent-on: []
created: 2026-06-12
updated: 2026-07-05
links:
  - rel: supports
    target: conjecture/aann-construction
  - rel: anchors
    target: resource/mahowald-2023-aann-stimuli
  - rel: depends-on
    target: claim/formal-competence-aann-ceiling
  - rel: refines
    target: theory/constructional-meaning-in-llms
  - rel: supports
    target: claim/aann-behavioral-gradient
---

# Result: AANN behavioral gradient probe v2 — SUPPORTED

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The follow-up this page's caveat 2
> asked for landed: [`result/aann-temporal-heldout-v2b`](aann-temporal-heldout-v2b.md) widened the
> temporal held-out cells 5× and found the stratum uniformly negative for all three models,
> sharpening the caveat into a finding (held-out productivity is noun-class-dependent). The line was
> promoted in session 176 to [`claim/aann-behavioral-gradient`](../claims/aann-behavioral-gradient.md)
> (scoped to Tier-2 gradient tracking), and the cross-date replication
> [`result/aann-behavioral-gradient-rep2`](aann-behavioral-gradient-rep2.md) (session 178; 408 fresh
> items drawn disjoint from this run) replicated the anchored gradient 3/3 with overlapping CIs,
> discharging the claim's single-run caveat for the graded gradient.
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

The first run of the AANN probe, under the behavioral instrument ratified 2026-06-12
([`decisions/resolved/aann-behavioral-operationalization`](../../decisions/resolved/aann-behavioral-operationalization.md),
ADOPT DEFAULT with nine binding conditions). Frozen design:
[`design/aann-construction-v2`](../../../experiments/designs/aann-construction-v2.md); PREREG +
pre-run-critic amendment, raw data, and run record:
[`experiments/runs/2026-06-12-aann-behavioral-probe-v2/`](../../../experiments/runs/2026-06-12-aann-behavioral-probe-v2/README.md).
1,782 calls, **$0.3125 billed**, **zero missing responses in every arm**. An independent
post-run verifier recomputed every gate from the raw data with its own code: **0 mismatches**.

## Headline (pre-registered verdict: SUPPORTED)

All three panel models' prompted graded acceptability (0–100, temperature 0) **rank-tracks the
human MTurk acceptability gradient** over the Mahowald Exp-2 adjective × noun-class space, and
the adjective-class gradient **replicates on frequency-matched held-out adjectives the human
raters never saw**:

| Gate (frozen pre-run) | A claude-sonnet-4.6 | B gpt-5.4-mini | C gemini-3.5-flash |
|---|---|---|---|
| Tier-0 manipulation check (≥ 20/24) | 23/24 | 23/24 | 24/24 † |
| Anchored cell-level Spearman, 204 cells (≥ 0.40) | **0.7017** | **0.6843** | **0.7505** |
| bootstrap 95% CI (excludes 0) | 0.61–0.77 | 0.60–0.75 | 0.68–0.81 |
| Zipf frequency guard, partial ρ (≥ 0.20) | 0.6919 | 0.6607 | 0.7363 |
| Noun-class guard, within-class mean ρ (≥ 0.25) | 0.630 | 0.659 | 0.654 |
| Held-out replication vs human class-cells (≥ 0.50) | 0.8336 | 0.8143 | 0.7525 |
| Held-out within-noun-class mean (≥ 0.30) | 0.4585 | 0.4476 | 0.4394 |
| Framing robustness, 0–100 vs 4-point ρ (≥ 0.50) | 0.9288 | 0.8168 | 0.8215 |

Secondary grain (28 adjective-class × noun-class cells, descriptive): ρ = 0.85 / 0.84 / 0.92.
Item-level against single human ratings (descriptive floor; single-rater noise): 0.49 / 0.45 /
0.45.

**What this adds beyond the known Tier-0 ceiling.** [`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md)
already documented that models accept licit AANN over degenerate variants (formal competence);
that claim's own carve-out named the *graded* adjective/noun-class sensitivity as requiring
separate treatment. This run is that treatment: the models do not merely prefer licit forms —
their graded ratings reproduce the **shape** of the human acceptability gradient (which
adjective classes license AANN more, in which noun-class environments), survive a frequency
control, survive a noun-class-marginal control, and **generalize the class gradient to novel
adjectives** under a locked, frequency-matched list. That is behavior consistent with a
productive form–meaning pairing, not a memorized template inventory.

## Anchor discipline

Anchored to [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md)
(Exp-2 MTurk ratings; 3,600 non-filler single-rating items aggregated to 204 cell means). The
**held-out arm carries no independent human claim**: its evidential type, declared pre-run, is
*gradient replication* — the model's held-out class ordering is scored against the human
**anchored-half** ordering. The human side of the held-out sentences themselves was never
measured (those adjectives are outside Mahowald's set by construction).

## Validity bounds (binding, from the design §5 — read the headline through these)

- **"Rates as good" conflates sensitivity with preference.** A high gradient correlation shows
  the models' acceptability behavior *tracks* the human gradient; it does **not** show the
  construction's meaning is *represented*, nor that the unification/evaluation semantics is
  *used* (the conjecture's inferential half remains untested — see Scope).
- The surprisal-validity claim ([`claim/cxg-probing-surprisal-validity`](../claims/cxg-probing-surprisal-validity.md))
  does not warrant this instrument; its validity rests on measure-homology with the anchor
  (humans gave prompted ratings too), Mahowald's own CoLA-validated prompted method, and the
  house dual-framing standard — argued in full in the design.
- Scale-use calibration differs by model; rank correlation mitigates, does not eliminate.

## Caveats (post-run verifier's required list — none change the verdict)

1. **Tier-0 parse defect on one item (footnote to C's 24/24).** The A/B parser takes the first
   bare token, so a prose indefinite article ("a") could be read as the answer "A". All 3 of
   model C's verbose Tier-0 responses were scored that way; on `tier0-ugly-three-desks-reverse_mods`
   the recorded "A" contradicts the model's own stated conclusion ("B"). Worst-case rescore:
   C = 23/24 — still a pass; no gate or verdict changes under any scoring of the item.
2. **The held-out gradient does not replicate in the temporal stratum.** Held-out within-class
   passes (0.44–0.46) mainly via objects (0.89–0.94) and distance (0.60–0.63); the **temporal
   stratum is ≈ −0.2 for all three models** (4 class-cells, one rank swap from positive at that
   n, but uniformly negative). Productivity is real at the overall grain and **uneven by noun
   class**; a follow-up should widen the temporal held-out cells before reading more into it.
3. **The headline depends on the pre-registered cell averaging.** Item-level correlations
   against single human ratings are 0.45–0.49 — the honest descriptive floor; single-rater item
   noise is why cell grain was (pre-run) declared primary.
4. **Upstream stimulus typo, faithfully reproduced.** 28 anchored sentences use Mahowald's
   template typo "The tourish stayed … in Papua New Guinea." Human raters saw the identical
   string (verified in the mirrored MTurk materials), so the comparison is apples-to-apples;
   model A noticed the typo twice and rated low — as, presumably, did some humans.
5. **Response quantization.** A used 21 distinct rating values, C 15 (multiples of 5, with
   ceiling-piling: 34.6% of C's anchored responses ≥ 90); B 70. Rank statistics with average
   ties handle this, and ties depress rather than inflate ρ, but the distributions are not
   smooth.

## Scope — what this result does NOT show

- Nothing about the **inferential half** of the conjecture (does the model draw the
  unified-stretch/evaluative paraphrase?) — a different indicator, explicitly out of this
  design's scope (§8) and the natural v3 question.
- Nothing about **representations** (behavioral acceptability only), **other constructions**
  (AANN-scoped, per [`decisions/resolved/cxg-probing-anchor`](../../decisions/resolved/cxg-probing-anchor.md)),
  or **human-likeness beyond the measured gradient** (MTurk raters, not an expert panel — the
  anchor's known limits carry over).
- The conjecture's prediction 3 (panel divergence by training mix) was **not** borne out in any
  interesting way and was not a gate: all three models pass all gates; gpt-5.4-mini is *not*
  the laggard the calibration hint suggested (its gradient numbers are competitive), which is
  itself worth recording as a small disconfirmed expectation.

## Verification chain

Pre-run: independent critic (3 blockers fixed pre-run, including the noun-class guard whose
absence would have let a zero-adjective-information responder pass at ρ = 0.466). Freeze:
PREREG + amendment committed before any call (verified against git history). Post-run:
independent verifier, own code, every number reproduced exactly; anti-cheat diff of PREREG /
analyze / stimuli / human tables between freeze and analysis: **empty**.
