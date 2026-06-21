---
type: essay
id: concordant-verdict-hides-spread
title: A concordant verdict still hides a spread — what a panel CONFIRM conceals when effect sizes decorrelate, and the reading discipline that follows
meaning-senses:
  - constructional
  - functional-vs-formal
status: revised
contingent-on: []
created: 2026-06-20
updated: 2026-06-21
links:
  - rel: depends-on
    target: result/dative-information-structure-v1
  - rel: depends-on
    target: result/dative-information-structure-v2
  - rel: depends-on
    target: conjecture/dative-alternation-information-structure
  - rel: refines
    target: essay/capability-split
  - rel: depends-on
    target: open-question/instrument-sensitivity-constructional-inference
  - rel: depends-on
    target: concept/formal-vs-functional-competence
---

# Essay: a concordant verdict still hides a spread

> **Status: draft (2026-06-20). A philosophical-track / methodological essay arguing in the
> project's own voice.** Its original contribution is a *reading discipline*, not an empirical
> claim: when a panel returns a **concordant** verdict — every model clears the bar — the binary
> label "CONFIRM" can still conceal an order-of-magnitude spread in *how cleanly* the models track
> the same constraint, and a reader who stops at the label will over-read "they all do it" into
> "they all do it alike." There is **no new empirical claim** here; every empirical sentence cites
> the in-repo page that carries it, at that page's stated strength. The essay makes **no human
> comparison** of magnitudes (the project has no human effect-*size* anchor for the dative; only the
> *direction* is human-anchored — see the Honesty box). Read the revision triggers before citing.

## The occasion

The sibling essay [`essay/capability-split`](capability-split.md) drew a distinction the project now
relies on: a panel verdict is **CONCORDANT** when every model in the panel cleared the bar, or
**SPLIT** when some did and some did not. That essay's whole argument was about the *split* case — a
one-model positive is an existential, never a panel property, and a split must be reported per-model,
never averaged. It left the concordant case with a single, deliberately permissive line: *"A
concordant verdict may license a cautious panel-scoped sentence."*

This essay takes up exactly that permission and argues it needs a fence. The occasion is the
project's first human-anchored Tier-2 positive of its own design,
[`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md): the
English dative alternation (*Mary gave John the book* / *Mary gave the book to John*) tracks
information structure in **all three** panel models — a clean **CONCORDANT CONFIRM (3/3)**. By the
capability-split rule, this licenses a cautious panel-scoped sentence: *these three models track the
information-structure constraint in the human direction.* That sentence is true and it is the
headline. But it is also coarser than the data, and the gap between the sentence and the data is the
subject of this essay.

## The thing the label hides

Here is what "CONCORDANT CONFIRM (3/3)" sits on top of (main within-item shift, bootstrap 95% CI):

| Model | shift | 95% CI | verdict |
|---|---|---|---|
| gemini-3.5-flash | **+0.524** | [0.495, 0.552] | CONFIRM |
| claude-sonnet-4.6 | **+0.327** | [0.289, 0.359] | CONFIRM |
| gpt-5.4-mini | **+0.056** | [0.023, 0.086] | CONFIRM |

All three clear the pre-registered lower-bound gate; all three are honestly labelled CONFIRM. And
yet the result page states the consequence without softening it: *"The shift spans an order of
magnitude (gemini +0.52, claude +0.33, gpt +0.06)"*, and gpt is *"roughly **one-tenth** gemini's
magnitude"* — a *"weak-but-clearing case"* that *"earns CONFIRM legitimately under the
pre-registered lower-bound gate"*
([`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md), "What the
numbers say", point 3). Three identical labels; a ~9× spread underneath them.

The binary verdict is doing real work — it is the right *gate*, and the pre-registration that fixed
it is what makes gpt's small positive trustworthy rather than a post-hoc rescue. But a binary gate is
a **threshold test**, and a threshold test is by construction blind to everything above the
threshold. "Did the shift clear zero?" returns the same bit for +0.524 and +0.056. The label is a
faithful answer to the question it was built to answer; the error is reading it as an answer to a
question it never asked — *how much*, and *how alike*.

## This was predicted, which is what makes it a finding and not noise

The spread is not an embarrassment to be explained away; it is a registered prediction that came
true. The dative conjecture's third prediction, fixed before any model was queried, reads verbatim:

