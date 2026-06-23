---
type: design
id: within-lexical-scalar-vs-disjunctive-v1
title: within-lexical scalar-vs-disjunctive probe v1 — one frozen lexical commitment instrument applied to a scalar (DWUG bridging) arm and a disjunctive (balanced-homonym) arm, level held fixed, to test whether the lexical commit-without-hedging survives a genuine disjunction or collapses to the deflationary kind-reading
meaning-senses:
  - distributional
  - referential
status: draft
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-23
updated: 2026-06-23
links:
  - rel: operationalizes
    target: essay/ambiguity-kind-not-level
  - rel: depends-on
    target: decisions/resolved/matched-ambiguity-kind-cross-level
  - rel: depends-on
    target: result/cross-level-shared-instrument-v1
  - rel: depends-on
    target: result/lexical-bridging-context-v1
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: resource/subtlex-us-frequency
---

# Experiment design v1 — within-lexical scalar-vs-disjunctive probe

> **Status: BUILT + FROZEN, NOT RUN (2026-06-23, build session).** No probe was run and no
> spend was opened in the build. The single lexical commitment instrument is frozen and sha256'd
> ([`within-lexical-scalar-vs-disjunctive-v1/instrument.json`](within-lexical-scalar-vs-disjunctive-v1/instrument.json),
> [`instrument.sha256`](within-lexical-scalar-vs-disjunctive-v1/instrument.sha256)); the
> author-built disjunctive Arm-2 items, the nuisance-match record, and the reused Arm-1 stratum
> are frozen in [`freeze_manifest.json`](within-lexical-scalar-vs-disjunctive-v1/freeze_manifest.json)
> and build-certified (15/15 no-API checks PASS,
> [`certification_report.json`](within-lexical-scalar-vs-disjunctive-v1/certification_report.json)).
> The probe refuses to run without an explicit critic-GO flag; `ABORT_USD=0.60`. The frozen
> reading rule is encoded ([`analyze.py`](within-lexical-scalar-vs-disjunctive-v1/analyze.py)).
> **What remains is the run itself**, gated by a fresh independent **pre-run critic GO/NO-GO**
> against the frozen instrument and a **budget** check (a NO-GO defers the run, it does not relax
> a band). Pre-flight ≈ **$0.10–0.25**.

This operationalizes [`essay/ambiguity-kind-not-level`](../../wiki/findings/essays/ambiguity-kind-not-level.md)
(the kind-not-level re-reading of the cross-level dissolution) under its **resolved** gate
[`decisions/resolved/matched-ambiguity-kind-cross-level`](../../wiki/decisions/resolved/matched-ambiguity-kind-cross-level.md)
(ADOPT DEFAULT, session 86: **Q1 Option B**, **Q2-b internal-contrast-only** for the disjunctive
arm, **Q3 reading rule as written**, plus the binding **nuisance-matching freeze**). It is the
essay's **R2 test for the lexical case**.

## 0. The bet, in one sentence

The cross-level dissolution ([`result/cross-level-shared-instrument-v1`](../../wiki/findings/results/cross-level-shared-instrument-v1.md))
left a confound: the lexical leg's commit-without-hedging (≈0% UNCLEAR on the ambiguous item)
could be a fact about the **layer** (word-sense) **or** about the **kind** of ambiguity it was
handed (a *scalar* usage-similarity midpoint, with a nearer pole to lean to, rather than a
*disjunctive* both/neither). This probe **holds the level fixed (lexical) and varies only the
kind**: one frozen instrument, a **scalar** arm (DWUG bridging) and a **disjunctive** arm
(author-built balanced homonyms), to test whether the lexical commit-without-hedging **survives**
a genuine disjunction (→ layer; the kind-reading dissolves at R2, a *more* interesting positive
about word-sense) or **collapses** (→ kind; the lexical specialness was the softer stimulus).

## 1. The single shared instrument (inherited verbatim, frozen)

[`instrument.json`](within-lexical-scalar-vs-disjunctive-v1/instrument.json) inherits the
cross-level probe's **lexical leg** byte-for-byte: the `SAME/DIFFERENT/UNCLEAR` + 0–100 confidence
system prompt, the verbatim `UNCLEAR` decline gloss, the `[40,60]` mid-band, the one-line answer
format, temperature 0, and the decline-load-bearing reading rule (C1). It is applied
**identically** to both arms; the **only** thing that varies is the stimulus body's ambiguity
**kind**. Binding conditions **C1–C4** are inherited and re-frozen (sha256). The inherited decline
gloss is *scalar-flavoured* ("genuinely in between"); inheriting it verbatim is required (gate:
instrument unchanged), it is a **constant** across arms, and its flavour biases **toward** survival
(a disjunction is "both/neither", not "in between") — which is exactly why survival carries the
**higher** bar. Disclosed; not re-worded (re-wording would break the freeze).

