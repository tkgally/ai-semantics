# Post-run verification report — aann-quant-temporal-inversion-v1 (session 189)

Independent recompute-from-raw (PROTOCOL §5), by a fresh agent that did not write the analysis. Own
script over `raw/*.json` (no `import analyze.py`); scratch removed. **VERDICT: NULL CONFIRMED; 0
discrepancies; no fabrication; anti-cheat clean.**

1. **Tier-0 gate — REPRODUCED.** A 21/24, B 21/24, C 23/24 (value == gold `aann_position`), all ≥ 20 →
   3/3 passers.
2. **Four-class means — REPRODUCED to 3 dp.** A quant 56.705 / ambig 65.75 / pos 49.80 / neg 45.25;
   B 51.99 / 65.35 / 38.85 / 22.55; C 81.725 / 94.75 / 69.25 / 79.00.
3. **NULL test (B2) — REPRODUCED: quant NOT lowest for any model.** Ranks low→high: A & B
   `neg < pos < quant < ambig` (quant 3rd of 4); C `pos < neg < quant < ambig` (3rd). Panel NULL.
4. **B_min, median/Q3 of d — REPRODUCED.** median_d +15.55 / +38.05 / +25.00 (strongly positive); Q3_d
   +21.58 / +40.08 / +25.88 — not inverting.
5. **Per-modifier inventory-artifact pattern — REPRODUCED.** `towering` inverts 3/3 (−21.2/−14.8/−50.2);
   `ample` A/C, `colossal` A only, `hefty` A, `substantial` C — all large-magnitude. Natural/small items
   {mere, scant, good, full, measly, paltry} positive in all three → do not invert.
6. **Arm-1 anchored — REPRODUCED.** n_model_low & human_high: A 1 (hefty), B 0, C 1 (substantial);
   Spearman(model,human) 0.552 / 0.600 / 0.814 (positive).
7. **Tourish (template-2) exclusion — REPRODUCED.** Quant still not lowest for any model → NULL holds
   (all `agrees: true`).
8. **Anti-cheat / no fabrication — CLEAN.** Raw texts parse to recorded integers; 0 missing across all 9
   raw files; verdict logic uses MIN baseline and NULL-first, matching the PREREG. **All 10 Arm-1
   per-modifier human means reproduce exactly** against a direct recount of `adjexp_turk.csv` (temporal
   only) — no invented ratings.

The located v2b inversion reads as an **inventory artifact** of a few large-magnitude carryover items
(towering foremost), not a class property.
