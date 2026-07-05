---
type: claim
id: preference-commitment-dissociation-aann-specific
title: On the project's evidence so far, the forced-choice-paraphrase-vs-entailment ("preference without commitment") dissociation is AANN-specific — it replicates across two disjoint AANN item sets but does not reproduce on the conative across two independent verb samples, in either direction
meaning-senses:
  - constructional
  - inferential
  - distributional
status: supported
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-15
updated: 2026-07-05
links:
  - rel: depends-on
    target: result/aann-inferential-v4
  - rel: depends-on
    target: result/aann-inferential-v6
  - rel: depends-on
    target: result/conative-preference-commitment-v1
  - rel: depends-on
    target: result/conative-commitment-replication-v2
  - rel: refines
    target: conjecture/preference-commitment-generality
  - rel: refines
    target: essay/preference-without-commitment
  - rel: refines
    target: theory/constructional-meaning-in-llms
---

# Claim: the preference/commitment dissociation is AANN-specific (on the evidence so far)

> **Anchor: `internal-contrast-only`.** This claim draws a **within-model, cross-construction
> contrast** — does a model's forced-choice-paraphrase-vs-entailment behaviour dissociate on the
> AANN but *not* on the conative, relative to matched controls? It inherits the
> `internal-contrast-only` status of its constituent results
> ([`result/aann-inferential-v4`](../results/aann-inferential-v4.md),
> [`result/aann-inferential-v6`](../results/aann-inferential-v6.md): both terminally
> `internal-contrast-only`; the conative runs'
> [`result/conative-preference-commitment-v1`](../results/conative-preference-commitment-v1.md) and
> [`result/conative-commitment-replication-v2`](../results/conative-commitment-replication-v2.md)
> forced-choice/cue arms are `internal-contrast-only`), introduces **no new human-comparison
> claim**, and therefore requires **no new resource anchor**. The cross-construction *contrast* this
> claim draws is internal. (In passing: the conative NLI commitment arm was itself human-anchored at
> the *result* level to [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
> — answer-key + ≈0.90 aggregate baseline, not a per-item gradient — but the AANN inferential line is
> permanently `internal-contrast-only` (CxNLI is not among its 8 constructions), so a *contrast*
> between the AANN's behaviour and the conative's cannot be a human comparison and is recorded as a
> within-model contrast only.)

## Statement

On the project's evidence so far, the forced-choice-paraphrase-vs-entailment dissociation the project
named **"preference without commitment"** — a construction shifting which paraphrase a model *prefers*
under a forced exclusive choice without shifting whether it will *commit* to the corresponding
entailment under NLI — is **AANN-specific**.

It **replicates across two disjoint AANN item sets** (v4 and its powered, fresh-item v6 replication)
but **does not reproduce on the conative** across two independent verb samples (v1, and the
commitment-only direct replication v2), in **either direction**. The one apparent counter-signal — a
single model's commitment-only shift on the conative — was shown to be **verb-set-specific noise**.

Three things follow, each calibrated to the evidence:

1. **The dissociation does not, on current evidence, generalize beyond the AANN.** The first
   generalization attempt — the conative — failed to reproduce the AANN shape, and the lone exception
   did not survive replication.
2. **A forced-choice "preference" can be driven by a bare lexical cue.** On the conative the
   construction's apparent preference shift was absorbed entirely by the bare-*at* lexical cue, so a
   paraphrase-preference shift is **not by itself evidence of constructional inference**.
3. **This is a construction-particular result.** The AANN-specific reading of the dissociation is
   *strengthened*, with no surviving counter-instance — but only relative to the **one** alternative
   construction tested.

**Calibration, binding on every reading:** this is *"AANN-specific on the evidence so far,"* **not**
*"the dissociation is unique to the AANN as a matter of fact."* Only **one** alternative construction
(the conative) has been tested; a third has not been run (the add-direction CxNLI constructions run at
ceiling and would need engineered headroom first). The claim is a bounded close on a single
generalization attempt, not a proof of AANN-uniqueness.

## Grounds

### The AANN side — the dissociation replicates across two disjoint item sets

The instrument is a double contrast on the *same frozen items*: a forced-choice paraphrase arm
(Δ² = P(uni|AANN) − P(uni|LCC)) and an NLI entailment arm, plus the grammaticalized
singular-agreement reflex as a load-bearing discriminator. In **v4**
([`result/aann-inferential-v4`](../results/aann-inferential-v4.md)) the construction shifts paraphrase
selection toward unification in **all three** panel models — paraphrase Δ² = **+0.783 / +0.696 /
+0.957** (claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash), "every CI clear of 0 and τ=+0.20" —
while the NLI entailment commitment clears the bar in **only one** model (gpt-5.4-mini, NLI Δ²
**+0.261** CI[0.07,0.46]; claude +0.152 not pos, gemini −0.087 not pos), and the agreement reflex
fires only for gpt (+0.652). The result's own pre-registered verdict is **PARTIAL**: "a paraphrase-level
constructional shift in all three models, converging to a full cross-instrument inferential shift in
one (gpt-5.4-mini)."

In **v6** ([`result/aann-inferential-v6`](../results/aann-inferential-v6.md)) — a powered replication on
**40 fresh held-out adjectives**, mechanically disjoint from v4's, with instrument, thresholds, verdict
map, and analysis code identical — the result **replicates cell-for-cell**: paraphrase Δ² = **+0.875 /
+0.575 / +0.90** (all CI clear of 0), gpt again the only NLI converger (Δ² **+0.225** CI[0.08,0.38];
claude +0.150, gemini −0.025), gpt again the only positive agreement reflex (+0.60), verdict again
**PARTIAL**. The v6 page's own gloss: "the construction effect on the primary paraphrase instrument is
now shown to be **stable in magnitude across two disjoint item sets**, not just a direction-of-effect."
So on the AANN the preference/commitment split is a robust, twice-instanced fact.

### The conative side — the dissociation does not reproduce, in either direction

The forward bet [`conjecture/preference-commitment-generality`](../conjectures/preference-commitment-generality.md)
predicted the AANN *shape* (broad paraphrase shift, narrow commitment, a split panel) would reproduce on
a fresh divergent-default construction. It was tested on the **conative** under the same double-contrast
instrument, governed by the ratified
[`decisions/resolved/fresh-construction-inferential-generalization`](../../decisions/resolved/fresh-construction-inferential-generalization.md)
(Option A — the conative).

**v1** ([`result/conative-preference-commitment-v1`](../results/conative-preference-commitment-v1.md))
returned **INCONCLUSIVE**: "The AANN preference-without-commitment shape did not reproduce on the
conative." Two facts carried it. First, the paraphrase double contrast Δ²_pref was **non-positive in
all three models** (claude **−0.21**, gpt **0.00**, gemini **−0.04**): the licensed conative did not
move the paraphrase preference *more than the matched anomalous "at"-string moves it* — the bare-*at*
lexical cue **absorbed** the cancel-preference. Second, the only construction effect was a single
model's *commitment*-only shift — claude Δ²_commit = **+0.46** (95% CI **[0.08, 0.79]**), a
COMMITMENT-ONLY effect that is the **mirror** of the AANN's preference-without-commitment (the other two
models were LEXICAL-CUE ARTIFACT). Crucially, headroom **PASSed for all three models**, so the
non-reproduction is **not** a ceiling artifact: there was room for a construction effect on the
paraphrase arm and none appeared.

