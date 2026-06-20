#!/usr/bin/env python3
"""probe.py — panel NLI labels on the let-alone + comp-correlative subset under a
WORKING-SURFACE response format (the ONLY API caller).

Run 2026-06-20-scivetti-let-alone-working-surface. FORMAT-ONLY follow-up to session 57
(2026-06-20-scivetti-cxnli-answer-key). The single manipulated variable vs the paired
baseline is the RESPONSE FORMAT:

    baseline (session 57): "Output a single digit 0, 1, or 2 and nothing else."  (forced)
    this run:              "Think it through step by step. Then ... FINAL: <0,1,2>"  (working surface)

EVERYTHING ELSE IS HELD BYTE-IDENTICAL TO SESSION 57:
  * items: the SAME 24 let-alone + 30 comp-correlative test items (subset sha verified
    against the frozen manifest; full-set sha verified == session 57's 1c5cffb18c5ef78e);
  * the 0/1/2 NLI label DEFINITIONS (the three lines) are copied verbatim from session
    57's NLI_SYS — only the trailing output-instruction line differs;
  * 0/1/2 scored against the same per-item gold (gold NOT shown to the model);
  * temperature 0; gemini (slot C) reasoning effort minimal -- the reasoning-effort knob
    is HELD CONSTANT so the contrast isolates the OUTPUT CHANNEL, not the reasoning
    budget (exactly as the 2026-06-19 working-surface witness re-run did).

NO new operationalization decision: this is a format/instrument extension under the
already-ratified Scivetti answer-key anchor (ratified 2026-05-29) and the
constructional-divergence-operationalization decision. It does NOT alter WHAT is scored
against the human gold (same labels, same gold) -- only HOW the label is produced.
Precedent: the 2026-06-19 working-surface re-run was "format-only ... no new decision
owed" (budget ledger). A FRESH independent pre-run critic must confirm GO before the
PREREG.md freeze.

RECIPE-NOT-CORPUS: the working-surface CoT RESTATES the unlicensed premise/hypothesis
text, so the full CoT is written to raw/cot/ (gitignored). The COMMITTED artifact is
raw/{slot}-labels.json: item_id + cxn + gold + parsed label + parse_mode + a sha256 of
the CoT content + usage -- NEVER any source or model-restated text.

Settings: max_tokens 1024 (A/B; room for a short rationale + FINAL tag), 4096 (C/google,
lib default). FREEZE GUARD: refuses to run unless PREREG.md and analyze.py exist AND
prep.py --check confirms the subset + full-set sha still match. ABORT_USD = 0.80
(pre-flight ~ $0.15-0.35; far under the daily cap and the $2.50 single-run flag).

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
from prep import SRC, parse_items, subset_items, subset_sha, fullset_sha, assert_balance  # noqa: E402

HERE = Path(__file__).parent
RAW = HERE / "raw"
COT = RAW / "cot"
RAW.mkdir(exist_ok=True)
COT.mkdir(exist_ok=True)

ABORT_USD = 0.80  # single-run flag; pre-flight ~ $0.15-0.35. Far under $5.00/day.

# ---- NLI instrument: WORKING SURFACE. The 0/1/2 definition lines are VERBATIM from
# session-57 NLI_SYS; ONLY the trailing output instruction changed (forced single digit
# -> step-by-step then a FINAL: tag). This is the single manipulated variable. ----
NLI_SYS_WS = (
    "You are an expert annotator for Natural Language Inference (NLI). Given a "
    "Premise and a Hypothesis, determine the inference relation:\n"
    "0 - entailment - the hypothesis must be true given the premise\n"
    "1 - neutral - the hypothesis may or may not be true given the premise\n"
    "2 - contradiction - the hypothesis must not be true given the premise\n"
    "Think it through step by step. Then, on the final line, output your answer in "
    "exactly this format:\n"
    "FINAL: <0, 1, or 2>"
)


def parse_ws(c):
    """Target-blind parse of a working-surface response. Prefer the FINAL: tag; fall
    back to the LAST 0/1/2 digit (same fallback discipline as session-57 parse_nli).
    Returns (label_str_or_None, parse_mode). Never peeks at the gold."""
    if not c:
        return None, "empty"
    m = re.search(r"FINAL:\s*\**\s*([012])", c, re.IGNORECASE)
    if m:
        return m.group(1), "tagged"
    digs = re.findall(r"[012]", c)
    if digs:
        return digs[-1], "fallback_lastdigit"
    return None, "no_digit"


def load_frozen_subset():
    items = parse_items(SRC.resolve())
    assert len(items) == 390
    fs = fullset_sha(items)
    frozen = json.load(open(HERE / "stimuli-manifest.json"))
    if fs != frozen["fullset_sha256"]:
        sys.exit(f"FATAL: full-set sha mismatch ({fs[:16]} != frozen "
                 f"{frozen['fullset_sha256'][:16]}). Upstream drifted; do NOT run.")
    sub = subset_items(items)
    assert_balance(sub)
    if subset_sha(sub) != frozen["subset_sha256"]:
        sys.exit("FATAL: subset sha mismatch; do NOT run.")
    return sub


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
    rows = []
    cot_rows = []
    for i, it in enumerate(items):
        user = f"Premise: {it['premise']}\nHypothesis: {it['hyp']}\nRelation:"
        r = ask(slot, NLI_SYS_WS, user)
        val, mode = parse_ws(r["content"])
        if val is None and not r.get("error"):
            r = ask(slot, NLI_SYS_WS, user)  # one retry, then missing
            val, mode = parse_ws(r["content"])
        content = r["content"] or ""
        csha = hashlib.sha256(content.encode("utf-8")).hexdigest()
        rows.append({"item_id": f"{it['cxn']}#{it['num']}", "cxn": it["cxn"],
                     "gold": it["gold"], "value": val, "parse_mode": mode,
                     "content_sha256": csha, "usage": r.get("usage"),
                     "error": r.get("error")})
        # CoT is gitignored (restates source text); kept for in-session verification.
        cot_rows.append({"item_id": f"{it['cxn']}#{it['num']}", "content": content})
        records.append(r)
        if (i + 1) % 18 == 0:
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
    modes = {}
    for x in rows:
        modes[x["parse_mode"]] = modes.get(x["parse_mode"], 0) + 1
    print(f"{slot}: {len(rows)} rows, {miss} missing, parse_modes={modes} -> {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["A", "B", "C"], default=None)
    args = ap.parse_args()
    # ---- FREEZE GUARD ----
    if not (HERE / "PREREG.md").exists():
        sys.exit("FATAL: PREREG.md not found — pre-registration not frozen. PREREG-draft.md "
                 "must pass a FRESH independent pre-run critic GO and be committed as "
                 "PREREG.md before any model call.")
    if not (HERE / "analyze.py").exists():
        sys.exit("FATAL: analyze.py not found — analysis code must exist at freeze time.")
    subprocess.run([sys.executable, str(HERE / "prep.py"), "--check"], check=True)
    items = load_frozen_subset()
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
