---
id: particle-placement-anchor-and-indicator
title: How to operationalize the verb-particle placement object-givenness probe — focal constraint, logprob-free indicator + shadow control, and anchor posture?
status: open
opened: 2026-07-14
opened-by: autonomous (session 224, opening the A5 third sibling — verb-particle placement)
eligible-to-ratify: 2026-07-15 (s225+; never the opening session)
anchor: human-anchored (Kim et al. 2016 / Gries 1999 native-speaker definite→split direction; per-item gradient a license-unverified deferred scout)
---

> **OPEN — opened session 224 (2026-07-14), the third A5 production-side sibling (verb-particle
> placement).** Ratifiable **s225+** via the autonomous cross-session adversarial-review procedure
> ([`PROJECT.md`](../../../PROJECT.md) §12.3): a fresh-agent reviewer with verdict authority, weighing one non-Anthropic
> decorrelation vote. **This session's pre-run critic + non-Anthropic vote are QA input recorded below,
> not a ratification.** The conjecture
> [`conjecture/particle-placement-givenness`](../../findings/conjectures/particle-placement-givenness.md)
> and design [`design/particle-placement-givenness-v1`](../../../experiments/designs/particle-placement-givenness-v1.md)
> are PROVISIONAL / `contingent-on` this decision; the freeze + run are **s225+**, honoring the anti-cheat
> separation (no probe ran in the opening session). Full options + the pre-run-critic record below.

# Decision: anchor + indicator + shadow control for the particle-placement givenness probe

## Why this exists

Program A5 (the production-side alternation battery) has landed two human-anchored siblings — the dative
([`claim/dative-information-structure-givenness`](../../findings/claims/dative-information-structure-givenness.md),
discourse-structural givenness) and the genitive
([`claim/genitive-alternation-animacy`](../../findings/claims/genitive-alternation-animacy.md), possessor
animacy). The **third sibling** is the **English verb-particle placement** alternation (joined *picked up
the book* vs split *picked the book up*), whose robust soft constraint is the **information status of the
direct object** (definite/given → split; Kim et al. 2016 / Gries 1999). The human anchor is now in-repo as
[`resource/particle-placement-givenness-human-anchor`](../../base/resources/particle-placement-givenness-human-anchor.md)
(Kim et al. 2016, CC BY 4.0, verified firsthand). But *how* the probe is run turns on value-laden choices a
session must not auto-take (CLAUDE.md rule 5). They interlock, so they are surfaced together.

Particle placement differs from both prior siblings in one design-critical way that is an **advantage**:
object givenness can be moved into the **discourse context** while the two scored order-strings (joined /
split) stay **byte-identical**. That yields a **strictly byte-identical firewall arm** — the cleanest
possible shortcut control, tighter than the genitive's nonce-possessor arm (which still varied the
possessor string). The design leans the CONFIRM on that firewall, not on a corpus covariate.

## The three sub-questions

### Q1 — Focal constraint (and its operationalization)

- **Option A (provisional default): object givenness / information-status, primary contrast =
  definiteness.** Directly anchor-matched (Kim et al.'s DET direction, verbatim: indefinite → joined,
  definite → split), and the **same information-structural driver as the dative** — so a CONFIRM
  demonstrates cross-construction generalization of the battery's discourse-structural thread. Paired with
  a byte-identical discourse-givenness firewall (Q2) that removes the definiteness arm's surface confound.
- **Option B: object length / end-weight as the focal constraint** (short → split; long → joined; also
  anchored verbatim). Real and robust, but length is a *processing / dependency-length-minimization*
  effect, murkier as a "distributional-shadow beater" (dependency-length minimization is itself a cognitive
  constraint, not merely a surface shadow), and it re-introduces a lexical difference across conditions
  (the modifier). Held as the **convergent-validity leg** (Arm 3), not the focal contrast.
- **Option C: a different sibling** (locative / spray-load alternation). A verified CC-BY anchor exists
  (Cao 2021, holism direction) and it is a viable future A5 row, but its constraint is a semantic-
  entailment (holistic-affectedness) reading rather than a graded soft production preference — a harder,
  less dative-parallel first cut. Hold as a later row.

### Q2 — Indicator + the shadow control (the crux)

