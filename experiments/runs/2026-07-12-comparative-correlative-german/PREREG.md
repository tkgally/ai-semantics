# PREREG — German comparative-correlative replication (A6)

**Date:** 2026-07-12 (session 213) · **Status:** FROZEN (pre-critic, pre-run). Governed by
[`decisions/resolved/cross-linguistic-cc-replication-scope`](../../../wiki/decisions/resolved/cross-linguistic-cc-replication-scope.md)
(Q1-C / Q2-B / Q3-A). Full design: [`design/comparative-correlative-german-v1`](../../designs/comparative-correlative-german-v1.md).

> **FREEZE (before any probe call).**
> `sha256(items.csv) = 2c2301c8bdc1eebe068cbf6fe60a17c56d4a5ec0b0030b01c83936ab573d3c92` (136 items).
> `sha256(freq_control.json) = cae2d144b2f189996a2bcbf9a94fdaf1cc4f10b095e324942f68c0712c36f823`.
> Instrument shape byte-parallel to the frozen English powered CC instrument; the only deliberate
> change is the target LANGUAGE (English `the…the` → German `je…desto/umso`).

**Program item:** A6 (cross-linguistic replication). **What it feeds:** whether
[`claim/comparative-correlative-covariation`](../../../wiki/findings/claims/comparative-correlative-covariation.md)'s
construction-driven covariation reading survives a surface-statistics change — a **partial** discharge
of the distributional-shadow worry (German is a *modest* lever; Japanese is the stronger conditional
successor). **Internal-contrast-only** (Q3-A): no human comparison.

## Purpose (one sentence)
Port the frozen English construction-isolation / direction-flip / atypical-robustness instrument to
German and read the same magnitudes with 95% CIs, testing whether the covariation reading is
construction-driven rather than English-n-gram-driven.

## Order of operations (anti-cheat, condition iii)
1. `build_items.py` → items.csv (FROZEN, sha above). ✅ committed before any call.
2. `build_cooc_de.py` → freq_control.json from UD German-GSD (FROZEN, sha above). ✅ committed before any call.
3. Independent pre-run critic (fresh agent + non-Anthropic vote) → GO/NO-GO.
4. `smoke.py` German-competence gate (each model ≥10/12 AND panel mean ≥0.90). If NO-GO, withhold the run.
5. `probe.py` (only after 3+4 GO) → raw/. `analyze.py` → results.json.

## Self-audit of items against the grammar source (freeze condition viii)
Lead-agent self-audit against [`source/meinunger-2023-je-desto`](../../../wiki/base/sources/meinunger-2023-je-desto.md)
(the no-human-subjects substitute for a human auditor; adequate for German because it is high-resource
and self-auditable — the reason German was chosen first). **Systematic checks (all PASS):**

- **Gold consistency (mechanical, `build_items.py` asserts + a verifier pass):** all 34 `cc-positive`
  → `fc_gold=increase`/`nli_gold=0`; all 34 `cc-inverse` → `decrease`/`2`; all 68 controls →
  `undetermined`/`1`. 0 mismatches. Unique pids; 24 typical + 10 atypical enforced.
- **`je`-clause verb-final (subordinate):** every `cc-positive`/`cc-inverse` je-clause ends in its
  finite verb (`… der Roman **war**`, `… die Öfen **liefen**`, `… die Band **spielte**`, …). PASS.
- **`desto`/`umso`-clause verb-second (main):** every desto-clause fronts `desto`+comparative with the
  finite verb in second position (`desto geduldiger **blieb** der Leser`; `desto höher **stieg** der
  Preis`; `desto größer **fiel** die Ernte aus` [separable verb, particle final]). PASS.
- **Inverse decreases dim2 (highest-risk gold):** each `cc-inverse` desto-clause makes the dim2 scale
  named in the item DECREASE — via an antonym comparative (`ungeduldiger`→patience↓, `saurer`→sweetness↓,
  `wacher`→drowsiness↓, `ruhiger`→restlessness↓, `stiller`→talkativeness↓, `gelassener`→frustration↓,
  `gesitteter`→rowdiness↓, `blasser`→brightness↓) or `weniger/kleiner/kürzer/niedriger/langsamer/billiger`.
  All 34 verified by hand. PASS.
- **Same-word controls hold lexis constant:** `ctrl-two` (two independent declaratives) and
  `ctrl-single` (one comparative clause) reuse the pair's scalar words with no cross-clause dependency,
  so the CC-vs-control gap is purely the construction. PASS.
- **Atypical pairs are direction-neutral by world knowledge:** the 10 atypical pairs (teacup roundness ↔
  jam length, carpet redness ↔ elevator speed, …) have no world-knowledge covariation direction; UD-GSD
  co-occurrence is near-zero (mean 3.4; 1.5 OOV words/pair), so any asserted direction must come from
  the construction. PASS.

**Residual authoring notes (honest):** a few atypical dim1 NPs pair oddly with "zunimmt" (e.g. *das
Streifenmuster der Socke*), exactly mirroring the English instrument's atypical awkwardness (*the sock's
stripiness increases*) — within design tolerance, and the awkwardness is symmetric across forms. `desto
umso` synonymy is exercised implicitly (all items use `desto`; `umso` is attested equivalent per the
source, not separately tested).

## Primary quantities + CIs, verdict frame, budget
See [`design/comparative-correlative-german-v1`](../../designs/comparative-correlative-german-v1.md)
(§Primary quantities, §Verdict frame, §Budget). Deliverable = point estimate + 95% CI (cluster
bootstrap over pairs, B=2000, seed 20260712); thresholds reported for continuity only. Symmetric
frame: REPLICATES / ATTENUATED / NULL-or-REVERSAL, a null first-class. Pre-flight ≈ $0.15–0.30 billed
(816 main calls + 36 smoke calls); actuals from `usage.cost`.
