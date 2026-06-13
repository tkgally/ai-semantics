# VERIFIER-REPORT — relational-history-perturbation-v3

Independent post-run verification. Fresh agent; every figure re-derived FROM RAW with
hand-written code in `/tmp/verify.py` (does NOT import `analyze.py`/`common.py`; it
re-maps `pick`→`pick_cid` from the frozen per-cluster matcher arrays in `stimuli.json`,
re-derives `in_pair`/`picked_chron_last`/`picked_phys_last`/`correct`, re-implements the
clustered bootstrap with the PREREG seed, and re-implements the verdict tree). No API
calls. Only file written: this report.

## Bottom line

**VERIFIED — 0 mismatches.** Every headline figure reproduces exactly from raw under
independent recomputation: row counts, sha256, uid set, truncation/compliance/retries,
gating, ρ_chron/ρ_phys, bootstrap CIs (to the digit), guards, floors, all three verdicts,
and the billed cost. The verdict tree was applied to my numbers and returns the same
labels with the same PREREG reasons. PREREG freeze provably precedes the finding-bearing
data. **One interpretation caveat (not a numeric error) the result page MUST state — see
§Interpretation.**

## Mismatch table (reported vs recomputed)

| Quantity | Reported | Recomputed | Match |
|---|---|---|---|
| rows claude/gpt/gemini | 144/96/144 | 144/96/144 | ✓ |
| stimuli.json sha256 | d0ae76…a94439 (PREREG = frozen file) | d0ae76…a94439 | ✓ |
| uid set = frozen stimuli trial set | yes | yes (all 3, exact) | ✓ |
| dup uids | 0 | 0 | ✓ |
| finding-bearing calls | 384 | 384 | ✓ |
| billed (full) | $0.385995 | $0.385995 | ✓ |
| billed by model | — | claude $0.244008 / gpt $0.035979 / gemini $0.106008 (Σ=0.385995) | ✓ |
| missing-cost | 0 | 0 | ✓ |
| finish_reason=length parsed (probe) | 0 | 0 | ✓ |
| finish_reason=length parsed (cert) | 0 | 0 (all 207 = stop) | ✓ |
| strict-compliance (all 3) | 1.000 | 1.000 | ✓ |
| retries (all 3) | 0 | 0 | ✓ |
| NA (all 3) | 0 | 0 | ✓ |
| pick_cid recompute mismatches | — | 0 (all 3 models) | ✓ |
| derived-flag recompute mismatches | — | 0 (all 3 models) | ✓ |
| gpt control gate / n_pass | 0.583 / 1 of 6 | 0.5833 / 1 of 6 | ✓ |
| claude control gate / n_pass | 0.833 / 5 of 9 | 0.8333 / 5 of 9 | ✓ |
| gemini control gate / n_pass | 0.917 / 7 of 9 | 0.9167 / 7 of 9 | ✓ |
| gpt realized clusters | 6/9 (96 trials) | 6: {0,1,2},{0},{0,1} = 72 mixed + 24 ctrl = 96 | ✓ |
| gpt shortfall F2/F4 | 3→1 sample / 5→2 samples | F2 cert 3 → min(1,3)=1; F4 cert 5 → min(2,3)=2 | ✓ |
| claude fwd ρ_chron / CI | 0.600 [0.533,0.667] | 0.6000 [0.5333,0.6667] side=1 | ✓ |
| claude rev ρ_chron / CI | 0.500 [0.367,0.667] | 0.5000 [0.3667,0.6667] side=0 | ✓ |
| claude rev ρ_phys / CI | 0.500 | 0.5000 [0.4000,0.6000] side=0 | ✓ |
| claude guard/floor24/floor36 | T/T/F | True/True/False | ✓ |
| gemini fwd ρ_chron=ρ_phys / CI | 0.780 [0.659,0.902] | 0.7805 [0.6585,0.9024] side=1 | ✓ |
| gemini rev ρ_chron / CI | 0.595 [0.500,0.738] | 0.5952 [0.5000,0.7381] side=0 | ✓ |
| gemini rev ρ_phys / CI | 0.500 [0.429,0.571] | 0.5000 [0.4286,0.5714] side=0 | ✓ |
| gemini guard/floor24/floor36 | T/T/T | True/True/True | ✓ |
| gpt out-of-pair | (UNDER-POWERED not reached) | 0.2361 (≤0.5) | ✓ |
| gpt guard_ok | False | False (1 gated cluster/dir < 3) | ✓ |
| gpt fwd/rev CIs | degenerate | degenerate (zero-width, side=None) | ✓ |
| VERDICT gpt | METHODOLOGICAL NULL | METHODOLOGICAL NULL | ✓ |
| VERDICT claude | INCONCLUSIVE-MIXED | INCONCLUSIVE-MIXED | ✓ |
| VERDICT gemini | INCONCLUSIVE-MIXED | INCONCLUSIVE-MIXED | ✓ |

