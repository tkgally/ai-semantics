# PREREG — DRAFT (NOT YET FROZEN) — AANN temporal held-out widening (v2b)

**STATUS: DRAFT, pre-run-critic fixes applied (2026-06-13, verdict GO after fixes).**
This pre-registration becomes binding only when committed as `PREREG.md` (the freeze),
and **no finding-bearing model call may be made before that freeze** (`probe.py` refuses
to run while only the draft exists, and refuses to run if `analyze.py` is absent — the
analysis code is part of the freeze). No model output for this run exists at draft time;
every number below was set from the committed v2 artifacts only.

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

**Pre-run critic rulings, resolved (no conditionals remain):** the adjective-grain
secondary read is **gate-bearing, full stop** (Conditions 2 and 4 of the governing
decision: grain and thresholds declared and frozen pre-run — which this document does);
binding **Condition 8 binds per-run**, so the 4-point framing-robustness subsample
**is run** (caveat-bearing); and Tier-0 is run **fresh** in this run (gate-bearing per
model), not inherited from v2.

## Arms (three; all required; 432 calls total)

| Arm | Items × models | Calls | Bearing |
|---|---|---|---|
| `heldout-temporal` | 80 × 3 | 240 | gate-bearing gradient read (primary + secondary) |
| `tier0` (fresh) | 24 × 3 | 72 | gate-bearing instrument check, per model |
| `robustness` (4-point) | 40 × 3 | 120 | caveat-bearing only, never gate-bearing |

An absent or partial file for **any** arm (e.g. after a budget abort) makes the run
**INCOMPLETE**: no substantive verdict is emitted.

## Frozen inputs (committed before the run)

