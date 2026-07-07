---
type: source
id: gurnee-2026-verbalizable-workspace
title: "Verbalizable Representations Form a Global Workspace in Language Models"
authors:
  - Gurnee, Wes
  - Sofroniew, Nicholas
  - Pearce, Adam
  - Piotrowski, Mateusz
  - Kauvar, Isaac
  - Chen, Runjin
  - Soligo, Anna
  - Bogdan, Paul
  - Ong, Euan
  - Wang, Rowan
  - Thompson, Ben
  - Abrahams, David
  - Kantamneni, Subhash
  - Ameisen, Emmanuel
  - Batson, Joshua
  - Lindsey, Jack
year: 2026
venue: "Transformer Circuits Thread (transformer-circuits.pub), Anthropic; published 2026-07-06. Not peer-reviewed."
url: https://transformer-circuits.pub/2026/workspace/index.html
access: open-access
meaning-senses:
  - model-internal
  - inferential
status: received
created: 2026-07-07
updated: 2026-07-07
links:
  - rel: refines
    target: concept/inferential-meaning
  - rel: refines
    target: concept/distributional-meaning
  - rel: supports
    target: claim/output-channel-working-surface
---

# Gurnee et al. 2026 — Verbalizable Representations Form a Global Workspace in Language Models

> **Cataloguing note (session 190, 2026-07-07).** Added at Tom's standing-override request: record this
> newly released Anthropic interpretability paper, its findings, and its theoretical touchstones, and
> flag the topics it raises for the project to consider moving forward. This is a **source-intake page**,
> not a critical re-reading — the forward-looking questions live in
> [`open-question/verbalizable-workspace-and-llm-meaning`](../../findings/open-questions/verbalizable-workspace-and-llm-meaning.md).
> Like the other interpretability ingests, it is a **map / representational counterpoint, NOT a human
> anchor and NOT behavioral evidence about the project's findings** (see "What it cannot ground").

## What it is

A multi-author **mechanistic-interpretability** paper from Anthropic (16 authors, Wes Gurnee &
Nicholas Sofroniew co-first, Jack Lindsey corresponding), published in the Transformer Circuits Thread
on 2026-07-06. It argues that a modern language model maintains **a privileged subset of internal
representations — available for report, modulation, and flexible internal reasoning — atop a much
larger volume of automatic processing**, and draws a functional analogy to the neuroscientific
**global workspace** account of conscious access. The authors introduce a new interpretability
technique, the **Jacobian lens (J-lens)**, to surface these "verbalizable" representations (which they
call the **J-space**), and run a battery of intervention experiments (report, directed modulation,
multi-step reasoning, ablation) to test five workspace-like properties. The flagship experiments are on
Anthropic's own production model, **Claude Sonnet 4.5**.

This is a **representational / model-internal** study — the same genre as the in-repo
mechanistic-interpretability sources ([`source/diera-2026-encode-semantic-relations`](diera-2026-encode-semantic-relations.md),
[`source/beckmann-queloz-2025-mechanistic-indicators`](beckmann-queloz-2025-mechanistic-indicators.md),
[`source/milliere-buckner-2024-philosophical-intro-ii`](milliere-buckner-2024-philosophical-intro-ii.md)).
The project's own evidence is strictly **behavioral** and repeatedly disclaims representational/mechanistic
reach; this page is therefore catalogued as a **map and interpretability-side counterpoint**, **not** as a
method the project uses, **not** as evidence about the project's behavioral findings, and **not** as a human
anchor (see "What it cannot ground").

## Provenance

Title, the full 16-author list, affiliation (Anthropic), the publication line ("Published July 6, 2026"),
and correspondence (Jack Lindsey) were read from the article's own HTML masthead. The article body was
fetched as raw HTML from the paper URL on 2026-07-07 (session 190) and **every quote below was verified
character-for-character against the tag-stripped plain text** of that fetch. Two honesty flags on the
provenance:

- **No figure/section-number locators.** In the statically-served HTML the article's cross-references
  render as unresolved `??` placeholders, so figure and numbered-section references are **not** recoverable;
  locators below are the document's own **top-level section names** (from its navigation:
  *Introduction · Methods · A Global Workspace Structure Supports Function · Alignment Auditing ·
  The Assistant's Perspective · Counterfactual Reflection · Training · Discussion*), never figure numbers.
- **No extractable reference list.** The bibliography did not survive extraction from the static HTML; the
  "theoretical touchstones" section below reports only prior work the **body text itself names** (global
  workspace theory; the logit lens and tuned lens; model introspection) — no citation is reconstructed or
  invented. In particular the popularly-associated names for global workspace theory are **not** asserted:
  "Baars" does **not** appear in the fetched text, and "Dehaene" appears **only in the acknowledgments**
  (a list of thanked commenters incl. Chalmers, Dehaene, Shanahan), not as a load-bearing citation.

