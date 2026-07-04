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
status: superseded
contingent-on: []
created: 2026-05-28
updated: 2026-07-04
links:
  - rel: depends-on
    target: result/dative-information-structure-v1
  - rel: depends-on
    target: result/dative-information-structure-v2
  - rel: refines
    target: claim/formal-competence-aann-ceiling
  - rel: depends-on
    target: claim/constructional-divergent-form-generalization-gap
  - rel: depends-on
    target: result/comparative-correlative-covariation-v1
  - rel: depends-on
    target: result/cxnli-distinction-divergence-v1
  - rel: depends-on
    target: result/scivetti-cxnli-answer-key-v1
  - rel: depends-on
    target: result/scivetti-let-alone-working-surface-v1
  - rel: depends-on
    target: result/conative-minimal-pair-divergence-v1
  - rel: depends-on
    target: result/caused-motion-minimal-pair-divergence-v1
  - rel: depends-on
    target: result/way-construction-traversal-v1
  - rel: depends-on
    target: result/argument-structure-coercion-v2
  - rel: depends-on
    target: result/conative-cancel-direction-v2
  - rel: depends-on
    target: result/coercion-implicit-cue-v2b
  - rel: depends-on
    target: result/comparative-correlative-covariation-v2
  - rel: depends-on
    target: result/comparative-correlative-covariation-v3
  - rel: depends-on
    target: result/caused-motion-near-miss-v2c
  - rel: depends-on
    target: result/function-word-swap-run-v2
  - rel: depends-on
    target: result/function-word-few-many-split
  - rel: depends-on
    target: result/function-word-modal-second-instrument
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
    target: concept/coercion
  - rel: depends-on
    target: concept/relational-meaning
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
  - rel: supports
    target: open-question/instrument-sensitivity-constructional-inference
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
  - rel: depends-on
    target: source/davis-2024-implicature-sep
---

# Theory (draft): evidence for constructional meaning in LLMs

> **SUPERSEDED (2026-07-04)** by the clean second edition
> [`theory/constructional-meaning-in-llms-v2`](constructional-meaning-in-llms-v2.md), per the
> theory-edition rule ([`PROTOCOL.md`](../../../PROTOCOL.md) §3: more than ~3 update boxes forces a
> rewrite). This page is kept visible as history — do not update it further; cite the second
> edition.

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

