---
type: result
id: particle-placement-givenness-rep2
title: Verb-particle placement object-givenness REPLICATES on fresh disjoint items — a second controlled run of the byte-frozen instrument on 48 fresh frames reproduces v1's PANEL CONFIRM (the byte-identical discourse-givenness firewall GIVEN − NEW-MENTIONED clears bootstrap 95% LB > 0 in 2/3 models, definiteness directionally consistent 3/3, length 3/3), and gpt's firewall stays a SHADOW even with the arm enlarged 40→48 to power it — the marginal leg did not cross; the firewall effect is small vs the strongly-tracked end-weight constraint, human-anchored direction-only; the fresh-item replication the v1 single-run flag needed
meaning-senses:
  - constructional
  - inferential
  - distributional
status: proposed
anchor: human-anchored
contingent-on: []
created: 2026-07-15
updated: 2026-07-15
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
    target: result/particle-placement-givenness-v1
  - rel: supports
    target: claim/dative-information-structure-givenness
  - rel: supports
    target: claim/particle-placement-givenness
---

# Result: verb-particle placement object-givenness replicates on fresh disjoint items (rep2)

> **→ PROMOTED (with v1) 2026-07-15, session 229.** This replication + v1 were consolidated the same session
> by a cross-session promotion review into
> [`claim/particle-placement-givenness`](../claims/particle-placement-givenness.md) (`supported`,
> **direction-only, 2/3-firewall**; gpt a persistent replicated SHADOW; no magnitude attached). Support
> migrates to the claim layer; this result stays `proposed`.
>
> **Status: proposed (2026-07-15, session 229).** The fresh-item powered **replication** of
> [`result/particle-placement-givenness-v1`](particle-placement-givenness-v1.md) (s225/s226, PANEL CONFIRM,
> single run) — a within-design powered re-run under the already-ratified
> [`decisions/resolved/particle-placement-anchor-and-indicator`](../../decisions/resolved/particle-placement-anchor-and-indicator.md)
> (s225, **no new decision**), the dative-s175 / genitive-rep2-s220 A2a pattern. The instrument is
> **byte-frozen** (sha-verified identical to v1: `probe.py`, `analyze.py`, `build_cooc_particle.py`,
> `freq_control.json`); the only change is **48 fresh frames** (all 48 (verb, particle, noun) triples and
> all 48 object nouns certified disjoint from v1), with the load-bearing firewall arm **enlarged 40 → 48**
> to power v1's marginal gpt leg. Frozen + fully pre-run-gated s228; **run executed s229** on a fresh
> full-$5 UTC day (2,016 calls, 0 NA / 0 length-trunc / 0 retries, $3.17645).
> **Panel verdict: CONFIRM — v1 REPLICATES.** The byte-identical discourse-givenness firewall
> (**GIVEN − NEW-MENTIONED**, object string held identical, only the preceding context varying) clears
> bootstrap 95% LB > 0 in **2/3 models** (claude **+0.035** [0.019, 0.051], gemini **+0.057** [0.032, 0.080])
> — both point estimates **within v1's CIs** — the anchor-exact definiteness arm is directionally consistent
> **3/3** (0 reversals), and the convergent length leg holds **3/3**. So claude and gemini again integrate
> **referential** discourse-givenness on a wholly different construction from the dative, robustly to the
> strongest logprob-free shortcut controls, on **disjoint items**. **gpt is again the weak leg: SHADOW** —
> its definite→split shift (+0.100) is real but its firewall shift is **+0.005** (CI [−0.027, 0.036], 24/48),
> so **the arm enlargement (40→48) did NOT pull the gpt firewall leg over CI-LB > 0** — the honestly
> pre-named outcome (the enlargement powers, it does not guarantee). **Honest fences (R1/R4/R6):** the
> referential firewall effect is **small** (≈0.035–0.057) relative to the strongly-tracked **end-weight**
> constraint (+0.31–0.39, 3/3); the covariate is near-vacuous (R² ≤0.004), so CONFIRM **rests on the
> firewall**, framed **narrowly directional** — not "the distributional shadow is defeated." **Human-anchored
> on the direction (sign) only** (Kim et al. 2016 / Gries 1999 restatement). This is the fresh-item
> replication v1's single-run flag needed; it clears the [`PROTOCOL.md §3`](../../../PROTOCOL.md)
> **REPLICATED ∧ controls-survived** bar and is the input to a cross-session promotion review (a
> **direction-only, 2/3-firewall** particle `claim`).

