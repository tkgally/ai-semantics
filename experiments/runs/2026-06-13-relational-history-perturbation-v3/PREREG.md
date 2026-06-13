# PREREG — relational-history-perturbation-v3 — **FROZEN 2026-06-13**

> **FROZEN by the orchestrator 2026-06-13**, after the independent pre-run critic's
> GO-after-fixes verdict and the application of every blocker and should-fix (logged
> below), with every placeholder filled — **before any finding-bearing call** (harvest
> and certification calls are stimulus-construction, not finding-bearing; the frozen
> `stimuli.json` sha256 below was produced by `build_trials.py` from the certification
> roster and no probe/preflight call existed at freeze time). The draft this was frozen
> from is kept verbatim as `PREREG-draft.md`.

Design (authoritative): `experiments/designs/relational-history-perturbation-v3.md`.
The decisive test named by `conjecture/commutative-convention` and recommended as the
perturbation arm by the ratified `decisions/resolved/relational-pilot-operationalization`;
v3 = the v2 instrument with the post-run verifier's five-item fix-list repaired, not a
new instrument. v2 outcome it supersedes: INCONCLUSIVE/MIXED for all three models
(`result/relational-history-perturbation-v2`).

## Pre-run critic revisions (fix log)

**2026-06-13 — independent pre-run critic: GO after fixes.** Rulings on the design's
five open issues: (1) harvested-and-certified description provenance ruled
**inside-class hygiene — no decision page opened** (the records were already constructed
artifacts; the shift is in degree, not kind; conditions recorded under Scope limits
below); (2) batch harvest retained; (3) guard k = 3 retained, with trial floors extended
to the effect clauses (blocker 3); (4) forced format retained, with the elicitation
scope limit recorded below; (5) same-model certification retained — the cross-model
cross-check is **deferred** (never gating; a future session; pre-registered descriptive
only).

Fixes applied 2026-06-13, before freeze:

- **Blocker 1** — decision rule re-specified as an ordered, exhaustive if/else tree with
  an explicit final else → INCONCLUSIVE-MIXED; named gap sub-label "INCONCLUSIVE — null
  pattern, certification floor unmet"; precedence stated (METHODOLOGICAL NULL >
  UNDER-POWERED > the CI clauses), in both this PREREG and `analyze.py verdict()`.
- **Blocker 2** — a reply with `finish_reason == "length"` is **never parsed** for a
  pick (parse-fail → stern retry → NA), in probe and certification alike; the "no
  truncation possible" claim softened everywhere (cap 512 makes truncation rare, not
  impossible); `finish_reason` recorded per call.
- **Blocker 3** — ≥24 gated in-pair parsed trials per direction added to the FALSIFIED
  and PHYSICAL-POSITION-ARTIFACT clauses (≥36 stays on null-certification); written
  reconciliation with v2 PREREG S4 added under §Decision rule.
- **S1** — consistent controls now run in BOTH presentation directions (4
  controls/cluster, 36/model; 432 finding-bearing calls); ARTIFACT verdict wording
  pre-registered as "position-following or direction-instruction neglect —
  observationally equivalent here".
- **S2** — per-model checkpoint inside `probe.py full` (projected-total abort against
  $1.50 from realized per-call billed costs); preflight composition now gpt + claude
  controls, not gpt-only.
- **S3** — certification cost bound corrected for top-ups (honest worst case stated in
  the cost table: each top-up call can add up to 8 more candidates).
- **S4** — ≤12-word budget enforced mechanically at harvest time, before certification;
  the deterministic partition of the 6 certified descriptions into 3 sample-pairs
  pre-registered (§Stimuli freeze).
- **S5** — no pooling / no numeric comparison with v2 (verdict-level supersession only);
  sensitivity cuts pre-registered as descriptive, never verdict-bearing.
- **S6** — power-section honesty notes added: the both-directions requirement is two
  *correlated* tests, not independent; a symmetric U-shaped serial-position profile
  dilutes ρ_chron toward 0.5 in both directions (biases toward the conjecture's own
  bet).
- **Issue-1 / Issue-4 conditions** — recorded under §Scope limits.

