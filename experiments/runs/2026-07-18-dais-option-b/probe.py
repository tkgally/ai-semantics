#!/usr/bin/env python3
"""probe.py -- the DAIS Option-B graded-preference correlation probe (s248).

Phases:
  liveness : 3 calls (one per model) on a held-out sanity trial (NOT from stimuli.json); all must
             parse the graded FINAL line. Never analyzed.
  arm A    : the 200 Arm-A trials x each model -> raw/probe-A-<model>.jsonl.
  arm B    : the 200 Arm-B trials x each model -> raw/probe-B-<model>.jsonl.
  full     : arm A then arm B.

Blind to the human targets during collection (human_targets.json is read only by analyze.py). Per-arm
+ total billed-cost hard stop; crash-safe resume. Refuses A/B/full until PREREG.md exists AND records
the frozen stimuli.json sha256 (freeze discipline mirrors the dative/relational lines).
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
        sys.exit("REFUSING: PREREG.md does not exist. Freeze it after the independent pre-run "
                 "critic GO.")
    sha = hashlib.sha256(open(STIM, "rb").read()).hexdigest()
    if sha not in open(PREREG).read():
        sys.exit(f"REFUSING: stimuli.json sha256 {sha} not recorded in PREREG.md (not frozen / "
                 "drifted).")
    return sha


def liveness():
    trial = {"doc": "The courier handed the tenant a package.",
             "pd": "The courier handed a package to the tenant.",
             "doc_is_a": True}
    user = C.build_user(trial)
    print(f"LIVENESS ({len(C.MODELS)} calls; all models must parse a graded FINAL line):")
    recs = []
    for name, slug in C.MODELS.items():
        r, a, b, mode, retried, usages = C.call_graded(slug, user)
        ok = a is not None
        pref = C.doc_pref(a, b, trial["doc_is_a"]) if ok else None
        print(f"  {name}: A={a} B={b} mode={mode} retried={retried} "
              f"{'OK' if ok else 'PARSE-FAIL'} (DO-pref={pref})")
        recs.append({"model": name, "usage": usages})
        if not ok:
            print(f"     raw: {r.get('content')!r}")
    billed, have, missing = C.flat_cost(recs)
    C.ledger_append("liveness", len(recs), billed, missing, "format gate")
    json.dump({"billed": billed}, open(os.path.join(C.RAW, "liveness.json"), "w"))


def run_arm(arm):
    sha = _require_frozen()
    trials = [t for t in json.load(open(STIM))["trials"] if t["arm"] == arm]
    n_calls = len(trials) * len(C.MODELS)
    print(f"ARM {arm}: {len(trials)} trials x {len(C.MODELS)} models = {n_calls} calls "
          f"(stimuli sha {sha[:12]})")
    for name, slug in C.MODELS.items():
        path = os.path.join(C.RAW, f"probe-{arm}-{name}.jsonl")
        done = {r["tid"] for r in C.read_jsonl(path)}
        recs_for_cost = C.read_jsonl(path)
        arm_recs = []
        for a_arm in ("A", "B"):
            for m in C.MODELS:
                arm_recs += C.read_jsonl(os.path.join(C.RAW, f"probe-{a_arm}-{m}.jsonl"))
        new_calls = 0
        for t in trials:
            if t["tid"] in done:
                continue
            user = C.build_user(t)
            r, a, b, mode, retried, usages = C.call_graded(slug, user)
            row = {"tid": t["tid"], "model": name, "arm": arm, "verb": t["verb"],
                   "condition": t["condition"], "classification": t["classification"],
                   "bucket": t["bucket"], "theme": t["theme"], "doc_is_a": t["doc_is_a"],
                   "a_points": a, "b_points": b,
                   "doc_pref": C.doc_pref(a, b, t["doc_is_a"]) if a is not None else None,
                   "parse_mode": mode, "retried": retried,
                   "finish_reason": r.get("finish_reason"), "raw": r.get("content"),
                   "usage": usages}
            C.append_jsonl(path, row)
            recs_for_cost.append(row)
            new_calls += 1
            if new_calls % 30 == 0:
                arm_spent, _, _ = C.flat_cost(
                    sum((C.read_jsonl(os.path.join(C.RAW, f"probe-{arm}-{m}.jsonl"))
                         for m in C.MODELS), []))
                C.check_hard_stop(0.20, f"arm{arm}/{name}", arm_spent=arm_spent)
        if new_calls:
            billed, have, missing = C.flat_cost(recs_for_cost)
            C.ledger_append(f"arm{arm}/{name}", len(recs_for_cost), billed, missing,
                            "finding-bearing")
    arm_spent, _, _ = C.flat_cost(
        sum((C.read_jsonl(os.path.join(C.RAW, f"probe-{arm}-{m}.jsonl")) for m in C.MODELS), []))
    print(f"ARM {arm} done. Arm billed ${arm_spent:.5f}.")


def full():
    run_arm("A")
    run_arm("B")
    print("FULL done. Run: python3 analyze.py")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "liveness"
    if mode in ("A", "B"):
        run_arm(mode)
    else:
        {"liveness": liveness, "full": full}[mode]()
