# 2026-06-20 — POWERED let-alone forced-decomposition re-run (trigger-(g))

The **powered re-run** that session 60
(`2026-06-20-scivetti-let-alone-forced-decomposition`) and
[`essay/witness-seeking-economics`](../../../wiki/findings/essays/witness-seeking-economics.md)
§"The partial witness" (revision trigger (g)) prescribed for session 60's **partial
witness** — gpt-5.4-mini's directional-but-underpowered +0.21 let-alone lift under forced
uptake (0.583 on n = 24, sign-test p = 0.090, below the ≈0.90 baseline). The prescribed
continuation: a **powered re-run of the *same* forced-decomposition axis** with **more
let-alone items**, explicitly exempt from the "more of the same probe cannot" caution
because session 60 left a directional *signal*, not a null.

## Design (single change: item count; instrument byte-identical)

The forced-decomposition NLI instrument (`NLI_SYS_DECOMP`) is held **byte-identical** to
session 60 (programmatically diff-checked). The ONLY change is the let-alone item set:

- **let-alone TEST** (24, 8/8/8) — the session-60 target (test.tsv).
- **let-alone TRAIN** (9, 3/3/3) — **NEW, DISJOINT** (CxNLI_3_examples_train.csv; 0 shared
  premise/hyp pairs, 0 shared premises — 3 distinct source sentences). The 1-example train
  split ⊆ these 9, so **33 is the ceiling** of available human-annotated let-alone N.
- **comparative-correlative** (30, 10/10/10) — ceiling control, byte-identical to s57/58/60.

Combined let-alone target n = 33 (balanced 11/11/11). Panel A/B/C, temperature 0, gemini
`effort: minimal` held constant. Provenance re-asserted: full-set sha `1c5cffb18c5ef78e`
(== s57/58/60), s60-subset sha `9be31a8fea8d7f16`, frozen-63 sha `1b87dc871e4ec8dd`,
train-LA sha `6b0c8d82536f25e6`.

## Result (verdict: CONFIRMS-RESIDUAL for gpt; the new limit is measurement noise, not N)

| | s60 test (24) | **combined (33)** | test (24) | train (9) | vs 0.90 |
|---|---:|---:|---:|---:|---|
| claude | 0.833 | **0.727** [0.558, 0.849] | 0.708 | 0.778 | CI hi < 0.90 (control; see noise) |
| gpt | 0.583 | **0.636** [0.466, 0.778] | 0.583 | 0.778 | **CI hi 0.778 < 0.90 → CONFIRMS-RESIDUAL** |
| gemini | 0.875 | **0.909** [0.764, 0.969] | 0.875 | 1.000 | covers 0.90 (at baseline) |

**Run-to-run label stability (identical 24 test items, s60 → this run):** claude 3 flips
**all adverse** (0.833→0.708; #10/#18/#31), gpt 3 flips **mixed/net-0** (0.583→0.583;
#15/#26/#27), gemini **0 flips** (deterministic). → ~12% temp-0 label stochasticity for
both claude and gpt, comparable to the residual gap.

**Reading.** gpt's below-baseline let-alone residual **holds at higher N** and reproduces at
the accuracy level (test exact via offsetting flips; fresh disjoint train 0.778) — the
**cleanest channel-controlled residual** in the record (`output-channel-confound` trigger
(b), sharpened from *candidate* toward *fired*, with a magnitude caveat; descriptive +
contamination-caveated, never "cannot"). All three **worked 33/33** (uptake induced; medians
claude 211 / gpt 125 / gemini 170) and the comp-corr ceiling control is **PRESERVED** (1.000)
for all three. **But** claude — a baseline-matcher and the manipulation-check control —
**fell to 0.708 on the identical 24 items** purely from temp-0 flips, exposing label
stochasticity as the **new binding limit (not item count)** — the trigger-(g) "design, not
count, limits power → redirect axis" outcome. gemini reproduced deterministically and stays
at baseline.

## Cost & integrity

- Billed `usage.cost`: **$0.3921** (claude $0.2353 / gpt $0.0444 / gemini $0.1123). On
  pre-flight ($0.39). 189 finding-bearing calls (63×3). **0 missing, 189/189 parsed via the
  `FINAL:` tag** (0 fallbacks), 0 missing `usage.cost`. ABORT_USD=$0.80 never approached.
- Cadence: PREREG (frozen) → fresh independent pre-run critic **GO** (9/9 checks;
  instrument byte-identity, disjointness, sha provenance, no gold leak, no new decision,
  exemption legitimate, verdict map exhaustive, budget, honesty) → probe → fresh independent
  post-run verifier **REPRODUCED** (every accuracy, Wilson CI, the flip counts + directions,
  internal replication, uptake, billed cost, parse integrity, content_sha256↔CoT binding,
  CoT genuineness, no gold-leak — with the honesty note that gpt's "exact" reproduction is
  accuracy-level via offsetting flips, folded into the result page).

## Files

- `prep.py` — freeze recipe (combined + train + full-set + s60-subset shas; disjointness +
  balance asserted); recipe-not-corpus.
- `probe.py` — forced-decomposition NLI probe (only API caller); `NLI_SYS_DECOMP` verbatim
  from session 60; records `split` + uptake (lengths/booleans, NO text).
- `analyze.py` — combined + per-split acc + Wilson CI vs 0.90 + internal replication vs s60
  + control guard + uptake check; frozen verdict map.
- `PREREG.md` — frozen pre-registration (GO'd). `stimuli-manifest.json` — sha-pinned counts.
- `raw/{A,B,C}-labels.json` — committed (NO text). `raw/cot/` — gitignored full CoT.
- `results.json` — analysis output.

Reproduce: re-clone upstream `@82699473` into `experiments/data/scivetti/`, then
`python3 prep.py --check && python3 analyze.py`. To re-collect, `python3 probe.py`.

Finding: [`result/scivetti-let-alone-powered-rerun-v1`](../../../wiki/findings/results/scivetti-let-alone-powered-rerun-v1.md).
