---
type: conjecture
id: particle-placement-givenness
title: LLMs track the object-givenness constraint on the English verb-particle placement alternation
meaning-senses:
  - constructional
  - inferential
  - distributional
status: tested
contingent-on: []
created: 2026-07-14
updated: 2026-07-14
links:
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: depends-on
    target: resource/particle-placement-givenness-human-anchor
  - rel: depends-on
    target: source/kim-2016-particle-placement
  - rel: supports
    target: claim/dative-information-structure-givenness
---

> **Proposed 2026-07-14 (session 224).** The **third sibling** of the program A5 production-side
> alternation battery — extending the dative
> ([`claim/dative-information-structure-givenness`](../claims/dative-information-structure-givenness.md),
> a discourse-structural givenness constraint) and the genitive
> ([`claim/genitive-alternation-animacy`](../claims/genitive-alternation-animacy.md), a semantic
> constraint) to the **verb-particle placement** alternation, with a **license-verified human-direction
> anchor** ([`resource/particle-placement-givenness-human-anchor`](../../base/resources/particle-placement-givenness-human-anchor.md);
> Kim et al. 2016, CC BY 4.0). The operationalization decision
> [`decisions/resolved/particle-placement-anchor-and-indicator`](../../decisions/resolved/particle-placement-anchor-and-indicator.md)
> (Q1 focal constraint / Q2 indicator + shadow control / Q3 anchor posture) was **ratified s225**
> (ADOPT-WITH-MODIFICATION, binding conditions R1–R7); the design
> [`design/particle-placement-givenness-v1`](../../../experiments/designs/particle-placement-givenness-v1.md)
> was **frozen + run s225** (the genitive s217→s218 pattern; no probe ran in the opening session s224).

# Conjecture: LLMs track the object-givenness constraint on verb-particle placement

## Statement

The English verb-particle (particle-placement) alternation — the **joined** order *picked up the book*
(V-Prt-DO) vs the **split** order *picked the book up* (V-DO-Prt) — is constrained by the **information
status (givenness / definiteness) of the direct object**: a **discourse-given / definite** object favours
the **split** order (object placed earlier, between verb and particle), an **indefinite / new** object
favours the **joined** order (Kim et al. 2016 / Gries 1999, native-speaker direction). The conjecture:
production-style particle-placement preferences in current panel LLMs are sensitive to this object-
givenness constraint **in the human direction**, and the sensitivity is not merely a shadow of the higher
surface frequency of definite-object split-order strings.

## Why this is interesting

Particle placement is the **third** flagship English production alternation, and it turns on the **same
information-structural driver as the dative** (givenness: given/accessible material placed earlier) — but
on a wholly different construction. A third human-anchored row lets the battery test whether "the panel
tracks the soft information-structural constraint in the human direction" **generalizes across
constructions**, or is specific to the dative's ditransitive frame. It is also the **cleanest** sibling on
the shadow axis: unlike the genitive (where animacy is lexical to the possessor, so the two scored strings
differ lexically), object givenness can be moved into the **discourse context** while the two scored
particle-placement strings stay **byte-identical** — so a load-bearing **shortcut-immune firewall** (any
preference shift on byte-identical scored strings *must* come from integrating the discourse context, not
from any scored-string statistic) is available by construction, tighter than the genitive's nonce firewall.
The sharpest form: **does the givenness shift survive when the object string is byte-identical and only the
discourse context varies**, or is definite→split just the model reading off which order-string it has seen
more often?

## Predictions

*(Provisional pending ratification of the open decision, which fixes the focal constraint, indicator, and
shadow control. Symmetric — a null is first-class.)*

1. **Definiteness arm (anchor-exact).** In a graded forced-choice production-preference probe (distribute
   100 points by naturalness between the joined and split orderings of the *same* verb-particle-object
   proposition, verb + particle + head-noun held fixed), the panel prefers the **split** order more for a
   **definite** object (*the box*) than an **indefinite** object (*a box*) — the human direction — object
   length, type, concreteness, animacy, and VP idiomaticity held constant.
