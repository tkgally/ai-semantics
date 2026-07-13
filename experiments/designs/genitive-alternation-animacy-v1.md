---
type: design
id: genitive-alternation-animacy-v1
title: "Genitive-alternation possessor-animacy probe (A5) — does the panel's s-genitive/of-genitive preference shift in the human-rated animacy direction, and does it survive a surface-frequency shadow control? PROVISIONAL (contingent on the open decision)"
meaning-senses:
  - constructional
  - inferential
  - distributional
status: draft
anchor: human-anchored
contingent-on:
  - genitive-alternation-anchor-and-indicator
created: 2026-07-13
updated: 2026-07-13
links:
  - rel: operationalizes
    target: conjecture/genitive-alternation-animacy
  - rel: depends-on
    target: resource/genitive-animacy-human-anchor
  - rel: depends-on
    target: source/dubois-2023-genitive-animacy
  - rel: depends-on
    target: result/dative-information-structure-powered
  - rel: anchors
    target: resource/genitive-animacy-human-anchor
---

# Design v1 — genitive-alternation possessor-animacy probe (program A5)

**Status:** PROVISIONAL — contingent on
[`decisions/open/genitive-alternation-anchor-and-indicator`](../../wiki/decisions/open/genitive-alternation-anchor-and-indicator.md)
(opened s217; ratifiable at the earliest s218). **Nothing is frozen and nothing runs before
ratification.** This page carries the design; the freeze (item sha + frequency-control sha), the PREREG,
and the run record follow in the run session, mirroring the dative
([`result/dative-information-structure-v1`](../../wiki/findings/results/dative-information-structure-v1.md))
and German-CC ([`design/comparative-correlative-german-v1`](comparative-correlative-german-v1.md))
patterns.

## The question (one sentence)

The dative line showed the panel tracks a *discourse-structural* soft constraint (givenness) in the
human production direction; this design tests whether the panel tracks a *semantic/referential* soft
constraint — **possessor animacy** on the **genitive alternation** (animate possessor → s-genitive; the
strongest genitive constraint per Dubois et al. 2023 / Rosenbach 2014) — in the **human-rated
acceptability direction**, and crucially whether that animacy shift **survives a surface-frequency
shadow control** or is merely the model reading off which genitive string it has seen more often.

## The instrument (port of the validated dative graded-forced-choice, Q2-(i))

Given a possessive proposition with the **possessum held fixed**, the model distributes **100 points**
by naturalness between the two phrasings of the *same* proposition:

- **s-genitive:** *the judge's decision* (possessor first)
- **of-genitive:** *the decision of the judge* (possessum first)

s-pref = s_points / (s_points + of_points) ∈ [0,1]. The s-gen↔A/B mapping is **counterbalanced** (every
item run with s-gen = option A and s-gen = option B) and the parser is **target-blind** (keys on reply
position, not on which option is the s-genitive). Same panel ([`config/models.md`](../../config/models.md)),
temperature 0, graded `FINAL:` line, cluster-bootstrap-over-items intervals — all inherited byte-parallel
in shape from the frozen dative/CC instruments.

## The within-item design (where the animacy manipulation lives)

Unlike the dative — where givenness lived in the discourse context and the two scored phrasings were
byte-identical — **animacy is a lexical property of the possessor**, so the manipulation is the
**possessor NP** itself, with the **possessum and syntactic frame held fixed**. One *frame* = a fixed
possessum crossed with possessors at ≥2 animacy levels:

| Frame (fixed possessum) | animate possessor | (collective) | inanimate possessor |
|---|---|---|---|
| `___ decision` | the judge's decision / the decision of the judge | the panel's / of the panel | the statute's decision / the decision of the statute |
| `___ surface` | the diver's surface / the surface of the diver | — | the lake's surface / the surface of the lake |

The finding-bearing measure is the within-frame **shift**:

> shift(frame) = mean(s-pref | animate possessor) − mean(s-pref | inanimate possessor)

Human direction ⇒ shift > 0 (animate possessor pulls preference toward the s-genitive). A
**collective / mid-animacy** level is included where feasible so the shift is shown to move around the
model's own default in both directions (the neutral-baseline logic of the dative), not a one-sided
ceiling artifact.

