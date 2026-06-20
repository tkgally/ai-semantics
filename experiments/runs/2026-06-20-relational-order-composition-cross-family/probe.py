#!/usr/bin/env python3
"""probe.py -- the CROSS-FAMILY (heterogeneous-operation) order-sensitive COMPOSITION finding-bearing
probe.

Phases:
  liveness  : 3 calls (one per model) on a held-out sanity record (NOT from stimuli.json); all
              must parse under the working-surface format (FINAL: tag). Never analyzed.
  full      : every stimuli.json record x each model -> raw/probe-<model>.jsonl (the only
              finding-bearing dataset). Per-model billed-cost hard stop; crash-safe JSONL resume.

Refuses `full` until PREREG.md exists AND records the frozen stimuli.json rstrip-sha256 (PREREG-draft
does NOT count). Mirrors the relational-line freeze discipline.
"""
import hashlib
import json
import os
import sys

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
STIM = os.path.join(HERE, "stimuli.json")
PREREG = os.path.join(HERE, "PREREG.md")


def _require_frozen():
    if not os.path.exists(PREREG):
        sys.exit("REFUSING: PREREG.md does not exist (PREREG-draft.md does NOT count). "
                 "Freeze it after the independent pre-run critic GO.")
    blob = open(STIM, "rb").read()
    sha = hashlib.sha256(blob.rstrip(b"\n")).hexdigest()
    txt = open(PREREG).read()
    if sha not in txt:
        sys.exit(f"REFUSING: stimuli.json sha256 {sha} not recorded in PREREG.md "
                 "(stimuli not frozen / drifted).")
    return sha


def _liveness_record():
    # a fixed sanity record (NOT from stimuli.json): K=4 row; the DAX spot is spot 1 (idx 0); SWAP
    # (spot1,spot2) round 2, RECOLOR(spot1 -> red) round 5. Stamp order SWAP-first -> spot1 gets
    # spot2's color (blue), then recolor spot1 -> RED. On-demand correct = red. DIRECT.
    rec = {"rid": -1, "subset": "direct", "query": "DIRECT",
           "a": 0, "b": 1, "s": 0, "o": 1, "m": 0,
           "readout_type": "SAME", "stamp_first": "SWAP", "stamp_order": ["SWAP", "RECOLOR"],
           "recolor_color": "red", "init_colors": ["green", "blue", "yellow", "purple"],
           "rounds": [2, 5], "display_order": ["SWAP", "RECOLOR"]}
    rec["hist_display"] = [{"round": rec["rounds"][i], "op": rec["stamp_order"][i],
                            "desc": C.op_desc(rec, rec["stamp_order"][i])} for i in (0, 1)]
    rec["target_color"] = C.answer_color(rec)
    return rec


def liveness():
    rec = _liveness_record()
    correct = rec["target_color"]
    user = C.build_user(rec)
    present = set(C.COLORS)
    label_list = ", ".join(C.COLORS)
    print(f"LIVENESS ({len(C.MODELS)} calls; all models must parse; on-demand correct = {correct}):")
    recs = []
    for name, slug in C.MODELS.items():
        r, pick, mode, retried, usages = C.call_forced(slug, user, present, label_list)
        ok = pick is not None
        print(f"  {name}: pick={pick} mode={mode} retried={retried} "
              f"{'OK' if ok else 'PARSE-FAIL'} (on-demand correct={pick == correct})")
        recs.append({"model": name, "usage": usages})
        if not ok:
            print(f"     raw: {r.get('content')!r}")
    billed, have, missing = C.flat_cost(recs)
    C.ledger_append("liveness", len(recs), billed, missing, "format gate")
    json.dump({"billed": billed}, open(os.path.join(C.RAW, "liveness.json"), "w"))


def full():
    _require_frozen()
    stim = json.load(open(STIM))
    records = stim["records"]
    # pre-flight: 384 calls (128/model x 3 = 96 COMP + 32 DIRECT per model). A working surface raises
    # OUTPUT tokens, but this is a DEPTH-2 task (two ops) with a short chain, so the CoT is shorter
    # than the three-move run ($0.80 for 324 calls); estimate ~= $0.7-1.0 (claude CoT the driver;
    # gemini held at effort minimal); hard stop $1.50.
    C.check_hard_stop(1.10, "full")
    print(f"FULL: {len(records)} records x {len(C.MODELS)} models")
    for name, slug in C.MODELS.items():
        path = os.path.join(C.RAW, f"probe-{name}.jsonl")
        done = {r["rid"] for r in C.read_jsonl(path)}
        recs_for_cost = C.read_jsonl(path)
        for rec in records:
            if rec["rid"] in done:
                continue
            user = C.build_user(rec)
            present = set(C.COLORS)
            label_list = ", ".join(C.COLORS)
            r, pick, mode, retried, usages = C.call_forced(slug, user, present, label_list)
            row = {"rid": rec["rid"], "model": name, "query": rec["query"],
                   "subset": rec["subset"], "pick": pick, "parse_mode": mode,
                   "retried": retried, "finish_reason": r.get("finish_reason"),
                   "raw": r.get("content"), "usage": usages}
            C.append_jsonl(path, row)
            recs_for_cost.append(row)
            if len(recs_for_cost) % 20 == 0:
                C.check_hard_stop(0.25, f"full/{name}")
        billed, have, missing = C.flat_cost(recs_for_cost)
        C.ledger_append(f"full/{name}", len(recs_for_cost), billed, missing, "finding-bearing")
    print("FULL done. Run: python3 analyze.py")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "liveness"
    {"liveness": liveness, "full": full}[mode]()
