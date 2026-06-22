---
type: conjecture
id: cross-level-gradience-aggregate-not-moment
title: "The 'graded-in-the-aggregate, discrete-in-the-moment' shape is ONE cross-level property of distributional competence, not three rhyming facts"
meaning-senses:
  - distributional
  - referential
  - constructional
  - relational
status: proposed
contingent-on:
  - cross-level-shared-instrument-operationalization
created: 2026-06-22
updated: 2026-06-22
links:
  - rel: refines
    target: open-question/gradience-population-not-moment
  - rel: depends-on
    target: open-question/gradience-population-not-moment
  - rel: depends-on
    target: result/lexical-bridging-context-v1
  - rel: depends-on
    target: result/lexical-bridging-context-working-surface-v1
  - rel: depends-on
    target: concept/distributional-meaning
---

# Conjecture: the aggregate/moment shape is one cross-level property, not three rhyming facts

> **Status: proposed (scoping only).** This page is a **forward bet**, not a result. It
> opens **no spend**, ratifies **nothing**, and runs **no probe**. The bet it states is
> contingent on the operationalization gate
> [`decisions/open/cross-level-shared-instrument-operationalization`](../../decisions/open/cross-level-shared-instrument-operationalization.md),
> which is itself **open** and ratifiable — at the earliest — by a *later* session via
> independent adversarial review ([`PROJECT.md`](../../../PROJECT.md) §12.3). Until that gate is ratified and a
> shared-instrument probe is designed, frozen, and run, every claim below stays provisional
> and the **honest default is the deflationary one** (three rhyming, instrument-specific
> facts), which this conjecture bets *against* — so the burden of proof is on the conjecture,
> not on the default.

## Statement

The forward bet, precisely:

> The "**graded across a population / aggregate, discrete-or-uncommitted on the single
> moment / item**" shape is **ONE property of distributional competence** that a
> next-token-trained model carries **across semantic levels** — not three separate,
> level-specific facts that merely share a vocabulary.

