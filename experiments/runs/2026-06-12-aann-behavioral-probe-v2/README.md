# Run record — AANN behavioral probe v2 (2026-06-12)

- **Design:** `experiments/designs/aann-construction-v2.md` (frozen pre-run);
  **PREREG:** `PREREG.md` in this dir (frozen + one pre-run amendment from the independent
  pre-run critic — all before any model call; see the amendment block).
- **Governing decision:** `wiki/decisions/resolved/aann-behavioral-operationalization.md`
  (ratified 2026-06-12, autonomous cross-session adversarial review; nine binding conditions).
- **Conjecture:** `wiki/findings/conjectures/aann-construction.md`.
- **Anchor:** `wiki/base/resources/mahowald-2023-aann-stimuli.md` (Exp-2 MTurk gradient;
  mirror commit `c8095a0008cd6538717de5cc937f90ce5944e688`, MIT).

## Pipeline

1. `prep.py` — derived `human_cell_means.csv` (204 cells) + `human_class_means.csv` (28
   class-cells) from all 3,600 non-filler Exp-2 ratings; froze `stimuli.json` (seed 20260612):
   408 anchored / 102 robustness / 60 held-out / 24 Tier-0. No model calls.
2. Independent **pre-run critic** → 3 blockers + 8 should-fixes, all applied pre-run
   (commit `b811065`), including the **noun-class guard** (a noun-class-marginal responder
   with zero adjective information would have passed the original thresholds at ρ=0.466/0.613).
3. `probe.py` — 1,782 calls (temp 0; A/B max_tokens 64, C 512 + `reasoning effort minimal`).
4. `analyze.py` — implements the frozen map exactly → `results.json`.
5. Independent **post-run verifier** — recomputed every gate from raw with independent code.

## Usage (billed `usage.cost`, summed; 0 missing in every arm)

```
A claude-sonnet-4.6   $0.1934   (anchored .1310 / robustness .0362 / heldout .0199 / tier0 .0063)
B gpt-5.4-mini        $0.0476
C gemini-3.5-flash    $0.0715
total_cost_usd:       $0.3125   (n_missing_cost = 0)
```

Pre-flight estimate was $1.0–1.5; actual ~4× under (single-integer outputs are cheap).
Day total 2026-06-12 (both sessions): ≈ $0.60 of the $5.00 cap.

## Outcome (pre-registered verdict map)

**SUPPORTED.** All three models: Tier-0 23/24, 23/24, 24/24 (pass ≥20); anchored cell-level
Spearman 0.7017 / 0.6843 / 0.7505 (threshold 0.40; bootstrap CIs exclude 0 by wide margins);
Zipf partial 0.69 / 0.66 / 0.74 (guard 0.20 — not frequency-confounded); within-noun-class
mean 0.63 / 0.66 / 0.65 (guard 0.25 — not a noun-class artifact); held-out replication 0.83 /
0.81 / 0.75 (threshold 0.50) with within-class 0.46 / 0.45 / 0.44 (guard 0.30); framing
correlation 0.93 / 0.82 / 0.82 (no fragility flag).

Result page: `wiki/findings/results/aann-behavioral-gradient-v2.md`.
