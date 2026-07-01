---
id: presupposition-projection-internal-contrast-anchor
title: "Is the presupposition-vs-matched-entailment projection contrast a legitimate internal-contrast-only terminal status (no human anchor)?"
status: open
opened: 2026-07-01
opened-by: orchestrator (session 158)
contingent-artifacts:
  - conjecture/presupposition-projection-vs-entailment
  - result/presupposition-projection-v1
---

# Decision: human anchor for the presupposition / projection result

## Why this exists (surface, do not self-ratify)

Session 158 designed, froze, and ran the presupposition / projection probe
([`experiments/runs/2026-07-01-presupposition-projection/`](../../../experiments/runs/2026-07-01-presupposition-projection/README.md)).
Its primary measure is a **within-model contrast** between two legs of the *same* base sentence — a
**presupposition** target (expected to project, i.e. survive negation / question / conditional
embedding) vs. a **matched ordinary entailment** target (expected to be cancelled under those
frames). The measure makes **no human comparison**: it does not claim, measure, or need a human
projectivity / projection-judgment baseline. Its force is *P survives more than E, within the same
model*.

This is exactly the shape the project has repeatedly ratified as
**`anchor: internal-contrast-only`** — the terminal declaration that a result makes no
human-comparison claim and so requires no resource anchor (introduced with
[`decisions/resolved/conflicting-cue-human-anchor`](../resolved/conflicting-cue-human-anchor.md),
ratified 2026-05-31; the same status carried by the indexicality corner's results, e.g.
[`result/tool-origo-deictic-anchor-v1`](../../findings/results/tool-origo-deictic-anchor-v1.md) and
[`result/indexical-character-application-v1`](../../findings/results/indexical-character-application-v1.md)).

But per charter §12.3 and `PROTOCOL.md §2`, that terminal status is **not** self-ratifiable in the
session that opened it. So this decision is **opened, not closed**, this session. The contingent
result `result/presupposition-projection-v1` (created in the run session; see the run record)
carries **`anchor: pending`** with this decision in its `contingent-on:` until an independent later
session ratifies.

## Options

- **A (provisional default): adopt `internal-contrast-only`.** The presupposition-vs-matched-entailment
  projection contrast is a within-model behavioral contrast making no human comparison, exactly like
  the constructional and indexical lines already ratified as `internal-contrast-only`. Promote the
  result's anchor field from `pending` to the terminal `internal-contrast-only` and drop its
  `contingent-on:`. Fixes the yardstick, **not** the result — every number and caveat stands as
  written.
- **B: require a human projectivity anchor.** Treat any projection reading as an implicit
  human-comparison claim and hold the result contingent until an externally-released human
  projection / projectivity judgment set is located in-repo. (None is in-repo; this would suspend
  the result indefinitely.)
- **C: keep open** — if the adversarial reviewer finds the within-model contrast smuggles a hidden
  human comparison (e.g. the item design or verdict map presupposes a human-normed "correct"
  projection pattern), name exactly where, and keep the anchor question open with that gap recorded.

## What ratification must respect

Ratification fixes the **yardstick, never the result** (`PROTOCOL.md §2`). If a later session finds
the verdict map or item construction covertly encodes a human-normed target, that is Option C, not a
reason to rewrite the numbers. The reviewer must be a **fresh agent** in a **later** session.

## Provisional default

**Option A** (`internal-contrast-only`), pending independent ratification in session 159+.
