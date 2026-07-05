---
type: result
id: vwsd-grounding-headroom-v1
title: "VWSD grounding-headroom probe v1 — the caption-text baseline SATURATES (per-model .86–.88; 40/50 items text-separable by all three models), leaving only 7 under-determined items, below the pre-registered stratification floor. Per the frozen design the binned gating interaction is NOT reported. The distraction control is clean (word-ablated gold-selection at chance, pooled .093); real images do NOT broadly beat their captions (gpt is WORSE with images: .60 vs .86) and rescue only 4/16 text-failed cells. This neither confirms nor falsifies the grounding-headroom gating prediction on VWSD; the saturation — driven partly by caption informativeness — is the primary finding."
meaning-senses:
  - grounded.perceptual
  - referential.sense
  - human-comparison
  - distributional
status: proposed
anchor: human-anchored
contingent-on: []
created: 2026-06-24
updated: 2026-07-05
links:
  - rel: depends-on
    target: conjecture/distributional-saturation-grounding-headroom
  - rel: anchors
    target: resource/vwsd-semeval-2023
  - rel: depends-on
    target: resource/vwsd-semeval-2023
  - rel: refines
    target: result/multimodal-grounding-image-v1
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/polysemy
---

# Result: VWSD grounding-headroom probe v1 — caption-text saturates; clean distraction null; no broad image lift; gating neither confirmed nor falsified

