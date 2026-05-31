# Run record — coercion-as-sense-modulation bridge probe (v2): the non-coercing transitive control

**Date:** 2026-05-31 · **Design (frozen):** [`design/coercion-as-sense-modulation-v2`](../../designs/coercion-as-sense-modulation-v2.md) · **Refines:** [`result/coercion-sense-modulation-v1`](../../../wiki/findings/results/coercion-sense-modulation-v1.md) · **Instrument:** the lexical-v1 relatedness rating ([`result/lexical-sense-gradience-v1`](../../../wiki/findings/results/lexical-sense-gradience-v1.md)).

## What this settles

v1 found constructional coercion registers as a partial lexical sense shift, but its coerced arm added object+path structure the intransitive control lacked (pre-run critic **I1**) — so the gap couldn't separate *sense shift* from *added argument structure*. v2 adds a **structure-matched non-coercing transitive** arm (V + NP + PP, conventional sense) alongside the coerced way-arm (V + *way* + PP). Both add arguments; only coercion shifts sense. **Decisive contrast: ISOLATION gap = transitive-ctrl − coerced-way** (positive ⇒ sense-specific, not surface).

## FREEZE (before any model call)

- `items.csv` sha256[:16] **`93a83efd98ece009`** — 28 items: 8 verbs (whistle, sing, hum, dance, **shout**, fight, write, read) × {coerced-way, transitive-ctrl, elab-ctrl} + 4 polysemy anchors. Own constructed sentences (no corpus/licence). Build asserts the verb is marked «» in both sentences of every item. *(Pre-run critic S2 fix applied + re-frozen: replaced "talk"→"shout" — "talk nonsense" was a cognate/mass object, less structurally parallel; "shout a warning to the crowd" is a clean count-NP+PP conventional same-sense transitive. fight's transitive tightened "a duel"→"a fierce battle" for clearer same-sense. Both fixes were conservative — they had pushed the transitive arm down. Prior hash `fb69ae26a3cba74e`.)*

**Residual surface caveat (critic NIT, carried to the result):** the coerced-way arm's object is always "POSS way" (a non-canonical / cognate object) while the transitive-ctrl object is a referential count NP. So a positive ISOLATION gap is "coercion + the way-object-form" vs a conventional transitive — an internal-contrast, not pure-sense-isolated-from-every-surface-feature. v2 removes the v1 confound (added arguments per se) but not the "way"-object-form asymmetry.

## Arms & reading rule (fixed pre-run)

`coerced-way` (LOW) / `transitive-ctrl` (HIGH, +structure same sense) / `elab-ctrl` (HIGH, replicates v1) / `polysemy-anchor` (LOW floor). Report-the-number; ISOLATION gap is the decisive figure; surface effect = elab − transitive (≈0 expected); pre-committed ordering elab ≥ transitive ≥ coerced ≥ poly. Internal-contrast-only (`anchor: internal-contrast-only`; no human gold for these constructed pairs).

## Scope limit

Way-construction only (its verbs have a clean conventional-transitive control). Caused-motion verbs (v1) are intransitive with no conventional transitive → their surface confound stays uncontrolled (not resolved by v2).

## Protocol status

- [x] Build + freeze (sha256 above) before any model call
- [ ] Independent pre-run critic (stimuli: are transitive-ctrl uses truly same-sense conventional? coerced uses truly coercion?)
- [ ] Probe (28 × 2 framings × 3 models = 168 calls; ~$0.2 by v1)
- [ ] Independent post-run number-verifier
- [ ] Result page

## Files

`build_items.py` (emits+freezes items.csv) · `probe.py` (durel+cont × 3 models; imports `experiments/lib/openrouter.py`) · `analyze.py` (per-arm means + isolation/coercion/surface gaps + within-verb sign + ordering → raw/results.json).
