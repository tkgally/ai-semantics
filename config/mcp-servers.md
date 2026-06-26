# mcp-servers.md — optional design-time MCP servers

This file documents MCP servers wired into the repo (`.mcp.json`) and, crucially, the
**boundary** on what they may and may not be used for. The boundary is the point: these
servers are **planning aids for the lead agent during design**, never part of an
experiment's execution path and never a source of recorded spend.

## `openrouter` — live model catalog / pricing / benchmarks (added 2026-06-26)

- **Endpoint:** `https://mcp.openrouter.ai/mcp` (HTTP transport).
- **Auth:** the session's `OPENROUTER_API_KEY` is passed as a `Bearer` token (no OAuth /
  browser step is needed — verified 2026-06-26). The blog announcement describes an OAuth
  flow that mints a 7-day, $10-capped key; the plain env key also works and is what
  `.mcp.json` uses, so a headless autonomous session can still reach it. If OpenRouter
  ever stops accepting the raw key, the server simply becomes unavailable — nothing in the
  experiment or budget path depends on it.
- **What it is for (design-time only):** checking *current* model pricing, context
  length, modalities, supported parameters (e.g. whether a model takes `reasoning`),
  per-provider latency/uptime, third-party benchmarks, daily usage rankings, and a
  documentation search — i.e. the questions you ask while *choosing a model and
  sizing a probe*, not while running one. Tools include `models-list`, `model-get`,
  `model-endpoints`, `benchmarks`, `rankings-daily`, `providers-list`, `docs-search`,
  `generation-get`, `credits-get`, and `chat-send` (ad-hoc prompt try-outs).

### Hard boundary — what this server must NOT be used for

1. **No experiments run through it.** Every probe and critique call stays on the existing
   REST harness, [`experiments/lib/openrouter.py`](../experiments/lib/openrouter.py)
   (`call()` / `billed_cost()`), which sets `"usage": {"include": true}` and records the
   API-returned `usage.cost`. The MCP `chat-send` tool returns only the reply plus token
   counts — **not** the billed cost inline (you would need a `generation-get` follow-up) —
   so it cannot produce cost-accounted, reproducible, frozen probe data. It is for
   throwaway prompt testing, nothing that lands in a finding.
2. **No recorded spend comes from it.** The headline cost figure in `config/budget.md` is
   always the harness's summed `usage.cost`. Numbers the MCP server reports (pricing,
   `generation-get` costs) are for *planning and reconciliation only*.
3. **It is informational, not authoritative for freezes.** A design that freezes a price,
   a model slug, or a capability must record the value it froze in the run dir; the live
   MCP catalog can drift between sessions and is not a substitute for a committed,
   checksummed artifact.

### How it earns its keep

The local pre-flight rate card in `experiments/lib/openrouter.py` had drifted 4–15x stale
(found 2026-06-26: gpt and gemini base prices were ~4-15x below the live numbers, the
main reason pre-flight estimates read far under the bill). A one-call `model-endpoints`
check against the live catalog catches that kind of drift before it distorts a budget
plan. Use it that way: confirm prices/params/latency while designing, then run and budget
on the REST harness as before. The same data is also available from the plain REST
`/api/v1/models` and `/endpoints` endpoints if the MCP server is unavailable.

## Disabling / opting out

`.mcp.json` is a project-scoped server: a client is prompted to approve it before it
loads, and it can be declined or removed without affecting anything else — the experiment
and budget paths have no dependency on it. Removing the `openrouter` block from
`.mcp.json` fully opts out.
