# Run record — comparative-correlative probe v2 (off-ceiling)

**Date:** 2026-05-30
**Design (frozen, pre-registered):** [`design/comparative-correlative-v2`](../../designs/comparative-correlative-v2.md)
**Governing decision (ratified):** [`decisions/resolved/cc-v2-difficulty-operationalization`](../../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md) (UNIFY + adopt default — conflicting-cue primary + multi-step + near-miss + graded ladder; defer embedded-CC to v3; report-the-rate). **No new decision.**
**Conjecture probed:** [`conjecture/comparative-correlative-construction`](../../../wiki/findings/conjectures/comparative-correlative-construction.md)
**Refines:** [`result/comparative-correlative-covariation-v1`](../../../wiki/findings/results/comparative-correlative-covariation-v1.md) (the v1 ceiling positive)
**Result page:** [`result/comparative-correlative-covariation-v2`](../../../wiki/findings/results/comparative-correlative-covariation-v2.md)

## What ran

The off-ceiling follow-up to the v1 CC ceiling positive. v1 showed the panel asserts the covariation direction for ~100% of clear CCs and matched the Scivetti human baseline; its caveat is that ceiling on an easy instrument can't separate robust constructional competence from task-easiness. v2 raises difficulty along the ratified axes.

- **Indicator:** construction-correct rate per arm (FC INCREASE/DECREASE/UNDETERMINED; NLI 0/1/2) on the covariation direction. Instrument reused verbatim from v1; temperature 0, no logprobs → existing 3-family panel.
- **Panel** ([`config/models.md`](../../../config/models.md)): claude-sonnet-4.6 (A), gpt-5.4-mini (B), gemini-3.5-flash (C).
- **Stimuli** (project's own, frozen pre-run; `items.csv` sha256[:16] `e7dfd3ad42e3bbe2`): 19 items across 4 arms.

## Arms (graded difficulty ladder)

| arm | d | what it tests | gold |
|---|---|---|---|
| `baseline` | 1 | clear CC, direction not world-obvious (v1 anchor / ladder bottom) | stated direction |
| `conflicting-cue` | 2 | **the key manipulation** — real-world direction unambiguous, construction states the **opposite** | the **stated** (construction) direction |
| `paraphrase` | 2 | near-miss **form** control — same covariation in a non-paired-`the` form (*As X got -er, Y got -er*) | stated direction |
| `multi-step` | 3 | two chained CCs; hypothesis probes the chain endpoints → must **compose** two covariation signs | product of the two step signs |

**Headline (report-the-rate):** the conflicting-cue **follow-construction** rate (vs follow-world-knowledge), the multi-step **composition** rate, and the **degradation shape** across d1<d2<d3 (graceful monotone vs brittle cliff). A cue-following or composition-collapse pattern is the informative partial-null that would qualify v1's ceiling as task-easiness. No pass bar; no threshold tuned after the run.

## Human anchor

**Pending / internal-contrast-only** (Option-4 logic; design §4). The `baseline` arm keeps the v1 phenomenon-level Scivetti CC anchor; the conflicting-cue / multi-step arms have **no in-repo human norm** → **no human-level claim** on them. No Scivetti arm is run here (no human-comparison item set for the hard arms). No human label invented.

## Pre-registration / no-retuning

- Difficulty axes, conflicting-cue reading rule, degradation criterion, and human-anchor scope were **fixed by the ratified gate BEFORE this build**.
- Items frozen + committed **before any probe call** (sha256[:16] `e7dfd3ad42e3bbe2`); **multi-step composition gold is cross-checked against the sign products in `build_items.py`** (an `assert` fails the build if any gold mismatches).
- **Adversarial pre-run pass:** independent read-only subagent critique (see below) — especially the conflicting-cue real-world directions and the multi-step composition golds.
- `analyze.py` reports per-arm correct rates + conflicting-cue follow-construction/follow-world split + composition rate; no threshold tuned after the run.

## Files

- `build_items.py` — emits + freezes `experiments/data/comparative-correlative-v2/items.csv` (with the composition-gold assert).
- `probe.py` — runner (NLI + FC × 3 models), self-contained (no Scivetti arm).
- `analyze.py` — per-arm construction-correct rate; conflicting-cue follow-construction vs follow-world; multi-step composition; degradation; emits `raw/results.json`.
- `raw/` — `nli_{A,B,C}.json`, `fc_{A,B,C}.json`, `results.json`, `run_summary.json`.

## Pre-run critique

An **independent read-only adversarial subagent** re-derived every gold from the sentence text (not the build comments). **VERDICT: sound to run as-is — all 19 golds correct, no fixes needed** (hash unchanged). It confirmed: all 6 conflicting-cue items have a genuine construction-vs-world conflict with the gold set to the stated (construction) direction; all 5 multi-step composition golds match an independent re-derivation; baseline/paraphrase golds match their stated directions; NLI/FC encodings consistent throughout. NITs (noted, not fixed): (1) `conf-sunlight`'s world-knowledge conflict relies on the default "more sun → more growth" (a reader invoking scorch could weaken it); (2) `para-cafe-inv` / `conf-training` require a one-step polarity recode between the surface adjective (quieter/weaker) and the dim2 noun (busyness/muscle strength) — the recodes are correct; (3) the set has **no `undetermined`-gold items**, so the NLI-neutral / FC-UNDETERMINED path is unexercised — an UNDETERMINED-biased model would not be flagged by this run (stated in the result page).

## Results / cost

114 calls, **0 NA**, cost **$0.026** (A $0.019 / B $0.001 / C $0.006). **Headline: the v1 ceiling survives the off-ceiling stress — it overshoots again.** Construction-correct rate: baseline 100% all; **conflicting-cue (follow-construction against world knowledge) 100% NLI, 100/83.3/83.3 FC** (a single 1-in-6 item slips to world knowledge for gpt-5.4-mini and gemini under FC); paraphrase 100% (gemini FC 75%); **multi-step composition 100% all models/instruments**, including the diagnostic `multi-bears` (negative × negative = positive) that a single-clause heuristic would fail. The CC covariation competence is robust, not a brittle template. Full write-up at [`result/comparative-correlative-covariation-v2`](../../../wiki/findings/results/comparative-correlative-covariation-v2.md); reproducible from `raw/results.json`.

**Post-run verification:** every figure independently recomputed from `raw/*.json` by a read-only adversarial subagent. (This probe used a fresh self-contained `probe.py` written for the v2 path — not the buggy copy — so it loaded the correct items on the first run.)
