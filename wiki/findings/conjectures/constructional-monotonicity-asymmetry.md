---
type: conjecture
id: constructional-monotonicity-asymmetry
title: LLM constructional inference is additive-easy but defeasance-hard (a monotonicity asymmetry)
meaning-senses:
  - constructional
  - inferential
status: tested
contingent-on: []
created: 2026-05-31
updated: 2026-07-05
links:
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: result/caused-motion-minimal-pair-divergence-v1
  - rel: depends-on
    target: result/way-construction-traversal-v1
  - rel: depends-on
    target: result/conative-minimal-pair-divergence-v1
  - rel: depends-on
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: result/monotonicity-within-verbal-battery-v1
  - rel: depends-on
    target: result/coercion-implicit-cue-v2b
  - rel: supports
    target: open-question/instrument-sensitivity-constructional-inference
  - rel: supports
    target: open-question/monotonicity-human-comparison-leg
  - rel: depends-on
    target: result/scivetti-cxnli-answer-key-v1
---

# Conjecture: LLM constructional inference is additive-easy but defeasance-hard (a monotonicity asymmetry)

> **First empirical touch (2026-06-20), NOT a test.** [`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md)
> reports add (caused-motion ∪ way-manner) vs cancel (conative) **base answer-key
> accuracy** on the human Scivetti items: the gaps are small and **inconsistent in
> sign** (claude −0.092 with the conative *highest*, gpt +0.035, gemini +0.021). This
> is **baseline-difficulty-confounded** and is **not** the matched-difficulty /
> ceiling-controlled confirm test this conjecture requires — it confirms nothing and
> falsifies nothing. It is, however, **consistent with** the conjecture's own scope
> statement: the asymmetry is posited for the *de-confounded suppression-with-no-cue*
> arms (the conative-cancel-v2 template), not for base NLI accuracy, where both
> directions sit near ceiling. The conjecture stays `proposed`; the matched-difficulty
> generalization test remains the only thing that can move it.

> **Decisive test now operationalized AND ratified (2026-06-28, session 134) — conjecture
> still `proposed`.** The matched-difficulty generalization battery's design is now a *fixed
> yardstick*: [`decisions/resolved/constructional-monotonicity-generalization-operationalization`](../../decisions/resolved/constructional-monotonicity-generalization-operationalization.md)
> (ADOPT-WITH-MODS, autonomous adversarial review) freezes the pair (**ADD = resultative** vs
> **CANCEL = the *for*-durative aspectual coercion**, a genuinely new pair), the B2 ceiling gate,
> and the frozen reading thresholds (20 pp asymmetry margin; ≥10 pp instrument-fragility margin);
> prerequisite-(1) headroom feasibility was discharged s133 ([`result/addarm-headroom-calibration-v1`](../results/addarm-headroom-calibration-v1.md)).
> This fixes *how* the bet will be tested — it does **not** test it. The conjecture advances to
> `tested` only after the spend-bearing battery runs and is read by the frozen rule, with the
> falsify arms (symmetric, or reversal) live.

> **Decisive test BUILT; cancel arm hit a B2 NO-GO (2026-06-28, session 135) — conjecture
> stays `proposed`, asymmetry NOT read.** The battery was built, frozen, and its B2 ceiling
> gate run ([`result/monotonicity-generalization-b2-nogo-v1`](../results/monotonicity-generalization-b2-nogo-v1.md)):
> the **add arm is buildable at ceiling** (resultative construction 1.00 / control 0.00, 3/3
> models), but the ratified **cancel arm fails the gate structurally** — its "only once"
> default is affirmed at **0.00 in 3/3 models** under both instruments, because
> single-occurrence is a defeasible quantity *implicature*, not a lexical entailment, so a
> strict-NLI default cannot reach the matched ceiling for any semelfactive. Per the frozen
> rule a B2 NO-GO **defers the run rather than relaxing the bar**, so the spend-bearing
> asymmetry was **not run** and **the asymmetry was never read**. A within-frame verb re-pair
> is futile (structural floor); the cancel arm needs a re-design whose default is a
> (near-)entailment at ceiling — surfaced for cross-session ratification in
> [`decisions/resolved/monotonicity-cancel-arm-redesign`](../../decisions/resolved/monotonicity-cancel-arm-redesign.md).
> One honest note this raises for the conjecture's own framing: part of what reads as
> "cancellation is hard" may be that the cancelled inferences the project reaches for are
> implicatures the models never held as entailments (weigh-question 4 of that decision).

> **Cancel-arm re-design RATIFIED (2026-06-28, session 136) — conjecture still `proposed`.** An
> independent fresh-agent adversarial review resolved [`decisions/resolved/monotonicity-cancel-arm-redesign`](../../decisions/resolved/monotonicity-cancel-arm-redesign.md):
> **ADOPT C1 (telic-completion accomplishment cancellation) conditional on its own B2
> default-at-ceiling calibration**, with **C2 (privative-modifier cancellation, requiring a
> deliberate written scope-broadening of this conjecture) as the pre-authorized fallback**, then a
> **principled-limit closure** ("the matched cancel arm is un-instrumentable at ceiling on a
> strict-NLI panel") only if both C1 and C2 fail their B2 gates. This fixes *which cancel coercion to
> try next* plus the unchanged requirement that it clear its own B2 gate before any asymmetry is read
> — it does **not** test the bet. The conjecture advances to `tested` only after a B2-passing cancel
> arm's matched battery runs (reusing the frozen B2-passing resultative ADD arm), read by the frozen
> thresholds with the falsify arms live. The weigh-question-4 framing point is developed in
> [`essay/nothing-to-cancel`](../essays/nothing-to-cancel.md): a cancel test built on an *implicature*
> (nothing to cancel) is ill-posed for defeasance, so a fair cancel arm needs a *held entailment* as
> its target — exactly what the B2 gate certifies.

> **STEP 1 (C1 telic-completion) is a B2 NO-GO (2026-06-28, session 137) — conjecture still
> `proposed`; routing to C2 with the M2 scope amendment below.** Following the decision's frozen
> STEP 1, this session froze + ran the completion-default B2 calibration *first*
> ([`result/monotonicity-c1-completion-calibration-v1`](../results/monotonicity-c1-completion-calibration-v1.md)):
> the completion entailment of a simple-past accomplishment ("built the house" → "finished building
> the house") is affirmed at only **0.25 / 0.375 / 0.75** (claude / gpt-mini / gemini) under strict
> NLI — **0/3 models at the ≥ 0.80 ceiling**. Even completion — a far stronger default than the s135
> "only once" — reads as **defeasible-not-categorical** under strict NLI (claude labels 2/8
> accomplishments an active *contradiction* of completion). Per the frozen instruction this does
> **not** relax the bar; it routes to **STEP 1b (C2 privative)**. This *reinforces* the
> weigh-question-4 point ([`essay/nothing-to-cancel`](../essays/nothing-to-cancel.md)): the cancel-side
> defaults the project reaches for are repeatedly inferences the panel does not hold as categorical
> entailments — part of "cancellation is hard" is that there is *less held entailment to cancel* than
> a human-semantics intuition expects. The asymmetry was **not** read; no battery ran.

> **M2 — DELIBERATE conjecture-scope amendment (2026-06-28, session 137), executing the ratified
> decision's pre-authorized C2 fallback.** The C1 NO-GO triggers STEP 1b (C2 = privative-modifier
> cancellation), which the ratified decision ([`decisions/resolved/monotonicity-cancel-arm-redesign`](../../decisions/resolved/monotonicity-cancel-arm-redesign.md),
> MOD-2) requires be preceded by a *written* scope-broadening. **Accordingly, the scope of this
> conjecture is hereby broadened, deliberately:** the add-vs-cancel monotonicity asymmetry is no longer
> tested over **verbal argument-structure constructions only**; it may be tested across **constructional
> inference more broadly, including a nominal/adjectival privative cancel arm** (a bare head noun
> entails its category — "a gun" ⊨ "a weapon" — and a privative modifier cancels it — "a fake gun" ⊭ a
> weapon). The verbal-only abstraction is **relaxed**. **Live caveat (recorded, binding on any C2
> result):** a C2 battery would pair a *verbal* ADD arm (the frozen resultative) with a
> *nominal/adjectival* CANCEL arm, so the add-verbal/cancel-nominal **domain mismatch** is a real
> confound on the asymmetry read — a C2 asymmetry is between *constructional inference types across a
> domain difference*, not a clean within-domain verbal contrast, and any C2 result must state this
> limitation prominently. This amendment is **deliberate, not incidental** (MOD-2 satisfied); it
> broadens what the conjecture is *about* and is logged here as a scope revision, not a result.

> **STEP 1b (C2 privative) is a B2 GO (2026-06-28, session 137) — conjecture still
> `proposed`; STEP 2 now unblocked.** The privative category-default calibration
> ([`result/monotonicity-c2-privative-calibration-v1`](../results/monotonicity-c2-privative-calibration-v1.md))
> is a clean **GO**: bare-head-noun category membership ("a gun" → "a weapon") is affirmed at
> **1.00 in 3/3 models** under strict NLI (every one of 24 NLI defaults = entailment) — sharply
> unlike the s135 "only once" (0.00) and the C1 completion default (0.25 / 0.375 / 0.75). So
> category membership **is** a categorical entailment for the panel, and a privative cancel arm
> can anchor a matched cancel arm at ceiling. The three calibrations now rank which cancel-side
> defaults the panel holds as entailments (implicature: no; aspectual default: no; taxonomic:
> yes) — vindicating the B2 gate. **STEP 2** (the matched battery, reusing the frozen
> B2-passing resultative ADD arm) is unblocked; the conjecture advances to `tested` only after
> it runs, read by the frozen thresholds with the falsify arms live. **Live caveat carried into
> STEP 2 (M2):** the battery pairs a *verbal* ADD arm with a *nominal/adjectival* CANCEL arm, so
> any C2 asymmetry is across a **domain difference** — a broadened, weaker version of the
> original verbal-only bet, to be stated prominently on the result.

> **STEP 2 RAN — a WEAK CONFIRM; conjecture advances `proposed → tested` (2026-06-28, session
> 137).** The matched C2 battery ran ([`result/monotonicity-c2-battery-v1`](../results/monotonicity-c2-battery-v1.md)):
> add licensing is at **uniform perfect ceiling (1.00, 3/3)**, privative cancellation (suppression)
> is **partial and item/model-dependent** (cancel_no_cue 0.75 / 0.625 / 0.875), the asymmetry is
> **positive in 3/3 models** and clears the pre-registered 20 pp bar in **2/3** (claude +0.25, gpt
> +0.375; gemini +0.125 below), with the cancel arm more instrument-fragile in 2/3 → **CONFIRMS by
> the frozen rule** (both legs), so the conjecture is now `tested`, **supported on this leg**
> (`internal-contrast-only`). **The support is weak and must not be over-stated:** (1) it spans a
> deliberate **verbal-add / nominal-cancel domain difference** (M2) — not a clean within-verbal
> contrast; (2) it is marginal in 2/3 models and a leave-one-out shows removing either of two
> pre-flagged borderline privatives (*toy violin*, *plastic apple*, which fail to suppress) drops it
> to 1/3; (3) small N, single run, no human baseline. With M1, the suppression shortfall is a genuine
> *defeasance* shortfall (the category default cleared B2 at ceiling, so there was a held entailment
> to cancel). The mechanism (LABELED speculation) is untouched; falsify arms did not fire (no
> symmetric/reversal; M3 closure not triggered). This is a fourth construction pair showing the same
> add-easy/cancel-hard shape, now with a B2-certified categorical default — bought at the cost of the
> domain mismatch.

> **CLEAN WITHIN-VERBAL CONFIRM — M2 DISCHARGED (2026-06-28, session 141); conjecture stays
> `tested`, now on materially firmer footing.** The within-verbal battery ran
> ([`result/monotonicity-within-verbal-battery-v1`](../results/monotonicity-within-verbal-battery-v1.md)):
> the frozen resultative ADD arm (verbatim) paired with a **verbal** progressive CANCEL arm
> (causative-inchoative; B2-default confirmed s139, suppression confirmed s140) — **both arms
> verbal**, so the M2 domain mismatch is **gone**. Read by the same frozen s134 thresholds: B2 GO
> (add construction 1.00 / control 0.00, cancel default 1.00, 3/3); add licensing at uniform ceiling
> (1.00, 3/3); progressive suppression partial (cancel_no_cue 0.50 / 0.67 / 0.33); **asymmetry
> +0.50 / +0.33 / +0.67 — ≥ 0.20 in 3/3 models** (confirm 3, symmetric 0, reversal 0); fragility leg
> confirms 3/3; cue robust (add & cancel cue-follow 3/3); and crucially **leave-one-out robust at the
> verdict level** (survives dropping any single cancel verb, worst case 2/3 — unlike the C2 confirm,
> which fell to 1/3). So the generalization criterion is met by a **genuinely new verbal cancel
> construction** (the progressive, beyond caused-motion / way / conative) on a **clean within-verbal
> contrast**. **Honest, persisting caveats:** suppression is **partial and verb-uneven** (`window`/
> shatter resists in all 3 models — punctual progressives read as culminated; gpt-5.4-mini sits
> nearest the 0.20 bar precisely because it *suppresses the most* (4/6 verbs), giving the smallest
> add-vs-cancel gap — best defeasance, smallest asymmetry); the add/cancel hypotheses are domain-matched but not surface-form
> identical ("became stiff" vs "the vase broke"); small N, single run, `internal-contrast-only` (no
> human baseline). The falsify arms were live and did not fire. This **discharges the M2 headline
> caveat** the s137 confirm carried; what remains open is human comparison and whether the
> partial/uneven suppression is defeasance *competence* or strict-NLI *labeling*.

## Statement

This is the **project's own, original** theoretical proposal — a forward bet generalizing a pattern that recurs across the argument-structure results, not an established finding. The descriptive observation it builds on is already recorded in [`concept/coercion`](../../base/concepts/coercion.md) and on the theory page ([`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md), "the tentative generalization the ladder should now carry") *(Superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md) — cited here as the edition this page engaged.)*; this page names it, frames it as a **monotonicity** asymmetry, and states sharp confirmation/falsification criteria so the empirical loop can later pick it up. The two pages are kept complementary: the theory page states the asymmetry descriptively in the course of placing each result on its ladder; this page is the typed conjecture that *abstracts over* those results and proposes a mechanism and a generalization test. It does not duplicate the ladder; it points at it.

