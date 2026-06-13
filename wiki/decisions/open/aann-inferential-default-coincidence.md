---
id: aann-inferential-default-coincidence
title: How to test a construction's inferential use when its licensed inference COINCIDES with the distributional default — the v3 ceiling problem
status: open
opened: 2026-06-13
opened-by: autonomous (workflow session 2026-06-13, third session — v3 inferential run follow-up)
provisional-default: Option A (engineer a distributive-default control) — with Option B as the named fallback if a clean such control cannot be built
contingent-artifacts:
  - conjecture/aann-construction
  - open-question/distributional-vs-inferential-constructional
---

# Decision: testing constructional inference when inference and distributional default coincide

> **OPENED 2026-06-13 (this session). NOT yet eligible for ratification** — surfacing and
> ratifying must be separated by at least one session boundary (PROTOCOL §2). A later session may
> ratify by independent adversarial review, or Tom may rule directly.

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

- **Option A — engineer a distributive-default control (provisional default).** Replace the
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
  untestable-at-this-instrument rather than testing it.
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
[`decisions/resolved/aann-inferential-operationalization`](../resolved/aann-inferential-operationalization.md)
except where the control redesign explicitly amends Condition 2 (the minimal-pair/overlap-parity
clause), which must then be re-justified.

## Separable side-note (not part of this decision)

The v3 run produced one real positive signal — gpt-5.4-mini's **grammaticalized singular-agreement
reflex** (+0.74, *was* for AANN vs *were* for control). That is a `functional-vs-formal` *form*
reflex, not the inferential discriminator this decision concerns. Whether to run a dedicated
**grammatical-reflex** probe (does the AANN singular-agreement reflex generalize across the panel
and across held-out items?) is a separate, lower-stakes design question that needs no new
operationalization gate (it reuses the v2 form-instrument family) and can be picked up independently
of this decision.
