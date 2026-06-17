#!/usr/bin/env python3
"""analyze.py (no API) — the pre-registered RUNG-(ii) INTEGRATION verdict.

Per model, two subsets:

  DIRECT (on-demand conjunction gate): direct_acc = P(pick == target) when the query EXPLICITLY
    restates both constraints and asks for the figure. Confirms the model CAN conjoin the earlier
    shape and the latest pattern in THIS instrument. Gate: direct_acc >= DIRECT_FLOOR. If it fails,
    INTEG is UNINTERPRETABLE (cannot tell spontaneous-non-integration from inability-to-conjoin).

  INTEG (headline): query does NOT instruct combination. Under the balanced design every grid-
    position strategy, every figure-identity preference and the frequency heuristic score exactly
    1/K, and every SINGLE-attribute reader (latest-pattern-only = overwrite; earlier-shape-only)
    scores exactly OVERWRITE_CEILING = 0.50 (each constraint is 2-way; proven at build). So an
    INTEG target-rate whose Wilson-95 lower bound EXCEEDS 0.50 can only come from conjoining BOTH
    turns -- the earlier, non-terminal turn SURVIVED = INTEGRATION (rung ii). We report:
      target_rate       = P(pick == both-match)      [integration]
      latest_only_rate  = P(pick == other pattern-match)   [overwrite "kept the latest only"]
      earlier_only_rate = P(pick == other shape-match)     [kept the earlier only]
      neither_rate      = P(pick == neither)
    target_rate Wilson-LB > 0.50 = INTEGRATION (earlier turn survives). target_rate ~0.50 with
    the DIRECT gate passed is the OVERWRITE-OR-WEAKER null (the thin verdict sharpened: overwrite,
    not integration, even when integration was available -- essay/update-is-not-constitution
    revision trigger (a)). Position diagnostics (pick==last/first grid line) confirm the model is
    not merely grid-position-driven.

Frozen verdict per model:
  UNINTERPRETABLE      : direct_acc < DIRECT_FLOOR (on-demand conjunction failed here).
  INTEGRATION          : direct gate passed AND target_rate Wilson-LB > OVERWRITE_CEILING.
  OVERWRITE-OR-WEAKER  : direct gate passed AND target_rate Wilson-LB <= OVERWRITE_CEILING.

Essay reading (update-is-not-constitution): INTEGRATION => rung (ii) occupied (the earlier turn is
not discarded; agreements compose). OVERWRITE-OR-WEAKER => rung (ii) NOT reached; the thin overwrite
verdict is sharpened (rung i only). BOTH outcomes are on the THIN / single-reader-recoverable side
-- neither approaches constitution. anchor: internal-contrast-only; no human-comparison claim.
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
    ceiling = stim["overwrite_ceiling"]
    pos_chance = stim["pos_chance"]
    out = {"direct_floor": floor, "overwrite_ceiling": ceiling, "pos_chance": pos_chance,
           "models": {}}
    print(f"\n=== Rung-(ii) INTEGRATION verdict (direct_floor={floor}, "
          f"overwrite_ceiling={ceiling}, pos_chance={pos_chance}) ===")
    for name in C.MODELS:
        recs = C.read_jsonl(os.path.join(raw_dir, f"probe-{name}.jsonl"))
        ig = [r for r in recs if by_rid[r["rid"]]["subset"] == "integ" and r.get("pick")]
        di = [r for r in recs if by_rid[r["rid"]]["subset"] == "direct" and r.get("pick")]
        na = [r for r in recs if r.get("pick") is None]

        dacc = rate(di, "correct_label", by_rid)
        manip_pass = dacc["rate"] >= floor

        target = rate(ig, "correct_label", by_rid)
        latest_only = rate(ig, "latest_only_label", by_rid)
        earlier_only = rate(ig, "earlier_only_label", by_rid)
        neither = rate(ig, "neither_label", by_rid)
        pos_last = rate(ig, "last_pos_label", by_rid)
        pos_first = rate(ig, "first_pos_label", by_rid)
        integ_sig = target["wilson95"][0] > ceiling

        if not manip_pass:
            verdict = "UNINTERPRETABLE"
        elif integ_sig:
            verdict = "INTEGRATION"
        else:
            verdict = "OVERWRITE-OR-WEAKER"

        m = {"n_total": len(recs), "n_na": len(na),
             "direct": {"acc": dacc, "manip_pass": manip_pass},
             "integ": {"target_governs": target, "latest_only": latest_only,
                       "earlier_only": earlier_only, "neither": neither,
                       "pos_last_rate": pos_last["rate"], "pos_first_rate": pos_first["rate"],
                       "integ_sig": integ_sig},
             "verdict": verdict}
        out["models"][name] = m
        print(f"\n  {name}: VERDICT = {verdict}  (NA={len(na)})")
        print(f"     DIRECT on-demand gate: acc={dacc['rate']:.3f} CI={dacc['wilson95']} "
              f"(n={dacc['n']}; floor {floor}) -> {'PASS' if manip_pass else 'FAIL'}")
        print(f"     INTEG target (integration) rate={target['rate']:.3f} CI={target['wilson95']} "
              f"(n={target['n']}; overwrite ceiling {ceiling}) sig={integ_sig}")
        print(f"     INTEG breakdown: latest-only={latest_only['rate']:.3f}, "
              f"earlier-only={earlier_only['rate']:.3f}, neither={neither['rate']:.3f}")
        print(f"     INTEG position diag: pick==last-line {pos_last['rate']:.3f}, "
              f"pick==first-line {pos_first['rate']:.3f}")

    verdicts = {k: m["verdict"] for k, m in out["models"].items()}
    integ_models = [k for k, v in verdicts.items() if v == "INTEGRATION"]
    overwrite_models = [k for k, v in verdicts.items() if v == "OVERWRITE-OR-WEAKER"]
    out["integration_models"] = integ_models
    out["overwrite_or_weaker_models"] = overwrite_models
    print(f"\n  => INTEGRATION (rung ii: earlier turn survives) models: {integ_models or 'none'}")
    print(f"  => OVERWRITE-OR-WEAKER (rung i only) models: {overwrite_models or 'none'}")
    print("  (essay/update-is-not-constitution: INTEGRATION = rung ii occupied; "
          "OVERWRITE-OR-WEAKER = thin overwrite verdict sharpened. Both THIN; no constitution.)")
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
