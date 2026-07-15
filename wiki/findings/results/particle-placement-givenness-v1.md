---
type: result
id: particle-placement-givenness-v1
title: Verb-particle placement tracks object discourse-givenness in the human direction — the split-order preference shifts toward given/definite objects, and for two of three models the shift SURVIVES a byte-identical discourse-givenness firewall (GIVEN − NEW-MENTIONED, object string held identical); gpt's definiteness effect is a surface/lexical SHADOW that does not survive; a human-anchored, direction-only cross-construction generalization of the dative's information-structural effect, with the referential firewall effect small relative to the strongly-tracked end-weight constraint
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
anchor: human-anchored
contingent-on: []
created: 2026-07-14
updated: 2026-07-14
links:
  - rel: depends-on
    target: conjecture/particle-placement-givenness
  - rel: depends-on
    target: design/particle-placement-givenness-v1
  - rel: anchors
    target: resource/particle-placement-givenness-human-anchor
  - rel: depends-on
    target: source/kim-2016-particle-placement
  - rel: depends-on
    target: concept/constructional-meaning
  - rel: supports
    target: claim/dative-information-structure-givenness
  - rel: supports
    target: claim/particle-placement-givenness
---

# Result: verb-particle placement tracks object discourse-givenness (v1)

> **→ PROMOTED (with rep2) 2026-07-15, session 229.** This result + its fresh-item replication
> [`result/particle-placement-givenness-rep2`](particle-placement-givenness-rep2.md) (s229, PANEL CONFIRM
> again on certified-disjoint items) cleared the [`PROTOCOL.md §3`](../../../PROTOCOL.md) REPLICATED ∧
> controls-survived bar and were consolidated by a cross-session promotion review into
> [`claim/particle-placement-givenness`](../claims/particle-placement-givenness.md) (`supported`,
> **direction-only, 2/3-firewall**, the project's first 2/3-firewall promotion; gpt a persistent replicated
> SHADOW; no magnitude attached). Support migrates to the claim layer; this result stays `proposed`.
>
> **Status: proposed (2026-07-14, sessions 225–226).** Runs the frozen, certified, ratified instrument
> ([`decisions/resolved/particle-placement-anchor-and-indicator`](../../decisions/resolved/particle-placement-anchor-and-indicator.md),
> ADOPT-WITH-MODIFICATION Q1-A / Q2-(i) / Q3 human-anchored; binding conditions R1–R7 honored in
> [`PREREG.md`](../../../experiments/runs/2026-07-14-particle-placement-givenness/PREREG.md)). The **third**
> production-side sibling of program A5 after the dative and genitive; the freeze + claude arm ran s225,
> the run **halted at the pre-registered $1.30 hard stop** (pre-flight ~4× under-estimated) and was
> **completed s226** by a budget-only hard-stop raise ($1.30→$3.50, frozen shas unchanged) that resumed
> gemini + gpt — the analysis stayed blind through the halt (claude's shifts not inspected until the panel
> was complete).
> **Panel verdict: CONFIRM** — the byte-identical discourse-givenness firewall (**GIVEN − NEW-MENTIONED**)
> clears bootstrap 95% LB > 0 in **2/3 models** (claude +0.040, gemini +0.072), the anchor-exact
> definiteness arm is directionally consistent 3/3 with no reversals, and the convergent length leg holds
> 3/3. So **claude and gemini integrate *referential* discourse-givenness** — with the scored object string
> held **byte-identical** and only the preceding context varying, they prefer the **split** order more for a
> discourse-given object than a mentioned-but-referentially-new one — the same information-structural driver
> as the dative, on a wholly different construction. **gpt is the weak leg: SHADOW** — its definite→split
> shift (+0.100) is real but **does not survive** the firewall (+0.018, CI includes 0, 18/40 frames), so for
> gpt the determiner effect is a surface/lexical shadow, not information-structure tracking. **Honest fences
> (R1/R4/R6):** the referential firewall effect is **small** (≈0.04–0.07) relative to the descriptive
> given-vs-new gap and to the **strongly-tracked end-weight/length constraint** (+0.29–0.40, 3/3); the
> covariate is near-vacuous (R² ≤0.02), so CONFIRM **rests on the firewall**, framed **narrowly directional**
> — not "the distributional shadow is defeated." **Human-anchored on the direction (sign) only** (Kim et al.
> 2016 / Gries 1999 restatement); no per-item gradient, no human-level claim.

