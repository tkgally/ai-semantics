# PREREG — BLiMP forced-choice sweep (A3b, s205)

**Frozen s205, 2026-07-10, BEFORE any model call.** Design:
[`design/blimp-forced-choice-sweep-v1`](../../designs/blimp-forced-choice-sweep-v1.md). Gates **RATIFIED
s205**: [`decisions/resolved/blimp-forced-choice-sweep-design`](../../../wiki/decisions/resolved/blimp-forced-choice-sweep-design.md)
— **Q1-B / Q2-A / Q3-A**, plus binding condition **C8**. This file freezes the paradigm list, the depth
strata, the human anchor, the elicitation, the verdict map with numeric thresholds, and the anti-cheat
fence. **Nothing below may be touched after any accuracy is observed.**

## The question

On a **human-agreement-anchored** behavioral 2AFC sweep of BLiMP English grammatical minimal pairs, run
on the panel:

- **R1 (PRIMARY, human-anchored — DESCRIPTIVE/DIRECTIONAL ONLY per C8+F2):** does each model's
  per-paradigm forced-choice accuracy track BLiMP's per-paradigm human-agreement profile (`total_mean`)
  across the 40 selected paradigms (Spearman ρ_prof, per model)? "Are the models hard exactly where
  people are hard?"
- **R2 (SECONDARY, STRICTLY within-panel):** does forced-choice error concentrate on the
  structurally-deep paradigms (scope + island) relative to the shallow-local ones (adjacent agreement)?
- **R2h (human-anchored sub-reading):** is the panel's shallow-minus-deep accuracy gap **larger** than
  the human shallow-minus-deep agreement gap (the panel finds deep contrasts *disproportionately* harder
  than humans do)?

**Anchor (Q3-A):** the result carries `anchors: resource/blimp` — a genuine **human-comparison** line,
NOT internal-contrast-only. Absolute accuracy is a **contamination upper bound**, never a headline.

## Frozen instrument (built + committed by `prep.py` BEFORE any model call)

