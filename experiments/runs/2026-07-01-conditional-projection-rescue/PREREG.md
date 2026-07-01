# PREREG — the conditional-projection-rescue follow-up probe

**Run:** `2026-07-01-conditional-projection-rescue` · **frozen** 2026-07-01 (session 159) ·
**manifest sha** `c88ef626abd1f0b8cb22e19dd27b7b96b7016ed634b79de3cabe2e399079fe54`

Follow-up to [`result/presupposition-projection-v1`](../../../wiki/findings/results/presupposition-projection-v1.md)
(run `2026-07-01-presupposition-projection`, session 158). That result found verdict **PROJECTION
(2/3)** but a sharp, across-panel **COLLAPSE of projection under the conditional-antecedent frame**:
presupposition-survival under the conditional frame was **0.42 / 0.17 / 0.17** (claude / gpt /
gemini), at or near the matched-entailment leg, while negation was textbook-clean and questions
projected strongly. Frozen *before* any probe call; the FREEZE GUARD in `probe.py` refuses to run
unless the manifest sha above is intact.

## The one question (nothing wider)

> Is the conditional-antecedent projection collapse **rescuable** by an explicit framing, or is it a
> **robust** feature of the text-trained projection behavior? Concretely: does reframing the
> conditional as a sincere speaker **commitment**, or moving the trigger **out of the antecedent**,
> or asking about the speaker's **belief**, restore presupposition-endorsement above the collapsed
> BASE level (and above the matched-entailment leg)?

The measure is a **within-model contrast**: (i) P-vs-E endorsement WITHIN each arm (E is the yes-bias
control), and (ii) P endorsement ACROSS arms relative to a BASE arm that replicates the s158
conditional cell verbatim.

## Scope cap — LOAD-BEARING (read before citing any result)

A positive (rescue) or negative (robust collapse) is a **within-model behavioral contrast ONLY**. It
does **not**:
- make **any human comparison** — no human projectivity / projection-judgment baseline is claimed,
  measured, or needed. The signal is *P endorsement changes (or not) across framings within the same
  model*, and *P survives more than E within an arm*.
- certify that the model **represents** presupposition vs. assertion, or that it "computes"
  projection; the contrast is behavioral (endorsement of an inference under embedding/framing), read
  off forced-choice answers. Text-consistency is not mechanism.
- adjudicate the projection problem or any theory of presupposition filtering; the CONSEQ arm uses
  standard consequent-projection as an operationalization of "non-antecedent position", not as a
  claim about how filtering works.

