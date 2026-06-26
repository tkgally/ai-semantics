import json, os, sys
import urllib.request, urllib.error
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL
URL = "https://openrouter.ai/api/v1/chat/completions"
key = os.environ["OPENROUTER_API_KEY"]
SYS = "You are a careful annotator. Rate 1-4 the usage-relatedness of two uses. Answer one integer." + (" filler" * 1500)
def one(reasoning, max_tokens):
    body = {"model": PANEL["C"], "messages":[{"role":"system","content":SYS},
            {"role":"user","content":"Use 1: river bank. Use 2: money bank. Rating:"}],
            "temperature":0, "max_tokens":max_tokens, "usage":{"include":True}}
    if reasoning is not None: body["reasoning"]=reasoning
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
        headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.load(r)
        return {"content": d["choices"][0]["message"].get("content"),
                "finish": d["choices"][0].get("finish_reason"),
                "usage": d.get("usage",{})}
    except urllib.error.HTTPError as e:
        return {"HTTPError": f"{e.code}: {e.read().decode()[:300]}"}
print("A reasoning={enabled:False} mt=16:", json.dumps(one({"enabled":False},16))[:400])
print("B reasoning={effort:none} mt=16:", json.dumps(one({"effort":"none"},16))[:400])
print("C reasoning=None mt=4096:", json.dumps(one(None,4096))[:400])
