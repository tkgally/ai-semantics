# Run record — coercion-as-sense-modulation bridge probe (v1)

**Date:** 2026-05-30
**Design (frozen):** [`design/coercion-as-sense-modulation-v1`](../../designs/coercion-as-sense-modulation-v1.md)
**Theory:** [`theory/lexicon-grammar-continuum`](../../../wiki/findings/theory/lexicon-grammar-continuum.md) (the empirical bridge it proposes)
**Reuses the instrument of:** [`result/lexical-sense-gradience-v1`](../../../wiki/findings/results/lexical-sense-gradience-v1.md)
**Result page:** [`result/coercion-sense-modulation-v1`](../../../wiki/findings/results/coercion-sense-modulation-v1.md)

## What ran (the lexicon–grammar bridge)

Tests whether **constructional coercion registers as a lexical sense shift** in the DWUG-style relatedness instrument. The target is the **verb**, marked «» in two sentences (sentence 1 = a bare/neutral use). Arms:

| arm | sentence 2 | predicted |
|---|---|---|
| `coerced-cm` | caused-motion coercion (*sneezed the napkin off the table*) | low (sense shifted) |
| `coerced-way` | way-construction coercion (*whistled her way down the hall*) | low |
| `control-elab` | length-matched **non-coercing** elaboration (*sneezed twice during the lecture*) | high (same sense) |
| `polysemy-anchor` | a genuine lexical sense shift (*ran a marathon* → *ran a company*) | low (calibration) |

- **Instrument:** the lexical v1 relatedness rating reused verbatim — `durel` (4-point) + `cont` (0–100). Temperature 0 → the 3-family panel ([`config/models.md`](../../../config/models.md)).
- **Stimuli:** own constructed sentences (committable; no corpus/licence issue), 30 items (6 cm + 6 way verbs × {coerced, control} + 6 polysemy anchors), frozen pre-run `items.csv` sha256[:16] `fda172ab707b6a73`. Verbs drawn from the caused-motion / way sets whose coercion is independently evidenced by [`result/caused-motion-near-miss-v2c`](../../../wiki/findings/results/caused-motion-near-miss-v2c.md) / [`result/way-construction-traversal-v1`](../../../wiki/findings/results/way-construction-traversal-v1.md).
- **Reading rule (report-the-rate; internal-contrast):** the **coercion sense-shift gap** = mean(`control-elab`) − mean(`coerced`); positive ⇒ the model rates the coerced verb as *less* sense-related than a matched elaboration ⇒ it registers coercion as sense modulation. `polysemy-anchor` must read low for a null to be interpretable. No pass bar; no threshold tuned post-run.

## Human anchor

**Pending / internal-contrast-only.** No in-repo human relatedness rating for constructed coercion pairs; no human-comparison claim. The *instrument* is DWUG-validated (it tracks human DURel, per the lexical v1 result), but these items are the project's own.

## Pre-registration / no-retuning

- Arms, predictions, reading rule fixed before the build; items frozen + committed before any probe call (sha256 above); a build assert checks the verb is marked in both sentences of every item.
- **Adversarial pre-run pass:** independent read-only subagent (see below).

## Files

- `build_items.py` — emits + freezes `items.csv`. `probe.py` — durel + cont × 3 models (imports `experiments/lib/openrouter.py`, billed `usage.cost`). `analyze.py` — per-arm means + coercion gap + within-verb sign + polysemy calibration → `raw/results.json`.

## Pre-run critique

An **independent read-only adversarial critic** reviewed the stimuli + design. **One BLOCKER fixed before the run + re-frozen:**

- **B1 (fixed) — `poly-bank` was a NOUN pair** (*river bank* / *the bank*), contradicting the "rate the VERB" instruction and contaminating the homonymy-floor anchor. **Fixed:** replaced with a verb homonym (*the plane «banked» sharply* / *she «banked» the cheque* — tilt vs deposit). Re-frozen; hash `6e6efb432be04a76` → **`fda172ab707b6a73`**.