The proposal, in one sentence: **current decoder LLMs treat a construction's inferences as readily *additive* — they license a construction-contributed entailment layered onto a non-licensing verb — but resist *retraction* — they suppress a lexically-default entailment far less reliably.** Cast in the vocabulary of inference: the models look better at *monotone accumulation* of entailments (add a new one) than at *defeasance* (cancel a default one). Adding is the easy direction; cancelling is the hard direction.

The connection to non-monotonic / defeasible reasoning is offered here as a **characterization, not a claimed result**: cancelling a default entailment is, formally, a defeasibility operation (the verb's lexical default is a defeasible inference the construction is meant to override), whereas adding a construction-contributed entailment is monotone (the construction's content is layered on without retracting anything). Under that framing the recurring asymmetry reads as: *these models are stronger at monotone accumulation than at the defeasance that cancellation requires.* The defeasible-reasoning literature is named as a framing only — no in-repo source grounds it, so the formal claim is held at the level of analogy (see *Provenance and what is not claimed*).

## The evidence this abstracts over

The asymmetry is visible across five own-design argument-structure results. Each is cited with its verified numbers (a direction-of-effect signal in every case — single panel/date/run, small N).

**The ADD direction is easy — at or near ceiling.**

- Caused-motion: the panel affirms the construction's causation-of-motion entailment onto non-motion verbs at **90–100%**, with a **70–100 pp** gap over controls, in **3/3 models**, both instruments, robust to atypical verbs ([`result/caused-motion-minimal-pair-divergence-v1`](../results/caused-motion-minimal-pair-divergence-v1.md)).
- The *way*-construction: the path-traversal (self-motion) entailment onto non-motion verbs holds at **77.8–100%**, gap **77.7–100 pp** over the location control, **3/3 models**, both instruments ([`result/way-construction-traversal-v1`](../results/way-construction-traversal-v1.md)).

