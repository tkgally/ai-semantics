---
type: result
id: aann-temporal-why-reanalysis
title: WHY the temporal AANN class fails to replicate the held-out gradient — a $0 re-analysis splits it into a compressed human gradient (H1) plus a localized quantity-adjective inversion (H4)
meaning-senses:
  - constructional
  - human-comparison
status: proposed
anchor: resource/mahowald-2023-aann-stimuli
contingent-on: []
created: 2026-06-13
updated: 2026-07-05
links:
  - rel: refines
    target: result/aann-temporal-heldout-v2b
  - rel: anchors
    target: resource/mahowald-2023-aann-stimuli
---

# Result: why time-words fail — compression makes the slice hard to read, but a localized quantity-adjective inversion is the actual hole

> **Status: proposed (2026-06-13).** A **$0, read-only re-analysis** (no model API calls;
> precedent [`experiments/runs/2026-05-30-instrument-disagreement-reanalysis/`](../../../experiments/runs/2026-05-30-instrument-disagreement-reanalysis/README.md))
> of already-collected raw, answering the open sub-question left by
> [`result/aann-temporal-heldout-v2b`](aann-temporal-heldout-v2b.md): **why** does the
> temporal noun class fail to replicate the AANN held-out acceptability gradient when the
> object and distance classes carry a clean positive (ρ ≈ 0.75–0.83)? Verdict: **it is two
> effects, and the second is the real story.** The temporal human gradient is the
> *narrowest of all six noun classes* (a measurement-precision drag, **H1**), but
> compression alone predicts ρ ≈ 0, not the observed *negative*. The negative sign is
> driven by **one cell — quantity adjectives × temporal nouns** ("a scant three days") —
> which humans rate **highest** and every model rates **lowest** (**H4**). Drop that one
> cell and the remaining ranking flips **positive for all three models**. A frequency
> artifact (**H3**) is **ruled out**; small inventory (**H2**) is true but secondary.
> Run record:
> [`experiments/runs/2026-06-13-aann-temporal-why-analysis/`](../../../experiments/runs/2026-06-13-aann-temporal-why-analysis/README.md).

## What this re-analysis is (and is not)