## The question (unchanged from v1)

Does the panel track the **information status of the direct object** on the English **verb-particle
placement** alternation (joined *picked up the box* vs split *picked the box up*), in the human-attested
direction (definite / discourse-given object → the split order; Kim et al. 2016 / Gries 1999)? And the
crux — does that shift **survive when the two scored order-strings are byte-identical and only the
discourse context varies**? v1 (s225/s226) answered CONFIRM but was a **single run**, so it earned no
`claim`. This rep2 re-tests the direction + firewall survival on **disjoint items** and enlarges the
load-bearing firewall arm (40 → 48 frames) to power the previously-marginal gpt leg.

## Instrument (byte-frozen; sha-verified identical to v1)

Graded forced-choice (byte-frozen dative/genitive/particle-v1 instrument): hold verb + particle + object
head-noun fixed; the model distributes 100 points by naturalness between the joined and split orders;
split-pref = split_pts/(split_pts+joined_pts). Resampling unit = the **frame** (a fixed verb+particle
+object-head). **48 fresh frames** × three arms × A/B counterbalancing = **672 trials** × 3 models =
**2,016 calls**; **0 NA, 0 length-truncations, 0 retries**. The three arms and the shadow control are
**byte-identical to v1** (R1–R4):

- **Arm 1 — DEFINITENESS** (anchor-exact, *confoundable*, a consistency check only): definite (*the box*)
  vs indefinite (*a box*). Human direction: definite → split. A reversal blocks CONFIRM; not a hard CI gate.
- **Arm 2 — DISCOURSE-GIVENNESS FIREWALL** (byte-identical, load-bearing, carries the CONFIRM; **enlarged
  40 → 48 frames**): the object string is **byte-identical** across GIVEN / NEW-MENTIONED / NEW; only the
  preceding context varies. **Decisive contrast = GIVEN − NEW-MENTIONED**, which additionally holds the
  object noun's lexical priming/recency constant (both conditions mention the noun at matched recency; only
  referential status differs — critic B-crit-1). Because the scored strings are byte-identical, **any
  string-frequency / determiner-collocation / always-split reader yields shift = 0 by construction**;
  a positive shift can only come from integrating referential information structure.
- **Arm 3 — LENGTH** (convergent-validity, secondary, non-gating — R5): short vs long object (short →
  split). Reported, never blended into the CONFIRM gate.
- **Frozen surface-collocation covariate** (corroboration, near-vacuous — R1/R7): per-(verb+particle)
  marginal SPLIT-order rate from UD-EWT (`freq_control.json`, **byte-identical to v1**). Sparse.

## The verdict (pre-registered asymmetric rule, R4 — byte-identical to v1)

**Panel CONFIRM** — firewall shift₂ (GIVEN − NEW-MENTIONED) CI-LB > 0 in **2/3** (claude, gemini);
definiteness arm directionally consistent **3/3** with **0/3 reversals**; convergent length leg **3/3**.
gpt returns **SHADOW** (definiteness positive but firewall CI includes 0). Because Arm 1 also clears
CI-LB > 0 in 3/3, the coded label is a *full* CONFIRM — but the **load-bearing** leg is the firewall,
which is **2/3, not 3/3**, so the reading is scoped **firewall-borne, 2/3**, exactly as in v1.

