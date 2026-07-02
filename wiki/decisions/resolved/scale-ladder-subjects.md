---
id: scale-ladder-subjects
title: May flagship instruments be re-run on within-family capability siblings (size ladders) as supplementary subjects?
status: resolved
opened: 2026-07-02
opened-by: special session (Tom-directed program adoption; program item A4b)
resolved: 2026-07-02
resolved-by: autonomous (adversarial review)
resolution: "ADOPT DEFAULT (Option A) WITH ONE BINDING CONDITION — within-family capability siblings may be added as supplementary subjects on byte-identical frozen flagship instruments, written as rows explicitly flagged `ladder`, never merged into panel-v1 verdicts, panel-v1 staying primary for all continuity replications; start with the two cheapest frozen instruments and two families. BINDING CONDITION (the safeguard the fresh reviewer and non-Anthropic panel both required): the `ladder` fence is NOT mechanically enforced today (no result-page template, no senselint check), so A4b's FIRST sub-step must add (a) a `ladder: true` front-matter field on every ladder result and (b) a senselint check that flags a missing flag on a ladder run AND forbids any `supports`/`anchors` link from a ladder-flagged page into a panel-v1 claim/result unless separately ratified — no ladder result page may be written before that gate exists. Two recorded riders: 'extend only if the first runs are clean' means EXECUTION-clean (no reasoning-token truncation), never result-direction-clean; and correlated within-family siblings must never be pooled with the cross-family panel to claim broader decorrelation. Ratification fixes the yardstick only; it asserts no finding. Session 168 independent fresh-agent adversarial review (ADOPT-DEFAULT) + one non-Anthropic panel vote (gpt-5.4-mini, ADOPT-DEFAULT); cross-session boundary held (opened special session 2026-07-02, ratified s168)."
provisional-default: "[RATIFIED — see resolution above.] Option A: adopt as a supplementary-subject lane, 2 families first, `ladder`-flagged, panel-v1 stays primary."
contingent-artifacts: []
---

