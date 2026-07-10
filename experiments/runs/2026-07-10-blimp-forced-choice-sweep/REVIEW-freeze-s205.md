# FREEZE PRE-RUN REVIEW — BLiMP forced-choice sweep (A3b, s205)

**Procedure (PROTOCOL §A3):** fresh-agent adversarial pre-run critic (GO/NO-GO authority, independent of
all artifacts) + one fresh non-Anthropic decorrelation vote (`gpt-5.4-mini`, cutoff-aware preamble).
Reviewed the FROZEN instrument (`PREREG.md`, `prep.py`, `probe.py`, `analyze.py`, `paradigms.json`,
`items.json`) with `raw/` empty (anti-cheat fence intact at review time).

## Fresh-agent critic — VERDICT: **GO** (spend authorized; no fatal flaw, no mandatory pre-spend change)

- **A. Ratified conditions honored — PASS.** F2 (40 paradigms; power note correct; R1 rides on no verdict
  this run per C8, so band generosity can't manufacture a positive). F3 saturation guard present + correct.
  F4 0.60 floor applied (min 0.606). F5 (R2 strictly within-panel; R2h labelled human-comparison). **F6
  verified mechanically:** `paradigm_meta.json` carries **no `total_mean` key**; `prep.py` selects solely
  on `linguistics_term`; the `human` dict is read only *after* selection — genuinely human-agreement-blind.
  C8 honored (R1 descriptive/non-promotable; F2 symmetry stated). Q2-A both orders + real position
  diagnostics.
- **B. analyze.py thresholds match PREREG exactly — PASS, no mismatch** (ρ +0.40/+0.20 with the
  [.20,.40] dead-zone; F3 SD 0.03; DEPTH/R2h 0.05; poslock 0.50/ans1 0.40; F4 0.60; BOOT 5000, seed
  20260710; N=30; ≥2/3 via `maj()`).
- **C. Scoring correct — PASS.** correct = selects `sentence_good` in both orders; order-averaged primary;
  Spearman with average-tie handling + paradigm-resampled bootstrap; position-lock diagnostic meaningful;
  a truncated/all-unparsed gemini → NaN acc contributes to no majority (degraded-not-silent). No
  verdict-corrupting bug.
- **D. Verdict map sound — PASS.** All nulls pre-named + first-class; no uncovered dead-zone; no asymmetry
  favoring a positive (the only verdict-bearing positives are within-panel/relative and contamination-
  robust; human gap +0.065 → EXCEEDS needs panel gap >0.115, a real bar).
- **E. Cost/safety — PASS.** 7,200 calls, est $0.6–1.6, under the $2.50 split flag; per-model
  `ABORT_USD=1.60` (worst case 3×=$4.80 < $5 cap); gemini bounded; `usage.cost` billed-real.
- **F. Anti-cheat — none found.** Selection provably human-agreement-blind; all 40 human values match the
  committed CSV verbatim (sha256 `ea0e7c21…`, 8 spot-checked); verdict-bearing readings are the
  contamination-robust within-panel ones, not R1; nothing tunable post-hoc; nulls symmetric; the 40-set is
  a whole-category sweep, not favorable curation.

**Four non-blocking notes (all post-run-fixable without re-spend; applied to `analyze.py` BEFORE the run,
additive-only — no threshold or verdict-logic change):**
1. Gemini truncation watch: `max_tokens=128` + minimal reasoning could truncate slot C's digit — **inspect
   slot C's first paradigm before completing the C sweep** (the per-file `miss` count reveals it early).
2. Consistency accuracy was computed but not surfaced → **now written to `results.json`
   (`mean_consistency_acc`) and printed** (the PREREG-promised position-hardened robustness check).
3. F4 floor was not enforced in `strat_mean()` (inert — all 40 pass) → **now enforced in code** with a
   comment (paradigms below 0.60 dropped from the reading-2 accuracy strata).
4. Retry cost undercount (negligible; one-digit task, rare retries) — left as-is.

## Non-Anthropic decorrelation vote (`gpt-5.4-mini`, QA input) — billed $0.00294075

**GO-WITH-CONDITIONS.** No anti-cheat concern; prompt neutral, order-balancing appropriate. Its
conditions (all analysis-side, applied before the run): **(i)** report **per-category means** alongside the
shallow/deep aggregate so readers can see whether one category carries R2 → **added to `results.json`
(`per_category_acc`) + print**; **(ii)** frame R1 as a **40-paradigm observed-set** metric, not "full
on-axis BLiMP" → **added `observed_set_note` + `human_by_category` to `results.json`**; **(iii)** scope
R2/R2h to **this exact frozen panel**, not a universal depth law → carried in the design scope-cap +
result-page framing. Its "depth bucket mixes heterogeneous phenomena" caution is answered by the
per-category breakdown (readers can see if one category drives the gap) and the within-panel/relative,
whole-category (non-curated) construction.

**Convergence:** fresh critic GO; vote GO-WITH-CONDITIONS. All conditions are additive reporting applied
pre-run; none changes a frozen threshold or verdict. **Spend authorized.**
