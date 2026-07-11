# Pre-run design review — BLiMP R1 content-word-swap arm (s209)

**Design under review:** [`design/blimp-swap-arm-v1`](../../designs/blimp-swap-arm-v1.md) +
[`decisions/open/blimp-swap-arm-design`](../../../wiki/decisions/open/blimp-swap-arm-design.md).
**Two-part pre-run critique (PROTOCOL §2/§A3):** a fresh-agent adversarial pre-run design critic
(harness model, **verdict authority**, independent of the s209 design author) + one non-Anthropic
decorrelation vote (`panel.B` = `gpt-5.4-mini`, QA input; [`VOTE-s209.json`](VOTE-s209.json),
$0.004603). **This session opened the decision (s209); ratification is s210+.** The blockers below are
**discharged in-design this session** (the s207 pattern); the decision stays open with the strengthened
gates + freeze conditions.

## Verdicts

- **Fresh-agent critic (verdict authority): GO-WITH-CONDITIONS.** Concurs **Q1-A / Q2-A / Q3-A** as the
  strategic frame; provenance + anchor discipline **CLEAN** (every cited number checked against the in-repo
  pages at stated strength; `anchor: resource/blimp` correctly human-comparison, never internal-contrast);
  anti-cheat essentially clean (two residual DoFs pointing in opposite directions, both tightened below).
  **Two BLOCKERS + one condition + one added freeze diagnostic**, all discharged in-design.
- **Non-Anthropic vote: GO-WITH-CONDITIONS**, converging **Q1-A / Q2-A / Q3-A**. Biggest risk =
  selectional/grammaticality drift after swapping → a pre-registered selectional-sanity exclusion +
  exact-inflected-form attestation; bound the promotion candidacy to "not explained by exact-string
  memorization or the tested surface frequency proxy" (residual construction/template familiarity);
  confirm the 3+3 split + band are frozen ex ante.

## BLOCKER-1 — POS-preservation ≠ grammaticality-preservation in gap-bearing (deep) + irregular (shallow) paradigms — DISCHARGED IN-DESIGN

The critic showed the design's "grammaticality preserved by construction" claim is **false** for
`filler_gap_dependency` / `island_effects` (the main verb's **subcategorization frame** licenses the gap:
swapping a transitive verb for an intransitive one destroys the filler-gap dependency — POS is too coarse a
grain), and for `irregular_*` agreement paradigms (the contrast turns on **irregular** plural morphology
man/men; swapping to a regular-plural noun silently converts the paradigm to an easier regular test → a
spurious Δacc that is neither memorization nor noise). The Q3 mechanical checks cannot detect a valence
mismatch.

**Discharge (design amended):** adopt the critic's **option (b)** as the provisional default — restrict the
swappable set to **frame-safe paradigms**: deep-3 drawn from `npi_licensing` ∪ `quantifiers` (closed-class
licensor: negation / `only` / quantifier → content-swap is frame-safe), shallow-3 from the **regular**
`determiner_noun_agreement` + `regular_plural_subject_verb_agreement` paradigms; **exclude**
`island_effects` / `filler_gap_dependency` and every `irregular_*` paradigm from the swappable set,
**reporting the deep-pole generality cost** (the swap arm covers the scope-deep pole, not the island-deep
pole). The more-general **option (a)** (subcategorization-tagged verb lexicon + same-frame substitution +
irregular↔irregular guard) is recorded as the alternative the ratifier may prefer. A **frame-preservation
admission check** (new **G-frame**) is added to Q3 regardless.

## BLOCKER-2 — the inherited SWAP-STABLE metric is an un-ratified "e.g.", noise-biased toward INCONCLUSIVE, and under-powered at N=30 — DISCHARGED IN-DESIGN

