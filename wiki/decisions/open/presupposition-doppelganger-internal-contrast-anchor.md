---
id: presupposition-doppelganger-internal-contrast-anchor
title: Does the presupposition doppelgänger residual make a human-comparison claim (owing a human anchor), or is it the terminal internal-contrast-only?
status: open
opened: 2026-07-03
opened-by: session-173
contingent-artifacts:
  - result/presupposition-doppelganger-control-v1
---

# Decision: the human-anchor status of the presupposition doppelgänger residual

## Why this is owed

[`result/presupposition-doppelganger-control-v1`](../../findings/results/presupposition-doppelganger-control-v1.md)
measures a **within-model residual** — `trigger P-endorse − matched-doppelgänger P-endorse` over the
projecting frames — and returns **BEATS-DOPPELGANGER** (the under-licensed, word-form-keyed outcome; see
the result's B1/B2 framing). Every empirical claim about LLM meaning must either carry an `anchors:` link
to a human `resource`, or **be a within-model contrast making no human comparison** (`anchor:
internal-contrast-only`, a ratified terminal state), or queue the anchor question
([`CLAUDE.md`](../../../CLAUDE.md) §Typed-links, senselint check 4). This page surfaces that question
rather than the run session self-ratifying it (charter §12.3 — only a later session ratifies).

## Question

Does the doppelgänger residual make a **human-comparison** claim (obliging a human presupposition/
doppelgänger baseline as a `resource` anchor), or is it correctly the terminal **`internal-contrast-only`**
— a within-model contrast whose entire force is *the trigger leg endorses the content more than the
matched doppelgänger leg, within the same model*, with no human number entering?

## Options

- **A (provisional default) — `internal-contrast-only`.** The measure is a difference of the model's
  **own** endorsement rates (`analyze.py` `parse_endorse` reads only the model's YES/NO/UNCLEAR token;
  `residual = trigger_project − doppel_project`; the verdict is a pure per-model/panel tally). No human
  key, gold label, external annotated dataset, or human doppelgänger baseline appears anywhere in the run;
  the thresholds (SANITY 0.60 / RESID 0.30 / FLATBAND 0.15) are cutoffs on the model's own rates that
  *name* a within-model pattern. Naming the trigger inventory after SEP §1.1 is using the source as the
  a-priori construction map, **not** as a human baseline. **Structurally identical** to the three already-
  ratified sibling anchors
  ([`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../resolved/presupposition-projection-internal-contrast-anchor.md),
  `presupposition-accommodation-internal-contrast-anchor`, `projection-trigger-inventory-internal-contrast-anchor`).
- **B — owes a human anchor.** Would hold that comparing the trigger to a *non-presupposing* doppelgänger
  implicitly imports a human competence norm (what "should" project). Rejected in the provisional default:
  the result makes **no** claim that the residual matches human projection/doppelgänger discrimination
  (none measured); the B1/B2 framing is explicit that a positive residual is a within-model,
  distributionally-encoded, word-form-keyed discrimination, not a human-competence match — so no human
  baseline is presupposed. If a later session wanted a **model-vs-human** doppelgänger comparison it would
  be a *new* probe against a licensed human dataset, not a re-reading of this within-model residual (and
  the presupposition human-anchor scout already found the candidate datasets license-UNVERIFIED,
  [`decisions/resolved/presupposition-projection-human-anchor`](../resolved/presupposition-projection-human-anchor.md)).

## Provisional default

**Option A (`internal-contrast-only`).** The result carries `anchor: pending` until ratified. A later
independent session should trace the scoring path directly in
[`analyze.py`](../../../experiments/runs/2026-07-03-presupposition-doppelganger/analyze.py) and
[`prep.py`](../../../experiments/runs/2026-07-03-presupposition-doppelganger/prep.py), confirm **no human
key enters** and that the anti-cheat holds (the same anchor conclusion follows regardless of whether the
verdict came out BEATS, SHADOW-SATURATED, or MIXED — the verdict is orthogonal to the anchor question),
route **one non-Anthropic panel vote**, and then either `resolved-by: autonomous (adversarial review)` or
replace. Tom's standing override outranks any autonomous ratification.

## Ratification note

Opened by **session 173**; **not** ratifiable by it (charter §12.3). Eligible s174+.