## Stimuli freeze

`stimuli.json`, generated deterministically by `build_trials.py` (SEED=20260613) from
`certification_report.json` (fresh harvest + per-description certification; the full
certification census is embedded in `stimuli.json`). v1 figures unchanged, original
content sha256 `a2709582a58e54378190b3e6e15191be4fe1f05d27c37830856f958371deb6c4`
(hash-checked in code).

**sha256 of `stimuli.json` = `d0ae70afe90d3907702230afcc8a1dc1b5d1f11a0f1e8108f93b67af18a94439`.**
No finding-bearing model call before this hash is committed.

- Per model, per near-twin pair (X, Y), per description sample s in {0, 1, 2}: MIXED
  records = 2 distinct **certified** descriptions of X + 2 of Y (that model's OWN freshly
  harvested descriptions), uniform positive feedback ("you FOUND it"), under all 6
  distinct orders of {X,X,Y,Y} (`XXYY, XYXY, YXXY, YYXX, YXYX, XYYX`) × 2 presentation
  directions (fwd/rev). Content multiset byte-identical across the 12 cells of a
  (pair × sample) cluster; only chronological position and physical layout vary,
  independently. No round-number labels (the v2 pre-registered change, retained).
- Coined term = a fresh frozen non-descriptive nonce per pair: `PLOVNEK`, `SKARMIL`,
  `VANTREX` (no v2 carryover even in principle).
- CONSISTENT controls: **4 per cluster** (all four lines describing one twin, same
  nonce) — one per twin × **both presentation directions** (critic S1: the rev-framed
  control checks direction-instruction following where it matters for the artifact
  diagnosis). The per-cluster manipulation gate = **all four** controls correct;
  retained on top of per-description certification as defense in depth.
- One frozen matcher figure-array permutation per cluster, constant across that
  cluster's 12 mixed cells + 4 controls (v1 discipline; frozen into `stimuli.json`).
- **Deterministic sample partition (pre-registered, critic S4):** each figure's frozen
  roster is its first 6 certified descriptions in deterministic harvest order; sample
  s ∈ {0, 1, 2} takes roster positions 2s and 2s+1 (`roster[2s:2s+2]`). No discretion
  at build time. The ≤12-word budget is enforced **mechanically at harvest time**,
  before certification — over-budget lines never reach a certification call.
- Nominal geometry: 9 clusters/model/direction → 108 mixed + 36 controls = 144
  trials/model, **432 finding-bearing calls total**.
  **Recorded shortfall (before freeze):** after the one pre-registered top-up,
  **claude 9/9 and gemini 9/9 clusters; gpt 6/9** (F2 certified 3/6 -> 1 sample;
  F4 certified 5/6 -> 2 samples; pair-2 = min(1,3) = 1 cluster/sample-triple short,
  pair-3 = min(2,3) = 2) -> gpt = 72 mixed + 24 controls = 96 trials; realized total
  **384 finding-bearing calls** (claude 144, gpt 96, gemini 144). The gpt reduction is
  a certification outcome, recorded here per the pre-registered shortfall rule; the
  >=3-gated-cluster guard and the 24/36-trial floors operate on realized counts.
- Stimulus-quality bias, disclosed: certification selects for individually
  discriminative lines, which sharpens the X-vs-Y conflict — it biases **against** the
  ~0.5-noise-toward-the-null failure mode (v2 critic B2), not toward the conjecture's
  bet.

## Elicitation (fix 1 — truncation-resistant; frozen)

- Forced format: system + user prompts demand the reply be **exactly one figure label**
  (`P1`…`P6`) and nothing else — no explanation, no restatement.
- Completion cap 512 (v2: 128) makes truncation **rare, not impossible** (critic
  blocker 2 softening); gemini keeps `reasoning: {"effort": "minimal"}`
  (config/models.md caveat 1).
- **Never parse a truncated reply (critic blocker 2, pre-registered):** a reply with
  `finish_reason == "length"` is **never parsed for a pick** — its visible text is a cut
  prefix and any label in it is untrustworthy. It counts as a parse-fail → stern retry →
  NA. Applies identically to probe and certification calls; `finish_reason` is recorded
  on every record.
