---
type: essay
id: predictive-objective-favors-accumulation
title: The add-easy / cancel-hard asymmetry would be the behavioral fingerprint of a next-token predictive objective — if it generalizes
meaning-senses:
  - constructional
  - inferential
  - distributional
status: draft
contingent-on: []
created: 2026-06-28
updated: 2026-06-28
links:
  - rel: depends-on
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: refines
    target: conjecture/constructional-monotonicity-asymmetry
  - rel: depends-on
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: result/coercion-implicit-cue-v2b
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
---

# Essay: the predictive objective favors accumulation over retraction

> **Status: draft (2026-06-28). A philosophical-track essay arguing in the project's own voice.** It introduces **no new empirical claim**: every empirical assertion cites the in-repo page that carries it, at that page's stated strength, and the original part is the argument — a reading of *why* the add/cancel asymmetry has the direction it does. The whole essay is **explicitly conditional** on an open forward bet: [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md) is `status: proposed`, **not tested**. None of the in-repo pages cited here is a human anchor (each grounds the theory or carries an internal-contrast-only within-model result, never a human comparison). The **Revision triggers** section states in advance exactly what would revise or retract the essay; read it before citing the argument.

## The position

The conjecture the essay leans on records a recurring pattern across the project's argument-structure probes: current decoder LLMs **add** a construction-contributed inference readily but **suppress** a lexically-default one far less reliably. The conjecture's own one-sentence statement is the bounded version, and the essay claims nothing past it:

> "current decoder LLMs treat a construction's inferences as readily *additive* — they license a construction-contributed entailment layered onto a non-licensing verb — but resist *retraction* — they suppress a lexically-default entailment far less reliably." ([`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md), §Statement)

This essay proposes a reading of *why* the asymmetry, **if it generalizes**, points the way it does — and the reading is sharp: **add-easy / cancel-hard would be the behavioral fingerprint of a next-token predictive objective.** Accumulating a construction-licensed inference moves *with* the prediction of a high-probability continuation; cancelling a lexical default moves *against* a strong lexical prior. So "license is easier than suppress" need not be a quirk of three constructions — it is what a meaning-as-prediction view would *predict*: a predictor is intrinsically monotone-friendly and defeasance-resistant. The asymmetry's direction is, on this reading, not extra information about constructional competence but a signature of the objective the competence was acquired under.

The essay's load-bearing word is **if**. The conjecture is a forward bet that the asymmetry *generalizes* beyond the three constructions seen so far; it is `proposed`, not `tested`. The essay is therefore a conditional: *if* the asymmetry survives the conjecture's own matched-difficulty generalization test, *then* it is the fingerprint of the predictive objective. The essay does **not** assert the asymmetry as an established general finding, and its fate rides entirely on the conjecture's open test.

## The evidence, at its actual strength

The conjecture abstracts over "**five small-N, single-run, three-model**" direction-of-effect probes (its words: "a **direction-of-effect** observation across five small-N, single-run, three-model probes"; §"Provenance and what is not claimed"). Two halves matter, and both must be quoted at their stated strength.

**The add direction is at or near ceiling.** The conjecture records the two add-direction positives:

> "Caused-motion: the panel affirms the construction's causation-of-motion entailment onto non-motion verbs at **90–100%**, with a **70–100 pp** gap over controls, in **3/3 models** … The *way*-construction: the path-traversal (self-motion) entailment onto non-motion verbs holds at **77.8–100%**, gap **77.7–100 pp** over the location control, **3/3 models**, both instruments" ([`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md), §"The evidence this abstracts over").

**The cancel direction is off-ceiling, and survives de-confounding from ceiling by a matched probe.** This is the load-bearing leg: the asymmetry is about *direction*, not about the add items merely being easier. The de-confounding result put the cancel direction into the *same* conflicting-cue paradigm the add-direction used, so the two are compared at matched task structure. Its one-line finding, quoted exactly:

> "The asymmetry survives de-confounding: at matched conflicting-cue task structure, the panel suppresses the lexical default far less reliably — and far less uniformly — than it licenses an added inference." ([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md), §"One-line finding")

