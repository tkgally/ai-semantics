---
id: particle-placement-anchor-and-indicator
title: How to operationalize the verb-particle placement object-givenness probe — focal constraint, logprob-free indicator + shadow control, and anchor posture?
status: resolved
opened: 2026-07-14
opened-by: autonomous (session 224, opening the A5 third sibling — verb-particle placement)
resolved: 2026-07-14
resolved-by: autonomous (adversarial review)
resolution: "ADOPT-WITH-MODIFICATION — Q1-A (object givenness, primary contrast = definiteness; length the SECONDARY convergent leg) / Q2-(i) (graded forced-choice + the byte-identical THREE-condition discourse-givenness firewall GIVEN/NEW-MENTIONED/NEW as the load-bearing shortcut control, decisive contrast GIVEN−NEW-MENTIONED, + a frozen surface-collocation covariate as near-vacuous corroboration; asymmetric CONFIRM rule with firewall shift₂ CI-LB>0 necessary+primary and Arm 1 directional-consistency only) / Q3 human-anchored on the DIRECTION only (per-item gradient a license-unverified deferred scout). Ratified s225 by a fresh-agent adversarial reviewer (verdict authority, independent of the s225 freeze/run) that WEIGHED a non-Anthropic decorrelation vote (gpt-5.4-mini, $0.003591, which voted REJECT). The reviewer decomposed the vote's Q2 REJECT: 'discourse salience / topical persistence / referential prominence' IS the target construct (givenness = referential discourse-accessibility), a category error to call it a shortcut; object-noun lexical recency is a genuine shortcut CLOSED by construction by the NEW-MENTIONED condition; and the deep 'reproduce the human context→order joint distribution from pretraining' reading is the standing distributional-shadow limit of the whole program, handled by FENCING the claim (R1, the genitive-R5 analog), not by a design change. The asymmetric CONFIRM rule rests the necessary CI-LB gate on the byte-identical shortcut-immune arm and demotes the confoundable determiner arm to a consistency check — the correct direction for rigor; the covariate was declared near-vacuous corroboration honestly and up front. The internal-contrast-only relabel the vote urged was REJECTED as an under-claim of a genuine CC-BY-4.0, textbook-robust, ICE-GB-corroborated native-speaker direction (the genitive sibling resolved the identical question the same way). Seven binding residual freeze conditions R1–R7 carried to the s225 freeze: R1 CONFIRM narrowly directional / no 'shadow defeated'; R2 independent certification that GIVEN vs NEW-MENTIONED match mention-count/recency, differ only in referential status, and carry no structural-priming leak; R3 (new) certify the definite scored object is comparably felicitous in GIVEN and NEW-MENTIONED so shift₂ cannot ride an accommodation asymmetry; R4 asymmetric rule stays honest (Arm-1 reversal blocks CONFIRM; firewall-borne prose scoped away from the determiner effect); R5 givenness focal / length secondary and non-gating; R6 human-anchored on the sign with the restatement caveat prominent (not internal-contrast-only, not Dubois-strength); R7 all s224 freeze conditions (i)–(x) + SHOULD-FIX 1–5 + sha-freeze + no-retuning + NO-GO-defers stay binding. Tom's standing override outranks this autonomous ratification."
anchor: human-anchored (Kim et al. 2016 / Gries 1999 native-speaker definite→split direction; per-item gradient a license-unverified deferred scout)
---

> **RESOLVED — session 225 (2026-07-14), autonomous cross-session adversarial review.
> ADOPT-WITH-MODIFICATION (Q1-A object givenness / Q2-(i) graded forced-choice + byte-identical
> three-condition firewall / Q3 human-anchored on the direction), subject to binding freeze conditions
> R1–R7.** A fresh-agent adversarial ratification reviewer (verdict authority, independent of the s225
> freeze/run) **weighed** a non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.003591) that voted
> **REJECT**. The reviewer's decomposition of the vote's Q2 crux: the "discourse salience" leakage the
> vote feared **is the target construct** (givenness = referential discourse-accessibility), a category
> error to call a shortcut; object-noun **lexical recency** is a genuine shortcut **closed by
> construction** by the **NEW-MENTIONED** condition (GIVEN and NEW-MENTIONED match mention count/recency;
> the decisive GIVEN−NEW-MENTIONED contrast cannot be recency); and the deep "reproduce the human
> context→order joint distribution" reading is the program's standing distributional-shadow limit,
> handled by **fencing the claim** (R1), not a design change. The internal-contrast-only relabel was
> **rejected as an under-claim** (the genitive sibling resolved this identically). Full ratification
> record: [`REVIEW-ratify-s225.md`](../../../experiments/runs/2026-07-14-particle-placement-givenness/REVIEW-ratify-s225.md);
> raw vote [`VOTE-ratify-s225.json`](../../../experiments/runs/2026-07-14-particle-placement-givenness/VOTE-ratify-s225.json).
> The conjecture [`conjecture/particle-placement-givenness`](../../findings/conjectures/particle-placement-givenness.md)
> and design [`design/particle-placement-givenness-v1`](../../../experiments/designs/particle-placement-givenness-v1.md)
> are promoted out of contingent status. **No probe ran in the opening session (s224); the freeze + run
> are s225**, honoring the anti-cheat separation. Full options + the pre-run-critic record below.

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

