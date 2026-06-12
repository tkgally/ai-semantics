#!/usr/bin/env python3
"""build_stimuli.py — freeze the history-perturbation stimuli (v2) before any model call.

Constructs per-model MIXED convention records for each confusable near-twin pair (X, Y):
the record's CONTENT MULTISET is held fixed (2 distinct descriptions of X + 2 of Y, drawn
from that model's OWN v1 live-game descriptions, uniform positive feedback) and only the
ORDER varies over all 6 distinct arrangements of {X,X,Y,Y}. A nonce nickname (frozen,
non-descriptive) plays the coined term. If the recovered convention is COMMUTATIVE
(conjecture/commutative-convention), the pick distribution is invariant across the 6 orders;
a path-dependent (recency / settled-repair) reading predicts the pick tracks the
chronologically-LAST twin.

PRE-RUN CRITIC REVISIONS (2026-06-12, before any finding-bearing call):
- B1: every mixed trial runs in TWO presentation directions — "fwd" (earliest first;
  chronologically-last line is physically last) and "rev" (most recent first; lines
  physically reversed, chronology identical). De-confounds chronology-tracking from a bare
  positional/adjacency attention artifact: genuine chronology-tracking follows the STATED
  chronology in both arms; an attention artifact follows the PHYSICALLY-last line in both.
- B2: CONSISTENT controls (manipulation check) now cover EVERY description sample, so every
  (pair x sample) cluster's descriptions are certified; analysis gates clusters on their own
  controls.

Descriptions are harvested from the committed v1 raw, per model per figure, DISTINCT strings
only, deterministic seed. Output: stimuli.json; sha256 recorded in PREREG.md; no
finding-bearing call before that hash is committed.
"""
import hashlib
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
V1 = os.path.abspath(os.path.join(HERE, "..", "2026-05-31-relational-reference-game-v1"))

SEED = 20260612
MODELS = ["claude", "gpt", "gemini"]
# All 6 distinct orders of the multiset {X,X,Y,Y}; 3 end in X, 3 end in Y (symmetric).
ORDERS = ["XXYY", "XYXY", "YXXY", "YYXX", "YXYX", "XYYX"]
DIRECTIONS = ["fwd", "rev"]  # B1: presentation-direction control arm
# Frozen non-descriptive nonce nicknames, one per twin pair.
NONCE = {0: "ZIMVOR", 1: "QUEXTAL", 2: "DRUBNIK"}


def main():
    figs = json.load(open(os.path.join(V1, "figures.json")))["figures"]
    raw = json.load(open(os.path.join(V1, "raw", "results.json")))
    pairs = {}
    for fid, f in figs.items():
        pairs.setdefault(f["pair"], []).append(fid)
    for p in pairs.values():
        p.sort()

    # distinct live-game descriptions per (model, figure), insertion-ordered (deterministic);
    # also record per-description live success stats (stimulus-quality disclosure, critic B2).
    pool, live_ok, live_n = {}, {}, {}
    for r in raw:
        if r["phase"] == "live" and r.get("desc"):
            k = (r["model"], r["target"])
            pool.setdefault(k, [])
            if r["desc"] not in pool[k]:
                pool[k].append(r["desc"])
            dk = (r["model"], r["target"], r["desc"])
            live_n[dk] = live_n.get(dk, 0) + 1
            live_ok[dk] = live_ok.get(dk, 0) + (1 if r["correct"] else 0)

    rng = random.Random(SEED)
    trials = {m: [] for m in MODELS}
    census = []
    for m in MODELS:
        for pid, (a, b) in sorted(pairs.items()):
            pa, pb = pool[(m, a)], pool[(m, b)]
            n_samples = 2 if (len(pa) >= 4 and len(pb) >= 4) else 1
            sa = rng.sample(pa, 2 * n_samples)
            sb = rng.sample(pb, 2 * n_samples)
            for fid, dd in ((a, sa), (b, sb)):
                for d in dd:
                    k = (m, fid, d)
                    census.append({"model": m, "fig": fid, "desc": d,
                                   "live_correct": live_ok.get(k, 0),
                                   "live_n": live_n.get(k, 0)})
            for s in range(n_samples):
                dx = sa[2 * s:2 * s + 2]
                dy = sb[2 * s:2 * s + 2]
                for order in ORDERS:
                    ix, iy = 0, 0
                    lines = []
                    for ch in order:
                        if ch == "X":
                            lines.append(dx[ix]); ix += 1
                        else:
                            lines.append(dy[iy]); iy += 1
                    for direction in DIRECTIONS:
                        trials[m].append({
                            "kind": "mixed", "pair": pid, "X": a, "Y": b,
                            "order": order, "direction": direction, "sample": s,
                            "nonce": NONCE[pid], "lines": lines,
                            "last": a if order[-1] == "X" else b,        # chron-last twin
                            "first": a if order[0] == "X" else b,        # chron-first twin
                        })
                # consistent controls (manipulation check) for EVERY sample (critic B2):
                # all 4 lines describe one twin (repeat the sample's 2 descriptions).
                for fid, dd in ((a, dx), (b, dy)):
                    trials[m].append({
                        "kind": "consistent", "pair": pid, "X": a, "Y": b,
                        "order": None, "direction": "fwd", "sample": s,
                        "nonce": NONCE[pid], "target": fid,
                        "lines": [dd[0], dd[1], dd[0], dd[1]],
                    })

    out = {"seed": SEED, "orders": ORDERS, "directions": DIRECTIONS, "nonce": NONCE,
           "figures": figs, "pairs": pairs, "trials": trials,
           "live_quality_census": census}
    path = os.path.join(HERE, "stimuli.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    h = hashlib.sha256(open(path, "rb").read()).hexdigest()
    n = {m: len(trials[m]) for m in MODELS}
    bad = sum(1 for c in census if c["live_n"] and c["live_correct"] < c["live_n"])
    print(f"stimuli.json written: {n} trials/model "
          f"(census: {bad}/{len(census)} used descriptions failed live at least once), "
          f"sha256={h}")


if __name__ == "__main__":
    main()