**Indicator.** Logprob/surprisal is unavailable under pure autonomy (the AANN blocker), so a behavioural
indicator is required.

- **Option (i) (provisional default): graded forced-choice.** Hold verb + particle + object head-noun
  fixed; the model distributes 100 points by naturalness between the joined and split orders; split-pref =
  split_pts/(split_pts+joined_pts). Mirrors the project's validated, shortcut-certified dative/genitive
  instrument. Within-frame measure: shift = split-pref(given/definite) − split-pref(new/indefinite).
- **Option (ii): separate single-variant acceptability rating** (rate each order 0–100 independently). A
  sensitivity check, not the primary (no direct within-item preference contrast).

**The shadow control (load-bearing).** Because the definiteness arm's conditions differ by determiner, a
definite→split shift could be a shadow of the higher surface frequency of definite-object split-order
strings. Provisional default control set:

1. A **byte-identical, three-condition discourse-givenness firewall arm** (the PRIMARY shortcut control):
   hold the object string byte-identical (*the box*) across conditions, manipulate information status only
   in the **preceding discourse context** — **GIVEN** (mentioned + topical), **NEW-MENTIONED** (object noun
   mentioned at matched recency but referentially new), **NEW** (unmentioned). The two scored order-strings
   are byte-identical across conditions, so **any string-frequency / determiner-collocation / always-split /
   always-joined reader yields shift = 0 by construction**. The **decisive contrast is GIVEN −
   NEW-MENTIONED**, which additionally holds the object noun's lexical priming/recency constant — so a
   positive firewall shift can only come from integrating *referential* information structure, not mere
   lexical recency (s224 critic B-crit-1; without NEW-MENTIONED, a two-condition GIVEN−NEW firewall
   confounds givenness with object-noun priming *by construction*). This is stricter than the genitive's
   nonce arm and is the decisive leg the CONFIRM rests on (Arm 1 requires only directional consistency, not
   a hard CI-LB gate — s224 SHOULD-FIX 1).
