#!/usr/bin/env python3
"""analyze.py (no API) -- the pre-registered INTEGRATION-UNDER-LOAD verdict (burial depth 2).

Per model, two subsets:

  DIRECT (on-demand conjunction-of-three gate): direct_acc = P(pick == target) when the query
    EXPLICITLY restates all three constraints and asks for the figure. Confirms the model CAN
    conjoin the earliest shape, the middle pattern and the latest color in THIS instrument. Gate:
    direct_acc >= DIRECT_FLOOR. If it fails, INTEG is UNINTERPRETABLE (cannot tell spontaneous
    non-integration from inability-to-conjoin-three).

  INTEG (headline): query does NOT instruct combination. Under the balanced design every grid-
    position strategy and figure-identity preference scores exactly 1/K = 0.125; every SINGLE-
    attribute reader scores <= 0.25; every TWO-attribute (drop-one-turn) reader -- including
    RECENT-TWO (keep the latest two = pattern+color, DROP the buried earliest shape) -- scores
    exactly TWO_ATTR_CEILING = 0.50 (proven at build, certified on fixtures). So an INTEG target-
    rate whose Wilson-95 lower bound EXCEEDS 0.50 can only come from conjoining ALL THREE turns --
    the buried earliest turn SURVIVED under depth-2 load = INTEGRATION-UNDER-LOAD. We report:
      target_rate     = P(pick == all-three-match)               [integration under load]
      twin_shape_rate = P(pick == figure differing only in shape) [RECENT-TWO: dropped the earliest]
      twin_pattern_rate / twin_color_rate                         [dropped the middle / latest]
    target_rate Wilson-LB > 0.50 = INTEGRATION-UNDER-LOAD (the buried earliest turn survives).
    target_rate ~0.50 with the DIRECT gate passed is the PARTIAL-OR-OVERWRITE null: a turn is shed
    under load (the earliest most plausibly, recoverable as an elevated twin_shape_rate), which
    BOUNDS claim/relational-order-sensitive-reassignment to depth-1 integration. Position
    diagnostics (pick==last/first grid line) confirm the model is not merely grid-position-driven.

Frozen verdict per model:
  UNINTERPRETABLE       : direct_acc < DIRECT_FLOOR (on-demand conjunction-of-three failed here).
  INTEGRATION-UNDER-LOAD: direct gate passed AND target_rate Wilson-LB > TWO_ATTR_CEILING.
  PARTIAL-OR-OVERWRITE  : direct gate passed AND target_rate Wilson-LB <= TWO_ATTR_CEILING.

Essay reading (update-is-not-constitution, rung (ii) honesty box "harder load / more turns"):
INTEGRATION-UNDER-LOAD => rung (ii) integration is ROBUST to burial depth 2 (strengthens the
result; the "more turns" caveat is bounded in the claim's favour). PARTIAL-OR-OVERWRITE => the
buried earliest turn is shed under load (bounds the integration claim to depth 1). BOTH outcomes
are on the THIN / single-reader-recoverable side -- neither approaches constitution. anchor:
internal-contrast-only; no human-comparison claim.
"""
import argparse
import json
import math
import os

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def rate(parsed, key, by_rid):
    k = sum(1 for r in parsed if r["pick"] == by_rid[r["rid"]][key])
    n = len(parsed)
    lo, hi = wilson(k, n)
    return {"k": k, "n": n, "rate": round(k / n, 4) if n else 0.0,
            "wilson95": [round(lo, 4), round(hi, 4)]}


