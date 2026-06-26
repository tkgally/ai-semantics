"""Shared OpenRouter probe helper — records the API's ACTUAL billed cost.

WHY THIS EXISTS (maintenance unit, 2026-05-30)
----------------------------------------------
Every prior `probe.py` estimated cost from a hardcoded local rate card
(prompt_tokens * price + completion_tokens * price). The 2026-05-30 session found
that estimate UNDERCOUNTS the real OpenRouter bill by ~4.5x (the local card omits
reasoning tokens, cache/byok adjustments, and upstream-cost differences). OpenRouter
returns the true billed cost per call in `usage.cost` — but ONLY if the request body
carries `"usage": {"include": true}`. This module bakes that flag in and sums the
returned `usage.cost`, so future runs record ACTUAL spend, not an estimate.

See config/budget.md ("After each probe") and NEXT.md (the queued fix this closes).

USAGE (import from a dated run dir)
-----------------------------------
    import os, sys
    sys.path.insert(0, os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", "..", "lib")))
    from openrouter import PANEL, call, billed_cost

    r = call(PANEL["A"], system, user)        # r["content"], r["usage"], r["error"]
    cost = billed_cost([list_of_records])      # sums the API-returned usage.cost

PANEL slugs mirror config/models.md (the single source of truth — do not edit here
without editing that file; this is a convenience copy for runnable code).
"""
import json
import os
import time
import urllib.error
import urllib.request

URL = "https://openrouter.ai/api/v1/chat/completions"

# Mirror of config/models.md "Current panel (2026-05-28)". config/models.md is the
# source of truth; keep these in sync by hand when the panel changes.
PANEL = {
    "A": "anthropic/claude-sonnet-4.6",
    "B": "openai/gpt-5.4-mini",
    "C": "google/gemini-3.5-flash",
}

# Local rate card (USD per 1M tokens, prompt/completion) — kept ONLY as a fallback
# estimate when usage.cost is absent (e.g. a provider that does not report cost). The
# 2026-05-30 finding: a naive token-estimate UNDERCOUNTS real spend, so this is a
# fallback, not the headline. Prefer billed_cost() (sums usage.cost) for the recorded
# figure.
#
# CORRECTION 2026-06-26: the prior numbers (gpt 0.20/0.60, gemini 0.15/0.60) were
# stale by ~4-15x against OpenRouter's live catalog and were a large part of why the
# pre-flight estimate read so far below the bill (gemini in particular billed ~14.5x its
# old estimate; see config/budget.md). Verified against the live OpenRouter endpoints
# this date (catalog reachable via the optional `openrouter` design-time MCP server, or
# the plain REST /api/v1/models endpoint — see config/mcp-servers.md). The headline
# recorded cost is STILL the API-returned usage.cost via billed_cost(); these numbers
# only sharpen the *pre-flight estimate*. Note the estimate remains a lower bound for
# reasoning-heavy gemini runs: gemini bills internal-reasoning tokens at the COMPLETION
# rate ($9/MT) and they are not separately modelled here — keep `reasoning` suppressed
# or capped on large gemini runs and budget against the billed expectation.
RATE_CARD = {
    "anthropic/claude-sonnet-4.6": (3.0, 15.0),   # unchanged — was already accurate
    "openai/gpt-5.4-mini": (0.75, 4.50),          # was (0.20, 0.60) — ~4x/7x too low
    "google/gemini-3.5-flash": (1.50, 9.00),      # was (0.15, 0.60) — ~10x/15x too low
}

# Cached-input-read price (USD per 1M tokens) — the rate billed for the portion of the
# prompt served from a cache hit, ~10x below the full prompt rate. Added 2026-06-26 after
# the prompt-caching pilot (decision: prompt-caching-repeated-prefix-probes, ratified s114;
# run experiments/runs/2026-06-26-prompt-caching-pilot/). estimated_cost() reads
# usage.prompt_tokens_details.cached_tokens and charges those tokens at this rate instead
# of the full prompt rate, so the pre-flight ESTIMATE stops over-counting a cached run.
# The recorded headline figure is still billed_cost() (sums usage.cost) — unchanged. Values
# from the live OpenRouter catalog (2026-06-26), corroborated by the pilot's measured
# warm-read costs (gpt -82.7%, gemini/claude via explicit cache_control -82.7%/-91.4%).
CACHE_READ = {
    "anthropic/claude-sonnet-4.6": 0.30,
    "openai/gpt-5.4-mini": 0.07,
    "google/gemini-3.5-flash": 0.15,
}


