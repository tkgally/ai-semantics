---
type: open-question
id: relational-meaning-pilot
title: What minimal two-agent setup constitutes evidence for relational meaning-constitution?
meaning-senses:
  - relational
status: open
created: 2026-05-28
updated: 2026-05-31
links:
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: concept/relational-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Open question: minimal two-agent setup for relational meaning

> **v1 RAN (2026-05-31) → a first-class relational NULL.** The pilot below was built and run:
> [`result/relational-reference-game-v1`](../results/relational-reference-game-v1.md). Across all three
> homogeneous-dyad panels the coined convention is recovered from the **set** of prior turns, not
> their **ordered trajectory** (history content lifts a fresh matcher's accuracy, but ordered ≈
> shuffled ≈ reversed; no order-gap CI excludes 0) — coordination, not constitution; the deflationary
> distributional story survives order-scrambling. The question **stays open** because the bounded
> null leaves the sharper arms unrun: the **history-perturbation arm** (reassign a coined term
> mid-trajectory, test position-sensitivity), **image referents**, and **cross-family dyads** — see
> [`decisions/resolved/relational-pilot-operationalization`](../../decisions/resolved/relational-pilot-operationalization.md)
> (v1 yardstick ratified 2026-06-12, autonomous adversarial review).
> What follows is the design as run.

## The question

The charter's distinctive axis is [`concept/relational-meaning`](../../base/concepts/relational-meaning.md) — meaning constituted *between* a model and a person, or between models — and notes that the existing multi-agent literature is about *coordination*, not *meaning-constitution* ([`PROJECT.md`](../../../PROJECT.md) §1). What is the smallest interactional setup whose results would count as evidence for or against meaning being constituted *between* agents, rather than computed *within* one and then aggregated?

The theory page frames this precisely as a **second ladder**: "The relational axis is not a higher rung of the same [form/meaning] ladder; it is a *second ladder* whose bottom rung is not yet defined" ([`theory/constructional-meaning-in-llms`](../theory/constructional-meaning-in-llms.md), §"The under-explored axis"). This page's job is to define that bottom rung — to name the *minimal* design and the *one* discriminating measure that would make the second ladder start.

## Why it matters

This is plausibly the project's strongest contribution if executed well. The project's constructional conjectures (dative, AANN, *way*, function-word, caused-motion, conative, comparative-correlative) are all `model-internal` probes — they ask what a single model knows. None touches the relational axis. Without a pilot here, the relational angle remains rhetoric, and the theory page's "standing IOU" stays unpaid.

## The hard part, named exactly

The page that this sharpens already named the difficulty: operationally distinguishing **"meaning constituted BETWEEN agents"** from **"meaning computed in each, then averaged."** Two agents that each independently compute the same convention from the same evidence would *look* coordinated without anything being constituted between them. A serious pilot has to make those two stories come apart in a measurement.

The proposed discriminator is **trajectory-dependence**. If a coined convention is genuinely constituted in the interaction, then agent B's interpretation/usage of the coined term should depend on the *ordered history* of the exchange — the particular sequence of repairs, partial acceptances, and refinements that produced it — and not merely on the *set* of utterances that happened to occur. If instead each agent is computing a convention from a bag of evidence, then presenting the same utterances in a scrambled order (or as static context) should yield the same convergence. Order-sensitivity that survives content-matching is the signature of a convention built *between*, not *within*.

## What would COUNT as evidence — the minimal bar, made concrete

Before the pilot design, fix what the result has to clear, because "evidence that meaning is constituted between agents rather than computed inside each" is easy to claim and hard to earn. Three commitments make the bar concrete:

1. **The bottom rung is a single contrast, not a battery.** The minimal evidential unit is *one* number: the live-vs-shuffled gap in agent B's interpretation/usage of a coined term, with the *content* of the prior turns held identical and only their *ordering / interactional structure* destroyed. Everything else (success rate, entrainment curve) is scaffolding that the deflationary story predicts equally — it is reported, but it does not climb the ladder. A pilot that shows convergence and entrainment but **no** live-vs-shuffled gap has produced a relational *null*, not a relational positive, and is written as such.

2. **The comparison is against independent human data, never model agreement.** The signal that "this is what a constituted convention looks like" comes from a human convention-formation resource, not from the two LLM agents agreeing with each other (model-agreement is exactly the "computed in each, then averaged" artifact we are trying to exclude). The fetchable candidate that supplies this is the **Hawkins/Stanford tangrams repeated-reference corpus** (`hawkrobe/tangrams`; see Human anchor below): per-dyad *ordered* referring-expression histories with success and length over repetitions of the same tangram. It gives (i) a human entrainment/compression curve the LLM dyads' convergence is calibrated against, and (ii) — because it preserves ordered per-dyad histories — a human reference point for what trajectory-dependent convergence looks like. The relational claim is licensed only by a contrast that holds against this human signal, not by the agents matching one another.

