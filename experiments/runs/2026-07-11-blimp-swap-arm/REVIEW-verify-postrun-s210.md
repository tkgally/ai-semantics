# REVIEW — Post-run verification, BLiMP R1 content-word-swap arm (s210)

*Independent fresh-agent post-run verifier. Recomputed every figure from `raw/` with an own script
(bootstrap seed 12345, different from the run's 20260711); did not import `analyze_swap.py`.*

## REPRODUCED: YES

Per-model per-stratum Δ̄ reproduce **exactly** to 4 decimals; bootstrap CIs match to ~2–3 decimals (3rd/4th
decimal only, as expected from a different seed). Per-paradigm order-averaged orig/swap accuracies reproduce
to <0.002 on all 36 cells. Independently re-derived `correct == (choice == good_pos)` on all 7200 rows — zero
mismatches.

| Model | Stratum | Reported Δ̄ / CI | Recomputed Δ̄ / CI (seed 12345) |
|---|---|---|---|
| A | shallow | −0.0300 [−0.0500, −0.0150] | −0.0300 [−0.0500, −0.0133] |
| A | deep | −0.0946 [−0.1199, −0.0709] | −0.0946 [−0.1199, −0.0709] |
| B | shallow | −0.0333 [−0.0533, −0.0150] | −0.0333 [−0.0550, −0.0166] |
| B | deep | −0.0567 [−0.0950, −0.0183] | −0.0567 [−0.0950, −0.0200] |
| C | shallow | −0.0267 [−0.0450, −0.0117] | −0.0267 [−0.0450, −0.0100] |
| C | deep | −0.0717 [−0.0950, −0.0483] | −0.0717 [−0.0950, −0.0483] |

**Call accounting:** 7200 total; 2400/model; 400/paradigm. **0 errors** all three. **13 unparsed** (all model
A deep: `sentential_negation_npi_scope` 4, `only_npi_scope` 9) — correctly explains A's deep `n_pairs=296`
(B, C deep = 300). **Diagnostics:** ans1 0.3904 / 0.4925 / 0.4288; poslock 0.2200 / 0.1467 / 0.1558 — the
INSTRUMENT-FAILURE guard (poslock>0.50 ∧ |ans1−0.5|>0.40) does not fire. Confirmed.

## Verdict check

- **Coded rule (whole CI ≤ −0.05):** SWAP-STABLE fails (no model deep within ±0.05); SWAP-DROPS-coded fires
  only for A's deep (1/3; B deep-hi −0.020, C deep-hi −0.048, neither ≤ −0.05) ⇒ **SWAP-INCONCLUSIVE.**
- **PREREG prose (Δ̄ ≤ −0.05 & CI excludes 0):** deep stratum satisfies on **3/3** ⇒ deep **SWAP-DROPS 3/3**.
- The coded implementation is **stricter** than the prose; SWAP-INCONCLUSIVE is the more conservative
  landing. Under **both** readings R1 is NOT SWAP-STABLE → **promotion correctly refused** (needs SURVIVES ∧
  SWAP-STABLE). The divergence should be stated so the first-class negative (deep DROPS 3/3 by prose) is
  recorded, not silently downgraded. *(Recorded on the result page + predictions row.)*

## C4 confound: +0.204 is MATERIAL and correctly blocks a memorization reading — PASS

orig mean log-C4 2.817 vs swap 2.614, gap +0.204 (orig ~1.6× more frequent in the pretraining proxy). Given
deep Δacc ≈ −0.07, a 0.2-dex pretraining-frequency deficit on the swap words is a plausible independent cause
of a drop that size ⇒ a deep drop **cannot be cleanly attributed to exact-string / lexical-item
memorization**. Nuances (do not change the conclusion): (1) the swap was tightly SUBTLEX-matched (mean |gap|
0.075) yet the C4 gap is +0.204 — a genuine subtitle-vs-web corpus mismatch, which is why the pretraining
check is not redundant with the SUBTLEX match; (2) the C4 comparison is over unique-word *sets* of unequal
size (489 orig vs 964 swap), a conservative set-level indicator, pointing in the confounding direction.

## Over-claim check: PASS

Every interpretive move is deflationary: R1 not promoted; the deep drop reported as real-but-confounded (not
clean memorization); the shallow drops attributed partly to build-defect artifacts; all PREREG scope caps
intact. The only asymmetry is a mild **under**-statement (coded INCONCLUSIVE where prose would license the
stronger SWAP-DROPS negative) — surfaced, not inflated.

## VERDICT: CONFIRMED-WITH-CAVEATS

All reported numbers reproduce exactly from raw; accounting/diagnostics/instrument-failure/C4-confound/
promotion-refusal all check out; the interpretation does not over-claim. The single caveat is the
coded-vs-prose verdict divergence — a conservative label choice that changes the name (INCONCLUSIVE vs deep
DROPS 3/3) but not the outcome (R1 refused promotion either way); stated explicitly in the write-up.
