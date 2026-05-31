---
type: result
id: coercion-sense-modulation-v1
title: Coercion as lexical sense modulation v1 — the lexicon–grammar bridge — constructional coercion registers as a partial verb-sense shift in the DWUG-style relatedness instrument (control ≥ coerced ≥ polysemy, all 3 models), with a surface-structure confound it cannot rule out
meaning-senses:
  - constructional
  - referential
  - inferential
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-05-30
updated: 2026-05-30
links:
  - rel: supports
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
  - rel: depends-on
    target: result/caused-motion-near-miss-v2c
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: open-question/instrument-sensitivity-constructional-inference
---

# Result: coercion as lexical sense modulation v1 (the lexicon–grammar bridge)

**One-line:** reusing the **lexical** sense-relatedness instrument (validated against human DURel in [`result/lexical-sense-gradience-v1`](lexical-sense-gradience-v1.md)) on **grammatical** coercion stimuli, all three panel models rate a verb's meaning as **less related** between its bare use and its caused-motion / way-coerced use than between its bare use and a length-matched **non-coercing** elaboration — a positive "coercion sense-shift gap" in every model and both framings, with the coerced arm sitting **between** a same-sense control (high) and a genuine sense-shift `polysemy-anchor` (low). So **constructional coercion registers, partially, as a lexical sense shift** — the place the two wedges touch ([`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md)). **Caveat (decisive for the claim):** the design cannot separate this from the coerced sentences' added argument structure — see Caveats.

Run record: [`experiments/runs/2026-05-30-coercion-sense-modulation-probe-v1/`](../../../experiments/runs/2026-05-30-coercion-sense-modulation-probe-v1/README.md). Design: [`design/coercion-as-sense-modulation-v1`](../../../experiments/designs/coercion-as-sense-modulation-v1.md). **Internal-contrast-only** (`anchor: internal-contrast-only`; [`decisions/resolved/conflicting-cue-human-anchor`](../../decisions/resolved/conflicting-cue-human-anchor.md)). Cost **$0.249 billed**.

## What was tested

[`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md) argues coercion is where the lexical and grammatical grains are the *same event*: the caused-motion construction making *sneeze* contribute causation-of-motion **is** a grammar-induced shift in the verb's sense. This probe tests the join directly, with the instrument the lexical probe already built: present a target **verb** (marked «») in two sentences and ask the panel how related its meaning is (4-point DURel + 0–100), where sentence 1 is a bare use and sentence 2 is one of:

- `coerced-cm` — a caused-motion coercion (*she «sneezed» the napkin off the table*);
- `coerced-way` — a way-construction coercion (*she «whistled» her way down the hall*);
- `control-elab` — a length-matched **non-coercing** elaboration (*she «sneezed» twice during the lecture*) [high anchor];
- `polysemy-anchor` — a genuine lexical sense shift (*«ran» a marathon* → *«ran» a company*) [low calibration anchor].

30 own constructed items (6 cm + 6 way verbs × {coerced, control} + 6 polysemy anchors), frozen pre-run (sha256 `fda172ab707b6a73`); a pre-run critic's BLOCKER (a noun-pair anchor) was fixed + re-frozen before any model call. Reading rule (report-the-rate, internal-contrast): the coercion gap = mean(`control-elab`) − mean(`coerced`); positive ⇒ the model registers the coercion as a sense shift; `polysemy-anchor` must read low for a null to be interpretable. No threshold tuned post-run.

## Result (independently re-verified from raw JSON — CLEAN)

Mean relatedness per arm (durel 1–4 / cont 0–100):

| model | framing | control-elab | coerced-cm | coerced-way | polysemy-anchor | gap (control − coerced) |
|---|---|---|---|---|---|---|
| claude-sonnet-4.6 | durel | 3.75 | 2.67 | 3.00 | 1.67 | **+0.92** |
| claude-sonnet-4.6 | cont | 91.2 | 57.8 | 61.7 | 15.8 | **+31.4** |
| gpt-5.4-mini | durel | 3.83 | 2.67 | 3.50 | 1.33 | **+0.75** |
| gpt-5.4-mini | cont | 96.8 | 64.8 | 87.8 | 18.7 | **+20.5** |
| gemini-3.5-flash | durel | 3.75 | 3.00 | 3.50 | 1.67 | **+0.50** |
| gemini-3.5-flash | cont | 96.7 | 86.7 | 90.0 | 15.0 | **+8.3** |

**Readings:**

1. **Coercion registers as a partial sense shift — the bridge bet is supported (with the caveat below).** The three-way ordering **control-elab ≥ coerced ≥ polysemy-anchor holds in all 6 cells**; the coercion gap is **positive for every model and framing** (within-verb 8–11 of 12). The calibration worked: same-sense controls read near-ceiling (91–97 cont), genuine sense shifts read low (15–19 cont), and the coerced verbs land **between** — a *milder* sense shift than a polysemy/homonymy switch, but a real, consistent downward move. The two wedges genuinely touch: a grammatical manipulation shows up in the lexical instrument.
2. **Construction- and model-structure.** Caused-motion registers as a **bigger** sense shift than the way-construction for every model (cm gap > way gap); the metaphorical way items (`smile`/`joke`/`bluff` *…way into/out of…*) are the mildest. **gemini shows the smallest coercion gap** (cont 8.3 — it rates coerced uses as still ~90 related) despite being the **strongest** pure sense-gradience tracker (lexical v1 ρ=0.83); **claude is the most coercion-sensitive** (gap 31.4). So sensitivity to *constructional* sense modulation does **not** track raw lexical-gradience strength — a model can be an excellent graded-sense rater yet treat a coerced verb as "still basically the same word."
3. **Instrument echo.** As on every prior probe, the ordinal (durel) and continuous (cont) framings agree in direction but differ in resolution (gpt's way gap is tiny on durel, larger on cont) — the standing instrument-sensitivity caution ([`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md)).