2. A **frozen surface-collocation covariate** (corroboration, one exact sha'd recipe): a per-item split-
   order marginal rate for the verb+particle from a license-verified corpus (UD English-EWT, CC BY-SA,
   in-scope), frozen before any call; `analyze.py` reports the definiteness shift's residual over it.
   Expected **near-vacuous** (particle-placement instances are sparse in a small corpus) — stated
   honestly; corroboration only.

Plus a **pre-registered CONFIRM-vs-SHADOW rule**: definiteness shift₁ CI-LB > 0 (≥2/3) **AND** byte-
identical firewall shift₂ CI-LB > 0 (≥2/3), else SHADOW — the adjudication fixed ex ante, the firewall the
decisive leg.

Plus the standard guards: object **length, type (full lexical NP — no pronouns), concreteness, animacy, VP
idiomaticity** held constant across conditions; A/B counterbalancing with a target-blind parser; the
GIVEN/NEW discourse contexts matched in length + lexical content except the givenness manipulation (Arm 2's
authoring crux — referential givenness, not mere lexical priming).

### Q3 — Anchor posture + what the result may claim

- **Provisional default: human-anchored** (NOT `internal-contrast-only`). The direction tested (definite /
  given object → split) is a native-speaker fact from Kim et al. (2016) / Gries (1999), so the result may
  make a calibrated **human-comparison** claim on the **direction**. **Modesty caveat (carried from the
  source):** the anchor is a **restatement** of the established native-speaker direction (not a fresh
  rating experiment like the genitive's Dubois), so it grounds the **sign only**; the per-item human
  gradient is license-unverified (verified null 2026-07-14) and deferred to a scout.
- **May NOT:** claim human-*level* particle-placement competence; claim the effect beats the distributional
  shadow unless the byte-identical firewall clears it; lift attested example sentences (use synthetic
  minimal pairs); make any cross-linguistic claim.

## What the reviewer should weigh (s225+)

1. Is object givenness (definiteness) the right *focal* constraint (Option A), given it re-tests the
   dative's information-structural driver on a new construction — a genuine generalization test — vs
   choosing length (Option B) as a fresh, non-dative driver? Is the dative-parallel a **strength**
   (cross-construction generalization) or a **weakness** (less novel than a new driver)?
2. Is the graded-forced-choice indicator (Option i) the honest match, or should the separate-rating
   (Option ii) be primary?
3. **Is the byte-identical discourse-givenness firewall (Arm 2) genuinely shortcut-immune, and is its
   authoring controlled so it manipulates referential givenness rather than mere lexical mention/priming?**
   This is the chief cheat-surface and the load-bearing leg.
4. Is "human-anchored on the direction, per-item gradient deferred, anchor-is-a-restatement" the right
   posture (Q3), or does the modest provenance of the Kim et al. anchor (vs the genitive's Dubois rating
   experiment) push this toward a weaker human-comparison claim — or even `internal-contrast-only` with the
   Kim direction as external corroboration?

## Provisional default (to be adopted, modified, or rejected s225+)

**Q1-A** (object givenness, primary = definiteness; length the convergent leg) / **Q2-(i)** graded forced-
choice with the **byte-identical discourse-givenness firewall** as the load-bearing shortcut control **and**
a frozen surface-collocation covariate as corroboration, confounds held, A/B counterbalanced, firewall arm
powered ≥ definiteness arm / **Q3** human-anchored (direction only; anchor is a restatement; per-item
gradient a queued license-verified upgrade only).

## Anti-cheat note

Ratifying fixes the **yardstick** (focal constraint, indicator, shadow control, anchor posture), never the
**result**. The probe must not be run, nor the item set / control retuned, in the session that ratifies; a
pre-run-critic NO-GO on the firewall **defers** the run rather than relaxing the control. A null (no
givenness shift, or a shift that fails the byte-identical firewall) is a first-class result.

## Pre-run critic (this design session, s224) — QA input, not a ratification

A fresh-agent pre-run critic (verdict authority for the eventual run) + one non-Anthropic decorrelation
vote (`gpt-5.4-mini`, $0.003934) reviewed this design and these provisional defaults. Full record:
[`REVIEW-critic-s224.md`](../../../experiments/runs/2026-07-14-particle-placement-givenness-design/REVIEW-critic-s224.md).

- **Fresh-agent critic → GO-WITH-CONDITIONS.** Anchor mapping verified correct; verdict frame symmetric.
  One BLOCKER folded into the design this session: **B-crit-1** — the byte-identical firewall moves the
  shortcut off the scored string but *into the context* (givenness is created by mentioning the object, so
  a two-condition GIVEN−NEW firewall confounds referential givenness with object-noun lexical priming *by
  construction*). **Fixed** by adding the **NEW-MENTIONED** third condition → decisive contrast GIVEN −
  NEW-MENTIONED (with an Option-B rescope fallback). Plus SHOULD-FIX 1 (asymmetric CONFIRM rule — firewall
  necessary+primary, Arm 1 directional-consistency only, to avoid a false-negative machine), 2 (independent
  parallelism certification), 3 (broaden Arm-1 confound disclosure), 4 (definite-in-NEW felicity), 5
  (FALSIFY → pre-registered v2). **Ratification recommendations: Q1 adopt Option A (givenness — only
  givenness affords the byte-identical firewall; length would forfeit it), Q3 keep human-anchored on the
  direction/sign only (internal-contrast-only would under-claim a genuine anchor).**
- **Non-Anthropic decorrelation vote → NO-GO**, convergent on the core (Arm-2 context→string leakage;
  muddled Arm-1/Arm-2 framing; length-as-cleaner; internal-contrast-only). The leakage + framing points are
  **addressed** by B-crit-1 + the asymmetric rule; the length and internal-contrast-only preferences were
  **weighed and not adopted** on the fresh-agent critic's reasoned grounds. A NO-GO decorrelation vote
  weighed-and-addressed is the intended decorrelation function.
- **Net:** GO-WITH-CONDITIONS; design hardened this session (B-crit-1 + SHOULD-FIX 1–5 folded), the A1a/
  genitive pattern. The ratifying session (s225+) should weigh Q1/Q3 above and require the Arm-2
  NEW-MENTIONED parallelism to be built + independently certified at freeze; a NO-GO on the firewall
  **defers** the run, never relaxes the control.
