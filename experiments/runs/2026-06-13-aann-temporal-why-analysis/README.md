# Run: AANN temporal "why does it fail?" re-analysis — 2026-06-13

A **$0, read-only re-analysis** (no model API calls) scoping the open sub-question
left by [`result/aann-temporal-heldout-v2b`](../../../wiki/findings/results/aann-temporal-heldout-v2b.md)
(NEXT.md item 3): **WHY does the temporal noun class fail to replicate the AANN
held-out acceptability gradient** when the object and distance classes carry a clean
positive (ρ ≈ 0.75–0.83)?

Precedent for a re-analysis-only result page:
`experiments/runs/2026-05-30-instrument-disagreement-reanalysis/`.

**Result page:**
[`result/aann-temporal-why-reanalysis`](../../../wiki/findings/results/aann-temporal-why-reanalysis.md).

## What ran

`analyze_why.py` re-reads the frozen raw + stimuli of two existing runs and adjudicates
four candidate explanations. It makes **no model calls** and computes nothing new from
models — every number comes from on-disk artifacts:

- `experiments/runs/2026-06-13-aann-temporal-heldout-v2b/` — the temporal-only widened run
  (`raw/`, `stimuli.json` with the human temporal yardstick + freq audit).
- `experiments/runs/2026-06-12-aann-behavioral-probe-v2/` — the parent run
  (`results.json` held-out per-noun-class Spearman; `human_class_means.csv` per-cell human
  means; `stimuli.json` held-out items with per-adjective Zipf).

Statistics conventions (`ranks`, `spearman`) are copied verbatim from the frozen
`analyze.py` files so the reproduction is byte-faithful.

## Headline

The temporal failure is **two effects, not one**, and the second is the real story:

1. **H1 (compressed human gradient) — SUPPORTED.** The temporal human gradient is the
   **narrowest of all six noun classes** (range 0.883 / sd 0.329 over ambig/neg/pos/quant)
   vs distance 1.826 and objects 2.373 — the two classes that carried v2's positive. A
   3× narrower target is intrinsically harder to rank-recover, so a low |ρ| is expected.
   But compression alone predicts ρ ≈ 0 (noise), **not** the observed *negative*.

2. **H4 (genuine model-side hole) — SUPPORTED, and localized.** The negative sign is
   driven by **one cell: quantity adjectives × temporal nouns** ("a scant three days",
   "a mere two weeks"). Humans rate this cell **highest** (8.45); all three models rate it
   **lowest** (claude 43, gpt 30, gemini 69, well below the other three classes). Drop the
   quant cell and the remaining 3-class ranking flips **positive for every model**
   (claude +1.0, gpt +0.5, gemini +0.5). This is a specific, reproducible inversion, not
   diffuse noise.

3. **H3 (frequency artifact) — RULED OUT.** Temporal and distance share the *identical*
   held-out adjective set and per-adjective Zipf (median 3.595, mean 3.685), yet distance
   tracks +0.60–0.63 and temporal goes negative. Frequency cannot separate them. The v2b
   per-adjclass freq audit also passes for all four classes.

4. **H2 (small inventory) — TRUE but secondary.** Temporal admits 5 Mahowald nouns and a
   structural maximum of 4 class-cells (lattice {0, ±0.2, ±0.4, ±0.6, ±0.8, ±1.0}). This
   caps cell-grain precision and is why v2b's adjective-grain secondary exists — but it
   does not *cause* the negative sign, which survives at adjective grain and per-noun.

**Verdict: not a measurement-precision artifact.** The compressed gradient (H1) makes the
slice hard to read, but the failure is a real, localized model-side hole (H4): models
treat quantity-modified temporal AANNs as *less* acceptable where humans treat them as
*more* acceptable.

## Provenance sanity check

The script first recomputes the published v2b temporal cell-grain Spearman from raw:
claude −0.2000, gpt −0.4000, gemini −0.4000 — **exact match** to the result-page table.

## Reproduce

```
python3 analyze_why.py     # prints the report, writes findings.json ; no API calls, $0
```

## Files

- `analyze_why.py` — the self-contained re-analysis (reads the two run dirs above).
- `findings.json` — all computed numbers (provenance check, H1 spreads, H2 inventory,
  H3 Zipf-by-class, H4 per-noun + quant-localization).
- `README.md` — this file.

## Spend

**$0.00** — no model calls; re-analysis of existing raw only.

## Data limitations (honest)

- n is fixed at the existing data. This run cannot test whether a *wider-spread* temporal
  human gradient would let the construction track positively, nor add temporal nouns.
- The quant-cell inversion is observed on 5 nouns × held-out (project-assigned) quant
  adjectives; it is a robust descriptive pattern across all three models but rests on the
  same human anchored-half yardstick v2b used (no new human data).
