# Function-word-vs-content-word swap probe — BUILD v1 (session 67, 2026-06-21)

**Outcome: BUILD + CERTIFY complete; independent pre-run review → NO-GO; run DEFERRED. $0 spent (no model called).**

The build for the ratified [`decisions/resolved/function-word-anchor-design`](../../../wiki/decisions/resolved/function-word-anchor-design.md)
(probe for [`conjecture/function-word-substitutability`](../../../wiki/findings/conjectures/function-word-substitutability.md)).
Result write-up: [`result/function-word-swap-build-v1`](../../../wiki/findings/results/function-word-swap-build-v1.md).
The blocker decision it forced — **RESOLVED 2026-06-21 (session 68, adversarial review)**:
[`decisions/resolved/function-word-count-vs-matching`](../../../wiki/decisions/resolved/function-word-count-vs-matching.md).

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

`certify.py` → `certification.json`: `"ok": false`. The frozen set **passes** minimal-pair
integrity (premise_fn differs from base ONLY by the function word; premise_ct ONLY by the content
word; no function-word leak) and the **length-only-reader** check (asymmetry **0.0 exactly** —
both function and content swaps are uniformly +1 char; a Δ0 content swap would let a length-only
reader manufacture the entire effect, caught at 0.46 before the +1 fix). But it **FAILS three
checks** (an earlier version of this README and the result page wrongly called it "sound on every
check / fails only the count" — corrected session 68):

1. **count** — only **66 clean items** (because 38, some 22, will 6) vs ≥200;
2. **≥4-class span** — only **3 viable classes** (noun_person, noun_thing, verb; adjective dead);
3. **freq-only reader** — `(i) max POSITIVE threshold asymmetry ≤ 0.12` = **FALSE** (0.1212 at
   θ=1.25): the `because`-arm content gap (1.335) sits below the function gap (1.406), so a
   freq-only reader thresholding near 1.25–1.41 separates the conditions. (The monotone pooled
   func_gap − content_gap = +0.031 stays small, but the per-θ check fails.)

Root cause of the count/class failures: the frequency∩length∩coherence intersection is thin.

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

## Decision RESOLVED (session 68, 2026-06-21 — adversarial review)

[`decisions/resolved/function-word-count-vs-matching`](../../../wiki/decisions/resolved/function-word-count-vs-matching.md)
is ratified. The reviewer **overturned** the relax-length default: the function arm is degenerate
in Δlen (every function swap is +1 char → Δlen ≡ +1, zero variance, perfectly collinear with
condition), so length **cannot be regressed/stratified out** — it stays a HARD freeze-time gate.
Adopted instead: **widen the function-word inventory** at the unchanged ±0.10 frequency tolerance
(per-pair signed-Δlen gate) + capped carrier-authoring; fix the freq-only residual; keep ≥200/≥4
classes. See the decision page for the 9 binding build-v2 conditions.

## Session-68 build-v2 reconnaissance (supply at the UNCHANGED tolerances)

`freqlib.py`-driven scan of the full norm for new function-word pairs with content controls within
±0.10 Lg10WF at both ends AND a signed-Δlen-matched (out,in) combination (open-class filter on the
`prep.py` stoplist). Counts are raw combinatorial candidates **before** hand coherence/POS/
manipulation-check pruning — they show where supply *exists*, not the frozen set:

| new pair | class | Δlen | signed-Δlen combos | verdict |
|----------|-------|------|--------------------|---------|
| `few→many` | quantifier | +1 | 1755 | **strong** — opposite-direction quantity, like some→every; flips NLI |
| `many→every` | quantifier | +1 | 1119 | **strong** — quantity strengthening; flips NLI |
| `shall→should` | deontic modal | +1 | 503 | **plausible** — future/legal → advisory; check the flip |
| `when→while` | temporal subordinator | +1 | 356 | **weaker** — temporal/contrast; flip may be soft |
| `may→might` | epistemic modal | +2 | 750 | **EXCLUDE** — near-synonymous; will NOT flip NLI (fails manip-check) |
| `the→a` | determiner | −2 | (no open-class content at Lg10WF≈6) | char-only arm (as v1) |

So build-v2 supply is real: the quantifier pairs (`few→many`, `many→every`) generalize the existing
`some→every` route and can carry many noun/verb carriers; `shall→should` adds a modal route; these
plus a fixed `because` arm (OUT verbs at/above 4.737 so content gap ≥ 1.406) and a fourth content
class plausibly clear ≥200/≥4. **Caution:** the combo counts include subtitle-corpus junk
(contractions `don/ll/re`, abbreviations `dr/mr`, interjections) — the clean, same-POS, coherent,
manipulation-check-passing subset is much smaller and is the hand-authoring job. The build session
must freeze + re-certify (all parent checks PLUS the fixed freq-only check) under a **fresh** pre-run
critic before any spend; no item added/dropped after the first probe call.

## For the next session (build-v2 + run)

(1) Add the new function pairs above to `build.py`'s `FUNC` dict (generalize `verify_pair` to
per-pair signed Δlen — currently hardcodes +1 via `func_dlen`); (2) author coherent carriers +
content controls in `frames.json` for the quantifier/modal routes to reach ≥200 across ≥4 classes;
(3) fix the `because` arm (OUT verbs at/above *because*'s 4.737 Lg10WF so the freq-only check
passes); (4) `build.py` → `certify.py` until `"ok": true`; (5) **fresh** independent pre-run critic
GO/NO-GO; (6) freeze `PREREG.md` (sha + GO); (7) `probe.py full` (pre-flight ~$0.5 for ~200×3×3 NLI
calls); (8) `analyze.py` + independent post-run verifier; (9) write the result.
