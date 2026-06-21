---
type: open-question
id: lexical-bridging-context-gradience
title: "Do bridging (sense-ambiguous) contexts elicit intermediate, lower-confidence same/different-sense behavior — the within-item fingerprint of graded sense?"
meaning-senses:
  - distributional
  - referential
status: open
contingent-on: []
created: 2026-06-21
updated: 2026-06-21
links:
  - rel: refines
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/referential-meaning
---

# Open question: do bridging contexts elicit intermediate, lower-confidence sense behavior?

> **Why this page exists.** The lexical axis has gone quiet — the last six sessions worked the function-word / modal line, and the lexical wedge has stood still since the v1–v3 sense-gradience results. This page re-opens the lexical axis on the **one untested clause** of an otherwise-`tested` conjecture, and scopes it as the next tractable, non-modal empirical unit. It is a **scoping** page: it surfaces the question and its two gates (operationalization, human anchor); it does **not** pre-commit a design or an anchor. Those are for a later session, and the anchor question is a future `wiki/decisions/open/` candidate (named below, not yet created).

## The question, sharply

[`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md) is `status: tested`, but unevenly: its central monotonicity bet (clauses a + c) is **supported** by [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md), and its distinctive discreteness bet (clause b) is a **powered null** at the WiC anchor ([`result/lexical-polysemy-homonymy-v3`](../results/lexical-polysemy-homonymy-v3.md)). One of its five predictions has never been run. Prediction 4, verbatim from the conjecture:

> "Deliberately sense-ambiguous (bridging) contexts, engineered so two senses are co-present, yield **intermediate, less-confident** model behavior rather than a forced discrete pick — the behavioral fingerprint of gradience."

The question this page opens:

> On a target word presented in a **bridging** context — a use engineered (or attested) so that two senses are genuinely co-present, leaving the sense indeterminate — does a panel model's same-sense / different-sense behavior land in an **intermediate, lower-confidence** regime, *between* its behavior on clearly-same and clearly-different uses, rather than collapsing to a forced discrete pick? Is *within-item indeterminacy* — uncertainty on the item that is itself ambiguous — visible in the model's behavior, as the lexicographer's gradience picture predicts it should be?

The conceptual object is [`concept/polysemy`](../../base/concepts/polysemy.md): on its account "the senses of a polysemous word … shade into one another, with bridging contexts where two senses are co-present and judgements are genuinely intermediate" and "these bridging contexts are not anomalies to be disambiguated away; they are the evidence that sense distinctions are scalar, not binary." That concept page also fixes the *use-pole* framing — sense is `referential.sense` (Frege's `Sinn`, mode of presentation) at fine grain, and the bridging context is exactly where one surface form leaves two modes of presentation co-present. Prediction 4 asks whether a model's behavior carries that scalar, indeterminate signal at the level of the *single ambiguous use*, not just across a set of clearer uses.

## Why it is the right next unit

Three reasons, in order of force:

1. **It diversifies off the function-word / modal line.** Six consecutive sessions have worked the grammatical/modal axis; the lexical axis — the project's other charter-named focus, "lexical *and* grammatical meaning" ([`PROJECT.md`](../../../PROJECT.md) §1) — has been dormant since the v1–v3 lexical results. This is a concrete, non-modal lexical unit a future session can pick up.
2. **It is the one untested clause of a `tested` conjecture.** Clauses (a) + (c) are settled (supported); clause (b) is settled as a powered null (not falsified, but adequately probed and diagnosed). Prediction 4 (bridging contexts) is, as far as the result pages show, simply **never run** — neither v1 (monotonicity + context control) nor v2/v3 (the polysemy-vs-homonymy discreteness arm) touched it. Closing it would complete the conjecture's evidential picture rather than re-litigate a settled clause.
3. **It probes gradience from a genuinely different direction than v1.** v1 measured gradience as a **cross-item monotonic correlation**: do the model's ratings, *across* many usage pairs, rank-order the way the human DURel median does (Spearman 0.60–0.83). That establishes the model has a graded *scale*. It does **not** establish that the model is *uncertain on the items that are themselves ambiguous*. Prediction 4's signature is **within-item uncertainty** — intermediate, low-confidence behavior on a single bridging use — which a strong cross-item correlation is silent about. A model could rank-order pairs perfectly yet still force every individual ambiguous item to a confident discrete pick; that would be a graded *scale* without graded *commitment*, and only a bridging-context probe can tell the two apart. This is a different empirical claim, not a re-run of v1.

## What a serious answer would look like

A design that contrasts three item classes for the **same** target word: **clearly-same** sense uses, **clearly-different** sense uses, and **bridging** uses (two senses co-present / a vague-or-ambiguous use). The prediction is ordinal on *two* axes: the bridging class should sit at an **intermediate** position on the model's same/different signal **and** carry **lower confidence / higher dispersion** than either clear class. The null is first-class and must be declared up front: bridging items are handled with the same confidence as clear items — a forced discrete pick — which would be a *within-item* discreteness signal (graded scale, ungraded commitment) and a clean negative for prediction 4. (Note the relation to clause b: v3 found no *separate discrete regime* across the homonymy/polysemy contrast; a within-item discreteness result here would be a different, complementary kind of discreteness evidence — at the level of single-item commitment rather than between-stratum separability.)

## The operationalization gate (surfaced, not resolved)

"Intermediate, less-confident" is not one measurement; it is a family, and the instruments can disagree. This is an operationalization choice to be **frozen before any result is seen** (charter §8 — the same instrument-before-results discipline the conjecture's own *Notes* and the v1/v3 designs imposed). Candidate instruments:

- **Spread / entropy of a forced same/different judgment** across paraphrases or repeated samples — the model is forced to pick, and the *dispersion* of its picks across re-promptings or paraphrase variants is the intermediacy signal. (Operationally close to v1's panel, run for variance rather than mean.)
- **An explicit graded-confidence elicitation** — ask for the same/different call *and* a confidence (or a 0–100 relatedness rating), and read the confidence/rating as the within-item signal. (Closest to v1's `durel`/`cont` framings, repurposed per-item.)
- **A "both senses / unclear" response option** — give the model an explicit third option and ask whether it takes it on bridging items more than on clear items. (A categorical instrument; behaves differently from the two continuous ones, and is sensitive to how willing the model is to decline a binary.)

These three instruments measure related but non-identical things and **may disagree** (the conjecture's *Notes* already flag instrument choice as a gate, and v1 documented exactly such an instrument-sensitivity pattern — gpt-5.4-mini read differently under the ordinal vs. continuous framings, [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md), [`open-question/instrument-sensitivity-constructional-inference`](instrument-sensitivity-constructional-inference.md)). The named failure mode: **tuning the instrument until intermediacy appears** — trying instruments or thresholds until one shows the predicted intermediate band. The gate must pick one instrument (or pre-register a small fixed panel of them with the reading rule) and freeze it, reporting whatever each shows including disagreement, rather than selecting post hoc. This is a future `wiki/decisions/open/` candidate (`lexical-bridging-context-operationalization`, not yet created), to be opened and — per the cross-session rule — ratified by a *later* session.

## The human-anchor question (surfaced honestly)

This is the load-bearing difficulty, and it must not be waved away. "The model is less confident on these items" is **uninterpretable** unless the bridging items are *certified* as genuinely bridging by some human-grounded signal independent of the model. Otherwise an apparent low-confidence band is unfalsifiable — any items the model happens to be unsure about could be relabelled "bridging" after the fact. The candidate human-grounded sources of a bridging stratum, with what each in-repo resource page actually affords (cited by the feature that bears, per the charter's verify-content rule):

- **DWUG high-disagreement / mid-scale pairs.** [`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md) carries graded, multi-rater 4-point DURel proximity judgments over usage pairs of the same target word; its page records (verbatim from the primary paper) that annotators "make frequent use of the intermediate levels of the scale ('2','3') and thus assign graded distinctions of word meaning." A bridging stratum could be the **mid-scale** pairs (DURel 2–3) or pairs with **high annotator disagreement** — usages humans themselves split on. *Caveat the resource page already forces:* DWUG EN human–human agreement is ρ ≈ 0.69, and the v1 result flagged that "151/200 pairs rest on only 2 annotators (the half-integer levels are 2-rater disagreements)" and "the half-integer levels are not treated as reliable graded gold." So DWUG's disagreement signal is real but thin per item — using it to certify bridging needs care, and the multi-rater requirement (≥3 raters) shrinks the usable pool. DWUG also "does not tag pairs as polysemy vs. homonymy" (resource page), so a bridging item drawn from DWUG is a *usage-similarity* mid-point, not a certified *within-sense bridge*.
- **WiC items near the decision boundary.** [`resource/wic-word-in-context`](../../base/resources/wic-word-in-context.md) carries **binary** lexicographer-inventory same/different labels — and its page is explicit that it "is **binary by design**" and "cannot ground 'the model's signal is *monotonic* in human-rated relatedness.'" There is **no per-item human graded or confidence axis** in WiC: the gold is the expert sense split, not a rating panel, so WiC has no native "near-boundary" annotation. Worse for this use, its construction "removed all pairs whose senses were first degree connections … sister senses … same supersense" (resource page, verbatim) — i.e. it **pruned the closest polyseme pairs**, exactly the near-bridge middle a bridging study most wants. WiC could supply *clearly-same* and *clearly-different* anchor items cleanly, but it does **not** out-of-the-box certify a bridging stratum; any "near-boundary" WiC subset would have to be defined by an *added* signal, not read off WiC's labels.
- **A fresh, engineered bridging construction — no human anchor.** Authoring deliberately ambiguous sentences (the "I read the paper" style bridge of [`concept/polysemy`](../../base/concepts/polysemy.md)) gives full control over co-presence but carries **no human grounding** for which items are genuinely bridging. Such a probe would be a **within-model contrast only** and, if promoted, would need the ratified `anchor: internal-contrast-only` terminal declaration (per [`CLAUDE.md`](../../../CLAUDE.md) anchor discipline) — a within-model claim, never a human-comparison one. It must not be used to dodge the anchor obligation; it is a *different, weaker* claim, and should be labelled as such.

