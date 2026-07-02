---
type: result
id: comparative-correlative-covariation-powered
title: Comparative-correlative POWERED re-run (A2a) — the construction-isolation, direction-flip, and atypical-robustness signatures reproduce on 136 fresh disjoint items with tight 95% intervals; the construction-isolation assertion gap is ~87pp [lower bound ~78pp], 3/3 models
meaning-senses:
  - constructional
  - inferential
  - functional-vs-formal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-02
updated: 2026-07-02
links:
  - rel: supports
    target: claim/comparative-correlative-covariation
  - rel: refines
    target: result/comparative-correlative-covariation-v1
  - rel: supports
    target: conjecture/comparative-correlative-construction
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
---

# Result: comparative-correlative covariation — POWERED re-run (A2a)

**One-line:** the three within-model signatures that [`result/comparative-correlative-covariation-v1`](comparative-correlative-covariation-v1.md) established only as founding-N threshold-passes — **construction-isolation** (the panel asserts a covariation direction for the construction but not for matched same-word controls), **direction-tracking** (inverse CCs flip the asserted direction), and **atypical-pair robustness** (no collapse on deliberately absurd scale pairs) — **reproduce on 136 fresh, disjoint, powered items with tight 95% intervals for 3/3 models.** The headline magnitude the claim deferred: the **construction-isolation assertion gap is ≈87 pp** (claude 86.8 [77.9, 94.1], gpt-5.4-mini 88.2 [77.9, 97.1], gemini-3.5-flash 86.8 [77.9, 94.1]), genuinely off-ceiling (the matched controls still spuriously assert a direction ≈12% of the time). This is a **magnitude-with-interval**, not a depth-of-processing verdict: the direction/flip/positive rates remain at or near ceiling, so the run confirms *how large and how reliable* the effect is on the tested instruments, not that the panel processes the construction the way humans do.

