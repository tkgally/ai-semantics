---
type: result
id: accommodation-cue-strength-v1
title: "The accommodation gate is GRADED by surface-contradiction strength (verdict GRADED-GATE 3/3): every model backs off a denied presupposition harder under an emphatic denial than under a hedged one"
meaning-senses:
  - inferential
  - distributional
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-02
updated: 2026-07-02
links:
  - rel: supports
    target: conjecture/presupposition-environment-gated-both-directions
  - rel: refines
    target: result/presupposition-accommodation-v1
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: the accommodation / cue-strength probe v1

The follow-up to the accommodation v1 run
([`result/presupposition-accommodation-v1`](presupposition-accommodation-v1.md), verdict
GATED-ACCOMMODATION 3/3). v1 found a **partial** accommodation gate: under a single "contradicting"
context the panel still endorsed the explicitly-denied presupposition a third to a half of the time.
This probe asks whether that gate is **graded by cue strength** — does a **stronger** surface
contradiction gate **harder** than a weaker one? — by splitting v1's single contradiction into a
**weak** (hedged) and a **strong** (emphatic) denial of the same proposition P, holding the trigger
sentence and P constant. It tests the cue-strength **confirming** arm of
[`conjecture/presupposition-environment-gated-both-directions`](../conjectures/presupposition-environment-gated-both-directions.md).
Run record:
[`experiments/runs/2026-07-02-accommodation-cue-strength/`](../../../experiments/runs/2026-07-02-accommodation-cue-strength/README.md);
frozen [`PREREG.md`](../../../experiments/runs/2026-07-02-accommodation-cue-strength/PREREG.md),
manifest sha `24a48564…`.

**One-line finding.** The pre-registered verdict is **GRADED-GATE (3/3)**. Every model accommodates
the unmet presupposition at ceiling in the neutral context (neutral-endorse **1.00 / 1.00 / 1.00**),
and every model **endorses the denied P more often under a hedged denial than under an emphatic one**
(weak-endorse **0.42 / 0.67 / 0.83** vs strong-endorse **0.08 / 0.50 / 0.17**), clearing the frozen
graded bar (strength-gradient **+0.33 / +0.17 / +0.67**, all ≥ 0.15). So v1's partial gate is not an
on/off contradiction switch: within each model, endorsement of the backgrounded content falls **as the
surface contradiction gets stronger**. That is the conjecture's stated confirming signature.

## Scope — LOAD-BEARING (read before citing)

**Within-model contrast only; no human comparison.** The signal is a *within-model asymmetry across
four contexts* on the same trigger — accommodate in neutral, back off more as the denial strengthens —
**not** *the model matches human accommodation behavior*. No human accommodation baseline is claimed,
measured, or needed. The result does **not** certify that a model *represents* presupposition-vs-
assertion or accommodation semantically; it reads endorsement of backgrounded content off
forced-choice answers.

**The genuine-blocking vs contradiction-detection ambiguity carries over, now sharpened by the
verdict.** v1's pre-run critic noted the gate leg cannot behaviorally separate accommodation-*blocking*
from generic contradiction-detection + yes-bias. This probe does not dissolve that ambiguity — but it
adds discriminating texture (pre-registered): a mechanism that is *pure* contradiction-detection (any
explicit ¬P → NO) predicts weak and strong denials gate **equally** (both contain an explicit ¬P) → a
**FLAT** gate; a mechanism sensitive to *surface cue strength* predicts a **graded** gate. The
observed GRADED-GATE is the second signature — the models are sensitive to *how strongly* the
contradiction is worded, not just to its presence. This is a reading of the within-model contrast,
**not** a claim the model computes accommodation; both readings are distributional.

