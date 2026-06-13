---
type: design
id: relational-history-perturbation-v3
title: Relational v3 — the history-perturbation arm, second attempt (verifier fix-list incorporated; the decisive commutativity test, properly powered and truncation-resistant)
meaning-senses:
  - relational
  - distributional
status: draft
contingent-on: []
created: 2026-06-13
updated: 2026-06-13
links:
  - rel: operationalizes
    target: conjecture/commutative-convention
  - rel: supersedes
    target: design/relational-history-perturbation-v2
  - rel: depends-on
    target: result/relational-history-perturbation-v2
  - rel: depends-on
    target: result/relational-reference-game-v1
  - rel: depends-on
    target: concept/relational-meaning
---

# Design: relational history-perturbation probe (v3)

> **Status: pre-run critic passed 2026-06-13 — GO after fixes, all applied.** The critic
> ruled the provenance shift (open issue 1) **inside-class — no decision page**; blockers
> 1–3 and should-fixes S1–S6 are incorporated below and in the run dir
> (`experiments/runs/2026-06-13-relational-history-perturbation-v3/`), logged in that
> run's `PREREG-draft.md`. The run's `PREREG.md` is frozen by the orchestrator (with the
> `stimuli.json` sha256) before any finding-bearing call. This design supersedes
> [`design/relational-history-perturbation-v2`](relational-history-perturbation-v2.md) and
> exists for one reason: the v2 run
> ([`result/relational-history-perturbation-v2`](../../wiki/findings/results/relational-history-perturbation-v2.md))
> came back **INCONCLUSIVE/MIXED for all three models** — the falsification clause did not
> fire and the commutative null was not certified — and its post-run verifier left a concrete
> five-item fix-list. v3 is the same instrument with those five defects repaired, not a new
> instrument.

## Construct (unchanged from v2)

The decisive test named by
[`conjecture/commutative-convention`](../../wiki/findings/conjectures/commutative-convention.md)
(§"What would confirm / falsify") and recommended as the perturbation arm by the ratified
[`decisions/resolved/relational-pilot-operationalization`](../../wiki/decisions/resolved/relational-pilot-operationalization.md):
present a fresh matcher with a **constructed contradictory convention record** — evidence
supporting twin X early and twin Y late, content multiset held byte-identical — and test
whether interpretation of a nonce coined term tracks **where in the chronology** the
conflicting evidence lands. A path-dependent (constituted) convention reader resolves the
conflict by recency in **both** presentation directions; an attention artifact follows the
*physically*-last line in both; a commutative (aggregated, set-based) reader is
order-invariant (ρ_chron ≈ 0.5). The logic section of the
[v2 design](relational-history-perturbation-v2.md) carries over verbatim; v1 grounding is
[`result/relational-reference-game-v1`](../../wiki/findings/results/relational-reference-game-v1.md).

## The verifier's fix-list → what v3 changes

| # | v2 defect (verifier) | v3 fix |
|---|---------------------|--------|
| 1 | Claude truncation non-random and cell-correlated: 11/72 mixed trials NA at the 128-token cap, all pair-2, 8 forward-arm; 10 truncated-but-parsed picks possibly deliberation-mentions. | **Truncation-resistant elicitation**: strict forced-format single-token answer ("reply with exactly one label, nothing else"), completion cap raised to 512 so truncation is rare (not impossible — a `finish_reason: length` reply is never parsed, per critic blocker 2), strict parse rule with a compliance flag, strict-only sensitivity cut (§Elicitation). |
| 2 | gpt effectively uninformative: its v1-harvested descriptions passed the manipulation gate in only 1/6 clusters (control acc 0.42). | **Regenerated, per-description certified stimuli for all three models** (uniform procedure, not a gpt-only patch): fresh description harvest + an individual certification call per description; only certified descriptions enter records (§Stimuli). |
| 3 | ≤6 clusters/model/direction (gemini 3); single/identical-cluster bootstrap CIs degenerate. | **9 clusters/model/direction** (3 pairs × 3 description samples, gemini included via fresh harvest — its v1 pool was too thin for more than 1 sample); power rationale in §Power. |
| 4 | Latent rule defect: the falsification clause had no minimum-cluster guard — a single gated cluster's zero-width CI could mechanically fire it. | **Pre-registered ≥k-cluster guard, k = 3**, applied symmetrically to every CI-bearing clause (falsification, artifact, *and* null-certification), plus a rule that degenerate (zero-width) CIs can satisfy no clause (§Decision rule). |
| 5 | (House pattern to keep, not a defect:) the presentation-direction arm caught claude's forward-only elevation as a position/chronology confound. | **Both-directions arm retained unchanged**: every mixed cell runs fwd ("earliest first") and rev ("most recent first", lines physically reversed, chronology identical), and every chronology clause requires CI agreement **in both directions** (§Decision rule). |

