---
id: prompt-caching-repeated-prefix-probes
title: Should the probe harness use OpenRouter prompt caching on repeated-prefix probes to cut input cost, and how is that reconciled with cost accounting and reproducibility?
status: open
opened: 2026-06-26
opened-by: orchestrator
contingent-artifacts:
  - []
---

# Decision: prompt caching on repeated-prefix probes

## Why this exists

Most probes in this project send the **same system prompt** (and often a long shared
instruction/few-shot prefix) across hundreds of calls that differ only in a short item
stem. The live OpenRouter catalog (checked 2026-06-26 via the optional `openrouter`
design-time MCP server — see [`config/mcp-servers.md`](../../../config/mcp-servers.md))
shows that the panel models price a **cached input read** far below a fresh input read:

| Model | prompt (in) $/MT | `input_cache_read` $/MT | implicit caching |
|-------|------------------|--------------------------|------------------|
| `anthropic/claude-sonnet-4.6` | 3.00 | 0.30 | — (explicit `cache_control`) |
| `google/gemini-3.5-flash` | 1.50 | 0.15 | `supports_implicit_caching: true` |
| `openai/gpt-5.4-mini` | 0.75 | 0.07 | implicit |

So the repeated prefix — which is currently re-billed at the full input rate on every
call — is in principle ~10x cheaper to re-read from cache. With the budget regularly
pushing the $5/day cap, that is a real lever worth examining. **But** turning it on
touches two things the project is strict about — cost accounting and reproducibility — so
it is surfaced as a decision rather than silently switched on. Tom's standing instruction
this session was explicit: **keep the experimental harnesses unchanged for now**; this
page records the question and a provisional default, it does not act.

## The live choices

1. **Adopt caching at all, and where.** Options: (a) leave the harness as-is (every call a
   fresh input read — current state, simplest, fully deterministic accounting); (b) enable
   caching only on the demonstrably repeated-prefix, high-call-count probes (e.g. the
   multi-hundred-call lexical / VWSD / AANN runs) where the prefix dominates input
   tokens; (c) enable it globally in `call()`. The prefix has to be genuinely large and
   re-sent for caching to pay — short-system / long-item probes get little.
2. **Explicit vs implicit.** Gemini and gpt cache implicitly (no code change needed — the
   provider may already be giving a partial discount, which would show up in `usage.cost`
   today); Anthropic needs an explicit `cache_control` breakpoint on the prefix. Decide
   whether to add the Anthropic breakpoint, or restrict the lever to the implicit-caching
   models only.
3. **Cost-accounting reconciliation.** `billed_cost()` already sums the API-returned
   `usage.cost`, which *includes* cache-read/-write line items, so the **recorded** figure
   stays correct automatically. The open question is the **pre-flight estimate**: the
   `RATE_CARD` models only prompt/completion, not `input_cache_read` / `input_cache_write`,
   so an estimate would over-count a cached run. Decide whether the estimate needs a
   cache-aware term or whether "estimate is a conservative upper bound" is acceptable.
4. **Reproducibility / validity.** Does serving part of the prompt from cache change model
   outputs versus a cold call? Expectation: no (cache affects billing/latency, not the
   computed logits for a given exact prompt), but this should be **verified on a small
   matched cold-vs-cached pilot** before any finding-bearing run depends on it, because the
   project freezes designs and must not let a cost optimization perturb the measured
   behavior. Cache TTL/eviction also makes realized savings non-deterministic run-to-run —
   acceptable for cost, not for any artifact that must be byte-reproducible.
5. **Magnitude — is it worth the complexity?** On the reasoning-heavy gemini runs that
   actually drive the bill, **output + internal-reasoning tokens** (billed at $9/MT)
   dominate, and caching only touches *input*. So the saving may be modest precisely where
   spend is highest. Decide against a measured estimate of input-token share per probe
   class, not in the abstract.

## Provisional default (in force until a later session ratifies — NOT acted on this session)

**Do not change the harness now.** Keep every probe on the current cold-read path
(`experiments/lib/openrouter.py` unchanged), so accounting and reproducibility stay exactly
as they are. *Before* adopting caching, run a scoped, $0-stakes **pilot** on one
repeated-prefix probe class: a matched cold-vs-cached pair (same frozen items, same seed)
that (a) confirms outputs are identical, and (b) measures the actual `usage.cost` delta
and the input-token share. Adopt caching only on probe classes where the pilot shows a
material, output-neutral saving — option (1b), implicit-caching models first (no code
change beyond reading what the provider already discounts), Anthropic `cache_control`
added only if its measured share justifies the breakpoint. If the pilot shows the saving
is small (the likely gemini case), record that null and leave the harness as-is. The
recorded cost stays `usage.cost`; if caching is adopted, add a cache-aware term to the
pre-flight `RATE_CARD` estimate so it stops over-counting.

## Notes for the resolver

A later session may ratify via the autonomous adversarial-review procedure ([`PROJECT.md`](../../../PROJECT.md)
§12.3) — never the session that opened this. The cheapest first step is just the pilot:
it is $0-budget-stakes (a few dozen calls on already-frozen stimuli) and turns choices
(1), (4) and (5) from speculation into measured numbers. The decision is **not urgent** —
it is a cost optimization, not a correctness gate; no current or planned result depends on
it, and the existing cold-read path is correct and fully reproducible. If the pilot shows
the input-token share is small across the project's actual probe mix, the honest outcome
is to retire this lever rather than carry caching complexity for a marginal gain.
