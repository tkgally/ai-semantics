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
