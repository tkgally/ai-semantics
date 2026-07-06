---
type: result
id: presupposition-projection-v1
title: "Presupposition projects above a matched entailment WITHIN each model (verdict PROJECTION, 2/3) — but the conditional-antecedent frame COLLAPSES projection across the whole panel"
meaning-senses:
  - inferential
  - distributional
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-01
updated: 2026-07-05
links:
  - rel: depends-on
    target: conjecture/presupposition-projection-vs-entailment
  - rel: depends-on
    target: open-question/presupposition-projection-corner
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: the presupposition / projection probe v1

The **first empirical touch on the presupposition / projection corner** opened session 157
([`open-question/presupposition-projection-corner`](../open-questions/presupposition-projection-corner.md)).
It runs the pre-registered bet of
[`conjecture/presupposition-projection-vs-entailment`](../conjectures/presupposition-projection-vs-entailment.md):
does a current model treat a base sentence's **presupposition** as **projecting** — surviving
negation / polar-question / conditional-antecedent embedding — *more than* a **matched ordinary
entailment** on the same base (the semantics literature's "hallmark of presuppositions",
[`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md),
§1.2)? Run record:
[`experiments/runs/2026-07-01-presupposition-projection/`](../../../experiments/runs/2026-07-01-presupposition-projection/README.md);
frozen [`PREREG.md`](../../../experiments/runs/2026-07-01-presupposition-projection/PREREG.md),
manifest sha `e3a04cdd…`.

> **Update (2026-07-05, session 183 — wiki-coherence pass).** Later artifacts on this line:
> [`result/conditional-projection-rescue-v1`](conditional-projection-rescue-v1.md) (session 159,
> ROBUST-COLLAPSE — the conditional collapse replicated exactly and resisted the rescue framings);
> [`result/projection-trigger-inventory-v1`](projection-trigger-inventory-v1.md) (session 160,
> MIXED) with its $0 per-family decomposition
> [`note/projection-trigger-inventory-family-decomposition-v1`](../notes/projection-trigger-inventory-family-decomposition-v1.md)
> (session 161); and [`result/presupposition-doppelganger-control-v1`](presupposition-doppelganger-control-v1.md)
> (session 173: BEATS-DOPPELGANGER pooled 3/3, but the under-licensed outcome — the residual is
> keyed to the trigger word-form and surface-cue-reconstructable; `anchor: internal-contrast-only`
> ratified s174). *(Back-annotation added by a maintenance pass; nothing measured or decided on
> this page changes.)*

**One-line finding.** The pre-registered verdict is **PROJECTION**: **2 of 3 models** (claude-sonnet-4.6,
gemini-3.5-flash) pass the plain-frame sanity floor **and** endorse the presupposition under the
entailment-cancelling frames far more than the matched entailment (per-model projection gaps
**+0.64** and **+0.72**); the third (gpt-5.4-mini) shows the same *direction* (gap **+0.36**) but its
presupposition-survival (0.53) falls just under the frozen 0.60 floor, so it does not clear the
projection bar (it is not flat either — a partial signal). **But** the headline hides a sharp
frame-asymmetry that is the more interesting finding: projection is **near-perfect under negation and
strong under questions, and COLLAPSES under the conditional antecedent for all three models**
(presupposition-survival under the conditional frame is **0.42 / 0.17 / 0.17**, barely above — and for
gemini equal to — the matched-entailment leg).

## Scope — LOAD-BEARING (read before citing)

**Within-model contrast only; no human comparison.** The signal is *the presupposition leg survives
more than the matched-entailment leg, within the same model* — **not** *the model matches human
projection judgments*. No human projectivity baseline is claimed, measured, or needed. The result
does **not** certify that a model *represents* presupposition-vs-assertion semantically; it reads
endorsement of an inference under embedding off forced-choice answers (text-consistency is not
mechanism). Anchor is **`anchor: internal-contrast-only`** — **ratified** by an independent
session-159 adversarial review
([`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../decisions/resolved/presupposition-projection-internal-contrast-anchor.md);
the reviewer checked `analyze.py`/`prep.py` and confirmed every threshold scores only the
within-model P-vs-E gap — no human key, no gold label, no external dataset). The within-model
contrast makes no human-comparison claim, so no resource anchor is required. Ratification fixed the
**yardstick, never the result** — every number and caveat below stands unchanged.

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A),
  `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C), as subjects. Temperature 0; text-only,
  single-turn, zero-shot; gemini `reasoning={"effort":"minimal"}`. A neutral system prompt
  ("You are a careful reader…") that never mentions presupposition, projection, or the right answer.
- **Items.** 12 project-authored matched base scenarios across **4 trigger families** (factive /
  aspectual / definite-description / it-cleft; 3 each) × **2 targets** (presupposition P vs. matched
  entailment E) × **4 frames** (plain / negation / question / conditional) = **96 item-conditions**
  per model, 288 calls total. Each item is one forced choice — *"does it follow that: <target>?
  YES / NO / UNCLEAR."* `endorsed` == answer parses to YES.
- **Cost.** **$0.0486 billed** (`usage.cost`-summed: claude $0.0286 / gpt $0.0087 / gemini $0.0113),
  0 missing cost, **0 unparsed** answers. Far under the $2.50 single-run flag; UTC-2026-07-01 day
  total after this run **$0.0486** of $5.00. Pre-flight (12 calls, $0.0019) extrapolated to ≈$0.046.

## Numbers (from `results.json`; independently reproduced)

**Per model** (rates; cancelling = negation + question + conditional pooled):

| model | plain P / E | presup-survival | entail-survival | projection-gap | sanity | projection? |
|-------|-------------|-----------------|-----------------|----------------|--------|-------------|
| A claude-sonnet-4.6 | 0.92 / 1.00 | **0.81** | 0.17 | **+0.64** | ✓ | **yes** |
| B gpt-5.4-mini | 0.92 / 0.92 | 0.53 | 0.17 | +0.36 | ✓ | no (survival < 0.60; not flat) |
| C gemini-3.5-flash | 1.00 / 1.00 | **0.72** | 0.00 | **+0.72** | ✓ | **yes** |

Verdict per the frozen map (SANITY 0.75 / SURVIVE 0.60 / GAP 0.30 / FLATBAND 0.15): **PROJECTION**
(≥2/3 models pass sanity and project). The **matched-entailment control bites cleanly** — entail-survival
is 0.17 / 0.17 / 0.00, so the gap is *not* a yes-bias (a model that just said YES to plausible
propositions would show E surviving too, landing in FLAT; none did).

**Per frame** (P-endorse / E-endorse):

| frame | A (P/E) | B (P/E) | C (P/E) |
|-------|---------|---------|---------|
| plain | 0.92 / 1.00 | 0.92 / 0.92 | 1.00 / 1.00 |
| negation | **1.00 / 0.00** | 0.58 / 0.00 | **1.00 / 0.00** |
| question | 1.00 / 0.42 | 0.83 / 0.42 | 1.00 / 0.00 |
| conditional | **0.42 / 0.08** | **0.17 / 0.08** | **0.17 / 0.00** |

- **Negation** is the cleanest cell: claude and gemini give the textbook pattern **P=YES, E=NO on
  all 12 items**; gpt is weaker (P 0.58) but still cancels E completely.
- **Question**: P projects strongly (0.83–1.00) but the matched entailment *also* survives more here
  (E 0.42 for claude and gpt) — expected, since a question does not assert ¬E, so E is merely "open"
  and some items draw YES/UNCLEAR.
- **Conditional**: projection **collapses for every model** — P-survival 0.42 / 0.17 / 0.17, at or
  near the entailment leg. Reading the raw answers, the models overwhelmingly return **UNCLEAR** (or
  NO) to "does the antecedent's presupposition follow?", treating the whole conditional as merely
  hypothetical and declining to extract the antecedent's backgrounded content — a behavioral
  **projection failure** exactly where the literature flags projection as hardest and most defeasible
  ([source](../../base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md), §1.3
  "Presuppositions typically project, but often do not").

**Per trigger family** (pooled across 3 models, cancelling frames; 27 obs/leg — *descriptive*, n thin):

| family | P-survival | E-survival | gap |
|--------|-----------|-----------|-----|
| factive (realize/discover/know) | 0.63 | 0.26 | +0.37 |
| aspectual (stop/continue/resume) | 0.81 | 0.11 | +0.70 |
| definite description | 0.70 | 0.04 | +0.67 |
| it-cleft | 0.59 | 0.04 | +0.56 |

Every family shows a positive gap, so the effect is **not** an artifact of one trigger type or of
the families with the largest surface-plausibility asymmetry (the pre-run critic's flagged confound
F). The factive family has the smallest gap — its presupposition survives least (0.63) — while the
aspectual family gives the widest separation.

## Interpretation (calibrated)

- **What the data support.** Within claude and gemini, and directionally within gpt, the presupposition
  behaves differently from a matched entailment under embedding: it survives negation and (mostly)
  questions where the entailment is cancelled. This is a **within-model behavioral reproduction of the
  projection asymmetry** the semantics literature documents — read off forced-choice endorsements, at
  `internal-contrast-only` strength.
- **What the data do NOT support.** (i) No human comparison — the models are not shown to match human
  projection judgments (none were measured). (ii) No mechanism claim — endorsing a projected inference
  is text-consistent-with projection, not evidence the model *computes* a presupposition/assertion
  split. (iii) The **conditional-frame collapse means the panel does NOT project uniformly**; a
  strong "LLMs project presuppositions" reading would over-claim. The honest statement is
  *projection under negation/question, projection failure under the conditional antecedent*.
- **gpt-5.4-mini** is the informative near-miss: same direction, weaker magnitude (its negation-frame
  P is only 0.58), so the panel is not uniform even on the frames where projection is strongest.

## Gates

- **Pre-run critic (independent fresh agent): GO** — 12/12 items linguistically sound (P projects, E
  cancels, frames grammatical, no consequent leaks P/E); verdict map symmetric and not rigged (a
  yes-bias lands in FLAT, correctly denied projection); SEP quotes verbatim; scope/anchor discipline
  correct. Three advisories (report per-family + per-frame tables; report unparsed counts; keep
  FLAT-vs-MIXED honest) — all carried into this page.
- **Post-run verifier (independent fresh agent): REPRODUCED** — every per-model, per-frame, and
  per-family figure re-derived from `raw/*.json` with independent scoring; verdict PROJECTION and the
  conditional-collapse confirmed; billed cost re-summed; 0 missing / 0 unparsed. (See wind-up note.)

## What this feeds

Discharges the "run a projection probe" branch of
[`open-question/presupposition-projection-corner`](../open-questions/presupposition-projection-corner.md)
and tests [`conjecture/presupposition-projection-vs-entailment`](../conjectures/presupposition-projection-vs-entailment.md)
(advance `proposed → tested`). Opens a sharp follow-up: **why does the conditional antecedent
break projection when negation does not?** — a within-panel frame-asymmetry that a later session can
probe (e.g. whether an explicit "assume the whole sentence is true" framing rescues conditional
projection, or whether it is a genuine limit of the text-trained projection behavior).
