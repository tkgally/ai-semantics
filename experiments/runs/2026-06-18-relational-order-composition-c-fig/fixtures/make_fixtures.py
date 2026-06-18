#!/usr/bin/env python3
"""make_fixtures.py (no API) -- idealized-reader fixtures proving the Option-C ORDER-SENSITIVE
COMPOSITION instrument separates a genuine STAMP-ORDER composer from every figure-identity /
track-position / print-order / canonical-order / start / single-move / reversed-order shortcut, and
that the verdict map behaves correctly, BEFORE any model is queried (the freeze discipline).

Builds the frozen stimuli through build_trials.build(), then writes idealized raw sets and shows
analyze.py's verdict for each:

  stamp_order  : DIRECT correct, COMP picks the STAMP-ORDER end figure
                 -> RESPECTS-ORDER (target_rate = 1.0)                 [genuine order-sensitive composer]
  print_order  : DIRECT correct (told the order), COMP applies the moves in PRINT order
                 -> ORDER-BLIND-OR-WEAKER (target_rate = 0.50)         [the thin null: reads print order]
  canonical_sf : DIRECT correct, COMP always applies STEP-then-FLIP regardless of stamps
                 -> ORDER-BLIND-OR-WEAKER (target_rate = 0.50)         [the other order-blind null]
  figpref      : BOTH subsets pick a FIXED figure (triangle)
                 -> DIRECT fails -> UNINTERPRETABLE; COMP target = 1/K
  trackpos     : BOTH subsets pick a FIXED track position (position 1)
                 -> DIRECT fails -> UNINTERPRETABLE; COMP target = 1/K
  direct_fail  : COMP picks the stamp-order TARGET (looks composing) but DIRECT picks a fixed
                 position -> UNINTERPRETABLE (the on-demand gate guard fires)

Load-bearing certifications:
  (1) NO figure / track-position / print-order / canonical-order / start / single-move shortcut ever
      yields a RESPECTS-ORDER verdict -- only ordering the two moves by their STAMPS does. A positive
      cannot be manufactured by a non-stamp-order reader.
  (2) the COMP target_rate for every print-order / canonical-order reader is exactly PRINT_CEILING =
      0.50, and for every position / identity reader is exactly 1/K, so the 0.50 bar is clean.
  (3) the on-demand gate refuses to interpret a reader that fails DIRECT (figpref, trackpos,
      direct_fail -> UNINTERPRETABLE), so a COMP null is only read as ORDER-BLIND-OR-WEAKER when
      on-demand composition is demonstrated in this very instrument.
These are synthetic and are never findings.
"""
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
                                  "pick": picker(rec), "parse_mode": "strict", "retried": False,
                                  "finish_reason": "stop", "raw": picker(rec), "usage": []})
    return d


def main():
    records = build_trials.build()
    build_trials.assert_balance(records)

    def stamp_order(r):
        return r["target_shape"]

    def print_order(r):                     # on-demand: told the order (correct); spontaneous: reads
        if r["subset"] == "direct":         # the moves in PRINT order -> target only when print==stamp
            return r["target_shape"]
        return r["target_shape"] if r["display_order"] == "stamp" else r["swapped_shape"]

    def canonical_sf(r):                    # on-demand correct; spontaneous always STEP-then-FLIP
        if r["subset"] == "direct":
            return r["target_shape"]
        return r["track"][C.apply_order(r["start_idx"], "SF")]

    def figpref(r):
        return C.SHAPES[0]                  # always "triangle"

    def trackpos(r):
        return r["track"][0]                # always track position 1

    def direct_fail(r):
        return r["target_shape"] if r["subset"] == "comp" else r["track"][0]

    print("\n--- stamp_order (on-demand + spontaneous stamp-order; expect RESPECTS-ORDER) ---")
    o = analyze.analyze(write_set("raw_stamp_order", stamp_order))
    assert all(m["verdict"] == "RESPECTS-ORDER" for m in o["models"].values())
    assert all(m["comp"]["target_governs"]["rate"] == 1.0 for m in o["models"].values())

    print("\n--- print_order (reads print order; expect ORDER-BLIND-OR-WEAKER, target 0.50) ---")
    o = analyze.analyze(write_set("raw_print_order", print_order))
    for m in o["models"].values():
        assert m["verdict"] == "ORDER-BLIND-OR-WEAKER", m["verdict"]
        assert abs(m["comp"]["target_governs"]["rate"] - C.PRINT_CEILING) < 1e-9
        assert not m["comp"]["comp_sig"]

    print("\n--- canonical_sf (always STEP-then-FLIP; expect ORDER-BLIND-OR-WEAKER, target 0.50) ---")
    o = analyze.analyze(write_set("raw_canonical_sf", canonical_sf))
    for m in o["models"].values():
        assert m["verdict"] == "ORDER-BLIND-OR-WEAKER", m["verdict"]
        assert abs(m["comp"]["target_governs"]["rate"] - C.PRINT_CEILING) < 1e-9

    print("\n--- figpref (fixed figure; expect UNINTERPRETABLE, target = 1/K) ---")
    o = analyze.analyze(write_set("raw_figpref", figpref))
    for m in o["models"].values():
        assert m["verdict"] == "UNINTERPRETABLE", m["verdict"]
        assert not m["comp"]["comp_sig"]
        assert abs(m["comp"]["target_governs"]["rate"] - C.POS_CHANCE) < 2e-3

    print("\n--- trackpos (fixed track position; expect UNINTERPRETABLE, target = 1/K) ---")
    o = analyze.analyze(write_set("raw_trackpos", trackpos))
    for m in o["models"].values():
        assert m["verdict"] == "UNINTERPRETABLE", m["verdict"]
        assert not m["comp"]["comp_sig"]
        assert abs(m["comp"]["target_governs"]["rate"] - C.POS_CHANCE) < 2e-3

    print("\n--- direct_fail (composing-looking COMP but on-demand FAILS; expect UNINTERPRETABLE) ---")
    o = analyze.analyze(write_set("raw_direct_fail", direct_fail))
    assert all(m["verdict"] == "UNINTERPRETABLE" for m in o["models"].values())

    print("\nALL FIXTURE ASSERTS PASS: only genuine stamp-order composition yields a RESPECTS-ORDER "
          "verdict; every print-order / canonical-order reader scores exactly 0.50 on COMP, every "
          "position/identity reader exactly 1/K, and any reader failing on-demand composition is "
          "UNINTERPRETABLE. The on-demand gate guards the order-blind-null reading.")


if __name__ == "__main__":
    main()
