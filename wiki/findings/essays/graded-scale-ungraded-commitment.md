---
type: essay
id: graded-scale-ungraded-commitment
title: Graded scale, ungraded commitment — why a model can rank-order senses smoothly yet still force every ambiguous use to a confident discrete pick, and why that combination would be a real finding about machine sense
meaning-senses:
  - distributional
  - referential
  - human-comparison
status: revised
contingent-on: []
created: 2026-06-21
updated: 2026-06-22
links:
  - rel: depends-on
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: result/lexical-bridging-context-v1
  - rel: depends-on
    target: result/lexical-bridging-context-working-surface-v1
  - rel: depends-on
    target: open-question/lexical-bridging-context-gradience
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/referential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: refines
    target: conjecture/lexical-sense-gradience
---

# Essay: graded scale, ungraded commitment

> **REVISION (2026-06-22, session 77) — trigger (b) FIRED: the central possibility is now
> realized.** The bridging probe ran ([`result/lexical-bridging-context-v1`](../results/lexical-bridging-context-v1.md))
> and returned exactly the combination this essay named: all three panel models place
> human-rated usage-similarity-midpoint pairs at an **intermediate relatedness position** (the
> within-item echo of v1's scale) yet meet them with **clear-item confidence**, almost never
> take an "UNCLEAR" option, and show near-zero forced-pick dispersion — **graded scale,
> ungraded commitment**, corroborated across all three commitment instruments, clear-class
> precondition met. So "graded scale, ungraded commitment" graduates from a *conceptual fork*
> to a *described feature* of the panel's behavior (scoped to the lemmas/register/instrument
> probed; behavioral, not representational; usage-similarity, not certified sense co-presence).
> The conceptual independence claim (the spine of the essay) is **unchanged and now
> empirically exercised**: v1 had established only the scale, and the probe had to be run to
> find what commitment does — they came apart, as argued. The empirical statement is carried by
> [`claim/lexical-graded-scale-ungraded-commitment`](../claims/lexical-graded-scale-ungraded-commitment.md).
> One honest qualification the probe adds: the *position/scale* reading partly tracks the
> model's own topic-similarity rating (Q3 r 0.32–0.53), the within-item distributional shadow
> this essay flagged as a third outcome — the **commitment** null is the shadow-robust part; the
> scale is the part the bound-but-weak control qualifies. The original argument below stands as
> written; "would" is now "did" for trigger (b).

> **FORWARD NOTE (2026-06-22, session 79) — the channel-artifact alternative was tested, and the
> commitment leg is largely CHANNEL-CONTROLLED.** A reader could object that "ungraded commitment"
> was read off a *cramped output channel* — the model forced to a single label may default to
> confidence it would not voice on a working surface (the
> [`output-channel-confound`](output-channel-confound.md) worry). That control has now run:
> [`result/lexical-bridging-context-working-surface-v1`](../results/lexical-bridging-context-working-surface-v1.md)
> re-ran the same frozen items with a **working surface** (format-only; reasoning held constant).
> Result: the commitment null is **not, in the main, a channel artifact** — it survives a
> genuinely-used wide channel for gemini, and the **categorical-decline** instrument stays ungraded
> for every model that took up the surface. The one place it softens is **claude's self-reported
> confidence** (it drops to a CI-strict-lower number under reflection while its *categorical*
> commitment holds — a self-report shift, not graded commitment); gpt **declined** the surface
> (inconclusive). So "gradience in the ledger, none in the moment" is strengthened on its robust
> (categorical) half and qualified on the self-report half: a model reasoning aloud may *report* a
> lower number on the ambiguous item, yet still *commit* to a discrete pick. The conceptual
> independence of scale and commitment is untouched; what the channel test adds is that the
> commitment leg is mostly real, not an aperture.

