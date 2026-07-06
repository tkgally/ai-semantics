# 2026-07-06 — AANN quant×temporal inversion (class-vs-lexical widening probe)

Operationalizes [`open-question/aann-quant-temporal-inversion`]; refines
[`result/aann-temporal-why-reanalysis`] (the one AANN cell where every panel model inverts the human
gradient — quant×temporal, "a scant three days": humans-highest, models-lowest). **Is that inversion
the whole quantity-adjective class or a few lexical items?**

## Session record

- **s188 (design stage):** `REVIEW-design-s188.md`, `vote-design.py`/`vote-design-nonanthropic.txt`
  — the design pre-run critic (GO-WITH-CONDITIONS) + non-Anthropic vote (NO-GO, convergent). Decision
  `decisions/open/aann-quant-temporal-inversion-design` opened.
- **s189 (ratify + freeze + run):** decision **ratified ADOPT-WITH-CHANGES** (Q1-C human-N-gated /
  **Q2-B monotone-primary** / Q3-A) → `wiki/decisions/resolved/aann-quant-temporal-inversion-design.md`.
  Froze: `prep.py` → `stimuli.json` (K=20 quant modifiers × 10 balanced items + 60 non-quant reference
  + 24 Tier-0 + 40 4-pt; 972 calls), `PREREG.md`, `analyze.py` (new §6 verdict logic, self-tested).
  `probe.py` byte-identical to v2b except `ABORT_USD`. `vote-ratify-s189*` = the ratification
  decorrelation vote; freeze-stage critic + vote below. Ran the panel; `results.json`;
  `VERIFIER-REPORT.md`; result → [`result/aann-quant-temporal-inversion-v1`].

Reproduce: `python3 prep.py` → `python3 analyze.py --selftest` → `python3 probe.py` → `python3 analyze.py`.
