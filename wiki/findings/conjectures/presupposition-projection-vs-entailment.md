---
type: conjecture
id: presupposition-projection-vs-entailment
title: "Under negation/question/conditional embedding, the panel endorses a base sentence's PRESUPPOSITION more than a MATCHED ENTAILMENT — a within-model projection asymmetry"
meaning-senses:
  - inferential
  - distributional
status: tested
contingent-on: []
created: 2026-07-01
updated: 2026-07-05
links:
  - rel: refines
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: open-question/presupposition-projection-corner
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Conjecture: presupposition projects above a matched entailment (within-model)

> **Status: tested** *(originally proposed 2026-07-01, session 158, as the pre-registration for the run
> [`experiments/runs/2026-07-01-presupposition-projection/`](../../../experiments/runs/2026-07-01-presupposition-projection/README.md),
> frozen [`PREREG.md`](../../../experiments/runs/2026-07-01-presupposition-projection/PREREG.md),
> manifest sha `e3a04cdd…`)*. Read the *Scope cap* before citing any sentence: this is a
> **within-model** contrast at `internal-contrast-only` strength (**no human comparison**), and its
> terminal anchor status was **ratified** by an independent session-159 adversarial review
> ([`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../decisions/resolved/presupposition-projection-internal-contrast-anchor.md)).

> **Outcome (run 2026-07-01, s158; box added 2026-07-05, session 183 — wiki-coherence pass, fixing
> a recorded front-matter/blockquote mismatch).** The run landed as
> [`result/presupposition-projection-v1`](../results/presupposition-projection-v1.md): **PROJECTION
> 2/3** — claude and gemini show the pre-registered within-model projection asymmetry (P endorsed
> above E under the cancelling frames); the panel-level signal carries a **conditional-antecedent
> collapse** (the antecedent frame is where projection thins). The line then ran the trigger
> inventory (s160), the environment-gated conjecture (s162), and the doppelgänger control (s173 —
> BEATS-DOPPELGANGER but under-licensed). *(Back-annotation: the s180 log verified this mismatch;
> this box records the outcome the front-matter's `tested` already reflected.)*

## The bet

Take a base sentence carrying a **presupposition** P and a **matched ordinary entailment** E (both
true when the base is plainly asserted). Embed the base under an **entailment-cancelling** operator
— negation, a polar question, or a conditional antecedent. The semantics literature's "hallmark of
presuppositions" ([`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md),
§1.2) is that **P survives (projects)** the embedding while **E is cancelled**.

The conjecture is that a panel of current models reproduces this asymmetry **as a behavioral
contrast within each model**: it endorses P under the three cancelling frames materially **more
often** than it endorses E under the same frames — the pre-registered signal being a per-model
**projection gap** (presup-survival − entail-survival) ≥ 0.30 in a majority of the panel, with a
plain-frame sanity floor that both P and E are endorsed when the base is plainly asserted.

## What would confirm / falsify it

- **Confirm (PROJECTION):** ≥ 2/3 models pass the plain-frame sanity floor AND show
  presup-survival ≥ 0.60 with projection-gap ≥ 0.30 (thresholds frozen in
  [`PREREG.md`](../../../experiments/runs/2026-07-01-presupposition-projection/PREREG.md)).
- **Falsify (FLAT / NULL):** ≥ 2/3 models pass sanity but treat P and E alike under embedding
  (|projection-gap| < 0.15) — the presupposition leg does not project above the matched-entailment
  leg. Written as a null.
- **MIXED / control failure:** sanity fails (models will not endorse P or E even when the base is
  plainly asserted), or the panel splits — the instrument is confounded and no projection claim is
  made.

## Scope cap (load-bearing)

The measure is a **within-model** contrast (P leg vs. E leg of the *same* base), not a comparison to
human projection judgments — **no human baseline is claimed, measured, or needed**. It does not
certify that the model *represents* presupposition-vs-assertion semantically; it reads endorsement
of an inference under embedding off forced-choice answers. Any reading beyond this within-model
behavioral contrast is out of scope. The `internal-contrast-only` terminal status was **ratified**
by an independent session-159 adversarial review
([`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../decisions/resolved/presupposition-projection-internal-contrast-anchor.md)).

## How this differs from the project's existing lines

Per [`open-question/presupposition-projection-corner`](../open-questions/presupposition-projection-corner.md):
the distinguishing manipulation is **survival under an entailment-cancelling environment**, which
none of the constructional-inference probes (they read an entailment off the *plain* construction)
or the indexicality corner (context-dependent *reference*, not inference-under-embedding) exercise.
Presupposition vs. matched entailment is also exactly the contrast that keeps this distinct from a
scalar/conversational-implicature line (those cancel and do not project).
