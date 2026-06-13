---
type: design
id: aann-temporal-heldout-v2b
title: AANN temporal held-out widening (v2b) — addendum under the ratified v2 behavioral instrument, resolving caveat 2 of the v2 result
meaning-senses:
  - constructional
  - human-comparison
status: draft (pre-critic; freeze after independent pre-run critic)
contingent-on: []
created: 2026-06-13
updated: 2026-06-13
links:
  - rel: refines
    target: design/aann-construction-v2
  - rel: depends-on
    target: result/aann-behavioral-gradient-v2
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
---

# Design addendum v2b — AANN temporal held-out widening

**What this is.** The named follow-up to **caveat 2** of
[`result/aann-behavioral-gradient-v2`](../../wiki/findings/results/aann-behavioral-gradient-v2.md):
v2's held-out gradient replication passed overall (0.44–0.46 within-class mean), but the
**temporal stratum was ≈ −0.2 for all three models over only 4 class-cells** — 4 single
items per cell, one rank swap from positive at that n, uniformly negative, too thin to
read. This addendum widens the temporal held-out stratum and re-reads it. It is a
**precision/robustness widening of an existing arm, not a new conjecture test**: the
outcome (replicates / fails-to-replicate / still-too-thin) refines the v2 result's
caveat 2 and does not re-adjudicate v2's overall verdict.

**No new operationalization decision is needed.** This run executes **under** the
ratified instrument of [`design/aann-construction-v2`](aann-construction-v2.md)
(governing decision
[`decisions/resolved/aann-behavioral-operationalization`](../../wiki/decisions/resolved/aann-behavioral-operationalization.md),
nine binding conditions): same primary indicator (prompted 0–100 graded acceptability,
integer-only, temperature 0), byte-identical prompt, same panel and per-model settings
(A claude-sonnet-4.6 / B gpt-5.4-mini / C gemini-3.5-flash with reasoning effort
minimal + 512 max_tokens, per `config/models.md`), same frequency-control procedure
(wordfreq 3.x Zipf, per-class median within ±0.5 of the Mahowald class median,
mechanically asserted), and the **same read**: held-out class-cell ordering scored
against the **human anchored-half** ordering — the gradient-replication evidential
type, with no independent human claim. Anchor route unchanged:
[`resource/mahowald-2023-aann-stimuli`](../../wiki/base/resources/mahowald-2023-aann-stimuli.md)
via the anchored-half gradient.

## 1. Widening geometry (what changes, and the one thing that cannot)

The v2 temporal stratum had 4 class-cells × 1 adjective-item each per cell-quarter —
concretely, 4 held-out adjectives per class × **1 temporal item each** = 4 items per
class-cell, 16 temporal items total.

v2b widens **within** cells (run dir
`experiments/runs/2026-06-13-aann-temporal-heldout-v2b/`):

| Dimension | v2 | v2b |
|---|---|---|
| Temporal class-cells | 4 (ambig, neg, pos, quant) | **4 — unchangeable** (see below) |
| Held-out adjectives per class | 4 | **10** (6 new + the 4 v2 carryovers) |
| Items per adjective (temporal) | 1 | **2** (distinct noun + template) |
| Items per class-cell | 4 | **20** |
| Temporal nouns | 4 of 5 | **all 5** (days, hours, weeks, months, years) |
| Temporal items / calls | 16 / 48 | **80 / 240** |

- **The class-cell count cannot exceed 4.** Per Mahowald's Exp-2 validity matrix (as
  realized in the committed v2 human tables), only ambig, neg, pos, quant are valid on
  temporal nouns (human/stubborn/color are not). So "widen the temporal held-out
  cells" can only mean more adjectives, nouns, and items **per** cell — the primary
  4-cell Spearman stays coarse, which is exactly why a finer-grain secondary read is
  pre-registered (§2). Stated plainly so nobody reads the addendum as having added
  cells.
- **New adjectives** (6 per class, frozen in `prep.py`): none in Mahowald's 50, none in
  the v2 held-out 24; per-class Zipf median within ±0.5 of the Mahowald class median
  for both the new-6 and the combined-10 lists — all 4 classes pass mechanically
  (audit table embedded in `stimuli.json`).
