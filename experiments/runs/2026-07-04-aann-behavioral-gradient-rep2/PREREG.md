# PREREG — AANN behavioral gradient, second-date powered REPLICATION (rep2), frozen before any finding-bearing model call

**What this run is.** The A2a owed cross-date powered re-run of the AANN **anchored acceptability
gradient** — the "overall positive" whose only gap, named in
`wiki/findings/claims/aann-behavioral-gradient.md`, is: *"There is no second-date replication of
the overall positive; the only second date (v2b) replicates the temporal hole."* This run supplies
exactly that: a **fresh-item, second-date** replication of the anchored gradient on the **byte-identical
frozen v2 instrument**, against the **identical human anchor**.

**Relationship to v2.** The instrument is byte-identical to
`experiments/runs/2026-06-12-aann-behavioral-probe-v2/` — `probe.py` and `analyze.py` are copied
unchanged (sha256 verified identical: `ec8f7334…` / `4ce5a709…`). The governing design is
`experiments/designs/aann-construction-v2.md` (frozen, ratified
`wiki/decisions/resolved/aann-behavioral-operationalization.md`, nine binding conditions). The
**only** differences from v2, both made before any finding-bearing model call:

1. **Sampling seed** 20260612 → **20260704** (a fresh occasion).
2. **Anchored arm drawn DISJOINT from v2.** For each of the 204 (adjective × noun-class) cells,
   the two item-ids v2 sampled are removed from the candidate pool before the seeded pick. Result:
   **408 anchored items, 0 shared surface items with v2** (`prep.py` asserts this mechanically;
   every cell retains ≥ 4 candidates — min pool 6, v2 removed 2). This is the fresh-item standard
   the sibling dative and CC powered re-runs met ("0 shared items").

**What is UNCHANGED (and mechanically verified before the run):**

- **Human anchor identical.** `human_cell_means.csv` (204 cells) and `human_class_means.csv`
  (28 class-cells) are computed from ALL 3,600 non-filler Exp-2 ratings (seed-independent) — both
  **byte-identical to v2** (verified by `diff`). The fresh model items map to the **same** human cells.
- **Held-out arm and Tier-0 tuples byte-identical** (lexically frozen, deterministic construction,
  not rng-sampled): held-out item ids and sentences are identical to v2; Tier-0 item ids identical
  (A/B position randomization reseeds, which the scoring path handles via `aann_position`). rep2
  therefore also delivers a **second-date re-run of the held-out overall positive and the temporal
  hole at the identical items** — a bonus, not the primary target.
- **Instrument:** primary framing 0–100 (integer only); robustness 4-point (digit only); Tier-0 A/B
  letter only. Temperature 0; max_tokens 64 (A, B) / 512 (C); gemini `reasoning:{"effort":"minimal"}`.
- **Parsing:** full-string bare integer else the LAST in-range token; one verbatim retry per
  unparseable response then missing. Missing > 10% in any arm = mandatory caveat; > 25% = arm
  instrument failure; any verdict-bearing arm absent/wrong-count ⇒ run verdict INCOMPLETE.
- Mirror: MIT `github.com/mahowak/aann-public`, commit `c8095a0008cd6538717de5cc937f90ce5944e688`,
  re-cloned this session and verified (regenerating v2's stimuli with the OLD seed reproduces the
  committed `stimuli.json` byte-identically — mirror is the exact one v2 used).

## Frozen statistics and thresholds (per model) — byte-identical to v2

- **ANCHORED PASS** = Spearman ρ(model cell mean, human cell mean) over 204 cells ≥ 0.40 AND
  10,000-resample percentile bootstrap 95% CI over cells excludes 0 AND partial Spearman
  controlling adjective Zipf (rank-residualization) ≥ 0.20 AND noun-class guard (mean within-noun-class
  Spearman across the 6 strata) ≥ 0.25.
- **HELD-OUT REPLICATION PASS** = Spearman ρ(model held-out class-cell means, HUMAN anchored
  class-cell means) over 15 held-out class-cells ≥ 0.50 AND mean within-noun-class Spearman over
  strata with ≥ 4 class-cells ≥ 0.30.
- **TIER-0 PASS** = ≥ 20/24 AANN preferred; failure ⇒ model excluded from the support count.
- **Framing-fragility flag:** item-level Spearman between framings on the 102-item subset < 0.50
  (or NaN) ⇒ FRAGILE.

## Frozen verdict map (conjecture level) — byte-identical to v2

- **SUPPORTED:** ≥ 2 of 3 Tier-0-passing models achieve ANCHORED PASS, AND every anchored passer
  also achieves HELD-OUT REPLICATION PASS.
- **PARTIAL (memorization-like):** ≥ 2 anchored passes but a held-out failure among them.
- **PARTIAL (form-without-gradient):** broad Tier-0 pass, < 2 anchored passes.
- **FALSIFIED (current form):** zero anchored passes among Tier-0 passers, or all passes
  frequency-confounded.
- **INSTRUMENT FAILURE:** fewer than 2 Tier-0-passing models.
- **INCOMPLETE:** any verdict-bearing arm absent/partial.
- Thresholds are ≥ (inclusive). No post-hoc adjustment under any outcome.

## Replication read (what rep2 adds to the claim, declared pre-run)

This run does **not** re-open the SUPPORTED/PARTIAL verdict of v2 (that verdict stands on v2's
occasion). Its evidential contribution, fixed before the data exist, is **cross-date replication of
the anchored gradient**: the pre-registered success criterion for "the overall positive replicates"
is that the anchored arm again passes for **≥ 2 of 3** Tier-0-passing models, at a cell-level ρ whose
bootstrap CI overlaps v2's per-model interval. A failure to replicate (fewer passers, or a
non-overlapping downward CI) is a first-class negative and would be written as such, **weakening** the
claim's overall-positive leg rather than strengthening it. No predicted per-model magnitude is
hardcoded anywhere in the scoring path; scoring is against the empirical human cell means only.

## Spend

Pre-flight billed expectation ≈ **$0.31** (v2's measured actual at the identical 1,782-call shape:
408 anchored + 102 robustness + 60 held-out + 24 Tier-0, × 3 models; single-integer outputs are
cheap). `ABORT_USD` in `probe.py` = **$2.50** (the single-run flag) — never expected to approach.
Session budget: Tom granted a $10 ceiling for the UTC-2026-07-04 day (day-so-far $4.3312345); this
run leaves wide headroom and is far under the $2.50 single-run flag. Actual billed `usage.cost`
recorded in the run README and `config/budget.md`.

## Freeze

Frozen 2026-07-04, before any model call. No AANN model output from this run exists at freeze time;
`prep.py` (no model calls) produced `stimuli.json` + the (v2-identical) human tables. An independent
fresh-agent pre-run critic reviews this PREREG + design + stimuli, and one non-Anthropic
decorrelation vote is routed through the probe REST path, **before** any finding-bearing call.