- `stimuli.json` — seed 20260613, built by `prep.py` **without the upstream mirror**,
  entirely from the committed v2 artifacts (`../2026-06-12-aann-behavioral-probe-v2/
  stimuli.json` and `human_class_means.csv`); templates recovered exactly from committed
  v2 sentences (consistency-asserted), including the upstream "tourish" typo template,
  kept for instrument continuity (and probed by a pre-declared sensitivity recompute,
  below).
  - **Geometry (main arm):** 4 temporal-eligible adjective classes (ambig, neg, pos,
    quant — the only classes valid on temporal nouns in Mahowald's Exp-2 design;
    **4 class-cells is the maximum possible**, so widening is *within-cell*) × 10
    held-out adjectives (6 **new** + the 4 **v2 carryovers**) × 2 items each =
    **80 items**; all 5 Mahowald temporal nouns (days, hours, weeks, months, years),
    nums three/five, all 3 temporal templates, balanced by rotation (nouns 16 each;
    nums 40/40; templates 28/28/24). The 80 items are **byte-identical** to the
    pre-critic build (verified by diff when the critic's additions were embedded).
  - **Tier-0 pairs:** the 24 v2 Tier-0 forced-choice pairs, copied **verbatim**
    (byte-identical) from the committed v2 `stimuli.json` into this run's
    `stimuli.json` (asserted at prep time).
  - **4-point subsample:** a fixed, pre-declared 40-item subset of the 80 main items —
    exactly **one item per adjective** (so 10 per class, class-balanced automatically),
    **template-balanced** (per-class template counts forced to the most balanced
    multiset {3,3,4}), selected **deterministically and seeded**: classes in sorted
    order, adjectives in the frozen build order, the 2^10 per-adjective item-index
    tuples enumerated lexicographically, filtered to template-balanced ones, one drawn
    per class with `random.Random(20260613)`. The 40 ids are frozen in
    `stimuli.json["robustness_4pt"]["ids"]` with the rule text alongside.
  - **Frequency control (same procedure as v2, Condition 5):** wordfreq 3.x Zipf (en),
    per-class median; the 6 new adjectives' class median within ±0.5 of the Mahowald
    class median, and the combined 10 within ±0.5 too — asserted mechanically in
    `prep.py`; **all 4 classes pass** (ambig 4.065|3.91|3.91, neg 3.52|3.505|3.34,
    pos 4.07|3.855|3.995, quant 3.43|3.405|3.38 — mahowald|new-6|combined-10, exact
    values as embedded in the `stimuli.json` audit). Local wordfreq (3.1.1) verified to
    reproduce every committed v2 Zipf value exactly (commensurability guard, asserted).
    New adjectives appear in neither Mahowald's 50 nor the v2 held-out 24 (asserted).
- **Human yardstick** (copied verbatim into `stimuli.json` from the frozen v2
  `human_class_means.csv`): anchored temporal class-cell means — quant 8.4508 >
  ambig 8.2526 > pos 8.0183 > neg 7.5673. No predicted ordering is hardcoded anywhere
  in the scoring path; scoring is against these empirical means only (Condition 1).
- **`analyze.py` exists at freeze** and computes exactly the statistics below
  (selftested on synthetic data); `probe.py` refuses to run without it. The post-run
  verifier recomputes from raw with independent code.

## Frozen instrument (identical to v2; no new operationalization)

Primary 0–100 framing, prompt byte-identical to v2's `P100`; 4-point robustness framing
byte-identical to v2's `P4`; Tier-0 forced choice byte-identical to v2's `PT0`.
Temperature 0; max_tokens 64 (A `claude-sonnet-4.6`, B `gpt-5.4-mini`) / 512
(C `gemini-3.5-flash`, `reasoning: {"effort": "minimal"}`), per `config/models.md` and
the v2 settings.

**Parsing.** Integer arms (0–100 and 4-point): full-string bare integer, else LAST
in-range token (v2 critic S4). **Tier-0 (gate): full-string A/B, else the LAST
standalone A/B token** — the same last-token convention, fixing v2's documented
first-bare-token defect; the v2-style FIRST-token parse of the same final response is
also recorded per row and reported **descriptively only**, for continuity with the v2
Tier-0 numbers. One verbatim retry per (gate-)unparseable response, then missing.

**Missingness (main arm):** > 10% = mandatory caveat; > 25% = instrument failure for
the stratum (forces that model's gradient verdict to STILL-TOO-THIN). Any arm
absent/partial = **INCOMPLETE**, no substantive verdict.

## Frozen gates and statistics (per model)

**Cell construction (main arm).** Model **class-cell mean** = mean of that class's
available parsed ratings; **adjective mean** = mean of that adjective's available
parsed ratings (i.e. of 2, or of 1 if the other is missing); an adjective with **both**
items missing is **dropped and counted/reported** (`adjectives_dropped_all_na`). Human
side is always the anchored-half temporal class-cell mean (above). Ties: average ranks
throughout.

**NaN rule (applies to gate statistics too, not only descriptives):** a NaN ρ from
degenerate (constant) model output counts as **0** and its bootstrap CI is undefined
(None) ⇒ STILL-TOO-THIN, with a mandatory degenerate-output caveat. A NaN inside a
single bootstrap resample (e.g. an all-tied draw) likewise **counts as 0 — zeroed, not
dropped** (this matches `analyze.py` exactly).

0. **TIER-0 GATE (fresh, this run):** the 24 v2 pairs, scored by the last-token parse.
   **Pass = ≥ 20/24 AANN preferred** (inclusive; a missing response cannot match and so
   counts against the total; >25% missing is instrument failure regardless).
   **Pre-declared failure consequence:** Tier-0 failure = **instrument failure for that
   model** → the model is **excluded from the ≥2-of-3 stratum count**; its gradient
   numbers and verdict are reported **descriptively only**, never counted. If **fewer
   than 2 models** pass Tier-0, the stratum verdict is **INSTRUMENT FAILURE** (no
   substantive stratum verdict). The v2-parse first-token score is reported
   descriptively beside the gate score.
1. **PRIMARY (the caveat-2 read, same read as v2):** Spearman ρ between the 4 widened
   model class-cell means and the 4 human anchored class-cell means. At n = 4 the
   ρ lattice is coarse (**{0, ±0.2, ±0.4, ±0.6, ±0.8, ±1.0}** — the full n=4 lattice) —
   **a Spearman over 4 class-cells is coarse and is read only jointly with the
   secondary statistic.**
2. **SECONDARY, finer grain (gate-bearing, full stop — declared before any data):**
   adjective-grain Spearman — the 40 held-out adjective means vs the human anchored
   temporal class-cell mean *assigned to each adjective by its class* (4 distinct human
   values; average-rank ties), with a 10,000-resample percentile bootstrap over the
   adjectives, 95% CI, **bootstrap seed 20260613** (declared here; coded in
   `analyze.py`). This is the same model-vs-anchored-half comparison at a grain with
   real resolution.
3. **4-POINT FRAMING ROBUSTNESS (caveat-bearing, never gate-bearing):** per model,
   item-level Spearman between the 0–100 rating and the 4-point rating on the 40-item
   subsample (pairs where both parsed). **ρ < 0.50 (strict; 0.50 exactly is not
   fragile) or NaN/undefined ⇒ mandatory instrument-fragility caveat for that model**
   — v2's exact fragility semantics. The caveat attaches to the result page; it never
   changes a gradient verdict.
4. **TOURISH-TEMPLATE SENSITIVITY (pre-declared MANDATORY descriptive):** `analyze.py`
   recomputes the class-cell and adjective-grain statistics (same code path, same
   bootstrap seed, the all-80 missingness gate reused) **excluding template-2 items**
   (the upstream "The tourish stayed …" typo template; 56 items remain, every adjective
   keeps ≥ 1 item). **The gate stays on all 80 items.** If the verdict category under
   the exclusion differs from the all-80 verdict, a **mandatory caveat sentence** (the
   exact sentence is generated by `analyze.py`) attaches to the result.
5. **Descriptive only (no gate):** pooled item-grain Spearman (n = 80, class-assigned
   human values); partial Spearman at adjective grain controlling Zipf
   (rank-residualization); per-class adjective spread; **new-only adjective-grain ρ**
   (the 24 new adjectives alone); **carryover consistency** — the 16 carryover
   adjectives' v2b means vs their v2 single-item temporal ratings (from committed
   `raw/*-heldout.json`), per model, as **Spearman + mean signed difference (v2b minus
   v2)** — a *consistency* number, **not test–retest** (v2 rated 1 item per adjective;
   v2b averages 2 different items); new-6 vs carryover-4 subgroup means, read with the
   pre-declared **noun-asymmetry note**: the frozen rotation gives new adjectives more
   days/hours items (12/12/8/8/8 over days/hours/months/weeks/years) and carryovers
   more months/weeks/years (4/4/8/8/8), so subgroup differences are not interpretable
   as adjective-set effects alone.

## Frozen verdict map (per model, then stratum) — exactly one reading

- **REPLICATES:** class-cell ρ ≥ 0.40 (inclusive; the smallest lattice point above
  v2's ≥ 0.30 within-class bar) AND adjective-grain ρ ≥ 0.20 (inclusive) AND
  adjective-grain bootstrap 95% CI lower bound > 0 (strict).
- **FAILS-TO-REPLICATE:** adjective-grain bootstrap 95% CI upper bound < 0.20 (strict;
  the human-tracking band confidently excluded; subsumes confidently-negative).
- **STILL-TOO-THIN:** anything else (CI straddles the band; grains disagree without CI
  resolution; undefined CI; >25% missing).
- **PRECEDENCE:** REPLICATES is evaluated before FAILS-TO-REPLICATE. If both branches
  fire (point estimate outside its own percentile CI — a bootstrap pathology), the
  verdict is **STILL-TOO-THIN with a contradiction note** (already mechanical in
  `analyze.py`).

Stratum verdict, over the **Tier-0-passing models only**: **REPLICATES** if ≥ 2
counted models REPLICATE and no counted model FAILS; **FAILS-TO-REPLICATE** if ≥ 2
counted models FAIL; otherwise **STILL-TOO-THIN / MIXED** (per-model detail reported).
Fewer than 2 Tier-0 passers ⇒ **INSTRUMENT FAILURE** (above). All outcomes, including
the null, are written into a refinement of `result/aann-behavioral-gradient-v2`
caveat 2; a null or a fail is a first-class result. Thresholds' inclusivity is as
stated per-threshold above and frozen in `analyze.py`'s docstring; no post-hoc
adjustment under any outcome.

## Spend (config/budget.md)

432 calls (144 × 3 models: 80 main + 24 Tier-0 + 40 four-point). Pre-flight from the
v2 run's **measured billed** per-call rates per arm (held-out 0–100: A $0.000331,
B $0.000080, C $0.000115; Tier-0: A $0.000263, B $0.000068, C $0.000221; 4-point:
A $0.000355, B $0.000083, C $0.000114): point estimate **$0.077** ($0.042 main +
$0.013 Tier-0 + $0.022 4-point); with retries and variance, **expected ≈ $0.08–0.15
billed**, under the **$0.30 abort flag** coded in `probe.py` (itself well under the
$2.50 single-run flag and the $5.00/day budget). Actual billed `usage.cost` recorded
in `raw/cost-log.txt` and the run record; **calls with missing `usage.cost` are
counted and logged** (never silently discarded) — a nonzero missing-cost count is a
mandatory note in the budget ledger because the billed total then undercounts.

## Disclosures (binding on the result page)

1. **The class-cell count cannot be widened.** Only 4 adjective classes are valid on
   temporal nouns; "widening" is within-cell (4 → 20 items per cell, 1 → 2 items per
   adjective, 24 new adjectives, 5 nouns instead of 4, all 3 templates). The primary
   read is therefore still a 4-point Spearman; the secondary adjective-grain read
   (gate-bearing, declared pre-data) does the real inferential work.
2. **The adjective-grain statistic is new at gate level** (v2 gated nothing at that
   grain). It is the same model-vs-anchored-half comparison, finer; declared before
   any data exist; ruled in scope by the pre-run critic under Conditions 2/4.
3. **Carryover pooling:** 16 of 40 adjectives were already rated (once each) in v2's
   held-out arm. They are re-rated fresh here; both subgroups are held-out from human
   raters by construction; subgroup means and carryover consistency are reported
   descriptively (with the noun-asymmetry note).
4. **Result-page disclosure note (mandatory):** *new-adjective class membership is
   project-assigned; no human validation is possible for held-out items by
   construction.* The evidential type is gradient replication only.

## Anchor discipline (unchanged from v2)

Held-out items have **no human ratings by construction**; the evidential type is
**gradient replication** against the human **anchored-half** temporal ordering. The arm
anchors to `resource/mahowald-2023-aann-stimuli` via the anchored-half gradient it must
replicate; it makes **no independent human claim**, and the result page will state
exactly that.

DRAFT written 2026-06-13, before any model call; pre-run critic fixes applied
2026-06-13, still before any model call. To freeze: the orchestrator commits this as
`PREREG.md` (this draft retained for the diff trail).
