# PREREG — DRAFT (NOT YET FROZEN) — AANN temporal held-out widening (v2b)

**STATUS: DRAFT.** This pre-registration is awaiting the independent pre-run critic.
It becomes binding only when committed as `PREREG.md` (the freeze), and **no
finding-bearing model call may be made before that freeze** (`probe.py` refuses to run
while only the draft exists). No model output for this run exists at draft time; every
number below was set from the committed v2 artifacts only.

Design addendum: `experiments/designs/aann-temporal-heldout-v2b.md`, which runs **under**
the ratified v2 instrument (`experiments/designs/aann-construction-v2.md`; governing
decision `wiki/decisions/resolved/aann-behavioral-operationalization.md`, nine binding
conditions). Purpose: resolve **caveat 2** of
`wiki/findings/results/aann-behavioral-gradient-v2.md` — the v2 held-out temporal stratum
was ≈ −0.2 for all three models over only 4 class-cells × 4 single items, too thin to
read. This is a **caveat-resolution / precision widening**, not a new conjecture test:
whatever the outcome, the result page *refines* `result/aann-behavioral-gradient-v2`
(its caveat 2), anchored to `resource/mahowald-2023-aann-stimuli` via the same
anchored-half-gradient route. It does **not** re-adjudicate v2's overall verdict, whose
gates already passed at the overall grain.

## Frozen inputs (committed before the run)

- `stimuli.json` — seed 20260613, built by `prep.py` **without the upstream mirror**,
  entirely from the committed v2 artifacts (`../2026-06-12-aann-behavioral-probe-v2/
  stimuli.json` and `human_class_means.csv`); templates recovered exactly from committed
  v2 sentences (consistency-asserted), including the upstream "tourish" typo template,
  kept for instrument continuity.
  - **Geometry:** 4 temporal-eligible adjective classes (ambig, neg, pos, quant — the
    only classes valid on temporal nouns in Mahowald's Exp-2 design; **4 class-cells is
    the maximum possible**, so widening is *within-cell*) × 10 held-out adjectives
    (6 **new** + the 4 **v2 carryovers**) × 2 items each = **80 items**; all 5 Mahowald
    temporal nouns (days, hours, weeks, months, years), nums three/five, all 3 temporal
    templates, balanced by rotation (nouns 16 each; nums 40/40; templates 28/28/24).
  - **Frequency control (same procedure as v2, Condition 5):** wordfreq 3.x Zipf (en),
    per-class median; the 6 new adjectives' class median within ±0.5 of the Mahowald
    class median, and the combined 10 within ±0.5 too — asserted mechanically in
    `prep.py`; **all 4 classes pass** (ambig 4.065|3.91|3.91, neg 3.52|3.505|3.34,
    pos 4.07|3.855|3.995, quant 3.43|3.405|3.38 — mahowald|new-6|combined-10, exact
    values as embedded in the `stimuli.json` audit). Local
    wordfreq (3.1.1) verified to reproduce every committed v2 Zipf value exactly
    (commensurability guard, asserted). New adjectives appear in neither Mahowald's 50
    nor the v2 held-out 24 (asserted).
- **Human yardstick** (copied verbatim into `stimuli.json` from the frozen v2
  `human_class_means.csv`): anchored temporal class-cell means — quant 8.4508 >
  ambig 8.2526 > pos 8.0183 > neg 7.5673. No predicted ordering is hardcoded anywhere
  in the scoring path; scoring is against these empirical means only (Condition 1).

## Frozen instrument (identical to v2; no new operationalization)

Primary 0–100 framing, prompt byte-identical to v2's `P100`; temperature 0;
max_tokens 64 (A `claude-sonnet-4.6`, B `gpt-5.4-mini`) / 512 (C `gemini-3.5-flash`,
`reasoning: {"effort": "minimal"}`), per `config/models.md` and the v2 settings.
Parsing: full-string bare integer, else LAST in-range token (v2 critic S4). One verbatim
retry per unparseable response, then missing. Missing > 10% = mandatory caveat;
> 25% = instrument failure for the stratum; arm absent/partial (e.g. budget abort)
= **INCOMPLETE**, no substantive verdict. No 4-point robustness arm (instrument-level
framing robustness was established in v2 on 102 items, ρ 0.82–0.93, and the instrument
is unchanged); no Tier-0 re-run (inherited from v2, see Disclosures).

## Frozen statistics (per model)

Cell construction: model **class-cell mean** = mean of that class's 20 ratings;
**adjective mean** = mean of that adjective's 2 ratings. Human side is always the
anchored-half temporal class-cell mean (above). Ties: average ranks throughout.

