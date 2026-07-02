# models.md — panel selection

Charter §6: three models from **different labs/architecture families** (family decorrelation), recorded with rationale and date, revisited when models change. Do not hardcode slugs anywhere else in the repo — refer to this file.

## Current panel (2026-05-28; truth-up 2026-07-02)

Selected on first run with a single liveness probe. **No longer tentative:** this panel has
carried every probe since 2026-05-28 — ~75 completed studies (experiments and analyses) across
five weeks — and is battle-tested on forced-choice, NLI, elicitation, and multimodal
instruments. Recorded 2026-07-02 per this file's own "revisit when models change" promise
(program item A4a); the open scale/refresh questions are queued as decisions, not drifted into
(see §Queued panel decisions below).

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
- **Critic role** (review of the project's own outputs, prompts, designs): the same three in parallel, with the **cutoff-aware preamble** (charter §6) prepended to every critic call. **Decorrelation rule (2026-07-02, `PROTOCOL.md §2`):** each adversarial ratification and each pre-run critique routes one vote through a **non-Anthropic** slot (`panel.B` or `panel.C`) — QA input to the fresh-agent reviewer, who keeps verdict authority.
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

## Queued panel decisions (2026-07-02 — ALL THREE RATIFIED s168)

Three subject/instrument questions were queued with the program adoption and **all three were
ratified 2026-07-02 (session 168), autonomous cross-session adversarial review** (each with one
non-Anthropic panel vote). All three adopted their provisional default (Option A), each with a
binding condition. No probe may presuppose the unrun items; the ladder/logprob lanes are
*unblocked, not yet built*.

- `scale-ladder-subjects` — **RESOLVED s168: ADOPT A with condition.** Within-family capability
  siblings may be added as *supplementary* subjects on byte-identical frozen instruments, written
  as `ladder`-flagged rows, never merged into panel-v1 verdicts. **Condition:** A4b's first sub-step
  must add a mechanical `ladder: true` front-matter field + a senselint check forbidding
  ladder→panel-v1 `supports`/`anchors` links — no ladder result page before that gate lands.
  ([`decisions/resolved/scale-ladder-subjects`](../wiki/decisions/resolved/scale-ladder-subjects.md))
- `panel-v2-refresh` — **RESOLVED s168: ADOPT A as a sequenced hold.** Panel-v1 stays primary for
  **all** lines; the v2 question is decided on evidence once ladder data lands. **⚠ RE-OPEN TRIGGER
  (binding safeguard, recorded here per the ratification):** this decision **re-opens** (then
  decided B-vs-C on evidence) the moment **ladder data lands OR `scale-ladder-subjects` is
  rejected**. Until then panel-v1 is the sole default; do not let this hold harden into indefinite
  v1. The non-Anthropic vote dissented toward "refresh now (B)"; the fresh reviewer weighed and
  rebutted it (v1 not yet stale; the ladder is the cheapest sensitivity test).
  ([`decisions/resolved/panel-v2-refresh`](../wiki/decisions/resolved/panel-v2-refresh.md))
- `logprob-supplementary-lane` — **RESOLVED s168: ADOPT A (re-verify, then pilot) with condition.**
  A $0 live re-check of which OpenRouter models expose logprobs — **recorded here with its date** —
  must precede any pilot; then (only if ≥2 decorrelated families survive) one flagged supplementary
  pilot on an already-frozen battery. **Condition:** every logprob-lane result carries a mechanical
  `logprob-lane: true` / `verdict-bearing: false` / `decorrelation: n-families=k` front-matter
  contract (senselint-enforced, never sole support); the lane may never reach for echo/prompt-logprob
  surprisal (the retired AANN Option-A ruling stays intact).
  ([`decisions/resolved/logprob-supplementary-lane`](../wiki/decisions/resolved/logprob-supplementary-lane.md))

> **Live logprob re-verification ledger (logprob-lane Step 1).** *Not yet run* — the first session
> that takes up A4d records the date and per-model logprob availability here before any pilot call.

## Revision history

- 2026-05-28 — Panel established with single-prompt liveness probe. Recorded as tentative pending real probe-turn use.
- 2026-07-02 — Truth-up (program item A4a): panel recorded as battle-tested (~75 completed studies since 2026-05-28); "tentative" dropped. Critic-decorrelation rule added (one non-Anthropic vote per ratification/pre-run critique, `PROTOCOL.md §2`). Three panel/instrument decisions queued (§Queued panel decisions). Panel composition itself **unchanged**.
- 2026-07-02 (session 168) — All three queued panel decisions **ratified** (autonomous cross-session adversarial review, each with a non-Anthropic panel vote): scale-ladder ADOPT-A (mechanical `ladder` flag owed as A4b's first sub-step); panel-v2 ADOPT-A as a sequenced hold with a binding **re-open trigger** (ladder data OR ladder-rejection; see §Queued panel decisions); logprob-lane ADOPT-A (re-verify-then-pilot, mechanical `verdict-bearing:false` contract owed). Panel composition itself **still unchanged**.