**v2** ([`result/conative-commitment-replication-v2`](../results/conative-commitment-replication-v2.md))
put that lone positive — claude's +0.46 — to a **direct replication on a fresh, disjoint conative verb
set** (12 new conative verbs + 8 new resist verbs; `analyze.py` byte-identical), asking whether it was a
stable single-model property or one-item-set noise. **It did not replicate.** claude's Δ²_commit
**collapsed from +0.46 → +0.04** (95% CI **[−0.29, 0.33]**, not positive), its category flipping to
LEXICAL-CUE ARTIFACT; the driver is transparent (claude withheld the contact entailment for the
licensed conative 58% of the time in v1 but only 17% — 2 of 12 verbs — on the fresh set). All three
models now land as LEXICAL-CUE ARTIFACT on both arms, headroom again PASSing at 1.00 / 1.00. The v2
verdict, verbatim: **"FAILS TO REPLICATE. The v1 +0.46 is best read as verb-set-specific (plausibly
one-item-set noise), not a stable single-model property."**

So across two independent conative verb samples the licensed conative moves **neither** the paraphrase
preference **nor** the NLI commitment in any model, net of the bare-*at* cue — a clean no-dissociation
result in both directions, with the lone apparent exception retired as noise.

### The cross-construction contrast — the load-bearing datum

