#!/usr/bin/env python3
"""probe.py -- the order-sensitive COMPOSITION (Option-C) finding-bearing probe.

Phases:
  liveness  : 2 calls (one per model) on a held-out sanity record (NOT from stimuli.json); both
              must parse under the forced format. Never analyzed.
  full      : every stimuli.json record x each model -> raw/probe-<model>.jsonl (the only
              finding-bearing dataset). Per-model billed-cost hard stop; crash-safe JSONL resume.

Refuses `full` until PREREG.md exists AND records the frozen stimuli.json sha256 (PREREG-draft does
NOT count). Mirrors the relational-line freeze discipline.
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


def liveness():
    # a fixed sanity record (NOT from stimuli.json): DAX starts at track position 4 (idx 3, "a
    # square"); STEP (round 2) then FLIP (round 7) -> STEP(3)=4 -> FLIP(4)=1 -> track idx 1. The
    # on-demand correct figure is computed from the ops, not hand-typed.
    track = ["triangle", "diamond", "circle", "square", "star", "heart"]
    start_idx = 3
    tgt_idx = C.apply_order(start_idx, "SF")
    rec = {"query": "DIRECT", "subset": "direct", "track": track,
           "present": list(C.SHAPES), "start_idx": start_idx, "start_shape": track[start_idx],
           "order": "SF", "op_lo": "STEP", "op_hi": "FLIP", "r_lo": 2, "r_hi": 7,
           "display_order": "stamp",
           "hist_display": [{"round": 2, "op": "STEP"}, {"round": 7, "op": "FLIP"}],
           "target_idx": tgt_idx, "target_shape": track[tgt_idx]}
    correct = track[tgt_idx]
    user = C.build_user(rec)
    present = set(C.SHAPES)
    label_list = ", ".join(C.shape_phrase(s) for s in track)
    print(f"LIVENESS (2 calls; both models must parse; on-demand correct = a {correct}):")
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
    # pre-flight: ~216 calls x ~$0.0008/call ~= $0.17 ; hard stop $0.55.
    C.check_hard_stop(0.20, "full")
    print(f"FULL: {len(records)} records x {len(C.MODELS)} models")
    for name, slug in C.MODELS.items():
        path = os.path.join(C.RAW, f"probe-{name}.jsonl")
        done = {r["rid"] for r in C.read_jsonl(path)}
        recs_for_cost = C.read_jsonl(path)
        for rec in records:
            if rec["rid"] in done:
                continue
            user = C.build_user(rec)
            present = set(rec["present"])
            label_list = ", ".join(C.shape_phrase(s) for s in rec["track"])
            r, pick, mode, retried, usages = C.call_forced(slug, user, present, label_list)
            row = {"rid": rec["rid"], "model": name, "query": rec["query"],
                   "subset": rec["subset"], "pick": pick, "parse_mode": mode,
                   "retried": retried, "finish_reason": r.get("finish_reason"),
                   "raw": r.get("content"), "usage": usages}
            C.append_jsonl(path, row)
            recs_for_cost.append(row)
            if len(recs_for_cost) % 20 == 0:
                C.check_hard_stop(0.07, f"full/{name}")
        billed, have, missing = C.flat_cost(recs_for_cost)
        C.ledger_append(f"full/{name}", len(recs_for_cost), billed, missing, "finding-bearing")
    print("FULL done. Run: python3 analyze.py")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "liveness"
    {"liveness": liveness, "full": full}[mode]()
