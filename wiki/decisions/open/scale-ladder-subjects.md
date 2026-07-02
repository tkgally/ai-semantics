---
id: scale-ladder-subjects
title: May flagship instruments be re-run on within-family capability siblings (size ladders) as supplementary subjects?
status: open
opened: 2026-07-02
opened-by: special session (Tom-directed program adoption; program item A4b)
contingent-artifacts: []
---

# Decision: within-family size ladders as supplementary subjects

**Opened by the 2026-07-02 special session** implementing
[`program-2026-07-adoption`](../resolved/program-2026-07-adoption.md) (review item A4.2).
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