**Matched confounds (freeze conditions).** Across an frame's animacy conditions, the possessor NPs are
matched for **word length** and **final sibilancy** (a possessor ending in a sibilant independently
disfavours the s-genitive — Dubois et al. name sibilancy and length as separate constraints); the
possessum, determiner, and frame are byte-identical. So a length-only / sibilancy-only / position-only /
always-s / always-of reader yields **shift = 0** by construction — to be certified at build the way the
dative certified its eight shortcut readers.

## The load-bearing shadow control (Q2 crux — hardened by the s217 pre-run critic)

Because the scored phrasings differ lexically across animacy conditions, a positive shift could be a
shadow of surface frequency. **The s217 pre-run critic identified the decisive channel (BLOCKER B1):**
a model with **no animacy representation** that has merely learned the possessor lemma's *marginal*
s-genitive propensity — `P(takes-'s | possessor)`, a pure lexical-selectional statistic, since animate
nouns take the possessive 's far more than inanimate nouns **regardless of possessum** — produces a
**positive shift on the atypical arm too**. Novel possessor↔possessum *pairings* that merely reuse
common possessors break only the joint/bigram channel, leaving this **marginal** channel (which *is*
"which genitive string it has seen more often") fully intact and collinear with animacy. So the naive
atypical split is **not** shortcut-immune. Two corrected controls (the critic's B1/B2 applied):

1. **Atypical arm = rare / nonce possessor lemmas (PRIMARY, corrected).** The atypical subset pairs
   each animacy level with **rare or nonce possessor lemmas** (matched animate vs inanimate for length
   + final sibilancy), **not** merely novel possessum pairings on common possessors. Only rare/nonce
   possessors break the marginal `P(takes-'s | possessor)` channel — a model then has no per-lemma
   genitive statistic to read off and must generalize from the animacy *category*. If the
   animate→s-genitive direction holds on this arm, it is animacy-driven, not marginal-frequency-driven.
2. **Frozen covariate = possessor-lemma MARGINAL genitive propensity (one exact recipe, corrected).**
   The critic's B2: freeze **one** exact covariate recipe in a named, sha'd build script (the CC
   `build_cooc_de.py` discipline — no "and/or", which is itself a cheat-surface). The load-bearing
   covariate is the **possessor-lemma marginal s-genitive-vs-of-genitive frequency** (not joint
   co-occurrence, which controls the channel that is *not* the likely shadow), derived from a
   license-verified corpus (**UD English-EWT**, CC BY-SA, in-scope; or the Simple-English-Wikipedia
   dump used s186, CC BY-SA) and frozen before any call. `analyze.py` partials **that** quantity out of
   the animacy shift. Power is bounded by corpus size — stated honestly.

**Pre-registered independence rule (B3 — fix the adjudication ex ante, the single most gameable
branch).** CONFIRM-vs-SHADOW must not be a post-hoc judgment call. Register before freeze: the animacy
effect's bootstrap CI, in a model that **includes the marginal-frequency covariate**, still excludes
zero (≥2/3 models), **AND** the rare/nonce-possessor atypical-arm shift CI lower bound > 0 (≥2/3). If
the animacy coefficient collapses once the marginal covariate is included, or the atypical arm does not
clear zero, the verdict is SHADOW.

## Primary quantities + 95% CIs (cluster bootstrap over frames)

**(1)** within-frame animacy shift (s-pref animate − s-pref inanimate), pp; **(2)** fraction of frames
with shift > 0; **(3)** graded-scale monotonicity across animate > collective > inanimate (prediction 2);
**(4)** animacy shift **on the atypical subset** (the shortcut-immune primary); **(5)** animacy-shift
residual over the frozen surface-frequency covariate (corroboration); plus per-model s-pref by animacy
level. Deliverable = point estimate + CI, not a threshold pass.

## Verdict frame (pre-registered, symmetric — a null is first-class)

- **CONFIRM (human-direction):** shift > 0 with bootstrap lower bound > 0 in ≥2/3 models, **AND** the
  pre-registered independence rule holds (animacy CI excludes zero with the marginal-frequency covariate
  included, ≥2/3; **AND** the rare/nonce-possessor atypical-arm shift CI lower bound > 0, ≥2/3) → a
  human-anchored production-side animacy positive; a genitive row for the shadow-depth table.
- **SHADOW / ATTENUATED:** a positive shift whose animacy coefficient **collapses once the marginal
  possessor-propensity covariate is included**, or that **does not clear zero on the rare/nonce-possessor
  atypical arm** → a distributional shadow of possessor genitive-propensity, not animacy tracking;
  recorded as such (a first-class negative for the shadow-depth reading).
- **WEAK:** shift > 0 but not graded across animacy levels (prediction 2 fails).
- **FALSIFY / REVERSAL:** no animate→s-genitive shift under the controlled manipulation, or a reversal
  → the English claim's animacy generality is contested; investigate item authoring, do **not** retune.

## What this run may / may NOT claim

- **May:** a **within-model, human-direction** claim that the panel's genitive preference does / does not
  shift toward the s-genitive for animate possessors, with magnitudes + intervals, and whether that
  survives the surface-frequency shadow control.
- **May NOT:** any claim of **human-level** genitive competence; any claim of beating the distributional
  shadow if the atypical arm / covariate does not clear it; any per-item human-gradient claim (no
  openly-licensed per-item genitive gradient in-repo — deferred to a scout).

## N and power (PROTOCOL §4) — stated in bootstrap (frame) units, per critic S3

The bootstrap resampling unit is the **frame** (a fixed possessum), not the trial. Target **≥40 frames**
with the atypical arm raised to a **near-50/50 split (≥20 rare/nonce-possessor frames)** per critic S2
(the atypical arm is the primary shortcut control and carries the CONFIRM, so it cannot be under-powered
at ~13 frames — the dative's 12-item control arm is exactly where gpt failed to replicate). Each frame is
run at ≥2 animacy levels × A/B counterbalance; **N is reported and powered in frames**, and the trial
count (~160–200/model) is *not* presented as independent-item N (critic S3 — A/B and animacy levels are
not independent items). Exact frame count fixed at freeze; stated with rationale in PREREG.

## Freeze conditions (to honor at the run session, after ratification — critic B1–B3 + S1–S7 folded)

- **(i)** items + the single frozen covariate recipe authored + **frozen (sha256) before running** in a
  named sha'd build script (no "and/or" covariate — critic B2); `probe.py full` refuses unless the exact
  shas are in PREREG (the dative/CC discipline).
- **(ii)** possessor length + final sibilancy **+ definiteness** matched across animacy conditions;
  possessum/frame + determiner byte-identical; **bare proper-name possessors excluded** (or article
  parallelism enforced) so animacy is not confounded with article-presence (critic S1 — Zaenen "animate"
  includes bare proper names like *god's plan*); shortcut-reader certification
  (length/sibilancy/position/always-s/always-of → shift 0), **stated to NOT cover the frequency reader**
  (critic S4 — the marginal-frequency reader is killed by the covariate + nonce arm, not by construction).
- **(iii)** the **corrected** shadow control: atypical arm = **rare/nonce possessor lemmas** (critic B1),
  the frozen covariate = **possessor-lemma marginal genitive propensity** (critic B2), and the
  **pre-registered independence rule** (critic B3) — all above. Atypical possessor–possessum co-occurrence
  (and possessor rarity) **verified empirically against the frozen corpus at build**, not asserted by
  authorship (critic S6, the CC-atypical discipline).
- **(iv)** powered N in **frames** (§4, critic S3); pre-flight estimate + post-run actual in [`config/budget.md`](../../config/budget.md).
- **(v)** what each outcome may / may not claim — stated above; falsify/shadow arms live, no retuning; a
  pre-run-critic NO-GO on the shadow control **defers** the run, never relaxes the control.
- **(vi)** result posture `human-anchored` on the **direction only**, anchored to
  [`resource/genitive-animacy-human-anchor`](../../wiki/base/resources/genitive-animacy-human-anchor.md);
  the "May NOT: any per-item human-gradient claim" fence stays hard (critic Q3) and CONFIRM prose must
  not imply gradient-matching; per-item gradient deferred to a license-verified scout.
- **(vii)** a **minimum collective-level frame count committed** (critic S7) so the graded animate >
  collective > inanimate test (prediction 2) and the WEAK verdict are cleanly adjudicable, not optional.
- **(viii)** a cheap **separate-rating sensitivity check** (Option ii — rate each variant 0–100
  independently) registered alongside the forced-choice primary (critic S5): it is Dubois' *actual* task,
  so a convergent direction on it strengthens the human anchor.
- **(ix)** lead-agent self-audit of every synthetic item against the animacy scheme (Zaenen et al.
  five levels via Dubois et al.) — the no-human-subjects substitute for a human auditor; no attested
  example sentences lifted (contamination guard).

## Budget (pre-flight, for the run session)

~2 arms (FC + counterbalance already folded) × ~180 items × 3 models ≈ **~540–1,080 calls**. No
metalanguage-competence smoke test needed (the task is in English). At observed dative/CC prices
(~$0.30 for ~800 forced-choice calls) ≈ **$0.20–0.45** billed — well under the $2.50 single-run flag
and the $5/day cap. Actuals from the returned `usage.cost`.

## Pre-run critic (this design session, s217)

An independent fresh-agent pre-run critic (verdict authority) + one non-Anthropic decorrelation vote
reviewed this design's operationalization and the open decision's provisional defaults. This is QA input
to the next-session ratification, not a substitute for it.

**Fresh-agent critic → GO-WITH-CONDITIONS.** Converged on Q1/Q2/Q3; confirmed the Dubois quotes are used
correctly (native-speaker *direction* only; learner deviations correctly excluded; Zaenen/Rosenbach
attributions accurate) and the verdict frame is symmetric and the budget trivial. But it caught a
**load-bearing hole** now applied above as BLOCKERS:

- **B1 (applied)** — the naive atypical arm (novel possessor↔possessum *pairings* on common possessors)
  does **not** break the **possessor-marginal s-genitive propensity** channel (`P(takes-'s | possessor)`,
  collinear with animacy), so a no-animacy surface reader scores CONFIRM on it too. **Fixed:** the
  atypical arm now uses **rare/nonce possessor lemmas** (the *Shadow control* section).
- **B2 (applied)** — the "and/or" covariate was itself a cheat-surface. **Fixed:** one exact sha'd
  covariate recipe = **possessor-lemma marginal genitive propensity** (not joint co-occurrence).
- **B3 (applied)** — no pre-registered CONFIRM-vs-SHADOW rule. **Fixed:** the independence rule is now
  registered ex ante (animacy CI with the marginal covariate included; rare/nonce atypical-arm CI).
- **SHOULD-FIX S1–S7 (folded into the freeze conditions + N section):** add definiteness + exclude bare
  proper-name possessors (S1); raise the atypical arm to ≥20 frames / ~50-50 (S2); report N in frame
  units (S3); state the shortcut-cert does not cover the frequency reader (S4); soften the
  shape-match rhetoric + register the separate-rating sensitivity check (S5, S8/(viii)); verify atypical
  co-occurrence/rarity empirically at build (S6); commit a minimum collective-level frame count (S7).
- **Q1 caveat recorded:** animacy is the strongest/best-anchored constraint (right for *value*) but also
  the constraint **most collinear with surface frequency** — hence the hardest to separate from the
  shadow. The critic still converges on Q1-A precisely because the shadow residual is the probe's whole
  point, *conditional on* B1/B2 closing the marginal channel. That trade-off is recorded here explicitly.

**Non-Anthropic decorrelation vote** (`gpt-5.4-mini`, $0.002661, cutoff-aware preamble) → **GO-WITH-
CONDITIONS**, convergent: it independently flagged "novel ≠ frequency-free" (the B1 channel — possessor
lexical class / world-knowledge / plausibility), urged a **precommitted/locked item-selection rule** with
explicit novelty + semantic-plausibility matching for the atypical set, calibration checks on the
100-point scale-use, and anchoring only the **sign** (not human-like magnitude/ranking). All folded into
the freeze conditions above.

**Net:** the design is ratifiable + freezable next session **once B1–B3 are honored at the freeze** (they
are written into the shadow-control section and freeze conditions this session, mirroring the A1a s172
pattern of applying blockers to the design and carrying them to the freezing session). A pre-run-critic
NO-GO on the shadow control **defers** the run, never relaxes the control.