## PASS/FAIL per check

1. Integrity — **PASS.** 144/96/144; uids unique, no dupes, set-equal to the frozen
   `stimuli.json` trial set per model; sha256 == PREREG value == frozen file. gpt 6/9
   realized exactly matches stimuli (6 clusters) and the recorded PREREG shortfall, with
   the F2(→1)/F4(→2) partition reproduced from the embedded certification census.
2. Truncation/compliance — **PASS.** 0 records parsed from a finish_reason=length reply
   (probe AND certification); strict-compliance 1.000; 0 NA; 0 retries — all reproduced.
3. Gating — **PASS.** All-4-controls-correct gate recomputed independently (re-mapping
   each control's pick to a CID and comparing to `target`): gpt 1/6, claude 5/9,
   gemini 7/9; exact cluster lists match analysis.json. Every cluster has exactly 4
   controls (2 twins × 2 directions), as PREREG S1 requires.
4. Primary stats — **PASS.** ρ_chron, ρ_phys, in-pair n, gated-cluster counts, out-of-pair,
   and the 10,000-resample clustered-bootstrap CIs all reproduce to the digit with the
   PREREG seed (SEED=20260613 ^ crc32("PRIMARY:{dir}:{nm}")), per-cluster aggregation,
   percentile at int(0.025·N)/int(0.975·N).
5. Guards/floors — **PASS.** guard_ok (≥3 gated clusters/dir), floor24_ok (≥24 in-pair/dir),
   floor36_ok (≥36/dir) all reproduce: claude T/T/F, gpt F/F/F, gemini T/T/T.
6. Verdict mapper — **PASS.** My independent ordered tree returns gpt METHODOLOGICAL NULL
   (clause 1, guard fails), claude + gemini INCONCLUSIVE-MIXED (final else). The
   FALSIFIED clause did NOT fire (no model has a both-directions same-side non-zero
   ρ_chron CI) and null-certification did NOT fire (no model has all-four-CIs-include-0.5);
   reasons match PREREG verbatim. Both-directions agreement and degenerate-CI handling
   verified (see §Anomalies).
7. Interpretation — **PASS with a required caveat** (see §Interpretation).
8. PREREG conformance — **PASS.** `git merge-base --is-ancestor ffdb7eb 2256d84` = YES
   (freeze precedes full-probe data). `diff PREREG-draft.md PREREG.md` shows ONLY the
   freeze-header change (2 hunks) + the sha256 placeholder fill + the shortfall
   placeholder fill — exactly the 3 documented edits, nothing else. Sensitivity cuts are
   stored as `verdict_descriptive_only` and none flips any primary verdict; no post-hoc
   threshold edits (K_GUARD=3, floors 24/36, OOP_MAX=0.5 match PREREG).
9. Anomalies — see below; all handled correctly per PREREG.

## Interpretation check (done carefully)

Headline: *"the forward chronology signal does not survive direction reversal — physical
position, not stated chronology."*

What raw actually shows for gemini's 7 gated clusters:
- **fwd:** ρ_chron = ρ_phys = 0.7805 — and these are necessarily IDENTICAL in fwd, because
  by construction the chronologically-last line is also the physically-last line in fwd.
  **The forward arm alone cannot separate chronology from physical position.**
- **rev:** ρ_phys = **0.5000 exactly** (CI [0.429,0.571], includes 0.5) and ρ_chron = 0.5952
  (CI [0.500,0.738], lower bound touches 0.5, includes 0.5).

The both-directions agreement requirement is correctly **NOT met**: fwd ρ_chron CI is
clean (side=1) but rev ρ_chron CI includes 0.5 (side=0). So no chronology verdict fires —
correct, and the INCONCLUSIVE-MIXED label is right.

**Flag — the headline's "physical position, not stated chronology" gloss is an OVER-CLAIM
and the result page must soften it.** If the behaviour were physical-position-following,
the reverse arm's ρ_phys would be ELEVATED above 0.5; instead rev ρ_phys collapses to
**exactly 0.50** (physical-last twin chosen at chance). The data are equally — arguably
better — read as: *the forward elevation does not replicate under reversal at all; in
reverse, the model tracks neither physical position nor (CI-clean) chronology.* The
reverse arm shows a non-significant numeric lean toward chronology (ρ_chron 0.595), not
toward physical position. The only defensible headline is the null/mixed one: **the
forward signal does not survive reversal in either interpretation; v3 does not separate
chronology from physical position, and INCONCLUSIVE-MIXED stands.** Asserting "physical
position" as the cause is not supported — that pattern would require rev ρ_phys > 0.5,
which is falsified by rev ρ_phys = 0.50.

## Anomalies (all correctly handled)

- **gpt near-total control failure** (control acc 0.583; only cluster (0,1) passes the
  all-4-controls gate). Combined with the 6/9 certification shortfall this leaves 1 gated
  cluster/direction → guard fails → METHODOLOGICAL NULL. The gpt primary CIs are all
  zero-width (degenerate, single cluster); under PREREG they satisfy no clause, and the
  guard outranks them anyway. Correct. gpt out-of-pair 0.236 (≤0.5) — UNDER-POWERED would
  not have fired even if reached.
- **Degenerate CIs**: gpt fwd/rev ρ_chron and ρ_phys are all zero-width (side=None);
  treated as satisfying no clause. Verified.
- **Boundary CI**: gemini rev ρ_chron CI lower bound = 0.500000 exactly (non-degenerate,
  hi=0.738). Per the code, lo>0.5 is required for side=1; lo==0.5 → side=0 (includes 0.5).
  This is the hinge of the whole verdict and it is handled exactly as PREREG specifies.
- **claude leave-one-pair-out cuts** drift between INCONCLUSIVE-MIXED and the named-gap
  sub-label across pairs — descriptive only, do not touch the primary verdict, but worth
  disclosing as instability at this n.
- **Suspicious uniformity**: none. Strict-compliance 1.000 / 0 retries / 0 NA across 384
  calls is clean but plausible under a forced single-label format with a 512-token cap;
  finish_reasons are all "stop"; no implausibly identical per-cluster patterns observed.

## What the result page MUST disclose or soften

1. **Soften the "physical position, not stated chronology" headline** (see §Interpretation):
   rev ρ_phys = 0.50 exactly refutes a physical-position-following reading; the honest
   claim is that the forward elevation does not survive reversal under EITHER reading,
   and fwd cannot separate the two by construction. State INCONCLUSIVE-MIXED plainly.
2. **gpt is a METHODOLOGICAL NULL driven by control failure + certification shortfall**
   (1 gated cluster/dir), not evidence about commutativity — say so; do not let gpt's
   degenerate fwd ρ_chron=0.667 read as any signal.
3. **claude floor36 unmet** (30 in-pair/dir < 36): even its all-null arms could not have
   been null-certified; its mixed pattern (fwd CI-clean, rev not) is why it is MIXED.
4. **The PREREG scope limits must be repeated** on the result page (critic issue-1(a)/(b)):
   harvested-and-certified (not live) stimuli; certification selects for solo-decodable
   lines; verdicts hold under forced-label elicitation only.
5. **No pooling / no numeric comparison with v2** (PREREG S5) — verdict-level supersession
   only.

— Independent verifier, 2026-06-13.
