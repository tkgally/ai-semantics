"""Comparative-correlative covariation-inference probe — POWERED re-run (A2a, 2026-07-02).

Re-uses the FROZEN v1 instrument (experiments/runs/2026-05-29-comparative-correlative-probe-v1/probe.py)
VERBATIM in every respect that could change a verdict — same system prompts (NLI_SYS, FC_SYS),
same user templates, same parsing (parse_nli / parse_fc = trailing digit / last keyword),
same temperature=0 greedy completion, same panel (config/models.md), same max_tokens policy
(4096 for google/ to absorb reasoning tokens, 64 otherwise). The ONLY change is the item set:
the fresh 34-pair powered set (data/comparative-correlative-powered/items.csv).

Two arms (both constructed; no Scivetti human arm — the human-comparison leg is unchanged from
v1's single run and out of scope for this within-model magnitude re-run):
  1. constructed-nli — NLI framing on the 136 fresh items
  2. constructed-fc  — forced-choice covariation-direction framing on the same items

Outputs raw JSON per (arm, panel-slot) under raw/. Run: OPENROUTER_API_KEY=... python3 probe.py
"""
import csv, json, os, re, time, urllib.error, urllib.request

KEY = os.environ["OPENROUTER_API_KEY"]
URL = "https://openrouter.ai/api/v1/chat/completions"

PANEL = {
    "A": "anthropic/claude-sonnet-4.6",
    "B": "openai/gpt-5.4-mini",
    "C": "google/gemini-3.5-flash",
}

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS_CSV = os.path.abspath(os.path.join(HERE, "..", "..", "data",
                                         "comparative-correlative-powered", "items.csv"))
RAW_DIR = os.path.join(HERE, "raw")

# --- FROZEN v1 prompts (byte-identical to the v1 probe) ---
NLI_SYS = (
    "You are an expert annotator for Natural Language Inference (NLI). Given a "
    "Premise and a Hypothesis, determine the inference relation:\n"
    "0 - entailment - the hypothesis must be true given the premise\n"
    "1 - neutral - the hypothesis may or may not be true given the premise\n"
    "2 - contradiction - the hypothesis must not be true given the premise\n"
    "Output a single digit 0, 1, or 2 and nothing else."
)

FC_SYS = (
    "You answer a single multiple-choice question about a short passage. "
    "Read the passage, then decide what it implies about how the second quantity "
    "changes as the first quantity increases. Answer with exactly one word: "
    "INCREASE, DECREASE, or UNDETERMINED. Output only that one word."
)


def call(model, system, user, max_tokens):
    body = {
        "model": model,
        "messages": [{"role": "system", "content": system},
                     {"role": "user", "content": user}],
        "temperature": 0,
        "max_tokens": max_tokens,
        "usage": {"include": True},
    }
    last = None
    for attempt in range(4):
        try:
            req = urllib.request.Request(
                URL, data=json.dumps(body).encode(),
                headers={"Authorization": f"Bearer {KEY}",
                         "Content-Type": "application/json"})
            t0 = time.time()
            with urllib.request.urlopen(req, timeout=120) as r:
                d = json.load(r)
            dt = time.time() - t0
            msg = d["choices"][0]["message"]
            content = (msg.get("content") or "").strip()
            return {"dt": dt, "content": content, "usage": d.get("usage", {})}
        except urllib.error.HTTPError as e:
            last = f"HTTP {e.code}: {e.read().decode()[:200]}"
        except Exception as e:  # noqa: BLE001
            last = f"{type(e).__name__}: {e}"
        time.sleep(2 ** attempt)
    return {"dt": None, "content": None, "usage": {}, "error": last}


def parse_nli(content):
    if not content:
        return None
    digs = re.findall(r"[012]", content)
    return digs[-1] if digs else None


def parse_fc(content):
    if not content:
        return None
    c = content.upper()
    hits = [(m.start(), m.group()) for m in
            re.finditer(r"INCREASE|DECREASE|UNDETERMINED", c)]
    return hits[-1][1].lower() if hits else None


def mt_for(model):
    return 4096 if model.startswith("google/") else 64


def run_arm(arm, items, system, build_user, parse, slot, model):
    recs = []
    for it in items:
        user = build_user(it)
        r = call(model, system, user, mt_for(model))
        recs.append({**it, "prompt": user, "raw": r.get("content"),
                     "error": r.get("error"), "pred": parse(r.get("content")),
                     "dt": r.get("dt"), "usage": r.get("usage")})
    os.makedirs(RAW_DIR, exist_ok=True)
    with open(os.path.join(RAW_DIR, f"{arm}_{slot}.json"), "w") as f:
        json.dump(recs, f, indent=1)
    return recs


def load_constructed():
    return list(csv.DictReader(open(ITEMS_CSV)))


def usage_cost(recs):
    """Sum the OpenRouter-billed usage.cost (USD) actually returned per record."""
    return sum(float((r.get("usage") or {}).get("cost") or 0) for r in recs)


def main():
    constructed = load_constructed()
    print(f"constructed items: {len(constructed)}")

    nli_user = lambda it: f"Premise: {it['sentence']}\nHypothesis: {it['nli_hypothesis']}\nRelation:"
    fc_user = lambda it: (f"Passage: {it['sentence']}\n"
                          f"As {it['dim1']} increases, what does the passage imply about "
                          f"{it['dim2']}? Answer INCREASE, DECREASE, or UNDETERMINED.")

    summary = {}
    for slot, model in PANEL.items():
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        nli = run_arm("constructed-nli", constructed, NLI_SYS, nli_user, parse_nli, slot, model)
        fc = run_arm("constructed-fc", constructed, FC_SYS, fc_user, parse_fc, slot, model)
        cost = usage_cost(nli) + usage_cost(fc)
        summary[slot] = {
            "model": model,
            "n_calls": len(nli) + len(fc),
            "cost_usd_billed": round(cost, 5),
            "elapsed_s": round(time.time() - t0, 1),
            "nli_na": sum(1 for r in nli if r["pred"] is None),
            "fc_na": sum(1 for r in fc if r["pred"] is None),
        }
        print(json.dumps(summary[slot], indent=1))
    with open(os.path.join(RAW_DIR, "run_summary.json"), "w") as f:
        json.dump(summary, f, indent=1)
    total = sum(s["cost_usd_billed"] for s in summary.values())
    print(f"\nTOTAL billed cost: ${total:.5f}")


if __name__ == "__main__":
    main()
