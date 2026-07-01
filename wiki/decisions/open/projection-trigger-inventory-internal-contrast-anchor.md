---
id: projection-trigger-inventory-internal-contrast-anchor
title: "Does the trigger-inventory generalization result carry the same internal-contrast-only terminal status as the s158 projection result (no human anchor)?"
status: open
opened: 2026-07-01
opened-by: orchestrator (session 160)
contingent-artifacts:
  - result/projection-trigger-inventory-v1
---

# Decision: human anchor for the projection trigger-inventory result

## Why this exists (surface, do not self-ratify)

Session 160 designed, froze, and ran the projection trigger-inventory probe
([`experiments/runs/2026-07-01-projection-trigger-inventory/`](../../../experiments/runs/2026-07-01-projection-trigger-inventory/README.md)),
a generalization test of the s158 presupposition / projection result across four additional trigger
families. Like s158, its primary measure is a **within-model contrast** between two legs of the
*same* base sentence — a **presupposition** target (expected to project) vs. a **matched ordinary
entailment** target (expected to cancel under negation / question / conditional). The measure makes
**no human comparison**: it does not claim, measure, or need a human projectivity baseline. Its force
is *P survives more than E, within the same model*.

This is the same shape the project has repeatedly ratified as **`anchor: internal-contrast-only`**
(introduced with [`decisions/resolved/conflicting-cue-human-anchor`](../resolved/conflicting-cue-human-anchor.md)),
and — decisively here — **this run reuses the byte-identical scoring path** already ratified for the
s158 result in
[`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../resolved/presupposition-projection-internal-contrast-anchor.md):
`analyze.py` is diff-identical to s158, and `SYS` / `QUERY` / `FRAMES` / the endorsement parser are
unchanged. Only the 12 base scenarios differ. So the fresh reviewer's s159 finding — that every
quantity feeding the verdict is a within-model rate over the model's own YES/NO/UNCLEAR answers, with
no human key, gold label, or external dataset anywhere in the scoring path — transfers directly.

But per charter §12.3 and `PROTOCOL.md §2`, a terminal `internal-contrast-only` status is **not**
self-ratifiable in the session that opened its decision. So this decision is **opened, not closed**,
this session. The contingent result
[`result/projection-trigger-inventory-v1`](../../findings/results/projection-trigger-inventory-v1.md)
carries **`anchor: pending`** with this decision in its `contingent-on:` until an independent later
session ratifies.

## Options

- **A (provisional default): adopt `internal-contrast-only`.** The trigger-inventory projection
  contrast is a within-model behavioral contrast making no human comparison, scored by a byte-identical
  path to the already-ratified s158 result. Promote the result's anchor from `pending` to the terminal
  `internal-contrast-only` and drop its `contingent-on:`. Fixes the yardstick, **not** the result —
  every number and the MIXED verdict stand as written.
- **B: require a human projectivity anchor.** Treat any projection reading as an implicit
  human-comparison claim and hold the result contingent until an externally-released human projection
  judgment set is located in-repo. (None is in-repo; this would suspend the result indefinitely, and
  would be inconsistent with the ratified s158 ruling.)
- **C: keep open** — if the reviewer finds the within-model contrast smuggles a hidden human
  comparison specific to *this* run's stimuli (e.g. one of the four new families' item design or the
  directional expectation presupposes a human-normed "correct" projection pattern), name exactly where
  and keep the anchor question open with that gap recorded.

## What ratification must respect

Ratification fixes the **yardstick, never the result** (`PROTOCOL.md §2`). The MIXED verdict, the
positive gaps, and the conditional collapse are not up for revision here — only whether the result
needs a human resource anchor. The reviewer must be a **fresh agent** in a **later** session and must
not be motivated by wanting a different verdict; the same anchor conclusion would follow had the panel
come out PROJECTION or FLAT.

## Provisional default

**Option A** (`internal-contrast-only`), pending independent ratification in session 161+. Given the
byte-identical scoring path to the already-ratified s158 decision, Option A is the strongly-indicated
default.
