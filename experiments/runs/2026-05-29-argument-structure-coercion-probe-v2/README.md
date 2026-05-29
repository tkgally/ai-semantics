# Run record — argument-structure coercion probe v2 (off-ceiling)

**Date:** 2026-05-29
**Design (frozen, pre-registered):** [`design/argument-structure-coercion-v2`](../../designs/argument-structure-coercion-v2.md)
**Governing decision (ratified):** [`decisions/resolved/cc-v2-difficulty-operationalization`](../../../wiki/decisions/resolved/cc-v2-difficulty-operationalization.md) (UNIFY + adopt default, 2026-05-29)
**Conjectures probed:** [`conjecture/caused-motion-construction`](../../../wiki/findings/conjectures/caused-motion-construction.md), [`conjecture/way-construction`](../../../wiki/findings/conjectures/way-construction.md)
**Result page:** [`result/argument-structure-coercion-v2`](../../../wiki/findings/results/argument-structure-coercion-v2.md)

## What ran

The first **off-ceiling** test of the two add-direction Tier-4 positives (caused-motion, way), built to separate **H-deep** (the model computes the construction's added inference and would withhold it under a resolving cue) from **H-default** (the model fires a learned "this frame → yes" template a conflicting cue cannot override). On the v1 instruments these predict the same near-ceiling affirm rate; v2 forces them apart.

- **Indicator:** affirm-construction-inference rate (FC YES, or NLI entailment) on the per-item hypothesis — same instrument as v1 (NLI 0/1/2 + forced-choice YES/NO/CANT_TELL), temperature 0, **no logprobs** (so it runs on the existing 3-family behavioral panel).
- **Panel** ([`config/models.md`](../../../config/models.md)): claude-sonnet-4.6 (A), gpt-5.4-mini (B), gemini-3.5-flash (C).
- **Stimuli** (project's own, frozen pre-run; `items.csv` sha256[:16] `<FREEZE_HASH>`): 60 items — 10 caused-motion stems + 10 way stems × 3 conditions.

## Conditions (graded difficulty ladder)

| condition | difficulty | example (caused-motion) | example (way) | affirm gold |
|---|---|---|---|---|
| `canonical` | 1 | Maria sneezed the napkin off the table. | Mia whistled her way down the hall. | YES (the v1 ceiling anchor) |
| `resist` | 2 | Maria knew the napkin off the table. | Mia slept her way down the hall. | NO (coercion-resisting verb; anomalous) |
| `cue` | 3 | Maria sneezed the napkin off the table, but the napkin never moved. | Mia whistled her way down the hall, but she never left the doorway. | NO (explicit denial cancels the inference) |

**Key arm = the `canonical` vs `cue` minimal pair** (same construction + verb + hypothesis; `cue` only adds the denial). The discriminators: the **cue affirm rate** (low = cue-respecting / H-deep; high = template / H-default) and the **canonical→cue drop**. Reading rule (ratified, report-the-rate): cue affirm ≥70% in ≥2/3 models = robustly template/cue-ignoring; ~chance/low = cue-respecting. No pass bar that manufactures a result; the null in either direction is first-class.

## Human anchor

**Pending / internal-contrast-only** (ratified Option-4 logic). The Scivetti CxNLI subsets contain no conflicting-cue / coercion-resisting items, and the "correct" reading of an anti-cued coercion is itself contestable for humans — so **no human baseline is asserted**; the result is read as an internal H-deep-vs-H-default contrast. No human label invented.

## License / data handling

Stimuli are the **project's own** (no third-party license); committed `raw/*.json` are **unredacted**. Re-derive via `build_items.py` then `probe.py`.

## Pre-registration / no-retuning

- Difficulty axes, the conflicting-cue reading rule, the degradation-shape criterion, and the human-anchor scope were **fixed by the ratified decision BEFORE this build** (anti-retuning, charter §8).
- Items frozen + committed **before any probe call**. An adversarial pre-run pass was run; fixes (if any) applied **before freezing** — see commit history + below.
- `analyze.py` reports raw rates per condition; no threshold tuned after the run.

## Files

- `build_items.py` — emits + freezes `experiments/data/argument-structure-coercion-v2/items.csv`.
- `probe.py` — runner (NLI + FC × 3 models); full outputs to `raw/`.
- `analyze.py` — affirm rate per construction × condition; canonical→cue drop; degradation monotonicity; cross-model cue summary; emits `raw/results.json`.
- `raw/` — `nli_{A,B,C}.json`, `fc_{A,B,C}.json`, `results.json`, `run_summary.json`.

## Results / cost

(filled after the run from the committed `raw/results.json` — see the result page. Every number reproducible from `raw/results.json`.)
