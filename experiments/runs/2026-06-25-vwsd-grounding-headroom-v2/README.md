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

## What's committed vs out of git

- **Committed:** the CC-BY-NC annotation overlay (`frozen/en.test.{data,gold}.v1.1.txt`), the built
  item/pool sets, the frozen descriptors + leak audit + draw + covariate, and the raw call records
  (text/floor + cost ledgers — text only, no image bytes).
- **OUT of git** (`.gitignore`; redistribution unconfirmed): the 572 MB resized EN test zip
  (sha256 `b9f2f1e1…af8f`) and the 4090 extracted candidate images. Fetched at runtime from the
  official task site (`raganato.github.io/vwsd`, Drive id `15ed8TXY…`), read via `$VWSD_IMAGES`,
  never re-hosted.

## Reproduce (day 1)

```
# fetch + extract the 572MB resized EN test images, verify sha256 b9f2f1e1…af8f
export VWSD_IMAGES=/path/to/en_images
export OPENROUTER_API_KEY=...
python3 build_items.py
python3 build_pool.py
python3 run.py descriptor-preflight     # eyeball policy + per-image cost
python3 run.py descriptor-full          # -> frozen/descriptors.json  (~$3.97; resumable)
python3 run.py leak-full                # -> frozen/descriptors.json:leak
python3 run.py text-full                # -> raw/pool_text.json  (separability covariate)
python3 draw_stratified.py             # -> frozen/run_items.json + raw/text.json (the 120)
python3 run.py floor-full              # -> raw/floor.json  (Option-A calibration)
python3 analyze.py                     # day-1 sections (text acc, sep strata, floor, leak)
```
