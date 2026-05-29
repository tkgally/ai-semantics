---
type: theory
id: constructional-meaning-in-llms
title: What would count as evidence that an LLM has internalized a construction's meaning, not only its form
meaning-senses:
  - constructional
  - functional-vs-formal
  - distributional
  - inferential
  - relational
status: draft
contingent-on: []
created: 2026-05-28
updated: 2026-05-29
links:
  - rel: refines
    target: claim/formal-competence-aann-ceiling
  - rel: depends-on
    target: claim/constructional-divergent-form-generalization-gap
  - rel: depends-on
    target: result/comparative-correlative-covariation-v1
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: source/scivetti-2025-beyond-memorization
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: conjecture/aann-construction
  - rel: depends-on
    target: conjecture/way-construction
  - rel: depends-on
    target: conjecture/dative-alternation-information-structure
  - rel: depends-on
    target: conjecture/function-word-substitutability
  - rel: depends-on
    target: conjecture/caused-motion-construction
  - rel: depends-on
    target: conjecture/conative-construction
  - rel: depends-on
    target: conjecture/comparative-correlative-construction
  - rel: supports
    target: open-question/relational-meaning-pilot
  - rel: supports
    target: open-question/constructional-divergence-probe
  - rel: depends-on
    target: source/mahowald-2024-dissociating
  - rel: depends-on
    target: source/weissweiler-2023-cxg-insight
  - rel: depends-on
    target: source/piantadosi-hill-2022-meaning-without-reference
  - rel: depends-on
    target: source/bender-koller-2020-climbing
  - rel: depends-on
    target: source/lyre-2024-semantic-grounding
---

# Theory (draft): evidence for constructional meaning in LLMs

## The theoretical object

This is the project's first synthesis page — the recursive object the charter calls for ([`PROJECT.md`](../../../PROJECT.md) §4: "the theory/claim page that gets rewritten by what an experiment teaches"). It exists to be rewritten when the founding conjectures run.

It answers one question, sharply: **what would count as evidence that an LLM has internalized a construction's *meaning* — its form–meaning pairing — as opposed to merely its *form*?**

The question is not "do LLMs understand language" (too coarse) nor "are LLMs grounded" (a separate, orthogonal axis; see below). It is the narrower, more tractable wedge the project has chosen: take a single English construction whose form and whose characteristic meaning are both reasonably well described in the linguistics literature, and ask what observable LLM behavior would license the inference that the model has the *pairing*, not just the form.

A construction, in the Construction Grammar sense the project adopts, is a form–meaning pairing at some level of abstraction. Weissweiler et al. 2023 ([`source/weissweiler-2023-cxg-insight`](../../base/sources/weissweiler-2023-cxg-insight.md)) states the unit directly:

> "According to CxG, meaning is encoded in abstract constellations of linguistic units of different sizes."

