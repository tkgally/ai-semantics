# BUILDABILITY — lexical bridging-context probe (v1 stratum)

Groundwork report demanded by the anchor decision's binding condition (2): report
the surviving per-class pool sizes **before any run**, and state plainly whether the
3-class contrast is powerable as a human-comparison claim (capped to usage
similarity) or must collapse to `internal-contrast-only`. No model calls were made;
no claim about LLM behavior is made here. Every number below is computed by
[`freeze_stratum.py`](freeze_stratum.py) from the already-committed v1 manifest
([`experiments/runs/2026-05-30-lexical-sense-gradience-probe-v1/manifest.csv`](../../runs/2026-05-30-lexical-sense-gradience-probe-v1/manifest.csv)).

Binding decisions:
[`decisions/resolved/lexical-bridging-context-anchor`](../../../wiki/decisions/resolved/lexical-bridging-context-anchor.md)
and
[`decisions/resolved/lexical-bridging-context-operationalization`](../../../wiki/decisions/resolved/lexical-bridging-context-operationalization.md).

## Frozen stratum

- File: [`stratum.csv`](stratum.csv) — manifest-derived columns only (ids, period,
  human_median/mean/n/spread, overlap_jaccard/overlap_tokenf1, bridging_class). **No
  corpus text**, matching the v1 manifest's CC BY-ND posture (the DWUG raw text is
  gitignored and absent from a fresh clone — see *Run blocker* below).
- sha256: `e7d36773cffaa8cccb90df229d518d75139b0666483f361a6ed867d405c8186d`
  ([`stratum.sha256`](stratum.sha256)). This is the frozen-before-output manifest
  hash required by anchor binding condition (3): no item may change class after any
  model output is seen.

## Class definitions (frozen)

On the rounded human DURel median (DWUG: 4 Identical / 3 Closely Related / 2
Distantly Related / 1 Unrelated):

| class | rule | reading |
|---|---|---|
| clear-same | `human_median >= 3.5` | high-agreement DURel-4 pole |
| bridging | `1.5 < human_median < 3.5` | DURel 2-3 mid-scale = **usage-similarity midpoint** |
| clear-different | `human_median <= 1.5` | DURel-1 pole |

Rater floor (binding): only pairs with **`human_n >= 3`** may enter any class. The
half-integer 2-rater levels are not reliable graded gold (v1: "151/200 pairs rest on
only 2 annotators").

## Pool sizes

### Source manifest, no rater floor (200 within-period pairs, 43 lemmas)

| class | pairs |
|---|---|
| clear-same | 50 |
| bridging | 85 |
| clear-different | 65 |

### After the `human_n >= 3` floor — **48 pairs survive** (152 dropped)

| class | pairs | lemmas |
|---|---|---|
| clear-same | **9** | 7 |
| **bridging** | **24** | **17** |
| clear-different | **15** | 9 |

Median composition of the floored classes:

- clear-same: 8 pairs at DURel 4.0, 1 at 3.5.
- bridging: 16 at DURel 3.0, 8 at DURel 2.0.
- clear-different: 15 at DURel 1.0.

The rater floor is brutal: it discards **76%** of the manifest (152/200). The floor
falls hardest on the two ends — the manifest was built balanced ~50/level, but the
≥3-rater judgments concentrate in the middle, leaving the **clear-same pole thinnest
at 9 pairs / 7 lemmas**.

## Disagreement (spread) distribution — secondary descriptor

`human_spread` = max−min annotator DURel within a pair. Reported per anchor
condition (1)'s "AND/OR high inter-rater disagreement" clause, but the **median-band
is frozen as primary**; high-disagreement is recorded as a secondary descriptor, not
a second class definition.

| class | spread 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| clear-same | 1 | 7 | 1 | 0 |
| bridging | 1 | 8 | 14 | 1 |
| clear-different | 3 | 8 | 2 | 2 |

The floored bridging band does carry the most internal disagreement (15/24 pairs at
spread ≥2), consistent with "usages humans themselves split on." But note this is a
descriptor of the same 24 pairs, not an independent enlargement of the pool.

## Q3 context-ambiguity control — the data slot, and its weakness

The operationalization gate's non-optional Q3 control (a context-similarity measure
computed independently of any sense signal) is already present in the stratum as the
v1 clause-(c) columns `overlap_jaccard` and `overlap_tokenf1` (content-token overlap
of the two usage sentences minus the target word). Across the 48 floored pairs:

- `overlap_jaccard`: min 0.0, max 0.0385, mean 0.0025; **only 4/48 pairs nonzero**.
- `overlap_tokenf1`: min 0.0, max 0.0741, mean 0.0049.

This reproduces the v1 finding that DWUG same-lemma usage sentences "barely share
content words," so lexical overlap is **near-degenerate**. That rules out the
*surface* distributional shadow a priori, but it is a **weak** Q3 control: it cannot
separate sense-indeterminacy from *topic/situation*-indeterminacy. v1 handled the
stronger control by partialling out the model's own `topic`-similarity rating — a
model-internal control flagged as only modest. A build session should plan to carry
the v1-style model-`topic` control as the operative Q3 instrument and disclose that
the independent lexical-overlap slot is near-degenerate. (The Q3 *design* belongs to
the operationalization gate; this report only confirms the data slot exists and is
near-degenerate.)

