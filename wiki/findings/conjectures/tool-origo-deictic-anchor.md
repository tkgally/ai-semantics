---
type: conjecture
id: tool-origo-deictic-anchor
title: "Given a clock/location tool and an UNANCHORED 'now'/'here', the panel will spontaneously query the tool and resolve to tool-state — an as-if deictic anchor (content-half sibling of the character probe)"
meaning-senses:
  - referential
  - grounded
status: proposed
contingent-on: []
created: 2026-06-30
updated: 2026-06-30
links:
  - rel: depends-on
    target: essay/indexical-character-learnable-content-supplied
  - rel: refines
    target: essay/origo-supplied-not-occupied
  - rel: depends-on
    target: source/braun-2015-indexicals-sep
  - rel: depends-on
    target: result/indexical-character-application-v1
---

# Conjecture: the tool as a deictic anchor (the as-if origo probe)

> **Status: proposed (2026-06-30). DESIGN / PRE-REGISTRATION ONLY — no probe is run this session, nothing is spent.** This page pre-registers exactly **one** tightly-scoped *behavioral* question and bounds it hard. It is the **content-half sibling** of the character-half probe [`result/indexical-character-application-v1`](../results/indexical-character-application-v1.md): that result tested whether the panel applies an indexical's *character-rule* to a fully **described** origo (it does, at ceiling); this conjecture asks the strictly different, narrower question of what the panel does with an **unanchored** ‘now’/‘here’ when a clock/location *tool* is available. A positive result would be an **as-if behavioral contrast** at `anchor: internal-contrast-only` strength — **no human comparison**, and **no certification** that the model "occupies" a context. See *Scope cap* before citing any sentence here.

## What this refines

The parent essay [`essay/indexical-character-learnable-content-supplied`](../essays/indexical-character-learnable-content-supplied.md) pre-registered, as its **trigger (b)**:

> "**(b) The model is given an origo.** A finding in which the system is supplied a *live* context it occupies (a tool-augmented setup with a real clock/location as its own deictic anchor, or a grounded/embodied probe) would test whether content can shift from premise-supplied to situation-supplied. If it can, the 'no deictic origo' claim becomes **regime-dependent**, not architectural, and this essay must be scoped to the text-only regime."

The sibling essay [`essay/origo-supplied-not-occupied`](../essays/origo-supplied-not-occupied.md) argues that this single trigger conflates three claims that must be kept apart:

- **(i) an *architectural* claim** — the model occupies no Kaplanian context (it "is not the agent of an utterance situation; it is not at a location; its 'now' is not a clock time it inhabits", parent essay, §"The two halves"). This is not behaviorally testable.
- **(ii) a *channel* claim** — every origo, including a tool-return like `get_current_time()`, reaches the model as **described** text, so a tool does not make a described origo *occupied*. The parent essay's load-bearing line: "a prompt-supplied date is *text the model conditions on* — a **described** origo — not a context the model is the agent of … the architectural fact the essay leans on is precisely that this is the *only* channel by which a context can reach it" (§"The two halves"). A tool-return is more of the same channel, not a new one.
- **(iii) a *behavioral as-if* question** — the one thing that **is** testable: *given a clock/location tool, does the model spontaneously treat tool-state as the deictic anchor for an **unanchored** ‘now’/‘here’ — querying the tool rather than resolving from narrated text?*

This conjecture pre-registers **exactly (iii)**, honestly bounded. A positive on (iii) shows the model behaves *as if* tool-state is its origo; the sibling essay's conclusion — which this page adopts as its ceiling — is that such a positive **cannot certify (i) or (ii)**, because the tool-return is itself described text. The probe is therefore interesting yet strictly bounded.

## The bet (the proposed claim)

> **When — and only when — the textual context leaves ‘now’/‘here’/‘today’ *unanchored* (no narrated origo) AND a clock/location tool is available, the panel will spontaneously query the tool and resolve the indexical to tool-state.** That is, on an unanchored deictic item the model treats the tool as a deictic anchor: it issues the tool call without being told to, and binds the indexical's content to the value the tool returns.

The bet is **directional and behavioral**, not a claim about internals. Stated as Kaplan's content half ([`source/braun-2015-indexicals-sep`](../../base/sources/braun-2015-indexicals-sep.md), §3.2: "The content of ‘here’ … is the location of \(c\). The content of ‘now’ is the time of \(c\)"): on an unanchored item the text supplies **no** agent/time/location for ‘c’, so the only available source of a content-value is the tool. The bet is that the panel reaches for it spontaneously.

**The deflationary alternative (stated plainly, so the bet can lose).** The panel does **not** spontaneously treat the tool as an origo. Faced with an unanchored ‘now’/‘here’ it instead does one of: (a) **refuses or hedges** ("I don't have a current time"), (b) **resolves to a described/default value** narrated elsewhere in the prompt or to a generic placeholder, or (c) **answers from a parametric/training-prior default** without calling the tool at all. On the deflationary reading the tool is just another describable resource the model uses *when instructed*, never an origo it adopts *unbidden*.