def analyze(raw_dir):
    stim = json.load(open(os.path.join(HERE, "stimuli.json")))
    by_rid = {r["rid"]: r for r in stim["records"]}
    floor = stim["direct_floor"]
    two_ceiling = stim["two_attr_ceiling"]
    one_ceiling = stim["single_attr_ceiling"]
    pos_chance = stim["pos_chance"]
    out = {"direct_floor": floor, "two_attr_ceiling": two_ceiling,
           "single_attr_ceiling": one_ceiling, "pos_chance": pos_chance, "models": {}}
    print(f"\n=== INTEGRATION-UNDER-LOAD verdict (direct_floor={floor}, "
          f"two_attr_ceiling={two_ceiling}, single_attr_ceiling={one_ceiling}, "
          f"pos_chance={pos_chance}) ===")
    for name in C.MODELS:
        recs = C.read_jsonl(os.path.join(raw_dir, f"probe-{name}.jsonl"))
        ig = [r for r in recs if by_rid[r["rid"]]["subset"] == "integ" and r.get("pick")]
        di = [r for r in recs if by_rid[r["rid"]]["subset"] == "direct" and r.get("pick")]
        na = [r for r in recs if r.get("pick") is None]

        dacc = rate(di, "correct_label", by_rid)
        manip_pass = dacc["rate"] >= floor

        target = rate(ig, "correct_label", by_rid)
        twin_shape = rate(ig, "twin_shape_label", by_rid)
        twin_pattern = rate(ig, "twin_pattern_label", by_rid)
        twin_color = rate(ig, "twin_color_label", by_rid)
        pos_last = rate(ig, "last_pos_label", by_rid)
        pos_first = rate(ig, "first_pos_label", by_rid)
        integ_sig = target["wilson95"][0] > two_ceiling

        if not manip_pass:
            verdict = "UNINTERPRETABLE"
        elif integ_sig:
            verdict = "INTEGRATION-UNDER-LOAD"
        else:
            verdict = "PARTIAL-OR-OVERWRITE"

        m = {"n_total": len(recs), "n_na": len(na),
             "direct": {"acc": dacc, "manip_pass": manip_pass},
             "integ": {"target_governs": target,
                       "twin_shape_recent_two": twin_shape,
                       "twin_pattern": twin_pattern, "twin_color": twin_color,
                       "pos_last_rate": pos_last["rate"], "pos_first_rate": pos_first["rate"],
                       "integ_sig": integ_sig},
             "verdict": verdict}
        out["models"][name] = m
        print(f"\n  {name}: VERDICT = {verdict}  (NA={len(na)})")
        print(f"     DIRECT on-demand gate (conjoin three): acc={dacc['rate']:.3f} "
              f"CI={dacc['wilson95']} (n={dacc['n']}; floor {floor}) -> "
              f"{'PASS' if manip_pass else 'FAIL'}")
        print(f"     INTEG target (integration-under-load) rate={target['rate']:.3f} "
              f"CI={target['wilson95']} (n={target['n']}; two-attr ceiling {two_ceiling}) "
              f"sig={integ_sig}")
        print(f"     INTEG breakdown: RECENT-TWO/twin-shape (dropped earliest)={twin_shape['rate']:.3f}, "
              f"twin-pattern={twin_pattern['rate']:.3f}, twin-color={twin_color['rate']:.3f}")
        print(f"     INTEG position diag: pick==last-line {pos_last['rate']:.3f}, "
              f"pick==first-line {pos_first['rate']:.3f}")

    verdicts = {k: m["verdict"] for k, m in out["models"].items()}
    integ_models = [k for k, v in verdicts.items() if v == "INTEGRATION-UNDER-LOAD"]
    partial_models = [k for k, v in verdicts.items() if v == "PARTIAL-OR-OVERWRITE"]
    out["integration_under_load_models"] = integ_models
    out["partial_or_overwrite_models"] = partial_models
    print(f"\n  => INTEGRATION-UNDER-LOAD (buried earliest turn survives depth 2) models: "
          f"{integ_models or 'none'}")
    print(f"  => PARTIAL-OR-OVERWRITE (a turn shed under load) models: {partial_models or 'none'}")
    print("  (update-is-not-constitution rung-(ii) honesty box: INTEGRATION-UNDER-LOAD = robust to "
          "'more turns'; PARTIAL-OR-OVERWRITE = bounds integration to depth 1. Both THIN.)")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw-dir", default=os.path.join(HERE, "raw"))
    a = ap.parse_args()
    out = analyze(a.raw_dir)
    json.dump(out, open(os.path.join(a.raw_dir, "analysis.json"), "w"), indent=2)
    print(f"\n  wrote {os.path.join(a.raw_dir, 'analysis.json')}")


if __name__ == "__main__":
    main()
