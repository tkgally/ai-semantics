#!/usr/bin/env python3
"""analyze.py (no API) — the pre-registered Option-B verdict.

Per model: accuracy = P(pick == correct stamp-designated nonce), pooled over MR+LR and over
the balanced target positions. Diagnostics: position-follower rate P(pick == physically-last
nonce) and P(pick == physically-first nonce) — under the balanced design a pure
position-follower's ACCURACY is ~1/K (POS_CHANCE); these rates show whether a model is in fact
position-driven. Verdict per model (frozen rule):

  PASS (comprehends the stamp value)  iff  acc >= PASS_FLOOR  AND  Wilson 95% lower bound > POS_CHANCE
  FAIL (stamp-blind on this instrument) otherwise

PASS earns that model an Option-A position-rotated, stamp-gated chronology arm (next phase).
FAIL for a model means v4's position-following is explained as stamp-blindness for it. A FAIL
for BOTH surviving panel models CLOSES the relational-history line at Option C (no stamp-format
retune — anti-cheat carry-forward, 2026-06-16 ratification).
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


def analyze(raw_dir):
    stim = json.load(open(os.path.join(HERE, "stimuli.json")))
    by_rid = {r["rid"]: r for r in stim["records"]}
    floor = stim["pass_floor"]
    pos_chance = stim["pos_chance"]
    out = {"pass_floor": floor, "pos_chance": pos_chance, "models": {}}
    print(f"\n=== Option-B stamp-comprehension verdict (floor={floor}, "
          f"pos_chance={pos_chance}) ===")
    for name in C.MODELS:
        recs = C.read_jsonl(os.path.join(raw_dir, f"probe-{name}.jsonl"))
        parsed = [r for r in recs if r.get("pick") is not None]
        na = [r for r in recs if r.get("pick") is None]
        n = len(parsed)
        correct = sum(1 for r in parsed if r["pick"] == by_rid[r["rid"]]["correct_nonce"])
        lastp = sum(1 for r in parsed if r["pick"] == by_rid[r["rid"]]["last_pos_nonce"])
        firstp = sum(1 for r in parsed if r["pick"] == by_rid[r["rid"]]["first_pos_nonce"])
        acc = correct / n if n else 0.0
        lo, hi = wilson(correct, n)
        # per-query breakdown
        q = {}
        for query in C.QUERIES:
            qr = [r for r in parsed if by_rid[r["rid"]]["query"] == query]
            qc = sum(1 for r in qr if r["pick"] == by_rid[r["rid"]]["correct_nonce"])
            q[query] = {"n": len(qr), "acc": (qc / len(qr) if qr else 0.0)}
        verdict = "PASS" if (acc >= floor and lo > pos_chance) else "FAIL"
        m = {"n_total": len(recs), "n_parsed": n, "n_na": len(na),
             "accuracy": round(acc, 4), "wilson95": [round(lo, 4), round(hi, 4)],
             "pos_last_rate": round(lastp / n, 4) if n else 0.0,
             "pos_first_rate": round(firstp / n, 4) if n else 0.0,
             "by_query": q, "verdict": verdict}
        out["models"][name] = m
        print(f"\n  {name}: acc={acc:.3f}  95%CI=[{lo:.3f},{hi:.3f}]  "
              f"(n={n}, NA={len(na)})  -> {verdict}")
        print(f"     by query: MR acc={q['MR']['acc']:.3f} (n={q['MR']['n']}), "
              f"LR acc={q['LR']['acc']:.3f} (n={q['LR']['n']})")
        print(f"     position-follower diagnostic: pick==last-line {lastp / n:.3f}, "
              f"pick==first-line {firstp / n:.3f}" if n else "     (no parsed)")
    both_fail = all(m["verdict"] == "FAIL" for m in out["models"].values())
    out["both_fail_close_at_C"] = both_fail
    print(f"\n  => both models FAIL (close line at Option C)? {both_fail}")
    passers = [k for k, m in out["models"].items() if m["verdict"] == "PASS"]
    print(f"  => models earning an Option-A arm: {passers or 'none'}")
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
