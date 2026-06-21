# 2026-06-21 — REPEATED-RUNS temp-0 jitter measurement (let-alone forced-decomposition)

The **repeated-run measurement** that session 62
(`2026-06-20-scivetti-let-alone-powered-rerun`) named as the trigger-(g) redirect and that
[`essay/point-estimate-is-a-draw`](../../../wiki/findings/essays/point-estimate-is-a-draw.md)
revision **trigger (a)** prescribed. Session 62 surfaced temp-0 run-to-run label stochasticity
as the new binding limit but inferred "~12% per run" from a **single** cross-session run-pair
(s60 → s62). This run **pins the jitter** by scoring the **byte-identical** forced-decomposition
instrument **K = 5** times at temperature 0 over the **same frozen 63-item set**, and tests
whether jitter shrinks at the ceiling control and concentrates at the hard near-chance let-alone.

## Design (single change vs session 62: REPEAT count)

- **Instrument** `NLI_SYS_DECOMP` byte-identical to s60/s62 (evaluated string sha
  `6b45fa900ce7321c`, 809 chars; the PREREG's "len 910" counts the escaped source literal — same
  string). Same panel, temperature 0, gemini `effort: minimal` held constant, max_tokens 1024 (A/B).
- **Items** the **same frozen 63** as s62 — 24 let-alone test + 9 let-alone train + 30 comp-corr
  ceiling control. All four shas == s62 (frozen `1b87dc871e4ec8dd`, full-set `1c5cffb18c5ef78e`,
  s60-subset `9be31a8fea8d7f16`, train-LA `6b0c8d82536f25e6`).
- **K = 5** independent same-session draws per (model, item); every one of the 945 calls a fresh
  HTTP request, nothing cached/deduped.

## Result (verdict: trigger (a) FIRES — jitter ceiling-protected; gpt residual robust to it)

| model | let-alone range (5 runs) | comp-corr range | gemini-style stability | de-noised LA majority-vote |
|---|---:|---:|---|---:|
| claude | 0.061 | 0.000 | churn 7/33 | 0.788 [0.622, 0.893] |
| gpt | **0.121** | 0.033 | churn 10/33 | **0.606 [0.437, 0.753]** |
| gemini | 0.030 | 0.000 | churn 2/33 (most stable) | 0.909 [0.764, 0.969] |

- **Trigger (a) fires** for all three: comp-corr ceiling control did not jitter; let-alone did.
- **~±0.12 confirmed for gpt, model-specific** (claude ~0.06, gemini ~0.03 — not a constant).
- **gpt's residual robust:** every one of 5 runs < 0.90 (band [0.545, 0.667]); de-noised 0.606,
  Wilson hi 0.753 < 0.90. Session 62's CONFIRMS-RESIDUAL was **not** a low draw.
- **Refinements of s62:** "gemini deterministic" → "most stable" (2/33 churn); claude's s62 0.708
  was a low draw (within-session test band [0.750, 0.792]); same-session spread is a **lower bound**
  (claude's single s60→s62 swing 0.125 > within-session test range 0.042).

## Cost & integrity

- Billed `usage.cost`: **$1.9642** (claude $1.1785 / gemini $0.5615 / gpt $0.2242). On pre-flight
  ($1.96 = 5 × s62's measured $0.392). 945 calls, **0 missing, 945/945 parsed via `FINAL:` (0
  fallbacks), 0 missing usage.cost**, uptake 33/33 every run. ABORT_USD $2.40 never approached.
- Cadence: PREREG (frozen) → independent fresh-agent pre-run critic **GO** (9/9 checks) → probe →
  independent fresh-agent post-run verifier **REPRODUCED** (every per-run accuracy, range/SD, churn,
  the C(5,2) pairwise agreements, majority-vote + Wilson, the gpt residual pin, the trigger-(a)
  contrast, cross-session, billed cost re-summed to the penny, parse integrity, no text/gold leak).

## Files

- `prep.py` — freeze recipe (shas == s62; recipe-not-corpus). `stimuli-manifest.json` — sha-pinned.
- `probe.py` — K-pass forced-decomposition probe (only API caller); `NLI_SYS_DECOMP` verbatim from
  s60/s62; writes `raw/run{k}-{slot}-labels.json` (NO text).
- `analyze.py` — per-run spread + per-item churn/pairwise-agreement + majority-vote + Wilson +
  trigger-(a) reading map + uptake/ceiling guard + cross-session; `--selftest` passes.
- `PREREG.md` — frozen pre-registration (GO'd). `results.json` — analysis output.
- `raw/run{k}-{slot}-labels.json` — committed (NO text). `raw/cot/` — gitignored full CoT.

Reproduce: re-clone upstream `@82699473` into `experiments/data/scivetti/`, then
`python3 prep.py --check && python3 analyze.py`. To re-collect, `python3 probe.py`.

Finding: [`result/scivetti-let-alone-repeated-runs-v1`](../../../wiki/findings/results/scivetti-let-alone-repeated-runs-v1.md).
