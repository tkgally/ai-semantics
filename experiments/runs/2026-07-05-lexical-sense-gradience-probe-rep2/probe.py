"""Lexical-sense-gradience v1 probe (2026-05-30).

Operationalizes design/lexical-sense-gradience-v1 under the RESOLVED operationalization gate.
v1 scope = P1 monotonicity + P3 context-similarity control. Behavioral panel (Q1), three
pre-registered framings per item, temperature 0, logprob-free -> existing 3-family panel:
  durel : DURel 4-point sense-relatedness of the marked target word across the two uses
          (4 Identical / 3 Closely Related / 2 Distantly Related / 1 Unrelated) -> the primary
          graded signal, directly rank-comparable to the human DURel median.
  cont  : 0-100 continuous sense-relatedness of the marked target word (instrument robustness).
  topic : 0-100 topic/situation similarity of the two sentences IGNORING the target word
          (the Q3 semantic context-similarity control).

DATA/LICENCE: reads the gitignored local full-text file (DWUG / CCOHA corpus text, NOT
committed). Committed raw JSON records item_id + lemma + framing + model output + the human
DURel gold + usage -- NO corpus sentences. Cost = API-billed usage.cost (experiments/lib).

Run: OPENROUTER_API_KEY=... python3 probe.py
"""
import json
import os
import re
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost, estimated_cost  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
# REP2: the ONLY line changed from the v1 probe.py — the input-data path points at this run's
# frozen rep2 items (lexical_rep2_fulltext.jsonl), not v1's. All behavioral logic below (the
# three framing system prompts, guillemet item rendering, parsing, temperature-0 panel loop) is
# byte-identical to v1. This also removes the item-id collision hazard the pre-run critic flagged:
# v1 and rep2 both number items lx-{level}-{idx}, so a shared input filename could silently join
# v1 predictions to rep2 gold; a rep2-specific input file makes that impossible.
FULLTEXT = os.path.abspath(os.path.join(HERE, "..", "..", "data", "dwug",
                                        "lexical_rep2_fulltext.jsonl"))
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
TOPIC_SYS = (
    "You will see two sentences. One word is marked with «guillemets». IGNORING that marked "
    "word entirely, rate how similar the overall TOPIC, SITUATION, and content of the two "
    "sentences are, on a 0-100 scale (100 = same situation/topic, 0 = completely different "
    "topics). Judge everything EXCEPT the marked word. Answer with a single integer from 0 to "
    "100 and nothing else."
)


def mark(ctx, span):
    a, b = span
    return ctx[:a] + "«" + ctx[a:b] + "»" + ctx[b:]


def user(it):
    lemma = it["lemma"].split("_")[0]
    s1 = mark(it["ctx1"], it["span1"])
    s2 = mark(it["ctx2"], it["span2"])
    return (f"Target word: {lemma}\nSentence 1: {s1}\nSentence 2: {s2}\n")


def parse_durel(c):
    if not c:
        return None
    d = re.findall(r"[1-4]", c)
    return int(d[-1]) if d else None


def parse_int(c):
    if not c:
        return None
    m = re.findall(r"\d+", c)
    if not m:
        return None
    v = int(m[0])
    return max(0, min(100, v))


FRAMINGS = {"durel": (DUREL_SYS, parse_durel),
            "cont": (CONT_SYS, parse_int),
            "topic": (TOPIC_SYS, parse_int)}


def run(framing, items, slot, model):
    sys_prompt, parse = FRAMINGS[framing]
    recs = []
    for it in items:
        r = call(model, sys_prompt, user(it))
        recs.append({"item_id": it["item_id"], "lemma": it["lemma"], "framing": framing,
                     "pred": parse(r.get("content")), "raw": r.get("content"),
                     "human_median": it["human_median"], "human_n": it["human_n"],
                     "error": r.get("error"), "usage": r.get("usage")})
    os.makedirs(RAW, exist_ok=True)
    json.dump(recs, open(os.path.join(RAW, f"{framing}_{slot}.json"), "w"), indent=1)
    return recs


def main():
    items = [json.loads(l) for l in open(FULLTEXT, encoding="utf-8")]
    print(f"{len(items)} items (first id={items[0]['item_id']})")
    summary, total = {}, 0.0
    for slot, model in PANEL.items():
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        allrecs = []
        for framing in FRAMINGS:
            allrecs.append(run(framing, items, slot, model))
        billed, have, missing = billed_cost(allrecs)
        total += billed
        summary[slot] = {"model": model, "n_calls": sum(len(r) for r in allrecs),
                         "cost_usd_billed": round(billed, 5),
                         "cost_usd_estimate": round(estimated_cost(allrecs, model), 5),
                         "n_cost_missing": missing,
                         "elapsed_s": round(time.time() - t0, 1),
                         "na": {fr: sum(1 for r in rs if r["pred"] is None)
                                for fr, rs in zip(FRAMINGS, allrecs)}}
        print(json.dumps(summary[slot], indent=1))
    json.dump(summary, open(os.path.join(RAW, "run_summary.json"), "w"), indent=1)
    print(f"\nTOTAL billed cost: ${total:.5f}")


if __name__ == "__main__":
    main()
