# PREREG — relational-history-perturbation-v3 — **DRAFT, NOT FROZEN**

> **THIS IS A DRAFT.** It becomes binding only when the orchestrator, AFTER the
> independent pre-run critic pass, applies the critic's fixes, fills every
> `<<PLACEHOLDER>>`, and saves the result as `PREREG.md` (that filename, in this
> directory) **before any finding-bearing call**. `probe.py` refuses to run while only
> this draft exists, and refuses `preflight`/`full` until the frozen `stimuli.json`
> sha256 below is filled in and matches. Critic revisions must be logged in the frozen
> PREREG, as in v2.

Design (authoritative): `experiments/designs/relational-history-perturbation-v3.md`.
The decisive test named by `conjecture/commutative-convention` and recommended as the
perturbation arm by the ratified `decisions/resolved/relational-pilot-operationalization`;
v3 = the v2 instrument with the post-run verifier's five-item fix-list repaired, not a
new instrument. v2 outcome it supersedes: INCONCLUSIVE/MIXED for all three models
(`result/relational-history-perturbation-v2`).

## Pre-run critic revisions (to be logged here before freeze)

<<PLACEHOLDER: list every critic revision applied, as in the v2 PREREG. The design
explicitly asks the critic to rule on five open issues: (1) harvested-and-certified vs
live-game description provenance — inside-class hygiene or a decision-page matter;
(2) batch harvest (8 per numbered-list call, t=0) vs one-per-call at t=0.8;
(3) guard calibration (k = 3; the asymmetric >=36-trial floor on null-certification);
(4) forced format as treatment (suppressed deliberation changing pick behavior);
(5) same-model certification — log a cross-model cross-check descriptively?>>

## Stimuli freeze

`stimuli.json`, generated deterministically by `build_trials.py` (SEED=20260613) from
`certification_report.json` (fresh harvest + per-description certification; the full
certification census is embedded in `stimuli.json`). v1 figures unchanged, original
content sha256 `a2709582a58e54378190b3e6e15191be4fe1f05d27c37830856f958371deb6c4`
(hash-checked in code).

**sha256 of `stimuli.json` = `<<PLACEHOLDER: hash printed by build_trials.py>>`.**
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
- CONSISTENT controls: 2 per cluster (all four lines describing one twin, same nonce,
  fwd), one per twin — the per-cluster manipulation gate, retained on top of
  per-description certification as defense in depth.
- One frozen matcher figure-array permutation per cluster, constant across that
  cluster's 12 mixed cells + 2 controls (v1 discipline; frozen into `stimuli.json`).
- Nominal geometry: 9 clusters/model/direction → 108 mixed + 18 controls = 126
  trials/model, 378 finding-bearing calls total.
  <<PLACEHOLDER: if any model fell short after the one pre-registered top-up harvest
  (t=0.8, logged), record the reduced sample/cluster count here BEFORE the freeze.>>
- Stimulus-quality bias, disclosed: certification selects for individually
  discriminative lines, which sharpens the X-vs-Y conflict — it biases **against** the
  ~0.5-noise-toward-the-null failure mode (v2 critic B2), not toward the conjecture's
  bet.

## Elicitation (fix 1 — truncation-proof; frozen)

- Forced format: system + user prompts demand the reply be **exactly one figure label**
  (`P1`…`P6`) and nothing else — no explanation, no restatement.
- Completion cap 512 (v2: 128), so even a non-compliant deliberating reply completes;
  gemini keeps `reasoning: {"effort": "minimal"}` (config/models.md caveat 1).
- Strict parse rule: (a) reply that is exactly one label after whitespace/punctuation
  stripping → pick, flagged `strict`; (b) else, if the final non-empty line contains
  exactly one label token → pick, flagged `non-strict`; (c) else parse-fail → **one
  retry** with a sterner one-label-only reminder; persistent failure → NA, reported
  separately. Out-of-pair computed over parsed picks only (v2 S3 retained).
- Compliance reporting: per-model strict-compliance rate; per-cell NA counts, with a
  flag if NAs concentrate (> 25% in any pair × direction cell — the v2 pathology);
  strict-only is a pre-registered sensitivity cut.
- Liveness gate: all three models must return a parseable label under the forced format
  before preflight/full proceed. Liveness and preflight raw are never analyzed; the
  `full` run is the only finding-bearing dataset (v2 rule S2, extended: harvest and
  certification raw are stimulus-construction data, kept but never analyzed as
  findings).

## Measures (frozen)

- **Manipulation gate (per cluster):** both consistent controls correct → cluster enters
  the gated primary. Gated-cluster list, per-model control accuracy, and ungated ρ all
  reported.
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
- **Pre-registered sensitivity cuts:** leave-one-pair-out (each of the 3 pairs); NAs
  scored as out-of-pair; strict-format-only subset; pair-level (3-cluster) bootstrap as
  a descriptive cross-check on the cluster-independence caveat (clusters within a pair
  share figures).

