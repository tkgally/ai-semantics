# PREREG — comparative-correlative covariation, POWERED re-run (A2a)

**Date:** 2026-07-02 (session 169) · **Status at write time:** DESIGN — pre-run critic pending; NOT frozen, NOT run.
**Program item:** A2a (powered confirmation). **Claim it feeds:** [`claim/comparative-correlative-covariation`](../../../wiki/findings/claims/comparative-correlative-covariation.md) — its *Bounds* says "A magnitude+CI is **owed to the A2a powered re-run**; until it runs, this claim states direction/ordering only."
**Prior runs (frozen, not re-tuned):** v1 [`.../2026-05-29-comparative-correlative-probe-v1`](../2026-05-29-comparative-correlative-probe-v1/README.md), v2, v3.

## Purpose (one sentence)
Attach a **magnitude with a 95% interval** to the construction-isolation, direction-flip, and atypical-robustness signatures that v1 established only as threshold-passes at founding N — by re-running the **frozen v1 instrument** on a **fresh, disjoint, powered** item set.

## What is held FROZEN from v1 (byte-identical; not re-tuned after any result)
- **Instrument prompts:** `NLI_SYS` and `FC_SYS` copied verbatim from the v1 probe.
- **Framings:** both instruments — forced-choice (INCREASE/DECREASE/UNDETERMINED) and NLI (0/1/2).
- **Parsing:** `parse_fc` = last keyword; `parse_nli` = trailing digit (handles CoT-ish output).
- **Panel:** the ratified 3-family panel ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6`, `openai/gpt-5.4-mini`, `google/gemini-3.5-flash`. temperature=0. `max_tokens` 4096 for `google/` (absorb reasoning tokens), 64 otherwise.
- **Item structure:** the four forms (cc-positive / cc-inverse / ctrl-two / ctrl-single) and their construction-correct gold answers.
- **Thresholds T1 ≥ 30pp / T2 ≥ 70% / T3 within 15pp** — reported for continuity, but the *deliverable is the point estimate + CI*, not the pass/fail gate.

## What CHANGES (the only change): the item set
- **34 fresh scale pairs** (24 typical + 10 atypical), **disjoint from v1's 20** (verified: 0 id overlap, all content new) × 4 forms = **136 constructed items**. Powered N per [`PROTOCOL.md`](../../../PROTOCOL.md) §4 (~100–150). Authored so covariation direction is not world-knowledge-obvious (typical) or is deliberately absurd (atypical).
- Emitted by `build_items.py` → `experiments/data/comparative-correlative-powered/items.csv`, committed **before** any probe call.

## Primary quantities + intervals (the magnitude the claim defers)
Per model, point estimate + **95% CI via cluster bootstrap over scale pairs** (B=2000, fixed seed 20260702; forms are nested within a pair, so whole pairs are resampled — the honest interval for this design):
1. **T1 construction-isolation gap (pp)** = FC covariation-*assertion* rate on CC items − on matched controls (the design's stated T1 quantity — same scalar words, CC syntax vs none).
2. **Inverse-flip rate (%)** = fraction of cc-inverse items answered DECREASE.
3. **Positive-increase rate (%)** = fraction of cc-positive answered INCREASE.
4. **Typical − atypical accuracy (pp)** and **atypical assertion rate (%)** (n-gram/memorization robustness).
5. **NLI cc-vs-ctrl accuracy gap (pp)** (cross-instrument read).

## Scope, anchor, and what this run does NOT claim
- **`anchor: internal-contrast-only`**, inheriting the ratified [`decisions/resolved/conflicting-cue-human-anchor`](../../../wiki/decisions/resolved/conflicting-cue-human-anchor.md) precedent for constructed CC arms (all five quantities are **within-model contrasts** — CC vs matched control, direction-flip, atypical vs typical — making **no human comparison**). `contingent-on: []`; **no new decision opened.**
- **The human-comparison leg is out of scope and UNCHANGED:** the claim's only human anchor is v1's single-run answer-key parity on the 30 real Scivetti items. This run does **not** touch it, does not re-run Scivetti, and makes no human-level-competence claim.
- **No magnitude smuggling into the human comparison:** the magnitude attached here is the *internal-contrast* magnitude (how large the construction-isolation / direction / robustness effects are, with intervals), exactly what the claim's *Bounds* defers — not a model-vs-human magnitude.
- **n = 3 models** remains a hard bound; the panel-level reading is a convergence across three decoders, not a population estimate.

## Verdict frame (pre-registered, symmetric — a shrinking or absent effect is first-class)
- **MAGNITUDE-CONFIRMED:** the v1 signatures reproduce on fresh powered items with CIs that exclude the null direction (T1 CI lower bound > 0; flip CI lower bound > 50%) for ≥2/3 models → the claim gains a stated magnitude+interval and is updated from direction-only to magnitude-bearing.
- **ATTENUATED:** point estimates hold direction but CIs are wide / straddle a threshold → record the honest interval; the claim states the magnitude *with* its width and keeps its directional scope.
- **NULL / REVERSAL:** a signature fails to reproduce on fresh items → a first-class negative; the claim is revised or contested accordingly and the discrepancy investigated (item authoring, not threshold, is the suspect — do not retune).

## Budget
Pre-flight estimate: 2 arms × 136 items × 3 models = **816 calls**. At observed v1 prices (~$0.12 for 570 calls) ≈ **$0.15–0.25** billed. Well under the $2.50 single-run flag and the $5.00/day cap. A ~30-item billed pre-flight will confirm the projection before the full run. Actuals recorded in [`config/budget.md`](../../../config/budget.md) from the returned `usage.cost`.