**Provisional default (not a decision):** the cleanest human-grounded route is a **DWUG-derived bridging stratum** — mid-scale (DURel 2–3) and/or high-disagreement multi-rater pairs as the bridging class, with high-agreement DURel-4 and DURel-1 pairs as the clear-same / clear-different anchors — because DWUG is the one in-repo resource with a *graded, multi-rater, per-pair* human signal that can certify "humans themselves found this intermediate." The competing route (an engineered construction) is more controllable but `internal-contrast-only`, a strictly weaker claim. This choice is **not made here**; it is laid out for a future `wiki/decisions/open/` entry (`lexical-bridging-context-anchor`, not yet created), to be ratified cross-session. No anchor is invented; the default names only what the existing resource pages already say they afford.

## Scope and limits

- **Small N is intrinsic.** Graded / bridging sense sets are modest (v1 ran 200 DWUG pairs over 43 lemmas; a certified-bridging subset would be smaller still). This is a **gradience-signal probe of within-item uncertainty, not a coverage benchmark** — direction-of-effect, wide per-lemma uncertainty, no claim beyond the lemmas/register/framing probed. The same caveat the v1 and v3 result pages lead with applies here.
- **Sense relatedness vs. usage similarity stay labelled distinctly.** The conjecture's standing caveat — "the graded set measures usage similarity; the lexicographic gradience claim is about sense relatedness — keep the two labelled distinctly" — binds any result here. A DWUG mid-scale pair is a *usage-similarity* mid-point; calling it a *sense bridge* is the slide this page must not make silently.
- **Behavioral, not representational.** Like v1–v3, any near-term probe is behavioral (panel same/different + confidence). It would be evidence about the model's *behavior* on ambiguous items, **not** about graded sense *representations* (the small-model representation lane stays deferred on local compute, per the v1/v3 caveats). Do not over-read a behavioral intermediacy result as a representational claim.
- **Within-item uncertainty ≠ between-stratum discreteness.** A clean result here neither confirms nor disturbs clause (b)'s powered null: v3 asked whether homonymy forms a *separate discrete regime across strata*; this asks whether *single ambiguous items* draw graded commitment. They are complementary, not substitutes.

