#!/usr/bin/env python3
"""probe.py -- the SECOND-INSTRUMENT forced-choice modal-force preference probe.

Indicator: a single-letter (A/B) forced choice between a STRONG modal-force paraphrase and
a HEDGE one. SAME single-token output channel as the NLI run (no working surface -> controls
the output-channel confound the project mapped), DIFFERENT question type (graded modal-force
preference, not 3-way entailment). Per item, 3 finding-bearing calls per model:
  (premise_base) -> base letter   [manip check: base should prefer STRONG]
  (premise_fn)   -> fn letter;     shift_fn = picked_hedge(fn) - picked_hedge(base)
  (premise_ct)   -> ct letter;     shift_ct = picked_hedge(ct) - picked_hedge(base)  [control]

PRIMARY per-arm signal (per model): mean(shift_fn). Instrument-validity anchor = the `must`
arm (NLI flipped it at ceiling; a sensitive instrument must register it). Target = the `will`
arm (NLI near-null). Falsify/control: mean(shift_ct) (modal unchanged) predicted ~0.

FREEZE GUARD: refuses `full` unless PREREG.md exists, records stimuli.json's sha256, and a
pre-run-critic GO is recorded. ABORT budget gate below.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

RAW = os.path.join(HERE, "raw")
os.makedirs(RAW, exist_ok=True)
STIM = os.path.join(HERE, "stimuli.json")
PREREG = os.path.join(HERE, "PREREG.md")

ABORT_USD = 0.80   # single-run flag; pre-flight ~$0.10-0.25 for 58 items x 3 calls x 3 models

FC_SYS = (
    "You are an expert annotator of meaning. You will read a sentence and two descriptions, "
    "A and B, of how the sentence presents an action or event. Choose the description that "
    "better fits the sentence. Output a single letter, A or B, and nothing else."
)


def parse_fc(c):
    """Last standalone A or B letter (case-insensitive)."""
    if not c:
        return None
    m = re.findall(r"\b([AB])\b", c.strip().upper())
    if m:
        return m[-1]
    m = re.findall(r"[AB]", c.strip().upper())
    return m[-1] if m else None


def ask(slot, premise, optA, optB):
    kwargs = {}
    if slot == "C":
        kwargs["reasoning"] = {"effort": "minimal"}
    user = (f"Sentence: {premise}\n"
            f"A. {optA}\n"
            f"B. {optB}\n"
            f"Which description better fits the sentence? Answer A or B:")
    r = call(PANEL[slot], FC_SYS, user, temperature=0, **kwargs)
    val = parse_fc(r["content"])
    if val is None and not r.get("error"):
        r = call(PANEL[slot], FC_SYS, user, temperature=0, **kwargs)
        val = parse_fc(r["content"])
    return val, r


def conditions(it):
    yield "base", it["premise_base"]
    yield "fn", it["premise_fn"]
    yield "ct", it["premise_ct"]


def require_frozen():
    if not os.path.exists(PREREG):
        sys.exit("REFUSING: PREREG.md absent. Freeze after the independent pre-run critic GO.")
    sha = hashlib.sha256(open(STIM, "rb").read()).hexdigest()
    txt = open(PREREG).read()
    if sha not in txt:
        sys.exit(f"REFUSING: stimuli.json sha {sha} not recorded in PREREG.md (drift).")
    if "PRE-RUN CRITIC: GO" not in txt:
        sys.exit("REFUSING: no 'PRE-RUN CRITIC: GO' recorded in PREREG.md.")
    return sha


def liveness():
    it = json.load(open(STIM))["items"][0]
    print("LIVENESS (one forced-choice call per model; all must parse A/B):")
    recs = []
    for name, slot in (("claude", "A"), ("gpt", "B"), ("gemini", "C")):
        val, r = ask(slot, it["premise_base"], it["optA"], it["optB"])
        recs.append(r)
        print(f"  {name}: {val} {'OK' if val else 'PARSE-FAIL ' + repr(r.get('content'))}")
    c, _, miss = billed_cost([recs])
    print(f"  billed ${c:.5f} ({miss} missing usage.cost)")


def full(slots):
    require_frozen()
    items = json.load(open(STIM))["items"]
    records = []
    for slot in slots:
        name = {"A": "claude", "B": "gpt", "C": "gemini"}[slot]
        out = os.path.join(RAW, f"{name}-fc.json")
        if os.path.exists(out):
            print(f"skip {name} (exists)")
            records += [{"usage": r["usage"]} for r in json.load(open(out)) if r.get("usage")]
            continue
        rows = []
        for i, it in enumerate(items):
            for cond, premise in conditions(it):
                val, r = ask(slot, premise, it["optA"], it["optB"])
                rows.append({"id": it["id"], "ftype": it["ftype"], "cond": cond,
                             "value": val, "hedge_letter": it["hedge_letter"],
                             "usage": r.get("usage"), "error": r.get("error"),
                             "raw": r.get("content")})
                records.append(r)
            if (i + 1) % 15 == 0:
                c, _, nmiss = billed_cost([records])
                print(f"  {name}: {i+1}/{len(items)} items, ${c:.4f}"
                      + (f" ({nmiss} missing)" if nmiss else ""), flush=True)
                if c >= ABORT_USD:
                    json.dump(rows, open(out + ".partial", "w"), indent=1)
                    sys.exit(f"ABORT: ${ABORT_USD} single-run flag reached; wrote {out}.partial")
            time.sleep(0.05)
        json.dump(rows, open(out, "w"), indent=1)
        miss = sum(1 for x in rows if x["value"] is None)
        print(f"{name}: {len(rows)} rows, {miss} unparsed -> {out}")
    total, _, nmiss = billed_cost([records])
    print(f"TOTAL billed this invocation: ${total:.4f}" + (f" ({nmiss} missing usage.cost)" if nmiss else ""))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("phase", choices=["liveness", "full"])
    ap.add_argument("--model", choices=["A", "B", "C"], default=None)
    a = ap.parse_args()
    if a.phase == "liveness":
        liveness()
    else:
        full([a.model] if a.model else ["A", "B", "C"])
