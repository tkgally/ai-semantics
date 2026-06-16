#!/usr/bin/env python3
"""analyze.py (no API) — the pre-registered Option-A verdict.

Per model, two subsets:

  DIRECT (manipulation check): direct_acc = P(pick == correct) pooled over DIR_MR + DIR_LR.
    Confirms ON-DEMAND recency comprehension survives in THIS instrument (figures + reassignment
    + grid). Gate: direct_acc >= DIRECT_FLOOR. If it fails, SPONT is UNINTERPRETABLE for that
    model (we cannot tell spontaneous-non-use from instrument failure).

  SPONT (headline): the query does NOT mention recency. Under the balanced design every position
    strategy, every figure-preference ordering, and the frequency heuristic all score exactly 1/K
    (proven at build), so any rate above chance can only come from spontaneously weighting the
    round stamp. We report:
      latest_rate = P(pick == max-round figure)   [latest-governs: the operative-convention reading]
      first_rate  = P(pick == min-round figure)   [anti-recency / first-governs diagnostic]
    Either rate's Wilson-95 lower bound exceeding POS_CHANCE (0.25) is order-sensitivity = a
    NON-COMMUTATIVE (path-dependent) convention. Neither exceeding it (both ~chance) with the
    DIRECT gate passed is the ratified narrow A-null: "comprehends recency on demand but does not
    spontaneously weight it here." Position-follower diagnostics (pick==last/first physical line)
    are reported to confirm the model is not merely position-driven.

Frozen verdict per model:
  UNINTERPRETABLE          : direct_acc < DIRECT_FLOOR (on-demand check failed here).
  SPONTANEOUS-RECENCY      : direct gate passed AND latest_rate Wilson-LB > 0.25 AND first not.
  SPONTANEOUS-ANTI-RECENCY : direct gate passed AND first_rate Wilson-LB > 0.25 AND latest not.
  ORDER-SENSITIVE-MIXED    : direct gate passed AND BOTH LBs > 0.25 (guard; report both).
  COMMUTATIVE-HERE         : direct gate passed AND NEITHER LB > 0.25 (the narrow A-null).

Conjecture reading (commutative-convention): SPONTANEOUS-* / ORDER-SENSITIVE-MIXED = order-
sensitive => evidence AGAINST commutativity (would move the conjecture toward falsification, under
the binding scope limits). COMMUTATIVE-HERE = consistent with commutativity, in the narrow
spontaneous-weighting sense ONLY (never "comprehends recency" in general, never "chose to
ignore recency"). anchor: internal-contrast-only; no human-comparison claim.
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
    pos_chance = stim["pos_chance"]
    out = {"direct_floor": floor, "pos_chance": pos_chance, "models": {}}
    print(f"\n=== Option-A spontaneous-recency verdict (direct_floor={floor}, "
          f"pos_chance={pos_chance}) ===")
    for name in C.MODELS:
        recs = C.read_jsonl(os.path.join(raw_dir, f"probe-{name}.jsonl"))
        sp = [r for r in recs if by_rid[r["rid"]]["subset"] == "spont" and r.get("pick")]
        di = [r for r in recs if by_rid[r["rid"]]["subset"] == "direct" and r.get("pick")]
        na = [r for r in recs if r.get("pick") is None]

        # DIRECT manipulation check
        dacc = rate(di, "correct_label", by_rid)
        dir_by = {}
        for q in ("DIR_MR", "DIR_LR"):
            qr = [r for r in di if by_rid[r["rid"]]["query"] == q]
            dir_by[q] = rate(qr, "correct_label", by_rid)
        manip_pass = dacc["rate"] >= floor

        # SPONT headline
        latest = rate(sp, "max_round_label", by_rid)
        first = rate(sp, "min_round_label", by_rid)
        pos_last = rate(sp, "last_pos_label", by_rid)
        pos_first = rate(sp, "first_pos_label", by_rid)
        latest_sig = latest["wilson95"][0] > pos_chance
        first_sig = first["wilson95"][0] > pos_chance

        if not manip_pass:
            verdict = "UNINTERPRETABLE"
        elif latest_sig and first_sig:
            verdict = "ORDER-SENSITIVE-MIXED"
        elif latest_sig:
            verdict = "SPONTANEOUS-RECENCY"
        elif first_sig:
            verdict = "SPONTANEOUS-ANTI-RECENCY"
        else:
            verdict = "COMMUTATIVE-HERE"

        m = {"n_total": len(recs), "n_na": len(na),
             "direct": {"acc": dacc, "by_query": dir_by, "manip_pass": manip_pass},
             "spont": {"latest_governs": latest, "first_governs": first,
                       "pos_last_rate": pos_last["rate"], "pos_first_rate": pos_first["rate"],
                       "latest_sig": latest_sig, "first_sig": first_sig},
             "verdict": verdict}
        out["models"][name] = m
        print(f"\n  {name}: VERDICT = {verdict}  (NA={len(na)})")
        print(f"     DIRECT manip-check: acc={dacc['rate']:.3f} CI={dacc['wilson95']} "
              f"(n={dacc['n']}; floor {floor}) -> {'PASS' if manip_pass else 'FAIL'}")
        print(f"       by dir: MR={dir_by['DIR_MR']['rate']:.3f} (n={dir_by['DIR_MR']['n']}), "
              f"LR={dir_by['DIR_LR']['rate']:.3f} (n={dir_by['DIR_LR']['n']})")
        print(f"     SPONT latest-governs rate={latest['rate']:.3f} CI={latest['wilson95']} "
              f"(n={latest['n']}; chance {pos_chance}) sig={latest_sig}")
        print(f"     SPONT first-governs  rate={first['rate']:.3f} CI={first['wilson95']} "
              f"sig={first_sig}")
        print(f"     SPONT position diag: pick==last-line {pos_last['rate']:.3f}, "
              f"pick==first-line {pos_first['rate']:.3f}")

    verdicts = {k: m["verdict"] for k, m in out["models"].items()}
    order_sensitive = [k for k, v in verdicts.items()
                       if v in ("SPONTANEOUS-RECENCY", "SPONTANEOUS-ANTI-RECENCY",
                                "ORDER-SENSITIVE-MIXED")]
    commutative = [k for k, v in verdicts.items() if v == "COMMUTATIVE-HERE"]
    out["order_sensitive_models"] = order_sensitive
    out["commutative_here_models"] = commutative
    print(f"\n  => order-sensitive (non-commutative) models: {order_sensitive or 'none'}")
    print(f"  => commutative-here (A-null) models: {commutative or 'none'}")
    print("  (conjecture/commutative-convention: order-sensitive = evidence AGAINST commutativity;"
          " commutative-here = consistent, narrow spontaneous-weighting sense only.)")
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
