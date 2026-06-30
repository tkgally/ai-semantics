---
id: indexical-character-anchor-type
title: Is the indexical character-application result internal-contrast-only, or does it owe a human anchor?
status: resolved
opened: 2026-06-30
opened-by: autonomous (session 154, opening the new result's mechanical anchor-tracking gate)
resolved: 2026-06-30
resolved-by: autonomous (adversarial review)
resolution: adopt-default (A — internal-contrast-only)
provisional-default: A (internal-contrast-only)
contingent-artifacts:
  - result/indexical-character-application-v1
---

> **Status: RESOLVED (2026-06-30, session 155, autonomous adversarial review — cross-session:
> opened session 154 on 2026-06-30, ratified session 155; the session boundary held; the s154
> opener and this session's downstream work are distinct from the fresh reviewer). VERDICT: ADOPT
> A (`internal-contrast-only`).** An independent fresh-agent reviewer (not the orchestrator) read
> the decision, the contingent result, the essay it tests, and the [`CLAUDE.md`](../../../CLAUDE.md) anchor discipline,
> and adversarially checked every angle on which the verdict could have been **B / keep-open**:
>
> - **No human-comparison claim anywhere.** The result's *Does NOT license* section explicitly
>   disclaims it ("**Any human comparison.** No human baseline is claimed, measured, or needed …
>   says nothing about whether people resolve described indexicals better, worse, or the same"),
>   and its headline is a **within-model** accuracy against a **stipulated answer key** (confirmed by
>   *Limits* §"Stipulated key, not a human gradient" — "answer-key resolution, never a per-item
>   human distribution"). The only cross-entity comparison present is **within-panel** (claude / gpt
>   / gemini at ceiling), which needs no human anchor.
> - **Essay consistency.** The essay it tests is itself `anchor: internal-contrast-only` and
>   disclaims human comparison "in either direction"; the one finding the essay leans on
>   (conversation-as-text) is itself internal-contrast-only. Consistent.
> - **No illegitimate strengthening.** Ratifying A promotes only the `anchor:` field
>   (`pending → internal-contrast-only`) and drops `contingent-on`; the ceiling figures and the
>   pre-registered "**non-falsification, not proof**" reading stand exactly as written. Yardstick,
>   not result.
> - **Quote-integrity: none found** (the decision page's characterizations are faithful).
> - **Anti-cheat: confirmed** — the reviewer had no stake in the figures or the anchor outcome and
>   would have returned B / keep-open had any human-comparison claim been present; none was.
>
> **Applied at integration (session 155):** [`result/indexical-character-application-v1`](../../findings/results/indexical-character-application-v1.md)
> promoted `anchor: pending → internal-contrast-only`; its `contingent-on: [indexical-character-anchor-type]`
> dropped to `[]`; its *Status* / *Provenance* prose updated to record the ratification. The finding
> stays `status: proposed` (a non-falsification, not a proof; promotion past `proposed` is Tom's call).
>
> ### Residual risks (survive adoption)
> - The Interpretation §3 phrase "low-bar, broadly-acquired competence rather than a
>   capability-separating one" is a **within-panel** inference; a future citing page must not
>   mis-read it forward as a human-population claim. Not a defect (it is explicitly a cross-model
>   contrast), but flagged.
> - The terminal state forecloses the human-comparison reading **for this result only**. If a
>   human-rated indexical/coreference-resolution resource later enters the repo, any human-baseline
>   claim is a **genuinely new** decision (option B below), not a re-opening of this one.
> - Standing caveat: `internal-contrast-only` must never later be used to launder a ceiling into
>   evidence *of* the affordance — already pre-empted by the result's *Does NOT license: Proof of the
>   affordance*.
>
> ---
>
> *The provisional-default analysis below is preserved as the reviewer's evidence base.*

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
