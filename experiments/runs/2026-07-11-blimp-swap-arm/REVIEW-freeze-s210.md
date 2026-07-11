# REVIEW-freeze-s210 — BLiMP R1 content-word-swap arm (independent pre-run freeze critic)

*Independent fresh-agent pre-run freeze critic (GO/NO-GO verdict authority; PROTOCOL §A3). QA companion: the
non-Anthropic freeze vote (`VOTE-freeze-s210.json`, `gpt-5.4-mini`, NO-GO — overridden here on reasoned
grounds, its audit condition adopted).*

**VERDICT: GO-WITH-CONDITIONS** — the frozen instrument faithfully realizes Q1-A / Q2-B / Q3-A +
noun-only-swap + G-coverage + G-margin-justification; its defects are real but *conservative* (they bias
against, not toward, the program's preferred SWAP-STABLE), so the freeze holds under reporting/interpretation
conditions. I diverge from the companion non-Anthropic freeze vote's NO-GO, on reasoned grounds, while
adopting its audit condition.

## Faithfulness
Strong. Analysis constants match PREREG exactly (`MARGIN=0.05`, `COV_FLOOR=0.50`, `POSLOCK_FAIL=0.50`,
`ANS1_EXTREME=0.40`, `BOOT=5000`, `SEED=20260711`); the verdict map is realized as coded (SWAP-STABLE = Δ̄ CI
⊂ [−0.05,+0.05] on both strata ≥2/3; DROPS ≥2/3; else INCONCLUSIVE). Selection is genuinely
accuracy/human-blind and the top-3-per-stratum picks reproduce from `selection.json`. Both conditions re-run
fresh in `probe.py` — the unknown-at-freeze anti-cheat advantage is intact. det-noun carve-out, sv
subject-name guard, a/an renormalization, `-ing`/irregular drops all implemented as described and verified on
sampled items; coverage gating real (all six clear 0.70–0.985; a sub-floor paradigm's pairs are excluded).
Three gaps to close by condition: (i) the **G-freq achieved per-word Lg10WF gap distribution** is never
computed/reported (PREREG says "reported"); (ii) the mandatory **G-freq-pretraining C4 cross-check** is
behind an optional `--c4` flag and must be run + committed; (iii) the coded SWAP-DROPS test (`hi ≤ −0.05`,
the *whole* CI at/below −0.05) is stricter than the PREREG prose ("Δ̄≤−0.05 with CI excluding 0") — conservative
and symmetric with STABLE, but the result page must describe the rule that actually ran.

## Grammaticality risk
Two defect classes slip past the mechanical re-validation, both confirmed by scanning all 600 pairs:
(1) **pseudo-partitive head swaps** — "a lot of X" has "lot" swapped, breaking notional plural SV agreement
(~25/600, shallow-concentrated); (2) **relative-clause/infinitival verbs mis-tagged as nouns** — the NP_LEFT
guard admits a "noun" preceded by another noun, so a verb after a noun subject can be swapped (one clear case
in `only_npi_scope`). Both inject distortions **identical across the good/bad members** (they cancel in
expectation for Δacc) and both *depress* swap accuracy or add noise — pushing toward SWAP-DROPS/INCONCLUSIVE,
never toward the preferred STABLE. They are validity risks for a *negative* reading (a spurious DROPS could
reflect broken items), not failures that manufacture the desired result. The det-noun carve-out's
plural-attestation check correctly filters mass nouns out of the number contrast.

## Anti-cheat
Sound, and I judge the companion NO-GO's steering concern **not materially applicable**: its feared mechanism
(swappability selection + coverage thresholding steer the outcome) requires visibility of Δacc, but
accuracies are unknown at freeze, selection is accuracy/human-blind, and all six paradigms clear the coverage
floor so **no paradigm is dropped** this run (the threshold is inert). No-op swaps (substitute == original)
are only 1.7% of subs. Bands are symmetric (STABLE and DROPS pre-registered identically); the ±0.05 margin is
un-tunable (fixed against s205 `DEPTH_MARGIN` before any swap accuracy existed). The build's defect vector
points *away* from the flagship claim — the strongest possible anti-cheat posture.

## Scope honesty
Correctly bounded: candidacy is "not exact-string/lexical-item memorization or the surface freq proxy," never
construction-frequency/template-difficulty (G3′), never grammatical competence (contamination upper bound
persists); perturbation honestly recorded as noun/name/adjective-only (verbs/adverbs fixed); deep-pole cost
(scope-deep covered, island-deep excluded) travels; SWAP-STABLE earns bounded candidacy only — `analyze_swap.py`
never emits a claim. The `predictions.md` row is registered and symmetric.

## Power
Adequate — better than a naive read suggests. Simulating the real s205 deep-paradigm accuracy mixture
(`sentential_negation_npi_scope` ≈0.93/0.93/0.97, `superlative_quantifiers_1` ≈0.93/0.80/1.0, `only_npi_scope`
≈0.60/0.82/0.47) under true equivalence gives deep-stratum CI half-widths ≈ 0.039/0.040/0.034 (inside ±0.05
with slack); shallow ~0.012. Residual risk: `only_npi_scope` is erratic (C at 0.47), and a large swap-specific
degradation there could widen/shift the deep CI into INCONCLUSIVE — the pre-registered conservative
under-power landing.

## Conditions (honor before/during the run; NO rebuild)
1. **Do not rebuild** to fix the two grammaticality defects — re-touching the instrument after seeing sample
   items forfeits the unknown-at-freeze anti-cheat advantage; the defects are conservative, handle by
   reporting (aligns with the ratified Q3-A "report, don't silently fix").
2. **Run the mandatory C4 diagnostic** (`analyze_swap.py --c4`) and commit `c4_pretraining_diag.json`; a
   material orig−swap C4 log-freq gap is a load-bearing caveat on any SWAP-DROPS.
3. **Report the G-freq achieved gap** (per-word |Lg10WF(orig)−Lg10WF(sub)| distribution).
4. **Deep-paradigm spot-audit**: quantify + report, per paradigm, (a) RC/infinitival verbs mis-tagged and
   (b) pseudo-partitive head swaps, as a stated limitation.
5. **DROPS-contingency**: if SWAP-DROPS or a deep-stratum drop, reckon the audited anomaly rate + the C4 gap
   as alternative explanations *before* reading the negative as exact-string memorization.
6. **State the operative DROPS rule as coded** (whole CI ≤ −0.05); report achieved per-stratum CI
   half-widths; classify any INCONCLUSIVE as under-power vs instability.
7. **Housekeeping**: update the stale "not fetched" rows in `resource/subtlex-us-frequency` for the 2012 PoS
   file, now fetched.
