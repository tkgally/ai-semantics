---
type: conjecture
id: commutative-convention
title: LLM referential conventions are (so far) commutative — order-invariant and set-based, not path-dependent; the aggregation-vs-constitution distinction
meaning-senses:
  - relational
  - distributional
status: proposed
contingent-on: []
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: depends-on
    target: result/relational-reference-game-v1
  - rel: depends-on
    target: concept/relational-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: supports
    target: open-question/relational-meaning-pilot
---

# Conjecture: the commutative convention (aggregation, not constitution)

> **Status: proposed (2026-05-31). The project's own forward, deflationary bet on the relational axis.** It generalizes a single, **bounded, pilot-scale null** — [`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), which the result page itself flags as **under-powered for order effects** — into a directional claim, names the distinction that makes the pilot's "coordination, not constitution" verdict precise, and states the sharp test that would overturn it. This is a **conjecture, not a settled claim**, and it does **not** assert that LLMs are *unable* to constitute meaning relationally; it bets only that the observed order-invariance *persists*, and it hands the loop the experiment that could falsify that bet. The v1 result it builds on is `contingent-on` a yardstick **still pending Tom** ([`decisions/open/relational-pilot-operationalization`](../../decisions/open/relational-pilot-operationalization.md)); ratifying that yardstick would fix the *measure*, never the *result*, and never this generalization of it.

## Statement

Across the three family-decorrelated panels in the relational pilot, a coined referential convention was recovered by a fresh matcher from the **content-set** of the prior turns — the *bag* of what was said — and **not** from their **ordered trajectory**. This conjecture names and sharpens that pattern:

> **LLM referential conventions are, so far, *commutative*.** A fresh agent's interpretation of a coined term is (within the pilot's power) **invariant under reordering** of the interaction record whose content it conditions on: shuffle the prior turns, reverse them, or present them in their true chronology, and interpretation does not reliably change. The convention behaves as a function of the *set* of prior turns ("a bag of turns"), not of the *path* that produced them. It is therefore **order-invariant / set-based**, not **path-dependent**.

"Commutative" is used in its plain algebraic sense: the operation that maps prior-turn content to a recovered convention does not depend on the order in which the turns are combined, just as `a + b = b + a`. The claim is **behavioral and bounded**, not a claim about the model's internals: it says the *recovered convention* is, at the grain the pilot can measure, an order-insensitive function of shared content.

## The distinction that makes "coordination, not constitution" precise — aggregation vs. constitution

The pilot's verdict — *coordination, not constitution* — turns on a distinction this conjecture supplies a name for. The two are **operationally separable** exactly by commutativity:

- **AGGREGATION (commutative).** A convention is **computed inside each agent** from the shared content and then **aggregated** across agents (two systems independently arriving at the same label from overlapping evidence). Because each agent's computation conditions on a *content set*, scrambling the order of that content leaves the result unchanged — the aggregated convention is **commutative**. This is the deflationary reading [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) predicts: two next-token predictors conditioned on overlapping recent context converge from co-occurrence content, "a convergence that survives order-scrambling" ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), §Headline).

- **CONSTITUTION (non-commutative).** A convention **constituted *between*** agents would be one whose content "exists in the interaction and not antecedently in either party" ([`concept/relational-meaning`](../../base/concepts/relational-meaning.md), §intro). There, the **live order** of the exchange — the particular sequence of repairs, partial acceptances, and refinements, and of *which* precedent got fixed *when* — is part of what the convention *is*. Such a convention would be **non-commutative**: reordering the trajectory would change the recovered interpretation, because order carries disambiguating information the content-set alone does not.

So the pilot's deflation has a precise shape: **the relational convergence the pilot observed is aggregation (commutative), not constitution (non-commutative).** This is the relational analogue of the project's running constructional discipline — "a distributional pass is not a constructional pass" ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), §Headline): coordination and convention-*use* are real, but they are the floor the deflationary distributional story already predicts, and only a *non-commutative* surplus would climb the second ladder. This page **names and sharpens** that surplus into the commutative/non-commutative contrast; the axis itself and its discriminating measure are defined on [`concept/relational-meaning`](../../base/concepts/relational-meaning.md) and [`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md), which this conjecture **complements rather than duplicates**.

## The evidence it generalizes (verified — numbers not altered)

From [`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), across **all three** homogeneous-dyad panels (`claude-sonnet-4.6`, `gpt-5.4-mini`, `gemini-3.5-flash`):

