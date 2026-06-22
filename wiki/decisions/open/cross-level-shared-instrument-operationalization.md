---
id: cross-level-shared-instrument-operationalization
title: "How to operationalize a SHARED-instrument cross-level probe of the aggregate/moment shape — which single commitment instrument, applied identically across levels, frozen before any result?"
status: open
opened: 2026-06-22
opened-by: autonomous (session 80, maturing open-question/gradience-population-not-moment into a conjecture)
contingent-artifacts:
  - conjecture/cross-level-gradience-aggregate-not-moment
meaning-senses:
  - distributional
  - constructional
  - referential
  - relational
links:
  - rel: operationalizes
    target: open-question/gradience-population-not-moment
  - rel: operationalizes
    target: conjecture/cross-level-gradience-aggregate-not-moment
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: refines
    target: open-question/gradience-population-not-moment
---

> **Status: OPEN (opened session 80, 2026-06-22).** Ratifiable at the earliest by a **LATER**
> session via independent adversarial review ([`PROJECT.md`](../../../PROJECT.md) §12.3); **NEVER** in the session
> that opened it. Ratifying this gate fixes the **yardstick** — which single instrument, which
> cross-level reading rule, which freeze discipline — **never the result** ([`CLAUDE.md`](../../../CLAUDE.md) rule
> 6). **No probe is run here and no spend is opened.** This page lays out options and a
> provisional default for a future reviewer; it decides nothing.

# Decision: which single commitment instrument, applied identically across levels, frozen before any result

## Why this exists

[`open-question/gradience-population-not-moment`](../../findings/open-questions/gradience-population-not-moment.md)
names a **shared-instrument cross-level probe** as the cleanest discriminator between *one*
cross-level property of distributional competence and *three* level-specific facts that merely
rhyme — and then explicitly **defers** the operationalization of that probe. Verbatim:

> "(This is scoping only — the operationalization of such a probe is **not** decided here and
> would be a future `wiki/decisions/open/` candidate, with the same freeze-before-results
> discipline the lexical and AANN designs imposed.)"

This page **is** that queued gate. It is the operationalization decision the conjecture
[`conjecture/cross-level-gradience-aggregate-not-moment`](../../findings/conjectures/cross-level-gradience-aggregate-not-moment.md)
is contingent on, built in the same shape as the resolved lexical gate
([`decisions/resolved/lexical-bridging-context-operationalization`](../resolved/lexical-bridging-context-operationalization.md)),
whose freeze-before-results and anti-instrument-shopping discipline it inherits and extends to
the cross-level case.

## What is being decided (scope), and what is not

**In scope (this page):**

- **Which SINGLE commitment instrument** is applied **identically** across the three levels
  (lexical bridging item / constructional ambiguous item / relational mid-record item).
- **What counts as the "aggregate" vs the "moment"** at each level — the **comparability
  problem** the OQ flags as disanalogy #2 ("The 'aggregate' is not one thing across legs").
- **The cross-level reading rule** that turns the instrument's outputs into a verdict
  (confirm / dissolve / weak).
- **The freeze-before-results discipline** (one instrument, frozen and sha256'd before the
  first probe call; per-level instrument-shopping forbidden by construction).

**Out of scope (other gates / future calls):**

- **The human-anchor question per leg.** Each leg's anchor is a *separate, deferred*
  obligation, not settled here: the lexical leg's cap to **usage-similarity** is inherited
  ([`result/lexical-bridging-context-v1`](../../findings/results/lexical-bridging-context-v1.md));
  the **constructional** and **relational** legs are `internal-contrast-only`. Bound below as
  Q4; resolved only by future per-leg anchor decisions.
- **Whether to run at all.** A future independent **pre-run critic** GO/NO-GO and a **budget**
  call (charter §8) decide that — not this page. A NO-GO defers the run; it never relaxes a
  band.

## The two-axis cross-level pattern the instrument must serve

The instrument, whichever is chosen, must be able to express **both** axes at **each** level
for the **same** model:

1. a **graded / structured** reading recoverable from the **aggregate** (the population of the
   model's judgments, or the content-bag of the record), **and**
2. a **discrete / ungraded / uncommitted** reading of the handling of the **single moment or
   item**.

An instrument that can express only one of the two axes, or that can express both at one level
but not at another, is **inadequate** and fails the gate. The cross-level signal the conjecture
bets on is the **same model** showing the (1)-vs-(2) dissociation under **one** frozen
instrument at **≥2** levels.

## The first-class NULL, declared up front

Per [`CLAUDE.md`](../../../CLAUDE.md) rule 6 ("write the null"), the negative is **first-class** and declared
**before** any data: **dissolution-under-equalization** — the shape that shows under each
level's own native instrument **dissolving** when the single shared instrument is applied — is
to be reported **as cleanly and legibly as confirmation**. A clean dissolution result is
positive evidence for the deflationary default (three rhyming, instrument-specific facts) and
must not be quietly recoded as "inconclusive." The reading rule below (Q2) must make the null
as reportable as a positive, with **no** after-the-fact relabelling of levels or re-wording of
the instrument.

## The sub-questions

### Q1 — Which single shared commitment instrument?

Each option is applied **identically** at all three levels; for each, *what it measures /
strength / weakness / gaming-tuning surface* (as the lexical gate did for its A/B/C).

- **Option A — Explicit graded "unsure / both senses / unclear" + 0–100 confidence,
  elicited identically at each level.** This is the OQ's **named** idea: "an explicit graded
  'I'm unsure / both / unclear' elicitation used on a lexical bridging item, a constructional
  ambiguous item, and a relational mid-record item, scored the same way."
  - *What it measures:* a per-item **stated** posture (graded confidence + a categorical
    "unclear" decline) on the single moment, contrasted with the model's **aggregate**
    ordering/recoverability at that level. Both axes in one elicitation.
  - *Strength:* expresses **both** required axes per item in one frozen elicitation; reuses
    the exact instrument family the lexical leg already validated (B confidence + C decline);
    most directly comparable across levels because the *wording* is held identical.
  - *Weakness:* stated confidence is a **self-report** and may be miscalibrated or anchored to
    surface features rather than to the level's actual indeterminacy (the lexical
    working-surface re-run already showed claude's self-reported confidence is *partly
    channel-sensitive*); a model may default mid-scale on any hard item, so a clear-class
    precondition is needed **per level**.
  - *Gaming/tuning surface:* picking the confidence band, the verbatim "unclear" wording, or
    which level's mid-band "counts," after seeing the distribution; re-wording the elicitation
    per level until the shape appears (this is the named failure mode — forbidden by Q2).

- **Option B — Forced choice + dispersion-across-resamples, applied identically.** The model
  is forced to commit (no third option, no stated confidence) and the moment-axis signal is
  **dispersion** (entropy / flip-rate) across repeated samples / paraphrase variants of the
  same item, at each level; the aggregate axis is read from the central tendency across the
  population at that level.
  - *What it measures:* behavioral **instability** of a forced commitment on the single moment
    — high dispersion = the item does not drive a stable discrete pick — against the aggregate
    ordering.
  - *Strength:* the model is never *told* an item is ambiguous, so it cannot perform "this is
    the unclear one" by reading the frame; closest to a behavior-only signal, least
    suggestible; ports cleanly across levels because "resample the same item" is
    level-agnostic.
  - *Weakness:* dispersion **conflates** indeterminacy with generic sampling noise and
    prompt-paraphrase sensitivity; needs a matched low-dispersion baseline on each level's
    clear class for the contrast to mean anything; sample/paraphrase count is a tunable knob;
    the lexical leg found forced-pick dispersion near-zero and demoted it to
    *characterizing-only* — so as a **primary** cross-level instrument it carries more weight
    than it did there and may be too blunt.
  - *Gaming/tuning surface:* choosing sample count, temperature, or paraphrase set per level
    until the moment-axis separates; reading an entropy threshold picked after seeing the
    spread.

