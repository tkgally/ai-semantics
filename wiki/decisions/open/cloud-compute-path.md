---
id: cloud-compute-path
title: Is there a cloud-hosted path to per-token surprisal / hidden states within $20/week, and do we open it?
status: open
opened: 2026-05-31
opened-by: orchestrator
contingent-artifacts:
  - decisions/open/aann-panel-logprob-blocker
---

# Decision: cloud-compute path for the logprob/representation-blocked work

## Why this exists (feasibility scoping → a real path opened — surfaced, not self-resolved)

Tom asked (decision 5) whether cloud-hosted platforms could run the experiments OpenRouter can't:
(i) per-token surprisal of a **provided** string (the AANN "Option-A" blocker —
[`decisions/open/aann-panel-logprob-blocker`](aann-panel-logprob-blocker.md)) and (ii) model-internal
representations (the deferred small-model representation lanes, lexical + grammatical). The scoping
unit ran ([`experiments/notes/cloud-compute-feasibility.md`](../../../experiments/notes/cloud-compute-feasibility.md))
and found a **real, in-budget path** — cheaper than the blocker assumed. That is a direction-setting
choice (new provider, new API key, new spend surface), so it is surfaced here, not auto-taken.

## Finding (verified where stated; see the note for the full per-platform table)

- **CAP-1 (provided-string surprisal) — YES via Together AI `/v1/completions` with
  `echo=true, logprobs=1`**, which returns per-token logprobs over the echoed prompt on a small open
  model for **<$1/probe**. Host reachable from this sandbox; an unauthenticated call returned HTTP 401
  "Missing API key" (not a parameter rejection) — the **only missing piece is one API key**. Fireworks
  exposes the same `/completions` echo+logprobs shape. (OpenRouter re-confirmed **NO**; HF legacy
  serverless host **blocked** from this sandbox.)
- **CAP-2 (hidden states) — YES only via a local `transformers` run** (`output_hidden_states=True`) on
  an HF Endpoint (T4 ≈ $0.50/hr, per-minute, no scale-to-zero) / Modal / Colab-Kaggle. No serverless
  chat API exposes hidden states. CAP-2 also has **no ratified design yet**.
- **Operational gate:** this sandbox has no GPU/torch and only `OPENROUTER_API_KEY`. So **no** option
  is end-to-end drivable by the agent today without Tom provisioning a key; Colab is strictly
  human-driven out-of-band.

## Options

- **A (provisional default) — open CAP-1 only via Together `echo+logprobs`.** Tom adds
  `TOGETHER_API_KEY` to the environment; a future session runs the **ratified AANN Option-A
  surprisal** on one small open model (<$1). Smallest/cheapest/most reversible; converts the standing
  AANN blocker into a one-key task. **Caveat:** single open model, **not** the decorrelated 3-family
  panel → flag as no cross-family signal; the result anchors to the Mahowald AANN stimuli, behaviour
  on one model.
- **B — open CAP-1 + CAP-2 via an HF Endpoint or Modal.** Unblocks AANN *and* the representation
  lanes, but more setup, no scale-to-zero, and CAP-2 needs a fresh ratified design first.
- **C — keep both deferred (status quo).** Zero new surface/spend; AANN stays on hold (Tom's decision
  6 keeps AANN on hold regardless until a compute path exists — this decision is precisely about
  whether to *create* that path).

## Provisional default

**Option A**, but **blocked on Tom**: it needs a `TOGETHER_API_KEY` (or Fireworks) that the agent
cannot provision. Until then, AANN stays on hold per decision 6. No spend or key is assumed. Tom: if
you want the AANN Option-A path opened, add a Together/Fireworks key and say "A"; else "hold."

**Unverified (confirm on first real use):** Fireworks pricing; that a *named 2026 Together model*
returns `prompt.token_logprobs` (reachability proven, returned-field contents not); Together free-tier
credits; Modal/Replicate GPU rates.

## Update 2026-05-31 (reaffirmed)

Tom reviewed this after the PR #32 consolidation merge and chose **HOLD** again — no `TOGETHER_API_KEY` / Fireworks key added; the AANN Option-A surprisal path stays blocked. This decision stays **open** (revisit if/when a key is provisioned).