- Strict parse rule (applied only to non-truncated replies): (a) reply that is exactly
  one label after whitespace/punctuation stripping → pick, flagged `strict`; (b) else,
  if the final non-empty line contains exactly one label token → pick, flagged
  `non-strict`; (c) else parse-fail → **one retry** with a sterner one-label-only
  reminder; persistent failure → NA, reported separately. Out-of-pair computed over
  parsed picks only (v2 S3 retained).
- Compliance reporting: per-model strict-compliance rate; per-cell NA counts, with a
  flag if NAs concentrate (> 25% in any pair × direction cell — the v2 pathology);
  strict-only is a pre-registered sensitivity cut.
- Liveness gate: all three models must return a parseable label under the forced format
  before preflight/full proceed. Liveness and preflight raw are never analyzed; the
  `full` run is the only finding-bearing dataset (v2 rule S2, extended: harvest and
  certification raw are stimulus-construction data, kept but never analyzed as
  findings).

## Measures (frozen)

- **Manipulation gate (per cluster):** **all four** consistent controls correct (2
  twins × 2 directions, critic S1) → cluster enters the gated primary. Gated-cluster
  list, per-model control accuracy, and ungated ρ all reported.
- **PRIMARY — gated ρ_chron per presentation direction:** among gated mixed trials with
  parsed in-pair picks, the fraction choosing the chronologically-last-line twin.
  Commutative ⇒ ρ_chron ≈ 0.5 both directions (per-twin salience cancels across the
  symmetric order set; the cancellation algebra is unchanged from v2 and was
  critic-verified there).
- **Artifact diagnostic — ρ_phys:** same, for the physically-last-line twin (= ρ_chron
  in fwd; = the chron-first twin in rev).
- **CIs:** clustered bootstrap, 10,000 resamples over the 9 (pair × sample) clusters per
  model. **Degenerate (zero-width) CIs carry no inferential weight and satisfy no
  clause** (a rule, not a post-hoc gloss).
- **NA / out-of-pair:** NAs reported separately after the single retry; out-of-pair over
  parsed picks; out-of-pair > 0.5 → UNDER-POWERED flag.
- **Secondary (descriptive only):** clean-switch orders (`XXYY`/`YYXX`) vs interleaved.
- **Pre-registered sensitivity cuts — descriptive only, NEVER verdict-bearing (critic
  S5):** the verdict is computed on the primary gated pool only; cuts are robustness
  readouts. Cuts: leave-one-pair-out (each of the 3 pairs); NAs scored as out-of-pair;
  strict-format-only subset; pair-level (3-cluster) bootstrap as a descriptive
  cross-check on the cluster-independence caveat (clusters within a pair share figures).
- **No pooling with v2 (critic S5):** no pooling and no numeric comparison with the v2
  run's data anywhere in the analysis or the result page — v3 supersedes v2 at the
  **verdict level only**.

## Decision rule (frozen; the verdict mapper is CODE in analyze.py, mirrored verbatim from the design)

**The ≥k guard, k = 3:** every CI-bearing clause requires **≥3 gated clusters in each
presentation direction** and non-degenerate CIs for the quantities it cites. The guard
is symmetric — it blocks a one-cluster zero-width CI from firing falsification (the v2
latent defect) *and* from certifying the null (no dodging in either direction).

**Trial floors (critic blocker 3):** the effect clauses (FALSIFIED,
PHYSICAL-POSITION ARTIFACT) require **≥24 gated in-pair parsed trials per direction**;
null-certification keeps the stricter **≥36** floor (the absence claim carries the
heavier burden).

**The verdict is an ordered, exhaustive if/else tree (critic blocker 1), evaluated
top-down per model; the first clause that fires is the verdict. Pre-registered
precedence: METHODOLOGICAL NULL > UNDER-POWERED > the CI clauses (in the order below) >
the final else.** Degenerate (zero-width) CIs satisfy no clause; every CI clause
requires agreement in BOTH presentation directions.