- **Option C — An NLI / entailment-style commitment instrument, ported to each level.** A
  categorical entailment-commitment probe (the AANN/CxNLI instrument family) applied at each
  level — e.g. "does the premise commit you to the unification / same-sense / latest-binding
  reading?"
  - *What it measures:* a defeasible **inferential commitment** on the single moment, against
    the aggregate distributional preference.
  - *Strength:* it is the project's sharpest existing *commitment* discriminator at the
    constructional level, and it cleanly separates a graded *preference* from a binary
    *commitment* (the
    [`essay/preference-without-commitment`](../../findings/essays/preference-without-commitment.md)
    dissociation).
  - *Weakness (flag, load-bearing):* it is **hard to port cleanly** to the lexical and
    relational levels — there is no natural "entailment" framing for a same/different-sense
    judgment on a bridging item, nor for convention-recovery from a transcript, so porting
    risks measuring **different constructs** at the three levels (defeating the whole point of
    *equalizing* the instrument). If C cannot be expressed at a level without changing what it
    asks, that level is not testable under C and the option fails the comparability constraint
    (Q3) there.
  - *Gaming/tuning surface:* re-framing the "entailment" per level until each yields the
    shape; choosing the aggregation rule over multiple hypotheses after seeing results (the
    AANN line's documented NLI-aggregation hazard).

### Q2 — The cross-level reading rule, and the load-bearing failure mode

The instruments at different levels (and the same instrument *across* levels) **may disagree**.
The **load-bearing failure mode** — the cross-level analogue of the lexical gate's named
cheat — is **per-level instrument-shopping**: trying each level's own native instrument, or
re-wording the shared instrument level-by-level, until all three rhyme. It must be **forbidden
by construction**:

1. **Pick exactly ONE shared instrument** (or, if a small fixed panel, pre-register the
   cross-level reading rule over it) and **freeze** it — wording, scales, bands, sample counts,
   the per-level "aggregate" and "moment" definitions, and the cross-level reading rule —
   **sha256-hashed before the first probe call**.
2. **Pre-commit the cross-level reading rule:** **confirm** iff the **same model** shows the
   two-axis dissociation under the one frozen instrument at **≥2** (ideally 3) levels;
   **dissolve** iff the shape holds under each level's native instrument but **fails** under
   the equalized one (moment-pole graded somewhere, or levels diverge with no coherent
   per-model pattern); **weak** iff the instrument cannot express both axes at all levels, a
   model declines the channel, or N is too small.
3. **Report whatever the frozen instrument shows, including dissolution and divergence.** No
   instrument may be added, dropped, re-worded, or re-thresholded per level after any output is
   seen. **Dissolution is reported as dissolution** — it is the first-class null, not a failed
   run.

### Q3 — The comparability constraint (NOT optional; bound)

This is the constraint the OQ's disanalogy #2 forces, and it is **binding, not an option**.
Before any data, the design must **pre-register what "the aggregate" and "the moment" mean
OPERATIONALLY at each level**, so the three legs are the **same measurement shape**, not three
different things relabelled:

- **Lexical** — aggregate = the model's ordering across a *population of bridging vs clear
  items*; moment = its posture on the *single bridging item*.
- **Constructional** — aggregate = the graded paraphrase-*preference* shift across items;
  moment = the entailment-*commitment* (or stated posture) on the *single ambiguous item*.
- **Relational** — aggregate = convention-recoverability from the *content-set of one record*
  (the OQ's caution applies: this is "**single-reader-recoverable**", a *weaker, within-record*
  notion than a population statistic); moment = the posture on the *single mid-record
  decision*.

An instrument set that does **not** carry an explicit, frozen comparability slot — defining
"aggregate" and "moment" per level so the three are the same shape — **fails the gate**. The
asymmetry the OQ names (the relational "aggregate" is within-record, not a population) must be
disclosed and either equalized or the relational leg's verdict explicitly scoped to that weaker
notion.

### Q4 — Anchor deferral (bound)

This gate **licenses no human-comparison claim**. Each leg's anchor is a **separate, deferred**
obligation: the lexical leg is **capped to usage-similarity** (inherited, never sense
co-presence); the constructional and relational legs are **`internal-contrast-only`** (no human
comparison). So a unified cross-level result built on this gate can be stated only as an
**internal, within-model contrast** at the **weakest common strength**, unless and until each
leg's anchor is separately established by its own future decision. **No anchor may be
invented** to lift a leg above its inherited cap.

## Provisional default (NOT a decision)

Recorded for a *later* independent adversarial-review pass; **not decided here**, and **not
run**.

- **Q1 / Q2 — instrument and reading rule:** **Option A** — a single explicit graded
  "**unsure / both / unclear**" elicitation **plus** a 0–100 confidence rating — applied
  **identically** at the lexical bridging item, the constructional ambiguous item, and the
  relational mid-record item, scored the same way. The **two-axis cross-level reading rule**
  (confirm / dissolve / weak, per Q2) is **pre-committed and sha256-frozen** before the first
  probe call; the **dissolution null is reported as cleanly as confirmation**.
- **Q3 — comparability:** the per-level operational definitions of "aggregate" and "moment"
  are **frozen** before data, with the relational "aggregate" explicitly disclosed as the
  weaker within-record / single-reader-recoverable notion.
- **Q4 — anchor:** the per-leg human-anchor question is **deferred**; any unified result is
  **internal-contrast-only** at the weakest common strength until each leg is separately
  anchored.

**Why this default makes a spurious positive harder, not easier.** One **frozen** shared
instrument removes the **per-level instrument-shopping** that is the named cross-level cheat
(no trying each level's native instrument until all rhyme); the **comparability freeze** (Q3)
blocks the relabelling route (calling three different measurements "the aggregate"); the
**dissolution null** is first-class, so equalization that *kills* the shape is reported as the
deflationary win it is, not buried. Option A is preferred over B and C because it expresses
**both** axes per item in **one** elicitation whose **wording is held identical across levels**
(the cleanest comparability), where B is blunter on the moment-axis (the lexical leg already
demoted forced-pick dispersion to characterizing-only) and C **does not port cleanly** to the
lexical and relational levels (Q1-C weakness) — so A is the option least likely to smuggle in a
positive by measuring different things at different levels. **This choice is NOT made here; it
is laid out for a future independent adversarial-review pass.**

## Anti-cheat note

The **session boundary is load-bearing**: this page was **opened 2026-06-22 (session 80)**, no
result exists, and there is no result to motivate a choice. Ratification — at the earliest by a
*later* session — fixes the **yardstick, never the result** ([`CLAUDE.md`](../../../CLAUDE.md) rule 6). The probe
must **not** be run, nor the instrument / scale / band / wording / cross-level reading rule
re-tuned, in any session that ratifies; a **pre-run critic NO-GO** against the *frozen*
instrument set **defers the run** rather than relaxing any band. The named failure mode —
**per-level instrument-shopping until the shape appears** — is **forbidden by construction**
(one frozen instrument, a pre-committed cross-level reading rule, dissolution reported as
dissolution). The paired per-leg human-anchor obligations (Q4) are **not** dodged here; they
are separate, deferred decisions, each ratified cross-session before any run that would make a
human comparison on that leg.