## WiC supplementation of the clear poles (anchor condition 1)

Anchor binding condition (1): WiC T/F may supplement **the two clear poles only,
never the bridging stratum**. This is relevant precisely because the floored
clear-same pole is thin (9 pairs / 7 lemmas) and clear-different is modest (15/9). A
build session may draw clean clear-same (WiC T) and clear-different (WiC F) anchor
items from [`resource/wic-word-in-context`](../../../wiki/base/resources/wic-word-in-context.md)
(7,466 balanced items) to give the poles enough mass for the precondition check
(clear classes must show high confidence / low decline-rate). WiC **cannot** touch
the bridging band: it is binary by design and pruned its closest polyseme negatives.
NB: WiC contributes corpus sentences under CC BY-NC — those would live in the run's
gitignored data area, not in this stratum file. The current `stratum.csv` is
DWUG-only; WiC poles are an at-build-time supplement, not yet frozen here.

## Verdict — RUNNABLE-as-human-comparison (capped), conditional; collapse-risk live

The 3-class ordinal contrast **is buildable from DWUG alone** at the level of a
**direction-of-effect gradience-signal probe**, with the human-comparison claim
**capped to usage-similarity intermediacy** (anchor condition 6) — NOT a
sense-co-presence claim. The bridging band (24 pairs / 17 lemmas) is the largest
floored class, and it sits between two real poles. So this is **not** an automatic
collapse to `internal-contrast-only`.

But the verdict is **conditional and the collapse risk is live**, for three reasons
the next session must weigh against its frozen instrument:

1. **Thin clear-same pole.** 9 pairs / 7 lemmas is marginal for establishing the
   clear-class precondition (operationalization condition (e): the clear classes must
   show high confidence and low decline rate, else NO-GO). WiC-T supplementation of
   this pole is advisable and permitted.
2. **Small, lemma-clustered N throughout.** 48 pairs over ~20 lemmas means per-lemma
   uncertainty is wide and the per-axis ordinal contrast (operationalization
   condition (c)) runs at intrinsically small N. Direction-of-effect only; no
   coverage claim.
3. **Usage-similarity ≠ sense-co-presence (persists after the cap).** A DURel 2-3
   pair is certified by humans only as a usage-similarity midpoint; it may be a
   homonym halfway-point, register/topic drift, or annotator noise. The DWUG EN low
   end mixes homonymy (v1 flagged `lass`/`lassi`), and the mid-band may inherit
   homonym halfway-points. Any result must **lead** with this; a positive does not
   show the model "represents bridging senses."

**Recommendation to the build session:** proceed as a **human-comparison probe
capped to usage-similarity intermediacy**, supplement the clear poles with WiC, and
treat the run as a direction-of-effect signal probe. **If**, after the instrument
numbers are frozen, the clear-same precondition cannot be met even with WiC support,
or the bridging pool proves too thin to express the per-axis ordinal pattern, the
design **collapses to `internal-contrast-only`** and must be relabelled (anchor
conditions 2 and 6). That call is empirical and belongs to the build/critic session,
not to this groundwork unit.

## Run blocker (remaining)

A **run is blocked** until the DWUG corpus usage sentences are re-fetched. The raw
DWUG archive and extracted CCOHA text are CC BY-ND and gitignored
(`experiments/data/dwug/.gitignore` is `*`), absent from a fresh clone, with **no
re-fetch script committed**. `stratum.csv` carries only usage *identifiers*
(`id1`/`id2`) and human ratings — to actually present a pair to a model, the build
session must re-fetch `dwug_en.zip` (Zenodo 14028531, sha to be re-recorded), re-map
the identifiers to their usage sentences and target offsets, and stage them in the
gitignored data area. The same applies to any WiC pole supplement (re-fetch
`WiC_dataset.zip`).

## What remains before a run (handoff)

1. **Re-fetch corpus text** (DWUG; WiC if poles supplemented) into the gitignored
   data area; re-record archive sha256(s). (Run blocker above.)
2. **Freeze the instrument numbers** under an independent pre-run critic
   (operationalization condition (b)): B's rating scale + exact intermediate midpoint
   band; C's verbatim third-option wording; A's sample/paraphrase count + temperature;
   sha256 the frozen instrument config. These are placeholders in the design spec.
3. **Optionally freeze the WiC clear-pole supplement** (T/F item ids + gold), kept
   separate from the DWUG stratum, with its own sha.
4. **Pre-run critic GO/NO-GO** against the frozen stratum + instrument
   (operationalization condition (h)): a NO-GO defers the run, never relaxes a band.
   Re-check the clear-same precondition empirically; if unmet, collapse to
   `internal-contrast-only`.
