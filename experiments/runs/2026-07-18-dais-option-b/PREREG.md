# PREREG — DAIS Option-B graded-preference correlation (s248 freeze)

**Frozen 2026-07-18 (session 248), BEFORE any model call.** This preregistration fixes the
instrument, the human targets, every statistic, threshold, and verdict band, and the deterministic
band-assignment decision-tree. Nothing below is touched after the correlations are seen (charter §8;
PROTOCOL §B anti-cheat).

- **Design (RATIFIED s247):** [`design/dais-graded-preference-correlation-v1`](../../designs/dais-graded-preference-correlation-v1.md)
  (Q1-A / Q2-A / Q3-A + freeze BLOCKERS **B1–B3** / SHOULD-FIX **S1–S3**); resolved decision
  [`decisions/resolved/dais-graded-preference-correlation-design`](../../../wiki/decisions/resolved/dais-graded-preference-correlation-design.md).
- **Frozen stimulus file:** `stimuli.json`
  **sha256 = `8e26f033bb47d9ff2db0bd346e1a572fcfb36394543775373827c0fee35b44ab`**
  (`probe.py` refuses to run unless this exact sha is recorded here — freeze gate).
- **Human targets** (`human_targets.json`) and the **frequency/classification control**
  (`freq_control.json`) are derived from the committed `verb_recipient_means.csv` + the sha-pinned
  gitignored raw DAIS CSV. `analyze.py` reads them; the **run** (`probe.py`) is BLIND to them.

## Scope fence (LOAD-BEARING — read before citing anything this produces)

This probe measures a **bare** (no-discourse-context) graded DO-preference and correlates it against
DAIS's human **definiteness/length + verb-bias preference surface**. It is **NOT** a human-effect-size
comparison for the project's discourse-context givenness shift
([`claim/dative-information-structure-givenness`](../../../wiki/findings/claims/dative-information-structure-givenness.md)),
which has no human effect-size anchor by design and is **untouched** here (its anchor stays
`languageR::dative` production, direction-only). The DAIS anchor edge lands on the **new result**,
scoped to the definiteness/length + verb-bias surface only (Q3-A). The self-description "the dative
line's first human effect-SIZE comparison" is used only **scoped**, never adjacent to the givenness
magnitudes (resolution's one residual guard).

## Instrument (frozen)

- **Panel** = the three [`config/models.md`](../../../config/models.md) slots (`panel.A` claude /
  `panel.B` gpt / `panel.C` gemini), all SUBJECTS; cross-model spread is data (charter §6, prediction 3).
- **Indicator:** the ratified dative graded forced-choice (100 points between the DOC and PD
  phrasings), reused **byte-shape** but with **NO discourse context** — a bare naturalness preference
  matching DAIS's isolated-pair slider. DO-preference = DOC_points / (DOC_points + PD_points) ∈ [0,1].
- **Settings:** temperature 0, zero-shot, single-turn; `MAX_TOKENS=512`; `google/*` gets
  `reasoning={"effort":"minimal"}` (config caveat). Position-based parse (target-blind); the DOC↔A/B
  mapping is counterbalanced and frozen per trial (`doc_is_a`).
- **Stimuli (Q1-A, project-constructed):** subject `Nadia`; DOC = "`Nadia {verb} {recipient} {theme}.`",
  PD = "`Nadia {verb} {theme} to {recipient}.`". DAIS supplies ONLY the 200-verb list + the human
  ratings — never a sentence.

### B3 — contamination disjointness (project realizations vs DAIS)

Asserted mechanically at build (`disjointness_manifest.json`): **0** project stimulus strings appear
verbatim among DAIS's 10,000 released `DOsentence`/`PDsentence` strings; no project recipient
realization equals a DAIS canonical realization; no project theme head-noun sits in DAIS's 333 theme
heads; the subject `Nadia` is disjoint from DAIS's 8 subjects.

**B3(b) fidelity audit** (`fidelity_audit.json`) — the 5 recipient conditions, project realization vs
the DAIS factor level, length/definiteness matched exactly:

| condition | project | DAIS canonical | wc (proj/DAIS) | definiteness | length |
|---|---|---|---|---|---|
| pronoun | `her` | `him` | 1/1 | pronoun | pronoun |
| shortDefinite | `the girl` | `the man` | 2/2 | definite | short |
| shortIndefinite | `a girl` | `a man` | 2/2 | indefinite | short |
| longDefinite | `the girl from college` | `the man from work` | 4/4 | definite | long |
| longIndefinite | `a girl from college` | `a man from work` | 4/4 | indefinite | long |

The theme is held **fixed** per verb across the 5 conditions, so only the recipient factor moves. The
theme cancels between an item's DOC and PD phrasings and never enters any correlation; one neutral
project theme per semantic bucket (`a parcel / a frisbee / a dividend / an anecdote / a warning /
a confidence / a ballad / a sketch / a memo / a riddle`, all head-nouns disjoint from DAIS).

## Arms, N, cost (Q2-A)

- **Arm A — verb-bias magnitude.** 200 verbs × the **canonical condition `shortDefinite`** (the same
  neutral matched baseline across all verbs) × 3 models = **600 calls**.
- **Arm B — recipient definiteness/length surface.** A freeze-frozen random **40** of the 100
  alternating verbs (seed 20260718) × 5 conditions × 3 models = **600 calls**.
- **Total 1,200 calls.** Pre-flight ≤ the powered dative probe's ~$0.00217/call (bare preference is
  shorter → likely lower) ⇒ ~$2.0–2.6. Per-arm `HARD_STOP_USD` $1.70; total ceiling $3.40 (caps the
  UTC-2026-07-18 day at ≤ ~$3.40 < $5.00 given $0.002286 prior). Above the $2.50 prefer-split flag →
  run as the day's only spend on this full-$5 UTC day (s229 precedent), or split the two arms across
  UTC days (each arm an independent frozen instrument; splitting changes neither measurement).

