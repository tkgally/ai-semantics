# PREREG — AANN behavioral probe v2 (frozen before any finding-bearing model call)

Design: `experiments/designs/aann-construction-v2.md` (the authoritative statement; this file
pins the run-level numbers so the analysis cannot drift). Governing decision:
`wiki/decisions/resolved/aann-behavioral-operationalization.md` (ratified 2026-06-12, nine
binding conditions). Conjecture: `wiki/findings/conjectures/aann-construction.md`.

Frozen inputs (committed before the run):
- `stimuli.json` — seed 20260612; 408 anchored items (2 per each of 204 adjective×nounclass
  cells), 102-item 4-point robustness subset, 60 held-out items (22 frozen adjectives,
  frequency-matched per class: wordfreq Zipf median within ±0.5 of the Mahowald class median),
  24 Tier-0 forced-choice pairs.
- `human_cell_means.csv` (204 cells), `human_class_means.csv` (28 class-cells) — computed from
  ALL 3,600 non-filler Exp-2 ratings; the human yardstick. Mirror commit c8095a0 (MIT).

Frozen instrument:
- Primary framing 0–100 (integer only); robustness framing 4-point (digit only); Tier-0 A/B
  letter only. Temperature 0, max_tokens 16, gemini `reasoning: {"effort": "minimal"}`.
- One verbatim retry per unparseable response, then missing. Missing >10% in any arm = mandatory
  caveat; >25% = instrument failure for that arm.

Frozen statistics and thresholds (per model):
- ANCHORED PASS = Spearman ρ(model cell mean, human cell mean) over 204 cells ≥ 0.40
  AND 10,000-resample percentile bootstrap 95% CI over cells excludes 0
  AND partial Spearman controlling adjective Zipf (rank-residualization) ≥ 0.20
  (raw pass + partial < 0.20 = frequency-confounded pass = NOT a pass).
- HELD-OUT REPLICATION PASS = Spearman ρ(model held-out class-cell means, HUMAN anchored
  class-cell means) over the 15 held-out class-cells ≥ 0.50.
- TIER-0 PASS = ≥ 20/24 AANN preferred; failure = instrument failure, model excluded from the
  support count (gradient numbers reported but not counted).
- Framing-fragility flag: item-level Spearman between framings on the 102-item subset < 0.50.

Frozen verdict map (conjecture level):
- SUPPORTED: ≥2 of 3 Tier-0-passing models achieve ANCHORED PASS, and each of those also
  achieves HELD-OUT REPLICATION PASS.
- PARTIAL (memorization-like): ≥2 anchored passes but a held-out failure among them.
- PARTIAL (form-without-gradient): broad Tier-0 pass, <2 anchored passes.
- FALSIFIED (current form): zero anchored passes among Tier-0 passers, or all passes
  frequency-confounded.
- Ties/boundary values: thresholds are ≥ (inclusive). No post-hoc adjustment under any outcome.

Spend: pre-flight ≈ $1.0–1.5 billed expectation (1,782 calls); abort mid-run if cumulative
billed cost reaches $2.50 (the single-run flag), report partial arms as incomplete.

Frozen: 2026-06-12, before any model call. Pilot/dry-run outputs did not inform any number
above (no AANN model output of any kind exists in the repo at freeze time).
