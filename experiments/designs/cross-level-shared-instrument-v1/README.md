# cross-level shared-instrument probe v1 — build status

**BUILT + FROZEN, NOT RUN. No probe was run and no money was spent building this.**

This directory holds a run-ready, frozen probe that applies ONE shared commitment
instrument (Option A: an explicit graded `SAME/DIFFERENT/UNCLEAR`-style categorical
decline **plus** a 0–100 confidence rating) **identically** at three semantic levels —
lexical, constructional, relational — to test the conjecture
[`conjecture/cross-level-gradience-aggregate-not-moment`](../../../wiki/findings/conjectures/cross-level-gradience-aggregate-not-moment.md)
under its resolved operationalization gate
[`decisions/resolved/cross-level-shared-instrument-operationalization`](../../../wiki/decisions/resolved/cross-level-shared-instrument-operationalization.md)
(Option A + binding conditions C1–C4 + bound Q2/Q3/Q4).

## What is frozen

- **`instrument.json`** — the single shared instrument. C2 (i)–(iv) all pinned here:
  the 0–100 confidence scale + `[40,60]` mid-band; the verbatim per-level
  `unsure/both/unclear` decline wording; the per-level `item_classes`; the per-level
  frozen `aggregate`/`moment` operational definitions (Q3, relational disclosed as the
  weaker within-record / single-reader-recoverable notion); and the cross-level
  CONFIRM/DISSOLVE/WEAK thresholds (Q2).
- **`instrument.sha256`** = `3cdfe17871a1669e690fe0f6c46ba66a5af594d48c7aa83e90538faf7a35e28f`
  (sha256 of `instrument.json` — the C2 numeric-freeze hash).
- **`items_constructional.json`** — 30 fresh synthetic items, 10 sets × {ambiguous,
  clear-reading1, clear-reading2}; six ambiguity types. `internal-contrast-only`.
- **`items_relational.json`** — 30 fresh synthetic records, 10 sets × {ambiguous-midrecord,
  clear-determinate, clear-other-determinate}. `internal-contrast-only`.
- **`items_lexical.json`** — a MANIFEST referencing the lexical leg's already-frozen
  `stratum.csv` (sha `e7d36773…`) and `wic_poles.csv` (sha `b8b1a7aa…`) by sha. No corpus
  text (DWUG CC BY-ND / WiC CC BY-NC are gitignored). Capped to usage-similarity.
- **`certify.py`** + **`certification_report.json`** — build-time, no-API shortcut/leak/
  geometry/balance checks; **17/17 PASS** (see `raw/certify_output.txt`).
- **`probe.py`** — run-ready runner; refuses to run without `--run --i-have-pre-run-critic-go`;
  `ABORT_USD = 0.60` hard stop; imports the shared harness; gemini `reasoning:{effort:"minimal"}`.
- **`analyze.py`** — the frozen cross-level reading rule encoding C1/C3/C4 + the Q2 verdict map.

## Pre-flight cost estimate (for a future run)

One temp-0 call per item per model (the decline call and confidence integer ride in one
elicitation). Item counts: constructional 30 + relational 30 = 60 synthetic; lexical up to
48 DWUG + 40 WiC = 88, if the lexical arm is staged. Worst case ≈ 148 items × 3 models ≈
**444 short-label calls**. Comparable recent single-line probes billed ≈ $0.00015–0.0007/call
(the dative working-surface runs were pricier only because they wrote justifications; this
instrument demands "one line and nothing else"). **Pre-flight estimate: ≈ $0.10–0.25** for the
full 3-model run — well inside the $5/day cap and under the $2.50 single-run flag. `ABORT_USD`
is set to $0.60 as a hard stop. Constructional+relational alone (`--skip-lexical`, 60 items ×
3) is ≈ $0.05–0.10.

## NOT run — exactly what a later session must do

This probe is **built and frozen but has NOT been run**: there is **no pre-run critic GO yet**
and **no budget has been spent**. To run it, a **later** session must, in order:

1. Obtain a **fresh independent pre-run critic GO/NO-GO** against the frozen `instrument.json`
   (its sha must still match `instrument.sha256`) and the frozen item files — re-deriving the
   cross-level cheat surface (per-level instrument-shopping is the named failure mode) and
   confirming C1–C4 are faithfully encoded in `analyze.py`. A **NO-GO defers the run**; it
   never relaxes a band.
2. Run a **budget pre-flight** per [`config/budget.md`](../../../config/budget.md) and confirm
   today's UTC-day headroom covers the ≈$0.10–0.25 estimate.
3. For the lexical arm, **stage the gitignored DWUG/WiC fulltext** via the lexical leg's
   `prep.py` / `prep_wic.py` (or run `--skip-lexical` for the two synthetic arms only).
4. Invoke `probe.py --run --i-have-pre-run-critic-go`, then `analyze.py`, then promote a
   result page (`internal-contrast-only` for the unified verdict; lexical leg capped to
   usage-similarity; **no human-comparison claim** — Q4).

## Residual design risks a pre-run critic should scrutinize

- **Comparability crux (the load-bearing risk).** The stimulus *body* unavoidably differs
  across levels (two-sentence word pair / one-sentence reading pair / stamped record). The
  design holds the *elicitation question* identical (same SAME/DIFFERENT/UNCLEAR + confidence
  frame; only the level noun and the decline gloss change). A critic should judge whether the
  body difference itself could drive a decline/confidence difference independent of
  indeterminacy. The C3 clear-class precondition per level is the guard (the instrument must
  read cleanly on each level's unambiguous controls first), but it does not fully neutralize
  the risk — disclosed in the design doc §comparability.
- **Synthetic ambiguity calibration.** The constructional "ambiguous" items are author-judged
  two-reading; the relational "ambiguous-midrecord" items are author-constructed
  same-round dual bindings. A critic should sanity-check that the ambiguous items are
  genuinely two-reading and the clear controls genuinely one-reading (certify.py checks
  *structure*, not human-judged ambiguity strength). `internal-contrast-only` bounds the
  claim regardless.
- **Relational "aggregate" is the weakest leg.** Per Q3 it is within-record /
  single-reader-recoverable, not a population statistic. A confirm that excludes relational is
  only a 2-level R2 regularity (reporting nuance, encoded in `analyze.py`).
- **Confidence as self-report (C4).** Already caught channel-sensitive at the lexical leg; C4
  re-routes a confidence-only shift to a self-report effect, encoded in `analyze.py`.
- **Small, clustered N.** ~10 sets/level; direction-of-effect with wide clustered CIs, no
  coverage claim.

## Open decision opened by this build

None. The build reused the resolved gate's already-fixed choices throughout. No new
`wiki/decisions/open/` entry was opened. (If a pre-run critic judges the comparability
residual above to be an *operationalization* choice the gate did not settle — rather than a
disclosed-and-bounded risk — that would be the trigger to open one; the builder judged it a
disclosed residual within Q3's frozen comparability slot, not a new undecided knob.)
