---
type: claim
id: particle-placement-givenness
title: On English verb-particle placement, TWO of three models (claude, gemini) shift their split-order preference toward discourse-given objects in the human direction and the shift SURVIVES a byte-identical discourse-givenness firewall across two controlled runs on certified-disjoint items (s225/s226 v1 + s229 rep2) — a direction-only, human-anchored cross-construction generalization of the dative's information-structural effect, promoted strictly BELOW the genitive's 3/3-firewall claim because the load-bearing firewall replicates at 2/3 not 3/3 and gpt is a persistent, replicated SHADOW (its determiner effect does not survive either run, and the arm enlargement built to power it did not pull it over); the referential effect is small vs the strongly-tracked end-weight constraint, no within-model magnitude attached, all fences carried verbatim
meaning-senses:
  - constructional
  - inferential
  - distributional
  - human-comparison
status: supported
anchor: human-anchored
contingent-on: []
created: 2026-07-15
updated: 2026-07-15
links:
  - rel: anchors
    target: resource/particle-placement-givenness-human-anchor
  - rel: depends-on
    target: result/particle-placement-givenness-v1
  - rel: depends-on
    target: result/particle-placement-givenness-rep2
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: conjecture/particle-placement-givenness
  - rel: supports
    target: claim/dative-information-structure-givenness
  - rel: depends-on
    target: source/kim-2016-particle-placement
---

# Claim: two of three models track object discourse-givenness on verb-particle placement — promoted direction-only, 2/3-firewall, strictly below the genitive