> **Status: RESOLVED — ratified 2026-07-02 (session 168, autonomous adversarial review,
> cross-session — opened by the 2026-07-02 special session, ratified s168; the boundary held).
> Verdict: ADOPT DEFAULT (Option A) WITH ONE BINDING CONDITION** (the `ladder` fence must be made
> mechanically enforceable as A4b's first sub-step — see the resolution field and the
> [Ratification](#ratification--adversarial-review-session-168) section below). **Ratification fixes
> the YARDSTICK only, never a result** ([`CLAUDE.md`](../../../CLAUDE.md) rule 6). Program item
> **A4b** is unblocked (now actionable, gated on the mechanical-flag sub-step); its sequencing feeds
> but does not resolve [`panel-v2-refresh`](panel-v2-refresh.md).

# Decision: within-family size ladders as supplementary subjects

**Opened by the 2026-07-02 special session** implementing
[`program-2026-07-adoption`](program-2026-07-adoption.md) (review item A4.2).
**Eligible for cross-session ratification from session 168** ([`PROJECT.md`](../../../PROJECT.md) §12.3); Tom may rule
at any time.

## The question

The subject panel has been the same three mid-tier models since 2026-05-28
([`config/models.md`](../../../config/models.md)). Every result therefore carries the standing
"single panel, n=3, orderings-not-coefficients" caveat, and the project has no measurement on
the most theoretically loaded axis its setup can cheaply reach: **does shadow-beating grow,
shrink, or hold with model capability?** A residual that scales up with capability supports a
different theory of the phenomenon than one that doesn't — and the project's own
concordant-verdict-hides-spread discipline says a same-verdict panel can hide exactly this
variation.

Proposed instrument: re-run the *cheapest already-frozen flagship probes, unmodified*, on
within-family capability siblings of the current panel (e.g. `openai/gpt-5.4` beside
`gpt-5.4-mini`; `google/gemini-3.5-pro` beside `gemini-3.5-flash`; an Anthropic sibling beside
`claude-sonnet-4.6` — exact slugs to be verified live at design time, never hardcoded from this
page). Subject *additions* are value-laden (they change what "the panel" means and how results
are read), so this queues rather than proceeds.

## Options

- **A — Adopt as a supplementary-subject lane (provisional default).** Ladder runs use the
  frozen instruments byte-identical; results are written as *supplementary* rows explicitly
  flagged `ladder`, never merged into panel-v1 verdicts; panel-v1 remains the primary subject
  set for all continuity replications. Start with the two cheapest flagship instruments and
  two families; extend only if the first runs are clean.
- **B — Adopt for all three families at once.** Same flags, more spend, faster coverage;
  loses the pilot's chance to catch an instrument/scale interaction cheaply.
- **C — Reject.** Keep the n=3 panel as the only subject set; the scale axis stays unmeasured
  and the caveat stays a caveat.

## Provisional default and rationale

**A.** It answers the loaded question for cents, extends (rather than relaxes) the
spread-over-concordance discipline, keeps panel-v1's continuity intact, and adds no new
instrument degrees of freedom (frozen probes re-run unmodified — nothing to retune). The
`ladder` flag keeps supplementary subjects from quietly widening any existing claim.

## What ratification must check (for the reviewer)

That re-running a frozen instrument on new subjects genuinely retunes nothing; that the
supplementary flag is enforced in the result-page template; that family/sibling slugs were
verified live (not assumed); that spend fits the day's cap; and that no pending result's
interpretation is silently contingent on ladder outcomes.

## Ratification — adversarial review (session 168)

**Ratified 2026-07-02 (session 168), autonomous cross-session adversarial review.** A fresh
independent agent (which did no downstream ladder work) read this page, [`config/models.md`](../../../config/models.md),
[`wiki/program.md`](../../program.md) (A4b), and the enforcement surfaces (`tools/senselint.py`, `tools/build-index.py`,
the front-matter schema), and returned **ADOPT-DEFAULT (Option A)**. One decorrelation vote was
routed through a non-Anthropic panel model (`gpt-5.4-mini`, cutoff-aware preamble), which also
returned **ADOPT-DEFAULT** — convergence, recorded as comfort not proof.

**What the review verified against the check-list.** (1) Re-running byte-identical frozen probes on
new subjects adds no instrument degree of freedom — the freeze discipline binds and the design
*strengthens* freeze-before-run rather than relaxing it. (2) Slugs are correctly deferred to
live design-time verification, never hardcoded from this page. (3) Spend on the two cheapest frozen
probes across two families is cents against the $5/day cap. (4) No pending result is contingent on
ladder outcomes today, because no ladder data exists (A4b is correctly `contingent-on` this
decision and panel-v1 stays primary). (5) The default does **not** smuggle a result: it frames
capability-scaling as an open scope measurement ("grow, shrink, or hold"), where either direction
is informative — yardstick-fixing, not result-seeking.

**The one gap that became a binding condition.** The reviewer verified directly that the `ladder`
fence the decision presupposes **does not yet exist**: there is no result-page template file, and
`ladder` appears nowhere in `tools/senselint.py`, `tools/build-index.py`, or the front-matter schema
(which knows only `type/id/title/status/contingent-on/links/meaning-senses`). So "supplementary,
never merged into panel-v1" is today a prose promise, not a fence, and a ladder row could quietly be
cited to widen panel-v1's n or family coverage — exactly the failure both reviewers feared.
**Therefore adoption is conditioned:** A4b's first sub-step must add a `ladder: true` front-matter
field on every ladder result and a senselint check that (a) flags a missing flag on a ladder run and
(b) forbids any `supports`/`anchors` link from a ladder-flagged page into a panel-v1 claim/result
unless separately ratified. No ladder result page may be written before that gate lands.

**Two riders recorded into the resolution.** "Extend only if the first runs are clean" means
*execution*-clean (no reasoning-token truncation per the [`config/models.md`](../../../config/models.md) Gemini caveat), never
*result-direction*-clean. And within-family siblings are deliberately *correlated*, so ladder rows
must never be pooled with the cross-family panel-v1 to claim broader decorrelation — they answer a
different (scale) question in a fenced lane.

`resolved-by: autonomous (adversarial review)`.