**The CANCEL direction is harder — off-ceiling and instrument-fragile.**

- The conative cancels the completed-contact entailment the transitive carries (*kicked at the ball* vs *kicked the ball*). The forced-choice gap is **42–88 pp** across all 3 models, but **gpt-5.4-mini fails the cancellation entirely under NLI** (calls all conative items "entailment") while partly recovering under forced-choice ([`result/conative-minimal-pair-divergence-v1`](../results/conative-minimal-pair-divergence-v1.md)).

**The asymmetry is de-confounded from ceiling by a matched probe.** This is the load-bearing piece: "license-easier-than-suppress" is about *direction*, not about the add items merely being easier. [`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md) put the cancel direction into the *same* conflicting-cue paradigm the add-direction v2 used. At matched task structure the transitive lexical default is at ceiling (**91.7–100%**), but conative **suppression-with-no-cue** is off-ceiling and model/instrument-dependent — NLI **[58.3, 0.0, 66.7] pp**, forced-choice **[66.7, 33.3, 83.3] pp** — where the add-direction's matched licensing-no-cue was ~ceiling. So the asymmetry survives matching for difficulty: it is a property of the *direction* (add vs cancel), not an artifact of where on the scale the items happened to sit.

**Both directions are bounded — this is not "deep cancellation competence" either.** The add direction's apparent "computes-and-withholds" ability is itself shallow: while an *explicit* in-premise outcome denial floors the added affirmation (argument-structure-coercion-v2, cited on the theory page), [`result/coercion-implicit-cue-v2b`](../results/coercion-implicit-cue-v2b.md) shows the panel still affirms a **physically impossible** caused-motion coercion at **near-ceiling (implicit-wk 90–100%)** when immovability is only *implied* by an in-premise descriptor, flooring (**0%**) only under an explicit outcome denial. So the add-direction's withholding is **explicit-outcome parsing, not world-model integration**. The conjecture is therefore *not* that cancellation is a deep competence the models lack; it is the narrower, more honest claim that *across matched probes the add direction is more uniformly executed than the cancel direction*, while both remain bounded.

## Mechanism (LABELED speculation)

The following is **speculation**, offered as a candidate explanation, not as a tested claim. It is deflationary-compatible — it does not require attributing reasoning to the model beyond next-token prediction over distributional structure.

Adding a construction-licensed inference is **distributionally cheap**: the construction's own co-occurrence statistics support the added entailment (the caused-motion frame co-occurs with caused-motion outcomes; the *way*-frame co-occurs with traversal), so a next-token predictor can affirm the added inference from the construction's distribution alone. Suppressing a lexical default, by contrast, requires representing a **cancellation against a strong lexical prior**: the verb (*kick*, *sip*) carries a robust completed-contact expectation in its own distribution, and the conative frame must override that prior rather than reinforce it. Holding down a strong prior is plausibly harder for a system whose objective is to predict the high-probability continuation. On this story the asymmetry is a signature of *distributional* meaning ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)) — accumulation aligns with the predictive objective; retraction works against it — rather than evidence of a constructional-meaning competence that is present in one direction and absent in the other. (The mechanism is compatible with the deflationary reading the theory page brackets; it is not an argument *for* deflationism, only consistent with it.)

This mechanism is itself a hypothesis the falsification criteria below can bear on: if the asymmetry reversed for some construction class, or vanished under matched difficulty, the distributional-prior story would be wrong or incomplete.

## What would confirm / falsify

Sharp criteria, so a later experiment can adjudicate. The decisive design feature in every case is **matched difficulty / ceiling control** — the conative-cancel-v2 probe is the template: compare add vs cancel at the *same* task structure, never add-at-ceiling vs cancel-off-ceiling.

**Confirms** (jointly):

1. The asymmetry **generalizes to new add-vs-cancel construction pairs** beyond caused-motion / way / conative — for example, other Levin alternations, or resultatives that *add* an entailment versus aspectual/conative-type coercions that *cancel* a default — tested at **matched difficulty and ceiling** (the add and cancel arms placed in a common paradigm, as conative-cancel-v2 did); AND
2. The cancel direction is reliably **more instrument-fragile** (larger NLI-vs-forced-choice disagreement) than the add direction on the same items — the pattern already seen for the conative ([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md); [`result/conative-minimal-pair-divergence-v1`](../results/conative-minimal-pair-divergence-v1.md)).

**Falsifies** (either):

- A matched, ceiling-controlled battery shows **symmetric** add/cancel performance — once difficulty is equated, the add and cancel arms are statistically indistinguishable; OR
- The asymmetry **reverses** for some construction class — a construction whose *cancel* direction is easy and whose *add* direction is hard.

A null on the generalization test (the asymmetry fails to extend beyond the three constructions seen so far) would retire the conjecture as an artifact of those particular items, not establish a competing claim.

## Candidate human anchor

A conjecture page needs no resource anchor (only `claim`/`result` pages do); naming a candidate is the project convention. The candidate human anchor for a matched-difficulty test is the **Scivetti CxNLI dataset** ([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)), which carries human-annotated NLI triples for both add-type constructions (Caused-Motion, Way-Manner) and the cancel-type Conative, with an aggregate native-speaker baseline (≈0.90 on Exp 1). It can anchor an answer-key comparison — model NLI labels against the per-item gold labels on the *same* add vs cancel constructions — but it delivers a single adjudicated gold label per item, **not** a per-item human-rating gradient (confirmed by inspection; see the resource page's *Known limits*).

Important scope note: the off-ceiling internal arms that establish the de-confounded asymmetry have so far been **internal-contrast-only** — the conative-cancel-v2 cue arm has no in-repo human norm, and that result carries `anchor: internal-contrast-only` by ratified decision ([`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)). So a future *result* testing this conjecture would need either (a) to confine its human-comparison claim to the Scivetti answer-key arms, or (b) to declare its off-ceiling arms internal-contrast-only, exactly as the existing cancel-direction result does. The conjecture does not assume a human gradient the anchor cannot supply.

