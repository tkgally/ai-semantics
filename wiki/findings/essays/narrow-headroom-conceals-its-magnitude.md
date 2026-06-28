---
type: essay
id: narrow-headroom-conceals-its-magnitude
title: "The narrow-headroom bet conceals its own magnitude — why prediction 3's truth-condition coincides with its low off-the-shelf measurability, and why that is structural, not bad luck"
meaning-senses:
  - grounded.perceptual
  - distributional
  - referential.sense
status: draft
contingent-on: []
created: 2026-06-28
updated: 2026-06-28
links:
  - rel: refines
    target: conjecture/distributional-saturation-grounding-headroom
  - rel: depends-on
    target: open-question/grounding-magnitude-instrument
  - rel: depends-on
    target: result/vwsd-grounding-headroom-v2
  - rel: depends-on
    target: result/vwsd-grounding-headroom-nlbaseline-regrade-v1
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: refines
    target: essay/headroom-positive-vindicates-the-null
  - rel: refines
    target: essay/audit-brackets-instrument-competence
---

# Essay: the narrow-headroom bet conceals its own magnitude

> **Status: draft (2026-06-28, session 130). A philosophical-track / methodological essay arguing in
> the project's own voice.** Its original contribution is a *self-concealing-prediction* point: the
> grounding-headroom conjecture's "narrow headroom" bet (prediction 3) is a forward claim whose **truth
> would make its own magnitude hard to measure with off-the-shelf resources** — the very condition that
> makes the bet true (concrete depictable words are mostly already text-determined) is the condition
> that makes the residual small *and* the qualifying material rare. The essay argues this is not the
> project's bad luck in failing to find an instrument; it is **entailed by the content of the bet
> itself**, and it sharpens the local "(a)/(b) in tension on VWSD" the magnitude open-question records
> into a *structural* difficulty about prediction 3's measurability. It contains **no new empirical
> claim** and makes **no human comparison**: every empirical sentence cites the in-repo page that
> carries it, at that page's stated strength. **Prediction 3 is UNTESTED** — neither supported nor
> refuted; this essay asserts no number and pre-judges neither a narrow nor a wide residual. It names a
> *reason a bespoke instrument must be built*, not a reason the bet is untestable in principle; the
> first revision trigger is exactly such a build succeeding. Read the revision triggers and honesty box
> before citing.

## The occasion: a bet whose magnitude keeps slipping the instrument

