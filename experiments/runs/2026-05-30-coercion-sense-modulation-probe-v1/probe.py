"""Coercion-as-sense-modulation bridge probe (v1, 2026-05-30).

Reuses the lexical v1 relatedness instrument (durel 1-4 + cont 0-100) on the frozen
constructional coercion stimuli (items.csv, sha256[:16] 6e6efb432be04a76). The target is the
VERB, already marked «» in both sentences. Temperature 0, logprob-free -> 3-family panel.
Internal-contrast-only. Cost = API-billed usage.cost (experiments/lib).

Run: OPENROUTER_API_KEY=... python3 probe.py
"""
import csv
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost, estimated_cost  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
ITEMS = os.path.join(HERE, "items.csv")
RAW = os.path.join(HERE, "raw")

DUREL_SYS = (
    "You are a linguistic annotator judging word meaning in context. You will see one target "
    "word, marked with «guillemets», in two sentences. Judge how related the MEANING of that "
    "target word is between the two uses, on this scale:\n"
    "4 = Identical\n3 = Closely Related\n2 = Distantly Related\n1 = Unrelated\n"
    "Answer with a single digit 1, 2, 3, or 4 and nothing else."
)
CONT_SYS = (
    "You are a linguistic annotator judging word meaning in context. You will see one target "
    "word, marked with «guillemets», in two sentences. Rate how related the MEANING of that "
    "target word is between the two uses on a 0-100 scale (100 = exactly the same meaning, "
    "0 = completely unrelated meanings). Answer with a single integer from 0 to 100 and "
    "nothing else."
)


def parse_durel(c):
    if not c:
        return None
    d = re.findall(r"[1-4]", c)
    return int(d[-1]) if d else None


def parse_int(c):
    if not c:
        return None
    m = re.findall(r"\d+", c)
    return max(0, min(100, int(m[0]))) if m else None


FRAMINGS = {"durel": (DUREL_SYS, parse_durel), "cont": (CONT_SYS, parse_int)}


def user(it):
    return (f"Target word: {it['verb']}\nSentence 1: {it['marked1']}\n"
            f"Sentence 2: {it['marked2']}\n")


def run(framing, items, slot, model):
    sys_prompt, parse = FRAMINGS[framing]
    recs = []
    for it in items:
        r = call(model, sys_prompt, user(it))
        recs.append({"item_id": it["item_id"], "verb": it["verb"], "arm": it["arm"],
                     "predicted": it["predicted"], "framing": framing,
                     "pred": parse(r.get("content")), "raw": r.get("content"),
                     "error": r.get("error"), "usage": r.get("usage")})
    os.makedirs(RAW, exist_ok=True)
    json.dump(recs, open(os.path.join(RAW, f"{framing}_{slot}.json"), "w"), indent=1)
    return recs


def main():
    items = list(csv.DictReader(open(ITEMS, encoding="utf-8")))
    print(f"{len(items)} items (first id={items[0]['item_id']})")
    summary, total = {}, 0.0
    for slot, model in PANEL.items():
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        allrecs = [run(fr, items, slot, model) for fr in FRAMINGS]
        billed, have, missing = billed_cost(allrecs)
        total += billed
        summary[slot] = {"model": model, "n_calls": sum(len(r) for r in allrecs),
                         "cost_usd_billed": round(billed, 5),
                         "cost_usd_estimate": round(estimated_cost(allrecs, model), 5),
                         "n_cost_missing": missing, "elapsed_s": round(time.time() - t0, 1),
                         "na": {fr: sum(1 for r in rs if r["pred"] is None)
                                for fr, rs in zip(FRAMINGS, allrecs)}}
        print(json.dumps(summary[slot], indent=1))
    json.dump(summary, open(os.path.join(RAW, "run_summary.json"), "w"), indent=1)
    print(f"\nTOTAL billed cost: ${total:.5f}")


if __name__ == "__main__":
    main()
