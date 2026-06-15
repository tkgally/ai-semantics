---
type: conjecture
id: preference-commitment-generality
title: The "preference without commitment" dissociation is a general property of divergent-default constructions, not an AANN artifact
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
anchor: pending
contingent-on: []
created: 2026-06-14
updated: 2026-06-15
links:
  - rel: depends-on
    target: result/aann-inferential-v6
  - rel: depends-on
    target: result/aann-inferential-v4
  - rel: depends-on
    target: essay/preference-without-commitment
  - rel: refines
    target: open-question/instrument-sensitivity-constructional-inference
  - rel: operationalizes
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: resource/scivetti-2025-cxnli-dataset
---

# Conjecture: preference without commitment generalizes beyond AANN

> **Status: proposed; a forward bet, unrun.** The governing decision
> [`decisions/resolved/fresh-construction-inferential-generalization`](../../decisions/resolved/fresh-construction-inferential-generalization.md)
> — which fresh construction carries the test, and under what binding conditions — was **ratified
> 2026-06-15** (autonomous adversarial review, cross-session: ADOPT Option A, the conative). So the
> construction is now the *ratified* choice, not a provisional default, and the frozen design
> [`design/conative-preference-commitment-v1`](../../../experiments/designs/conative-preference-commitment-v1.md)
> implements it. **`contingent-on` is cleared.** But the bet itself stays a *forward bet*: **no probe
> has yet been run**, so every claim below about what the panel *will* do is provisional. `anchor:
> pending` until a result lands — the anchor situation (entailment arm CxNLI-anchored answer-key;
> FC/cue arms internal-contrast-only) is spelled out under *Human anchor* below and applies to the
> result, not to this unrun conjecture.

## Statement

The AANN inferential probe produced the project's sharpest cross-instrument dissociation, now
**replicated cell-for-cell** on a fresh, larger, held-out item set
([`result/aann-inferential-v6`](../results/aann-inferential-v6.md), replicating
[`result/aann-inferential-v4`](../results/aann-inferential-v4.md)): a forced-choice **paraphrase
preference** shifts toward the construction's licensed reading in **all three** panel models, but
the NLI **entailment commitment** (and the grammaticalized agreement reflex) carries over in **only
one** model (gpt-5.4-mini), with claude-sonnet-4.6 and gemini-3.5-flash **paraphrase-only**. The
essay [`essay/preference-without-commitment`](../essays/preference-without-commitment.md) argues
this is a *type* difference — the two instruments measure graded distributional compatibility vs.
defeasible inferential commitment — so for two of three models "use" decomposes into a preference
component without a commitment component.

The conjecture is the forward bet that this dissociation is **not an AANN artifact** but a **general
property of constructions whose licensed inference diverges from their distributional default**:

> On a *fresh* construction whose licensed inference diverges from its distributional default
> (run under the same double-contrast preference-vs-commitment instrument, with the headroom
> precondition met), the panel will reproduce the **qualitative AANN pattern** — a forced-choice
> paraphrase-preference shift in (most or all of) the panel, an NLI entailment-commitment shift in
> only a minority, with at least one model converging across instruments and at least one model
> preferring without committing.

The bet is *qualitative and structural*, not a magnitude claim: it predicts the **shape** of the
dissociation (broad preference, narrow commitment, a split panel), not that a fresh construction's
numbers match the AANN's.

## Why this is interesting

- It tests whether the essay's central methodological claim — that a forced-choice paraphrase
  preference and an NLI entailment commitment are evidence for *two different constructs* — is a
  property of one marked English construction or a regularity of how current decoders handle
  divergent-default constructions generally.
- It sharpens [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md):
  the AANN gave that question its broadest, off-ceiling FC-vs-NLI divergence; a second construction
  reproducing the split would move "the two instruments index different constructs" from an
  AANN-instanced reading toward a panel-level regularity.
- It is the natural forward unit for the empirical track: the instrument is already ratified for
  AANN ([`decisions/resolved/aann-inferential-default-coincidence`](../../decisions/resolved/aann-inferential-default-coincidence.md)),
  and at least one fresh, divergent-default, in-repo-anchored candidate (the conative) is already
  off-ceiling, so the test is buildable without inventing a new resource.

## The instrument and the candidate

Under the open decision's provisional default, the fresh construction is the **conative**
("Maria kicked **at** the ball" → did not necessarily make completed contact) — a
**cancel-direction** construction whose licensed inference (no completed contact) runs *opposite* to
the verb's distributional default (*kick* lexically implies contact). The verb-held-constant minimal
pair ([`result/conative-minimal-pair-divergence-v1`](../results/conative-minimal-pair-divergence-v1.md))
already shows the transitive default at or near ceiling (affirm-contact 92–100%) while the
conative affirm-contact is off-ceiling and model/instrument-dependent — so the inference-vs-default
divergence and the headroom the AANN had to *engineer* are here **for free**. The add-direction
CxNLI constructions (way, caused-motion) ran *at* ceiling on both instruments
([`result/way-construction-traversal-v1`](../results/way-construction-traversal-v1.md): way rate
77.8–100%; [`result/caused-motion-minimal-pair-divergence-v1`](../results/caused-motion-minimal-pair-divergence-v1.md):
cm rate 90–100%) — precisely the no-dissociation regime, where compatibility and commitment move
together — so they are poor hosts for this split. The decision page records the full option set and
rationale; this conjecture states only the bet the chosen design would test.

