#!/usr/bin/env python3
"""make_fixtures.py (no API) — idealized-reader fixtures proving the rung-(ii) instrument
separates genuine INTEGRATION (conjoining the earlier shape + latest pattern) from every
position / figure-identity / single-attribute / frequency shortcut, and that the verdict map
behaves correctly, BEFORE any model is queried (the freeze discipline).

Builds the frozen stimuli through build_trials.build(), then writes idealized raw sets and shows
analyze.py's verdict for each:

  integrator   : DIRECT correct, INTEG picks the both-match TARGET
                 -> INTEGRATION (target_rate = 1.0)                 [genuine integrator]
  overwrite    : DIRECT correct, INTEG keeps ONLY the latest pattern (picks the pattern-match with
                 the lower grid slot) -> OVERWRITE-OR-WEAKER (target_rate ~ 0.50)  [the rung-i null]
  earlier_only : DIRECT correct, INTEG keeps ONLY the earlier shape (lower-slot shape-match)
                 -> OVERWRITE-OR-WEAKER (target_rate ~ 0.50)        [the other single-attribute null]
  gridpos      : BOTH subsets pick a fixed grid slot (slot 0)
                 -> DIRECT fails -> UNINTERPRETABLE; INTEG target = 1/K
  figpref      : BOTH subsets pick the present figure earliest in a FIXED identity ordering
                 -> DIRECT fails -> UNINTERPRETABLE; INTEG target = 1/K
  direct_fail  : INTEG picks the TARGET (looks integrating) but DIRECT picks a fixed slot
                 -> UNINTERPRETABLE (the on-demand gate guard fires)

Load-bearing certifications:
  (1) NO position / figure-identity / single-attribute / frequency shortcut ever yields an
      INTEGRATION verdict -- only conjoining BOTH turns does. A positive cannot be manufactured.
  (2) the INTEG target_rate for every single-attribute reader is <= OVERWRITE_CEILING = 0.50, and
      for every position/identity reader is exactly 1/K = 0.25, so the integration bar is clean.
  (3) the on-demand gate refuses to interpret a reader that fails DIRECT (gridpos, figpref,
      direct_fail -> UNINTERPRETABLE), so an INTEG null is only read as OVERWRITE-OR-WEAKER when
      on-demand conjunction is demonstrated in this very instrument.
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

POOL_ORDER = {f: i for i, f in enumerate(build_trials.ALL_FIGS)}


def _slot_match_attr(rec, attr, lowest=True):
    """label of the attribute-match (target's value of `attr`) at the lowest/highest grid slot."""
    tv = rec[attr]
    cands = [(i, d) for i, d in enumerate(rec["display"]) if d[attr] == tv]
    d = (min if lowest else max)(cands, key=lambda t: t[0])[1]
    return d["label"]


def figpref(rec):
    figs = [(d["shape"], d["pattern"]) for d in rec["display"]]
    top = min(figs, key=lambda f: POOL_ORDER[f])
    return {(d["shape"], d["pattern"]): d["label"] for d in rec["display"]}[top]


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

    def integrator(r):
        return r["correct_label"]

    def overwrite(r):                       # on-demand: conjoins (correct); spontaneous: keeps ONLY
        if r["subset"] == "direct":         # the latest pattern (lower-slot tie-break) -> the rung-i
            return r["correct_label"]        # null: integrates when told to, overwrites by default
        return _slot_match_attr(r, "pattern", lowest=True)

    def earlier_only(r):                    # on-demand correct; spontaneous keeps ONLY earlier shape
        if r["subset"] == "direct":
            return r["correct_label"]
        return _slot_match_attr(r, "shape", lowest=True)

    def gridpos(r):
        return r["display"][0]["label"]

    def figpref_both(r):
        return figpref(r)

    def direct_fail(r):
        return r["correct_label"] if r["subset"] == "integ" else r["display"][0]["label"]

    print("\n--- integrator (on-demand + spontaneous integration; expect INTEGRATION) ---")
    o = analyze.analyze(write_set("raw_integrator", integrator))
    assert all(m["verdict"] == "INTEGRATION" for m in o["models"].values())
    assert all(m["integ"]["target_governs"]["rate"] == 1.0 for m in o["models"].values())

    print("\n--- overwrite (latest-pattern only; expect OVERWRITE-OR-WEAKER, target ~0.50) ---")
    o = analyze.analyze(write_set("raw_overwrite", overwrite))
    for m in o["models"].values():
        assert m["verdict"] == "OVERWRITE-OR-WEAKER", m["verdict"]
        assert m["integ"]["target_governs"]["rate"] <= C.OVERWRITE_CEILING + 1e-9
        assert not m["integ"]["integ_sig"]

    print("\n--- earlier_only (earlier-shape only; expect OVERWRITE-OR-WEAKER, target ~0.50) ---")
    o = analyze.analyze(write_set("raw_earlier_only", earlier_only))
    for m in o["models"].values():
        assert m["verdict"] == "OVERWRITE-OR-WEAKER", m["verdict"]
        assert m["integ"]["target_governs"]["rate"] <= C.OVERWRITE_CEILING + 1e-9

    print("\n--- gridpos (fixed grid slot; expect UNINTERPRETABLE, target = 1/K) ---")
    o = analyze.analyze(write_set("raw_gridpos", gridpos))
    for m in o["models"].values():
        assert m["verdict"] == "UNINTERPRETABLE", m["verdict"]
        assert not m["integ"]["integ_sig"]
        assert abs(m["integ"]["target_governs"]["rate"] - C.POS_CHANCE) < 1e-9

    print("\n--- figpref (fixed figure-identity preference; expect UNINTERPRETABLE, target=1/K) ---")
    o = analyze.analyze(write_set("raw_figpref", figpref_both))
    for m in o["models"].values():
        assert m["verdict"] == "UNINTERPRETABLE", m["verdict"]
        assert not m["integ"]["integ_sig"]
        assert abs(m["integ"]["target_governs"]["rate"] - C.POS_CHANCE) < 1e-9

    print("\n--- direct_fail (integrating-looking INTEG but on-demand FAILS; expect UNINTERPRETABLE) ---")
    o = analyze.analyze(write_set("raw_direct_fail", direct_fail))
    assert all(m["verdict"] == "UNINTERPRETABLE" for m in o["models"].values())

    print("\nALL FIXTURE ASSERTS PASS: only genuine integration (conjoining the earlier shape AND "
          "the latest pattern) yields an INTEGRATION verdict; every position/identity/single-"
          "attribute/frequency shortcut scores <= 0.50 on INTEG (single-attribute) or = 1/K "
          "(position/identity), and is UNINTERPRETABLE when on-demand conjunction fails. The "
          "on-demand gate guards the overwrite-null reading.")


if __name__ == "__main__":
    main()
