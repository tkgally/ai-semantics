#!/usr/bin/env python3
"""analyze.py -- per-arm, per-model forced-choice shift analysis.

For each item and model, derive picked_hedge in {0,1} per condition from the chosen letter
and the item's hedge_letter. Then:
  shift_fn = picked_hedge(fn) - picked_hedge(base)   in {-1,0,1}
  shift_ct = picked_hedge(ct) - picked_hedge(base)   in {-1,0,1}
Per arm x model report: mean(shift_fn) [PRIMARY], mean(shift_ct) [control],
base strong-pref rate = mean(1 - picked_hedge(base)) [manip check], with bootstrap 95% CIs.
"""
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
ARMS = ("will", "shall", "must")
MODELS = ("claude", "gpt", "gemini")


def load(model):
    rows = json.load(open(os.path.join(RAW, f"{model}-fc.json")))
    by = {}
    for r in rows:
        by.setdefault((r["id"], r["ftype"], r["hedge_letter"]), {})[r["cond"]] = r["value"]
    return by


def picked_hedge(letter, hedge_letter):
    if letter is None:
        return None
    return 1 if letter == hedge_letter else 0


def boot(vals, f, n=10000, seed=0):
    vals = [v for v in vals if v is not None]
    if not vals:
        return (None, None, None)
    rng = random.Random(seed)
    stats = []
    for _ in range(n):
        s = [vals[rng.randrange(len(vals))] for _ in vals]
        stats.append(f(s))
    stats.sort()
    return (f(vals), stats[int(0.025 * n)], stats[int(0.975 * n)])


def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def main():
    out = {"arms": {}}
    print(f"{'arm':6} {'model':7} {'n':>3} {'base_strong':>11} {'shift_fn':>20} {'shift_ct':>20}")
    for arm in ARMS:
        out["arms"][arm] = {}
        for model in MODELS:
            by = load(model)
            keys = [k for k in by if k[1] == arm]
            shift_fn, shift_ct, base_strong = [], [], []
            for k in keys:
                hl = k[2]
                conds = by[k]
                ph_base = picked_hedge(conds.get("base"), hl)
                ph_fn = picked_hedge(conds.get("fn"), hl)
                ph_ct = picked_hedge(conds.get("ct"), hl)
                if ph_base is not None and ph_fn is not None:
                    shift_fn.append(ph_fn - ph_base)
                if ph_base is not None and ph_ct is not None:
                    shift_ct.append(ph_ct - ph_base)
                if ph_base is not None:
                    base_strong.append(1 - ph_base)
            m_fn, lo_fn, hi_fn = boot(shift_fn, mean, seed=1)
            m_ct, lo_ct, hi_ct = boot(shift_ct, mean, seed=2)
            bs = mean(base_strong)
            out["arms"][arm][model] = {
                "n_items": len(keys),
                "base_strong_pref": bs,
                "shift_fn_mean": m_fn, "shift_fn_ci": [lo_fn, hi_fn],
                "shift_ct_mean": m_ct, "shift_ct_ci": [lo_ct, hi_ct],
                "n_unparsed": sum(1 for k in keys for c in ("base", "fn", "ct")
                                  if by[k].get(c) is None),
            }
            print(f"{arm:6} {model:7} {len(keys):>3} {bs:>11.3f} "
                  f"{m_fn:>+7.3f}[{lo_fn:+.2f},{hi_fn:+.2f}] "
                  f"{m_ct:>+7.3f}[{lo_ct:+.2f},{hi_ct:+.2f}]")
    json.dump(out, open(os.path.join(HERE, "analysis.json"), "w"), indent=1)
    print("\nwrote analysis.json")


if __name__ == "__main__":
    main()
