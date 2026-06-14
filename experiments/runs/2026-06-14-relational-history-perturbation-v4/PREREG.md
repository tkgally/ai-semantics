# PREREG — relational-history-perturbation-v4 — **FROZEN 2026-06-14**

> **FROZEN by the orchestrator 2026-06-14**, after the independent pre-run critic's
> **GO-after-fixes** verdict and the application of its two should-fix text calibrations
> (logged immediately below) — **before any finding-bearing call**. Harvest and
> certification calls are stimulus-construction (already run; not finding-bearing) and the
> frozen `stimuli.json` sha256 below was produced before any probe/preflight call. The
> draft this was frozen from is kept verbatim as `PREREG-draft.md`.

## Pre-run critic revisions (fix log)

**2026-06-14 — independent pre-run critic: GO-after-fixes (zero code changes).** Rulings:
- **Question A (the flagged borderline — chronology STAMP vs v3 physical position): ruled
  INSIDE-CLASS INDICATOR HYGIENE; NO `decisions/open/` page required.** The construct is
  unchanged (does interpretation track *where in the chronology* conflicting evidence lands,
  or only the content set?); the stamp changes *how cleanly*, not *what* is measured, and is
  exactly the within-arm decoupling the v3 verifier named as the real next step. The design
  did not smuggle back the v3 over-claim: a pure position reader lands in the
  relational-claim-free TEXT-POSITION ARTIFACT terminal. **The run is therefore NOT blocked.**
- **Adaptation 2 (subsume v3's {fwd,rev} into DPOS + variant): faithful, inside-class.**
- Verified read-only: 5 verdict branches reachable; `stimuli.json` sha256 matches; geometry
  exact (claude 240 / gemini 220; per-cell 48/44); CLAST⊥physical-last cov = 0 in every
  cluster; byte-identical multiset holds; build-time `clast_cid`/`last_cid`/`decisive_cid`
  and the probe's `picked_chron_last`/`picked_phys_last` recompute with 0 mismatches; freeze
  gate refuses to run without PREREG.md; never-parse-truncated, hard-stop, and crash-safe
  resume all correct; the instrument does not bias toward a positive (the anti-null stimulus
  bias cuts against the conjecture's bet; degenerate CIs satisfy no clause).

**Two should-fix TEXT calibrations applied before freeze (no code change):**
1. **Stamp-respect control licenses only "not derailed by non-monotonic layout," NOT "reads
   stamp values."** The control is a single-twin record (every line points to the one twin
   regardless of stamps), so a model that ignores stamp *values* passes it trivially.
   Consequence (now stated in §Measures and to be repeated in the result page): **a clean
   Δ_pos / null Δ_chron outcome is INDISTINGUISHABLE from stamp-blindness** and must be
   written as TEXT-POSITION ARTIFACT, **never** as "the model chose to ignore recency."
2. **The ≥36 null-floor "with margin" claim is fragile at v3-observed attrition.** Each
   gated-out cluster removes 4 trials/cell; gemini (44/cell) tolerates losing only 2 of 11
   clusters before floor36 is unmet, claude (48/cell) only 3 of 12. At the v3-observed gate
   survival (claude 5/9 ≈ 44% loss, gemini 7/9 ≈ 22%) the null floor **may be unmet**, in
   which case the honest outcome is the **named-gap INCONCLUSIVE** label, not a certified
   null. The instrument still fails safe — attrition cannot manufacture a false FALSIFIED
   (the orthogonal 2×2 routes a position-follower into Δ_pos, not Δ_chron), only a
   non-certification. §"Realized geometry" and the power caveat are softened accordingly.

Design (authoritative): `experiments/designs/relational-history-perturbation-v4.md`.
v4 = the v2/v3 instrument with the v3 verifier's named next step implemented (a
non-adjacent perturbation point dissociating stamped chronology from text-position within
one arm) and the v3 fix-list applied (gpt dropped; claude/gemini powered up). It supersedes
v3 (`result/relational-history-perturbation-v3`, INCONCLUSIVE/MIXED) at the **verdict level
only** — no pooling, no numeric comparison with v3.

