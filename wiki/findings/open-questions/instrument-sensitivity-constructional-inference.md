---
type: open-question
id: instrument-sensitivity-constructional-inference
title: Does measured constructional-inference competence depend on the elicitation instrument (NLI vs forced-choice), and what does that imply for the evidence ladder?
meaning-senses:
  - constructional
  - inferential
  - functional-vs-formal
status: open
created: 2026-05-29
updated: 2026-07-05
links:
  - rel: depends-on
    target: result/conative-minimal-pair-divergence-v1
  - rel: depends-on
    target: result/way-construction-traversal-v1
  - rel: depends-on
    target: claim/cxg-probing-surprisal-validity
  - rel: depends-on
    target: result/comparative-correlative-covariation-v3
  - rel: depends-on
    target: result/caused-motion-near-miss-v2c
  - rel: depends-on
    target: result/instrument-disagreement-reanalysis-v1
  - rel: depends-on
    target: result/scivetti-cxnli-answer-key-v1
  - rel: depends-on
    target: result/scivetti-let-alone-working-surface-v1
  - rel: depends-on
    target: result/scivetti-let-alone-forced-decomposition-v1
---

# Open question: does constructional-inference competence depend on the elicitation instrument?

> **Update / what landed (2026-05-31) — two distinct sources of instrument sensitivity identified; its pervasiveness bounded; question stays open (standing methodological question).** Since this page was written, three own-design results have run that are exactly its subject matter, and they sharpen the picture from "gpt-5.4-mini diverges on the conative" into **two separable mechanisms plus a pervasiveness bound**:
>
> 1. **A model-specific logical slip.** [`result/comparative-correlative-covariation-v3`](../results/comparative-correlative-covariation-v3.md) embedded the comparative correlative under negation / epistemic hedging. claude and gemini track the operator scope at/near ceiling on both instruments; gpt-5.4-mini **cracks under forced-choice specifically**, but the mechanism is now precise: an **excluded-middle over-inference** under negation/forced-choice (treating ¬(X decreases) as entailing X increases), *not* a bare rate gap and not a surface template firing. The instrument-fragility is again confined to gpt-5.4-mini and localized to one logical error.
> 2. **A general pragmatics/entailment NLI-vs-FC effect.** [`result/caused-motion-near-miss-v2c`](../results/caused-motion-near-miss-v2c.md) found a **second, non-model-specific** source: the caused-motion causation inference is genuinely form-keyed (construction 100% affirm vs near-miss withheld), but the construction-vs-near-miss gap is **smaller under NLI than forced-choice uniformly across all three models** — NLI admits the Gricean post-hoc causal reading that forced-choice's strict-entailment framing withholds. This is a content-level instrument effect tracking the pragmatics/entailment boundary, distinct from the gpt-specific cracks.
> 3. **A pervasiveness bound.** [`result/instrument-disagreement-reanalysis-v1`](../results/instrument-disagreement-reanalysis-v1.md) (read-only, $0) turned the anecdote into a descriptive statistic across two existing runs: **large instrument disagreement (50.0 pp) is confined to the single gpt-5.4-mini × conative cell**; the other eight cells (claude/gemini × conative, all three models × both add-direction constructions in coercion-v2) show ≤20.8 pp, mostly ≤10 pp. So instrument fragility is **not pervasive** in this panel — though the add-direction cells' agreement is partly ceiling/floor compression, not demonstrated invariance (the re-analysis is descriptive, no significance test).
>
> Net: instrument sensitivity now has **two identified sources** — a model-specific logical-slip mechanism (gpt-5.4-mini's excluded-middle over-inference, FC-localized) and a general NLI-vs-FC pragmatics/entailment effect (NLI more permissive of Gricean inference, uniform across models) — and the re-analysis **bounds its pervasiveness** to one model × construction cell at the large end. The page **stays `open`**: it is a standing methodological question that conditions how every Tier-4 result is read, and the "serious answer" below (a dedicated cross-instrument × cross-construction design with a pre-registered primary instrument and an operationalization gate queued for Tom) has **not** been run — these three results motivate and partially characterize the question, they do not close it.
>
> **Update (2026-06-13, fifth session) — the AANN inferential v4 produces the *largest* FC-vs-NLI
> disagreement in the record, and it is *not* a ceiling artifact.**
> [`result/aann-inferential-v4`](../results/aann-inferential-v4.md) ran a forced-choice paraphrase
> arm and an entailment-NLI arm on the *same* frozen items (the AANN against a distributive-default
> control). The named |FC Δ² − NLI Δ²| statistic is flagged for **all three** models — **0.63 / 0.43
> / 1.04** — exceeding the prior 0.50 pp single-cell maximum, and now spread across *every* model
> rather than confined to one. The pattern: the exclusive forced-choice instrument registers the
> construction's unification shift cleanly in all three models (Δ² +0.78 / +0.70 / +0.96), while the
> permissive NLI entailment instrument registers it only in gpt-5.4-mini (+0.26; claude +0.15 not
> clearing, gemini −0.09). Crucially the NLI nulls are **off-ceiling** (both-hypothesis DDC affirm
> rates 0.48 / 0.57 / 0.63 — verified after a fixed aggregation bug; the earlier-looking "NLI
> ceiling" was the bug), so this is genuine instrument *divergence*, not compression: the forced
> exclusive choice is simply more sensitive to the construction than the "is it entailed?" judgment.
> This is the **third** datum-type for the page — distinct from the gpt-specific logical slip and the
> uniform Gricean-permissiveness effect: here FC and NLI disagree because **FC's exclusivity surfaces
> a construction effect that NLI's permissiveness dilutes**, and the disagreement is now *broad* (all
> three models) rather than confined. The page stays **`open`**, with this as its sharpest and most
> general FC-vs-NLI datum yet.
>
> **Pointer (2026-06-20, session 52) — a sibling texture of panel heterogeneity, named as a reading
> discipline.** [`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md)
> uses this page's across-instrument *convergence heterogeneity* (the AANN PARTIAL: all models shift on
> FC, only one carries it across instruments) as the contrast case to a *different* texture — *magnitude*
> decorrelation **on a single instrument**, where all three models CONFIRM on the same forced choice but
> the effect size spans ~10× ([`result/dative-information-structure-v1`](../results/dative-information-structure-v1.md)).
> Both are ways a single panel-level label (CONFIRM / PARTIAL) flattens real per-model heterogeneity; this
> page's mechanism (on-which-instruments) and the essay's (how-much-on-one-instrument) are distinct but
> share the moral.
>
> **Update (2026-06-20, session 59) — a *fourth* instrument-sensitivity mechanism: the output channel
> (forced single token vs working surface), distinct from the FC-vs-NLI *input* axis this page has tracked.**
> Sessions 57→58 add a datum the page's three prior mechanisms (gpt's FC-localized logical slip; the uniform
> Gricean NLI-permissiveness effect; FC-exclusivity surfacing an effect NLI dilutes) do not cover, because it
> lives at the *output* end of the instrument rather than in the NLI-vs-FC framing of the *input*. The
> Scivetti answer-key probe ([`result/scivetti-cxnli-answer-key-v1`](../results/scivetti-cxnli-answer-key-v1.md))
> found the phrasal-scalar **let-alone** construction at near-chance for all three models under a **forced
> single-token** NLI channel (the prompt required a single digit and nothing else), while the eight argument-structure
> constructions sat at/near the ≈0.90 human native-speaker baseline. The format-only follow-up
> ([`result/scivetti-let-alone-working-surface-v1`](../results/scivetti-let-alone-working-surface-v1.md))
> re-ran the *same* let-alone items under a **working surface** (step-by-step permitted, a `FINAL:` tag
> parsed; everything else byte-identical, reasoning-effort held constant) and **two of three models lifted to
> the human baseline** (claude 0.542→0.792, gemini 0.667→0.917; within-item sign test p = 0.035; a
> comparative-correlative ceiling control preserved). So a Tier-4 inference that read as near-chance was
> largely **channel-bounded**, not competence-absent — the elicitation dependence here is along the *output
> channel*, the response-format dimension, not the FC-vs-NLI *input instrument* this page's first three
> mechanisms concern. This is the same caution the page exists to register (a single-instrument result can
> mis-state competence), now extended to the response-format dimension; the dedicated methodological treatment
> — the confound, its scope condition, and the control it forces — lives in
> [`essay/output-channel-confound`](../essays/output-channel-confound.md). One honesty note carried from that
> result, parallel to this page's recurring gpt-5.4-mini story: the third model did **not** lift, but largely
> **declined** the offered surface (16/24 bare one-token answers, 0 reasoning tokens), so its persistence is
> *channel-not-taken-up*, not a demonstrated channel-controlled failure — the output-channel axis, like the
> FC-vs-NLI axis, shows **model-graded** sensitivity (and again it is gpt-5.4-mini at the fragile end). The
> page **stays `open`**: the output channel joins NLI-vs-FC as a dimension along which "constructional-inference
> competence" can prove elicitation-dependent, and the standing methodological question is unchanged.
>
> **Update (2026-06-20, session 60) — the output-channel sensitivity is *graded within* a single model, not
> all-or-none.** [`result/scivetti-let-alone-forced-decomposition-v1`](../results/scivetti-let-alone-forced-decomposition-v1.md)
> closed the session-58 honesty note's gap by **forcing** gpt to use the channel (a mandatory 3-step
> decomposition; gpt's median let-alone completion jumped 8 → 120 tokens, 24/24 worked). The result refines the
> model-graded picture: forcing uptake **partly** closes gpt's let-alone gap (+0.21, directional but
> underpowered, within-item sign test p = 0.090 → UNCHANGED) yet leaves it **below** the human ≈0.90 baseline
> (0.583), where claude (0.833) and gemini (0.875) sit. So the output channel's effect on measured
> constructional-inference competence is not binary (artifact vs real) even within the fragile model: part of
> gpt's let-alone gap is channel-bounded (uptake helps) and part **survives a genuinely-exercised channel**.
> This is the same lesson the page registers for the FC-vs-NLI axis — that "competence" reads off the
> instrument in graded, model-specific ways — now sharpened on the output-channel axis to a *partial* effect.
> The page **stays `open`**.

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The output-channel mechanism the two
> boxes above track (sessions 59–60) has since been consolidated into a promoted claim:
> [`claim/output-channel-working-surface`](../claims/output-channel-working-surface.md) (session 177,
> cross-session adversarial promotion review) — a forced single-token channel can mask a
> serial-inference capability, with the format-only flip replicated across **two task families**
> (relational order-composition; let-alone scalar-construction NLI) and **three geometry axes**
> (operation pair / alt-pair, grid size K=6, composition depth / three-move), and a **boundary
> control** carried (the bridging-context commitment null survives the identical channel control, so
> the effect is computation-specific, not universal).
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

## The question

When we probe whether an LLM tracks a construction's characteristic inference, the measured competence can depend on *how we ask*. A binary or 3-way NLI entailment judgment ("does sentence A entail sentence B?") and a forced-choice elicitation ("based only on the sentence, did the event complete? YES / NO / CANT_TELL") are both ratified operationalizations in this project, running in parallel on the same frozen items — yet they can return materially different answers for the same model on the same construction.

The question: **is "constructional-inference competence" a stable property of the model, or is it partly an artifact of the elicitation instrument?** If two instruments disagree for the same model on the same items, which (if either) is the truer measure — and what does instrument-disagreement itself tell us about the nature of the competence being measured?

This is a `functional-vs-formal` question: the `constructional` / `inferential` reading of a construction's meaning is not a form judgment, and it is exactly at the functional end of the Mahowald et al. 2024 formal/functional distinction that instrument-sensitivity should hurt most. If a model's inference-licensing competence only surfaces under one elicitation frame, the "competence" may be less stable — more elicitation-dependent — than a single positive result suggests.

## The motivating in-repo evidence

Two own-design result pages share a joint operationalization and motivate this question. Both ran the same panel (claude-sonnet-4.6, gpt-5.4-mini, gemini-3.5-flash), both used the ratified divergence operationalization — the same frozen pre-run design with both instruments simultaneously — so the instrument disagreement is *within a single frozen design*, not a confound across different experiments. That strengthens the observation: any instrument gap cannot be explained by differences in stimuli, models, or temperature.

### From [`result/conative-minimal-pair-divergence-v1`](../results/conative-minimal-pair-divergence-v1.md): a stark case

The conative probe ran verb-held-constant minimal pairs (*Maria kicked the ball* vs. *Maria kicked at the ball*) probing whether the *at*-frame cancels the completed-contact entailment. The panel-wide finding was positive — forced-choice gaps of **42–88 pp across all 3 models**; NLI gaps of **54–67 pp for 2 of 3** — but the discriminating wrinkle was gpt-5.4-mini's cross-instrument divergence:

- **gpt-5.4-mini under NLI**: gap **−8 pp** — the model called all 24 conative items "entailment" (0/12 verbs with a positive gap), treating *kicked at the ball* as entailing made contact with the ball. The core prediction fails entirely.
- **gpt-5.4-mini under forced-choice**: gap **+42 pp** (7/12 verbs at or above the 30 pp bar). The same model, same items, same run — the conative non-completion inference partly surfaces.

As the result page states in its one-line finding: "the conative non-completion inference is **latent but instrument-fragile** in gpt-5.4-mini: the forced-choice 'based only on the sentence' framing surfaces it; the NLI entailment framing collapses it to a default 'yes, contact.'" Claude and gemini are stable across both instruments (NLI/FC gaps within 13 pp of each other). So the divergence is model-specific and instrument-specific, not a global artifact.

### From [`result/way-construction-traversal-v1`](../results/way-construction-traversal-v1.md): a milder case

The way-construction probe ran non-motion verbs in the construction (*Mia whistled her way down the hall*) against a location control (*Mia whistled in the hall*) to test whether models draw the path-traversal entailment from the construction. Here the panel-wide finding was strongly positive — way rates of **77.8–100%**, gaps of **77.7–100 pp** over the location control, in 3/3 models on both instruments — but gpt-5.4-mini was again the conservative outlier. Its only non-affirms (4–5 items: *hum*, *eat*, *chat*, and under forced-choice *snack*) were read as "may or may not have moved" / CANT_TELL rather than outright wrong, and the result page notes that for *eat/chat/snack* a metaphorical-progress alternative is genuinely available, making CANT_TELL cautious-not-wrong. The divergence here is mild and does not undercut the confirm bar.

The way result illustrates a different elicitation-sensitivity flavor: not instrument-collapse (gpt does not reverse the inference the way it does under conative-NLI) but **conservatism** — a more stringent entailment bar that declines to commit where the inference is less than certain. As the result page states, "the unifying point is not a tidy verb-class effect but that gpt applies a **more conservative entailment bar**."

Together, the two results define a range: at one end, instrument-collapse (conative-NLI: competence effectively absent); at the other, instrument-conservatism (way: competence present but hedged on ambiguous items). Both are forms of elicitation-sensitivity, but with different implications.

## Why it matters

### (a) Single-instrument results can mis-state competence

A project using only NLI would conclude gpt-5.4-mini **lacks** the conative non-completion inference; a project using only forced-choice would conclude it **has** it (partially). Both conclusions are instrument-relative. This is a caution against trusting any one probe — a point [`claim/cxg-probing-surprisal-validity`](../claims/cxg-probing-surprisal-validity.md) already registers at the method level: the surprisal/minimal-pair operationalization is "valid but bounded," and the bounds include the instrument's framing. The present observation extends that caution explicitly to NLI and forced-choice as operationalizations at the `inferential` tier.

### (b) The evidence ladder's "tiers should rise together" prediction is complicated

The theory page ([`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)) states: "The tiers should rise together; a model with genuine constructional competence should not be strong at Tier 4 while failing Tier 2 on the same construction." Instrument-dependence complicates this prediction: **competence can be present yet elicitation-dependent**. The theory page flags the conative result as surfacing "instrument-fragility as a first-class variable" — but that flag currently lives as scattered prose, not a typed question. This page makes it a citable open question with a typed home.

