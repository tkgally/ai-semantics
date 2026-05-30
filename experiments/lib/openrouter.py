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
# 2026-05-30 finding: this UNDERCOUNTS real spend ~4.5x, so it is a fallback, not the
# headline. Prefer billed_cost() (sums usage.cost) for the recorded figure.
RATE_CARD = {
    "anthropic/claude-sonnet-4.6": (3.0, 15.0),
    "openai/gpt-5.4-mini": (0.20, 0.60),
    "google/gemini-3.5-flash": (0.15, 0.60),
}


def call(model, system, user, max_tokens=None, temperature=0, retries=4, timeout=120):
    """One chat completion. Returns {content, usage, error}.

    `usage` carries the API-billed `cost` field because the request sets
    `"usage": {"include": true}`. google/* models burn the visible-output budget on
    reasoning tokens under a small cap (see config/models.md caveat), so they default
    to a large max_tokens unless overridden.
    """
    key = os.environ["OPENROUTER_API_KEY"]
    if max_tokens is None:
        max_tokens = 4096 if model.startswith("google/") else 64
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
        "usage": {"include": True},  # <- makes OpenRouter return the billed usage.cost
    }
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
    """
    pin, pout = RATE_CARD[model]
    tin = tout = 0
    for recs in record_lists:
        tin += sum((r.get("usage") or {}).get("prompt_tokens", 0) or 0 for r in recs)
        tout += sum((r.get("usage") or {}).get("completion_tokens", 0) or 0 for r in recs)
    return (tin * pin + tout * pout) / 1_000_000
