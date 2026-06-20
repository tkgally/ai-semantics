#!/usr/bin/env python3
"""probe.py — panel NLI labels on the POWERED let-alone set (33 = 24 test + 9 train) +
the 30-item comp-correlative ceiling control, under the FORCED-DECOMPOSITION working
surface (the ONLY API caller).

Run 2026-06-20-scivetti-let-alone-powered-rerun. The trigger-(g) POWERED re-run of session
60 (2026-06-20-scivetti-let-alone-forced-decomposition). The forced-decomposition INSTRUMENT
is held BYTE-IDENTICAL to session 60 — NLI_SYS_DECOMP below is copied verbatim from that
run's probe.py. The ONLY change is the ITEM SET: the let-alone target grows 24 -> 33 with
the 9 DISJOINT let-alone items in the upstream TRAIN split (verified disjoint by prep.py),
giving a tighter Wilson CI vs the 0.90 human baseline and an internal replication of the
session-60 24-item result. The comp-correlative control is byte-identical to s57/58/60.

This is a powered re-run of the SAME axis after a directional-but-underpowered first run —
exempt from the "more of the same probe cannot" caution (essay/witness-seeking-economics
§"The partial witness"; essay/output-channel-confound trigger (b)) because session 60 left a
SIGNAL (gpt +0.21, below baseline), not a null.

RECIPE-NOT-CORPUS: the response RESTATES the unlicensed premise/hypothesis text, so the full
text is written to raw/cot/ (gitignored). The COMMITTED artifact is raw/{slot}-labels.json:
item_id + cxn + split + gold + parsed label + parse_mode + an UPTAKE metric (pre-FINAL char
length + step-marker presence; lengths/booleans only, NO text) + a sha256 of the content +
usage — NEVER any source or model-restated text.

Settings: max_tokens 1024 (A/B), default (C/google); temperature 0; gemini reasoning
effort minimal (held constant -> isolates the output channel, not the reasoning budget).
FREEZE GUARD: refuses to run unless PREREG.md and analyze.py exist AND prep.py --check
confirms the frozen + full-set + s60-subset + train shas still match. ABORT_USD = 0.80
(pre-flight ~$0.40-0.55; far under the $5.00/day cap and the $2.50 single-run flag).

Usage: OPENROUTER_API_KEY=... python3 probe.py [--model A|B|C]
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402
from prep import (TEST_SRC, TRAIN_SRC, parse_items, build_sets, assert_structure,  # noqa: E402
                  sha_over)

HERE = Path(__file__).parent
RAW = HERE / "raw"
COT = RAW / "cot"
RAW.mkdir(exist_ok=True)
COT.mkdir(exist_ok=True)

ABORT_USD = 0.80  # single-run flag; pre-flight ~$0.40-0.55. Far under $5.00/day.

# ---- NLI instrument: FORCED-DECOMPOSITION working surface. COPIED VERBATIM from session
# 60's probe.py (2026-06-20-scivetti-let-alone-forced-decomposition). This is the held-
# constant instrument; the manipulated variable in THIS run is the item set, not the
# format. ----
NLI_SYS_DECOMP = (
    "You are an expert annotator for Natural Language Inference (NLI). Given a "
    "Premise and a Hypothesis, determine the inference relation:\n"
    "0 - entailment - the hypothesis must be true given the premise\n"
    "1 - neutral - the hypothesis may or may not be true given the premise\n"
    "2 - contradiction - the hypothesis must not be true given the premise\n"
    "You MUST show your work. Before giving an answer, write out each of these three "
    "numbered steps, each on its own line:\n"
    "1. PREMISE: in your own words, what does the premise assert?\n"
    "2. HYPOTHESIS: in your own words, what does the hypothesis assert?\n"
    "3. LINK: does the premise's being true force the hypothesis to be true, leave it "
    "open, or force it to be false? Explain why.\n"
    "Only after writing all three steps, output the final line in exactly this format:\n"
    "FINAL: <0, 1, or 2>"
)

STEP_RE = re.compile(r"(?m)^\s*([123])[.)]")


def split_pre_final(c):
    m = re.search(r"FINAL:\s*\**\s*([012])", c, re.IGNORECASE)
    if m:
        return c[:m.start()], m
    return c, None


def uptake_metrics(content):
    pre, _ = split_pre_final(content or "")
    steps_present = sorted(set(STEP_RE.findall(content or "")))
    return {"pre_final_chars": len(pre.strip()),
            "step_markers": steps_present,
            "n_step_markers": len(steps_present),
            "worked": len(pre.strip()) >= 40 and len(steps_present) >= 2}


def parse_ws(c):
    if not c:
        return None, "empty"
    m = re.search(r"FINAL:\s*\**\s*([012])", c, re.IGNORECASE)
    if m:
        return m.group(1), "tagged"
    digs = re.findall(r"[012]", c)
    if digs:
        return digs[-1], "fallback_lastdigit"
    return None, "no_digit"


def load_frozen():
    test_items = parse_items(TEST_SRC.resolve(), "\t")
    train_items = parse_items(TRAIN_SRC.resolve(), ",")
    frozen, parts = build_sets(test_items, train_items)
    assert_structure(parts)
    man = json.load(open(HERE / "stimuli-manifest.json"))
    if sha_over(frozen) != man["frozen_sha256"]:
        sys.exit("FATAL: frozen sha mismatch; do NOT run.")
    if sha_over(test_items) != man["fullset_sha256"]:
        sys.exit("FATAL: full-set sha mismatch; upstream drifted; do NOT run.")
    return frozen


def ask(slot, system, user):
    kwargs = {"max_tokens": 1024} if slot in ("A", "B") else {}
    if slot == "C":
        kwargs["reasoning"] = {"effort": "minimal"}
    return call(PANEL[slot], system, user, temperature=0, **kwargs)


def run_model(slot, items, records):
    out = RAW / f"{slot}-labels.json"
    cot_out = COT / f"{slot}-cot.json"
    if out.exists():
        print(f"skip {out} (exists)")
        return
    rows, cot_rows = [], []
    for i, it in enumerate(items):
        user = f"Premise: {it['premise']}\nHypothesis: {it['hyp']}\nRelation:"
        r = ask(slot, NLI_SYS_DECOMP, user)
        val, mode = parse_ws(r["content"])
        if val is None and not r.get("error"):
            r = ask(slot, NLI_SYS_DECOMP, user)  # one retry, then missing
            val, mode = parse_ws(r["content"])
        content = r["content"] or ""
        csha = hashlib.sha256(content.encode("utf-8")).hexdigest()
        rows.append({"item_id": f"{it['cxn']}#{it['num']}", "cxn": it["cxn"],
                     "split": it.get("split", "test"), "gold": it["gold"],
                     "value": val, "parse_mode": mode,
                     "uptake": uptake_metrics(content),
                     "content_sha256": csha, "usage": r.get("usage"),
                     "error": r.get("error")})
        cot_rows.append({"item_id": f"{it['cxn']}#{it['num']}", "content": content})
        records.append(r)
        if (i + 1) % 21 == 0:
            c, _, nmiss = billed_cost([records])
            print(f"  {slot}: {i+1}/{len(items)} cost so far ${c:.4f}"
                  + (f" ({nmiss} missing usage.cost)" if nmiss else ""), flush=True)
            if c >= ABORT_USD:
                json.dump(rows, open(str(out) + ".partial", "w"), indent=1)
                json.dump(cot_rows, open(str(cot_out) + ".partial", "w"), indent=1)
                print(f"ABORT: single-run flag ${ABORT_USD} reached; wrote partials",
                      flush=True)
                sys.exit(1)
        time.sleep(0.1)
    json.dump(rows, open(out, "w"), indent=1)
    json.dump(cot_rows, open(cot_out, "w"), indent=1)
    miss = sum(1 for x in rows if x["value"] is None)
    la = [x for x in rows if x["cxn"] == "let-alone"]
    worked = sum(1 for x in la if x["uptake"]["worked"])
    modes = {}
    for x in rows:
        modes[x["parse_mode"]] = modes.get(x["parse_mode"], 0) + 1
    print(f"{slot}: {len(rows)} rows, {miss} missing, let-alone worked {worked}/{len(la)}, "
          f"parse_modes={modes} -> {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["A", "B", "C"], default=None)
    args = ap.parse_args()
    # ---- FREEZE GUARD ----
    if not (HERE / "PREREG.md").exists():
        sys.exit("FATAL: PREREG.md not found — pre-registration not frozen.")
    if not (HERE / "analyze.py").exists():
        sys.exit("FATAL: analyze.py not found — analysis code must exist at freeze time.")
    subprocess.run([sys.executable, str(HERE / "prep.py"), "--check"], check=True)
    items = load_frozen()
    slots = [args.model] if args.model else ["A", "B", "C"]
    records = []
    for slot in slots:
        run_model(slot, items, records)
    total, _, n_missing_cost = billed_cost([records])
    print(f"TOTAL billed this invocation: ${total:.4f}")
    if n_missing_cost:
        print(f"WARNING: {n_missing_cost} call(s) reported no usage.cost — billed total "
              f"UNDERCOUNTS; flag in the budget ledger.")
    with open(RAW / "cost-log.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} "
                f"slots={slots} billed=${total:.4f} missing_cost_calls={n_missing_cost}\n")


if __name__ == "__main__":
    main()