| Model | Verdict | **Firewall shift₂ GIVEN−NM [95% CI]** (pos) | Definiteness shift₁ [95% CI] (pos) | Length shift₃ [95% CI] (pos) | given / newment / new | Cov-adj b0 [CI] (R²) |
|-------|---------|----------------------------------------------|-------------------------------------|-------------------------------|-----------------------|----------------------|
| claude | **CONFIRM** | **+0.035** [0.019, 0.051] (32/48) | +0.095 [0.083, 0.107] (47/48) | +0.332 [0.312, 0.352] (48/48) | 0.505 / 0.470 / 0.415 | +0.108 [0.067, 0.153] (0.004) |
| gemini | **CONFIRM** | **+0.057** [0.032, 0.080] (35/48) | +0.076 [0.062, 0.090] (44/48) | +0.386 [0.358, 0.411] (48/48) | 0.685 / 0.629 / 0.486 | +0.081 [0.024, 0.157] (0.000) |
| gpt | **SHADOW** | +0.005 [**−0.027**, 0.036] (24/48) | +0.100 [0.072, 0.130] (40/48) | +0.307 [0.268, 0.347] (47/48) | 0.502 / 0.497 / 0.492 | +0.113 [0.028, 0.260] (0.001) |

Descriptive GIVEN − NEW gap (includes the lexical-mention component): claude +0.089, gemini +0.199,
gpt +0.011. Total billed **$3.17645** (0 missing cost). Analysis reproduced independently — see Provenance.

## Reading the result — v1 replicates on disjoint items

- **v1's PANEL CONFIRM replicates, byte-identically, on fresh items (the point of the run).** The decisive
  firewall clears CI-LB > 0 in 2/3 again — and the two confirming legs land **within v1's CIs** (claude
  v1 +0.040 [0.022, 0.059] → rep2 +0.035 [0.019, 0.051]; gemini v1 +0.072 [0.049, 0.095] → rep2 +0.057
  [0.032, 0.080]). With the scored object string held **identical** across conditions and only the
  preceding discourse varying, claude and gemini prefer the **split** order more when the object is
  discourse-given than when it is mentioned-but-referentially-new — a reader that had only learned which
  order-string is more frequent, or that only reacted to the object noun being recently mentioned, scores
  **zero** here. The dative's discourse-structural effect **generalizes to a new construction**, now on
  **two disjoint item sets**.
- **gpt is a SHADOW again, and the enlargement did NOT rescue it (the honest negative).** gpt shows a clear
  definite→split shift (+0.100, 40/48) but its firewall shift is **+0.005** (CI [−0.027, 0.036], 24/48,
  sign-p 0.56) — indistinguishable from zero. The rep2 enlarged the firewall arm 40 → 48 frames
  *specifically* to power this leg (v1 gpt +0.018), and it **still** does not clear CI-LB > 0 — in fact its
  point estimate is *lower* than v1's. So the enlargement was well-powered enough to have detected a small
  true effect and did not, which strengthens (does not merely repeat) the reading that **for gpt the
  determiner effect is a surface/lexical shadow, not information-structure tracking**. gpt is the weak leg
  **again** (weakest on the dative, marginal on the genitive firewall, SHADOW on the particle firewall
  twice). This is exactly the pre-named SHADOW branch — the enlargement powers, it does not guarantee.
- **The referential effect is real but small — and much smaller than the end-weight constraint.** The
  firewall shifts (≈0.035–0.057) are a fraction of the **length/end-weight** effect (+0.31–0.39, 3/3, every
  frame positive). The panel tracks the *processing/end-weight* soft constraint robustly and the
  *referential-givenness* soft constraint weakly-but-detectably (2/3) — a gradient of constraint-tracking,
  reproduced from v1.
- **Magnitudes decorrelate across models, again.** On the decisive firewall gemini (+0.057) > claude
  (+0.035) > gpt (+0.005, fails); on the descriptive given-new gap the spread is ~18× (gemini +0.199 ≫
  claude +0.089 ≫ gpt +0.011). A concordant panel *direction* (for the two confirming models) hides a wide
  magnitude spread — the dative / genitive / CC pattern (the concordant-verdict-hides-spread texture).

## Supplementary robustness read (disclosure condition 2 — non-decisive; does NOT relabel the verdict)

The pre-registered verdict is the frame bootstrap above. As a disclosed sensitivity check on the pair-reuse
structure (below), the decisive firewall shift₂ was recomputed two further ways from `raw/` (own seed
20260715; these **supplement**, never replace, the pre-registered reading):

