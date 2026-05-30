"""Caused-motion implicit-cue v2b probe (2026-05-30) -- copied from the add-direction v2 harness.

Operationalizes design/coercion-implicit-cue-v2b with the project OWN stimuli
(experiments/data/coercion-implicit-cue-v2b/items.csv, frozen by build_items.py
BEFORE this runs), under the RATIFIED difficulty gate (decisions/resolved/
cc-v2-difficulty-operationalization). Behavioral NLI + forced-choice, temperature 0,
NO logprobs -> runs on the existing 3-family behavioral panel (config/models.md).

Indicator: affirm-construction-inference rate (FC YES, or NLI label 0 = entailment) on
the per-item hypothesis. Key arm = conflicting-cue (canonical vs cue minimal pair):
a model still affirming under the explicit denial = template/H-default; withholding = H-deep.

Arms per slot:
  NLI: premise = sentence, hypothesis = nli_hypothesis -> 0/1/2
  FC : "is the following statement true: '<hypothesis>'? YES / NO / CANT_TELL"

Run: OPENROUTER_API_KEY=... python3 probe.py
"""
import csv, json, os, re, time, urllib.error, urllib.request

KEY = os.environ["OPENROUTER_API_KEY"]
URL = "https://openrouter.ai/api/v1/chat/completions"
PANEL = {"A": "anthropic/claude-sonnet-4.6", "B": "openai/gpt-5.4-mini",
         "C": "google/gemini-3.5-flash"}
HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.abspath(os.path.join(HERE, "..", "..", "data",
                                     "coercion-implicit-cue-v2b", "items.csv"))
RAW = os.path.join(HERE, "raw")

NLI_SYS = (
    "You are an expert annotator for Natural Language Inference (NLI). Given a "
    "Premise and a Hypothesis, determine the inference relation:\n"
    "0 - entailment - the hypothesis must be true given the premise\n"
    "1 - neutral - the hypothesis may or may not be true given the premise\n"
    "2 - contradiction - the hypothesis must not be true given the premise\n"
    "Output a single digit 0, 1, or 2 and nothing else."
)
FC_SYS = (
    "You answer a single question about a short sentence, using ONLY what the sentence "
    "states or logically entails (not what is merely plausible). Answer with exactly one "
    "of: YES, NO, CANT_TELL. Output only that token and nothing else."
)


def load_items():
    return list(csv.DictReader(open(ITEMS)))


def call(model, system, user):
    mt = 4096 if model.startswith("google/") else 64
    body = {"model": model, "messages": [{"role": "system", "content": system},
            {"role": "user", "content": user}], "temperature": 0, "max_tokens": mt}
    last = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(
                URL, data=json.dumps(body).encode(),
                headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=120) as r:
                d = json.load(r)
            msg = d["choices"][0]["message"]
            return {"content": (msg.get("content") or "").strip(), "usage": d.get("usage", {})}
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read().decode()[:150]}"
        except Exception as e:  # noqa: BLE001
            last = f"{type(e).__name__}: {e}"
        time.sleep(2 ** attempt)
    return {"content": None, "usage": {}, "error": last}


def parse_nli(c):
    if not c:
        return None
    digs = re.findall(r"[012]", c)
    return digs[-1] if digs else None


def parse_fc(c):
    if not c:
        return None
    u = c.upper()
    if "CANT" in u.replace("'", "") or "CAN'T" in u or "TELL" in u:
        return "CANT_TELL"
    if re.search(r"\bYES\b", u):
        return "YES"
    if re.search(r"\bNO\b", u):
        return "NO"
    return None


def fc_q(it):
    return (f"Sentence: {it['sentence']}\nQuestion: Based only on the sentence, is the "
            f"following statement true: \"{it['nli_hypothesis']}\" Answer YES, NO, or CANT_TELL.")


def run(arm, sys_prompt, items, slot, model, make_user, parse):
    recs = []
    for it in items:
        r = call(model, sys_prompt, make_user(it))
        recs.append({"item_id": it["item_id"], "construction": it["construction"],
                     "stem": it["stem"], "condition": it["condition"],
                     "difficulty": it["difficulty"], "pred": parse(r.get("content")),
                     "raw": r.get("content"), "error": r.get("error"), "usage": r.get("usage")})
    os.makedirs(RAW, exist_ok=True)
    json.dump(recs, open(os.path.join(RAW, f"{arm}_{slot}.json"), "w"), indent=1)
    return recs


def cost(recs_lists, model):
    price = {"anthropic/claude-sonnet-4.6": (3.0, 15.0),
             "openai/gpt-5.4-mini": (0.20, 0.60),
             "google/gemini-3.5-flash": (0.15, 0.60)}[model]
    pin = pout = 0
    for recs in recs_lists:
        pin += sum((r["usage"] or {}).get("prompt_tokens", 0) or 0 for r in recs)
        pout += sum((r["usage"] or {}).get("completion_tokens", 0) or 0 for r in recs)
    return (pin * price[0] + pout * price[1]) / 1_000_000


def main():
    items = load_items()
    print(f"{len(items)} items")
    nli_user = lambda it: f"Premise: {it['sentence']}\nHypothesis: {it['nli_hypothesis']}\nRelation:"
    summary, total = {}, 0.0
    for slot, model in PANEL.items():
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        nli = run("nli", NLI_SYS, items, slot, model, nli_user, parse_nli)
        fc = run("fc", FC_SYS, items, slot, model, fc_q, parse_fc)
        cst = cost([nli, fc], model)
        total += cst
        summary[slot] = {"model": model, "n_calls": len(nli) + len(fc),
                         "cost_usd_est": round(cst, 4), "elapsed_s": round(time.time() - t0, 1),
                         "nli_na": sum(1 for r in nli if r["pred"] is None),
                         "fc_na": sum(1 for r in fc if r["pred"] is None)}
        print(json.dumps(summary[slot], indent=1))
    json.dump(summary, open(os.path.join(RAW, "run_summary.json"), "w"), indent=1)
    print(f"\nTOTAL est cost: ${total:.4f}")


if __name__ == "__main__":
    main()
