---
id: panel-v2-refresh
title: Should the default subject/critic panel be refreshed (panel v2), and on what evidence?
status: resolved
opened: 2026-07-02
opened-by: special session (Tom-directed program adoption; program item A4c)
resolved: 2026-07-02
resolved-by: autonomous (adversarial review)
resolution: "ADOPT DEFAULT (Option A) AS A SEQUENCED HOLD WITH A FIRING CONDITION — keep panel-v1 as the primary subject/critic set for all lines; decide the v2 question on evidence once the ladder data lands, rather than by a reflexive swap. BINDING SAFEGUARD (both reviewers required it): the hold must carry an explicit, tracked RE-OPEN TRIGGER written into [`config/models.md`](../../../config/models.md) and [`NEXT.md`](../../../NEXT.md) — this decision re-opens (and is then decided B vs C on evidence) the moment ladder data lands OR the `scale-ladder-subjects` decision is rejected. Without that firing condition Option A can silently harden into Option C (indefinite v1), which is the stall the non-Anthropic panel vote objected to. NOTE THE DECORRELATION DIVERGENCE: the non-Anthropic panel vote (gpt-5.4-mini) dissented toward Option B (refresh now), on two premises — that v1 is 'already stale' and that the ladder is an 'unrelated instrument'. The fresh-agent reviewer rebutted both (v1's three slots are still recorded as current-generation and battle-tested five weeks on; the ladder is the CHEAPEST direct sensitivity test of whether a refresh would change any result, so sequencing on it is principled sensitivity-before-spend, not a stall) and additionally weighed B's real costs (forks the subject set, pays a calibration round before anyone knows the fork matters, and creates a mixed-panel bookkeeping state that is itself a silent-mixing hazard). Verdict A stands with the divergence recorded and the anti-stall firing condition locked in. Ratification fixes the yardstick only. Session 168 independent fresh-agent adversarial review (ADOPT-DEFAULT) + one non-Anthropic panel vote (ADOPT-OTHER:B, weighed and not followed); cross-session boundary held (opened special session 2026-07-02, ratified s168)."
provisional-default: "[RATIFIED — see resolution above.] Option A: keep panel-v1 primary until ladder data lands, then decide with data; now carrying a binding re-open trigger."
contingent-artifacts: []
---

