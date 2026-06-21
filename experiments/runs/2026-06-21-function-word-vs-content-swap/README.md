# Function-word-vs-content-word swap probe — BUILD v1 (session 67, 2026-06-21)

**Outcome: BUILD + CERTIFY complete; independent pre-run review → NO-GO; run DEFERRED. $0 spent (no model called).**

The build for the ratified [`decisions/resolved/function-word-anchor-design`](../../../wiki/decisions/resolved/function-word-anchor-design.md)
(probe for [`conjecture/function-word-substitutability`](../../../wiki/findings/conjectures/function-word-substitutability.md)).
Result write-up: [`result/function-word-swap-build-v1`](../../../wiki/findings/results/function-word-swap-build-v1.md).
The blocker decision it forced: [`decisions/open/function-word-count-vs-matching`](../../../wiki/decisions/open/function-word-count-vs-matching.md).

## What was built

- **Design (consistent-content-swap):** each item carries a target function word at an
  inferential pivot + a hypothesis it licenses. The **function swap** (because→although,
  some→every, will→would) is applied in the PREMISE ONLY (predicted to flip the NLI label);
  the **content swap** is applied CONSISTENTLY in both premise and hypothesis (predicted NOT
  to flip — a flip there would indicate model entanglement, not a lexical mismatch). The
  independent reviewer confirmed this design is sound and, if anything, biased toward the null.
- **Indicator:** 3-way NLI entailment-flip (instrument reused VERBATIM from the CxNLI /
  conative line). `probe.py` (3 calls/matched item × 3 models) and `analyze.py` (flip-rate
  contrast + bootstrap CI + manipulation check + per-class breakdown + falsify arm) are
  complete and runnable; they were never run.
- **Matching (build.py `verify_pair`):** content-out within |ΔLg10WF| ≤ 0.10 of the function
  word; content-in within 0.10 of the partner (mirrored spread); **signed length-delta equal
  to the function swap's (+1 for all three pairs)**. SUBTLEX-US `Lg10WF` via `freqlib.py`
  (full list gitignored; re-fetch with `experiments/data/subtlex-us/prep.py`).

## Why NO-GO (the measured obstacle)

`certify.py` → `certification.json`: the frozen set is **SOUND on every matching / shortcut-reader
/ integrity check** —

- length-only reader asymmetry **= 0.0 exactly** (both function and content swaps are uniformly
  +1 char; a Δ0 content swap would let a length-only reader manufacture the entire effect — the
  first certification pass caught this at 0.46 before the +1 fix);
- minimal-pair integrity holds (premise_fn differs from base ONLY by the function word;
  premise_ct ONLY by the content word; no function-word leak into the hypothesis);
- frequency-only reader: monotone pooled (func_gap − content_gap) = +0.031 (small);

— but it **FAILS the count**: under faithful matching only **66 clean items across 3 viable
content semantic classes** survive (because 38, some 22, will 6), versus the conjecture's
**≥200 / ≥4-class** confirm criterion (binding condition (e)). Root cause: the
frequency∩length∩coherence intersection is thin.

- The high-yield **person-noun route dies**: no open-class person noun sits at Lg10WF ≈ 3.33
  (matching `although`) with +1 length against a ≈4.74 partner.
- The **`the`→`a` swap admits NO frequency-matched content control** (no open-class word reaches
  Lg10WF ≈ 6.0) — it runs only as a function-only characterizing arm (`det_char`, 10 items).
- The **adjective content class has no clean frequency+length-matched swap** (the only matched
  candidates, sure→tight/empty/heavy, are semantically anomalous — the reviewer flagged them;
  removed).
- `some` and `will` are intrinsically low-yield: only **one** matched out-word each
  (`some`: *man*; `will`: *see*).

## Independent pre-run review (fresh agent) — VERDICT: NO-GO

Reproduced the build + certification; spot-checked items (caught and forced removal of ~14% broken
items: 5 ungrammatical `some:verb` "say the <person>" frames and 6 anomalous `because:adj`
items — now purged); independently probed SUBTLEX and confirmed ≥200 is near-infeasible under
faithful matching (generous authorable ceiling ~150–160, mostly carrier-repetition of a handful
of swaps, not lexical diversity); confirmed both confound controls sound (the +1 length match is
necessary; the consistent-swap design is not rigged). **Do not relax the ratified tolerances
autonomously; defer.** Full verdict folded into the result page.

## Files

`freqlib.py` · `build.py` · `frames.json` · `stimuli.json` (sha in `certification.json`) ·
`certify.py` · `certification.json` · `matching-report.json` · `probe.py` · `analyze.py`.
No `raw/` outputs (never run). No PREREG.md frozen (run deferred — `probe.py` refuses `full`
until a PREREG records the sha + a pre-run-critic GO).

## For the next session

After [`decisions/open/function-word-count-vs-matching`](../../../wiki/decisions/open/function-word-count-vs-matching.md)
is ratified: (1) purge already done; (2) mine the `because:verb` headroom (add OUT verbs
nearer/above *because* — give/need — to drive the content-gap residual to ≤0; the reviewer
noted talk/call sit ~0.10 below *because*, compressing the gap); (3) apply the ratified
count-vs-matching resolution; (4) re-freeze + independent pre-run critic GO; (5) run + verify.
