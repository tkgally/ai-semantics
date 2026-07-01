---
id: presupposition-accommodation-internal-contrast-anchor
title: "Is the supported/neutral/contradicting accommodation contrast a legitimate internal-contrast-only terminal status (no human anchor)?"
status: open
opened: 2026-07-01
opened-by: orchestrator (session 162)
contingent-artifacts:
  - result/presupposition-accommodation-v1
---

# Decision: human anchor for the presupposition / accommodation result

## Why this exists (surface, do not self-ratify)

Session 162 designed, froze, and ran the presupposition / accommodation probe
([`experiments/runs/2026-07-01-presupposition-accommodation/`](../../../experiments/runs/2026-07-01-presupposition-accommodation/README.md)),
operationalizing [`open-question/presupposition-accommodation-corner`](../../findings/open-questions/presupposition-accommodation-corner.md)
(opened session 161). Its primary measure is a **within-model contrast** across three CONTEXT
conditions on the *same* trigger sentence — **supported** (the presupposition is explicitly stated;
a sanity/retrieval floor), **neutral** (the presupposition is new and unopposed; the accommodation
test), and **contradicting** (a prior sentence explicitly denies it; the gate). The measure makes
**no human comparison**: it does not claim, measure, or need a human accommodation-judgment
baseline. Its force is a *within-model asymmetry across the three contexts* (does the model supply an
unmet presupposition in the neutral context while withholding it under explicit contradiction?), not
*the model matches human accommodation behavior*.

This is exactly the shape the project has repeatedly ratified as
**`anchor: internal-contrast-only`** — the terminal declaration that a result makes no
human-comparison claim and so requires no resource anchor (introduced with
[`decisions/resolved/conflicting-cue-human-anchor`](../resolved/conflicting-cue-human-anchor.md),
ratified 2026-05-31; the same status carried by the projection line's results, e.g.
[`result/presupposition-projection-v1`](../../findings/results/presupposition-projection-v1.md) and
[`result/projection-trigger-inventory-v1`](../../findings/results/projection-trigger-inventory-v1.md),
and the indexicality corner's results).

But per charter §12.3 and `PROTOCOL.md §2`, that terminal status is **not** self-ratifiable in the
session that opened it. So this decision is **opened, not closed**, this session. The contingent
result [`result/presupposition-accommodation-v1`](../../findings/results/presupposition-accommodation-v1.md)
carries **`anchor: pending`** with this decision in its `contingent-on:` until an independent later
session ratifies.

## Options

- **A (provisional default): adopt `internal-contrast-only`.** The supported/neutral/contradicting
  accommodation contrast is a within-model behavioral contrast making no human comparison, exactly
  like the projection, constructional, and indexical lines already ratified as
  `internal-contrast-only`. Every quantity feeding the verdict is a within-model endorsement rate
  over the model's own YES/NO/UNCLEAR answers (`supported_endorse`, `neutral_endorse`,
  `contradicting_endorse`, and `accommodation_gap = neutral − contradicting`); there is no human key,
  gold label, or external dataset anywhere in the scoring path (`parse_endorse` reads the model's own
  token — the only ground truth). Promote the result's anchor from `pending` to
  `internal-contrast-only` and drop its `contingent-on:`. Fixes the yardstick, **not** the result —
  every number and caveat stands as written.
- **B: require a human accommodation anchor.** Treat any accommodation reading as an implicit
  human-comparison claim and hold the result contingent until an externally-released human
  accommodation-judgment set is located in-repo. (None is in-repo; this would suspend the result
  indefinitely — the open-question page already recorded that no such resource exists.)
- **C: keep open** — if the adversarial reviewer finds the within-model contrast smuggles a hidden
  human comparison (e.g. the verdict thresholds — SANITY 0.75 / ACCOM 0.60 / GAP 0.30 / FLATBAND
  0.15 / LOWACC 0.40 — presuppose a human-normed "correct" accommodation pattern, or the item
  construction encodes a human key), name exactly where, and keep the anchor question open with that
  gap recorded.

## What the reviewer should scrutinize (result-specific)

The pre-run critic (session 162) flagged one interpretive point the ratifier should weigh against
Option C: the "gate" leg cannot *behaviorally* separate genuine accommodation-blocking from generic
contradiction-detection plus a "does it follow?" yes-bias. This is inherent to the operationalization
and is already fenced by the strictly-behavioral, `internal-contrast-only` scope cap (the result
disclaims any semantic-representation claim and states the yes-bias+contradiction-detection reading
explicitly). The anchor question is narrower than that interpretive one: it asks only whether the
*within-model contrast* needs a *human resource anchor*, and the yes-bias alternative does not
introduce a hidden human comparison — so it bears on how strongly the result may be *read*, not on
whether it owes an anchor. The reviewer should confirm this separation holds.

## What ratification must respect

Ratification fixes the **yardstick, never the result** (`PROTOCOL.md §2`). If a later session finds
the verdict map or item construction covertly encodes a human-normed target, that is Option C, not a
reason to rewrite the numbers. The reviewer must be a **fresh agent** in a **later** session (this
decision is **not** eligible for ratification in session 162, the session that opened it).

## Provisional default

**Option A** (`internal-contrast-only`), pending independent ratification in session 163+.