These two readings make **opposite** predictions on the same items, which is what gives the probe its (bounded) bite.

## Design sketch (a sketch, NOT a frozen PREREG)

A frozen pre-registration — exact items, gold keys, thresholds, manifest sha — is a future **build session's** job (and must clear the deferred gate below first). This is only the shape.

- **Tool-calling setup.** Expose a single function-calling tool to the panel — e.g. `get_current_time()` and/or `get_current_location()` — with a real (or deterministically stubbed-and-logged) return. Tool-call traces are captured verbatim so a *spontaneous* call is distinguishable from a prompted one. The system prompt must **not** instruct the model to use the tool for time/place; the tool is merely *available*.
- **The contrast (three arms over matched items):**
  - **Anchored control (tool available).** The text narrates an origo ("Right now, in Tokyo, it is 09:00 on June 30…") and asks an indexical question whose content is fully fixed by the narrated origo. *Correct behavior:* resolve from the described context and **not** spuriously override it with the tool. This is the control that the panel reads narrated origos correctly even with a tool present — without it, a high tool-query rate on the test arm is uninterpretable.
  - **Unanchored test (tool available).** The text leaves ‘now’/‘here’/‘today’ **unanchored** — no narrated agent/time/location — and asks an indexical question whose content can only come from tool-state. *As-if positive:* spontaneous tool query + resolution to tool-state.
  - **No-tool baseline.** The same unanchored items with **no** tool exposed. This separates "treats tool as origo" from "answers unanchored ‘now’ from a parametric default anyway": the baseline measures the refuse/hedge/default rate when no tool exists, against which the test arm's tool-query rate is the as-if signal.
- **The as-if metric (two rates, pre-specified direction):**
  1. **Spontaneous-query rate** — fraction of unanchored test items on which the model issues the tool call *without* being told to.
  2. **Resolution-to-tool-state rate** — fraction on which the indexical's content is bound to the value the tool returned (verified against the captured tool return, not a fixed key).
  A clean as-if positive is **high on both** in the test arm, with the anchored control resolving from the narrated origo (low spurious-override) and the no-tool baseline showing the deflationary fallbacks (refuse/hedge/default).
- **Guards (contamination / artifact):**
  - **Nonce / fresh values.** Use tool returns the model cannot have memorized (nonce dates/places, or randomized-per-call values logged at run time) so "resolved to tool-state" cannot be a training-prior coincidence.
  - **Spontaneity guard.** Strip every imperative-to-use-the-tool from the prompt; treat any item whose framing leaks "call the tool" as void. Distinguish a genuinely *spontaneous* call from compliance with an instruction.
  - **De-confound query from answer.** A model can call the tool and *still* answer from a default; score query and resolution **separately**.
  - **Order/format guards** in the lineage of the relational line's hard-won lesson that surface geometry can masquerade as the effect of interest (cf. [`result/indexical-character-application-v1`](../results/indexical-character-application-v1.md) and its predecessors): balance item order, avoid making the tool the only salient affordance.
  - **Panel + temperature** per house convention ([`config/models.md`](../../../config/models.md)), models as **subjects** (charter §6), temperature 0, one date, zero-shot, billed `usage.cost` recorded.

## Scope cap (LOAD-BEARING — read before citing)

A positive result on this probe is an **as-if behavioral contrast ONLY**. Concretely, it would license a within-model statement of the form *"on these unanchored items, given a clock/location tool, the panel spontaneously queries the tool and binds ‘now’/‘here’ to tool-state at rate R, where the anchored control resolves from the narrated origo and the no-tool baseline does not."* It would **not** license any of the following, and the page commits to that in advance:

- **It does NOT certify the architectural claim (i)** — that the model "occupies" a Kaplanian context. Spontaneously querying a tool and binding to its return is *behavior consistent with* treating tool-state as an origo; it is not evidence that the model *is the agent of* a context in Kaplan's sense.
- **It does NOT bear on the channel claim (ii).** A tool-return is itself **described text the model conditions on** — exactly the parent essay's "a prompt-supplied date is *text the model conditions on* — a **described** origo … the *only* channel by which a context can reach it" ([`essay/indexical-character-learnable-content-supplied`](../essays/indexical-character-learnable-content-supplied.md), §"The two halves"). So even a perfect as-if positive leaves the described/occupied distinction untouched: the model resolving to tool-state has resolved to *more described context*, supplied through a different surface (a function return rather than a system-prompt sentence), not to a context it occupies. The probe **cannot** turn a described origo into an occupied one; that is the sibling essay's central point and this conjecture's hard ceiling.
- **It does NOT make any human comparison, in either direction.** No human baseline is claimed, measured, or needed. The eventual result would carry **`anchor: internal-contrast-only`** (a within-model, as-if behavioral contrast across the three arms) — the same posture as [`result/indexical-character-application-v1`](../results/indexical-character-application-v1.md). It says nothing about whether people treat a clock as their origo.
- **It does NOT touch the character half.** Character-application to *described* origos is already covered (and unfalsified) by [`result/indexical-character-application-v1`](../results/indexical-character-application-v1.md); this probe is purely about the *content* half under the unanchored-plus-tool condition.