That same source frames why CxG is the right lens for this question rather than syntactic or semantic probing taken separately: a construction probe "is not probing for a syntactic pattern and separately probing for a semantic preference — it is probing for the form–meaning unity" (paraphrase of the source's §2.1 framing). The whole difficulty — and the whole interest — is that form-tracking and meaning-tracking can come apart, and a fluent model can have the first without the second.

## The wedge: formal vs. meaning

The cut that organizes this theory is the formal-vs-functional competence distinction of Mahowald et al. 2024 ([`source/mahowald-2024-dissociating`](../../base/sources/mahowald-2024-dissociating.md)):

> "we evaluate LLMs using a distinction between formal linguistic competence—knowledge of linguistic rules and patterns—and functional linguistic competence—understanding and using language in the world."

Formal competence is defined operationally as getting the form right:

> "Broadly, being formally competent means getting the form of language right: knowing which strings could be valid words of a language (e.g., bnick cannot be a word in English but blick can)."

And the paper's central empirical asymmetry is that LLMs are strong on the formal side and uneven on the functional side:

> "Although LLMs are surprisingly good at formal competence, their performance on functional competence tasks remains spotty and often requires specialized fine-tuning and/or coupling with external modules."

The load-bearing move for this project is the methodological corollary the Mahowald source page draws out: success on a structural-acceptability task is evidence of *formal* competence and does not, by itself, warrant a conclusion about meaning-tracking. [`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md) already commits the project to this: an AANN acceptability ceiling "does not, by itself, constitute evidence of functional linguistic competence or constructional meaning-tracking in the CxG sense." This theory **refines** that claim by generalizing it past AANN: for *any* construction, the form-acceptability result is the floor of evidence, not the proof.

Two caveats travel with the wedge and must not be elided:

1. **Formal/functional is not the same cut as the constructional form/meaning cut.** Mahowald's "formal semantics" (compositional structure-to-meaning mapping) overlaps with, but is not identical to, `constructional` meaning (the source page warns of exactly this: "Citing it for construction probing requires care."). The project uses formal/functional as a *frame* for sorting evidence, not as a substitute for a construction-specific meaning theory.
2. **Formal/functional is orthogonal to grounded/ungrounded.** Per the Mahowald source: a model "can be formally competent but not grounded." The grounding question (next section) is a distinct axis; conflating them is a defect this theory explicitly forbids.

## What "meaning" is, on this page

The project refuses the unqualified word "meaning" ([`wiki/meaning-senses.md`](../../meaning-senses.md)). Three senses are in play here, and the theory keeps them separate. Each is now a full concept page: [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md), [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md), [`concept/constructional-meaning`](../../base/concepts/constructional-meaning.md), with the orthogonal grounding axis treated at [`concept/grounding`](../../base/concepts/grounding.md).

- **Distributional** — meaning as co-occurrence structure; the implicit theory of the next-token objective (Firth/Harris). This is the *null hypothesis* against which constructional-meaning claims must be set: a fluent model has distributional structure for free. The senses page flags that distributional structure "by itself ... is silent on reference and on truth — this is exactly the contested boundary."
- **Inferential** — meaning as inferential role: a construction means what it licenses you to infer. Piantadosi & Hill 2022 ([`source/piantadosi-hill-2022-meaning-without-reference`](../../base/sources/piantadosi-hill-2022-meaning-without-reference.md)) give the framing under which inference-preservation counts as genuinely semantic: "meaning ... arises from conceptual role," constituted by "the relationships between internal representational states" (abstract). On this view, a model that systematically licenses a construction's characteristic inferences has more than distributional mimicry.
- **Constructional** — meaning as the form–meaning pairing itself, the thing the probe is for.

The distributional/inferential boundary is not assumed to collapse (the senses page leaves the collapse question open: "Should `distributional` and `inferential` collapse ... Probably no"). This theory treats inferential structure as the *upgrade* over distributional structure that constructional-meaning evidence must demonstrate — which is precisely why the top tiers of the evidence ladder below are inferential, not distributional.

### The grounding axis, and why it is bracketed (not denied)

Two poles bound the grounding debate the project sits inside. Bender & Koller 2020 ([`source/bender-koller-2020-climbing`](../../base/sources/bender-koller-2020-climbing.md)) is the form-only denial:

> "we argue that a system trained only on form has a priori no way to learn meaning"

— where meaning is defined as "the relation M ⊆ E × I which contains pairs (e, i) of natural language expressions e and the communicative intents i they can be used to evoke." On this definition, *no* text-only behavior, however systematic, counts as meaning, because the grounding relation to communicative intent is absent from the training signal.

Lyre 2024 ([`source/lyre-2024-semantic-grounding`](../../base/sources/lyre-2024-semantic-grounding.md)) supplies the framing this project actually adopts — grounding as graded rather than binary (p. 10):

> "semantic grounding isn't a yes-no matter, but rather a matter of degree. Intelligent or cognitive agents and systems can be more or less semantically grounded"

with the verdict that LLMs are "neither stochastic parrots nor semantic zombies, but already understand the language they generate, at least in an elementary sense" (p. 1, abstract).

This theory takes the Lyre stance methodologically: the question is not whether an LLM has constructional meaning full stop, but *how far up the evidence ladder* its behavior reaches. Bender & Koller mark the position that even the top rung of a text-only ladder does not reach grounded communicative meaning; that position is recorded, not refuted here. The ladder below measures *constructional* meaning-tracking within the text-only setting; it is deliberately silent on whether tracking ever amounts to grounding in Bender & Koller's stronger sense. That silence is the honest scope of a text-only probe program.

## The evidence ladder

The core contribution of this page: a tier ordering on what counts as evidence, from weakest to strongest. Each rung subsumes the ones below; a higher rung is harder to fake with distributional structure alone. The project's existing pages are placed on the ladder explicitly.

**Tier 0 — Form-acceptability.** The model distinguishes well-formed instances of the construction from minimally different ill-formed ones (e.g. *a beautiful three days* vs. *a three beautiful days*). This is formal competence in Mahowald's exact sense, and it is the floor. [`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md) lives here, by design: it asserts that an AANN acceptability ceiling, even matching human raters, is Tier-0 evidence and "a necessary but not sufficient test" for meaning. A model can reach Tier 0 with surface-pattern learning and no grasp of what the construction means.

**Tier 1 — Surprisal-contrast sensitivity.** The model's graded continuation likelihoods separate licit from illicit instantiations in a way that is not reducible to the unigram frequency of the swapped item. This is sharper than Tier 0 (it uses the model's full distribution, not a binary judgment) but it is still distributional: it shows the construction is a unit in the model's predictive structure, not yet that the model tracks the construction's *meaning*. [`conjecture/aann-construction`](../conjectures/aann-construction.md) Prediction 2 (licit vs. illicit surprisal contrast on held-out items) and [`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md) Prediction 1 (KL divergence on continuation distributions) sit here. Weissweiler's memorization confound bites hardest at this tier: the source warns that minimal-pair probing "does not tell us anything about if the model has identified the extent of the construction correctly."

**Tier 2 — Gradient semantic tracking.** The model's behavior tracks a *meaning* gradient internal to the construction, not just a well-formedness gradient — and tracks it in the direction the construction's semantics predicts. For AANN this is the evaluative-adjective effect ([`conjecture/aann-construction`](../conjectures/aann-construction.md) Prediction 1: higher likelihood with *beautiful*/*gruelling* than with neutral measure-modifiers, controlling for unigram frequency), reflecting that the construction's meaning is partly evaluative. For the dative, it is sensitivity to the information-structure constraint — given-before-new, pronominal-recipient → DOC ([`conjecture/dative-alternation-information-structure`](../conjectures/dative-alternation-information-structure.md) Predictions 1–2). This tier is where Lyre's "gradual" framing does real work: the prediction is monotonic correspondence with a human gradient, not a hard flip. It is also the first tier whose positive result would be hard to attribute to distributional structure alone — which is exactly why [`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md) names "adjective-type gradient tracking" as the separate meaning-diagnostic that the plain acceptability contrast cannot supply.

