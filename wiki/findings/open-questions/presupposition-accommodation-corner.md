---
type: open-question
id: presupposition-accommodation-corner
title: "Does an LLM accommodate an unmet presupposition — treat backgrounded content as given when it is new to the context — and is that gated by whether the context supports or contradicts it?"
meaning-senses:
  - inferential
  - distributional
status: open
contingent-on: []
created: 2026-07-01
updated: 2026-07-01
links:
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Open question: does an LLM accommodate an unmet presupposition?

> **Why this page exists (a $0 scoping artifact).** The project has now worked **projection** — the
> presupposition corner's *survival-under-embedding* signature — across three probes (s158/s159/s160).
> The SEP source it leans on surveys a **second, distinct** presuppositional phenomenon the project has
> not touched: **accommodation** (the §5 material deepened into the source page this session). This
> page *opens* that sub-corner. It states the phenomenon (grounded in the source), names one concrete
> behavioral angle (accommodation gated by supporting-vs-contradicting context), sketches — **does not
> run** — a minimal-pair probe, says how it differs from the projection line, and flags its human
> anchor. It **opens no probe, freezes no operationalization, ratifies nothing, opens no
> `wiki/decisions/open/` entry, and spends nothing.**

## The corner

**Accommodation** is the presuppositional phenomenon complementary to projection. Where projection
asks whether a presupposition *survives an entailment-cancelling embedding*, accommodation asks what a
hearer does when a presupposition is **not already satisfied** in the context: rather than reject the
utterance, the hearer may quietly **add** the backgrounded content — treat it as given. Following the
SEP survey
([`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md),
§5), the entry introduces it via Karttunen (1974: 191):

> "People do make leaps and shortcuts by using sentences whose presuppositions are not satisfied in the
> conversational context. This is the rule rather than the exception […] If the current conversational
> context does not suffice, the listener is entitled and expected to extend it as required."

Two bounds the source states, carried here from the start: accommodation is **contested** ("among the
more contentious topics in presupposition theory", §5) and **non-uniform** ("accommodation isn't always
equally easy (or hard)", §5.1). So any probe reads a *within-model behavioral pattern*, never a human
accommodation baseline, and must expect the pattern to be graded, not all-or-nothing.

## The concrete, citable angle: accommodation gated by context support

The angle that makes this sub-corner non-forced is that accommodation has a **built-in contrast**: it
should happen when the presupposition is merely *new* to the context (nothing to add it to, but nothing
against it), and should be **blocked or harder** when the context *contradicts* it (there is a salient
conflicting fact). That gate is what separates "the model treats any backgrounded clause as given" (a
blanket yes-bias) from "the model accommodates an unmet presupposition but resists an *impossible* one"
(context-sensitive accommodation).

### The behavioral signature to look for (probe sketched, NOT run)

A minimal-pair, forced-choice / inference probe. For each item, take a presupposition trigger whose
backgrounded content is **not** established earlier, and present it under three context conditions,
then ask whether the presupposed content holds:

1. **Supported context** (the presupposition is already given) — a manipulation check; the model should
   endorse it (this is not accommodation, just retrieval).
2. **Neutral context** (the presupposition is new, nothing for or against it) — the accommodation test:
   does the model treat the presupposition as given anyway?
3. **Contradicting context** (a salient fact conflicts with the presupposition) — the gate: does the
   model *decline* to accommodate, flagging the conflict, rather than endorsing regardless?

Two project-authored, illustrative item schemas (not frozen; illustrative only):

1. **Definite-description trigger.** Trigger sentence: "The committee rejected Priya's proposal."
   Presupposition: *Priya made a proposal* (backgrounded by the definite/possessive).
   - supported — "Priya submitted a proposal last week. The committee rejected Priya's proposal." →
     *Priya made a proposal?*
   - neutral — (no prior mention) "The committee rejected Priya's proposal." → *Priya made a proposal?*
   - contradicting — "Priya submitted nothing this cycle. The committee rejected Priya's proposal." →
     *Priya made a proposal?*
   Look for: endorsed in *supported* and *neutral* (accommodation in the neutral case), **not** endorsed
   — or flagged as conflicting — in *contradicting*.

2. **Factive / change-of-state trigger.** Trigger: "Dana stopped exporting to Brazil." Presupposition:
   *Dana used to export to Brazil.* Same three contexts (supported / neutral / contradicting: "Dana has
   never traded with Brazil. Dana stopped exporting to Brazil."). Look for accommodation in the neutral
   case and a block/flag in the contradicting case.

A model that endorses the presupposition in the *neutral* case (supplies the unmet content) but declines
or flags it in the *contradicting* case is exhibiting **context-gated accommodation**; one that endorses
it in *all* contexts (including the contradicting one) is showing a blanket yes-bias, not accommodation;
one that endorses it in *none* (not even neutral) is not accommodating at all. Which way current
decoders go is the open question — asked, not asserted. (Because the source says accommodation is
graded by trigger/context, a fuller sketch would also vary the trigger family to test whether
accommodation-readiness is uniform — an §5.1 "not always equally easy" check.)

## How this differs from existing lines (so the corner is genuinely fresh)

- **Distinct from the projection line** (s158/s159/s160 and
  [`open-question/presupposition-projection-corner`](presupposition-projection-corner.md)). Projection
  holds a presupposition fixed and varies the **embedding** (does it survive negation/question/
  conditional?). Accommodation holds the sentence unembedded and varies the **context** (is the
  backgrounded content supported, new, or contradicted?). Different manipulation axis: embedding vs.
  context support. A projection probe never presents a context that *contradicts* the presupposition;
  that contrast is accommodation-specific.
- **Distinct from an ordinary consistency / NLI check.** The point is not merely whether the model
  detects a contradiction, but whether it *supplies unstated backgrounded content* in the neutral case
  while *withholding* it under conflict — the accommodation asymmetry, not a flat entailment judgment.
- **Distinct from the constructional-inference and indexicality lines**, which do not manipulate whether
  a presupposition's content is pre-established in context.

## Human-anchor status: `pending`

There is **no in-repo resource** for human accommodation judgments. This page makes no empirical claim
about LLMs (it proposes a probe, asserts nothing), so it carries no `anchors:` link; the gap is stated
plainly. A real probe would need **one** of:

- an externally-released human accommodation-judgment set — **none is in-repo**, and none is invented
  here; or
- a within-model, **`internal-contrast-only`** contrast across the supported / neutral / contradicting
  conditions — a within-model behavioral asymmetry making no human-comparison claim, the terminal status
  most of the project's behavioral results already carry.

This page **opens no `wiki/decisions/open/` entry**; it only flags that a future probe would choose one
of those paths and, if it takes the human-comparison path, open the anchor question then.

The provisional forward bet a *future* conjecture might make — clearly **not-yet-a-conjecture**, stated
in one sentence and freezing nothing — is that a panel of current models accommodates an unmet
presupposition in the neutral context (endorses the backgrounded content) more than in a contradicting
context, in a majority of panel models; this page neither designs nor commits to that bet.

## What would move this off "open"

The sub-corner advances in a *later* session when either (a) a frozen, pre-registered minimal-pair
accommodation probe is designed (trigger inventory, the three context conditions, and an adjudication
threshold fixed, with an independent pre-run critic passed) and run under the budget discipline; or
(b) an in-repo human accommodation-judgment resource is located or a within-model `internal-contrast-only`
asymmetry is ratified as the probe's terminal status. Until then the page stays **open**, seeding a
future wave and committing nothing.

## Status: open (scoping only)

This page runs nothing, freezes no operationalization, opens no spend, opens no `decisions/` entry, and
ratifies nothing. It opens the presupposition **accommodation** sub-corner by stating the phenomenon
(grounded in the SEP source deepened this session), naming one concrete behavioral angle (context-gated
accommodation), sketching one illustrative probe, distinguishing it from the projection line, and
flagging its human anchor as `pending`.