> **Status: supported (2026-07-15, session 229).** Cross-session, independent, adversarial claims-promotion
> review ([`PROTOCOL.md §3`](../../../PROTOCOL.md); program item A2a) of the verb-particle placement
> **object-givenness** line — [`result/particle-placement-givenness-v1`](../results/particle-placement-givenness-v1.md)
> (sessions 225/226, PANEL CONFIRM, single run) and its fresh-item replication
> [`result/particle-placement-givenness-rep2`](../results/particle-placement-givenness-rep2.md)
> (session 229, PANEL CONFIRM again, all 48 frames + nouns certified disjoint from v1). It promotes the
> **givenness-direction** production-preference positive **for the two firewall-surviving members (claude,
> gemini) only**, and it mirrors the shape of the sibling
> [`claim/genitive-alternation-animacy`](genitive-alternation-animacy.md) — but is held **strictly below**
> it. **This is the project's first 2/3-firewall promotion**, and the scope ceiling is a binding condition
> of the verdict: the load-bearing byte-identical firewall replicates at **2/3, not 3/3**, and **gpt is a
> persistent, replicated SHADOW** (its determiner effect does not survive the firewall on either run, and
> the arm enlargement built to power it did not pull it over — its rep2 point estimate is *lower* than v1's).
> The fresh-agent reviewer (verdict authority) returned **PROMOTE-DIRECTION-ONLY, 2/3-firewall**; the
> non-Anthropic decorrelation vote returned **PROMOTE-WITH-CONDITIONS** (exclude gpt from the confirmed
> effect; no panel-wide language) — convergent, weighed in Anti-cheat below. **No within-model magnitude is
> attached** (unlike the genitive's fence i): the claim asserts direction + firewall-survival (2/3) + a
> stable gpt-SHADOW + "small vs end-weight," nothing quantitative beyond the reported shifts.

## Statement

Across **two** controlled runs on **disjoint item sets** (v1, sessions 225/226, 40 frames; rep2, session
229, 48 frames, every (verb, particle, noun) triple and every object noun certified disjoint from v1) on
the ratified 3-family panel (`claude-sonnet-4.6`, `gpt-5.4-mini`, `gemini-3.5-flash`), **two of the three
models — `claude-sonnet-4.6` and `gemini-3.5-flash` — shift their verb-particle placement preference
toward the *split* order for a discourse-given object**, in the human-attested direction (definite /
discourse-given object → split; *picked the barrel up* over *picked up the barrel*), and — the load-bearing
control — **the shift survives the byte-identical discourse-givenness firewall on both runs**. In the
firewall arm the scored object string is held **byte-identical** (*the {noun}*) across GIVEN /
NEW-MENTIONED / NEW, and the givenness manipulation lives only in one preceding discourse sentence, so the
decisive within-frame contrast `shift₂ = mean(split-pref | GIVEN) − mean(split-pref | NEW-MENTIONED)` is
scored on identical strings — any string-frequency / determiner-collocation / always-split / lexical-recency
reader yields **zero by construction**. For claude and gemini `shift₂` clears its bootstrap 95% lower bound
above zero on **both** runs (claude +0.040 / +0.035; gemini +0.072 / +0.057, both rep2 legs within v1's
CIs). So for these two models the split-order preference tracks **referential** discourse-givenness — the
same information-structural driver as the dative
([`claim/dative-information-structure-givenness`](dative-information-structure-givenness.md)) — on a
**wholly different construction**, robustly to the strongest logprob-free shortcut controls available.

The claim is promoted **direction-only** and is **scoped and qualified**, never panel-uniform and **not** at
the genitive's breadth:

- **Two of three, named individually — NOT a panel claim, NOT 3/3.** The positive covers **claude and
  gemini**. This is below the genitive's and dative's 3/3 firewall breadth; the particle's load-bearing
  firewall replicates at **2/3** (fence a).
- **gpt is a persistent, replicated SHADOW — a first-class negative in the claim's spine.** gpt shows a
  clear definite→split determiner shift (+0.100 on both runs) but its firewall shift does **not** survive:
  +0.018 (v1, CI [−0.017, 0.055], 18/40) and +0.005 (rep2, CI [−0.027, 0.036], 24/48). The rep2 enlarged the
  firewall arm 40→48 frames *specifically* to power this leg, and gpt **still** did not cross CI-LB>0 — its
  point estimate *dropped*. So for gpt the determiner effect is a **surface/lexical shadow**, not
  information-structure tracking; gpt is the weakest leg **again** (weakest on the dative, marginal on the
  genitive firewall, SHADOW on the particle firewall **twice**) (fence b). Displayed, never averaged.
- **Direction is human-anchored (sign only); no magnitude is attached.** The human anchor is a native-speaker
  **direction/sign** (Kim et al. 2016 / Gries 1999, a restatement), so the human-comparison force is on the
  **sign** of the effect, not any size, and — unlike the genitive — **no** within-model magnitude has been
  measured (no powered/pooled magnitude arm was run; the effect is small; fence j).

## Grounds

Two own-design results, a byte-identical (sha-verified) instrument, replicating the **direction** and the
**byte-identical-firewall survival** on disjoint item sets — the A2a pattern that discharged the dative's,
CC's, and genitive's single-run flags. Read the **per-model shifts** below, not a pooled panel scalar.
Within-frame firewall shift `shift₂ = mean(split-pref | GIVEN) − mean(split-pref | NEW-MENTIONED)` per
model, bootstrap 95% CI over frames (verdict map fixed before any call: cond_fw iff mean shift₂ > 0 **and**
bootstrap lower bound > 0):

| model | v1 firewall (N=40) | rep2 firewall (N=48) | definiteness (v1 / rep2) | length (v1 / rep2) | firewall verdict (both) |
|---|---:|---:|---:|---:|---|
| `claude-sonnet-4.6` | **+0.040** [0.022, 0.059] (26/40) | **+0.035** [0.019, 0.051] (32/48) | +0.081 / +0.095 | +0.344 / +0.332 | SURVIVES ∧ SURVIVES |
| `gemini-3.5-flash` | **+0.072** [0.049, 0.095] (31/40) | **+0.057** [0.032, 0.080] (35/48) | +0.068 / +0.076 | +0.402 / +0.386 | SURVIVES ∧ SURVIVES |
| `gpt-5.4-mini` | +0.018 [**−0.017**, 0.055] (18/40) | +0.005 [**−0.027**, 0.036] (24/48) | +0.100 / +0.100 | +0.287 / +0.307 | **SHADOW ∧ SHADOW** |

Panel verdict **CONFIRM** on both runs (firewall CI-LB>0 in 2/3; definiteness directionally consistent 3/3,
0 reversals; convergent length 3/3). Total billed: v1 $2.5811, rep2 $3.1765 (both 0 missing). Full CIs,
covariate legs, per-cell means, and the rep2 supplementary robustness reads (28-unique-pair + pair-clustered
bootstrap, both preserving the 2/3 CONFIRM): [`result/particle-placement-givenness-v1`](../results/particle-placement-givenness-v1.md),
[`result/particle-placement-givenness-rep2`](../results/particle-placement-givenness-rep2.md).

- **What replicated (the claim's spine).** For claude and gemini, both the **definite/given→split direction**
  and the **byte-identical-firewall survival** reproduce on certified-disjoint items, with the rep2 firewall
  legs landing **within v1's CIs** — a clean replication of the reading, not just of a verdict label. This is
  fresh-item replication (`certification.json` check D: 0 shared triples, all 48 nouns fresh), not a re-run.
- **The SHADOW replicated and strengthened, as the design tested.** rep2 enlarged only the load-bearing
  firewall arm (40→48 frames) to power gpt's paired contrast; gpt's firewall leg did **not** cross CI-LB>0
  and its point estimate dropped (+0.018 → +0.005) — the pre-named SHADOW branch, confirmed twice. That makes
  the 2/3 reading *more* stable (same 2 confirm, same 1 shadows, on both runs) than a flickering marginal-3/3.
- **Both runs are recompute-verified.** Independent post-run fresh-agent verifiers reproduced every headline
  statistic from the raw jsonl with their own scripts and different bootstrap seeds (REPRODUCED, 0 material
  discrepancies; billed costs matched).

## Human-comparison leg (direction only)

The claim's human-comparison force is on the **direction of the effect**, not its size. The anchor is
[`resource/particle-placement-givenness-human-anchor`](../../base/resources/particle-placement-givenness-human-anchor.md)
— the native-speaker **direction** (definite / discourse-given object → split order) from
[`source/kim-2016-particle-placement`](../../base/sources/kim-2016-particle-placement.md) (Kim, Lee & Lee
2016, PACLIC 30, CC BY 4.0, verified firsthand; corroborated by Gries 1999). Because the anchor is a
**restatement** of the established native-speaker direction (not a fresh rating experiment), it grounds the
**sign only** — so the human-comparison statement is exactly: *claude and gemini shift their production
preference in the direction native-speaker usage attests.* The claim is therefore **not**
`internal-contrast-only` (it leans, in part, on the human givenness direction, at direction-only strength);
the byte-identical firewall arm is an **internal within-model shortcut control**, not a second human
comparison.

## The control that earns the rigor

- **The byte-identical discourse-givenness firewall (load-bearing).** The scored object string is held
  **byte-identical** (*the {noun}*) across GIVEN / NEW-MENTIONED / NEW; only the preceding discourse varies.
  A reader that had only learned which order-string is more frequent, or that only reacted to the object noun
  being recently mentioned (the decisive GIVEN − NEW-MENTIONED contrast holds lexical recency constant),
  scores **zero by construction** (certification check (2): 7 scored-string readers each yield within-frame
  shift₂ = 0). The shift persists for claude and gemini 2/2 runs; it catches gpt's determiner effect as a
  shadow 2/2 runs. This is a construction-level shortcut elimination (the direct analog of the dative's
  immune-by-construction design), and gpt's failure is the control **demonstrating its discriminating power**,
  not the control failing.
- **The frequency covariate (near-vacuous — a fence, not corroboration).** A frozen UD-EWT per-(verb+particle)
  marginal split-rate covariate is the secondary control; on both runs it has essentially **no** predictive
  validity for the per-frame definiteness shift (R² ≤0.02 v1 / ≤0.004 rep2; slopes negative), because
  particle-verb tokens are sparse in a small corpus (16/38 stimulus pairs have any token). Corroboration-only
  and weak; CONFIRM rests on the firewall (fence d).

## Fences the claim carries verbatim (a–l)

A future reader must carry all twelve; none is erased by promotion:

- **(a) 2/3, NOT 3/3 — the headline scope.** The load-bearing firewall replicates at **2/3** (claude, gemini),
  strictly below the genitive's and dative's 3/3 firewall. The coded "full CONFIRM" panel label (Arm 1 also
  clears CI-LB>0 3/3) must **not** be read as a 3/3 firewall; the load-bearing leg is Arm 2, which is 2/3.
- **(b) gpt is a persistent, replicated SHADOW** (first-class negative): determiner shift +0.100 both runs,
  firewall +0.018 (v1) / +0.005 (rep2), CI includes 0 both times; the 40→48 enlargement to power it did
  **not** cross and the point estimate *dropped*. The weakest leg **again**; **not** "marginal" (a leg that
  never clears, unlike the genitive's gpt which cleared once powered). Displayed, never averaged.
- **(c) The referential effect is SMALL vs the strongly-tracked end-weight constraint.** Firewall shifts
  ≈0.035–0.072 vs length/end-weight +0.31–0.40 (3/3, every frame positive). The panel tracks end-weight
  robustly and referential-givenness weakly-but-detectably (2/3) — a gradient of constraint-tracking.
- **(d) Covariate near-vacuous → CONFIRM rests on the firewall.** R² ≤0.02 / ≤0.004; corroboration-only.
- **(e) Firewall-borne, scoped away from the confoundable definiteness arm.** Decisive evidence is the
  byte-identical firewall (Arm 2), not the determiner contrast (Arm 1); gpt's determiner shift is precisely
  the surface shadow the firewall catches. No Arm-1 reversal (0/3 both runs).
- **(f) Direction-only human anchor.** Restatement (Kim/Gries), sign only — no per-item human gradient
  (license-verified null 2026-07-14), no human-level competence, no cross-linguistic claim.
- **(g) Behavioral / stated-preference only.** A 100-point naturalness distribution on a working surface,
  logprob-/surprisal-free; silent on representations and grounding; not a per-item human acceptability rating.
- **(h) Fresh-item but nearly same-date, same-version, single-lab, n=3 shared-prior decoders.** The two runs
  are **one calendar day apart** (v1 2026-07-14, rep2 2026-07-15) — a hair better than the genitive's
  same-date replication — but **same model versions**, single-lab, n=3. No meaningful temporal/version
  decorrelation; three decoders converging is weak on its own — the human **direction** anchor is what gives
  the result independent bearing.
- **(i) Not "the distributional shadow is defeated."** The byte-identity + NEW-MENTIONED exclude scored-string
  shortcuts and object-noun lexical recency — the strongest logprob-free shortcut controls available — but
  **not** the panel reproducing the human context→order joint distribution from pretraining. Narrowly
  directional.
- **(j) No within-model magnitude attached** (contrast the genitive's fence i). No powered/pooled magnitude
  arm was run; the claim asserts direction + firewall-survival (2/3) + stable gpt-SHADOW + "small vs
  end-weight," nothing quantitative beyond the reported shifts. A magnitude would be a future powered arm,
  **not** owed.
- **(k) Pair-reuse disclosure (rep2-specific).** rep2's 48 frames use 38 distinct verb+particle pairs; 10
  recur (frames f39–f48, a fresh noun + fresh context each), all drawn from v1's frozen 38-pair set to keep
  the covariate + `analyze.py` byte-frozen; selection criterion **linguistic** ("flexible/both-orders"),
  **not** v1-outcome-based. Because the firewall is a within-frame contrast, a pair's baseline split-propensity
  cancels, so pair-reuse cannot import v1's firewall magnitude; the 28-unique-pair restriction and a
  pair-clustered bootstrap **both** preserve the 2/3 CONFIRM (interval-width effect only, negligible).
- **(l) Cross-construction generalization is at 2/3.** "The dative's givenness effect generalizes to particle
  placement" holds for **claude + gemini only**; held explicitly distinct from and **below** the genitive's
  3/3-firewall claim and the dative's row on [`theory/shadow-depth-table-v4`](../theory/shadow-depth-table-v4.md).

## Where it sits

The particle line extends the dative finding — "the model tracks the soft discourse-givenness constraint in
the human direction" — from the ditransitive frame to **verb-particle placement**, byte-identically, for
**two of three models**. It is the third production-side alternation in the A5 battery (dative givenness,
genitive animacy, particle givenness), and — the battery's new reading — the **same discourse-givenness
driver** now appears on **two constructions** (dative + particle), byte-identically. But it is the **weakest
beater**: a **2/3-firewall** line with a persistent gpt SHADOW and no attached magnitude, held below the
genitive (3/3 firewall, magnitude attached) and the dative (thrice-observed, powered). It patterns with the
project's recurring **add/easy-direction** observation (current decoders track a well-described soft
constraint in the human direction, membership itself model-specific) and with
[`essay/concordant-verdict-hides-spread`](../essays/concordant-verdict-hides-spread.md) (a concordant
*direction* for the two confirming models hides a wide magnitude spread; gpt fails outright). It does **not**
reach an inference-licensing reading: the effect is a gradient *preference*, not the licensing of a
construction-contributed entailment. On the flagship
[`theory/shadow-depth-table-v4`](../theory/shadow-depth-table-v4.md) it is the sixth beater, now migrated
**result-cited → claim-cited** (a **2/3-firewall, gpt-SHADOW, effect-small, no-magnitude** promoted-direction
row, held visibly distinct from the five stronger beaters).

## What this claim does NOT say

- **Not a panel claim.** The firewall positive is **2/3** (claude, gemini); gpt fails the firewall on both
  runs. Never "the panel tracks object-givenness on particle placement."
- **Not 3/3, not equal to the genitive/dative in breadth.** The load-bearing firewall is 2/3; the Arm-1
  definiteness 3/3 and the coded "full CONFIRM" are **not** the load-bearing evidence.
- **gpt is a persistent SHADOW, not "marginal."** It never clears the firewall (worse than the genitive's
  gpt, which cleared once powered).
- **No human comparison of magnitudes; no within-model magnitude at all.** The anchor is direction-only, and
  no magnitude arm was run (fence j).
- **Not "the distributional shadow is defeated"** — narrowly directional, robust to the firewall's
  logprob-free shortcut controls, nothing stronger (fence i).
- **Not temporally/version robust** — nearly same-date, same versions, single-lab, n=3 (fence h).
- **No model-internal or grounding claim** — behavioral only.
- **Not a model ranking** — "gemini > claude > gpt at particle placement" licenses no "better model" reading
  (the spread decorrelates from general competence).
- **Not cross-linguistic.**

## Anti-cheat and the decorrelation vote (convergent — recorded, weighed)

Promotion fixes the **yardstick** — the Kim/Gries human givenness direction, the byte-identical firewall, and
the pre-registered lower-bound gate — never the result. Both runs' verdict maps were frozen before any call,
the panel roster was the standing ratified one, each run carried a fresh pre-run critic GO + a non-Anthropic
vote and an independent recompute-from-raw verifier, and promotion changes **no number**. The review could
equally have refused (the numbers stand either way), so there is no result-fixing motive.

**The non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.002576,
[`VOTE-promotion-s229.json`](../../../experiments/runs/2026-07-15-particle-placement-givenness-rep2/VOTE-promotion-s229.json))
returned PROMOTE-WITH-CONDITIONS** — it **converged** with promotion but conditioned it sharply: *"2/3
firewall with persistent gpt shadow is not panel-level confirmation … promote only if the claim language can
explicitly exclude gpt from the confirmed effect and avoid panel-wide language,"* framing the ceiling as *"a
direction-only behavioral regularity in a subset of models."* Per [`PROTOCOL.md §2`](../../../PROTOCOL.md) the
vote is signal to weigh, not a tiebreak; the fresh-agent reviewer (verdict authority) **adopted its condition
in full** — the claim is promoted **as a 2/3 claim**, naming claude and gemini individually, with gpt carried
as a replicated first-class SHADOW and **no** panel-wide language for the confirmed firewall effect (fences
a, b, l). The vote's live worry — that same-instrument disjoint-item runs are *"a second sample of one
assay"* — is answered exactly as in the genitive promotion: same-instrument-fresh-disjoint-items is the
project's **established** replication standard (dative, CC, genitive all promoted on it; §3's own text is
*"REPLICATED — fresh items or a genuine second run"*), and applying a stricter *"materially different
instrument"* bar would retroactively break every promoted claim; systematic instrument risk survives as
fences (f)/(i), not discharged by replication. The convergence and its one binding condition are **recorded
and honored**, not smoothed over.

## Status

`status: supported`. What is supported: on English verb-particle placement, **two of three models (claude,
gemini)** shift their split-order preference toward discourse-given objects in the **human-attested
direction** across **two controlled runs on certified-disjoint item sets**, and the shift **survives the
byte-identical discourse-givenness firewall** on both runs (a string-frequency / lexical-recency reader
scores zero by construction) — human-anchored on its **direction** leg. `supported` attaches to the
**direction/sign**, the **replication**, and the **firewall shortcut-immunity for the two covered members** —
with the load-bearing qualifiers that the firewall is **2/3 not 3/3**, **gpt is a persistent replicated
SHADOW**, the effect is **small vs end-weight**, the covariate is **near-vacuous**, the anchor is
**direction-only**, and **no within-model magnitude is attached**. It does **not** attach to a panel-uniform
reading, a human comparison of sizes, a within-model magnitude, a causal shadow-defeat reading, or a
human-level competence reading — all explicitly disclaimed above. The two underlying results (v1, rep2)
remain `status: proposed` (this claim consolidates them). `contingent-on: []` — the governing
operationalization
([`decisions/resolved/particle-placement-anchor-and-indicator`](../../decisions/resolved/particle-placement-anchor-and-indicator.md),
ADOPT-WITH-MODIFICATION) is ratified.
