# Design — VWSD grounding-headroom probe v1 (frozen prereg)

**Status:** frozen design (2026-06-24, session 100). Implements the ratified DV decision
[`decisions/resolved/vwsd-grounding-headroom-dv`](../../wiki/decisions/resolved/vwsd-grounding-headroom-dv.md)
(ADOPT MODIFIED: **Option A** / the **interaction as the sole test of record** / the **Q3 narrow
human-anchored posture**, with **five binding tightening modifications**). Anchored to
[`resource/vwsd-semeval-2023`](../../wiki/base/resources/vwsd-semeval-2023.md). Operationalizes
prediction 1 of [`conjecture/distributional-saturation-grounding-headroom`](../../wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
on VWSD — its **gating *shape*** via a selection-accuracy interaction, **explicitly NOT
prediction-1-as-written** (the graded-Δ × separability interaction), which stays open for a future
graded-image resource. Run dir: `experiments/runs/2026-06-24-vwsd-grounding-headroom-v1/`.

> **This design is frozen BEFORE any image condition runs.** The text-only separability covariate
> is computed, written to a checksummed file, and frozen before the image arm (binding mod 2). The
> design is cleared to author by the resolved decision; the **result is gated on a fresh independent
> pre-run critic GO** against this frozen design and the observed covariate distribution — a NO-GO
> defers the image run and relaxes no condition.

## The question (as VWSD can pose it)

Prediction 1 of the grounding-headroom conjecture says: perceptual input moves an LLM's lexical-sense
behavior **only in the residual the text distribution under-determines**, and that residual is narrow
for concrete sense. VWSD instantiates the **under-determined regime by construction** (minimal 1–2
word context; trigger words chosen "so as not to give away the meaning of the image in isolation"),
but supplies only a **binary** human gold (which of 10 images is correct), not the graded relatedness
gradient the conjecture's instrument uses. So this probe tests a **re-shaped operationalization**:

> **Does adding the candidate images improve correct-sense selection specifically where text alone
> under-determines the sense — read as an interaction, not a main effect?**

The load-bearing object is the **interaction** between per-item text-only separability and image-induced
selection improvement, predicted **negative** (less text-separable items gain more from the image).

## Anchor and scope (Q3 narrow posture — what this does and does NOT establish)

- **Anchor:** the human-curated VWSD **English gold test** (463 items; gold = the human-selected
  correct image after human-authored trigger words + human distractor curation). Sense locus
  `grounded.perceptual` × `referential.sense` × `human-comparison`. This run uses a **frozen
  50-item seeded subset** (seed 20260624, `frozen/run_items.json`, sha256 in the run record) of the
  463 — a budget-bounded first probe, **not** the full test set; the small N is a stated limit
  (mandatory power caveat below).
- **Establishes (if positive + distraction-controlled):** that model sense *selection* is sensitive
  to perceptual input in the under-determined residual, gated by text separability — the conjecture's
  **gating shape**.
- **Does NOT establish:** (i) **not** prediction-1-as-written (no graded human relatedness gradient);
  (ii) **not** reference — picking the gold image is behavior *sensitive to* perceptual input, **not**
  a perceptual symbol system or reference-fixing (`referential.externalist` untouched); (iii) **not** a
  graded human judgment (VWSD gold is binary).
- **Caveats carried to the result** (all from the resource): binary gold; limited annotator
  independence (English annotators "includ[ed] the authors of this paper"; BabelNet-automatic seed; no
  inter-annotator agreement reported); image redistribution unconfirmed (images out of git,
  fetch-at-runtime only); anchored only to the gold test split (training is silver).

## Data (binding condition a — fetch + checksum, images out of git)

Fetched this session from the official task site Drive links (`raganato.github.io/vwsd`), checksummed:

- **Test queries + gold** (EN/FA/IT), zip sha256 `e0520129…aef0`; `en.test.data.v1.1.txt` sha256
  `0799d8aa…cc59b` (463 lines), `en.test.gold.v1.1.txt` sha256 `1e183ecf…5db8` (463 lines). These
  (the annotation overlay) are **committed** under `frozen/` (usable under CC-BY-NC for non-commercial
  research with attribution).
- **Resized EN test images** (572 MB zip), sha256 `b9f2f1e1…af8f`; 4090 unique EN candidate images
  extracted. **Images are OUT of git** (`.gitignore`); redistribution is unconfirmed
  (resource License & redistribution). They are read at runtime from `$VWSD_IMAGES` and never
  re-hosted. Anchored only to the gold **test** split.

## Three behavioural arms (binding condition b — prereg the DV before any model call)

All selection prompts present the target word, the phrase, and the ten candidates **in the dataset's
own order** (gold position is ≈ uniform across slots 1–10 in the frozen set — no positional-prior
shortcut). Panel: all three current models (claude-sonnet-4.6 / gpt-5.4-mini / gemini-3.5-flash);
the conjecture's stratification is **per-model** (headroom is a property of *text × model*), so the
interaction is read per-model and pooled. Gemini runs `reasoning:{effort:"minimal"}`; images low
detail (cost driver).

1. **CAPTION (one-time, frozen pre-image artifact).** Each unique candidate image is captioned once
   by gemini into a short neutral noun phrase (the text proxy the ratified DV — "image identities
   masked to text labels" — requires). Captions are **frozen + checksummed** (`frozen/captions.json`)
   and committed. They are a *fixed text rendering of the candidates*, authored before any selection
   arm. **Honest note on what the text-only baseline therefore measures:** text-only separability here
   is "can the target word + phrase pick the gold candidate from its **caption** alone," i.e. how far
   the linguistic context determines the sense *given a text description of each candidate*. This is
   the closest VWSD-native realization of the conjecture's "text-only baseline separability"; it is
   **not** a pure no-candidate measure, and the result states this.

2. **TEXT (text-only caption-based selection) — the SEPARABILITY covariate AND the improvement
   baseline.** Target word + phrase + the ten **captions** (no images), pick 1–10. Per item × model,
   correct/incorrect. **This is computed and FROZEN to `raw/text.json` (checksummed) BEFORE the IMAGE
   arm runs** (binding mod 2 — no retuning). Per-item separability `sep_i` = fraction of the 3 models
   correct in TEXT (0, 1/3, 2/3, 1).

3. **IMAGE (image-conditioned selection) — the main arm.** Identical prompt, candidates shown as the
   ten real images (low detail), pick 1–10. Per item × model, correct/incorrect.

4. **DISTRACT (word-ablated control) — reported FIRST (binding mod 3).** The ten images, **no target
   word or phrase**: "pick the most prototypical / canonical / everyday image." If gold is selected
   **>> chance (0.10)** with no word — and at a rate near the IMAGE arm — then image selection is
   driven by image-intrinsic salience, not by the word→sense→image mapping, and any IMAGE-arm lift is
   the **distraction null, not headroom**. This is the VWSD analogue of the prior image probe's
   same-referent / surface-dissimilarity control (the conjecture's distraction caveat). The
   distraction result is reported and credited **before** the interaction.

## Dependent variable and analysis (test of record = the interaction)

Let `t_im` = TEXT correctness and `g_im` = IMAGE correctness for item *i*, model *m* (0/1).

- **Primary test of record — continuous, per-item, leakage-aware.** Per-item image-induced
  improvement `Δ_i = mean_m(g_im) − mean_m(t_im)`; per-item separability `sep_i = mean_m(t_im)`.
  Regress `Δ_i` on `sep_i` across the N items (Spearman + OLS slope, per-model and pooled). The
  conjecture predicts a **negative** slope: where text under-determines (low `sep_i`), the image helps
  more. **Reported with the mechanical-ceiling caveat made explicit** (see below) — the primary read
  is therefore the **image-rescue rate among text-failed items**: among items where TEXT is wrong
  (`t_im=0`), the rate at which IMAGE is right (`g_im=1`), contrasted with IMAGE accuracy where TEXT
  already succeeded. Gating predicts image rescue concentrated in the text-failed (under-determined)
  cells.
- **Mechanical-ceiling caveat (stated, not hidden).** Because per-item accuracy is binary, an item
  where TEXT is already correct has `Δ ≤ 0` by construction (no room to improve), so a raw negative
  `Δ`–`sep` correlation is partly mechanical. The non-trivial content is the **image-rescue rate in
  the text-failed cells** and whether it **survives the DISTRACT control** — that is what distinguishes
  genuine grounding-in-the-residual from a ceiling artifact. The OLS/Spearman slope is reported as a
  descriptive companion, not the headline.
- **Strata view (binding mod 1 — floor + non-degeneracy).** Items are also binned: **saturated** =
  `sep_i = 1` (all 3 models text-correct); **under-determined** = `sep_i ≤ 1/3`. The result reports the
  full `sep_i` distribution and both bin counts. The pre-run critic certifies the strata are **not
  degenerate** (each bin holds a stated minimum; floor = **≥ 8 items per reported bin** for the binned
  view to be credited; if a bin falls below floor, the binned interaction is **not** reported and only
  the continuous + rescue-rate reads + the distraction null stand, with the power caveat foregrounded).
- **Distraction null first (binding mod 3).** DISTRACT gold-selection rate vs chance 0.10, per model
  and pooled, reported before the interaction is credited.
- **Power / coarseness caveat (binding mod 4 — MANDATORY in the result).** N=50 items, binary per-item
  accuracy, a coarse read of a 463-item anchor: a flat (null) interaction is **"no detectable gating
  OR underpowered,"** never proven absence of headroom. A positive that does not survive DISTRACT is
  the distraction null.

## Pre-run critic gate (binding condition d)

Before the IMAGE/DISTRACT spend, a **fresh independent critic** certifies, against this frozen design
and the **observed** `sep_i` distribution from `raw/text.json`: (1) the DV honestly tests the gating
shape, not prediction-1-as-written by sleight; (2) the text-only baseline is genuinely pre-frozen
(captions + text arm checksummed before image); (3) no surface-salience-only reader beats the
interaction (the DISTRACT control is adequate); (4) the strata are non-degenerate per the floor, or
the analysis correctly falls back to the continuous + rescue-rate reads. **GO/NO-GO. A NO-GO defers
the image run and relaxes nothing.**

## Budget (binding condition e — pre-flight; charter §8 / config/budget.md)

Measured per-call (this session's preflights): caption $0.00179/image (497 images ≈ $0.89); IMAGE
$0.0107/(item,model) [claude $0.0128 / gpt $0.0028 / gemini $0.0164]; DISTRACT ≈ same; TEXT (text-only,
short) ≪ that. Pre-flight estimate for N=50 × 3 models: captions ≈ $0.89 + text ≈ $0.15 + image ≈ $1.6
+ distract ≈ $1.6 ≈ **$4.2 day total** incl. preflights, each arm under the $2.50 single-run prudence
flag, under the $5/day cap. If any arm's running tally would take the **UTC-day total over $5**, it is
split or deferred (the resolved decision's anti-cheat: a budget defer never relaxes a condition).

## What would confirm / falsify (inherited from the conjecture, re-shaped to selection)

- **Confirms the gating shape:** image rescue concentrated in text-failed (under-determined) cells,
  little image lift where text already separates, **surviving** the DISTRACT control. (Still **not**
  prediction-1-as-written.)
- **Falsifies / fails to support:** (a) image helps uniformly, including where text already succeeds —
  breaks "only in the residual"; (b) image fails to rescue even where text demonstrably under-determines
  (distraction-controlled) — breaks "headroom is sufficient" (the inert-modality possibility); (c)
  DISTRACT gold-selection ≈ IMAGE rate — the apparent effect is salience, the distraction null.