2. **Discourse-givenness firewall (shortcut-immune, load-bearing; three-condition).** With the object
   string held **byte-identical** (*the box* in every condition) and information status manipulated only in
   the **preceding discourse context**, the panel prefers the **split** order more when the object is
   **discourse-given** than when it is **mentioned-but-referentially-new** (the decisive GIVEN vs
   NEW-MENTIONED contrast). Because the two scored strings are byte-identical, any string-frequency /
   collocation reader yields shift = 0 by construction; and because NEW-MENTIONED holds the object noun's
   lexical priming/recency constant with GIVEN, a positive GIVEN − NEW-MENTIONED shift is **referential
   information structure**, not mere lexical-recency priming (s224 critic B-crit-1). A third bare-NEW
   (unmentioned) condition is reported descriptively.
3. **Convergent length leg.** The panel also prefers the **split** order more for a **short** object than a
   **long** one (the second named human direction) — corroboration that the panel tracks the construction's
   soft constraints, not one arm's confound.
4. Effect size decorrelates across models in a way that need not track overall benchmark performance
   (the dative / genitive / CC pattern: a concordant panel direction can hide a wide magnitude spread).

## What would confirm / falsify

- **Confirm (human-direction, primary):** the **byte-identical discourse-givenness firewall** shift
  (GIVEN − NEW-MENTIONED) clears zero in ≥2/3 models — the decisive shortcut-immune leg — **AND** the
  anchor-exact definiteness shift is directionally consistent (human direction). → a human-anchored
  production-side information-structure positive; a particle-placement row for the shadow-depth table, and
  cross-construction generalization of the dative's givenness effect.
- **Shadow / attenuated:** a positive definiteness shift exists but the **firewall shift (GIVEN −
  NEW-MENTIONED) does not clear zero** (≥2/3) → the definiteness effect is a distributional/lexical shadow
  (surface-string frequency or object-noun lexical-recency priming), not information-structure tracking;
  recorded as such (a first-class negative for the shadow-depth reading).
- **Weak:** a definiteness shift exists but the convergent length leg fails (prediction 3), or the effect
  does not generalize beyond one arm.
- **Falsify:** no definite→split shift under the controlled manipulation, or a reversal → the cross-
  construction generality of the information-structural effect is contested; investigate item authoring,
  do **not** retune.

> **→ TESTED 2026-07-14 (s225 freeze + claude arm; s226 completion) — CONFIRM (primary clause met).**
> [`result/particle-placement-givenness-v1`](../results/particle-placement-givenness-v1.md): the
> byte-identical discourse-givenness firewall (GIVEN − NEW-MENTIONED) clears zero in **2/3** models
> (claude +0.040, gemini +0.072) and the definiteness arm is directionally consistent 3/3 (0 reversals) —
> the pre-registered primary Confirm clause. **gpt returns the pre-named SHADOW branch** (definite→split
> +0.100 but firewall +0.018, CI includes 0) — a first-class negative for the third model. The referential
> firewall effect is small relative to the strongly-tracked end-weight/length constraint (+0.29–0.40, 3/3);
> CONFIRM rests on the firewall (covariate near-vacuous). Direction-only, restatement-anchored; a single
> run (no `claim` yet — fresh-item replication is the successor). predictions.md bet **fired-for**.

## Human anchor

[`resource/particle-placement-givenness-human-anchor`](../../base/resources/particle-placement-givenness-human-anchor.md)
— the native-speaker direction (definite/given object → split order) from Kim et al. (2016) / Gries
(1999), a license-verified (CC BY 4.0) human-comparison leg for the **sign** of the effect. A **per-item**
human gradient is **not** license-verified (verified null 2026-07-14; the classic gradient corpora are
paywalled) and is a queued scout, not a precondition — the direction anchor is the adopted primary,
mirroring the dative and genitive lines.

## Notes / caveats

- The construction is **English-specific** in this exact form; bracket cross-linguistic ambition.
- **Pronominal objects excluded** — pronoun objects are near-categorically split (*pick it up*), a
  categorical grammatical fact, not the graded soft preference under test. Full lexical NP objects only.
- The anchor grounds the **direction only** (Kim et al. is a restatement of the native-speaker direction,
  not a fresh rating experiment) — no per-item human-gradient or human-*level* claim.
- Watch the operationalization-tuning failure mode (charter §8): the item set and the shadow control are
  frozen before any spend and not retuned after seeing model outputs.
