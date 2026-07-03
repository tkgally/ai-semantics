---
id: presupposition-doppelganger-internal-contrast-anchor
title: Does the presupposition doppelgänger residual make a human-comparison claim (owing a human anchor), or is it the terminal internal-contrast-only?
status: resolved
opened: 2026-07-03
opened-by: session-173
resolved: 2026-07-03
resolved-by: autonomous (adversarial review)
resolved-session: 174
contingent-artifacts:
  - result/presupposition-doppelganger-control-v1
---

# Decision: the human-anchor status of the presupposition doppelgänger residual

## Resolution (session 174) — ADOPT A (`internal-contrast-only`)

**Ratified 2026-07-03 (session 174), autonomous adversarial review + one non-Anthropic panel vote, cross-session** (opened by session 173, ratified by session 174 — the surfacing/ratifying boundary held; the fresh reviewer did no downstream work on this line). **The two votes CONVERGED on Option A.**

A fresh independent reviewer traced the complete scoring path directly in
[`analyze.py`](../../../experiments/runs/2026-07-03-presupposition-doppelganger/analyze.py) and
[`prep.py`](../../../experiments/runs/2026-07-03-presupposition-doppelganger/prep.py), not via this page's summary, and ran the three required checks:

- **Check A — no human key enters. CONFIRMED.** `parse_endorse` (`analyze.py` L57–62) regex-extracts the first `yes|no|unclear` token from the model's own raw `answer` — the *only* ground truth read anywhere. `leg_rate` (L74–90) is a rate over the model's own YES tokens; `residual_block` (L93–112) computes `residual = trigger_project − doppel_project`, and in `main()` (L164–175) each model's block is built from *its own* `raw/{slot}.json` only, so the residual is unambiguously a difference of the **same model's own two endorsement rates**. `label_for`/`panel_verdict` branch only on within-model rates/labels. The raw records carry `{id, sid, family, powered, leg, frame, cancelling, projecting, target, sentence, answer, answer_sha, usage}` — **no `gold`/`correct`/`expected`/`annotation` field**; a grep for `gold|human|correct|ground_truth` over the run's code returned only "no human comparison" disclaimers. The trigger inventory (factive/aspectual/cleft, SEP §1.1) functions as the **a-priori construction map** — fixing which forms are triggers and the pre-registered contrast direction, and naming the two legs — not as a per-item human key; `SANITY = 0.60` is a within-model robustness floor on the model's *own* trigger rate (gpt's cleft control-fail at 0.583 is the model failing *its own* floor, not mismatching a human), structurally identical to the sibling's ratified `SURVIVE = 0.60`.
- **Check B — anti-cheat / orthogonality. CONFIRMED.** The identical path reads only the models' own tokens whether the outcome is BEATS-DOPPELGANGER, SHADOW-SATURATED, or MIXED; no branch loads a human key on any outcome. The `scope: "internal-contrast-only … no human comparison"` field in `results.json` is written *unconditionally* (L233), not gated on the verdict. Decisively: adopting A yields no "nicer result" — the outcome that obtained is BEATS-DOPPELGANGER, the explicitly **under-licensed** outcome that does *not* fire the essay's revision trigger and does *not* move the corner to the beater side, so there is zero result-motivated pressure to pick A. The yardstick is fixed against the grain of a deflationary result.
- **Check C — structural parity. CONFIRMED.** The already-resolved sibling [`presupposition-projection-internal-contrast-anchor`](presupposition-projection-internal-contrast-anchor.md) (2026-07-01, ADOPT A) computes `projection_gap = presup_survival − entail_survival`, both endorse-rates over the same model's own answers, guarded by the same within-model `0.60` floor and decided by the same panel tally. This probe's `residual = trigger_project − doppel_project` is the identical shape; the only design difference (the sibling varies the target proposition P vs. E, this one varies the predicate/construction with target P held constant) does not change the anchor character.

**Non-Anthropic decorrelation vote (gpt-5.4-mini, panel.B): converged on A** — "the scorer depend[s] only on each model's own YES/NO outputs, with no human labels, no gold key, and no external annotated dataset … The anchor conclusion is orthogonal to whether the residual is positive or flat … it does not read any human key regardless of outcome." No divergence to weigh.

**Option B (rejected).** Classifying `realize` as factive and `suspect` as non-factive uses human linguistic knowledge to *construct the legs*, as every stimulus does; but the scorer never asks "did the model match a human judgment?" — it computes trigger-leg-minus-doppel-leg *within* the model. A genuine model-vs-human doppelgänger claim would be a *new* probe against a licensed human dataset, and the presupposition human-anchor scout already found the candidate sets license-UNVERIFIED ([`presupposition-projection-human-anchor`](presupposition-projection-human-anchor.md)).

**Residual nit (non-blocking).** The D1 controls for factive/aspectual vary the trigger *word*, so a positive residual is lexical-distribution-attributable (surface-cue-reconstructable). That is an **interpretive** ceiling — fully captured by the result's B1/B2 "under-licensed" framing, the `asymmetry_note`, and the LOAD-BEARING Scope section — bearing on *what the residual means*, not on *whether a human number enters*. It does not touch the anchor question.

**Applied at integration (fixes the yardstick, never the result):** [`result/presupposition-doppelganger-control-v1`](../../findings/results/presupposition-doppelganger-control-v1.md) anchor promoted `pending → internal-contrast-only`, its `contingent-on` dropped to `[]`. The BEATS-DOPPELGANGER verdict, all residuals (+0.78/+0.47/+0.94), the per-family cells, the cleft wrinkle, and every caveat stand **unchanged**; the finding stays `status: proposed`. Tom's standing override outranks this autonomous ratification.

---

## Why this was owed

[`result/presupposition-doppelganger-control-v1`](../../findings/results/presupposition-doppelganger-control-v1.md)
measures a **within-model residual** — `trigger P-endorse − matched-doppelgänger P-endorse` over the
projecting frames — and returns **BEATS-DOPPELGANGER** (the under-licensed, word-form-keyed outcome; see
the result's B1/B2 framing). Every empirical claim about LLM meaning must either carry an `anchors:` link
to a human `resource`, or **be a within-model contrast making no human comparison** (`anchor:
internal-contrast-only`, a ratified terminal state), or queue the anchor question
([`CLAUDE.md`](../../../CLAUDE.md) §Typed-links, senselint check 4). This page surfaced that question
rather than the run session self-ratifying it (charter §12.3 — only a later session ratifies).

## Question

Does the doppelgänger residual make a **human-comparison** claim (obliging a human presupposition/
doppelgänger baseline as a `resource` anchor), or is it correctly the terminal **`internal-contrast-only`**
— a within-model contrast whose entire force is *the trigger leg endorses the content more than the
matched doppelgänger leg, within the same model*, with no human number entering?

## Options

- **A (provisional default, ADOPTED) — `internal-contrast-only`.** The measure is a difference of the model's
  **own** endorsement rates (`analyze.py` `parse_endorse` reads only the model's YES/NO/UNCLEAR token;
  `residual = trigger_project − doppel_project`; the verdict is a pure per-model/panel tally). No human
  key, gold label, external annotated dataset, or human doppelgänger baseline appears anywhere in the run;
  the thresholds (SANITY 0.60 / RESID 0.30 / FLATBAND 0.15) are cutoffs on the model's own rates that
  *name* a within-model pattern. Naming the trigger inventory after SEP §1.1 is using the source as the
  a-priori construction map, **not** as a human baseline. **Structurally identical** to the three already-
  ratified sibling anchors
  ([`decisions/resolved/presupposition-projection-internal-contrast-anchor`](presupposition-projection-internal-contrast-anchor.md),
  `presupposition-accommodation-internal-contrast-anchor`, `projection-trigger-inventory-internal-contrast-anchor`).
- **B (rejected) — owes a human anchor.** Would hold that comparing the trigger to a *non-presupposing*
  doppelgänger implicitly imports a human competence norm (what "should" project). Rejected: the
  result makes **no** claim that the residual matches human projection/doppelgänger discrimination
  (none measured); the B1/B2 framing is explicit that a positive residual is a within-model,
  distributionally-encoded, word-form-keyed discrimination, not a human-competence match — so no human
  baseline is presupposed. A **model-vs-human** doppelgänger comparison would be a *new* probe against a
  licensed human dataset, not a re-reading of this within-model residual (and the presupposition
  human-anchor scout already found the candidate datasets license-UNVERIFIED,
  [`decisions/resolved/presupposition-projection-human-anchor`](presupposition-projection-human-anchor.md)).

## Provisional default

**Option A (`internal-contrast-only`).** The result carried `anchor: pending` until ratified. A later
independent session should trace the scoring path directly in
[`analyze.py`](../../../experiments/runs/2026-07-03-presupposition-doppelganger/analyze.py) and
[`prep.py`](../../../experiments/runs/2026-07-03-presupposition-doppelganger/prep.py), confirm **no human
key enters** and that the anti-cheat holds (the same anchor conclusion follows regardless of whether the
verdict came out BEATS, SHADOW-SATURATED, or MIXED — the verdict is orthogonal to the anchor question),
route **one non-Anthropic panel vote**, and then either `resolved-by: autonomous (adversarial review)` or
replace. Tom's standing override outranks any autonomous ratification. *(Done s174 — see Resolution above.)*

## Ratification note

Opened by **session 173**; **not** ratifiable by it (charter §12.3). Ratified **session 174**.
