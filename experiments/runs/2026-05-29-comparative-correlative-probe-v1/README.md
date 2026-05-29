# Run record — comparative-correlative covariation-inference probe v1

**Date:** 2026-05-29
**Design:** [`experiments/designs/comparative-correlative-v1.md`](../../designs/comparative-correlative-v1.md)
**Conjecture:** [`conjecture/comparative-correlative-construction`](../../../wiki/findings/conjectures/comparative-correlative-construction.md)
**Result page:** [`result/comparative-correlative-covariation-v1`](../../../wiki/findings/results/comparative-correlative-covariation-v1.md)

This is the project's **first probe of its own design to actually run** (charter §5.4 "Run").

## What ran

A read-only behavioral API probe over the ratified panel ([`config/models.md`](../../../config/models.md)):
`anthropic/claude-sonnet-4.6` (A), `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C).

Three arms:
1. **constructed-nli** — NLI framing (entailment/neutral/contradiction → 0/1/2) on the
   80 project-authored items in [`items.csv`](../../data/comparative-correlative/items.csv).
2. **constructed-fc** — forced-choice covariation-direction framing (INCREASE / DECREASE /
   UNDETERMINED) on the same 80 items.
3. **scivetti-nli** — human-comparison arm: the same NLI framing on the **30 real
   Scivetti CC items** (the comparative-correlative subset of CxNLI Exp 1), read in place
   from a local clone of `github.com/melissatorgbi/beyond-memorization` and scored against
   the released per-item gold labels + the aggregate native-speaker baseline (≈0.90).

### Logprobs note (the AANN-blocking issue, handled here)

The ratified panel chat models expose **no token logprobs** on OpenRouter (verified
2026-05-29 against the live model catalog: `logprobs=False` for all three). The CC design
anticipated this and ratified a fallback — temperature=0 greedy completion + string parse —
so this probe runs cleanly without logprobs. (The AANN probe cannot: its ratified indicator
*requires* logprobs. See `NEXT.md` / the queued decision.)

`google/gemini-3.5-flash` requires reasoning to be enabled ("Reasoning is mandatory for this
endpoint and cannot be disabled", HTTP 400 when `reasoning.enabled=false`); we set
`max_tokens=4096` and parse the trailing digit / last keyword. A and B answered with a bare
token at `max_tokens=64`.

## Files

- `build_items.py` — emits the frozen item set. **Run before the probe**; item set lexically
  frozen at commit (charter §8). Scale pairs hand-authored so covariation direction is not
  world-knowledge-obvious (14 typical + 6 atypical pairs × 4 forms = 80 items).
- `probe.py` — the probe runner (3 arms × 3 models). Raw JSON per (arm, slot) under `raw/`.
- `analyze.py` — applies the frozen thresholds T1/T2/T3; emits `raw/results.json`.
- `raw/` — raw model outputs (prompts, responses, parsed predictions, usage). The Scivetti
  items appear here as premise/hypothesis text; this is run output, not a mirror of the
  un-licensed dataset (which is read in place from `/tmp`, never copied into the repo).

## Operationalization (frozen, per the ratified decisions — NOT retuned after results)

- **Instrument:** both (NLI + forced-choice). Forced-choice grounds the direction indicators
  (closest analogue to Weissweiler's semantic-application task); NLI grounds the
  human-comparison arm against Scivetti.
- **T1** CC-vs-control covariation gap ≥ 30 pp (forced-choice). **T2** inverse-CC direction-flip
  rate ≥ 70%. **T3** atypical-pair rate within 15 pp of typical-pair (no collapse).
  A clause is supported only if met in ≥ 2 of 3 panel models.

## Budget

Pre-flight estimate (design §6): < $1. Actual est. (from token usage): see `raw/run_summary.json`
— recorded in [`config/budget.md`](../../../config/budget.md) ledger. Well under the $5 single-run flag.

## Results

See `raw/results.json` and the table printed by `analyze.py`, written up as the typed
result page linked above. Cross-model divergence is itself a finding (charter §6).
