"""Bootstrap panel-liveness probe (2026-05-28).

Single one-shot probe per candidate model. Purpose is to confirm the API path
works for each model and to surface per-model gotchas (reasoning tokens,
truncation) before they bite a real experimental probe. NOT an empirical
finding about AANN.

Run: `OPENROUTER_API_KEY=... python3 probe.py`
"""
import json
import os
import time
import urllib.error
import urllib.request

KEY = os.environ["OPENROUTER_API_KEY"]
URL = "https://openrouter.ai/api/v1/chat/completions"

CANDIDATES = [
    "anthropic/claude-sonnet-4.6",
    "openai/gpt-5.4-mini",
    "google/gemini-3.5-flash",
    "deepseek/deepseek-v4-flash",
]

PROMPT = (
    "In one sentence, what does the English construction 'a beautiful three days' "
    "(the AANN construction) typically convey? Be concise."
)

for model in CANDIDATES:
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": PROMPT}],
        "max_tokens": 120,
        "temperature": 0,
    }).encode()
    req = urllib.request.Request(URL, data=body, headers={
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json",
    })
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.load(r)
        dt = time.time() - t0
        content = data["choices"][0]["message"]["content"].strip().replace("\n", " ")
        usage = data.get("usage", {})
        print(f"OK   {model}  {dt:.1f}s  "
              f"in={usage.get('prompt_tokens')}  out={usage.get('completion_tokens')}")
        print(f"     {content[:240]}")
    except urllib.error.HTTPError as e:
        print(f"FAIL {model}  HTTP {e.code}: {e.read().decode()[:200]}")
    except Exception as e:
        print(f"FAIL {model}  {type(e).__name__}: {e}")
