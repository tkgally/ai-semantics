# PREREG — Japanese comparative-correlative replication (A6)

**Date:** 2026-07-13 (session 215) · **Status:** FROZEN (pre-critic, pre-run). Governed by
[`decisions/resolved/cross-linguistic-cc-replication-scope`](../../../wiki/decisions/resolved/cross-linguistic-cc-replication-scope.md)
(Q1-C / Q2-B / Q3-A). Full design: [`design/comparative-correlative-japanese-v1`](../../designs/comparative-correlative-japanese-v1.md).

> **FREEZE (post-C1, before any probe call).**
> `sha256(items.csv) = 31597d2901cfe68ce54fa1aa393975ec139a8bb1dfe4b9e8de273aa83f5b8b8c` (136 items).
> `sha256(freq_control.json) = 02d275a1c72c1bf4d979e5c6e6508fc5b6a2ff9a168ce8f0788a5633ff9e4b94`.
> Instrument shape byte-parallel to the frozen English powered + German CC instruments; the only
> deliberate change is the target LANGUAGE (English `the…the` / German `je…desto` → Japanese `〜ば〜ほど`).
> First freeze (pre-C1): items `2d212d92…` / freq `5b780f98…`; C1 = 4 cc-inverse consequents made
> explicitly scale-decreasing per the pre-run critic (see the design's *Pre-run critic outcome* section).

**Program item:** A6 (cross-linguistic replication), the **Japanese** (stronger, typologically-distant)
arm — the committed-but-conditional successor the scope decision names (Q1-C), unblocked by the German
replication (s213, REPLICATES 3/3) + `-ba…hodo` source-verification (condition ii, s215). **What it
feeds:** whether [`claim/comparative-correlative-covariation`](../../../wiki/findings/claims/comparative-correlative-covariation.md)'s
construction-driven covariation reading survives a **typologically distant** surface-statistics change —
a **stronger** (still within-model, still partial: n=3, two non-English languages ≠ all) discharge of
the distributional-shadow worry than German's modest lever gave. **Internal-contrast-only** (Q3-A): no
human comparison.

## Purpose (one sentence)
Port the frozen English/German construction-isolation / direction-flip / atypical-robustness instrument
to Japanese (`〜ば〜ほど`, no overt comparative morpheme) and read the same magnitudes with 95% CIs,
testing whether the covariation reading is construction-driven rather than a surface template of English
(or of any single language).

## Order of operations (anti-cheat, condition iii)
1. `build_items.py` → items.csv (FROZEN, sha above). ✅ committed before any call.
2. `build_cooc_ja.py` → freq_control.json from UD Japanese-GSD via janome (FROZEN, sha above). ✅ committed before any call.
3. Independent pre-run critic (fresh agent + non-Anthropic Japanese-fidelity vote) → GO/NO-GO.
4. `smoke.py` Japanese-competence gate (each model ≥10/12 AND panel mean ≥0.90). If NO-GO, withhold the run.
5. `probe.py` (only after 3+4 GO) → raw/. `analyze.py` → results.json.

## Self-audit of items against the grammar source (freeze condition viii)
Lead-agent self-audit against [`source/japanese-ba-hodo-cc`](../../../wiki/base/sources/japanese-ba-hodo-cc.md).
See [`design/comparative-correlative-japanese-v1`](../../designs/comparative-correlative-japanese-v1.md)
§"Self-audit of items" for the systematic checks (antecedent `[Pred‑ば][Pred]ほど` repetition; verb-final
consequent direction; same-word controls; atypical direction-neutrality) — all PASS — and the honest
residual notes (antonym inverse consequents; janome collision noise; lead-agent self-audit is weaker
than a native auditor, corroborated by the smoke gate + the non-Anthropic Japanese-fidelity vote).

## Primary quantities + CIs, verdict frame, budget
See [`design/comparative-correlative-japanese-v1`](../../designs/comparative-correlative-japanese-v1.md)
(§Primary quantities, §Verdict frame, §Budget). Deliverable = point estimate + 95% CI (cluster
bootstrap over pairs, B=2000, seed 20260713); thresholds reported for continuity only. Symmetric
frame: REPLICATES / ATTENUATED / NULL-or-REVERSAL, a null first-class (and, on the stronger lever, an
especially informative one). Pre-flight ≈ $0.15–0.35 billed (816 main calls + 36 smoke calls); actuals
from `usage.cost`.
