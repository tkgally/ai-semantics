# 2026-07-06 — AANN quant×temporal inversion (DESIGN-STAGE ONLY)

This directory holds the **session-188 design-stage** artifacts for the
`aann-quant-temporal-inversion-v1` probe. **No probe has run; $0 of experiment spend.**
The design (`experiments/designs/aann-quant-temporal-inversion-v1.md`) is **frozen-to-be**,
contingent on `wiki/decisions/open/aann-quant-temporal-inversion-design.md` (opened s188).

Contents (s188):
- `vote-design.py` / `vote-design-nonanthropic.txt` — the PROTOCOL §A3 non-Anthropic
  decorrelation vote on the design (QA companion to the fresh-agent design pre-run critic;
  the fresh agent keeps verdict authority). One `openai/gpt-5.4-mini` call via the probe REST path.

The probe **freezes (prep.py + PREREG) and RUNS a later session**, only after the decision
ratifies (cross-session adversarial review + non-Anthropic vote), with a freeze-stage pre-run
critic and a post-run recompute-from-raw verifier.
