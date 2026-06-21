---
type: design
id: lexical-bridging-context-v1
title: lexical bridging-context probe v1 — does a model land in an intermediate, lower-confidence regime on human-rated usage-similarity-midpoint (bridging) items, between clear-same and clear-different, with a context-ambiguity control and a claim cap to usage-similarity?
meaning-senses:
  - distributional
  - referential
  - human-comparison
status: draft
anchor: resource/dwug-usage-graphs
contingent-on: []
created: 2026-06-21
updated: 2026-06-21
links:
  - rel: operationalizes
    target: open-question/lexical-bridging-context-gradience
  - rel: refines
    target: conjecture/lexical-sense-gradience
  - rel: depends-on
    target: resource/dwug-usage-graphs
  - rel: depends-on
    target: resource/wic-word-in-context
  - rel: depends-on
    target: concept/polysemy
  - rel: depends-on
    target: concept/referential-meaning
---

# Experiment design v1 — lexical bridging-context probe (within-item gradience)

> **Status: draft — frozen stratum + design, NOT yet runnable.** Both gates are
> ratified cross-session:
> [`decisions/resolved/lexical-bridging-context-operationalization`](../../wiki/decisions/resolved/lexical-bridging-context-operationalization.md)
> (B-primary graded-confidence + C-categorical-cross-check fixed panel; A
> characterizing-only; per-axis reading rule; numeric freeze before data) and
> [`decisions/resolved/lexical-bridging-context-anchor`](../../wiki/decisions/resolved/lexical-bridging-context-anchor.md)
> (DWUG-derived bridging stratum + WiC clear poles; ≥3-rater floor; claim CAP to
> usage-similarity; collapse to `internal-contrast-only` if the floored pool is too
> thin). This page encodes the design and references the **frozen candidate
> stratum**; two things still block a run: (i) the DWUG corpus text must be
> **re-fetched** (gitignored, absent from a fresh clone, no re-fetch script), and
> (ii) the **instrument numbers** (B's midpoint band, C's verbatim third-option
> wording, A's sample/temperature) must be **frozen + sha256'd** at build time under
> an independent pre-run critic. See [`BUILDABILITY.md`](lexical-bridging-context-v1/BUILDABILITY.md)
> for the surviving pool sizes and the conditional RUNNABLE/collapse verdict.

This operationalizes the **one untested clause** of
[`conjecture/lexical-sense-gradience`](../../wiki/findings/conjectures/lexical-sense-gradience.md)
— Prediction 4, verbatim:

> "Deliberately sense-ambiguous (bridging) contexts, engineered so two senses are
> co-present, yield **intermediate, less-confident** model behavior rather than a
> forced discrete pick — the behavioral fingerprint of gradience."

The probe asks whether a panel model's same/different-sense behavior on a **bridging**
item lands in an **intermediate, lower-confidence** regime *between* its behavior on
clearly-same and clearly-different items — the **within-item** gradience fingerprint,
distinct from v1's cross-item monotonicity. See
[`open-question/lexical-bridging-context-gradience`](../../wiki/findings/open-questions/lexical-bridging-context-gradience.md).

## 0. The binding claim cap and label discipline (read first)

Anchor condition (6): any human-comparison claim from this design is **about
usage-similarity intermediacy only** — the model is less confident where humans rated
/ split mid usage-similarity. It may **NOT** claim humans certified two senses
co-present. A DWUG mid-scale (DURel 2-3) pair is a **human-rated usage-similarity
midpoint / high-disagreement** item, **not** a certified within-sense bridge: it can
also arise from a homonym halfway-point, register/topic drift, or annotator noise
(DWUG "does not tag pairs as polysemy vs. homonymy"). "bridging" names the *class
being probed*, never the *certification* of an item. Every artifact built on this
design carries that label. On the DWUG route the result is **not**
`internal-contrast-only` (a real human signal anchors it), but its human-comparison
force is scoped to usage similarity.

## 1. The three frozen item classes + the stratum artifact

Three classes are contrasted for usage pairs of the same target word. Definitions are
frozen on the rounded human DURel median, with a binding **≥3-rater floor**:

| class | rule | reading |
|---|---|---|
| clear-same | `human_median >= 3.5` | high-agreement DURel-4 pole |
| **bridging** | `1.5 < human_median < 3.5` | DURel 2-3 = usage-similarity midpoint |
| clear-different | `human_median <= 1.5` | DURel-1 pole |

The bridging band may be cross-cut by high `human_spread` (annotator disagreement);
spread is reported as a **secondary descriptor**, not a second class definition (the
median-band is primary).

**Stratum artifact (frozen):**
[`lexical-bridging-context-v1/stratum.csv`](lexical-bridging-context-v1/stratum.csv),
emitted deterministically by
[`lexical-bridging-context-v1/freeze_stratum.py`](lexical-bridging-context-v1/freeze_stratum.py)
from the v1 within-period manifest. **Manifest-derived columns only — no corpus
text** (CC BY-ND posture). sha256
`e7d36773cffaa8cccb90df229d518d75139b0666483f361a6ed867d405c8186d`
([`stratum.sha256`](lexical-bridging-context-v1/stratum.sha256)) — the
frozen-before-output hash (anchor condition 3). Surviving pool (anchor condition 2):
clear-same **9** pairs / 7 lemmas, bridging **24** / 17, clear-different **15** / 9
(48 of 200; 152 dropped by the rater floor). Within-period is **already enforced** in
the source manifest (v1's Q4 filter; the `period` column is the single shared period
per pair) — anchor condition (4) is satisfied by construction.

**WiC clear-pole supplement (permitted, not yet frozen).** Anchor condition (1)
allows [`resource/wic-word-in-context`](../../wiki/base/resources/wic-word-in-context.md)
T/F items to supplement the **two clear poles only, never the bridging stratum**.
Advisable because the floored clear-same pole is thin (9/7). A build session may
freeze a separate WiC pole manifest (kept apart from the DWUG stratum, its own sha).

## 2. Instrument panel (frozen panel shape; numeric values are PLACEHOLDERS)

Per the operationalization gate: a **fixed two-instrument panel** plus a
characterizing-only third. No instrument may be added, dropped, re-worded, or
re-thresholded after any output is seen (condition a).

- **B (primary) — explicit graded-confidence.** The model gives the same/different
  call **and** a graded confidence/relatedness rating per item. Expresses *both*
  axes (position = side of midpoint; confidence = distance from the confident
  extremes). Reuses the v1-validated `durel`/`cont` framing repurposed per-item.
  - PLACEHOLDER (freeze at build, sha256'd): the rating **scale** and the exact
    numeric **intermediate midpoint band** that counts as "intermediate."
- **C (categorical cross-check) — a "both / unclear" third option.** The model is
  given an explicit third option and the signal is whether it takes it **more on
  bridging than on clear items** (an elevated decline rate). Behaves differently from
  B, so B–C agreement is stronger than either alone.
  - PLACEHOLDER (freeze at build, sha256'd): the **verbatim third-option wording**.
- **A (characterizing-only) — forced-judgment dispersion.** The model is forced to
  pick same/different (no third option, no confidence); the dispersion of picks
  across paraphrases/samples *describes* but never *decides* (condition g); its knobs
  never enter the verdict.
  - PLACEHOLDER (freeze at build, sha256'd): **sample/paraphrase count** and
    **temperature** for any A read.

Temperature 0 for B and C (panel default; A may sample). Logprob-free, runs on the
existing panel ([`config/models.md`](../../config/models.md)).

## 3. Per-axis reading rule (frozen before data)

Not a blanket AND (operationalization condition c / modification 2):

- **Position axis** — certified by **B alone**: bridging sits strictly *between* the
  two clear classes on B's same/different signal.
- **Confidence/dispersion axis** — certified by **both B and C**: bridging shows
  mid-band confidence (B) *and* an elevated decline rate vs **both** clear classes (C).
- **Prediction 4 = supported** only if position holds (B) **and** dispersion holds on
  **both** B and C.
- **Disagreement = mixed/weak, NOT the null** (condition d / modification 3): B–C
  disagreement on the dispersion axis is reported as a mixed/weak result with both
  readings shown, never collapsed into the clean null.
- **Clean null** (reported as cleanly as a positive): bridging handled at clear-item
  confidence **and** clear-item decline rate — a graded *scale* with ungraded
  *commitment* (within-item discreteness).
- **Clear-class precondition** (condition e): interpretable only if the clear classes
  show high confidence (B) and low decline rate (C); report as a precondition, else
  NO-GO. (The thin clear-same pole is why WiC supplementation is advised — §1.)

## 4. Q3 context-ambiguity control (non-optional; data slot present, weak)

Operationalization condition (f): a v1-style context-similarity control measured
**independently** of the sense signal must be in the design, so within-item
uncertainty is shown to track **sense** indeterminacy, not mere **context**
indeterminacy (the distributional shadow at the lexical-uncertainty grain).

The stratum carries the v1 clause-(c) columns `overlap_jaccard` / `overlap_tokenf1`
(content-token overlap of the two usage sentences minus the target). Across the 48
floored pairs these are **near-degenerate** (mean jaccard 0.0025; only 4/48 nonzero) —
this rules out the *surface* shadow a priori but is a **weak** independent control. As
in v1, the operative stronger control is partialling out the model's own
**topic-similarity** rating (a model-internal control, flagged modest). The result
must disclose that the independent lexical-overlap slot is near-degenerate and not
over-claim sense-tracking (a residual risk the operationalization gate names).

## 5. Indicators and reading (frozen with the stratum + instrument; no manufactured pass bar)

- **Position (B):** per-class central tendency of the same/different signal; bridging
  expected between the clear classes. Report with per-lemma-clustered uncertainty.
- **Confidence (B):** per-class rating distance from the confident extremes; bridging
  expected mid-band, clear classes confident (precondition).
- **Decline rate (C):** per-class rate of the third option; bridging expected
  elevated vs both clear classes.
- **Dispersion (A, characterizing-only):** per-class flip-rate/entropy across
  paraphrases — described, never decisive.
- **Q3:** the partial relation controlling for the independent context measure and
  the model's topic rating (§4).

No threshold is tuned after the run. The clean null and the mixed/weak result are
each reported as cleanly as a positive (§3).

## 6. Claim scope, human anchor, collapse condition

- **Anchor:** the bridging position/confidence contrast is anchored to DWUG's graded
  human DURel signal ([`resource/dwug-usage-graphs`](../../wiki/base/resources/dwug-usage-graphs.md)),
  **capped to usage-similarity intermediacy** (§0). The clear-pole supplement is
  anchored to WiC binary labels. No human label is invented.
- **Collapse condition (anchor 2, 6):** if, after the instrument is frozen, the
  clear-same precondition cannot be met even with WiC support, or the bridging pool is
  too thin to express the per-axis ordinal pattern, the probe runs as **Route 3
  `internal-contrast-only`** and must be relabelled — a within-model contrast, no
  human-comparison claim. That call is empirical and belongs to the build/critic
  session.

## 7. Run blocker + pre-run-critic gate (handoff)

1. **Re-fetch corpus text** — DWUG `dwug_en.zip` (Zenodo 14028531) into the
   gitignored data area; re-map `id1`/`id2` to usage sentences + target offsets;
   re-record archive sha256. WiC `WiC_dataset.zip` likewise if poles are supplemented.
   **This is the run blocker:** the stratum carries only identifiers + ratings, no
   text. (See [`BUILDABILITY.md`](lexical-bridging-context-v1/BUILDABILITY.md).)
2. **Freeze + sha256 the instrument numbers** (the §2 placeholders) under an
   independent pre-run critic (operationalization condition b).
3. **Optionally freeze the WiC clear-pole supplement** (item ids + gold), separate
   from the DWUG stratum, its own sha.
4. **Pre-run critic GO/NO-GO** against the frozen stratum + instrument
   (operationalization condition h): a NO-GO defers the run, never relaxes a band,
   wording, or the agreement rule. Re-check the clear-class precondition; if unmet,
   collapse to `internal-contrast-only` (§6).
5. Run (spend-bearing; pre-flight per [`config/budget.md`](../../config/budget.md));
   review; only then promote a result, leading with the usage-similarity-vs-sense
   label discipline.

## 8. Scope and limits (lead with these)

- **Behavioral, not representational.** Like v1-v3, this is behavior on ambiguous
  items, not evidence of graded sense *representations* (small-model lane deferred).
- **Small, lemma-clustered N.** 48 floored pairs over ~20 lemmas; direction-of-effect
  with wide per-lemma uncertainty, no coverage claim, no claim beyond these
  lemmas/register/framing.
- **Usage-similarity ≠ sense-co-presence** persists after the claim cap; the result
  must **lead** with it (§0).
- **DWUG EN low end mixes homonymy** (v1 flagged `lass`/`lassi`); the mid-band may
  inherit homonym halfway-points, contaminating the polysemy-bridge reading.
- **Within-item uncertainty ≠ between-stratum discreteness;** a result here neither
  confirms nor disturbs the conjecture's clause-(b) powered null.
