#!/usr/bin/env python3
"""probe.py — REPEATED-RUN temp-0 jitter measurement (the ONLY API caller).

Run 2026-06-21-scivetti-let-alone-repeated-runs. Re-runs the BYTE-IDENTICAL session-60/62
forced-decomposition NLI instrument (NLI_SYS_DECOMP, copied verbatim) K times at temperature
0 over the SAME frozen 63-item set (24 let-alone test + 9 let-alone train + 30 comp-corr
ceiling control), to CHARACTERIZE the run-to-run label jitter session 62 surfaced as the new
binding limit (~12% inferred from a single s60->s62 run-pair). The ONLY change vs session 62
is that each item is scored K times instead of once; the instrument, item set, panel,
temperature, and gemini effort are all held constant.

WHY THIS IS A LICIT SAME-INSTRUMENT RE-RUN (essay/point-estimate-is-a-draw, the discipline +
trigger (a); essay/undischargeable-negative, the threaded needle): re-running the identical
hard instrument to "firm up" a null buys nothing (each failing run is one more exists-instance,
never the universal). But re-running to MEASURE THE NOISE FLOOR buys the floor itself — the one
quantity that tells you whether the project's small-effect point estimates were ever precise
enough to carry the differences read off them. This run measures the jitter; it does NOT try to
turn the let-alone null into a positive, and the verdict map (analyze.py, frozen) reports the
jitter distribution, not a pass/fail on the residual.

INDEPENDENCE: every one of the K x 3 x 63 calls is a fresh, independent HTTP request. Nothing
is cached or deduped; the WHOLE POINT is that two byte-identical requests can return different
labels at temperature 0. Runs are scored sequentially within ONE session, so the measured
jitter is a within-session figure; cross-session/cross-day jitter (as in the s60->s62 pair)
can be LARGER, so this run's spread is read as a lower bound on true run-to-run jitter and is
reported alongside the s60/s62 cross-session draws (analyze.py).

RECIPE-NOT-CORPUS: the response RESTATES the unlicensed premise/hypothesis text, so the full
CoT is written to raw/cot/ (gitignored). The COMMITTED artifact is raw/run{k}-{slot}-labels.json:
item_id + cxn + split + gold + parsed label + parse_mode + an UPTAKE metric (lengths/booleans
only, NO text) + a sha256 of the content + usage — NEVER any source or model-restated text.

Settings: max_tokens 1024 (A/B), default (C/google); temperature 0; gemini reasoning effort
minimal (held constant). FREEZE GUARD: refuses to run unless PREREG.md and analyze.py exist
AND prep.py --check confirms the frozen + full-set + s60-subset + train shas still match.
ABORT_USD = 2.40 (pre-flight ~$1.96 = K=5 x session-62's measured $0.392/run; under the $2.50
single-run flag and well under the $5.00/day cap with $0 spent so far this UTC day).

Usage: OPENROUTER_API_KEY=... python3 probe.py [--model A|B|C] [--run K]
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

K = 5  # number of independent same-session draws per (slot, item)
ABORT_USD = 2.40  # pre-flight ~$1.96 (K x s62's measured $0.392). Under the $2.50 flag.

# ---- NLI instrument: FORCED-DECOMPOSITION working surface. COPIED VERBATIM from session
# 60/62's probe.py. This is the held-constant instrument; the manipulated variable in THIS
# run is the REPEAT (run index), not the format or the item set. ----
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


def run_one(run_idx, slot, items, records):
    out = RAW / f"run{run_idx}-{slot}-labels.json"
    cot_out = COT / f"run{run_idx}-{slot}-cot.json"
    if out.exists():
        print(f"skip {out.name} (exists)")
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
        rows.append({"run": run_idx, "item_id": f"{it['cxn']}#{it['num']}", "cxn": it["cxn"],
                     "split": it.get("split", "test"), "gold": it["gold"],
                     "value": val, "parse_mode": mode,
                     "uptake": uptake_metrics(content),
                     "content_sha256": csha, "usage": r.get("usage"),
                     "error": r.get("error")})
        cot_rows.append({"item_id": f"{it['cxn']}#{it['num']}", "content": content})
        records.append(r)
        time.sleep(0.1)
    json.dump(rows, open(out, "w"), indent=1)
    json.dump(cot_rows, open(cot_out, "w"), indent=1)
    miss = sum(1 for x in rows if x["value"] is None)
    la = [x for x in rows if x["cxn"] == "let-alone"]
    worked = sum(1 for x in la if x["uptake"]["worked"])
    c, _, nmiss = billed_cost([records])
    print(f"run{run_idx} {slot}: {len(rows)} rows, {miss} missing, let-alone worked "
          f"{worked}/{len(la)}, cumulative ${c:.4f}"
          + (f" ({nmiss} missing usage.cost)" if nmiss else "") + f" -> {out.name}",
          flush=True)
    if c >= ABORT_USD:
        print(f"ABORT: single-run flag ${ABORT_USD} reached after run{run_idx} {slot}; "
              f"stopping (completed (run,slot) files are preserved).", flush=True)
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=["A", "B", "C"], default=None)
    ap.add_argument("--run", type=int, default=None, help="score only this run index (1..K)")
    args = ap.parse_args()
    # ---- FREEZE GUARD ----
    if not (HERE / "PREREG.md").exists():
        sys.exit("FATAL: PREREG.md not found — pre-registration not frozen.")
    if not (HERE / "analyze.py").exists():
        sys.exit("FATAL: analyze.py not found — analysis code must exist at freeze time.")
    subprocess.run([sys.executable, str(HERE / "prep.py"), "--check"], check=True)
    items = load_frozen()
    runs = [args.run] if args.run else list(range(1, K + 1))
    slots = [args.model] if args.model else ["A", "B", "C"]
    records = []
    for run_idx in runs:
        for slot in slots:
            run_one(run_idx, slot, items, records)
    total, _, n_missing_cost = billed_cost([records])
    print(f"TOTAL billed this invocation: ${total:.4f}")
    if n_missing_cost:
        print(f"WARNING: {n_missing_cost} call(s) reported no usage.cost — billed total "
              f"UNDERCOUNTS; flag in the budget ledger.")
    with open(RAW / "cost-log.txt", "a") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())} "
                f"runs={runs} slots={slots} billed=${total:.4f} "
                f"missing_cost_calls={n_missing_cost}\n")


if __name__ == "__main__":
    main()