## Caveats (lead with these — the first is decisive)

- **Surface-vs-sense confound (inherent; the pre-run critic's I1).** The coerced sentence-2 always carries **added object+path argument structure** that the `control-elab` arm lacks — that is what coercion *is*. So the positive gap **cannot by itself separate "the model registers a SENSE shift" from "the model rates any added transitive/path structure as less verb-related."** This result therefore makes only the **internal-contrast** claim (coerced rated less verb-related than a matched elaboration) and **does not** establish that the model represents coercion as lexical sense modulation in a human-validated way. The `polysemy-anchor` arm shows pure sense shift *can* drive low ratings (no added structure, reads lowest), but it does not control the coerced arm's surface confound. The clean follow-up (v2) is a **non-coercing transitive control** of the same verb (added object, no coercion) — deferred.
- **No human gold.** Constructed items; no in-repo human relatedness rating for them, so no human-comparison claim (the *instrument* is DWUG-validated, the *items* are the project's own). Internal-contrast-only, anchor pending.
- **Small N, single run, text-only.** 12 coerced verbs (6 cm / 6 way), 6 controls-paired, 6 anchors; one temp-0 pass per model. Read the pattern (positive gap, three-way ordering, cm>way, gemini smallest), not the exact values. `huff`-the-wrapper is the most marginal coercion; the polysemy floor mixes homonymy (`bank`/`charge`) and polysemy (`run`/`set`), so it is high-variance.

## Where it sits

- **Supports** [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md): the bridge probe it proposed ran and found the predicted direction (coercion ⇒ lower lexical relatedness), partially and with the surface caveat — the first *empirical* link between the project's lexical and grammatical axes, complementing the *theoretical* unification.
- **Refines** [`result/caused-motion-near-miss-v2c`](caused-motion-near-miss-v2c.md): there the caused-motion construction's causation inference was shown genuinely construction-keyed; here that same construction's effect is detectable as a verb-sense shift — caused-motion is again the stronger of the add-direction coercions (cm gap > way gap).
- Adds a lexical-side datum to [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md) and a model-ordering datum the continuum theory flagged to watch (strongest lexical tracker ≠ most coercion-sensitive).