## The deferred gate (do NOT pre-resolve here)

Before any run makes a claim **stronger than as-if** — in particular, before any run treats a spontaneous tool-query-and-resolve as bearing on whether the model "occupies" a context — the run session **MUST** surface a `wiki/decisions/open/` **operationalization gate**:

> *"Can any tool-return count as an **occupied** (situation-supplied) origo rather than a **described** (premise-supplied) one — and if so, by what operational criterion?"*

This page **does not** pre-resolve that gate; it **flags** it. The parent essay and the sibling essay both lean on the channel claim (ii) that a tool-return is described text, and the sibling essay's conclusion is that the as-if probe *cannot* settle it. So the gate is genuinely open: a future session must either (a) run the probe at strict `internal-contrast-only` / as-if strength with **no** occupation claim (no gate needed for that bounded reading), or (b) if it wants to argue the tool makes the origo occupied, open the gate with options and a provisional default per [`CLAUDE.md`](../../../CLAUDE.md) rule 5, mark the result contingent on it, and leave ratification to a *later* independent adversarial pass ([`PROJECT.md`](../../../PROJECT.md) §12.3). Pre-resolving "a tool makes it occupied" inside the run that wants the conclusion is exactly the move the house rules forbid.

## Confirmation / falsification criteria (pre-registered)

Concrete, fixed in advance; a build session may tighten thresholds in its frozen PREREG but may not loosen the *shape*.

- **CONFIRM (the as-if bet holds).** On the **unanchored test** arm, **spontaneous-tool-query rate AND resolution-to-tool-state rate both ≥ a pre-stated threshold (sketch: ≥ 0.80)** in **≥ 2 of 3** panel models, **with** the **anchored control** behaving correctly (resolves from the narrated origo; does not spuriously override it with the tool above a low pre-stated false-override rate) **and** the **no-tool baseline** showing the model does *not* already produce the tool-state answer without the tool (i.e. the test-arm signal is attributable to the tool, not to a parametric default). Reported strictly as an **as-if** contrast, `internal-contrast-only`; explicitly **not** as "the model occupies a context."
- **FALSIFY / NULL (the deflationary alternative holds).** On the unanchored test arm the panel predominantly **refuses, hedges, resolves to a described/default value, or answers from a parametric default without querying the tool** — i.e. spontaneous-query and/or resolution-to-tool-state fall **below threshold** in ≥ 2 of 3 models. A null is a first-class result and would say: even handed a clock/location tool, a text-only model does **not** spontaneously adopt tool-state as a deictic origo for an unanchored ‘now’/‘here’ — consistent with the parent essay's "no deictic origo" reading at the *behavioral* grain (without bearing on (i)/(ii)).
- **MIXED reported as MIXED.** Models split, or query-without-resolve (calls the tool but answers from a default), or the anchored control fails (the panel can't even resolve narrated origos with a tool present), or the no-tool baseline already yields the tool-state answer (signal not tool-attributable) — each is reported as the mixed/uninterpretable picture it is, not rounded to either pole. As with the character probe, an uninterpretable control voids the test-arm reading.

## Candidate anchor (named, per house rules — none claimed)

The as-if metric (spontaneous-query rate, resolution-to-tool-state rate) is a **within-model contrast across the three arms** (anchored control vs. unanchored test vs. no-tool baseline, same models throughout) and is **`internal-contrast-only`** — it makes **no human-comparison claim**, the same posture ratified for [`result/indexical-character-application-v1`](../results/indexical-character-application-v1.md) (via [`decisions/resolved/indexical-character-anchor-type`](../../decisions/resolved/indexical-character-anchor-type.md)). So a result from this probe would carry **no resource-anchor obligation** for the as-if measure itself. This conjecture therefore needs no resource anchor to stand as a forward, bounded behavioral bet; the only open governance item is the deferred occupation gate above, which a stronger-than-as-if reading would trigger.

## Honesty box

- **As-if only.** Every confirming reading is "behaves *as if* tool-state is its origo," never "occupies a context." The scope cap is the point of the page, not a hedge.
- **The tool-return is described text.** This is the sibling essay's load-bearing channel claim and this conjecture's ceiling; a positive cannot convert a described origo into an occupied one.
- **No human comparison.** `internal-contrast-only` in force for the eventual result.
- **Design sketch, not PREREG.** Items, keys, thresholds, and manifest are deferred to a build session, which must also clear the occupation gate before any stronger-than-as-if claim.
- **Modest framing.** Per the charter, this is a bounded behavioral bet: it predicts a specific spontaneous behavior on unanchored items, names the deflationary alternative that would null it, and fixes the verdict shape before any run.
