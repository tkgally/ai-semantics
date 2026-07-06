---
type: open-question
id: presupposition-projection-corner
title: "Does an LLM treat presupposition as projecting — surviving negation/questions/conditionals — the way the semantics literature documents?"
meaning-senses:
  - inferential
  - distributional
status: open
contingent-on: []
created: 2026-07-01
updated: 2026-07-05
links:
  - rel: refines
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Open question: does an LLM treat presupposition as projecting?

> **Update (2026-07-01, session 158): the probe branch is RUN.**
> [`result/presupposition-projection-v1`](../results/presupposition-projection-v1.md) built, froze,
> and ran the minimal-pair projection probe this page sketched (pre-run critic GO; post-run verifier
> REPRODUCED). **Verdict PROJECTION (2/3 models)** — within claude and gemini the presupposition
> survives negation/question embedding far more than a matched entailment; gpt is directional but
> below the survival floor. **The load-bearing nuance:** projection **collapses under the conditional
> antecedent for all three models**, exactly where this page warned projection is "graded, not
> survives-everything" (§1.3). The corner **stays open** — the anchor decision was **ratified**
> session 159 (ADOPT A, `internal-contrast-only`;
> [`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../decisions/resolved/presupposition-projection-internal-contrast-anchor.md)),
> and the conditional-collapse asymmetry is worked by the session-159 rescue follow-up.

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The corner kept moving after the box
> above. Session 160 widened the probe to more trigger families
> ([`result/projection-trigger-inventory-v1`](../results/projection-trigger-inventory-v1.md), verdict
> MIXED — the asymmetry generalizes in direction to four more families, clears the pre-registered bar
> for 1/3 models, and the conditional-frame collapse replicates on the new triggers; session 161
> added its family decomposition,
> [`note/projection-trigger-inventory-family-decomposition-v1`](../notes/projection-trigger-inventory-family-decomposition-v1.md)).
> Session 162 raised the bridging conjecture
> [`conjecture/presupposition-environment-gated-both-directions`](../conjectures/presupposition-environment-gated-both-directions.md)
> (projection frame-gated, accommodation context-gated — one environment-gated signature). And the
> session-173 matched surface-cue control
> ([`result/presupposition-doppelganger-control-v1`](../results/presupposition-doppelganger-control-v1.md))
> returned **BEATS-DOPPELGANGER** (pooled +0.78 / +0.47 / +0.94, 3/3) but is read as
> **under-licensed** — the residual is trigger word-form-keyed and surface-cue-reconstructable.
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

> **Why this page exists (a $0 scoping artifact).** The project has just consolidated the
> indexicality / deixis corner. It has **not** worked **presupposition** — a distinct
> grammatical-meaning corner with a clean, canonical behavioral angle: **projection**. This page
> *opens* that corner. It states the phenomenon (grounded in the SEP source just ingested), names
> the one concrete, non-forced angle (projection through entailment-cancelling environments),
> sketches — **does not run** — a minimal-pair probe, says exactly how the corner differs from the
> project's existing lines, and flags its human anchor as `pending`. It **opens no probe, freezes no
> operationalization, ratifies nothing, opens no `wiki/decisions/open/` entry, and spends nothing.**

## The corner

**Presupposition** is a fresh grammatical-meaning corner. Following the SEP survey just ingested
([`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md)),
it is "the phenomenon whereby speakers mark linguistically information as being taken for granted,
rather than being part of the main propositional content of a speech act" (§1.1), carried by a large,
well-catalogued inventory of **triggers**: factive verbs ("Berlusconi knows that he is signing the
end of Berlusconism" → "Berlusconi is signing the end of Berlusconism"), aspectual / change-of-state
verbs ("stop, continue" — "China has stopped stockpiling metals" → "China used to stockpile metals"),
cleft sentences ("It was Jesus who set me free" → "Somebody set me free"), definite descriptions,
and others (§1.1). What distinguishes a presupposition from an ordinary entailment is its behavior
under embedding — the subject of the next section.

## The concrete, citable angle: projection

The angle that makes this corner non-forced is **projection**, the source's own "hallmark of
presuppositions" (§1.2). The diagnostic is *survival under embedding*. When a base sentence is
embedded under an entailment-cancelling operator — negation, a conditional antecedent, a question,
or a modal — its **ordinary entailments drop** but its **presupposition survives**. The source states
the contrast directly, given base sentence (2) "It's the knave that stole the tarts", its
presuppositions (3), and its ordinary entailments (4):

> "In all these examples, sentence (2) is embedded under various operators. What is notable is that
> whereas the statements in (4) do not follow from any of these embeddings (and would not be expected
> to follow according to classical logics), the presuppositions do follow. We say that the
> presuppositions are _projected_." ([`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md), §1.2)

The embedding operators the source enumerates for this contrast are, in its own labels, "(_negation_)",
"(_antecedent of a conditional_)", "(_question_)", "(_possibility modal_)", and "(_belief operator_)"
(§1.2, example set (5)). Negation is the canonical probe ("hence the term "negation test""), but the
source is explicit that one should "try several types of embedding" because projection is *defeasible*
— "Presuppositions typically project, but often do not" (§1.3). That defeasibility is a feature to
respect, not smooth over: the human pattern itself is graded, so any probe must treat "survives more
than a matched entailment does" as the signature, not "survives everything."

### The behavioral signature to look for (probe sketched, NOT run)

A minimal-pair, forced-choice / inference probe. For each item, take a presupposition trigger and a
**matched ordinary entailment** on the *same* base sentence, then embed the base under each of the
plain / negation / question / conditional-antecedent frames, and ask, at each frame, whether the target
inference still holds. The signature of projection: the **presupposition inference persists** under
negation / question / conditional while the **matched entailment is cancelled**.

Two project-authored, illustrative item schemas (not frozen; illustrative only):

1. **Factive trigger.** Base: "Sam realized that the door was locked." Presupposition: *the door was
   locked* (backgrounded by the factive). Matched ordinary entailment: *Sam came to know the door was
   locked* (an assertion-level consequence). Family:
   - plain — "Sam realized that the door was locked."
   - negation — "Sam didn't realize that the door was locked."
   - question — "Did Sam realize that the door was locked?"
   - conditional antecedent — "If Sam realized that the door was locked, he left."
   Look for: *the door was locked* endorsed across all four; *Sam came to know …* endorsed only in the
   plain frame.

2. **Change-of-state / aspectual trigger.** Base: "Dana stopped smoking." Presupposition: *Dana used
   to smoke*. Matched ordinary entailment: *Dana is not smoking now*. Family: plain / "Dana didn't stop
   smoking." / "Did Dana stop smoking?" / "If Dana stopped smoking, she'll feel better." Look for:
   *Dana used to smoke* surviving negation/question/conditional; *Dana is not smoking now* not
   surviving them.

A model that endorses the presupposition across the entailment-cancelling frames while dropping the
matched entailment is exhibiting a **projection** signature; one that treats the two identically (both
survive, or both drop) is not. Which way current decoders go is the open question — asked, not asserted.

## How this differs from existing lines (so the corner is genuinely fresh)

The distinguishing property is precisely *survival under an entailment-cancelling environment*, which
none of the project's existing probes isolate:

- **Distinct from the constructional-inference line** (*way* / caused-motion / conative / comparative-
  correlative / AANN, catalogued at [`concept/inferential-meaning`](../../base/concepts/inferential-meaning.md)).
  Those probes test whether a construction *contributes an entailment* — e.g. whether *whistled her way
  down the hall* entails motion. That is an inference read off the **plain, unembedded** construction.
  Presupposition's diagnostic is the opposite manipulation: hold the inference fixed and vary the
  **embedding**, asking whether it *survives negation/question/conditional* where a truth-conditional
  entailment would be cancelled. No constructional probe in the repo embeds its target under
  entailment-cancelling operators to test survival, so this is not a relabel of the constructional line.
- **Distinct from any implicature / pragmatics line.** Scalar or conversational implicatures are
  cancellable and do not project the way presuppositions do; conflating the two is exactly the error the
  projection diagnostic is designed to prevent. This corner isolates *projection*, the presupposition-
  specific signature.
- **Distinct from the indexicality / deixis corner** just consolidated: that corner is about
  context-dependent *reference* (character/content), not about inferences surviving embedding.

So the corner adds a manipulation axis — *embedding under entailment-cancellers* — that the existing
constructional and lexical lines do not exercise.

## Human-anchor status: `pending`

There is **no in-repo resource** for human presupposition / projection judgments. This page makes no
empirical claim about LLMs (it proposes a probe, asserts nothing), so it carries no `anchors:` link; but
the anchor gap is stated plainly. A real probe would need **one** of:

- an externally-released human presupposition / projection judgment set (e.g. a human-annotated
  projection or "projectivity" dataset) — **none is in-repo**, and none is invented here; or
- a within-model, **`internal-contrast-only`** contrast between the *projecting trigger* leg and the
  *matched non-projecting entailment* leg — a within-model behavioral contrast making no human-comparison
  claim, the terminal status most of the project's behavioral results already carry.

This page **opens no `wiki/decisions/open/` entry**; it only flags that a future probe would have to
choose one of those two paths and, if it takes the human-comparison path, open the anchor question then.

The provisional forward bet a *future* conjecture might make — clearly **not-yet-a-conjecture**, stated
in one sentence and freezing nothing — is that a panel of current models tracks projection above a
matched-entailment baseline (presupposition survives entailment-cancelling embedding more than the
matched entailment does) in a majority of panel models; this page neither designs nor commits to that
bet.

## What would move this off "open"

The corner advances in a *later* session when either (a) a frozen, pre-registered minimal-pair
projection probe is designed (measure, trigger inventory, embedding frames, and adjudication threshold
fixed, and an independent pre-run critic passed) and run under the budget discipline; or (b) an in-repo
human projection-judgment resource is located or a within-model `internal-contrast-only` contrast is
ratified as the probe's terminal status. Until then the page stays **open**, seeding a future wave and
committing nothing.

## Status: open (scoping only)

This page runs nothing, freezes no operationalization, opens no spend, opens no `decisions/` entry, and
ratifies nothing. It opens the presupposition / projection corner by stating the phenomenon (grounded in
the newly-ingested SEP source), naming the one concrete behavioral angle (projection), sketching one
illustrative probe, distinguishing the corner from the project's existing constructional and lexical
lines, and flagging its human anchor as `pending`.