Typographic apostrophes are curly (`’`) as in the source; in-text citation placeholders were stripped
where they interrupted a quoted sentence (noted at the one place it matters).

## Core claim and the five workspace properties

The paper opens (Introduction):

> "If the mind is an ocean, we spend our lives floating at the surface. Beneath us, an enormous amount of
> processing takes place without our knowledge"

and states its method and aim:

> "We identify these representations using a new interpretability technique, which surfaces the concepts a
> model is poised to verbalize at any point in its processing."

> "Measuring and intervening on these representations provides us a window into a model’s thought
> processes, uncovering internal reasoning and reactions that do not appear in its output."

Under the heading **"Motivation: conscious access and the global workspace"**, the authors define the
workspace by **five properties** "which mirror the properties characteristic of conscious access" (all
verbatim):

- **Verbal report.** "When the model is asked what it is thinking about, it names concepts represented in
  the workspace. Swapping one active workspace vector for another changes its answer to match."
- **Directed modulation.** "When instructed to hold a concept in mind, or perform mental calculations, the
  model is capable of activating and computing with workspace vectors, independent of its outputs."
- **Internal reasoning.** "Workspace vectors can be used to represent the value of intermediate
  computations, when the model chains inferential steps or composes plans, and intervening on them is
  sufficient to redirect the conclusion."
- **Flexible generalization.** "The same representation serves as a valid argument to many different
  downstream computations. In other words, a workspace vector lifted from one context and placed in another
  is correctly operated on by whatever function the new context supplies."
- **Selectivity.** "The workspace comprises a small subset of the total representational content of the
  model’s activations. It is required for only a fraction of the model’s behavior, and in particular is not
  involved in pervasive, routine processing like text parsing or grammatical fluency."

The load-bearing characterization of what the workspace *contains* (Introduction):

> "These representations consist of a small, evolving set of unspoken words, neither pure echoes of the
> input nor predictions of the next token, naming the concepts the model is currently reasoning with."

## The Jacobian lens (the method)

> "The Jacobian lens is a technique for inspecting the contents of the residual stream at these
> intermediate layers." … "The basic idea is to characterize an intermediate activation vector by its
> first-order causal effect on the model’s outputs, over a broad distribution of potential contexts."

Positioned against the prior interpretability tool it refines (citation placeholder stripped at the
period):

> "The J-lens can be understood as a principled refinement of the logit lens. While the logit lens assumes
> that representations use the same coordinates in all layers, the Jacobian lens corrects for
> representational changes that take place across layers."

## Selected findings (as the authors state them)

- The five properties are demonstrated via concept-injection, directed-modulation, and multi-step-reasoning
  interventions; **swapping** a workspace vector changes the model's report/answer, and **intervening** on a
  workspace vector is "sufficient to redirect the conclusion" of a chained inference (verbatim, above).
- **Ablation of the J-space** changes register without breaking fluency: "the ablation reduces the rate of
  experiential, sensory language and produces a more mechanical, detached register." When Sonnet 4.5 is
  asked to narrate its stream of consciousness, with the J-space ablated "the model still writes fluently"
  but in the flatter register (section "The Assistant's Perspective").
- The workspace is **selective**: it is "not involved in pervasive, routine processing like text parsing or
  grammatical fluency" (verbatim) — i.e. automatic linguistic processing proceeds beneath it.

## The theoretical touchstones it builds on (its "references")

The reference list did not survive extraction (see Provenance); the following are the prior lines the
**body text itself names**, flagged as touchstones rather than reconstructed citations:

- **Global workspace theory** — the neuroscience account of conscious access the paper's central analogy is
  drawn from. The authors **explicitly bracket** the strong reading: "we do not claim that language models
  reproduce the full architecture global workspace theory ascribes to the brain—specialized, encapsulated
  processors competing for entry to a workspace that broadcasts back to them through recurrent connections."
- **The logit lens and the tuned lens** — interpretability precursors; the J-lens is presented as "a
  principled refinement of the logit lens" that "corrects for representational changes that take place across
  layers."
- **Model introspection / self-report** — the "Verbal report" property is a mechanistic operationalization of
  a model naming its own internal contents.

## What it bears on in-repo (topics to consider — carried in the open-question)

Each connection is a **question the paper raises for the project**, not an in-repo finding it establishes.
They are stated once here and developed as live questions in
[`open-question/verbalizable-workspace-and-llm-meaning`](../../findings/open-questions/verbalizable-workspace-and-llm-meaning.md).

- **The distributional-vs-inferential seam** — [`concept/distributional-meaning`](../concepts/distributional-meaning.md),
  [`concept/inferential-meaning`](../concepts/inferential-meaning.md),
  [`open-question/distributional-vs-inferential-constructional`](../../findings/open-questions/distributional-vs-inferential-constructional.md).
  The paper's claim that intermediate content is "neither pure echoes of the input nor predictions of the
  next token, naming the concepts the model is currently reasoning with" is a **representational-side**
  statement about a layer of content beyond next-token surface statistics — the inside-the-model companion to
  the project's **behavioral** distributional-shadow test (does a meaning gradient beat a matched co-occurrence
  control?). Neither settles the other; they bear on the same seam from opposite methods.
