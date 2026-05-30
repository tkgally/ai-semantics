"""Comparative-correlative v2 (off-ceiling) probe (2026-05-30).

Operationalizes design/comparative-correlative-v2 with the project's OWN frozen stimuli
(experiments/data/comparative-correlative-v2/items.csv, built by build_items.py BEFORE this
runs), under the RATIFIED difficulty gate (decisions/resolved/cc-v2-difficulty-
operationalization). Behavioral NLI + forced-choice, temperature 0, NO logprobs -> runs on
the existing 3-family behavioral panel (config/models.md). Internal-contrast-only (no
Scivetti human-comparison arm: the conflicting-cue / multi-step arms have no in-repo human
norm; design s4).

Instrument (reused verbatim from the v1 CC probe):
  NLI: premise = sentence, hypothesis = "As <dim1> increases, <dim2> increases." -> 0/1/2
  FC : "As <dim1> increases, how does <dim2> change?" -> INCREASE / DECREASE / UNDETERMINED

Run: OPENROUTER_API_KEY=... python3 probe.py
"""
import csv, json, os, re, time, urllib.error, urllib.request

KEY = os.environ["OPENROUTER_API_KEY"]
URL = "https://openrouter.ai/api/v1/chat/completions"
PANEL = {"A": "anthropic/claude-sonnet-4.6", "B": "openai/gpt-5.4-mini",
         "C": "google/gemini-3.5-flash"}
HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.abspath(os.path.join(HERE, "..", "..", "data",
                                     "comparative-correlative-v2", "items.csv"))
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
    "You answer a single multiple-choice question about a short passage. Read the passage, "
    "then decide what it implies about how the second quantity changes as the first quantity "
    "increases. Use ONLY what the passage states or logically entails (not what is merely "
    "plausible in the real world). Answer with exactly one word: INCREASE, DECREASE, or "
    "UNDETERMINED. Output only that one word."
)


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
    if "UNDETERMIN" in u:
        return "UNDETERMINED"
    if "INCREASE" in u:
        return "INCREASE"
    if "DECREASE" in u:
        return "DECREASE"
    return None


def nli_user(it):
    return f"Premise: {it['sentence']}\nHypothesis: {it['nli_hypothesis']}\nRelation:"


def fc_user(it):
    return (f"Passage: {it['sentence']}\nAs {it['dim1']} increases, how does {it['dim2']} "
            f"change? Answer INCREASE, DECREASE, or UNDETERMINED.")


def run(arm, sys_prompt, items, slot, model, make_user, parse):
    recs = []
    for it in items:
        r = call(model, sys_prompt, make_user(it))
        recs.append({"item_id": it["item_id"], "arm": it["arm"], "difficulty": it["difficulty"],
                     "direction_gold": it["direction_gold"], "pred": parse(r.get("content")),
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
    items = list(csv.DictReader(open(ITEMS)))
    print(f"{len(items)} items")
    summary, total = {}, 0.0
    for slot, model in PANEL.items():
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        nli = run("nli", NLI_SYS, items, slot, model, nli_user, parse_nli)
        fc = run("fc", FC_SYS, items, slot, model, fc_user, parse_fc)
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
