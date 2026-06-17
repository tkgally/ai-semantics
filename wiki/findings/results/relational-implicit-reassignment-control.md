---
type: result
id: relational-implicit-reassignment-control
title: The implicit-reassignment control — latest-binding-wins survives without the explicit "was reassigned" flag (both models still SPONTANEOUS-RECENCY); the Option-A order-sensitivity is not a wording artifact
meaning-senses:
  - relational
  - model-internal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-17
updated: 2026-06-17
links:
  - rel: depends-on
    target: result/relational-spontaneous-recency-a
  - rel: supports
    target: claim/relational-order-sensitive-reassignment
  - rel: depends-on
    target: result/relational-stamp-comprehension-b
  - rel: depends-on
    target: concept/relational-meaning
---

# Result: implicit-reassignment control — latest-binding-wins survives without the explicit "was reassigned" flag

> **Status: proposed (2026-06-17).** The **implicit-reassignment control** of
> [`result/relational-spontaneous-recency-a`](relational-spontaneous-recency-a.md) (Option A).
> Option A found both panel models recover a **reassigned** coined term by its most-recent binding,
> spontaneously → [`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md).
> That claim's sharpest open caveat (scope limit 4 / revision trigger 2) was that "spontaneous"
> meant *query-not-directed, not cue-free*: Option A's INTRO told the model the term *"was
> reassigned … in different rounds you agreed it referred to different figures."* **This control
> removes exactly that sentence and re-measures the SPONT latest-binding rate. The result is clean
> and identical across both models: latest-binding-wins persists at ceiling.** The Option-A
> order-sensitivity is therefore **not** a surface artifact of the explicit reassignment wording.
> `anchor: internal-contrast-only` (within-model contrast over byte-identical content; no
> human-comparison claim).

## The question (precise)

[`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)
holds that both models recover a reassigned term by its **most-recent binding** when only recency
disambiguates. Its **revision trigger 2** named the decisive control verbatim: *"Evidence that the
latest-binding-wins behaviour is a surface artifact of the explicit 'was reassigned' wording (e.g.
it vanishes when reassignment is implicit) would narrow it."* The question here is exactly that:
**when the coined term simply *is* used for different figures across stamped rounds — with no
sentence flagging that a reassignment occurred — and the query does not mention recency, does the
model still spontaneously recover the most-recent binding, or does removing the explicit flag
collapse the behaviour?**

## Instrument (frozen; a single-factor control of Option A)

Run dir: [`experiments/runs/2026-06-17-relational-implicit-reassignment/`](../../../experiments/runs/2026-06-17-relational-implicit-reassignment/).
Design: [`relational-implicit-reassignment-v5`](../../../experiments/designs/relational-implicit-reassignment-v5.md).

- **The sole manipulation vs Option A: the INTRO drops the explicit reassignment flag.** Option A's
  INTRO said *"The term was reassigned: in different rounds you agreed it referred to different
  figures."*; this control omits that sentence entirely. It **keeps** the stamp semantics ("a higher
  round number means it was said more recently") and the not-in-round-order note — the framing
  [`result/relational-stamp-comprehension-b`](relational-stamp-comprehension-b.md) proved both models
  read on demand, and which is required for the stamp to be interpretable and the DIRECT gate to be
  meaningful. The model must itself notice the term picks out different figures across rounds.
- **The frozen stimuli roster is byte-identical to Option A** (same `stimuli.json` sha256
  `432cb57d…`; the INTRO text lives in the prompt renderer, not the roster). Figures, non-contiguous
  round quadruples, balanced-block geometry, `TERM = "DAX"`, seed, the two query conditions (SPONT
  48/model headline + DIRECT 32/model manipulation check), forced single-label elicitation, parse,
  scoring, and the verdict map are all carried unchanged. So the **only** difference between this run
  and Option A is the one dropped sentence — a clean single-factor control.
- **Shortcut-proof by construction.** Every constant-physical-history-slot strategy, every fixed
  figure-preference ordering (incl. grid order), and the frequency heuristic all score **exactly
  1/K = 0.25** — proven at build and on six idealized-reader fixtures. An **independent pre-run
  critic** (fresh agent) re-derived every bound from scratch with its own script (best non-recency
  shortcut on SPONT: Wilson-95 LB 0.149, below the 0.25 bar), ran the fixtures, mechanically verified
  the manipulation over all 80 rendered prompts, and ruled the construct an **authorized control of
  the existing claim** needing **no new decision** — **GO**.
- Forced single-label elicitation; strict parse; `finish_reason == "length"` never parsed.

## The headline (verified — numbers not altered)

Latest-binding-wins persists at ceiling, identical across both separately-trained models:

| model | SPONT latest-binding rate | Wilson 95% | SPONT first-binding rate | pick==last-line | pick==first-line | DIRECT manip-acc (MR / LR) | NA | verdict |
|---|---|---|---|---|---|---|---|---|
| claude-sonnet-4.6 | **1.000** (48/48) | [0.926, 1.000] | 0.000 | 0.250 | 0.250 | **1.000** (1.000 / 1.000) | 0 | **SPONTANEOUS-RECENCY** |
| gemini-3.5-flash | **1.000** (48/48) | [0.926, 1.000] | 0.000 | 0.250 | 0.250 | **1.000** (1.000 / 1.000) | 0 | **SPONTANEOUS-RECENCY** |