3. **The deflationary null is a `distributional` story and must be beatable.** Two next-token predictors conditioned on overlapping recent context will converge and entrain *from co-occurrence content alone*, and that convergence **survives order-scrambling**. So the shuffled-history condition is not a nuisance control — it *is* the deflationary hypothesis instantiated. A live ≈ shuffled result is the relational analogue of "a distributional pass is not a constructional pass," and is a first-class negative (charter §5.4), not something to retune away.

A result counts as **bottom-rung evidence for relational meaning-constitution** iff: (a) live-dialogue interpretation/usage of the coined term differs reliably from shuffled-history replay with content held constant; (b) that gap is not reproduced by the single-agent-with-self baseline (so it is not a bare intra-agent regularity); and (c) the live-condition convergence dynamics are at least as history-shaped as the human tangrams baseline (so "convergence" is not an artifact of a trivially easy referent set). Failing (a) is a relational deflation; failing (b) or (c) means the design is under-powered or the referents too easy, not that constitution was shown.

## What a serious answer would look like — a concrete minimal pilot

### Task: iterated dyadic reference game

Two LLM agents (A = director, B = matcher) play an iterated referential-communication game over a small set of **hard-to-name novel referents** — e.g. abstract tangram-like figures, or nonce objects with no conventional lexical label. Per round: A sees the target plus distractors and produces a referring expression; B picks a figure from its own (independently ordered) array; both get feedback (hit/miss); roles may swap. Over rounds, human dyads in this paradigm coin and compress a shared label (Krauss & Weinheimer 1964/1966; Clark & Wilkes-Gibbs 1986; replicated at corpus scale by Hawkins, Frank & Goodman 2020). The question is whether LLM dyads do something that is relational rather than merely convergent.

**The agents are the project panel** — the three family-decorrelated models recorded in [`config/models.md`](../../../config/models.md) (currently `claude-sonnet-4.6` / `gpt-5.4-mini` / `gemini-3.5-flash`), used in the standard subject role. Run as **homogeneous dyads first** (same model in both roles) so that any live-vs-shuffled gap cannot be an artifact of two *different* systems with different priors talking past each other; cross-family dyads are a later arm, not the bottom rung. Cross-model divergence (does the gap appear for some families and not others?) is itself data, exactly as in the constructional probes. Note the panel's reasoning-token caveat (Gemini/DeepSeek) flagged in `config/models.md` — budget `max_tokens` accordingly, since every round is a multi-turn generation.

Keep it deliberately small: ~6–12 figures, ~6 rounds per dyad, a handful of dyads per condition. The relational case multiplies API calls (every round is a fresh generation conditioned on growing history, for *both* agents) — this is the budget concern the prior page flagged, and it is the reason this stays a pilot. Calibrate the referent difficulty and the entrainment-curve expectation against the human tangrams corpus (below) so "hard-to-name" is grounded in a paradigm where humans demonstrably take several rounds to converge, not set by guesswork.

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

**Anchor RATIFIED 2026-05-29** ([`decisions/resolved/relational-anchor-shortlist`](../../decisions/resolved/relational-anchor-shortlist.md), Option A): the empirical anchor is **Clark & Wilkes-Gibbs 1986** (the tangram referential-communication paradigm the pilot directly instantiates; supplies the human convergence/compression baseline), with **Pickering & Garrod 2004** (interactive-alignment) as theoretical backdrop only. This fixes the *anchor* — it does **not** make the pilot runnable: both papers are queued in [`base/wanted.md`](../../base/wanted.md) and are **not yet in-repo**, so no relational result can be promoted until Clark & Wilkes-Gibbs 1986 is fetched and read. The broader two-AI experiment ("Decision 9") was **GREEN-LIT by Tom on 2026-05-31** (see [`decisions/resolved/relational-pilot-go`](../../decisions/resolved/relational-pilot-go.md)): the pilot is to be built and run.

**A fetchable, machine-readable human baseline now exists (2026-05-31 scouting).** Because Clark & Wilkes-Gibbs 1986 is unfetchable for several days, a scouting pass (see [`relational-axis-literature.md`](../../../experiments/notes/relational-axis-literature.md)) verified that the **Hawkins/Stanford tangrams repeated-reference corpus** — the modern, *released* replication of the very C&W-G paradigm (Hawkins, Frank & Goodman 2020, *Cognitive Science* 44(6):e12845; "We release an open corpus (>15,000 utterances) of extended dyadic interactions") — is publicly fetchable (`hawkrobe/tangrams`, `data/tangrams.csv`, HTTP 200, 3.1 MB) and carries **ordered per-dyad referring-expression histories** with role, success (`correct`), repetition number, and utterance length. This supplies, *in-repo and machine-readable*, the human entrainment/compression curve and an ordered-history reference point the pilot's measures calibrate against — exactly the signal the ratified C&W-G anchor names, but in a form that can be joined now. **Caveat:** the repo declares no SPDX license (authorial "we release an open corpus" statement only); reading/comparing against it is within research norms, but redistribution terms are unspecified — this should be surfaced as a decision before the corpus is committed as a typed `resource`. The Hawkins corpus would *supplement*, not replace, C&W-G as the ratified theoretical reference; it does not itself run the live-vs-shuffled control (novel to the LLM probe), so it anchors the *human convergence baseline*, not the trajectory-dependence measure.