- **Option A (RATIFIED default): object givenness / information-status, primary contrast =
  definiteness.** Directly anchor-matched (Kim et al.'s DET direction, verbatim: indefinite → joined,
  definite → split), and the **same information-structural driver as the dative** — so a CONFIRM
  demonstrates cross-construction generalization of the battery's discourse-structural thread. Paired with
  a byte-identical discourse-givenness firewall (Q2) that removes the definiteness arm's surface confound.
- **Option B: object length / end-weight as the focal constraint** (short → split; long → joined; also
  anchored verbatim). Real and robust, but length is a *processing / dependency-length-minimization*
  effect, murkier as a "distributional-shadow beater" (dependency-length minimization is itself a cognitive
  constraint, not merely a surface shadow), and it re-introduces a lexical difference across conditions
  (the modifier). **Ratified as the convergent-validity leg (Arm 3), not the focal contrast — and
  crucially, only givenness affords the byte-identical firewall; length would forfeit the shortcut-immune
  leg (R5).**
- **Option C: a different sibling** (locative / spray-load alternation). A verified CC-BY anchor exists
  (Cao 2021, holism direction) and it is a viable future A5 row, but its constraint is a semantic-
  entailment (holistic-affectedness) reading rather than a graded soft production preference — a harder,
  less dative-parallel first cut. Hold as a later row.

### Q2 — Indicator + the shadow control (the crux)

**Indicator.** Logprob/surprisal is unavailable under pure autonomy (the AANN blocker), so a behavioural
indicator is required.

- **Option (i) (RATIFIED default): graded forced-choice.** Hold verb + particle + object head-noun
  fixed; the model distributes 100 points by naturalness between the joined and split orders; split-pref =
  split_pts/(split_pts+joined_pts). Mirrors the project's validated, shortcut-certified dative/genitive
  instrument. Within-frame measure: shift = split-pref(given/definite) − split-pref(new/indefinite).
- **Option (ii): separate single-variant acceptability rating** (rate each order 0–100 independently). A
  sensitivity check, not the primary (no direct within-item preference contrast).

**The shadow control (load-bearing).** Because the definiteness arm's conditions differ by determiner, a
definite→split shift could be a shadow of the higher surface frequency of definite-object split-order
strings. Ratified control set:

1. A **byte-identical, three-condition discourse-givenness firewall arm** (the PRIMARY shortcut control):
   hold the object string byte-identical (*the box*) across conditions, manipulate information status only
   in the **preceding discourse context** — **GIVEN** (mentioned + topical), **NEW-MENTIONED** (object noun
   mentioned at matched recency but referentially new), **NEW** (unmentioned). The two scored order-strings
   are byte-identical across conditions, so **any string-frequency / determiner-collocation / always-split /
   always-joined reader yields shift = 0 by construction**. The **decisive contrast is GIVEN −
   NEW-MENTIONED**, which additionally holds the object noun's lexical priming/recency constant — so a
   positive firewall shift can only come from integrating *referential* information structure, not mere
   lexical recency (s224 critic B-crit-1). This is stricter than the genitive's nonce arm and is the
   decisive leg the CONFIRM rests on (Arm 1 requires only directional consistency, not a hard CI-LB gate —
   s224 SHOULD-FIX 1; R4).
