---
type: open-question
id: aann-quant-temporal-inversion
title: "Is the quant×temporal AANN inversion — the one cell where every model rates 'a scant three days' LOW where humans rate it HIGH — the whole quantity-adjective class or a few lexical items?"
meaning-senses:
  - constructional
  - human-comparison
status: open
contingent-on: []
created: 2026-07-06
updated: 2026-07-06
links:
  - rel: refines
    target: result/aann-temporal-why-reanalysis
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
  - rel: depends-on
    target: conjecture/aann-construction
  - rel: depends-on
    target: concept/constructional-meaning
---

# Open question: is the quant×temporal AANN inversion a class effect or a lexical effect?

> **Why this page exists (a $0 scoping artifact).** A read-only re-analysis
> ([`result/aann-temporal-why-reanalysis`](../results/aann-temporal-why-reanalysis.md)) pinned the
> temporal AANN class's failure to replicate the human acceptability gradient to **one cell** and named
> the decider in its handoff — but nobody ran it. This page gives that named decider a typed home. It
> states the question, records the in-repo human anchor honestly (the cleanest of any current
> open-question — a real human gradient already in-repo), sketches — **does not run** — the widened
> probe, and commits no spend.

## The finding this sharpens

The AANN construction ("a beautiful three days", *article–adjective–adjective/numeral–noun*) has a human
acceptability gradient over adjective × noun classes ([`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md),
Experiment-2, 1–10 MTurk scale). Most noun classes replicate the human gradient held-out (objects,
distance carry ρ ≈ 0.6–0.9); the **temporal** class does not — it goes *negative*. The $0 re-analysis
[`result/aann-temporal-why-reanalysis`](../results/aann-temporal-why-reanalysis.md) decomposed that
failure and found it is **two effects, and the second is the real story**: the temporal human gradient
is the narrowest of any noun class (a compression drag on precision), but the *negative sign* is carried
by a single cell — **quantity adjectives × temporal nouns** ("a scant three days", "a mere two weeks"):

| adjective class (× temporal) | human mean | claude | gpt | gemini |
|---|---|---|---|---|
| neg | 7.57 | 49.4 | 40.2 | 75.0 |
| pos | 8.02 | 50.6 | 37.5 | 70.0 |
| ambig | 8.25 | 55.0 | 50.6 | 84.3 |
| **quant** | **8.45 (highest)** | **43.0 (lowest)** | **30.1 (lowest)** | **68.8 (lowest)** |

Humans rate the quant×temporal cell **highest** of the four; **every panel model rates it lowest.** Drop
that one cell and the remaining three-class ranking flips **positive for all three models**. A frequency
artifact is ruled out; small inventory limits precision but not the direction. So this is a **clean,
localized, panel-wide model-vs-human inversion** — and the re-analysis explicitly handed it off:

> "**Targeted quant×temporal items.** Widen the quant adjective set against temporal nouns (more
> *scant/mere/measly/paltry/good*-type quantity modifiers × more temporal nouns) to test whether the
> inversion is the whole quant class or a few lexical items — the present read rests on held-out
> (project-assigned) quant adjectives on 5 nouns." ([`result/aann-temporal-why-reanalysis`](../results/aann-temporal-why-reanalysis.md),
> *What would decide it*)

## The question, sharply

> Is the quant×temporal inversion (humans-high / models-low) a property of the **whole
> quantity-adjective class**, or is it carried by **a few lexical items** (*scant*, *mere*)? Does it
> **persist** when the quantity-adjective set and the temporal-noun set are widened beyond the thin
> held-out inventory (5 nouns, project-assigned quant adjectives) — i.e. is it a genuine, reproducible
> model-vs-human divergence in graded constructional acceptability, or an artifact of a small
> inventory?

## Why it matters for constructional meaning

This is the **one cell in the entire AANN line where every model inverts the human gradient** — the
sharpest available handle on where the AANN construction's learned graded semantics part ways from the
human one (`constructional` × `human-comparison`). The AANN construction is a good wedge precisely
because its acceptability is *graded* and *human-anchored*; a place where the model gradient does not
merely compress but **reverses** relative to humans is a candidate **productivity hole** — the model
generalizes the AANN acceptability gradient correctly for amplitude/evaluative adjectives but treats
*quantity-modified* temporal AANNs as *less* acceptable exactly where humans treat them as *more*. If the
inversion is the whole quant class, that hole is real and construction-internal; if it is a couple of
lexical items, it is noise the thin inventory happened to surface. Either resolution sharpens the AANN
human-comparison picture and bears on [`conjecture/aann-construction`](../conjectures/aann-construction.md).

## What a serious answer would look like (probe sketched, NOT run)

The re-analysis names the design; this page only gives it a home.

1. **Widen the quant × temporal cell.** More quantity modifiers (*scant, mere, measly, paltry, good,
   full, whole, solid, bare*, …) × more temporal nouns (*days, hours, weeks, months, years*, and
   further), read per-cell against the Mahowald human means.
2. **Separate class from item.** If the inversion holds across the widened quant set → a **class** effect
   (a genuine quant×temporal productivity hole). If it collapses to a couple of modifiers → a **lexical**
   effect (*scant/mere* idiosyncrasy), and the temporal class's negative sign is an inventory artifact.
3. **Optional companion arm** (the re-analysis's other handoff): a **wider-spread temporal human
   gradient** (more extreme within-temporal acceptability contrasts) to confirm the compression drag is
   isolable from the quant hole — i.e. that outside the quant cell the construction tracks positive.

The null is first-class: if the inversion **does not** reproduce on the widened set, that dissolves the
temporal class's negative into an inventory artifact — a clean, useful negative, written as such.

## Human-anchor status (honest): IN-REPO, with a scope caveat

Unusually for a fresh open-question, the human anchor is **already in-repo and ratified**:
[`resource/mahowald-2023-aann-stimuli`](../../base/resources/mahowald-2023-aann-stimuli.md) (the
Experiment-2 adjective × noun acceptability gradient, 1–10 scale) is the same human yardstick the
re-analysis used, so a widened quant×temporal probe makes a genuine **human-comparison** claim on any
item Mahowald's stimuli cover. The honest caveat: **new** quant × temporal items not in Mahowald's set
carry no human rating, so a widened probe either (a) restricts to Mahowald-attested quant×temporal items
(fully anchored, but limited to the existing inventory — which may not be wide enough to separate class
from item), or (b) authors new items and reads those as `internal-contrast-only` unless a human rating is
obtained. This trade-off — anchored-but-narrow vs wide-but-partly-unanchored — is the operationalization
choice a real design session would freeze; it is not decided here, and no human rating is invented.

## Tractability and cost

High, and better-anchored than most. The human anchor is in-repo; the instrument is settled (the
re-analysis notes "Tier-0 and framing-robustness already pass in v2b, so the inversion is the models'
graded behavior, not an artifact" — "Neither requires re-litigating the instrument"). A first pass is a
small, low-cost panel probe; a claim-carrying version would use powered N (~100–150 items,
[`PROTOCOL.md`](../../../PROTOCOL.md) §4). Small-N, n=3-models, direction-of-effect caveats apply, and the
coarse temporal lattice (5 nouns, 4 class-cells) is exactly what the widening is meant to relieve.

## How this differs from the existing AANN lines (so it is genuinely fresh)

- **Distinct from the answered founding questions** [`open-question/constructional-vs-frequency-confound`](constructional-vs-frequency-confound.md)
  and [`open-question/distributional-vs-inferential-constructional`](distributional-vs-inferential-constructional.md):
  those settled *whether* AANN sensitivity is more than frequency and whether it is inferential. This is
  a **human-comparison** question about a *specific graded-acceptability cell*, not a frequency or
  inferential-role question — frequency is already ruled out as the driver of this inversion.
- **Distinct from its parent** [`result/aann-temporal-why-reanalysis`](../results/aann-temporal-why-reanalysis.md):
  that was a $0 re-analysis of frozen raw that *located* the inversion in one cell; this is the forward
  probe that would test whether the located inversion is class or item — the decider the re-analysis
  named but did not run.
- It is `model-internal` behaviour set against a human gradient; it does **not** touch the relational
  axis.

## Status: open (scoping only)

This page runs nothing, freezes no operationalization, opens no `wiki/decisions/open/` entry, and spends
nothing. It gives the quant×temporal inversion decider a typed home, states it as a class-vs-item
human-comparison question, records the in-repo Mahowald anchor (with the anchored-vs-wide trade-off flagged
honestly), and points at [`result/aann-temporal-why-reanalysis`](../results/aann-temporal-why-reanalysis.md)'s
handoff as the design of record.