with the matched-difficulty numbers stated on that page: at matched structure "the transitive lexical default is at ceiling (affirm-contact 91.7–100%), but **suppression with no cue** (the conative; `100 − conative_affirm`) is off-ceiling and model/instrument-dependent — NLI **[58.3, 0.0, 66.7] pp**, FC **[66.7, 33.3, 83.3] pp** — where the *add*-direction's matched **licensing-no-cue** … was ~ceiling" ([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md), §"One-line finding"). The single most telling cell: "gpt-5.4-mini **fails conative suppression entirely under NLI** (conative affirm 100% — it calls *kicked at the ball* an entailment of contact)" (same section). That result is `anchor: internal-contrast-only` by ratified decision, so its off-ceiling arms carry **no human-comparison claim** (its caveats: "**Internal-contrast-only; no human baseline on the cue arm.**").

So the asymmetry's strongest leg is one de-confounded, small-N, internal-contrast-only result on the project's own stimuli — exactly as the conjecture says: "The de-confounding from ceiling … is the strongest leg, but it too is small-N and internal-contrast-only" ([`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md), §"Provenance and what is not claimed"). Both directions are also **bounded** — the add direction's apparent withholding is shallow. The conjecture states it, citing the implicit-cue result:

> "the add-direction's withholding is **explicit-outcome parsing, not world-model integration**." ([`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md), §"The evidence this abstracts over")

That bound is the implicit-cue result's own finding: with only an in-premise immovability descriptor, decoders affirm a physically impossible coercion at "near-ceiling (implicit-wk 90–100%) … only the **explicit** outcome denial drives it to **floor**" ([`result/coercion-implicit-cue-v2b`](../results/coercion-implicit-cue-v2b.md), §"One-line finding"), also `anchor: internal-contrast-only`. The essay's claim is therefore **only** about the *relative* reliability of add vs cancel — not that addition is genuine constructional-meaning computation, not that cancellation is a deep competence the models lack.

## Why a predictor favors accumulation over retraction

Here is the essay's own candidate explanation. It is offered as a **position the project argues**, not as a tested claim — and it is the project's, sharpened from a mechanism the conjecture itself **labels speculation**. It is **deflationary-compatible**: it attributes nothing to the model beyond next-token prediction over distributional structure.

Cast the two directions in the vocabulary of [`concept/coercion`](../../base/concepts/coercion.md). **Adding** a construction-licensed inference (caused-motion's "the object moved", the *way*-construction's "the agent traversed") layers a new entailment onto a verb that does not lexically carry it — but the construction's *own* co-occurrence statistics support that entailment. The caused-motion frame co-occurs with caused-motion outcomes; the *way*-frame co-occurs with traversal. A next-token predictor can affirm the added inference **from the construction's distribution alone** — and crucially, the inference points the *same* way the high-probability continuation does. Accumulation is distributionally cheap, monotone, and aligned with the objective: nothing has to be held down.

**Cancelling** a lexical default (the conative suppressing the completed-contact that *kick*, *sip* carry by default) is the opposite shape. The verb's robust completed-contact expectation lives in its own distribution; the conative frame must **override that prior rather than reinforce it**. Holding down a strong prior is plausibly harder for a system whose objective is precisely to predict the high-probability continuation — the prior *is* what the objective rewards tracking. Defeasance works *against* the objective. This is exactly the conjecture's labeled-speculation mechanism, which the essay adopts as its position:

> "accumulation aligns with the predictive objective; retraction works against it." ([`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md), §"Mechanism (LABELED speculation)")

The step the essay adds is the inversion of the inference. On the project's existing reading (carried on the theory page, where the asymmetry is "abstracted into" the conjecture as "additive-easy, defeasance-hard — a distributional-prior-compatible signature", [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md), §"Theoretical situating"), the asymmetry is *compatible with* a distributional-prior story. The essay presses harder: the direction is not just compatible with the predictive objective — it is **what that objective predicts**. A system optimized to continue the high-probability string should, all else equal, find monotone accumulation cheap and defeasance dear. So if the add/cancel split is real and general, its *direction* is not a further fact about constructional meaning that the objective happens to permit; it is the objective's own fingerprint, read off the behavior. This squares with [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)'s framing that the next-token objective "implicitly encodes distributional structure", and with the open note on [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md) that "next-token prediction is implicitly inferential" — but it specifies a *direction* that the bare distributional/inferential entanglement does not by itself fix: monotone-friendly, defeasance-resistant.

Two disciplines keep this honest. First, it is the conjecture's own labeled speculation, not a tested claim; the conjecture says so plainly ("The following is **speculation**, offered as a candidate explanation, not as a tested claim", §Mechanism), and the essay inherits that status. Second, it is **not an argument for deflationism** — only consistent with it; the conjecture's bracket holds ("it is not an argument *for* deflationism, only consistent with it"). The essay reads the asymmetry's direction *as if* meaning were prediction and asks what that predicts; it does not thereby establish that meaning *is* prediction. The fingerprint reading is a conditional consequence of a deflationary premise, offered because it is sharp and falsifiable, not because the premise is settled.

## What this is not

- **Not an established general finding.** The asymmetry's *generalization* is an open forward bet — the conjecture is `status: proposed`, not tested. The essay is conditional throughout: *if* the asymmetry generalizes (the conjecture's matched-difficulty test), *then* it is the fingerprint of the predictive objective. The essay must not be cited as showing that add-easy/cancel-hard is a general property of decoder LLMs.
- **Not a tested mechanism.** "Prediction favors accumulation over retraction" is the conjecture's *labeled speculation*, developed here as the project's candidate position. It is not upgraded to a claim. It is deflationary-compatible (no reasoning attributed beyond next-token prediction) and is *not* an argument for deflationism.
- **Not a claim that addition is genuine constructional competence.** The add direction's "withholding" is bounded to **explicit-outcome parsing, not world-model integration** ([`result/coercion-implicit-cue-v2b`](../results/coercion-implicit-cue-v2b.md)). The essay's claim is only about the *relative* reliability of add vs cancel.
- **Not a claim that cancellation is a deep competence the models lack.** The conjecture is explicit that it does "**not** claim cancellation is a deep competence the models lack, nor that addition reflects genuine constructional-meaning computation … Both directions are bounded; the claim is only about their *relative* reliability." The essay holds to that line.
- **Not a human-comparison claim.** The de-confounded off-ceiling arms that carry the asymmetry's strongest leg are `anchor: internal-contrast-only`; their force is a within-model contrast, not a contrast with any human norm. The essay adds no human comparison the cited pages do not make — which is none.
- **Not a primary-source claim about non-monotonic logic.** The "monotone accumulation vs defeasance" framing is a *characterization*, not a grounded formal result; the conjecture flags that "no in-repo source treats the LLM-defeasance connection" and holds the mapping "as analogy". The essay uses it the same way and no more strongly.

## Sibling note

This essay shares a parent observation with two siblings but cuts a different axis from each.

- [`essay/gradient-from-overlap`](gradient-from-overlap.md) sorts what a *gradient* licenses about a stored *representation* (the underdetermination of representation by behavior). That is a representation-vs-behavior axis. This essay is about the *predictive objective's directional bias on inference* — add vs cancel — not about whether any gradient licenses a representation. They are complementary, not overlapping: that essay disciplines "behavior, not representation"; this one reads a *direction* in the behavior.
- [`essay/inference-default-coincidence`](inference-default-coincidence.md) is about a place where the add direction **cannot be measured** because the construction's licensed inference already coincides with the phrase's distributional default ("the default eats the construction"), so a shift-from-control design has no headroom. This essay is the converse case: it is about why **cancel is harder than add precisely where both *are* measurable** — the conative cancel arm is off-ceiling and separable *because* its default runs the other way. That essay names where the add signal vanishes into the default; this one reads the direction of the signal where it survives. (That essay's own revision-trigger (c) already points at the conative as the construction "where the default points the other way" — the same separability this essay's cancel leg rests on.)
- [`essay/compositionality-asymptote-not-wall`](compositionality-asymptote-not-wall.md) is about how behavioral evidence falls short of the compositionality target (homomorphism) — a graph-vs-form gap. Different target entirely; cited only to mark the boundary.

## Revision triggers (read before citing)

The essay's fate rides on the conjecture's open test. Its falsifiers are, chiefly, the conjecture's own:

- **(a) A matched, ceiling-controlled battery shows SYMMETRIC add/cancel.** The conjecture's first falsifier: "once difficulty is equated, the add and cancel arms are statistically indistinguishable" ([`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md), §"What would confirm / falsify"). If the asymmetry vanishes under matched difficulty, the "fingerprint of the predictive objective" reading has no asymmetry to be a fingerprint *of*; the essay is **retracted** (moves to `status: retracted` with an in-page log entry).
- **(b) The asymmetry REVERSES for some construction class** — "a construction whose *cancel* direction is easy and whose *add* direction is hard" (same section). A reversal directly contradicts the directional prediction the essay reads off the predictive objective; the essay is **retracted**.
- **(c) A null on the generalization test** — the asymmetry fails to extend beyond the three constructions seen so far. The conjecture treats this as retiring it "as an artifact of those particular items" (same section). The essay's conditional then has a false antecedent: with no generalized asymmetry, there is no fingerprint to claim. The essay moves to `status: revised`, narrowing to "for these three constructions only, the direction is predictive-objective-compatible" — a far weaker statement.
- **(d) An in-repo non-monotonic-logic source that recasts the add/cancel mapping.** The defeasance framing is held as analogy (the conjecture flags it for `wanted.md`). If such a source enters the repo and the formal mapping is found weaker or different, the essay re-checks that "monotone accumulation vs defeasance" is stated against the correct target and is relativized accordingly.
- **(e) Representational evidence on the directional asymmetry.** This essay is behavioral. If a mechanistic / representational probe were to separate the add and cancel directions internally, the "predictor favors accumulation" reading would be relativized to behavioral instruments — the behavioral signature stays, but the mechanism story would be testable rather than speculative, and the essay's status as *labeled speculation* would change.

