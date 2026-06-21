---
id: lexical-bridging-context-operationalization
title: How to operationalize "intermediate, less-confident" model behavior on bridging items — which within-item gradience instrument (and reading rule), frozen before any result?
status: open
opened: 2026-06-21
opened-by: autonomous (session 74, opening the lexical bridging-context probe's operationalization gate)
contingent-artifacts:
  - open-question/lexical-bridging-context-gradience
meaning-senses:
  - distributional
  - referential
links:
  - rel: operationalizes
    target: open-question/lexical-bridging-context-gradience
  - rel: refines
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/referential-meaning
---

> **Status: OPEN (opened 2026-06-21, session 74).** This page **surfaces** the
> operationalization gate for the lexical bridging-context probe; it does **not**
> resolve it. It is **NOT ratifiable in this session** (the cross-session rule,
> [`PROJECT.md`](../../../PROJECT.md) §12.3 / [`CLAUDE.md`](../../../CLAUDE.md) rule 5):
> the **earliest** it may be ratified is a **later** session's independent
> adversarial-review pass, with written rationale recorded `resolved-by: autonomous
> (adversarial review)`. **No probe runs before that ratification.** This page lays
> out the instrument options and a *provisional default for a later reviewer* — it
> does **not** pick an instrument. Tom's standing override outranks any autonomous
> ratification.
>
> **Paired gate.** The human-anchor question for this probe — what *certifies* an
> item as genuinely bridging, independent of the model — is handled in a sibling
> decision, `lexical-bridging-context-anchor` (being opened in the same session by
> a sibling unit; its exact final content is not assumed here). This page is **only**
> the operationalization gate: how to *measure* "intermediate, less-confident,"
> given a bridging stratum the anchor decision certifies. The two gates must both be
> ratified (cross-session) before any run.

# Decision: which within-item gradience instrument, and its reading rule, frozen before any result

## Why this exists

[`open-question/lexical-bridging-context-gradience`](../../findings/open-questions/lexical-bridging-context-gradience.md)
re-opens the lexical axis on the one untested clause of an otherwise-`tested`
conjecture: **Prediction 4** of
[`conjecture/lexical-sense-gradience`](../../findings/conjectures/lexical-sense-gradience.md),
verbatim —

> "Deliberately sense-ambiguous (bridging) contexts, engineered so two senses are
> co-present, yield **intermediate, less-confident** model behavior rather than a
> forced discrete pick — the behavioral fingerprint of gradience."

The phrase **"intermediate, less-confident"** is not one measurement; it is a
*family* of measurements, and the instruments in that family can **disagree**. The
open-question page states this directly:

> "'Intermediate, less-confident' is not one measurement; it is a family, and the
> instruments can disagree. This is an operationalization choice to be **frozen
> before any result is seen** (charter §8 …)."

That makes the choice of instrument a value-laden operationalization decision a
session must not auto-take ([`CLAUDE.md`](../../../CLAUDE.md) rule 5). This page
interlocks the choices and makes the freeze-before-results discipline binding — in
the same shape as the resolved
[`decisions/resolved/function-word-anchor-design`](../resolved/function-word-anchor-design.md)
and the conjecture's own
[`decisions/resolved/lexical-sense-gradience-operationalization`](../resolved/lexical-sense-gradience-operationalization.md).

Two facts constrain the whole space and are stated up front so no option smuggles
them past a later reviewer:

- **The instrument-sensitivity pattern is real and documented, not hypothetical.**
  [`result/lexical-sense-gradience-v1`](../../findings/results/lexical-sense-gradience-v1.md)
  recorded that gpt-5.4-mini "is the noisier model under the *ordinal* DURel framing
  (ρ 0.60 …) but cleaner under the *continuous* framing (ρ 0.68) — the lexical
  reappearance of the instrument-sensitivity pattern." A model's reading can depend
  on the elicitation format; the same risk applies to a within-item uncertainty
  instrument, only more sharply, because here the *signal itself* is the dispersion
  or confidence, not a correlation that survives reframing.
- **The conjecture's own *Notes* already flagged instrument as a gate.** Its
  caveats state: "pick and **freeze the instrument before seeing results** (charter
  §8) — do not tune it until the collapse becomes gradience or vice versa. Queue
  this gate before running." This page *is* that queued gate, for Prediction 4
  specifically.

