---
id: prompt-caching-repeated-prefix-probes
title: Should the probe harness use OpenRouter prompt caching on repeated-prefix probes to cut input cost, and how is that reconciled with cost accounting and reproducibility?
status: resolved
opened: 2026-06-26
opened-by: orchestrator (session 113, Tom-directed tooling pass)
resolved: 2026-06-26
resolved-by: autonomous (adversarial review)
resolution: "ADOPT THE DEFAULT unchanged (session 114, independent fresh-agent adversarial review; opened s113, ratified s114, cross-session boundary held). The probe harness stays on the cold-read path; experiments/lib/openrouter.py is UNCHANGED. Caching is gated behind a $0-stakes matched cold-vs-cached pilot on one repeated-prefix probe class that must (a) confirm byte-identical outputs for the same frozen items/seed and (b) measure the actual usage.cost delta and input-token share; adopt only on probe classes where the pilot shows a material, output-neutral saving — implicit-caching models (gemini, gpt) first, Anthropic cache_control breakpoint only if its measured share justifies it; if the saving is small (the expected gemini case, where output+reasoning at $9/MT dominate), record the null and retire the lever; if caching is adopted, add a cache-aware input_cache_read/input_cache_write term to the RATE_CARD pre-flight estimate so it stops over-counting cached runs. Code-checked against openrouter.py: billed_cost() sums the API-returned usage.cost (cache line items already folded in → recorded figure stays correct automatically); RATE_CARD/estimated_cost() model only (prompt, completion), so a cached run would be over-ESTIMATED until the term is added. Yardstick fixed (the recorded-cost rule = sum usage.cost, and the cold-read reproducibility guarantee), never any result — no current or planned result depends on this decision."
provisional-default: "[RATIFIED — see resolution above and the Ratification section below.] Leave the harness unchanged now; before adopting caching run a $0-stakes matched cold-vs-cached pilot on one repeated-prefix probe class; adopt only where it shows a material, output-neutral saving (implicit-caching models first); if the saving is small, record the null and leave the harness as-is."
contingent-artifacts: []
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

## Ratification (session 114, 2026-06-26 — autonomous adversarial review)

An independent fresh-agent adversarial-review pass (it did no downstream work this session) read this
page, its options, the provisional default, and the relevant harness code, and returned **VERDICT: ADOPT
THE DEFAULT as written** — the option that strictly dominates on the project's own stated priorities. The
cross-session boundary held (opened session 113, ratified session 114).

**Why the default dominates.** It changes nothing in the frozen execution path now, so cost-accounting
correctness and byte-reproducibility are preserved by construction — there is nothing to perturb until a
pilot has measured the effect. It gates adoption behind an empirical, $0-stakes measurement rather than an
abstract assumption (the same operationalization discipline the project enforces elsewhere: measure first,
then decide, and write the null if the lever is marginal). And it correctly names the one accounting gap
adoption would open — the `RATE_CARD` pre-flight estimate over-counting a cached run — and queues the fix as
a precondition of adoption rather than leaving it implicit. A more aggressive option (global enablement in
`call()`) was rejected: it would add cache-TTL/eviction non-determinism to the realized-cost path with no
measured payoff; and keeping the decision open was rejected because the page is complete (clear options, a
defensible default, a named precondition, and a correct account of the accounting/reproducibility
implications).

**Code-check (verified against [`experiments/lib/openrouter.py`](../../../experiments/lib/openrouter.py)).**
Both load-bearing factual claims on this page check out:

- *Recorded cost stays correct automatically* — **VERIFIED.** `call()` sets `"usage": {"include": True}`
  so OpenRouter returns the billed `usage.cost`; `billed_cost()` simply sums that returned figure
  (`c = u.get("cost")`, `total += c`) with no rate-card arithmetic, so any cache-read/-write line items the
  provider applies are already folded into the recorded total.
- *Pre-flight estimate would over-count a cached run* — **VERIFIED.** `RATE_CARD` stores only a
  `(prompt, completion)` price tuple per model and `estimated_cost()` charges every input token at the full
  prompt rate with no discounted cache-read path, so a run that served part of its prefix from cache (billed
  far below the prompt rate) would be *estimated* higher than *billed*. (Orthogonal to the docstring's note
  that the estimate generally *under*-counts by omitting reasoning tokens — that is a completion-side gap.)
  The page's magnitude analysis (choice 5) is corroborated by `RATE_CARD`'s gemini completion price
  ($9/MT): caching touches only input, while output+reasoning drive the gemini bill, so the honest expected
  pilot outcome is a small saving precisely where spend is highest.

**Anti-cheat: PASS.** The verdict is not result-motivated — no current or planned result depends on this
decision (it is a cost optimization, not a correctness gate), and adopting the default *strengthens* rather
than weakens cost-accounting correctness (recorded cost stays `usage.cost`) and design reproducibility (the
frozen cold-read path is untouched until a pilot proves output-neutrality).

**Contingent artifacts: none** (`contingent-artifacts: []`) — nothing to promote or retire. The pilot this
decision authorizes is new optional follow-on work (carried as a low-priority [`NEXT.md`](../../../NEXT.md) backlog item), not a
contingent page awaiting promotion. The harnesses remain UNCHANGED, exactly as Tom directed when the
decision was opened.
