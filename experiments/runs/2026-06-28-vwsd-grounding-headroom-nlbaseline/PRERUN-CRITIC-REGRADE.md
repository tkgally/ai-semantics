# Pre-run critic certification — VWSD NL-baseline RE-GRADE (valid category-match scorer)

**Critic:** fresh, independent agent (did NOT build the harness, run the re-grade, or ratify the
scorer). Per the frozen design's "Pre-run critic gate (binding)" and the resolved decision
[`vwsd-nlbaseline-recovery-scorer-validity`](../../../wiki/decisions/resolved/vwsd-nlbaseline-recovery-scorer-validity.md)
(ADOPT Q-A WITH MODIFICATIONS).
**Date:** 2026-06-28 (session 128). **Scope:** GO/NO-GO of the re-graded adequacy-audit distribution
against the FIXED band `[0.60, 0.95]`, *before* the reused IMAGE arm is read.

## VERDICT: NO-GO — sub-reading (a) CLEAN DEGENERATE NO-GO

The valid two-judge category-match scorer puts the band metric **below the 0.60 floor**. The s127
"it's just a scorer artifact, the fluent channel is competent" optimism is **NOT borne out**: under a
scorer that explicitly forbids string overlap and grades semantic referent identity, a held-out
competent reader still fails to *specifically* recover the depicted referent for the majority of items.
The magnitude read is deferred, the IMAGE arm is not read, prediction 3 stays untested. A secondary
validity nuance for a later session is noted under "Surface forward" but does **not** relax this gate.

## 1. Independent band-metric recomputation (from `raw/regrade_calls.json`, not the summary)
- 480/480 calls parsed clean, 0 errors, leg labels correct (cross ⟺ judge≠source, 0 mislabels);
  `frozen/regrade.json` grades consistent with raw on both cross legs.
- Cross legs: **gpt-judge × gemini-guesses = 46/120 = 0.3833**; **gemini-judge × gpt-guesses = 59/120 =
  0.4917**.
- **Band metric = two-judge mean over cross legs = 0.43750**, matching the frozen summary exactly.
  **0.4375 < 0.60 → OUT OF BAND, BELOW the floor.** Confirmed, no discrepancy. (Self legs, diagnostics
  only: gpt 0.367, gemini 0.458.)

## 2. HIGH-verdict spot-check (the ratified binding safeguard) — PASS, no rubber-stamp
Hand-read **all 105 cross-leg HIGH verdicts** for word_referent ≟ recovered_referent. The (a)/(b)
fields genuinely match the same specific referent in the large majority, and — decisive for anti-cheat
— the judges award HIGH on **zero-string-overlap** synonym/Latinate/variant pairs while naming the
shared referent (`thymus`→thyme, `ara`→hyacinth macaw, `aquila`→golden eagle, `mescal`→mezcal,
`gantlet`→gauntlet, `sty`→stye, `mike`→microphone, `mouse`(injury)→black eye, `lumber`→baseball bats,
`supporter`→jockstrap). That is the rubric working as designed, not string-matching. A handful are
mildly generous (`mercury`→Hermes [Roman vs Greek, same depicted statue], `lid`→fedora hats,
`rice`-sticky→white rice), but all are genuine category-level identities — **no HIGH is an (a)≠(b)
rubber-stamp that must be struck.** Net effect: the HIGH side is, if anything, slightly **lenient**, so
0.4375 is an upper-ish estimate, never deflated.

## 3. Mirror over-strictness assessment — 0.4375 is a VALID measurement, not depressed by an over-strict judge
The crucial new question, and the evidence is clear.
- **All 32 cross-leg NONE verdicts are validly none.** Each is a genuine *different-referent* miss the
  auditor produced (`bag`→woman in red dress, `argonaut`→Helen of Troy, `lift`→wrestling match,
  `bug`(surveillance)→soldier with radio, `boat`-travel→Santorini decoration, `cinnabar`→erythrite,
  `brace`(orthopedic)→suspenders [British "braces", different referent], `anapurna`→Durga). Field (a)
  shows the judge correctly reading the gold sense and marking a different referent. None are
  same-referent recoveries mis-scored none.
