---
type: design
id: aann-construction-v2
title: AANN construction probe v2 — graded behavioral instrument, gradient-primary, anchored to the Mahowald 2023 Exp-2 MTurk gradient
meaning-senses:
  - constructional
  - distributional
  - functional-vs-formal
  - human-comparison
status: frozen (pre-run)
contingent-on: []
created: 2026-06-12
updated: 2026-06-12
links:
  - rel: operationalizes
    target: conjecture/aann-construction
  - rel: depends-on
    target: resource/mahowald-2023-aann-stimuli
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supersedes
    target: design/aann-construction-v1
---

# Experiment design v2 — AANN construction (behavioral, gradient-primary)

**Governing decision:** [`decisions/resolved/aann-behavioral-operationalization`](../../wiki/decisions/resolved/aann-behavioral-operationalization.md)
— **ratified 2026-06-12** (autonomous cross-session adversarial review): ADOPT DEFAULT (Option A),
instrument-class only, under **nine binding conditions**. This design is written to satisfy all
nine; each is cited where it bites. The superseded v1
([`design/aann-construction-v1`](aann-construction-v1.md), logprob instrument) was retired unrun.

**Freeze discipline.** Everything in this page — stimuli, prompts, grain, thresholds, per-model
settings — is frozen **before any finding-bearing model call**. Pilot/dry-run outputs must not
inform thresholds (Condition 4). The held-out adjective list is lexically frozen in
`experiments/runs/2026-06-12-aann-behavioral-probe-v2/prep.py` and `stimuli.json` (Condition 5).

## 1. Construct

Unchanged from v1 §1: the AANN construction (*a beautiful three days*) as a productive
form–meaning pairing; the question is whether panel models' **graded acceptability behavior
tracks the human acceptability gradient** over adjective-class × noun-class structure, beyond
the Tier-0 licit/illicit form ceiling already documented in
[`claim/formal-competence-aann-ceiling`](../../wiki/findings/claims/formal-competence-aann-ceiling.md).

## 2. Indicator (ratified instrument-class, made concrete)

**Primary indicator:** prompted graded acceptability (0–100 framing), rank-correlated against the
**empirical** Mahowald Experiment-2 MTurk gradient.

- **Condition 1 (empirical, not stipulated gradient).** The human side is computed from the
  mirrored `mturk_data/adjexp_turk.csv` (3,600 non-filler single-rating items): committed
  derived tables `human_cell_means.csv` (204 adjective × noun-class cells, n ≈ 11–20 ratings
  each) and `human_class_means.csv` (28 adjective-class × noun-class cells). **No predicted
  class ordering is hardcoded anywhere in the scoring path.** Noted discrepancy, per the
  ratification: the decision page's parenthetical ("evaluative > quantitative > stubborn/color")
  and the resource page's canonical ordering ("quantitative > ambiguous > qualitative >
  stubborn/color") disagree; both are *ignored* — scoring is against empirical cell means only.
  Vocabulary note: the released `adj_exp.csv` uses 7 classes (`ambig`, `quant`, `pos`, `neg`,
  `human`, `stubborn`, `color`); the paper's "qualitative" = `pos` + `neg`.
- **Condition 2 (grain, fixed now).** **Primary grain: cell-level** — Spearman ρ between the
  model's cell mean (2 sampled items per cell, primary framing) and the human cell mean (all
  ratings in the cell), across the **204** (adjective × noun-class) cells. Ties: average ranks.
  **Secondary grain:** the 28 (adjective-class × noun-class) cell means, same statistic.
  **Item-level** Spearman across the 408 sampled items is reported as a descriptive robustness
  number only (each item carries a single human rating — rater noise attenuates item-level ρ;
  this is why cell grain is primary, and the attenuation is disclosed wherever item-level ρ is
  reported).
