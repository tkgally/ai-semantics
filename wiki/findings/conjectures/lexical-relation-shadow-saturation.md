---
type: conjecture
id: lexical-relation-shadow-saturation
title: "Antonymy is shadow-saturated: the relation where lexical-relation competence is least separable from the distributional control"
meaning-senses:
  - distributional
  - inferential
  - human-comparison
status: proposed
contingent-on: []
created: 2026-06-29
updated: 2026-06-29
anchor: pending
links:
  - rel: depends-on
    target: essay/antonymy-outlier-distributional-shadow
  - rel: depends-on
    target: source/cao-2025-semantic-relation-knowledge
  - rel: depends-on
    target: source/diera-2026-encode-semantic-relations
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: refines
    target: theory/lexicon-grammar-continuum
---

# Conjecture: antonymy is shadow-saturated

## Where this comes from

Two in-repo sources, working from opposite directions, agree that **antonymy is the lexical relation models recover best**. Behaviorally and human-compared, Cao et al. 2025 report that "**Antonymy is the outlier relation where all models perform reasonably well**" — in numbers, "**All models perform relatively well for antonymy, where the best model Llama-8B (L1) achieves 𝒮=0.57, whereas for other relations, best values typically lie around 𝒮=0.30**" ([`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md), Abstract + §8). Representationally, Diera & Scherp 2026 find a "**consistent difficulty ordering across models, with antonymy easiest**" — "**antonymy approaches ceiling on Llama**" ([`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md), §4.1).

The companion essay [`essay/antonymy-outlier-distributional-shadow`](../essays/antonymy-outlier-distributional-shadow.md) (written in this same wave) argues *why*: antonymy is the relation most fully cued by **symmetric contrastive co-occurrence** — *hot…cold*, *up…down*, *open…closed* recur in the same contrastive frames — so the antonymy result is the distributional shadow cast most completely. The relation models recover best is the relation the corpus hands them for free. This conjecture turns that reading into a falsifiable bet about the **project's own panel**, which neither paper tested: Cao runs BERT/RoBERTa/Llama-3, Diera runs Pythia-70M/GPT-2/Llama-3.1-8B, and the Cao source page is explicit that its gap-to-human result "**does not transfer**" to the project's frontier decoders "without re-running the probe on them" ([`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md), "What it cannot ground").

## Statement

> On a same-task lexical-relation probe over the six relations (hypernymy, hyponymy, holonymy, meronymy, antonymy, synonymy), run on the project's frontier panel (claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash) against a **co-occurrence / contrastive-frame distributional control**, **antonymy is the relation where the panel's competence is *least separable* from the control** — the relation with the smallest "over-and-above the distributional shadow" residual — while relations like **meronymy and hyponymy retain a larger residual**. Equivalently: the across-relation ranking of *raw* recovery is positively related to how strongly each relation is distributionally / contrastively cued, and antonymy tops both rankings.

This is a lexical-pole instance of the single test that organizes the continuum theory: "**does a meaning gradient beat the distributional shadow?**" ([`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md)). Here the unit is a *relation* rather than a graded sense scale, and the bet is not that some relation beats the shadow but that one relation — antonymy — is the one that **most fails to**, because for antonymy the shadow already does the work.

### Which meaning-senses this is, and is not

The three tags are `distributional` (the contrastive-frame control is a pure co-occurrence baseline — the shadow); `inferential` (a lexical relation is inferential-role structure: knowing *X is the opposite of Y*, *X is a part of Y* licenses inferences — the [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md) sense, in its thin Piantadosi-Hill internalist reading, not the Brandomian one); and `human-comparison` — carried because the bet's framing leans on Cao's *same-task human-vs-model* result and because the natural way to score relatum "competence" is against the human-produced relata of Cao's `ProbeResponses`, so a run of this bet would be a human-compared probe (which is exactly why the anchor below is human data, and why the test is blocked on adopting it). The bet is precisely about how much of the *inferential*-relation signal is **not** reducible to the *distributional* shadow, relation by relation.

It is **not** a `referential` claim and **not** a graded-polysemy claim. The probe is word-form-level relatum production/recognition, sense-agnostic — Cao's task "**is performed at the word form level … and not the sense level**" ([`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md), §4 footnote, as quoted on its page), so nothing here turns on reference, Fregean sense, or the usage-similarity gradience that [`conjecture/lexical-sense-gradience`](lexical-sense-gradience.md) runs on. Those are a complementary corner of the lexical wedge, not this one.

## The control (the spine of the bet)

The conjecture is about a **residual over a control**, exactly as clause (c) of [`conjecture/lexical-sense-gradience`](lexical-sense-gradience.md) makes the context-similarity control load-bearing for the sense wedge. Here the control is the relation analogue:

- A **distributional / contrastive-frame baseline** that predicts the relatum of a cue word from co-occurrence alone — e.g. a corpus or embedding measure of how strongly the candidate relatum co-occurs with the cue, with special weight on **symmetric contrastive frames** ("neither X nor Y", "X versus Y", "from X to Y") that are the antonymy-cuing signature. This baseline must be computed **independently of the panel's own responses**, so the control is real and not circular (the same discipline [`conjecture/lexical-sense-gradience`](lexical-sense-gradience.md) imposes on its context-overlap measure).
- The quantity of interest is the **control-adjusted residual** for each relation: how much of the panel's relatum recovery survives once the distributional/contrastive-frame baseline's prediction is partialled out (or otherwise held constant). The bet is that this residual is **smallest for antonymy**.

