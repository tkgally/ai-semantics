"""Prompt-caching pilot (decision: prompt-caching-repeated-prefix-probes, ratified s114).
Matched cold-vs-warm on one repeated-prefix probe class. Measures (a) byte-identical
outputs, (b) usage.cost delta + cached-token share, per model.
  - gpt, gemini: IMPLICIT caching (no request change; same prefix re-sent within TTL).
  - claude: EXPLICIT cache_control breakpoint on the system prefix (Anthropic has no
    implicit caching). This is the key un-captured lever (claude input 3.00 -> 0.30 $/MT).
$0-stakes: ~3 items x 2 reads x 3 models = ~18 calls on a large synthetic prefix.
Hard abort guard at $0.40 cumulative billed.
"""
import json, os, sys, time
import urllib.request, urllib.error
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, billed_cost

URL = "https://openrouter.ai/api/v1/chat/completions"
ABORT_USD = 0.40

# Large shared prefix (>~6k tokens) — the repeated-prefix shape of a high-call-count probe.
filler = "\n".join(
    f"- Example {i}: the word 'bank' in context {i} relates to sense A at level "
    f"{(i % 4)} on a 0-3 scale; consider co-occurrence, selectional restrictions, and "
    f"typical referential targets when you judge graded usage-relatedness." for i in range(120))
SYSTEM = (
    "You are a careful lexical-semantics annotator. You rate the graded usage-relatedness "
    "of two uses of the same word form on a 4-point scale (1=unrelated meanings, "
    "2=distantly related, 3=closely related, 4=identical/same sense). Judge USE in context, "
    "not dictionary senses. Be consistent and deterministic.\n\nReference examples:\n"
    + filler +
    "\n\nAlways answer with a single integer 1, 2, 3, or 4 and nothing else.")
ITEMS = [
    "He sat on the river bank watching the water.",
    "The pilot banked the plane sharply to the left.",
    "I deposited my paycheck at the bank downtown.",
]
def user_for(item):
    return f"Use 1: {item}\nUse 2: She kept her money in the bank.\nRating:"

def call_raw(model, system_content, user, max_tokens, reasoning=None):
    key = os.environ["OPENROUTER_API_KEY"]
    body = {"model": model,
            "messages": [{"role": "system", "content": system_content},
                         {"role": "user", "content": user}],
            "temperature": 0, "max_tokens": max_tokens, "usage": {"include": True}}
    if reasoning is not None:
        body["reasoning"] = reasoning
    last = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(URL, data=json.dumps(body).encode(),
                headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                d = json.load(r)
            return {"content": (d["choices"][0]["message"].get("content") or "").strip(),
                    "usage": d.get("usage", {})}
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read().decode()[:200]}"
        except Exception as e:
            last = f"{type(e).__name__}: {e}"
        time.sleep(2 ** attempt)
    return {"content": None, "usage": {}, "error": last}

# system content forms: plain string (implicit models) vs cache_control block (claude)
PLAIN = SYSTEM
CACHED_BLOCK = [{"type": "text", "text": SYSTEM, "cache_control": {"type": "ephemeral"}}]

ARMS = [
    ("gpt",    PANEL["B"], PLAIN,        16, None),
    ("gemini", PANEL["C"], PLAIN,        16, {"enabled": False}),
    ("claude", PANEL["A"], CACHED_BLOCK, 16, None),
]

records = []
def cum_cost():
    return billed_cost([records])[0]

print(f"PREFIX char len: {len(SYSTEM)}")
for name, model, sysc, mt, reasoning in ARMS:
    print(f"\n===== {name} ({model}) =====")
    for item in ITEMS:
        for read in ["COLD", "WARM"]:
            r = call_raw(model, sysc, user_for(item), mt, reasoning)
            r2 = {"arm": name, "model": model, "item": item, "read": read,
                  "content": r["content"], "usage": r.get("usage", {}), "error": r.get("error")}
            records.append(r2)
            u = r.get("usage", {})
            ptd = u.get("prompt_tokens_details") or {}
            print(f"  {read:4s} item={item[:32]!r:36s} ans={r['content']!r} "
                  f"prompt_tok={u.get('prompt_tokens')} cached={ptd.get('cached_tokens')} "
                  f"cache_write={ptd.get('cache_write_tokens')} cost=${u.get('cost')}")
            if cum_cost() > ABORT_USD:
                print(f"!! ABORT: cumulative ${cum_cost():.5f} > {ABORT_USD}")
                json.dump(records, open(os.path.join(os.path.dirname(__file__), "raw.json"), "w"), indent=2)
                sys.exit(1)

out = os.path.join(os.path.dirname(__file__), "raw.json")
json.dump(records, open(out, "w"), indent=2)
total, have, missing = billed_cost([records])
print(f"\nTOTAL billed: ${total:.6f}  ({have} with cost, {missing} missing)  -> {out}")
