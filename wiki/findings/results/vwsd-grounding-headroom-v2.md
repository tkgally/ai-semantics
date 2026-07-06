---
type: result
id: vwsd-grounding-headroom-v2
title: "VWSD grounding-headroom probe v2 — the re-operationalized (non-caption, stratified N=120, raised-max_tokens) run SUPPORTS the gating SHAPE: with the word-ablated DISTRACT control clean (pooled .097 ≈ chance), the image rescues the descriptor-text-failed (under-determined) cells at .453 pooled (per-model .500 claude / .303 gpt / .609 gemini, all > chance) while it does NOT lift the cells the descriptor already separates (saturated Δ −0.122) — image-conditioned sense selection is gated by descriptor-text separability, 3/3 models in the predicted direction. The first confirming-direction VWSD evidence (v1 was inconclusive). Caveats foregrounded: gemini's Option-A floor is elevated (.158, Wilson LB .104 > chance); gpt degrades overall (.725→.592, gating visible only in its residual, sign-only); the headroom MAGNITUDE is inflated by the deliberately de-referented Option-B descriptor channel, so this supports the gating SHAPE, NOT the conjecture's 'narrow headroom' magnitude sub-bet, and remains gating-shape-on-binary-selection, NOT prediction-1-as-written (no graded relatedness), NOT reference."
meaning-senses:
  - grounded.perceptual
  - referential.sense
  - human-comparison
  - distributional
status: proposed
anchor: human-anchored
contingent-on: []
created: 2026-06-27
updated: 2026-07-05
links:
  - rel: depends-on
    target: conjecture/distributional-saturation-grounding-headroom
  - rel: anchors
    target: resource/vwsd-semeval-2023
  - rel: depends-on
    target: resource/vwsd-semeval-2023
  - rel: refines
    target: result/vwsd-grounding-headroom-v1
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/polysemy
---

# Result: VWSD grounding-headroom probe v2 — the gating SHAPE is supported (3/3 in direction, distraction-controlled); first confirming-direction VWSD evidence; magnitude inflated by the de-referented channel and so not the "narrow headroom" bet