**Tier 3 — Generalization to held-out material.** The Tier-2 effect holds for lexical items the model is unlikely to have seen *in the construction* during training. This is Goldberg's productivity criterion and the project's main defense against memorization ([`conjecture/aann-construction`](../conjectures/aann-construction.md): "the held-out lexical-item check is the main defense"; its "weak" outcome is explicitly "contrast exists for items that appeared in training (memorization) but does not generalize"). Generalization converts a "the model has stored these instances" story into a "the model has the schema" story.

**Tier 4 — Inference-licensing.** The model treats the construction as licensing its characteristic *inferences*, where the inference is contributed by the construction and not by any lexical part. This is the strongest text-internal rung and the one that earns the `inferential` tag in Piantadosi & Hill's sense. The paradigm case is [`conjecture/way-construction`](../conjectures/way-construction.md): the *way*-construction contributes the path-traversal meaning, and the verbs (*whistle*, *elbow*, *drink*) are not motion verbs — so a high path-traversal "yes" rate for non-motion verbs, with a large gap against minimal-pair controls (`way-construction` Predictions 1–2, confirm threshold ≥70% / ≥30pp gap), is evidence that the *construction*, not the verb, is carrying the inference. [`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md) Prediction 2 (entailment flips after function-word swaps) reaches for this tier in the general case. Inference-licensing is the rung at which Piantadosi & Hill's claim becomes testable: systematic inference-preservation that the lexical items cannot explain is the behavioral signature of conceptual role.

The ladder is the page's claim, in compressed form: **form-acceptability < surprisal-contrast < gradient semantic tracking < generalization < inference-licensing.** Each upward step narrows the space of distributional-only explanations; only the top two steps are evidence for constructional *meaning* as opposed to constructional *form*.

## Where the existing wedge sits

