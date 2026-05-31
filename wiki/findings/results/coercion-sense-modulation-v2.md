---
type: result
id: coercion-sense-modulation-v2
title: The non-coercing transitive control for the lexicon–grammar bridge — a small, fragile, fine-scale-only sense-specific residual survives controlling for added argument structure (v1 partially de-confounded, not pure surface, not strongly sense either)
meaning-senses:
  - constructional
  - referential.sense
  - distributional
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-05-31
updated: 2026-05-31
links:
  - rel: refines
    target: result/coercion-sense-modulation-v1
  - rel: supports
    target: theory/lexicon-grammar-continuum
  - rel: depends-on
    target: concept/coercion
  - rel: depends-on
    target: result/lexical-sense-gradience-v1
---

# Result: the non-coercing transitive control — v1's coercion-as-sense-shift is partially de-confounded

> **Status: proposed (2026-05-31).** Internal-contrast-only (`anchor: internal-contrast-only`; own
> constructed stimuli, no human gold for these pairs; the *instrument* is the DWUG-validated
> lexical-v1 relatedness rating). Design [`design/coercion-as-sense-modulation-v2`](../../../experiments/designs/coercion-as-sense-modulation-v2.md);
> run record + freeze hash [`experiments/runs/2026-05-31-coercion-sense-modulation-probe-v2/`](../../../experiments/runs/2026-05-31-coercion-sense-modulation-probe-v2/README.md).
> **168 calls, $0.220 billed, 0 NA.** Independent pre-run critic (no blockers; one stimulus fix
> applied + re-frozen) + independent post-run number-verifier (every figure reproduced exactly; the
> one positive stress-tested to fragility).

## The one-line finding

The [`result/coercion-sense-modulation-v1`](coercion-sense-modulation-v1.md) effect — the panel rates a
verb's sense as *less related* between its bare use and a constructionally-coerced (way-construction)
use — **partially survives** a structure-matched non-coercing transitive control, but only **weakly**:
a sense-specific component (the **ISOLATION gap** = transitive-ctrl − coerced-way) is **positive on the
fine 0–100 scale for all three models** (claude +13.6, gpt +6.1, gemini +1.9) yet **≈ 0 on the coarse
4-point scale** (0.0 / −0.1 / +0.4), is **fragile** (claude's +13.6 falls to +8.4 if a single verb
*shout* is dropped; only 4/8 verbs are positive, *hum* runs the wrong way), and is accompanied by a
**real surface component** (adding a *conventional* object also lowers relatedness ~6–8 cont points).
So v1's gap was **a mix**: a small genuine sense-shift signal (strongest for claude) **plus** a real
added-argument-structure effect — it is **not a pure surface artifact**, but neither does v2 establish a
strong sense-specific reading. For gemini the coercion drop is **mostly surface** (isolation +1.9 vs
surface +5.6).

## Why v2 — the confound it targets

v1's pre-run critic flagged inherent confound **I1**: the coerced arm (*whistled her way down the hall*)
always adds object+path argument structure the intransitive `control-elab` arm (*whistled softly*) lacks,
so v1's gap could not separate "the model registers a **sense** shift" from "the model rates **any** added
argument structure as less verb-related." v2 adds a **structure-matched conventional-transitive** arm
(*whistled a tune to the baby* — V + NP + PP, a lexically conventional same-sense use) alongside the
coerced way-arm (V + POSS *way* + PP). Both add comparable argument structure; only the coerced arm
coerces a new sense. The decisive contrast is the **ISOLATION gap = mean(transitive-ctrl) −
mean(coerced-way)**: positive ⇒ the drop is sense-specific.

## Numbers (every figure independently reproduced from raw)

8 way-verbs (*whistle, sing, hum, dance, shout, fight, write, read*) × {coerced-way, transitive-ctrl,
elab-ctrl} + 4 polysemy anchors. Panel claude (A) / gpt-5.4-mini (B) / gemini (C).