The complication is not that the ladder prediction is wrong, but that it may need an instrument-stability clause: "the tiers should rise together, *and the competence at each tier should be instrument-stable*." A Tier-4 positive under one instrument and a Tier-4 negative under another, on the same frozen items, is not yet a ladder result — it is a ladder-plus-instrument interaction result.

### (c) It bears on the formal-vs-functional cut

One interpretation of instrument-sensitivity is that it marks shallow or `functional-vs-formal` fragility: a model whose "competence" only surfaces under a specific framing may be tracking surface patterns in that frame rather than a stable inferential commitment. A more charitable reading is that elicitation is genuinely noisy — different frames emphasize different aspects of the judgment — and instrument-sensitivity is not a sign of shallow competence but of imprecise measurement. Discriminating between these interpretations is part of what a serious answer would look like.

## What a serious answer would look like

A design that treats **per-model instrument-disagreement** as the dependent variable rather than a nuisance. The key features:

1. **Cross-instrument × cross-construction matrix.** Run NLI × forced-choice (× possibly a third instrument, e.g. cloze/continuation) on the *same* frozen items across the *same* panel, measuring instrument-disagreement score per model per construction — not just reporting gaps as a by-product of a conjecture test.
2. **Pre-register which instrument is primary.** Fix this before seeing results — it is an operationalization gate (charter §8 and the project's `constructional-divergence-operationalization` precedent). Choosing the "winning" instrument post-hoc would re-import the confound the question is about. Any new operationalization gate would be queued as a decision — since 2026-06-12, ratified by autonomous cross-session review; [`PROJECT.md`](../../../PROJECT.md) §12.3.
3. **Check concentration.** Is instrument-disagreement concentrated in particular *models* (gpt-5.4-mini in both results so far) or particular *constructions* (cancel-direction / conative so far)? The cancel-direction constructions (conative, where the construction must suppress a lexically-default entailment) appear harder and more instrument-sensitive than add-direction constructions (caused-motion, way, comparative-correlative — all near ceiling on both instruments). Whether this is a cancel/add structural asymmetry or a difficulty-level confound is the first hypothesis to check.
4. **Check whether instrument-disagreement is itself systematic.** If NLI consistently under-states competence relative to forced-choice for certain model × construction combinations, that is a finding about the NLI framing's default-entailment pull (the conative collapse looks like NLI pulling toward a "yes" default when the verb's typical reading is completion). If the direction of disagreement varies, a framing-noise story is more plausible than a systematic bias story.

