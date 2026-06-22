---
type: claim
id: lexical-graded-scale-ungraded-commitment
title: "On human-rated usage-similarity-midpoint pairs, panel models place the pair at an intermediate relatedness position but meet it with clear-item confidence and almost never decline — a graded scale with ungraded commitment (behavioral; usage-similarity-capped)"
meaning-senses:
  - distributional
  - referential
  - human-comparison
status: supported
anchor: resource/dwug-usage-graphs
contingent-on: []
created: 2026-06-22
updated: 2026-06-22
links:
  - rel: supports
    target: essay/graded-scale-ungraded-commitment
  - rel: refines
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: result/lexical-bridging-context-v1
  - rel: depends-on
    target: result/lexical-bridging-context-working-surface-v1
  - rel: anchors
    target: resource/dwug-usage-graphs
  - rel: depends-on
    target: resource/wic-word-in-context
---

# Claim: graded scale, ungraded commitment (lexical, behavioral)

> **Status: supported (2026-06-22, session 77; channel-checked session 79).** Supported by a
> direct test, [`result/lexical-bridging-context-v1`](../results/lexical-bridging-context-v1.md)
> (3/3 panel models, clear-class precondition met), and the channel-artifact alternative named
> below has since been tested:
> [`result/lexical-bridging-context-working-surface-v1`](../results/lexical-bridging-context-working-surface-v1.md)
> re-ran the probe under a **working surface** (format-only, reasoning held constant) and found
> the commitment null is **largely channel-CONTROLLED, not a forced-format artifact** — it
> survives a genuinely-used working surface for gemini, and the **categorical-decline** half holds
> for every model that took up the channel; the one crack is claude's **self-reported confidence**
> (it softens under reflection, CI-strict lower), and gpt **declined** the surface (inconclusive).
> So the claim stands with a sharpened scope: the *categorical-commitment* component is
> channel-controlled; the *self-reported-confidence* component is partly channel-sensitive (claude).
> Direction-of-effect at small, lemma-clustered N — not a coverage claim.

## Statement

On usage pairs of a target word that **humans rated as usage-similarity midpoints**
(DWUG within-period DURel 2–3, ≥3-rater; the "bridging" class), all three panel models
(claude-sonnet-4.6, gpt-5.4-mini, gemini-3.5-flash):

1. place the pair at an **intermediate relatedness position** — between their
   clearly-same and clearly-different behavior, inside a pre-frozen [40,60] band (the
   **graded scale**, within-item); **and**
2. meet that same ambiguous item with **clear-item-level confidence**, **almost never**
   take an explicit "UNCLEAR" option (decline rate ≈0, not elevated over clear items),
   and show **near-zero dispersion** across forced re-samples (the **ungraded
   commitment**).

In short: the panel's gradience lives in the *ordering across items*, not in its
*epistemic posture on the single ambiguous item*. "Gradience in the ledger, none in the
moment."

## Scope and caps (binding)

- **Usage-similarity, not sense co-presence.** A DWUG mid-scale pair is a human-rated
  usage-similarity midpoint, **not** a certified within-sense bridge (it may be a homonym
  halfway-point, register/topic drift, or annotator noise). The claim is about behavior on
  *usage-similarity-midpoint* items only.
- **Behavioral, not representational.** A statement about what the models *do*, not about
  graded sense *representations*.
- **Small, lemma-clustered N** (24 bridging pairs / 17 lemmas): direction-of-effect, wide
  per-lemma uncertainty, nothing beyond these lemmas/register/framing.
- **The commitment null is the robust part.** It is corroborated by three independent
  commitment instruments (self-reported confidence B, categorical decline C, forced-pick
  dispersion A). The *position* (scale) reading is the part qualified by the bound-but-weak
  Q3 topic control (relatedness partly tracks topic similarity, r 0.32–0.53).

## Human anchor

Anchored to [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md): the
graded, multi-rater (≥3) DURel human signal certifies *which* pairs are usage-similarity
midpoints (the bridging class) vs the clear poles, so "the models are not less committed on
the items humans found intermediate" is a genuine human comparison (capped to
usage-similarity). The clear poles are supplemented by
[`resource/wic-word-in-context`](../../base/resources/wic-word-in-context.md) binary gold.
The clear-class precondition was met on all three models, so the result is anchored, **not**
`internal-contrast-only`.

## What would change this

- A larger, lemma-disjoint bridging set showing a robust confidence drop / elevated decline
  on bridging items (graded commitment) would **contest** the claim.
- A representational probe could show graded commitment at the representation grain even
  where behavior is ungraded — orthogonal, not a contradiction (the claim is behavioral).
- Evidence that the ungraded-commitment pattern is an artifact of the working channel
  (single-token output) rather than the relation — c.f. the
  [`output-channel-confound`](../essays/output-channel-confound.md) line on the modal/
  let-alone axis — would bound it. **This test has now run**
  ([`result/lexical-bridging-context-working-surface-v1`](../results/lexical-bridging-context-working-surface-v1.md)):
  the pattern is **largely channel-controlled**, not an artifact, so this would-change-it
  route is mostly closed — with the residual that claude's *self-reported confidence* component
  is partly channel-sensitive. A future probe showing the **categorical-decline** half (not just
  a self-report number) crack under a genuinely-used wide channel would still bound the claim.
- A larger, lemma-disjoint bridging set, or an uptake-induced re-run for gpt (which declined the
  working surface here), would widen the channel check beyond the two models that took it up.
