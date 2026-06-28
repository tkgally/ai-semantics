"""Add-arm headroom calibration probe (2026-06-28, session 133).

Operationalizes PREREG.md on the project's OWN frozen stimuli
(experiments/data/addarm-headroom-calibration/items.csv, sha256[:16] 471a5940ba8f65ff,
frozen by build_items.py BEFORE this runs). Behavioral NLI + forced-choice, temperature 0,
the 3-family behavioral panel (config/models.md). Records ACTUAL billed usage.cost via
experiments/lib/openrouter.py.

Indicator: affirm-the-added-entailment rate (NLI label 0 = entailment; FC YES). The
headroom question is whether the CONTROL arm (bare default) already supplies the entailment
the CONSTRUCTION arm licenses -- see PREREG.md for the frozen reading rule.

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
                                     "addarm-headroom-calibration", "items.csv"))
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
# gemini-3.5-flash rejects full reasoning suppression (HTTP 400); use minimal (NEXT.md).
REASONING = {"C": {"effort": "minimal"}}


def load_items():
    return list(csv.DictReader(open(ITEMS)))


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


def nli_user(it):
    return f"Premise: {it['sentence']}\nHypothesis: {it['nli_hypothesis']}\nRelation:"


def fc_user(it):
    return (f"Sentence: {it['sentence']}\nQuestion: Based only on the sentence, is the "
            f"following statement true: \"{it['nli_hypothesis']}\" Answer YES, NO, or "
            f"CANT_TELL.")


def run(arm, sys_prompt, items, slot, model, make_user, parse, reasoning):
    recs = []
    for it in items:
        r = call(model, sys_prompt, make_user(it), reasoning=reasoning)
        recs.append({"item_id": it["item_id"], "construction": it["construction"],
                     "stem": it["stem"], "condition": it["condition"],
                     "pred": parse(r.get("content")), "raw": r.get("content"),
                     "error": r.get("error"), "usage": r.get("usage")})
    os.makedirs(RAW, exist_ok=True)
    json.dump(recs, open(os.path.join(RAW, f"{arm}_{slot}.json"), "w"), indent=1)
    return recs


def main():
    items = load_items()
    print(f"{len(items)} items; ITEMS sha check recommended before run")
    summary, all_recs = {}, []
    for slot, model in PANEL.items():
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        reasoning = REASONING.get(slot)
        nli = run("nli", NLI_SYS, items, slot, model, nli_user, parse_nli, reasoning)
        fc = run("fc", FC_SYS, items, slot, model, fc_user, parse_fc, reasoning)
        all_recs += [nli, fc]
        billed, have, missing = billed_cost([nli, fc])
        est = estimated_cost([nli, fc], model)
        summary[slot] = {"model": model, "n_calls": len(nli) + len(fc),
                         "billed_usd": round(billed, 5), "cost_have": have,
                         "cost_missing": missing, "est_usd": round(est, 5),
                         "elapsed_s": round(time.time() - t0, 1),
                         "nli_na": sum(1 for r in nli if r["pred"] is None),
                         "fc_na": sum(1 for r in fc if r["pred"] is None)}
        print(json.dumps(summary[slot], indent=1))
    total, have, missing = billed_cost(all_recs)
    summary["_total"] = {"billed_usd": round(total, 5), "cost_have": have,
                         "cost_missing": missing}
    json.dump(summary, open(os.path.join(RAW, "run_summary.json"), "w"), indent=1)
    print(f"\nTOTAL billed: ${total:.5f}  ({have} priced, {missing} missing)")


if __name__ == "__main__":
    main()
