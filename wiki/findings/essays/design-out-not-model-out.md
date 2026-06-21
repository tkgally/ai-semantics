---
type: essay
id: design-out-not-model-out
title: Design it out, do not model it out — why a control covariate that is degenerate within the condition of interest must be fixed at construction time, not at analysis time
meaning-senses:
  - constructional
  - functional-vs-formal
  - model-internal
status: draft
contingent-on: []
created: 2026-06-21
updated: 2026-06-21
links:
  - rel: depends-on
    target: resource/subtlex-us-frequency
  - rel: depends-on
    target: conjecture/function-word-substitutability
  - rel: refines
    target: essay/point-estimate-is-a-draw
  - rel: refines
    target: essay/output-channel-confound
---

# Essay: design it out, do not model it out

> **Status: draft (2026-06-21). A philosophical-track / methodological essay arguing in the project's
> own voice.** Its original contribution is a single design-epistemics rule and the principled line that
> bounds it: **a control covariate that is degenerate — zero-variance, hence perfectly collinear — within
> the condition of interest cannot be "controlled for" by regression or stratification; it must be designed
> out at construction time, not modelled out at analysis time.** The rule is methodological, not a finding
> about any model: it is a claim about how behavioral probes of grammatical/constructional meaning have to
> be *built*. It is anchored in one worked case from the project's own record — the function-word-vs-content
> swap probe, where the orthographic length-delta is constant (+1) in the function arm and therefore cannot
> be regressed out — but the rule it draws is general. It contains **no new empirical claim** and makes
> **no human comparison**: the probe it reads is `internal-contrast-only`, and every empirical sentence
> cites the in-repo page that carries it, at that page's stated strength. Read the revision triggers before
> citing.

## The occasion

The cleanest object the project has produced for this question is a piece of *failed* statistical
reasoning that an adversarial review caught and reversed. The function-word-vs-content swap probe asks
whether substituting one function word for another (which shifts a grammatical/constructional relation)
flips a model's inference more readily than substituting one content word for another at matched frequency
and length. The build needed two things at once that pulled against each other: ≥200 faithfully matched
items, and a length match tight enough that a "length-only reader" — a degenerate strategy that looks only
at how many characters the swap added — could not reproduce the function-vs-content asymmetry on its own.

A reviewer proposed the natural-looking relief. Reaching ≥200 under a *hard* length match was expensive
and starved the item supply, so why not relax the hard match and instead **regress length-delta out of the
flip-rate contrast as a covariate** — the standard, auditable move when a nuisance variable threatens a
comparison? That is
[`decisions/resolved/function-word-count-vs-matching`](../../decisions/resolved/function-word-count-vs-matching.md)'s
Option B, and the page admitted it as the provisional default, on a plausibility prior: *"a 1-character
length change is not a credible alternative explanation for an inference flip, and moving it from a hard
freeze-gate to an auditable analysis-time covariate is standard practice."*

The provisional default was overturned, and the reason it was overturned is this essay's seed. The function
arm is **degenerate in length**. Every named function swap lengthens the word by exactly one character:
the decision page records *"every named function swap lengthens the word by exactly one character —
`because`→`although`, `some`→`every`, `will`→`would`."* So within the condition of interest — the function
swaps — the length-delta is not a variable at all. It is the constant +1. And a covariate that is constant
within a condition cannot be controlled for *with respect to that condition*.

## Why a degenerate covariate cannot be controlled out

This is textbook perfect collinearity, but it is worth stating concretely because the intuition that "you
can always regress out a nuisance" is so strong that the failure mode hides in plain sight.

Take the two analysis tools the relaxation offered — stratification and regression — and run each against
the degenerate covariate, exactly as the overturn re-derived it from scratch.

- **Stratify by length-delta.** You would split the items into a Δlen=+1 stratum and a Δlen=0 stratum and
  read the function-vs-content contrast within each. But the function arm lives *entirely* in the +1
  stratum; there are no Δlen=0 function swaps. So the Δ0 stratum — the length-neutral content items the
  relaxation was supposed to add — *"has no function counterpart, so it carries no function-vs-content
  contrast."* The bearing contrast survives only in the +1 stratum, and that stratum *"is the build-v1
  set"* — the original hard-matched set. Stratifying collapses the relaxation back to the thing it was
  supposed to relax. The new items never enter the comparison they were added to support.

