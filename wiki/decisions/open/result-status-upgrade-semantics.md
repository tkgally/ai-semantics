---
id: result-status-upgrade-semantics
title: What does `status: supported` mean on a RESULT page — who may set it, when — and should operative theory pages be `live` rather than `draft`?
status: open
opened: 2026-07-05
opened-by: session-183
contingent-artifacts: []
---

# Decision: result-page status semantics (and the theory `draft`/`live` labeling)

## Why this is owed (surfaced by the s183 wiki-coherence audit)

The schema ([`CLAUDE.md`](../../../CLAUDE.md)) gives results the vocabulary
`proposed | supported | contested | retired` but no *transition rule*. Practice has diverged
silently, in both directions:

- **~10 result pages carry `status: supported` self-assigned at creation** with no in-page
  promotion or replication record (the monotonicity gate/calibration family,
  `third-construction-headroom-harvest-v1`, `addarm-headroom-calibration-v1`, several
  function-word pages) — while the project's *thrice-replicated flagship results*
  (`comparative-correlative-covariation-v1`, `aann-behavioral-gradient-v2`,
  `dative-information-structure-v1`) sit at `proposed`, each stating that what is `proposed` is
  the *reading*, not the numbers. Two independent audit slices flagged the same inconsistency.
- **The operative theory pages** (`constructional-meaning-in-llms-v2`, `situating-llm-meaning-v2`,
  `shadow-depth-table-v1`) all carry `status: draft` although the theory vocabulary has `live`
  and the program describes the v2 editions as the live syntheses. Consistent practice, but
  unexamined.

Nothing here changes any finding; it is pure status semantics. But status fields steer readers
(and future promotion reviews), so the rule is worth fixing once, deliberately, not by drift.

## Options

- **A (provisional default).** *Results:* `status` on a result page describes the **reading's
  lifecycle**, and only a **recorded event** moves it — a dated in-page note naming the session
  and the ground (a replication, a promotion review citing it, or a contested/retired call).
  `supported`-at-creation is deprecated going forward; the ~10 existing pages get a one-line
  dated normalization note **at the next touch of each page** (no mass edit; the note may either
  justify keeping `supported` — e.g. a $0 gate whose "support" is mechanical — or set `proposed`).
  *Theory:* operative syntheses may move `draft → live` at their next substantive touch; a
  `live` page that gains a `supersedes` successor becomes `superseded`.
- **B.** Freeze current statuses as-is and only document the two observed conventions in
  [`CLAUDE.md`](../../../CLAUDE.md) (describe, don't normalize). Cheapest; leaves the flagship-vs-gate inversion
  standing.
- **C.** Mass-normalize now: all un-promoted results to `proposed` in one sweep. Cleanest graph,
  but rewrites ~10 pages' metadata without per-page judgement, and a gate page's `supported`
  arguably *is* the right description of a mechanical check that passed.

## Provisional default

**A** — event-based transitions, deprecation forward, per-page normalization at next touch. It
matches what the flagship pages already do explicitly and costs no churn now. Nothing was changed
in s183 on the strength of this default (the audit's status-related fixes were confined to
front-matter/blockquote *mismatches* on pages whose own text already recorded the event).

## Ratification

Cross-session, per [`PROJECT.md`](../../../PROJECT.md) §12.3: eligible from session 184 —
independent adversarial review + one non-Anthropic panel vote; Tom's standing override outranks.