**The literature-reading gate is now substantially discharged** (see [`relational-axis-literature.md`](../../../experiments/notes/relational-axis-literature.md) for verbatim provenance). The reads confirm the discriminator is not already solved/trivial in the human case and not already run in the LLM case:
- **Interactive alignment (Pickering & Garrod 2004)** frames alignment as "a largely automatic process" of cross-level priming — i.e. coordination, *not* a meaning-constitution claim. This is the deflationary backdrop, not a competitor: alignment predicts convergence/entrainment without trajectory-dependence.
- **Conceptual pacts (Brennan & Clark 1996)** is the human result that most directly *motivates* the discriminator: lexical entrainment has a **historical** (not merely ahistorical/salience-driven) and **partner-specific** component — the human-side analogue of "live ≠ shuffled." Strong candidate to add to [`base/wanted.md`](../../base/wanted.md) alongside C&W-G.
- **Emergent-communication (Lazaridou et al. 2017)** and **multi-agent-LLM convention work (Ashery, Aiello & Baronchelli 2025, *Science Advances* — naming-game convention emergence in LLM populations)** are the prior art the pilot must position *against*: both report convergence/convention emergence with **no order-scramble or trajectory-dependence control**, and both are human-free. They are foils that demonstrate the gap the live-vs-shuffled contrast fills, not anchors (a relational claim cannot be anchored on model-agreement).

## Why this is queued, not active

The **literature-reading gate is now substantially discharged** (2026-05-31; verbatim provenance in [`relational-axis-literature.md`](../../../experiments/notes/relational-axis-literature.md)):

- The **lexical-alignment / Pickering & Garrod / Brennan & Clark** line was read: the trajectory-dependence discriminator is *not* trivial in the human case — interactive alignment is a coordination/priming mechanism silent on constitution, while conceptual pacts give positive human evidence that entrainment is history- and partner-specific (the "live ≠ shuffled" prediction is non-vacuous).
- The **emergent-communication / multi-agent-LLM** line (Lazaridou et al.; Ashery et al. 2025) was read: convention emergence in agent populations is reported, but the iterated-reference-game-**with-shuffle-control** is *not* among the surveyed setups — no order-scramble / static-history / trajectory-dependence control appears. The pilot is not a duplicate; it adds the one control these results lack.

What remains gating: a **fetched primary anchor**. C&W-G 1986 is still not in-repo (unfetchable for days); the scouted Hawkins tangrams corpus is fetchable now and can supply the human convergence baseline as a typed `resource` **once a license decision is taken** (no SPDX in the repo). Sharpening the question — task, conditions, discriminating measure, deflationary null, the evidential bar, the panel-as-agents — is the deliverable, now done. **Resolving** it (promoting to a `conjecture`/runnable design) is now the next-loop build and is **no longer gated**: the Hawkins-corpus license/anchor question was resolved 2026-05-31 (the human convergence baseline is in-repo), and Tom **GREEN-LIT Decision 9 on 2026-05-31** ([`decisions/resolved/relational-pilot-go`](../../decisions/resolved/relational-pilot-go.md)). The next session builds + runs the pilot; fetching Clark & Wilkes-Gibbs 1986 for the fuller theoretical anchor is optional, not blocking.

## Pointers for the next visit

- **Anchor decision RESOLVED 2026-05-29** ([`decisions/resolved/relational-anchor-shortlist`](../../decisions/resolved/relational-anchor-shortlist.md), Option A: Clark & Wilkes-Gibbs 1986 + Pickering & Garrod 2004 backdrop). Decision 9 (two-AI pilot) is **GREEN-LIT (2026-05-31)** — build + run the pilot next. Fetching **Clark & Wilkes-Gibbs 1986** (queued in [`base/wanted.md`](../../base/wanted.md)) for the fuller theoretical anchor is optional, not blocking (Hawkins supplies the in-repo convergence baseline).
- **Faster unblock:** the **Hawkins/Stanford tangrams corpus** (`hawkrobe/tangrams/data/tangrams.csv`) is fetchable now and is the modern released instance of the C&W-G paradigm with ordered per-dyad histories — pending a license-usage decision (RECOMMENDED id `relational-fetchable-anchor`), it could become the in-repo human baseline without waiting for the C&W-G fetch. Consider also adding **Brennan & Clark 1996** to `wanted.md` (the conceptual-pacts result motivating the discriminator).
- The emergent-communication / multi-agent-LLM literature is the prior art to position *against*, not duplicate; the Ashery et al. 2025 *Science Advances* naming-game result is the clearest example of convergence reported without a constitution test.
- On a positive result, the natural promotion is a `conjecture` page that the theory page would absorb as the bottom rung of its relational second ladder.