## What is being decided here (scope), and what is not

**In scope (this page):** which behavioral instrument(s) measure within-item
intermediacy / lower confidence on bridging items; the *reading rule* that turns the
instrument's output into a confirm / null / falsify verdict; and the freeze
discipline that prevents instrument-shopping.

**Out of scope (other gates):** *which items count as bridging* and their human
certification (sibling `lexical-bridging-context-anchor`); whether the result makes
a human-comparison claim at all (inherited from that anchor decision); and the
context-ambiguity control, which is **not optional** and is bound below as a
design-inherited constraint, not re-decided here.

## The two-axis ordinal prediction this instrument must serve

Per the open-question page, the prediction is ordinal on **two axes at once**, and
any instrument must be able to express both:

> "The prediction is ordinal on *two* axes: the bridging class should sit at an
> **intermediate** position on the model's same/different signal **and** carry
> **lower confidence / higher dispersion** than either clear class."

So the design contrasts **three** item classes for the *same* target word —
**clearly-same**, **clearly-different**, and **bridging** — and the chosen
instrument must yield, per class: (i) a **same/different position** (bridging
expected to sit *between* the two clear classes) **and** (ii) a **confidence /
dispersion** reading (bridging expected *lower-confidence / higher-dispersion* than
*either* clear class). An instrument that can report only one of these two axes is
inadequate on its own.

## The first-class NULL, declared up front

Per [`CLAUDE.md`](../../../CLAUDE.md) rule 6 ("write the null") and the open-question
page, the negative is first-class and is declared **before** any data:

> "The null is first-class and must be declared up front: bridging items are handled
> with the same confidence as clear items — a forced discrete pick — which would be
> a *within-item* discreteness signal (graded scale, ungraded commitment) and a
> clean negative for prediction 4."

