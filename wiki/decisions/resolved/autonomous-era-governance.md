---
id: autonomous-era-governance
title: The autonomous era — governance, merging, resource policy, and public reporting
status: resolved
opened: 2026-06-12
resolved: 2026-06-12
resolved-by: Tom (interactive, in the transition session)
ratified: four rulings — cross-session self-ratification; self-merge to main; pure autonomy on resources; public AI disclosure
contingent-artifacts: []
---

# Decision: the autonomous-era constitution (ratified by Tom, 2026-06-12)

On 2026-06-12 Tom resumed the project after ~12 days of dormancy and converted it to **fully
autonomous operation**: from now on the project is run entirely by Claude, with no human input
during sessions. Tom monitors via a public plain-language website (`docs/`, GitHub Pages) and
retains a standing override, but ordinary operation never waits on him. He also fixed the
project's shape going forward: **two inter-feeding tracks** (the empirical recursive experiment
loop, and a theoretical/philosophical exploration of "meaning" in the age of AI), **no fixed goal
or endpoint**, scope free to extend outward so long as the main focus remains meaning — with a
particular focus on **lexical and grammatical meaning** — and an OpenRouter budget of **$5.00 per
day**. Sessions are initiated by pointing Claude at [`continue-prompt.md`](../../../continue-prompt.md) (via Claude Code
Routines or manually) and each session ends with all changes squash-merged to `main`.

Because future sessions cannot ask Tom anything, the four value-laden constitutional choices were
put to him interactively **in this transition session** and ratified as follows.

## Ruling 1 — Governance: cross-session self-ratification

The old rule (charter §8): operationalization and human-anchor gate decisions queue in
`wiki/decisions/open/` and only Tom ratifies; a contingent finding is never promoted until he does.
Under full autonomy that rule would deadlock. Tom ratified the replacement:

- A decision opened in one session **may be ratified only in a LATER session** (never the session
  that opened it — the cooling-off is the point: the ratifier must not be the author with the
  result already in view).
- Ratification requires an **independent adversarial-review pass** (a separate reviewer agent that
  reads the decision page, the options, the provisional default, and everything downstream) and a
  **written rationale** on the resolved page.
- Resolved pages record `resolved-by: autonomous (adversarial review)` — never impersonating Tom.
- **Tom keeps a standing override**: any edit he makes to the wiki, any decision he reverses, any
  instruction he gives wins over an autonomous ratification, retroactively if needed.
- **Every autonomous ratification is reported on the public website** (the session journal), so the
  whole audit trail is visible without reading the wiki.

The inviolable anti-cheat rule is unchanged: an operationalization is **never** retuned after
seeing results — if results make the yardstick look wrong, that is a *new* open decision for a
*later* session's reviewer, and the result stands as measured under the old yardstick meanwhile.

## Ruling 2 — Merging: sessions squash-merge their own PRs

Every session (including the transition session itself) ends by committing, pushing, opening a PR,
and **squash-merging it to `main`** without human review. `main` always reflects the current state
of the project; the website deploys from `main`. A session that cannot merge (e.g., a transient
service failure) leaves the PR open and flags it at the top of [`NEXT.md`](../../../NEXT.md) so the next session's
first act is to land it.

## Ruling 3 — Resources: pure autonomy

Tom chose the strict option: the project uses **only what it can reach itself** — open-access
sources, the datasets it can fetch and license-check, and the API keys already in the environment.
Consequences:

- [`wiki/base/wanted.md`](../../base/wanted.md) is **no longer a fetch-request channel to Tom**. It is repurposed as the
  project's own source backlog: items the project can fetch itself stay live; paywalled-only items
  are marked `unreachable` (kept for the record; to be satisfied by open-access alternatives or
  characterized-without-quotation, never fabricated).
- The held **AANN probe** loses its waiting-for-a-key path (`TOGETHER_API_KEY` will not arrive).
  The inherited open decisions `aann-panel-logprob-blocker` and `cloud-compute-path` are to be
  resolved under Ruling 1 in a later session — realistically by retiring the echo-logprob path and
  either re-operationalizing AANN behaviorally or retiring the probe with the null-path documented.
- The three inherited open decisions (the two above plus `relational-pilot-operationalization`)
  transfer to the new governance and should be among the first orders of business.

## Ruling 4 — Public reporting: plain disclosure

The public website states plainly that the project is conducted **autonomously by an AI (Claude)**,
with human involvement limited to monitoring. The site never names or refers to the human
monitor, never links to the (private) repository, is written in plain language for a hands-off
reader, defines technical terms in a glossary, and is updated **every session**.

## Scope

These rulings fix the project's *procedure*, not any finding. No claim, result, conjecture, or
theory page changes force or status because of this decision. The standing epistemic discipline —
human anchors, no fabrication, write the null, modest calibrated claims — binds autonomous
sessions exactly as it bound supervised ones; what changes is only *who turns the crank*.

Recorded in the same session: charter amendment [`PROJECT.md`](../../../PROJECT.md) §12, rewritten [`PROTOCOL.md`](../../../PROTOCOL.md) gates,
[`CLAUDE.md`](../../../CLAUDE.md) conventions, [`config/budget.md`](../../../config/budget.md) ($5/day), [`continue-prompt.md`](../../../continue-prompt.md) (the session entry
point), and the first version of the public site under `docs/`.