- **Selection (Q1-B via the maximal-defensible WHOLE-CATEGORY rule; F6-sharp + the ratification vote's
  mechanical anti-cherry-pick condition).** Select **every paradigm in the on-axis `linguistics_term`
  categories**; assign each to a depth stratum by a **structural locality rule**; **no within-category /
  within-stratum hand-picking**. Selection references **only** BLiMP's own structural metadata
  (`paradigm_meta.json`, each file's `linguistics_term`/`field`, fetched firsthand), **never the
  human-agreement values** — human-agreement-BLIND by construction. **40 paradigms** result (well above
  F2's ≥16 floor). Exact list + sha256 pins + stratum + human anchor in
  [`paradigms.json`](paradigms.json) / [`items.json`](items.json).

  | stratum (depth rank) | n | on-axis category source | human agreement range |
  |---|---|---|---|
  | **local** (1, shallow — adjacent, n-gram-detectable) | 12 | `determiner_noun_agreement` (8) + regular/irregular `subject_verb_agreement` (4) | 0.850–0.960 |
  | **medium** (2 — agreement across an intervener) | 2 | `distractor_agreement_*` (the `distractor_` split of `subject_verb_agreement`) | 0.810–0.857 |
  | **scope** (3, deep — c-command polarity/quantifier licensing) | 11 | `npi_licensing` (7) + `quantifiers` (4) | 0.720–0.980 |
  | **island** (4, deep — long-distance filler-gap / island) | 15 | `island_effects` (8) + `filler_gap_dependency` (7) | 0.606–0.990 |

  `subject_verb_agreement` is split by BLiMP's own `distractor_` marker — a **structural** criterion (an
  intervener between controller and verb), not a hand-pick.

- **Excluded categories (off-axis, with structural reasons — F6).** `binding` (referential-dependency,
  different axis), `anaphor_agreement` (binding-domain), `argument_structure` (lexical-semantic
  selection), `s-selection` (animacy selectional restriction), `control_raising` (A-movement/PRO +
  there-raising confound), `irregular_forms` (morphological-lexical), `ellipsis` (deletion licensing).
  Full reasons in [`paradigms.json`](paradigms.json).

- **Two paradigms with a human-agreement row but NO data file on master (404) are excluded for
  data-availability (structural), not for their values:** `coordinate_structure_constraint_subject_extraction`
  (human 0.514) and `wh_questions_object_gap_long_distance` (0.47). **Limitation flagged:** both happen
  to be low-agreement, so their absence removes 2 of the hardest human points — **mildly conservative
  for R1** (an alignment reading is slightly *harder* to obtain without the low-human tail, not easier).

- **Items.** SEED 20260710. For each paradigm, a fixed, per-paradigm-seeded subsample of **N=30 minimal
  pairs** from its 1,000 (deterministic `random.Random(sha256(SEED-uid))`). Each pair
  `(sentence_good, sentence_bad)`. Full 1,000-pair `.jsonl` files are sha256-pinned in
  [`paradigms.json`](paradigms.json) (`sha256_full`) but NOT committed (recipe-not-corpus, CC-BY); the
  frozen 30-pair subsample IS committed in [`items.json`](items.json).

- **Human anchor.** `total_mean` per paradigm, joined from the committed, sha256-pinned
  `experiments/data/blimp/human_validation_summary.csv` (sha256 `ea0e7c21…`), catalogued in
  [`resource/blimp`](../../../wiki/base/resources/blimp.md). **F4 floor 0.60:** paradigms below 0.60
  would be dropped from the R2 accuracy strata (contested gold); **freeze finding: all 40 clear 0.60**
  (min `sentential_subject_island` 0.606), so no paradigm is F4-dropped.

## Elicitation (Q2-A — behavioral 2AFC, BOTH orders, position-bias netted)

- Panel = [`config/models.md`](../../../config/models.md) `panel.A/.B/.C` (never hardcode slugs).
  Temperature 0, zero-shot, single-turn. `google/*` gets `reasoning={"effort":"minimal"}` + a small
  `max_tokens` (forced-choice = one digit; config Caveat 1 — bound the gemini reasoning bill).
- **Prompt (frozen, `probe.py`):** *"Which of these two sentences is the more grammatically acceptable
  sentence of standard written English? Sentence 1: {s1} Sentence 2: {s2}. Answer with ONLY the single
  digit 1 or 2 — no other text."*
- **Both orders per pair:** `gf` (good = Sentence 1) and `gs` (good = Sentence 2). A pick is **correct**
  iff the model selects `sentence_good`. `parse_choice` extracts 1/2 (with a one verbatim retry on an
  unparsed non-error reply).
- **Scored quantities (both pre-registered):** (a) **order-averaged accuracy** (mean correct over the
  two orders) — PRIMARY for all readings; (b) **consistency accuracy** (correct in *both* orders) —
  position-bias-hardened robustness; plus the **position-lock rate** (same digit in both orders) and
  **ans1_rate** diagnostics.

## Metrics + verdict map (FROZEN thresholds; direction fixed; copied verbatim into `analyze.py`)

`acc(m,p)` = model m order-averaged accuracy on paradigm p; `H(p)` = human agreement; ρ_prof(m) =
Spearman over the 40 paradigms of `acc(m,·)` vs `H(·)`; bootstrap CI over paradigms (B=5000, seed
20260710). Aggregate verdicts require **≥2/3 models**.

- **R1 — profile alignment (DESCRIPTIVE/DIRECTIONAL ONLY this run, per C8; report ρ_prof + CI):**
  **PROFILE-ALIGNED** iff ρ_prof > **+0.40** (and NOT F3-saturated) on ≥2/3; **PROFILE-DIVERGES** iff
  ρ_prof < **+0.20** (and NOT F3-saturated) on ≥2/3; **[+0.20,+0.40] = PROFILE-INCONCLUSIVE**
  (pre-registered dead-zone; no uncovered gap). **Power (F2):** n=40 → two-sided p<0.05 at |ρ|≈0.31, so
  the +0.40 band is above significance and ρ_prof is genuinely powered — **but per C8 R1 is
  non-promotable on this run alone** regardless (a training-frequency confound control is the
  pre-registered next step; see C8). **F2 symmetry:** this descriptive-only / non-promotable status is
  fixed HERE by the n=40 power calc, applied identically whether ρ_prof is positive or negative.
- **R2 — depth gradient (verdict-bearing, STRICTLY within-panel, no human key):** **DEPTH-GRADED** iff
  `mean acc(shallow=local) − mean acc(deep=scope∪island) ≥ +0.05` on ≥2/3; **DEPTH-FLAT** otherwise
  (includes reversed). Uses only the panel's own shallow-vs-deep accuracy gap. (All 40 pass F4, so no
  paradigm is dropped from the strata.)
