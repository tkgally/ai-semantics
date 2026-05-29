"""Comparative-correlative covariation-inference probe v1 (2026-05-29).

Operationalizes conjecture/comparative-correlative-construction per the ratified
design (experiments/designs/comparative-correlative-v1.md) and the ratified
constructional-divergence-operationalization decision (both instruments, frozen
thresholds T1=30pp gap / T2=70% direction-flip / T3=within-15pp atypical).

Read-only behavioral API probe over the panel (config/models.md). No logprobs are
needed: panel chat models do not expose token logprobs on OpenRouter (verified
2026-05-29), so per the design's fallback we use temperature=0 greedy completion
and parse the label/direction string.

Three arms:
  1. NLI framing on the project's frozen constructed items (data/.../items.csv)
  2. Forced-choice framing on the same constructed items
  3. Human-comparison arm: NLI framing on the 30 real Scivetti CC items
     (read in place from a local clone; NOT mirrored in-repo, repo has no license).

Outputs raw JSON per (arm, panel-slot) under runs/<this dir>/raw/.

Run: OPENROUTER_API_KEY=... python3 probe.py [--scivetti-dir PATH]
"""
import argparse, csv, json, os, re, time, urllib.error, urllib.request

KEY = os.environ["OPENROUTER_API_KEY"]
URL = "https://openrouter.ai/api/v1/chat/completions"

PANEL = {
    "A": "anthropic/claude-sonnet-4.6",
    "B": "openai/gpt-5.4-mini",
    "C": "google/gemini-3.5-flash",
}

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS_CSV = os.path.abspath(os.path.join(HERE, "..", "..", "data",
                                         "comparative-correlative", "items.csv"))
RAW_DIR = os.path.join(HERE, "raw")

# NLI prompt: paraphrased from Scivetti prompts/CxNLI_prompts.py (prompt #1) so the
# human-comparison arm is run on the same instrument and label scheme.
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
    return digs[-1] if digs else None  # trailing digit (handles CoT-ish output)


def parse_fc(content):
    if not content:
        return None
    c = content.upper()
    # take the last keyword mentioned (handles any preamble)
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
        pred = parse(r.get("content"))
        recs.append({**it, "prompt": user, "raw": r.get("content"),
                     "error": r.get("error"), "pred": pred,
                     "dt": r.get("dt"), "usage": r.get("usage")})
    os.makedirs(RAW_DIR, exist_ok=True)
    path = os.path.join(RAW_DIR, f"{arm}_{slot}.json")
    with open(path, "w") as f:
        json.dump(recs, f, indent=1)
    return recs


def load_constructed():
    return list(csv.DictReader(open(ITEMS_CSV)))


def load_scivetti_cc(scivetti_dir):
    """Parse the 30 real Scivetti CC items from CxNLI_3_examples_test.tsv (in place)."""
    path = os.path.join(scivetti_dir, "data", "CxNLI", "CxNLI_3_examples_test.tsv")
    rows = list(csv.reader(open(path), delimiter="\t"))[1:]
    items, cur = [], {}
    for cxn, num, phr, val in rows:
        p = phr.strip().lower()
        if p == "premise":
            cur = {"cxn": cxn.strip(), "num": num, "premise": val}
        elif p == "hypothesis":
            cur["hyp"] = val
        elif p == "relation":
            cur["rel_raw"] = val
            items.append(cur); cur = {}
    cc = [it for it in items if it["cxn"].lower() == "comparative-correlative"]
    for it in cc:
        m = re.match(r"\s*([012])", it["rel_raw"])
        it["gold"] = m.group(1) if m else None
    return cc


def usage_cost(recs, model):
    # rough cost in USD using config/budget.md per-MT prices
    price = {"anthropic/claude-sonnet-4.6": (3.0, 15.0),
             "openai/gpt-5.4-mini": (0.20, 0.60),
             "google/gemini-3.5-flash": (0.15, 0.60)}[model]
    pin = sum((r["usage"] or {}).get("prompt_tokens", 0) or 0 for r in recs)
    pout = sum((r["usage"] or {}).get("completion_tokens", 0) or 0 for r in recs)
    return pin, pout, (pin * price[0] + pout * price[1]) / 1_000_000


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scivetti-dir", default="/tmp/beyond-memorization")
    args = ap.parse_args()

    constructed = load_constructed()
    scivetti = load_scivetti_cc(args.scivetti_dir)
    print(f"constructed items: {len(constructed)} | scivetti CC items: {len(scivetti)}")

    nli_user = lambda it: f"Premise: {it['sentence']}\nHypothesis: {it['nli_hypothesis']}\nRelation:"
    fc_user = lambda it: (f"Passage: {it['sentence']}\n"
                          f"As {it['dim1']} increases, what does the passage imply about "
                          f"{it['dim2']}? Answer INCREASE, DECREASE, or UNDETERMINED.")
    sci_user = lambda it: f"Premise: {it['premise']}\nHypothesis: {it['hyp']}\nRelation:"

    summary = {}
    for slot, model in PANEL.items():
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        nli = run_arm("constructed-nli", constructed, NLI_SYS, nli_user, parse_nli, slot, model)
        fc = run_arm("constructed-fc", constructed, FC_SYS, fc_user, parse_fc, slot, model)
        sci = run_arm("scivetti-nli", scivetti, NLI_SYS, sci_user, parse_nli, slot, model)
        c1 = usage_cost(nli, model); c2 = usage_cost(fc, model); c3 = usage_cost(sci, model)
        cost = c1[2] + c2[2] + c3[2]
        summary[slot] = {
            "model": model,
            "n_calls": len(nli) + len(fc) + len(sci),
            "cost_usd_est": round(cost, 4),
            "elapsed_s": round(time.time() - t0, 1),
            "nli_na": sum(1 for r in nli if r["pred"] is None),
            "fc_na": sum(1 for r in fc if r["pred"] is None),
            "sci_na": sum(1 for r in sci if r["pred"] is None),
        }
        print(json.dumps(summary[slot], indent=1))
    with open(os.path.join(RAW_DIR, "run_summary.json"), "w") as f:
        json.dump(summary, f, indent=1)
    total = sum(s["cost_usd_est"] for s in summary.values())
    print(f"\nTOTAL est cost: ${total:.4f}")


if __name__ == "__main__":
    main()
