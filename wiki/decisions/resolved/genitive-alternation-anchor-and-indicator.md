---
id: genitive-alternation-anchor-and-indicator
title: How to operationalize the genitive-alternation animacy probe — focal constraint, logprob-free indicator + shadow control, and anchor posture?
status: resolved
opened: 2026-07-13
opened-by: autonomous (session 217, opening the A5 genitive sibling)
resolved: 2026-07-13
resolved-by: autonomous (adversarial review)
resolution: "ADOPT DEFAULTS — Q1-A (possessor animacy) / Q2-(i) (graded forced-choice + BOTH shadow controls: the rare/nonce-possessor arm as the shortcut-immune PRIMARY control and the frozen possessor-lemma marginal genitive-propensity covariate as corroboration; length+sibilancy+definiteness matched, A/B counterbalanced, collective mid-level) / Q3 human-anchored on the DIRECTION only (per-item gradient deferred to a license-verified scout). Ratified s218 by a fresh-agent adversarial reviewer (verdict authority, independent of the s218 downstream freeze/run) that WEIGHED a non-Anthropic decorrelation vote (gpt-5.4-mini, $0.002129): CONVERGENT on the yardstick — the fresh reviewer ADOPT-DEFAULTS, the vote ADOPT-WITH-MODIFICATION (agreeing Q1 animacy is the right hard target and Q3 direction-only is honest, adding that the control is risk-reducing CORROBORATION, not a definitive shadow-defeat). The critic's B1–B3 (nonce=rare/nonce possessors not novel pairings; ONE sha'd marginal-propensity covariate; ex-ante CONFIRM-vs-SHADOW independence rule) were judged sound and sufficient to close the marginal-frequency channel. Five residual freeze conditions carried to the run: R1 nonce-arm animacy conveyed by gloss not orthography, string forms neutralized across arms; R2 report the covariate's OWN predictive validity — if too weak to absorb collinear variance, CONFIRM rests on the nonce arm and the covariate leg is weak corroboration; R3 power the load-bearing nonce arm (≥20 paired-contrast frames or justify) toward the §4 floor; R4 B1–B3 + S1–S7 + (vi) 'no gradient-match prose' stay binding; R5 (from the vote) frame CONFIRM narrowly directional — no 'distributional shadow defeated' overclaim. Tom's standing override outranks this autonomous ratification."
anchor: human-anchored (Dubois et al. 2023 native-speaker animacy direction; per-item gradient a queued upgrade only)
---

> **RESOLVED — session 218 (2026-07-13), autonomous cross-session adversarial review. ADOPT DEFAULTS
> (Q1-A / Q2-(i) / Q3 human-anchored on the direction).** A fresh-agent adversarial ratification
> reviewer (verdict authority, independent of the s218 freeze/run) **weighed** a non-Anthropic
> decorrelation vote (`gpt-5.4-mini`, $0.002129) — convergent on the yardstick (fresh reviewer
> ADOPT-DEFAULTS; vote ADOPT-WITH-MODIFICATION, agreeing on Q1/Q3 and adding that the shadow control is
> corroboratory, not a definitive shadow-defeat). The s217 pre-run critic's B1–B3 were judged sound and
> sufficient to close the marginal-frequency channel. **Five residual freeze conditions R1–R5** (nonce
> animacy by gloss not orthography + neutralized string forms; report covariate predictive validity /
> CONFIRM rests on the nonce arm; power the nonce arm; B1–B3 + S1–S7 stay binding; CONFIRM stays
> narrowly directional — no "shadow defeated") were carried to the run and honored at the s218 freeze
> ([`PREREG.md`](../../../experiments/runs/2026-07-13-genitive-alternation-animacy/PREREG.md)). The
> design [`design/genitive-alternation-animacy-v1`](../../../experiments/designs/genitive-alternation-animacy-v1.md)
> and conjecture [`conjecture/genitive-alternation-animacy`](../../findings/conjectures/genitive-alternation-animacy.md)
> are promoted out of contingent status. **No probe ran in the opening session (s217); the freeze + run
> are s218**, honoring the anti-cheat separation. Full options + the pre-run-critic record below.

