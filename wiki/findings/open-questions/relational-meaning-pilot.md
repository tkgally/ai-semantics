---
type: open-question
id: relational-meaning-pilot
title: What minimal two-agent setup constitutes evidence for relational meaning-constitution?
meaning-senses:
  - relational
status: open
created: 2026-05-28
updated: 2026-05-29
links:
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: concept/distributional-meaning
---

# Open question: minimal two-agent setup for relational meaning

## The question

The charter's distinctive axis is `relational` meaning — meaning constituted *between* a model and a person, or between models — and notes that the existing multi-agent literature is about *coordination*, not *meaning-constitution* ([`PROJECT.md`](../../../PROJECT.md) §1). What is the smallest interactional setup whose results would count as evidence for or against meaning being constituted *between* agents, rather than computed *within* one and then aggregated?

The theory page frames this precisely as a **second ladder**: "The relational axis is not a higher rung of the same [form/meaning] ladder; it is a *second ladder* whose bottom rung is not yet defined" ([`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md), §"The under-explored axis"). This page's job is to define that bottom rung — to name the *minimal* design and the *one* discriminating measure that would make the second ladder start.

## Why it matters

This is plausibly the project's strongest contribution if executed well. The project's constructional conjectures (dative, AANN, *way*, function-word, caused-motion, conative, comparative-correlative) are all `model-internal` probes — they ask what a single model knows. None touches the relational axis. Without a pilot here, the relational angle remains rhetoric, and the theory page's "standing IOU" stays unpaid.

## The hard part, named exactly

The page that this sharpens already named the difficulty: operationally distinguishing **"meaning constituted BETWEEN agents"** from **"meaning computed in each, then averaged."** Two agents that each independently compute the same convention from the same evidence would *look* coordinated without anything being constituted between them. A serious pilot has to make those two stories come apart in a measurement.

The proposed discriminator is **trajectory-dependence**. If a coined convention is genuinely constituted in the interaction, then agent B's interpretation/usage of the coined term should depend on the *ordered history* of the exchange — the particular sequence of repairs, partial acceptances, and refinements that produced it — and not merely on the *set* of utterances that happened to occur. If instead each agent is computing a convention from a bag of evidence, then presenting the same utterances in a scrambled order (or as static context) should yield the same convergence. Order-sensitivity that survives content-matching is the signature of a convention built *between*, not *within*.

## What a serious answer would look like — a concrete minimal pilot

### Task: iterated dyadic reference game

Two LLM agents (A = director, B = matcher) play an iterated referential-communication game over a small set of **hard-to-name novel referents** — e.g. abstract tangram-like figures, or nonce objects with no conventional lexical label. Per round: A sees the target plus distractors and produces a referring expression; B picks a figure from its own (independently ordered) array; both get feedback (hit/miss); roles may swap. Over rounds, human dyads in this paradigm coin and compress a shared label (Krauss & Weinheimer 1964/1966; Clark & Wilkes-Gibbs 1986). The question is whether LLM dyads do something that is relational rather than merely convergent.

Keep it deliberately small: ~6–12 figures, ~6 rounds per dyad, a handful of dyads per condition. The relational case multiplies API calls (every round is a fresh generation conditioned on growing history, for *both* agents) — this is the budget concern the prior page flagged, and it is the reason this stays a pilot.

### Conditions (the discriminator lives here)

1. **Live dialogue (relational candidate).** A and B interact turn-by-turn with real feedback; each conditions on the actual interaction history as it accrues. This is the only condition where a convention could be constituted *between*.
2. **Shuffled-history replay (the "averaged-within" control).** Take the exact set of prior utterances produced in a live dialogue, present them to a fresh B as *order-scrambled* static context (a bag of past turns, not a trajectory), then probe B's interpretation/usage of the coined term. Content is held identical to condition 1; only the ordering/interactional structure is destroyed.
3. **Single-agent-with-self (the within-agent baseline).** One agent plays both roles, or refers repeatedly to the figures alone. This isolates how much label-compression happens with no second party at all — convention as a purely intra-agent regularity.
4. *(Optional perturbation arm)* **History-perturbation.** Replay a live dialogue to a fresh B but alter one earlier turn of A's history (e.g. swap which figure a coined term was first attached to). If B's later interpretation shifts in proportion to *where* in the trajectory the perturbation lands — not just whether the altered content is present — that is sharper trajectory-dependence evidence than the shuffle alone.

### Dependent measures

- **Referential-success rate** over rounds (hit rate; the basic coordination signal — necessary but not sufficient).
- **Lexical convergence / entrainment**: reduction in expression length and increase in shared-token overlap across rounds (the standard tangram-conventionalization curve).
- **Trajectory-dependence (the load-bearing measure)**: the *difference* in B's interpretation/usage of the coined term between live dialogue (cond. 1) and shuffled-history replay (cond. 2), with content held constant. A live-vs-shuffled gap is the operational signature of "constituted between."
- **Perturbation sensitivity** (optional arm): whether B's interpretation tracks *which ordered turn* was altered, beyond tracking that the content was altered.

### What positive vs. null would license

- **Positive** (live ≠ shuffled; interpretation depends on ordered history; perturbation effects are position-sensitive): evidence that the convention is **trajectory-dependent**, i.e. constituted in the interaction rather than recomputed from a content bag. This would define the bottom rung of the relational ladder and license a `conjecture` page.
- **Null** (live ≈ shuffled; convergence is fully explained by the *set* of prior utterances regardless of order; single-agent baseline already compresses labels): a first-class negative. It would say the observed "coordination" is **computed within each agent and aggregated** — a relational *deflation*, the relational analogue of "a distributional pass is not a constructional pass." Per the charter's first-class-negatives commitment, this is written, not retuned.

## Tie to the meaning-senses vocabulary

This pilot is tagged `relational` ([`meaning-senses.md`](../../meaning-senses.md): "Meaning constituted between a model and a person, or between models … the multi-agent literature is about coordination, not meaning-constitution"). The whole design exists to operationalize that "constituted between" clause rather than assume it.

The crucial discipline is the **relational analogue of the distributional null** that runs through the constructional pages ([`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md); the theory page's Open Tension 1, "distributional null vs. constructional signal"). Here the deflationary alternative is **lexical entrainment that is fully distributional**: two agents drifting toward a shared label simply because each is a next-token predictor conditioned on overlapping recent context would produce convergence *and* would survive order-scrambling, because what drives it is the co-occurrence content, not the interactional trajectory. So:

- `relational` meaning-constitution requires a *surplus* over distributional convergence — the live-vs-shuffled gap is exactly that surplus.
- Mere lexical entrainment (length compression, token overlap) is **not** sufficient evidence for the `relational` tag; it is explainable by `distributional` structure alone and would equally appear in the shuffled control.
- The pilot is therefore designed so that the headline coordination measures (success rate, entrainment curve) are *expected even under the deflationary story*, and only the trajectory-dependence contrast separates `relational` from `distributional`.

This keeps the relational ladder honest in the same way the form/meaning ladder is: the eye-catching convergence is the floor, and the discriminating contrast is the only thing that climbs.

## Human anchor

Per always-on rule 5 and the charter's independent-human-bearing commitment, a relational claim needs a human-generated dyadic-interaction resource. Candidate anchors (well-known psycholinguistics; **none are in-repo** — each would have to be fetched, and none is cited here with a page number or quote):

- **Clark & Wilkes-Gibbs 1986** — referential-communication / tangram-naming convergence; the canonical demonstration that dyads collaboratively coin and compress shared labels over rounds. The closest human analogue to the iterated reference game above.
- **Krauss & Weinheimer 1964/1966** — earlier reference-phrase-shortening studies; the convergence curve the entrainment measure would be calibrated against.
- **HCRC Map Task corpus** — task-oriented dialogue with referential alignment; a corpus-grade anchor for entrainment in goal-directed dyads.
- **Pickering & Garrod 2004** — the "interactive alignment" framework; the most-cited dyadic-linguistic model, useful as the *theoretical* anchor for what alignment-across-levels predicts (and what it does **not** claim about meaning-constitution).

**Anchor RATIFIED 2026-05-29** ([`decisions/resolved/relational-anchor-shortlist`](../../decisions/resolved/relational-anchor-shortlist.md), Option A): the empirical anchor is **Clark & Wilkes-Gibbs 1986** (the tangram referential-communication paradigm the pilot directly instantiates; supplies the human convergence/compression baseline), with **Pickering & Garrod 2004** (interactive-alignment) as theoretical backdrop only. This fixes the *anchor* — it does **not** make the pilot runnable: both papers are queued in [`base/wanted.md`](../../base/wanted.md) and are **not yet in-repo**, so no relational result can be promoted until Clark & Wilkes-Gibbs 1986 is fetched and read. A separate **literature-reading gate** (multi-agent-LLM + alignment, below) remains before the pilot promotes to a runnable design, and the broader two-AI experiment ("Decision 9") is still not taken.

## Why this is queued, not active

This still needs reading first, so that "minimal" is honest:

- The **lexical-alignment / Pickering & Garrod** line, to confirm the trajectory-dependence discriminator is not already a solved or trivial prediction in the human case.
- The **multi-agent LLM** literature (CAMEL, communicative-agents, debate/negotiation setups), to confirm the iterated-reference-game-with-shuffle-control is not already run — and, where it overlaps, to read it against a meaning-constitution lens it was not designed for.

Sharpening the question — fixing the task, the conditions, the discriminating measure, and the deflationary null — is the deliverable here. **Resolving** it (promoting to a `conjecture`/design) is the next-loop step and is gated on the reading above and on a fetched anchor.

## Pointers for the next visit

- **Anchor decision RESOLVED 2026-05-29** ([`decisions/resolved/relational-anchor-shortlist`](../../decisions/resolved/relational-anchor-shortlist.md), Option A: Clark & Wilkes-Gibbs 1986 + Pickering & Garrod 2004 backdrop). Next concrete step: **fetch Clark & Wilkes-Gibbs 1986** (queued in [`base/wanted.md`](../../base/wanted.md)) so the human convergence baseline is in-repo.
- Pickering & Garrod "interactive alignment" as the theoretical anchor — check open-access availability when fetched.
- The MultiAgent-LLM literature as the corpus to *not* duplicate; read for whether any setup already includes an order-scramble or static-history control (the load-bearing control here).
- On a positive result, the natural promotion is a `conjecture` page that the theory page would absorb as the bottom rung of its relational second ladder.
