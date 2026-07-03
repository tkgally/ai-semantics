---
type: essay
id: shadow-depth-cross-cuts-grain
title: "Shadow-depth, not grain — the continuum's single test sorts phenomena by how much is already written into co-occurrence, and that axis cross-cuts the word↔construction cline"
meaning-senses:
  - distributional
  - inferential
  - constructional
status: revised
contingent-on: []
created: 2026-07-02
updated: 2026-07-03
links:
  - rel: refines
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: result/presupposition-doppelganger-control-v1
  - rel: depends-on
    target: essay/antonymy-outlier-distributional-shadow
  - rel: depends-on
    target: essay/presupposition-environment-gated
  - rel: depends-on
    target: conjecture/presupposition-environment-gated-both-directions
  - rel: depends-on
    target: result/accommodation-cue-strength-v1
  - rel: depends-on
    target: result/presupposition-accommodation-v1
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: result/comparative-correlative-covariation-v1
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
---

# Shadow-depth, not grain

> **REVISION (2026-07-03, s173) — the presupposition corner's owed control has RUN; the first revision
> trigger does NOT fire; the placement stands in a weakened form.**
> [`result/presupposition-doppelganger-control-v1`](../results/presupposition-doppelganger-control-v1.md)
> ran the matched surface-cue doppelgänger control this essay named as owed. Verdict
> **BEATS-DOPPELGANGER** (pooled residual +0.78 / +0.47 / +0.94): the panel discriminates the trigger
> from a matched non-presupposing doppelgänger, so the corner is **not behaviorally FLAT**. But this is
> the **under-licensed** outcome — the residual is **keyed to the trigger word-form** and
> **surface-cue-reconstructable** (the powered D1 controls vary the *word*; the one construction-grain leg,
> cleft, gives no clean cross-panel residual — gpt near-flat and control-failing, claude/gemini carried by
> a negation-frame surface cue). So it is **not** "a residual a surface-cue account cannot reconstruct,
> held stably across frames" — the first revision trigger's exact bar — and the trigger **does not fire**.
> **Net:** the corner moves from *pure reading/bet* to *reading with a measured caveat*: shadow-saturated
> in this essay's precise sense (its residual is one a surface-cue account can reconstruct), though **not
> flat**. It is **not** moved to the beater side. The Honesty box's "weakest where it most needs strength"
> bullet is updated accordingly below.

> **Status: revised (2026-07-03, was draft 2026-07-02). A philosophical-track essay in the project's own voice.**
> It introduces **no new empirical claim** and makes **no human comparison of its own**. Every
> empirical assertion cites the in-repo `result` or `essay` page that carries it, at that page's
> stated strength. Its two load-bearing empirical inputs on the *shadow-saturated* side — the
> antonymy relation-recovery reading and the presupposition corner — are **not measured failures to
> beat a distributional shadow**: the antonymy input is prior-art plus a blocked conjecture
> ([`essay/antonymy-outlier-distributional-shadow`](antonymy-outlier-distributional-shadow.md)), and
> the presupposition inputs are `internal-contrast-only` within-model contrasts with **no human
> comparison** ([`result/presupposition-accommodation-v1`](../results/presupposition-accommodation-v1.md),
> [`result/accommodation-cue-strength-v1`](../results/accommodation-cue-strength-v1.md)). Placing
> either phenomenon at the shadow-saturated end is a **reading/bet**, not a controlled result — the
> essay is explicit about that asymmetry throughout, and about the fact that its original contribution
> is a **structural re-description**, not evidence.

## The claim

The lexicon–grammar continuum ([`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md))
is organized around one test: *does the model track a meaning gradient that beats the distributional
shadow?* The continuum lays that test along a **grain** axis — a word is a maximally specific
construction, an argument-structure template a maximally schematic one, and the same beat-the-shadow
skeleton runs at both grains. Its headline is that current decoders track a graded form–meaning signal
that beats the distributional null **at both** the word grain and the construction grain.

This essay's contribution is a second, cross-cutting observation about *what the test actually sorts*.
Run the single test across the whole cline and it does **not** order phenomena by grain. It orders them
by **shadow-depth**: how much of the phenomenon is already written into surface co-occurrence — how
much daylight there is between the phenomenon and its distributional trace. And shadow-depth
**cross-cuts** grain. Each pole of the continuum turns out to contain *both* a phenomenon where the
gradient beats the shadow *and* a corner where the shadow is deep enough that a pure surface-cue
account has no residual to answer for. The word↔construction grain is not the informative ordering of
the continuum. Shadow-depth is, and it runs orthogonal to grain.

## The lexical pole is already internally graded by shadow-depth

The continuum page already records this for the lexical pole, so the essay only names the structure.
At the word grain there is a demonstrated **shadow-beater**: graded sense gradience
([`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md)), where the panel's
graded sense-relatedness rating rank-tracks the human DURel median (Spearman **0.60–0.83**) and, the
load-bearing part, **survives partialling out the model's own topic-similarity rating** (e.g. gemini
0.80→0.73) — a signal that carries rank information *over and above* the context-similarity shadow.

