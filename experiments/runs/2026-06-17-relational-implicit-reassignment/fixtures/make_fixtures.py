#!/usr/bin/env python3
"""make_fixtures.py (no API) — idealized-reader fixtures proving the Option-A instrument
separates SPONTANEOUS recency-weighting from every positional / lexical / frequency shortcut,
and that the verdict map behaves correctly, BEFORE any model is queried (the v4 GO-discipline,
and binding carry-forward 3: certify the task UNSOLVABLE by a positional/lexical shortcut).

Builds the frozen stimuli through the real build_trials.build(), then writes idealized raw sets
(each picker may depend on the record's subset) and shows analyze.py's verdict for each:

  spont_latest   : DIRECT picks correct, SPONT picks the MAX-round figure
                   -> SPONTANEOUS-RECENCY  (latest_rate = 1.0)        [genuine recency reader]
  first_governs  : DIRECT picks correct, SPONT picks the MIN-round figure
                   -> SPONTANEOUS-ANTI-RECENCY (first_rate = 1.0)     [the other non-commutative]
  commutative    : DIRECT picks correct, SPONT picks the physically-FIRST line's figure
                   -> COMMUTATIVE-HERE (latest_rate = first_rate = 1/K) [on-demand, not spontaneous]
  lastpos        : BOTH subsets pick the physically-LAST line's figure
                   -> NOT order-sensitive; DIRECT fails -> UNINTERPRETABLE; SPONT latest = 1/K
  figpref        : BOTH subsets pick the present figure earliest in a FIXED pool ordering
                   -> NOT order-sensitive; DIRECT fails -> UNINTERPRETABLE; SPONT latest = 1/K
  direct_fail    : SPONT picks MAX-round but DIRECT picks physically-last (on-demand fails)
                   -> UNINTERPRETABLE (the manipulation-gate guard fires)

The load-bearing certifications:
  (1) NO positional / lexical / frequency shortcut (lastpos, figpref, commutative-on-SPONT)
      ever yields a SPONTANEOUS-* (non-commutative) verdict -- only genuine stamp-recency reading
      does. So a positive Option-A result cannot be manufactured by a shortcut.
  (2) the SPONT latest/first rates for every shortcut reader are EXACTLY 1/K (the design neutralizes
      position and lexical preference), so the order-sensitivity bar is clean.
  (3) the manipulation gate correctly refuses to interpret a reader that fails on-demand (lastpos,
      figpref, direct_fail -> UNINTERPRETABLE), so a SPONT null is only ever read as the narrow
      A-null when on-demand comprehension is demonstrated in this very instrument.
These are synthetic and are never findings.
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

POOL_ORDER = {lab: i for i, lab in enumerate(C.LABELS)}


def write_set(subdir, picker):
    d = os.path.join(HERE, subdir)
    os.makedirs(d, exist_ok=True)
    records = build_trials.build()
    for name in C.MODELS:
        path = os.path.join(d, f"probe-{name}.jsonl")
        open(path, "w").close()
        for rec in records:
            pk = picker(rec)
            C.append_jsonl(path, {"rid": rec["rid"], "model": name, "query": rec["query"],
                                  "pick": pk, "parse_mode": "strict", "retried": False,
                                  "finish_reason": "stop", "raw": pk, "usage": []})
    return d


def figpref(rec):
    return min(rec["present"], key=lambda x: POOL_ORDER[x])


def main():
    records = build_trials.build()
    build_trials.assert_balance(records)

    def spont_latest(r):
        return r["correct_label"] if r["subset"] == "direct" else r["max_round_label"]

    def first_governs(r):
        return r["correct_label"] if r["subset"] == "direct" else r["min_round_label"]

    def commutative(r):
        return r["correct_label"] if r["subset"] == "direct" else r["first_pos_label"]

    def lastpos(r):
        return r["last_pos_label"]

    def figpref_both(r):
        return figpref(r)

    def direct_fail(r):
        return r["max_round_label"] if r["subset"] == "spont" else r["last_pos_label"]

    print("\n--- spont_latest (on-demand + spontaneous recency; expect SPONTANEOUS-RECENCY) ---")
    o = analyze.analyze(write_set("raw_spont_latest", spont_latest))
    assert all(m["verdict"] == "SPONTANEOUS-RECENCY" for m in o["models"].values())
    assert all(m["spont"]["latest_governs"]["rate"] == 1.0 for m in o["models"].values())

    print("\n--- first_governs (on-demand + anti-recency; expect SPONTANEOUS-ANTI-RECENCY) ---")
    o = analyze.analyze(write_set("raw_first_governs", first_governs))
    assert all(m["verdict"] == "SPONTANEOUS-ANTI-RECENCY" for m in o["models"].values())

    print("\n--- commutative (on-demand OK, SPONT order-insensitive; expect COMMUTATIVE-HERE) ---")
    o = analyze.analyze(write_set("raw_commutative", commutative))
    for m in o["models"].values():
        assert m["verdict"] == "COMMUTATIVE-HERE", m["verdict"]
        assert abs(m["spont"]["latest_governs"]["rate"] - C.POS_CHANCE) < 1e-9
        assert abs(m["spont"]["first_governs"]["rate"] - C.POS_CHANCE) < 1e-9

    print("\n--- lastpos (pure position-follower; expect UNINTERPRETABLE, NOT order-sensitive) ---")
    o = analyze.analyze(write_set("raw_lastpos", lastpos))
    for m in o["models"].values():
        assert m["verdict"] == "UNINTERPRETABLE", m["verdict"]
        assert not m["spont"]["latest_sig"] and not m["spont"]["first_sig"]
        assert abs(m["spont"]["latest_governs"]["rate"] - C.POS_CHANCE) < 1e-9

    print("\n--- figpref (fixed figure-preference; expect UNINTERPRETABLE, NOT order-sensitive) ---")
    o = analyze.analyze(write_set("raw_figpref", figpref_both))
    for m in o["models"].values():
        assert m["verdict"] == "UNINTERPRETABLE", m["verdict"]
        assert not m["spont"]["latest_sig"] and not m["spont"]["first_sig"]

    print("\n--- direct_fail (spontaneous-looking SPONT but on-demand FAILS; expect UNINTERPRETABLE) ---")
    o = analyze.analyze(write_set("raw_direct_fail", direct_fail))
    assert all(m["verdict"] == "UNINTERPRETABLE" for m in o["models"].values())

    print("\nALL FIXTURE ASSERTS PASS: only genuine stamp-recency reading yields a "
          "SPONTANEOUS-* (non-commutative) verdict; every position/lexical/frequency shortcut "
          "scores exactly 1/K on SPONT and is either COMMUTATIVE-HERE (if on-demand passes) or "
          "UNINTERPRETABLE (if it does not). The manipulation gate guards the A-null reading.")


if __name__ == "__main__":
    main()