- [`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md) — **Tier 0**, and the page that fixes Tier 0 as a floor rather than a proof. Status `proposed`; not contingent on any open decision.
- [`conjecture/aann-construction`](../conjectures/aann-construction.md) — spans **Tier 1 → Tier 3** (surprisal contrast, evaluative gradient, held-out generalization). Status `designed`; both governing decisions (`aann-stimulus-source`, `aann-operationalization`) were **ratified 2026-05-29**, fixing the yardstick — but the probe is **blocked, unrun**: its ratified indicator (continuation-likelihood logprob contrast, with a prompted-`p("good")` fallback) requires token logprobs, and the ratified panel exposes none on OpenRouter (verified 2026-05-29). A decision to substitute the panel or the indicator is queued for Tom (`NEXT.md`); until then no AANN result exists.
- [`result/comparative-correlative-covariation-v1`](../results/comparative-correlative-covariation-v1.md) — **the project's first probe of its own design to run**, and the first *positive* upper-ladder result: a **Tier-4 (inference-licensing)** pass with a **Tier-3 (atypical/generalization)** control passed, on the comparative correlative. The 2026 decoder panel deploys the CC's covariation meaning at ceiling — construction-driven (T1 +80–90 pp over matched controls), direction-tracking (T2 inverse-flip 95–100%), n-gram-robust (T3 no atypical collapse) — and matches the Scivetti ≈0.90 human baseline (93–100%). Status `proposed`. **Crucial caveat:** ceiling on an easy instrument is weak evidence for the strong reading, so this is read as "the [`source/weissweiler-2022-comparative-correlative`](../../base/sources/weissweiler-2022-comparative-correlative.md) encoder-era form/meaning dissociation is *not reproduced by this instrument*," not as proof of deep constructional processing. It is the first datum on the ladder that is both upper-tier *and* positive *and* of the project's own design.
- [`conjecture/dative-alternation-information-structure`](../conjectures/dative-alternation-information-structure.md) — **Tier 2** (gradient information-structure tracking). Anchor pending; not yet at design.
- [`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md) — **Tier 1 → Tier 4** in the general case, and the most abstract conjecture; its operationalization gate (what counts as a frequency-matched pair) is named as the place a loop could "quietly cheat." Anchor pending.
- [`conjecture/way-construction`](../conjectures/way-construction.md) — **Tier 4** (inference-licensing); the cleanest case where meaning is located in the construction. Anchor pending (Goldberg 1995 inventory; `way-construction-anchor`, with [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md) surfaced as a candidate Option D — a CxG-native inference anchor with a human baseline).
- [`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md) — **Tier 3 → Tier 4**, and the first claim on this ladder carrying in-repo *human-comparison* evidence rather than only a methodological commitment. It reads Scivetti et al. 2025's >40% divergent-form drop (GPT-o1) against a native-speaker baseline (≈0.90 / ≈0.83) as a *negative* result at the generalization / inference-licensing boundary for current models: the same surface form does not generalize to its divergent constructional meaning the way human speakers manage. Status `proposed`; `contingent-on: []` (it rests on the aggregate published result and aggregate baseline, not on the per-construction anchors). Anchored to [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md).

Read top-down, the project's existing wedge already targets every rung of the ladder. The *evidence in hand* changed materially this revision: in addition to one `proposed` Tier-0 claim (the AANN ceiling), the conjectures spanning Tiers 1–4, and the externally-grounded Tier 3→4 claim ([`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md), a *negative* aggregate finding from an external paper), the project now has its **first `result` page from a probe of its own design** — [`result/comparative-correlative-covariation-v1`](../results/comparative-correlative-covariation-v1.md), a *positive* upper-ladder result (Tier-4 inference-licensing, Tier-3 atypical control passed) on the comparative correlative.

This juxtaposition is the interesting tension and must not be flattened. The external Scivetti claim is a *negative* generalization result (a >40% drop on syntactically-identical/semantically-divergent forms, aggregate, GPT-o1); the project's own CC probe is a *positive* ceiling result on covariation inference. They are not in contradiction — they probe different things (Scivetti's hard case is *surface-identical, meaning-divergent* forms; the CC probe's items are *unambiguous* CC tokens with matched non-CC controls) — but together they sketch the live hypothesis: current decoders handle a well-marked construction's core inference at ceiling, while still failing where the *same surface form* must be split to a divergent meaning. The honest reading is that the *easy* direction of the upper ladder is now demonstrably climbable by current models, and the *hard* direction (divergent-form generalization) is where the remaining gap lives. Three cautions still bind: (i) the CC positive is a **ceiling result on an easy instrument** — weak evidence for any strong "deep processing" reading (its own *Limits* lead with this); (ii) it is a single panel/date/run with small N and only 30 human-anchored items; (iii) it does not touch the relational ladder or grounding. This page should be rewritten again when a harder CC v2 returns, when the AANN logprob blocker is resolved and that probe runs, or when the Scivetti per-construction subsets are probed directly.

## The under-explored axis: relational meaning

Every rung above is a `model-internal` probe — it asks what a single model knows. The charter's distinctive axis, `relational` meaning (meaning constituted *between* agents, not computed within one), is untouched by the ladder. [`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md) records this gap squarely: the founding conjectures "are all `model-internal` probes ... None touches the relational axis. Without a pilot here, the relational angle remains rhetoric." That open question is now sharpened to a concrete iterated dyadic reference-game pilot whose live-vs-shuffled-history contrast is the candidate bottom rung of the relational "second ladder."