**Anchor discipline.** This follow-up stays strictly within the within-model contrast whose terminal
`internal-contrast-only` status was **ratified** for the parent line this session
([`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../../wiki/decisions/resolved/presupposition-projection-internal-contrast-anchor.md),
session 159, autonomous adversarial review). So the result carries **`anchor: internal-contrast-only`**
and opens **no new anchor decision**.

## Panel & settings

Panel per [`config/models.md`](../../../config/models.md): `panel.A` = anthropic/claude-sonnet-4.6,
`panel.B` = openai/gpt-5.4-mini, `panel.C` = google/gemini-3.5-flash. Temperature 0; zero-shot;
text-only, single-turn (no tools); gemini `reasoning={"effort":"minimal"}` (config/models.md caveat);
billed `usage.cost` recorded. The system prompt
("You are a careful reader. Answer the user's question directly.") — identical to s158 — never
mentions presupposition, projection, or the "right" answer.

## Design — 12 base scenarios (REUSED VERBATIM from s158) x 4 arms x 2 targets = 96 item-conditions

`prep.py` freezes the items. The 12 scenarios reuse **verbatim** s158's frozen `SCEN`: same sids,
same `presup`/`entail` targets, same **antecedent-conditional** sentences (four trigger families —
factive / aspectual / definite / cleft — 3 each). New per scenario: a `cond_consequent` sentence
(the same trigger relocated to the consequent of a conditional with a neutral, unrelated antecedent).

The **four arms** factorize cleanly:

| arm | sentence | query wrapper | isolates |
|-----|----------|---------------|----------|
| **base** | antecedent-conditional (s158) | s158 plain query, VERBATIM | replication anchor |
| **commit** | antecedent-conditional (s158) | "A speaker sincerely asserts …; considering everything the speaker is thereby committed to, does it follow that: {target}" | FRAMING (commitment) |
| **conseq** | trigger in CONSEQUENT, neutral antecedent | s158 plain query | POSITION (out of antecedent) |
| **belief** | antecedent-conditional (s158) | "A speaker sincerely asserts …; does the speaker believe that: {target}" | FRAMING (speaker belief) |

- `base` and `conseq` share the query and differ only in the sentence → isolates trigger **position**.
- `base`, `commit`, `belief` share the antecedent-conditional sentence and differ only in the query →
  isolates **framing**.

Each item is one forced-choice completion answered **YES / NO / UNCLEAR**; `endorsed` == YES
(`analyze.py`). The three-way choice lets a non-endorsed inference be marked UNCLEAR rather than
forced to a false YES.

**The rescue signature.** In `base`, presup-endorse is expected **LOW** (reproducing the s158
collapse). A rescue arm restores projection if its presup-endorse climbs back **above the RESCUE
floor** *and* its (presup − entail) gap re-opens — while the E leg stays low (a framing that merely
inflates YES lifts E too, caught by the yes-bias flag).

## Why the plain-frame sanity is not re-run

s158 already established the plain-frame sanity floor (plain presup-endorse 0.92 / 0.92 / 1.00; plain
entail-endorse 1.00 / 0.92 / 1.00) on these exact base scenarios — the models *do* endorse both legs
when the base is plainly asserted. Re-running it would be re-grinding a frozen result. This probe's
internal validity anchors are instead **BASE replication** (must reproduce the collapse) and the
**CONSEQ position control** (a non-antecedent environment where projection is expected to survive).

## Metrics (pre-specified, direction fixed) — see `analyze.py`

Per (model, arm), from parsed answers:
- **presup_endorse** — P-endorse rate over the arm's 12 items.
- **entail_endorse** — E-endorse rate over the arm's 12 items (yes-bias control).
- **gap** = presup_endorse − entail_endorse (within-arm projection signal).
- **rescue_lift** = arm presup_endorse − base presup_endorse (per rescue arm).

## Verdict map (thresholds fixed NOW; may be tightened, never loosened)

```
RESCUE            = 0.60   per-model per-arm presup_endorse floor to count projection RESTORED.
GAP               = 0.30   per-model per-arm (presup - entail) floor to count RESTORED.
BASE_COLLAPSE_MAX = 0.60   base presup_endorse must be BELOW this for >=2/3 models to confirm the
                           s158 collapse replicated (design-validity anchor).
YESBIAS           = 0.60   per-arm entail_endorse at/above this flags a yes-shift confound on that arm.
```

- Per rescue arm (commit / conseq / belief), panel level: **RESCUED** if ≥2/3 models rescued
  (presup_endorse ≥ RESCUE AND gap ≥ GAP); **NOT-RESCUED** if ≥2/3 models have presup_endorse <
  RESCUE; **MIXED** otherwise.
- **Overall:**
  - If BASE did **not** replicate the collapse (<2/3 models below BASE_COLLAPSE_MAX) →
    **REPLICATION-ANOMALY**; rescue readings caveated (the collapse itself did not reproduce).
  - Else if ≥1 rescue arm is RESCUED → **PARTIAL/RESCUED** (name which lever restores projection).
  - Else → **ROBUST-COLLAPSE** (the conditional-antecedent collapse survives all three framings — a
    within-panel limit of the text-trained behavior).

A robust collapse is a first-class result and is written as such (charter §4). A rescue is equally
first-class and would reframe the s158 collapse as a **surface-cue artifact** of the neutral query
rather than a deep limit.

## Cost

96 conditions × 3 models = 288 single-turn, single-word completions — the same size and shape as
s158, which billed **$0.0486**. Pre-flight expectation **≈ $0.05** (gemini's minimal-reasoning tokens
dominate). `ABORT_USD = 1.00` hard-stops a runaway; far under the $2.50 single-run flag and the
$5.00/day cap (UTC-2026-07-01 spend before this run: $0.0486). A real pre-flight (`--limit` on one
model) is measured and recorded before the full run.

## What each outcome would feed

- **PARTIAL/RESCUED** → the conditional collapse is (at least partly) an artifact of framing/position,
  not a hard limit; strengthens the "frame-conditioned distributional regularity" reading of
  [`essay/projection-defeasible-by-frame`](../../../wiki/findings/essays/projection-defeasible-by-frame.md);
  the s158 result's Interpretation gains a rescue caveat (numbers unchanged).
- **ROBUST-COLLAPSE** → the collapse is robust to commitment / position / belief framing — a genuine
  within-panel limit of the text-trained projection behavior; strengthens the "genuine limit" reading.
- **REPLICATION-ANOMALY** → the s158 conditional cell did not reproduce under a fresh run; reported
  honestly, no rescue claim, and flags instability in the parent result's conditional cell.
