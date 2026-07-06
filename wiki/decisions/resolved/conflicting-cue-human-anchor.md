---
id: conflicting-cue-human-anchor
title: Does the off-ceiling conflicting-cue result need a human-rated anchor, and which one?
status: resolved
opened: 2026-05-29
opened-by: orchestrator
resolved: 2026-05-31
resolved-by: tom
resolution: A
contingent-artifacts:
  - result/argument-structure-coercion-v2
  - result/caused-motion-near-miss-v2c
  - result/coercion-implicit-cue-v2b
  - result/coercion-sense-modulation-v1
  - result/comparative-correlative-covariation-v2
  - result/comparative-correlative-covariation-v3
  - result/conative-cancel-direction-v2
  - note/cross-axis-lexical-constructional-ordering-v1
---

# Decision: human anchor for the conflicting-cue coercion result

## RESOLUTION (2026-05-31, Tom — Option A)

**Ratified: leave the internal-contrast-only results as internal-contrast-only.** Tom's
ruling this round (verbatim intent): "leave the internal-contrast-only results
(argument-structure-coercion-v2 and the off-ceiling/bridge results) as
internal-contrast-only … they make no human-comparison claim, so this closes the gate
without changing any finding."

This **fixes the yardstick, not any result**: no finding changes; the off-ceiling /
bridge / cross-axis results stand exactly as written, drawing their force from the
within-model `canonical`→`cue` (and ordering / direction-of-effect) contrast. No human
baseline is claimed or invented for the conflicting-cue / coercion-resisting / embedded /
near-miss / bridge arms.

**Mechanical consequence (applied this commit):** the eight contingent results below have
their `contingent-on: conflicting-cue-human-anchor` removed and their anchor field promoted
from the ambiguous `anchor: pending` to the explicit terminal state
**`anchor: internal-contrast-only`** — a ratified declaration that the result makes no
human-comparison claim and so requires no resource anchor. `tools/senselint.py`
check 4 was extended to recognize this terminal state (it previously accepted only
`anchor: pending` + an open decision); the convention is documented in [`CLAUDE.md`](../../../CLAUDE.md). If a
*human-comparison* claim on any of these arms is ever wanted, that is a **new** anchor
question (Option B below) to be opened fresh, not this one.

Promoted results: [`result/argument-structure-coercion-v2`](../../findings/results/argument-structure-coercion-v2.md),
[`result/caused-motion-near-miss-v2c`](../../findings/results/caused-motion-near-miss-v2c.md),
[`result/coercion-implicit-cue-v2b`](../../findings/results/coercion-implicit-cue-v2b.md),
[`result/coercion-sense-modulation-v1`](../../findings/results/coercion-sense-modulation-v1.md),
[`result/comparative-correlative-covariation-v2`](../../findings/results/comparative-correlative-covariation-v2.md),
[`result/comparative-correlative-covariation-v3`](../../findings/results/comparative-correlative-covariation-v3.md),
[`result/conative-cancel-direction-v2`](../../findings/results/conative-cancel-direction-v2.md),
[`note/cross-axis-lexical-constructional-ordering-v1`](../../findings/notes/cross-axis-lexical-constructional-ordering-v1.md).

---

# Decision: human anchor for the conflicting-cue coercion result *(original, for the record)*

## Why this exists (low-priority, mechanical anchor-tracking)

[`result/argument-structure-coercion-v2`](../../findings/results/argument-structure-coercion-v2.md) ran the off-ceiling conflicting-cue probe **internal-contrast-only** — exactly as the ratified [`decisions/resolved/cc-v2-difficulty-operationalization`](cc-v2-difficulty-operationalization.md) specified for the harder arms ("run internal-contrast-only with the human clause marked pending; queue a human-rated harder anchor in `wanted.md` rather than blocking"). The Scivetti CxNLI subsets contain **no** conflicting-cue / coercion-resisting items, so there is no in-repo human norm for these items, and the result makes **no** human-comparison claim — its force is the within-model `canonical`→`cue` contrast.

This page exists to **track that pending anchor** (and to satisfy the anchor-discipline gate: an `anchor: pending` result must name the open anchor question it depends on). It is **low-priority**: the result's claim (the v1 add-direction ceilings are cue-sensitive, not a brittle template) stands on the internal contrast and does **not** require a human anchor to be valid as stated.

## The question

If the project later wants a *human-comparison* claim on conflicting-cue coercions — "humans withhold the construction's inference under an explicit cue at rate X; models match/differ" — it needs a human-rated anchor on such items. None exists in-repo.

## Options

- **A — Leave internal-contrast-only (provisional default).** The conflicting-cue reading is near-trivial for humans (an explicit denial "…but it never moved" is obviously decisive), so a rated human baseline adds little; keep the result internal-contrast-only and do not fetch/collect anything. The result stays `proposed`, anchor `pending`, no human claim made.
- **B — Queue a human-rated conflicting-cue / coercion-resisting set in `wanted.md`** (existing released ratings only — no new human-subject collection, charter §8) if/when a human-comparison claim is actually wanted. Promote only then.
- **C — Build the matched off-ceiling cancel-direction (harder conative) probe first** (the add/cancel asymmetry de-confounding the design calls for), and decide the anchor question for the pair together.

## Provisional default

**Option A** — the result is internal-contrast-only by ratified design and needs no human anchor for its stated (internal) claim; this page just records the gap. Revisit only if a human-comparison claim on conflicting-cue items is later wanted (then Option B). Tom: a one-liner ("A stands" / "queue B" / "do C first") is enough; this is **not** blocking.