> **Rungs 2–3 climbed for AANN (2026-06-12).** [`result/aann-behavioral-gradient-v2`](../results/aann-behavioral-gradient-v2.md)
> is the first AANN run, under the ratified behavioral instrument (the surprisal indicator of
> the Tier-1 paragraph above was retired unexecutable; gradient elicitation is prompted, not
> likelihood-based). All three panel models **rank-track the empirical human Exp-2 gradient**
> (cell-level ρ 0.68–0.75, frequency- and noun-class-guarded — Tier 2) **and replicate the
> class gradient on a locked, frequency-matched held-out adjective list** (0.75–0.83 — Tier 3,
> with the honest caveat that replication is uneven by noun class: the temporal stratum comes
> out negative). The Tier-0 ceiling claim
> ([`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md)) is
> unchanged: this result is exactly the "separate meaning-diagnostic" its carve-out called for.
>
> **AANN's Tier 4 attempted (2026-06-13) — a ceiling-bounded NULL.** [`result/aann-inferential-v3`](../results/aann-inferential-v3.md)
> ran the inference-licensing arm (does the construction *shift* the unification/whole-evaluation
> reading vs a matched plural control?) at the ratified paraphrase-FC + NLI + singular-agreement
> package. **No model clears the shift bar** (paraphrase shift +0.17 / +0.04 / 0.00). But this is
> a **measurement null with a named cause, not a Tier-4 failure verdict**: the unification reading
> is the **default for the plural control too** (control rates 0.78–1.00), so the construction has
> no headroom to move it — and the under-pressure subset (distributive locally fluent) did not
> rescue it. This is the ladder's first encounter with the limit
> [`open-question/distributional-vs-inferential-constructional`](../open-questions/distributional-vs-inferential-constructional.md)
> warned of: at Tier 4 the inferentially-licensed reading and the distributional default
> **coincide**, so a shift-from-control design cannot separate them unless the control's default is
> engineered to be *distributive*. The lone positive — gpt-5.4-mini's **grammaticalized
> singular-agreement reflex (+0.74)** — sits at the **form/agreement** rung, not the inference
> rung (the pre-registered headline-gating refused to read it as inference), reinforcing the
> recurring AANN pattern: strong on *form*, unproven on *inferential use*.
>
> **AANN's Tier 4, second attempt (2026-06-13, fifth session) — PARTIAL: the ceiling was removed
> and a real construction effect appeared.** [`result/aann-inferential-v4`](../results/aann-inferential-v4.md)
> implemented the fix the v3 null demanded: a **distributive-default control** (an itemizing "on each
> of the three days…" frame) whose baseline reading is genuinely distributive, plus a **lexical-cue
> control**, so the headline is a double contrast Δ² = P(uni|AANN) − P(uni|LCC). The control read
> distributive at baseline for all three models (P(uni|DDC) = 0 / 0.22 / 0 — the v3 ceiling is gone),
> and against it **all three models shift paraphrase selection toward unification** (Δ² +0.78 / +0.70
> / +0.96, net of the cue). So the ladder's Tier-4 limit the v3 null hit — *inference and default
> coincide* — is **escapable**: with a headroom-bearing control the construction's effect on the
> reading is measurable. But it **converges across instruments (paraphrase + NLI + the
> grammaticalized agreement reflex) in only one model, gpt-5.4-mini**; claude and gemini show the
> paraphrase shift **without** NLI convergence or the agreement reflex (PARAPHRASE-ONLY). So the AANN
> reaches a **clearing-the-bar Tier-4 signal for one of three models**, with the standing caution
> that a forced-choice paraphrase preference is weaker than a converging NLI + agreement shift — for
> the two paraphrase-only models, read it as a shift in *paraphrase preference*, not inference. The
> instrument disagreement is the largest in the record (|FC−NLI| up to 1.04), feeding
> [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md);
> `internal-contrast-only`. (An independent verifier caught and fixed an NLI-aggregation bug to the
> frozen spec; the overall PARTIAL verdict was unchanged.)
>
> **The AANN agreement reflex generalizes beyond gpt on held-out items — a form/agreement-rung
> result, not an inference upgrade (2026-06-14, sixth session).** [`result/aann-agreement-reflex-v5`](../results/aann-agreement-reflex-v5.md)
> re-ran the ratified was/were agreement arm (the grammaticalized singular-agreement reflex — the one
> place a distributional account predicts the *opposite* of the construction's single-unit construal)
> on 30 fresh held-out items. **gpt-5.4-mini replicates** its reflex (+0.43, attenuated from v3/v4 but
> clearing a stricter τ=+0.30), and **claude-sonnet-4.6 shows it off the ceiling** (+0.33; its
> bare-plural control falls to 0.667 *was* where v3/v4 had it pinned at ceiling) → the reflex is **not
> gpt-specific**. gemini stays at ceiling. The verdict is bounded: claude's shift is a clean within-item
> contrast but is **temporal-subset-driven** (distance stays at ceiling) and one item above the bar, so
> the v3/v4 "agreement ceiling for claude/gemini" reading was **item-set-bound**, not structural. This
> sits at the ladder's **form/agreement rung, not the inference rung** (the pre-registered gating still
> refuses to read agreement as inference), so it does **not** move v4's PARTIAL inferential verdict; it
> says the *form*-side reflex is robust to held-out material and present in two of three models.
>
> **AANN's Tier-4 PARTIAL replicates, powered, on fresh held-out adjectives (2026-06-14, ninth
> session).** [`result/aann-inferential-v6`](../results/aann-inferential-v6.md) re-ran the v4 design
> **unchanged** (same instrument, thresholds, verdict map, analysis code) on a fresh, larger item set —
> **40 held-out items** (temporal 20 / distance 20, adjectives disjoint from v4 and the v5-reflex probe).
> Both pre-registered questions came back **yes**: the panel-wide paraphrase double contrast **holds up
> powered** (Δ² +0.875 / +0.575 / +0.90, all CI-clear, headroom PASS all), and **gpt-5.4-mini's
> cross-instrument convergence replicates** (paraphrase + NLI Δ² +0.225 + agreement +0.60 →
> CONVERGENT-POSITIVE), with claude and gemini again PARAPHRASE-ONLY (NLI null, agreement at ceiling).
> Verdict **PARTIAL**, cell-for-cell as v4. The Tier-4-for-one-model signal is therefore not a small-N or
> single-date artifact: the construction's effect on the paraphrase reading is **stable in magnitude
> across two disjoint item sets**, and gpt's is the only model whose effect survives onto the
> distributionally-dispreferred agreement reflex. The single-panel and expert-stipulated-key caveats
> stand; `internal-contrast-only`. The instrument disagreement replicates as the record's sharpest
> (|FC−NLI| up to 0.925), still feeding the instrument-sensitivity open question.

> **The AANN preference/commitment dissociation does NOT generalize to the conative (2026-06-15,
> twelfth session).** [`result/conative-preference-commitment-v1`](../results/conative-preference-commitment-v1.md)
> ran the *same* double-contrast preference-vs-commitment instrument on a fresh divergent-default
> construction (the conative), testing whether the AANN shape ([`essay/preference-without-commitment`](../essays/preference-without-commitment.md))
> is general — **VERDICT INCONCLUSIVE**. The AANN shape did not reproduce: the paraphrase double
> contrast was **non-positive in all three models** (a bare-*at* lexical cue absorbs the
> cancel-preference, so the broad "preference" component has no construction-specific analogue here),
> and the only construction effect was a **single model's commitment-only** shift (claude Δ²_commit
> +0.46) — the *mirror* of AANN. So the instrument-sensitivity story is now **construction-particular**:
> the two instruments *can* dissociate (AANN), but the *way* they dissociate does not transfer, and on
> the conative it is the weaker paraphrase instrument that shows no construction-specific signal at all.
> The preference-without-commitment ordering reads as **AANN-specific so far** ([`conjecture/preference-commitment-generality`](../conjectures/preference-commitment-generality.md),
> tested → not confirmed). One construction cannot prove AANN-uniqueness; the way/caused-motion
> near-miss fallback could revisit it. Headroom PASS all three (not a ceiling artifact); NLI conative
> arm human-anchored to CxNLI (answer-key), FC/resist arms `internal-contrast-only`.
>
> **Update — the lone counter-signal does not replicate (2026-06-15, thirteenth session).** A direct
> replication of claude's commitment-only effect on a **fresh, disjoint** conative verb set
> ([`result/conative-commitment-replication-v2`](../results/conative-commitment-replication-v2.md), same
> instrument/scoring, `analyze.py` byte-identical) found it **collapsed +0.46 → +0.04** (CI [−0.29,
> 0.33], not positive): all three models are now LEXICAL-CUE ARTIFACT, so the v1 anomaly was
> **verb-set-specific noise**. The conative therefore reads as a **clean no-dissociation construction on
> both arms across two independent samples** — strengthening the AANN-specific reading and removing the
> one apparent exception. This sits with the wider instrument-sensitivity picture: a wide-CI single-model
> directional effect is exactly the kind of signal that should be replicated before it is theorized, and
> here replication correctly retired it.
>
> **The bounded close is now a typed claim (2026-06-15, fourteenth session).** The synthesis those two
> updates point to is recorded as a first-class claim:
> [`claim/preference-commitment-dissociation-aann-specific`](../claims/preference-commitment-dissociation-aann-specific.md)
> (`status: supported`, `anchor: internal-contrast-only`) — on the evidence so far the
> preference-without-commitment dissociation is **AANN-specific**, replicating across two disjoint AANN
> item sets but not reproducing on the conative across two verb samples in either direction. It carries
> the ladder caution explicitly: a forced-choice paraphrase-preference shift can be produced by a bare
> lexical cue (the conative bare-*at* case), so such a shift is Tier-4-relevant evidence about
> distributional compatibility at most, **not** evidence of inference-licensing on its own. Calibrated to
> "AANN-specific *so far*" — only one alternative construction has been tested.

> **The dative alternation tracks information structure — a clean Tier-2 panel positive, human-anchored
> to corpus production (2026-06-20, session 51).** [`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md)
> ran the project's return to its grammatical core under the ratified operationalization
> ([`decisions/resolved/dative-anchor-and-indicator`](../../decisions/resolved/dative-anchor-and-indicator.md)).
> **All three panel models CONFIRM**: each shifts its double-object-vs-prepositional-dative preference in
> the human direction (given recipient → DOC, given theme → PD) across a manipulation that holds length
> and animacy **identical by construction** — so the within-item shift is provably immune to any
> length/position/order shortcut (build-certified: all eight shortcut readers → shift 0) — and the effect
> **survives the control arm** that makes the given constituent the *longer* one (information structure vs.
> end-weight), so it is not a short-before-long heuristic. This is the ladder's **Tier 2** (gradient
> semantic tracking), and the project's **first human-anchored Tier-2 positive of its own design** —
> anchored to a corpus *production* surface ([`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md),
> Bresnan et al. 2007), the apt human signal for a production-preference indicator. It patterns with the
> recurring **add/easy-direction** observation: current decoders track a well-described soft constraint in
> the human direction cleanly. Two sharp, calibrating notes: (i) **prediction 3 (effect-size decorrelation)
> is confirmed in the strongest form yet** — the shift spans an order of magnitude (gemini +0.52 ≫ claude
> +0.33 ≫ gpt +0.06), with gpt a weak-but-clearing CONFIRM (~1/10 gemini's size); so "the panel does it"
> conceals a large competence spread the binary verdict hides. (ii) It is a gradient *preference* effect,
> **not** Tier-4 inference-licensing — the construction is not contributing an entailment the lexical items
> cannot supply. The secondary corpus-gradient Spearman (ρ 0.48–0.83) strengthens but is non-decisive by
> pre-registration. Single panel/date/run, small N; a graded-preference, not logprob, measure.
>
> **Replicated on a fresh, disjoint item set (2026-06-20, session 53) — the panel positive holds but is
> qualified.** [`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md)
> re-ran the byte-identical design on 44 newly authored items (same ratified operationalization, no new
> decision). **claude (+0.325 vs +0.327) and gemini (+0.500 vs +0.524) reproduced almost exactly** and
> again survive the control arm, but **gpt's v1 CONFIRM did not replicate**: its shift fell to +0.018 with
> a bootstrap CI including zero (WEAK). So the panel verdict drops from **3/3 to 2/3 CONFIRM**, the
> order-of-magnitude spread *widened* (≈9×→≈27×) rather than compressing, and note (i)'s decorrelation is
> firmed up: v1's concordant 3/3 demonstrably hid a fragile member whose pass did not survive replication
> (the reading discipline of [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md),
> whose revision trigger (c) this fires). The Tier-2 placement is unchanged for the two reproducing models
> and is now twice-observed at near-identical magnitude on disjoint items.

**Tier 4 — Inference-licensing.** The model treats the construction as licensing its characteristic *inferences*, where the inference is contributed by the construction and not by any lexical part. The paradigm Tier-4 phenomenon is [`concept/coercion`](../../base/concepts/coercion.md) — the construction overriding a verb that does not lexically carry the inference (*sneeze the napkin off the table*), so any systematic reading of the inference must come from the construction. This is the strongest text-internal rung and the one that earns the `inferential` tag in Piantadosi & Hill's sense. The paradigm case is [`conjecture/way-construction`](../conjectures/way-construction.md): the *way*-construction contributes the path-traversal meaning, and the verbs (*whistle*, *elbow*, *drink*) are not motion verbs — so a high path-traversal "yes" rate for non-motion verbs, with a large gap against minimal-pair controls (`way-construction` Predictions 1–2, confirm threshold ≥70% / ≥30pp gap), is evidence that the *construction*, not the verb, is carrying the inference. [`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md) Prediction 2 (entailment flips after function-word swaps) reaches for this tier in the general case. Inference-licensing is the rung at which Piantadosi & Hill's claim becomes testable: systematic inference-preservation that the lexical items cannot explain is the behavioral signature of conceptual role.

> **The function-word swap reaches this rung — but "function word" is not one inferential kind, so the load is type-specific, not uniform (2026-06-21).** [`result/function-word-swap-run-v2`](../results/function-word-swap-run-v2.md)
> ran the project's most abstract constructional bet ([`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md)
> Prediction 2) as a within-model contrast: how often does swapping a **function word** flip a 3-way
> NLI label vs swapping a **frequency+length-matched content word**? **All three panel models CONFIRM** —
> "Function-word swaps change the inference vastly more often than frequency+length-matched content-word
> swaps, and the **content control behaves exactly as designed** — matched content swaps almost never flip
> the label" (per-model contrast claude +0.340, gpt +0.825, gemini +0.859, every bootstrap lower bound
> clear of zero). The falsify arm did not fire: "Content-swap flip rates are near zero for every model
> (1.0% / 4.4% / 3.4%)" and "the falsify arm (content ≥ function) **did not fire** in any model or any arm."
> This is **strong support for the constructional reading over the pure-distributional null** at this rung:
> a content swap of equal frequency and length leaves the inference alone, so it is not matched-frequency
> distributional neighbourhood that moves these inferences — the closed-class swap is. It belongs with the
> page's **add direction is easy** observation, now extended to closed-class items.
>
> **But the pooled CONFIRM hides type-structure that bears directly on this page's "tiers rise together"
> prediction and on Open Tension 1.** The per-arm contrast (flip_fn − flip_ct) is **not uniform across
> function-word types**: `because`→`although` (subordinator) **+1.000 / +0.875 / +1.000** and `some`→`every`
> (existential→universal quantifier) **+0.929 / +0.750 / +0.750** flip the inference almost every time in
> every model — the cleanest Tier-4 closed-class signal; but `will`→`would` (future→conditional modal) is
> **+0.000 / +0.000 / +0.150**, essentially null across the panel — the models read "the council *would* see
> the visitor next week" as "still entailing 'the council is going to see the visitor next week,' not as the
> irrealis/conditional shift the design predicted"; and `few`→`many` (paucal→multal quantifier) **splits the
> panel** at **+0.095 / +0.960 / +0.960** (claude near-null, gpt/gemini near-total). A companion within-model
> re-analysis localizes that split entirely on the "Many X → All X" reading (claude keeps it a contradiction,
> gpt/gemini relax it to neutral), without claiming which reading is correct or that any model "computes" an
> implicature ([`result/function-word-few-many-split`](../results/function-word-few-many-split.md)).
>
> **Two consequences for the ladder.** (i) **Prediction 3 ("not driven by a few categories") holds at the
> *content-class* level but fails at the *function-word-type* level.** "Every **content semantic class** (adj,
> noun_person, noun_thing, verb) shows flip_fn > flip_ct in every model," but "across **function-word types**
> the effect is *not* uniform: two of four arms (the modal `will`, and `few` for claude) are near-null" — the
> asymmetry is "carried by a **subset of function-word types** ... not uniformly by all closed-class items."
> So **"constructional load" is not one quantity attached to a part-of-speech class**; it is type-specific,
> the conceptual correction argued in [`essay/function-words-not-one-category`](../essays/function-words-not-one-category.md).
> (ii) **The pooled magnitude is *not* a model-capability ranking.** Because `few` is **126/206 (61%)** of
> items, the pooled contrast is dominated by it; claude's lower +0.34 "is **dragged down** by its near-null
> `few` arm (claude is actually at ceiling on `because`/`some`)," so "The same 'CONFIRM' therefore rests on
> **different arms for different models**" and "The cross-model magnitude spread is an artifact of the
> `few`-arm split × `few`-arm dominance, not evidence that claude has a weaker general function-word
> sensitivity (it does not — see `because`/`some`)." This is a sharper instance of the **carry-the-spread**
> discipline ([`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md)): a 3/3
> concordant verdict here conceals not just a magnitude spread but that the *concordance itself rests on
> different items per model*. **The modal near-null does NOT generalize (2026-06-21, session 71):**
> [`result/function-word-modal-widening`](../results/function-word-modal-widening.md) widened the modal arm
> and found `must`→`might` (necessity→possibility, **but crossing deontic→epistemic flavor — a category
> mismatch, the easy non-entailment, not a clean within-scale test**) flips at **ceiling in all three
> models**, while the clean within-scale `shall`→`should` (deontic obligation→advisory) **splits the panel**
> (gemini 0.778 vs claude/gpt 0.056, resting on one content pair),
> while `will`→`would` replicates the null — so under NLI the near-null *looked* like a
> **future→conditional-specific** fact. The NLI instrument registers a modal swap in proportion to how
> truth-conditionally "loud" it is (loud category mismatch > within-deontic-strength, partly model-dependent
> > subtle irrealis). **But a SECOND instrument relocates the nulls to the instrument itself (2026-06-21,
> session 72):** [`result/function-word-modal-second-instrument`](../results/function-word-modal-second-instrument.md)
> holds the modal swap byte-identical and changes only the indicator (3-way NLI → a single-token
> forced-choice modal-force preference). It **registers** `will`→`would` in all three models (claude 6/20,
> gpt 13/20, gemini 17/20, CIs clear zero) where NLI flipped 0/0/3, and the `shall`→`should` NLI panel-split
> **dissolves** into concordance (17/18, 18/18, 18/18) — so the modal nulls/splits were
> **NLI-instrument-specific, not relation-intrinsic**. This is the strongest in-repo demonstration that
> *which closed-class swap reaches this rung is co-determined by the inferential **instrument's**
> calibration, not by the part-of-speech class* — the conceptual correction of
> [`essay/function-words-not-one-category`](../essays/function-words-not-one-category.md), now shown by
> direct manipulation rather than read off the arms (essay trigger (c), fired positive). **Bounded:** the
> forced-choice `will` HEDGE option names the irrealis reading, so this licenses the *relocation* (the null
> was not relation-intrinsic), not a "robustly inferential" claim — a registered preference is weaker than a
> computed entailment. `internal-contrast-only` — no human comparison (a BLiMP/NLI human baseline stays an
> optional, not-in-repo upgrade).
>
> **An external semantics typology now grounds the split *a priori* (2026-06-21, session 73):**
> [`source/davis-2024-implicature-sep`](../../base/sources/davis-2024-implicature-sep.md) (Davis's SEP
> "Implicature") supplies the classification the type-specificity reading had been making off the arms. A
> 3-way NLI judgment probes *what is said* — at-issue, truth-conditional content — and is by construction blind
> to a *scalar implicature*, since on the standard view "conversational implicatures cannot be [entailed]" by
> what is said. So which closed-class swaps reach this rung *under NLI* is **predicted, not observed post hoc**:
> the at-issue swaps register (`some`→`every`; the causal content of `because`), the scalar swap (`few`→`many`)
> is the licensed-divergence arm, and the modal arm is modal semantics handled by trigger (c). This converts
> the essay's calibrated reading "from interpretation toward claim" — **bounded:** a typology that *predicts*
> the pattern is corroboration, not a demonstration that the models *compute* implicatures, and Davis reports
> the non-entailment of implicature as the standard-but-contested view
> ([`essay/function-words-not-one-category`](../essays/function-words-not-one-category.md), trigger (d), fired).

The ladder is the page's claim, in compressed form: **form-acceptability < surprisal-contrast < gradient semantic tracking < generalization < inference-licensing.** Each upward step narrows the space of distributional-only explanations; only the top two steps are evidence for constructional *meaning* as opposed to constructional *form*.

## Where the existing wedge sits

- [`claim/formal-competence-aann-ceiling`](../claims/formal-competence-aann-ceiling.md) — **Tier 0**, and the page that fixes Tier 0 as a floor rather than a proof. Status `proposed`; not contingent on any open decision.
- [`conjecture/aann-construction`](../conjectures/aann-construction.md) — spans **Tier 1 → Tier 3** (surprisal contrast, evaluative gradient, held-out generalization). Status `designed`; both governing decisions (`aann-stimulus-source`, `aann-operationalization`) were **ratified 2026-05-29**, fixing the yardstick — but the probe is **blocked, unrun**: its ratified indicator (continuation-likelihood logprob contrast, with a prompted-`p("good")` fallback) requires token logprobs, and the ratified panel exposes none on OpenRouter (verified 2026-05-29). A decision to substitute the panel or the indicator is queued for Tom (`NEXT.md`); until then no AANN result exists.
- [`result/comparative-correlative-covariation-v1`](../results/comparative-correlative-covariation-v1.md) — **the project's first probe of its own design to run**, and the first *positive* upper-ladder result: a **Tier-4 (inference-licensing)** pass with a **Tier-3 (atypical/generalization)** control passed, on the comparative correlative. The 2026 decoder panel deploys the CC's covariation meaning at ceiling — construction-driven (T1 +80–90 pp over matched controls), direction-tracking (T2 inverse-flip 95–100%), n-gram-robust (T3 no atypical collapse) — and matches the Scivetti ≈0.90 human baseline (93–100%). Status `proposed`. **Crucial caveat:** ceiling on an easy instrument is weak evidence for the strong reading, so this is read as "the [`source/weissweiler-2022-comparative-correlative`](../../base/sources/weissweiler-2022-comparative-correlative.md) encoder-era form/meaning dissociation is *not reproduced by this instrument*," not as proof of deep constructional processing. It is the first datum on the ladder that is both upper-tier *and* positive *and* of the project's own design.
- [`conjecture/dative-alternation-information-structure`](../conjectures/dative-alternation-information-structure.md) — **Tier 2** (gradient information-structure tracking). **Tested 2026-06-20 → CONFIRM, 3/3 models** ([`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md)); **replicated 2026-06-20 on a disjoint item set → CONFIRM holds but 2/3** ([`result/dative-information-structure-v2`](../results/dative-information-structure-v2.md): claude & gemini reproduce near-identically, gpt's CONFIRM falls to WEAK, the effect-size spread widens). The first human-anchored Tier-2 positive of the project's own design (see below). Status `tested`; anchor ratified ([`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md)).
- [`conjecture/function-word-substitutability`](../conjectures/function-word-substitutability.md) — **Tier 1 → Tier 4** in the general case, and the most abstract conjecture; its operationalization gate (what counts as a frequency-matched pair) is named as the place a loop could "quietly cheat." **Tested 2026-06-21 → CONFIRM, 3/3 models** ([`result/function-word-swap-run-v2`](../results/function-word-swap-run-v2.md)): swapping a function word flips 3-way NLI far more than swapping a frequency+length-matched content word, with the matched-content control near-floor and the falsify arm unfired — strong support for constructional over pure distributional meaning. But the per-arm breakdown shows the inferential load is **type-specific, not uniform across closed-class items** — so prediction 3 holds at the *content-class* level and fails at the *function-word-type* level (see the dedicated block below). Status `tested`; `anchor: internal-contrast-only` (ratified — no human comparison).
- [`conjecture/way-construction`](../conjectures/way-construction.md) — **Tier 4** (inference-licensing); the cleanest case where meaning is located in the construction. Status `tested` (2026-05-29); anchor ratified (`way-construction-anchor` → [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md) way-manner subset; Goldberg 1995 inventory seed). **Probed this session** → [`result/way-construction-traversal-v1`](../results/way-construction-traversal-v1.md), a Tier-4 positive above the ratified bar (see below).
- [`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md) — **Tier 3 → Tier 4**, and the first claim on this ladder carrying in-repo *human-comparison* evidence rather than only a methodological commitment. It reads Scivetti et al. 2025's >40% divergent-form drop (GPT-o1) against a native-speaker baseline (≈0.90 / ≈0.83) as a *negative* result at the generalization / inference-licensing boundary for current models: the same surface form does not generalize to its divergent constructional meaning the way human speakers manage. Status `proposed`; `contingent-on: []` (it rests on the aggregate published result and aggregate baseline, not on the per-construction anchors). Anchored to [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md).

Read top-down, the project's existing wedge already targets every rung of the ladder. The *evidence in hand* changed materially this revision: in addition to one `proposed` Tier-0 claim (the AANN ceiling), the conjectures spanning Tiers 1–4, and the externally-grounded Tier 3→4 claim ([`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md), a *negative* aggregate finding from an external paper), the project now has its **first `result` page from a probe of its own design** — [`result/comparative-correlative-covariation-v1`](../results/comparative-correlative-covariation-v1.md), a *positive* upper-ladder result (Tier-4 inference-licensing, Tier-3 atypical control passed) on the comparative correlative.

This juxtaposition is the interesting tension and must not be flattened — and this session it became a *within-project* tension, because the project ran **both** sides itself. [`result/cxnli-distinction-divergence-v1`](../results/cxnli-distinction-divergence-v1.md) is the second own-design probe: it ran the panel on Scivetti's base vs. distinction items and found the divergent-form gap **reproduces** (mean ≈39 pp base→distinction drop, convergent across all three models, conative hardest at 55–75 pp). So the two own-design results point in opposite directions, consistently: the **CC probe is a *positive* ceiling result** on an unambiguous construction's core covariation inference; the **distinction probe is a *negative* result** where the *same surface form* must be mapped to a divergent constructional meaning. They are not in contradiction — they probe different things (unambiguous construction → its core inference, vs. surface-identical → divergent meaning) — and together they sketch the live hypothesis cleanly: current decoders handle the **easy direction** of the upper ladder at ceiling and fail the **hard direction** (divergent-form generalization). The distinction probe is the one that *discriminates* (it is off ceiling); the CC probe is the one whose ceiling is the caution.

A later session (2026-06-20) **completed the base side** of that distinction probe: [`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md) ran the panel on the **full** 390-item Scivetti Exp-1 base task across all 8 constructions (the distinction probe's base arm was a 20-item subsample of 5 — limit 1, now discharged). On the base task **2/3 models reach the human ≈0.90 native-speaker accuracy** (claude 0.903, gemini 0.915 both have CIs covering 0.90; gpt-5.4-mini 0.813, ~9 pp below — the same model weakest on the distinction base arm, so the ordering reproduces). The new locus: the single construction **all three** fail is the **phrasal scalar `let-alone`** (0.46–0.67, near 3-way chance), which was **absent** from the distinction study's argument-structure set — so the "easy base direction" generalization holds for the argument-structure constructions (caused-motion/way/conative all at or near ceiling on the base task) but **not** for a scalar phrasal construction. Two honest bounds carry: it is **answer-key agreement under possible training-data contamination** (so the `let-alone` *failure* is the robust signal, the matches the weak one), and the add-vs-cancel base accuracies are small and **sign-inconsistent** (claude's conative is *highest*), which is **consistent with** — not a test of — the monotonicity asymmetry's own claim that its effect lives in the de-confounded cue arms, not base answer-key accuracy.

> **The `let-alone` failure is largely an OUTPUT-CHANNEL artifact, not a scalar-phrasal *competence* boundary (2026-06-20, session 58).** [`result/scivetti-let-alone-working-surface-v1`](../results/scivetti-let-alone-working-surface-v1.md) ran the witness-seeking control the project's own methodological spine prescribes for a forced-format near-chance negative ([`essay/output-channel-confound`](../essays/output-channel-confound.md), [`essay/undischargeable-negative`](../essays/undischargeable-negative.md)): re-run the SAME `let-alone` (24) + a comparative-correlative ceiling control (30) under a **working surface** (step-by-step + `FINAL:` tag), format-only, everything else byte-identical and gemini's reasoning-effort knob held constant. **2/3 models LIFT to the human baseline on the same items**: claude 0.542 → 0.792 and gemini 0.667 → 0.917 (within-item sign test 7 gains / 1 loss, p = 0.035 each; both CIs now cover 0.90), with the control PRESERVED (so the format did not break the instrument). So the session-57 cross-model dissociation above is **substantially a channel artifact** — `let-alone` inference is scalar/serial (order two clauses on a scale, then compute the a-fortiori direction), and a forced single-token channel masks that serial work; an *argument-structure-vs-scalar-phrasal* split is therefore **NOT a new content-type axis on this ladder**, it is a **channel-sensitivity** difference (the scalar construction needs a working surface; the argument-structure ones do not). This refines the **scope** of [`essay/output-channel-confound`](../essays/output-channel-confound.md), which had scoped single-premise NLI *out* of the channel confound: the cut is not at the *task* (NLI) but at whether the *inference is serial* — a scalar single-premise NLI item carries masked working after all (its revision trigger (a), fired). **One honest residue:** gpt-5.4-mini did **not** recover (0.375), but the verifier showed it largely **declined** the offered surface (16/24 bare one-token answers, 0 reasoning tokens), so its persistence is **channel non-uptake**, not a demonstrated channel-controlled failure — trigger (b) stays open, needing an uptake-inducing arm (few-shot / forced decomposition). Net for the ladder: the easy/hard split the section above frames is **not** widened by a scalar-phrasal axis; the `let-alone` datum collapses into the standing instrument/channel-sensitivity theme (cf. [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md)) and the recurring gpt-as-fragile-member ordering.

A **third own-design result this session sharpens this picture**: [`result/conative-minimal-pair-divergence-v1`](../results/conative-minimal-pair-divergence-v1.md) ran the project's *own* verb-held-constant conative minimal pairs (the corroboration this page previously listed as a revision trigger). It is a **Tier-4 (inference-licensing) result with the cleanest verb-control the wedge has run** (verb identical across the two frames; non-completion reading persists on low-frequency objects, Tier-3 control passed), and it lands **between** the CC ceiling and the distinction collapse: 2/3 models (claude, gemini) cleanly cancel the completed-contact entailment for the conative *at*-frame (forced-choice gap 67/88 pp; NLI 54/67 pp), and even gpt-5.4-mini does under forced-choice (42 pp) — but gpt-5.4-mini **fails the conative entirely under NLI** (treats *kicked at the ball* as entailing contact). Two things this adds to the theory: (a) it **refines** the distinction probe's "conative collapses hardest" — the collapse there reflects partly the *adversarial difficulty* of Scivetti's distinction items, not a blanket inability, since the clean minimal-pair contrast is substantially tracked; and (b) it surfaces **instrument-fragility as a first-class variable** — the *same* model can carry a constructional inference under forced-choice and lose it under NLI, so a single-instrument result mis-states competence. The "tiers rise together" prediction (below) is complicated by this: competence can be present yet elicitation-dependent. This elicitation-dependence now has its own typed home, [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md), which collects the cross-instrument evidence (the conative collapse here; the milder *way* conservatism) and asks whether instrument-disagreement is a model-specific artifact, a cancel-vs-add structural effect, or a measurement-noise floor on every Tier-4 reading.

A **fourth own-design result, same session, completes the argument-structure pair**: [`result/caused-motion-minimal-pair-divergence-v1`](../results/caused-motion-minimal-pair-divergence-v1.md) ran the project's own caused-motion minimal pairs and found the panel affirms the construction's causation-of-motion entailment onto **non-motion verbs at ceiling** (90–100%, gap 70–100 pp, 3/3 models, atypical-robust), while correctly *withholding* it when the object moves by another cause (the causation-specific control passes — genuine causal attribution, not motion detection). This is a Tier-4 **positive at ceiling**, like the CC. The juxtaposition with the conative yields the session's sharpest structural observation: **adding** a construction-contributed entailment (caused-motion) is *easy* — ceiling for every model on both instruments — whereas **cancelling** a lexically-default entailment (the conative's completed-contact) was *harder* and instrument-fragile (gpt-5.4-mini failed it under NLI but handles caused-motion fine under both). The tentative generalization the ladder should now carry: current decoders more readily *license* a construction's added inference than *suppress* a default one. Both remain ceiling/near-ceiling cautions — the easy direction of the upper ladder.

A **fifth own-design result, same session, completes the argument-structure set**: [`result/way-construction-traversal-v1`](../results/way-construction-traversal-v1.md) ran the project's own way-construction minimal pairs (18 non-motion verbs × {way, location-control, motion-control} + idiomatic guards) and found the panel draws the construction's path-traversal entailment onto non-motion verbs **above the ratified bar in 3/3 models on both instruments** (way 77.8–100%, gap 77.7–100 pp over the location control), with the anti-motion verb-reading guard holding at/near ceiling and the idiomatic over-generalization guard at 0%. The *way*-construction was the **paradigm Tier-4 case named in the ladder above** — and it now sits there as a confirmed positive. It is an "add" case and **patterns with caused-motion** (the easy direction), reinforcing the session's structural observation: decoders more readily *license* a construction-contributed inference than *suppress* a lexically-default one. The one cross-model split (gpt-5.4-mini declines 4–5 scattered manner/activity items as "may or may not have moved," while affirming the harder anti-motion items at 100%) is conservative-not-wrong and, like the conative, flags elicitation-sensitivity rather than absence of competence. Same ceiling caveat as CC/caused-motion.

A **sixth own-design result — the first *off-ceiling* one — directly stresses caution (i)**: [`result/argument-structure-coercion-v2`](../results/argument-structure-coercion-v2.md) ran a conflicting-cue probe on the two add-direction positives (caused-motion, way), holding the construction + verb constant and appending an explicit clause that **denies** the added inference. If the v1 ceilings were a brittle "this-frame→yes" template (H-default), the denial would be ignored; instead **all three models drop to floor on the cue items (affirm 0–20%, a 60–100 pp drop from canonical, 3/3 models, both instruments, both constructions)** — they withhold the inference when the cue cancels it. So the add-direction ceilings are **cue-sensitive computation, not a brittle template** (H-deep over H-default). This *upgrades* the modest reading of the v1 positives — they survive an off-ceiling stress test. **Two bounds keep it calibrated:** the cue tested is an *explicit verbal denial* (the easy end of conflicting-cue; a subtler world-knowledge cue is unrun), and a construction asymmetry appears — the way-construction coerces traversal even on a self-motion-precluding `resist` verb (it carries traversal independent of the verb), where caused-motion's verb-dependent causal attribution is correctly blocked by a cognition verb. The probe is internal-contrast-only (no human anchor on conflicting-cue items, ratified).

**Three more own-design results (2026-05-30) resolve two of the standing cautions and add a unifying observation.** They are off-ceiling follow-ups, run as a single workflow wave:

- **(7th) The add/cancel asymmetry survives de-confounding** — [`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md) ran the **matched** off-ceiling *cancel*-direction probe (the conative in the same conflicting-cue paradigm as the add-direction v2). At matched task structure the transitive lexical default is at ceiling but conative **suppression-no-cue** is off-ceiling and variable (NLI [58.3, 0, 66.7]; FC [66.7, 33.3, 83.3]), where the add-direction's matched **licensing-no-cue** was ~ceiling. gpt-5.4-mini fails suppression entirely under NLI; gemini over-suppresses under FC. So "license-easier-than-suppress" is **about direction, not ceiling** — the asymmetry the prior revision flagged as confounded is now (modestly) **established off ceiling**, and the cancel direction carries *more* instrument/model fragility than the add.
- **(8th) The add-direction "H-deep" reading is bounded to explicit-outcome parsing** — [`result/coercion-implicit-cue-v2b`](../results/coercion-implicit-cue-v2b.md) ran the subtler **implicit world-knowledge** cue (an immovable object, no outcome stated). Decoders affirm the *physically impossible* coercion at near-ceiling (implicit-wk 90–100%) and only floor under an **explicit** outcome denial — even under FC, claude/gemini still affirm it; only gpt-5.4-mini partially engages world knowledge. So the v2 cue-sensitivity is **explicit-outcome parsing, not world-model integration**: the Tier-4 "computes-and-withholds" reading is weaker than v2 alone implied.
- **(9th) The CC ceiling survives off-ceiling stress** — [`result/comparative-correlative-covariation-v2`](../results/comparative-correlative-covariation-v2.md) ran conflicting-cue + multi-step + paraphrase arms. The panel follows the construction against conflicting world knowledge (~100% NLI, 83–100% FC) and **composes** two-step covariation chains (100%, incl. the diagnostic negative×negative=positive case that a single-clause heuristic fails) — not a covariation-asserting bias. The CC is the project's **most robust constructional positive**; its v1 ceiling was not mere task-easiness.

**A unifying observation across (8) and (9):** one disposition — *take the construction's stated content at face value and do not override it with world knowledge* — fits both. It is **correct** for the CC conflicting-cue (the construction explicitly asserts the covariation, so following it is right) and **questionable** for the impossible caused-motion (following it ignores physical world knowledge); only an explicit in-premise denial flips the latter. The constructional signal is privileged over world knowledge in both — a property, not a competence-or-failure verdict.

**(10th, 2026-05-30) The CC covariation reading mostly survives *operator* embedding — but model- and instrument-conditionally.** [`result/comparative-correlative-covariation-v3`](../results/comparative-correlative-covariation-v3.md) placed the identical `the more X, the more Y` under an *in-sentence* operator that cancels or suspends its assertion — sentential **negation** ("it is not the case that…") and **epistemic hedging** ("it remains unproven whether…"). This is a sharper `functional-vs-formal` test than the v2 conflicting-cue arm: the cancelling operator is compositional, not extra-linguistic world knowledge. **claude-sonnet-4.6 and gemini-3.5-flash track the operator scope at/near ceiling** (they withhold the covariation direction under negation/hedging; gemini 100% on every arm/instrument), so the v1/v2 robustness is **not** a bare "the-more…the-more → INCREASE" template — it survives an operator that cancels the assertion, and a `baseline-inv` arm (100% everywhere) confirms genuine direction-tracking rather than INCREASE-bias. **But gpt-5.4-mini cracks under forced-choice specifically, via an excluded-middle *over*-inference** (not template-firing): on negated-inverse CCs it answers INCREASE (treats ¬decrease as entailing increase, FC negation-inv 0%), flips one negation to DECREASE, and reads one epistemic hedge as asserted; its NLI is far stronger. This both **strengthens** the CC-as-most-robust-positive reading (2/3 models track operator scope perfectly) and gives [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md) its sharpest datum yet: gpt-5.4-mini's instrument-fragility is now localized to a *specific logical error* under negation, not just a rate gap. It also mirror-images (8): there the panel **under**-computed (affirmed an impossible coercion); here the failing model **over**-computes (infers a direction the operator leaves open). Internal-contrast-only (no human norm on negated/hedged CC items).

**(11th, 2026-05-30) The caused-motion ceiling is genuinely construction-keyed — and instrument sensitivity has a *second*, non-model-specific source.** [`result/caused-motion-near-miss-v2c`](../results/caused-motion-near-miss-v2c.md) ran the near-miss form control the coercion v2 deferred: holding verb + object + displacement outcome constant and varying only the **form** between the caused-motion construction and two near-miss frames (coordinated *and* / temporal sequence) that report the same content without construction-licensing the causation. All three models affirm the causation at **100% for the construction** but **withhold** it for the near-miss frames — a **62.5–100 pp gap under forced-choice** (gemini a clean 100%→0%). So v1's at-ceiling caused-motion affirmation is **construction-driven, not a loose "displacement happened → the verb caused it" heuristic** — tightening the v1 floor and reinforcing the "add direction is easy *and* genuinely constructional" reading. The gap is **smaller under NLI** because NLI is more permissive of the **Gricean** post-hoc causal reading (the *and*-frame is affirmed as causation-entailing more often than under entailment-strict FC; the temporal-sequence frame is the cleaner withhold). Crucially this NLI-vs-FC effect is **uniform across all three models** — unlike the conative / CC-v3 cracks, which were gpt-5.4-mini-specific. So the project now has **two** distinct sources of instrument fragility: a *model-specific* one (gpt-5.4-mini's logical slips) and a *general pragmatics/entailment* one (NLI admits a pragmatic inference that FC's strict-entailment framing withholds). Internal-contrast-only (the near-miss "withhold" is the strict-entailment reading; the headline is the within-scene gap).

Cautions that still bind: (i) all eleven results are single panel/date/run with small N — direction-of-effect, not magnitude; (ii) the CC robustness is shown under conflicting-cue + composition + operator embedding, but the instrument is still modest, and the cracks (gpt-5.4-mini's FC over-inference under negation, v3) are now characterized rather than dismissed; (iii) instrument fragility now has **two** identified sources (model-specific + the general pragmatics/entailment NLI-vs-FC effect, v2c), which conditions every single-instrument Tier-4 reading; (iv) the eleven results are all `model-internal`; the relational ladder now has its **first finding** (a bounded null, [`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md)), and grounding stands at two negatives. The two prior cautions that are now **retired**: the add-direction ceilings are cue-sensitive for *both* an explicit cue (v2) *and* — for gpt-5.4-mini — partial world-knowledge engagement (v2b), with the world-knowledge bound stated; and the **add/cancel asymmetry is no longer confounded with ceiling** (the matched cancel probe ran). The lexical-axis trigger this list once carried is now **discharged**: the lexical probe ran and its line is folded into the closing section below. The genuinely-open triggers that remain: this page should be rewritten again when the AANN logprob blocker is resolved (held — the live API exposes no usable surprisal path) and that probe runs, or when a relational *positive* earns a bottom rung of the second ladder (the pilot has now run as a first-class **null** — [`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md) — characterizing the floor, not climbing the ladder).

## The under-explored axis: relational meaning

> **This subsection is now a stub. The relational axis has its own dedicated synthesis page:
> [`theory/relational-meaning-in-llms`](relational-meaning-in-llms.md) (2026-06-29)** — the recursive
> theoretical object for the whole "second ladder" arc (the reference-game pilot, the coined-term
> reassignment line with its `latest-binding-wins` order-sensitivity *positive*, the perturbation
> v2–v4 text-position finding, the order-of-operations composition C-series, and the seven essays
> built around them). What follows is the original v1-era summary, kept for continuity; the dedicated
> page carries the current, fuller picture (a **thin-positive / floor-characterizing** arc, not the
> "one bounded negative" this paragraph first recorded).

Every rung above is a `model-internal` probe — it asks what a single model knows. The charter's distinctive axis, [`concept/relational-meaning`](../../base/concepts/relational-meaning.md) (meaning constituted *between* agents, not computed within one), is a *second ladder*. The standing IOU on it is **now partly paid: the relational pilot has run** ([`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md), 2026-05-31) — the project's first relational *finding*, a **first-class null**.

The pilot built the design [`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md) names: a two-AI iterated dyadic reference game, homogeneous dyads, whose load-bearing contrast is **trajectory-dependence** (does a fresh matcher's interpretation of an opaque coined term depend on the *ordered* history when the *content* is held identical and only the *order* is destroyed?). The result, uniform across all three panel families: **convergence without trajectory-dependence.** The history's *content* is load-bearing (it lifts a fresh matcher's accuracy well above the coined term alone), but its *order* is not (chronological ≈ shuffled ≈ reversed; no order-gap CI excludes 0). The coined convention is recovered from the *set* of prior turns, not their ordered trajectory — coordination, not constitution. This is the relational analogue of Open Tension 1: the deflationary `distributional` story (next-token predictors converging from co-occurrence content, a convergence that *survives* order-scrambling) holds. So the second ladder now has its first finding, but it is a characterization of the **floor**, not a positive bottom rung: the pilot shows what relational convergence looks like *without* the order-sensitivity that would mark constitution. (A second, Hawkins-anchored observation from the same run: the LLM dyads converge on referential *success* but, unlike humans, do **not compress** their referring expressions — convergence without entrainment.)

The null is bounded — pilot scale (n≈12 coined terms/model), and a sharper trajectory test (the deferred **history-perturbation arm**, plus image referents and cross-family dyads) could still expose an order effect this design is under-powered to detect ([`decisions/resolved/relational-pilot-operationalization`](../../decisions/resolved/relational-pilot-operationalization.md)). But the rhetoric is now a result: until a relational *positive* is earned, claims on this page remain scoped to single-model constructional meaning, and the relational axis stands at **one bounded negative**.

## Open tensions

1. **Distributional null vs. constructional signal.** Tiers 1–3 must be read against the distributional null. A Tier-2 evaluative-adjective effect is only evidence for meaning *if* unigram frequency is controlled; otherwise it collapses back to Tier 1. `function-word-substitutability` makes this explicit: a null there "is a positive result for the distributional position, not a failure." The theory must not silently treat a distributional pass as a constructional pass.
2. **Inferential evidence vs. grounding.** Piantadosi & Hill would count Tier-4 inference-licensing as genuine meaning; Bender & Koller would say it is still form, because communicative intent is absent from the signal. This theory does not adjudicate. It records that Tier 4 is the ceiling of *text-internal* evidence and that the grounding question lies beyond it — a boundary, not a verdict.
3. **Memorization at every tier.** Weissweiler's confound is not retired by any single tier; it is *managed* by Tier 3 (held-out generalization). A Tier-4 result without a held-out check is interpretable as stored inference, not schematic inference.
4. **Formal/functional is a frame, not a measurement.** Mahowald's distinction sorts evidence; it does not itself measure constructional meaning. The ladder is the measurement instrument; the formal/functional cut tells us which rungs are "formal" (0–1) and which begin to be "functional/meaning" (2–4).

## What the theory predicts and forbids

**Predicts.** If LLMs have constructional meaning in the project's sense, then for a well-described construction we should observe a *coherent climb*: not just Tier-0 acceptability, but Tier-2 gradient tracking that survives frequency control, Tier-3 generalization to held-out items, and — for inference-bearing constructions like *way* — Tier-4 inference-licensing that the lexical items cannot explain. The tiers should rise together; a model with genuine constructional competence should not be strong at Tier 4 while failing Tier 2 on the same construction. This is a per-construction prediction, and the function-word swap result ([`result/function-word-swap-run-v2`](../results/function-word-swap-run-v2.md)) sharpens *why* it must stay per-construction: the Tier-4 signal is **type-specific** — robust for the subordinator and the existential→universal quantifier, near-null for the future→conditional modal, panel-split for the paucal→multal quantifier — so a *part-of-speech class* like "function word" is the wrong unit to predict over, and a pooled magnitude across a class is not a model-capability measure.

**Forbids.** The theory forbids three inferences:
- From Tier 0 to constructional meaning (the `formal-competence-aann-ceiling` block, generalized).
- From a frequency-uncontrolled gradient (Tier 1 dressed as Tier 2) to semantic tracking.
- From any text-internal tier (0–4) to grounded communicative meaning in Bender & Koller's sense, absent a separate grounding argument.

It also forbids promoting a contingent conjecture's eventual result to settled language while its `contingent-on` decisions are open — the AANN line was the live instance until 2026-06-12, when its instrument decision was ratified, the v2 design frozen, and the probe run under it (an example of the discipline running end-to-end: surface → cross-session ratify → freeze → run).

## Theoretical situating

The ladder is an *evidential* instrument; where its rungs sit on the **philosophical** map of meaning is treated separately, on [`theory/situating-llm-meaning`](situating-llm-meaning.md). In brief: the inference-licensing top rung is a *use/inferential* test, not a truth-conditional one ([`concept/truth-conditional-and-use-meaning`](../../base/concepts/truth-conditional-and-use-meaning.md)); the comparative correlative's multi-step composition is the project's cleanest evidence for genuine **compositionality** at the construction grain ([`concept/compositionality`](../../base/concepts/compositionality.md)), where coercion shows the relevant "parts" include constructions, not only lexemes; and the recurring **add/cancel asymmetry** the results above carry is abstracted into the project's own [`conjecture/constructional-monotonicity-asymmetry`](../conjectures/constructional-monotonicity-asymmetry.md) (additive-easy, defeasance-hard — a distributional-prior-compatible signature). The inferential reading these rungs invite is the *thin*, NLI-style one, explicitly **not** Brandom's normative inferentialism ([`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)) — and is itself instrument-fragile, which is why a single-instrument Tier-4 pass is read cautiously.

## Status and revision hook

`status: draft`. This page is `contingent-on: []` *directly* — it introduces no new empirical claim of its own and depends on no open decision in its own right. It leans on findings that are themselves contingent: [`conjecture/aann-construction`](../conjectures/aann-construction.md) is contingent on `aann-stimulus-source` and `aann-operationalization`, and three conjectures have anchors still pending. It also now leans on [`claim/constructional-divergent-form-generalization-gap`](../claims/constructional-divergent-form-generalization-gap.md), which is itself `contingent-on: []` (it uses only the aggregate published result), so it does not import a new contingency — though its *per-construction* sharpenings remain gated by `caused-motion-anchor` / `conative-anchor` / `way-construction-anchor`, three decisions the newly-catalogued [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md) has been surfaced as a candidate anchor for (pending Tom). The prose above flags those dependencies as provisional rather than settled, per [`CLAUDE.md`](../../../CLAUDE.md) rule 5; this theory claims a *structure* (the ladder, the placements) plus one externally-grounded negative data point at the Tier 3→4 boundary — and not yet any *result* of the project's own.

**The lexical axis is now live, and joined to this one.** The project has since run the lexical wedge extensively; its detailed synthesis is the sister page [`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md), which argues that this ladder (grammar) and the lexical findings are two grains of **one** form–meaning cline tested by **one** skeleton ("does a meaning gradient beat the distributional shadow?"). Only the parts that bear on *this* page's reading are noted here; depth lives there.

- The first lexical probe ([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md), 2026-05-30) found graded word-sense relatedness tracking the human DURel median and surviving a context-similarity control — the lexical-end positive that mirrors this page's "add direction is easy" observation at the word grain.
- The lexical *hard* direction — the conjecture's distinctive bet that homonymy is a discrete floor separable from polysemy — is **not established**: untestable at DWUG (only 3 clean homonyms; [`result/lexical-polysemy-homonymy-v2`](../results/lexical-polysemy-homonymy-v2.md)) and then a **powered null** on a homonymy-enriched WiC subset ([`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md), where the one floor signal cannot be told from plain graded distance). This is the lexical counterpart of the grammatical hard direction (divergent-form generalization), and like it, it stays off the easy ceiling.
- **Coercion is where the grains touch.** The bridge probe reuses the lexical instrument on constructional stimuli: [`result/coercion-sense-modulation-v1`](../results/coercion-sense-modulation-v1.md) found constructional coercion registers as a partial verb-sense shift in the relatedness instrument (direction held, all 3 models), and the structure-matched follow-up [`result/coercion-sense-modulation-v2`](../results/coercion-sense-modulation-v2.md) **partially de-confounds** it — a small, fine-scale-only, fragile sense-specific residual survives alongside a real surface component, so the contact is genuine but fainter than v1's raw gap implied. Both are internal-contrast-only.
- The **grounding** axis (orthogonal to this ladder) has been touched only by two nulls: a word's perceptual groundedness does not predict text-only sense-tracking ([`result/lexical-perceptual-grounding-moderation-v1`](../results/lexical-perceptual-grounding-moderation-v1.md)), and showing the depicting image does not improve sense separation for clear homonyms — a redundancy null, since text already separates them ([`result/multimodal-grounding-image-v1`](../results/multimodal-grounding-image-v1.md)). These bear on the grounding boundary this page brackets, not on any rung of the ladder.

This revision (2026-05-30) incorporates the project's **seventh through tenth own-design results**: the matched cancel-direction conative ([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md)), the implicit-world-knowledge caused-motion cue ([`result/coercion-implicit-cue-v2b`](../results/coercion-implicit-cue-v2b.md)), the off-ceiling CC v2 ([`result/comparative-correlative-covariation-v2`](../results/comparative-correlative-covariation-v2.md)), the embedded-CC operator-scope CC v3 ([`result/comparative-correlative-covariation-v3`](../results/comparative-correlative-covariation-v3.md)), and the caused-motion near-miss form control v2c ([`result/caused-motion-near-miss-v2c`](../results/caused-motion-near-miss-v2c.md)). The project now holds **eleven own-design results** spanning the upper ladder. The net change to the theory: the **add/cancel asymmetry is de-confounded from ceiling** (license easier than suppress, off ceiling), the **add-direction cue-sensitivity is bounded** to explicit-outcome parsing rather than world-model integration, and the **CC is the most robust constructional positive** (survives conflicting-cue + multi-step composition). The AANN placement still stands corrected (decisions ratified, probe logprob-blocked and unrun). A 2026-05-31 consistency pass folded the now-discharged lexical-probe trigger into the section above: the lexical wedge has run extensively (sense-gradience positive; polysemy/homonymy hard direction a powered null; the coercion bridge partially de-confounded; two grounding nulls), with its synthesis on [`theory/lexicon-grammar-continuum`](lexicon-grammar-continuum.md). Next revision triggers (genuinely open): resolution of the AANN logprob blocker and an AANN result; or a relational *positive* (the relational pilot has now run as a first-class **null** — [`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md) — so a v2 perturbation/image/cross-family arm earning a genuine trajectory effect would be the next relational trigger; [`open-question/relational-meaning-pilot`](../open-questions/relational-meaning-pilot.md)).