## Decision rule (frozen; the verdict mapper is CODE in analyze.py, mirrored verbatim from the design)

**The ≥k guard, k = 3:** every clause below additionally requires **≥3 gated clusters in
each presentation direction** and non-degenerate CIs for the quantities it cites. Below
that floor the run is METHODOLOGICAL NULL for that model, whatever the point estimates
say. The guard is symmetric — it blocks a one-cluster zero-width CI from firing
falsification (the v2 latent defect) *and* from certifying the null (no dodging in
either direction).

Per model, pre-registered verdict categories:

- **FALSIFIED (non-commutative, chronology-tracking)** iff ≥3 gated clusters per
  direction AND out-of-pair ≤ 0.5 AND ρ_chron's CI excludes 0.5 **on the same side in
  BOTH presentation directions** (two-sided: recency or primacy, direction reported). →
  the conjecture's invariance bet falsified for that model; the positive surfaced, not
  auto-promoted, under the usual contingency discipline.
- **PHYSICAL-POSITION ARTIFACT** iff the guard holds and ρ_phys's CI excludes 0.5 on the
  same side in both directions while the ρ_chron clause is unmet. → methodological
  finding about prompt-position bias; says nothing relational.
- **COMMUTATIVE-NULL-CERTIFIED** iff ≥3 gated clusters per direction, out-of-pair ≤ 0.5,
  all four CIs (ρ_chron, ρ_phys × both directions) include 0.5, **AND ≥36 gated in-pair
  parsed trials per direction** (an absence claim needs a sample-size floor, not just CI
  coverage — pre-registered so "certified" cannot be earned on scraps). → extends the v1
  null to "position of conflicting convention evidence"; the conjecture stays
  `proposed`, strengthened, not proven; "certified" means the pre-registered null clause
  fired, never a precise zero.
- **INCONCLUSIVE / MIXED** iff the guard holds but the arms disagree (one CI-clean, the
  other not, or opposite sides without the artifact pattern) — the v2 outcome, reported
  with point estimates and no substantive label. (Also the residual category when the
  null pattern holds but the 36-trial floor is unmet: no clause fires.)
- **METHODOLOGICAL NULL** iff < 3 gated clusters in either direction. **UNDER-POWERED**
  iff out-of-pair > 0.5.
- **Multiplicity (acknowledged, inherited):** "≥1 model fires" over 3 models at 95% CIs
  carries ≈14% family-wise false-positive risk under the global null; the
  both-directions requirement tightens it.

**Power caveat (pre-registered):** with 9 clusters, only a consistent ρ_chron ≳ 0.7 is
reliably CI-clean; CI-includes-0.5 remains *inconclusive-leaning-null*, not a precise
zero; orderings and effect-direction, not effect sizes. Still pilot-scale.

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
probe-shaped). v3 is ≈3× v2's call count:

| phase | calls | est. billed |
|---|---|---|
| harvest (18 + ≤18 top-ups; director-shaped) | ≤36 | ≈$0.05 |
| certification (≤48 distinct candidates × 3 models; 1-line probe-shaped) | ≤144 | ≈$0.17 |
| probe `full` (3 × [108 mixed + 18 controls]) | 378 (+retries) | ≈$0.55 |
| liveness + preflight (never analyzed) | ≈21 | ≈$0.02 |
| **total** | ≈575–650 | **≈$0.80; expectation: < $1.00** |

Worst-case sensitivity, disclosed: the 512-token cap means a persistently non-compliant
claude could push the probe phase toward ≈$1.30 total; the forced format exists to
prevent this, the liveness format-gate checks compliance before any finding-bearing
call, and **phase checkpoints** apply — billed cost recorded in `raw/cost-ledger.json`
after harvest, certification, liveness and preflight, with a pre-registered **hard stop
at $1.50 projected total** (enforced in code, including mid-`full`: re-design, don't
push through). Actual billed `usage.cost` recorded per phase in `config/budget.md`.

## Scope limits stated up front (inherited from v2, plus the v3 provenance shift)

- Records are constructed, not live: a contradictory description-set composed from
  certified descriptions and asserted about "ONE target" (all lines marked "FOUND",
  logically impossible across twins — the conflict IS the manipulation). v3 descriptions
  are harvested-and-certified rather than live-game by-products (the design's gate check
  argues this is inside-class hygiene; the pre-run critic is explicitly asked to contest
  it — open issue 1).
- Uniform positive feedback removes outcome information by design; a mixed-feedback arm
  is deferred.
- Homogeneous per-model probes; text grids (the ratified v1 yardstick, v1-scoped); n is
  pilot scale.
