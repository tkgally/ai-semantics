#!/usr/bin/env python3
"""probe.py -- the function-word-vs-content-word swap NLI probe.

Indicator (ratified decision Q2 Option (i)): entailment-flip rate. NLI instrument REUSED
VERBATIM from the CxNLI / conative-cancel line (0=entailment, 1=neutral, 2=contradiction;
single-digit output). Per matched item, 3 finding-bearing NLI calls per model:
  (premise_base, hyp_base)  -> base label  [manipulation check: == pred_base?]
  (premise_fn,   hyp_base)  -> function-swap label;  flip_fn = (!= base label)
  (premise_ct,   hyp_ct)    -> content-swap label;   flip_ct = (!= base label)
det_char items: 2 calls (base, fn) -- function-only determiner arm, no content control.

PRIMARY contrast (per model): mean(flip_fn) - mean(flip_ct) over matched items.
Falsify arm (binding): content flip rate >= function flip rate is a clean positive for the
distributional camp -- recorded, no item re-selection after outputs.

FREEZE GUARD: refuses `full` unless PREREG.md exists AND records stimuli.json's sha256, AND
an independent pre-run-critic GO is recorded. Pre-flight + ABORT budget gate below.
"""
import argparse
import hashlib
import json
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

RAW = os.path.join(HERE, "raw")
os.makedirs(RAW, exist_ok=True)
STIM = os.path.join(HERE, "stimuli.json")
PREREG = os.path.join(HERE, "PREREG.md")

MODELS = {"claude": PANEL["A"], "gpt": PANEL["B"], "gemini": PANEL["C"]}
ABORT_USD = 1.00   # single-run flag (pre-flight ~ $0.45-0.70 for 80 items; far under $2.50)

# ---- NLI instrument: REUSED VERBATIM from the CxNLI / conative-cancel-v2 line ----
NLI_SYS = (
    "You are an expert annotator for Natural Language Inference (NLI). Given a "
    "Premise and a Hypothesis, determine the inference relation:\n"
    "0 - entailment - the hypothesis must be true given the premise\n"
    "1 - neutral - the hypothesis may or may not be true given the premise\n"
    "2 - contradiction - the hypothesis must not be true given the premise\n"
    "Output a single digit 0, 1, or 2 and nothing else."
)
import re  # noqa: E402


def parse_nli(c):
    """VERBATIM: last 0/1/2 digit."""
    if not c:
        return None
    digs = re.findall(r"[012]", c)
    return digs[-1] if digs else None


def ask(slot, premise, hyp):
    kwargs = {}
    if slot == "C":
        kwargs["reasoning"] = {"effort": "minimal"}
    user = f"Premise: {premise}\nHypothesis: {hyp}\nRelation:"
    r = call(PANEL[slot], NLI_SYS, user, temperature=0, **kwargs)
    val = parse_nli(r["content"])
    if val is None and not r.get("error"):
        r = call(PANEL[slot], NLI_SYS, user, temperature=0, **kwargs)
        val = parse_nli(r["content"])
    return val, r


def conditions(it):
    """Yield (cond, premise, hyp) for an item."""
    yield "base", it["premise_base"], it["hyp_base"]
    yield "fn", it["premise_fn"], it["hyp_base"]
    if it["arm"] == "matched":
        yield "ct", it["premise_ct"], it["hyp_ct"]


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
    held = ("The visitor signed the form because the office had reopened.",
            "The office reopening is the reason the visitor signed the form.")
    print("LIVENESS (one NLI call per model; all must parse a 0/1/2):")
    recs = []
    for name, slot in (("claude", "A"), ("gpt", "B"), ("gemini", "C")):
        val, r = ask(slot, *held)
        recs.append(r)
        print(f"  {name}: {val} {'OK' if val is not None else 'PARSE-FAIL ' + repr(r.get('content'))}")
    c, _, miss = billed_cost([recs])
    print(f"  billed ${c:.5f} ({miss} missing usage.cost)")


def full(slots):
    require_frozen()
    items = json.load(open(STIM))["items"]
    records = []
    for slot in slots:
        name = {"A": "claude", "B": "gpt", "C": "gemini"}[slot]
        out = os.path.join(RAW, f"{name}-nli.json")
        if os.path.exists(out):
            print(f"skip {name} (exists)")
            records += [{"usage": r["usage"]} for r in json.load(open(out)) if r.get("usage")]
            continue
        rows = []
        for i, it in enumerate(items):
            for cond, premise, hyp in conditions(it):
                val, r = ask(slot, premise, hyp)
                rows.append({"id": it["id"], "arm": it["arm"], "ftype": it["ftype"],
                             "pos": it["pos"], "cond": cond, "value": val,
                             "pred_base": it["pred_base"], "pred_fn": it["pred_fn"],
                             "usage": r.get("usage"), "error": r.get("error"),
                             "raw": r.get("content")})
                records.append(r)
            if (i + 1) % 25 == 0:
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
