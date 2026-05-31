"""Lexical-v3 probe (2026-05-31) — the SAME ratified graded panel as v1, run on a
homonymy-enriched WiC noun subset. Two framings (durel 4-point + cont 0-100); the v1
`topic` control is dropped (design 3: clause c already supported by v1; v3 tests binary
separation by stratum, not a context shadow). Temperature 0, logprob-free, 3-family panel.

Reads the gitignored fulltext.jsonl (WiC corpus sentences, NOT committed). Commits raw
records: item_id + wic_id + stratum + gold + framing + model pred + usage. NO sentences.
Cost = API-billed usage.cost (experiments/lib/openrouter.py).

PREFLIGHT: `python3 probe.py --preflight 30` runs only the first 30 items (durel+cont) on
all 3 models and prints projected full cost; per design 6/7, drop to durel-only if it
projects > $5 and flag in NEXT.md.

Run: OPENROUTER_API_KEY=... python3 probe.py        (full)
     OPENROUTER_API_KEY=... python3 probe.py --preflight 30
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
FULLTEXT = os.path.join(HERE, "fulltext.jsonl")
RAW = os.path.join(HERE, "raw")

# verbatim from the v1 probe (gate Q1 instrument; do not alter)
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


def mark(ctx, idx):
    toks = ctx.split(" ")
    if 0 <= idx < len(toks):
        toks[idx] = "«" + toks[idx] + "»"
    return " ".join(toks)


def user(it):
    s1 = mark(it["ctx1"], it["idx1"])
    s2 = mark(it["ctx2"], it["idx2"])
    return f"Target word: {it['lemma']}\nSentence 1: {s1}\nSentence 2: {s2}\n"


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
    return max(0, min(100, int(m[0])))


FRAMINGS = {"durel": (DUREL_SYS, parse_durel), "cont": (CONT_SYS, parse_int)}


def run(framing, items, slot, model, tag=""):
    sys_prompt, parse = FRAMINGS[framing]
    recs = []
    for it in items:
        r = call(model, sys_prompt, user(it))
        recs.append({"item_id": it["item_id"], "wic_id": it["wic_id"],
                     "lemma": it["lemma"], "stratum": it["stratum"], "gold": it["gold"],
                     "framing": framing, "pred": parse(r.get("content")),
                     "raw": r.get("content"), "error": r.get("error"),
                     "usage": r.get("usage")})
    os.makedirs(RAW, exist_ok=True)
    json.dump(recs, open(os.path.join(RAW, f"{tag}{framing}_{slot}.json"), "w"), indent=1)
    return recs


def main():
    items = [json.loads(l) for l in open(FULLTEXT, encoding="utf-8")]
    preflight_n = None
    tag = ""
    if "--preflight" in sys.argv:
        preflight_n = int(sys.argv[sys.argv.index("--preflight") + 1])
        items = items[:preflight_n]
        tag = "preflight_"
    print(f"{len(items)} items{' (PREFLIGHT)' if preflight_n else ''}")
    summary, total = {}, 0.0
    for slot, model in PANEL.items():
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        allrecs = [run(fr, items, slot, model, tag) for fr in FRAMINGS]
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
    json.dump(summary, open(os.path.join(RAW, f"{tag}run_summary.json"), "w"), indent=1)
    print(f"\nTOTAL billed: ${total:.5f}")
    if preflight_n:
        full_n = sum(1 for _ in open(FULLTEXT, encoding="utf-8"))
        proj = total * full_n / preflight_n
        print(f"PROJECTED full ({full_n} items, 2 framings, 3 models): ${proj:.4f}")
        if proj > 5:
            print("  ** PROJECTION > $5 — drop to durel-only and flag in NEXT.md (design 6) **")


if __name__ == "__main__":
    main()
