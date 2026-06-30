---
id: indexical-character-anchor-type
title: Is the indexical character-application result internal-contrast-only, or does it owe a human anchor?
status: open
opened: 2026-06-30
opened-by: orchestrator
provisional-default: A (internal-contrast-only)
contingent-artifacts:
  - result/indexical-character-application-v1
---

# Decision: anchor type for the indexical character-application result

## Why this exists (mechanical anchor-tracking; opened session 154)

[`result/indexical-character-application-v1`](../../findings/results/indexical-character-application-v1.md)
measures whether the panel **mis-applies** an indexical's convention-fixed rule (its Kaplanian
*character*) to a fully **described** origo — a behavioral run of **trigger (c)** of
[`essay/indexical-character-learnable-content-supplied`](../../findings/essays/indexical-character-learnable-content-supplied.md).
The headline is a **within-model** accuracy against a **stipulated key** (each item's correct
resolution is fixed by the described context), pooled over plain / origo-shift / embedded
conditions. The verdict is a **non-falsification** (all three models at ceiling).

Per [`CLAUDE.md`](../../../CLAUDE.md) §anchor discipline, a `result` either carries an `anchors:`
link to a `resource`, or is marked `anchor: pending` + a queued decision, or is the ratified
terminal `anchor: internal-contrast-only`. The honest type here is **internal-contrast-only**:
the result makes **no human-comparison claim** — it neither asserts nor needs a human accuracy
baseline; its force is entirely a within-model "does the rule get applied to the described
content." But `internal-contrast-only` is a **ratified terminal declaration that cannot be
ratified in the session that opens it** (charter §12.3). So the result ships **`anchor: pending`**,
contingent on this decision, until a later session ratifies via independent adversarial review.

## The question

Does the indexical character-application result (and any sibling pure-character probe) make a
human-comparison claim that obliges a human resource anchor, or is it correctly terminal
`internal-contrast-only`?

## Options

- **A (provisional default) — `internal-contrast-only`.** The result claims only a within-model
  contrast (rule applied vs not, against a stipulated key); it draws **no** human baseline and the
  essay it tests is itself `internal-contrast-only`. Ratifying A promotes the result's anchor field
  from `pending` to the terminal `internal-contrast-only` and drops its `contingent-on`. This
  **fixes the yardstick, not the result** — the ceiling figures stand exactly as written.
- **B — owe a human anchor.** If a *human-comparison* reading is ever wanted (e.g. "models resolve
  described indexicals as accurately as people do"), that is a **new** anchor question needing a
  human-rated indexical/coreference resolution resource (none is in-repo or queued). The current
  result makes no such claim, so B would only apply to a *future* human-comparison extension, not
  to this within-model run.

## Eligibility

Opened **session 154**; **not** ratifiable this session (must be a later session, independent
adversarial review — charter §12.3). Provisional default **A**.
