---
type: result
id: projection-trigger-inventory-family-decomposition-v1
title: "Per-family decomposition of the s160 MIXED verdict: the weaker pooled gap is driven by ONE family (manner adverbs, zero within-model asymmetry in all three models); temporal / only / quantifier all show clean positive gaps panel-wide"
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
    target: result/projection-trigger-inventory-v1
  - rel: depends-on
    target: result/projection-trigger-inventory-v1
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: essay/projection-defeasible-by-frame
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: per-family decomposition of the s160 projection trigger-inventory MIXED verdict

A **pure re-analysis** of the already-committed session-160 raw
([`result/projection-trigger-inventory-v1`](projection-trigger-inventory-v1.md), verdict **MIXED**).
No new model calls, **no spend ($0)**, no probe — this page recomputes the same pre-registered
metrics (`presup_survival`, `entail_survival`, `projection_gap`) *split by trigger family*, using the
**byte-identical scoring path** (the `parse_endorse` regex `\b(yes|no|unclear)\b` from
[`analyze.py`](../../../experiments/runs/2026-07-01-projection-trigger-inventory/analyze.py),
`endorsed == YES`). It answers the question the s160 "Honest bounds" section explicitly deferred:
*"the per-family split is in `results.json`/raw for a later session to decompose."* Raw:
[`experiments/runs/2026-07-01-projection-trigger-inventory/raw/{A,B,C}.json`](../../../experiments/runs/2026-07-01-projection-trigger-inventory/README.md).

**One-line finding.** The weaker pooled gap that pushed s160 to MIXED is driven by **one of the four
families — manner adverbs — which shows zero within-model projection asymmetry (gap +0.00) in all
three models**; the other three families (temporal / only / quantifier) show **clean positive gaps in
every model (+0.33 to +0.67)**. The pre-run critic's flag was **half-right**: manner is indeed the
drag, but **"only" projects fine** (it was flagged as theoretically harder yet shows a clean
+0.33 / +0.33 / +0.44 gap).

## Scope — LOAD-BEARING (read before citing)

**Within-model contrast only; no human comparison.** This inherits the scope of the s160 result
verbatim: the signal is *the presupposition leg survives more than the matched-entailment leg, within
the same model* — **not** *the model matches human projection judgments*. No human projectivity
baseline is claimed, measured, or needed; the page reads endorsement of an inference under embedding
off forced-choice answers (text-consistency is not mechanism).

**Anchor: `internal-contrast-only`, inherited.** This decomposition reuses the byte-identical scoring
path of the s160 result on the byte-identical raw — same data, same measurement, no new data. Its
`internal-contrast-only` status is **inherited** from the s160 result's anchor, ratified this session
under
[`decisions/resolved/projection-trigger-inventory-internal-contrast-anchor`](../../decisions/resolved/projection-trigger-inventory-internal-contrast-anchor.md)
(ADOPT A). Because there is no new data and no human comparison, this page adds no fresh
anchor obligation beyond the parent's. `contingent-on: []`.