The grounding axis has, this far, a clean *shape* and an unread *size*. The shape — perception moves an
LLM's lexical sense behavior only in the residue the text distribution leaves under-determined — now
has confirming-direction evidence
([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md), 3/3 models in
direction, distraction-controlled). The size — *how wide* that residue is for concrete depictable
words — is the content of prediction 3 of
[`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md),
and two attempts to read it have now stopped short. v2 could not read it because its under-determined
stratum was manufactured; the natural-language-baseline successor designed to fix that was built, frozen,
and deferred when its fluent channel scored **0.438** strict held-out referent-recovery, "still below
the 0.60 floor" ([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)).
The magnitude open-question then surveyed every in-repo candidate and concluded that "**No in-repo
resource is a drop-in magnitude instrument.**"
([`open-question/grounding-magnitude-instrument`](../open-questions/grounding-magnitude-instrument.md)).

Read as a sequence of mishaps, that is a run of bad luck: one confound, one below-floor channel, one
empty cupboard of resources. This essay argues the opposite reading. The difficulty is not a string of
accidents around prediction 3; it is a property *of* prediction 3. The bet, if true, **predicts its own
measurement to be hard with the resources lying around** — and seeing why turns three separately-filed
obstacles into one structural fact.

## The bet, and the two consequences hidden in it

Prediction 3 is a conjunction of a magnitude claim and a reason. The magnitude claim: even in the
under-determined stratum, "the **magnitude** of Δ for concrete, depictable senses should be **modest**"
([`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md),
prediction 3). The reason, stated in the same breath, is the saturation premise: this holds "because
most concrete words a fluent model is worth probing on are already largely text-determined, so the
residual is small" (same page) — the conjecture's general form of which is that "a model fluent enough
to be worth probing has, for most clearly-pictureable words, already extracted the sense-relevant
distinction from text, so the cases where grounding *can* help are a minority, not the rule" (same page,
the saturation premise). That premise is not free-floating: the conjecture rests it on a real positive,
[`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md), where "the text-only
panel's graded sense-relatedness rating strongly rank-correlated with the human DURel median (Spearman
0.60–0.83, in or above the human inter-annotator range)" (as carried by the conjecture). For the
easy/concrete cases, text *carries* the distinction.

Now read off what that conjunction entails for *measuring* the residual. Two consequences are baked in,
and both push toward low measurability with existing resources.

**(i) A small effect reads as a sign long before it reads as a size.** If the residual is narrow, Δ is —
by the bet's own content — a small quantity. A small quantity needs more sensitivity and more power to
be resolved *as a magnitude* than to be resolved *as a direction*. v2 illustrates the asymmetry from the
benign side: its de-referenced channel was, in its own words, an instrument whose magnitude is
"operationalization-inflated," yet the gating *shape* reads cleanly off it regardless — a sign survives
a sloppy instrument. The neighboring [`essay/audit-brackets-instrument-competence`](audit-brackets-instrument-competence.md)
makes the converse half of this point for the instrument: on a magnitude read "the dominant uncertainty
is the instrument's competence." Put the two together and the lesson for prediction 3 specifically is
sharper than either alone: *a narrow effect is the hardest kind to read as a magnitude*, because the
quantity you are trying to size is, by hypothesis, close to the noise — so the bet's truth and the
read's difficulty rise together. The narrower the headroom, the more instrument you need to call it
narrow rather than merely present.

**(ii) The bet's premise makes the qualifying material rare.** This is the deeper consequence, and it is
where the local tension the open-question records becomes structural. To read the magnitude honestly you
need items that meet *all* of the open-question's four requirements at once — in particular a channel
"certified-competent ... on the *specific target items*" (requirement (a)), material where "visual
contrast is present but text separability is not" (requirement (c), quoting the conjecture's positive
cell), and "the de-referencing trap avoided" (requirement (d))
([`open-question/grounding-magnitude-instrument`](../open-questions/grounding-magnitude-instrument.md)).
But the saturation premise *is the claim that such items are a minority*: if concrete depictables are
mostly text-determined, then items where a competent text channel **genuinely** under-determines the
sense, **and** an image can carry it, **and** the channel can still be **certified competent**, are
exactly the rare residual the bet says is rare. The material a clean magnitude read needs is scarce *for
the same reason the magnitude is predicted to be small*. You cannot stock the shelf with under-determined
concrete items off the rack, because the bet is precisely that the rack is full of the determined ones.

So two of the project's obstacles are not independent. The "no drop-in resource" finding and the "narrow
residual" prediction are the same fact seen from two sides: a world in which prediction 3 is true is a
world in which the items that would let you measure it are uncommon.

## Why this forces the de-referencing trap — and why the trap is the bet biting back

The two consequences combine into a characteristic pressure, and naming it is the essay's most concrete
payoff. If under-determined concrete items are rare in nature, an experimenter who wants the residual
"on tap" has two routes. One is to *find or build* a scarce naturally-fine-polysemy graded-image set —
expensive, and not in-repo. The other is to **manufacture** the residual by crippling the text channel:
strip the referent name so that text under-determines the sense on demand. The second route is cheap and
always available — and it is exactly the trap the project has already sprung once. v2's residual is, in
its own first-class words, "partly *manufactured* by stripping referent names," so the run "says nothing
about the **size** of the residual a fluent text channel would leave"
([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md), Headline and Limitation 1); and the
magnitude open-question's requirement (d) forbids precisely this, because de-referencing "is precisely
what inflated v2's residual and made it a shape-only read"
([`open-question/grounding-magnitude-instrument`](../open-questions/grounding-magnitude-instrument.md),
requirement (d)).

Here is the structural point. The pressure *toward* de-referencing is not laziness or a design slip; it
is the bet's own scarcity consequence (ii) pushing back. Because genuinely under-determined concrete
items are rare — as prediction 3 says they are — the path of least resistance to "enough" residual is to
make it artificially, which destroys the magnitude read while leaving the shape read intact. The trap is
seductive *exactly in proportion to how true the bet is*. This is why the open-question's observation
that "Requirements (a) and (b) are in tension on VWSD"
([`open-question/grounding-magnitude-instrument`](../open-questions/grounding-magnitude-instrument.md))
is better read as a *local instance of a structural coincidence* than as a fact about one dataset's
unfortunate vocabulary. On VWSD the tension surfaced as technical/proper-noun targets a fluent
description names by common name, dropping the certified channel below floor. But the general shape — the
material that under-determines a *competent* channel is rare, so you are tempted to under-determine an
*incompetent* one instead — is what prediction 3's content implies on *any* off-the-shelf corpus, not
just this one. The local tension is the structural one wearing VWSD's particular clothes.

## The thesis, stated plainly

> **A self-concealing prediction.** Prediction 3 — "for concrete lexical sense the headroom is narrow" —
> is a forward bet whose **truth-condition coincides with its low off-the-shelf measurability**. The
> condition that would make the bet true (concrete depictable words are mostly already text-determined,
> the saturation premise) is the very condition that makes the residual **small** (so Δ reads as a sign
> long before a size) and the qualifying material **rare** (so under-determination must be either sourced
> from scarce fine-polysemy sets or manufactured by de-referencing — the trap that turns a magnitude read
> into a shape read). The difficulty of measuring the magnitude with existing resources is therefore
> **entailed by the content of the bet**, not an accident of which instruments happen to be lying around.

The bet partly hides its own size from the cheap instruments. Not perfectly — a bespoke instrument can
still read it (see the escape below) — but enough that every off-the-shelf attempt is pushed toward one
of the two failure modes the bet itself predicts: too little signal to size, or a residual manufactured
by crippling text. That is the sense in which prediction 3 "conceals its own magnitude."

## What this is NOT (the load-bearing differentiations)

The neighborhood is dense, and the value of this essay is partly in seeing it is none of its neighbors.
Each distinction is checked against the cited page's own thesis.

- **It is NOT the undischargeable negative.** [`essay/undischargeable-negative`](undischargeable-negative.md)
  is about the impossibility of closing out a capability's *absence* from behavior: "a behavioral probe
  ... can *witness* a capability ... but can **never** close out a capability's *absence*." That is a
  claim about an *unprovable negative universal*. This essay is about the low measurability of a *positive,
  quantitative* prediction — and the mechanism is the reverse: prediction 3's truth makes the effect
  *small* and the material *rare*, so the obstacle is sizing a real positive, not proving an absence. The
  undischargeable negative is undischargeable because behavior under-determines a universal; prediction 3
  is hard to size because its own content shrinks what there is to measure.

- **It is NOT the instrument-corrects-the-hand-read lesson.** [`essay/instrument-corrects-the-hand-read`](instrument-corrects-the-hand-read.md)
  is about an expert eyeball systematically *over-crediting* relative to a frozen strict instrument — a
  point about the epistemics of *estimation* once an instrument exists. This essay is upstream of any
  estimate: it is about the prediction's *content* implying that an off-the-shelf instrument will be hard
  to assemble at all. One essay says "trust the instrument over the eyeball"; this one says "the bet's
  truth is why a fit-for-magnitude instrument is scarce in the first place."

- **It refines, but is not, the shape-not-size essay.** [`essay/headroom-positive-vindicates-the-null`](headroom-positive-vindicates-the-null.md)
  establishes that v2's positive "licenses the **shape**, not the **size**," and leaves the size genuinely
  open as a *question*. This essay supplies the layer that essay does not: *why* the size is structurally
  hard to read — that the openness is not a neutral gap but one the bet's own content widens. Where the
  shape-not-size essay says "size is unknown, here is the test that would settle it," this says "the bet
  predicts that test to be hard to instantiate off the shelf, and here is why." It is a refinement of that
  essay's hinge, not a restatement of its interpretation-fixing argument (which concerns nulls and a
  positive, not measurability).

- **It refines, but is not, the bracketing essay.** [`essay/audit-brackets-instrument-competence`](audit-brackets-instrument-competence.md)
  is about *what a magnitude instrument must do to be trustworthy* — bracket its channel's competence
  between an oracle and a degenerate channel with a two-sided band. That is an instrument-*design*
  prescription, and it assumes you have the material to point the instrument at. This essay is one step
  further upstream: even granting a perfect bracketing band, the bet's scarcity consequence (ii) makes the
  *items* that could fill the band rare, and its small-effect consequence (i) makes the band's verdict
  hard to read as a magnitude. Requirement (a)'s certification problem — the channel "certified-competent
  ... on the *specific target items*" — is a face of the bracketing essay's concern and, in another light,
  of the certifier gap [`essay/no-admissible-certifier`](no-admissible-certifier.md) names; but this
  essay's thesis is neither the band nor the certifier *per se*. It is the **self-concealing structure**
  that makes both of those harder for prediction 3 specifically than they would be for a prediction whose
  truth did not shrink its own measurand.

- **It does not lean on the distributional sorting.** [`essay/two-distributional-hypotheses`](two-distributional-hypotheses.md)
  sorts which ancestor (Harris vs Firth) a distributional success names. This essay uses the saturation
  premise only as the conjecture states it — text *carries* the concrete-sense distinction for easy cases
  — and makes **no** claim about whether that distributional competence is or is not meaning in any
  reference-involving sense. The grounding question stays exactly where the sorting essay leaves it; this
  essay neither resolves nor re-labels it.

## The escape, and why it is the primary revision trigger

This is **not** "untestable in principle," and saying so is the constructive half of the essay. The
self-concealing structure names a *specific reason a bespoke instrument must be built*: a fine-polysemy
graded-image set on which a competent text channel **genuinely** under-determines the sense (so the
residual is real, not manufactured — requirement (d)), the channel can be **certified** competent on the
specific items (requirement (a)), an image can carry the sense (requirement (c)), and a **graded** human
signal lets Δ be read as a width, not a sign (requirement (b)). The magnitude open-question already names
the build that would meet this — the conjecture's "a fine-polysemy image set ... **not yet in-repo**" —
and flags that, on VWSD, "a **different** magnitude instrument ... may be needed"
([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)).
A resource or build meeting all four requirements that yielded a **clean positive magnitude** would
*discharge* this difficulty entirely: it would show the self-concealment is defeasible by construction,
even if not by off-the-shelf means.

A parallel session-130 empirical scout tested exactly that escape and came back empty: no open-access
resource pairs a graded *word-sense* relatedness signal with disambiguating images, and the one buildable
route needs *per-item graded human sense relatedness over images* — which this project cannot itself
produce, because it runs no new human annotation
([`resource/multimodal-anchor-scouting`](../../base/resources/multimodal-anchor-scouting.md), session-130
deeper scout). So the project-admissible discharge is **not** an in-house build but an **externally
released** resource (or external build) meeting all four requirements that the project could then ingest.
The honest posture is therefore not "prediction 3 cannot be sized" but "prediction 3's size is hard to
read with what is on the shelf — and, on the project's no-new-annotation constraint, not buildable
in-house either — until the right thing is built elsewhere and released." If such a resource lands, this
essay's difficulty is *named and then dissolved* — the better outcome, and the first trigger below.

## Revision triggers (read before citing)

- **(a) A resource or build meeting all four magnitude requirements is found and yields a readable
  positive magnitude.** This is the escape firing. If a fine-polysemy graded-image set — with a competent,
  certified, non-de-referenced text channel and a graded human signal — produces a clean width for the
  residual (narrow *or* wide), the self-concealing difficulty is **discharged**: the essay's claim was
  that the magnitude is hard to read *off the shelf*, not that it cannot be read by a purpose-built
  instrument. The essay is **confirmed and then retired-as-resolved** for that instrument, gaining a
  worked example of the escape. (The parallel session-130 scout found no such resource off the shelf and
  judged an in-house build out of charter reach — so this trigger now awaits an *externally released*
  resource; see the escape above.)
- **(b) The build is attempted and the four requirements prove jointly un-satisfiable** even by a bespoke
  set (e.g. certifying a competent channel always either leaks the gold or drops below floor, on
  fine-polysemy material too). This **strengthens** the essay and pushes it toward the un-measurability
  end: the self-concealment would then look not merely off-the-shelf but robust to construction — at
  which point the essay borders on [`essay/no-admissible-certifier`](no-admissible-certifier.md)'s
  gap and should be re-read against it.
- **(c) The magnitude is read and returns WIDE** (a fluent, certified channel still leaves a large
  residual the image rescues). This does **not** retract the essay — its claim is about *measurability*,
  not about the answer — but it would **refute prediction 3's "narrow headroom" content**, and the
  saturation premise the self-concealment is built on would have to concede a larger ungrounded share of
  concrete lexical sense than the project's prior nulls suggested. The essay's structural argument is
  conditional on the bet; if the bet's magnitude claim is false, the self-concealment was a feature of a
  false premise, and the essay should be re-scoped to "*had* prediction 3 been true, its magnitude would
  have been self-concealing."
- **(d) The magnitude is read and returns NARROW under a certified non-arbitrary band.** This **strengthens**
  the essay twice over: it confirms prediction 3's content *and* vindicates the structural claim, since a
  narrow positive is exactly the small-effect-hard-to-size object consequence (i) describes — its being
  read at all would show the difficulty was real but defeasible by a sufficiently sensitive bespoke
  instrument.
- **(e) A later page cites this essay as proving prediction 3 untestable, or as a *result* about
  headroom.** Either over-reach is itself a trigger: the essay must be re-read to its honesty box, which
  holds the claim at *low off-the-shelf measurability, defeasible by a build*, asserts no magnitude, and
  leaves prediction 3 UNTESTED.

## Honesty box

- The essay's **original** contribution is the *self-concealing-prediction* structure: that prediction 3's
  truth-condition (concrete depictables mostly text-determined) coincides with its low off-the-shelf
  measurability, via two consequences entailed by the bet itself — (i) a narrow effect reads as a sign
  long before a size, and (ii) the saturation premise makes the qualifying under-determined material rare,
  forcing either a scarce bespoke set or the de-referencing trap that destroys the magnitude read. The
  essay generalizes the magnitude open-question's local "(a)/(b) in tension on VWSD" into this structural
  claim about prediction 3's measurability. **No empirical claim here is new, original, or reported.**
- **Prediction 3 is UNTESTED.** The essay asserts no magnitude, no number beyond those it quotes from
  source pages, and pre-judges neither a narrow nor a wide residual. It names a *reason a bespoke
  instrument must be built*, explicitly **not** a claim that the magnitude is untestable in principle; the
  primary revision trigger is such a build succeeding.
- The in-repo facts leaned on, at their stated strength and verified against the source files: prediction
  3's content — "the **magnitude** of Δ for concrete, depictable senses should be **modest** ... because
  most concrete words a fluent model is worth probing on are already largely text-determined, so the
  residual is small" — and the saturation premise — "a model fluent enough to be worth probing has, for
  most clearly-pictureable words, already extracted the sense-relevant distinction from text, so the cases
  where grounding *can* help are a minority, not the rule"
  ([`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md));
  the saturation premise's support — "Spearman 0.60–0.83, in or above the human inter-annotator range"
  (carried by the conjecture from
  [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)); v2's magnitude limit —
  the residual "operationalization-inflated," "partly *manufactured* by stripping referent names," so the
  run "says nothing about the **size** of the residual a fluent text channel would leave"
  ([`result/vwsd-grounding-headroom-v2`](../results/vwsd-grounding-headroom-v2.md), Limitation 1); the
  blocked channel — "0.438," "still below the 0.60 floor," and "a **different** magnitude instrument ...
  may be needed" ([`result/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../results/vwsd-grounding-headroom-nlbaseline-regrade-v1.md));
  and the open-question's four requirements, "Requirements (a) and (b) are in tension on VWSD," and "**No
  in-repo resource is a drop-in magnitude instrument.**"
  ([`open-question/grounding-magnitude-instrument`](../open-questions/grounding-magnitude-instrument.md)).
  Nothing here outruns those.
- **No human comparison** is made or owed. The grounding results cited are gating-shape-on-binary-selection
  or `internal-contrast-only`, and the magnitude is UNTESTED; this essay asserts nothing about people. The
  meaning-sense tags `grounded.perceptual` / `distributional` / `referential.sense` name the axis the bet
  lives on — perceptual grounding of *sense* (Fregean `Sinn`), gated by the text distribution — never
  reference (`referential.externalist` untouched) and never a perceptual symbol system.
- **Single-conjecture provenance.** The structural claim generalizes from **one** in-repo conjecture and
  its two stalled magnitude attempts. It is a *claim about why this prediction is hard to measure*, not a
  proven law about predictions in general; the revision triggers above are the conditions under which it
  strengthens, narrows, or is re-scoped.