**Anchor is `anchor: internal-contrast-only`** (terminal), **inherited** — not newly opened — from the
ratified precedent
[`decisions/resolved/presupposition-accommodation-internal-contrast-anchor`](../../decisions/resolved/presupposition-accommodation-internal-contrast-anchor.md)
(opened session 162, ratified session 163 by an independent fresh-agent adversarial review). The
scoring path is identical in kind to v1 — every quantity feeding the verdict is a within-model
endorsement rate over the model's own YES/NO/UNCLEAR answers, with **no human key** — so the same
terminal declaration applies and **no new `wiki/decisions/open/` entry is opened**.

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A),
  `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C), as subjects. Temperature 0; text-only,
  single-turn, zero-shot; gemini `reasoning={"effort":"minimal"}`. The neutral system prompt and
  forced-choice QUERY wrapper are reused **verbatim** from v1 and never mention presupposition,
  accommodation, or the right answer.
- **Items.** The SAME 12 v1 base scenarios across **4 trigger families** (factive / aspectual /
  definite / cleft; 3 each), trigger sentence and P held constant verbatim from v1, × **4 context
  conditions** — `supported` (states P; sanity floor) / `neutral` (topic-adjacent; the accommodation
  test) / `weak_contra` (a hedged denial of P) / `strong_contra` (an emphatic denial of the same P) =
  **48 item-conditions** per model, **144 calls** total. weak_contra and strong_contra deny the
  **same** proposition ¬P and differ **only in surface strength** (downtoner — "apparently not",
  "reportedly not", "seemingly" — vs intensifier + absolute — "never … at all", "no … whatsoever",
  "definitely not … at all"), with context length held close (per-item word delta strong − weak in
  −1..+2, mean +0.42, mixed sign — see [`PREREG.md`](../../../experiments/runs/2026-07-02-accommodation-cue-strength/PREREG.md)
  §Confounds; `prep.py --check` asserts |Δ| ≤ 2 per item). One v1 fix carried: `cle2`'s neutral was
  changed from the mildly-leaky "The contract ran for three years." to the orthogonal "The conference
  room overlooked the harbor." (the only change to any reused v1 sentence).
- **Cost.** **$0.0259 billed** (`usage.cost`-summed: claude $0.0154 / gpt $0.0045 / gemini $0.0060),
  0 missing cost, **0 unparsed** answers; pre-flight 4 calls $0.0013. Session total **$0.0272**, far
  under the $2.50 single-run flag; UTC-2026-07-02 day total after this run **$0.0272** of $5.00.
- **Discipline.** Frozen before any call (FREEZE GUARD on manifest sha `24a48564…`); an **independent
  pre-run critic** (session 163) returned **GO-WITH-NOTES**, its one SHOULD-FIX (the `fac1` weak cell
  was mere uncertainty, not a denial) applied and the set re-frozen before the run; an **independent
  post-run verifier** recomputed every rate and the gradient from the raw answers by its own route and
  reproduced the table and the GRADED-GATE (3/3) verdict exactly (**VERIFIED**), including the
  robustness check below.

## Numbers (from `results.json`; independently reproduced)

**Per model** (P-endorse rate per condition; gradient = weak − strong; gap = neutral − strong):

| model | supported | neutral | weak_contra | strong_contra | strength-gradient | accom-gap | sanity | label |
|-------|-----------|---------|-------------|---------------|-------------------|-----------|--------|-------|
| A claude-sonnet-4.6 | 1.00 | 1.00 | 0.42 | **0.08** | **+0.33** | +0.92 | ✓ | graded_gate |
| B gpt-5.4-mini | 1.00 | 1.00 | 0.67 | 0.50 | **+0.17** | +0.50 | ✓ | graded_gate |
| C gemini-3.5-flash | 1.00 | 1.00 | 0.83 | **0.17** | **+0.67** | +0.83 | ✓ | graded_gate |

**Per family** (weak_contra → strong_contra endorse — where the graded drop lives; supported =
neutral = 1.00 everywhere):

| model | factive w→s | aspectual w→s | definite w→s | cleft w→s |
|-------|-------------|---------------|--------------|-----------|
| A | 0.33 → 0.00 | 0.33 → 0.33 | 0.00 → 0.00 | 1.00 → 0.00 |
| B | 1.00 → 1.00 | 0.33 → 0.00 | 0.33 → 0.33 | 1.00 → 0.67 |
| C | 0.67 → 0.33 | 0.67 → 0.00 | 1.00 → 0.00 | 1.00 → 0.33 |

**Verdict** (frozen thresholds SANITY 0.75 / ACCOM 0.60 / GAP 0.30 / GRAD 0.15 / FLATBAND 0.10 /
NOGATEBAND 0.15 / LOWACC 0.40): graded = {A,B,C}, flat = {}, blanket = {}, none = {} → 3/3 majority →
**GRADED-GATE**.

## Reading it

- **The gate is graded, not on/off.** All three models endorse the denied P more often under the
  hedged denial than under the emphatic one (gradient +0.33 / +0.17 / +0.67, all ≥ 0.15). A pure
  contradiction-detector — flip to NO whenever an explicit ¬P is on the surface — would gate weak and
  strong **equally** (a FLAT gate), because both conditions contain an explicit ¬P. It did not: the
  models are sensitive to *how strongly* the denial is worded. The strong contradiction pushes
  endorsement to the floor for A (0.08) and near it for C (0.17); the hedged one leaves substantially
  more of the presupposition standing.
- **Accommodation itself is unchanged and at ceiling.** Neutral-endorse is 1.00 for all three (up from
  v1's 1.00 / 0.92 / 1.00), so there is a full accommodation effect to grade. The `cle2` neutral fix
  did not lower the neutral rate — accommodation in the neutral context stays indiscriminate-looking,
  which is the point: the grading lives entirely in the two contradiction cells.
- **B is the shallow-gradient model, but it clears the bar and is robust.** gpt-5.4-mini's gradient is
  +0.17, only ~0.02 (a fifth of one item) above the GRAD = 0.15 bar. Per the PREREG's residual guard,
  the post-run verifier read all 12 of B's weak_contra texts: 11/12 are unambiguous hedged denials;
  the one borderline item (`fac2`, "It was doubtful that the figures had been changed" — probabilistic
  ¬P) contributes **zero** to B's gradient (B answered YES under both weak and strong there), so
  **excluding it raises B's gradient to +0.18**, still clearing GRAD. B's graded_gate label survives
  the robustness check. Its shallowness is real texture: B is also the model with the highest
  strong-contra endorsement (0.50) — it backs off least even under an emphatic denial, the residual
  yes-bias pocket v1 located on B's existentials showing up here as a family that gates weakly (factive
  1.00 → 1.00, cleft 1.00 → 0.67).
- **Where the drop lives, by family.** The graded drop is carried by aspectual, definite, and cleft
  triggers; factive is where B does not gate at all. This mirrors v1's non-uniformity: the panel-level
  graded verdict is real, but per-family the gate is stronger on some triggers than others, and one
  model has a family (factive) where even a strong denial does not move it. Reported, not smoothed.

## What it feeds

- **Confirms the conjecture's cue-strength arm.** This is exactly the confirming evidence
  [`conjecture/presupposition-environment-gated-both-directions`](../conjectures/presupposition-environment-gated-both-directions.md)
  names: "Accommodation's partial gate turning out to be **graded by cue strength** (a stronger
  surface contradiction gates harder), paralleling projection's graded frame effect." The conjecture's
  confirming column is updated accordingly. It **strengthens** (does not prove) the bet, within the
  `internal-contrast-only` fence.
- **Supports the environment-gated essay.** GRADED-GATE is the outcome the essay
  [`essay/presupposition-environment-gated`](../essays/presupposition-environment-gated.md) hoped for
  and does **not** trigger its first revision trigger (which fires on a FLAT gate). It supports the
  "graded distributional cue" gloss on the accommodation leg — endorsement tracks *cue reliability /
  strength*, not just cue presence — the property that lets the accommodation signature parallel
  projection's graded frame effect.

## Honest bounds

- **Behavioral, within-model, no human comparison** (see Scope). `anchor: internal-contrast-only`
  (inherited); makes no claim a model *computes* accommodation; both the cue-strength and the
  contradiction-detection readings of the gradient are distributional.
- **The grading does not resolve the mechanism.** GRADED-GATE says the models are sensitive to surface
  contradiction *strength*; it does not certify a represented presupposition/assertion split. A
  cue-strength–sensitive distributional learner predicts exactly this.
- **B is marginal and one family (factive) barely gates for it.** The 3/3 verdict is carried by clear
  margins on A and C and a thin, robustness-checked margin on B; per-family, the gate is non-uniform.
- **Small Ns, n=3 models, three 2026 commercial models, 12 project-authored synthetic scenarios × 4
  conditions.** Direction-of-effect only; no coverage claim. Each threshold moves in ~0.083 steps, so
  B's verdict hinges on ~2 items — reported as texture, not smoothed.
- **Sanity is a retrieval floor.** The 1.00 supported-endorse is a control (P is literally stated);
  the graded-gate claim rests on the two contradiction cells and their difference.
