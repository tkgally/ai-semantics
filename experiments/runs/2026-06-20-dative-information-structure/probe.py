#!/usr/bin/env python3
"""probe.py -- the DATIVE information-structure finding-bearing probe.

Phases:
  liveness : 3 calls (one per model) on a held-out sanity trial (NOT from stimuli.json);
             all must parse the graded FINAL line. Never analyzed.
  full     : every stimuli.json trial x each model -> raw/probe-<model>.jsonl (the only
             finding-bearing dataset). Per-model billed-cost hard stop; crash-safe resume.

Refuses `full` until PREREG.md exists AND records the frozen stimuli.json sha256
(PREREG-draft does NOT count). Mirrors the relational/composition-line freeze discipline.
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
        sys.exit("REFUSING: PREREG.md does not exist. Freeze it after the independent "
                 "pre-run critic GO.")
    blob = open(STIM, "rb").read()
    sha = hashlib.sha256(blob).hexdigest()
    txt = open(PREREG).read()
    if sha not in txt:
        sys.exit(f"REFUSING: stimuli.json sha256 {sha} not recorded in PREREG.md "
                 "(stimuli not frozen / drifted).")
    return sha


def liveness():
    # a fixed sanity trial NOT from stimuli.json
    trial = {"context": "The visitor had been waiting in the lobby all morning.",
             "doc": "The receptionist gave the visitor a badge.",
             "pd": "The receptionist gave a badge to the visitor.",
             "doc_is_a": True}
    user = C.build_user(trial)
    print(f"LIVENESS ({len(C.MODELS)} calls; all models must parse a graded FINAL line):")
    recs = []
    for name, slug in C.MODELS.items():
        r, a, b, mode, retried, usages = C.call_graded(slug, user)
        ok = a is not None
        pref = C.doc_pref(a, b, trial["doc_is_a"]) if ok else None
        print(f"  {name}: A={a} B={b} mode={mode} retried={retried} "
              f"{'OK' if ok else 'PARSE-FAIL'} (DOC-pref={pref})")
        recs.append({"model": name, "usage": usages})
        if not ok:
            print(f"     raw: {r.get('content')!r}")
    billed, have, missing = C.flat_cost(recs)
    C.ledger_append("liveness", len(recs), billed, missing, "format gate")
    json.dump({"billed": billed}, open(os.path.join(C.RAW, "liveness.json"), "w"))


def full():
    _require_frozen()
    stim = json.load(open(STIM))
    trials = stim["trials"]
    # pre-flight: 240 trials x 3 models = 720 calls; graded outputs w/ brief justification
    # (~512 tok cap). Honest estimate (rate card undercounts billed ~4.5x): claude ~$0.6-0.9 +
    # gpt ~$0.05 + gemini(effort minimal) ~$0.05-0.10 -> ~$0.7-1.1 billed. Hard stop $1.50.
    C.check_hard_stop(1.10, "full")
    print(f"FULL: {len(trials)} trials x {len(C.MODELS)} models")
    for name, slug in C.MODELS.items():
        path = os.path.join(C.RAW, f"probe-{name}.jsonl")
        done = {r["tid"] for r in C.read_jsonl(path)}
        recs_for_cost = C.read_jsonl(path)
        for i, t in enumerate(trials):
            tid = f"{t['item']}|{t['context_kind']}|{'A' if t['doc_is_a'] else 'B'}"
            if tid in done:
                continue
            user = C.build_user(t)
            r, a, b, mode, retried, usages = C.call_graded(slug, user)
            row = {"tid": tid, "model": name, "item": t["item"], "arm": t["arm"],
                   "context_kind": t["context_kind"], "doc_is_a": t["doc_is_a"],
                   "a_points": a, "b_points": b,
                   "doc_pref": C.doc_pref(a, b, t["doc_is_a"]) if a is not None else None,
                   "parse_mode": mode, "retried": retried,
                   "finish_reason": r.get("finish_reason"),
                   "raw": r.get("content"), "usage": usages}
            C.append_jsonl(path, row)
            recs_for_cost.append(row)
            if len(recs_for_cost) % 30 == 0:
                C.check_hard_stop(0.15, f"full/{name}")
        billed, have, missing = C.flat_cost(recs_for_cost)
        C.ledger_append(f"full/{name}", len(recs_for_cost), billed, missing, "finding-bearing")
    print("FULL done. Run: python3 analyze.py")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "liveness"
    {"liveness": liveness, "full": full}[mode]()