The shape is documented at the **lexical** level by
[`result/lexical-bridging-context-v1`](../results/lexical-bridging-context-v1.md) (now
channel-checked by
[`result/lexical-bridging-context-working-surface-v1`](../results/lexical-bridging-context-working-surface-v1.md)),
whose headline is "**a graded SCALE with ungraded COMMITMENT**" — every panel model places
human-rated usage-similarity-midpoint pairs at "an **intermediate relatedness position** …
**yet meets that same ambiguous item with clear-item-level confidence, almost never takes
the explicit "UNCLEAR" option, and shows near-zero dispersion across forced re-samples**"
([`result/lexical-bridging-context-v1`](../results/lexical-bridging-context-v1.md)), glossed
"**Gradience in the ledger; none in the moment.**" The same shape *rhymes* at the
**constructional** level via
[`essay/preference-without-commitment`](../essays/preference-without-commitment.md) (a
graded paraphrase *preference* "present in all three" models dissociates from an entailment
*commitment* "present in one" — "'use' decomposes into a preference component … and a
commitment component … and the two need not travel together") and at the **relational**
level via
[`essay/aggregation-not-constitution`](../essays/aggregation-not-constitution.md) (the
recoverable convention lives in the aggregate content-bag — "The convention is recovered
from the *set* of prior turns, not their *trajectory*").

The bet is **operationalized** as a single discriminating prediction: when **one** commitment
instrument is **frozen** and applied identically to (i) a lexical bridging item, (ii) a
constructional ambiguous item, and (iii) a relational mid-record item, the **same model**
shows the two-axis dissociation — **graded across the aggregate** *and*
**discrete/uncommitted on the single moment** — under that **one** instrument at **more than
one** level (ideally all three).

This conjecture is explicitly the bet **against** the deflationary default the
[`open-question/gradience-population-not-moment`](../open-questions/gradience-population-not-moment.md)
records — that the three legs are "**three separate, level-specific facts that merely rhyme**,
measured by three different instruments and unified only by a suggestive turn of phrase," and
that "**The honest default is the deflationary one (three rhyming facts) until a
shared-instrument probe says otherwise.**" The conjecture does not relax that default; it
proposes the test that could, in principle, move off it, and accepts the burden.

## Why this is interesting

- **It turns a phrasing into a testable mechanism-or-coincidence question.** The open
  question reads the cross-level parallel as, at present, "a *family resemblance among
  phrasings*, not a demonstrated mechanism." This conjecture is the forward unit that would
  decide between *one shared property* and *coincidence* — exactly the call the OQ defers.
- **It is the empirical track's natural next forward unit.** The lexical leg is now a run
  result with its channel checked; the constructional and relational legs are settled essays.
  The shared-instrument probe is the one move that would make the cross-level claim earn its
  keep rather than rest on a memorable gloss.
- **It connects to the project's standing caution about distributional competence.** Even a
  clean confirmation would be a statement *about distributional competence*, never about
  meaning proper:
  [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md) holds
  that distributional structure is "by itself, **silent on reference and on truth**," and
  that "A distributional success therefore does not settle the formal/functional question."
  A cross-level regularity in distributional *behavior* would inherit that silence in full.

## The instrument and the levels

The test holds **one** commitment instrument fixed and applies it across levels — the
**shared-instrument cross-level probe** the OQ names as the cleanest discriminator. Verbatim,
the OQ's named discriminator:

> "The cleanest discriminator would hold *one* commitment instrument fixed and apply it at
> more than one level — e.g. an explicit graded "I'm unsure / both / unclear" elicitation
> used on a lexical bridging item, a constructional ambiguous item, and a relational
> mid-record item, scored the same way. If the same model shows graded-aggregate /
> discrete-moment under *one* instrument across levels, that is evidence for a general
> constraint; if the shape appears under each level's *own* instrument but dissolves when the
> instruments are equalized, that is evidence for three rhyming instrument-specific facts."

The **actual choice of instrument is deferred** to the operationalization gate
[`decisions/open/cross-level-shared-instrument-operationalization`](../../decisions/open/cross-level-shared-instrument-operationalization.md)
and is **not decided here**. The OQ is explicit that "the operationalization of such a probe
is **not** decided here and would be a future `wiki/decisions/open/` candidate, with the same
freeze-before-results discipline the lexical and AANN designs imposed." This conjecture states
only the bet that a frozen shared instrument, once chosen, would test.

## What would confirm / falsify (symmetric — anti-cheat)

These criteria are **symmetric by design**: neither a uniform "discrete everywhere" nor a
uniform "graded everywhere" can be read as confirmation. What must replicate is the
**specific two-axis dissociation**.

- **Confirm.** Under **one** pre-registered, frozen shared instrument applied at **≥2**
  (ideally 3) levels, the **same model** shows the two-axis dissociation — graded across the
  aggregate **and** discrete/uncommitted on the single moment — at **multiple** levels: the
  shape **survives instrument-equalization**. (The per-level verdict map and the cross-level
  reading rule must be pre-registered and frozen in the operationalization gate's design,
  carried unless re-justified.)
- **Falsify (dissolution).** The shape appears under each level's **own native** instrument
  (as it does today) but **dissolves when the instrument is equalized** — the moment-pole
  becomes *graded* at some level under the shared instrument, or the levels **diverge** with
  no coherent per-model cross-level pattern. That is evidence for **three instrument-specific
  facts that rhyme**, and the deflationary default stands confirmed.
- **Weak / inconclusive.** The shared instrument **cannot be built** to express both axes
  cleanly at all three levels (the comparability problem, below); or one or more models
  **decline the channel** the instrument requires (the
  [`result/lexical-bridging-context-working-surface-v1`](../results/lexical-bridging-context-working-surface-v1.md)
  "channel-not-taken-up" precedent — gpt there "**declined** the surface … its leg is
  untested"); or N is too small to read a per-model cross-level pattern. None of these
  confirms or falsifies; they route to the gate's fallback.

**Anti-cheat (the cross-level version of the lexical design's named failure mode).** Neither a
uniform "discrete everywhere" nor a uniform "graded everywhere" confirms — confirmation
requires the **specific two-axis dissociation replicating across levels under ONE
pre-registered, frozen instrument**. **Per-level instrument-shopping** — trying each level's
own native instrument, or re-wording the shared instrument level-by-level, until the shape
appears — is **forbidden by construction**. This is the cross-level analogue of the lexical
gate's load-bearing prohibition (its decision binds against "instrument-shopping until
intermediacy appears"); here the forbidden move is shopping a *different* instrument per level
until all three rhyme. One instrument, frozen before any output, applied identically; the
cross-level reading rule pre-committed; dissolution reported as dissolution.

## Human anchor

`anchor: pending.` This conjecture invents **no** anchor, and a unified cross-level
human-comparison claim is **not** licensed at this stage. The OQ's "mixed anchor status"
disanalogy is inherited verbatim and is binding:

- The **lexical** leg is human-anchored but **capped**: it is DWUG-anchored "**capped to
  usage-similarity, not sense-co-presence**", never a certified sense bridge
  ([`result/lexical-bridging-context-v1`](../results/lexical-bridging-context-v1.md)'s binding
  cap).
- The **constructional** leg "rests on an **expert-stipulated scoring key, not human judgment
  data** (its result is `internal-contrast-only`)."
- The **relational** leg "(aggregation-vs-constitution) is `internal-contrast-only` too (no
  human comparison)."

So, in the OQ's words, "the legs do not even make the same *kind* of claim, so a unified
statement would have to be stated at the **weakest common strength**." Concretely: any unified
cross-level claim built on this conjecture could be made only as an **internal, within-model
contrast** unless each leg's anchor is *separately* established — which is a deferred,
per-leg anchor obligation, routed to the operationalization gate
([`decisions/open/cross-level-shared-instrument-operationalization`](../../decisions/open/cross-level-shared-instrument-operationalization.md),
Q4) and to future per-leg anchor decisions, **never** dodged here.

## Notes / caveats

- **Provisional throughout.** The instrument, the per-level verdict map, the cross-level
  reading rule, and every leg's anchor status all depend on the open gate's *later*
  ratification. Until then this is a forward bet, not a design — and ratifying that gate would
  fix the **yardstick**, never the result ([`CLAUDE.md`](../../../CLAUDE.md) rule 6).
- **Behavioral, not representational.** Every leg is about what the models *do*; none touches
  graded *representations*. A cross-level property, if found, would be a **behavioral
  regularity**, not a claim about internals or about next-token training mechanics directly.
- **Small N; n=3 commercial models.** The legs are each scoped to their own
  items/constructions/lemmas/register and to three 2026 commercial models; this bet inherits
  every such cap. No coverage claim — direction-of-shape only.
- **The "aggregate" is not the same construct across levels** (OQ disanalogy #2). Lexical: a
  *population of items*. Relational: "**single-reader-recoverable**" from one transcript —
  "a weaker, within-record notion than a population statistic." Constructional: a *graded
  compatibility* within a forced choice. Calling all three "the aggregate" "papers over real
  differences in what is being aggregated." This is a **real risk the design must confront**,
  not a wording quibble — it is the comparability problem the operationalization gate binds as
  non-optional (Q3).
- **Shared priors are not independent witnesses** (charter §2.5, as the OQ's legs each note).
  Three decoders are not three independent witnesses, and within a single shared instrument
  three *levels* read off one model are not three independent confirmations either; the
  cross-level *shape* under one frozen instrument is the signal, and its strength is bounded
  accordingly.
- **A pattern that spans levels is the pattern most at risk of being a phrasing artifact.**
  The OQ flags exactly this: a cross-level pattern "is also the pattern most likely to be an
  artifact of how the project phrases its findings rather than of the models" — which is the
  deeper reason the deflationary default holds the burden against this conjecture, not for it.
- **Evidence standard.** The sibling essay [`essay/cross-level-convergence-ladder`](../essays/cross-level-convergence-ladder.md) states, in
  the project's own voice, the general evidence standard this conjecture's confirm/falsify
  criteria instantiate (one frozen instrument, equalization survival, dissolution reported as
  first-class); read it for the principled version of the symmetric criteria above.
