# VERIFIER-REPORT — AANN temporal held-out widening (v2b)

**Independent post-run verification.** Fresh agent; all statistics re-derived from raw
with independently-written code (`/tmp/verify.py`, `/tmp/verify2.py`), not reusing
`analyze.py` functions. No API calls. No repo file edited except this report.

## Bottom line

**VERIFIED, 0 substantive mismatches.** Every reported headline figure reproduces
exactly from the raw data under the frozen instrument and frozen statistics. The run
obeyed its frozen PREREG: the freeze commit (`ef53b26`, 2026-06-13 01:42:57Z) precedes
the raw-data commit (`299ceaa`, 2026-06-13 01:54:00Z); the P100/P4/PT0 prompt strings are
byte-identical to v2's `probe.py`; PREREG.md differs from PREREG-draft.md only in the
freeze header (lines 1–9). Three items require disclosure (below); all are already
handled by the result's mandatory-caveat machinery or are inherent instrument facts.

## Mismatch table (reported vs independently recomputed)

| Figure | Reported | Recomputed | Match |
|---|---|---|---|
| Rows per model/arm | 80 / 24 / 40 | 80 / 24 / 40 | ✓ |
| uid match to stimuli, dupes | match / 0 | match / 0 | ✓ |
| Missing (all arms, all models) | 0 | 0 | ✓ |
| Billed total (Σ usage.cost) | $0.0793 | $0.079260 → $0.0793 | ✓ |
| Missing-cost calls | 0 | 0 | ✓ |
| Tier-0 last-token A (claude) | 23/24 | 23/24 | ✓ |
| Tier-0 last-token B (gpt) | 21/24 | 21/24 | ✓ |
| Tier-0 last-token C (gemini) | 22/24 | 22/24 (frozen parser) | ✓ * |
| Tier-0 first-token A/B/C | 23 / 21 / 24 | 23 / 21 / 24 | ✓ |
| Tier-0 by_position A/B/C | {9,15}/{13,11}/{8,16} | {9,15}/{13,11}/{8,16} | ✓ |
| Tier-0 pass (all) | true | true (all ≥20) | ✓ |
| Cell means A | 54.95/49.35/50.55/43.0 | identical | ✓ |
| Cell means B | 50.6/40.15/37.5/30.05 | identical | ✓ |
| Cell means C | 84.25/75.0/70.0/68.75 | identical | ✓ |
| Cell ρ A/B/C | −0.2 / −0.4 / −0.4 | −0.2 / −0.4 / −0.4 | ✓ |
| Adj ρ A/B/C | −0.1389 / −0.0281 / −0.0458 | identical | ✓ |
| Bootstrap CI A | [−0.4382, 0.1715] | [−0.4382, 0.1715] | ✓ |
| Bootstrap CI B | [−0.3534, 0.3051] | [−0.3534, 0.3051] | ✓ |
| Bootstrap CI C | [−0.3521, 0.2652] | [−0.3521, 0.2652] | ✓ |
| Verdict A/B/C | FAILS / THIN / THIN | FAILS / THIN / THIN | ✓ |
| Stratum verdict | STILL-TOO-THIN / MIXED | STILL-TOO-THIN / MIXED | ✓ |
| Tourish-excl cell ρ A/B/C | −0.2 / −0.4 / −0.4 | identical | ✓ |
| Tourish-excl adj ρ A/B/C | −0.038 / −0.0834 / −0.1539 | identical | ✓ |
| Tourish-excl CI A/B/C | as reported | identical | ✓ |
| Tourish verdict-differs A/B/C | true / false / true | true / false / true | ✓ |
| Framing ρ A/B/C | 0.9388 / 0.8783 / 0.815 | identical | ✓ |
| Framing fragility flag | false (all) | false (all) | ✓ |
| New-only adj ρ A/B/C | −0.1512 / −0.1508 / −0.0595 | identical | ✓ |
| Pooled item ρ A/B/C | −0.0635 / 0.0041 / −0.0815 | identical | ✓ |
| Partial ρ (Zipf) A/B/C | −0.1441 / −0.0273 / −0.0578 | identical | ✓ |
| Per-class spread SD (all) | as reported | identical | ✓ |
| New vs carryover means (all) | as reported | identical | ✓ |
| Carryover-vs-v2 ρ A/B/C | −0.09 / −0.0589 / 0.0823 | identical | ✓ |
| Carryover-vs-v2 mean signed diff | −2.4375 / −0.7812 / −8.5938 | identical | ✓ |
| Tier-0 pairs byte-identical to v2 | asserted | confirmed (24/24) | ✓ |
| P100/P4/PT0 byte-identical to v2 | asserted | confirmed | ✓ |
| PREREG vs draft = freeze header only | asserted | confirmed | ✓ |
| Freeze precedes run (git) | asserted | confirmed (01:42 < 01:54) | ✓ |
| Item balance (nouns/nums/templates/classes) | 16ea/40-40/28-28-24/20ea | identical | ✓ |
| Robustness 4pt: 40 unique adj, {3,3,4} per class | asserted | confirmed | ✓ |
| Freq audit (4 classes pass, exact medians) | as PREREG | identical | ✓ |

