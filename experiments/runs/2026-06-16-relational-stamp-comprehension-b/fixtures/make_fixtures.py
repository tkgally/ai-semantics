#!/usr/bin/env python3
"""make_fixtures.py (no API) — idealized-reader fixtures proving the B instrument separates
stamp-comprehension from position-following BEFORE any model is queried (the v4 GO-discipline).

Builds the frozen stimuli through the real build_trials.build(), then writes three idealized
raw sets and shows what analyze.py returns for each:
  raw_stamp  : a perfect stamp-reader (always picks correct_nonce)            -> PASS / PASS
  raw_lastpos: a pure position-follower (always picks physically-last nonce)  -> FAIL / FAIL (~1/K)
  raw_firstpos: a pure first-line follower (always picks physically-first)    -> FAIL / FAIL (~1/K)

A PASS on raw_lastpos/raw_firstpos would mean the instrument leaks position as comprehension;
it must not. These are synthetic and are never findings.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, RUN)
import build_trials  # noqa: E402
import common as C    # noqa: E402
import analyze        # noqa: E402


def write_set(subdir, picker):
    d = os.path.join(HERE, subdir)
    os.makedirs(d, exist_ok=True)
    records = build_trials.build()
    for name in C.MODELS:
        path = os.path.join(d, f"probe-{name}.jsonl")
        open(path, "w").close()
        for rec in records:
            C.append_jsonl(path, {"rid": rec["rid"], "model": name, "query": rec["query"],
                                  "pick": picker(rec), "parse_mode": "strict",
                                  "retried": False, "finish_reason": "stop",
                                  "raw": picker(rec), "usage": []})
    return d


def main():
    # ensure stimuli.json exists & matches build (geometry assert runs inside build->assert)
    records = build_trials.build()
    build_trials.assert_balance(records)

    print("\n--- raw_stamp (perfect stamp-reader; expect PASS/PASS) ---")
    d = write_set("raw_stamp", lambda r: r["correct_nonce"])
    o = analyze.analyze(d)
    assert all(m["verdict"] == "PASS" for m in o["models"].values()), "stamp-reader should PASS"

    print("\n--- raw_lastpos (position-follower: always physically-last; expect FAIL/FAIL ~1/K) ---")
    d = write_set("raw_lastpos", lambda r: r["last_pos_nonce"])
    o = analyze.analyze(d)
    assert all(m["verdict"] == "FAIL" for m in o["models"].values()), "position-follower should FAIL"
    assert all(abs(m["accuracy"] - C.POS_CHANCE) < 1e-9 for m in o["models"].values()), \
        "position-follower accuracy must equal POS_CHANCE under balance"

    print("\n--- raw_firstpos (always physically-first; expect FAIL/FAIL ~1/K) ---")
    d = write_set("raw_firstpos", lambda r: r["first_pos_nonce"])
    o = analyze.analyze(d)
    assert all(m["verdict"] == "FAIL" for m in o["models"].values()), "first-line follower should FAIL"

    print("\nALL FIXTURE ASSERTS PASS: the instrument separates stamp-comprehension from "
          "position-following (both directions score exactly 1/K).")


if __name__ == "__main__":
    main()