- **The output-channel / working-surface line** — [`claim/output-channel-working-surface`](../../findings/claims/output-channel-working-surface.md),
  [`essay/output-channel-confound`](../../findings/essays/output-channel-confound.md). The **Internal
  reasoning** property ("Workspace vectors can be used to represent the value of intermediate computations …
  intervening on them is sufficient to redirect the conclusion") is a mechanistic picture of exactly the
  serial computation the project argues can proceed *beneath the forced output channel* — the "front-matter
  `supports` link" above points here for that reason. It is representational corroboration of the confound's
  premise, **not** a discharge of any behavioral verdict.
- **Introspection and the behavioral method's constitutive silences** — [`essay/undischargeable-negative`](../../findings/essays/undischargeable-negative.md),
  [`essay/reference-as-premise-bound`](../../findings/essays/reference-as-premise-bound.md). "Verbal report"
  is a representational handle on introspection that the project's purely behavioral instruments cannot reach;
  worth flagging both as a method the project deliberately does not use and as a caution that a self-report the
  project would treat skeptically may here have a claimed mechanistic correlate.
- **The situating map's model-internal locus** — [`theory/situating-llm-meaning-v2`](../../findings/theory/situating-llm-meaning-v2.md).
  The four-loci synthesis currently fills the **model-internal** cell from behavior alone; this paper is a
  strong new representational-side datapoint on that cell specifically (a candidate revision-*input*, not a
  revision).

## What it can ground

- A citation that a 2026 Anthropic interpretability paper reports, via a new "Jacobian lens" technique, a
  **privileged, verbalizable, causally-load-bearing subset of internal representations** (the "J-space") in a
  frontier model (Claude Sonnet 4.5), characterized by five workspace-like properties (verbal report,
  directed modulation, internal reasoning, flexible generalization, selectivity) — all verbatim above.
- A citation, from the representational side, that **automatic linguistic processing (text parsing,
  grammatical fluency) proceeds *beneath* this privileged subset** (the "Selectivity" property) — a
  mechanistic gloss on the project's recurring behavioral distinction between routine form-fluency and
  effortful inference.
- A representational-side **counterpoint** whenever an essay or theory page marks the inside/outside
  (mechanistic vs behavioral) distinction (cf. the framing of the Beckmann & Queloz and Diera & Scherp
  sources).

## What it cannot ground

- **Any behavioral or human-comparison claim about the project's findings.** This is a
  representational/interpretability study with **no human-judgment resource**; it is **not a human anchor** and
  must not be cited as one, nor as behavioral evidence for or against any project result.
- **Transfer to the project's frontier panel as evidence.** The results are internal-mechanism claims about
  one model family (Anthropic's own, Sonnet 4.5 named), by a novel and self-described-imperfect method; nothing
  here licenses a behavioral prediction on the [`config/models.md`](../../../config/models.md) panel.
- **A consciousness claim.** The authors themselves bracket it: "we do not claim that language models
  reproduce the full architecture global workspace theory ascribes to the brain," and the philosophical
  implications are flagged as "unclear and likely controversial." The project's subject is lexical and
  grammatical **meaning**, not consciousness — the "conscious access" analogy must **not** be imported as a
  meaning claim.
- **The reliability of the J-lens as ground truth.** By the authors' statement it is "an imperfect tool,
  which we believe only approximately and incompletely captures the model’s underlying workspace structure"
  (e.g. it "only identifies vectors associated with concepts that correspond to single tokens").

## Known limits

- **First-party, non-peer-reviewed.** Published in Anthropic's own Transformer Circuits Thread, on Anthropic's
  own models; no independent replication. Treat as a preprint-strength interpretability report, no stronger.
- **Novel, self-described-approximate method.** The J-lens is introduced here; the authors flag it as
  approximate/incomplete and single-token-concept-limited (verbatim above).
- **Provenance ceiling.** Quotes are verified against the 2026-07-07 raw-HTML fetch, but figure/section-number
  locators and the reference list are **not** recoverable from the static HTML (see Provenance); a later
  session reaching a fully-rendered version should re-pin locators and the bibliography before any heavier use.
- **Model-internal, not behavioral.** Nothing here is a behavioral probe with a human anchor; the project's
  own evidence base and this paper's do not mix.

## Status in wanted.md

Not previously listed. Catalogued 2026-07-07 (session 190) at Tom's standing-override request as a
representational/interpretability counterpoint source (the inside-the-model companion to the project's
behavioral wedge), and recorded RECEIVED in [`wanted.md`](../wanted.md).