## Adaptations of the frozen design — FLAGGED FOR THE PRE-RUN CRITIC

The design's §"Gate check" left one borderline call **for the orchestrator to decide
whether a `decisions/open/` page is warranted**, and this build made two further
operational choices the critic must rule on. **If the critic judges any of these a new
*operationalization* (not indicator hygiene), it must open a `wiki/decisions/open/` page;
ratification is cross-session, so the run is BLOCKED this session** — the build + ruling is
still legitimate progress (NEXT.md backlog item 1).

1. **Chronology indicator: explicit per-line round STAMP vs v3 physical position (the
   design's flagged borderline).** v3 conveyed chronology purely by physical position; v4
   conveys it by an explicit "Round k:" stamp and deliberately places the decisive line
   non-terminally. Provisional judgement (design + this build): **inside-class hygiene** —
   same construct ("does interpretation track *where in the chronology* conflicting
   evidence lands"), a sharper indicator that decouples the two readings v3 confounded. The
   stamp introduces a readability assumption, handled by the **stamp-respect control** (a
   reasonable critic could still call this a new operationalization). `contingent-on` is
   left **empty** on that provisional judgement.
2. **v3's presentation-direction {fwd, rev} factor is SUBSUMED, not retained as a separate
   factor.** In v4, physical position is a *manipulated* factor (DPOS), so v3's
   earliest-first/most-recent-first reversal (which WAS the position manipulation) cannot be
   re-added without double-counting position and contradicting a fixed decisive-position.
   The design's "retained convergent check that a robust effect survives reordering" is
   provided instead by (a) the 4 frozen line-ordering **variants** per cell and (b) the
   **early-only / late-only** sensitivity split. Provisional judgement: **inside-class** (a
   faithful re-organization of the same robustness check). Flagged because the design's
   Conditions table literally lists "× presentation direction {fwd, rev}".
3. **The stamp-respect control and its threshold.** The v4-specific stamp-respect control
   is implemented as a single-twin record with **non-monotonic** stamps vs physical order;
   the model must still identify that twin. Model-level pass floor **STAMP_RESPECT_MIN =
   0.75**; below it the model is read **stamp-blind → METHODOLOGICAL NULL** on the
   chronology question. The control is **necessary, not sufficient**, for stamp-reading
   (it shows the model is not derailed by non-monotonic stamps; it does not prove the model
   uses stamps to compute recency). Flagged for the critic.

## Stimuli freeze

`stimuli.json`, generated deterministically by `build_trials.py` (SEED=20260614) from
`certification_report.json` (fresh harvest + per-description certification; full
certification census embedded in `stimuli.json`). v1 figures unchanged, original content
sha256 `a2709582a58e54378190b3e6e15191be4fe1f05d27c37830856f958371deb6c4` (hash-checked in
code).

**sha256 of `stimuli.json` = `fca7c548d0887cab9898cd7d4860d24d26be3f8515079580f386660949a297cb`.**
No finding-bearing model call before this hash is committed to `PREREG.md`.

- **Panel (finding-bearing): claude + gemini only.** gpt dropped (design §Panel decision:
  two harvest+certification attempts showed gpt cannot supply solo-decodable near-twin
  descriptions at this difficulty).
- **The 2×2 within one arm**, per (model × pair × sample) cluster over the byte-identical
  4-description multiset {x1, x2, y1, y2}: **CLAST** ∈ {X, Y} (which twin owns the two
  latest round stamps R3,R4; R4 = the decisive line) × **DPOS** ∈ {late, early} (R4
  physically last vs non-terminal with chronologically-earlier lines after it) ×
  **VARIANT** ∈ {0,1,2,3} (frozen line-orderings/cell). = **16 mixed cells/cluster**.
  CLAST and the physically-last-line twin are balanced and orthogonal (cov 0; asserted at
  build).
- **Controls per cluster (4):** 2 CONSISTENT (single-twin, monotonic stamps, one per twin)
  + 2 STAMP-RESPECT (single-twin, non-monotonic stamps, one per twin). Manipulation gate =
  **all four** controls correct.
- **One frozen matcher figure-array permutation per cluster**, constant across that
  cluster's 16 mixed + 4 control cells (v1 discipline; frozen into `stimuli.json`).
- **Coined term** = a fresh frozen non-descriptive nonce per pair: `GORLAX`, `MIVUNT`,
  `ZEPHRO` (no v3 carryover).
- **Sample partition (pre-registered, carried from v3 critic S4):** sample s ∈
  {0,…,n_samples−1} takes roster positions 2s, 2s+1 of the frozen first-8-certified-in-
  harvest-order roster. The ≤12-word budget is enforced mechanically at harvest, before
  certification.
- **Realized geometry (after the one pre-registered top-up; recorded before freeze):**
  **claude 12/12 clusters** (all figures ≥ 8 certified); **gemini 11/12 clusters** — F4
  certified 7/8 after its one top-up, so pair-2 drops to 3 samples (min(4, 7//2, 16//2) =
  3), the pre-registered shortfall rule. → claude **240** finding-bearing trials (192 mixed
  + 48 controls); gemini **220** (176 mixed + 44 controls); **460 finding-bearing calls
  total**. The ≥3-gated-cluster guard and the per-cell ≥24/≥36 floors operate on realized
  gated counts. Per (clast × dpos) cell **before gating**: claude 48, gemini 44 (both ≥ 36).
  **Critic calibration (2026-06-14) — the ≥36 floor is fragile at v3-observed attrition:**
  each gated-out cluster removes 4 trials/cell, so gemini tolerates losing only 2 of 11
  clusters and claude only 3 of 12 before the null floor is unmet. At the v3-observed gate
  survival (claude 5/9 ≈ 44% loss, gemini 7/9 ≈ 22%) the ≥36 null floor **may not be met**,
  in which case the honest outcome is the **named-gap INCONCLUSIVE** label (clause 6), not a
  certified null. Attrition **cannot** manufacture a false FALSIFIED (the orthogonal 2×2
  routes a position-follower into Δ_pos, not Δ_chron), only a non-certification.
- **Stimulus-quality bias, disclosed (carried from v3):** certification selects for
  individually discriminative lines, which sharpens the X-vs-Y conflict — it biases
  **against** the ~0.5-noise-toward-the-null failure mode, not toward the conjecture's bet.

## Elicitation (forced format; truncation-resistant; frozen)

Carried verbatim from v3: forced single-label format (reply exactly one figure label
`P1`…`P6`, nothing else); completion cap 512 → truncation rare, not impossible; a reply
with `finish_reason == "length"` is **never parsed** for a pick (parse-fail → one stern
retry → NA); gemini keeps `reasoning: {"effort": "minimal"}`. Strict parse rule (strict /
non-strict / NA-after-one-retry); out-of-pair over parsed picks; per-model strict-compliance
rate; NA-concentration flag (> 25% in any clast×dpos cell). Liveness format-gate (both
models must return a parseable label) before preflight/full; liveness/preflight/harvest/
certification raw are never analyzed — `full` is the only finding-bearing dataset.

The v4 INTRO states **neutrally** that each line is stamped with its round (higher = more
recent) and that lines are **not** necessarily in round order. It does **not** instruct the
model to weight recency — whether the model spontaneously weights the stamp, the line order,
or treats the evidence as an order-free set is exactly what Δ_chron/Δ_pos measure.

## Measures (frozen)

- **Manipulation gate (per cluster):** all four controls correct → cluster enters the gated
  primary. Per-model control accuracy (consistent + stamp-respect separately) and ungated
  rates reported.
- **Stamp-respect sub-gate (model level):** stamp-respect accuracy ≥ STAMP_RESPECT_MIN =
  0.75, else the model is **stamp-blind** → METHODOLOGICAL NULL on the chronology question.
  **Critic calibration (2026-06-14):** because the stamp-respect control is a single-twin
  record, passing it shows only that the model is **not derailed by non-monotonic layout** —
  it does **not** prove the model reads stamp *values*. Therefore a clean Δ_pos / null
  Δ_chron outcome is **indistinguishable from stamp-blindness** and must be reported as
  TEXT-POSITION ARTIFACT, never as "the model chose to ignore recency."
- **PRIMARY — Δ_chron = ρ(pick = CLAST twin) − 0.5** and **Δ_pos = ρ(pick =
  physically-last-line twin) − 0.5**, over gated, parsed, in-pair mixed trials, pooled
  across the orthogonal factors (per-twin salience cancels by the balanced/orthogonal
  design). Both also reported per DPOS level (descriptive).
- **CIs:** clustered bootstrap, 10,000 resamples over (pair × sample) clusters per model,
  SEED=20260614, percentile method. **Degenerate (zero-width) CIs carry no inferential
  weight and satisfy no clause** (the v3 rule, retained).
- **Floors (per (clast × dpos) cell, min over the 4 cells):** ≥24 gated in-pair parsed
  trials for an effect clause (FALSIFIED / TEXT-POSITION ARTIFACT); **≥36** for
  null-certification.
- **Guard:** ≥ k = 3 gated clusters with in-pair data.
- **Sensitivity cuts — DESCRIPTIVE ONLY, never verdict-bearing:** leave-one-pair-out (×3);
  strict-format-only; NAs-as-out-of-pair; **late-only / early-only** (the convergent
  reordering check); pair-level (3-cluster) bootstrap cross-check. None flips a primary
  verdict.
- **No pooling with v3** (verdict-level supersession only).

## Decision rule (frozen; the verdict mapper is CODE in `analyze.py verdict()`)

Ordered, exhaustive if/else tree, evaluated top-down per model; first clause that fires is
the verdict. Precedence: **METHODOLOGICAL NULL > UNDER-POWERED > FALSIFIED > TEXT-POSITION
ARTIFACT > COMMUTATIVE-NULL-CERTIFIED > named-gap sub-label > INCONCLUSIVE/MIXED.**
Degenerate CIs satisfy no clause.

1. **METHODOLOGICAL NULL** if the model is **stamp-blind** (stamp-respect acc <
   STAMP_RESPECT_MIN) **OR** < 3 gated clusters with in-pair data — whatever the point
   estimates say.
2. **UNDER-POWERED** if out-of-pair > 0.5 on parsed picks.
3. **FALSIFIED (non-commutative, chronology-tracking; RECENCY if Δ_chron > 0, PRIMACY if <
   0)** if Δ_chron's CI excludes 0.5 **and** Δ_pos's CI includes 0.5, with ≥24 gated
   in-pair parsed trials in every (clast × dpos) cell. → the conjecture's invariance bet
   falsified for that model **under forced-label elicitation** (scope limit below); surfaced,
   not auto-promoted.
4. **TEXT-POSITION ARTIFACT** if Δ_pos's CI excludes 0.5 (last-line- or first-line-
   following) **and** Δ_chron's CI includes 0.5, with ≥24 gated in-pair parsed trials in
   every cell. → a methodological finding about prompt geometry / stamp neglect; **says
   nothing relational** (the honest terminal home for the reading the v3 verifier refused to
   assert because v3's collinear arm could not earn it).
5. **COMMUTATIVE-NULL-CERTIFIED** if Δ_chron's and Δ_pos's CIs both include 0.5
   (non-degenerate) with ≥36 gated in-pair parsed trials in every cell. → extends the v1/v3
   null to "position *and* stamped chronology of a reassignment do not move the pick"; the
   conjecture stays `proposed`, **strengthened, not proven**; "certified" = the
   pre-registered null clause fired, never a precise zero. Under forced-label elicitation.
6. **INCONCLUSIVE — null pattern, certification floor unmet** if both CIs include 0.5
   (non-degenerate) but the ≥36 floor is unmet in some cell — no clause fires.
7. **Else: INCONCLUSIVE / MIXED** — both CIs exclude 0.5 (the channels confounded in the
   picks); a both-channels pattern below the ≥24 floor; or a degenerate/mixed pattern.
   Reported with point estimates, no substantive label.

**Multiplicity (acknowledged):** two models at 95% CIs. The early/late and variant cuts are
correlated cross-checks of the same records, not independent replications.

**Power caveat (pre-registered, honest):** still pilot-scale. Only a consistent Δ ≳ 0.2
(ρ ≳ 0.7) is reliably CI-clean at this cluster count; a CI-including-0.5 remains
inconclusive-leaning-null, not a precise zero. A symmetric U-shaped serial-position profile
would dilute Δ_pos toward 0.5; the explicit stamps are intended to make Δ_chron less
serial-position-susceptible than v3's position-only cue, but that is a design expectation,
not a guarantee. Because CLAST and physical-last twin are orthogonal, a pure chronology
reader gives Δ_pos ≈ 0.5 and a pure position reader gives Δ_chron ≈ 0.5 (verified on
idealized-reader fixtures); the joint reading is what separates them.

## Anchor discipline (frozen)

`anchor: internal-contrast-only` — the Δ_chron/Δ_pos measure is the probe's own within-model
contrast over byte-identical-content records differing only in stamp and line order; **no
human-comparison claim**, per the ratified relational-line posture
(`decisions/resolved/relational-pilot-operationalization`,
`decisions/resolved/relational-fetchable-anchor`; terminal-state mechanics per
`decisions/resolved/conflicting-cue-human-anchor`). No in-repo human resource anchors
order-sensitivity (Brennan & Clark anchors historicity/partner-specificity only and reports
an order-*insensitive* statistic; Hawkins anchors the convergence baseline only).

## Cost pre-flight (billed `usage.cost`, not rate-card)

Stimulus construction already billed (recorded in `raw/cost-ledger.json`): harvest $0.0417,
top-up $0.0198, certification (both passes) $0.2169 → **≈$0.278 so far**. Probe pre-flight:
460 finding-bearing calls at v3's measured ~$0.0010/call (probe-shaped single-token) ≈
$0.46 + liveness/preflight ≈$0.03 → **≈$0.5 probe**, **≈$0.78 total session**, under the
**$1.50** pre-registered hard stop (per-phase ledger + per-record + per-model checkpoint in
`probe.py full`) and well under the **$5.00/day** cap. Actual billed recorded per phase in
`config/budget.md`.

## Scope limits (carried from v2/v3, plus the v4 stamp shift)

- Records are constructed, not live; a contradictory description-set composed from certified
  descriptions, all lines marked "FOUND" (logically impossible across twins — the conflict
  IS the manipulation).
- **Harvested-and-certified, not live-game by-products** (must be repeated in the result
  page); certification **selects for individually decodable lines** — the result says
  nothing about conventions whose lines are only interpretable in context.
- **Chronology is an explicit stamp** (the v4 indicator shift, flagged above): any verdict
  is conditional on the stamp being read at all (the stamp-respect control licenses the
  Δ_chron reading but is necessary-not-sufficient).
- Any FALSIFIED / CERTIFIED verdict holds **under forced-label elicitation**; it does not
  automatically transfer to free-form settings.
- Homogeneous per-model probes; text grids (the ratified v1 yardstick, v1-scoped); gpt
  dropped; n is pilot scale.
