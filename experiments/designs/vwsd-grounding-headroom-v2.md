# Design — VWSD grounding-headroom probe v2 (frozen prereg)

**Status:** frozen design (2026-06-25, session 106). Implements the ratified re-operationalization
gate [`decisions/resolved/vwsd-grounding-headroom-dv-v2`](../../wiki/decisions/resolved/vwsd-grounding-headroom-dv-v2.md)
(VERDICT: **ADOPT-DEFAULT** — **Q1 Option B** sense-neutral visual-form **descriptor** as the
separability baseline, **Option A** mandatory chance-floor calibration arm, **Option C** leakage score
carried as a reported audit covariate; **Q2** stratified draw clearing a re-stated per-stratum floor
with the covariate frozen per-model pre-image, day-split across UTC if over cap; **Q3** v1's narrow
human-anchored posture unchanged; **binding pre-spend conditions (a)–(f)** including new **(d)** raised
claude image-arm `max_tokens`). Anchored to
[`resource/vwsd-semeval-2023`](../../wiki/base/resources/vwsd-semeval-2023.md). Revises
[`design/vwsd-grounding-headroom-v1`](vwsd-grounding-headroom-v1.md) in response to the three
first-class Limitations of [`result/vwsd-grounding-headroom-v1`](../../wiki/findings/results/vwsd-grounding-headroom-v1.md)
(caption-leakage contamination of the separability covariate; floor-not-met / underpowered; 6 claude
reasoning-then-truncation parse-fails). Operationalizes the **gating *shape*** of prediction 1 of
[`conjecture/distributional-saturation-grounding-headroom`](../../wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
on VWSD, **explicitly NOT prediction-1-as-written** (the graded-Δ × separability interaction), which
stays open for a future graded-image resource. Run dir:
[`experiments/runs/2026-06-25-vwsd-grounding-headroom-v2/`](../runs/2026-06-25-vwsd-grounding-headroom-v2/README.md).

> **BUILD STATUS — DAY 1 EXECUTED (session 107, UTC 2026-06-25).** The text-only condition-(b)
> freeze is complete: the 1889 Option-B visual-form descriptors over the seeded 200-item pool, the
> Option-C leak-audit, the descriptor-TEXT separability covariate, the stratified **N = 120** draw
> (under-determined **35** / saturated **85** — **both clear the ≥ 15 floor**, unlike v1's 7 < 8),
> and the Option-A floor arm are all generated + checksummed in the run dir. **No image / distract
> arm has run.** Day-2+ (the IMAGE then DISTRACT arms) stays gated on a **fresh independent pre-run
> critic GO** against the observed `sep_i`/`leak_i` distributions (condition e) and a re-measured
> claude raised-`max_tokens` per-call cost (condition d). The `result/vwsd-grounding-headroom-v2`
> still does not exist.

> **This freezes the YARDSTICK only — no probe has run.** No descriptors are generated, no leak-audit
> is scored, no images are fetched, no model call is made by freezing this design. The result
> `result/vwsd-grounding-headroom-v2` **does NOT yet exist and is NOT cleared**. It is gated, by the
> resolved decision, on a *later session* completing all of: (1) the Option-B descriptors **and** the
> Option-C leak-audit scores actually generated, frozen, and checksummed (`frozen/descriptors.json`)
> **before any image arm** (condition b); (2) the resized EN test images fetched at runtime + checksummed
> and **kept out of git** (condition a); (3) a **fresh independent pre-run critic GO** against this
> frozen design *and* the observed covariate distribution (condition e); (4) a pre-flight budget estimate
> that clears the $5/day UTC cap — almost certainly via the **UTC-day-split** plan below (condition f).
> Any of those failing **defers** the run and **relaxes no condition**; a pre-run-critic NO-GO may
> legitimately rule the non-caption baseline un-authorable-without-leakage on VWSD and defer the gate to
> a future graded-image resource (resolved decision, Anti-cheat).

## Why v2 exists (the three v1 limitations it answers)

The v1 probe **ran** (session 100) and returned a clean but **inconclusive** result — it neither
confirms nor falsifies the gating prediction. Three first-class Limitations of
[`result/vwsd-grounding-headroom-v1`](../../wiki/findings/results/vwsd-grounding-headroom-v1.md) drive
v2, and the first is value-laden and could not be auto-patched. Quoted verbatim from that page
(Limitations):

1. Caption-leakage contamination — *"The text-only baseline is "can the model pick gold from a
   **caption** of each candidate," and the gemini captions are concrete noun phrases that frequently
   **name the referent** ("a pile of mustard seeds"). So `sep_i` conflates "the target word + phrase
   determines the sense" with "the gold image's caption is descriptive enough to match.""*
2. Floor not met / underpowered — *"N=50, only 7 under-determined items, ~16 text-failed cells. The
   binned interaction is suppressed and the rescue read is descriptive. A larger, stratified draw (or a
   non-caption text baseline) is needed to test the gating shape."*
3. The truncation bias — *"6 image parse-fails, all claude, on rare-phrasing items ... claude reasoned
   aloud and was truncated at `max_tokens=16` before emitting a number. ... (a v2 should raise
   `max_tokens` for claude)."*

So v2 is a **re-operationalization**, not a re-run: it changes what the separability covariate *means*
(a non-caption visual-form descriptor instead of a referent-naming caption), enlarges and stratifies
the draw so the under-determined stratum can clear a real floor, and removes the claude truncation
bias. The conjecture stays **`proposed`**; freezing this yardstick fixes none of that — it fixes only
how the next probe would measure.

## Anchor and scope (Q3 narrow posture — what this does and does NOT establish)

Carried forward **unchanged** from v1 and from the resolved gate's Q3 (no widening):

- **Anchor:** the human-curated VWSD **English gold test** (463 items; gold = the human-selected
  correct image after human-authored trigger words + human distractor curation). Sense locus
  `grounded.perceptual` × `referential.sense` × `human-comparison`. v2 uses a **frozen stratified
  subset** of the 463 (see Q2), **not** the full set — a budget-bounded probe; the draw size is a
  stated limit (mandatory power caveat below).
- **Establishes (if positive + distraction-controlled):** that model sense *selection* is sensitive to
  perceptual input in the under-determined residual, gated by per-item (non-caption) text separability
  — the conjecture's **gating shape**.
- **Does NOT establish:** (i) **not** prediction-1-as-written (no graded human relatedness gradient —
  VWSD gold is binary); (ii) **not** reference — picking the gold image is behavior *sensitive to*
  perceptual input, **not** a perceptual symbol system or reference-fixing (`referential.externalist`
  untouched); (iii) **not** a graded human judgment.
- **Caveats carried to the result, verbatim in force** (all from
  [`resource/vwsd-semeval-2023`](../../wiki/base/resources/vwsd-semeval-2023.md)): **binary gold** (no
  graded signal); **limited annotator independence** (English annotators "includ[ed] the authors of
  this paper"; BabelNet-automatic seed; no inter-annotator agreement reported); **image redistribution
  unconfirmed** (images out of git, fetch-at-runtime only, never re-hosted); **anchored only to the gold
  test split** (the 12,869 training instances are silver).

## Data (binding condition a — fetch + checksum, images out of git)

Identical handling to v1. The resized EN test images (572 MB zip, v1 sha256 `b9f2f1e1…af8f`; 4090
unique EN candidate images) are **fetched at runtime** from the official task site
(`raganato.github.io/vwsd`), checksummed, and **kept OUT of git** (`.gitignore`) — redistribution is
unconfirmed ([`resource/vwsd-semeval-2023`](../../wiki/base/resources/vwsd-semeval-2023.md), License &
redistribution). The annotation overlay (`en.test.data.v1.1.txt` sha256 `0799d8aa…cc59b`,
`en.test.gold.v1.1.txt` sha256 `1e183ecf…5db8`; 463 lines each) is committed under `frozen/`, usable
under CC-BY-NC for non-commercial research with attribution. Anchored **only** to the gold test split.

## Q1 — The non-caption text baseline: Option B sense-neutral visual-form descriptor

The covariate must read **linguistic under-determination** — how far the target word + the VWSD trigger
word(s) fix the sense — *independent of* how richly any candidate is described in words. v1's caption
baseline failed this because the captions named the referent. v2 implements **Option B** from the
resolved gate: a candidate **descriptor** that names **visual form only** (shapes, colours, layout) and
is **barred from naming the depicted referent concept**.

### B.1 — The descriptor-generation procedure (authored ONCE, frozen before any image arm)

- **Author model.** Descriptors are machine-generated by a single fixed generator —
  **gemini-3.5-flash** (the same model that authored v1's captions; low image detail, the cost driver),
  one pass over the **unique candidate images appearing in the frozen draw** (see Q2), image read at
  runtime from `$VWSD_IMAGES`.
- **Generator prompt / policy (the load-bearing constraint).** Each image is described with the policy:

  > "Describe ONLY the visual form of this image — its shapes, colours, textures, spatial layout, and
  > number of elements — in one short neutral phrase. Do NOT name, label, or identify what the depicted
  > object, scene, creature, or concept IS, and do NOT use any noun that names the referent or its
  > category. Write what an eye sees, not what a mind recognises. Example of the REQUIRED style: "a
  > dense cluster of small round yellowish particles." Example of the FORBIDDEN style (names the
  > referent): "a pile of mustard seeds.""

  The intended effect: a model that picks gold from these descriptors must map the *linguistic context*
  (target word + trigger) onto *visual form*, not string-match a referent name — so `sep_i` tracks
  linguistic under-determination rather than caption informativeness.
- **Generated once, frozen, never re-derived.** The full descriptor set is written to a single
  checksummed file `frozen/descriptors.json` (sha256 recorded in the run record and committed)
  **before any image arm runs**, and is **not re-derived after image results land** (condition b). The
  per-model, per-item separability covariate computed from these descriptors (the TEXT arm, below) is
  likewise frozen per-model to a checksummed file **before any image condition** (condition b) — "no
  retuning" stays mechanically auditable.

### B.2 — Honest note: descriptor authoring is itself value-laden and leak-prone

Per the resolved gate's Risk flags (i)–(iii) on Option B, stated as plainly here as in the decision:
(i) the line between "names the visual form" and "names the referent" is **fuzzy** ("a pile of small
seeds" already half-names it), so every authoring choice could re-introduce the confound it is meant to
remove; (ii) the generator is itself a model, so the confound could be **displaced** (into how
aggressively the generator abstracts away identity) rather than removed; (iii) the descriptors are
therefore **untrusted until the Option-C leak-audit passes** — and that audit is itself an
operationalization a **later session must ratify**, not this design. v2 does not claim the descriptors
are leak-free; it claims only that the leak is **measured and reported** (the leak-audit covariate) and
that the **pre-run critic must certify it credible** before any spend (condition e). If the critic
judges the descriptor un-authorable without leakage on VWSD, the run defers — that is an allowed and
honest outcome, not a failure of this design.

### B.3 — Option A floor-calibration arm (mandatory)

A separate **Option A** arm runs: the target word + the VWSD trigger word(s), the ten candidates
replaced by **bare index labels only** ("image 1 … image 10"), **no descriptor and no image**. By
construction there is nothing for the model to match the linguistic context against, so this arm
**must sit at/near chance (0.10)**. Its honest role is **floor calibration**: it confirms that the
linguistic context *alone* — the target word + trigger that every other arm also carries — does **not**
leak the gold by itself. If Option A is meaningfully above chance, the linguistic context is doing
covert work and the whole instrument is suspect; this is a NO-GO trigger for the pre-run critic. Option
A is **not** the separability baseline (it has no per-item gradient — resolved gate, Option A Risk flags
i–ii); it is a calibration arm only.

### B.4 — Option C leakage-audit covariate (reported, not the baseline)

For each item, a **per-item leakage score** `leak_i` measures how strongly the frozen Option-B
descriptor *still* names the referent. Procedure: a **held-out referent-name-recovery check** — a
fresh model instance (held out from the generator; the panel's gpt-5.4-mini, to avoid generator
self-consistency), shown **only** the gold candidate's descriptor with no image and no target word, is
asked to recover the depicted referent's name/category; `leak_i` is scored on whether/how closely it
recovers the gold referent (graded: exact category match = high leak, related-but-wrong = partial,
unrelated = no leak). `leak_i` is **frozen + checksummed alongside the descriptors** in
`frozen/descriptors.json` **before any image arm** and reported as an **audit covariate on the
Option-B descriptors** — *not* as the baseline. Its role is the mechanical check that Option B did not
re-leak; the gating interaction is reported with `leak_i` carried as a covariate (and, if `leak_i`
correlates strongly with `sep_i`, that correlation is reported as a contamination warning, since
regressing one out would partly remove the other — the resolved gate's Option-C circularity flag). The
leak-audit is **itself an operationalization a later session ratifies**; this design fixes the
procedure, not its validity.

## Q2 — Stratification, N, and the re-stated per-stratum floor

The Option-B descriptor baseline should reduce the saturation that crushed v1's under-determined
stratum (7 < floor 8), but v2 must **not assume** it does. The draw is **stratified** from the 463 EN
gold, **oversampling the predicted under-determined band**, and sized so **both** strata clear a
re-stated per-stratum floor.

### B.5 — The exact N and floor (this design's judgement call)

- **Per-stratum floor: ≥ 15 EN gold items in EACH reported stratum** (saturated `sep_i` = 1;
  under-determined `sep_i` ≤ 1/3), computed per the frozen covariate. This raises v1's floor of ≥ 8.
- **N = 120 EN gold items**, a **stratified** draw (seeded; `frozen/run_items.json` with sha256 in the
  run record), built to oversample the predicted under-determined band so the under-determined stratum
  has a real chance to clear ≥ 15.

**One-line justification.** v1's under-determined stratum drew only ~14% of a *random* 50 (7 items) and
missed the floor of 8; a floor of ≥ 15 needs the under-determined band to supply ~15 of N, so v2 both
**raises the floor** (≥ 15, for a less knife-edge binned read) **and stratifies + enlarges to N = 120
with deliberate oversampling of the under-determined band** — sized to give that stratum a genuine
chance to clear ≥ 15 even if the non-caption descriptor only partly relieves saturation, while staying
small enough to fit the $5/day cap under a UTC-day split (Budget below).

### B.6 — How the stratified draw is built (without peeking at images)

The stratifier is the **frozen, per-model, pre-image** descriptor-separability covariate, so the draw
cannot be built from the final covariate before that covariate exists. The honest procedure, frozen
here:

1. Generate the Option-B descriptors over a **candidate pool** larger than 120 (e.g. a seeded ~200-item
   EN-gold pool), freeze them, then run the **TEXT (descriptor) arm** on the pool to obtain `sep_i` per
   item per model. This is the covariate computation — **text-only, no image touched**.
2. From the scored pool, **draw the stratified N = 120** so each stratum holds ≥ 15 (oversampling the
   under-determined band), **freeze the 120** to `frozen/run_items.json`, and freeze the
   per-item/per-model covariate for exactly those 120 to a checksummed `raw/text.json`.
3. **All of (1)–(2) complete before any IMAGE / DISTRACT call** — no image result can retune the draw
   or the covariate (condition b). The descriptor set, the `leak_i` scores, the draw, and the covariate
   are all frozen + checksummed before the image arm.

If, after step (1), the under-determined band **cannot** supply ≥ 15 even from the ~200 pool, the
binned interaction is **not credited** and the result falls back to the continuous + rescue-rate reads
+ the distraction null, with the power caveat foregrounded — exactly the v1 fallback, re-set for the
new floor. The pre-run critic certifies the strata are non-degenerate against the **observed** `sep_i`
distribution (condition e); a degenerate draw is a NO-GO that defers and relaxes nothing.

## Behavioural arms (binding condition b — prereg the DV before any model call)

All selection prompts present the target word, the trigger phrase, and the ten candidates **in the
dataset's own order**. Panel: all three current models (claude-sonnet-4.6 / gpt-5.4-mini /
gemini-3.5-flash); the conjecture's stratification is **per-model**, so the interaction is read
per-model and pooled. Gemini runs `reasoning:{effort:"minimal"}`; images low detail (cost driver).

1. **DESCRIPTOR (Option B, one-time, frozen pre-image artifact).** Each unique candidate image in the
   draw is described once by gemini under the B.1 visual-form policy into a short neutral phrase that
   **does not name the referent**. Descriptors are **frozen + checksummed** (`frozen/descriptors.json`,
   with the `leak_i` audit scores) and committed. Authored before any selection arm; **not re-derived**
   after image results land.
2. **TEXT (descriptor-based selection) — the SEPARABILITY covariate AND the improvement baseline.**
   Target word + trigger phrase + the ten **descriptors** (no images), pick 1–10. Per item × model,
   correct/incorrect. **Computed and FROZEN to `raw/text.json` (checksummed) BEFORE the IMAGE arm**
   (condition b — no retuning). Per-item separability `sep_i` = fraction of the 3 models correct in TEXT
   (0, 1/3, 2/3, 1).
3. **FLOOR (Option A calibration) — bare index labels.** Target word + trigger phrase + ten **index
   labels only** (no descriptor, no image), pick 1–10. Must sit at/near chance; confirms the linguistic
   context alone does not leak. Calibration, not the baseline.
4. **IMAGE (image-conditioned selection) — the main arm.** Identical prompt, candidates shown as the
   ten real images (low detail), pick 1–10. Per item × model, correct/incorrect. **Claude image-arm
   `max_tokens` raised — see condition (d) below.**
5. **DISTRACT (word-ablated control) — reported FIRST (condition c).** The ten images, **no target word
   or trigger phrase**: "pick the most prototypical / canonical / everyday image." If gold is selected
   **>> chance (0.10)** with no word — and near the IMAGE rate — image selection is driven by
   image-intrinsic salience, not the word→sense→image mapping, and any IMAGE-arm lift is the
   **distraction null, not headroom**. The VWSD analogue of the prior image probe's same-referent /
   surface-dissimilarity control. Reported and credited **before** the interaction.

## Condition (d) — raised claude image-arm `max_tokens`

v1 truncated claude's image-arm output at **`max_tokens = 16`**, causing **6 parse-fails (all claude,
on rare-phrasing items)** when claude reasoned aloud before emitting a number — biasing the read (it
overstated claude image accuracy by dropping 4 hard items and understated the rescue-cell count). v2
sets the claude image-arm **`max_tokens = 512`** — high enough that reasoning-then-answer is not
truncated before a parseable 1–10 selection is emitted. The answer is parsed by extracting the final
emitted index from the (now untruncated) response; an unparseable response is still recorded as a
parse-fail, but truncation is removed as the cause. (gpt and gemini, which did not truncate at v1's
budget, keep a generous selection budget as well; this condition's binding force is specifically the
claude image arm.) Raising claude's `max_tokens` **raises the claude per-call cost** — accounted for in
the Budget pre-flight below.

## Dependent variable and analysis (test of record = the interaction)

Let `t_im` = TEXT (descriptor) correctness and `g_im` = IMAGE correctness for item *i*, model *m*
(0/1).

- **Primary test of record — the gating interaction, read as image rescue among text-failed cells.**
  Among item × model cells where TEXT (descriptor) is wrong (`t_im = 0`), the rate at which IMAGE is
  right (`g_im = 1`), contrasted with IMAGE accuracy where TEXT already succeeded. Gating predicts image
  rescue **concentrated in the text-failed (under-determined) cells**. This is the load-bearing read.
- **OLS / Spearman slope — descriptive companion only.** Per-item image-induced improvement
  `Δ_i = mean_m(g_im) − mean_m(t_im)`; per-item separability `sep_i = mean_m(t_im)`. Regress `Δ_i` on
  `sep_i` (Spearman + OLS slope, per-model and pooled); the conjecture predicts a **negative** slope.
  Reported as a **descriptive companion, not the headline**, because of the mechanical-ceiling caveat.
- **Mechanical-ceiling caveat (stated, not hidden).** Per-item accuracy is binary, so an item where
  TEXT is already correct has `Δ ≤ 0` by construction — a raw negative `Δ`–`sep` correlation is partly
  mechanical. The non-trivial content is the **image-rescue rate in the text-failed cells** and whether
  it **survives the DISTRACT control**; the slope is companion only.
- **Strata view (floor + non-degeneracy).** Items binned: **saturated** = `sep_i = 1`;
  **under-determined** = `sep_i ≤ 1/3`. The result reports the full `sep_i` distribution and both bin
  counts. The binned interaction is credited **only if each reported bin holds ≥ 15 items** (B.5); if a
  bin falls below floor, the binned view is **not** reported and only the continuous + rescue-rate reads
  + the distraction null stand, with the power caveat foregrounded. No post-hoc re-binning.
- **Leak-audit covariate carried.** The `leak_i` distribution is reported; if `leak_i` correlates
  strongly with `sep_i`, that is flagged as residual contamination (the Option-C circularity warning).
- **Distraction null FIRST (condition c).** DISTRACT gold-selection rate vs chance 0.10, per model and
  pooled, reported and credited before the interaction. A positive IMAGE lift that does not survive
  DISTRACT is the distraction null, not headroom.
- **Power / coarseness caveat (MANDATORY in the result).** N = 120 items, binary per-item accuracy, a
  coarse read of a 463-item anchor: a flat (null) interaction is **"no detectable gating OR
  underpowered,"** never proven absence of headroom. A positive that does not survive DISTRACT is the
  distraction null.

## Pre-run critic gate (binding condition e)

Before any IMAGE / DISTRACT / descriptor-authoring spend that commits the run, a **fresh independent
critic** (not the orchestrator doing the build) certifies, against this frozen design **and the
observed `sep_i` and `leak_i` distributions**: (1) the Option-B descriptor baseline honestly measures
linguistic under-determination and does **not** re-leak the referent name (the leak-audit is credible
and `leak_i` is acceptably low / its correlation with `sep_i` acceptably weak); (2) the covariate is
genuinely pre-frozen (descriptors + `leak_i` + TEXT arm checksummed before any image); (3) the strata
clear the ≥ 15 floor and are non-degenerate, or the analysis correctly falls back; (4) the Option-A
floor arm sits at/near chance; (5) no surface-dissimilarity-only reader beats the interaction (the
DISTRACT control is adequate). **GO/NO-GO. A NO-GO defers the run and relaxes nothing** — and may
legitimately conclude the non-caption baseline is **un-authorable without leakage on VWSD**, deferring
the gate to a future graded-image resource.

## Budget (binding condition f — pre-flight; charter §8 / config/budget.md)

**Measured v1 per-call numbers** (from [`design/vwsd-grounding-headroom-v1`](vwsd-grounding-headroom-v1.md),
Budget; and [`result/vwsd-grounding-headroom-v1`](../../wiki/findings/results/vwsd-grounding-headroom-v1.md)):
descriptor/caption ≈ **$0.00179/image** (gemini, low detail); IMAGE ≈ **$0.0107/(item, model)** [claude
**$0.0128** / gpt **$0.0028** / gemini **$0.0164**]; DISTRACT ≈ same as IMAGE; TEXT (text-only, short)
**≪** that; FLOOR (Option A, index-labels only, text-only) ≪ that as well. **Condition (d) raises the
claude image-arm cost**: raising claude `max_tokens` from 16 to 512 lets claude emit its full
reasoning, increasing claude completion tokens on the IMAGE and DISTRACT arms, so the claude IMAGE/
DISTRACT per-call cost will rise materially above the v1 $0.0128 figure. The pre-flight estimate below
applies a **conservative ~3× multiplier to the claude IMAGE and DISTRACT per-call cost** (claude
≈ $0.038/call) as a placeholder; **a later session MUST re-measure claude's raised-`max_tokens`
per-call cost in a small preflight before committing** (the resolved gate forbids running on a stale
number).

**Pipeline and pre-flight estimate for N = 120 (× 3 models), with a ~200-item descriptor pool:**

| Component | Scope | Estimate |
|---|---|---|
| DESCRIPTOR authoring (Option B) | one pass over the unique candidate images in the ~200-pool draw; ≈ up to ~2000 unique images at $0.00179 | ≈ **$3.6** (pool-size dependent; ≤ $3.6 if ~2000 unique images, less if fewer) |
| Leak-audit (Option C) | one held-out gpt text call per **gold** item over the pool (~200, text-only) | **≪ $0.1** |
| TEXT / separability arm | ~200 pool items × 3 models, text-only (descriptors) | ≈ **$0.15** |
| FLOOR arm (Option A) | 120 items × 3 models, text-only (index labels) | ≈ **$0.1** |
| IMAGE arm | 120 items × 3 models [claude ≈$0.038 (raised) / gpt $0.0028 / gemini $0.0164] ≈ $0.057/item | ≈ **$6.9** |
| DISTRACT arm | 120 items × 3 models, same per-call as IMAGE | ≈ **$6.9** |
| preflights | small | ≈ **$0.3** |

The descriptor pass + image-bearing arms together **far exceed the $5/day UTC cap** and the IMAGE and
DISTRACT arms each **exceed the $2.50 single-run prudence flag**. So an explicit **UTC-day-split** is
**mandatory** (resolved gate Q2 + condition f). A clean v2 needs **≥ 3 UTC days**:

- **UTC day 1 — descriptor authoring + covariate freeze (text-only).** Generate Option-B descriptors
  over the ~200 pool (≈ $3.6), score the leak-audit (≪ $0.1), run the TEXT/separability arm (≈ $0.15),
  draw + freeze the stratified N = 120, run the Option-A FLOOR arm (≈ $0.1), plus preflights (~$0.1).
  **Day-1 total ≈ $4.0**, under the cap. **No image is touched on day 1** — this is the condition-(b)
  freeze, complete before any image arm. (If the descriptor pool's unique-image count pushes day 1 over
  the cap, split the descriptor pass itself across two days; descriptor authoring is the single largest
  line and is the natural split point.)
- **UTC day 2 — IMAGE arm.** 120 items × 3 models ≈ **$6.9** alone **exceeds the daily cap**, so the
  IMAGE arm itself **splits across two UTC days** (e.g. ~60 items/day ≈ $3.5/day, each just over the
  $2.50 single-run flag → run as two sub-batches with the running UTC tally checked between batches, or
  ~45 items/day to keep each sub-batch under $2.50). Treat as **day 2 + day 3** for the IMAGE arm.
- **UTC day 4 — DISTRACT arm.** Same ≈ $6.9, **split across two UTC days** identically (day 4 + day 5).

So the realistic plan is **≈ 5 UTC days** (descriptor/freeze day; two IMAGE days; two DISTRACT days),
each day kept **under the $5 cap** and each sub-batch handled against the **$2.50 single-run prudence
flag** (split or deferred if a running tally would breach either). The exact day-count depends on the
re-measured claude per-call cost (condition d) and the pool's unique-image count, both of which a later
session pins in a small preflight before committing; **the pre-flight that actually clears the cap is
an execution-session step, not frozen here**. The estimate is recorded in
[`config/budget.md`](../../config/budget.md) before the run; the actual is recorded after. A budget
defer **never relaxes a condition** (resolved gate, Anti-cheat).

## What would confirm / falsify (inherited from the conjecture, re-shaped to selection)

- **Confirms the gating shape:** image rescue concentrated in text-failed (under-determined) cells,
  little image lift where the descriptor text already separates, **surviving** the DISTRACT control, with
  the Option-A floor at chance and the leak-audit clean. (Still **not** prediction-1-as-written.)
- **Falsifies / fails to support:** (a) image helps uniformly, including where descriptor text already
  separates — breaks "only in the residual"; (b) image fails to rescue even where descriptor text
  demonstrably under-determines (distraction-controlled) — breaks "headroom is sufficient" (the
  inert-modality possibility); (c) DISTRACT gold-selection ≈ IMAGE rate — the apparent effect is
  salience, the distraction null.
- **Inconclusive (the live v1 outcome, still possible):** the under-determined stratum fails the ≥ 15
  floor, or the leak-audit shows the descriptors re-leaked the referent, or the pre-run critic returns
  NO-GO — in which case v2 **neither confirms nor falsifies**, the conjecture stays `proposed`, and
  prediction-1-as-written remains reserved for a future graded-image resource.

## Anti-cheat note (the resolved gate's guards, honored)

Freezing this design fixes the **yardstick** (the Option-B descriptor baseline + its generation policy,
the Option-A floor arm, the Option-C leak-audit, the N = 120 stratified draw, the ≥ 15 per-stratum
floor, the raised claude `max_tokens`, the anchor posture and scope), **never the result**. No probe is
run and no descriptor is generated by freezing it. The Option-B descriptors and the separability
covariate, **once frozen + checksummed, are not re-derived after seeing image results** — that
commitment is what makes "no retuning" auditable (condition b). The DISTRACT null is reported and
credited **first** (condition c); **no accuracy lift counts as headroom unless it survives it**. A
pre-run-critic **NO-GO defers the run, never relaxes a condition**, and may rule the non-caption
baseline un-authorable-without-leakage on VWSD. A flat (null) interaction remains *"no detectable
gating OR underpowered,"* never proven absence of headroom.
