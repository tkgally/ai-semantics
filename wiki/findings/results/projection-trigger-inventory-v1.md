---
type: result
id: projection-trigger-inventory-v1
title: "The within-model projection asymmetry GENERALIZES in direction to four more trigger families — but clears the pre-registered bar for only 1/3 (verdict MIXED); the conditional-frame collapse replicates on the new triggers"
meaning-senses:
  - inferential
  - distributional
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-01
updated: 2026-07-01
links:
  - rel: refines
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: conjecture/presupposition-projection-vs-entailment
  - rel: depends-on
    target: essay/projection-defeasible-by-frame
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: the projection trigger-inventory probe v1 (generalization test)

A **generalization test** of the session-158 presupposition / projection result
([`result/presupposition-projection-v1`](presupposition-projection-v1.md), verdict PROJECTION 2/3).
That probe measured, within a model, whether a base sentence's **presupposition** survives
entailment-cancelling embedding (negation / question / conditional antecedent) *more than* a
**matched ordinary entailment** — the semantics literature's "hallmark of presuppositions"
([`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md),
§1.2) — across four trigger families (factive / aspectual / definite / cleft). This run asks the
**same question with the byte-identical instrument** for **four ADDITIONAL trigger families the SEP
source names** (temporal-clause "before/after/since" / manner-adverb / "only"-focus / quantifier
"both/each"): does the projection asymmetry hold across a wider slice of the trigger inventory? Run
record:
[`experiments/runs/2026-07-01-projection-trigger-inventory/`](../../../experiments/runs/2026-07-01-projection-trigger-inventory/README.md);
frozen [`PREREG.md`](../../../experiments/runs/2026-07-01-projection-trigger-inventory/PREREG.md),
manifest sha `d0aa515e…`.

**One-line finding.** The pre-registered verdict is **MIXED**. All three models pass the plain-frame
sanity floor and show a **positive projection gap** — the presupposition survives more than the
matched entailment in *every* model (gaps **+0.36 / +0.30 / +0.44**) — so the projection asymmetry
**generalizes in direction** to the new trigger families. But only **1 of 3** (claude-sonnet-4.6)
clears the frozen projection bar (presup-survival ≥ 0.60 **and** gap ≥ 0.30); gpt-5.4-mini
(survival 0.58) and gemini-3.5-flash (survival 0.47) miss on **pooled survival** despite large
positive gaps, so no ≥2 majority forms for either pole. Two frame effects, both visible per-frame,
explain the miss and are the more interesting content: **(1)** under **negation** the signature is
clean and large in all three (P endorsed 0.67–0.75 while the matched entailment cancels to **0.00**);
**(2)** the **conditional-antecedent frame collapses** presupposition survival for all three
(P = 0.25 / 0.17 / 0.00) — the same s158/s159 collapse, now **replicated on four brand-new trigger
families** — and the **question** frame cancels the entailment only weakly for two models
(E = 0.75 / 0.75 / 0.08), compressing the gap. So relative to s158, the projection reading is
**weaker on this wider trigger slice**: the direction holds panel-wide, the magnitude clears the bar
for one model.

## Scope — LOAD-BEARING (read before citing)

**Within-model contrast only; no human comparison.** The signal is *the presupposition leg survives
more than the matched-entailment leg, within the same model* — **not** *the model matches human
projection judgments*. No human projectivity baseline is claimed, measured, or needed. The result
does **not** certify that a model *represents* presupposition-vs-assertion semantically; it reads
endorsement of an inference under embedding off forced-choice answers (text-consistency is not
mechanism).

**Anchor is `anchor: internal-contrast-only`** (terminal), ratified by an independent fresh-agent
adversarial review in **session 161** —
[`decisions/resolved/projection-trigger-inventory-internal-contrast-anchor`](../../decisions/resolved/projection-trigger-inventory-internal-contrast-anchor.md)
(ADOPT A). This run **reuses the byte-identical scoring path** (`analyze.py` diff-identical to s158,
verified by the reviewer at diff=0; `SYS` / `QUERY` / `FRAMES` / thresholds unchanged) as the
already-ratified
[`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../decisions/resolved/presupposition-projection-internal-contrast-anchor.md),
so the same `internal-contrast-only` reasoning transferred: every quantity feeding the verdict is a
within-model rate over the model's own YES/NO/UNCLEAR answers, with no human key anywhere in the
scoring path. Ratification fixed the **yardstick, never the result** — every number and the MIXED
verdict below stand unchanged.

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A),
  `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C), as subjects. Temperature 0; text-only,
  single-turn, zero-shot; gemini `reasoning={"effort":"minimal"}`. A neutral system prompt
  ("You are a careful reader…") that never mentions presupposition, projection, or the right answer —
  byte-identical to s158.
- **Items.** 12 project-authored matched base scenarios across **4 NEW trigger families**
  (temporal-clause / manner-adverb / "only"-focus / quantifier; 3 each) × **2 targets**
  (presupposition P vs. matched entailment E) × **4 frames** (plain / negation / question /
  conditional) = **96 item-conditions** per model, 288 calls total. Each item is one forced choice —
  *"does it follow that: &lt;target&gt;? YES / NO / UNCLEAR."* `endorsed` == answer parses to YES.
  The four families are the ones the SEP source lists beyond s158's set (§1.1: "temporal clauses
  ('before', 'after', 'since'), manner adverbs, … quantifiers, … and intonation (focus, contrast)").
- **Cost.** **$0.0490 billed** (`usage.cost`-summed: claude $0.0293 / gpt $0.0082 / gemini $0.0114),
  0 missing cost, **0 unparsed** answers. Far under the $2.50 single-run flag; UTC-2026-07-01 day
  total after this run **$0.1528** of $5.00.

## Numbers (from `results.json`; independently reproduced)

**Per model** (rates; cancelling = negation + question + conditional pooled):

| model | plain P / E | presup-survival | entail-survival | projection-gap | sanity | projection? |
|-------|-------------|-----------------|-----------------|----------------|--------|-------------|
| A claude-sonnet-4.6 | 1.00 / 1.00 | **0.67** | 0.31 | **+0.36** | ✓ | **yes** |
| B gpt-5.4-mini | 1.00 / 1.00 | 0.58 | 0.28 | +0.30 | ✓ | no (survival &lt; 0.60; not flat) |
| C gemini-3.5-flash | 1.00 / 1.00 | 0.47 | 0.03 | **+0.44** | ✓ | no (survival &lt; 0.60; not flat) |

**Per frame** (P-endorse / E-endorse):

| model | plain | negation | question | conditional |
|-------|-------|----------|----------|-------------|
| A | 1.00 / 1.00 | 0.75 / 0.00 | 1.00 / 0.75 | 0.25 / 0.17 |
| B | 1.00 / 1.00 | 0.67 / 0.00 | 0.92 / 0.75 | 0.17 / 0.08 |
| C | 1.00 / 1.00 | 0.75 / 0.00 | 0.67 / 0.08 | 0.00 / 0.00 |

**Verdict** (frozen thresholds SANITY 0.75 / SURVIVE 0.60 / GAP 0.30 / FLATBAND 0.15, **unchanged
from s158**): projection = {A}, flat = {}, sanity-failed = {} → no ≥2 majority → **MIXED**.

## Reading it

- **The projection direction generalizes; the pre-registered magnitude does not (fully).** Every
  model separates P from its matched E in the expected direction on the new triggers — the negation
  frame alone gives a clean, large asymmetry in all three (negation-only P-vs-E gap **+0.75 / +0.67 /
  +0.75**, with E cancelling to **0.00** for every model). So the s158 *direction* replicates across a
  wider trigger slice. What does **not** replicate is the panel-wide clearance of the bar: s158's
  gaps were +0.64 / +0.36 / +0.72 (2/3 over the floor); here they are +0.36 / +0.30 / +0.44
  (1/3 over the floor). On these families the effect is **smaller**, so the frozen 0.60 survival
  floor now separates the panel — an honest qualification, not a re-tuning (the floor is s158's).

- **The conditional collapse is trigger-general.** The presupposition fails to survive the
  conditional antecedent in *every* model on *every* new family (conditional-frame P = 0.25 / 0.17 /
  0.00), exactly as in s158 and as the s159 rescue probe found robust. That the collapse reproduces
  on four trigger families it was never tuned on **strengthens** the
  [`essay/projection-defeasible-by-frame`](../essays/projection-defeasible-by-frame.md) reading that
  projection here is **frame-shaped, not item- or trigger-scattered**: the frame, not the trigger,
  governs whether the presupposition survives.

- **The question frame is a weak canceller — and that is a second, distinct compressor.** For A and B
  the *entailment* is endorsed under a polar question 75% of the time, so the question frame fails to
  cancel E and the P-vs-E gap shrinks there for reasons unrelated to the conditional collapse. Only C
  cancels E cleanly under the question. This is a new wrinkle relative to s158's headline and part of
  why pooled survival lands where it does.

- **Not a yes-bias.** E-under-negation is 0.00 for all three and overall YES rates are moderate
  (0.62 / 0.57 / 0.44); the P-survival is a genuine within-model asymmetry, not a blanket-YES
  artifact (a yes-to-everything model lands in FLAT, not projection). Verified independently by the
  post-run reviewer.

## Relation to the conjecture and the corner

The run is a further test of
[`conjecture/presupposition-projection-vs-entailment`](../conjectures/presupposition-projection-vs-entailment.md)
(status `tested`): it **refines** the conjecture rather than simply confirming it — the within-model
projection asymmetry it bets on holds *in direction* across eight trigger families now, but its
magnitude is **trigger-family-dependent** and clears the pre-registered bar panel-wide only on the
s158 families, not on the harder/broader ones here. The corner
([`open-question/presupposition-projection-corner`](../open-questions/presupposition-projection-corner.md))
is now worked across **three probes** (s158 projection, s159 conditional-rescue, s160 trigger-widening).

## Honest bounds

- **Behavioral, within-model, no human comparison** (see Scope). `anchor: internal-contrast-only`
  (ratified session 161); makes no claim a model *computes* projection.
- **Two families are theoretically harder triggers.** Manner-adverb presuppositions are
  scope-ambiguous under negation, and "only"'s prejacent status is contested; the pre-run critic
  passed both as valid-but-weaker (disclosed in [`PREREG.md`](../../../experiments/runs/2026-07-01-projection-trigger-inventory/PREREG.md)
  §"Known weak pairs"). Part of the smaller gap may be these harder triggers rather than a general
  weakening — the per-family split is in `results.json`/raw for a later session to decompose.
- **Small Ns, n=3 models, three 2026 commercial models, project-authored synthetic items.** No
  coverage claim; direction-of-effect only, scoped to these families/frames.
- **MIXED is a real split, not a null.** The gap is positive and same-signed in all three; the
  verdict is MIXED because the *survival floor* separates the panel, not because the legs are flat.