**No-retuning guardrail — CRITICAL.** This decomposition is **descriptive**. The frozen pooled
**MIXED** verdict of s160 **stands, untouched**. This page does **not** re-run `analyze.py` with
manner excluded, does **not** compute a "corrected" pooled verdict, and does **not** claim "actually
it's PROJECTION if you drop manner." Excluding a family and re-reading the verdict would be exactly
the operationalization-tuning the protocol forbids (`PROTOCOL.md §8`; the failure mode "quietly tuning
until a null becomes positive"). The decomposition **locates where the weakness lives**; it does not
move the yardstick. The manner null is itself a legitimate finding, not a defect to be corrected away:
a theoretically-flagged weak trigger behaves as non-projective in this instrument, and its inclusion —
by design, pre-registered — is what pulled the pooled gap down.

## Numbers (computed directly from raw; every number reproduced this session)

**Per family × per model** (rates; cancelling = negation + question + conditional pooled;
gap = presup_survival − entail_survival):

| family | model | plain P / E | presup_survival | entail_survival | projection_gap |
|--------|-------|-------------|-----------------|-----------------|----------------|
| **temporal** | A claude-sonnet-4.6 | 1.00 / 1.00 | 0.67 | 0.11 | **+0.56** |
| | B gpt-5.4-mini | 1.00 / 1.00 | 0.44 | 0.00 | **+0.44** |
| | C gemini-3.5-flash | 1.00 / 1.00 | 0.67 | 0.00 | **+0.67** |
| **manner** | A claude-sonnet-4.6 | 1.00 / 1.00 | 0.56 | 0.56 | **+0.00** |
| | B gpt-5.4-mini | 1.00 / 1.00 | 0.44 | 0.44 | **+0.00** |
| | C gemini-3.5-flash | 1.00 / 1.00 | 0.11 | 0.11 | **+0.00** |
| **only** | A claude-sonnet-4.6 | 1.00 / 1.00 | 0.67 | 0.33 | **+0.33** |
| | B gpt-5.4-mini | 1.00 / 1.00 | 0.67 | 0.33 | **+0.33** |
| | C gemini-3.5-flash | 1.00 / 1.00 | 0.44 | 0.00 | **+0.44** |
| **quantifier** | A claude-sonnet-4.6 | 1.00 / 1.00 | 0.78 | 0.22 | **+0.56** |
| | B gpt-5.4-mini | 1.00 / 1.00 | 0.78 | 0.33 | **+0.45** |
| | C gemini-3.5-flash | 1.00 / 1.00 | 0.67 | 0.00 | **+0.67** |

Plain-frame sanity holds at 1.00 for both legs in every family × model cell. The three
non-manner families give a positive gap in **every** one of their 9 model cells (+0.33 to +0.67);
manner gives **+0.00 in all three**. (One rounding note: the B-quantifier gap is **+0.45** as computed
here — presup_survival 0.778 − entail_survival 0.333 — versus a stated +0.44 in the assignment brief;
the 0.01 is pure display rounding of the same underlying counts. All other cells match exactly.)

## The manner mechanism — P and E collapse *together*

Manner is the only family where the two legs **track each other frame-by-frame**, so the gap is ≈ 0 at
every frame, not just pooled. Under **negation**, manner P and E **both collapse to 0.00** in all three
models. Per-frame P / E for manner:

| model | plain | negation | question | conditional |
|-------|-------|----------|----------|-------------|
| A claude-sonnet-4.6 | 1.00 / 1.00 | **0.00 / 0.00** | 1.00 / 1.00 | 0.67 / 0.67 |
| B gpt-5.4-mini | 1.00 / 1.00 | **0.00 / 0.00** | 1.00 / 1.00 | 0.33 / 0.33 |
| C gemini-3.5-flash | 1.00 / 1.00 | **0.00 / 0.00** | 0.33 / 0.33 | 0.00 / 0.00 |

In every manner cell outside the plain frame, P-endorse equals E-endorse. This is the disclosed
scope-ambiguity of manner adverbs under negation that the
[`PREREG.md`](../../../experiments/runs/2026-07-01-projection-trigger-inventory/PREREG.md)
flagged pre-run ("Known weak pairs"): negating a manner adverb ("Owen didn't reluctantly sign the
contract") does not clearly presuppose the underlying action occurred — the projecting reading ("he
signed, just not reluctantly") competes with a "he didn't sign at all" reading — so the manner adverb
is **not behaving as a projective trigger in this instrument**. The P and E legs are effectively
indistinguishable under embedding for manner: there is no within-model asymmetry to read.

By contrast, for temporal / only / quantifier the **negation frame gives the clean textbook
asymmetry** — P endorsed while E cancels to 0.00 — in every model (see the per-family gaps above),
which is where their positive pooled gaps come from.

## The pre-run critic was half-right

The [`PREREG.md`](../../../experiments/runs/2026-07-01-projection-trigger-inventory/PREREG.md)
"Known weak pairs" note flagged **two** families as theoretically harder / weaker-projecting: manner
(scope-ambiguous under negation) **and** "only" (contested prejacent status). The decomposition
adjudicates that flag:

- **Manner: flag confirmed.** Zero within-model asymmetry in all three models; the collapse-together
  under negation is exactly the predicted failure mode. Manner is the drag on the pooled gap.
- **"Only": flag not borne out.** Despite the theoretical worry, "only" shows a **clean positive gap
  in every model** (+0.33 / +0.33 / +0.44), driven by a clean negation asymmetry (P endorsed, E
  cancels to 0.00 in all three). The prejacent projected fine in this instrument.

So one of the two flagged-weak families (manner) is genuinely non-projective here and the other
(only) projects cleanly — the critic located the *drag* correctly but over-predicted its extent.

## Reading it

- **The s158 projection *direction* generalizes cleanly to three of the four new families,
  panel-wide.** Temporal, only, and quantifier each give a positive within-model gap in every one of
  their model cells (+0.33 to +0.67). Read as *description*, the s158 generalization is **cleaner than
  the pooled MIXED suggested** for these three families — but this is a description of *where* the
  signal lives, not a re-tuned verdict. The frozen MIXED stands (see the no-retuning guardrail).

- **The fourth family (manner) is a genuinely weaker / non-projective trigger in this instrument, not
  a model failure.** All three models treat P and E alike for manner; a triple non-asymmetry that
  tracks the pre-registered scope-ambiguity is best read as a property of the *trigger under this
  operationalization*, not as three independent model deficits. Its inclusion — pre-registered, by
  design — is what pulled the pooled gap down to the MIXED region. That is an honest qualification of
  the generalization, not a defect.

- **Tie to the frame-shaped-defeasibility reading.** The
  [`essay/projection-defeasible-by-frame`](../essays/projection-defeasible-by-frame.md) argues that
  projection here is governed by the *frame*, not the *item or trigger* — the conditional-antecedent
  collapse is frame-shaped and trigger-general. This decomposition adds a **trigger-side
  qualification** the essay should note: while the *frame* governs survival for the projective
  families, one trigger *family* — manner — is simply not projective in this instrument at all (its
  two legs move together at every frame). So the essay's "frame, not trigger" reading holds *within*
  the set of triggers that project, but there is at least one trigger family here that does not enter
  the frame-shaped regime because it shows no P/E asymmetry to begin with. This sharpens rather than
  contradicts the essay: the frame governs survival *given* a projective trigger; manner shows that
  not every source-listed trigger is projective under this behavioral instrument.

## Honest bounds

- **Behavioral, within-model, no human comparison** (see Scope); `anchor: internal-contrast-only`
  inherited from the s160 result. Makes no claim any model *computes* projection.
- **Descriptive re-analysis only; the frozen MIXED verdict is untouched.** No family is excluded to
  produce a "corrected" verdict (no-retuning guardrail).
- **Very small per-cell Ns.** Each per-frame per-family P (or E) cell is **n = 3 items**; each
  per-family pooled survival is **n = 9** (3 items × 3 cancelling frames). Rates move in steps of 1/3
  (per frame) or 1/9 (pooled). Direction-of-effect only; no magnitude precision is claimed at this
  granularity, and the manner "+0.00" is a genuine leg-equality across those small cells, not a
  precise zero.
- **n = 3 models, three 2026 commercial models, project-authored synthetic items.** No coverage claim.
- **$0, pure re-analysis of committed raw.** No API calls, no budget spend; the numbers reproduce the
  s160 raw under the identical scoring path.