| Model | Pre-registered frame bootstrap (48) | **28 unique-pair frames only** | **Pair-clustered bootstrap (all 48; cluster = verb+particle pair)** |
|-------|--------------------------------------|--------------------------------|----------------------------------------------------------------------|
| claude | +0.035 [0.019, 0.051] | +0.034 [0.014, 0.054] | +0.035 [0.018, 0.053] |
| gemini | +0.057 [0.032, 0.080] | +0.050 [0.014, 0.084] | +0.057 [0.031, 0.082] |
| gpt | +0.005 [−0.027, 0.036] | +0.000 [−0.042, 0.040] | +0.005 [−0.029, 0.037] |

The CONFIRM survives both: claude and gemini keep CI-LB > 0 on the strict 28-unique-pair restriction (no
intra-pair correlation at all) **and** under a pair-clustered bootstrap that fully absorbs any intra-pair
correlation from the 10 recurring pairs; gpt stays SHADOW (CI includes 0) in both. The pair-clustered CI is
essentially identical to the frame bootstrap — the anti-conservative bias the pre-run critic flagged is
**negligible in the data**, as predicted (paired frames carry different nouns + contexts → low intra-pair
correlation). The verdict is not relabeled.

## Honest fences (R1, R4, R6 — unchanged from v1) + the 4 pre-run-critic disclosure conditions

- **Narrowly directional; not "the distributional shadow is defeated" (R1).** The byte-identity + the
  NEW-MENTIONED condition exclude scored-string shortcuts and object-noun lexical recency — the strongest
  logprob-free shortcut controls available — but **not** the panel reproducing the human context→order
  joint distribution from pretraining. The claim is that claude and gemini track the givenness *sign* in
  the human direction, robustly to those shortcuts, nothing stronger.
- **Firewall-borne CONFIRM, scoped away from the determiner effect (R4).** The decisive evidence is the
  byte-identical firewall (2/3), not the confoundable Arm-1 determiner contrast; gpt's determiner effect is
  precisely the surface shadow the firewall is built to catch, and it is caught (twice). No Arm-1 reversal.
- **The covariate is near-vacuous; CONFIRM rests on the firewall (R1/R7).** The frozen UD-EWT
  per-(verb+particle) marginal split-rate covariate has essentially no predictive validity for the per-frame
  definiteness shift (R² 0.004 / 0.000 / 0.001; slope negative all three; b0 CIs positive but that is the
  definiteness shift itself, not covariate corroboration), because particle-verb tokens are sparse in a
  small corpus. Corroboration-only and weak; the reading rests on Arm 2. **(Disclosure condition 4:** the
  covariate is byte-frozen from v1, so its x-values are duplicated for the 10 recurring pairs; non-gating.**)**
- **Human-anchored on the sign only; restatement caveat (R6).** The direction tested (definite / given
  object → split) is a native-speaker fact from Kim et al. (2016) / Gries (1999), so the result makes a
  calibrated human-comparison claim on the **direction**. The anchor is a **restatement** (not a fresh
  rating experiment), so it grounds the **sign only**; the per-item human gradient is license-unverified
  (deferred to a scout). **May NOT:** claim human-*level* particle-placement competence; claim any per-item
  human gradient; claim the effect beats the distributional shadow beyond the firewall; make any
  cross-linguistic claim.