> **Status: proposed (2026-06-24, session 100).** The first **run** of the VWSD grounding-headroom
> probe, built + frozen this session under the ratified DV decision
> [`decisions/resolved/vwsd-grounding-headroom-dv`](../../decisions/resolved/vwsd-grounding-headroom-dv.md)
> (ADOPT MODIFIED: Option A / interaction-as-test-of-record / Q3 narrow human-anchored posture, five
> binding mods). Frozen design: [`design/vwsd-grounding-headroom-v1`](../../../experiments/designs/vwsd-grounding-headroom-v1.md).
> It operationalizes the **gating shape** of prediction 1 of
> [`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
> on VWSD — **explicitly NOT prediction-1-as-written** (no graded human relatedness gradient).
> Frozen artifacts: `run_items.json` sha `657fceb7…` (50-item seeded subset, seed 20260624);
> `captions.json` sha `528772e4…`; `raw/text.json` sha `ff6289bb…` (the separability covariate,
> **frozen + checksummed before any image condition**, binding mod 2). **Independent fresh-agent
> pre-run critic GO** (result-neutral; required the binned interaction suppressed and barred any
> gating confirm/falsify claim — see Anti-cheat) **+ independent post-run verifier REPRODUCED** every
> finding-bearing number from raw. **450 finding-bearing calls** (text 150 + image 150 + distract 150),
> **`usage.cost`-summed, 0 missing**; **$3.204 billed for the three arms** ($0.0667 text / $1.572 image
> / $1.565 distract); **$4.091 with the $0.887 caption pass**; **$4.260 day total** with ~$0.17
> preflights, under the $5/day cap. 6 image parse-fails (all claude, reasoning-then-truncation on
> rare-phrasing items — see Limitations).

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The re-operationalized v2 ran
> (sessions 107/112/121): [`result/vwsd-grounding-headroom-v2`](vwsd-grounding-headroom-v2.md)
> removed this run's caption confound and returned the first confirming-direction positive
> (gated-rescue shape: the image rescues descriptor-text-failed cells, 3/3 models in direction,
> distraction-controlled), and [`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
> was promoted `tested` (gating shape only) in session 130.
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

## What was run

A frozen **50-item seeded subset** of the SemEval-2023 VWSD **English gold test** (the human-curated
1-of-10 image-selection task; gold = the human-selected correct image after human-authored trigger
words). Three behavioural arms, all three panel models (claude-sonnet-4.6 / gpt-5.4-mini /
gemini-3.5-flash); images low detail; gemini `reasoning:{effort:"minimal"}`:

- **TEXT** — text-only **caption-based** selection (candidates shown as short neutral gemini-authored
  captions, no images). This is BOTH the per-item text-only separability covariate AND the baseline
  for image-induced improvement; **frozen + checksummed before the image arm**.
- **IMAGE** — the same prompt, candidates shown as the ten real images.
- **DISTRACT** — word-ablated control (ten images, **no target word**; "pick the most prototypical /
  canonical image"). Reported FIRST (binding mod 3).

The images are **out of git** (redistribution unconfirmed — [`resource/vwsd-semeval-2023`](../../base/resources/vwsd-semeval-2023.md)
License & redistribution; fetched at runtime, checksummed, never re-hosted). The annotation overlay
(queries + gold) and the captions ARE committed.

## Headline (the framing the pre-run critic required)

On this frozen 50-item subset the **text-only caption baseline saturates** (per-model accuracy
.86–.88; **40/50 items text-separable by all three models**), leaving only **7 under-determined
items — below the pre-registered stratification floor of 8**. Per the frozen design, the **binned
gating interaction is therefore NOT reported**. We report: (a) the **distraction-control null**; (b)
**main caption-text vs image accuracies**; (c) a **descriptive image-rescue rate** among the text-failed
cells, denominator-bounded and **not a test**; (d) a Δ~separability companion carried with the
binary-ceiling caveat. **This probe neither confirms nor falsifies the grounding-headroom gating
prediction on VWSD**; a flat result is *"no detectable gating OR underpowered"* (binding mod 4), and
the saturation itself — driven partly by **caption informativeness** — is the primary finding.

## Results, in the mandated order

### 1. Distraction null — FIRST (binding mod 3) — CLEAN

Word-ablated gold-selection (no target word; chance = 0.10):

| model | gold-selected | rate | Wilson 95% |
|---|---|---|---|
| claude | 3/50 | 0.060 | [0.021, 0.162] |
| gpt | 5/50 | 0.100 | [0.043, 0.214] |
| gemini | 6/50 | 0.120 | [0.056, 0.238] |
| **pooled** | **14/150** | **0.093** | **[0.056, 0.151]** |

**Gold images are not intrinsically salient: with the word removed, models pick gold at chance**, and
the picks are spread across all ten positions (no constant-default artifact). The control **passes** —
any image-conditioned gold-selection is **word/sense-driven, not surface-salience-driven**. This is the
load-bearing positive control, and it is clean.

### 2. Main accuracy per arm per model

| arm | claude | gpt | gemini |
|---|---|---|---|
| TEXT (captions) | 44/50 = .88 | 43/50 = .86 | 43/50 = .86 |
| IMAGE (real images) | 39/44 = .886* | **30/50 = .60** | 44/50 = .88 |

\* claude image denominator is 44, not 50 — 6 truncation parse-fails (Limitations).

**Real images do not broadly beat their captions.** claude and gemini roughly match their caption
baseline; **gpt is markedly WORSE with real images than with their captions** (.60 vs .86 — **15
items text-correct-from-caption but image-wrong**). For gpt, the visual modality is *noisier* than a
text description of the same content — a model-specific anti-grounding signal, not a lift.

### 3. Separability distribution + strata (binding mod 1 — floor NOT met)

Per-item `sep_i` = fraction of 3 models text-correct: `sep=1.0` → **40**; `sep=0.667` → 3;
`sep=0.333` → 4; `sep=0.0` → 3. **Saturated (sep=1): 40. Under-determined (sep≤1/3): 7 — below the
floor of 8.** The binned saturated-vs-under-determined interaction is **not credited and not
reported** (the frozen fallback fired automatically; no post-hoc re-binning — see Anti-cheat).

### 4. Test of record — image-rescue rate by text outcome (DESCRIPTIVE ONLY, not a test)

Item × model cells (parsed):

- **text-FAILED cells: image-correct 4/16 = 0.25** (Wilson [0.10, 0.50]).
- text-OK cells: image-correct 109/128 = 0.85 (Wilson [0.78, 0.90]).

Where the caption-text already failed, **the real image rescued only a quarter of cells (4/16), a CI
that spans chance-to-modest** — the image does **not** clearly rescue the under-determined residual.
This is the gating prediction's *opposite* tendency, but at 16 cells (concentrated on ~10 distinct
hard items, with claude's hardest items lost to truncation — Limitations) it is **far too thin to
test**: a flat/low rescue is *"no detectable gating OR underpowered,"* never proven absence.

Descriptive companion (ceiling-confounded, **not the headline**): Spearman(sep, Δ) = −0.251, OLS slope
= −0.197. The negative sign is **partly mechanical** — saturated items can only have Δ ≤ 0 — so it is
**not** evidence of gating (binding caveat; the design names this).

## What this establishes / does not (Q3 narrow posture)

- **Establishes:** a **clean distraction control** on a human-anchored, image-native sense-selection
  task — gold-selection without the word is at chance — so the models' image-conditioned selection is
  word/sense-driven. And a **bounded negative**: adding the real images does **not** broadly improve
  sense selection over an informative text description of the candidates, and for one model it
  *degrades* it. This is the **redundancy-null spirit** of
  [`result/multimodal-grounding-image-v1`](multimodal-grounding-image-v1.md) reappearing in an
  image-native *selection* task — now with the honest twist that the "text" channel here is a caption,
  so the saturation is partly caption-driven.
- **Does NOT establish:** (i) **not** prediction-1-as-written (no graded human relatedness gradient —
  VWSD gold is binary); (ii) **not** the gating interaction confirmed *or* falsified (floor not met;
  the rescue read is underpowered); (iii) **not** reference — `referential.externalist` untouched; a
  model picking the gold image shows behaviour *sensitive to* the word→sense→image mapping, **not** a
  perceptual symbol system or reference-fixing.

## Limitations (first-class — read before citing)

1. **Caption-leakage contamination of the separability covariate (the deepest limit, per the critic).**
   The text-only baseline is *"can the model pick gold from a **caption** of each candidate,"* and the
   gemini captions are concrete noun phrases that frequently **name the referent** ("a pile of mustard
   seeds"). So `sep_i` conflates "the target word + phrase determines the sense" with "the gold image's
   caption is descriptive enough to match." The conjecture targets the former; the instrument measures a
   blend. The high caption-text accuracy is therefore **not** clean evidence that *language* determines
   the sense — and the whole gating geometry is only weakly identified even setting N aside. This is
   co-equal with the floor failure.
2. **Floor not met / underpowered.** N=50, only 7 under-determined items, ~16 text-failed cells. The
   binned interaction is suppressed and the rescue read is descriptive. A larger, stratified draw (or a
   non-caption text baseline) is needed to test the gating shape.
3. **6 image parse-fails, all claude, on rare-phrasing items** (retard, amit, bovid bag, sea steamer,
   clocks weed, sharp crease) — claude reasoned aloud and was truncated at `max_tokens=16` before
   emitting a number. Four of the six are under-determined (`sep ≤ 1/3`); two (bovid bag, sharp crease)
   are `sep=1` (caption-solvable) but odd-phrasing — so "rare" is exact, "hardest" would overstate for
   those two. The losses **cut both ways**: they **overstate** claude's image accuracy (4 hard items
   dropped) and **understate** the rescue-cell count. They were **deliberately not re-run**: recovering
   claude's hard-item image answers could only *inflate* the rescue read, so leaving them missing is the
   anti-cheat-safe choice (a v2 should raise `max_tokens` for claude).
4. **VWSD resource caveats carried forward** (all from [`resource/vwsd-semeval-2023`](../../base/resources/vwsd-semeval-2023.md)):
   **binary gold** (no graded signal); **limited annotator independence** (English annotators "includ[ed]
   the authors of this paper"; BabelNet-automatic seed; no inter-annotator agreement reported); **image
   redistribution unconfirmed** (images out of git); **anchored only to the gold test split** (training
   is silver). N=50 of the 463 EN gold items.

## Bearing on the conjecture

The grounding-headroom conjecture predicts grounding helps **only in the text-under-determined
residual**, and that residual is **narrow** for concrete sense. This run **cannot test the gating
interaction** (caption confound + floor + underpower), so it leaves prediction 1 **untested** on VWSD.
What it *does* add is consistent with the conjecture's **general posture** rather than against it: on an
image-native selection task, once candidates are described in words the task largely solves from text,
and the real images add no broad lift (and degrade one model) — the **redundancy null reappears**,
now bounded by the caption confound. The conjecture stays **`proposed`**; this is neither a confirming
nor a falsifying run, and prediction-1-as-written remains open for a **future graded-image resource**
(the VWSD scope note already records this).

## Anti-cheat note (the pre-run critic's binding guards, honored)

- **No post-hoc re-binning.** The floor (8) and bin thresholds were frozen in the design and read
  mechanically from the checksummed `raw/text.json`; the under-determined bin (7) was **not** widened to
  manufacture n≥8. The binned interaction is suppressed.
- **No gating confirm/falsify claim.** Barred by the critic; the headline says "neither confirms nor
  falsifies."
- **Slope demoted.** The negative Δ~sep slope is reported only as a ceiling-confounded descriptive, with
  its mechanical sign stated in the same breath.
- **Rescue rate subordinated to the distraction null and denominator-bounded**, with "too few cells to
  test" stated.
- **The one read that could look positive (the binned interaction) is exactly the one the floor
  suppresses; every other honest read here is null-or-negative-leaning** — so a spurious positive is
  structurally hard to manufacture, and none was.
