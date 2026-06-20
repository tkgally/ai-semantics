#!/usr/bin/env python3
"""analyze.py (no API) -- the pre-registered CROSS-FAMILY (heterogeneous-operation) ORDER-SENSITIVE
COMPOSITION verdict. Identical verdict map to every prior Option-C run.

Per model, two subsets:

  DIRECT (on-demand cross-family composition gate): direct_acc = P(pick == stamp-order final color)
    when the query states the order explicitly ("first ... and then ..."). Confirms the model CAN
    compose the SWAP (spatial) and the RECOLOR (attribute) in THIS instrument. Gate: direct_acc >=
    DIRECT_FLOOR. If it fails, COMP is UNINTERPRETABLE (cannot tell spontaneous order-blindness from
    inability-to-compose a heterogeneous pair).

  COMP (headline): the two stamped op-lines are shown (display order decoupled from stamp order) and
    the query does NOT say in which order to apply them. Under the balanced design (proven at build)
    every non-composing reader scores at most PRINT_CEILING = 0.50 -- report-C0 / report-Cr /
    recolor-only / either fixed order / print-order / any fixed-spot or const color. So a COMP
    target-rate whose Wilson-95 lower bound EXCEEDS 0.50 can ONLY come from composing the SWAP and
    the RECOLOR in STAMP order = cross-family order-sensitive COMPOSITION. We report:
      target_rate = P(pick == stamp-order final color)     [cross-family stamp-order composition]
      rev_rate    = P(pick == reversed-order final color)   [applied the two ops in reverse order]
      print_rate  = P(pick == printed/display-order end)    [applied in the order listed]
      c0_rate / cr_rate                                      [reported a single op's color]

Frozen verdict per model (identical map to every prior Option-C run):
  UNINTERPRETABLE        : direct_acc < DIRECT_FLOOR (cannot compose the two ops on demand).
  RESPECTS-ORDER         : direct gate passed AND target_rate Wilson-LB > PRINT_CEILING (0.50).
  ORDER-BLIND-OR-WEAKER  : direct gate passed AND target_rate Wilson-LB <= PRINT_CEILING.

ADJUDICATION (binding, decided BEFORE the run, biased AGAINST the rich reading -- per
decisions/resolved/relational-rung-iii-path-dependence): an operation-order gap here is THIN. The
stamped operation list, the spots, and the colors are IN the record; a single reader applies the two
ops in stamp order and reads off the color (single-reader-recoverable). RESPECTS-ORDER is therefore
reported as a thin "respects operation order" / cross-family-composition finding -- NOT promoted to
rung (iii) / constitution. The rich-side rung (iii) program is documented STRUCTURALLY CLOSED for
text-only stimuli. anchor: internal-contrast-only; no human-comparison claim.
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


def _rate(parsed, pick_fn):
    k = sum(1 for r in parsed if r["pick"] == pick_fn(r))
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

    def print_pick(rec):
        return C.color_at(rec, tuple(rec["display_order"]), rec["s"])

    out = {"direct_floor": floor, "print_ceiling": ceiling, "pos_chance": pos_chance, "models": {}}
    print(f"\n=== CROSS-FAMILY order-sensitive COMPOSITION verdict (direct_floor={floor}, "
          f"print_ceiling={ceiling}, pos_chance={pos_chance:.4f}) ===")
    for name in C.MODELS:
        recs = C.read_jsonl(os.path.join(raw_dir, f"probe-{name}.jsonl"))
        cp = [dict(r, **by_rid[r["rid"]]) for r in recs
              if by_rid[r["rid"]]["subset"] == "comp" and r.get("pick")]
        di = [dict(r, **by_rid[r["rid"]]) for r in recs
              if by_rid[r["rid"]]["subset"] == "direct" and r.get("pick")]
        na = [r for r in recs if r.get("pick") is None]

        dacc = _rate(di, lambda r: r["target_color"])
        manip_pass = dacc["rate"] >= floor

        target = _rate(cp, lambda r: r["target_color"])
        rev = _rate(cp, lambda r: r["rev_color"])
        prnt = _rate(cp, print_pick)
        cr = _rate(cp, lambda r: r["recolor_color"])
        c_oth = _rate(cp, lambda r: r["init_colors"][r["o"]])
        earlier = _rate(cp, lambda r: C.color_at(r, (r["stamp_order"][0],), r["s"]))
        comp_sig = target["wilson95"][0] > ceiling

        if not manip_pass:
            verdict = "UNINTERPRETABLE"
        elif comp_sig:
            verdict = "RESPECTS-ORDER"
        else:
            verdict = "ORDER-BLIND-OR-WEAKER"

        m = {"n_total": len(recs), "n_na": len(na),
             "direct": {"acc": dacc, "manip_pass": manip_pass},
             "comp": {"target_governs": target, "rev": rev, "print": prnt,
                      "cr": cr, "c_oth": c_oth, "earlier_only": earlier, "comp_sig": comp_sig},
             "verdict": verdict}
        out["models"][name] = m
        print(f"\n  {name}: VERDICT = {verdict}  (NA={len(na)})")
        print(f"     DIRECT on-demand gate (cross-family): acc={dacc['rate']:.3f} "
              f"CI={dacc['wilson95']} (n={dacc['n']}; floor {floor}) -> "
              f"{'PASS' if manip_pass else 'FAIL'}")
        print(f"     COMP target (stamp-order composition) rate={target['rate']:.3f} "
              f"CI={target['wilson95']} (n={target['n']}; print ceiling {ceiling}) sig={comp_sig}")
        print(f"     COMP breakdown: reversed-order={rev['rate']:.3f}, print-order={prnt['rate']:.3f}, "
              f"Cr(recolor)={cr['rate']:.3f}, C_oth={c_oth['rate']:.3f}, earlier-only={earlier['rate']:.3f}")

    verdicts = {k: m["verdict"] for k, m in out["models"].items()}
    out["respects_order_models"] = [k for k, v in verdicts.items() if v == "RESPECTS-ORDER"]
    out["order_blind_models"] = [k for k, v in verdicts.items() if v == "ORDER-BLIND-OR-WEAKER"]
    out["uninterpretable_models"] = [k for k, v in verdicts.items() if v == "UNINTERPRETABLE"]
    print(f"\n  => RESPECTS-ORDER (cross-family composition) models: "
          f"{out['respects_order_models'] or 'none'}")
    print(f"  => ORDER-BLIND-OR-WEAKER models: {out['order_blind_models'] or 'none'}")
    print(f"  => UNINTERPRETABLE models: {out['uninterpretable_models'] or 'none'}")
    print("  (ADJUDICATED THIN before the run: the stamped operation list, spots, and colors are in "
          "the record, so an order gap is single-reader-recoverable -- 'respects operation order', "
          "NOT rung (iii). Rich-side rung (iii) is documented structurally closed for text-only "
          "stimuli. internal-contrast-only; no human-comparison claim.)")
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