## Arm A statistics + B2 control

- **Primary:** Spearman ρ(model per-verb DO-pref at `shortDefinite`, human per-verb mean `DOpreference`
  at `shortDefinite`) — the **matched-condition** ρ, per model, 10,000-boot verb-resample 95% CI.
- **Robustness (reported, non-decisive):** ρ vs the human per-verb **collapsed** mean.
- **B2 — the frequency/classification control is a CONJUNCT of TRACKS, not a side-caveat.** The binding
  control = **alternating-only ρ** (restrict to the 100 alternating verbs — removes the
  alternating/non-alternating lexical-subcategorization split that dominates the full ρ), with a boot
  CI. Also reported: **partial** Spearman ρ(model, human | classification, within-class freq rank). A
  model "passes the control" iff **alternating-only ρ CI-LB > 0**. The flagship **TRACKS** label
  requires this control to survive ≥2/3; a full-ρ that clears but whose control fails earns only
  **VERB-BIAS-ONLY (may be lexical)**.
- **Contamination ceiling:** matched ρ ≥ **0.95** on any model ⇒ CONTAMINATION-CEILING flag (ρ read as
  a memorization upper bound, not competence).

## Arm B statistics — B1 pinned predicate + null

- **B1 — per-verb monotonicity predicate + chance null (FROZEN).**
  - Human canonical direction: mean DOpreference **decreasing** across `pronoun > shortDefinite >
    shortIndefinite > longDefinite > longIndefinite` (ranks 5,4,3,2,1; the firsthand-reproduced DAIS
    gradient 37.7 > 30.5 > 25.2 > 20.8 > 18.3).
  - **SUCCESS(verb)** := Spearman ρₛ(model's 5 condition-mean DO-prefs, human direction ranks) **≥
    +0.50**. A verb whose 5 condition means are ALL TIED (ρₛ undefined) counts as a **non-success**.
  - **Null p0** := P(ρₛ ≥ 0.50 | the 5 condition means are a uniform random permutation of 5 distinct
    values) = **27/120 = 0.225** (enumerated exactly over all 120 permutations of ranks; ρₛ = 1 −
    Σd²/20 for n=5).
  - **Powered Arm-B measure:** the per-model **monotonicity RATE** over the ≤40 used verbs, tested
    **one-sided binomial** H0: rate ≤ p0. "Beats chance" := binomial p < 0.05. At n=40 this needs ≥14
    successes (35%); power ≥ 0.98 at a true success rate ≥ 0.50. The 5-condition marginal ρ is reported
    as a **direction check only** (n=5, no CI).
- **Binding within-length definiteness control** (the LENGTH-ONLY guard). Per model over the used
  verbs: `short_contrast` = mean(shortDefinite − shortIndefinite DO-pref), `long_contrast` =
  mean(longDefinite − longIndefinite DO-pref), each with a boot CI. A model **passes** iff BOTH boot
  CI-LBs > 0 (definite raises DO at both lengths, the human direction: human short +5.35, long +2.47).
  Absent this (≥2/3), a reproduced recipient gradient is **end-weight counting**, not
  definiteness-tracking → **LENGTH-ONLY**.

## S3 — deterministic band-assignment decision-tree (identical in `analyze.py::decide`)

Let (each a boolean over the 3 models, ≥2/3):
`armA_full` = per-verb matched-ρ CI-LB>0; `armA_ctrl` = alternating-only ρ CI-LB>0 (B2);
`armB_mono` = monotonicity rate beats chance (binom p<0.05, B1); `armB_within` = within-length
definiteness control passes.

```
if armB_mono and armB_within:
    band = TRACKS-HUMAN-SURFACE   if (armA_full and armA_ctrl)   else SURFACE-ONLY
elif armB_mono and not armB_within:
    band = LENGTH-ONLY
elif armA_full and not armB_mono:
    band = VERB-BIAS-ONLY         (+" (may be lexical)" if not armA_ctrl)   # B2
else:
    band = DECOUPLED-OR-NULL
CONTAMINATION-CEILING flag (any matched-ρ ≥ 0.95) annotates the band; ρ read as an upper bound.
```

Every band is a pre-named first-class outcome. **S1 standing contamination caveat (binding on any
non-null band):** DAIS verb bias is exactly what the source paper showed LMs partly capture, and
per-verb bias is memorizable under Q1-A even with disjoint sentences — so a moderate-but-clean ρ stays
contamination-vulnerable; the ceiling flag is one tripwire, not the defense (the real defenses are the
controls + Q1-A + "pattern not magnitude"). **S2:** the result headline leads with **Arm B** (the
s245-named definiteness/length surface + within-length control); Arm A (verb-bias) is the companion,
recorded as an explicit honest extension of the s245 scope to the paper's headline verb-bias construct,
never re-anchoring the givenness claim.

## Anchor + promotability (Q3-A)

`anchor: human-anchored`, `anchors: → resource/dais-dative-ratings`, scoped to the definiteness/length
+ verb-bias surface, NOT the givenness shift. Single run ⇒ the result stays **`proposed`**; a `claim`
(a human-effect-size dative claim on the definiteness/length surface, held distinct from the givenness
claim) needs a fresh-item replication + a cross-session promotion review.

## Registered bet

[`predictions.md`](../../../wiki/predictions.md) §B DAIS-correlation bet, finalized at this freeze:
**pre-registered prediction = TRACKS-HUMAN-SURFACE fails as a clean 3/3 — most likely LENGTH-ONLY or
VERB-BIAS-ONLY** (the panel reproduces the raw recipient gradient and/or the verb-bias magnitude, but
the binding within-length definiteness control and/or the alternating-only frequency control does not
clear ≥2/3), with gpt the weakest leg (its persistent-shadow pattern across the dative/particle lines).
Outcome updated the run session.

## Pre-run gates (before the frozen instrument runs)

1. Independent **fresh-agent pre-run critic** → recorded below.
2. One **non-Anthropic decorrelation vote** (`PANEL["B"]` = gpt-5.4-mini) → recorded below.
3. **Liveness** (3 calls, held-out trial) must parse the graded FINAL line on all 3 models.
4. Blind scoring: `probe.py` never reads `human_targets.json`; `analyze.py` recomputes every figure
   from raw; a post-run verifier re-runs `analyze.py` to reproduce.

### Gate outcomes (freeze, s248)

- **Non-Anthropic decorrelation vote** (`PANEL["B"]` = gpt-5.4-mini, `vote.py` / `VOTE-freeze-s248.json`,
  $0.003340): **GO-WITH-CONDITIONS**. B1 FIX (make tie-handling explicit); B2 FIX (require the
  alternating-only control be *positive*, CI-LB>0, not merely "not failed" — already the coded rule);
  B3 OK (faithful factor match, firewall materially stronger than a theme/recipient overlap check, no
  DOC/PD asymmetry from the fixed cancelling theme); BANDS FIX (a strong memorizer + two weak positives
  under ≥2/3 could be hidden; CONTAMINATION-CEILING is a warning not a fence). Conditions folded below.
  - **B1 tie-handling (explicit, per the vote).** ρₛ is computed with average ranks (scipy
    `spearmanr`) so *partial* ties are handled; a verb with **all 5 condition means tied** yields
    ρₛ = nan and is a **non-success**. The pinned null **p0 = 0.225 is the no-ties permutation
    baseline** — a fixed, conservative reference for the tie-inclusive realized rate (ties can only
    lower a verb's ρₛ, so using the no-ties null does not inflate "beats chance").
  - **B2 (explicit).** The control is a *positive* requirement: **alternating-only ρ boot CI-LB > 0**
    (`analyze.py` `alt_ci_lb_gt0`), a TRACKS **conjunct**, not a side-caveat. A full-ρ that clears while
    the control fails earns only VERB-BIAS-ONLY (may be lexical).
  - **BANDS (per the vote's ≥2/3 concern).** Every model's ρ, CI, and monotonicity rate are reported
    **per model** in `analysis.json` and the result page; the verdict is n=3 orderings, **not** pooled
    coefficients, so a single strong memorizer behind two weak positives is **visible, not hidden**, and
    the S1 standing contamination caveat binds any non-null band. The end-weight failure mode (a
    monotonicity rate that beats chance via pure length-counting) is caught by the **binding
    within-length definiteness control** → the LENGTH-ONLY band. CONTAMINATION-CEILING is explicitly
    "one tripwire, not the defense" (S1); the real defenses are the two controls + Q1-A + "pattern not
    magnitude".
- **Fresh-agent pre-run critic** (verdict authority): **GO-WITH-CONDITIONS**. Reproduced the freeze
  artifacts and re-derived the load-bearing numbers; B1 null/predicate, B2 conjunct wiring, B3
  disjointness+fidelity, S1–S3, anti-cheat, and the scope fence all verified. One binding condition:
  - **C1 (binding, APPLIED before any model call):** the implemented Arm-B predicate `rs >= 0.50`
    silently excluded the six exact-ρₛ=0.5 permutations (scipy returns 0.4999…94), so the *scored*
    predicate was effectively `> 0.50` whose true null is 21/120 = 0.175, **not** the frozen 27/120 =
    0.225 — breaking B1's predicate↔null pairing (conservative in direction, not result-inflating).
    **Fixed:** `analyze.py::arm_b` now compares `rs >= RHO_THR - 1e-9`, so the six exact-0.5 patterns
    score as successes exactly as the pinned null assumes (re-verified: 27/120; ≥14/40 threshold
    unchanged). No frozen PREREG value moved; `stimuli.json` sha unchanged.
  - **C2 (recommended, HONORED):** the result page + `analysis.json` surface **per-model** gate
    booleans and the three raw ρ / monotonicity-rate values alongside the ≥2/3 verdict, so a single
    strong-memorizer driving a gate is visible, not hidden.
  - Critic also confirmed the end-weight escape (a monotonicity rate beating chance via pure
    length-counting) is correctly quarantined to **LENGTH-ONLY** by the within-length control, and Arm
    A cannot be end-weight-gamed (single fixed condition across all verbs).
- **Liveness:** _appended at run._
