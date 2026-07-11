# REVIEW — G5-plus anti-cheat build verification (s210 BLiMP content-word-swap arm)

*Independent fresh-agent verifier. Reproduce the frozen swap-build from `PREREG.md` + `build_swap.py`, audit
grammaticality/faithfulness of the committed `items_swap.json`, confirm anti-cheat posture. No committed repo
file edited; all work in `/tmp/g5verify`.*

## REPRODUCED: YES (byte-identical)

Copied the committed `items_swap.json` + `selection.json` aside, re-ran `build_swap.py` in an isolated dir
that **forced a fresh fetch** of the sha256-pinned SUBTLEX-2012 xlsx + all BLiMP paradigm files (the pins
held). Freshly built outputs are **byte-for-byte identical** to the committed instrument: `items_swap.json`
sha256 `faf64086…af310b3`, `selection.json` sha256 `9b5c5708…eb0ef498`. Same pool sizes (names 4835 /
nouns_sg 20400 / adjs 7870), same 15 swappability scores, same selected 6 paradigms, same 600 swapped pairs
+ substitutions. The build's sole degree of freedom is reproduced exactly.

## Mechanical re-validation (all 600 pairs, independently recomputed): CLEAN

a/an-before-vowel introduced: 0; swapped good == swapped bad: 0; locus token-position count mismatch
(orig vs swap): 0. dn-noun carve-out verified: good_swap/bad_swap differ only by the head-noun number, each
member keeping its own sg/pl feature — the determiner-noun contrast faithfully preserved.

## Grammaticality / faithfulness audit

Sampled 54 pairs (9/paradigm, seed 424242) + full-set programmatic scans. 48/54 clean; the flagged 6 fall
into two patterns, quantified across all 600:

- **Defect 1 — main-verb swapped as a noun (~11 pairs, both shallow `det_noun` paradigms only).** nltk
  mis-tags a sentence-medial 3sg verb as a noun and the NP_LEFT rule admits it (e.g. "Becky visits this
  customer" → "Becky **onions** this toe"). **0 in the three deep paradigms; 0 in sv.**
- **Defect 2 — partitive-subject agreement flip (4 pairs, `regular_plural_subject_verb_agreement_1` only).**
  swapping the head of "a lot of X" (notional plural) yields a singular head ("A **girl** of terms
  notice…") that flips which member is grammatical (pairs 477, 407, 608, 779; 4/100).
- Register hygiene: the JUNK filter misses some coarse terms (cosmetic; shared content cancels).

**Decisive property — none is a blocker:** every off-locus swap is applied **identically to both members**
(0/23 flagged swaps failed to mirror into `bad_swap`), so it cancels in the 2AFC; and where Defect 2 flips
polarity it pushes Δacc **negative** → biases toward SWAP-DROPS/INCONCLUSIVE, **never** toward the preferred
SWAP-STABLE. There is no inflationary defect that could manufacture a false STABLE. Both defects are
concentrated in the **shallow** stratum (near ceiling, does not carry the test); the deep-3 audit clean
(nouns/names swapped; `not`/`only`/`ever`/verbs held fixed).

## Anti-cheat posture: CONFIRMED

`probe.py` runs BOTH conditions fresh, both orders — swapped accuracies genuinely unknown at freeze.
`analyze_swap.py` thresholds match PREREG (`MARGIN=0.05`, `COV_FLOOR=0.50`, `≥2/3`, `BOOT=5000`,
`SEED=20260711`; within_margin = CI ⊂ [−0.05,+0.05]; drops = CI ≤ −0.05 excluding 0; instrument-failure
guard). Frequency match (±0.10 Lg10WF) enforced in `pick()` and reproduced byte-identically.

## VERDICT: CERTIFY-WITH-CAVEATS

Proceed to the probe. The instrument's only DoF (the build) reproduces byte-identically from the pinned
inputs; the anti-cheat design is sound; mechanical re-validation is clean across all 600 pairs. Two genuine
grammaticality defects (~11 verb-as-noun in shallow det_noun; 4 partitive flips in sv_1, ~4%) are confined to
the near-ceiling shallow stratum, cancel in the 2AFC or bias conservatively against the promotion, and cannot
fabricate a SWAP-STABLE reading.

**Caveats to carry into the reading:** (1) if the shallow stratum lands DROPS/INCONCLUSIVE, discount it —
~15% combined contamination in det_noun/sv_1 injects downward Δacc noise there; the deep-3 carry the
load-bearing test and audit clean. (2) Report the verb-as-noun leak (NP_LEFT admitting a NN/NNP left-context
lets a tagger-misread finite verb be swapped) and the sv partitive-flip as build limitations. (3) Register
leaks are cosmetic (shared content cancels).