The sharpest fact is the **contrast between the two constructions under one instrument**: on the AANN
the paraphrase double contrast is positive in all three models on two item sets, while on the conative
it is non-positive in all three on two verb samples; and the AANN's preference-without-commitment
ordering has no stable analogue on the conative in either direction. That contrast is what makes the
dissociation read as **construction-particular** rather than general — and, because it is a comparison
of within-model behaviours under a shared instrument, it is an internal contrast (see Anchor box).

## Where it sits on the evidence ladder

On the ladder in [`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md)
*(superseded s177 by [`theory/constructional-meaning-in-llms-v2`](../theory/constructional-meaning-in-llms-v2.md)
— cited here as the edition this page engaged.)*,
this claim records that the **instrument-sensitivity story is construction-particular**: the
forced-choice paraphrase arm and the NLI entailment arm — both used to probe Tier-4-adjacent
meaning-tracking — *can* dissociate (AANN), but the *way* they dissociate **does not transfer** to the
conative, and on the conative it is the weaker paraphrase instrument that shows no construction-specific
signal at all once the lexical cue is netted out. It also supplies a concrete caution the ladder should
carry: a forced-choice paraphrase-preference shift can be produced by a bare lexical cue (the conative
bare-*at* case), so such a shift is Tier-4-relevant evidence about distributional compatibility at most,
**not** evidence of inference-licensing on its own. The theory page already logs the conative
non-reproduction and the retired counter-signal; this claim is the typed, bounded close those callouts
point to.

## What it does NOT claim

- **It does not claim AANN-uniqueness as a matter of fact.** Only the conative has been tested. Two
  conative samples failing to reproduce the shape strengthen "AANN-specific so far" but cannot
  establish that the dissociation is unique to the AANN; that needs a genuinely different construction
  with engineered headroom (the ratified decision's named way/caused-motion near-miss fallback, which
  runs at ceiling and has not been built for this instrument).
- **It does not retract the essay's conceptual point.** The essay
  [`essay/preference-without-commitment`](../essays/preference-without-commitment.md) argues a *type*
  distinction — that a forced-choice paraphrase preference and an entailment commitment are evidence for
  two different constructs. That conceptual point **stands, un-instanced outside AANN**; this claim
  bounds only the empirical *generality* of the preference-without-commitment **ordering**, which the
  essay never asserted (its triggers are AANN-internal and none fired).
- **It is not a human-comparison claim.** `anchor: internal-contrast-only` (see Anchor box). Nothing
  here is a claim about whether models prefer-or-commit *the way humans do*, on either construction.
- **It does not claim the conative "lacks" the inference.** The conative result is a non-reproduction
  of a *shape* under one instrument, with the NLI arm human-anchored at the result level; it does not
  establish that no model ever tracks the conative inference (v1/v2 record only that no model reliably
  *withholds* contact for the licensed conative under this instrument).

## Limits

- **One alternative construction.** A single fresh construction failing to reproduce the shape (twice)
  is a genuine, informative negative against the forward bet — but it is one construction. The claim is
  scoped to "AANN-specific on the evidence so far," not to a quantified property of divergent-default
  constructions as a class.
- **Single panel; the conative arms partly expert-stipulated.** All four results are the same three
  2026-panel models. The conative paraphrase/cue arms are `internal-contrast-only` with an
  expert-stipulated cancel reading; the AANN line is permanently `internal-contrast-only` with an
  expert-stipulated unification key. The cross-construction contrast is therefore a within-panel,
  within-model comparison.
- **The conative double contrast is licensed-conative-vs-anomalous-*at*-string**, not a perfect lexical
  minimal pair (only non-alternating verbs are non-conative) — the verb-class confound is real and
  disclosed on both conative result pages; the claim leans on Δ² net of the cue.
- **A non-replication is not proof of absence.** The retired claude +0.46 had a wide CI on a single
  sample; failing to reproduce it on one fresh sample is strong evidence it was noise, not proof claude
  never shows a conative commitment effect.

## Status

`status: supported`. The empirical numbers are published in-repo and verified verbatim on their result
pages (every figure here traces to v4 / v6 / conative-v1 / conative-v2). What is `supported` is the
bounded close itself — that the preference/commitment dissociation is AANN-specific *on the evidence so
far*, with the conative non-reproduction holding in both directions across two verb samples and the lone
counter-signal retired as noise. `anchor: internal-contrast-only`: the claim is a within-model,
cross-construction contrast and makes no human-comparison claim. `contingent-on: []` — it rests on four
landed, non-contingent results, not on any open decision.