## What this essay is not (in one line)

It does not assert the asymmetry is general, does not upgrade the mechanism to a tested claim, does not claim the add direction is genuine competence or the cancel direction a competence the models lack, and makes no human comparison. It argues one conditional: **if** the add/cancel asymmetry generalizes, **then** its direction is the behavioral fingerprint of a next-token predictive objective.

## Honesty box

- The essay's **original** contribution is the **inversion of the inference**: where the project already reads the add/cancel asymmetry as *compatible with* a distributional-prior story, this essay argues that — *if it generalizes* — its *direction* is what a next-token predictive objective would *predict*, so add-easy/cancel-hard would be the objective's behavioral fingerprint rather than a further fact about constructional competence the objective permits. This shape is the essay's own; no source page asserts it.
- The strongest sentence the evidence supports is **conditional**: *if the add/cancel asymmetry generalizes (the conjecture's open, untested bet), then its direction is the behavioral fingerprint of a next-token predictive objective — a predictor being intrinsically monotone-friendly and defeasance-resistant.* The antecedent is supported only by five small-N, single-run, three-model direction-of-effect probes, with the de-confounded cancel arm (off-ceiling, internal-contrast-only) as the strongest leg; nothing here outruns that.
- The mechanism ("prediction favors accumulation over retraction") is the **conjecture's labeled speculation**, developed as the project's candidate position, not a tested claim, and not an argument for deflationism. Both directions are bounded: the add direction's withholding is explicit-outcome parsing, not world-model integration.
- **No human-comparison claim.** The de-confounded off-ceiling arms are `anchor: internal-contrast-only`; none of the pages cited here is a human anchor.
- Every quotation is verified against its in-repo source page (page/section locators given inline) and matches it verbatim; the numbers (90–100%, 77.8–100%, 91.7–100%, NLI [58.3, 0.0, 66.7], FC [66.7, 33.3, 83.3]) are quoted from the conjecture and the conative-cancel-v2 result and are not restated more strongly than those pages state them. No quotation or number is reconstructed from memory.