## 2. The two arms (level held fixed = lexical word-sense)

| arm | ambiguous class | clear controls | stimulus kind | items | anchor |
|---|---|---|---|---|---|
| **scalar** | bridging | clear-same / clear-different | DWUG human-rated usage-similarity midpoint (DURel ≈ 2–3); a *graded* similarity with a nearer pole | MANIFEST → frozen DWUG stratum (48: 24 bridging + 9 + 15), reused unchanged | usage-similarity (capped) |
| **disjunctive** | disjunctive | clear-same / clear-different | author-built **balanced homonym** context: two unrelated senses both licensed, **no tie-break** (no nearer pole) | 36 author-built (12 homonyms × 1 disjunctive + 2 clear), committed | `internal-contrast-only` (Q2-b) |

- **Arm 1 (scalar)** reuses the lexical leg's frozen DWUG bridging stratum verbatim
  ([`items_arm1.json`](within-lexical-scalar-vs-disjunctive-v1/items_arm1.json) → `stratum.csv`
  sha `e7d36773…`); no re-authoring, no corpus text in-repo (staged from the gitignored DWUG
  fulltext via the lexical leg's `prep.py`).
- **Arm 2 (disjunctive)** items
  ([`items_arm2.json`](within-lexical-scalar-vs-disjunctive-v1/items_arm2.json), author-built,
  committed). Each of 12 balanced homonyms (bank, crane, file, mole, organ, trunk, tank, punch,
  plot, pupil, ring, club) carries: a **balanced** context (both unrelated senses licensed, no
  tie-break), two sense-A-fixed contexts, one sense-B-fixed context. Three items per homonym:
  **disjunctive** = (balanced, sense-A-fixed) → genuinely both/neither; **clear-same** =
  (sense-A, sense-A) → SAME; **clear-different** = (sense-A, sense-B) → DIFFERENT. The disjunctive
  item is the moment-pole test; the clear controls give the C3 precondition and the within-arm
  contrast.

## 3. The nuisance-matching freeze (binding condition, gate session 86)

Before any model call, the two arms are matched (or controlled) on the four named dimensions and
the record is frozen ([`nuisance_match.json`](within-lexical-scalar-vs-disjunctive-v1/nuisance_match.json),
checked by `certify.py`). Achieved match (Arm-2 disjunctive vs Arm-1 bridging):

- **Target-word frequency band** (SUBTLEX-US `Lg10WF`, [`resource/subtlex-us-frequency`](../../wiki/base/resources/subtlex-us-frequency.md)):
  Arm 2 mean **3.09** / median **3.15**; Arm 1 bridging mean 2.98 / **median 3.15** → **|median
  gap| = 0.00**.
- **Token/sentence length**: Arm 2 disjunctive sentences mean **28.5** tokens; Arm 1 bridging mean
  **28.0** → **|mean gap| = 0.46**. Within Arm 2, disjunctive (28.5) ≈ clear-same (27.4) ≈
  clear-different (26.9) — the **within-arm** length is uniform, so the load-bearing within-arm
  collapse contrast is length-clean.
- **Syntactic frame**: 12/12 Arm-2 targets are common nouns used as nouns (Arm 1 = 43 nn / 5 vb,
  mostly nn1 nouns).
- **Register (the irreducible residual, led with).** Arm 1 = DWUG/COHA corpus prose
  (literary/journalistic, 1810s–2010s); Arm 2 = author-built contemporary plain declarative prose.
  An author cannot make Arm 2 corpus-attested, so register cannot be fully matched. **Direction
  disclosed:** cleaner contemporary prose is, if anything, *easier* — it cuts **toward survival**
  (lower decline), so a **collapse** finding is the *harder* one to obtain under this residual, and
  a survival finding is the one the residual could partly manufacture (hence survival's higher bar).
  Crucially, the **primary collapse criterion is within-arm** (disjunctive vs its *own* Arm-2 clear
  controls, same register), so the register residual does **not** touch it; it only weakly affects
  the secondary cross-arm survival leg.

## 4. The frozen reading rule (survival vs collapse, gate Q3)

Encoded in [`analyze.py`](within-lexical-scalar-vs-disjunctive-v1/analyze.py); per model:

- **C1** — the categorical **decline rate** (%UNCLEAR) on the disjunctive class, **not**
  confidence, is load-bearing.
- **C3** — an arm is interpretable only if its clear controls show decline < 0.20 **and** mean
  confidence > 70; a failing arm collapses to weak / `internal-contrast-only` and gives no verdict.
- **COLLAPSE** (within-arm; robust to the register residual): the disjunctive within-arm
  decline-gap CI (disjunctive − its clear controls) has **lower bound > 0**.
- **SURVIVAL** (higher bar; both legs): the disjunctive within-arm gap CI lower bound is **not** > 0
  **and** the cross-arm gap CI (disjunctive − scalar bridging) **includes 0** **and** the
  disjunctive decline is **near-zero** (≤ 0.10).
- **MIXED/INCONCLUSIVE**: anything else.

Clustered bootstrap (10000 reps, seed 20260623; clusters: lemma for scalar, homonym surface for
disjunctive). Direction-of-effect only; small clustered N → wide CIs, no coverage claim. The
named anti-cheat violation — **re-selecting the disjunctive class against model confidence** — is
foreclosed by the sha256 freeze of `items_arm2.json` + the threshold **before** any output.

### Pre-run critic GO + the pre-registered clean-8 subset (2026-06-23)

A fresh independent pre-run critic returned **GO** (result-neutral; the freeze verified
byte-for-byte). It judged **8/12** disjunctive balanced contexts genuinely two-way and flagged
**4 as leaning** toward one sense: **mole** (→ spy), **punch** (→ drink), **club** (→
heirloom-stick) — mild/moderate — and **pupil** (→ student) — strong. Its load-bearing
observation: because each balanced `ctx1` is paired with a sense-fixed `ctx2`, a lean in *either*
direction suppresses `UNCLEAR` (a sense-A lean → confident SAME; a sense-B lean → confident
DIFFERENT) and so **biases toward survival** — leaning items erode the *collapse* signal, they do
not pad collapse. Per the gate, a handful of mildly-leaning items are carried as a **disclosed
limit** (8 clean remain), and `analyze.py` reports the within-arm collapse statistic on **both
all-12 and a pre-registered clean-8 subset** (`CLEAN_SUBSET` = {bank, crane, file, organ, trunk,
tank, plot, ring}). This subset is a **fixed linguistic partition declared before any model
output** (not a post-hoc re-selection against model confidence; `items_arm2.json` is unchanged).
The result must disclose the four leaning items, their direction, and that the lean cuts toward
survival.

## 5. Anchor posture (Q4) and claim scope

**No human-comparison claim for the disjunctive arm.** Arm 1 keeps its inherited usage-similarity
cap (a DWUG midpoint is a usage-similarity midpoint, **not** a certified sense bridge). Arm 2 is
**`internal-contrast-only`** (Q2-b: author-stipulated balanced homonyms; no in-repo resource
certifies homonym sense co-presence). Any unified within-lexical statement is floored at
`internal-contrast-only` for the disjunctive arm (weakest-common-strength). **No anchor invented.**
Behavioural, not representational; n=3 commercial 2026 models.

## 6. Cost and run discipline

One temp-0 call per item per model. 84 items (48 scalar + 36 disjunctive) × 3 = **252
finding-bearing calls** + 3 liveness. Pre-flight ≈ **$0.10–0.25** (same shape as the cross-level
run: $0.207 for 444 calls); `ABORT_USD = 0.60`; gemini `effort: minimal`. The run is gated on a
fresh independent pre-run critic GO/NO-GO against the frozen instrument and a budget pre-flight.

## 7. Scope and limits (lead with these)

- **No human comparison** (Q4): scalar capped to usage-similarity; disjunctive `internal-contrast-only`.
- **Register residual** (§3): the irreducible Arm-1-vs-Arm-2 corpus-vs-author difference; cuts
  toward survival; the primary collapse criterion is within-arm and immune to it.
- **Scalar-flavoured decline gloss** (§1): inherited verbatim, a constant across arms, biases
  toward survival → survival's higher bar.
- **Author-judged balance.** `certify.py` checks structure/balance/leak/nuisance-match, **not**
  human-rated disjunctiveness; the balance of each homonym context is author-stipulated and
  vetted by the independent pre-run critic, frozen before any output; `internal-contrast-only`
  bounds the claim.
- **Small, clustered N** (12 homonyms / 24 bridging lemmas-pairs): direction-of-effect, wide CIs.
- **A within-model contrast is not a human fact**; the result reads only what *these* models do.