A naming caution carried from the source pages: this is a Harris-style *form-internal* distributional control, not a situated Firthian one ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md), historiographic caveat). "Beating the shadow" here means beating co-occurrence structure, nothing wider.

## What would confirm

Confirmation requires the direction of effect, not a precise magnitude (n=3 models — read orderings, not coefficients):

1. **Smallest residual for antonymy.** After the contrastive-frame control, antonymy shows the **smallest control-adjusted residual** of the six relations on **≥2 of 3 panel models**, with meronymy and/or hyponymy retaining a visibly larger residual on the same models.
2. **Raw recovery tracks distributional cue strength.** The across-relation ranking of *raw* (pre-control) recovery is **positively associated** with an independent ranking of how strongly each relation is distributionally / contrastively cued, on ≥2 of 3 models, with antonymy at the top of both.

Either of (1) or (2) on its own is weak support; both together, same-direction on ≥2 models, is the conjecture's central bet met.

## What would falsify

1. **Antonymy keeps a large residual.** If antonymy retains a **large control-adjusted residual** after the contrastive-frame control — its recovery is *not* explained away by the distributional baseline — then the "shadow-saturated" reading is wrong: the panel's antonymy competence would be over-and-above co-occurrence, i.e. genuine relational structure rather than a cast shadow.
2. **A weakly-cued relation is recovered best.** If a relation the contrastive-frame baseline cues only weakly — e.g. **meronymy** (part-whole, not a symmetric contrastive frame) — is the **best**-recovered or the smallest-residual relation, the cue-strength-tracks-recovery story fails directly.

Either outcome falsifies shadow-saturation. A third, non-falsifying outcome worth pre-naming: the residuals could be **flat across relations** (no relation clearly separates), which would be a null — it would neither confirm the antonymy-specific bet nor establish that some other relation is the shadow-saturated one.

## Blockers — why this is recorded, not run

This conjecture is **recorded for a future session, not a queued next move.** Three blockers, stated honestly:

1. **Spend-bearing.** It is a panel probe over six relations across three frontier models, so it would draw OpenRouter budget against the USD 5.00/day cap. A pre-flight estimate and the budget discipline of [`PROTOCOL.md`](../../../PROTOCOL.md)/[`config/budget.md`](../../../config/budget.md) apply before any run.
2. **No adopted human anchor.** The natural anchor is the released **human relata** from Cao's `hancules/ProbeResponses` — 48 MTurk Master annotators' open-ended noun relata over the six relations, "a candidate future `resource`," **not an adopted anchor.** Two concrete blockers stand in the way, both recorded on the source page ([`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md), "Resource / anchor potential"): **"No LICENSE file and no license statement were present in the repo on 2026-06-29"** so license status is "unknown — a blocker for adopting it as an anchor until clarified"; and a **count discrepancy** — "the paper §6.1 states 10,507 probes; the released GitHub README states 10,546." Adopting it is therefore "a separate, cross-session step (PROJECT.md §12.3): it requires fetching and cataloguing `human_responses.json` as its own `resource` page, resolving the missing license, and reconciling the 10,507/10,546 count discrepancy." Until that `resource` page exists with a resolved license, this conjecture's `anchor` stays **pending** and any test of it is **BLOCKED on the anchor**.
3. **No transfer from the prior art.** Per the Cao source page, that paper's gap-to-human result "**does not transfer**" to the project's panel "without re-running the probe on them" — so the prior-art numbers cannot stand in for a panel result; the probe must actually run on claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash. Diera & Scherp likewise tested only Pythia/GPT-2/Llama-3.1 and "**No transfer of these representational results to the panel is established**" ([`source/diera-2026-encode-semantic-relations`](../../base/sources/diera-2026-encode-semantic-relations.md), "What it cannot ground").

No `decisions/open/` entry is opened by this page: it records a bet, it does not make a value-laden methodological choice. The anchor-adoption decision (license + count reconciliation) is the cross-session step that a *later* session must take before this conjecture can be tested.

## What even a confirmation would and would not show

A confirmation would be a statement about **how distributional competence is organized across the six relations** on these models — which relations the co-occurrence shadow carries furthest — **not** a statement about meaning proper. Distributional structure is, "**by itself, silent on reference and on truth**" ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md)); shadow-saturation, if confirmed, says antonymy is the relation the *shadow* delivers most completely, which is the deflationary reading, not a finding that the panel grasps opposition. It would also be **behavioral, not representational** (the project's evidence is behavioral; Diera's representational asymmetry is a counterpoint method, not this probe's), on a three-model panel where the orderings, not any coefficient, carry the weight.

## Relation to the continuum

This `refines` [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md) at its **lexical pole**: the theory's "beat the distributional shadow" skeleton, applied not to a graded sense scale but to a six-relation gradient, predicting *which* relation least beats the shadow. It sharpens the source page's own observation that antonymy "(the relation most strongly cued by symmetric contrastive co-occurrence) is the one models recover best, which is exactly what a distributional-shadow story predicts" ([`source/cao-2025-semantic-relation-knowledge`](../../base/sources/cao-2025-semantic-relation-knowledge.md), "What this bears on in-repo") into a directional, panel-level, control-adjusted bet — currently blocked on the anchor.
