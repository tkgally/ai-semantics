#!/usr/bin/env python3
"""make_fixtures.py (no API) -- idealized-reader fixtures proving the CROSS-FAMILY (heterogeneous-
operation, POSITION-ANCHORED) Option-C ORDER-SENSITIVE COMPOSITION instrument separates a genuine
STAMP-ORDER composer from every non-composing strategy -- INCLUDING the stamp-using PARTIAL readers
(apply-only-the-earlier op) that broke the earlier object-anchored design -- and that the verdict map
behaves correctly, BEFORE any model is queried.

Builds the frozen stimuli through build_trials.build(), then writes idealized raw sets and shows
analyze.py's verdict for each:

  stamp_order   : DIRECT correct, COMP picks the STAMP-ORDER color at the DAX spot
                  -> RESPECTS-ORDER (target_rate = 1.0)               [genuine cross-family composer]
  report_cr     : DIRECT correct, COMP always reports the recolor color
                  -> ORDER-BLIND-OR-WEAKER (target_rate = 0.50)
  fixed_order   : DIRECT correct, COMP always applies SWAP-then-RECOLOR regardless of stamps
                  -> ORDER-BLIND-OR-WEAKER (target_rate = 0.50)
  print_order   : DIRECT correct, COMP applies the two ops in PRINT order
                  -> ORDER-BLIND-OR-WEAKER (target_rate = 0.50)
  earlier_only  : DIRECT correct, COMP applies ONLY the stamp-earlier op (the object-anchored killer)
                  -> ORDER-BLIND-OR-WEAKER (target_rate = 0.25, well below 0.50)
  constcolor    : BOTH subsets pick a FIXED color (red)
                  -> DIRECT fails -> UNINTERPRETABLE; COMP target = 1/6
  direct_fail   : COMP picks the stamp-order TARGET (looks composing) but DIRECT picks a fixed color
                  -> UNINTERPRETABLE (the on-demand gate guard fires)

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
        return r["target_color"]

    def report_cr(r):
        return r["target_color"] if r["subset"] == "direct" else r["recolor_color"]

    def fixed_order(r):
        return r["target_color"] if r["subset"] == "direct" else C.color_at(r, ("SWAP", "RECOLOR"), r["s"])

    def print_order(r):
        return r["target_color"] if r["subset"] == "direct" else C.color_at(r, tuple(r["display_order"]), r["s"])

    def earlier_only(r):
        return r["target_color"] if r["subset"] == "direct" else C.color_at(r, (r["stamp_order"][0],), r["s"])

    def constcolor(r):
        return C.COLORS[0]

    def direct_fail(r):
        return r["target_color"] if r["subset"] == "comp" else C.COLORS[0]

    print("\n--- stamp_order (on-demand + spontaneous stamp-order; expect RESPECTS-ORDER) ---")
    o = analyze.analyze(write_set("raw_stamp_order", stamp_order))
    assert all(m["verdict"] == "RESPECTS-ORDER" for m in o["models"].values())
    assert all(m["comp"]["target_governs"]["rate"] == 1.0 for m in o["models"].values())

    for label, picker, exp in [("report_cr", report_cr, 0.50), ("fixed_order", fixed_order, 0.50),
                               ("print_order", print_order, 0.50), ("earlier_only", earlier_only, 0.25)]:
        print(f"\n--- {label} (non-composer; expect ORDER-BLIND-OR-WEAKER, target ~{exp}) ---")
        o = analyze.analyze(write_set(f"raw_{label}", picker))
        for m in o["models"].values():
            assert m["verdict"] == "ORDER-BLIND-OR-WEAKER", (label, m["verdict"])
            assert m["comp"]["target_governs"]["rate"] <= C.PRINT_CEILING + 1e-9, label
            assert abs(m["comp"]["target_governs"]["rate"] - exp) < 1e-9, (label, m["comp"]["target_governs"]["rate"])
            assert not m["comp"]["comp_sig"], f"{label} must NOT clear the 0.50 bar"

    print("\n--- constcolor (fixed color; expect UNINTERPRETABLE, target = 1/6) ---")
    o = analyze.analyze(write_set("raw_constcolor", constcolor))
    for m in o["models"].values():
        assert m["verdict"] == "UNINTERPRETABLE", m["verdict"]
        assert not m["comp"]["comp_sig"]
        assert abs(m["comp"]["target_governs"]["rate"] - C.POS_CHANCE) < 2e-3

    print("\n--- direct_fail (composing-looking COMP but on-demand FAILS; expect UNINTERPRETABLE) ---")
    o = analyze.analyze(write_set("raw_direct_fail", direct_fail))
    assert all(m["verdict"] == "UNINTERPRETABLE" for m in o["models"].values())

    print("\nALL FIXTURE ASSERTS PASS: only genuine cross-family stamp-order composition yields a "
          "RESPECTS-ORDER verdict; every fixed-order / single-op / print reader scores at most 0.50 "
          "on COMP and the stamp-using earlier-only reader scores 0.25 -- all read as nulls -- and "
          "any reader failing on-demand composition is UNINTERPRETABLE.")


if __name__ == "__main__":
    main()
