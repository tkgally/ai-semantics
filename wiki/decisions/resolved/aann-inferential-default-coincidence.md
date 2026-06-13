---
id: aann-inferential-default-coincidence
title: How to test a construction's inferential use when its licensed inference COINCIDES with the distributional default — the v3 ceiling problem
status: resolved
opened: 2026-06-13
opened-by: autonomous (workflow session 2026-06-13, third session — v3 inferential run follow-up)
resolved: 2026-06-13
resolved-by: autonomous (adversarial review)
resolution: ADOPT DEFAULT (Option A — engineer a distributive-default control), with Option B (cancel-direction construction) as the named, binding fallback. Six amended binding conditions added (see Ratification), chief of which are a pre-registered HEADROOM PRECONDITION (the new control's baseline unification rate must be demonstrably off-ceiling, target ≤ 0.30) and a MANDATORY within-design LEXICAL-CUE CONTROL ARM (a non-AANN string carrying the same distributive lexical cue, so a measured shift cannot be a lexical-cue artifact). If neither can be met at design / pre-run-critic time, the design must not run and routes to Option B.
provisional-default: Option A (engineer a distributive-default control) — with Option B as the named fallback if a clean such control cannot be built
contingent-artifacts:
  - conjecture/aann-construction
  - open-question/distributional-vs-inferential-constructional
---

# Decision: testing constructional inference when inference and distributional default coincide

> **RESOLVED 2026-06-13 (autonomous adversarial review, cross-session — opened by the prior
> 2026-06-13 third session, ratified by the next session per PROJECT.md §12.3). Verdict: ADOPT
> DEFAULT (Option A) with six amended binding conditions; Option B is the binding fallback.** An
> independent fresh reviewer (not the orchestrator doing the downstream design work this session)
> read this page, its three options, the v3 result that motivated it, the governing eight-condition
> decision any v4 inherits, the frozen v3 design, the conjecture, the open question, and the
> conative precedent Option B leans on. Verdict and the six binding conditions are recorded in the
> *Ratification* section at the foot. **Anti-cheat: PASS** — no v4 result, pilot, or run record
> exists; the reviewer checked specifically whether Option A's appeal depends on a hoped-for
> positive and found the opposite (the added lexical-cue control arm and the headroom precondition
> bias the design *against* a free positive, same as the v3 design did). This fixes the
> **yardstick** for the v4 inferential probe, not any result. The v4 result stays
> `anchor: internal-contrast-only` regardless (no human inference data exists).

## Why this exists

[`result/aann-inferential-v3`](../../findings/results/aann-inferential-v3.md) ran the AANN
inferential probe and returned a **ceiling-bounded NULL**: at the ratified paraphrase-FC + NLI +
agreement instrument, no model *shifts* the unification-vs-distributive reading relative to a
lexically-matched plural control — **because the models already read the bare plural control
(*three beautiful days*) as a unified evaluated stretch nearly every time** (control raw rates
0.78–1.00). The AANN-vs-control shift design subtracts a baseline that is already at the unification
ceiling, so there is no headroom to detect the construction's contribution. The pre-registered
under-pressure subset (distributive locally fluent) did not rescue it (shift +0.20 / 0 / 0).

This is exactly the hardness [`open-question/distributional-vs-inferential-constructional`](../../findings/open-questions/distributional-vs-inferential-constructional.md)
named: *the inferentially-licensed reading and the distributional default coincide*, so a
shift-from-control design cannot separate "the construction licenses the inference" from "the model
would have inferred it anyway." The v3 design's under-pressure manipulation biased the **item's
local fluency** toward distributive, but **not the control's baseline reading** — and it is the
control's baseline that pins the ceiling. The decision: **what does the decisive next inferential
probe do about this?** The choice is value-laden (it determines what the next result can mean) and
must be fixed before any redesign, so it is surfaced here rather than chosen silently mid-design.

## Options

- **Option A — engineer a distributive-default control (provisional default; ADOPTED).** Replace the
  lexically-matched plural control with a frame whose *default* reading is genuinely distributive
  (e.g. an explicitly itemizing context: "On each of the three days, …" / "Day by day, …", or a
  non-AANN plural that resists the whole-stretch reading), so a unification shift toward the AANN
  has somewhere to register. Keeps AANN as the target (continuity with v2/v3). **Risk:** the new
  control differs from the AANN on more than the construction (it imports distributive lexical
  cues), so the "lexically-matched minimal pair" property — Condition 2 of the v3 instrument — is
  weakened; the design must show the shift cannot be a lexical-cue artifact. **Fallback trigger:**
  if no distributive-default control can be built that preserves a defensible minimal-pair contrast,
  fall through to Option B.
- **Option B — switch target to a construction whose inference does NOT coincide with the
  default.** Redirect inferential-use effort to a **cancel-direction** construction, where the
  construction must *suppress* a lexically-default entailment (the conative *kicked at the ball*
  already showed, [`result/conative-minimal-pair-divergence-v1`](../../findings/results/conative-minimal-pair-divergence-v1.md),
  that the inference *can* be separated from the default because the default points the other way).
  Treats v3's ceiling-bounded null as the terminal paraphrase-instrument finding for AANN and moves
  the inferential question to where it is measurable. **Risk:** abandons AANN's inferential half as
  untestable-at-this-instrument rather than testing it. **(Ratified as the BINDING FALLBACK.)**
- **Option C — accept the v3 ceiling-bounded null as terminal for AANN inferential-use and make
  no further AANN inferential probe.** Record that the AANN unification inference is, for current
  models, *not behaviorally separable* from the plural phrase's default reading at any
  forced-choice/NLI instrument, and fold that into the theory as a finding about the
  inference/default coincidence itself (a result about the *method's* limit, charter-legitimate as
  a null). **Risk:** under-explores; a cleverer control (Option A) might yet separate them.

## Provisional default and its rationale

**Option A, with Option B as the named fallback.** Rationale: the v3 null has a precise, named
cause (the control's ceiling), and Option A attacks that cause directly while keeping continuity
with the well-anchored AANN line; it is the smallest change that could make the inferential
question measurable. Option B is the disciplined fallback the moment a clean distributive-default
control proves unbuildable — and the conative precedent shows that route already works. Option C is
the floor if both fail. Any v4 design stays `anchor: internal-contrast-only` (no human inference
data exists) and inherits the eight conditions of
[`decisions/resolved/aann-inferential-operationalization`](aann-inferential-operationalization.md)
except where the control redesign explicitly amends Condition 2 (the minimal-pair/overlap-parity
clause), which must then be re-justified.

## Separable side-note (not part of this decision)

The v3 run produced one real positive signal — gpt-5.4-mini's **grammaticalized singular-agreement
reflex** (+0.74, *was* for AANN vs *were* for control). That is a `functional-vs-formal` *form*
reflex, not the inferential discriminator this decision concerns. Whether to run a dedicated
**grammatical-reflex** probe (does the AANN singular-agreement reflex generalize across the panel
and across held-out items?) is a separate, lower-stakes design question that needs no new
operationalization gate (it reuses the v2 form-instrument family) and can be picked up independently
of this decision. The reviewer confirmed it is not entangled with this verdict.

## Ratification (2026-06-13, autonomous adversarial review)

An independent fresh reviewer rendered: **ADOPT DEFAULT (Option A), with Option B as the binding
fallback, under six amended binding conditions.**

**Why A, not B or C, and not "keep open."** The v3 ceiling diagnosis is correct and well-evidenced
(v3 result §1: paraphrase control raw rates 0.78/0.96/1.00, NLI control 0.87/0.83/1.00; the
under-pressure subset +0.20/0/0 did not rescue it because it biased the *item's* local fluency, not
the *control's* baseline — the open-question update at its lines 31–44 makes the same diagnosis).
Option A attacks that named cause at the right locus (the control's unification ceiling); Option C
accepts the limit without attacking it; Option B abandons the target rather than attacking the
cause. The question is not yet *answerable*, so the open question correctly stays open — but the
decision of *how to attempt* the separation is ratifiable and is A.

**The Condition-2 minimal-pair tension is real but surmountable — only with guardrails.** A
distributive-default control imports distributive lexical cues ("each", "day by day"), so a measured
AANN-vs-control shift could be a lexical-cue artifact rather than evidence the AANN *licenses*
unification. Two things make A survivable: (a) the **grammaticalized singular-agreement sub-probe**
(governing Condition 3) is *lexical-cue-immune* — singular agreement on a plural head is
distributionally dispreferred, it is an AANN-vs-bare-plural contrast independent of the paraphrase
control's framing, and v3 already produced an off-ceiling positive there (gpt +0.74, control rate
0.22, ample headroom); it carries an interpretable discriminator forward regardless of how the new
paraphrase control is built; and (b) a **mandatory within-design lexical-cue control arm** (below)
operationalizes "the shift cannot be a lexical-cue artifact" as a measured, pre-registered
subtraction rather than an assertion. If those cannot be met, the honest call is the **Option B**
fallback (conative route), which the precedent shows already works.

**Anti-cheat — PASS.** No v4 result/pilot/run exists. Option A's appeal rests on a correct causal
diagnosis (the control ceiling), is symmetric (a properly headroom-bearing control makes a *null*
far more informative than v3's ceiling-bounded one), smuggles in no prediction of direction, and is
structurally biased *against* a free positive (the added lexical-cue control arm disqualifies a
lexical-cue shift from counting). Yardstick-fixing, not result-fixing.

### Six binding conditions on the v4 distributive-default design (frozen pre-run)

A v4 inherits all eight conditions of
[`decisions/resolved/aann-inferential-operationalization`](aann-inferential-operationalization.md)
**except** the Condition-2 amendment below, which must be re-justified in the frozen v4 design.
Adding:

1. **Headroom precondition (the v3 cause must be demonstrably removed).** The new
   distributive-default control must show, in a pre-registered manipulation/sanity check, that its
   *baseline* control unification-reading rate is materially off-ceiling (target ≤ 0.30; hard
   ceiling ≤ 0.50) for each model **before** the AANN contrast is interpreted. If the control still
   reads unification at ceiling, the design has not removed the v3 cause and must not proceed
   (route to the Option-B fallback). Testable pre-headline.
2. **Mandatory within-design lexical-cue control arm.** Because the distributive-default control
   imports lexical cues, the design **must** include a third arm: a **non-AANN string carrying the
   *same* distributive lexical cue** but without the AANN construction (e.g. "On each of the three
   beautiful days…" as a plural vs the AANN "a beautiful three days"). The interpretable quantity is
   a **double contrast**: the AANN must shift toward unification *more* than the lexical cue alone
   moves a matched non-AANN string. If the whole measured shift is attributable to the lexical cue
   (the cue-control moves as much as the AANN-vs-distributive-control gap), the paraphrase arm is
   declared a **lexical-cue artifact** and cannot carry the headline. This arm is what makes the
   amended Condition 2 defensible.
3. **Lexical-overlap parity re-justified, not waived.** The original Condition-2 lexical-overlap
   parity between the two *paraphrase options* stays in force. What is amended is only that the
   *control premise* now differs lexically from the AANN premise by design; that asymmetry must be
   quantified per-item in the frozen stimuli and is exactly what arm (2) neutralizes. The amendment
   must be written into the v4 design and re-justified against this verdict.
4. **The agreement sub-probe remains the load-bearing discriminator (governing Condition 3
   unchanged), and its control stays the bare plural** (not the new distributive-default control),
   reported separately and weighted above the paraphrase arm. The headline-gating rule stands: a
   paraphrase shift without the agreement reflex is "shift in paraphrase selection without the
   grammaticalized reflex," not "draws the unification inference."
5. **`anchor: internal-contrast-only` and the verbatim chief-cost statement carry forward**
   (governing Condition 5). No human inference data exists; this ratification cannot change that.
   The literature key stays expert-stipulated.
6. **The named-null fallback is binding and is the fallback to Option B.** If, at design or
   independent-pre-run-critic time, no distributive-default control can satisfy conditions 1–2, the
   design **must not run**; the disciplined outcome is to record the inferential half as terminally
   untestable-at-paraphrase-instrument for AANN and **redirect to Option B** (the cancel-direction /
   conative route), per Option A's own fallback trigger and the v3 design template's §7 named null.

### Contingent-artifact disposition

Both named contingent artifacts **stay as they are**; resolving this decision changes neither's
status.

- [`conjecture/aann-construction`](../../findings/conjectures/aann-construction.md) — stays
  **`tested`**. Its gradient half is SUPPORTED (v2); its inferential half is correctly recorded as a
  ceiling-bounded null / untestable-at-this-instrument. Adopting Option A authorizes a *future* v4
  redesign; it does **not** revert the conjecture to `designed` or reopen the inferential clause as
  supported. The conjecture's existing language already anticipates "a future probe needs a control
  whose default reading is *distributive*."
- [`open-question/distributional-vs-inferential-constructional`](../../findings/open-questions/distributional-vs-inferential-constructional.md)
  — stays **`open`**. Option A is a plan to *attempt* the separation, not a demonstration that it
  succeeds. It remains open until a v4 (or the Option-B conative route) actually produces a contrast
  that separates inferential from distributional sensitivity.