At the *same* grain there is a **shadow-saturated corner**: relation-type recovery, where
[`essay/antonymy-outlier-distributional-shadow`](antonymy-outlier-distributional-shadow.md) reads the
convergent finding that antonymy is the relation models recover best as deflationary — antonym pairs
recur in tight contrastive frames, so antonymy is the relation where the distributional shadow is
*largest* and the over-and-above residual a competence claim must show is *smallest*. "The relation at
which models look best is precisely the relation at which 'looking good' is least informative about
anything over and above co-occurrence." So the lexical pole is not one cell but a **relation-type
gradient**: a shadow-beater
(graded sense) at one end, a shadow-saturated corner (antonymy) at the other — both at the word grain.

## The grammatical pole is *also* internally graded by shadow-depth

The new structural point is that the **same internal split** appears at the construction grain, which
the continuum's grain-only reading does not lead you to expect.

The grammatical pole has its own demonstrated **shadow-beater**: the comparative-correlative
covariation inference ([`result/comparative-correlative-covariation-v1`](../results/comparative-correlative-covariation-v1.md)
→ v2 → v3). All three models assert a covariation direction for ~100% of CC items but only 10–20% of
matched non-CC controls that reuse the *same words* (assertion gap **+80–90 pp**), flip direction on
inverse-CC items (**95–100%**), and hold on deliberately absurd scale pairs — so the inference is
keyed to the **construction**, not to the scalar vocabulary, above matched controls that share the
surface material. That is a construction-grain phenomenon with a genuine over-and-above residual.

And now, from the presupposition line, the grammatical pole has a **shadow-saturated corner** of its
own. The presupposition corner is, on a semantic theory's telling, a represented presupposition/
assertion split that ought to hold *invariantly* across embeddings and contexts — an inferential
competence. What the within-model probes find instead is that its behavior is fully described by
*follow the surface cue; its reliability is set by the environment*
([`essay/presupposition-environment-gated`](presupposition-environment-gated.md)):

- **Projection** is gated by the embedding **frame** — the presupposition survives negation (matched
  entailment cancels to E = 0.00) and **collapses under the conditional antecedent** for every model
  (survival **0.42 / 0.17 / 0.17**) ([`result/presupposition-projection-v1`](../results/presupposition-projection-v1.md)).
- **Accommodation** is gated by **context support** — supplied near-ceiling in a neutral context
  (**1.00 / 0.92 / 1.00**), substantially withheld under explicit contradiction (**0.33 / 0.58 / 0.42**)
  ([`result/presupposition-accommodation-v1`](../results/presupposition-accommodation-v1.md), verdict
  GATED-ACCOMMODATION 3/3).

There is no residual here, on this reading, that a surface-cue account cannot reconstruct: the
environment-gated description predicts both signatures directly, and a frame-/context-*invariant* represented split
would predict the invariance the panel does **not** show. This is exactly what a shadow-saturated
corner looks like at the construction grain — a phenomenon whose within-model behavior is written into
how reliably the licensing environment leaves the trigger's cue on the surface.

So presupposition marks the grammatical pole's shadow-saturated end just as antonymy marks the lexical
pole's. Both poles are structurally parallel: each carries a shadow-beater and a shadow-saturated
corner. Grain does not separate the beaters from the saturated corners; shadow-depth does, at both
grains.

## Why the graded gate does *not* rescue a "computes the split" reading

The one place this could seem to break is the accommodation gate's **grading**. The follow-up probe
found the gate is **GRADED by surface-contradiction strength** (GRADED-GATE 3/3): every model backs
off a denied presupposition harder under an emphatic denial than a hedged one — weak-endorse
**0.42 / 0.67 / 0.83** vs strong-endorse **0.08 / 0.50 / 0.17**, strength-gradient
**+0.33 / +0.17 / +0.67** ([`result/accommodation-cue-strength-v1`](../results/accommodation-cue-strength-v1.md)).
Sensitivity to *how strongly* a contradiction is worded can look like sophistication — like the model
computing something finer than a surface switch.

