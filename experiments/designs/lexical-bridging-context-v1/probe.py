"""Lexical bridging-context probe v1 runner (build session 2026-06-21; NOT yet run).

Operationalizes experiments/designs/lexical-bridging-context-v1.md under the two RESOLVED
gates (operationalization + anchor). Reads the FROZEN instrument config (instrument.json,
sha256'd in instrument.sha256 — the numeric-freeze hash) and the gitignored full-text
files staged by prep.py (DWUG) and prep_wic.py (WiC clear poles). Logprob-free; runs on
the existing 3-family panel (experiments/lib/openrouter.py / config/models.md).

FROZEN PANEL (no instrument added/dropped/re-worded/re-thresholded after any output —
operationalization condition a). All scales, bands, the third-option wording, A's sample
count + temperature, and the item classes live in instrument.json, NOT here, so this
runner carries no tunable knob: it only dispatches the frozen config.

  B (primary, temp 0):  b_rel  (0-100 relatedness = position axis, graded)
                        b_conf (SAME/DIFFERENT + 0-100 confidence = confidence axis)
  C (cross-check, t 0): c_third (SAME/DIFFERENT/UNCLEAR; decline rate = %UNCLEAR)
  A (characterizing,    a_forced (forced SAME/DIFFERENT; N stochastic samples at temp>0;
     temp 1.0):          dispersion = flip-rate/entropy — DESCRIBES, never DECIDES)
  Q3 control (temp 0):  topic  (0-100 topic similarity ignoring the target word)

DATA/LICENCE: reads the gitignored local full text (DWUG/CCOHA is CC BY-ND; WiC is
CC BY-NC). Committed raw records carry item_id + class + framing + model output + the
human pole label only — NO corpus sentences. Cost = API-billed usage.cost.

Reasoning is suppressed per model: every framing emits a short label or a single integer,
so reasoning tokens are pure cost (v1's lexical run billed gemini ~$2.61 over reasoning-heavy
calls — the known budget driver). The suppression MODE is model-dependent (2026-06-22 fix):
google/gemini-3.5-flash REJECTS reasoning={"enabled": False} with HTTP 400 ("Reasoning is
mandatory for this endpoint and cannot be disabled"), so gemini uses the project's documented
norm reasoning={"effort": "minimal"} (config/budget.md), while claude/gpt fully disable it.
This is a transport detail; it touches no FROZEN instrument number. The analysis is a SEPARATE
step (analyze.py); this runner only collects raw outputs.

Run (a LATER, spend-bearing session, after the pre-run-critic GO and a budget pre-flight):
    OPENROUTER_API_KEY=... python3 probe.py
    OPENROUTER_API_KEY=... PROBE_SLOTS=C python3 probe.py   # re-run only certain panel slots
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
INSTRUMENT = os.path.join(HERE, "instrument.json")
DWUG_FULLTEXT = os.path.abspath(os.path.join(
    HERE, "..", "..", "data", "dwug", "lexical_bridging_v1_fulltext.jsonl"))
WIC_FULLTEXT = os.path.abspath(os.path.join(
    HERE, "..", "..", "data", "wic", "wic_poles_fulltext.jsonl"))
RAW = os.path.join(HERE, "raw")


def reasoning_for(model):
    """Per-model reasoning suppression. google/* rejects {"enabled": False} (HTTP 400),
    so it uses the documented {"effort": "minimal"} norm; others fully disable reasoning."""
    return {"effort": "minimal"} if model.startswith("google/") else {"enabled": False}


def load_items():
    """DWUG stratum (required) + WiC clear-pole supplement (optional, if staged)."""
    items = []
    if not os.path.exists(DWUG_FULLTEXT):
        sys.exit(f"missing {DWUG_FULLTEXT} — run prep.py first (re-fetches DWUG).")
    with open(DWUG_FULLTEXT, encoding="utf-8") as f:
        for line in f:
            it = json.loads(line)
            it["source"] = "dwug"
            items.append(it)
    if os.path.exists(WIC_FULLTEXT):
        with open(WIC_FULLTEXT, encoding="utf-8") as f:
            for line in f:
                it = json.loads(line)
                it["source"] = "wic"
                items.append(it)
    else:
        print(f"NOTE: {WIC_FULLTEXT} absent — running DWUG-only "
              "(WiC clear-pole supplement not staged; the thin clear-same pole "
              "precondition is then at higher collapse risk).")
    return items


def mark(ctx, span):
    a, b = span
    return ctx[:a] + "«" + ctx[a:b] + "»" + ctx[b:]


def user(it):
    lemma = it["lemma"].split("_")[0]
    s1 = mark(it["ctx1"], it["span1"])
    s2 = mark(it["ctx2"], it["span2"])
    return f"Target word: {lemma}\nSentence 1: {s1}\nSentence 2: {s2}\n"


def parse_int100(c):
    if not c:
        return None
    m = re.findall(r"\d+", c)
    if not m:
        return None
    return max(0, min(100, int(m[0])))


def parse_call_conf(c):
    """b_conf: SAME/DIFFERENT call + 0-100 confidence. -> (call, conf)."""
    if not c:
        return None, None
    cu = c.upper()
    call_ = "SAME" if "SAME" in cu else ("DIFFERENT" if "DIFF" in cu else None)
    conf = parse_int100(c)
    return call_, conf


def parse_choice(c, opts):
    if not c:
        return None
    cu = c.upper()
    for o in opts:
        if o in cu:
            return o
    return None


def run_single(framing, sys_prompt, items, slot, model, parse):
    """One temp-0 call per item; parse stored under 'pred' (+ 'pred2' for b_conf)."""
    recs = []
    for it in items:
        r = call(model, sys_prompt, user(it), temperature=0, reasoning=reasoning_for(model))
        rec = {"item_id": it["item_id"], "lemma": it["lemma"],
               "bridging_class": it["bridging_class"], "source": it["source"],
               "framing": framing, "raw": r.get("content"),
               "human_median": it["human_median"], "error": r.get("error"),
               "usage": r.get("usage")}
        if framing == "b_conf":
            call_, conf = parse(r.get("content"))
            rec["pred"], rec["pred2"] = call_, conf
        else:
            rec["pred"] = parse(r.get("content"))
        recs.append(rec)
    return recs


def run_dispersion(framing, sys_prompt, items, slot, model, n_samples, temp, parse):
    """A (characterizing-only): n_samples stochastic forced picks per item."""
    recs = []
    for it in items:
        picks, usages, raws = [], [], []
        for _ in range(n_samples):
            r = call(model, sys_prompt, user(it), temperature=temp, reasoning=reasoning_for(model))
            picks.append(parse(r.get("content")))
            usages.append(r.get("usage"))
            raws.append(r.get("content"))
        recs.append({"item_id": it["item_id"], "lemma": it["lemma"],
                     "bridging_class": it["bridging_class"], "source": it["source"],
                     "framing": framing, "picks": picks, "raws": raws,
                     "human_median": it["human_median"],
                     "usage_list": usages})
    return recs


def main():
    cfg = json.load(open(INSTRUMENT, encoding="utf-8"))
    items = load_items()
    print(f"{len(items)} items "
          f"(dwug={sum(1 for i in items if i['source']=='dwug')}, "
          f"wic={sum(1 for i in items if i['source']=='wic')})")
    os.makedirs(RAW, exist_ok=True)

    B = cfg["instruments"]["B"]["framings"]
    C = cfg["instruments"]["C"]["framings"]
    A = cfg["instruments"]["A"]
    Q3 = cfg["instruments"]["Q3_context_control"]["framings"]
    c_opts = C["c_third"]["options"]

    # Optional slot filter (e.g. PROBE_SLOTS=C to re-run only gemini without re-spending
    # on already-collected A/B). Existing run_summary.json is merged, not clobbered.
    want = os.environ.get("PROBE_SLOTS")
    want_slots = set(want.split(",")) if want else set(PANEL)

    summary, total = {}, 0.0
    sumpath = os.path.join(RAW, "run_summary.json")
    if os.path.exists(sumpath):
        summary = json.load(open(sumpath, encoding="utf-8"))
    for slot, model in PANEL.items():
        if slot not in want_slots:
            continue
        print(f"\n=== panel.{slot} {model} ===")
        t0 = time.time()
        allrecs, disp_usage = [], []

        allrecs.append(run_single("b_rel", B["b_rel"]["system"], items, slot, model,
                                   parse_int100))
        allrecs.append(run_single("b_conf", B["b_conf"]["system"], items, slot, model,
                                   parse_call_conf))
        allrecs.append(run_single("c_third", C["c_third"]["system"], items, slot, model,
                                   lambda c: parse_choice(c, c_opts)))
        allrecs.append(run_single("topic", Q3["topic"]["system"], items, slot, model,
                                   parse_int100))
        for fr in allrecs:
            json.dump(fr, open(os.path.join(RAW, f"{fr[0]['framing']}_{slot}.json"), "w"),
                      indent=1)

        # A: characterizing-only dispersion (flatten usage for billing)
        a_recs = run_dispersion("a_forced", A["framings"]["a_forced"]["system"], items,
                                slot, model, A["n_samples"], A["temperature"],
                                lambda c: parse_choice(c, ["SAME", "DIFFERENT"]))
        json.dump(a_recs, open(os.path.join(RAW, f"a_forced_{slot}.json"), "w"), indent=1)
        disp_usage = [{"usage": u} for r in a_recs for u in r["usage_list"]]

        billed, have, missing = billed_cost(allrecs + [disp_usage])
        total += billed
        summary[slot] = {"model": model,
                         "n_calls": sum(len(r) for r in allrecs) + len(disp_usage),
                         "cost_usd_billed": round(billed, 5),
                         "n_cost_missing": missing,
                         "elapsed_s": round(time.time() - t0, 1)}
        print(json.dumps(summary[slot], indent=1))

    json.dump(summary, open(os.path.join(RAW, "run_summary.json"), "w"), indent=1)
    print(f"\nTOTAL billed cost: ${total:.5f}")


if __name__ == "__main__":
    main()