- **Condition 8 (framings).** Primary framing: **0–100** ("respond with only the integer").
  Robustness framing: **4-point** (1–4), on a fixed 102-item subset flagged in `stimuli.json`.
  Divergence check: item-level Spearman between the two framings' ratings on the subset; if
  < 0.50 for a model, an instrument-fragility caveat is mandatory in the result page for that
  model. Per-model settings locked: temperature 0; `max_tokens` 16; panel C (gemini) runs with
  `reasoning: {"effort": "minimal"}` (the ratified cost/behavior mitigation); panel per
  `config/models.md` (A claude-sonnet-4.6, B gpt-5.4-mini, C gemini-3.5-flash).

**Productivity arm (Conditions 5, 6):** 22 **held-out adjectives** (4 per class, 6 classes;
`HELD_OUT` in `prep.py`; none in Mahowald's 50), frequency-controlled: resource = **wordfreq 3.x
Zipf scale (en)**; statistic = per-class **median Zipf**; procedure = each held-out class median
within **±0.5** of the Mahowald class median (asserted mechanically in `prep.py`; all 6 pass).
60 items over the validity-matrix noun classes. **Evidential type, declared now:** held-out
items have **no human ratings by construction**; the arm is **gradient replication** — does the
model's held-out (adjective-class × noun-class) cell-mean ordering reproduce the **human
anchored-half ordering** over the same 15 class-cells? The arm's anchor discipline: it anchors
to [`resource/mahowald-2023-aann-stimuli`](../../wiki/base/resources/mahowald-2023-aann-stimuli.md)
**via the anchored-half gradient it must replicate**; it makes no independent human claim, and
the result page will state exactly that.

**Tier-0 manipulation check (Condition 7):** 24 forced-choice pairs (6 item-tuples × Mahowald's
4 degenerate variants: `reverse_mods`, `no_mod`, `no_plural`, `no_a`), AANN position randomized
(seeded). **Pass: ≥ 20/24 (≈83%) AANN preferred.** Pre-declared failure consequence: a model
failing Tier-0 has its gradient numbers reported as **instrument failure** and is **excluded
from the support count** — not reinterpreted.

## 3. Numeric support criteria (Condition 4 — fresh, frozen pre-run)

Per model, **anchored-arm pass** requires all of:

1. cell-level Spearman **ρ ≥ 0.40** across the 204 cells (primary framing), AND
2. bootstrap 95% CI (10,000 resamples over cells, percentile method) **excludes 0**, AND
3. **frequency guard:** partial Spearman of model cell means vs human cell means, controlling
   the adjective's Zipf frequency (rank-residualization), **ρ_partial ≥ 0.20**. A model whose
   raw ρ passes but whose partial falls below 0.20 is a **frequency-confounded pass = not a
   pass** (recorded as such).

**Held-out replication pass** (per model): Spearman between the model's held-out class-cell
means and the **human anchored** class-cell means over the 15 held-out class-cells **ρ ≥ 0.50**.

**Conjecture-level verdict (pre-registered):**

- **SUPPORTED:** ≥ 2 of 3 Tier-0-passing models achieve the anchored-arm pass, AND each of
  those models also passes held-out replication.
- **PARTIAL (memorization-like):** ≥ 2 of 3 pass anchored but held-out replication fails for
  at least one of them.
- **PARTIAL (form-without-gradient):** Tier-0 passes broadly but < 2 models pass the anchored
  gradient — formal competence without graded constructional sensitivity (a
  `functional-vs-formal` finding, mirroring v1 §7).
- **FALSIFIED (current form):** no Tier-0-passing model achieves the anchored-arm pass, OR
  every nominal pass is frequency-confounded (guard 3 fails for all).
- Any null is written as a first-class result.

T1 (ρ ≥ 0.30) from the retired surprisal operationalization was **not** carried over; the 0.40
cell-level threshold is set higher because cell means (n ≈ 11–20 human ratings, 2 model items)
remove much of the rater noise that motivated T1's leniency, and it was fixed before any model
output existed (Condition 4).

## 4. Human anchor

[`resource/mahowald-2023-aann-stimuli`](../../wiki/base/resources/mahowald-2023-aann-stimuli.md)
— **catalogued 2026-06-12** (mirror inspected; MIT license verified; Condition 3 satisfied:
Exp-2 item-level ratings confirmed usable — 3,600 non-filler rows, one rating per item, 1–10
scale). The anchor grounds the **graded acceptability gradient** (Exp 2 adjective × noun
structure). Known limits carry over from the resource page (MTurk raters, not expert panel).
Experiment-3 (`adjorder_turk.csv`) is **not** consumed: it covers a two-adjective order contrast
outside this design's scope — "Exp 2/3" in the decision text reduces, for this design, to Exp 2,
and that narrowing is recorded here openly.

## 5. Validity argument and its bounds (Condition 9 — stated as prominently as the surprisal claim stated its own)

**For the instrument:** (i) **measure-homology** — the anchor's human ratings were themselves
prompted graded acceptability judgments (1–10), so model-prompted ratings need no extra linking
hypothesis from log-probability to acceptability; (ii) **method precedent in the anchor's own
source** — Mahowald validated prompted good/bad acceptability on the CoLA dev set (84% accuracy,
MCC 0.63; see [`source/mahowald-2023-aann-judgments`](../../wiki/base/sources/mahowald-2023-aann-judgments.md))
before applying it to AANN; (iii) the dual-framing graded instrument is the project's standard
across ~10 prior runs.

**Bounds (binding on any result's prose):**

- "Rates as good" **conflates sensitivity to the construction with preference for it**; a high
  gradient correlation shows the model's acceptability behavior *tracks* the human gradient, not
  that the construction's meaning is *represented*.
- **Framing dependence is real in this repo** (instrument-disagreement re-analysis: per-model
  instrument gaps up to ~50 pp); hence the dual framing and the mandatory fragility caveat.
- **Scale-use calibration differs by model**; rank correlation mitigates but does not eliminate.
- [`claim/cxg-probing-surprisal-validity`](../../wiki/findings/claims/cxg-probing-surprisal-validity.md)
  warrants the **surprisal** instrument only and does **not** transfer to this behavioral one.
- Human item ratings are **single-rater**; model cell means use 2 items vs the human ~11–20 —
  composition noise is unbiased under the seeded random sample but nonzero.

## 6. Pre-flight cost (config/budget.md)

594 calls/model (408 anchored + 102 robustness + 60 held-out + 24 Tier-0) × 3 models = **1,782
calls**, ~80 tokens in / ~8 out each. Rate-card ≈ $0.24; billed expectation with the known
~4.5× factor and gemini-minimal mitigation ≈ **$1.0–1.5**. Today's prior spend $0.29; headroom
$4.71 — under the $2.50 single-run flag. Actual billed `usage.cost` recorded in the run record.

## 7. Run protocol

1. `prep.py` (already run — no model calls) froze `stimuli.json`, `human_cell_means.csv`,
   `human_class_means.csv`; mirror commit `c8095a0` pinned.
2. Independent **pre-run critic** reviews this design + PREREG + stimuli before any call.
3. `probe.py`: all calls via `experiments/lib/openrouter.py` (`usage: include`), raw JSON per
   model under `raw/`; unparseable responses get **one** verbatim retry, then count as missing
   (missingness reported per model; > 10% missing in any arm = mandatory caveat; > 25% =
   instrument failure for that arm).
4. `analyze.py` computes exactly the §3 statistics; an independent **post-run verifier** checks
   numbers against raw before the result page is written.
5. Result page `wiki/findings/results/aann-behavioral-gradient-v2.md`, anchored to
   [`resource/mahowald-2023-aann-stimuli`](../../wiki/base/resources/mahowald-2023-aann-stimuli.md).

## 8. What this design does not do

Unchanged in spirit from v1 §8: no inferential-paraphrase arm (a future v3 question); no
cross-construction generality claim; no commitment to Mahowald's theoretical analysis. It also
does **not** reuse v1's thresholds, item counts, or logprob machinery anywhere.
