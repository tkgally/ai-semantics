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
updated: 2026-06-14
links:
  - rel: depends-on
    target: result/relational-reference-game-v1
  - rel: depends-on
    target: concept/relational-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: supports
    target: open-question/relational-meaning-pilot
  - rel: depends-on
    target: source/brennan-clark-1996-conceptual-pacts
---

# Conjecture: the commutative convention (aggregation, not constitution)

> **Status: proposed (2026-05-31). The project's own forward, deflationary bet on the relational axis.** It generalizes a single, **bounded, pilot-scale null** — [`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), which the result page itself flags as **under-powered for order effects** — into a directional claim, names the distinction that makes the pilot's "coordination, not constitution" verdict precise, and states the sharp test that would overturn it. This is a **conjecture, not a settled claim**, and it does **not** assert that LLMs are *unable* to constitute meaning relationally; it bets only that the observed order-invariance *persists*, and it hands the loop the experiment that could falsify that bet. The v1 yardstick was **ratified 2026-06-12** (autonomous cross-session adversarial review, [`decisions/resolved/relational-pilot-operationalization`](../../decisions/resolved/relational-pilot-operationalization.md)); the ratification fixed the *measure*, never the *result*, and never this generalization of it.

## Statement

Across the three family-decorrelated panels in the relational pilot, a coined referential convention was recovered by a fresh matcher from the **content-set** of the prior turns — the *bag* of what was said — and **not** from their **ordered trajectory**. This conjecture names and sharpens that pattern:

> **LLM referential conventions are, so far, *commutative*.** A fresh agent's interpretation of a coined term is (within the pilot's power) **invariant under reordering** of the interaction record whose content it conditions on: shuffle the prior turns, reverse them, or present them in their true chronology, and interpretation does not reliably change. The convention behaves as a function of the *set* of prior turns ("a bag of turns"), not of the *path* that produced them. It is therefore **order-invariant / set-based**, not **path-dependent**.

"Commutative" is used in its plain algebraic sense: the operation that maps prior-turn content to a recovered convention does not depend on the order in which the turns are combined, just as `a + b = b + a`. The claim is **behavioral and bounded**, not a claim about the model's internals: it says the *recovered convention* is, at the grain the pilot can measure, an order-insensitive function of shared content.

## The distinction that makes "coordination, not constitution" precise — aggregation vs. constitution

The pilot's verdict — *coordination, not constitution* — turns on a distinction this conjecture supplies a name for. The two are **operationally separable** exactly by commutativity:

- **AGGREGATION (commutative).** A convention is **computed inside each agent** from the shared content and then **aggregated** across agents (two systems independently arriving at the same label from overlapping evidence). Because each agent's computation conditions on a *content set*, scrambling the order of that content leaves the result unchanged — the aggregated convention is **commutative**. This is the deflationary reading [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) predicts: two next-token predictors conditioned on overlapping recent context converge from co-occurrence content, "a convergence that survives order-scrambling" ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), §Interpretation).

- **CONSTITUTION (non-commutative).** A convention **constituted *between*** agents would be one whose content "exists in the interaction and not antecedently in either party" ([`concept/relational-meaning`](../../base/concepts/relational-meaning.md), §intro). There, the **live order** of the exchange — the particular sequence of repairs, partial acceptances, and refinements, and of *which* precedent got fixed *when* — is part of what the convention *is*. Such a convention would be **non-commutative**: reordering the trajectory would change the recovered interpretation, because order carries disambiguating information the content-set alone does not.

So the pilot's deflation has a precise shape: **the relational convergence the pilot observed is aggregation (commutative), not constitution (non-commutative).** This is the relational analogue of the project's running constructional discipline — "a distributional pass is not a constructional pass" ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), §Headline): coordination and convention-*use* are real, but they are the floor the deflationary distributional story already predicts, and only a *non-commutative* surplus would climb the second ladder. This page **names and sharpens** that surplus into the commutative/non-commutative contrast; the axis itself and its discriminating measure are defined on [`concept/relational-meaning`](../../base/concepts/relational-meaning.md) and [`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md), which this conjecture **complements rather than duplicates**.

## The evidence it generalizes (verified — numbers not altered)

From [`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), across **all three** homogeneous-dyad panels (`claude-sonnet-4.6`, `gpt-5.4-mini`, `gemini-3.5-flash`):