- **SPONT latest-binding rate = 1.000** for both, Wilson lower bound 0.926 — far above the 0.25
  chance floor every position/lexical/frequency shortcut is pinned to. The models put **100%** of
  their SPONT mass on the figure agreed at the **maximum** round, **without** the "was reassigned"
  scaffolding.
- **first-binding rate = 0.000; physical-position-following at exactly chance** (0.250 / 0.250) —
  genuine stamp-recency reading, specifically recency (latest wins), not a text-position artifact.
- **DIRECT manipulation check = 1.000** on both directions — on-demand comprehension is intact in
  this instrument **even without the reassignment flag**, so the SPONT result is interpretable.
- **Clean record:** 160/160 strict parses, 0 NA, 0 retried, 0 length-truncation.
- **Numerically indistinguishable from Option A** (which was also 1.000 / 0.000 / chance / 1.000):
  removing the explicit flag changed **nothing** in the measured behaviour.

**Discipline.** Independent pre-run critic GO (re-derived shortcut bounds from scratch; certified
unsolvable-by-shortcut; ruled the control authorized). Independent **post-run verifier** reproduced
every number from raw via its own route (re-derived the max/min-round keys directly from the rendered
lines, audited parses and cost, confirmed the frozen sha256, confirmed the implicit prompt rendered)
— **REPRODUCED**, 0 mismatches.

## What this shows — and what it does NOT (binding scope)

**Shows (within-model, internal-contrast-only):** the Option-A latest-binding-wins behaviour is
**robust to removing the explicit reassignment flag**. When a coined term is simply used for
different figures across stamped rounds — with no sentence telling the model a reassignment occurred
— both models still spontaneously recover the **most-recent** binding, at ceiling. So the
order-sensitivity Option A found is **not** a surface artifact of the "was reassigned" wording: it
survives when the only cue is the stamped history itself. This **bounds revision trigger 2** of the
claim in the claim's favour and **tightens scope limit 4**: "spontaneous" was already
query-not-directed; it is now also **flag-not-directed** (the model is not even told that a choice
among bindings is required — it infers the multiplicity from the history and resolves it by recency).

It does **NOT** show:

- **Not "rich constitution."** Exactly as in Option A, latest-binding-wins is consistent with a thin
  **convention-update / overwrite** rule ("the latest agreement supersedes earlier ones"), which is
  order-sensitive but is **not** the deep [`concept/relational-meaning`](../../base/concepts/relational-meaning.md)
  notion of a convention *constituted between* agents through a live trajectory. This control removes
  a *wording*-artifact worry; it does **not** separate thin order-sensitivity from deep
  path-dependence. The claim stays held to order-sensitivity, not constitution.
- **Not literally cue-free.** The stamped history *is* a cue: the model is shown that DAX was used
  for four figures across rounds. What this control removes is the *explicit framing sentence*, not
  the structural fact that the history is multi-valued. "Implicit" here means **no sentence flags the
  reassignment**, not that no information distinguishes the bindings.
- **Not a human comparison** (`anchor: internal-contrast-only`). No in-repo resource grounds human
  order-/path-sensitivity at this grain; none is owed because no human contrast is asserted.
- **Not a new effect.** This is a control, not a new finding direction: it raises confidence in the
  existing Option-A positive by removing one alternative explanation. The remaining open generality
  questions (image referents, cross-family dyads, non-overwrite repairs, thin-vs-rich separation)
  are untouched and stay open.

## Why it matters

Option A's clean positive carried one obvious deflationary escape: maybe the models tracked recency
only because the INTRO *told* them a reassignment had happened — a prompt artifact, not a property of
how they recover conventions. This control closes that escape. With the flag gone and everything else
byte-identical, both models behave exactly as before. The order-sensitivity of LLM referential
convention-recovery (in the regime where recency disambiguates) is one alternative explanation more
robust. The result is folded back into
[`claim/relational-order-sensitive-reassignment`](../claims/relational-order-sensitive-reassignment.md)
(scope limit 4 tightened, revision trigger 2 bounded), which stays `supported` and
`internal-contrast-only`.

## Honesty box

- **Ceiling effect, two independent models, n=48/model SPONT, identical to Option A.** Wilson LB
  0.926, position at exactly chance, DIRECT at ceiling, 0 NA. As clean as a behavioural contrast
  gets — but **saturated**: 48/48 censors the effect magnitude at the ceiling (it is "≈1.000", not a
  distribution), so the control establishes *robustness of direction*, not a finer magnitude estimate.
- **One control, one operationalization of "implicit."** Dropping the one framing sentence is one way
  to make reassignment implicit. A more aggressive implicitness (e.g. burying the multiplicity, or
  never using the word "agreed") is untested; this result is scoped to the registered manipulation.
- **Thin vs rich still un-separated.** This control removes a wording-artifact worry; it does not
  move the claim toward or away from the constitution rung.
- **Spend.** 160 finding-bearing calls + 2 liveness = **$0.118248 billed** (`usage.cost`-summed,
  0 missing), inside the $0.50 per-run hard stop and the $5.00/day cap (day total $0.118).
