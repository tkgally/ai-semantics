# POST-RUN VERIFICATION — BLiMP forced-choice sweep (A3b, s205)

Independent fresh-agent verifier recomputed every headline figure from the 7,200 raw per-call records +
`items.json` with its **own** script (`verify_indep.py`, did **not** import `analyze.py`).

## VERDICT: **REPRODUCED (0 discrepancies)** — matches `results.json` to 4 decimals on every figure and all four verdicts.

| model | ρ_prof | depth-gap | abs-acc (SD, min–max) | shallow / deep | F3-saturated? |
|---|---|---|---|---|---|
| A (claude-sonnet-4.6) | +0.6063 | +0.1106 | 0.9150 (0.1206, 0.57–1.00) | 0.9875 / 0.8769 | no |
| B (gpt-5.4-mini) | +0.5432 | +0.1684 | 0.8704 (0.1500, 0.53–1.00) | 0.9806 / 0.8122 | no |
| C (gemini-3.5-flash) | +0.6278 | +0.0697 | 0.9417 (0.1052, 0.47–1.00) | 0.9889 / 0.9192 | no |

Human depth-gap = +0.0647 (shallow 0.9304, deep 0.8657). Per-model excess-over-human: A +0.0459,
B +0.1037, C +0.0049.

**Verdicts (all match):**
- **R1 = PROFILE-ALIGNED** — all 3 ρ_prof > +0.40, none F3-saturated (3/3 ≥ 2/3). Descriptive/directional,
  non-promotable this run per C8.
- **R2 = DEPTH-GRADED** — depth-gap ≥ +0.05 on 3/3.
- **R2h = TRACKS-DIP** — only B's excess exceeds +0.05; A and C within ±0.05 → 2/3 TRACKS (not EXCEEDS).
- **instrument-failure = False** — poslock 0.055–0.163 (≪0.50), ans1_rate 0.438–0.490 (well within 0.5±0.40).

**Integrity — clean:**
- 7,200 total calls, 0 unparsed (no null choices).
- 120 data files (A/B/C × 40); every (model,paradigm) = 60 calls, 30 pairs, both `gf`/`gs` orders per pair,
  no duplicate orders.
- `correct` field self-consistent with `choice == good_pos` on every parsed row (0 mismatches).
- All 40 `items.json` `human_agreement` values match `human_validation_summary.csv` `total_mean` exactly
  (0 mismatches), incl. `sentential_subject_island` 0.60632 (the F4-floor min).
- Extra files in `raw/` are only logs, not stray data.

Scratch script `verify_indep.py` left in the run directory; no repository files edited by the verifier.
