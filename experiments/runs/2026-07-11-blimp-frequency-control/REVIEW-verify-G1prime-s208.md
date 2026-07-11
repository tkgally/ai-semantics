# G1′ verification record — F(p) reproduction + zero-latitude certification (s208, covariate arm)

Fresh independent verifier (spec-only reproduction; did NOT author build_freq.py). Scratch:
`verify_scratch/verify_freq.py`. No frozen artifact edited. Run BEFORE F(p) touched the real C4 /
paradigm→H mapping.

## TASK A — independent reproduction on a synthetic fixture: PASS
Reimplemented the PREREG §F recipe from the spec alone; ran both the independent impl and build_freq.py's
own tokenize/content_ngrams/score/f_of_paradigm + count_in_c4 counting on a 20-sentence synthetic corpus
+ 3 synthetic paradigms (bigrams, trigrams, stopword filtering, zero-content drops, present-vs-absent
n-grams). F_primary / F_sensitivity / drop-counts IDENTICAL across paradigms; consecutive-token counts
identical (hand-audited spot counts: chase-mice=5, cats-chase=3, mice-mice=2, mice-mice-mice=1,
small-small=3, cats-chase-mice=3, absent purple-elephant=0). **max abs difference 2.22e-16** (< 1e-9 bar).

## TASK B — zero-post-freeze-latitude: CERTIFIED
Every free choice (n-gram order; STOPWORDS membership incl. contraction fragments s/t/re/ve/ll/d/m; log1p;
good-sentence-only / 40 paradigms / 30 pairs; drop policy; within-sentence duplicate handling; C4 shards +
volume floor; rank-tie averaging; BOOT=5000/SEED=20260711/95% CI; bands CORR_LOW=0.20/CORR_HIGH=0.70/
SURVIVE_MAJ=2/PARTIAL_FLOOR=0.30-non-binding/direction=+; corr(F,H)-decided-first; NC1 scramble-H / NC2
scramble-F; G7 audit metrics + predicted signs) is a hard-coded constant / fixed formula in the committed
code, matched in PREREG, fixed before F(p) is computed and before F(p) meets the paradigm→H mapping. None
resolvable after any accuracy/H value is seen. build_freq.py reads only items.json good sentences + C4 —
never human_agreement or results.json, so F(p) is computed blind. Note (not a defect): BIGRAM_MIN/MAX are
unused dead constants; §F.4 "every adjacent-token bigram/trigram" = the positional keep-duplicates reading
the code + the independent impl both take (no post-data latitude either way).

## TASK C — reuse-boundary (G1′): CONFIRMED
build_freq.py reuses from build_cooc_c4.py ONLY the C4 streaming adapter (stream_sentences) + tokenizer
regex (_nonword), import-pinned by runtime asserts on _nonword.pattern / _sent.pattern / NUM_SHARDS /
C4_BASE (all passed on import). build_cooc_c4.py has NO consecutive-token n-gram frequency counter (only
unigram df, cue co-occurrence, Hearst-window participation, the signed-G² kernel — which is NOT imported).
count_in_c4 / content_ngrams / score / f_of_paradigm are genuinely new code with real DoF, consistent with
G8 capping this arm at robustness/corroboration.

## Defects before the real run: NONE — cleared to run F(p) on real C4.
