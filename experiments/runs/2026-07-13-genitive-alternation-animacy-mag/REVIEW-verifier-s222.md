# Post-run recompute verification — genitive-animacy MAGNITUDE pooling (mag, s222)

Fresh, independent agent; wrote its own analysis from scratch (numpy, bootstrap seed `99991117`,
100k resamples), did not touch `analyze_merged.py`.

**VERDICT: REPRODUCED-WITH-NOTES** — all point estimates, fractions, CIs, row counts, billed cost,
and possessor disjointness reproduce; 0 material discrepancies.

## Structural / integrity
- mag raw: probe-{claude,gemini,gpt}.jsonl each **216 rows, 0 nulls**, all `arm=="typical"`. ✓
- mag-arm billed over 648 rows: **$0.84203** vs claimed $0.84203 — exact. ✓
- Possessor-lemma disjointness (read all three stimuli.json): mag's 108 typical possessors have
  **0 overlap** with the s218∪rep2 union, at the all-possessor level and within each animacy level. ✓
  *(Aside: the prior s218∪rep2 union is 71/72/71 per level — s218 and rep2 share one lemma each at
  the animate and inanimate levels, i.e. 214 unique prior lemmas not 216; irrelevant to the mag
  disjointness, which is 0-overlap against the whole union.)*

## Pooled-108 (claimed vs recomputed)
- claude 0.1452 [0.1237,0.1672] 102/108 → **0.1452 [0.1240,0.1670] 102/108** ✓
- gemini 0.1688 [0.1404,0.1976] 93/108 → **0.1688 [0.1402,0.1978] 93/108** ✓
- gpt 0.1392 [0.1104,0.1695] 88/108 → **0.1392 [0.1098,0.1690] 88/108** ✓

## New-36 blind (claimed vs recomputed)
- claude 0.1554 [0.1199,0.1937] 35/36 → **0.1554 [0.1193,0.1950] 35/36, sign-p 5.4e-10** ✓
- gemini 0.1750 [0.1181,0.2347] 30/36 p 3.5e-5 → **0.1750 [0.1181,0.2340] 30/36 p 3.48e-5** ✓
- gpt 0.1781 [0.1174,0.2420] 28/36 p 6.0e-4 → **0.1781 [0.1174,0.2418] 28/36 p 0.000597** ✓

CI endpoints wiggle in the 4th decimal from the different seed — expected, immaterial.

## Note (convention, not error)
The project's sign-p uses **n = 36** (all frames as binomial trials, ties counted); the verifier
reproduced that convention to an exact match. A tie-excluding convention (gemini n=35, gpt n=33)
yields smaller but qualitatively identical p-values — all highly significant either way.