## What would confirm / falsify

These criteria are symmetric by design (the anti-cheat note in the open decision): neither a uniform
positive nor a uniform negative can be read as confirmation.

- **Confirm:** the fresh construction reproduces the **qualitative dissociation** — a forced-choice
  paraphrase double-contrast shift (net of the lexical cue) in most or all of the panel, an NLI
  entailment double-contrast shift in a *minority* of models, with **at least one model converging
  across instruments and at least one model preferring without committing**. (The exact verdict map
  — per-model PARAPHRASE-ONLY / CONVERGENT-POSITIVE / NULL and the panel-level threshold — must be
  pre-registered in the frozen design, carried from the AANN instrument unless re-justified.)
- **Falsify (convergence):** the fresh construction shows **full cross-instrument convergence in
  all three models** (paraphrase and NLI move together everywhere) — then the AANN's
  preference/commitment split is plausibly AANN-specific (or specific to its unification semantics),
  and the dissociation does not generalize.
- **Falsify (null):** the fresh construction shows a **full null in all three models** on both
  instruments (no paraphrase shift to dissociate *from*) — then the antecedent of the bet is absent
  for this construction and the instance falls; the general conceptual point survives un-instanced.
- **Weak / inconclusive:** the headroom precondition fails (the construction reads at ceiling on
  both instruments), so the design must not run — this neither confirms nor falsifies and routes to
  the decision's fallback.

A binding scoring caution the design must pre-register: the conative *already* exposes
gpt-5.4-mini's NLI-fails / FC-recovers fragility
([`result/conative-cancel-direction-v2`](../results/conative-cancel-direction-v2.md)). The test is
whether the **full panel** reproduces the AANN *shape*, **not** whether any single model diverges —
the pre-existing single-model fragility must not be retrofitted as new evidence for generality.

## Human anchor

`anchor: pending` until a result lands — the now-ratified decision
[`decisions/resolved/fresh-construction-inferential-generalization`](../../decisions/resolved/fresh-construction-inferential-generalization.md)
fixes the anchor situation, realized only when the probe runs. The honest situation, stated precisely:

- If the conative (or another CxNLI construction) carries the test and the result makes a
  human-comparison NLI claim against the CxNLI gold labels, the **entailment arm** would be
  **human-anchored** via [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
  — the ratified anchor for the conative (2026-05-29). That resource carries a verbatim conative NLI
  triple (premise *"I sipped at the Heineken."*, hypothesis *"The Heineken was not the target of my
  sipping."*, relation **Contradiction**, Table 9) and a native-speaker baseline (Exp 1 ≈ 0.90).
  **Caveat, verbatim from the resource:** the release gives a *single* adjudicated gold label per
  item, "so it anchors an answer-key comparison, not a graded human-judgment gradient." So the
  entailment arm could ground an **answer-key + aggregate-baseline** human comparison, **not** a
  per-item human gradient — and this is more than the AANN inferential line could claim, which is
  permanently `internal-contrast-only` (CxNLI "is **not** among the 8 constructions. Do not cite
  this dataset for AANN").
- The **forced-choice paraphrase arm** and any lexical-cue arm without an in-repo human norm stay
  `internal-contrast-only` (no human paraphrase-preference data exists for these constructions).
- If an un-anchored construction were chosen instead (the decision's Option C), the whole result
  would be `internal-contrast-only` and a fresh anchor decision would have to be queued first. No
  anchor may be invented.

## Notes / caveats

- **Provisional throughout.** The construction, the verdict map, and the anchor status all depend on
  the open decision's ratification; until then this is a forward bet, not a design.
- **Shared priors (charter §2.5).** Three decoders are not three independent witnesses; the
  panel-level *shape* of the dissociation is the signal, and any human bearing is the CxNLI anchor,
  not the model agreement.
- **The paraphrase arm is the weaker instrument.** As in the AANN line, a paraphrase-preference
  shift is weaker evidence than a converging NLI shift; a paraphrase shift without commitment is to
  be reported as "preference without commitment," not "draws the inference." The conative has no
  AANN-style grammaticalized agreement reflex, so the NLI arm carries the discriminator role.
- **One construction is not "general."** Even a clean confirmation would license only "the
  dissociation reproduces on a *second* divergent-default construction," not a quantified claim about
  divergent-default constructions as a class — that would need several.
