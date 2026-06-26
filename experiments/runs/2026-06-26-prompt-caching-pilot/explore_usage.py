"""Exploratory: dump the FULL usage object OpenRouter returns, cold then warm,
for a large repeated-prefix prompt. Implicit caching (gpt) needs no code change.
We just send the same prefix twice and inspect what `usage` reports.
$0-stakes: 2 gpt calls only."""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL

import urllib.request, urllib.error
URL = "https://openrouter.ai/api/v1/chat/completions"

# Build a LARGE shared prefix (>~1500 tokens) so it can cross provider cache minimums.
# Mirrors the shape of a project probe: a long instruction block, then a short item stem.
filler_examples = "\n".join(
    f"- Example {i}: the word 'bank' in context {i} relates to sense A at level "
    f"{(i % 4)} on a 0-3 scale; consider co-occurrence, selectional restrictions, and "
    f"typical referential targets when you judge graded usage-relatedness." for i in range(120))
SYSTEM = (
    "You are a careful lexical-semantics annotator. You rate the graded usage-relatedness "
    "of two uses of the same word form on a 4-point scale (1=unrelated meanings, "
    "2=distantly related, 3=closely related, 4=identical/same sense). Judge USE in context, "
    "not dictionary senses. Be consistent and deterministic.\n\nReference examples:\n"
    + filler_examples +
    "\n\nAlways answer with a single integer 1, 2, 3, or 4 and nothing else.")
def user_for(item):
    return f"Use 1: {item}\nUse 2: She kept her money in the bank.\nRating:"

def call_raw(model, system, user, max_tokens, reasoning=None):
    key = os.environ["OPENROUTER_API_KEY"]
    body = {"model": model,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
            "temperature": 0, "max_tokens": max_tokens,
            "usage": {"include": True}}
    if reasoning is not None:
        body["reasoning"] = reasoning
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)

item = "He sat on the river bank watching the water."
print("PREFIX char len:", len(SYSTEM))
for tag in ["COLD", "WARM"]:
    d = call_raw(PANEL["B"], SYSTEM, user_for(item), max_tokens=16)
    print(f"\n=== {tag} (gpt) ===")
    print("content:", repr(d["choices"][0]["message"].get("content")))
    print("usage:", json.dumps(d.get("usage", {}), indent=2))