- **History content is load-bearing.** Giving the matcher the record lifts accuracy well above the opaque nickname alone: `coined_only → ordered` lift **+0.25 … +0.42** — a positive point estimate for all three models (the claude and gemini lift CIs touch 0 at the lower bound; the interpretability gate is point-estimate-based, as the result page's caveat 7 discloses).
- **Order is *not* load-bearing.** The `ordered − shuffled` gap is **+0.06 … +0.11**, and **no model's clustered-bootstrap CI excludes 0**.
- **Not chronology-specific.** The coherent `reversed` arm is **≤ random `shuffled`** in every cell (claude reversed 0.750 < shuffled 0.833; gemini 0.750 < 0.806), so even the small positive order-gap point estimates are order-insensitive noise around a content-driven baseline, not a trajectory effect.
- **Convergence without entrainment (the run's one anchored, human-comparison finding).** The dyads reach near-ceiling referential *accuracy* but keep expression length roughly constant (~8.5–10.8 words), whereas the human Hawkins dyads *compress* (length 7.73→4.10 words, accuracy 0.78→0.94 over repetitions) — convergence without human-like compression. This secondary finding is anchored to [`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md).

In the aggregation/constitution vocabulary: content lifts interpretation (the convention *uses* shared content), but order does not (the convention is *commutative* in that content) — the signature of aggregation, not constitution.

## The predicted human contrast (revised 2026-06-12 — partner leg now citable; order leg still open)

If the conjecture holds, it predicts a **sharp human/LLM contrast at the relational grain**. The human relational convention appears to be **non-commutative** — but the in-repo ground for that "appears" must now be stated in two parts, because the conceptual-pacts primary source was fetched and read 2026-06-12 ([`source/brennan-clark-1996-conceptual-pacts`](../../base/sources/brennan-clark-1996-conceptual-pacts.md)), and it grounds **less than the earlier characterization implied**:

- **Grounded (citable): historicity and partner-specificity.** Brennan & Clark 1996 shows human lexical entrainment is **historical** (speakers keep pact terms even when a plain basic-level word would do) and **partner-indexed** (Experiment 3: term retention 48% with the same matcher vs 18% with a switched matcher; pacts are established jointly). *Which partner* a pact was formed with matters to later interpretation — that much of the human side is now anchored, in-page quotes and pagination included.
- **Not grounded (still a characterization): order-sensitivity.** The paper never perturbs interaction *order*, and its own analysis cuts the other way for the sequence dimension: "Frequency of use better explains our data than does simple recency" (p. 1492) — frequency being an **order-insensitive** statistic of the history. So the leap from "historical and partner-specific" to "**path-dependent / non-commutative**" is **not licensed by this source**. Human order-sensitivity at the grain the pilot probes (would a human matcher's interpretation change under a shuffled record?) remains untested in-repo.

The deflationary backdrop on the same axis — interactive alignment (Pickering & Garrod 2004; not in-repo; characterization via [`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md), not quoted) — frames alignment as largely automatic cross-level priming, i.e. coordination without a constitution claim, which is exactly the commutative/aggregation story. So the conjecture's bet now reads, more carefully: **humans form partner-indexed, historical pacts (anchored); whether the human convention is additionally *order-sensitive* — the precise contrast with the LLM dyads' commutativity — is an open empirical question on both sides of the contrast.**

This contrast remains a *prediction*, not a measured result: the human side is anchored only on the partner/historicity leg, and the LLM side is the pilot's own bounded null. If anything, the frequency-over-recency finding **softens the presumption that humans must come out non-commutative** — which makes the predicted contrast a genuinely open bet rather than a foregone conclusion, and is recorded here as the exercise of this page's own revision discipline rather than smoothed over.

## Update 2026-06-12 — the decisive test ran once: INCONCLUSIVE (bet survives an attempt, unstrengthened)

The history-perturbation arm ran as
[`result/relational-history-perturbation-v2`](../results/relational-history-perturbation-v2.md)
(PREREG frozen after an independent pre-run critic pass; independent post-run verifier, zero
mismatches). **Pre-registered verdict, all three models: INCONCLUSIVE/MIXED.** The falsification
clause did **not** fire (no model tracked stated chronology in both presentation-direction
arms), and the commutative null was **not** certified either (claude shows a CI-clean
forward-arm elevation that vanishes when chronology and prompt position are decoupled — where
it points anywhere, it points at *physical prompt position*, not chronology). So this
conjecture **stays `proposed`: neither falsified nor meaningfully strengthened.** Do not cite
the v2 run as the bet "holding" — only as the bet surviving a first, power-limited attempt
whose most solid product is methodological (chronological recency and prompt-positional recency
must be de-confounded by design; the direction-control arm is now the house pattern). The
decisive test remains open pending truncation-proof elicitation, better-certified stimuli, and
more clusters.

## Update 2026-06-13 — the decisive test ran again on a clean instrument: still INCONCLUSIVE

The v2 verifier's five-item fix-list was implemented and the test re-run as
[`result/relational-history-perturbation-v3`](../results/relational-history-perturbation-v3.md)
(PREREG frozen post-critic; independent post-run verifier, zero mismatches). The fixes worked
mechanically — **0 truncation, 0 NA, strict-compliance 1.000**, and gemini reached full power
(gate 0.92, 7/9 clusters, both pre-registered trial-floors passed). **Verdict: INCONCLUSIVE/MIXED
again** for the two informative models (gemini, claude); gpt is a **METHODOLOGICAL NULL** (1/6
clusters — stimulus quality still its weak point). The clean read (gemini) shows a strong
**forward** chronology elevation (ρ_chron 0.780, CI excludes 0.5) that **does not survive
direction reversal** (reversed ρ_chron CI lower bound exactly 0.500). The verifier **corrected a
first-pass over-claim**: this is *not* evidence for "physical position over chronology" — a
position-following account predicts the reversed ρ_phys above 0.5, but it collapses to exactly
0.500 (chance), and the forward arm cannot separate the two by construction. The defensible
reading is only that **the forward elevation is direction-fragile**: the falsification clause did
not fire (no direction-invariant chronology/position effect) and the commutative null was not
certified. So the conjecture **stays `proposed`** — neither falsified nor strengthened — but the
inconclusiveness is now *located* (a forward-only elevation of unknown origin on a clean
instrument) rather than buried in instrument noise. v4 would need a design that decouples
chronology from position *within* a single arm (a non-adjacent perturbation point).

## Update 2026-06-14 — the within-arm decoupling ran: TEXT POSITION, not chronology (still neither falsified nor certified)

v3 named the fix it could not perform: decouple chronology from text-position *within* a
single arm. [`result/relational-history-perturbation-v4`](../results/relational-history-perturbation-v4.md)
does it — chronology carried by an explicit per-line **round stamp**, the decisive
most-recent line placed **non-terminally**, so "chronologically-latest twin" and
"physically-last-line twin" are crossed **orthogonally** (cov 0, asserted at build; PREREG
frozen post-critic, GO-after-fixes with the stamp-indicator ruled **inside-class**;
independent post-run verifier). **The decoupling worked, and the answer is text position.**
**claude → TEXT-POSITION ARTIFACT** (Δ_pos CI-clean 0.698[0.594,0.804]; Δ_chron null
0.509[0.465,0.556]); **gemini → INCONCLUSIVE/MIXED**, same direction (position-dominant
Δ_pos 0.812, a small late/early asymmetry leaving Δ_chron's CI marginally off 0.5). In the
conflict cells both models pick the physically-last (chronologically-*earlier*) twin ~0.69–0.75
of the time.

Consequences for this conjecture: it **stays `proposed` — neither falsified nor certified.**
**Not falsified:** neither model tracks the stamped chronology (the falsification clause is
chronology-tracking; the models move, if anything, *against* chronology toward physical
position), so no constituted, path-dependent convention appeared. **Not certified:** the
models are **not** content-only — they are strongly **position-driven** (Δ_pos clean in both),
so the commutative null is **not** strengthened. Two further cautions, both binding on how this
is cited: (a) per the pre-run critic's calibration, position-following here is
**indistinguishable from stamp-blindness** — the result is methodological (prompt geometry /
stamp-value neglect), **not** "the models chose to ignore recency"; (b) v4's real product is
the **located confound**: v3's verifier *refused* to assert "physical position over chronology"
because v3 could not earn it, and v4 earns it cleanly — any future recency/chronology probe over
a *linear* prompt must decouple stamped recency from physical position, or it cannot tell "tracks
the latest convention" from "reads the last line." The decisive relational question therefore
remains **open**, now with a known geometry trap to avoid.

## What would confirm / falsify (the bet the loop picks up)

The decisive test is the **history-perturbation arm** already recommended for v2 in [`decisions/resolved/relational-pilot-operationalization`](../../decisions/resolved/relational-pilot-operationalization.md) (§"Recommended resolution") and named in the open question ([`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md), §"Conditions"): **reassign a coined term mid-trajectory** (e.g. swap which figure a coined term was first attached to at a chosen point in the order) and test whether a fresh matcher's interpretation tracks ***where* in the sequence the change landed** — *beyond* merely tracking *that* the content changed.

- **Confirms (the deflationary bet holds):** interpretation stays largely **commutative** — a **weak or no position-in-sequence effect** once content is matched. The convention is recovered from the content set regardless of where the perturbation sits. This would extend the v1 null from "order of a static record doesn't matter" to "position of a *live* repair doesn't matter," strengthening the aggregation reading.
- **Falsifies (the first evidence of constitution):** v2 shows a **robust, CI-clean order/position effect** — interpretation tracks *sequence position* beyond content (the matcher's reading shifts in proportion to *where* the perturbation lands, not just whether the altered content is present). That would be the first evidence of a **non-commutative, constituted-between** convention, and the bottom rung of the relational second ladder ([`concept/relational-meaning`](../../base/concepts/relational-meaning.md), §"a second ladder"). The conjecture would be **retired**, and the positive promoted to a candidate relational `conjecture`/claim under the usual contingency discipline.

Two **scope extensions** (not falsification conditions, but where the bet might first break): **image referents** (the Q1→B v2 upgrade — higher ecological validity, a closer tie to the Hawkins paradigm) and **cross-family (heterogeneous) dyads** (two *different* systems with different priors, where a between-agent surplus is more plausible than in the homogeneous-dyad pilot). A non-commutative effect could plausibly appear in those richer settings even if homogeneous text-grid dyads stay commutative — which would *bound* the conjecture rather than overturn it wholesale.

## Candidate anchor (named, per house rules — none claimed)

- The trajectory / commutativity measure is the pilot's own **internal within-model contrast** (`ordered` vs `shuffled`, same model both arms) and is **internal-contrast-only** — it makes **no human-comparison claim**, exactly as ratified for the relational line in [`decisions/resolved/relational-fetchable-anchor`](../../decisions/resolved/relational-fetchable-anchor.md) and stated in [`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md) (§"Anchor discipline"). So a v2 commutativity result would carry **no resource anchor obligation** for the order measure itself; it would be a within-model contrast.
- [`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md) anchors the **human convergence / entrainment baseline ONLY** (the "convergence without compression" secondary finding), **not** the trajectory/commutativity measure — its page states explicitly that the live-vs-shuffled trajectory measure is "novel to the LLM probe and unanchored by any human resource."
- The **human side** of the predicted contrast: **Brennan & Clark 1996 is now in-repo**
  ([`source/brennan-clark-1996-conceptual-pacts`](../../base/sources/brennan-clark-1996-conceptual-pacts.md),
  fetched and verified 2026-06-12), and it anchors the **historicity + partner-specificity** leg
  of the human characterization. It does **not** anchor human *order-sensitivity* (it never
  manipulates order, and reports frequency-over-recency) — so a human-comparison claim on the
  commutativity contrast itself would still need a human order-perturbation result, which no
  in-repo resource supplies. The earlier anchor IOU is **partly redeemed, and the unredeemed
  remainder is now precisely delimited**.

So this conjecture needs **no resource anchor** to stand as a forward bet (it is a within-model directional prediction); the human-contrast *clause* is anchored on the partner/historicity leg and carries a delimited open question (human order-sensitivity) on the other.

## Interpretive note — convergence from a shared distributional substrate (links to holism)

The commutative/aggregation reading sits comfortably with a holist picture of the panel ([`concept/semantic-holism`](../../base/concepts/semantic-holism.md)). That three separately-trained systems (different makers) **converge on a usable convention recovered from shared content** is, as that page notes, "the kind of cross-system commonality strong holism predicts should be unavailable" — but it is marked there as **INTERPRETATION, not a holism test**, and "the deflationary reading actually fits holism comfortably: shared distributional substrate → overlapping webs → convergence, no shared *content* in the strict atomist sense required" ([`concept/semantic-holism`](../../base/concepts/semantic-holism.md), §"What the project's own findings say about it"). Cross-model convergence from a shared distributional substrate is therefore *consistent with* the commutative/aggregation story, not extra evidence for constitution: overlapping training-distribution webs would produce convergent, order-insensitive conventions without anything being constituted *between* the agents. This conjecture inherits that page's caution — the convergence is **suggestive, not decisive**, and its force points toward deflation, not toward settling either holism or constitution.

## Honesty box

- **Generalizes a bounded null.** The v1 result detects only **large, consistent** order effects (n=12 coined terms/model, 2 games, 6 figures); a *moderate* real trajectory effect could read as this null. The result page's own honest claim is "*direction and absence-of-large-effect*, not a precise zero" ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), §Caveats). This conjecture is a **forward bet that the pattern persists under the sharper v2 test**, not a settled claim that LLMs *cannot* constitute meaning relationally.
- **Yardstick ratified (2026-06-12).** The v1 yardstick (text-grid referents; order-isolating `ordered`-vs-`shuffled` headline; monologue floor) was ratified v1-scoped by autonomous cross-session adversarial review ([`decisions/resolved/relational-pilot-operationalization`](../../decisions/resolved/relational-pilot-operationalization.md)); the result's `contingent-on` was cleared. The ratification fixed the *measure*, never the *result*, and never this generalization. (The null itself stood as a first-class negative regardless, because a null does not over-claim.)
- **A possibly-too-easy probe.** The opaque-nickname setting may simply not be one where ordered history *can* carry disambiguating information beyond its content ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), §Caveat 2). The perturbation arm is designed to create exactly such a setting, which is why it — not a rerun of v1 — is the decisive test.
- **Modest framing.** Per the charter, this is a **deflationary** bet written under-claimed: it predicts persistence of an order-invariance already observed, names the one experiment that would overturn it, and makes the human contrast it predicts explicit and falsifiable rather than assumed.
