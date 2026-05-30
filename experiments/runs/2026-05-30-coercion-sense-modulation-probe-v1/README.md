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

_(to be filled after the run + independent post-run number verification.)_