- **Regress length-delta out as a covariate.** A linear model with terms for condition (function vs
  content) and for length-delta identifies the condition coefficient only off variation where the two are
  not collinear. Since length-delta is constant within the function arm, the model *"identifies the
  condition coefficient only off the +1 stratum"*; the Δ0 content items *"inform only the length slope,
  never the contrast."* Again the length-neutral items the relaxation promised to recruit *"never enter the
  bearing contrast."*

The conclusion the overturn drew is exact and general: *"a covariate that is constant within the condition
of interest cannot be controlled for with respect to that condition."* The relaxation *"buys no valid
supply and strictly weakens the freeze-time guard"* — it loosens the build-time defense against the
length-only reader while delivering none of the items it was sold on. Worse, the plausibility prior that
licensed it ("a 1-character change can't matter") was a prior the build had already *refuted* empirically:
the first certification pass measured a length-only reader reproducing nearly the whole asymmetry, *"length-only
asymmetry 0.46 before the fix, 0.00 after."* As the page puts it, *"a plausibility prior the build itself
refuted; it cannot ground the yardstick."*

So length stayed a **hard freeze-time gate** — a per-pair signed-Δlen equality enforced at construction —
and the supply problem was solved a different way: by **widening the function-word inventory** at unchanged
tolerances plus a capped dose of carrier authoring. The control was designed out, not modelled out.

## The general rule, and where the line actually sits

Strip the case down. There is a manipulation (the condition of interest) and a nuisance covariate you wish
were not confounded with it. The standard toolkit — stratify, regress, match-on-the-fly — works *only when
the covariate varies within the condition*. When the covariate is **degenerate within the condition**
(zero variance, or near-zero variance: perfectly or nearly collinear with the manipulation), there is no
within-condition variation off which to identify the covariate's effect separately from the manipulation's.
Analysis cannot separate what construction fused.

> **The design-out rule.** When a nuisance covariate has (near-)zero within-condition variance — when it is
> (nearly) collinear with the manipulation — it cannot be controlled for at analysis time by regression or
> stratification. It must be controlled at **construction time**: designed out by matching the stimulus
> set so the nuisance is constant *across* conditions (so it cannot separate them), or balanced so it
> varies *within* each condition. "Control for it statistically" is available only when the covariate
> already varies inside the condition you are testing; otherwise the only honest control is a design choice
> made before any data exists.

The line is not "design always beats analysis." It sits precisely at within-condition variance. Three
regimes:

- **Covariate varies within the condition (the comfortable case).** Regression and stratification work as
  advertised; statistical control is legitimate and often preferable, because it preserves stimulus supply
  that a hard match would throw away. Most textbook covariate adjustment lives here. The function-word probe
  *frequency* match is partly here: frequency does vary, so a tolerance band (|ΔLg10WF| ≤ 0.10) plus
  reported residuals is a coherent control even though it, too, is partly enforced at construction.

- **Covariate has tiny-but-nonzero within-condition variance (the genuinely hard middle).** This is where
  the rule needs honesty rather than a slogan. A *little* variance does in principle let you regress — but
  the estimate of the covariate's effect rests on that sliver of variation and is correspondingly fragile,
  high-variance, and easy to fool yourself about. The right reading is not "design-out is mandatory" but
  "the burden of proof shifts hard toward construction": you may model it out only if you can show the
  residual is one the degenerate-strategy reader cannot exploit, and that the sliver of variance is real
  signal, not rounding. In the function-word case the variance was not tiny, it was *zero* (+1 with no
  spread), which is why the case is clean and decisive rather than a judgement call.

- **Covariate is degenerate within the condition (the case that forces the rule).** Zero within-condition
  variance, perfect collinearity. No analysis can control it relative to the manipulation. Design it out or
  abandon the contrast. There is no third option.

The function-word probe is valuable precisely because it is the clean extreme — it makes the line visible
in the flesh. Most confounds in behavioral probing are not this stark; the rule's everyday use is the
*diagnostic*: before reaching for "we'll regress it out," check the within-condition variance of the thing
you mean to regress. If it is degenerate, the regression is a comforting no-op at best and a guard-weakening
move at worst.