- **Nouns and templates come from Mahowald's own inventory**, recovered exactly from
  the committed v2 stimuli: the 5 temporal nouns are Mahowald's full temporal noun
  class (all appear in v2's anchored sample), and the 3 temporal sentence templates are
  string-recovered from committed v2 sentences with consistency asserts — including
  the upstream "tourish" typo template, retained for instrument continuity (held-out
  items make no item-level human comparison, so the typo carries no anchor risk here).
- **Mirror-independence:** the gitignored upstream mirror is absent in this checkout;
  `prep.py` builds everything from the committed v2 `stimuli.json` +
  `human_class_means.csv`, and aborts unless the local wordfreq reproduces every
  committed v2 Zipf value exactly (it does: wordfreq 3.1.1, zero mismatches over all
  74 adjectives).

## 2. Read and pre-registered statistics (summary; PREREG-draft is authoritative)

- **Primary (same read as v2 caveat 2):** per-model Spearman between the 4 widened
  held-out temporal class-cell means and the human anchored temporal class-cell means
  (quant 8.45 > ambig 8.25 > pos 8.02 > neg 7.57, from the frozen v2
  `human_class_means.csv`). Honest caveat, stated pre-run: at 4 class-cells a Spearman
  is coarse (lattice {0, ±0.2, ±0.4, ±0.8, ±1}); it is read jointly with —
- **Secondary, finer grain (chosen before any data):** adjective-grain Spearman — 40
  held-out adjective means vs the class-assigned human anchored temporal mean
  (average-rank ties), with a 10,000-resample percentile bootstrap 95% CI over
  adjectives. Same comparison, real resolution.
- **Verdict categories (frozen in the PREREG):** per model **replicates** (class-cell
  ρ ≥ 0.40 AND adjective-grain ρ ≥ 0.20 with CI lower bound > 0) /
  **fails-to-replicate** (adjective-grain CI upper bound < 0.20) / **still-too-thin**
  (otherwise); stratum verdict by the ≥2-of-3 rule. All outcomes, including the null,
  are written as a refinement of the v2 result's caveat 2.
- Descriptive extras (no gates): pooled item-grain rank agreement (n = 80), Zipf
  partial at adjective grain, carryover-vs-v2 consistency, new-vs-carryover subgroup
  means.

Full numbers, missingness rules (>10% caveat / >25% instrument failure / INCOMPLETE on
abort), and disclosures:
`experiments/runs/2026-06-13-aann-temporal-heldout-v2b/PREREG-draft.md`.

## 3. Honest strains on "same instrument, no new decision"

Flagged for the pre-run critic rather than smoothed over:

1. The **secondary adjective-grain statistic is new at gate level** — v2 gated nothing
   at that grain. It is the same model-vs-anchored-half comparison at finer grain,
   declared pre-data; if the critic reads it as a new operationalization rather than a
   precision read, the fallback is to demote it to descriptive and accept that 4-cell
   coarseness may force a still-too-thin verdict.
2. **Tier-0 is inherited from v2** (all three models passed 23–24/24 one day earlier,
   identical settings), not re-run. A fresh Tier-0 costs ~$0.013 if required.
3. **Carryover re-rating** pools previously-probed held-out adjectives with new ones
   (both human-unseen by construction); subgroup numbers are reported.

## 4. Cost (config/budget.md)

240 calls. Pre-flight from v2's **measured billed** held-out per-call rates:
point estimate **$0.042**, expected **≈ $0.04–0.09 billed**; abort flag $0.30 coded in
`probe.py`. Well under the $2.50 single-run flag and the $5.00/day budget.

## 5. Run protocol

1. `prep.py` (run, no model calls) froze `stimuli.json` (80 items, audit embedded).
2. Independent **pre-run critic** reviews this addendum + PREREG-draft + stimuli;
   fixes applied; `analyze.py` written; PREREG-draft committed as `PREREG.md`
   (**freeze**). `probe.py` refuses to run before the freeze.
3. `probe.py` — 240 calls via `experiments/lib/openrouter.py` (`usage: include`),
   raw JSON per model under `raw/`, one verbatim retry, billed-cost log, $0.30 abort.
4. `analyze.py` computes exactly the PREREG statistics; independent **post-run
   verifier** recomputes from raw before any wiki edit.
5. Result: an update refining
   [`result/aann-behavioral-gradient-v2`](../../wiki/findings/results/aann-behavioral-gradient-v2.md)
   caveat 2 (or a small follow-up result page linked `refines` to it), anchored to
   [`resource/mahowald-2023-aann-stimuli`](../../wiki/base/resources/mahowald-2023-aann-stimuli.md)
   via the anchored-half-gradient route, stating the gradient-replication evidential
   type explicitly.

## 6. What this addendum does not do

No new constructions, no inferential-paraphrase arm, no anchored-arm re-run, no
re-adjudication of v2's overall verdict map, no independent human claim for held-out
items, and no claim that 4 class-cells became more than 4.
