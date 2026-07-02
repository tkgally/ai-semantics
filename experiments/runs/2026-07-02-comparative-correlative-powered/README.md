# Run record — comparative-correlative covariation, POWERED re-run (A2a)

**Date:** 2026-07-02 (session 169)
**Program item:** A2a (powered confirmation, [`wiki/program.md`](../../../wiki/program.md)).
**Pre-registration:** [`PREREG.md`](PREREG.md)
**Feeds:** [`claim/comparative-correlative-covariation`](../../../wiki/findings/claims/comparative-correlative-covariation.md) (its *Bounds* defers the magnitude to this run).
**Result page:** [`result/comparative-correlative-covariation-powered`](../../../wiki/findings/results/comparative-correlative-covariation-powered.md)
**Frozen baseline re-used:** [`.../2026-05-29-comparative-correlative-probe-v1`](../2026-05-29-comparative-correlative-probe-v1/README.md)

## What ran
The FROZEN v1 instrument (same NLI + forced-choice prompts, parsing, panel, thresholds — see PREREG) on a **fresh, disjoint, powered** item set: 34 new scale pairs (24 typical + 10 atypical) × 4 forms = **136 constructed items**, two instruments × 3 panel models = **816 calls**. temperature=0; `max_tokens` 4096 for `google/`, 64 otherwise. No Scivetti human arm (the human-comparison leg is unchanged from v1 and out of scope; this run measures the *within-model* magnitudes).

## Files
- `build_items.py` — emits the frozen fresh item set → `experiments/data/comparative-correlative-powered/items.csv`. Run + committed **before** the probe (charter §8).
- `probe.py` — probe runner (2 constructed arms × 3 models). Records the OpenRouter-billed `usage.cost` per record. Raw JSON per (arm, slot) under `raw/`.
- `analyze.py` — the v1 quantities PLUS 95% CIs via **cluster bootstrap over scale pairs** (B=2000, fixed seed). Emits `raw/results.json`.
- `raw/` — full prompts/responses/usage for the constructed items (the project's own items; no license constraint).

## Freeze
Item set frozen at the sha256 recorded in `PREREG.md`'s freeze note (committed before any probe call). The instrument is byte-frozen from v1; only the items are new.

## Deliverable
Point estimate + 95% interval per model for: the T1 construction-isolation assertion gap, the inverse-flip rate, the positive-increase rate, typical−atypical robustness, and the NLI cc-vs-ctrl gap — the magnitude the claim defers. Cross-model divergence is itself a finding (charter §6). See `raw/results.json` and the result page.
