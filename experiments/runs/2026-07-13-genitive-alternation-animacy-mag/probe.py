#!/usr/bin/env python3
"""probe.py -- the GENITIVE-alternation possessor-animacy finding-bearing probe.

Phases:
  liveness : 3 calls (one per model) on a held-out sanity trial (NOT from stimuli.json); all must
             parse the graded FINAL line. Never analyzed.
  full     : every stimuli.json trial x each model -> raw/probe-<model>.jsonl (the only
             finding-bearing dataset). Per-model billed-cost hard stop; crash-safe resume.

Refuses `full` until PREREG.md exists AND records BOTH the frozen stimuli.json sha256 and the frozen
freq_control.json sha256 (the covariate is part of the pre-registered shadow control). PREREG-draft
does NOT count.
"""
import hashlib
import json
import os
import sys

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
STIM = os.path.join(HERE, "stimuli.json")
FREQ = os.path.join(HERE, "freq_control.json")
PREREG = os.path.join(HERE, "PREREG.md")


def _require_frozen():
    if not os.path.exists(PREREG):
        sys.exit("REFUSING: PREREG.md does not exist. Freeze it after the ratification + build.")
    txt = open(PREREG).read()
    for label, path in (("stimuli.json", STIM), ("freq_control.json", FREQ)):
        sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
        if sha not in txt:
            sys.exit(f"REFUSING: {label} sha256 {sha} not recorded in PREREG.md (not frozen).")


def liveness():
    trial = {"option_a": "the mayor's speech", "option_b": "the speech of the mayor",
             "s_is_a": True, "gloss": None}
    user = C.build_user(trial)
    print(f"LIVENESS ({len(C.MODELS)} calls; all models must parse a graded FINAL line):")
    recs = []
    for name, slug in C.MODELS.items():
        r, a, b, mode, retried, usages = C.call_graded(slug, user)
        ok = a is not None
        pref = C.s_pref(a, b, trial["s_is_a"]) if ok else None
        print(f"  {name}: A={a} B={b} mode={mode} retried={retried} "
              f"{'OK' if ok else 'PARSE-FAIL'} (s-pref={pref})")
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
    done_now = sum(len(C.read_jsonl(os.path.join(C.RAW, f"probe-{n}.jsonl"))) for n in C.MODELS)
    remaining = max(0, len(trials) * len(C.MODELS) - done_now)
    C.check_hard_stop(min(1.10, remaining * 0.0009 + 0.02), "full")
    print(f"FULL: {len(trials)} trials x {len(C.MODELS)} models")
    for name, slug in C.MODELS.items():
        path = os.path.join(C.RAW, f"probe-{name}.jsonl")
        done = {r["tid"] for r in C.read_jsonl(path)}
        recs_for_cost = C.read_jsonl(path)
        new_calls = 0
        for t in trials:
            tid = f"{t['frame']}|{t['level']}|{'A' if t['s_is_a'] else 'B'}"
            if tid in done:
                continue
            user = C.build_user(t)
            r, a, b, mode, retried, usages = C.call_graded(slug, user)
            row = {"tid": tid, "model": name, "frame": t["frame"], "arm": t["arm"],
                   "level": t["level"], "possessum": t["possessum"], "possessor": t["possessor"],
                   "s_is_a": t["s_is_a"], "a_points": a, "b_points": b,
                   "s_pref": C.s_pref(a, b, t["s_is_a"]) if a is not None else None,
                   "parse_mode": mode, "retried": retried,
                   "finish_reason": r.get("finish_reason"), "raw": r.get("content"),
                   "usage": usages}
            C.append_jsonl(path, row)
            recs_for_cost.append(row)
            new_calls += 1
            if len(recs_for_cost) % 30 == 0:
                C.check_hard_stop(0.15, f"full/{name}")
        if new_calls:
            billed, have, missing = C.flat_cost(recs_for_cost)
            C.ledger_append(f"full/{name}", len(recs_for_cost), billed, missing, "finding-bearing")
    print("FULL done. Run: python3 analyze.py")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "liveness"
    {"liveness": liveness, "full": full}[mode]()
