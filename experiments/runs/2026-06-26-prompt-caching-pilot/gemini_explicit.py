import json, os, sys, time
import urllib.request, urllib.error
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL
URL = "https://openrouter.ai/api/v1/chat/completions"
key = os.environ["OPENROUTER_API_KEY"]
filler = "\n".join(f"- Example {i}: word 'bank' context {i} relates at level {(i%4)}; "
    f"consider co-occurrence and selectional restrictions for graded usage-relatedness." for i in range(120))
SYS = ("You are a careful lexical-semantics annotator rating graded usage-relatedness on a "
       "4-point scale. Judge use in context. Reference examples:\n"+filler+
       "\nAnswer with a single integer 1-4 and nothing else.")
BLOCK = [{"type":"text","text":SYS,"cache_control":{"type":"ephemeral"}}]
def one(item):
    body = {"model": PANEL["C"], "messages":[{"role":"system","content":BLOCK},
            {"role":"user","content":f"Use 1: {item}\nUse 2: She kept her money in the bank.\nRating:"}],
            "temperature":0, "max_tokens":2048, "usage":{"include":True},
            "reasoning":{"effort":"minimal"}}
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
        headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"})
    for a in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                d = json.load(r)
            return {"content": d["choices"][0]["message"].get("content"), "usage": d.get("usage",{})}
        except urllib.error.HTTPError as e:
            err=f"{e.code}: {e.read().decode()[:200]}"; time.sleep(2**a)
    return {"error": err}
item = "He sat on the river bank watching the water."
recs=[]
for read in ["COLD","WARM"]:
    r=one(item); recs.append(r); u=r.get("usage",{}); ptd=u.get("prompt_tokens_details") or {}
    print(f"{read:5s} ans={r.get('content')!r} prompt={u.get('prompt_tokens')} cached={ptd.get('cached_tokens')} "
          f"cache_write={ptd.get('cache_write_tokens')} cost=${u.get('cost')} err={r.get('error')}")
json.dump(recs, open(os.path.join(os.path.dirname(__file__),"gemini_explicit_raw.json"),"w"), indent=2)
