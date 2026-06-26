# Prompt-caching pilot — results (session 115, 2026-06-26 UTC)

Authorized by [`decisions/resolved/prompt-caching-repeated-prefix-probes`](../../../wiki/decisions/resolved/prompt-caching-repeated-prefix-probes.md)
(opened s113, ratified s114 = ADOPT DEFAULT: gate caching behind a `$0`-stakes matched
cold-vs-cached pilot that confirms byte-identical outputs and measures the real saving;
implicit-caching models first; Anthropic `cache_control` only if its measured share
justifies it; if the saving is small (the expected gemini case) record the null and retire).

**This run is the pilot.** It is a tooling/cost measurement, not a meaning finding — no
wiki `result/` page; the loop is closed in the decision page (a "Pilot result" addendum)
and `NEXT.md`.

## Design

One repeated-prefix probe class: a ~6.4k-token shared system prefix (a lexical
usage-relatedness annotation instruction + 120 reference examples) followed by a short item
stem — the shape of the project's high-call-count single-token-output probes (lexical
ratings, AANN FC/NLI, VWSD picks). For each model, the same prefix was sent twice (cold,
then warm within the cache TTL); outputs and `usage.cost` were compared. `temperature=0`.

- **gpt-5.4-mini** — implicit caching (no request change).
- **gemini-3.5-flash** — implicit caching tested first; then explicit `cache_control`.
- **claude-sonnet-4.6** — explicit `cache_control` breakpoint on the system block
  (Anthropic has no implicit caching).

Scripts: `explore_usage.py` (first gpt cold/warm dump), `pilot.py` (3-model loop; timed out
mid-claude — the key numbers were already printed), `diag_gemini.py` (why gemini errored),
`gemini_cache.py` (gemini implicit), `gemini_explicit.py` (gemini explicit). Raw usage:
`gemini_raw.json`, `gemini_explicit_raw.json` (live-written); `gpt_claude_raw.json`
(transcribed from stdout — `pilot.py` writes `raw.json` only at end/abort and the run timed
out mid-claude, so the gpt/claude usage objects printed to the transcript are committed
here for parity; all numbers reconcile, coherence pass).

## What OpenRouter reports

`usage.prompt_tokens_details.cached_tokens` (and `cache_write_tokens`) and a `cost_details`
breakdown are returned per call when `"usage": {"include": true}` is set (the harness
already sets it). `billed_cost()` sums `usage.cost`, which is **already net of the cache
discount** — so the recorded headline figure was always correct; caching changes only the
size of that figure, never how it is read.

## Results — all outputs byte-identical cold vs cached (output-neutral)

| Model | mechanism | no-cache `usage.cost` | cached `usage.cost` | saving | cached / prompt tokens |
|-------|-----------|-----------------------|---------------------|--------|------------------------|
| gpt-5.4-mini | **implicit** (automatic) | $0.00480675 | $0.00083235 | **−82.7%** | 5888 / 6379 (92%) |
| gemini-3.5-flash | implicit → **did NOT fire** | $0.0066315 | $0.0066315 (cached=0) | **0%** | 0 / 4415 (0%) |
| gemini-3.5-flash | **explicit `cache_control`** | $0.0066315 | $0.00114915 | **−82.7%** | 4061 / 4415 (92%) |
| claude-sonnet-4.6 | **explicit `cache_control`** | write call $0.0271455 | read call $0.00234 | **−91.4%** on reads | 7190 / 7226 (99%) |

Byte-identical answers were observed on every cold/warm pair (gpt items → `1`/`2`/`4`;
gemini → `1`; claude → `1`), confirming the caching is output-neutral, as the decision
required.

## Two findings that overturn the decision's stated assumptions

1. **Gemini implicit caching does NOT fire via OpenRouter's route.** Despite the live
   catalog flag `supports_implicit_caching: true`, three back-to-back identical-prefix
   gemini calls all reported `cached_tokens: 0` and a flat cost. Gemini realizes the saving
   **only with an explicit `cache_control` breakpoint** — i.e. it behaves like claude, not
   like gpt, for capture purposes. (gpt's implicit caching fired automatically, so the
   project may *already* be getting an un-noticed gpt discount on calls 2..N within TTL of
   any high-call-count run.)

2. **The saving is material (~83–91%), not the "small null" the decision half-expected —
   on input-dominated probes.** The decision anticipated a small gemini saving because
   "output+reasoning at $9/MT dominate." That holds **only for reasoning-heavy runs**. On
   the project's many *single-token-output, large-prefix, high-call-count* probes the input
   is ~99% of the bill, so caching the repeated prefix cuts ~83–91% of per-call cost after
   the first call.

   Caveat preserved: caching touches **input only**, and **reasoning is now mandatory on
   gemini-3.5-flash** — `reasoning:{enabled:false}` and `{effort:none}` are both rejected
   with HTTP 400 *"Reasoning is mandatory for this endpoint and cannot be disabled"*; only
   `{effort:minimal}` is accepted, and even a one-integer answer can burn ~224
   reasoning/completion tokens (~47% of that call's bill) when reasoning is left at default.
   So on reasoning-heavy gemini runs the realized saving on *total* cost shrinks toward the
   decision's expectation; on minimal-reasoning single-token probes it is large.

## Break-even (claude explicit caching)

The first call pays a one-off cache-write premium (claude write tokens billed ~1.25× the
input rate: the cold-write call cost $0.0271 vs ~$0.0217 for a hypothetical uncached call),
and each subsequent warm read is ~$0.00234. Break-even is ≈ 2 calls; on a several-hundred-
call run the amortized claude input saving approaches ~89%. So caching pays off precisely on
the high-call-count repeated-prefix probes the decision named, and is a net loss only on a
prefix sent once or twice.

## Action taken (this session) — enabling capability only, default-OFF

Per the resolution ("adopt only on probe classes where the pilot shows a material,
output-neutral saving … if caching is adopted, add a cache-aware term to the RATE_CARD
pre-flight estimate"), the pilot's material output-neutral saving authorizes the lever.
Changes to [`experiments/lib/openrouter.py`](../../lib/openrouter.py), both **byte-identical
to the prior behaviour when unused** (verified: `verify_harness.py`):

1. `call(..., cache_prefix=False)` — new opt-in param. When `False` (default) the request
   body is byte-identical to before (system turn = plain string), so **every existing probe
   and every frozen design's execution path is unchanged**. When `True`, the system turn is
   wrapped in a single `cache_control: {type: ephemeral}` block (works for anthropic and
   google; gpt caches implicitly without it).
2. `CACHE_READ` rate card + cache-aware `estimated_cost()` — cached tokens
   (`usage.prompt_tokens_details.cached_tokens`) are charged at the cache-read rate, so the
   pre-flight ESTIMATE stops over-counting a cached run. With `cached=0` (every cold run)
   the arithmetic is identical to before.

Adoption is **per-probe** (a probe author passes `cache_prefix=True` and, for gpt, relies on
implicit caching); no existing probe was changed and nothing was re-run.

## Spend

| Calls | Billed (`usage.cost`) |
|-------|------------------------|
| gpt (explore cold/warm + pilot ×6 warm) | $0.010741 |
| claude (cache write + read) | $0.029485 |
| gemini (diag ×1 + implicit ×3 + explicit ×2) | $0.026521 |
| gemini implicit-disable attempts (HTTP 400, no charge) | $0 |
| **Total** | **≈ $0.066747** |

Under the $2.50 single-run flag; UTC-day 2026-06-26 total ≈ $3.900 of $5.00.
