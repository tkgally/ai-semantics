# 2026-05-28 — panel calibration probe

## Purpose

Bootstrap check: confirm each candidate panel model responds via OpenRouter, and surface any per-model gotchas (rate limits, hidden reasoning tokens, output truncation) before they bite a real probe.

## Setup

- OpenRouter API; `temperature=0`, `max_tokens=120`.
- Single one-shot user message asking what the AANN construction (*a beautiful three days*) conveys, in one sentence.
- Candidates: `anthropic/claude-sonnet-4.6`, `openai/gpt-5.4-mini`, `google/gemini-3.5-flash`, `deepseek/deepseek-v4-flash`.

Code: `probe.py`. Raw output: `probe-output.txt`.

## Results

| Model | Latency | Out tokens | Visible answer |
|-------|--------:|-----------:|----------------|
| `anthropic/claude-sonnet-4.6` | 2.2s | 46 | "evaluative or exclamative assessment of a quantity or period, treating it as a unified, bounded whole" — substantively right |
| `openai/gpt-5.4-mini` | 0.7s | 18 | "each of the three days was beautiful" — substantively **wrong** (compositional reading, not the constructional meaning) |
| `google/gemini-3.5-flash` | 1.6s | 116 | truncated to "The construction typically conveys that" — visible answer was empty even though 116 tokens were billed |
| `deepseek/deepseek-v4-flash` | 4.9s | 120 | truncated to "a unified, collective experience or period, treating the…" — also looks like reasoning-token consumption |

## Findings

1. **Gemini 3.5 Flash and DeepSeek V4 Flash are consuming the `max_tokens` budget on hidden reasoning tokens.** Visible message content is short or empty while billed completion tokens are at the cap. Lesson for later probes: either set `reasoning: {effort: "none"}` (or the OpenRouter-equivalent extra_body parameter) for these models, or set `max_tokens` substantially higher (≥1024) when reasoning is enabled. See [OpenRouter reasoning docs] for the correct toggle per model.
2. **GPT-5.4-mini got the AANN reading wrong** on a one-shot single-sentence prompt. This is the only model out of four to miss the constructional meaning. Treat this as a single data point — not a verdict on the model — but it is **already** an instance of the kind of inter-model semantic divergence the project is built to study, and it slots cleanly into `findings/conjectures/aann-construction.md`.
3. **Claude Sonnet 4.6 and DeepSeek V4 Flash agreed on the unification-of-period gloss**, the standard CxG description. The convergence is QA, not validation — but the divergence (GPT-mini) is the informative signal here (charter §2.7, §6).

## Not done here

- This is a single one-shot probe per model. No minimal pairs. No surprisal. No human anchor checked. It is **not** an empirical finding about AANN — it is a panel-liveness check that happened to surface a divergence.
- No retries, no API error handling beyond a basic try/except.

## Next visit

When the AANN conjecture (`findings/conjectures/aann-construction.md`) becomes the active experiment, lift this probe into a real design with:

- Held-out adjectives.
- Licit / illicit minimal pairs.
- The Weissweiler stimulus list as the human anchor (`base/resources/`).
- Reasoning-token mitigation for Gemini and DeepSeek.
