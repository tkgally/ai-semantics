---
id: lexical-sense-gradience-operationalization
title: How is the lexical-sense-gradience probe operationalized (instrument, polysemy/homonymy stratification source, context-similarity control, synchronic filter)?
status: open
opened: 2026-05-30
opened-by: orchestrator
contingent-artifacts:
  - design/lexical-sense-gradience-v1
---

# Decision: lexical-sense-gradience probe operationalization

## Why this exists

The **anchor direction** for [`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md) is already settled — [`decisions/resolved/lexical-sense-gradience-anchor`](../resolved/lexical-sense-gradience-anchor.md) ratified Option B (a graded set, not Usim), and DWUG was independently verified 2026-05-30 ([`resource/dwug-usage-graphs`](../../base/resources/dwug-usage-graphs.md), VERDICT: YES-WITH-CAVEATS). But [`design/lexical-sense-gradience-v1`](../../../experiments/designs/lexical-sense-gradience-v1.md) still has **operationalization choices** that are not fixed. The conjecture's own Notes flag this: *"Instrument is an operationalization gate … pick and freeze the instrument before seeing results … Queue this gate before running."* Choosing these after seeing a gradience-or-collapse pattern is the canonical retuning trap (charter §8). **No lexical probe runs until this is ratified.** This is surfacing, not a resolution — the orchestrator does not auto-resolve.

## The live choices (see design §3–§5)

1. **Instrument (Q1).** Behavioral panel (prompt the 3-family panel for a graded same/different-sense rating + confidence on the two usage sentences; logprob-free, runs now) vs the small-model representation-similarity lane (cosine of the target word's contextual vectors; the cleaner `distributional` instrument but needs **local compute**, the same blocker as AANN) — or commit to **both** as separate pre-registered instruments.
2. **Polysemy / homonymy stratification source (Q2).** WordNet-based (unrelated coarse roots / distinct homographs = homonymy; related senses = polysemy) vs dictionary-based (separate headwords = homonymy, numbered senses = polysemy) vs a manual expert tag of the 40 DWUG EN lemmas. DWUG does **not** carry this split; prediction 2 needs it added and frozen.
3. **Context-similarity control measure (Q3).** Lexical overlap (Jaccard / token-F1 minus the target), sentence-embedding cosine, or both — computed independently of the model's sense signal, then partialled out. This is the design's spine (clause c).
4. **Synchronic filter (Q4).** Within-period pairs only (clean synchronic anchor) vs include cross-period pairs with the period gap as a covariate. DWUG mixes two CCOHA periods.

## Provisional default (in force until Tom ratifies — NOT acted on; the probe stays unrun)

1. **Q1 → behavioral panel**, small-model lane deferred (it needs local compute, held the same way AANN is). Rationale: every prior probe is behavioral; this keeps the lexical wedge runnable now and comparable to the constructional findings. Re-add the representation lane when local compute lands.
2. **Q2 → WordNet-based stratification**, frozen with the item set and stored separately from the raw DWUG files (CC BY-ND forbids distributing a modified DWUG). Manual expert tags of the 40 lemmas are an acceptable supplement if WordNet relatedness is ambiguous, but must be pre-registered.
3. **Q3 → both** lexical overlap *and* sentence-embedding cosine, reported separately; the partial correlation controls for each.
4. **Q4 → within-period pairs only** for the synchronic gradience anchor; a cross-period arm may be reported descriptively but is not the primary test.

## Notes for the resolver

Tom: a one-line ratification or amendment fixes the yardstick. The point of this gate is only to stop the next run from tuning the instrument/stratification/control to whatever turns a collapse into gradience or vice versa. Not urgent — the lexical probe is a new axis, not a follow-up to a pending result. If you'd rather not pursue it yet (e.g. wait for the small-model lane / local compute so the cleaner `distributional` instrument is available), say so and the design stays parked. The DWUG anchor itself is verified and ready either way.
