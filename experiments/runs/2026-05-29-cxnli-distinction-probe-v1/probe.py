"""Scivetti CxNLI base-vs-distinction probe v1 (2026-05-29).

The experimental cash-out of open-question/constructional-divergence-probe: turn the
EXTERNAL Scivetti >40% divergent-form drop (claim/constructional-divergent-form-
generalization-gap) into a PROJECT-RUN result. Runs the project panel as subjects on
Scivetti's own NLI items and measures, per construction, the panel's accuracy on the
base task (Exp 1, CxNLI) vs. the syntactically-identical/semantically-divergent task
(Exp 2, CxNLI-Distinction) — the same base-vs-distinction drop Scivetti reports.

Instrument: NLI (entailment/neutral/contradiction -> 0/1/2), the ratified instrument
(constructional-divergence-operationalization). No logprobs needed (panel exposes none);
temperature 0 greedy completion + parse, identical to the comparative-correlative probe.

Human anchor: the Scivetti gold labels + aggregate baselines (Exp1 ~0.90, Exp2 ~0.83),
resource/scivetti-2025-cxnli-dataset. Dataset has NO license -> read in place from a
local clone, NOT mirrored. Raw outputs are redacted of dataset text before commit.

Scope: the 5 argument-structure constructions present in BOTH experiments
(causative-with, caused-motion, conative, intransitive-motion, resultative). For the
base task we subsample to 20 items/construction to match the distinction set's 20/cxn,
so the base-vs-distinction comparison is N-matched. Subsample is the FIRST 20 by item
number, fixed before the run (no cherry-picking).

Run: OPENROUTER_API_KEY=... python3 probe.py [--scivetti-dir PATH]
"""
import argparse, csv, json, os, re, time, urllib.error, urllib.request

KEY = os.environ["OPENROUTER_API_KEY"]
URL = "https://openrouter.ai/api/v1/chat/completions"
PANEL = {"A": "anthropic/claude-sonnet-4.6", "B": "openai/gpt-5.4-mini",
         "C": "google/gemini-3.5-flash"}
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")

# Same NLI system prompt as the comparative-correlative probe (paraphrase of Scivetti
# prompt #1), so the two project probes use one instrument.
NLI_SYS = (
    "You are an expert annotator for Natural Language Inference (NLI). Given a "
    "Premise and a Hypothesis, determine the inference relation:\n"
    "0 - entailment - the hypothesis must be true given the premise\n"
    "1 - neutral - the hypothesis may or may not be true given the premise\n"
    "2 - contradiction - the hypothesis must not be true given the premise\n"
    "Output a single digit 0, 1, or 2 and nothing else."
)
SHARED_CXNS = ["causative-with-CxN", "caused-motion", "conative",
               "intransitive-motion", "resultative"]
N_PER_CXN = 20  # match the distinction set


def parse_tsv(path):
    recs = list(csv.DictReader(open(path), delimiter="\t"))
    relcol = "Annotation Targets - Gold Standard Relation"
    items, cur = [], {}
    for r in recs:
        phr = r["P/H/R"].strip().lower()
        if phr == "premise":
            cur = {"cxn": r["CxN Type"].strip(), "num": r["Number"], "premise": r[relcol]}
        elif phr == "hypothesis":
            cur["hyp"] = r[relcol]
        elif phr == "relation":
            m = re.match(r"\s*([012])", r[relcol])
            cur["gold"] = m.group(1) if m else None
            items.append(cur); cur = {}
    return items


def subsample_base(items):
    """First N_PER_CXN items per shared construction, by integer item number."""
    out = []
    for cxn in SHARED_CXNS:
        sub = sorted([x for x in items if x["cxn"] == cxn],
                     key=lambda z: int(z["num"]))[:N_PER_CXN]
        out.extend(sub)
    return out


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


def run_arm(arm, items, slot, model):
    recs = []
    for it in items:
        user = f"Premise: {it['premise']}\nHypothesis: {it['hyp']}\nRelation:"
        r = call(model, NLI_SYS, user)
        recs.append({"cxn": it["cxn"], "num": it["num"], "gold": it["gold"],
                     "pred": parse_nli(r.get("content")), "error": r.get("error"),
                     "usage": r.get("usage")})
    # redact: keep only scoring fields (dataset has no license)
    red = [{"cxn": x["cxn"], "num": x["num"], "gold": x["gold"], "pred": x["pred"],
            "correct": str(x["pred"]) == str(x["gold"])} for x in recs]
    os.makedirs(RAW, exist_ok=True)
    json.dump(red, open(os.path.join(RAW, f"{arm}_{slot}.json"), "w"), indent=1)
    return recs


def cost(recs, model):
    price = {"anthropic/claude-sonnet-4.6": (3.0, 15.0),
             "openai/gpt-5.4-mini": (0.20, 0.60),
             "google/gemini-3.5-flash": (0.15, 0.60)}[model]
    pin = sum((r["usage"] or {}).get("prompt_tokens", 0) or 0 for r in recs)
    pout = sum((r["usage"] or {}).get("completion_tokens", 0) or 0 for r in recs)
    return (pin * price[0] + pout * price[1]) / 1_000_000


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scivetti-dir", default="/tmp/beyond-memorization")
    args = ap.parse_args()
    base_all = parse_tsv(os.path.join(args.scivetti_dir, "data", "CxNLI",
                                      "CxNLI_3_examples_test.tsv"))
    base = subsample_base(base_all)
    dist = parse_tsv(os.path.join(args.scivetti_dir, "data", "CxNLI_distinction",
                                  "CxNLI_distinction_test.tsv"))
    print(f"base (matched subsample): {len(base)} items | distinction: {len(dist)} items")
    summary = {}
    total = 0.0
    for slot, model in PANEL.items():
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        b = run_arm("base", base, slot, model)
        d = run_arm("distinction", dist, slot, model)
        cst = cost(b, model) + cost(d, model)
        total += cst
        summary[slot] = {"model": model, "n_calls": len(b) + len(d),
                         "cost_usd_est": round(cst, 4), "elapsed_s": round(time.time() - t0, 1),
                         "base_na": sum(1 for r in b if r["pred"] is None),
                         "dist_na": sum(1 for r in d if r["pred"] is None)}
        print(json.dumps(summary[slot], indent=1))
    json.dump(summary, open(os.path.join(RAW, "run_summary.json"), "w"), indent=1)
    print(f"\nTOTAL est cost: ${total:.4f}")


if __name__ == "__main__":
    main()
