"""Caused-motion NEAR-MISS FORM-CONTROL probe (v2c, 2026-05-30).

Runs the near-miss form-control arm deferred by design/argument-structure-coercion-v2 (s3d),
under the ratified cc-v2-difficulty-operationalization gate (no new decision). Uses the
project's OWN frozen stimuli (experiments/data/caused-motion-near-miss-v2c/items.csv, built by
build_items.py BEFORE this runs; sha256[:16] 6d0b92e39b2d9eb8). Behavioral NLI + forced-choice,
temperature 0, NO logprobs -> existing 3-family panel. Internal-contrast-only.

Instrument (reused verbatim from the caused-motion v1/v2b harness):
  NLI: premise = sentence, hypothesis = "<Subj>'s <gerund> caused <obj> to move." -> 0/1/2
  FC : "is the following statement true: '<hypothesis>'?" -> YES / NO / CANT_TELL

Cost is the API-BILLED usage.cost (via experiments/lib/openrouter.py), not a rate-card estimate.

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
ITEMS = os.path.abspath(os.path.join(HERE, "..", "..", "data",
                                     "caused-motion-near-miss-v2c", "items.csv"))
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


def parse_nli(c):
    if not c:
        return None
    digs = re.findall(r"[012]", c)
    return digs[-1] if digs else None


def parse_fc(c):
    if not c:
        return None
    u = c.upper()
    if "CANT" in u.replace("'", "") or "TELL" in u:
        return "CANT_TELL"
    if re.search(r"\bYES\b", u):
        return "YES"
    if re.search(r"\bNO\b", u):
        return "NO"
    return None


def nli_user(it):
    return f"Premise: {it['sentence']}\nHypothesis: {it['nli_hypothesis']}\nRelation:"


def fc_user(it):
    return (f"Sentence: {it['sentence']}\nQuestion: Based only on the sentence, is the "
            f"following statement true: \"{it['nli_hypothesis']}\" Answer YES, NO, or CANT_TELL.")


def run(arm, sys_prompt, items, slot, model, make_user, parse):
    recs = []
    for it in items:
        r = call(model, sys_prompt, make_user(it))
        recs.append({"item_id": it["item_id"], "scene": it["scene"], "arm": it["arm"],
                     "difficulty": it["difficulty"], "affirm_gold": it["affirm_gold"],
                     "pred": parse(r.get("content")), "raw": r.get("content"),
                     "error": r.get("error"), "usage": r.get("usage")})
    os.makedirs(RAW, exist_ok=True)
    json.dump(recs, open(os.path.join(RAW, f"{arm}_{slot}.json"), "w"), indent=1)
    return recs


def main():
    items = list(csv.DictReader(open(ITEMS)))
    print(f"{len(items)} items (first id={items[0]['item_id']})")
    summary, total = {}, 0.0
    for slot, model in PANEL.items():
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        nli = run("nli", NLI_SYS, items, slot, model, nli_user, parse_nli)
        fc = run("fc", FC_SYS, items, slot, model, fc_user, parse_fc)
        billed, have, missing = billed_cost([nli, fc])
        total += billed
        summary[slot] = {"model": model, "n_calls": len(nli) + len(fc),
                         "cost_usd_billed": round(billed, 5),
                         "cost_usd_estimate": round(estimated_cost([nli, fc], model), 5),
                         "n_cost_missing": missing,
                         "elapsed_s": round(time.time() - t0, 1),
                         "nli_na": sum(1 for r in nli if r["pred"] is None),
                         "fc_na": sum(1 for r in fc if r["pred"] is None)}
        print(json.dumps(summary[slot], indent=1))
    json.dump(summary, open(os.path.join(RAW, "run_summary.json"), "w"), indent=1)
    print(f"\nTOTAL billed cost: ${total:.5f}")


if __name__ == "__main__":
    main()