> **Scoping verdict (2026-06-29, session 144): the *asymmetry's* human-comparison leg is un-instrumentable on the project's available resources.** [`open-question/monotonicity-human-comparison-leg`](../open-questions/monotonicity-human-comparison-leg.md) scopes this in full. In short: the per-construction *arms* have a human comparison ([`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md)), but the load-bearing **gap** does not, because the one held anchor (Scivetti) supplies a single binary gold rather than a graded *robustness* signal, offers no difficulty-matching across the add and cancel arms (the answer-key add-vs-cancel contrast is baseline-difficulty-confounded), and omits the project's actual cancel constructions (progressive / privative / completion / single-occurrence). This is a fact about the available resources and the no-human-subjects rule, not a falsification: the finding stays `internal-contrast-only` until an externally-released graded-cancellability resource over matched pairs turns up — at which point trigger (a) of [`essay/construct-validity-without-a-criterion`](../essays/construct-validity-without-a-criterion.md) would fire for this construct.

## Provenance and what is not claimed

- Every number above is quoted from an in-repo result page and matches it verbatim; none is invented.
- The framing in terms of **non-monotonic / defeasible reasoning** is a *characterization*, not a grounded result: no in-repo source treats the LLM-defeasance connection, so the formal mapping (cancellation = defeasibility operation; add = monotone) is held as analogy. If the project later leans on this formally, a defeasible-reasoning / non-monotonic-logic reference should be fetched first (flagged for `wanted.md`).
- The asymmetry is a **direction-of-effect** observation across five small-N, single-run, three-model probes. The conjecture is a forward bet that it *generalizes*; it is explicitly **not** presented as established. The de-confounding from ceiling ([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md)) is the strongest leg, but it too is small-N and internal-contrast-only.
- The conjecture does **not** claim cancellation is a deep competence the models lack, nor that addition reflects genuine constructional-meaning computation: [`result/coercion-implicit-cue-v2b`](../results/coercion-implicit-cue-v2b.md) bounds the add direction's depth (explicit-outcome parsing, not world-model integration). Both directions are bounded; the claim is only about their *relative* reliability.