> *Effect size will vary cross-model in a way that decorrelates from surface accuracy — i.e., two
> models with similar overall benchmark performance can differ in how cleanly they track information
> structure here.*
> ([`conjecture/dative-alternation-information-structure`](../conjectures/dative-alternation-information-structure.md),
> Prediction 3)

The result page records that this *"prediction 3 [is] confirmed"*, and the effect size spanned an
order of magnitude across a panel of frontier models from three different makers. So the magnitude
spread is not measurement slop around a single underlying "track givenness" quantity; it is the
**decorrelation itself** behaving as theorized. The cleanness with which a model tracks a soft,
well-described constraint is, on the conjecture's framing, a *separate axis* from whatever makes it a
capable general model — the two need not move together, and here the per-model magnitudes spread by an
order of magnitude across three frontier-maker panel models (whether that spread is genuinely
decorrelated *from competence* rests on the unmeasured comparable-generalists premise the Honesty box
flags).

That is the load-bearing point. If magnitude tracked general competence, a panel CONFIRM would be
cheap to read: "they all do it, more or less to the degree you'd expect from how good they are." But
under decorrelation, the *amount* a model does it carries information that its *passing* does not, and
that information is exactly what the concordant label discards.

## Two textures of heterogeneity a binary panel label flattens

The dative is the cleanest instance — a single instrument, a single scalar per model, a ~10× spread
hidden under one shared label. It is worth naming that this is not the only way a concordant-looking
verdict can be coarser than its panel. The project's record holds at least one other texture:

- **Magnitude decorrelation on one instrument** (the dative): all models clear the same gate, but
  the *effect sizes* span an order of magnitude and decorrelate from general competence.
- **Convergence heterogeneity across instruments** (the AANN inferential line): all three models
  shift on the forced-choice paraphrase instrument, but only one carries the shift across *every* way
  of asking, while the other two show it on the surface instrument alone — the
  [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md)
  records the named |FC Δ² − NLI Δ²| disagreement flagged for all three models (0.63 / 0.43 / 1.04). There
  the per-instrument verdicts agree at the surface but diverge in *depth*, and the result is reported
  as **PARTIAL** precisely so the depth-difference is not lost.

These are different mechanisms — one is about *how much* on a single instrument, the other about *on
which instruments* — and this essay's clean claim is only about the first. But they share the moral:
a single panel-level label, whether "CONFIRM" or "PARTIAL", is a *summary*, and a summary of a
heterogeneous panel throws away the heterogeneity unless something is built to keep it.

## The reading discipline

The fix is small and continuous with what [`essay/capability-split`](capability-split.md) already
asks. That essay made CONCORDANT-vs-SPLIT a named property of every panel verdict. This essay adds one
clause to the concordant branch:

> **A concordant verdict carries its spread.** When a panel returns CONCORDANT (every model cleared
> the bar), report the **per-model magnitudes alongside the shared label**, and state whether they are
> **tight** (comparable across the panel) or **decorrelated** (spanning a wide range). A concordant
> verdict with a wide magnitude spread licenses the panel-scoped *existence/direction* sentence —
> *"all three models track X in the human direction"* — but it does **not** license a panel-scoped
> *magnitude* sentence — *"the models track X"* read as "to a similar degree", or "the panel tracks X
> at a rate of …". The degree is a per-model quantity, and where it decorrelates, averaging it or
> eliding it manufactures a uniformity the data denies.

Put negatively: the same flattening error capability-split warned against for split panels —
averaging two qualitatively different verdicts into one panel quantity — has a quieter cousin for
concordant panels. There, all the verdicts are the same *bit*, so nothing looks like it is being
averaged; but reading the shared bit as a shared *magnitude* commits the identical error, just below
the resolution of the label. The dative result page already practices the fix — it prints all three
shifts and names the order-of-magnitude spread in the same breath as the CONFIRM. The discipline is to
make that a *rule*, not a courtesy: a concordant label without its spread is an under-reported finding.

This also sharpens what a panel CONFIRM is *evidence for*. It is strong evidence that the behavior is
**available across the panel** — three separately-trained models from three makers all exhibit it, the
strongest kind of "not one model's quirk" the project can assemble. It is *not* evidence that the
behavior is **uniform across the panel**, and under decorrelation those come apart: a robustly
available behavior that every model has, held to wildly different degrees. The first is the headline
the concordance earns; the second is the over-read the spread forbids.

## Why this is a `functional-vs-formal` point, not a scoreboard

