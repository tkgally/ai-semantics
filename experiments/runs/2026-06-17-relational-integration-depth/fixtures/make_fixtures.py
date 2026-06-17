#!/usr/bin/env python3
"""make_fixtures.py (no API) -- certify the frozen verdict map on idealized readers.

Generates synthetic raw/probe-<reader>.jsonl for several idealized strategies, runs analyze.py on
each, and asserts the verdict is what the design's logic demands. This proves -- BEFORE any model
is queried -- that NO position / figure-identity / single-attribute / two-attribute (drop-one-turn)
strategy can manufacture an INTEGRATION-UNDER-LOAD verdict, and that the on-demand gate guards
against inability-to-conjoin.

Readers (on INTEG; on DIRECT every reader except the gate-fail ones answers with the full
conjunction = correct, so the gate isolates spontaneous behaviour from capability):
  integrator   -> picks the all-three-match target          => INTEGRATION-UNDER-LOAD
  recent_two   -> drops the buried earliest shape; picks among {target, twin_shape} by slot_lo
                  (a clean "shed the oldest" recency reader) => PARTIAL-OR-OVERWRITE (target ~0.50)
  overwrite    -> keeps only the latest (color); picks among the 4 color-matches by slot_lo
                                                              => PARTIAL-OR-OVERWRITE (target ~0.25)
  gridpos      -> always picks physical slot G1 (INTEG & DIRECT) => UNINTERPRETABLE (DIRECT fails)
  figpref      -> always picks the lowest-FIG_KEY present figure (INTEG & DIRECT)
                                                              => UNINTERPRETABLE (DIRECT fails)
  direct_fail  -> integrator on INTEG but answers None on DIRECT => UNINTERPRETABLE (gate guard)
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUN = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, RUN)
import analyze as A  # noqa: E402
import build_trials as B  # noqa: E402
import common as C  # noqa: E402

STIM = json.load(open(os.path.join(RUN, "stimuli.json")))
RECORDS = STIM["records"]


def _slot_lo_among(rec, keep):
    """pick the lowest-physical-slot present figure matching the target's values of `keep`."""
    cands = [(i, d) for i, d in enumerate(rec["display"]) if all(d[a] == rec[a] for a in keep)]
    return min(cands, key=lambda t: t[0])[1]["label"]


def _lowest_key_label(rec):
    best = min(rec["display"],
               key=lambda d: B.FIG_KEY[(d["shape"], d["pattern"], d["color"])])
    return best["label"]


def reader_pick(reader, rec):
    q = rec["query"]
    if reader == "integrator":
        return rec["correct_label"]
    if reader == "recent_two":
        return rec["correct_label"] if q == "DIRECT" else _slot_lo_among(rec, ("pattern", "color"))
    if reader == "overwrite":
        return rec["correct_label"] if q == "DIRECT" else _slot_lo_among(rec, ("color",))
    if reader == "gridpos":
        return rec["display"][0]["label"]              # always G1, both arms -> DIRECT fails
    if reader == "figpref":
        return _lowest_key_label(rec)                  # both arms -> DIRECT fails
    if reader == "direct_fail":
        return None if q == "DIRECT" else rec["correct_label"]
    raise ValueError(reader)


EXPECT = {
    "integrator": "INTEGRATION-UNDER-LOAD",
    "recent_two": "PARTIAL-OR-OVERWRITE",
    "overwrite": "PARTIAL-OR-OVERWRITE",
    "gridpos": "UNINTERPRETABLE",
    "figpref": "UNINTERPRETABLE",
    "direct_fail": "UNINTERPRETABLE",
}


def main():
    all_ok = True
    for reader, expect in EXPECT.items():
        raw = os.path.join(HERE, reader)
        os.makedirs(raw, exist_ok=True)
        for name in C.MODELS:
            path = os.path.join(raw, f"probe-{name}.jsonl")
            with open(path, "w") as f:
                for rec in RECORDS:
                    pick = reader_pick(reader, rec)
                    f.write(json.dumps({"rid": rec["rid"], "model": name, "query": rec["query"],
                                        "subset": rec["subset"], "pick": pick,
                                        "parse_mode": "strict" if pick else None}) + "\n")
        out = A.analyze(raw)
        verdicts = {m: out["models"][m]["verdict"] for m in C.MODELS}
        ok = all(v == expect for v in verdicts.values())
        all_ok = all_ok and ok
        print(f"\n  [fixture] {reader}: verdicts={verdicts} expected={expect} "
              f"-> {'OK' if ok else 'MISMATCH'}")
    print(f"\n  ALL FIXTURES {'PASS' if all_ok else 'FAIL'}: the verdict map is certified -- only a "
          f"genuine integrator-of-three -> INTEGRATION-UNDER-LOAD.")
    if not all_ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