1. **METHODOLOGICAL NULL** if < 3 gated clusters in either direction — whatever the
   point estimates say.
2. **UNDER-POWERED** if out-of-pair > 0.5 on parsed picks.
3. **FALSIFIED (non-commutative, chronology-tracking)** if ρ_chron's CI excludes 0.5
   **on the same side in BOTH presentation directions** (two-sided: recency or primacy,
   direction reported) AND ≥24 gated in-pair parsed trials per direction. → the
   conjecture's invariance bet falsified for that model; the positive surfaced, not
   auto-promoted, under the usual contingency discipline. Holds **under forced-label
   elicitation** (scope limit below).
4. **PHYSICAL-POSITION ARTIFACT** if ρ_phys's CI excludes 0.5 on the same side in both
   directions (the ρ_chron clause having not fired) AND ≥24 gated in-pair parsed trials
   per direction. → **"position-following or direction-instruction neglect —
   observationally equivalent here"** (pre-registered wording, critic S1): a
   methodological finding about prompt-position behavior; says nothing relational.
5. **COMMUTATIVE-NULL-CERTIFIED** if all four CIs (ρ_chron, ρ_phys × both directions)
   include 0.5 (non-degenerate) AND ≥36 gated in-pair parsed trials per direction. →
   extends the v1 null to "position of conflicting convention evidence"; the conjecture
   stays `proposed`, strengthened, not proven; "certified" means the pre-registered null
   clause fired, never a precise zero. Holds under forced-label elicitation.
6. **INCONCLUSIVE — null pattern, certification floor unmet** (named gap sub-label,
   critic blocker 1) if the guard holds, out-of-pair ≤ 0.5, all four CIs include 0.5
   (non-degenerate), but the ≥36-trial floor is unmet — no clause fires; the absence
   claim may not be certified on that n.
7. **Else: INCONCLUSIVE / MIXED** — exhaustively everything not caught above: arms
   disagree (one CI-clean, the other not; opposite sides without the artifact pattern;
   a degenerate CI), or a both-directions CI pattern present but below the ≥24 effect
   floor. Reported with point estimates and no substantive label (the v2 outcome).

The verdict mapper is CODE (`analyze.py verdict()`), the same ordered tree, mirrored
clause for clause.

**Reconciliation with v2 PREREG S4 (critic blocker 3):** v2's S4 floor concerned a
**3-cluster nominal total** in a regime where identical-rate clusters made bootstrap CIs
degenerate — its job was to stop a single degenerate cluster from deciding anything. v3
addresses that regime three ways v2 could not: degenerate-CI exclusion (no zero-width CI
satisfies any clause), the both-directions agreement requirement, and these explicit
per-direction trial floors (≥24 effect / ≥36 null). The v3 floors are therefore a
sharpening of v2 S4's intent, not a relaxation of it.

- **Multiplicity (acknowledged, inherited):** "≥1 model fires" over 3 models at 95% CIs
  carries ≈14% family-wise false-positive risk under the global null. The
  both-directions requirement tightens it, **but less than two independent tests
  would** (critic S6): the fwd and rev arms share clusters and stimuli, so they are two
  *correlated* tests of the same records, not independent replications.

**Power caveat (pre-registered):** with 9 clusters, only a consistent ρ_chron ≳ 0.7 is
reliably CI-clean; CI-includes-0.5 remains *inconclusive-leaning-null*, not a precise
zero; orderings and effect-direction, not effect sizes. Still pilot-scale. Two honesty
notes (critic S6), disclosed next to that caveat:

- **(a) Correlated, not independent, directions:** the fwd/rev arms share clusters and
  stimuli, so the both-directions agreement requirement is two correlated tests; any
  claimed tightening (the ≈14% figure above) must be read with that correlation in
  mind, not as the product of independent error rates.
- **(b) U-shaped serial-position profiles dilute toward the null:** a symmetric
  primacy+recency (U-shaped) profile moves ρ_chron toward 0.5 in **both** directions —
  i.e. it biases the instrument **toward the conjecture's own bet**. A
  CI-includes-0.5 outcome is therefore consistent with either genuine order-invariance
  or a symmetric U-shaped order effect; the clean-switch vs interleaved secondary is
  the (descriptive) probe of that profile.

