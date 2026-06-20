#!/usr/bin/env python3
"""probe.py — panel NLI labels on the Scivetti CxNLI Exp-1 test set (the ONLY API caller).

Run 2026-06-20-scivetti-cxnli-answer-key. Zero-shot 3-way NLI (entailment/neutral/
contradiction) on the full 390-item human-annotated test set, scored against the
per-item gold label, across the three-model panel. This is the long-deferred
ANSWER-KEY comparison the resource page flagged ("the next step is to actually run a
probe... compare panel-model NLI labels against the per-item gold labels and report
against the aggregate ~0.90 human baseline").

NO new operationalization: the NLI instrument (NLI_SYS + parse_nli) is REUSED VERBATIM
from conative-cancel-probe-v2 / conative-preference-commitment-v1, and the 0/1/2 label
scheme is exactly the dataset's own. The items are the FULL released test set (zero
item-selection latitude — no cheat surface), and the gold labels are NOT shown to the
model. Anchor ratified 2026-05-29 (Tom); no decision is owed.

Settings: temperature 0; gemini (slot C) reasoning effort minimal; max_tokens default
(64 A/B, 4096 google/* via the lib). FREEZE GUARD: refuses to run unless PREREG.md and
analyze.py exist AND prep.py --check confirms the upstream sha still matches the frozen
manifest. ABORT_USD = 0.60 (pre-flight ~ $0.20-0.25).

Recipe-not-corpus: raw/ stores item_id + construction + gold + model label + usage
ONLY — never the premise/hypothesis text (that stays gitignored).

Usage: OPENROUTER_API_KEY=... python3 probe.py [--model A|B|C]
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402
from prep import SRC, parse_items, canonical_sha, assert_balance  # noqa: E402

HERE = Path(__file__).parent
RAW = HERE / "raw"
RAW.mkdir(exist_ok=True)

ABORT_USD = 0.60  # single-run flag; pre-flight ~ $0.20-0.25. Far under $5.00/day.

# ---- NLI instrument: REUSED VERBATIM from conative-cancel-probe-v2/probe.py ----
NLI_SYS = (
    "You are an expert annotator for Natural Language Inference (NLI). Given a "
    "Premise and a Hypothesis, determine the inference relation:\n"
    "0 - entailment - the hypothesis must be true given the premise\n"
    "1 - neutral - the hypothesis may or may not be true given the premise\n"
    "2 - contradiction - the hypothesis must not be true given the premise\n"
    "Output a single digit 0, 1, or 2 and nothing else."
)


def parse_nli(c):
    """VERBATIM from conative-cancel-probe-v2: last 0/1/2 digit."""
    if not c:
        return None
    digs = re.findall(r"[012]", c)
    return digs[-1] if digs else None


def load_frozen_items():
    """Read items from the gitignored source and assert the sha still matches the
    frozen manifest — the upstream data must not have drifted since freeze."""
    items = parse_items(SRC.resolve())
    assert_balance(items)
    sha = canonical_sha(items)
    frozen = json.load(open(HERE / "stimuli-manifest.json"))
    if sha != frozen["sha256"]:
        sys.exit(f"FATAL: sha mismatch (recomputed {sha[:16]} != frozen "
                 f"{frozen['sha256'][:16]}). Upstream data drifted; do NOT run.")
    return items


def ask(slot, system, user):
    kwargs = {}
    if slot == "C":
        kwargs["reasoning"] = {"effort": "minimal"}
    return call(PANEL[slot], system, user, temperature=0, **kwargs)


def run_model(slot, items, records):
    out = RAW / f"{slot}-nli.json"
    if out.exists():
        print(f"skip {out} (exists)")
        return
    rows = []
    for i, it in enumerate(items):
        user = f"Premise: {it['premise']}\nHypothesis: {it['hyp']}\nRelation:"
        r = ask(slot, NLI_SYS, user)
        val = parse_nli(r["content"])
        if val is None and not r.get("error"):
            r = ask(slot, NLI_SYS, user)  # one verbatim retry, then missing
            val = parse_nli(r["content"])
        # raw stores NO source text — item identity + gold + model label only.
        rows.append({"item_id": f"{it['cxn']}#{it['num']}", "cxn": it["cxn"],
                     "gold": it["gold"], "raw": r["content"], "value": val,
                     "usage": r.get("usage"), "error": r.get("error")})
        records.append(r)
        if (i + 1) % 30 == 0:
            c, _, nmiss = billed_cost([records])
            print(f"  {slot}: {i+1}/{len(items)} cost so far ${c:.4f}"
                  + (f" ({nmiss} missing usage.cost)" if nmiss else ""), flush=True)
            if c >= ABORT_USD:
                json.dump(rows, open(str(out) + ".partial", "w"), indent=1)
                print(f"ABORT: single-run flag ${ABORT_USD} reached; wrote "
                      f"{out}.partial", flush=True)
                sys.exit(1)
        time.sleep(0.1)
    json.dump(rows, open(out, "w"), indent=1)
    miss = sum(1 for x in rows if x["value"] is None)
    print(f"{slot}: {len(rows)} rows, {miss} missing -> {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["A", "B", "C"], default=None)
    args = ap.parse_args()
    # ---- FREEZE GUARD ----
    if not (HERE / "PREREG.md").exists():
        sys.exit("FATAL: PREREG.md not found — pre-registration not frozen. "
                 "PREREG-draft.md must pass a FRESH independent pre-run critic GO and "
                 "be committed as PREREG.md before any model call.")
    if not (HERE / "analyze.py").exists():
        sys.exit("FATAL: analyze.py not found — analysis code must exist at freeze time.")
    # Re-verify the upstream sha against the frozen manifest before spending.
    subprocess.run([sys.executable, str(HERE / "prep.py"), "--check"], check=True)
    items = load_frozen_items()
    slots = [args.model] if args.model else ["A", "B", "C"]
    records = []
    for slot in slots:
        run_model(slot, items, records)
    total, _, n_missing_cost = billed_cost([records])
    print(f"TOTAL billed this invocation: ${total:.4f}")
    if n_missing_cost:
        print(f"WARNING: {n_missing_cost} call(s) reported no usage.cost — the billed "
              f"total above UNDERCOUNTS; flag in the budget ledger.")
    with open(RAW / "cost-log.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} "
                f"slots={slots} billed=${total:.4f} "
                f"missing_cost_calls={n_missing_cost}\n")


if __name__ == "__main__":
    main()
