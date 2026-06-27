# VWSD grounding-headroom probe v2 (run dir) — DAY-1 text-only build

Implements the frozen design
[`experiments/designs/vwsd-grounding-headroom-v2.md`](../../designs/vwsd-grounding-headroom-v2.md)
(ratified gate `decisions/resolved/vwsd-grounding-headroom-dv-v2`, ADOPT-DEFAULT). Anchor:
[`resource/vwsd-semeval-2023`](../../../wiki/base/resources/vwsd-semeval-2023.md) (463 EN gold test).
This re-operationalizes v1's three first-class limitations: a **non-caption Option-B visual-form
descriptor** separability baseline (v1's captions named the referent), an enlarged **stratified
N=120** draw clearing a raised **≥15/stratum** floor, and **raised claude image `max_tokens`** (v1
truncated 6 claude image-arm answers at 16). The result `result/vwsd-grounding-headroom-v2` does
**not** exist yet and is **not** cleared — it is gated on a fresh pre-run critic GO next session.

## Day-split (design Budget, condition f) — this dir is DAY 1 only

A clean v2 needs ≈ 5 UTC days; the descriptor pass + image-bearing arms together far exceed the
$5/day cap. **Day 1 (this build) is text-only**, completing the condition-(b) freeze before any
image arm:

1. `build_items.py` → `frozen/items.json` (all 463 EN gold, sha in stdout).
2. `build_pool.py` → `frozen/pool_items.json` (seeded **200-item** pool, seed 20260625; 1889 unique
   candidate images).
3. `run.py descriptor-full` → `frozen/descriptors.json` — **Option-B visual-form descriptors** over
   the 1889 unique pool images (gemini, low detail; the B.1 policy bars naming the referent). The
   single large day-1 spend (≈ $3.97; checkpointed + hard `DESC_ABORT_USD` guard).
4. `run.py leak-full` → adds `leak{}` to `frozen/descriptors.json` — **Option-C** held-out **gpt**
   referent-recovery audit over the 200 gold descriptors; `leak_i` ∈ {0 none, 1 partial, 2 high},
   scored deterministically (token overlap of the recovered referent with the target word / phrase;
   raw guess stored for a later model re-grade — the leak-audit's validity is itself a later-session
   ratification, design B.4).
5. `run.py text-full` → `raw/pool_text.json` — descriptor-based **TEXT/separability** arm over the
   200 pool items × 3 models; `sep_i` = fraction of 3 models correct (0, 1/3, 2/3, 1).
6. `draw_stratified.py` → `frozen/run_items.json` (the stratified **N=120**, oversampling the
   under-determined band, seed 20260625) + `raw/text.json` (the frozen covariate for the 120).
7. `run.py floor-full` → `raw/floor.json` — **Option-A** bare-index-label calibration arm over the
   120 × 3 models (must sit at/near chance 0.10; confirms the linguistic context alone does not leak).

**No image / distract arm runs on day 1.** Day 2+ (gated by a fresh independent pre-run critic GO
against the observed `sep_i`/`leak_i` distributions — design condition e) runs the IMAGE arm (raised
claude `max_tokens=512`; re-measure claude's per-call cost first, condition d) then the DISTRACT
control (its null reported FIRST), then writes the result + an independent post-run verifier.

## Day-1 RESULTS (session 107, UTC 2026-06-25) — the OBSERVED distributions the pre-run critic reads

The text-only freeze is complete (`python3 analyze.py` regenerates this). **No image arm has run.**

- **TEXT (descriptor) arm accuracy** (over the frozen 120): claude **0.750** / gpt **0.725** /
  gemini **0.808**. The non-caption Option-B descriptor baseline is **not saturated** (v1's
  referent-naming captions ran .86–.88) — it leaves real text-failed headroom, the point of v2.
- **Separability `sep_i`** (fraction of 3 models correct) over the 120: `{0: 16, 1/3: 19, 1: 85}`.
  Strata: **under-determined (sep≤1/3) = 35**, intermediate (2/3) = **0**, **saturated (sep=1) = 85**.
  **Both reported bins clear the ≥15 floor** (v1 failed at 7<8) → the binned interaction would be
  **credited** next session. *Transparency:* the seeded draw rule (fill saturated first to guarantee
  that floor) left **0 intermediate items**, so the continuous `sep_i` companion has a gap at 2/3;
  the rule was fixed before the covariate was scored (`draw_stratified.py`), so it is not retuned.
- **Option-A FLOOR calibration** (bare index labels; target chance 0.10): pooled **0.122**
  Wilson[0.092, 0.160] (includes 0.10). claude 0.092 (clean), gpt 0.117 (near-clean), but
  **gemini 0.158 Wilson[0.104, 0.234] — marginally ABOVE chance** (lower bound 0.104 > 0.10). The
  linguistic context + a position/label prior is doing a little covert work for **gemini specifically**.
  The design names an above-chance floor a **pre-run-critic NO-GO trigger**; here it is marginal and
  gemini-only (pooled and claude/gpt are at/near chance), so it is **flagged, not auto-resolved** —
  a load-bearing input to next session's GO/NO-GO.
- **Option-C LEAK audit** (held-out gpt referent recovery; 0 none / 1 partial / 2 high):
  **154 / 20 / 26** → high-leak rate **0.130**. Spearman(`leak_i`, `sep_i`) = **0.160** — a **weak**
  positive (mild residual contamination, well short of the strong correlation that would trigger the
  Option-C circularity warning). 13% of gold descriptors still let gpt recover the exact target word
  (e.g. mustard seeds, whose visual form is itself near-diagnostic); this covariate is carried, not
  regressed out.

**Day-1 billed: $4.72482** (descriptors $4.01649 + text $0.53545 + floor $0.12724 + leak $0.02299 +
preflights $0.02265). Recorded in [`config/budget.md`](../../../config/budget.md).

## Day-2 (IMAGE arm) — session 112, UTC 2026-06-26 — DONE, but NOT a result yet

The **IMAGE arm** (`run.py image-full`, design arm 4) ran over the frozen 120 × 3 models on the first
fresh UTC day after the day-1 freeze. **This is the main grounding arm — but it is raw data, not a
result. No grounding-headroom claim can be read from it until the DISTRACT control runs and its null
is reported FIRST (binding condition 3 / design condition c). `result/vwsd-grounding-headroom-v2`
still does NOT exist.** What landed:

- `raw/image.json` — **360 records (120 items × 3 models), 0 missing-cost, 0 parse-fails**, sha256
  **`6884eea0…430870`**. Candidate images low-detail, shown in dataset order; the word+phrase prompt is
  byte-identical to v1's IMAGE arm except for **condition (d)** (claude `max_tokens` 16 → 512).
- **Condition (d) discharged — claude's raised-`max_tokens` per-call cost re-measured, not assumed.**
  The image-preflight + full arm measured claude at **$0.01244/call** (raised `max_tokens=512`), which
  is **essentially v1's $0.0128**, *not* the design's conservative ~3× placeholder ($0.038). claude
  emits the bare index digit (`raw_len=1` in the preflight), so the raised cap **removes the v1
  truncation bias** (v1 had 6 claude parse-fails at `max_tokens=16`; here **0 parse-fails, all three
  models**) **without materially raising cost**. Per-model billed: claude **$1.49279** / gpt
  **$0.32269** ($0.00269/call) / gemini **$1.95487** ($0.01629/call). Full IMAGE arm **$3.77035**, far
  under the ~$6.9 placeholder → the arm fit a **single** UTC day, run as **two sub-batches** (60 + 60,
  ~$1.87 + ~$1.90 of new spend each) to keep every sub-batch under the $2.50 single-run prudence flag.
- **Preliminary `analyze.py` numbers exist but carry NO weight yet** (DISTRACT null owed first). For
  the record only, not as a finding: image accuracy claude **0.850** / gpt **0.592** / gemini **0.867**
  (gpt is *lower* with images than its descriptor-text 0.725 — a not-yet-interpretable inversion). The
  test-of-record cells (rescue 39/86 in text-failed cells; 238/274 in text-OK cells) are **printed but
  uninterpretable** until the DISTRACT word-ablated control establishes how much of any image lift is
  image-intrinsic salience rather than the word→sense→image mapping.

**Day-2 billed: $3.83238** (IMAGE arm $3.77035 + image-preflight $0.06203). Recorded in
[`config/budget.md`](../../../config/budget.md).

## Day-3 (DISTRACT arm) — session 121, UTC 2026-06-27 — DONE; result WRITTEN

The **DISTRACT word-ablated control** (`run.py distract-full`, design arm 5) ran on the next fresh UTC
day, completing the probe. Its null is **reported and credited FIRST** (binding condition 3).

- `raw/distract.json` — **360 records (120 items × 3 models), 0 missing-cost, 0 parse-fails**, sha256
  **`f8fbb6be…`**. Same images low-detail; prompt ablates the target word + trigger ("pick the most
  prototypical / canonical / everyday image").
- Run as **two 60-item sub-batches** ($1.87346 + $1.88971, each under the $2.50 single-run flag) +
  `distract-preflight` $0.06184 → **$3.82501 day-3 billed**, under the $5/day cap. Per-model per-call
  ≈ IMAGE (claude $0.01194 / gpt $0.00266 / gemini $0.01632).
- **DISTRACT null CLEAN:** pooled 35/360 = **.097** Wilson[.071,.132]; per-model claude .133 / gpt .042
  / gemini .117 — **no model's Wilson LB exceeds chance .10**. Gold images are not intrinsically
  salient, so any image lift is creditable as word/sense-driven grounding, not salience.
- **Result WRITTEN:** [`result/vwsd-grounding-headroom-v2`](../../../wiki/findings/results/vwsd-grounding-headroom-v2.md)
  — **SUPPORTS the gating SHAPE, 3/3 models in direction**: image rescues the descriptor-text-failed
  (under-determined) cells (pooled .453; per-model .500/.303/.609, all > chance) while adding no lift
  where the descriptor already separates (saturated Δ −.122). First confirming-direction VWSD evidence.
  Caveats foregrounded: gemini floor elevated (.158, LB > chance); gpt degrades overall (gating
  sign-only); magnitude inflated by the de-referented Option-B channel (supports SHAPE, not the "narrow
  headroom" magnitude bet); gating-shape-on-binary-selection, NOT prediction-1-as-written, NOT
  reference. An **independent fresh-agent post-run verifier REPRODUCED** every finding-bearing number
  from raw (1440/1440 records consistent) and confirmed the three binding conditions hold.

**Day-3 billed: $3.82501** (DISTRACT $3.76317 + distract-preflight $0.06184). Recorded in
[`config/budget.md`](../../../config/budget.md). The probe is **complete**; `analyze.py` regenerates
every result section from the committed raw.

## What's committed vs out of git

- **Committed:** the CC-BY-NC annotation overlay (`frozen/en.test.{data,gold}.v1.1.txt`), the built
  item/pool sets, the frozen descriptors + leak audit + draw + covariate, and the raw call records
  (text/floor/**image** picks + cost ledgers — **text only, no image bytes**; `raw/image.json` records
  the model's 1–10 selection and `usage.cost` per call, never the image data).
- **OUT of git** (`.gitignore`; redistribution unconfirmed): the 572 MB resized EN test zip
  (sha256 `b9f2f1e1…af8f`) and the 4090 extracted candidate images. Fetched at runtime from the
  official task site (`raganato.github.io/vwsd`, Drive id `15ed8TXY…`), read via `$VWSD_IMAGES`,
  never re-hosted.

## Reproduce

```
# fetch + extract the 572MB resized EN test images, verify sha256 b9f2f1e1…af8f
export VWSD_IMAGES=/path/to/en_images
export OPENROUTER_API_KEY=...
# --- day 1 (text-only freeze; session 107) ---
python3 build_items.py
python3 build_pool.py
python3 run.py descriptor-preflight     # eyeball policy + per-image cost
python3 run.py descriptor-full          # -> frozen/descriptors.json  (~$3.97; resumable)
python3 run.py leak-full                # -> frozen/descriptors.json:leak
python3 run.py text-full                # -> raw/pool_text.json  (separability covariate)
python3 draw_stratified.py             # -> frozen/run_items.json + raw/text.json (the 120)
python3 run.py floor-full              # -> raw/floor.json  (Option-A calibration)
# --- day 2 (IMAGE arm; session 112) ---
python3 run.py image-preflight          # re-measure claude raised-max_tokens cost (condition d)
IMG_LIMIT=60 python3 run.py image-full  # sub-batch 1 (60 items, <$2.50); resumable, cost-guarded
IMG_LIMIT=60 python3 run.py image-full  # sub-batch 2 (remaining 60) -> raw/image.json (120/120)
# --- day 3 (DISTRACT control; session 121) ---
python3 run.py distract-preflight        # re-confirm per-call cost + image load
IMG_LIMIT=60 python3 run.py distract-full # x2 sub-batches -> raw/distract.json; null reported FIRST
python3 analyze.py                     # day-1 sections + the full result sections (image + distract present)
```
