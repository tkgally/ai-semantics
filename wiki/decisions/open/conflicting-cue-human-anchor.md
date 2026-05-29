---
id: conflicting-cue-human-anchor
title: Does the off-ceiling conflicting-cue result need a human-rated anchor, and which one?
status: open
opened: 2026-05-29
opened-by: orchestrator
contingent-artifacts:
  - result/argument-structure-coercion-v2
---

# Decision: human anchor for the conflicting-cue coercion result

## Why this exists (low-priority, mechanical anchor-tracking)

[`result/argument-structure-coercion-v2`](../../findings/results/argument-structure-coercion-v2.md) ran the off-ceiling conflicting-cue probe **internal-contrast-only** — exactly as the ratified [`decisions/resolved/cc-v2-difficulty-operationalization`](../resolved/cc-v2-difficulty-operationalization.md) specified for the harder arms ("run internal-contrast-only with the human clause marked pending; queue a human-rated harder anchor in `wanted.md` rather than blocking"). The Scivetti CxNLI subsets contain **no** conflicting-cue / coercion-resisting items, so there is no in-repo human norm for these items, and the result makes **no** human-comparison claim — its force is the within-model `canonical`→`cue` contrast.

This page exists to **track that pending anchor** (and to satisfy the anchor-discipline gate: an `anchor: pending` result must name the open anchor question it depends on). It is **low-priority**: the result's claim (the v1 add-direction ceilings are cue-sensitive, not a brittle template) stands on the internal contrast and does **not** require a human anchor to be valid as stated.

## The question

If the project later wants a *human-comparison* claim on conflicting-cue coercions — "humans withhold the construction's inference under an explicit cue at rate X; models match/differ" — it needs a human-rated anchor on such items. None exists in-repo.

## Options

- **A — Leave internal-contrast-only (provisional default).** The conflicting-cue reading is near-trivial for humans (an explicit denial "…but it never moved" is obviously decisive), so a rated human baseline adds little; keep the result internal-contrast-only and do not fetch/collect anything. The result stays `proposed`, anchor `pending`, no human claim made.
- **B — Queue a human-rated conflicting-cue / coercion-resisting set in `wanted.md`** (existing released ratings only — no new human-subject collection, charter §8) if/when a human-comparison claim is actually wanted. Promote only then.
- **C — Build the matched off-ceiling cancel-direction (harder conative) probe first** (the add/cancel asymmetry de-confounding the design calls for), and decide the anchor question for the pair together.

## Provisional default

**Option A** — the result is internal-contrast-only by ratified design and needs no human anchor for its stated (internal) claim; this page just records the gap. Revisit only if a human-comparison claim on conflicting-cue items is later wanted (then Option B). Tom: a one-liner ("A stands" / "queue B" / "do C first") is enough; this is **not** blocking.
