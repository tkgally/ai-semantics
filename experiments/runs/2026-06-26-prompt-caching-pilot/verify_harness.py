import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
import openrouter
from openrouter import PANEL, call, estimated_cost, billed_cost, RATE_CARD, CACHE_READ

# 1. body-build sanity: cache_prefix=False -> system content is the plain string (byte-identical).
#    Monkeypatch urlopen to capture the request body without hitting the network.
import json as _json, urllib.request as _u
captured = {}
class _Resp:
    def __enter__(self): return self
    def __exit__(self,*a): return False
    def read(self): return b'{}'
def _fake(req, timeout=None):
    captured["body"] = _json.loads(req.data.decode())
    # minimal valid-ish response
    class R(_Resp):
        def read(self): return b'{"choices":[{"message":{"content":"x"}}],"usage":{}}'
    return R()
_orig = _u.urlopen
_u.urlopen = _fake
try:
    call(PANEL["A"], "SYS-PREFIX", "ITEM", max_tokens=8)
    off = captured["body"]["messages"][0]["content"]
    call(PANEL["A"], "SYS-PREFIX", "ITEM", max_tokens=8, cache_prefix=True)
    on = captured["body"]["messages"][0]["content"]
finally:
    _u.urlopen = _orig
print("OFF system content (should be plain str):", repr(off))
print("ON  system content (should be cache_control block):", on)
assert off == "SYS-PREFIX", "cache_prefix=False must send plain string (byte-identical)"
assert isinstance(on, list) and on[0]["cache_control"] == {"type":"ephemeral"}, "cache_prefix=True must wrap"

# 2. estimated_cost cache-aware: cached=0 identical to old formula; cached>0 discounts.
m = PANEL["B"]; pin,pout = RATE_CARD[m]; cread = CACHE_READ[m]
rec_cold = [{"usage":{"prompt_tokens":1000,"completion_tokens":10,
             "prompt_tokens_details":{"cached_tokens":0}}}]
rec_warm = [{"usage":{"prompt_tokens":1000,"completion_tokens":10,
             "prompt_tokens_details":{"cached_tokens":900}}}]
old_formula = (1000*pin + 10*pout)/1e6
print("\nest(cold)=", estimated_cost([rec_cold], m), "old_formula=", old_formula,
      "match:", abs(estimated_cost([rec_cold], m)-old_formula) < 1e-12)
print("est(warm)=", estimated_cost([rec_warm], m),
      "expected=", (100*pin + 900*cread + 10*pout)/1e6)
assert abs(estimated_cost([rec_cold], m)-old_formula) < 1e-12, "cached=0 must equal old formula"
print("\nUNIT CHECKS PASS")