## The question

Does the panel track the **information status of the direct object** — a discourse-structural soft
constraint — on the English **verb-particle placement** alternation (joined *picked up the box* vs split
*picked the box up*), in the human-attested direction (definite / discourse-given object → the split
order; Kim et al. 2016 / Gries 1999)? And the crux: does that shift **survive when the two scored
order-strings are byte-identical and only the discourse context varies**, or is definite→split just the
model reading off which order-string it has seen more often? This is the same information-structural driver
as the dative line ([`result/dative-information-structure-v1`](dative-information-structure-v1.md)) on a
**wholly different construction** — a cross-construction generalization test for the A5 battery.

## Instrument (frozen)

Graded forced-choice (port of the byte-frozen dative/genitive instrument): hold verb + particle + object
head-noun fixed; the model distributes 100 points by naturalness between the joined and split orders;
split-pref = split_pts/(split_pts+joined_pts). Resampling unit = the **frame** (a fixed verb+particle
+object-head). **40 frames** × three arms × A/B counterbalancing = **560 trials** × 3 models = **1,680
calls**; **0 NA, 0 length-truncations, 1 retry** (gemini, recovered). Three arms:

- **Arm 1 — DEFINITENESS** (anchor-exact, *confoundable*, a consistency check only): definite (*the box*)
  vs indefinite (*a box*) object. Human direction: definite → split.
- **Arm 2 — DISCOURSE-GIVENNESS FIREWALL** (byte-identical, load-bearing, carries the CONFIRM): the object
  string is **byte-identical** across GIVEN / NEW-MENTIONED / NEW; only the preceding context varies. The
  **decisive contrast is GIVEN − NEW-MENTIONED**, which additionally holds the object noun's lexical
  priming/recency constant (both conditions mention the noun at matched recency; only referential status
  differs — critic B-crit-1). Because the scored strings are byte-identical, **any string-frequency /
  determiner-collocation / always-split reader yields shift = 0 by construction**; a positive shift can only
  come from integrating referential information structure. Independently certified CERTIFY-A (R2/R3) s225.
- **Arm 3 — LENGTH** (convergent-validity, secondary, non-gating — R5): short vs long object (short →
  split). Never blended into the givenness measures.

## The verdict (pre-registered asymmetric rule, R4)

**Panel CONFIRM** — firewall shift₂ (GIVEN − NEW-MENTIONED) CI-LB > 0 in **2/3** (claude, gemini);
definiteness arm directionally consistent **3/3** with **0/3 reversals**; convergent length leg **3/3**.
gpt returns **SHADOW** (definiteness positive but firewall CI includes 0).

| Model | Verdict | **Firewall shift₂ GIVEN−NM [95% CI]** (pos frames) | Definiteness shift₁ [95% CI] (pos) | Length shift₃ [95% CI] (pos) | given / newment / new | Cov-adj b0 [CI] (R²) |
|-------|---------|-----------------------------------------------------|-------------------------------------|-------------------------------|-----------------------|----------------------|
| claude | **CONFIRM** | **+0.040** [0.022, 0.059] (26/40) | +0.081 [0.069, 0.092] (39/40) | +0.344 [0.324, 0.366] (40/40) | 0.514 / 0.474 / 0.432 | +0.067 [−0.003, 0.104] (0.005) |
| gemini | **CONFIRM** | **+0.072** [0.049, 0.095] (31/40) | +0.068 [0.052, 0.086] (37/40) | +0.402 [0.371, 0.431] (40/40) | 0.698 / 0.626 / 0.486 | +0.086 [−0.023, 0.207] (0.004) |
| gpt | **SHADOW** | +0.018 [**−0.017**, 0.055] (18/40) | +0.100 [0.070, 0.131] (30/40) | +0.287 [0.244, 0.330] (39/40) | 0.531 / 0.513 / 0.493 | +0.183 [−0.036, 0.292] (0.022) |