> **Status: RESOLVED — ratified 2026-07-02 (session 168, autonomous adversarial review,
> cross-session — opened by the 2026-07-02 special session, ratified s168). Verdict: ADOPT DEFAULT
> (Option A) as a SEQUENCED HOLD WITH A FIRING CONDITION.** The non-Anthropic decorrelation vote
> **dissented toward Option B** (refresh now); the fresh reviewer weighed and rebutted that dissent
> in writing (see the resolution field and the [Ratification](#ratification--adversarial-review-session-168)
> section). The adopted hold is null-preserving (panel-v1 continues for every line, no frozen design
> is invalidated) and, crucially, carries a **tracked re-open trigger** so it cannot decay into
> indefinite-v1. **Ratification fixes the YARDSTICK only, never a result.**

# Decision: panel v2 refresh

**Opened by the 2026-07-02 special session** implementing
[`program-2026-07-adoption`](program-2026-07-adoption.md) (review item A4.3).
**Eligible for cross-session ratification from session 168** ([`PROJECT.md`](../../../PROJECT.md) §12.3); Tom may rule
at any time. Related but separable:
[`scale-ladder-subjects`](scale-ladder-subjects.md) (supplementary subjects, panel unchanged).

## The question

Charter §6 says the panel is "revisited when models change." Panel v1
([`config/models.md`](../../../config/models.md)) was selected 2026-05-28 and has now carried
~75 runs across five weeks in which every named lab shipped new releases. Nothing suggests
panel v1 is *broken* — the truth-up note in [`config/models.md`](../../../config/models.md) records it as battle-tested —
but the charter's revisit promise is due, and the choice of subjects is value-laden: switching
mid-stream breaks continuity with every existing result; never switching quietly turns a
"current models" claim into a "spring-2026 models" claim.

## Options

- **A — Keep panel v1 as primary until ladder data lands; then decide with data (provisional
  default).** If [`scale-ladder-subjects`](scale-ladder-subjects.md) is adopted and run, its
  results (does behavior shift with capability within family?) directly inform whether a v2
  refresh would change anything worth changing. Re-open this decision with that evidence
  attached; panel v1 continues for all lines meanwhile.
- **B — Refresh to v2 now.** Select three current-generation, family-decorrelated models
  (verified live), re-run a small calibration battery, and designate v2 the default for *new*
  lines; v1 is retained for continuity replications of existing lines. Fastest path to
  "current models" claims; costs a calibration round and forks the subject set before the
  ladder evidence exists.
- **C — Keep panel v1 indefinitely.** Explicitly re-scope all claims as panel-v1-specific.
  Cheapest; concedes the "current models" framing permanently.

## Provisional default and rationale

**A.** The revisit promise is honored by *deciding on evidence* rather than by reflexively
swapping subjects; the ladder pilot is the cheapest instrument that could make this decision
informed. If the ladder decision is rejected, this one should be re-argued on its own (B vs C)
rather than defaulting through.

## What ratification must check (for the reviewer)

That the sequencing genuinely depends on the ladder decision's outcome; that "v1 for
continuity, v2 for new lines" (if B) is written into [`config/models.md`](../../../config/models.md) with dates so no
result silently mixes panels; and that no in-flight frozen design names a panel this decision
would invalidate.

## Ratification — adversarial review (session 168)

**Ratified 2026-07-02 (session 168), autonomous cross-session adversarial review.** A fresh
independent agent read this page, [`config/models.md`](../../../config/models.md) (the panel + its 2026-07-02 truth-up), the
related [`scale-ladder-subjects`](scale-ladder-subjects.md) decision, and `wiki/program.md`
(A4b/A4c), and returned **ADOPT-DEFAULT (Option A)**. The decorrelation vote (`gpt-5.4-mini`,
cutoff-aware preamble) **dissented toward Option B (refresh now)** — a divergence, which is signal,
weighed below.

**Why A over the panel's B.** The panel's dissent rests on two premises the fresh reviewer could
not confirm. (1) *"Already stale":* v1 is five weeks old, and [`config/models.md`](../../../config/models.md) still lists its
three slots as current-generation flagships/mid-tier, truthed-up 2026-07-02; new releases shipping
in the window is not the same as the panel's own models being superseded, so the "current models →
spring-2026 models" decay the panel fears is not yet established. (2) *"Unrelated instrument":* the
ladder is the cheapest direct test of whether a refresh would change any result — flat within-family
behavior across capability means a v2 swap is cosmetic and v1 claims generalize; scaling behavior
makes the refresh substantively important and better designed with that evidence in hand. So the
sequencing is principled sensitivity-before-spend, not hostage-taking. Against B's speed the
reviewer weighed its real costs: B forks the subject set and pays a calibration round before anyone
knows the fork matters, and it creates a mixed-panel bookkeeping state (v1-continuity vs v2-new)
that is itself a live source of the silent-mixing error ratification is meant to prevent — whereas A
introduces no new instrument degrees of freedom and invalidates no in-flight frozen design. The
reviewer noted it would move to B *were v1 materially older, or were the ladder measuring something
orthogonal to the refresh question*; on the present facts A is the cheaper, null-preserving,
reversible choice, and it honors charter §6 ("revisited when models change") by deciding on evidence
rather than by a reflexive swap.

**The binding safeguard.** A must be recorded as a *sequenced hold with a firing condition*, not a
quiet close, or it hardens into Option C (indefinite v1) — the very stall the panel objected to.
The resolution therefore requires an explicit, tracked **re-open trigger** in [`config/models.md`](../../../config/models.md) and
[`NEXT.md`](../../../NEXT.md): this decision re-opens (decided B vs C on evidence) the moment ladder data lands OR the
`scale-ladder-subjects` decision is rejected. Option A already contains its own anti-stall clause
("if the ladder decision is rejected, re-argue B vs C rather than defaulting through"); the re-open
trigger makes that mechanical rather than a prose promise.

`resolved-by: autonomous (adversarial review)`.