## Anchor discipline (frozen)

`anchor: internal-contrast-only` — the recency/commutativity measure is the probe's own
within-model contrast; **no human-comparison claim**, per the ratified relational-line
posture (`decisions/resolved/relational-pilot-operationalization`,
`decisions/resolved/relational-fetchable-anchor`; terminal-state mechanics per
`decisions/resolved/conflicting-cue-human-anchor`). Hawkins anchors nothing here. The
conjecture's human-contrast clause stays a characterized prediction: Brennan & Clark
1996 anchors historicity/partner-specificity only, not human order-sensitivity.

## Cost pre-flight (billed `usage.cost`, not rate-card)

Yardstick: v2's finding-bearing run billed $0.277 for 210 calls (≈$0.0013/call,
probe-shaped). v3 is ≈3.3× v2's call count (critic S1 added 54 control calls):

| phase | calls | est. billed |
|---|---|---|
| harvest (18 + ≤18 top-ups; director-shaped) | ≤36 | ≈$0.05 |
| certification (≤48 distinct candidates × 3 models; 1-line probe-shaped) | ≤144 first pass | ≈$0.17 |
| certification of top-up candidates (honest worst case, critic S3: each top-up call can add up to 8 more candidates → up to +144) | ≤+144 | worst ≈+$0.17; expected ≈$0 |
| probe `full` (3 × [108 mixed + 36 controls]) | 432 (+retries) | ≈$0.62 |
| liveness + preflight (3 + 9 gpt + 9 claude controls; never analyzed) | 21 | ≈$0.03 |
| **total** | ≈630 expected; ≤790 worst case (+retries) | **≈$0.87; expectation: < $1.00** |

Worst-case sensitivity, disclosed: the 512-token cap means a persistently non-compliant
claude could push the probe phase toward ≈$1.35 total; the forced format exists to
prevent this, the liveness format-gate checks compliance before any finding-bearing
call, and **phase checkpoints** apply — billed cost recorded in `raw/cost-ledger.json`
after harvest, certification, liveness and preflight, **plus a per-model checkpoint
inside `full` (critic S2)**: before each model's batch, the projected total (spend so
far + remaining trials priced at *realized* per-call billed costs, per-model preflight
figures until realized ones exist) is re-checked against the pre-registered **hard stop
at $1.50** (enforced in code, including per-record mid-`full`: re-design, don't push
through). Preflight includes claude controls precisely so the projection sees the
priciest model. Actual billed `usage.cost` recorded per phase in `config/budget.md`.

## Scope limits stated up front (inherited from v2, plus the v3 provenance shift)

- Records are constructed, not live: a contradictory description-set composed from
  certified descriptions and asserted about "ONE target" (all lines marked "FOUND",
  logically impossible across twins — the conflict IS the manipulation).
- **Provenance (critic issue-1 ruling: inside-class, no decision page — with two
  recorded conditions):**
  - (a) v3 stimuli are **harvested-and-certified, not live-game by-products**; this
    scope limit **must be repeated in the eventual result page's scope limits**, not
    just here.
  - (b) certification **selects for individually decodable lines** — every verdict is
    conditional on evidence lines that work singly; the result says **nothing about
    conventions whose lines are only interpretable in context** (anaphoric, elliptical,
    or pact-internal descriptions that fail solo certification are out of scope by
    construction).
- **Elicitation scope (critic issue-4):** any FALSIFIED or CERTIFIED verdict holds
  **under forced-label elicitation**; suppressing visible deliberation could itself
  change the pick mechanism, so the verdicts do not automatically transfer to
  free-form-response settings.
- Uniform positive feedback removes outcome information by design; a mixed-feedback arm
  is deferred. The cross-model certification cross-check is likewise deferred (critic
  issue-5: never gating; a future session; pre-registered descriptive only).
- Homogeneous per-model probes; text grids (the ratified v1 yardstick, v1-scoped); n is
  pilot scale.