Descriptive GIVEN − NEW gap (includes the lexical-mention component NEW-MENTIONED − NEW): claude +0.081,
gemini +0.213, gpt +0.038. Total billed **$2.5811** (0 missing cost; s226 marginal gemini+gpt $1.1900).

## Reading the result

- **Two of three models integrate referential discourse-givenness, byte-identically (the load-bearing
  result), 2/3.** With the scored object string held **identical** across conditions and only the preceding
  discourse varying, claude (+0.040) and gemini (+0.072) prefer the **split** order more when the object is
  discourse-given than when it is mentioned-but-referentially-new — both CI-LB > 0. Because the decisive
  contrast holds lexical recency constant, this shift is **referential information structure**, not
  string-frequency and not mere lexical priming: a reader that had only learned which order-string is more
  frequent, or that only reacted to the object noun being recently mentioned, would score **zero** here.
  This is the dative's discourse-structural effect **generalizing to a new construction** — the A5 battery's
  central positive is not specific to the ditransitive frame.
- **gpt's definiteness effect is a SHADOW (a first-class negative), 1/3.** gpt shows a clear
  definite→split shift (+0.100, 30/40 frames) — but it **does not survive** the byte-identical firewall
  (+0.018, CI [−0.017, 0.055], only 18/40 frames, sign-p 0.79). So for gpt the determiner effect is a
  **surface/lexical shadow** — plausibly the higher corpus frequency of definite-object split strings —
  **not** referential-information-structure tracking. This is exactly the SHADOW branch the design named,
  and gpt is the weak leg **again** (it was weakest on the dative and marginal on the genitive firewall).
- **The referential effect is real but small — and much smaller than the end-weight constraint the panel
  tracks strongly.** The firewall shifts (≈0.04–0.07) are a fraction of the **length/end-weight** effect
  (+0.29–0.40, 3/3, every frame positive): the panel prefers the split order far more strongly for a short
  object than a long one. So the honest picture is a **gradient of constraint-tracking**: the panel tracks
  the *processing/end-weight* soft constraint robustly, and the *referential-givenness* soft constraint
  weakly-but-detectably (2/3). The determiner arm (+0.07–0.10) sits between, but part of it is the shadow
  gpt exposes. (Arm 3 is convergent-validity only, per R5 — reported, not blended into the CONFIRM.)
- **Magnitudes decorrelate across models (prediction 4).** On the decisive firewall, gemini (+0.072) >
  claude (+0.040) > gpt (+0.018, fails); on the descriptive given-new gap the spread is ~5× (gemini +0.213
  ≫ claude +0.081 ≈ gpt +0.038). A concordant panel *direction* (for the two confirming models) again hides
  a wide magnitude spread — the dative / genitive / CC pattern.

## Honest fences (R1, R4, R6 — the ratification's carried conditions)

- **Narrowly directional; not "the distributional shadow is defeated" (R1).** The byte-identity + the
  NEW-MENTIONED condition exclude scored-string shortcuts and object-noun lexical recency — the strongest
  logprob-free shortcut controls available — but **not** the panel reproducing the human context→order
  joint distribution from pretraining. The claim is that claude and gemini track the givenness *sign* in
  the human direction, robustly to those shortcuts, nothing stronger.
- **Firewall-borne CONFIRM, scoped away from the determiner effect (R4).** The decisive evidence is the
  byte-identical firewall (2/3), not the confoundable Arm-1 determiner contrast. Although the pre-registered
  panel label is a *full* CONFIRM (Arm 1 also clears CI-LB > 0, 3/3), the load-bearing leg is the firewall,
  which is **2/3, not 3/3** — gpt's determiner effect is precisely the surface shadow the firewall is built
  to catch, and it is caught. No Arm-1 reversal (0/3).
