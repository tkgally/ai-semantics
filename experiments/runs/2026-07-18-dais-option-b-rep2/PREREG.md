# PREREG — DAIS Option-B graded-preference correlation REP2 (s250 freeze)

**Frozen 2026-07-18 (session 250), BEFORE any model call.** A **fresh-item replication** of the s248
result [`result/dais-graded-preference-correlation-v1`](../../../wiki/findings/results/dais-graded-preference-correlation-v1.md).
The **instrument is byte-frozen**; only the project fillers change (fresh, disjoint from DAIS *and*
from v1). Nothing below is touched after the correlations are seen (charter §8; PROTOCOL §B anti-cheat).

- **Design (RATIFIED s247):** [`design/dais-graded-preference-correlation-v1`](../../designs/dais-graded-preference-correlation-v1.md)
  (Q1-A / Q2-A / Q3-A + B1–B3 / S1–S3). The replication + promotion route is named in the design's Q3
  ("a `claim` … needs a fresh-item replication + a cross-session promotion review") and in the s248
  result's "What it feeds".
- **Byte-frozen instrument.** `probe.py` and `analyze.py` are **sha256-identical** to the s248 run
  (`probe.py` `7826bbca…`; `analyze.py` `14065ab2…` — verify with `sha256sum`). `common.py` differs from
  s248 **only** in the two budget hard-stop constants (`HARD_STOP_PER_ARM_USD` 1.70→1.30,
  `HARD_STOP_USD` 3.40→2.60, so this run cannot breach the $5/day UTC cap given $1.826368 already spent
  UTC-2026-07-18); all measurement machinery (SYS/USER_TMPL/parse/doc_pref/call_graded) is byte-identical.
- **Frozen stimulus file:** `stimuli.json`
  **sha256 = `a5779f04cd9ea70f337b749c2233fdf832ba0a6bab4be67e32dd9636a341e159`**
  (`probe.py` refuses to run unless this exact sha is recorded here — freeze gate). *(The pre-freeze
  build sha `5b87f4c0…` was superseded when the s250 freeze-vote FRESHNESS condition was folded in
  pre-data — Arm-B verbs made fully disjoint from v1's subset; see Gate outcomes below. No model call
  was ever made against the superseded build.)*