## Conditions

Per panel model, per near-twin pair (X, Y), per description sample s ∈ {0, 1, 2}:

- **MIXED** (the manipulation): 4-line record — 2 distinct certified descriptions of X + 2 of
  Y, that model's **own** freshly harvested descriptions, uniform positive feedback ("you
  FOUND it"), nonce coined term — under **all 6 distinct orders** of {X,X,Y,Y} (`XXYY, XYXY,
  YXXY, YYXX, YXYX, XYYX`) **× 2 presentation directions** (fwd/rev). Content multiset
  byte-identical across the 12 cells within a cluster; only chronological position and
  physical layout vary, independently.
- **CONSISTENT** (per-cluster manipulation gate): **4 control records per cluster** (all
  four lines describing one twin, same nonce) — one per twin × **both presentation
  directions** (critic S1, 2026-06-13: the rev-framed control checks
  direction-instruction following exactly where the artifact diagnosis needs it) —
  retained on top of per-description certification as defense in depth (certification
  certifies lines singly; the gate certifies the assembled record). The gate requires
  **all four** controls correct.

Cluster = (pair × sample), the bootstrap and gating unit, as in v2. v1 discipline retained:
one frozen matcher figure-array permutation per cluster, constant across that cluster's 12
mixed cells + 4 controls. Totals: 108 mixed + 36 controls = 144 trials/model, **432
finding-bearing calls**.

## Stimuli plan

- **Figures**: the 6 frozen v1 text-grid figures, 3 confusable near-twin pairs, unchanged
  (v1 `figures.json`, original sha256 `a2709582…`). More *pairs* (new figures) was the other
  route to more clusters; v3 deliberately takes the harvest route instead — new pairs would
  add an uncontrolled stimulus dimension (uncertified difficulty profile) in the very run
  whose job is to remove stimulus noise, and they would break comparability with v1/v2.
  Image referents remain the named scope extension, not part of this design.
- **Fresh description harvest (all three models, uniform)**: per (model × figure), one
  harvest call mirroring the v1 director framing — the 6-figure array with the target
  marked, the v1 ≤12-word budget — requesting **8 candidate descriptions** in a numbered
  list, temperature 0. Deduplicate (within figure and against the twin's set).
- **Per-description certification**: each distinct candidate gets **one certification
  call** — a fresh same-model matcher, probe-shaped prompt, the single description line, no
  nonce, no history: which figure is described? Certified iff correct. The ≤12-word budget
  is enforced **mechanically at harvest time**, before certification (critic S4 —
  over-budget lines never reach a certification call). The first **6 certified
  descriptions per figure** (deterministic harvest order) are frozen in; 6 = 3 samples × 2
  descriptions, partitioned deterministically as sample s ← roster positions 2s, 2s+1
  (pre-registered). Shortfall procedure (pre-registered): one top-up harvest call at
  temperature 0.8, logged; if still short, that model's sample count drops and the reduced
  cluster count is recorded in the PREREG **before** the stimuli freeze.
- **Deferred (never gating, critic issue-5 ruling)**: a **cross-model certification
  cross-check** — re-certifying each model's frozen roster with the other two models'
  matchers — is deferred to a future session, pre-registered there as **descriptive
  only**; it can contextualize, never gate or re-open, this run's verdicts.
- **Known bias direction, disclosed**: certification selects for individually discriminative
  lines, which *sharpens* the X-vs-Y conflict — i.e. it biases **against** the
  ~0.5-noise-toward-the-null failure mode the v2 critic identified (B2), not toward the
  conjecture's bet. The v2 run's frozen live-quality census showed exactly why this is
  needed (gpt pair-2 descriptions failed live 4/4).
- **Nonces**: fresh frozen non-descriptive nonce per pair — `PLOVNEK`, `SKARMIL`, `VANTREX`
  (no descriptive content, no shape-suggestive phonesthemes; new strings so no v2 carryover
  even in principle). Round-number labels stay removed (the v2 pre-registered change);
  order is conveyed purely by position + stated direction.
- **Freeze discipline**: `build_stimuli.py` (deterministic seed) → `stimuli.json` with the
  full certification census embedded; sha256 recorded in `PREREG.md`; **no finding-bearing
  probe call before that hash is committed**. Harvest and certification raw are
  stimulus-construction data, kept but never analyzed as findings; the probe `full` run is
  the only finding-bearing dataset (v2 rule S2, extended).

## Elicitation (fix 1 — truncation-resistant)

- **Forced format**: system + user prompts demand the reply be **exactly one figure label**
  (`P1`…`P6`) and nothing else — no explanation, no restatement.
- **Truncation made rare AND made harmless** (critic blocker 2 softened the original
  "no truncation possible" claim): completion cap 512 (vs v2's 128) makes truncation
  rare, not impossible; the pre-registered rule that closes the hole is that a reply
  with `finish_reason: length` is **never parsed for a pick** — it counts as a
  parse-fail → stern retry → NA, in probe and certification alike, with `finish_reason`
  recorded per call. gemini keeps `reasoning: effort minimal` (per
  [`config/models.md`](../../config/models.md) caveat 1).
- **Strict parse rule (pre-registered)**: (a) reply that is exactly one label after
  whitespace/punctuation stripping → pick, flagged `strict`; (b) else, if the final
  non-empty line contains exactly one label token → pick, flagged `non-strict`; (c) else
  parse-fail → **one retry** with a sterner one-label-only reminder; persistent failure →
  NA, reported separately. Out-of-pair computed over parsed picks only (v2 S3 retained).
- **Compliance reporting**: per-model strict-compliance rate reported; per-cell NA counts
  reported, with a pre-registered flag if NAs concentrate (> 25% in any pair × direction
  cell — the v2 pathology); strict-only is a pre-registered sensitivity cut.
- **Liveness gate**: the liveness phase doubles as a format probe — all three models must
  return a parseable label under the forced format before preflight/full proceed.

## Panel

Per [`config/models.md`](../../config/models.md): `anthropic/claude-sonnet-4.6` /
`openai/gpt-5.4-mini` / `google/gemini-3.5-flash` (panel A/B/C; slugs from `lib/openrouter.py`,
never hardcoded). Homogeneous per-model probes, as ratified for this line; cross-family
divergence is itself data.

## Measures and analysis plan

All frozen in `PREREG.md` post-critic; no retuning after seeing data.

- **Manipulation gate (per cluster)**: both consistent controls correct → cluster enters
  the gated primary. Gated-cluster list, per-model control accuracy, and ungated ρ all
  reported.
- **PRIMARY — gated ρ_chron per presentation direction**: among gated mixed trials with
  parsed in-pair picks, the fraction choosing the **chronologically-last-line** twin.
  Commutative ⇒ ρ_chron ≈ 0.5 both directions (per-twin salience cancels across the
  symmetric order set — the v2 critic verified the cancellation algebra, which is unchanged).
- **Artifact diagnostic — ρ_phys**: same, for the physically-last-line twin (= ρ_chron in
  fwd; = chron-first twin in rev).
- **CIs**: clustered bootstrap, 10,000 resamples over the 9 (pair × sample) clusters per
  model. **Degenerate (zero-width) CIs carry no inferential weight and satisfy no clause**
  (now a rule, not a post-hoc gloss).
- **NA / out-of-pair**: NAs reported separately after the single retry; out-of-pair over
  parsed picks; out-of-pair > 0.5 → UNDER-POWERED flag.
- **Secondary (descriptive only)**: clean-switch orders (`XXYY`/`YYXX`) vs interleaved.
- **Pre-registered sensitivity cuts**: leave-one-pair-out (each of the 3 pairs); NAs scored
  as out-of-pair; strict-format-only subset; pair-level (3-cluster) bootstrap as a
  descriptive cross-check on the cluster-independence caveat (clusters within a pair share
  figures).

## Decision rule (fixes 4 and 5 baked in; critic blockers 1 and 3 applied 2026-06-13)

**The ≥k guard, k = 3**: every CI-bearing clause requires **≥3 gated clusters in each
presentation direction** and non-degenerate CIs for the quantities it cites. The guard is
symmetric — it blocks a one-cluster zero-width CI from firing falsification (the v2
latent defect) *and* from certifying the null (no dodging in either direction).

**Trial floors (critic blocker 3)**: the effect clauses (FALSIFIED, ARTIFACT) require
**≥24 gated in-pair parsed trials per direction**; null-certification keeps the stricter
**≥36** floor. (Reconciliation with v2 PREREG S4: that floor concerned a 3-cluster
nominal total in a degenerate identical-rate-cluster regime; v3 adds degenerate-CI
exclusion + both-direction agreement + these explicit floors — a sharpening of S4's
intent, recorded in full in the run PREREG.)

**The verdict is an ordered, exhaustive if/else tree (critic blocker 1)** — first clause
that fires wins; explicit final else; precedence METHODOLOGICAL NULL > UNDER-POWERED >
the CI clauses. Per model:

1. **METHODOLOGICAL NULL** if < 3 gated clusters in either direction — whatever the point
   estimates say.
2. **UNDER-POWERED** if out-of-pair > 0.5 on parsed picks.
3. **FALSIFIED (non-commutative, chronology-tracking)** if ρ_chron's CI excludes 0.5 **on
   the same side in BOTH presentation directions** (two-sided: recency or primacy,
   direction reported) and the ≥24 floor holds. → the conjecture's invariance bet
   falsified for that model, **under forced-label elicitation** (scope limit); the
   positive surfaced, not auto-promoted, under the usual contingency discipline.
4. **PHYSICAL-POSITION ARTIFACT** if ρ_phys's CI excludes 0.5 on the same side in both
   directions (ρ_chron clause unfired) and the ≥24 floor holds. → pre-registered reading
   (critic S1): **"position-following or direction-instruction neglect — observationally
   equivalent here"**; methodological, says nothing relational.
5. **COMMUTATIVE-NULL-CERTIFIED** if all four CIs (ρ_chron, ρ_phys × both directions)
   include 0.5 (non-degenerate) and the ≥36 floor holds (an absence claim needs a
   sample-size floor, not just CI coverage). → extends the v1 null to "position of
   conflicting convention evidence"; the conjecture stays `proposed`, strengthened, not
   proven; "certified" means the pre-registered null clause fired, never a precise zero.
6. **INCONCLUSIVE — null pattern, certification floor unmet** (named gap sub-label) if
   the guard holds, out-of-pair ≤ 0.5, all four CIs include 0.5, but the ≥36 floor is
   unmet — no clause fires.
7. **Else: INCONCLUSIVE / MIXED** — everything not caught above (arms disagree, opposite
   sides, a degenerate CI, or a CI pattern below the ≥24 effect floor) — the v2 outcome,
   reported with point estimates and no substantive label.

- **Multiplicity (acknowledged, inherited)**: "≥1 model fires" over 3 models at 95% CIs
  carries ≈14% family-wise false-positive risk under the global null; the both-directions
  requirement tightens it, **but as two correlated tests, not independent ones** (critic
  S6: fwd/rev share clusters and stimuli).

## Power rationale (fix 3)

v2's binding constraint was not nominal n but **gate survival and truncation**: nominal 6
clusters/model decayed to 4 (claude, then −NA attrition), 1 (gpt), 2-of-3 (gemini). v3
attacks realized-n directly: certified stimuli should put gate survival near ceiling, and
the forced format plus the never-parse-truncated rule should drive truncation NAs to near
zero, so realized gated n should approach the nominal **9 clusters / 54 mixed trials per
direction per model** (vs v2's nominal 6/36, gemini 3/18; realized far less). That is
~1.5× nominal and ~2×–9× *realized* over v2, and it removes the single-cluster
degenerate-CI regime entirely. Still pilot-scale, stated plainly: with 9 clusters, only a
**consistent ρ_chron ≳ 0.7** is reliably CI-clean; CI-includes-0.5 remains
*inconclusive-leaning-null*, not a precise zero; orderings and effect-direction, not
effect sizes. Two honesty notes (critic S6), disclosed next to that caveat: (a) the
fwd/rev arms share clusters and stimuli, so the both-directions agreement requirement is
**two correlated tests, not independent replications**; (b) a symmetric U-shaped
(primacy+recency) serial-position profile dilutes ρ_chron toward 0.5 in **both**
directions — a bias **toward the conjecture's own bet** — so CI-includes-0.5 is
consistent with either genuine order-invariance or a symmetric order effect (the
clean-switch vs interleaved secondary is the descriptive probe of that profile).

## Cost pre-flight (billed `usage.cost`, not rate-card)

Yardstick: v2's finding-bearing run billed **$0.277 for 210 calls** (≈$0.0013/call,
probe-shaped); v1's game calls billed ≈$0.0011 each. v3 is **≈3.3× v2's call count**
(critic S1 added 54 control calls, ≈+$0.07) — said plainly:

| phase | calls | est. billed |
|---|---|---|
| harvest (18 calls + ≤18 top-ups; director-shaped) | ≤36 | ≈$0.05 |
| certification (≤48 distinct candidates × 3 models; 1-line probe-shaped) | ≤144 first pass | ≈$0.17 |
| certification of top-up candidates (honest worst case, critic S3: each top-up call can add up to 8 more candidates) | ≤+144 | worst ≈+$0.17; expected ≈$0 |
| probe `full` (3 × [108 mixed + 36 controls]) | 432 (+retries) | ≈$0.62 |
| liveness + preflight (3 + 9 gpt + 9 claude controls; never analyzed) | 21 | ≈$0.03 |
| **total** | **≈630 expected; ≤790 worst case (+retries)** | **≈$0.87; expectation stated: < $1.00** |

Worst-case sensitivity, disclosed: the 512-token cap means a persistently non-compliant
claude (deliberating to cap on most trials) could push the probe phase toward ≈$1.35 total;
the forced format exists precisely to prevent this, the liveness format-gate checks
compliance before any finding-bearing call, and **phase checkpoints** apply — billed cost
recorded after harvest, certification, and preflight, plus a **per-model checkpoint inside
the `full` phase** (critic S2: projected total re-checked before each model's batch from
*realized* per-call billed costs; preflight includes claude controls so the projection
sees the priciest model), with a pre-registered **hard stop at $1.50 projected total**
(re-design, don't push through). Well under the $2.50 single-run flag and the $5.00/day
cap; actual billed `usage.cost` recorded per phase in `config/budget.md`.

## Anchor posture

`anchor: internal-contrast-only` — the recency/commutativity measure is the probe's own
**within-model contrast**; **no human-comparison claim**, per the ratified relational-line
posture
([`decisions/resolved/relational-pilot-operationalization`](../../wiki/decisions/resolved/relational-pilot-operationalization.md),
[`decisions/resolved/relational-fetchable-anchor`](../../wiki/decisions/resolved/relational-fetchable-anchor.md);
terminal-state mechanics introduced with
[`decisions/resolved/conflicting-cue-human-anchor`](../../wiki/decisions/resolved/conflicting-cue-human-anchor.md)).
Hawkins anchors nothing here. The conjecture's human-contrast clause stays a characterized
prediction: Brennan & Clark 1996 anchors historicity/partner-specificity only, not human
order-sensitivity
([`source/brennan-clark-1996-conceptual-pacts`](../../wiki/base/sources/brennan-clark-1996-conceptual-pacts.md)).

## Gate check — does v3 stay inside the ratified instrument class?

**Verdict: yes; no new operationalization decision page is opened.** Justification, choice
by choice:

- **Instrument class unchanged**: text-grid referents, near-twin pairs, fresh-matcher
  probe-shaped elicitation, constructed contradictory records with byte-identical
  multisets, nonce coined terms, internal within-model contrast — all exactly the v2
  instrument, which the ratified
  [`decisions/resolved/relational-pilot-operationalization`](../../wiki/decisions/resolved/relational-pilot-operationalization.md)
  recommended as the perturbation arm. Text grids in particular: the ratification's Q1-A
  rationale (the order manipulation requires byte-identical reorderable content, which text
  serializes exactly) applies with *more* force here, since byte-identical multisets are
  the whole manipulation. The ratification is v1-scoped, so this is a justified reuse, not
  a claimed entitlement; the image upgrade stays a named future extension.
- **Fixes 1, 3, 4, 5 are instrument hygiene, not construct choices**: elicitation format,
  cluster count, a minimum-n guard, and a retained control arm change *measurement quality*
  of the same yardstick, not what is measured.
- **The one borderline call, flagged rather than smuggled (fix 2)**: v3's descriptions are
  **freshly harvested + individually certified**, where v1/v2's were live-game by-products.
  Judged here as inside-class — the records were *already* constructed artifacts (composed,
  uniform fabricated feedback, asserted about "ONE target"), so ecological status changes
  in degree, not kind; certification operationalizes the same stimulus-quality requirement
  the v2 critic's B2 gate introduced, and its bias direction (sharper conflict, anti-null)
  is disclosed above. **The pre-run critic was explicitly asked to contest this judgement**
  (open issue 1 below) and **ruled it inside-class** (2026-06-13): no decision page; two
  conditions recorded as scope limits in the run PREREG (stimuli are
  harvested-and-certified, not live-game by-products — to be repeated in the eventual
  result page — and certification selects for individually decodable lines, so the result
  is conditional on evidence lines that work singly and says nothing about conventions
  whose lines are only interpretable in context).

## Open issues for the pre-run critic — RESOLVED 2026-06-13 (critic verdict: GO after fixes)

1. **Provenance shift** — ruled **inside-class hygiene; no decision page**, with the two
   scope-limit conditions above recorded in the run PREREG.
2. **Batch harvest** — retained as designed; certification absorbs the register worry.
3. **Guard calibration** — k = 3 retained; the asymmetry resolved by adding a **≥24-trial
   per-direction floor to the effect clauses** (FALSIFIED, ARTIFACT) while
   null-certification keeps ≥36 (blocker 3).
4. **Forced format vs deliberation** — retained, with the pre-registered scope limit that
   any FALSIFIED/CERTIFIED verdict holds **under forced-label elicitation**; suppressing
   visible deliberation could change the pick mechanism.
5. **Certification by the same model** — same-model certification retained; the
   cross-model cross-check is **deferred** (see §Stimuli plan: never gating; a future
   session; pre-registered descriptive only).

## Run plan

New run directory `experiments/runs/<date>-relational-history-perturbation-v3/`:
`harvest.py` (harvest + certification → census) → `build_stimuli.py` (frozen sha256 in
`PREREG.md`) → `probe.py` (liveness/format-gate, preflight, full) → `analyze.py` →
result page. `PREREG.md` is frozen **after** the independent pre-run critic pass and
**before** any finding-bearing call; critic revisions logged in the PREREG as in v2.