1. **PRIMARY (the caveat-2 read, same read as v2):** Spearman ρ between the 4 widened
   model class-cell means and the 4 human anchored class-cell means. At n = 4 the
   ρ lattice is coarse ({0, ±0.2, ±0.4, ±0.8, ±1.0…}) — **a Spearman over ~4 class-cells
   is coarse and is read only jointly with the secondary statistic.**
2. **SECONDARY, finer grain (chosen now, before any data):** adjective-grain Spearman —
   the 40 held-out adjective means vs the human anchored temporal class-cell mean
   *assigned to each adjective by its class* (4 distinct human values; average-rank
   ties), with a 10,000-resample percentile bootstrap over the 40 adjectives, 95% CI.
   This is the same comparison at a grain with real resolution; it asks whether the
   model's temporal ratings order adjectives by class the way the human anchored
   gradient does.
3. **Descriptive only (no gate):** pooled item-grain Spearman (n = 80, class-assigned
   human values); partial Spearman at adjective grain controlling Zipf
   (rank-residualization) as a frequency sanity number; per-class adjective spread;
   **carryover consistency** — the 16 carryover adjectives' v2b means vs their v2
   single-item temporal ratings (from committed `raw/*-heldout.json`), per model;
   new-6 vs carryover-4 subgroup means. A NaN ρ from constant model output counts as 0
   and its CI as undefined (degenerate-output caveat mandatory).

## Frozen verdict map (per model, then stratum)

- **REPLICATES:** class-cell ρ ≥ 0.40 (the smallest lattice point above v2's ≥ 0.30
  within-class bar) AND adjective-grain ρ ≥ 0.20 AND adjective-grain bootstrap 95% CI
  lower bound > 0.
- **FAILS-TO-REPLICATE:** adjective-grain bootstrap 95% CI upper bound < 0.20 (the
  human-tracking band confidently excluded; subsumes confidently-negative).
- **STILL-TOO-THIN:** anything else (CI straddles the band; grains disagree without CI
  resolution; undefined CI).

Stratum verdict: **REPLICATES** if ≥ 2 of 3 models REPLICATE and none FAILS;
**FAILS-TO-REPLICATE** if ≥ 2 FAIL; otherwise **STILL-TOO-THIN / MIXED** (per-model
detail reported). All three outcomes are written into a refinement of
`result/aann-behavioral-gradient-v2` caveat 2; a null or a fail is a first-class
result. Thresholds are ≥/inclusive; no post-hoc adjustment under any outcome.

## Spend (config/budget.md)

240 calls (80 × 3). Pre-flight from the v2 run's **measured billed** held-out per-call
rates (A $0.000331, B $0.000080, C $0.000115): point estimate **$0.042**; with retries
and variance, **expected ≈ $0.04–0.09 billed**, well under the $0.30 abort flag coded
in `probe.py` (itself well under the $2.50 single-run flag and the $5.00/day budget).
Actual billed `usage.cost` recorded in `raw/cost-log.txt` and the run record.

## Disclosures for the pre-run critic (honest strains)

1. **The class-cell count cannot be widened.** Only 4 adjective classes are valid on
   temporal nouns; "widening" is within-cell (4 → 20 items per cell, 1 → 2 items per
   adjective, 24 new adjectives, 5 nouns instead of 4, all 3 templates). The primary
   read is therefore still a 4-point Spearman; the secondary adjective-grain read is
   doing the real inferential work. If the critic judges that this strains "same read
   as v2", the remedy is wording, not new machinery — both grains are declared here,
   pre-data.
2. **The adjective-grain statistic is new at gate level** (v2 gated nothing at that
   grain). It is the same model-vs-anchored-half comparison, just finer; it is declared
   before any data exist.
3. **Tier-0 is inherited, not re-run:** all three models passed Tier-0 in v2 (23–24/24)
   one day earlier under byte-identical settings. If the critic requires a fresh Tier-0,
   it adds 72 calls ≈ $0.013 — flag it.
4. **Carryover pooling:** 16 of 40 adjectives were already rated (once each) in v2's
   held-out arm. They are re-rated fresh here; both subgroups are held-out from human
   raters by construction; subgroup means and carryover consistency are reported
   descriptively.
5. **No analyze.py exists yet.** It must be written and committed at freeze time,
   before any call, computing exactly the statistics above (the post-run verifier then
   recomputes from raw with independent code, per house protocol).

## Anchor discipline (unchanged from v2)

Held-out items have **no human ratings by construction**; the evidential type is
**gradient replication** against the human **anchored-half** temporal ordering. The arm
anchors to `resource/mahowald-2023-aann-stimuli` via the anchored-half gradient it must
replicate; it makes **no independent human claim**, and the result page will state
exactly that.

DRAFT written 2026-06-13, before any model call. To freeze: pre-run critic pass →
apply fixes → commit as `PREREG.md` (this draft retained for the diff trail).