The relational axis is not a higher rung of the same ladder; it is a *second ladder* whose bottom rung is not yet defined. The open question's own criterion — a measure distinguishing "meaning constituted between" from "meaning computed in each, then averaged," e.g. a behavior shift in one agent that depends on the *trajectory* of the other's prior outputs — is the project's standing IOU. This theory **supports** that open question by marking it as the natural extension: the form/meaning ladder is the first-loop object; a relational ladder is the second-loop object. Until a relational pilot exists, claims on this page are scoped to single-model constructional meaning.

## Open tensions

1. **Distributional null vs. constructional signal.** Tiers 1–3 must be read against the distributional null. A Tier-2 evaluative-adjective effect is only evidence for meaning *if* unigram frequency is controlled; otherwise it collapses back to Tier 1. `function-word-substitutability` makes this explicit: a null there "is a positive result for the distributional position, not a failure." The theory must not silently treat a distributional pass as a constructional pass.
2. **Inferential evidence vs. grounding.** Piantadosi & Hill would count Tier-4 inference-licensing as genuine meaning; Bender & Koller would say it is still form, because communicative intent is absent from the signal. This theory does not adjudicate. It records that Tier 4 is the ceiling of *text-internal* evidence and that the grounding question lies beyond it — a boundary, not a verdict.
3. **Memorization at every tier.** Weissweiler's confound is not retired by any single tier; it is *managed* by Tier 3 (held-out generalization). A Tier-4 result without a held-out check is interpretable as stored inference, not schematic inference.
4. **Formal/functional is a frame, not a measurement.** Mahowald's distinction sorts evidence; it does not itself measure constructional meaning. The ladder is the measurement instrument; the formal/functional cut tells us which rungs are "formal" (0–1) and which begin to be "functional/meaning" (2–4).

## What the theory predicts and forbids

**Predicts.** If LLMs have constructional meaning in the project's sense, then for a well-described construction we should observe a *coherent climb*: not just Tier-0 acceptability, but Tier-2 gradient tracking that survives frequency control, Tier-3 generalization to held-out items, and — for inference-bearing constructions like *way* — Tier-4 inference-licensing that the lexical items cannot explain. The tiers should rise together; a model with genuine constructional competence should not be strong at Tier 4 while failing Tier 2 on the same construction.

**Forbids.** The theory forbids three inferences:
- From Tier 0 to constructional meaning (the `formal-competence-aann-ceiling` block, generalized).
- From a frequency-uncontrolled gradient (Tier 1 dressed as Tier 2) to semantic tracking.
- From any text-internal tier (0–4) to grounded communicative meaning in Bender & Koller's sense, absent a separate grounding argument.

It also forbids promoting a contingent conjecture's eventual result to settled language while its `contingent-on` decisions are open — the AANN line is the live instance.

## Status and revision hook

`status: draft`. This page is `contingent-on: []` *directly* — it introduces no new empirical claim of its own and depends on no open decision in its own right. It leans on findings that are themselves contingent: [`conjecture/aann-construction`](../conjectures/aann-construction.md) is contingent on `aann-stimulus-source` and `aann-operationalization`, and three conjectures have anchors still pending. It also now leans on [`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md), which is itself `contingent-on: []` (it uses only the aggregate published result), so it does not import a new contingency — though its *per-construction* sharpenings remain gated by `caused-motion-anchor` / `conative-anchor` / `way-construction-anchor`, three decisions the newly-catalogued [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md) has been surfaced as a candidate anchor for (pending Tom). The prose above flags those dependencies as provisional rather than settled, per [`CLAUDE.md`](../../../CLAUDE.md) rule 5; this theory claims a *structure* (the ladder, the placements) plus one externally-grounded negative data point at the Tier 3→4 boundary — and not yet any *result* of the project's own.

This revision (2026-05-29, second of the day) incorporates the project's **first own-design probe result** ([`result/comparative-correlative-covariation-v1`](../results/comparative-correlative-covariation-v1.md)) — the revision trigger from the prior draft ("rewrite when the first probe of the project's own design returns a result") has now fired. It also corrects the AANN placement (the two AANN decisions are ratified, but the probe is logprob-blocked and unrun — a substitution decision is queued for Tom). Next revision triggers: a harder CC v2 that escapes the ceiling; resolution of the AANN logprob blocker and an AANN result; a direct probe of the Scivetti per-construction subsets; or a relational-meaning pilot defining the bottom rung of the second ladder ([`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md)).