## Why this is a project-level point, not a probe-local one

The project's recurring work is operationalizing the **constructional / distributional** contrast — and,
more broadly, the lexical-vs-grammatical-meaning question — into behavioral indicators. The function-word
probe is one such operationalization: it tries to isolate *grammatical/constructional* bearing (function
words shift inferential relations) from *lexical/distributional* bearing (content words shift co-occurrence
neighborhoods), holding frequency and length fixed. The seductive error the overturn caught is the belief
that a clever analysis can rescue an operationalization that construction did not isolate. It cannot, when
the confound is fused into the condition by design.

This is the through-line. A behavioral probe of machine meaning is only as clean as its *stimulus set*, and
the stimulus set is fixed before the model is ever queried — frozen and hashed, in this project's
discipline, exactly so that no analysis-time choice can be back-fitted to a result. Once the set is frozen,
any confound that is collinear with the manipulation *within* that set is permanent: it is in the bones of
the instrument, and no covariate column added later can extract it. The decision page's binding conditions
say as much operationally — length *"is not demoted to a covariate,"* the length-only-reader asymmetry
*"must stay 0.0,"* and if the count cannot be reached at the unchanged tolerances the correct move is
*"a further deferral / new decision, not relaxing a control or lowering the bar."*

So the rule is a sibling of two existing essays about the limits of post-hoc reading. It **refines**
[`essay/point-estimate-is-a-draw`](point-estimate-is-a-draw.md): that essay says a single-run number cannot
be made precise by re-reading a within-run interval, because the missing uncertainty (run-to-run jitter) is
*outside* what the interval models; this essay says a confound cannot be removed by adding a covariate
column, because the missing variation (within-condition spread of the nuisance) is *outside* what the
regression can use. Both are "the analysis cannot manufacture information the design did not put there."
It also **refines** [`essay/output-channel-confound`](output-channel-confound.md): that essay names a
degree of freedom of the instrument that must be *varied* to be read; this one names a degree of freedom
that must be *fixed* to be read. They are two faces of the same discipline — the instrument has parameters,
and which ones you freeze and which you vary is a design decision that analysis can neither make nor undo.

## The cost of the rule (so it is not sold as free)

Design-out is not a free lunch, and the function-word probe shows the bill in the flesh. Forcing a nuisance
to be constant across conditions, or balanced within them, **constrains the stimulus inventory** — it
throws away every otherwise-usable item that does not also satisfy the match. The decision page documents
the collapse precisely: under the full simultaneous match the high-yield *"person-noun route dies
entirely,"* the *"`the`→`a` determiner swap admits NO frequency-matched content control at all,"* and
*"only ~13 distinct content swap-out words survive matching,"* topping out near *"80"* items against a
≥200 target. That is the operationalization-vs-power tension in concrete numbers: every tightening of a
construction-time gate that buys validity costs supply, and supply is what powers the test.

So the rule does not say "always design it out at any cost." It says: *when the covariate is degenerate
within the condition, design-out is the only valid control, and its cost in supply is a real cost to be
paid honestly* — by widening the manipulation's inventory (more function-word pairs), by capped authoring,
and, if the bar still cannot be met, by deferring rather than by quietly demoting a gate to a covariate
that cannot do the job. The temptation to relax is strongest exactly when the design is most expensive, and
that is exactly when the degeneracy check matters most, because the relaxation on offer is usually the
collinear no-op.

## What this essay is not

- **Not a finding about any model.** Its contribution is a design-epistemics rule. The probe it reads has
  no model output yet and is `internal-contrast-only`; nothing here asserts how an LLM treats function
  words.
- **Not a claim that statistical control is generally suspect.** The reverse: it sharpens *when* covariate
  adjustment is valid (within-condition variance present) and *when* it is a collinear illusion (degenerate
  within the condition), leaving ordinary covariate control untouched in its proper regime.
- **Not "design always beats analysis."** The line sits at within-condition variance, and the genuinely
  hard middle (tiny-but-nonzero variance) is acknowledged as a judgement call, not a slogan.
