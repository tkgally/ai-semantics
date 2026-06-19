#!/usr/bin/env python3
"""analyze.py (no API) -- the pre-registered ORDER-SENSITIVE COMPOSITION (Option-C) verdict.

Per model, two subsets:

  DIRECT (on-demand composition gate): direct_acc = P(pick == stamp-order target) when the query
    states the order explicitly ("first ... then ..."). Confirms the model CAN compose the two non-
    commuting moves in THIS instrument. Gate: direct_acc >= DIRECT_FLOOR. If it fails, COMP is
    UNINTERPRETABLE (cannot tell spontaneous order-blindness from inability-to-compose).

  COMP (headline): the two stamped move-lines are shown (possibly out of round order) and the query
    does NOT say which move came first. Under the balanced design every figure-identity picker and
    every track-position picker scores 1/K; the PRINT-ORDER reader and BOTH canonical fixed-order
    readers score EXACTLY PRINT_CEILING = 0.50; the start / single-move / reversed-order readers
    score 0 (all proven at build). So a COMP target-rate whose Wilson-95 lower bound EXCEEDS 0.50
    can ONLY come from ordering the two moves by their STAMPS = order-sensitive COMPOSITION. We
    report:
      target_rate   = P(pick == stamp-order end figure)     [order-sensitive composition]
      swapped_rate  = P(pick == reversed-order end figure)  [applied the moves in the wrong order]
      start_rate / cycle1_rate / swap1_rate                 [didn't compose both moves]
    target_rate Wilson-LB > 0.50 = RESPECTS-ORDER. target_rate ~0.50 with the DIRECT gate passed is
    the ORDER-BLIND-OR-WEAKER null (the model reads the moves in print/canonical order, not stamp
    order -- a thin verdict sharpened).

Frozen verdict per model:
  UNINTERPRETABLE        : direct_acc < DIRECT_FLOOR (cannot compose the two moves on demand).
  RESPECTS-ORDER         : direct gate passed AND target_rate Wilson-LB > PRINT_CEILING.
  ORDER-BLIND-OR-WEAKER  : direct gate passed AND target_rate Wilson-LB <= PRINT_CEILING.

ADJUDICATION (binding, decided BEFORE the run, biased AGAINST the rich reading -- per
decisions/resolved/relational-rung-iii-path-dependence): an operation-order gap here is THIN. The
stamped operation list is IN the record; a single reader applies it in stamp order and reads off the
answer (single-reader-recoverable). RESPECTS-ORDER is therefore reported as a thin "respects
operation order" / order-sensitive-COMPOSITION finding -- it is NOT promoted to rung (iii) /
constitution. The rich-side rung-(iii) program is documented as STRUCTURALLY CLOSED for text-only
stimuli (a transcript IS a final content+stamps record). Both verdicts are THIN; anchor: internal-
contrast-only; no human-comparison claim.
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
    ceiling = stim["print_ceiling"]
    pos_chance = stim["pos_chance"]
    out = {"direct_floor": floor, "print_ceiling": ceiling, "pos_chance": pos_chance, "models": {}}
    print(f"\n=== Order-sensitive COMPOSITION verdict (direct_floor={floor}, "
          f"print_ceiling={ceiling}, pos_chance={pos_chance:.4f}) ===")
    for name in C.MODELS:
        recs = C.read_jsonl(os.path.join(raw_dir, f"probe-{name}.jsonl"))
        cp = [r for r in recs if by_rid[r["rid"]]["subset"] == "comp" and r.get("pick")]
        di = [r for r in recs if by_rid[r["rid"]]["subset"] == "direct" and r.get("pick")]
        na = [r for r in recs if r.get("pick") is None]

        dacc = rate(di, "target_shape", by_rid)
        manip_pass = dacc["rate"] >= floor

        target = rate(cp, "target_shape", by_rid)
        swapped = rate(cp, "swapped_shape", by_rid)
        start = rate(cp, "start_shape", by_rid)
        cycle1 = rate(cp, "cycle1_shape", by_rid)
        swap1 = rate(cp, "swap1_shape", by_rid)
        comp_sig = target["wilson95"][0] > ceiling

        if not manip_pass:
            verdict = "UNINTERPRETABLE"
        elif comp_sig:
            verdict = "RESPECTS-ORDER"
        else:
            verdict = "ORDER-BLIND-OR-WEAKER"

        m = {"n_total": len(recs), "n_na": len(na),
             "direct": {"acc": dacc, "manip_pass": manip_pass},
             "comp": {"target_governs": target, "swapped": swapped, "start": start,
                      "cycle1": cycle1, "swap1": swap1, "comp_sig": comp_sig},
             "verdict": verdict}
        out["models"][name] = m
        print(f"\n  {name}: VERDICT = {verdict}  (NA={len(na)})")
        print(f"     DIRECT on-demand gate: acc={dacc['rate']:.3f} CI={dacc['wilson95']} "
              f"(n={dacc['n']}; floor {floor}) -> {'PASS' if manip_pass else 'FAIL'}")
        print(f"     COMP target (stamp-order composition) rate={target['rate']:.3f} "
              f"CI={target['wilson95']} (n={target['n']}; print ceiling {ceiling}) sig={comp_sig}")
        print(f"     COMP breakdown: swapped(reversed-order)={swapped['rate']:.3f}, "
              f"start={start['rate']:.3f}, cycle-only={cycle1['rate']:.3f}, "
              f"swap-only={swap1['rate']:.3f}")

    verdicts = {k: m["verdict"] for k, m in out["models"].items()}
    out["respects_order_models"] = [k for k, v in verdicts.items() if v == "RESPECTS-ORDER"]
    out["order_blind_models"] = [k for k, v in verdicts.items() if v == "ORDER-BLIND-OR-WEAKER"]
    print(f"\n  => RESPECTS-ORDER (order-sensitive composition) models: "
          f"{out['respects_order_models'] or 'none'}")
    print(f"  => ORDER-BLIND-OR-WEAKER models: {out['order_blind_models'] or 'none'}")
    print("  (ADJUDICATED THIN before the run: a stamped operation list is in the record, so an "
          "order gap is single-reader-recoverable -- 'respects operation order', NOT rung (iii). "
          "Rich-side rung (iii) is documented structurally closed for text-only stimuli. "
          "internal-contrast-only; no human-comparison claim.)")
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