The parent design writes the band as **"e.g. |Δacc| ≤ 0.05"** — illustrative, not a pinned yardstick — so
"inherited, not re-opened" over-stated what s208 ratified: the **aggregation + band are a live
operationalization DoF** to pin in PREREG this line. And `mean|Δ_paradigm|` is **upward-biased under
sampling noise**: at 30 items/paradigm the per-paradigm Δ SE ≈ 0.065, so under a *true* Δ=0 the expected
`mean|Δ|` ≈ 0.05 — right at the band, so a genuinely stable panel can land INCONCLUSIVE (or trip DROPS) from
noise alone.

**Discharge (design amended):** (a) pin the aggregation as a **per-model, per-stratum signed stratum-mean Δ
with a bootstrap CI**, and **SWAP-STABLE = a TOST-style equivalence** (the CI sits *within* ±0.05) on both
strata for ≥2/3; **SWAP-DROPS = signed stratum-mean Δ ≤ −0.05 with CI excluding 0** on ≥2/3; else
SWAP-INCONCLUSIVE — replacing the noise-biased mean-of-absolutes (new **G-metric**). (b) **Expand N** toward
the parent's ~100+/paradigm: default **≈100 fresh paired items/paradigm** so the per-paradigm Δ SE falls to
~0.03 and the equivalence test is meaningful. **Corrected cost arithmetic:** 6 × 100 × 2 conditions × 2
orders × 3 models = **7,200 calls ≈ $1.3–1.6** at the s205 economics (the critic's 15,840 double-counted) —
**still under the $2.50 prefer-split flag.** N is pinned in PREREG at freeze with the per-model per-stratum
Δ CI power stated (new **G-power** sharpening).

## CONDITION — lexicon-selection determinism — BOUND

Hand-curating + per-item hand-assigning substitutes is a DoF the G5-plus verifier-reproduction does not
audit (it reproduces the build from the frozen lexicon but not whether the lexicon was biased toward easy,
high-collocation substitutes). **Bound (new G-lexicon-determinism):** the per-position substitute is chosen
**deterministically (seeded) from the full eligible in-band, POS-and-frame-matched set**; the only human DoF
is **membership** (junk removal via a published stoplist rule), which the verifier + stoplist audit — not
per-item hand-assignment.

## ADDED FREEZE CONDITION — G-freq-pretraining — ADOPTED

SUBTLEX-US is a **human-facing** subtitle norm, not the models' web-scale pretraining distribution, so a
SUBTLEX-matched substitute can be materially rarer in pretraining — a Δacc could be a pretraining-frequency
drop in a matched-frequency costume, re-introducing the exact confound the covariate arm spent s208
controlling. **Adopt (new G-freq-pretraining):** at freeze, report the swap set's **C4 (pretraining-proxy)
log-frequency distribution against the originals'** (reuse the s208 C4 pipeline; streaming compute, no model
cost); a material difference is a load-bearing limitation on any SWAP-DROPS reading and travels into the
candidacy alongside G3′. This repurposes Q2-C from an optional sensitivity arm into a **mandatory
diagnostic**.

## Promotion-scope tightening (from both reviewers) — BOUND

The critic's ceiling note (shallow stratum at 0.98–0.99 → near-automatically within-band, so the **deep-3
carry the real test**) + the vote's "bounded candidacy" converge: SWAP-STABLE ∧ SURVIVES-COVARIATE earns
only a **bounded** promotion candidacy — explicitly "**not explained by exact-string / lexical-item
memorization or the tested surface frequency proxy**," **not** a construction-frequency-controlled or
template-difficulty-controlled reading. The candidacy carries this bound + both G3′ caveats into the later
claim review.

## Provenance + anchor: CLEAN. Anti-cheat: essentially clean (two offsetting residual DoFs, both tightened above).

## Net (s209): decision OPEN, ratifiable s210, with the strengthened gates (Q1-A frame-safe / Q2-A
deterministic / Q3-A + G-frame) and freeze conditions G5-plus, G3′-travels, G-freq, G-power (sharpened),
G-frame, G-metric, G-lexicon-determinism, G-freq-pretraining. Nothing frozen, nothing run. The only spend is
the one non-Anthropic vote ($0.004603).