Note: this design is tractable with existing frozen stimuli and the existing panel. The conative and argument-structure-coercion harnesses already run both instruments and could be re-analyzed for instrument-disagreement as a summary statistic before any new run.

## Relation to the existing wedge

This question is **methodological / cross-cutting**: it conditions how every Tier-4 (inference-licensing) result on the evidence ladder should be read. It is not a question about what construction is being tracked or whether the distributional null explains the result — those are the objects of the `constructional-vs-frequency-confound` and `distributional-vs-inferential-constructional` open questions. This question is about whether the *measurement* of the result is stable.

It is `model-internal` (the instrument-sensitivity is observed within individual models' behavioral outputs) and does not touch the relational axis. It is `functional-vs-formal` in the sense that the instrument-sensitivity appears precisely at the `inferential` / functional end of the ladder — Tier-4 inference-licensing — not at Tier-0 form-acceptability, where NLI and forced-choice are unlikely to diverge on whether a string is well-formed.

It is distinct from the lexical open questions (`distributional` shadow, graded polysemy) — those ask what the model is tracking; this asks whether what the model tracks can be reliably read off a single elicitation.

## Why queued, not active; pointers for next visit

The question is tractable with existing resources (both instruments already run on conative + way + coercion-v2; the panel is fixed; the stimuli are frozen), but it needs a dedicated instrument-crossing design written and an operationalization gate queued before any new run. Without that gate, any re-analysis risks post-hoc instrument selection.

The current evidence base (two own-design probes, one stark cross-instrument divergence, one mild one) is enough to motivate the question and suggest the add/cancel asymmetry hypothesis — but not to answer it. Two results, both pointing to gpt-5.4-mini, are not yet a general finding about instrument-sensitivity.

**Pointers for the next visit:**

- The conative and coercion-v2 harnesses already run both instruments; a re-analysis summarizing per-model, per-construction instrument-disagreement as a named statistic (e.g. |NLI gap − FC gap|) could be done as a read-only pass before any new stimuli are generated.
- The most informative new probe would be a **harder** cancel-direction construction paired with a matched add-direction construction, run on both instruments simultaneously, with the primary instrument pre-registered. The add/cancel asymmetry hypothesis (cancel-direction is harder *and* more instrument-fragile) is the first thing to test.
- Any new operationalization gate for this question follows the same discipline as `constructional-divergence-operationalization`: write and freeze the design; queue the primary-instrument choice for Tom before running; do not self-resolve.
- This question does not block any current work — the existing result pages report both instruments in full, so instrument-disagreement is already in the record. The gap is that it has no typed home to spawn a dedicated loop turn.