It is not evidence against the shadow reading; it is what *makes the shadow deep here*. As the result
page argues, a **cue-strength–sensitive distributional learner predicts exactly this graded gate**: a
learner that follows the surface cue, weighting it by its reliability, will back off a denied
presupposition in proportion to how strongly the surface denies it. Graded ≠ "computes the split." The
grading tells you the surface cue is being read at fine resolution, not that a represented
presupposition/assertion object is being carried invariantly through the environment. A deeper,
better-calibrated response to the surface cue is a *deeper* shadow, not a shallower one. This mirrors
the lexical side, where antonymy's cross-method robustness (behavioral + representational agreement)
likewise *raises* the prior on the shadow reading rather than rebutting it, because both methods are
downstream of the same co-occurrence structure.

## The evidential status is parallel too — and weak on the saturated side

The parallel between the two poles extends to the **status** of the evidence, and honesty requires
stating that the two saturated corners are the weak halves of both poles.

The two shadow-**beaters** are measured against controls that strip the shadow: CC covariation clears
matched same-word controls and carries a human anchor
([`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md), via
the result page); lexical sense gradience survives a partialled topic-similarity control and carries
the DWUG human anchor. These are results that *pass* — a residual over a shadow was measured.

The two shadow-**saturated** corners are **not** measured failures to beat a shadow. Antonymy is
prior-art on non-panel models plus a **blocked** conjecture
([`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md)):
no matched contrastive-frame control has been run on the project's panel that would show antonymy
recovery *fails* to clear a shadow. Presupposition is `internal-contrast-only`: its behavior is
*consistent with* a surface-cue description, but **no matched distributional control** was run that
would show it *fails* to beat a shadow the way CC *passes*. Placing presupposition at the
shadow-saturated end is therefore a **reading/bet, structurally parallel to the antonymy bet** — not a
controlled result. The asymmetry is exact: on the beater side we have a residual over a control; on the
saturated side we have a phenomenon whose behavior a surface-cue account *reconstructs*, with the
discriminating control still owed. This essay claims the *structure* (two poles, each with a beater
and a saturated corner, sorted by shadow-depth) is the better-fitting reading — not that the
saturated corners have been demonstrated to sit where it places them.

## What this sharpens, and what it complicates

**Sharpens.** It adds a second ordering axis to the continuum, orthogonal to grain, and it locates the
grammatical pole's shadow-saturated corner empirically-adjacently (via the presupposition line) where
the continuum previously had only the lexical pole's. The informative question the single test answers
is not "word or construction?" but "how deep is the shadow here?" — and that question has a
same-shaped answer at both grains.

**Complicates.** It qualifies the continuum's headline. "Current decoders track a graded form–meaning
signal that beats the distributional null at both grains" is true of the *beaters* at both grains, but
the grammatical pole is **not uniformly a shadow-beater**: its presupposition corner, on the reading
here, is not one — its within-model behavior is described without residual by a surface-cue account.
The headline is a claim about where the beaters are, not a claim that every corner of either pole
beats the shadow. Read with the shadow-depth axis, the continuum's positive is real but local: it
holds at the beater corners, and each pole also has a corner where it does not.

This does not touch the continuum's other structural finding — that the model *competences* dissociate
across the panel even where the *targets* unify (the cross-axis ordering result). Shadow-depth is a
property of the **phenomenon** (how much is written into co-occurrence), not of a model; it re-sorts
the targets, and is silent on which model tracks which.

## Revision triggers (read before citing)

- **The presupposition placement is a bet; a matched control could move it. — PARTIALLY DISCHARGED
  2026-07-03 (s173); the trigger did NOT fire.** The matched-control probe
  [`result/presupposition-doppelganger-control-v1`](../results/presupposition-doppelganger-control-v1.md)
  ran. It did **not** show a residual a surface-cue account cannot reconstruct held stably across frames:
  the verdict was BEATS-DOPPELGANGER but **under-licensed** (word-form-keyed; the powered D1 legs vary the
  word; the cleft leg gives no clean cross-panel residual). So the placement is **not** overturned — the
  grammatical pole does **not** gain a second beater. What *did* change: the corner is not behaviorally
  flat. This trigger now fires only if a **construction-grain-only** control (a cleft-family battery with
  the question-frame confound removed) produced a residual not reducible to a surface cue. If a
  matched-control probe *had* shown the corner beats a distributional shadow — a residual a surface-cue
  account cannot reconstruct, held stably across frames and contexts — then "shadow-saturated" would be the
  wrong placement, and the grammatical pole would have *two* beaters. (Symmetrically for antonymy: if the blocked
  [`conjecture/lexical-relation-shadow-saturation`](../conjectures/lexical-relation-shadow-saturation.md)
  ran and antonymy competence survived a contrastive-frame control, the lexical saturated corner moves.)