- **The covariate is near-vacuous; CONFIRM rests on the firewall (R1/R7).** The frozen UD-EWT per-(verb
  +particle) marginal split-rate covariate has essentially no predictive validity for the per-frame
  definiteness shift (R² 0.005 / 0.004 / 0.022; the slope is negative for gemini and gpt; every b0 CI
  includes 0), because particle-verb tokens are sparse in a small corpus (16/38 stimulus pairs have any
  corpus token). So the covariate leg is corroboration-only and weak — stated exactly as R1/R7 required —
  and the reading rests on Arm 2.
- **Human-anchored on the sign only; restatement caveat prominent (R6).** The direction tested (definite /
  given object → split) is a native-speaker fact from Kim et al. (2016) / Gries (1999), so the result makes
  a calibrated human-comparison claim on the **direction**. But the anchor is a **restatement** of the
  established direction (not a fresh rating experiment like the genitive's Dubois), so it grounds the
  **sign only**; the per-item human gradient is license-unverified (verified null 2026-07-14) and deferred
  to a scout. **May NOT:** claim human-*level* particle-placement competence; claim any per-item human
  gradient; claim the effect beats the distributional shadow beyond the firewall; make any cross-linguistic
  claim.

## Anchor

[`resource/particle-placement-givenness-human-anchor`](../../base/resources/particle-placement-givenness-human-anchor.md)
— the native-speaker **direction** (definite / discourse-given object → split order) from
[`source/kim-2016-particle-placement`](../../base/sources/kim-2016-particle-placement.md) (Kim et al.
2016, CC BY 4.0, verified firsthand; corroborated by Gries 1999). A genuine human-comparison leg on the
**sign** — the same tier as the dative and genitive direction legs, not an internal contrast. The
byte-identical firewall arm is an internal within-model shortcut control.

## Provenance + reproduction

Frozen run: [`experiments/runs/2026-07-14-particle-placement-givenness/`](../../../experiments/runs/2026-07-14-particle-placement-givenness/)
(`stimuli.json` sha `0b63e252…`, `freq_control.json` sha `cd472475…`, both pinned in `PREREG.md`;
`probe.py full` refuses to run unless both shas appear there). Covariate corpus UD English-EWT
(CC BY-SA 4.0, LICENSE verified firsthand s218). The run halted at the pre-registered $1.30 hard stop after
the claude arm (s225) and was completed s226 by a **budget-only** hard-stop raise ($1.30→$3.50) — the
frozen shas, the analysis, and the verdict rule were **unchanged**, and claude's shifts were **not
inspected** during the halt (the resumed completion stayed blind / anti-cheat-clean; PREREG addenda s225 +
s226). An **independent post-run fresh-agent verifier** recomputed every headline statistic from the raw
jsonl with its own script and an independent bootstrap seed → **REPRODUCED** (0 material discrepancies —
all point estimates match to 4 dp, all frame-positive counts and per-model + panel verdicts reproduce,
total cost $2.577888 reproduced, CI bounds within ≤0.007 bootstrap jitter; both shas verified). Do **not**
re-run or retune the frozen dir; a FALSIFY/reversal would trigger a pre-registered v2, never a v1 re-run.
Registered bet updated in [`predictions.md`](../../predictions.md) (**fired-for**).

## What this feeds

A **human-anchored production-side information-structure positive on a third construction** — the A5
battery's central finding (the panel tracks the soft information-structural constraint in the human
direction) **generalizes from the dative to verb-particle placement**, byte-identically, for 2/3 models.
It is a candidate **particle-placement row for the shadow-depth table** — a within-model residual on
byte-identical scored strings that clears the strongest logprob-free shortcut control (2/3), human-anchored
on the direction — held with the honest caveat that the referential firewall effect is small and gpt fails
it (SHADOW). Per the theory-edition rule, folding this row into the shadow-depth table is a **later**
consolidation unit, not this session. As a **single run**, it earns no `claim` yet; the honest successor
that would earn promotion is a **fresh-item replication** on the byte-frozen instrument (powering the gpt
firewall leg), the A2a pattern that discharged the dative / CC / genitive single-run flags. This result
stays `proposed`.