- **Human targets** (`human_targets.json`, byte-verified **identical** to v1's `human_arma_matched`) and
  the **frequency/classification control** (`freq_control.json`) derive from the committed
  `verb_recipient_means.csv` + the sha-pinned gitignored raw DAIS CSV. `analyze.py` reads them; the
  **run** (`probe.py`) is BLIND to them.

## Scope fence (LOAD-BEARING — carried verbatim-in-force from s248)

This probe measures a **bare** (no-discourse-context) graded DO-preference and correlates it against
DAIS's human **definiteness/length + verb-bias preference surface**. It is **NOT** a human-effect-size
comparison for the project's discourse-context givenness shift
([`claim/dative-information-structure-givenness`](../../../wiki/findings/claims/dative-information-structure-givenness.md)),
which has no human effect-size anchor by design and is **untouched** here (its anchor stays
`languageR::dative` production, direction-only). The DAIS anchor edge lands on the **rep2 result**,
scoped to the definiteness/length + verb-bias surface only (Q3-A).

## What is fresh, what is frozen (the replication)

**Fresh (the items):** subject `Priya` (v1 `Nadia`); recipient realizations `them / the clerk / a clerk
/ the clerk from downtown / a clerk from downtown` (v1 `her / the girl / a girl / the girl from college
/ a girl from college`); the 10 per-bucket theme nouns (`a crate / a boomerang / a rebate / a fable /
an alert / a confession / a hymn / a diagram / a postcard / a puzzle`, all disjoint from v1's); the Arm-B
40-verb subset (seed 20260250, sampled from the **60 alternating verbs NOT in v1's subset** → **0/40
shared with v1**, fully verb-disjoint as well as sentence-fresh; the freshness firewall folded in
pre-data per the freeze vote).

**Frozen (the instrument + yardstick, all UNCHANGED from s248):** the 200-verb list; the human targets;
the canonical Arm-A condition (`shortDefinite`); the 5 factor levels; the graded forced-choice indicator;
the Arm-A ρ + bootstrap-CI statistic; the B2 alternating-only + partial controls; the B1 monotonicity
predicate (ρₛ≥+0.50) + its exact chance null p0 = 27/120 = 0.225 (with the C1 fix `rs >= RHO_THR-1e-9`
already in the frozen `analyze.py`); the within-length definiteness control; the S3 band decision-tree;
the contamination-ceiling threshold (0.95).

### Two disjointness firewalls (both asserted at build; both PASS — `disjointness_manifest.json`)

1. **vs DAIS (B3):** 0 rep2 stimulus strings appear verbatim among DAIS's released sentences; no rep2
   recipient realization equals a DAIS canonical; no rep2 theme head-noun sits in DAIS's 333 theme
   heads; subject `Priya` disjoint from DAIS's 8.
2. **vs v1 (the fresh-item firewall):** 0 rep2 stimulus strings appear in the committed s248
   `stimuli.json`; rep2 subject / recipient realizations / theme head-nouns all disjoint from v1's; the
   Arm-B 40-verb subset is **0/40 shared** with v1's. This is the "0 shared items" standard
   (sense-gradience-rep2 / dative-powered).

**B3(b) fidelity audit** (`fidelity_audit.json`) — the 5 recipient conditions, rep2 realization vs the
DAIS factor level, word-count + definiteness matched exactly:

| condition | rep2 | v1 | DAIS canonical | wc | definiteness | length |
|---|---|---|---|---|---|---|
| pronoun | `them` | `her` | `him` | 1 | pronoun | pronoun |
| shortDefinite | `the clerk` | `the girl` | `the man` | 2 | definite | short |
| shortIndefinite | `a clerk` | `a girl` | `a man` | 2 | indefinite | short |
| longDefinite | `the clerk from downtown` | `the girl from college` | `the man from work` | 4 | definite | long |
| longIndefinite | `a clerk from downtown` | `a girl from college` | `a man from work` | 4 | indefinite | long |

## Arms, N, cost (Q2-A, unchanged)

- **Arm A — verb-bias magnitude.** 200 verbs × canonical `shortDefinite` × 3 models = **600 calls**.
- **Arm B — recipient definiteness/length surface.** 40 alternating verbs (seed 20260250) × 5 conditions
  × 3 models = **600 calls**.
- **Total 1,200 calls.** Pre-flight at the s248 measured rate (~$0.001517/call, from $1.820742/1,200)
  ⇒ **~$1.82**. Per-arm `HARD_STOP_USD` $1.30; total ceiling $2.60 → caps the UTC-2026-07-18 day at
  ≤ $1.826368 + $2.60 = **$4.43 < $5.00**. The run is this session's only planned spend (plus one
  ~$0.003 non-Anthropic vote). Below the $2.50 single-run flag ($1.82 expected), so no split needed.

## Arm A / Arm B statistics + controls (ALL FROZEN, identical to s248)

Reproduced from the s248 PREREG for reference; `analyze.py` is byte-identical so the computation is
literally the same code:

- **Arm A primary:** Spearman ρ(model per-verb DO-pref at `shortDefinite`, human per-verb mean at
  `shortDefinite`), 10,000-boot verb-resample 95% CI, per model. **B2 binding control:** alternating-only
  ρ (100 alternating verbs) with a boot CI — pass iff CI-LB > 0; plus partial ρ(model,human |
  classification, within-class freq rank). Contamination-ceiling flag at matched ρ ≥ 0.95.
- **Arm B:** per-verb monotonicity RATE over the used verbs (SUCCESS := ρₛ(model 5 condition-means, human
  ranks 5,4,3,2,1) ≥ +0.50; all-tied ⇒ non-success), tested one-sided binomial H0: rate ≤ 0.225 (beats
  chance iff p < 0.05; ≥14/40 needed). **Binding within-length definiteness control:** short_contrast =
  mean(shortDef − shortIndef), long_contrast = mean(longDef − longIndef), each boot-CI; pass iff BOTH
  CI-LBs > 0. The 5-condition marginal ρ is a direction check only (n=5, no CI).
- **S3 band decision-tree** (identical wording in `analyze.py::decide`): TRACKS-HUMAN-SURFACE /
  SURFACE-ONLY / LENGTH-ONLY / VERB-BIAS-ONLY(+may be lexical) / DECOUPLED-OR-NULL. **S1 standing
  contamination caveat** binds any non-null band. **S2** the result headline leads with Arm B.

## THE REPLICATION PREDICATE (frozen; `replication_check.py`, committed before any model call)

The **promotable leg** is the **Arm-A verb-bias ρ** (the s248 result's "What it feeds"; the design's Q3).
The Arm-B within-length definiteness leg is a **null-leaning LENGTH-ONLY dissociation, NOT promotable** —
its replication is reported (does the dissociation hold?) but never gates promotion.

Per model, then ≥2/3:
- **R1** rep2 matched-ρ **CI-LB > 0** — the verb-bias correlation exists on fresh items.
- **R2** rep2 **alternating-only ρ CI-LB > 0** — the binding B2 control survives (the correspondence is
  not merely the memorizable alternating/non-alternating lexical-subcategorization split).
- **R3** rep2 matched-ρ **point estimate lies within v1's 95% CI** — a magnitude consistent with v1
  (the documented sense-gradience-rep2 standard, "every base ρ within v1's CI"). This is **strictly
  tighter than a CI-overlap test**, which the s250 freeze vote flagged as gameable by two wide intervals;
  the pre-run critic separately showed a null rep2 cannot reach v1's CIs anyway, but R3-as-point-in-CI
  removes the objection by construction. CI-overlap and (v1-point-in-rep2-CI) are kept as **descriptive,
  non-gating** fields in `replication.json`.

**VERB-BIAS-REPLICATES := (R1 ≥2/3) ∧ (R2 ≥2/3) ∧ (R3 ≥2/3).** A VERB-BIAS-REPLICATES verdict only
**LICENSES a separate, precommitted cross-session promotion review** — it does **not** itself promote and
does **not** automatically unlock a `claim`. That review (fresh reviewer + one non-Anthropic vote) is an
independent adjudication that **MAY DECLINE** even when VERB-BIAS-REPLICATES holds (e.g. if it judges the
contamination caveat bars a scoped claim). The claim it could write is a human-effect-size dative claim on
the **verb-bias surface**, held **distinct** from the (untouched) givenness claim. Anything short of ≥2/3
on any conjunct ⇒ report the divergence, **no promotion**.

Also reported (non-gating): whether the s248 **instrument band** (LENGTH-ONLY) itself replicates (rep2
`analyze.py::decide` band == LENGTH-ONLY), i.e. whether the whole verb-bias-tracked-but-definiteness-
length-dominated dissociation is stable across fresh items.

**S1 contamination caveat (binding).** Even a clean, replicated, moderate verb-bias ρ stays
contamination-vulnerable — DAIS is public since 2020 and per-verb bias is memorizable under Q1-A. A
replication of the verb-bias ρ raises confidence in the *correspondence's stability*, **not** in a
"competence beyond memorized lexical bias" reading; the controls (B2 alternating-only + partial) + the
Q1-A disjoint-sentence firewall + "pattern not magnitude" remain the defenses, and the promotion review
must hold the claim to the **direction/correspondence**, not a competence gloss.

## Anchor + promotability (Q3-A)

`anchor: human-anchored`, `anchors: → resource/dais-dative-ratings`, scoped to the verb-bias +
definiteness/length surface, NOT the givenness shift. The rep2 result stays **`proposed`** (a result
page's reading-lifecycle resting state; CLAUDE.md result-status discipline); a **`claim`** earns
`supported` on the claim layer only via the cross-session promotion review this replication licenses.

## Registered bet

[`predictions.md`](../../../wiki/predictions.md) §B. The **primary** DAIS-correlation bet
(TRACKS-HUMAN-SURFACE) was scored a **LOSS** at s248 (LENGTH-ONLY) and is not re-scored. This rep2
registers a **replication sub-bet**: **VERB-BIAS-REPLICATES = True** (the promotable Arm-A leg replicates
on fresh items ≥2/3 all-three-conjuncts). **Confidence: moderate-to-high** — the s248 Arm-A ρ was clean
(+0.61/+0.76/+0.63) with the alternating-only control surviving 3/3, so a fresh-item replication is
expected to hold; the residual risk is a per-model CI-overlap miss (R3) or gpt (the persistent weak leg)
slipping its alternating-only control. Scored on `replication_check.py`; outcome updates §B this session.

## Pre-run gates (before the frozen instrument runs)

1. Independent **fresh-agent pre-run critic** (verdict authority) → recorded below.
2. One **non-Anthropic decorrelation vote** (`PANEL["B"]` = gpt-5.4-mini) → recorded below.
3. **Liveness** (3 calls, held-out trial) must parse the graded FINAL line on all 3 models.
4. Blind scoring: `probe.py` never reads `human_targets.json`; `analyze.py` recomputes every figure from
   raw; a post-run verifier re-runs `analyze.py` + `replication_check.py` to reproduce.

### Gate outcomes (freeze, s250)

- **Fresh-agent pre-run critic** (verdict authority): **GO** — no binding conditions. Confirmed the
  instrument byte-identity, the reproducible freeze, both firewalls, the identical human anchor, and the
  fidelity audit; and **proved the replication predicate cannot be satisfied by a null** (a simulated null
  rep2 at n=200 gives CI-upper ≈ +0.14, max +0.39, which cannot reach v1's lowest CI-LB +0.50, so R1∧R2∧R3
  force a moderate positive ρ). Full verbatim verdict + reconciliation:
  [`REVIEW-critic-s250.md`](REVIEW-critic-s250.md).
- **Non-Anthropic decorrelation vote** (`PANEL["B"]` = gpt-5.4-mini, `vote.py` / `VOTE-freeze-s250.json`,
  $0.002181): **NO-GO** with three **tightening** FIX conditions (QA input; the fresh reviewer keeps
  verdict authority per the decorrelation rule). **All three folded pre-data** (no model call had been
  made — the s248 C1 precedent):
  - **FRESHNESS** (16/40 Arm-B verbs shared with v1) → Arm-B verbs re-sampled from the 60 v1-disjoint
    alternating verbs → **0/40 shared**; `stimuli.json` re-frozen `5b87f4c0…` → `a5779f04…`.
  - **PREDICATE** (R3 CI-overlap gameable) → R3 tightened to **rep2 point estimate ∈ v1's 95% CI** (the
    documented sense-gradience-rep2 standard, strictly tighter than overlap); overlap kept descriptive.
  - **PROMOTION** (should not auto-unlock) → PREREG + `replication_check.py` now state the promotion
    review is a separate, precommitted, independent adjudication that **may decline** even when
    VERB-BIAS-REPLICATES holds.
  Every fold only tightens the yardstick, so the critic's GO (on the looser pre-fold build) holds a
  fortiori. **Combined pre-run verdict: GO (yardstick tightened).**
- **Liveness (run):** 3/3 parsed the graded FINAL line (claude A=55/B=45, gemini A=45/B=55, gpt A=60/B=40),
  held-out trial `The courier handed the tenant a package.`, $0.00405.

## Run outcome (s250, appended after the run — frozen bands unchanged)

**Ran 2026-07-18 (session 250).** 1,200 calls (600 Arm A + 600 Arm B), **0 NA**, **$1.85321** billed
(liveness $0.00405 + Arm A $0.86668 + Arm B $0.98249; under the $2.60 total / $1.30 per-arm caps).

- **Arm-A verb-bias — VERB-BIAS-REPLICATES = True (3/3 all conjuncts).** matched ρ claude **+0.684
  [+0.600,+0.755]**, gemini **+0.815 [+0.761,+0.858]**, gpt **+0.701 [+0.627,+0.761]** — each inside the
  s248 95% CI (R3 3/3; gpt +0.701 vs v1 upper +0.702, a near-boundary pass); alternating-only control
  +0.630/+0.691/+0.539 all CI-LB>0 (R2 3/3); R1 3/3; partial ρ +0.526/+0.666/+0.524; no contamination
  ceiling. **The promotable leg replicated → licenses the cross-session promotion review** (conducted
  this session).
- **Arm-B definiteness/length — the BAND FLIPPED: rep2 = TRACKS-HUMAN-SURFACE (v1 was LENGTH-ONLY).** The
  within-length definiteness control cleared **2/3** (claude within_pass=True, gemini True, gpt False at
  long length: +0.026, CI incl. 0), where in v1 it failed 3/3 at long length. **Honest reading: the
  definiteness/length band is filler-UNSTABLE across two runs — not that TRACKS is now the answer.** Two
  single runs giving opposite bands ⇒ the band is under-determined at this N/filler (the long-length
  definite−indefinite contrast is small — human +2.47 pts — and filler-sensitive). **This leg is NOT
  promoted;** it is reported as a cross-filler band instability (a first-class caution). The verb-bias
  claim must not ride on the rep2 TRACKS band.
- **Registered §B replication sub-bet (VERB-BIAS-REPLICATES=True): WON.** (The primary TRACKS bet was
  scored a LOSS at s248 and is not re-scored; the rep2 band flip does **not** convert that loss —
  band-level TRACKS is not replicated, it is unstable.)
- **Post-run verifier:** _recorded in the run dir (VERIFY-s250)._ **Promotion review:** _see
  `REVIEW-promote-s250.md` + `claim/…` (this session)._