\* See disclosure 1 — the C 22/24 figure is parser-dependent.

## PASS/FAIL per check

1. **Completeness / integrity — PASS.** 80/24/40 rows × 3 models; all uids match
   stimuli.json; 0 dupes; 0 missing; Σ usage.cost = $0.079260 (→ $0.0793), 0 missing-cost.
2. **Tier-0 gate — PASS.** All three pass (≥20/24) under the frozen last-token parser
   (A 23, B 21, C 22); first-token descriptive (23/21/24) matches; by_position matches.
3. **Primary 4-cell Spearman — PASS.** Cell means and ρ reproduce exactly.
4. **Secondary adjective-grain + bootstrap — PASS, EXACT.** Adj ρ and all three 95% CIs
   reproduce to 4 dp with seed 20260613, 10,000 resamples, indices [249, 9749],
   average-rank ties, NaN-resample→0, **using analyze.py's sorted-adjective ordering**
   (see note). Independent code, exact match.
5. **Verdict mapper — PASS.** Applying the frozen thresholds to my own numbers yields
   A = FAILS-TO-REPLICATE (CI upper 0.1715 < 0.20), B = STILL-TOO-THIN, C =
   STILL-TOO-THIN; precedence (REPLICATES before FAILS) is moot here; ≥2-of-3 over all
   three passers ⇒ STILL-TOO-THIN / MIXED. Matches.
6. **Pre-declared descriptives — PASS.** Tourish sensitivity (verdict flips for A and C,
   stays for B; mandatory caveat triggered for A and C); framing ρ (all ≥ 0.815, no
   fragility); new-only ρ; pooled item ρ; partial ρ; spread; new-vs-carryover;
   carryover-vs-v2 (Spearman + mean signed diff) — all reproduce exactly.
7. **PREREG conformance — PASS.** Freeze precedes run; prompts byte-identical to v2;
   draft↔frozen diff confined to the freeze header.
8. **Anomalies — see disclosures.** No degenerate/constant outputs (12–34 distinct
   ratings per model); a few verbose Tier-0 responses handled by the frozen parser.

## Anomalies / disclosures the result page MUST carry

1. **Tier-0 C is parser-sensitive (already gate-safe).** Gemini emitted verbose,
   "neither is grammatical, but if forced…" Tier-0 answers on three `ugly-three-desks`
   pairs, each mentioning both A and B. The frozen `parse_ab_last` does **not** strip
   markdown bold (`**A**`), so it sees no bare A/B token in two of them and falls to an
   earlier in-text bare letter — yielding the stored `B` (against gold A). An equally
   defensible parser that strips `**` would score those as `A`, giving C **24/24**
   first-token but only **21/24** last-token. Either way C passes (≥20), so the gate
   verdict is unaffected; but the headline "C Tier-0 = 22" rests on the frozen parser's
   markdown-blindness. Worth a one-line note. (A also has one verbose `**A**` response,
   correctly scored.)
2. **Strong "tourish"-typo template effect drives the verdict flips.** Mean rating on
   template-2 (the upstream typo "The tourish stayed…") is far below the other two
   templates for every model — A 81.9/46.2/**15.4**, B 73.5/35.4/**4.8**,
   C 90.2/78.6/**51.5** (templates 0/1/2). This is a large surface confound on the
   gradient read; removing template-2 flips A (FAILS→THIN) and C (THIN→FAILS). The
   mandatory tourish caveat is correctly generated for A and C and **must appear** on the
   result page (it already does in `results.json`). The instrument-continuity decision to
   keep the typo template is the source of this fragility.
3. **The whole stratum is negatively-signed at every grain.** All cell ρ are negative
   (−0.2/−0.4/−0.4), all adjective ρ negative, all pooled/new-only/partial ρ ≤ 0. No
   model tracks the human anchored-half ordering positively. This is consistent with the
   reported null/fail reading; the result page should not soften it.

## Notes for reproducers

- **Bootstrap order matters.** `analyze.py` resamples over `adjs = sorted(amean)`
  (alphabetical). The RNG draw sequence is order-independent, but the index→value map is
  not, so reproducing the CI to the last digit requires the **sorted** adjective order.
  My first pass used build order and got CIs off by ≤0.009 (e.g. A [−0.4368, 0.1757]);
  switching to sorted order gave an exact match. Not a defect — just a reproducibility
  prerequisite worth recording.
- **by_position** in `results.json` is the count of A-answers vs B-answers across all 24
  pairs (not correct-by-gold-position); recomputed under that definition it matches.
