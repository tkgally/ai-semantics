---
type: result
id: lexical-bridging-context-v1
title: "Lexical bridging-context probe v1 — graded scale, ungraded commitment: all three models place human-rated usage-similarity-midpoint pairs at an intermediate relatedness position, yet meet them with clear-item confidence and almost never decline (Prediction 4 null, 3/3)"
meaning-senses:
  - distributional
  - referential
  - human-comparison
status: proposed
anchor: resource/dwug-usage-graphs
contingent-on: []
created: 2026-06-22
updated: 2026-07-05
links:
  - rel: operationalizes
    target: open-question/lexical-bridging-context-gradience
  - rel: refines
    target: conjecture/lexical-sense-gradience
  - rel: supports
    target: essay/graded-scale-ungraded-commitment
  - rel: refines
    target: result/lexical-sense-gradience-v1
  - rel: anchors
    target: resource/dwug-usage-graphs
  - rel: depends-on
    target: resource/wic-word-in-context
  - rel: depends-on
    target: concept/polysemy
  - rel: supports
    target: claim/lexical-graded-scale-ungraded-commitment
---

# Result: lexical bridging-context probe v1 — graded scale, ungraded commitment

> **Status: proposed (2026-06-22, session 77).** The first run of the lexical
> bridging-context probe — the **one untested clause** (Prediction 4) of the otherwise
> `tested` [`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md).
> Design: [`design/lexical-bridging-context-v1`](../../../experiments/designs/lexical-bridging-context-v1.md).
> Gates ratified cross-session ([`decisions/resolved/lexical-bridging-context-operationalization`](../../decisions/resolved/lexical-bridging-context-operationalization.md),
> [`decisions/resolved/lexical-bridging-context-anchor`](../../decisions/resolved/lexical-bridging-context-anchor.md));
> instrument frozen+sha256'd before the run; independent pre-run critic GO (session 76).
> **2376 calls, $0.756 billed, 0 missing cost, 0 parse failures, 0 errors.**

> **Update (2026-07-05, session 183 — wiki-coherence pass).** The commitment leg was later
> channel-checked and qualified: [`result/lexical-bridging-context-working-surface-v1`](lexical-bridging-context-working-surface-v1.md)
> (session 79) found the null largely channel-controlled but read claude **MIXED/WEAK** under a
> format-only working surface (self-reported confidence softened; categorical decline held), with
> gpt declining the surface. [`result/lexical-bridging-context-forced-decomposition-v1`](lexical-bridging-context-forced-decomposition-v1.md)
> (session 82) then forced gpt's uptake (MIXED/WEAK at the jitter floor), and
> [`result/lexical-bridging-context-forced-decomposition-repeated-runs-v1`](lexical-bridging-context-forced-decomposition-repeated-runs-v1.md)
> (session 88) de-noised that leg to the channel-controlled null. The consolidated statement is
> [`claim/lexical-graded-scale-ungraded-commitment`](../claims/lexical-graded-scale-ungraded-commitment.md).
> *(Back-annotation added by a maintenance pass; nothing measured or decided on this page changes.)*

## Lead with the cap (binding, read first)

Every human comparison below is **about usage-similarity intermediacy ONLY** (anchor
condition 6). A DWUG mid-scale (DURel 2–3, ≥3-rater) pair is a **human-rated
usage-similarity midpoint / high-disagreement** item — **not** a certified within-sense
bridge. "bridging" names the *class being probed*, never the *certification* of an item;
a DWUG mid-band pair can also be a homonym halfway-point, register/topic drift, or
annotator noise (DWUG "does not tag pairs as polysemy vs. homonymy", and the EN low end
mixes homonymy). This result does **not** claim humans certified two senses co-present,
and a positive on the position axis is **not** evidence the model "represents bridging
senses." This is behavioral, not representational.

## Headline

**Prediction 4 returns its first-class NULL, cleanly and on all three models: a graded
SCALE with ungraded COMMITMENT.** On usage pairs humans rated as usage-similarity
midpoints (the bridging class), every panel model places the pair at an **intermediate
relatedness position** between its clearly-same and clearly-different behavior — the
within-item echo of v1's cross-item scale — **yet meets that same ambiguous item with
clear-item-level confidence, almost never takes the explicit "UNCLEAR" option, and shows
near-zero dispersion across forced re-samples.** Gradience in the ledger; none in the
moment.

This is exactly the possibility [`essay/graded-scale-ungraded-commitment`](../essays/graded-scale-ungraded-commitment.md)
argued was logically independent of v1's scale and substantive if realized — and it is
realized (the essay's revision trigger **(b)** fires).

## Panel and design (frozen)

- **Panel:** [`config/models.md`](../../../config/models.md) — claude-sonnet-4.6 (A),
  gpt-5.4-mini (B), gemini-3.5-flash (C). Logprob-free behavioral probe.
- **Items (88):** 48 DWUG within-period stratum pairs (clear-same 9 / **bridging 24** /
  clear-different 15; ≥3-rater floor) + 40 WiC clear-pole supplement (20 gold-T
  clear-same + 20 gold-F clear-different). WiC supplements the **two clear poles only,
  never the bridging stratum** (anchor condition 1). DWUG archive sha `64eef477…`
  (matches pin); WiC archive sha `f1a2fb67…` (matches [`resource/wic-word-in-context`](../../base/resources/wic-word-in-context.md)).
- **Frozen instrument** ([`instrument.json`](../../../experiments/designs/lexical-bridging-context-v1/instrument.json),
  sha `901ea89f…`), per-axis reading rule fixed before any output:
  - **B (primary, temp 0):** `b_rel` 0–100 relatedness = **position** axis; `b_conf`
    SAME/DIFFERENT + 0–100 **confidence** = confidence axis.
  - **C (cross-check, temp 0):** `c_third` SAME/DIFFERENT/**UNCLEAR**; decline rate =
    %UNCLEAR (a categorical commitment instrument, robust to B's self-report).
  - **A (characterizing-only, temp 1.0, 5 samples):** `a_forced` dispersion (entropy of
    forced picks). **Never enters the verdict.**
  - **Q3 control (temp 0):** `topic` 0–100 topic similarity ignoring the target.

The reading rule certifies the **position** axis by B alone, and the
**confidence/dispersion** axis by **both** B (confidence) and C (decline). Prediction 4
is supported *iff* position holds **and** confidence/dispersion holds on **both** B and C.
The first-class null — bridging handled at clear-item confidence **and** clear-item
decline — is "graded scale, ungraded commitment," to be **reported as cleanly as a
positive**.

## Clear-class precondition: MET (3/3) — the result is interpretable as a human comparison

The contrast is interpretable only if the clear classes are confident and rarely decline
(else NO-GO → collapse to `internal-contrast-only`). **All three models pass, with the
WiC supplement giving the thin DWUG clear-same pole enough mass:**

| model | clear-same b_rel | clear-diff b_rel | clear-same b_conf | clear-diff b_conf | clear %UNCLEAR |
|---|---|---|---|---|---|
| claude | 78.9 | 29.3 | 85.1 | 88.1 | ≤3.4% |
| gpt | 74.4 | 29.7 | 94.2 | 96.3 | 0% |
| gemini | 82.5 | 24.1 | 92.4 | 98.3 | 0% |

Poles saturated (clear-same high, clear-different low), confidence high (≥85), decline
near-zero. So this result is **DWUG-anchored** (capped to usage-similarity), **not**
`internal-contrast-only`.

## The three axes (dwug+wic scope; n: clear-same 29, bridging 24, clear-different 35)

### Position axis (B/`b_rel`) — GRADED, 3/3

Bridging sits strictly between the clear classes and lands inside the frozen [40,60]
intermediate band for all three:

| model | clear-diff | **bridging** | clear-same | in [40,60]? | between (CI-strict)? |
|---|---|---|---|---|---|
| claude | 29.3 | **41.3** | 78.9 | yes | partial (DWUG+WiC br−cd CI [−3.9, 28.0] grazes 0; **DWUG-only CI-strict yes**) |
| gpt | 29.7 | **49.8** | 74.4 | yes | **yes** |
| gemini | 24.1 | **45.5** | 82.5 | yes | **yes** |

The position signal is graded for all three (CI-strict for all three on the DWUG-only
clears; claude's DWUG+WiC lower gap grazes zero only because adding WiC clear-different
items raises that pole's mean). This is v1's cross-item scale reappearing at the
**within-class** grain — the "graded scale."

### Confidence axis (B/`b_conf`) — UNGRADED, 3/3

Bridging confidence is **not robustly lower** than the clear classes; it is high
everywhere, with ≤5-point spread, and for two models it is not even pointwise below
clear-same:

| model | clear-diff | **bridging** | clear-same | bridging lower than BOTH? |
|---|---|---|---|---|
| claude | 88.1 | **82.6** | 85.1 | pointwise yes (~3–5 pts), **CI not strict** |
| gpt | 96.3 | **95.7** | 94.2 | **no** (above clear-same) |
| gemini | 98.3 | **94.8** | 92.4 | **no** (above clear-same) |

### Decline axis (C/`c_third` %UNCLEAR) — UNGRADED, 3/3

Given an explicit "UNCLEAR — genuinely in between" option, the models almost never take
it, and **not more on bridging**:

| model | clear-diff | **bridging** | clear-same |
|---|---|---|---|
| claude | 0% | **0%** | 3.4% |
| gpt | 0% | **4.2%** (1/24) | 0% |
| gemini | 0% | **0%** | 0% |

### Dispersion (A, characterizing-only — never decisive)

Forced-pick entropy is near-zero everywhere (≤0.3 bits of a possible 1.0); bridging is
not consistently the most dispersed (gpt's *clear-same* is actually its most dispersed
cell). Reported, not load-bearing.

### Verdict (frozen rule)

Position holds (3/3) but the confidence/dispersion axis fails on **both** B and C (3/3) —
this is **agreement, not B–C disagreement**, so it is the **clean null**, not a
"mixed/weak" result. **Prediction 4 is NOT supported on any model; the first-class null —
graded scale, ungraded commitment — is confirmed 3/3.** (The analyzer labels claude
"CLEAN NULL" and gpt/gemini "PARTIAL"; the split is only whether the *position* gap
cleared CI-strictness under WiC pooling — substantively all three are the same finding:
graded position, ungraded commitment.)

## Why the ungraded-commitment null is robust here

Three independent commitment instruments agree, which is what the per-axis rule was built
to require:

1. **Self-reported confidence (B):** flat and high on bridging.
2. **Categorical decline (C):** ≈0 on bridging even with an explicit, neutrally-worded
   third option — the instrument designed to be robust to B's self-report shows the same
   thing.
3. **Forced-pick dispersion (A, char-only):** near-zero entropy even at temperature 1.0.

The design flagged the b_conf self-report risk (a model defaulting high on every item);
the C and A corroboration is exactly the mitigation, and it holds. The models are not
hedging-on-everything (the precondition rules that out: they *do* sit at an intermediate
*position*, and clear classes are confident) — they are uniformly **committed** while
being **graded in placement**.

## Q3 context control (bound, weak — disclosed)

On bridging items, the model's relatedness rating (`b_rel`) correlates with its own
topic-similarity rating (`topic`): Pearson r = **0.53 (claude) / 0.32 (gpt) / 0.52
(gemini)**, n=24. So part of the *position* signal tracks context/topic similarity, not
purely sense — the within-item distributional shadow the design names. This qualifies the
**graded-scale** (position) reading, the same caveat v1 carried ("model-internal … not a
fully independent control"). It bears little on the **headline commitment null**, which is
about confidence/decline, not placement. The committed independent lexical-overlap control
is near-degenerate (4/48 nonzero), ruling out only the surface shadow a priori.

## What this means for the conjecture and the essay

- **[`conjecture/lexical-sense-gradience`](../conjectures/lexical-sense-gradience.md)
  Prediction 4 is now run → NULL.** The conjecture's evidential picture is complete:
  central bet (a)+(c) supported (v1), distinctive bet (b) a powered null (v3), Prediction
  4 a clean null (here). The *scale* is graded; the *commitment* is not.
- **[`essay/graded-scale-ungraded-commitment`](../essays/graded-scale-ungraded-commitment.md)
  revision trigger (b) fires:** the essay's central possibility ("graded scale, ungraded
  commitment") graduates from a conceptual fork to a described feature of the panel's
  behavior — scoped to these lemmas/register/instrument, behavioral not representational,
  usage-similarity not sense-co-presence. A `claim` page
  ([`claim/lexical-graded-scale-ungraded-commitment`](../claims/lexical-graded-scale-ungraded-commitment.md))
  carries the empirical statement.
- **Relation to clause (b):** complementary, not a substitute. v3 found no separate
  discrete *regime across strata*; this finds ungraded *commitment on single items* — a
  different, within-item kind of discreteness, now positively observed.

## Scope and limits (lead with these)

- **Behavioral, not representational.** Evidence about what the models *do* on ambiguous
  items, not about graded sense *representations*.
- **Usage-similarity ≠ sense-co-presence** (the cap, restated): bridging = human-rated
  usage-similarity midpoint, not a certified sense bridge; the DWUG EN low end mixes
  homonymy.
- **Small, lemma-clustered N.** 24 bridging pairs over 17 lemmas; direction-of-effect
  with wide per-lemma bootstrap CIs only; no coverage claim, nothing beyond these
  lemmas/register/framing.
- **b_conf is a self-report** (mitigated, not eliminated, by the C+A corroboration).
- **Q3 is bound-but-weak**: the position signal partly tracks topic; the commitment null
  is the robust part.
- **Within-item uncertainty ≠ between-stratum discreteness**: this neither confirms nor
  disturbs clause (b)'s powered null.

## Reproduce

- Stage corpus (gitignored, recipe-not-corpus): `prep.py` (DWUG, 48/48 remap) +
  `map_wic_fulltext.py` (maps the committed frozen WiC manifest's exact `wic_line`s to
  text — see the run note below).
- `OPENROUTER_API_KEY=… python3 probe.py` then `python3 analyze.py`.
- Raw outputs (no corpus text — item ids, model outputs, ratings only):
  [`experiments/designs/lexical-bridging-context-v1/raw/`](../../../experiments/designs/lexical-bridging-context-v1/);
  analysis: `analysis.json` (10000-rep lemma-clustered bootstrap, seed 20260622).

### Two run-session fixes (disclosed)

1. **gemini reasoning endpoint:** as of 2026-06-22 `gemini-3.5-flash` *rejects* reasoning
   suppression (HTTP 400, "Reasoning is mandatory … cannot be disabled"); `probe.py` now
   passes the documented `effort: minimal` fallback for google/* (reasoning_tokens=0
   confirmed; the design's `cost_control` note and §7 handoff both sanction "gemini effort
   minimal"). No frozen instrument value changed.
2. **WiC freeze reproducibility:** `prep_wic.py` seeds selection with
   `(SEED,gold).__hash__()`, which Python salts per-process, so re-running selects a
   *different* 40 items than the committed frozen manifest (`wic_poles.csv` sha
   `b8b1a7aa…`). The run used `map_wic_fulltext.py`, which treats the **committed
   manifest** as the freeze and maps its exact `wic_line`s to text — fully reproducible.
   The WiC poles are clear-pole supplements (class fixed by gold T/F, ungameable), so the
   specific items do not enter any bridging verdict.

## Verifier note

Data integrity machine-checked: 0 parse failures across the 12 single-framing files
(88 each), 0 non-parsed picks across 1320 a_forced samples, 0 API errors, 0 missing
`usage.cost` across all 2376 calls, gemini reasoning_tokens=0 throughout.
