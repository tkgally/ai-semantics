#!/usr/bin/env python3
"""make_fixtures.py (no API) -- idealized-reader fixtures proving the THREE-MOVE Option-C
ORDER-SENSITIVE COMPOSITION instrument separates a genuine STAMP-ORDER composer from every
figure-identity / track-position / canonical-order / print-order / HALF-COMPOSER / start / single-move
shortcut, and that the verdict map behaves correctly, BEFORE any model is queried.

Builds the frozen stimuli through build_trials.build(), then writes idealized raw sets and shows
analyze.py's verdict for each:

  stamp_order   : DIRECT correct, COMP picks the STAMP-ORDER end figure
                  -> RESPECTS-ORDER (target_rate = 1.0)               [genuine 3-move composer]
  half_composer : DIRECT correct (told the order), COMP pins ONE move's slot by stamp and fills the
                  remaining two-move sub-order by the PRINT order
                  -> ORDER-BLIND-OR-WEAKER (target_rate = 0.50)       [the strongest non-composer]
  canonical     : DIRECT correct, COMP always applies a FIXED type-order regardless of stamps
                  -> ORDER-BLIND-OR-WEAKER (target_rate = 1/6)        [a fixed-order reader]
  print_order   : DIRECT correct, COMP applies the moves in PRINT order
                  -> ORDER-BLIND-OR-WEAKER (target_rate = 1/6)        [reads the listed order]
  figpref       : BOTH subsets pick a FIXED figure (triangle)
                  -> DIRECT fails -> UNINTERPRETABLE; COMP target = 1/K
  trackpos      : BOTH subsets pick a FIXED track position (position 0)
                  -> DIRECT fails -> UNINTERPRETABLE; COMP target = 1/K
  direct_fail   : COMP picks the stamp-order TARGET (looks composing) but DIRECT picks a fixed
                  position -> UNINTERPRETABLE (the on-demand gate guard fires)

Load-bearing certifications:
  (1) NO figure / track-position / canonical-order / print-order / HALF-COMPOSER / start / single-move
      shortcut ever yields a RESPECTS-ORDER verdict -- only ordering ALL THREE moves by their STAMPS
      does. A positive cannot be manufactured by a non-composer; in particular the strongest
      non-composer (the half-composer) sits exactly at the 0.50 ceiling and is read as a null.
  (2) the COMP target_rate for the half-composer is exactly PRINT_CEILING = 0.50 (Wilson-LB < 0.50,
      not significant); for the canonical / print reader exactly 1/6; for the position / identity
      reader exactly 1/K. So the 0.50 bar is clean.
  (3) the on-demand gate refuses to interpret a reader that fails DIRECT (figpref, trackpos,
      direct_fail -> UNINTERPRETABLE), so a COMP null is only read as ORDER-BLIND-OR-WEAKER when
      on-demand THREE-move composition is demonstrated in this very instrument.
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

    def half_composer(r):                   # DIRECT correct; COMP pins last slot by stamp, rest print
        if r["subset"] == "direct":
            return r["target_shape"]
        return build_trials._half_composer_pick(r, 2)

    def canonical(r):                       # DIRECT correct; COMP always the fixed order (FLIP,SLIDE,TWIST)
        if r["subset"] == "direct":
            return r["target_shape"]
        return r["track"][C.apply_seq(r["start_idx"], tuple(C.MOVE_NAMES))]

    def print_order(r):                     # DIRECT correct; COMP applies moves in PRINT order
        if r["subset"] == "direct":
            return r["target_shape"]
        return r["track"][C.apply_seq(r["start_idx"], tuple(r["display_moves"]))]

    def figpref(r):
        return C.SHAPES[0]                  # always "triangle"

    def trackpos(r):
        return r["track"][0]                # always track position 0

    def direct_fail(r):
        return r["target_shape"] if r["subset"] == "comp" else r["track"][0]

    print("\n--- stamp_order (on-demand + spontaneous 3-move stamp-order; expect RESPECTS-ORDER) ---")
    o = analyze.analyze(write_set("raw_stamp_order", stamp_order))
    assert all(m["verdict"] == "RESPECTS-ORDER" for m in o["models"].values())
    assert all(m["comp"]["target_governs"]["rate"] == 1.0 for m in o["models"].values())

    print("\n--- half_composer (pins one slot, prints the rest; expect ORDER-BLIND, target 0.50) ---")
    o = analyze.analyze(write_set("raw_half_composer", half_composer))
    for m in o["models"].values():
        assert m["verdict"] == "ORDER-BLIND-OR-WEAKER", m["verdict"]
        assert abs(m["comp"]["target_governs"]["rate"] - C.PRINT_CEILING) < 1e-9
        assert not m["comp"]["comp_sig"], "half-composer must NOT clear the 0.50 bar"

    print("\n--- canonical (fixed type-order; expect ORDER-BLIND-OR-WEAKER, target 1/6) ---")
    o = analyze.analyze(write_set("raw_canonical", canonical))
    for m in o["models"].values():
        assert m["verdict"] == "ORDER-BLIND-OR-WEAKER", m["verdict"]
        assert abs(m["comp"]["target_governs"]["rate"] - C.POS_CHANCE) < 2e-3  # 1/K rounds to 0.1667
        assert not m["comp"]["comp_sig"]

    print("\n--- print_order (reads print order; expect ORDER-BLIND-OR-WEAKER, target 1/6) ---")
    o = analyze.analyze(write_set("raw_print_order", print_order))
    for m in o["models"].values():
        assert m["verdict"] == "ORDER-BLIND-OR-WEAKER", m["verdict"]
        assert abs(m["comp"]["target_governs"]["rate"] - C.POS_CHANCE) < 2e-3  # 1/K rounds to 0.1667

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

    print("\nALL FIXTURE ASSERTS PASS: only genuine THREE-move stamp-order composition yields a "
          "RESPECTS-ORDER verdict; the strongest non-composer (the half-composer) scores exactly 0.50 "
          "on COMP and reads as a null; every canonical / print reader scores 1/6, every "
          "position/identity reader 1/K, and any reader failing on-demand composition is "
          "UNINTERPRETABLE. The on-demand gate guards the order-blind-null reading.")


if __name__ == "__main__":
    main()
