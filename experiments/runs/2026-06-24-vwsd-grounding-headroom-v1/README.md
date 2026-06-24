# VWSD grounding-headroom probe v1 (run dir)

First **image-native / multimodal RUN** in the project. Implements the frozen design
[`experiments/designs/vwsd-grounding-headroom-v1.md`](../../designs/vwsd-grounding-headroom-v1.md)
under the ratified DV decision `decisions/resolved/vwsd-grounding-headroom-dv`. Finding:
[`wiki/findings/results/vwsd-grounding-headroom-v1.md`](../../../wiki/findings/results/vwsd-grounding-headroom-v1.md).

## What's here (committed)

- `build_items.py` — freezes the 463 EN gold-test items from the annotation overlay → `frozen/items.json`.
- `run.py` — the harness: `caption-full`, `text-full`, `image-full`, `distract-full` (+ `*-preflight`).
- `analyze.py` — scores per the design (distraction null first; floor check; rescue read; ceiling-caveated slope).
- `frozen/` — `en.test.data.v1.1.txt` + `en.test.gold.v1.1.txt` + `README.txt` (the CC-BY-NC annotation
  overlay), `items.json` (all 463), `run_items.json` (the 50-item seeded subset, seed 20260624,
  sha `657fceb7…`), `captions.json` (497 captions, sha `528772e4…`).
- `raw/` — `text.json` (sha `ff6289bb…`), `image.json` (sha `e171d4a8…`), `distract.json` (sha `5be792b1…`).

## What's NOT here (out of git — see .gitignore)

**VWSD images are not redistributable** (resource `vwsd-semeval-2023`, License & redistribution
unconfirmed). The 572 MB resized EN test zip (sha `b9f2f1e1…af8f`) and the 4090 extracted EN candidate
images are **fetched at runtime** and never committed.

## Reproduce

```
# fetch the resized EN test images from the official task site (raganato.github.io/vwsd),
# extract the 4090 EN candidates to a local dir, then:
export VWSD_IMAGES=/path/to/en_images
export OPENROUTER_API_KEY=...
python3 build_items.py                 # -> frozen/items.json (then the seeded subset is frozen)
python3 run.py caption-full            # -> frozen/captions.json   (one-time, $0.89)
python3 run.py text-full               # -> raw/text.json  (FROZEN covariate, before images)
python3 run.py image-full              # -> raw/image.json
python3 run.py distract-full           # -> raw/distract.json
python3 analyze.py                     # the scored result
```

## Result in one line

Caption-text baseline **saturated** (.86–.88; 40/50 text-separable; under-determined bin 7 < floor 8 →
binned interaction suppressed); **distraction null clean** (.093 ≈ chance); **no broad image lift**
(gpt worse with images; rescue 4/16) → **neither confirms nor falsifies** the gating prediction.
450 finding-bearing calls, $3.204 billed (+ $0.887 captions). Pre-run critic GO + post-run verifier
REPRODUCED.