2. A **frozen surface-collocation covariate** (corroboration, one exact sha'd recipe): a per-item split-
   order marginal rate for the verb+particle from a license-verified corpus (UD English-EWT, CC BY-SA,
   in-scope), frozen before any call; `analyze.py` reports the definiteness shift's residual over it.
   Expected **near-vacuous** (particle-placement instances are sparse in a small corpus) — stated
   honestly; corroboration only.

Plus a **pre-registered CONFIRM-vs-SHADOW rule** (asymmetric, R4): byte-identical firewall shift₂ (GIVEN −
NEW-MENTIONED) CI-LB > 0 (≥2/3) is **necessary + primary**; Arm 1 (definiteness) need only be directionally
consistent (point estimate same sign, human direction), else SHADOW.

Plus the standard guards: object **length, type (full lexical NP — no pronouns), concreteness, animacy, VP
idiomaticity** held constant across conditions; A/B counterbalancing with a target-blind parser; the
GIVEN/NEW-MENTIONED/NEW discourse contexts matched in length + lexical content except the givenness
manipulation (Arm 2's authoring crux — referential givenness, not mere lexical priming).

### Q3 — Anchor posture + what the result may claim

- **RATIFIED default: human-anchored** (NOT `internal-contrast-only`). The direction tested (definite /
  given object → split) is a native-speaker fact from Kim et al. (2016) / Gries (1999), so the result may
  make a calibrated **human-comparison** claim on the **direction**. **Modesty caveat (carried from the
  source):** the anchor is a **restatement** of the established native-speaker direction (not a fresh
  rating experiment like the genitive's Dubois), so it grounds the **sign only**; the per-item human
  gradient is license-unverified (verified null 2026-07-14) and deferred to a scout. Internal-contrast-only
  was **rejected as an under-claim** (R6).
- **May NOT:** claim human-*level* particle-placement competence; claim the effect beats the distributional
  shadow unless the byte-identical firewall clears it; lift attested example sentences (use synthetic
  minimal pairs); make any cross-linguistic claim.

## Ratification record (s225) — binding freeze conditions R1–R7

The fresh-agent adversarial ratification reviewer (verdict authority) issued **ADOPT-WITH-MODIFICATION**
after weighing the non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.003591 → REJECT). Seven binding
residual freeze conditions carried to the s225 freeze (full text + the vote's REJECT and its point-by-point
disposition in [`REVIEW-ratify-s225.md`](../../../experiments/runs/2026-07-14-particle-placement-givenness/REVIEW-ratify-s225.md)):

- **R1 (fence, Q2-deep).** CONFIRM framed narrowly directional — no "distributional shadow defeated";
  byte-identity + NEW-MENTIONED exclude scored-string shortcuts and lexical recency but not the panel
  reproducing the human context→order joint distribution.
- **R2 (certification).** Independent non-authoring certification that GIVEN vs NEW-MENTIONED match the
  object noun's mention count/recency, differ only in referential status, and carry no structural-priming
  leak. Uncertifiable ⇒ the run defers.
- **R3 (new).** Certify the definite scored object is comparably felicitous in GIVEN and NEW-MENTIONED so
  shift₂ cannot ride an accommodation/processing-difficulty asymmetry.
- **R4 (asymmetric rule honest).** Firewall shift₂ CI-LB>0 necessary+primary; Arm 1 directional-
  consistency only; an Arm-1 reversal blocks CONFIRM → FALSIFY; "firewall-borne" prose scoped away from
  the Kim et al. determiner effect specifically.
- **R5 (Q1).** Givenness focal; length (Arm 3) SECONDARY, non-gating, not blended into the givenness
  measures. Switching the focal constraint to length rejected.
- **R6 (Q3).** Human-anchored on the sign; restatement caveat prominent; not internal-contrast-only, not
  Dubois-strength.
- **R7 (standing).** All s224 freeze conditions (i)–(x) + SHOULD-FIX 1–5 + sha-freeze + no-retuning +
  NO-GO-defers remain binding.

## Anti-cheat note

Ratifying fixes the **yardstick** (focal constraint, indicator, shadow control, anchor posture), never the
**result**. The probe must not be run, nor the item set / control retuned, in the session that ratifies; a
pre-run-critic NO-GO on the firewall **defers** the run rather than relaxing the control. A null (no
givenness shift, or a shift that fails the byte-identical firewall) is a first-class result.

## Pre-run critic (opening design session, s224) — QA input, not a ratification

A fresh-agent pre-run critic (verdict authority for the eventual run) + one non-Anthropic decorrelation
vote (`gpt-5.4-mini`, $0.003934) reviewed this design at s224. Full record:
[`REVIEW-critic-s224.md`](../../../experiments/runs/2026-07-14-particle-placement-givenness-design/REVIEW-critic-s224.md).

- **Fresh-agent critic → GO-WITH-CONDITIONS.** Anchor mapping verified correct; verdict frame symmetric.
  One BLOCKER folded into the design at s224: **B-crit-1** — the byte-identical firewall moves the shortcut
  off the scored string but *into the context* (a two-condition GIVEN−NEW firewall confounds referential
  givenness with object-noun lexical priming *by construction*). **Fixed** by adding the **NEW-MENTIONED**
  third condition → decisive contrast GIVEN − NEW-MENTIONED. Plus SHOULD-FIX 1 (asymmetric CONFIRM rule),
  2 (independent parallelism certification), 3 (broadened Arm-1 disclosure), 4 (definite-in-NEW felicity),
  5 (FALSIFY → pre-registered v2). Recommendations: Q1 adopt givenness, Q3 keep human-anchored.
- **Non-Anthropic decorrelation vote (s224) → NO-GO**, convergent on the core (Arm-2 context→string
  leakage; muddled framing; length-as-cleaner; internal-contrast-only). Addressed by B-crit-1 + the
  asymmetric rule; the length and internal-contrast-only preferences weighed and not adopted.
