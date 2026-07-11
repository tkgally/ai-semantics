# Post-run verification record — covariate arm (s208)

Fresh independent recomputation from frozen inputs (freq.json, s205 results.json + items.json). Own
Spearman + rank + partial-correlation code (verify_scratch2/verify.py), own bootstrap seed (424242,
BOOT=5000). analyze_partial.py NOT imported.

## Figure-by-figure — overall REPRODUCED
| Figure | Recomputed | Reported | Verdict |
|--------|-----------|----------|---------|
| corr(F,H) | 0.2595 | 0.2595 | REPRODUCED |
| corr(F,H) bi-only | 0.2537 | 0.2537 | REPRODUCED |
| raw ρ_prof A/B/C | 0.6063/0.5432/0.6278 | = s205 rho_prof | REPRODUCED |
| partial ρ·F A/B/C | 0.5717/0.5104/0.6064 | 0.5717/0.5104/0.6064 | REPRODUCED |
| partial sens A/B/C | 0.5732/0.5086/0.6098 | same | REPRODUCED |
| boot CI A | (0.329,0.779) excl0 p+1.000 | (0.3085,0.774) excl0 | REPRODUCED (±0.03, sign+0-excl match) |
| boot CI B | (0.239,0.723) excl0 p+0.9994 | (0.2253,0.7182) excl0 | REPRODUCED |
| boot CI C | (0.344,0.792) excl0 p+0.9996 | (0.3288,0.7939) excl0 | REPRODUCED |
| G7 F vs unigram-logfreq | +0.4812 | +0.4812 | REPRODUCED (predicted +) |
| G7 F vs word-length | −0.3525 | −0.3525 | REPRODUCED (predicted −) |
| total dropped | 180 | 180 | REPRODUCED |
| max per-paradigm drop | 25 (left_branch_island_echo_question) | 25 | REPRODUCED |
| min retained | 5 (n=40 stands) | — | CONFIRMED |
| verdict | corr∈[0.20,0.70] interpretable; 3/3 CIs excl 0 → SURVIVES-COVARIATE | same | REPRODUCED |

All point estimates match to <1e-3 (to 1e-4 in fact); all three bootstrap CIs agree to within ±0.03 at
both endpoints and independently exclude 0 with positive sign on 3/3. Cross-check succeeded: recomputed raw
ρ_prof equals both results_partial.json.raw_rho and s205 rho_prof to 4 dp (accuracies + H loaded in correct
paradigm alignment).

## Robustness of SURVIVES-COVARIATE: robust, with one honest caveat
(1) Sentence drops (180 total, max 25/30 on function-word-heavy island paradigms; every paradigm retains
≥5, n=40 holds) make F(p) thinner/noisier on those paradigms — attenuating F toward noise, which removes
LESS shared variance and pushes the partial TOWARD raw ρ. So the drops bias the machinery TOWARD SURVIVES,
not away: the verdict is conservative-for-BREAKS and must NOT be over-read as proof the surface-lexical
confound is fully controlled on the thin-F paradigms. NC2 scramble-F (partial≈raw) corroborates the
covariate is doing little work, consistent with the modest corr(F,H) + drop-thinning. (2) corr(F,H)=0.26
sits low in the interpretable band, clear of the >0.70 over-control branch and above the <0.20 no-confound
branch — partialling neither strips shared depth structure nor is vacuous. raw→partial drop small
(0.035/0.033/0.021), exactly what a weakly-collinear surface proxy predicts.

Scope carried (PREREG §S/G8): robustness/corroboration against a C4 surface-lexical proxy only; controls
lexical/surface familiarity NOT construction frequency; does NOT satisfy C8's promotion gate — the Q1-C
swap arm remains outstanding. No figure discrepancy.