It runs **no new conditions** and makes **no model calls**. `analyze_why.py` re-reads the
frozen raw JSONL + stimuli of two existing runs — the temporal-widened
[`result/aann-temporal-heldout-v2b`](aann-temporal-heldout-v2b.md) and its parent
[`result/aann-behavioral-gradient-v2`](aann-behavioral-gradient-v2.md) — and adjudicates
four candidate explanations from numbers already on disk. The human yardstick throughout is
the Mahowald Experiment-2 adjective×noun acceptability gradient
([`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md),
`mturk_data/adjexp_turk.csv`, 1–10 scale); this page makes **no independent human claim** —
its force is *why an existing within-model contrast against that yardstick comes out
negative*. The arm anchors to the resource only via the human gradient it is asked to explain.

**Provenance sanity check (mandatory):** the script first recomputes the published v2b
temporal cell-grain Spearman from raw — claude **−0.2000**, gpt **−0.4000**, gemini
**−0.4000** — an **exact match** to the v2b result-page table. The new numbers below sit on
top of a verified reproduction.

## H1 — compressed human gradient: SUPPORTED (but insufficient on its own)

The human anchored-half class means, taken over the four adjective classes the temporal
noun admits (ambig / neg / pos / quant), have a **within-class range of only 0.883** on the
1–10 scale (sd 0.329). Across all six noun classes:

| noun class | human range (ambig/neg/pos/quant) | sd | v2 *parent-run* held-out ρ (claude / gpt / gemini) |
|------------|-----------------------------------|-----|----------------------------------------|
| objects | **2.373** | 0.882 | +0.943 / +0.943 / +0.886 |
| art | 1.980 | 0.722 | — (not in held-out) |
| distance | **1.826** | 0.736 | +0.633 / +0.600 / +0.633 |
| human | 1.617 | 0.651 | — (not in held-out) |
| unitlike | 1.098 | 0.444 | — (not in held-out) |
| **temporal** | **0.883** | **0.329** | **−0.20 / −0.20 / −0.20** |

> **Reading the temporal ρ — two runs, not a discrepancy.** The ρ column above is from the
> **v2 *parent* run** (the thin 16-item held-out arm), where the temporal stratum was ≈ −0.2 for
> all three models. The **v2b widened run** (80 items) re-measured the same cell-grain ρ as
> **−0.20 / −0.40 / −0.40** (claude / gpt / gemini) — the figure the provenance check above
> reproduces exactly. Both are correct; they are two runs at two stratum widths, both uniformly
> non-positive. This page's decomposition (H1, H4) draws on the v2b widened raw throughout.

Temporal is the **narrowest gradient of any noun class** — about one-third the spread of
objects and half that of distance, the two classes that carried v2's positive held-out
replication. A 3× narrower target is intrinsically harder to rank-recover, so a low |ρ| on
temporal is unsurprising on measurement grounds alone. **This much is a precision story.**

But it is incomplete: a flat target predicts ρ ≈ 0 (the ranking degrades to noise), **not**
the clean *negative* v2b observed. The human ordering is in fact **identical** across
temporal, distance, objects, art, and human (neg < pos < ambig < quant) — so compression
cannot explain why temporal alone *inverts*. Something model-side is adding a signed effect.

## H4 — genuine model-side hole: SUPPORTED, and localized to one cell

The signed effect is the **quantity-adjective × temporal-noun cell** ("a scant three days",
"a mere two weeks"). Humans rate it **highest** of the four (8.45); every model rates it
**lowest**:

| class | human mean | claude | gpt | gemini |
|-------|-----------|--------|-----|--------|
| neg | 7.57 | 49.4 | 40.2 | 75.0 |
| pos | 8.02 | 50.6 | 37.5 | 70.0 |
| ambig | 8.25 | 55.0 | 50.6 | 84.3 |
| **quant** | **8.45 (highest)** | **43.0 (lowest)** | **30.1 (lowest)** | **68.8 (lowest)** |

This single misplacement carries the negative ρ. **Dropping the quant cell**, the remaining
three-class ranking (neg < pos < ambig) flips **positive for all three models**: claude
**+1.00**, gpt **+0.50**, gemini **+0.50**. The per-noun read agrees — the inversion is not
one rogue noun: it recurs across the inventory (per-noun ρ negative for the higher-frequency
short-span nouns *days*/*hours*, positive for *years*), consistent with a cell-level rather
than noun-level effect. This is a specific, reproducible inversion, not diffuse noise.

**Reading:** held-out, the models generalize the temporal AANN gradient *correctly* for
amplitude/evaluative adjectives but treat **quantity-modified** temporal AANNs as *less*
acceptable exactly where humans treat them as *more* acceptable. That is a real productivity
hole at the quant×temporal intersection — the kind of construction-internal unevenness v2's
caveat 2 first flagged, now pinned to a cell.

## H3 — frequency artifact: RULED OUT

The v2 held-out items carry a per-**adjective** wordfreq Zipf (Condition-5 freq-matched).
Temporal and distance use the **identical** held-out adjective set, hence identical Zipf
(median 3.595, mean 3.685) — yet **distance tracks +0.60–0.63 while temporal goes negative**.
Frequency cannot separate the two classes, so it cannot be the cause. The widened v2b
temporal set is likewise freq-matched (median 3.675) and its per-adjclass freq audit passes
for all four classes. Objects do sit higher (Zipf median 4.16), but objects *replicate*, so
the higher frequency, if anything, runs the wrong way for a frequency explanation of failure.

## H2 — small inventory: TRUE but secondary

Temporal admits **5 Mahowald nouns** (days, hours, months, weeks, years) and a **structural
maximum of 4 class-cells**, so the cell-grain Spearman lives on a coarse lattice
({0, ±0.2, ±0.4, ±0.6, ±0.8, ±1.0}) where one swapped pair moves ρ by 0.2–0.4. This caps
cell-grain precision — and is exactly why v2b pre-registered an adjective-grain secondary.
But it does not *cause* the negative sign: the inversion survives at adjective grain, at
per-noun grain, and in the quant-drop test, so coarseness widens the error bars without
explaining the direction.

## Verdict

**Not a pure measurement-precision artifact.** The compressed human gradient (H1) makes the
temporal slice genuinely hard to read and explains why |ρ| is small and the CIs straddle for
two of three models — but the *sign* comes from a real, localized model-side hole (H4): the
quant×temporal cell is inverted relative to humans across all three models. H3 is ruled out;
H2 limits precision but not direction. The honest two-part summary: **compression ⇒ low
power; a quant-cell inversion ⇒ the negative sign.** This refines, and does not overturn,
[`result/aann-temporal-heldout-v2b`](aann-temporal-heldout-v2b.md)'s
"too-thin/mixed, uniformly non-positive" stratum verdict — it says *where* the non-positivity
lives.

## What would decide it (handoff)

- **A wider-spread temporal human gradient.** The cleanest test of the residual H1 worry is
  a temporal probe whose human anchor has object-class-sized spread (e.g. include more
  extreme acceptability contrasts within temporal). If the construction tracks positive there
  *outside* the quant cell, H1's drag is confirmed isolable from H4's hole.
- **Targeted quant×temporal items.** Widen the quant adjective set against temporal nouns
  (more *scant/mere/measly/paltry/good*-type quantity modifiers × more temporal nouns) to
  test whether the inversion is the whole quant class or a few lexical items — the present
  read rests on held-out (project-assigned) quant adjectives on 5 nouns.
- Neither requires re-litigating the instrument: Tier-0 and framing-robustness already pass
  in v2b, so the inversion is the models' graded behavior, not an artifact.

## Provenance / reproduction

Run dir
[`experiments/runs/2026-06-13-aann-temporal-why-analysis/`](../../../experiments/runs/2026-06-13-aann-temporal-why-analysis/README.md):
`analyze_why.py` (self-contained, reads the two frozen run dirs' raw + stimuli; **$0, no API
import**; Spearman conventions copied verbatim from the frozen `analyze.py` files),
`findings.json` (every figure above), [`README.md`](../../../experiments/runs/2026-06-13-aann-temporal-why-analysis/README.md). The v2b temporal cell-grain ρ reproduces
exactly (−0.20 / −0.40 / −0.40) as a provenance gate before any new conclusion. Human means
from [`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md)
(Experiment-2 `adjexp_turk.csv` adjective×noun gradient, via the v2 `human_class_means.csv`
table and the v2b embedded human temporal yardstick). Refines
[`result/aann-temporal-heldout-v2b`](aann-temporal-heldout-v2b.md); `contingent-on: []`.