Run record: [`experiments/runs/2026-07-02-comparative-correlative-powered/`](../../../experiments/runs/2026-07-02-comparative-correlative-powered/README.md). Pre-registration + freeze: [`PREREG.md`](../../../experiments/runs/2026-07-02-comparative-correlative-powered/PREREG.md) (frozen `sha256(items.csv)=7662bd0a…`). Program item **A2a** ([`wiki/program.md`](../../program.md)). **Internal-contrast-only** (`anchor: internal-contrast-only`; inherits [`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md) — no new decision). Cost **$0.53136 billed** (816 calls, 0 NA).

## Why this run

[`claim/comparative-correlative-covariation`](../claims/comparative-correlative-covariation.md) was promoted (s168) as a **direction/ordering** statement, with its *Bounds* recording that "A magnitude+CI is **owed to the A2a powered re-run**; until it runs, this claim states direction/ordering only." v1/v2/v3 rested on founding N (20 items/cell in v1's constructed set; 3–6 per arm in v2/v3), so a single item moved a cell 5–33 pp and no interval could be stated. This run attaches the interval by re-running the **byte-frozen v1 instrument** (same NLI + forced-choice prompts, parsing, panel, `temperature=0`, thresholds) on a **fresh, disjoint, powered** item set — the only change is the items. It does **not** touch the human-comparison leg (the v1 Scivetti answer-key arm is unchanged and out of scope) and makes **no** human-level claim.

## Method (frozen pre-run; numbers independently re-verified)

- **Items:** 34 fresh scale pairs (24 typical + 10 atypical), **disjoint from v1's 20** (0 id overlap, enforced by an assertion in `build_items.py`), × 4 forms (cc-positive / cc-inverse / ctrl-two / ctrl-single) = **136 items**. Typical pairs are plausible-either-direction; atypical pairs are deliberately absurd (covariation direction can come *only* from the construction).
- **Instrument (frozen from v1):** both forced-choice (INCREASE/DECREASE/UNDETERMINED) and NLI (0/1/2). Panel: `anthropic/claude-sonnet-4.6`, `openai/gpt-5.4-mini`, `google/gemini-3.5-flash`. 2 arms × 136 × 3 = **816 calls, 0 NA**.
- **Intervals:** 95% CI via **cluster bootstrap over scale pairs** (B=2000, fixed seed 20260702) — the four forms are nested within a pair, so whole pairs are resampled; a naive item-level bootstrap would understate width.
- **Gates:** independent fresh-agent **pre-run critic → GO-WITH-NOTES** (all 34 golds verified correct, instrument byte-identical to v1, statistics sound, `internal-contrast-only` correct; the one SHOULD-FIX — a dead-code disjointness guard — was wired into an enforced assertion with items unchanged, sha stable). Non-Anthropic decorrelation vote (gpt-5.4-mini) → GO-WITH-NOTES (no gold errors). Independent fresh-agent **post-run verifier → REPRODUCED**: it wrote its own parser and counting (not analyze.py) and reproduced **every** number exactly — 136+136 records/model, **0 NA**, **0 misparses across all 816 records**, all rates, the T1 gap, the control-assertion split (ctrl-two > ctrl-single in all 3 models), the typ−atyp values, and the per-model `usage.cost` (total $0.53136). It independently confirmed the ≈87 pp gap is driven by real CC-assertion vs real control-non-assertion (not an artifact), that the residual control assertion is concentrated on world-knowledge-leaning `ctrl-two` items (making the gap conservative), that the CIs resample over the 34 scale-pair clusters (not items), and that no human-comparison or depth-of-processing claim is smuggled in. **No discrepancy, no overreach.**

## Results — magnitudes with 95% intervals

Point estimate [95% CI], per model. Full machine output: [`raw/results.json`](../../../experiments/runs/2026-07-02-comparative-correlative-powered/raw/results.json).

| quantity | claude-sonnet-4.6 | gpt-5.4-mini | gemini-3.5-flash |
|---|---|---|---|
| **T1 construction-isolation assertion gap (pp)** | **86.8 [77.9, 94.1]** | **88.2 [77.9, 97.1]** | **86.8 [77.9, 94.1]** |
| FC covariation-direction accuracy on CC items (%) | 100 [100, 100] | 100 [100, 100] | 98.5 [95.6, 100] |
| inverse-CC direction-flip (% answering DECREASE) | 100 [100, 100] | 100 [100, 100] | 97.1 [91.2, 100] |
| positive-CC (% answering INCREASE) | 100 [100, 100] | 100 [100, 100] | 100 [100, 100] |
| typical − atypical FC accuracy (pp) | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 5.0 [0.0, 16.7] |
| atypical-pair assertion rate (%) | 100 [100, 100] | 100 [100, 100] | 95.0 [83.3, 100] |
| NLI covariation-reading accuracy on CC items (%) | 100 [100, 100] | 95.6 [91.2, 100] | 97.1 [92.6, 100] |

**Frozen-threshold gates (continuity with v1; not the deliverable):** T1 ≥ 30pp **3/3**, T2 inverse-flip ≥ 70% **3/3**, T3 atypical within 15pp **3/3**.

### The construction-isolation gap is real and off-ceiling
The gap is the design's T1 quantity (the CC covariation-*assertion* rate minus the matched-control assertion rate — same scalar words, CC syntax vs none). CC-item assertion is ≈100% (claude 100, gpt 100, gemini 98.5); **matched controls still assert a direction only ≈12%** of the time (claude 13.2, gpt 11.8, gemini 11.8), so the ≈87 pp gap is a genuine, non-ceiling contrast: the construction, not the vocabulary, drives the covariation reading. The residual ≈12% control assertion is **concentrated on `ctrl-two`** (two juxtaposed declaratives; claude 23.5 / gpt 14.7 / gemini 20.6) and near-absent on `ctrl-single` (2.9 / 8.8 / 2.9), and the specific pairs that leak are the world-knowledge-leaning ones (`summer`, `highway`, `clinic`, `brochure`, `current`, plus the `footpath` NIT pair). This is **conservative for the gap**: any world-knowledge pull raises the *control* assertion rate and *shrinks* the measured effect — so ≈87 pp is a floor, not an inflation.

### Direction-tracking, not a template
Inverse CCs flip the asserted direction to DECREASE at 97–100%, and — the strongest construction-only evidence — the **10 atypical inverse pairs** (absurd pairings whose direction can come only from the construction) flip at **100 / 100 / 90%**. Positive CCs assert INCREASE at 100%. A bare "the-more…the-more → increase" template would not flip; these do.

### No collapse on absurd pairs (n-gram/memorization robustness)
Typical − atypical FC accuracy is 0 / 0 / 5 pp — the panel handles the deliberately-absurd scale pairs essentially as well as the plausible ones, so the covariation reading is not a memorized-collocation effect. gemini's single atypical miss (one item; 5 pp, CI [0, 16.7]) is noise, not a collapse.

## What this run confirms — and its scope

- **MAGNITUDE-CONFIRMED (the pre-registered positive outcome).** All three v1 signatures reproduce on fresh disjoint powered items with 95% CIs that exclude the null direction for 3/3 models. The claim can now state the **construction-isolation effect as ≈87 pp [lower bound ≈78 pp]** rather than a bare threshold-pass, and the direction-flip and atypical-robustness as at/near ceiling with tight intervals.
- **Ceiling is still the lead caveat.** Every quantity except the T1 gap and the control assertion rate is at/near 100%, so this run **cannot** separate robust constructional competence from task-easiness. It delivers the *deferred magnitude+interval*, exactly as scoped — not a depth-of-processing verdict. The one genuinely off-ceiling number (the ≈87 pp gap, driven by ≈12% control assertion) is the informative magnitude; the rest are precise-but-saturated.
- **Internal-contrast-only; no human claim.** All quantities are within-model contrasts (CC vs matched control, positive vs inverse, typical vs atypical). No Scivetti arm was run; no human comparison and no model-vs-human magnitude is made or implied. The magnitude attached is the *internal-contrast* magnitude the claim's *Bounds* defers.
- **3 models, one date, one panel.** Cross-model convergence across three decoders is the evidence; n=3 remains a hard bound and the panel shares training-era priors.
- **gpt-5.4-mini's v3 operator-embedding crack is not re-tested here** (this run uses only asserted/inverse CCs and controls, as v1 did); that non-uniformity lives in [`result/comparative-correlative-covariation-v3`](comparative-correlative-covariation-v3.md) and is unaffected.

## Relation to the claim and conjecture
This run **supports** [`claim/comparative-correlative-covariation`](../claims/comparative-correlative-covariation.md) by attaching the magnitude+interval its *Bounds* deferred, upgrading the construction-isolation / direction / robustness legs from direction-only to magnitude-bearing (the human-comparison leg is unchanged). For [`conjecture/comparative-correlative-construction`](../conjectures/comparative-correlative-construction.md), the powered run confirms the covariation-reading direction on fresh items; it says nothing new about the conjecture's "narrows-but-does-not-close" human-gap clause (no human arm here). On the shadow-depth reading ([`essay/shadow-depth-cross-cuts-grain`](../essays/shadow-depth-cross-cuts-grain.md)) it firms the CC's status as the grammatical pole's **shadow-beater** with a measured, interval-bearing construction-isolation contrast — a candidate row for the flagship shadow-depth table (A1c).