- **Pair-reuse structure (disclosure conditions 1 + 3).** The 48 frames use **38 distinct verb+particle
  pairs**: 28 frames whose pair appears once, plus 10 pairs each appearing twice (frames f39–f48 re-use one
  of f01–f38 with a **fresh noun + fresh context**, so each is a new triple/frame). Every pair is drawn from
  v1's frozen 38-pair set — this is **required** to keep the covariate + `analyze.py` `VERB_LEMMA` byte-frozen
  (any outside pair would KeyError the covariate or force a re-freeze, breaking the A2a byte-frozen-instrument
  discipline). The duplicate-pair selection criterion was **linguistic** ("flexible / both-orders-natural"),
  **not** v1-outcome-based; and because the decisive firewall is a **within-frame** contrast (verb, particle,
  noun, and the entire scored string byte-identical across GIVEN/NEW-MENTIONED/NEW), a pair's baseline
  split-propensity enters both means identically and **cancels** — so pair-reuse cannot import v1's firewall
  magnitude and cannot carry the effect (certification check (2): 7 scored-string readers each yield
  within-frame shift₂ = 0). The **only** residual is that the frame bootstrap is mildly anti-conservative
  under intra-pair correlation (10 recurrences vs v1's 2) → this affects interval **width** only, not point
  estimates, and is shown negligible by the pair-clustered read above.

## Anchor

[`resource/particle-placement-givenness-human-anchor`](../../base/resources/particle-placement-givenness-human-anchor.md)
— the native-speaker **direction** (definite / discourse-given object → split order) from
[`source/kim-2016-particle-placement`](../../base/sources/kim-2016-particle-placement.md) (Kim et al.
2016, CC BY 4.0, verified firsthand; corroborated by Gries 1999). A genuine human-comparison leg on the
**sign** — the same tier as the dative and genitive direction legs. The byte-identical firewall arm is an
internal within-model shortcut control.

## Provenance + reproduction

Frozen run: [`experiments/runs/2026-07-15-particle-placement-givenness-rep2/`](../../../experiments/runs/2026-07-15-particle-placement-givenness-rep2/)
(`stimuli.json` sha `3544656488…`, `freq_control.json` sha `cd472475…` [byte-identical to v1], both pinned
in `PREREG.md`; `probe.py full` refuses to run unless both shas appear there). Instrument bytes sha-verified
identical to the v1 dir (`2026-07-14-particle-placement-givenness/`). Covariate corpus UD English-EWT
(CC BY-SA 4.0, LICENSE verified firsthand s218). Frozen + pre-run-gated s228 (build certification PASS incl.
disjointness (D); independent parallelism/disjointness certification **CERTIFY-B**; non-Anthropic
decorrelation vote NO-GO on pair-reuse **weighed-and-declined-on-merits** by the fresh-agent pre-run critic
→ **GO-WITH-CONDITIONS** with the 4 post-run disclosures honored above;
[`note/particle-placement-givenness-rep2-freeze-v1`](../notes/particle-placement-givenness-rep2-freeze-v1.md)),
**run executed s229** on a fresh full-$5 UTC day (2026-07-15). Nothing was peeked before analysis. An
**independent post-run fresh-agent verifier** recomputed every headline statistic from the raw jsonl with
its own script and an independent bootstrap seed (999333) → **REPRODUCED** (0 material discrepancies — all
point estimates match to 4 dp, all frame-positive counts and per-model + panel verdicts reproduce, total
cost $3.17645 reproduced, both shas verified; CI bounds within ≤0.001 bootstrap jitter). Do **not** re-run
or retune the frozen dir; a FALSIFY/reversal would trigger a pre-registered v2, never a re-run. Registered
replication bet in [`predictions.md`](../../predictions.md) updated (**fired-for**).

## What this feeds

The **fresh-item replication** the v1 single-run flag needed. Together with
[`result/particle-placement-givenness-v1`](particle-placement-givenness-v1.md) this is **two controlled
runs on certified-disjoint item sets**, both PANEL CONFIRM with the firewall clearing CI-LB > 0 in 2/3 and
gpt a persistent SHADOW — the [`PROTOCOL.md §3`](../../../PROTOCOL.md) **REPLICATED ∧ controls-survived**
bar. It is the direct input to a cross-session promotion review, which — if it promotes — writes a
**direction-only, 2/3-firewall** particle `claim` (scoped below the genitive's 3/3-firewall claim: the
particle's load-bearing leg replicates at **2/3, not 3/3**, gpt a SHADOW both times) and migrates the
[`theory/shadow-depth-table-v4`](../theory/shadow-depth-table-v4.md) particle row **result-cited →
claim-cited**. Per the theory-edition rule, folding into the table is a later consolidation. This result
stays `proposed` (the reading-bearing lifecycle default; support, if promoted, migrates to the claim layer).
