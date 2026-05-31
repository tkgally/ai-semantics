---
type: design
id: coercion-as-sense-modulation-v2
title: coercion-as-sense-modulation v2 — the non-coercing transitive control that settles the v1 sense-vs-surface confound
meaning-senses:
  - constructional
  - referential.sense
  - distributional
status: run
anchor: internal-contrast-only
contingent-on: []
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: refines
    target: result/coercion-sense-modulation-v1
  - rel: operationalizes
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
---

# Design v2 — the non-coercing transitive control

## Why this exists

[`result/coercion-sense-modulation-v1`](../../wiki/findings/results/coercion-sense-modulation-v1.md)
found that all three models rate a verb's sense as **less related** between its bare use and its
coerced (caused-motion / way) use than a matched non-coercing *elaboration*. But the pre-run critic
flagged an **inherent confound (I1)**: the v1 coerced arm always adds **object + path argument
structure** the (intransitive) `control-elab` arm lacks. So the v1 gap **cannot separate** "the model
registers a SENSE shift" from "the model rates *any* added argument structure as less verb-related."
v2 is the clean follow-up the v1 result named.

## The fix — a structure-matched conventional-transitive arm

For each verb, v2 adds a **non-coercing transitive** arm: a **lexically conventional** use with a
direct object + PP (V + NP + PP), **structure-matched** to the coerced way-construction arm
(V + POSS *way* + PP). Both arms add comparable argument structure to the bare reference; **only the
coerced arm coerces a new sense.** Arms (sentence 1 = bare reference, verb marked «»):

| arm | sentence 2 | structure | predicted |
|---|---|---|---|
| `coerced-way` | *whistled her way down the hall* | V + way + PP | LOW (sense shifted) |
| `transitive-ctrl` | *whistled a tune to the baby* | V + NP + PP | HIGH (same sense, +structure) |
| `elab-ctrl` | *whistled softly in the dark* | V + adverbial | HIGH (replicates v1) |
| `polysemy-anchor` | *ran a marathon* → *ran a company* | — | LOW (calibration floor) |

## The decisive contrast

**ISOLATION gap = mean(`transitive-ctrl`) − mean(`coerced-way`).** Both arms add argument structure,
so a **positive** isolation gap means the relatedness drop is **SENSE-specific**, not a surface
artifact — settling I1. The **surface effect = mean(`elab-ctrl`) − mean(`transitive-ctrl`)** measures
whether merely adding a *conventional* object lowers relatedness (≈0 expected). Pre-committed ordering:
`elab-ctrl` ≥ `transitive-ctrl` ≥ `coerced-way` ≥ `polysemy-anchor`. Report-the-number; no pass bar.

## Scope limit

v2 covers the **way-construction** only — the construction whose verbs (sound/manner-of-action:
*whistle, sing, hum, dance, talk, fight, write, read*) have a clean bare + conventional-transitive +
coercion paradigm. The v1 **caused-motion** verbs (*sneeze, cough*…) are intransitive with **no**
conventional transitive, so their surface confound is not cleanly controllable within-verb; v2 does
not resolve I1 for caused-motion. Stated in the result.

## Instrument / discipline

Reuses the DWUG-validated lexical-v1 relatedness instrument verbatim (durel 1–4 + cont 0–100, temp 0,
3-family panel). 28 own-constructed items (8 verbs × 3 arms + 4 polysemy anchors), frozen + committed
(sha256) before any model call. Internal-contrast-only (`anchor: internal-contrast-only`): own
sentences, no human gold; the *instrument* is human-validated but these items are the project's own.
≥1 independent pre-run critic + ≥1 post-run number-verifier. Run record:
[`experiments/runs/2026-05-31-coercion-sense-modulation-probe-v2/`](../runs/2026-05-31-coercion-sense-modulation-probe-v2/README.md).