## Relation to the existing wedge

- It **refines** [`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md) by isolating and scoping its one untested prediction (4); it does not restate the seed [`open-question/lexical-polysemy-gradience`](lexical-polysemy-gradience.md), whose three hypotheses (graded tracking / discrete collapse / distributional shadow) were the *cross-item* framing already largely resolved by v1–v3. This page's object — *within-item* indeterminacy on bridging uses — is the distinct, unrun axis those pages flagged but never operationalized.
- It is `model-internal` plus, on the DWUG route, `human-comparison`; on the engineered-construction route it would be a within-model contrast only. It does **not** touch the relational axis ([`open-question/relational-meaning-pilot`](relational-meaning-pilot.md)).
- The distributional shadow still lurks: a model could be less confident on bridging items merely because their *contexts* are more ambiguous, not their *senses*. Any serious design inherits v1's clause-(c) discipline — a context-similarity / context-ambiguity control measured independently of the model's sense signal — so within-item uncertainty is shown to track *sense* indeterminacy, not mere context indeterminacy. This is the lexical-uncertainty analogue of the `distributional` shadow that runs through the repo ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)).

## Status: open (scoping only)

This page does not run anything and does not ratify either gate. It re-opens the lexical axis, names prediction 4 as the cleanest untested lexical unit, and lays out the two decisions a future session must open and (cross-session) ratify before a probe: the **operationalization** of "intermediate, less-confident," and the **human anchor** for "genuinely bridging." Provisional defaults are recorded above for both; neither is decided here.
