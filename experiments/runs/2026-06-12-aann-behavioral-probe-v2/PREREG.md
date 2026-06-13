# PREREG — AANN behavioral probe v2 (frozen before any finding-bearing model call)

Design: `experiments/designs/aann-construction-v2.md` (the authoritative statement; this file
pins the run-level numbers so the analysis cannot drift). Governing decision:
`wiki/decisions/resolved/aann-behavioral-operationalization.md` (ratified 2026-06-12, nine
binding conditions). Conjecture: `wiki/findings/conjectures/aann-construction.md`.

Frozen inputs (committed before the run):
- `stimuli.json` — seed 20260612; 408 anchored items (2 per each of 204 adjective×nounclass
  cells), 102-item 4-point robustness subset, 60 held-out items (24 frozen adjectives — 4 × 6
  classes — frequency-matched per class: wordfreq Zipf median within ±0.5 of the Mahowald class
  median), 24 Tier-0 forced-choice pairs.
- `human_cell_means.csv` (204 cells), `human_class_means.csv` (28 class-cells) — computed from
  ALL 3,600 non-filler Exp-2 ratings; the human yardstick. Mirror commit c8095a0 (MIT).

Frozen instrument:
- Primary framing 0–100 (integer only); robustness framing 4-point (digit only); Tier-0 A/B
  letter only. Temperature 0; max_tokens 64 (A, B) / 512 (C — the 2026-05-28 calibration showed
  gemini burns small caps on hidden reasoning; pre-run critic B3); gemini
  `reasoning: {"effort": "minimal"}`.
- Parsing: full-string bare integer, else the LAST in-range token (a first-token rule records a
  scale echo like "of 0 to 100, 85" as 0 — pre-run critic S4). One verbatim retry per
  unparseable response, then missing. Missing >10% in any arm = mandatory caveat; >25% =
  instrument failure for that arm; a verdict-bearing arm absent or with a wrong row count makes
  the run verdict INCOMPLETE (no substantive verdict is emitted).

Frozen statistics and thresholds (per model):
- ANCHORED PASS = Spearman ρ(model cell mean, human cell mean) over 204 cells ≥ 0.40
  AND 10,000-resample percentile bootstrap 95% CI over cells excludes 0
  AND partial Spearman controlling adjective Zipf (rank-residualization) ≥ 0.20
  (raw pass + partial < 0.20 = frequency-confounded pass = NOT a pass)
  AND **noun-class guard** (pre-run critic B2, added before any call): mean within-noun-class
  Spearman across the 6 noun-class strata ≥ 0.25 (per-stratum NaN from constant model values
  counts as 0). Rationale, computed from the committed human tables only: a degenerate
  responder emitting the human noun-class marginal — zero adjective information — scores
  ρ = 0.466 on the 204 cells and 0.613 on the held-out class-cells, passing the original
  thresholds; the conjecture's predictions are about the ADJECTIVE gradient, and that confound
  scores ~0 within noun-class strata. 0.25 sits clearly above the confound's ~0 and clearly
  below the adjective-class-only baseline (0.665 at class grain).
- HELD-OUT REPLICATION PASS = Spearman ρ(model held-out class-cell means, HUMAN anchored
  class-cell means) over the 15 held-out class-cells ≥ 0.50 AND mean within-noun-class
  Spearman over strata with ≥4 class-cells (temporal, objects, distance) ≥ 0.30; an overall
  pass with a within-class failure is recorded as "not separable from noun-class main effect"
  and does not count as replication.
- TIER-0 PASS = ≥ 20/24 AANN preferred; failure = instrument failure, model excluded from the
  support count (gradient numbers reported but not counted). Per-position (A/B) breakdown
  reported as a sanity number.
- Framing-fragility flag: item-level Spearman between framings on the 102-item subset < 0.50,
  or undefined (NaN from degenerate constant output) — undefined counts as FRAGILE.

Frozen verdict map (conjecture level):
- SUPPORTED: ≥2 of 3 Tier-0-passing models achieve ANCHORED PASS, and **every** anchored
  passer also achieves HELD-OUT REPLICATION PASS (the strict all-passers reading: 3 anchored
  passers with 2 held-out passes is PARTIAL, not SUPPORTED).
- PARTIAL (memorization-like): ≥2 anchored passes but a held-out failure among them.
- PARTIAL (form-without-gradient): broad Tier-0 pass, <2 anchored passes.
- FALSIFIED (current form): zero anchored passes among Tier-0 passers, or all passes
  frequency-confounded.
- INSTRUMENT FAILURE: fewer than 2 Tier-0-passing models — no conjecture-level verdict is
  emitted (a single passing model is reported descriptively, never as support).
- INCOMPLETE: any verdict-bearing arm absent/partial (e.g. after a budget abort) — no
  substantive verdict.
- Ties/boundary values: thresholds are ≥ (inclusive). No post-hoc adjustment under any outcome.

Spend: pre-flight ≈ $1.0–1.5 billed expectation (1,782 calls); abort mid-run if cumulative
billed cost reaches $2.50 (the single-run flag), report partial arms as incomplete.

Frozen: 2026-06-12, before any model call. Pilot/dry-run outputs did not inform any number
above (no AANN model output of any kind exists in the repo at freeze time).

Amendment (2026-06-12, still pre-run, before any model call): the independent pre-run critic's
fix-list was applied — crash fix in the cost check (B1), the noun-class guard and its held-out
analogue (B2; rationale above, derived from the committed human tables only), per-slot
max_tokens (B3), missingness/completeness enforcement and the INCOMPLETE/INSTRUMENT FAILURE
verdict clauses (S1/S3), real abort semantics (S2), last-token parsing (S4), NaN-fragility
handling (S5), and the held-out adjective count corrected 22 → 24 (S7; the frozen list itself
never changed). No model output existed when any of these numbers were set.