> **Status: revised (2026-06-22; draft 2026-06-21). A philosophical-track essay arguing in the
> project's own voice, written *before* the probe that would test it; trigger (b) has since
> fired (see the revision banner above).** Its original contribution is conceptual: it
> argues that a *graded sense scale* (cross-item: the model rank-orders usage pairs the way humans
> do) and *graded sense commitment* (within-item: the model is less sure on the single use that is
> itself ambiguous) are **logically independent**, that the project's v1 result established only the
> first, and that the combination "graded scale, ungraded commitment" — were it to hold — is a
> *substantive* finding about how a model carries sense, not a measurement artifact. There is **no
> new empirical claim** here. The one empirical fact the argument leans on (the v1 cross-item
> monotonicity) is cited at the strength the result page states it, and every human comparison is
> held to the ratified **claim-scope cap**: it is about human-rated *usage similarity*, never
> certified sense co-presence. Read the revision triggers before citing.

## The occasion

The lexical wedge has a `tested` conjecture with one untested prediction. [`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md)
stakes out graded-sense tracking as a directional claim; [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)
supported its central bet, and the polysemy-vs-homonymy arm came back a powered null. Prediction 4 —
deliberately bridging contexts yielding *intermediate, less-confident* behavior — has never run.
[`open-question/lexical-bridging-context-gradience`](../open-questions/lexical-bridging-context-gradience.md)
re-opened the lexical axis on exactly that gap, and the two gates it surfaced (instrument and human
anchor) are now both ratified ([`decisions/resolved/lexical-bridging-context-operationalization`](../../decisions/resolved/lexical-bridging-context-operationalization.md),
[`decisions/resolved/lexical-bridging-context-anchor`](../../decisions/resolved/lexical-bridging-context-anchor.md)).
The probe is buildable; it has not been built.

That is the occasion for this essay. The interval between a ratified design and a run result is the
right moment to state, in the project's own voice, *what is actually at stake in the prediction* —
because the prediction has a first-class null that is easy to mis-hear as a failure, and the whole
point of writing now is to argue that the null would be a finding. The open-question page already
coined the phrase this essay defends: a model "could rank-order pairs perfectly yet still force every
individual ambiguous item to a confident discrete pick; that would be a graded *scale* without graded
*commitment*" ([`open-question/lexical-bridging-context-gradience`](../open-questions/lexical-bridging-context-gradience.md)).
This essay takes that one sentence and argues it names a real fork in how a machine can carry sense.

## The distinction, sharply

Two things go under the single word "gradience," and they are not the same thing.

- **A graded scale** is a *cross-item* property. Lay out many pairs of usages of a word, ask the
  model how related the two senses are, and see whether its answers *rank-order* the pairs the way a
  human relatedness signal does. If unrelated pairs score low, closely-related pairs score high, and
  the in-between pairs land in between — monotonically, across the set — the model has a graded
  scale. The evidence is a correlation over many items.
- **Graded commitment** is a *within-item* property. Take the *one* use that is itself ambiguous —
  a bridging context where two senses are genuinely co-present — and ask whether the model's behavior
  on *that single item* is intermediate and less confident than its behavior on a clearly-same or
  clearly-different use. The evidence is the model's epistemic posture on the item, not its ordering
  of a set.

These come apart cleanly, and the cleanest way to see it is to notice that the scale is built out of
*verdicts*, while commitment is about *the confidence of a verdict*. A model can produce a perfectly
ordered set of confident verdicts. Nothing in "your relatedness ratings rank-order the way humans'
do" entails "and on the genuinely ambiguous item you hedge." A ruler that measures lengths
faithfully is silent on whether it trembles at the midpoint. The scale lives in the *aggregate
ordering*; commitment lives in the *item-level posture*. One is logically free of the other.

The project's own results show the first half of this already. v1 established the scale — and it
established *only* the scale. Its one-line is explicit that the finding is "a *behavioral* rank
correlation (the model rates pairs much as humans do)," that across 200 DWUG EN within-period usage
pairs every panel model's rating is "strongly rank-correlated with the human DURel median," and the
open-question page reads v1 the same way: it "measured gradience as a **cross-item monotonic
correlation** … That establishes the model has a graded *scale*. It does **not** establish that the
model is *uncertain on the items that are themselves ambiguous*"
([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md);
[`open-question/lexical-bridging-context-gradience`](../open-questions/lexical-bridging-context-gradience.md)).
So one side of the fork is in-repo and supported. The other side — commitment — is exactly the unrun
Prediction 4. The essay's claim is that which way that side falls is informative *whichever way it
falls*, and that the two sides are independent enough that the answer is not foreordained by v1.

## The null is a position, not a failure

The first-class null of Prediction 4 is: bridging items are handled with the **same** confidence as
clear items — a forced discrete pick on the very use that is ambiguous. The ratified
operationalization gate states it as "a *within-item* discreteness signal (graded scale, ungraded
commitment) and a clean negative for prediction 4," and binds the reading rule to "make that null
**as legible and reportable as a positive**"
([`decisions/resolved/lexical-bridging-context-operationalization`](../../decisions/resolved/lexical-bridging-context-operationalization.md)).
This essay argues that this is the right posture, and says why the null deserves it.

A model that carried a smooth relatedness scale *and* collapsed every single ambiguous use to a
confident pick would be telling us something specific and surprising about where its gradience lives.
Its gradience would be a property of *the model's behavior over a population of items* — a statistical
regularity recoverable only by aggregating — and **not** a property of its stance on any one of them.
The model would "know," in the distributional, across-the-corpus sense, that *paper*-as-newspaper and
*paper*-as-article are more related than *bank*-riverside and *bank*-financial; and it would
nonetheless meet the actual bridging use — "I left the paper on the train" — with the same untroubled
confidence it brings to an unambiguous one. Gradience in the ledger, none in the moment.

That would be a real fact about machine sense, and the contrast that makes it bite is the
lexicographer's picture. On [`concept/polysemy`](../../base/concepts/polysemy.md)'s account, bridging
contexts "are not anomalies to be disambiguated away; they are the evidence that sense distinctions
are scalar, not binary," and they are exactly where "judgements are genuinely indeterminate." For a
human lexicographer the indeterminacy is **individual**: the bridging use is the one you cannot
cleanly assign, and that local difficulty is *constitutive* of the gradience claim — it is what
"scalar, not binary" means at the point of use. A model with a graded scale but ungraded commitment
would reproduce the lexicographer's *ranking* while not reproducing the lexicographer's *hesitation*.
It would have the map's contour lines without the cartographer's "I'm not sure where the ridge is
here." That dissociation — fine across the set, blunt at the point — is not a degenerate result. It
is a description of a different way of having senses than the human one, and the project exists to
describe exactly such differences rather than to grade the model pass/fail against a human template.

Three disciplines keep this from over-reaching, and they are load-bearing, not hedges:

1. **Behavior, not representation.** This is about what the model *does* on ambiguous items, never
   about graded sense *representations*. v1 led with this caveat — "Monotonicity, not representation
   … it is **not** evidence of graded sense *representations*"
   ([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)) — and the
   bridging probe inherits it. "Ungraded commitment" would be a fact about the model's stated stance,
   not a peek inside it.
2. **Usage similarity, not certified sense co-presence.** The ratified anchor gate caps the human
   side: a DWUG mid-scale / high-disagreement pair certifies a "**human-rated usage-similarity
   midpoint**," and "may **NOT** claim humans certified two senses co-present"
   ([`decisions/resolved/lexical-bridging-context-anchor`](../../decisions/resolved/lexical-bridging-context-anchor.md)).
   So any human comparison this essay's argument licenses is to *usage-similarity* intermediacy. The
   slide from "humans split on how similar these uses are" to "humans found two senses co-present" is
   the one the cap forbids, and the essay forbids it too.
3. **The contrast must clear, or there is nothing to read.** "Less confident on bridging items" is
   only interpretable against clear items the model is confident on; the gate makes a high-confidence
   clear-class a precondition, not a finding. An ungraded-commitment null only means something if the
   model *does* show confidence-spread somewhere — otherwise it is a model that hedges on everything,
   which is a different and duller story.

## Why it matters to the meanings of "meaning"

The fork between scale and commitment is not housekeeping; it bears on what kind of meaning
distributional competence yields. Two threads make this concrete.

First, the **distributional shadow**, here in its within-item form. The deflationary reading of *any*
apparent within-item uncertainty is that the model is unsure on bridging items merely because their
*contexts* are more ambiguous, not because their *senses* are — the lexical-uncertainty analogue of
the [`distributional`](../../base/concepts/distributional-meaning.md) shadow that runs through the
repo. The open-question page makes this the inherited control: "a model could be less confident on
bridging items merely because their *contexts* are more ambiguous, not their *senses*," so any design
carries "a context-similarity / context-ambiguity control measured independently of the model's sense
signal" ([`open-question/lexical-bridging-context-gradience`](../open-questions/lexical-bridging-context-gradience.md)).
This sharpens the essay's stakes rather than threatening them. There are now *three* live outcomes,
not two: graded commitment that survives the context control (the model hesitates on *senses*);
ungraded commitment (the model does not hesitate at all on the single item); and graded commitment
that *evaporates* under the control (the model hesitates on *contexts*, not senses — the
within-item distributional shadow). The middle outcome is this essay's headline possibility; the
third is the deflationary one; and only a control-bearing probe separates them. v1's own context
control was honestly flagged as "model-internal" and "not a fully independent control"
([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)), and the ratified
gate carries the same residual risk forward — so even a clean positive must disclose that the
context control is bound-but-weak and not over-claim sense-tracking.

Second, the **shape of the competence**. There is a long-running question in this project of whether
distributional training recovers the *graded, situated indeterminacy* that human sense exhibits, or
only a coarser same/different discrimination dressed up as gradience by aggregation.
[`concept/referential-meaning`](../../base/concepts/referential-meaning.md) notes that "sense as
position in an inferential/associative web" is close to "what next-token prediction optimizes for";
the fine-grained test is how far that closeness goes. A graded scale shows distributional structure
recovers the *relatedness ordering*. Graded commitment would show it also recovers the *local
indeterminacy* — that the model's *handling* of a single ambiguous use is itself unsettled, the
way a human's hesitation is. Ungraded commitment would bound the recovery: distributional training gets you the
ordering but stops short of the hesitation, locating the model's gradience in the population of its
judgments rather than in any one of them. Either answer is a calibrated statement about a real
boundary of distributional meaning — which is the kind of statement this project is for. Under-claim
is the standing instruction, and the under-claim here is deliberate: the essay asserts only that the
two outcomes are *distinct and both informative*, not that either is more likely.

## What the claim-scope cap forbids me from concluding

It is worth stating the boundary of this essay's own argument as plainly as its content, because the
cap is easy to honor in the abstract and slide past in prose.

- It does **not** conclude that a model with a graded scale "represents senses" — graded or
  otherwise. The whole argument is behavioral.
- It does **not** treat a DWUG-derived bridging item as a certified *sense bridge*. It is a
  human-rated *usage-similarity* midpoint, and "two senses co-present" describes the *concept being
  probed*, never the *certification* of any item
  ([`decisions/resolved/lexical-bridging-context-anchor`](../../decisions/resolved/lexical-bridging-context-anchor.md)).
- It does **not** claim that within-item discreteness here would confirm or disturb clause (b)'s
  powered null. v3 asked whether homonymy forms a *separate discrete regime across strata*; this asks
  whether *single ambiguous items* draw graded commitment. The open-question page is explicit they are
  "complementary, not substitutes."
- It does **not** predict which way the probe will land. The essay's claim is about the *structure of
  the possibility space* — that scale and commitment are independent and the null is substantive — not
  about the outcome.

## Revision triggers (read before citing)

- **(a) The probe returns graded commitment that survives the context control.** If a future
  bridging probe shows bridging items handled at intermediate position *and* lower confidence than
  both clear classes, surviving the inherited context-ambiguity control — i.e. clean within-item
  intermediacy that tracks *sense* indeterminacy, per the per-axis reading rule of
  [`decisions/resolved/lexical-bridging-context-operationalization`](../../decisions/resolved/lexical-bridging-context-operationalization.md)
  — then the model carries graded *commitment*, not just a graded scale. This essay's "scale-without-
  commitment is a live, distinct possibility" stance is then **demonstrated as a fork the model did
  not take**: the two are still shown independent (v1 had to be supplemented to find commitment), but
  the headline possibility did not obtain. The essay would be revised to record that, in this case,
  the human-like outcome held, while keeping the conceptual independence claim intact.
- **(b) The probe returns the null (ungraded commitment).** If bridging items are handled at
  clear-item confidence — a forced discrete pick on the ambiguous use — the essay's central
  possibility is *realized*, and "graded scale, ungraded commitment" graduates from a conceptual fork
  to a described feature of the panel's behavior (scoped to the lemmas/register/instrument probed,
  behavioral not representational, usage-similarity not sense-co-presence). The essay would be
  strengthened, and a `claim` page (anchored or `internal-contrast-only` per the route the probe
  actually ran) would carry the empirical statement the essay here only anticipates.
- **(c) B–C instrument disagreement, or a Route-3 collapse.** If the frozen instrument panel
  disagrees on the dispersion axis (a "mixed/weak" result, *not* the null, per the gate's modification
  3), or the ≥3-rater bridging pool is too thin and the probe collapses to `internal-contrast-only`,
  then no human-comparison claim is licensed and the essay must not be read as one. The conceptual
  independence of scale and commitment survives either way; what weakens is the *empirical
  resolution* with which the fork can be observed.
- **(d) A representational instrument becomes available.** This essay is behavioral by necessity (the
  small-model representation lane stays deferred on local compute, per v1). If a representation-level
  probe of graded sense ever runs, "graded scale, ungraded commitment" would need restating at the
  representational grain, where the behavioral framing here may not transfer — a model's *behavior*
  can be discrete while its *representation* is graded, or vice versa.

## What this essay is not

- Not a new empirical claim. Its original contribution is the conceptual argument that a graded sense
  *scale* and graded sense *commitment* are independent, and that the null combination is a
  substantive finding. The single empirical fact it leans on (v1's cross-item monotonicity) is cited
  at the result page's stated strength.
- Not a prediction of the probe's outcome. The essay maps the possibility space and argues both
  outcomes are informative; it does not bet on which obtains.
- Not a human-comparison of sense co-presence. Every human comparison is capped to *usage-similarity*
  intermediacy by the ratified anchor gate; "two senses co-present" names the concept probed, not any
  certified item.
- Not a representational claim. "Commitment" is the confidence of a behavioral verdict, not a window
  into the model's sense representations.
- Not a re-litigation of clause (b). Between-stratum discreteness (v3's powered null) and within-item
  discreteness (this fork) are complementary, not substitutes.

## Honesty box

- The essay's **original** contribution is conceptual/methodological: graded scale (cross-item
  monotonicity) and graded commitment (within-item item-level uncertainty) are logically independent,
  v1 established only the former, and "graded scale, ungraded commitment" — if a bridging probe finds
  it — would be a substantive behavioral finding about machine sense, with the null reported as
  cleanly as a positive.
- The strongest empirical sentence supported: across 200 DWUG EN within-period usage pairs, every
  panel model's graded sense-relatedness rating is "strongly rank-correlated with the human DURel
  median," a *behavioral* rank correlation that is "**not** evidence of graded sense
  *representations*" ([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)).
  This essay does not state v1's specific correlation magnitudes; it relies only on the qualitative
  fact that a graded scale was established and that it was cross-item and behavioral. Nothing here
  outruns that page.
- **No bridging probe has run.** Prediction 4 is unrun as of this writing; the operationalization and
  anchor gates are ratified but no result exists. Every "would" in this essay is conditional on a
  future probe, by design — the essay is written in the interval between ratified design and run
  result, and claims nothing about the result.
- **The human side is capped.** Any human comparison the argument licenses is to *usage-similarity*
  intermediacy (the ratified anchor cap), never to certified sense co-presence; a DWUG mid-scale pair
  is a usage-similarity midpoint, not a certified within-sense bridge.
- **The context control is bound-but-weak.** v1's own context control was flagged "model-internal"
  and "not a fully independent control"; the bridging gate carries the same residual risk. A graded-
  commitment positive could still be a within-item *context* shadow rather than a *sense* one, and the
  essay's stakes are stated with that limit, not around it.
