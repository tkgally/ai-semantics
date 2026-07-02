---
id: presupposition-projection-human-anchor
title: "Adopt which, if any, external HUMAN projection-variability dataset as a human anchor for the presupposition/projection line?"
status: open
opened: 2026-07-02
opened-by: session 168 (program A3a scout)
contingent-artifacts: []
---

# Decision: adopt an external HUMAN projection-variability anchor for the projection line

**Opened by session 168** implementing program item **A3a** (a $0 license-check scout of candidate
human projection-variability datasets). **Eligible for cross-session ratification from a later session
only** ([`PROJECT.md`](../../../PROJECT.md) §12.3); it is **not** ratifiable in the session that opened
it. Tom's standing override outranks any autonomous ratification.

## Why this exists — and how it differs from the already-resolved projection decisions

The project already has **`internal-contrast-only`** ratifications for the projection line —
[`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../resolved/presupposition-projection-internal-contrast-anchor.md),
[`decisions/resolved/projection-trigger-inventory-internal-contrast-anchor`](../resolved/projection-trigger-inventory-internal-contrast-anchor.md),
and [`decisions/resolved/presupposition-accommodation-internal-contrast-anchor`](../resolved/presupposition-accommodation-internal-contrast-anchor.md).
**This decision is different.** Those fixed the *within-model contrast* as needing **no** human anchor
(the results make no human comparison). **This** decision asks the opposite-facing question: **should
the project adopt an external HUMAN projection dataset to build a NEW, additional `human-comparison`
result** — turning the striking conditional-collapse finding into a **quantified model-vs-human
comparison**? Adopting a human anchor here does **not** revisit or reopen the `internal-contrast-only`
status of the existing results; it would create a *separate* human-comparison artifact alongside them.

The prize is real and interesting **in either direction**: the panel's conditional-antecedent
projection collapses across all three models
([`result/conditional-projection-rescue-v1`](../../findings/results/conditional-projection-rescue-v1.md);
[`result/presupposition-projection-v1`](../../findings/results/presupposition-projection-v1.md)). If a
human dataset shows **humans also dip** under the conditional antecedent, the panel *tracks* human
projection variability; if **humans do not dip** where the models collapse, that is a **quantified
divergence** exactly where the semantics literature says projection is robust. Both outcomes are
publishable-as-knowledge (under the project's modest-claims discipline). The
[`result/projection-trigger-inventory-v1`](../../findings/results/projection-trigger-inventory-v1.md)
family-dependence could likewise be compared to human by-trigger variability.

## The question

Adopt which, if any, of the four scouted human projection-variability datasets as a human anchor for
the presupposition/projection line — and under what license precondition? The scouting evidence is in
[`resource/presupposition-projection-human-anchor-scouting`](../../base/resources/presupposition-projection-human-anchor-scouting.md).
**Headline scouting finding: all four candidates are license-UNVERIFIED** (no `LICENSE` file in any
repository; no quotable data-use terms on paper or project page; NOPE's only verifiable license string,
arXiv CC BY-SA 4.0, covers the paper, not the corpus).

## Options

- **A (provisional default): adopt none yet; re-scout the unresolved licenses first.** Because **no
  candidate's license could be verified this session**, adopt nothing. Queue a later, low-$ task to
  verify a license by a route this scout could not use — reading the GitHub API `license` field with a
  repo-scoped token, checking any OSF/Zenodo deposit for an explicit license, or emailing an author for
  terms — and clear the underlying source-text terms for the naturally-occurring corpora (CommitmentBank,
  NOPE). Only a candidate whose data license is *verified* (permissive, or explicitly permitting
  analysis + short verbatim quotation) may then be adopted, via a *further* decision. Meanwhile the
  existing results stay `internal-contrast-only`, unchanged. **This is the default precisely because the
  charter forbids adopting an unverified license as if permissive** (CLAUDE.md; the scout adopts
  nothing).
- **B: adopt CommitmentBank as the target anchor, CONTINGENT on license verification.** It is the only
  candidate covering the **antecedent-of-conditional** with human projection judgments — the exact
  environment behind the project's headline collapse. Adopt it *conditionally*: if and only if a later
  session verifies its data license (and clears the underlying source-text terms), it becomes the anchor
  for a conditional-collapse model-vs-human comparison. Until verified, this collapses into Option A.
- **C: adopt NOPE or MegaVeridicality/Degen-&-Tonhauser for the trigger-inventory / variability leg,
  CONTINGENT on license verification.** NOPE (10 trigger types, explicit per-item human variability) or
  the predicate/variability norms would anchor the
  [`result/projection-trigger-inventory-v1`](../../findings/results/projection-trigger-inventory-v1.md)
  comparison rather than the conditional cell. Same license precondition; until verified, collapses into
  Option A.
- **D: reject an external human anchor for this line entirely.** Judge that no aggregate
  projection-rate comparison is worth the item-mismatch (every candidate is naturally-occurring or
  predicate-norming, none item-matched to the project's authored matched-P-vs-E pairs), and keep the
  line permanently `internal-contrast-only`. This forecloses the model-vs-human upgrade.

## Provisional default and rationale

**Option A — adopt none yet; re-scout the unresolved licenses.** No license was verifiable this
session, and adopting an unverified license as if permissive is exactly what the project forbids. Option
A keeps the door open (a verified license later routes to B or C via a further decision) without
adopting anything on faith, and leaves the existing `internal-contrast-only` results untouched. If a
later session *does* verify CommitmentBank's terms, B is the strongest substantive target because it is
the only candidate matching the conditional-antecedent environment behind the headline finding.

## What ratification must check (for the later reviewer)

Ratification here is **cross-session and autonomous** ([`PROJECT.md`](../../../PROJECT.md) §12.3); a
**fresh agent in a later session** must:

1. **License is genuinely verified, not assumed.** For any candidate promoted past Option A, quote an
   actual license file or explicit data-use statement (not the arXiv paper license; not "no LICENSE
   found"). If it still cannot be verified, Option A stands.
2. **Underlying source-text terms cleared** for naturally-occurring corpora (CommitmentBank, NOPE) —
   the annotation release and the source-text terms are two separate license layers.
3. **The anchor is cited by the specific human feature that bears** — the per-operator (esp.
   antecedent-of-conditional) or per-trigger human projection rate — never by existence alone, and the
   comparison grain (aggregate rate, not item-matched) is stated honestly as a limit.
4. **The existing results stay `internal-contrast-only`.** Adopting a human anchor creates a *new*
   human-comparison artifact; it does **not** reopen or downgrade
   [`result/presupposition-projection-v1`](../../findings/results/presupposition-projection-v1.md),
   [`result/conditional-projection-rescue-v1`](../../findings/results/conditional-projection-rescue-v1.md),
   or [`result/projection-trigger-inventory-v1`](../../findings/results/projection-trigger-inventory-v1.md).
5. **The yardstick, never the result.** Fixing the anchor must be independent of which direction the
   eventual model-vs-human comparison would come out (convergence or divergence are equally acceptable).

## Note on ratifiability

Because this decision is **opened this session (168)**, it is **not ratifiable now**. Only a later
session, via an independent adversarial-review pass with written rationale recorded
`resolved-by: autonomous (adversarial review)`, may ratify — or Tom may rule at any time.