- **If either signature turns environment-*invariant*.** The presupposition corner's saturated status
  depends on the environment-gating being real. If projection turned frame-invariant, or accommodation
  context-invariant, the [`essay/presupposition-environment-gated`](presupposition-environment-gated.md)
  reading retracts, and with it this essay's placement of that corner.
- **If a shadow-beater fails to replicate.** The parallel needs a beater at each pole. If CC
  covariation or lexical sense gradience failed to replicate — or their shadow-controls (matched
  same-word controls; partialled topic-similarity) turned out not to hold — the "each pole has a
  beater" half of the structure weakens.
- **If the graded gate turned out FLAT on re-run** (endorsement insensitive to contradiction strength),
  the "deep shadow, not computed split" gloss on the accommodation corner would need re-stating —
  though a flat gate is *also* a distributional story (pure contradiction-detection), so it would not
  by itself move presupposition off the saturated end.
- **If the underlying numbers move**, the empirical premises above move with them and this reading is
  re-examined in-page.

## Honesty box

- The **original** contribution is the **re-description**: that the continuum's single test sorts by
  **shadow-depth**, a second axis orthogonal to grain, and that each pole is internally split into a
  shadow-beater and a shadow-saturated corner — presupposition standing to the grammatical pole as
  antonymy stands to the lexical pole. The beat-the-shadow frame is from
  [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md); the antonymy reading
  and the presupposition reading are from the two essays cited; this essay only argues they are the
  *same structural move at the two poles* and that shadow-depth, not grain, is the informative axis.
- **No empirical claim here is new, original, or reported.** Every number is cited at its source page's
  stated strength: Spearman 0.60–0.83 and the topic-partial survival from
  [`result/lexical-sense-gradience-v1`](../results/lexical-sense-gradience-v1.md); the CC assertion gap
  (+80–90 pp), inverse-flip (95–100%), and 3/3 gates from
  [`result/comparative-correlative-covariation-v1`](../results/comparative-correlative-covariation-v1.md);
  projection survival/collapse (E = 0.00; 0.42/0.17/0.17) from
  [`result/presupposition-projection-v1`](../results/presupposition-projection-v1.md); the
  accommodation gate (neutral 1.00/0.92/1.00, contradicting 0.33/0.58/0.42) from
  [`result/presupposition-accommodation-v1`](../results/presupposition-accommodation-v1.md); the graded
  gate (weak 0.42/0.67/0.83 vs strong 0.08/0.50/0.17; gradient +0.33/+0.17/+0.67) from
  [`result/accommodation-cue-strength-v1`](../results/accommodation-cue-strength-v1.md).
- **No human comparison of its own, no mechanism.** The presupposition inputs are
  `internal-contrast-only` within-model contrasts (no human projection/accommodation baseline was
  measured); the antonymy input is prior-art on non-panel models plus a blocked conjecture. The essay
  reads *descriptions*, not what the models compute internally.
- **Weakest where it most needs strength — now partly measured on the presupposition side (2026-07-03).**
  The antonymy corner remains a **reading/bet** (no matched contrastive-frame control run on the panel). The
  presupposition corner has now had its matched surface-cue control **run**
  ([`result/presupposition-doppelganger-control-v1`](../results/presupposition-doppelganger-control-v1.md)):
  it is **not** a clean controlled failure-to-beat-a-shadow (the doppelgänger *is* discriminated —
  BEATS-DOPPELGANGER, not the flat null) and **not** a controlled shadow-beater (the residual is
  word-form-keyed and surface-cue-reconstructable). It lands in the **under-licensed middle** — measured,
  but neither pole — so "shadow-saturated in the precise sense that the residual is surface-cue-
  reconstructable" is now a *measured caveat*, not a bare reading, while the strong flat-null form is
  disconfirmed. The strongest thing the essay asserts is still that shadow-depth is the **better-fitting
  structural ordering** of the continuum and cross-cuts grain — offered at weak evidential strength (n=3
  models, small synthetic item sets, direction-of-effect only), as the reading to knock down, not as a
  demonstrated property of language models.