def call(model, system, user, max_tokens=None, temperature=0, retries=4, timeout=120,
         images=None, reasoning=None, cache_prefix=False):
    """One chat completion. Returns {content, usage, error}.

    `usage` carries the API-billed `cost` field because the request sets
    `"usage": {"include": true}`. google/* models burn the visible-output budget on
    reasoning tokens under a small cap (see config/models.md caveat), so they default
    to a large max_tokens unless overridden.

    REASONING (optional, added 2026-05-31 for the relational reference-game probe — the
    most call-heavy probe to date, where Gemini reasoning tokens are the dominant cost
    driver per the budget ledger). Pass `reasoning=` to forward OpenRouter's `reasoning`
    control verbatim, e.g. `reasoning={"enabled": False}` or `{"effort": "none"}` to
    suppress reasoning tokens on tasks that do not need them (short labels / single-token
    picks). When `reasoning is None` the field is omitted and behaviour is byte-identical
    to before, so existing probes are unaffected.

    MULTIMODAL (image input). Pass `images=` to attach images to the user turn — all
    three current panel families accept image input (verified 2026-05-30 against the
    OpenRouter /models catalog: anthropic/claude-sonnet-4.6, openai/gpt-5.4-mini,
    google/gemini-3.5-flash all list `image` in input_modalities; gemini also lists
    audio+video). `images` is a list, each element either a URL string
    ("https://…" or a "data:image/png;base64,…" data URI) or a dict
    {"url": "...", "detail": "low|high|auto"}. When `images` is None the user turn is
    sent as a plain string (text-only, unchanged from prior behaviour), so existing
    text probes are byte-for-byte identical. When images are present the user turn is
    built as the OpenAI/OpenRouter multimodal content array
    ([{type:text,...}, {type:image_url, image_url:{url:...}}, ...]).

    PROMPT CACHING (cache_prefix, optional, added 2026-06-26 after the caching pilot —
    decision: prompt-caching-repeated-prefix-probes, ratified s114). Default False, in
    which case the request body is byte-identical to before (the system turn is sent as a
    plain string), so EVERY existing probe is unaffected and every frozen design's
    execution path is unchanged. When True, the system turn is wrapped as a single
    cache_control breakpoint block — [{"type": "text", "text": system,
    "cache_control": {"type": "ephemeral"}}] — marking the (typically large, repeated)
    system prefix for caching. The pilot measured this as OUTPUT-NEUTRAL (byte-identical
    answers cold vs cached on the panel) and a material input saving on repeated-prefix,
    high-call-count probes: a warm read costs ~17% of a cold read on claude/gemini and gpt.
    NOTES: (a) gpt caches the repeated prefix IMPLICITLY with no flag, so cache_prefix is
    only needed for anthropic and google (the pilot found google's *implicit* caching does
    NOT fire via OpenRouter's route — google needs this explicit breakpoint, like
    anthropic). (b) Caching touches INPUT only; on reasoning-heavy google runs (reasoning
    is now mandatory on gemini-3.5-flash and bills at the completion rate) the realized
    saving on TOTAL cost shrinks because output+reasoning dominate. (c) The first call pays
    a one-off cache-write premium (~1.25x input on anthropic), so caching pays off only
    when the same prefix is re-sent many times within the cache TTL — i.e. exactly the
    high-call-count probe case. (d) Adopt per-probe; the recorded cost stays usage.cost
    (already cache-aware); estimated_cost() now discounts cached_tokens too.
    """
    key = os.environ["OPENROUTER_API_KEY"]
    if max_tokens is None:
        max_tokens = 4096 if model.startswith("google/") else 64
    if images:
        user_content = [{"type": "text", "text": user}]
        for im in images:
            if isinstance(im, str):
                user_content.append({"type": "image_url", "image_url": {"url": im}})
            else:  # dict with at least "url", optionally "detail"
                iu = {"url": im["url"]}
                if im.get("detail"):
                    iu["detail"] = im["detail"]
                user_content.append({"type": "image_url", "image_url": iu})
    else:
        user_content = user
    # cache_prefix wraps the (repeated) system prefix in a cache_control breakpoint.
    # Default False => plain string, byte-identical to the historical request body.
    if cache_prefix:
        system_content = [{"type": "text", "text": system,
                           "cache_control": {"type": "ephemeral"}}]
    else:
        system_content = system
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
        "usage": {"include": True},  # <- makes OpenRouter return the billed usage.cost
    }
    if reasoning is not None:
        body["reasoning"] = reasoning
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                URL,
                data=json.dumps(body).encode(),
                headers={"Authorization": f"Bearer {key}",
                         "Content-Type": "application/json"},
            )
            with urllib.request.urlopen(req, timeout=timeout) as r:
                d = json.load(r)
            msg = d["choices"][0]["message"]
            return {"content": (msg.get("content") or "").strip(),
                    "usage": d.get("usage", {})}
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read().decode()[:150]}"
        except Exception as e:  # noqa: BLE001
            last = f"{type(e).__name__}: {e}"
        time.sleep(2 ** attempt)
    return {"content": None, "usage": {}, "error": last}


def billed_cost(record_lists):
    """ACTUAL billed USD: sum the API-returned usage.cost across record lists.

    Each element of `record_lists` is a list of records that each carry a `usage`
    dict (as written by a probe's run loop). Returns (total_usd, n_with_cost,
    n_missing_cost) so the caller can tell whether any call lacked a reported cost.
    """
    total = 0.0
    have = missing = 0
    for recs in record_lists:
        for r in recs:
            u = r.get("usage") or {}
            c = u.get("cost")
            if c is None:
                missing += 1
            else:
                total += c
                have += 1
    return total, have, missing


def estimated_cost(record_lists, model):
    """Fallback rate-card ESTIMATE (use only when billed_cost reports missing costs).

    Documented to UNDERCOUNT real spend ~4.5x (2026-05-30). Kept for parity with the
    historical ledger rows, not as the headline figure.

    CACHE-AWARE (2026-06-26, caching-pilot precondition): tokens reported as served from
    cache (usage.prompt_tokens_details.cached_tokens) are charged at the CACHE_READ rate
    instead of the full prompt rate, so a cached run is no longer over-ESTIMATED. When no
    cached_tokens are reported (the default, every cold run) the arithmetic is identical to
    before: cached=0 => all prompt tokens at the full prompt rate.
    """
    pin, pout = RATE_CARD[model]
    cread = CACHE_READ.get(model, pin)
    tin_full = tin_cached = tout = 0
    for recs in record_lists:
        for r in recs:
            u = r.get("usage") or {}
            pt = u.get("prompt_tokens", 0) or 0
            cached = ((u.get("prompt_tokens_details") or {}).get("cached_tokens", 0)) or 0
            cached = min(cached, pt)
            tin_full += pt - cached
            tin_cached += cached
            tout += (u.get("completion_tokens", 0) or 0)
    return (tin_full * pin + tin_cached * cread + tout * pout) / 1_000_000