**Inherent confound the critic flagged (I1) — handled by down-claiming in the result, not editable:** the coerced sentence-2 always carries **added object+path argument structure** that the `control-elab` arm lacks (that *is* what coercion is). So a positive gap **cannot by itself separate "the model detects a SENSE shift" from "the model rates any added transitive/path structure as less verb-related."** The result therefore makes only the internal-contrast claim ("the panel rates a coerced use as less verb-related than a matched non-coercing elaboration") and **explicitly disclaims** the stronger sense-vs-surface reading; the polysemy anchors (no added structure, yet should read low) show pure sense shift *can* drive low ratings but do not control the coerced arm's surface confound. A cleaner v2 control (a non-coercing *transitive* use of the same verb) is noted as future work.

**Framing notes applied to the result (SHOULD-FIX / NIT):** report the **cm/way split** and the **per-item polysemy spread** rather than one averaged number (the poly anchors span homonymy `bank`/`charge` → polysemy `run`/`set`, so the floor is high-variance — a non-low anchor is not the anchor "failing"); `huff`-the-wrapper is the most marginal cm coercion (outlier risk); the metaphorical way items (`smile`/`joke`/`bluff` *way into/out of*) carry an extra literal→figurative shift on top of the coercion. Pre-committed three-way ordering to report: control ≥ coerced ≥ polysemy-anchor.

VERDICT after fix: sound to run (with the result-page down-claim per I1).

## Results / cost

180 calls, **0 NA**, cost **$0.249 billed** (A $0.024 / B $0.012 / C $0.212; gemini reasoning-heavy as usual).

**Headline: constructional coercion registers as a PARTIAL sense shift in the lexical instrument — for all three models, both framings.** Mean relatedness per arm (the calibration worked: `control-elab` near-ceiling, `polysemy-anchor` low, `coerced` in between):

| model | framing | control-elab | coerced-cm | coerced-way | polysemy-anchor | gap (control − coerced) |
|---|---|---|---|---|---|---|
| claude-sonnet-4.6 | durel | 3.75 | 2.67 | 3.00 | 1.67 | **0.92** (cm 1.08 / way 0.75) |
| claude-sonnet-4.6 | cont | 91.2 | 57.8 | 61.7 | 15.8 | **31.4** |
| gpt-5.4-mini | durel | 3.83 | 2.67 | 3.50 | 1.33 | **0.75** |
| gpt-5.4-mini | cont | 96.8 | 64.8 | 87.8 | 18.7 | **20.5** (cm 32 / way 9) |
| gemini-3.5-flash | durel | 3.75 | 3.00 | 3.50 | 1.67 | **0.50** |
| gemini-3.5-flash | cont | 96.7 | 86.7 | 90.0 | 15.0 | **8.3** |

- The **three-way ordering control ≥ coerced ≥ polysemy-anchor holds in all 6 cells**; the coercion gap is **positive for every model/framing**; the within-verb sign is 8–11 of 12. So the panel rates a coerced verb use as **less sense-related to its bare use than a matched non-coercing elaboration** — coercion shows up *inside* the lexical relatedness instrument.
- **Partial, not full:** the coerced arms stay well above the genuine-sense-shift `polysemy-anchor` floor — coercion is a *milder* sense modulation than a polysemy/homonymy switch.
- **Construction + model structure:** caused-motion (cm) registers as a bigger shift than the way-construction for every model (cm gap > way gap); the metaphorical way items (`smile`/`joke`/`bluff`) are the mildest. **gemini shows the smallest coercion gap** (cont 8.3; it rates coerced uses as still ~90 related) despite being the strongest pure sense-gradience tracker (lexical v1 ρ=0.83) — strongest lexical tracker ≠ most coercion-sensitive; claude is the most coercion-sensitive (gap 31).

**Critical caveat (the pre-run critic's I1, inherent to the design):** the coerced sentence-2 always adds object+path argument structure the control lacks, so this gap **cannot fully separate "the model registers a SENSE shift" from "the model rates added transitive/path structure as less verb-related."** The result is an **internal-contrast** finding; the polysemy anchors show pure sense shift *can* drive low ratings but do not control the coerced arm's surface confound. A v2 with a non-coercing *transitive* control is the clean follow-up.

Reproducible from `raw/results.json`. **Post-run verification:** all arm means, gaps, within-verb signs, the 180/0 totals, and the three-way ordering independently recomputed from `raw/*.json` → **CLEAN — all figures verified**.