A reader could mistake this essay for a quiet ranking — gemini > claude > gpt at the dative. It is
not, and the distinction matters. The spread is a fact about *this constraint on this instrument*, and
prediction 3's whole content is that such a spread **decorrelates from general competence** — so it
cannot be read up into "gemini is the better model" any more than capability-split's one-probe split
could be read into "claude is the stronger composer." A high dative shift is a statement about how
cleanly a model's stated preferences track one information-structure constraint under a working-surface
elicitation; it is silent on the model's competence elsewhere, and the project has no in-repo
cross-task tabulation that would license a ranking (the same refusal capability-split's "thing to
watch" already records).

The functional/formal cut is where the bite lands. Tracking a soft, gradient, discourse-conditioned
preference in the human direction is a *functional* competence — language used to model what is given
vs. new in a discourse — not a *formal* judgment of well-formedness, where the project's panels tend to
sit at ceiling and concord tightly (the AANN formal-acceptability ceiling, where every model sat at the
top, is one in-repo instance — [`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md)).
It is exactly at the functional end that magnitude should be
expected to spread and decorrelate, for the same reason
[`concept/formal-vs-functional-competence`](../../base/concepts/formal-vs-functional-competence.md)
gives that the two competences dissociate. So a concordant CONFIRM at the *formal* end (everyone calls
the well-formed string well-formed) and a concordant CONFIRM at the *functional* end (everyone tracks
givenness, but across a 10× range) are not the same kind of result, and collapsing both to "3/3
CONFIRM" hides precisely the dissociation the project exists to describe.

## Revision log

- **2026-06-21 (session 63), a measurement-level sibling named — no clause changed; honesty-box caveat
  given teeth.** A later result,
  [`result/scivetti-let-alone-powered-rerun-v1`](../results/scivetti-let-alone-powered-rerun-v1.md),
  quantified a **third, distinct** source of variation under a tidy number — not at the level of the
  phenomenon (the two *textures* this essay names — between-model magnitude decorrelation, and
  across-instrument convergence heterogeneity), but one level down, at the level of the **measurement**:
  *within-model run-to-run jitter* at temperature 0 (~12% label churn on a hard near-chance instrument;
  *"a single run's accuracy is a draw"*). This essay's "carry the per-model magnitudes" discipline invites
  a reader to compare small magnitudes like gpt's +0.056 against gemini's +0.524; the new measurement-level
  essay [`essay/point-estimate-is-a-draw`](point-estimate-is-a-draw.md) adds the prior question that
  comparison presupposes — *is the smaller magnitude bigger than its own run-to-run jitter?* — and is the
  home for it. **No clause of this essay's discipline changes** (between-model spread is still carried, and
  the dative was a different, larger, graded instrument than the let-alone NLI on which the ~12% was
  measured, so no dative jitter number exists). What *is* sharpened is the Honesty-box "single run" caveat:
  gpt's +0.056 sits exactly in the small-functional-effect cell where the new finding shows a single-run
  point estimate is least settled — so "wants replication before weight rests on its size" now has a named
  mechanism (run-to-run jitter), and the discipline gains a sibling that asks whether a between-model gap
  could be a within-model draw.
- **2026-06-20 (session 53), trigger (c) exercised → essay strengthened, status `draft`→`revised`.**
  The fresh-item replication
  [`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md) (a disjoint
  32+12-item set, same ratified operationalization) returned the outcome trigger (c) anticipated — and it
  fired in the **strengthening** direction, not the softening one the trigger flagged as a risk. The
  decorrelation did **not** compress: claude (+0.325 vs v1 +0.327) and gemini (+0.500 vs +0.524)
  reproduced almost exactly, while gpt fell from a clearing +0.056 to **+0.018 with a CI that includes
  zero (WEAK)** — so the gemini-to-gpt magnitude ratio *widened* from ≈9× to ≈27×, and the panel verdict
  dropped from a concordant **3/3** to **2/3**. This supplies the essay's sharpest demonstration to date:
  **v1's concordant 3/3 label hid a fragile member** — the single model whose CONFIRM did not survive
  replication. The reading discipline this essay prescribes (report per-model magnitudes; never read a
  shared label as a shared degree) is exactly what would have flagged gpt's order-of-magnitude-smaller
  +0.056 as the CONFIRM to distrust. No clause of the discipline changes; its empirical spine is firmer,
  and the "in strongest form" reading of prediction 3 stands (trigger (c)'s "if a replication compresses
  the spread" condition did not occur). The Honesty-box caveat *"gpt's small positive especially wants
  replication before weight rests on its size"* is now **discharged**: it was checked, and the weight did
  not hold.

## Revision triggers (read before citing)

- **(a) A tight concordant functional positive.** If a future functional-end probe returns a
  concordant CONFIRM with *comparable* magnitudes across the panel (a narrow spread), that would show
  decorrelation is not the default at the functional end — magnitude can concord too — and the essay
  would narrow from "concordant labels generally hide spread at the functional end" to "they *can*,
  and the dative is one case." The discipline (carry the spread) is unaffected either way; only the
  claimed *prevalence* of wide spreads would move.
- **(b) A human magnitude anchor.** The essay is careful to claim no human comparison of *sizes*
  because none is in-repo (only the direction is anchored). If a resource ever supplies a graded human
  effect-*size* for the dative (e.g. the Bresnan & Ford 2010 ratings, ratified an opportunistic
  upgrade only and not used in v1), the per-model magnitudes could be read against it, and "decorrelated
  across models" could be supplemented by "and model M's magnitude is closest to / farthest from the
  human one." Until then, the spread is a within-panel observation, not a human-comparison.
- **(c) Decorrelation fails to replicate.** The dative magnitudes are a single panel / single date /
  single run, and gpt's +0.056 in particular is small and *"wants replication on a fresh item set
  before any weight is put on its size"*
  ([`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md),
  Caveats). If a replication compresses the spread (e.g. gpt's effect grows, or gemini's shrinks),
  the *strength* of "in strongest form" weakens, though the qualitative point — a concordant label can
  hide a spread — survives as long as any non-trivial spread remains. A replication is the cleanest way
  to firm or soften this essay's empirical spine.

## What this essay is not

- Not a new empirical claim — its original contribution is the **carry-the-spread** reading
  discipline for concordant verdicts, an extension of capability-split's CONCORDANT/SPLIT framing.
  Every empirical sentence cites the in-repo page that carries it, at that page's stated strength.
- Not a model ranking — prediction 3's content is that this spread *decorrelates from general
  competence*, so it licenses no "better model" reading; the project has no in-repo cross-task
  tabulation that would.
- Not a human comparison of magnitudes — the dative's *direction* is human-anchored; its
  cross-model *magnitude spread* is not, and no human effect-size claim is made or owed.
- Not a retraction of any past panel-scoped sentence — the dative's headline ("all three track the
  constraint in the human direction") is correct and earns its panel scope; the essay adds what the
  headline should be *read alongside*, not in place of.

## Honesty box

- The essay's **original** contribution is methodological: a concordant panel verdict should carry
  its per-model magnitudes and mark them tight vs. decorrelated; a wide spread licenses the panel-scoped
  *direction* sentence but forbids a panel-scoped *magnitude/uniformity* sentence. No empirical claim
  is original here.
- The strongest empirical sentences supported: on the dative information-structure probe, all three
  panel models CONFIRM (gemini +0.524 [0.495, 0.552], claude +0.327 [0.289, 0.359], gpt +0.056 [0.023,
  0.086]), and the effect size *"spans an order of magnitude"* with gpt *"roughly one-tenth gemini's
  magnitude"* — *"prediction 3 confirmed"*
  ([`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md)). Nothing
  here outruns that.
- **"Comparable general competence" is a background assumption, not an in-repo measurement.**
  The result page speaks of *"two models with comparable general competence"* (point 3); Prediction 3's
  own wording is *"two models with similar overall benchmark performance"*. Either way, the project has
  **not** measured these models' general benchmark competence in-repo. The decorrelation claim rests on
  the (reasonable but unverified-here) premise that three frontier panel models from three makers are
  roughly comparable generalists. The essay's discipline (carry the spread) does not depend on that
  premise; only the sharper gloss "decorrelates *from competence*" does, and it is flagged throughout as
  inheriting the conjecture's framing.
- The AANN convergence-heterogeneity case is cited as a *different* mechanism (across-instrument, not
  within-instrument magnitude), via the
  [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md)
  page; the essay's clean claim is about the dative magnitude case only.
- Single panel / single date / single run; gpt's small positive especially wants replication before
  weight rests on its size. The reading discipline is general; its empirical instance is one probe.