A clean null here is a **within-item discreteness** result — the model carries a
graded *scale* (already shown by v1's cross-item monotonicity) but ungraded
*commitment* on the single ambiguous item. The reading rule below must make that
null **as legible and reportable as a positive**, with no after-the-fact relabelling
of items.

## The sub-questions

### Q1 — Which within-item intermediacy instrument?

The open-question page names three candidate instruments. They are lifted and
sharpened into options below. Each measures a related-but-non-identical thing, and
**they may disagree** (Q2). For each: what it measures, its strength, its weakness,
and how it could be gamed/tuned.

- **Option A — Spread / entropy of a forced same/different judgment.** The model is
  **forced** to pick same-or-different (no third option, no confidence), and the
  intermediacy signal is the **dispersion** of its picks across **paraphrase variants
  and/or repeated samples** of the same bridging item. Operationally this is v1's
  panel "run for variance rather than mean" (open-question page).
  - *What it measures:* behavioral *instability* of the forced commitment — high
    entropy / high flip-rate across re-promptings = the item is not driving a stable
    discrete pick. The same/different *position* axis is read from the central
    tendency of the picks; the *dispersion* axis from their spread/entropy.
  - *Strength:* the model is never *told* an item is ambiguous, so it cannot perform
    "this is the unclear one" by reading the frame; the intermediacy must emerge from
    behavior. Closest to a behavior-only signal, least suggestible.
  - *Weakness:* dispersion conflates *sense indeterminacy* with *generic sampling
    noise* and with *prompt-paraphrase sensitivity* unrelated to sense; needs a
    matched dispersion baseline on the clear classes (the clear classes should show
    *low* dispersion for the contrast to mean anything), and the number of
    samples/paraphrases is a tunable knob.
  - *Gaming/tuning surface:* choosing the sample count, the temperature, or the
    paraphrase set until the bridging class's dispersion separates from the clear
    classes; reading entropy at a threshold picked after seeing the spread.

- **Option B — Explicit graded-confidence elicitation.** The model gives the
  same/different call **and** a **0–100 confidence (or relatedness) rating**; the
  **per-item rating** is the within-item signal. Closest to v1's `durel` / `cont`
  framings, repurposed per-item (open-question page).
  - *What it measures:* the model's *stated* confidence/relatedness on the single
    item. Same/different *position* axis = the call (or the rating's side of the
    midpoint); *confidence* axis = the rating's distance from the confident extremes
    (bridging expected to cluster mid-scale).
  - *Strength:* directly and per-item expresses *both* required axes in one
    elicitation; continuous, so it grades naturally; reuses an instrument v1 already
    validated as monotonic against a human signal.
  - *Weakness:* stated confidence is a self-report and may be miscalibrated or
    anchored to surface features of the sentence rather than to sense indeterminacy;
    a model may default mid-scale for *any* hard item, not specifically bridging
    ones (so the clear-class confidence must be shown high as a precondition).
  - *Gaming/tuning surface:* picking the rating scale, the midpoint band that counts
    as "intermediate," or the confidence threshold after seeing the distribution;
    re-wording the confidence prompt until the mid-band populates.

- **Option C — A "both senses / unclear" third response option.** A **categorical**
  instrument: the model is given an explicit **third option** (e.g. "same /
  different / both-or-unclear") and the signal is whether it **takes the third
  option more on bridging items than on clear items** (open-question page).
  - *What it measures:* the model's *willingness to decline the binary* on bridging
    vs clear items — a categorical rate, not a continuous band.
  - *Strength:* a clean, legible, directly-Prediction-4-shaped signal ("forced
    discrete pick" vs "declines the binary"); behaves differently from the two
    continuous instruments and so is a genuine cross-check, not a duplicate.
  - *Weakness:* it makes only one of the two axes crisp (the *decline rate*); the
    same/different *position* of items it does commit on is a separate read. It is
    also **sensitive to how willing the model is to decline a binary at all** — a
    model that over-uses or refuses the third option globally washes out the
    contrast; the third option's wording is itself an instrument knob.
  - *Gaming/tuning surface:* wording the third option to be more/less inviting until
    its bridging-vs-clear rate separates; choosing which models' decline-behavior to
    report.

### Q2 — The reading rule, and the load-bearing failure mode

The three instruments **measure related but non-identical things and may disagree**
(open-question page; the v1 instrument-sensitivity pattern is the documented
precedent). The **load-bearing failure mode**, flagged by *both* the conjecture and
the open-question page, must be named explicitly and designed against:

> "The named failure mode: **tuning the instrument until intermediacy appears** —
> trying instruments or thresholds until one shows the predicted intermediate band.
> The gate must pick one instrument (or pre-register a small fixed panel of them with
> the reading rule) and freeze it, reporting whatever each shows including
> disagreement, rather than selecting post hoc."

So the reading rule must satisfy, **before any data**:

1. **Pick exactly ONE instrument, OR pre-register a SMALL FIXED PANEL** of two or
   three of A/B/C **with the cross-instrument reading rule fixed in advance** — e.g.
   "the prediction counts as supported only if instruments X and Y *agree* on the
   two-axis ordinal pattern; disagreement is reported as disagreement and is itself
   a (weaker) result," with the agreement rule written down *now*, not chosen after
   seeing which instruments cooperate.
2. **Freeze the instrument(s), the scale(s), the sample/paraphrase counts, the
   midpoint/threshold bands, and the cross-instrument reading rule** before the first
   probe call (the v1/v3 and function-word freeze discipline).
3. **Report whatever each frozen instrument shows, including disagreement and
   including the null.** No instrument may be added, dropped, re-worded, or
   re-thresholded after outputs are seen. Picking the one instrument that shows the
   band, post hoc, is the cheat this gate exists to forbid.

The reading rule must also bind the **two-axis** requirement (an instrument or panel
must express *both* the position and the confidence/dispersion axes) and the
**first-class null** (within-item discreteness reported as cleanly as a positive).

### Q3 — Inherited design constraint: the context-ambiguity control (NOT re-decided, bound)

Any design here **inherits v1's clause-(c) discipline**, and this is a binding
constraint, not an option. The open-question page:

> "Any serious design inherits v1's clause-(c) discipline — a context-similarity /
> context-ambiguity control measured independently of the model's sense signal — so
> within-item uncertainty is shown to track *sense* indeterminacy, not mere context
> indeterminacy."

The distributional shadow at the lexical-uncertainty grain is: a model could be
less-confident on bridging items merely because their *contexts* are more ambiguous,
not their *senses*. So whichever instrument is frozen, the design must carry a
**context-ambiguity / context-similarity control measured independently of the
model's sense-uncertainty signal**, so that an intermediacy result is shown to track
**sense** indeterminacy rather than **context** indeterminacy. (This mirrors v1's
`topic` control, computed independently of the sense rating.) An instrument cannot
be ratified without a design slot for this control.

## Provisional default (not a decision)

Recorded for a *later* reviewer; **not decided here**, and not run.

- **Q1 / Q2 — instrument and reading rule:** a **small fixed panel of two**
  instruments, **Option B (explicit graded-confidence)** as the **primary**
  (it expresses *both* required axes per-item in one elicitation, and reuses the
  v1-validated `durel`/`cont` framing) and **Option C (third "both/unclear"
  option)** as a **categorical cross-check** (it is the most directly
  Prediction-4-shaped and behaves differently from the continuous instrument, so
  agreement between B and C is a stronger signal than either alone). The
  cross-instrument reading rule, **fixed in advance**: Prediction 4 counts as
  *supported* only if **both** B's mid-band confidence *and* C's elevated decline
  rate land bridging *between* (B) / *above* (C) the two clear classes on the
  two-axis pattern; **B–C disagreement is reported as disagreement**, not resolved by
  picking the cooperative one; the **null** (bridging handled at clear-item
  confidence / clear-item decline rate) is reported as a clean within-item
  discreteness negative. **Option A (forced-judgment dispersion)** is held as an
  *optional, characterizing-only* secondary that may *describe* but never *decide* —
  it is the most behavior-only instrument but conflates sense indeterminacy with
  sampling/paraphrase noise, so it is not load-bearing without a heavier baseline.
  All scales, sample/paraphrase counts, midpoint bands, the third-option wording, and
  the B–C agreement rule are **frozen and recorded before the first probe call.**
- **Q3 — context control:** bound, not optional — a v1-style independently-measured
  context-ambiguity / context-similarity control is part of any design built on this
  gate.

**Why this default makes a spurious positive harder, not easier:** a *fixed two-of-
three panel with a pre-committed agreement rule* removes instrument-shopping (the
named failure mode); requiring **B–C agreement** raises the bar above any single
instrument; demoting A to characterizing-only removes its tunable dispersion knobs
from the verdict; freezing scales/thresholds/wording removes post-hoc band-picking;
the inherited context control removes the distributional-shadow route to a false
positive; and the first-class null is reportable as cleanly as a positive. The
competing single-instrument routes are simpler but each is *more* tunable on its own
threshold, which is exactly the cheat-surface this gate closes. **This choice is not
made here**; it is laid out for a future independent adversarial-review pass.

## Anti-cheat note

Ratifying this decision (in a *later* session) fixes the **yardstick** — which
instrument(s), which reading rule, which freeze discipline — **never the result**
([`CLAUDE.md`](../../../CLAUDE.md) rule 6). The probe must **not** be run, nor the
instrument / scale / threshold / panel re-tuned, in any session that ratifies; a
pre-run critic GO/NO-GO against the *frozen* instrument set defers the run rather
than relaxing it. The session boundary is load-bearing: this page was **opened
2026-06-21 (session 74)**, no result exists, and there is no result to motivate a
choice. The named failure mode — instrument-shopping until intermediacy appears — is
forbidden by construction: one instrument or a pre-committed fixed panel, frozen
before data, with disagreement and the null both reported. The paired human-anchor
obligation (what certifies an item as bridging) is **not** dodged here; it is carried
by the sibling `lexical-bridging-context-anchor` decision and must also be ratified
cross-session before any run.