- **Not a human comparison.** The rule is about how to construct the project's own behavioral instruments;
  it asserts nothing about humans and owes no resource anchor for its original argument (every empirical
  sentence it leans on cites the in-repo decision page at that page's stated strength).

## Revision triggers (read before citing)

- **(a) A worked case where tiny-but-nonzero within-condition variance is exploited honestly.** If a probe
  in this project (or an ingested source) shows a nuisance with small but real within-condition variance
  being regressed out *and* the residual demonstrated unexploitable by a degenerate-strategy reader, the
  essay would **sharpen** the middle regime from "burden shifts hard to construction" into a concrete
  standard for how much variance, and what residual check, licenses model-out. The core rule (degenerate ⇒
  design-out) is unaffected; only the line's middle gets operationalized.
- **(b) A demonstration that a frozen confound *can* be repaired post-hoc.** If a method (e.g. a principled
  re-weighting or an instrumental-variable design) were shown to remove a within-condition-collinear
  confound from an *already-frozen* set without re-construction, the essay's strong claim ("permanent once
  frozen") would need narrowing. Nothing in-repo licenses that; the freeze-and-hash discipline assumes the
  opposite.
- **(c) The build-v2 set ships and the inventory-widening fails to reach the bar.** If widening the
  function-word inventory at unchanged tolerances cannot reach ≥200 / ≥4-class, that is the cost of the
  rule biting harder than expected. The essay would not be *wrong* — deferral is its prescribed move — but
  it would gain a worked example that design-out can price a contrast out of feasibility entirely, which
  the cost section should then carry more prominently.
- **(d) A source that locates the line differently.** If a methodological source argues the degenerate-covariate
  case admits a valid analysis-time control this essay denies, ingest it and re-derive; the present argument
  rests on a from-scratch re-derivation inside one decision page, not on an external methodology literature,
  and that is the place it is weakest.

## Honesty box

- The essay's **original** contribution is the design-out rule and its line: a covariate degenerate
  (zero/near-zero within-condition variance, hence collinear) within the condition of interest cannot be
  controlled at analysis time and must be designed out at construction time; the line sits at
  within-condition variance, with a genuinely hard tiny-but-nonzero middle; design-out has a real supply
  cost. No empirical claim here is new.
- The strongest empirical sentences leaned on, at their stated strength, all from
  [`decisions/resolved/function-word-count-vs-matching`](../../decisions/resolved/function-word-count-vs-matching.md):
  *"every named function swap lengthens the word by exactly one character — `because`→`although`,
  `some`→`every`, `will`→`would`"*; *"a covariate that is constant within the condition of interest cannot
  be controlled for"* (the page's phrasing: *"a covariate that is constant within the condition of interest
  cannot be controlled for with respect to that condition"*); the +1 stratum *"is the build-v1 set"* and the
  Δ0 stratum *"has no function counterpart, so it carries no function-vs-content contrast"*; regression
  *"identifies the condition coefficient only off the +1 stratum"* and the Δ0 items *"inform only the length
  slope, never the contrast"*; the relaxation *"buys no valid supply and strictly weakens the freeze-time
  guard"*; *"length-only asymmetry 0.46 before the fix, 0.00 after"*; *"a plausibility prior the build itself
  refuted; it cannot ground the yardstick"*; the supply-collapse figures (*"person-noun route dies
  entirely,"* *"the `the`→`a` determiner swap admits NO frequency-matched content control at all,"* *"only
  ~13 distinct content swap-out words survive,"* *"80"* vs the ≥200 target); and the binding conditions
  (*"is not demoted to a covariate,"* must stay *"0.0,"* *"a further deferral / new decision, not relaxing a
  control or lowering the bar"*). Nothing here outruns those.
- **No human comparison** is made or owed: the rule governs construction of the project's own LLM probes,
  the worked probe is `internal-contrast-only`, and the essay's original argument is methodological, so it
  carries no resource anchor obligation (the frequency resource it mentions,
  [`resource/subtlex-us-frequency`](../../base/resources/subtlex-us-frequency.md), is cited only as the
  probe's matching floor, not as an anchor for any human-comparison claim).
- **Provenance note (weaker than page-level).** The methodological literature on perfect collinearity and
  covariate degeneracy is textbook, but the essay deliberately rests its *general* rule on a from-scratch
  re-derivation recorded in one in-repo decision page rather than on an ingested external methods source.
  That is the essay's weakest provenance point and is named as revision trigger (d).