- **R2h — vs the human dip (human-anchored sub-reading, F5-labelled human-comparison):**
  **EXCEEDS-HUMAN-DIP** iff `(panel depth-gap) − (human depth-gap) > +0.05` on ≥2/3 (panel finds deep
  contrasts *disproportionately* harder than humans); **TRACKS-DIP** iff within ±0.05 on ≥2/3;
  **BELOW-HUMAN-DIP** otherwise. Human depth-gap = mean H(local) − mean H(deep), fixed at freeze.
- **F3 saturation/range guard:** if a model's across-paradigm `acc` SD < **0.03** (all near ceiling),
  ρ_prof(m) is **INCONCLUSIVE**, not a coefficient (a memorization-saturation signal). Per-model
  **absolute-accuracy dispersion (mean, SD, range)** is reported as the **contamination diagnostic** (a
  frequency-driven pseudo-alignment would show high absolute accuracy with compressed dispersion).
- **Instrument-failure guard (Q2-A):** if position-lock rate > **0.50** AND |ans1_rate − 0.5| > **0.40**
  on ≥2/3 models, the 2AFC has collapsed to position-answering → **INSTRUMENT-FAILURE** voids the
  accuracy readings (reported as such, not silently dropped). A single position-locked model is reported
  per-model, not a global void.
- **Pre-named nulls (all first-class):** PROFILE-DIVERGES; PROFILE-INCONCLUSIVE; DEPTH-FLAT;
  contamination-saturation (F3 fires on ≥2/3 → the readings are voided and saturation is the finding);
  INSTRUMENT-FAILURE. **n=3 models; orderings, not pooled coefficients; ρ_prof reported per model.**

## C8 (BINDING — the s205 ratification's added condition)

R1 (PROFILE-ALIGNED) is **non-promotable to a `claim`** without a training-frequency confound control
(the F7 content-word-swap arm, or a corpus-frequency covariate partialled from ρ_prof). **This run DEFERS
the control:** R1 is reported **descriptive/directional + non-promotable-on-this-run**; the C8 frequency
control is the pre-registered step for a later promotion-prep session. The verdict-bearing outputs this
run are **R2** (within-panel depth gradient) and **R2h** (human-anchored excess-over-dip); the F3
absolute-accuracy dispersion is the contamination diagnostic.

## Cost (pre-flight, re-estimated at freeze)

40 paradigms × 30 pairs × 2 orders × 3 models = **7,200 calls**; prompt ≈ 60–110 tokens (two short
sentences + instruction), completion ≈ 1 token. At the corrected rate card (`openrouter.py`) ≈ **$0.6–1.6**
(claude ≈ $0.5, gpt ≈ $0.1, gemini the wildcard — reasoning suppressed to `minimal`, `max_tokens=128`).
**Under the $2.50 prefer-split flag → no split.** Per-model hard `ABORT_USD = 1.60` in `probe.py`. Every
call records `usage.cost` via [`experiments/lib/openrouter.py`](../../lib/openrouter.py).

## Anti-cheat fence (PROTOCOL §B)

The 40-paradigm list, the stratum assignment (structural, human-agreement-blind), the subsample seed +
N, the elicitation prompt + both orders, the ρ_prof bands (+0.40/+0.20 with the INCONCLUSIVE dead-zone),
the F3 saturation SD (0.03), the DEPTH/R2h margins (0.05), the instrument-failure thresholds, and the
F4 floor (0.60) are **all frozen here BEFORE any model call**. No band, stratum, paradigm, or threshold
is added/dropped/tuned after any accuracy is seen. PROFILE-DIVERGES, DEPTH-FLAT, and every null are
pre-named first-class. Absolute accuracy is a contamination upper bound and is never the headline.
Registers a [`predictions.md`](../../../wiki/predictions.md) row at freeze; outcome updated the run
session.