- **History content is load-bearing.** Giving the matcher the record lifts accuracy well above the opaque nickname alone: `coined_only → ordered` lift **+0.25 … +0.42** (clustered-bootstrap CIs; the lift is clearly positive for all three, so the order test is interpretable, not a methodological artifact).
- **Order is *not* load-bearing.** The `ordered − shuffled` gap is **+0.06 … +0.11**, and **no model's clustered-bootstrap CI excludes 0**.
- **Not chronology-specific.** The coherent `reversed` arm is **≤ random `shuffled`** in every cell (claude reversed 0.750 < shuffled 0.833; gemini 0.750 < 0.806), so even the small positive order-gap point estimates are order-insensitive noise around a content-driven baseline, not a trajectory effect.
- **Convergence without entrainment (the run's one anchored, human-comparison finding).** The dyads reach near-ceiling referential *accuracy* but keep expression length roughly constant (~8.5–10.8 words), whereas the human Hawkins dyads *compress* (length 7.73→4.10 words, accuracy 0.78→0.94 over repetitions) — convergence without human-like compression. This secondary finding is anchored to [`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md).

In the aggregation/constitution vocabulary: content lifts interpretation (the convention *uses* shared content), but order does not (the convention is *commutative* in that content) — the signature of aggregation, not constitution.

## The predicted human contrast (characterized; not in-repo — flagged)

If the conjecture holds, it predicts a **sharp human/LLM contrast at the relational grain**. The human relational convention appears to be **non-commutative**. The most directly relevant human result is **conceptual pacts** — *Brennan, S.E. & Clark, H.H. 1996, "Conceptual pacts and lexical choice in conversation," Journal of Experimental Psychology: LMC 22(6): 1482–1493* — which reports that human lexical entrainment has a **historical** (not merely ahistorical/salience-driven) and **partner-specific** component (as characterized in [`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md) §"Human anchor"; the paper is queued in [`base/wanted.md`](../../base/wanted.md) at P2 and is **not in-repo**, so it is **characterized, not quoted**, and no page number or quotation is attributed here). On that characterization, *which* partner you formed a pact with, and *when* in the history a term got fixed, matter to later interpretation — i.e. the human convention is **path-dependent / non-commutative**. The deflationary backdrop on the same axis — interactive alignment (Pickering & Garrod 2004; also not in-repo; characterization) — frames alignment as "a largely automatic process" of cross-level priming, i.e. coordination without a constitution claim, which is exactly the commutative/aggregation story (again as characterized in [`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md), not quoted). So the conjecture's bet is: **humans (conceptual pacts) are non-commutative; LLM dyads (so far) are commutative.**

This contrast is a *prediction*, not a measured result. The human side is unanchored in-repo (Brennan & Clark 1996 unfetched), and the LLM side is the pilot's own bounded null. The page makes the contrast explicit precisely so that fetching the human anchor and running the v2 perturbation arm could decisively confirm or break it.

## What would confirm / falsify (the bet the loop picks up)

The decisive test is the **history-perturbation arm** already recommended for v2 in [`decisions/open/relational-pilot-operationalization`](../../decisions/open/relational-pilot-operationalization.md) (§"Recommended resolution") and named in the open question ([`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md), §"Conditions"): **reassign a coined term mid-trajectory** (e.g. swap which figure a coined term was first attached to at a chosen point in the order) and test whether a fresh matcher's interpretation tracks ***where* in the sequence the change landed** — *beyond* merely tracking *that* the content changed.

- **Confirms (the deflationary bet holds):** interpretation stays largely **commutative** — a **weak or no position-in-sequence effect** once content is matched. The convention is recovered from the content set regardless of where the perturbation sits. This would extend the v1 null from "order of a static record doesn't matter" to "position of a *live* repair doesn't matter," strengthening the aggregation reading.
- **Falsifies (the first evidence of constitution):** v2 shows a **robust, CI-clean order/position effect** — interpretation tracks *sequence position* beyond content (the matcher's reading shifts in proportion to *where* the perturbation lands, not just whether the altered content is present). That would be the first evidence of a **non-commutative, constituted-between** convention, and the bottom rung of the relational second ladder ([`concept/relational-meaning`](../../base/concepts/relational-meaning.md), §"a second ladder"). The conjecture would be **retired**, and the positive promoted to a candidate relational `conjecture`/claim under the usual contingency discipline.

Two **scope extensions** (not falsification conditions, but where the bet might first break): **image referents** (the Q1→B v2 upgrade — higher ecological validity, a closer tie to the Hawkins paradigm) and **cross-family (heterogeneous) dyads** (two *different* systems with different priors, where a between-agent surplus is more plausible than in the homogeneous-dyad pilot). A non-commutative effect could plausibly appear in those richer settings even if homogeneous text-grid dyads stay commutative — which would *bound* the conjecture rather than overturn it wholesale.

## Candidate anchor (named, per house rules — none claimed)

- The trajectory / commutativity measure is the pilot's own **internal within-model contrast** (`ordered` vs `shuffled`, same model both arms) and is **internal-contrast-only** — it makes **no human-comparison claim**, exactly as ratified for the relational line in [`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md) and stated in [`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md) (§"Anchor discipline"). So a v2 commutativity result would carry **no resource anchor obligation** for the order measure itself; it would be a within-model contrast.
- [`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md) anchors the **human convergence / entrainment baseline ONLY** (the "convergence without compression" secondary finding), **not** the trajectory/commutativity measure — its page states explicitly that the live-vs-shuffled trajectory measure is "novel to the LLM probe and unanchored by any human resource."
- The **human non-commutativity** side of the predicted contrast (the conceptual-pacts comparison) would need **Brennan & Clark 1996** fetched and read into a `source/` page before any human-comparison claim on that contrast could be made; it is queued in [`base/wanted.md`](../../base/wanted.md) (P2) and is not in-repo. Until then the human contrast is a *characterized prediction*, not an anchored finding.

So this conjecture needs **no resource anchor** to stand as a forward bet (it is a within-model directional prediction); the human-contrast *clause* carries an explicit anchor IOU naming Brennan & Clark 1996.

## Interpretive note — convergence from a shared distributional substrate (links to holism)

The commutative/aggregation reading sits comfortably with a holist picture of the panel ([`concept/semantic-holism`](../../base/concepts/semantic-holism.md)). That three separately-trained systems (different makers) **converge on a usable convention recovered from shared content** is, as that page notes, "the kind of cross-system commonality strong holism predicts should be unavailable" — but it is marked there as **INTERPRETATION, not a holism test**, and "the deflationary reading actually fits holism comfortably: shared distributional substrate → overlapping webs → convergence, no shared *content* in the strict atomist sense required" ([`concept/semantic-holism`](../../base/concepts/semantic-holism.md), §"What the project's own findings say about it"). Cross-model convergence from a shared distributional substrate is therefore *consistent with* the commutative/aggregation story, not extra evidence for constitution: overlapping training-distribution webs would produce convergent, order-insensitive conventions without anything being constituted *between* the agents. This conjecture inherits that page's caution — the convergence is **suggestive, not decisive**, and its force points toward deflation, not toward settling either holism or constitution.

## Honesty box

- **Generalizes a bounded null.** The v1 result detects only **large, consistent** order effects (n=12 coined terms/model, 2 games, 6 figures); a *moderate* real trajectory effect could read as this null. The result page's own honest claim is "*direction and absence-of-large-effect*, not a precise zero" ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), §Caveats). This conjecture is a **forward bet that the pattern persists under the sharper v2 test**, not a settled claim that LLMs *cannot* constitute meaning relationally.
- **Yardstick pending Tom.** The v1 result is `contingent-on` [`decisions/open/relational-pilot-operationalization`](../../decisions/open/relational-pilot-operationalization.md) (text-grid referents; order-isolating `ordered`-vs-`shuffled` headline; monologue floor). Ratifying that yardstick fixes the *measure*, never the *result*, and never this generalization. (The null itself stands as a first-class negative regardless, because a null does not over-claim.)
- **A possibly-too-easy probe.** The opaque-nickname setting may simply not be one where ordered history *can* carry disambiguating information beyond its content ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), §Caveat 2). The perturbation arm is designed to create exactly such a setting, which is why it — not a rerun of v1 — is the decisive test.
- **Modest framing.** Per the charter, this is a **deflationary** bet written under-claimed: it predicts persistence of an order-invariance already observed, names the one experiment that would overturn it, and makes the human contrast it predicts explicit and falsifiable rather than assumed.