| model · framing | elab-ctrl | transitive-ctrl | coerced-way | poly-anchor | **ISOLATION (trans−coerced)** | surface (elab−trans) | coercion_gap (elab−coerced) | within-verb iso sign |
|---|---|---|---|---|---|---|---|---|
| claude · durel | 3.5 | 3.0 | 3.0 | 2.0 | **0.0** | 0.5 | 0.5 | 0/8 |
| claude · cont | 88.9 | 82.6 | 69.0 | 20.0 | **+13.6** | 6.3 | 19.9 | 4/8 |
| gpt · durel | 4.0 | 3.0 | 3.12 | 2.0 | **−0.1** | 1.0 | 0.9 | 2/8 |
| gpt · cont | 97.8 | 89.8 | 83.6 | 23.5 | **+6.1** | 8.0 | 14.1 | 3/8 |
| gemini · durel | 4.0 | 3.75 | 3.38 | 1.75 | **+0.4** | 0.25 | 0.6 | 4/8 |
| gemini · cont | 100.0 | 94.4 | 92.5 | 20.0 | **+1.9** | 5.6 | 7.5 | 3/8 |

The pre-committed ordering **elab ≥ transitive ≥ coerced ≥ poly** holds in 5/6 cells (gpt-durel has
transitive 3.0 ≈ coerced 3.12, a coarse-scale tie). The polysemy anchors read low (20–23.5 cont / 1.75–2.0
durel), so the instrument's low end is calibrated.

### How to read it

- **A sense-specific residual exists, on the fine scale, for all three models** (ISOLATION cont
  +13.6/+6.1/+1.9 > 0) — so v1's coercion drop is **not entirely** the added argument structure. The
  ordering **claude > gpt > gemini** matches v1's coercion-sensitivity ordering.
- **It is small and fine-scale-only.** On the 4-point DURel scale the isolation gap is ≈ 0 (transitive
  and coerced both round to ~3) — the sense-specific component is below the coarse instrument's
  resolution.
- **It is fragile / few-verb-driven** (post-run verifier). claude-cont's +13.6 is carried by *shout*
  (+50), *write* (+25), *fight* (+23), *sing* (+21); *dance/read/whistle* are flat and *hum* runs −10
  against. Drop *shout* → +8.4; drop *shout*+*write* → +5.7. Only 3–4 of 8 verbs carry it; gemini's +1.9
  is thinner still (built from *fight* +10, with *read* −5 against).
- **A real surface component is present too** (surface effect = elab − transitive = ~6–8 cont): adding a
  *conventional* object does lower relatedness somewhat. So part of v1's raw coercion gap (cont
  19.9/14.1/7.5) **was** surface — roughly, claude's drop is mostly sense (13.6 of 19.9), gpt's is about
  half-and-half (6.1 sense vs 8.0 surface), gemini's is **mostly surface** (1.9 sense vs 5.6 surface).

## Honest limits

- **Internal-contrast-only.** No human relatedness gold for these constructed pairs; the claim is a
  within-panel direction-of-effect, not a human comparison. (The instrument tracks human DURel per the
  lexical-v1 result, but these items are the project's own.)
- **Residual "POSS *way*" object-form asymmetry** (pre-run critic NIT). The coerced arm's object is always
  "her/his way" — a non-canonical/cognate object — while the transitive control uses a referential count
  NP. So the ISOLATION gap is "coercion + the way-object-form" vs a conventional transitive; v2 removes
  v1's *added-arguments-per-se* confound but **not** the way-object-form asymmetry. The residual could be
  the model reacting to the odd "way" object rather than to sense.
- **Way-construction only.** v2's clean within-verb control exists because sound/manner verbs have a
  conventional transitive. The v1 **caused-motion** verbs (*sneeze, cough*…) are intransitive with **no**
  conventional transitive, so their surface confound is **not** resolved here.
- **Fragile, small, fine-scale-only, n = 8 verbs / 3 models, single temp-0 run.** The sense-specific
  reading rests on a handful of verbs; a coarse instrument sees nothing.

## Relation to other findings

- **Refines** [`result/coercion-sense-modulation-v1`](coercion-sense-modulation-v1.md): v1's
  coercion-as-sense-shift is **partially de-confounded** — a small, fragile, fine-scale sense-specific
  residual survives the structure-matched control (so not pure surface), but a real surface component is
  also present and the sense-specific part is below resolution on the coarse scale and carried by few
  verbs. The v1 effect should be read as a **mix**, strongest-for-claude, essentially-surface-for-gemini.
- **Supports** (weakly, with the above caveats) [`theory/lexicon-grammar-continuum`](../theory/lexicon-grammar-continuum.md):
  constructional coercion does register *partly* as a lexical sense modulation in the relatedness
  instrument, so the two wedges still touch — but the contact is fainter than v1's raw gap implied once
  added structure is controlled.

Anchored: `internal-contrast-only`. `contingent-on: []`. Cost **$0.220 billed** (gemini-dominated as usual).
