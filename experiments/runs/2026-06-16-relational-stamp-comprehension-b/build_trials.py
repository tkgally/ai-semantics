#!/usr/bin/env python3
"""build_trials.py (no API) — the frozen Option-B stamp-comprehension stimuli.

Balanced-block construction (2026-06-16, fixes pre-run critic blocker 2 — the residual
nonce-identity cue). 12 distinct present-sets (4-nonce subsets of the 8-nonce pool, each nonce
in exactly 6 sets); each set yields K=4 records. Within a set's 4 records, a Latin square makes
the CORRECT nonce cycle through all 4 members exactly once AND the correct line's physical
position cycle through all 4 slots exactly once. Round values come from frozen non-contiguous
quadruples, with the correct member given the max round (MR) or min round (LR); the others get
the remaining rounds in shuffled order — so round value and nonce identity are independent of
physical position.

Two shortcut bounds are asserted EMPIRICALLY before freeze:
- every constant-physical-slot strategy (position-follower) scores exactly 1/K;
- every one of the 8! fixed nonce-preference orderings scores exactly 1/K.
So ONLY reading the stamp value as recency can clear the PASS_FLOOR (0.80). Prints the sha256
that must go into PREREG.md.
"""
import hashlib
import itertools
import json
import os
import random

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stimuli.json")


def balanced_blocks(rng):
    """12 distinct 4-subsets of the 8 nonces, each nonce in exactly 6 blocks. Rejection-sample
    with the frozen seed until membership is exactly balanced (fast)."""
    from collections import Counter
    pool = C.NONCES
    target_per = C.N_BLOCKS * C.K // len(pool)  # 12*4/8 = 6
    for _ in range(200000):
        blocks, seen, cnt = [], set(), Counter()
        ok = True
        cand = list(itertools.combinations(pool, C.K))
        rng.shuffle(cand)
        for b in cand:
            if len(blocks) == C.N_BLOCKS:
                break
            if any(cnt[x] >= target_per for x in b):
                continue
            blocks.append(list(b))
            cnt.update(b)
        if len(blocks) == C.N_BLOCKS and all(cnt[x] == target_per for x in pool):
            return blocks
        rng.seed(rng.random())  # reshuffle and retry
    raise RuntimeError("could not build balanced blocks")


def build():
    rng = random.Random(C.SEED0)
    blocks = balanced_blocks(rng)
    records = []
    rid = 0
    for bi, block in enumerate(blocks):
        # Latin square over (correct-member-index, target-position): record j uses
        # correct member = block[j], target_pos = (j + bi) % K  -> each cycles 0..K-1 once.
        # Queries: 2 MR + 2 LR per block (j<2 -> MR, else LR), so 24 MR + 24 LR globally.
        for j in range(C.K):
            correct_nonce = block[j]
            target_pos = (j + bi) % C.K
            query = "MR" if j < C.K // 2 else "LR"
            rounds = list(C.ROUND_SETS[rid % len(C.ROUND_SETS)])  # sorted ascending
            others = [n for n in block if n != correct_nonce]
            rng.shuffle(others)
            # correct member gets the extreme round; others get the rest (shuffled).
            if query == "MR":
                extreme, rest = rounds[-1], rounds[:-1]
            else:
                extreme, rest = rounds[0], rounds[1:]
            rng.shuffle(rest)
            nonce_round = {correct_nonce: extreme}
            for n, r in zip(others, rest):
                nonce_round[n] = r
            # place correct line at target_pos; others fill remaining slots in shuffled order
            display = [None] * C.K
            display[target_pos] = {"round": nonce_round[correct_nonce], "nonce": correct_nonce}
            slot = 0
            for n in others:
                while display[slot] is not None:
                    slot += 1
                display[slot] = {"round": nonce_round[n], "nonce": n}
            records.append({
                "rid": rid,
                "block": bi,
                "query": query,
                "lines_display": display,
                "correct_nonce": correct_nonce,
                "correct_round": nonce_round[correct_nonce],
                "target_pos": target_pos,
                "last_pos_nonce": display[-1]["nonce"],
                "first_pos_nonce": display[0]["nonce"],
                "present": sorted(block),
            })
            rid += 1
    return records


def assert_balance(records):
    from collections import Counter
    n = len(records)
    # 1) target physical position EXACTLY uniform within each query (kills position shortcuts)
    for query in C.QUERIES:
        rs = [r for r in records if r["query"] == query]
        pos = Counter(r["target_pos"] for r in rs)
        assert set(pos) == set(range(C.K)) and len(set(pos.values())) == 1, \
            f"{query}: target_pos not balanced: {dict(pos)}"
    # 2) every constant-physical-slot strategy scores exactly 1/K
    for slot in range(C.K):
        acc = sum(1 for r in records
                  if r["lines_display"][slot]["nonce"] == r["correct_nonce"]) / n
        assert abs(acc - C.POS_CHANCE) < 1e-9, f"slot-{slot} follower acc {acc} != 1/K"
    # 3) within each present-set the correct nonce is UNIFORM over its members
    #    => every fixed nonce-preference ordering scores exactly 1/K. Assert structurally
    #    (each member correct once per block) AND verify the worst ordering empirically.
    by_block = {}
    for r in records:
        by_block.setdefault(r["block"], []).append(r)
    for bi, rs in by_block.items():
        assert len(rs) == C.K, f"block {bi}: {len(rs)} records (expected {C.K})"
        corrects = Counter(r["correct_nonce"] for r in rs)
        assert set(corrects.values()) == {1}, f"block {bi}: correct nonce not uniform: {dict(corrects)}"
    worst = 0.0
    for order in itertools.permutations(C.NONCES):
        rank = {nm: i for i, nm in enumerate(order)}
        c = sum(1 for r in records
                if min(r["present"], key=lambda x: rank[x]) == r["correct_nonce"])
        worst = max(worst, c / n)
    assert abs(worst - C.POS_CHANCE) < 1e-9, \
        f"best nonce-preference ordering scores {worst:.4f} != 1/K (residual lexical cue!)"
    # 4) sanity: K distinct nonces & rounds per record; correct in present
    for r in records:
        ns = [ln["nonce"] for ln in r["lines_display"]]
        rd = [ln["round"] for ln in r["lines_display"]]
        assert len(set(ns)) == C.K and len(set(rd)) == C.K
        assert r["correct_nonce"] in r["present"]
    # 5) query balance
    qc = Counter(r["query"] for r in records)
    assert qc["MR"] == qc["LR"] == n // 2, f"query imbalance: {dict(qc)}"
    print(f"  geometry OK: {n} records ({n // 2}/query; {len(by_block)} blocks x {C.K}); "
          f"position-follower acc = 1/K exactly; best nonce-preference ordering acc = "
          f"{worst:.3f} (= 1/K). Only stamp-reading clears {C.PASS_FLOOR}.")


def main():
    records = build()
    assert_balance(records)
    blob = json.dumps({"records": records, "k": C.K, "queries": C.QUERIES,
                       "n_blocks": C.N_BLOCKS, "pass_floor": C.PASS_FLOOR,
                       "pos_chance": C.POS_CHANCE, "seed0": C.SEED0},
                      indent=2, sort_keys=True)
    open(OUT, "w").write(blob + "\n")
    sha = hashlib.sha256(blob.encode()).hexdigest()
    print(f"  wrote {OUT}")
    print(f"  stimuli.json sha256 = {sha}")
    print("  -> put this sha256 in PREREG.md before any finding-bearing call")


if __name__ == "__main__":
    main()