# Decision: anchor + indicator + shadow control for the genitive-animacy probe

## Why this exists

Program A5 (the production-side alternation battery) extends the best-designed result — the dative
information-structure line ([`claim/dative-information-structure-givenness`](../../findings/claims/dative-information-structure-givenness.md))
— to a **second sibling** anchored to a published human direction. The chosen sibling is the **English
genitive alternation** (s-genitive *the judge's decision* vs of-genitive *the decision of the court*),
whose strongest constraint is **possessor animacy** (animate → s-genitive), a *semantic/referential*
driver distinct from the dative's discourse-structural givenness. The human anchor is now in-repo as
[`resource/genitive-animacy-human-anchor`](../../base/resources/genitive-animacy-human-anchor.md)
(Dubois et al. 2023, 25 native-speaker acceptability ratings, CC BY 4.0). But *how* the probe is run
turns on value-laden choices a session must not auto-take (CLAUDE.md rule 5). They interlock, so they
are surfaced together.

The genitive differs from the dative in one design-critical way: **animacy is a lexical property of the
possessor**, so it cannot be moved into the discourse context while keeping the two scored phrasings
byte-identical (the way the dative moved givenness into context). The two phrasings a genitive item
scores differ in the possessor word across animacy conditions. That makes the **surface-frequency
shadow** the load-bearing worry here (Q2 below), the analog of the dative's length↔givenness
dissociation.

## The three sub-questions

### Q1 — Focal constraint (and sibling)

- **Option A (provisional default): possessor animacy on the genitive.** The strongest, best-human-rated
  constraint (Dubois et al. 2023; Rosenbach 2014), with a clean native-speaker acceptability direction.
- **Option B: a different genitive constraint** — end-weight (longer possessor → of-genitive) or
  givenness. Weight is real but is a *processing/length* effect that overlaps the confounds a clean
  design must neutralize; givenness of the possessor has weaker/contested corpus support. Lower value
  as a *first* row.
- **Option C: a different sibling** — verb-particle placement (*pick up the book* / *pick the book up*)
  or the locative/spray-load alternation. Both are viable A5 rows but lack an equally clean, in-repo,
  CC-licensed native-speaker rating anchor right now; hold them as later rows.

### Q2 — Indicator + the shadow control (the crux)

**Indicator.** Logprob/surprisal is unavailable under pure autonomy (the AANN blocker), so a behavioural
indicator is required.

- **Option (i) (provisional default): graded forced-choice.** Given a possessive proposition with the
  possessum held fixed, the model distributes 100 points by naturalness between the s-genitive and
  of-genitive phrasings; s-pref = s_points/(s_points+of_points). Mirrors the project's validated,
  shortcut-certified dative instrument and the Dubois midpoint-50 rating shape → like-for-like human
  comparison. Within-item measure: shift = mean(s-pref | animate possessor) − mean(s-pref | inanimate).
- **Option (ii): separate single-variant acceptability rating** (rate each variant 0–100 independently),
  closer to Dubois' own task but yielding no direct within-item preference contrast. A sensitivity check.

**The shadow control (load-bearing — this is what a session could cheat on by item selection).** Because
the scored phrasings vary lexically with animacy, an animate→s-genitive shift could be a shadow of the
higher corpus frequency of animate-possessor s-genitive strings. The design must certify the shift is
**not reconstructable from surface frequency alone**. Provisional default = **both**:

1. A **frozen possessor-lemma marginal genitive-propensity covariate** — the possessor lemma's marginal
   s-genitive-vs-of-genitive frequency (**one** exact sha'd recipe, no "and/or"), derived from a
   license-verified corpus (UD English-EWT, CC BY-SA, in-scope; or the Simple-English-Wikipedia dump used
   s186, CC BY-SA), frozen before any call. `analyze.py` partials **that** quantity out of the animacy
   shift. *(Corrected by the s217 pre-run critic, B2: joint possessor↔possessum co-occurrence controls
   the channel that is **not** the likely shadow; the marginal `P(takes-'s | possessor)` propensity —
   animate nouns take 's more regardless of possessum — is the collinear-with-animacy channel that must
   be partialled out. Power bounded by corpus size — corroboration arm.)*
2. An **atypical arm of rare / nonce possessor lemmas** (the PRIMARY shortcut control): a subset pairs
   each animacy level with **rare or nonce possessor lemmas** (matched animate vs inanimate for length +
   sibilancy), so the model has **no per-lemma genitive statistic to read off** and must generalize from
   the animacy *category*. *(Corrected by the s217 pre-run critic, B1: novel possessor↔possessum
   **pairings** on common possessors break only the bigram channel and leave the marginal
   possessor-propensity channel — the likely shadow — intact, so a no-animacy surface reader scores a
   spurious CONFIRM on them; only rare/nonce **possessors** break that channel.)*

Plus a **pre-registered CONFIRM-vs-SHADOW independence rule** (critic B3): the animacy CI with the
marginal covariate included still excludes zero (≥2/3) **AND** the rare/nonce atypical-arm shift CI
lower bound > 0 (≥2/3), else SHADOW — the adjudication fixed ex ante, not after seeing outputs.

Plus the standard guards: possessor **length** and **final sibilancy** matched across animacy conditions;
A/B counterbalancing (s-gen = option A and = option B) with a target-blind parser; a **neutral/collective**
mid-level to show the shift moves around the model's own default in both directions.

### Q3 — Anchor posture + what the result may claim

- **Provisional default: human-anchored** (NOT `internal-contrast-only`). The direction tested
  (animate → s-genitive) is a native-speaker acceptability fact from Dubois et al. (2023), so the result
  may make a calibrated **human-comparison** claim (does the panel's animacy-driven genitive preference
  shift in the human-rated direction). The **per-item human gradient** (per-item ratings or the TLC
  production surface) is a **secondary** measure, contingent on a separate license-verified dataset scout
  (TLC is a controlled corpus; not adopted now) — mirroring the dative's corpus-primary / ratings-upgrade
  resolution.
- **May NOT:** claim human-*level* genitive competence; claim the effect beats the distributional shadow
  unless the frozen frequency control / atypical arm clears it; lift attested example sentences (use
  synthetic minimal pairs built to the animacy scheme).

## What the reviewer should weigh

1. Is possessor animacy the right *first* focal constraint (Option A), or does end-weight give a cleaner
   first calibrated row (Q1)?
2. Is the graded-forced-choice indicator (Option i) the honest match for a native-speaker *rating*
   anchor, or should the separate-rating (Option ii) be primary since it mirrors Dubois' actual task?
3. **Is the shadow control specified tightly enough to bind the build?** Specifically: is the
   typical-vs-atypical split the correct primary shortcut control (as for the CC), and are the corpus
   covariate's power limits stated honestly rather than hidden? This is the chief cheat-surface.
4. Is "human-anchored on the direction, per-item gradient deferred" the right posture (Q3), or does the
   absence of an openly-licensed per-item genitive gradient push this toward a weaker human-comparison
   claim than the dative's (which had a fittable corpus)?

## Provisional default (to be adopted, modified, or rejected next session)

**Q1-A** (possessor animacy) / **Q2-(i)** graded forced-choice with **both** the frozen surface-frequency
covariate **and** the typical-vs-atypical split as controls, length+sibilancy matched, A/B
counterbalanced, collective mid-level reported / **Q3** human-anchored (direction), per-item gradient a
queued license-verified upgrade only.

## Anti-cheat note

Ratifying fixes the **yardstick** (focal constraint, indicator, shadow control, anchor posture), never
the **result**. The probe must not be run, nor the item set / control retuned, in the session that
ratifies; a pre-run-critic NO-GO on the shadow control **defers** the run rather than relaxing the
control. A null (no animacy shift, or a shift fully explained by surface frequency) is a first-class
result.
