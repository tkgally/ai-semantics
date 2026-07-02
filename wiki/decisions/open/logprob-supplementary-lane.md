---
id: logprob-supplementary-lane
title: Reopen a narrowly-scoped 2-family logprob lane as a supplementary graded instrument (premise change on aann-panel-logprob-blocker)?
status: open
opened: 2026-07-02
opened-by: special session (Tom-directed program adoption; program item A4d)
contingent-artifacts: []
---

# Decision: a supplementary logprob lane on changed premises

**Opened by the 2026-07-02 special session** implementing
[`program-2026-07-adoption`](../resolved/program-2026-07-adoption.md) (review item A4, logprob
paragraph). **Eligible for cross-session ratification from session 168** ([`PROJECT.md`](../../../PROJECT.md) §12.3);
Tom may rule at any time.

## Premise-change statement (why this is not a re-litigation)

[`decisions/resolved/aann-panel-logprob-blocker`](../resolved/aann-panel-logprob-blocker.md)
(resolved 2026-06-12) **retired the logprob instrument-class for AANN** because the *primary*
ratified indicator (Option A: per-token surprisal of a *provided* string) was verified
uncomputable on OpenRouter for any model, and the surviving fallback (Option B: next-token
logprob of a prompted judgment token) existed only on a 2-family panel (Alibaba/Qwen +
OpenAI/gpt-4o-class — its 2026-05-29 live check found `qwen/qwen3.7-max` and
`openai/gpt-4o`/`gpt-4o-mini` exposing logprobs via the existing key) that had been declined
as degraded for *that* probe. That ruling stands and is not re-opened for AANN's primary
indicator.

What is new here: (1) the question is a **supplementary graded lane for minimal-pair batteries
generally** — a different, weaker role than "AANN's primary indicator" (supplementary = runs
beside the forced-choice instrument, flagged, never the verdict-bearer alone); (2) the
capability facts are a **2026-05-29 snapshot, now five weeks stale** — providers and the
catalog drift, so the premise must be re-verified live before anything runs.

## The question

Forced-choice is the bluntest instrument on exactly the lines where gradedness is the finding
(the AANN acceptability gradient; minimal-pair batteries such as a BLiMP sweep, program item
A3b). Should the project stand up a **narrowly-scoped supplementary lane** — next-token-logprob
continuation-likelihood measures on the (re-verified) logprob-capable families — explicitly
flagged as **degraded decorrelation** (≤2 families), to sharpen graded comparisons where the
panel's forced-choice instrument saturates?

## Options

- **A — Re-verify, then pilot (provisional default).** Step 1: a $0/near-$0 live re-check of
  which OpenRouter models expose logprobs under the existing key (recorded with date in
  [`config/models.md`](../../../config/models.md)). Step 2 (only if ≥2 decorrelated families survive): one pilot on one
  already-frozen minimal-pair battery, results written as supplementary, flagged
  `logprob-lane, degraded decorrelation (n families = k)`, never sole support for a verdict.
  Step 3: return here with pilot evidence before any wider use.
- **B — Reject.** The 2-family ceiling makes the lane permanently un-decorrelated; keep
  forced-choice only, and leave graded sharpening to the (Tom-held) surprisal-key lever
  ([`cloud-compute-path`](../resolved/cloud-compute-path.md)).
- **C — Adopt as a full instrument class.** Rejected in advance as the provisional stance:
  ≤2-family decorrelation cannot carry primary verdicts under charter §6, and adopting it as
  primary *would* re-litigate the blocker.

## Provisional default and rationale

**A.** It buys the sharpest available graded signal at near-zero cost, inside an explicit
degraded-decorrelation flag that keeps charter §6 honest; the re-verify step keeps the stale
snapshot from silently becoming a premise; and the supplementary-only scope keeps the retired
AANN ruling intact.

## What ratification must check (for the reviewer)

That the re-verify step precedes any run and is recorded with its date; that "supplementary,
never sole support" is enforced in the result template; that the pilot target is an already-
frozen battery (nothing designed around the new instrument before it is admitted); and that
nothing in this lane touches the retired AANN Option-A ruling.