- **103 cross-leg PARTIALs (45 hand-sampled, seed-fixed):** dominated by genuinely partial recoveries —
  hypernym/whole-for-part (`cardamom seed`→pods, `mimosa flowers`→tree, `wood barrel`→wine barrels),
  co-present object (`boa scarf`→fashion attendee, `delivery package`→scooter), related-but-different
  specific (`tack pins`→cut nails, `stinger`-scorpion→bee stinger, `cinnabar`→cobaltite), or
  scene-not-object (`butterfly stroke`→swimmer, `sea voyage`→sailboat race). **No genuine
  same-specific-referent recovery wrongly demoted to partial.** The few borderline calls
  (`absinthe liqueur`→absinthe glass; `lid eye`→woman's eye; `aurora tale`→Sleeping Beauty scene) are
  exactly the partial/high boundary the rubric asks a judge to draw.
- **Band-sensitivity bound:** reaching the 0.60 floor would require **39 of 103 cross partials** to be
  wrongly-demoted same-referent recoveries promoted to HIGH. My read finds at most a handful of
  borderline cases — an order of magnitude short of 39. **The judge is not over-strict; 0.4375 is a
  valid strict-referent-category-recovery rate.**

## 4. Inter-judge agreement — stable enough to certify
Reproduced exactly: pooled exact 0/1/2 = **0.683**, high-vs-not = **0.808**, Cohen-κ(high) = **0.608**
(substantial). Leniency diagnostic: self-vs-cross deltas small and **opposite-signed** (gpt self −0.125,
gemini self +0.075) — no systematic self-rubber-stamp; cross-only is doing its job. Most HIGH/PARTIAL
disagreements trace to genuine referent-granularity ambiguity in the gold `{word, phrase}`
(`graph`=node-edge-graph vs generic chart; `viola shrub`; `disk`-music), not an unstable boundary. The
boundary is stable enough to certify, and both cross legs sit below 0.60 individually (0.383 and 0.492).

## Surface forward (for a LATER session — strictly separate from this deferral)
One genuine, non-blocking validity nuance is now visible and is **queued in `NEXT.md` as an
open-decision *candidate*** (not opened this session — it changes nothing here and would only create
ratification overhead for a refinement that strengthens, not threatens, the NO-GO): **the band
`[0.60, 0.95]` was calibrated against v2's *de-referenced literal-lemma* `.130` floor (audit-params
P3), but the metric is now the more-generous *category-match* rate.** Reasoning it through: a
category-match scorer would *raise* the de-referenced floor too (v2's stripped descriptors would score
some category hits the literal scorer missed), which pushes the lower edge **UP, not down** — so
re-deriving the floor on the new metric makes the `[0.60, 0.95]` floor look, if anything, *too lenient*,
**strengthening** (not weakening) this NO-GO. There is no reading on which the transfer issue rescues
the run. A later session may want to ratify the band explicitly *on the category-match metric* (a
re-derived de-referenced floor) for cleanliness; that is a yardstick-refinement for a future critic and
changes nothing here.

## Anti-cheat statement — PASS
- I formed **no** preference about whether the eventual residual would read narrow or wide; this verdict
  turns only on the fixed band and the scorer's validity, never on the magnitude it would yield.
- **Freeze held.** The frozen rubric is a literal in the committed `regrade.py`; its sha256 recomputed
  from `JUDGE_SYS` = `55a67e39…` = the `rubric_sha256` in `frozen/regrade.json` and in the run log —
  what was run is what was frozen (committed in the wave-1 commit *before* the run). The harness
  faithfully implements the ratified rule: two held-out judges (panel.B gpt + panel.C gemini),
  CROSS-ONLY band metric, gold target = human `{word, phrase}` (not `gold_descriptor`, not a gloss),
  strict-semantic instruction declaring string overlap insufficient/irrelevant, mandatory (a)/(b)/(c)
  fields, band `[0.60,0.95]` fixed with >0.95 oracle-NO-GO / <0.60 degenerate-NO-GO. No gaming found.
- I did **NOT** read `raw/image.json` at any point. **No magnitude/rescue/RESULT/sep_nl artifact
  exists** (`analyze.py` scores RESULT sections only after a GO; none was run).
- The NO-GO **relaxes nothing**: IMAGE arm not read, band not re-tuned, magnitude deferred. The
  diagnosis that 0.4375 is a *valid* low rate (not an artifact) does not license proceeding — it
  confirms the honest read is (a), defer.
