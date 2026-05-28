# models.md — panel selection

Charter §6: three models from **different labs/architecture families** (family decorrelation), recorded with rationale and date, revisited when models change. Do not hardcode slugs anywhere else in the repo — refer to this file.

## Current panel (2026-05-28)

Selected on first run; calibration was a single liveness probe, not a real capability check. Treat as **tentative** until the next loop turn uses them on a real experiment.

| Slot | Model | Family | Why chosen |
|------|-------|--------|------------|
| `panel.A` | `anthropic/claude-sonnet-4.6` | Anthropic | Strong instruction-following baseline; gave the standard CxG-style gloss in the bootstrap probe. |
| `panel.B` | `openai/gpt-5.4-mini` | OpenAI | Different lab; markedly cheaper than `gpt-5.4`; in the bootstrap probe missed the AANN reading — already an instance of the cross-family divergence the project is set up to study. |
| `panel.C` | `google/gemini-3.5-flash` | Google | Different lab again; multimodal-native (useful when `grounded.perceptual` becomes active). Caveat: in the bootstrap probe, reasoning tokens consumed the visible-output budget — handle in code (see §Caveats). |

## Alternates

Held for substitution if a panel slot becomes unsuitable, or for sensitivity checks.

- `deepseek/deepseek-v4-flash` — Chinese training pipeline (different geographic/data composition). Cheap. Same reasoning-token caveat as Gemini.
- `x-ai/grok-4.3` — xAI, different lab; not chosen for the founding panel only because three slots is enough.
- `moonshotai/kimi-k2.6`, `qwen/qwen3.6-flash`, `z-ai/glm-5.1` — further family decorrelation if needed.

## Task → model assignments

Until experience tells us otherwise, default policy:

- **Subject role** (the model whose behavior is the object of study): all three panel slots; cross-model divergence is itself data (charter §6).
- **Critic role** (review of the project's own outputs, prompts, designs): the same three in parallel, with the **cutoff-aware preamble** (charter §6) prepended to every critic call.
- **Coding / planning assistance for the lead agent itself** (this Claude session): the harness model, not the panel; the panel is reserved for *probe* and *critique* calls.

## Caveats from the bootstrap probe

See `experiments/runs/2026-05-28-panel-calibration/`. Carry these into every future probe:

1. **Reasoning-token consumption.** `google/gemini-3.5-flash` and `deepseek/deepseek-v4-flash` produced empty/truncated visible answers under `max_tokens=120`. Mitigation options when building real probes:
   - Set OpenRouter's `reasoning: {"enabled": false}` (or `{"effort": "none"}`) where supported.
   - Otherwise set `max_tokens` ≥ 1024 and budget accordingly.
2. **Inter-model divergence on AANN is already real.** `gpt-5.4-mini` gave the compositional (wrong) reading; the others gave the constructional (right) reading. Don't over-interpret one prompt — but it's a flag for the AANN conjecture.

## Cutoff-aware critic preamble (charter §6)

When the panel acts as critic, prepend something like:

> Today is 2026-05-28. You may encounter references to papers, datasets, or models that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper you do not recognize is not for that reason fabricated. Where you must rely on what you know, label it as such.

Store the canonical wording when it stabilizes; until then, copy-from-here is fine.

## Revision history

- 2026-05-28 — Panel established with single-prompt liveness probe. Recorded as tentative pending real probe-turn use.