> **Status: proposed (2026-06-27, session 121).** The completed **run** of the v2
> re-operationalization, finishing the multi-day day-split design: day-1 text-only freeze (s107),
> IMAGE arm (s112), and now the **DISTRACT word-ablated control** (this session, the last arm), which
> the design requires reported and credited **first**. Built + frozen under the ratified gate
> [`decisions/resolved/vwsd-grounding-headroom-dv-v2`](../../decisions/resolved/vwsd-grounding-headroom-dv-v2.md)
> (ADOPT-DEFAULT). Frozen design:
> [`design/vwsd-grounding-headroom-v2`](../../../experiments/designs/vwsd-grounding-headroom-v2.md).
> It operationalizes the **gating shape** of prediction 1 of
> [`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
> on VWSD — **explicitly NOT prediction-1-as-written** (no graded human relatedness gradient).
> Frozen artifacts (checksums verbatim-in-force): `frozen/descriptors.json` sha `26616a55…` (1889
> Option-B visual-form descriptors + Option-C leak audit); `frozen/run_items.json` sha `7f9e52fa…`
> (stratified N=120, seed 20260625); `raw/text.json` sha `3a9dfcbf…` (the separability covariate,
> **frozen + checksummed before any image condition**); `raw/image.json` sha `6884eea0…430870`
> (IMAGE arm, s112). DISTRACT arm `raw/distract.json` sha `f8fbb6be…` (this session). The s108
> independent **pre-run critic GO** (against the observed `sep_i`/`leak_i` distributions) gated the
> image-bearing arms; an **independent fresh-agent post-run verifier REPRODUCED every
> finding-bearing number from raw** (1440/1440 records consistent; the precomputed `correct` field
> matches recomputed `pick==gold_idx` in all records; verdict PASS-WITH-NITS, all nits caveats
> already carried below). **360 DISTRACT calls, `usage.cost`-summed, 0 missing-cost, 0 parse-fails;
> $3.76317 billed** (two ~60-item sub-batches, $1.873 + $1.890, each under the $2.50 single-run
> flag), + $0.062 preflight → **$3.825 day total**, under the $5/day cap.

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The natural-language-baseline run owed
> by Limitation 1 was built and frozen, then twice stopped short of a magnitude read:
> [`note/vwsd-grounding-headroom-nlbaseline-audit-v1`](../notes/vwsd-grounding-headroom-nlbaseline-audit-v1.md)
> (session 127, deferred at the adequacy-audit gate) and
> [`note/vwsd-grounding-headroom-nlbaseline-regrade-v1`](../notes/vwsd-grounding-headroom-nlbaseline-regrade-v1.md)
> (session 128, re-graded under a ratified valid scorer — 0.438, still below the [0.60, 0.95]
> competence floor). The magnitude was then documented un-instrumentable on current open resources —
> [`open-question/grounding-magnitude-instrument`](../open-questions/grounding-magnitude-instrument.md)
> (an externally-released graded-image fine-polysemy set is the only route).
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

## What was run

The full v2 pipeline over a frozen **stratified N=120** EN-gold subset of the SemEval-2023 VWSD
**English gold test** (human-curated 1-of-10 image selection; gold = the human-selected correct image
after human-authored trigger words + human distractor curation). Five arms, all three panel models
(claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash); images low detail; gemini
`reasoning:{effort:"minimal"}`:

- **DESCRIPTOR (Option B, frozen pre-image).** Each unique candidate image described once by gemini
  under a visual-form-only policy **barred from naming the referent** (v1's captions named it; that was
  v1's deepest confound). Frozen + checksummed before any selection arm.
- **TEXT (descriptor-based selection)** — the per-item separability covariate AND the improvement
  baseline; **frozen to `raw/text.json` before the image arm** (no retuning). `sep_i` = fraction of the
  3 models text-correct (0, 1/3, 2/3, 1).
- **FLOOR (Option A)** — bare index labels, no descriptor and no image; calibration arm that must sit
  at/near chance (confirms the linguistic context alone does not leak).
- **IMAGE** — same prompt, candidates shown as the ten real images; **claude `max_tokens` raised
  16→512** (condition d — removes v1's truncation bias; 0 parse-fails here, all three models).
- **DISTRACT** — word-ablated control (ten images, **no target word or trigger**): "pick the most
  prototypical / canonical / everyday image." Reported **FIRST** (binding condition 3).

The images are **out of git** (redistribution unconfirmed — [`resource/vwsd-semeval-2023`](../../base/resources/vwsd-semeval-2023.md),
License & redistribution; the 572 MB EN zip was re-fetched at runtime, sha256 `b9f2f1e1…af8f`
re-verified exactly, never re-hosted). The annotation overlay (queries + gold) and the descriptors ARE
committed; `raw/distract.json` records the 1–10 selection and `usage.cost` per call, never image bytes.

## Headline

Unlike v1 — which **could not test** the gating interaction (caption-leakage confound + only 7
under-determined items, below floor) — v2's non-caption descriptor baseline left a **real, adequately
powered under-determined stratum** (35 items / 86 text-failed cells, both bins clearing the ≥15 floor),
and the result is now interpretable. **The gating shape is supported, 3/3 models in the predicted
direction, distraction-controlled.** With the word-ablated DISTRACT control **clean** (pooled .097 ≈
chance; no model's Wilson lower bound exceeds .10), the real image **rescues the cells where the
descriptor-text failed** — pooled **39/86 = .453** [.353, .558], per-model **.500 / .303 / .609** (all
above chance) — while adding **no lift where the descriptor already separates** (image actually drops
.122 in the saturated stratum). That is the conjecture's prediction-1 *shape*: perceptual input moves
sense selection **in the residual the (sense-fixing) text under-determines, not where text already
separates**, and the clean DISTRACT control licenses reading the lift as word→sense→image grounding
rather than image salience. **This is the project's first confirming-direction VWSD evidence.**

Three honesty bounds are foregrounded, not buried: (i) **gemini's floor is elevated** (.158, Wilson LB
.104 > chance), so gemini's strong rescue (.609) is partly discounted — claude (floor .092, clean) and
pooled carry primary weight; (ii) **gpt degrades overall** (.725→.592), with its gating support
**sign-only** (text-failed rescue .303, wide CI, near its own behavior); (iii) the **magnitude** of the
headroom is **inflated by the deliberately de-referented Option-B channel** — the under-determined
stratum is partly *manufactured* by stripping referent names from the descriptors, so this supports the
gating **shape**, **not** the conjecture's "narrow headroom" magnitude sub-bet (prediction 3). And it
remains **gating-shape-on-binary-selection**, **not** prediction-1-as-written (no graded relatedness),
**not** reference.

## Results, in the mandated order

### 1. Distraction null — FIRST (binding condition 3) — CLEAN

Word-ablated gold-selection (no target word or trigger; chance = 0.10):

| model | gold-selected | rate | Wilson 95% | above chance? |
|---|---|---|---|---|
| claude | 16/120 | 0.133 | [0.084, 0.206] | no (LB < .10) |
| gpt | 5/120 | 0.042 | [0.018, 0.094] | no (below chance) |
| gemini | 14/120 | 0.117 | [0.071, 0.186] | no (LB < .10) |
| **pooled** | **35/360** | **0.097** | **[0.071, 0.132]** | **no — at chance** |

**Gold images are not intrinsically salient: with the word removed, all three models pick gold at
chance.** The control **passes** — any image-conditioned gold-selection is **word/sense-driven, not
surface-salience-driven**. This is the load-bearing positive control, and it is clean; it is what makes
the §3 rescue creditable as grounding headroom rather than image salience or a position/format artifact.

### 2. Main accuracy per arm per model

| arm | claude | gpt | gemini |
|---|---|---|---|
| TEXT (Option-B descriptors) | 90/120 = .750 | 87/120 = .725 | 97/120 = .808 |
| IMAGE (real images) | 102/120 = .850 | 71/120 = .592 | 104/120 = .867 |

The non-caption descriptor baseline is **not saturated** (.725–.808 vs v1's referent-naming captions at
.86–.88), leaving genuine text-failed headroom — the point of v2. With real images, **claude (+.100)
and gemini (+.059) improve**, but **gpt is markedly WORSE** (.725→.592) — the same model-specific
**anti-grounding** signal v1 found (for gpt, the visual modality is noisier than a text description of
the same content). Net image≥text is therefore **not** the finding; the finding is *where* the image
helps (§3), which is gated even for gpt.

### 3. Test of record — image rescue by text outcome (binned interaction now CREDITED)

Both reported strata clear the ≥15 floor (under-determined 35 ≥ 15; saturated 85 ≥ 15) — so unlike v1
the binned interaction **is** credited. The load-bearing read is the item×model **cell-level** rescue
(less contaminated than the item-mean stratum Δ below):

| cell type | image-correct | rate | Wilson 95% |
|---|---|---|---|
| **text-FAILED cells** (descriptor wrong) | 39/86 | **0.453** | [0.353, 0.558] |
| text-OK cells (descriptor right) | 238/274 | 0.869 | [0.823, 0.904] |

Per model, text-FAILED rescue (all above chance .10, and above each model's own floor):

| model | text-FAILED rescue | Wilson 95% |
|---|---|---|
| claude | 15/30 = **.500** | [0.332, 0.668] |
| gpt | 10/33 = **.303** | [0.174, 0.473] (sign-only; near its floor) |
| gemini | 14/23 = **.609** | [0.408, 0.778] (read against gemini's elevated .158 floor) |

**Where the de-referented descriptor under-determined the sense, the real image rescued ~45% of cells
pooled** — far above chance, and (since the DISTRACT control is clean) sense-driven, not salience. In
the cells the descriptor already got right, the image did **not** add (it retained .869, in fact losing
some — concentrated in gpt). The lift is concentrated in the residual. This is the gating shape.

### 4. Strata view (per-item mean accuracy; companion to §3, carries the mechanical caveat)

| stratum | n items | mean TEXT | mean IMAGE | Δ (image − text) |
|---|---|---|---|---|
| saturated (`sep_i` = 1) | 85 | 1.000 | 0.878 | **−0.122** |
| under-determined (`sep_i` ≤ 1/3) | 35 | 0.181 | 0.505 | **+0.324** |

The sign contrast is in the predicted direction, but this item-mean Δ is **partly mechanical and is NOT
the headline**: (a) the saturated stratum's text is pinned at 1.000 by construction, so its Δ can only
be ≤ 0 (floor asymmetry); (b) the under-determined stratum is *defined* by text-failure, so an
independent image signal yields an apparent "rescue" partly by selection-on-the-conditioning-variable.
The non-mechanical evidence is the **cell-level rescue rate (§3) sitting well above both chance and every
model's floor**, plus the **clean DISTRACT control (§1)** — together these establish a real image signal
beyond the mechanical story. The continuous Spearman/OLS slope is **doubly weakened** (mechanical
ceiling + the empty 2/3 band, binding condition 2) and is **not reported as a test**.

### 5. Calibration + leak audit (the instrument checks)

- **Option-A FLOOR** (bare index labels; target chance .10): claude .092 [.052,.157] (clean), gpt .117
  [.071,.186] (near-clean), **gemini .158 [.104,.234] — Wilson LB .104 > chance** (binding condition
  1). Pooled .122 [.092,.160]. The linguistic context + a position/label prior does a little covert
  work **for gemini specifically**; gemini's reads are referenced against its own ~.158 floor, not bare
  .10, and claude + gpt + pooled carry primary weight.
- **Option-C LEAK audit** (held-out gpt referent recovery; 0 none / 1 partial / 2 high over the 200
  pool): 154 / 20 / 26 → high-leak rate **.130**; Spearman(`leak_i`, `sep_i`) = **.160** over the 120
  in common — a **weak** positive (mild residual contamination, short of the strong correlation that
  would trigger the Option-C circularity warning). 13% of gold descriptors still let gpt recover the
  exact target word; this covariate is **carried, never regressed out**.

## What this establishes / does not (Q3 narrow posture)

- **Establishes:** on a human-anchored, image-native sense-selection task, with a **clean distraction
  control** and a non-caption separability baseline, **image-conditioned sense selection is gated by
  descriptor-text separability** — the real image rescues the under-determined residual (pooled .453,
  3/3 models in direction) and adds nothing where the descriptor already separates. This is the
  **gating SHAPE** of [`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
  prediction 1, and the **first confirming-direction** evidence the project has on the grounding axis
  (v1 was inconclusive; the two prior clear-homonym grounding results were nulls). It is the redundancy
  null's mirror image: where v1/the image-redundancy result saw **Δ ≈ 0 at saturation**, v2 now sees
  **Δ > 0 in the residual** — the same structural story, with the positive cell finally testable.
- **Does NOT establish:** (i) **not** prediction-1-as-written — VWSD gold is **binary** correct-image,
  not a graded human relatedness gradient; this is selection accuracy, not graded similarity; (ii)
  **not** the conjecture's **"narrow headroom" magnitude bet** (prediction 3) — the under-determined Δ
  is *large* (+.324 / .453 rescue), but that magnitude is **inflated by the deliberately de-referented
  Option-B descriptor channel** (the residual is partly manufactured by stripping referent names), so
  the magnitude here speaks to the instrument, not to "how narrow concrete-sense headroom is in natural
  use"; (iii) **not** reference — `referential.externalist` untouched; a model picking the gold image
  shows behavior *sensitive to* the word→sense→image mapping in the residual, **not** a perceptual
  symbol system or reference-fixing; (iv) **not** a uniform-across-models effect — gpt degrades overall
  and its gating support is sign-only.

## Limitations (first-class — read before citing)

1. **The headroom magnitude is operationalization-inflated.** The TEXT arm uses Option-B descriptors
   that *deliberately* strip the referent name (the v2 fix for v1's caption leakage). So "text-failed"
   means "the visual-form-only descriptor + target word + trigger under-determined the sense," not "a
   competent natural-language description failed." The image rescuing ~45% of such cells confirms the
   gating **shape** but says nothing about the **size** of the residual a fluent text channel would
   leave — that is why prediction 3 ("narrow headroom for concrete sense") is **not** supported or
   refuted here. A natural-language (non-abstracted) baseline would test magnitude; v2 tests shape.
2. **The item-mean stratum Δ (+.324 / −.122) is partly mechanical** (floor asymmetry at saturation +
   selection on the text-failure conditioning variable). The cell-level rescue (§3) above chance and
   above each model's floor, with the clean DISTRACT control, is the part that is not mechanical; the
   writeup leads with it and demotes the stratum Δ to a caveated companion.
3. **gemini's Option-A floor is elevated** (.158, LB .104 > chance) — gemini contributes the largest
   text-failed rescue (.609), so this is foregrounded, not footnoted; gemini-specific reads are
   discounted against its own floor and claude/pooled carry primary weight.
4. **gpt's confirming direction is the weakest** — text-failed rescue .303 [.174, .473] is wide and
   near its own behavior; gpt also degrades overall (.725→.592). gpt's support is sign-only.
5. **Bimodal separability, empty 2/3 band** (binding condition 2): `sep_i ∈ {0, 1/3, 1}` with **0**
   intermediate items, so the binned saturated-vs-under-determined contrast is the test of record and
   the graded sep→rescue slope stays descriptive-only.
6. **Power / coarseness (MANDATORY).** N=120 of the 463 EN gold, binary per-item accuracy, a coarse
   read. A positive read in the predicted direction is **support for the gating shape**, not proof of a
   law; the magnitude is instrument-bound (limit 1).
7. **VWSD resource caveats carried forward, verbatim in force** (all from
   [`resource/vwsd-semeval-2023`](../../base/resources/vwsd-semeval-2023.md)): **binary gold** (no
   graded signal); **limited annotator independence** (English annotators "includ[ed] the authors of
   this paper"; BabelNet-automatic seed; no inter-annotator agreement reported); **image
   redistribution unconfirmed** (images out of git, fetch-at-runtime only, never re-hosted); **anchored
   only to the gold test split** (the 12,869 training instances are silver).

## Bearing on the conjecture

[`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
predicts grounding helps **only in the text-under-determined residual** (prediction 1, gating shape),
that the redundancy null is **regime-specific not modality-specific** (prediction 2), and that the
residual headroom for concrete sense is **narrow** (prediction 3). This run:

- **Supports prediction 1's gating shape** (3/3 in direction, distraction-controlled) — the strongest
  evidence the project has for it, and the first positive cell on the grounding axis.
- **Supports prediction 2's regime-specificity** — the redundancy null (Δ ≈ 0) reappears in the
  saturated stratum while Δ > 0 appears in the matched under-determined stratum, same panel + instrument,
  opposite Δ.
- **Does NOT support prediction 3's "narrow headroom" magnitude bet** — the residual headroom here is
  *wide* (.453 rescue), but inflated by the de-referented channel (limit 1), so this neither confirms
  nor refutes prediction 3; a natural-language-baseline run is owed to test magnitude.

At this run (session 121) the conjecture was held **`proposed`** — a single supporting run on a binary
selection task, with the magnitude sub-bet untested, did not warrant promotion *that* session, and
promotion is in any case a later session's cross-session call (charter §12.3). **Session 130 made that
call: an independent cross-session adversarial review promoted the conjecture `proposed → tested` for the
GATING SHAPE ONLY (predictions 1–2), with prediction 3 held explicitly UNTESTED** (see
[`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md),
status block). This run is the confirming-direction evidence that promotion rests on — the grounding axis
now carries a **confirming-direction** result alongside the two nulls and v1's inconclusive run.
prediction-1-as-written (graded relatedness × separability) remains open for a future graded-image
resource, and the magnitude (prediction 3) remains untested.

## Anti-cheat note (the binding guards, honored)

- **DISTRACT null reported and credited FIRST** (binding condition 3); no image lift was read as
  headroom before the control was shown clean.
- **No retuning.** The Option-B descriptors, the `leak_i` audit, the N=120 draw, and the per-model
  separability covariate (`raw/text.json` sha `3a9dfcbf…`) were all frozen + checksummed **before** the
  image and distract arms; the verdict was read off the frozen covariate, not a post-hoc re-bin. No bin
  was widened; the empty 2/3 band was left empty, not filled.
- **Gemini floor elevation foregrounded** (binding condition 1), not used to inflate a pooled positive.
- **The graded slope demoted** to descriptive-only (binding condition 2); the mechanical components of
  the stratum Δ are stated in the same breath as the Δ itself, and the headline leans on the cell-level
  rescue + the clean control instead.
- **Independent fresh-agent post-run verifier** re-derived every finding-bearing number from raw
  (1440/1440 records consistent), confirmed all three binding conditions hold, and judged the verdict
  calibrated (PASS-WITH-NITS; the nits are the caveats carried above).
- **Under-claimed by construction:** the one read that could most overstate (the +.324 stratum Δ) is
  explicitly demoted for its mechanical content, the magnitude sub-bet is declared *not* supported, and
  the scope is held to gating-shape-on-binary-selection — not reference, not graded relatedness.
