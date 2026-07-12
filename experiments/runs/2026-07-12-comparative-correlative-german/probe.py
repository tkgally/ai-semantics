"""German comparative-correlative covariation-inference probe (A6, 2026-07-12, s213).

A faithful PORT of the frozen English v1/powered CC probe
(experiments/runs/2026-07-02-comparative-correlative-powered/probe.py). Every design choice that
could change a verdict is held identical in SHAPE — same two instruments (forced-choice covariation
direction + NLI), same parsing logic (last keyword / trailing digit), same temperature=0 greedy
completion, same panel (config/models.md), same max_tokens policy (4096 for google/ to absorb
reasoning tokens, 64 otherwise). The ONE deliberate change is the TARGET LANGUAGE: the stimulus
sentences, the instrument scaffolding (system prompts, the forced-choice question, the NLI
hypothesis) and the answer vocabulary are ALL German. This is intentional — the probe tests whether
the panel reads the covariation meaning off the GERMAN construction (je…desto/umso), so the whole
task is posed in-language; a freeze-time German-competence smoke test (smoke.py) guards that the
panel can do German at all before any inference is read as constructional.

Answer vocabulary: FC = ZUNAHME (increase) / ABNAHME (decrease) / UNBESTIMMT (undetermined); NLI =
digit 0/1/2. Parsed back to the language-neutral gold labels increase/decrease/undetermined and
0/1/2 so analyze.py is byte-comparable to the English analyzer.

Two arms (both constructed; NO human arm — Q3-A internal-contrast-only, no non-English CC human
dataset exists per the scout):
  1. constructed-nli — NLI framing on the 136 German items
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
                                         "comparative-correlative-german", "items.csv"))
RAW_DIR = os.path.join(HERE, "raw")

# --- German instrument prompts (a faithful translation of the frozen English NLI_SYS / FC_SYS) ---
NLI_SYS = (
    "Du bist ein Experte für Natural Language Inference (NLI). Gegeben eine Prämisse und eine "
    "Hypothese, bestimme die Inferenzrelation:\n"
    "0 - Entailment - die Hypothese muss angesichts der Prämisse wahr sein\n"
    "1 - neutral - die Hypothese kann angesichts der Prämisse wahr sein oder nicht\n"
    "2 - Widerspruch - die Hypothese darf angesichts der Prämisse nicht wahr sein\n"
    "Gib eine einzige Ziffer 0, 1 oder 2 aus und sonst nichts."
)

FC_SYS = (
    "Du beantwortest eine einzelne Multiple-Choice-Frage zu einer kurzen Passage. Lies die Passage "
    "und entscheide, was sie darüber impliziert, wie sich die zweite Größe ändert, wenn die erste "
    "Größe zunimmt. Antworte mit genau einem Wort: ZUNAHME, ABNAHME oder UNBESTIMMT. Gib nur dieses "
    "eine Wort aus."
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


# German answer keyword -> language-neutral gold label (last keyword wins, as in the English probe)
_FC_MAP = {"ZUNAHME": "increase", "ABNAHME": "decrease", "UNBESTIMMT": "undetermined"}


def parse_fc(content):
    if not content:
        return None
    c = content.upper()
    hits = [(m.start(), m.group()) for m in
            re.finditer(r"ZUNAHME|ABNAHME|UNBESTIMMT", c)]
    return _FC_MAP[hits[-1][1]] if hits else None


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
        json.dump(recs, f, indent=1, ensure_ascii=False)
    return recs


def load_constructed():
    return list(csv.DictReader(open(ITEMS_CSV)))


def usage_cost(recs):
    return sum(float((r.get("usage") or {}).get("cost") or 0) for r in recs)


def main():
    constructed = load_constructed()
    print(f"constructed items: {len(constructed)}")

    nli_user = lambda it: f"Prämisse: {it['sentence']}\nHypothese: {it['nli_hypothesis']}\nRelation:"
    fc_user = lambda it: (f"Passage: {it['sentence']}\n"
                          f"Wenn {it['dim1']} zunimmt, was impliziert die Passage über "
                          f"{it['dim2']}? Antworte mit ZUNAHME, ABNAHME oder UNBESTIMMT.")

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
