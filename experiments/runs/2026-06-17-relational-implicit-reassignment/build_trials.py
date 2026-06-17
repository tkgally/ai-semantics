#!/usr/bin/env python3
"""build_trials.py (no API) — the frozen Option-A spontaneous-recency stimuli.

Two independent balanced-block rosters over the 8-FIGURE pool (the Option-B construction,
generalized from nonces to figures):

  SPONT  : N_BLOCKS_SPONT present-sets x K records (Latin square) -> 48 records/model.
           query = "SPONT" (no recency mention); the GOVERNING figure (latest-governs) is the
           one agreed at the MAX round. The min-round figure is recorded as the anti-recency
           diagnostic. This is the headline.
  DIRECT : N_BLOCKS_DIRECT present-sets x K records -> 32 records/model. Half DIR_MR (correct =
           max round), half DIR_LR (correct = min round) -- the B-style on-demand manipulation
           check, in THIS instrument.

Within each subset and each present-set, a Latin square makes the GOVERNING figure cycle through
all K members once AND the governing line's physical history-slot cycle through all K slots once.
Round values come from frozen non-contiguous quadruples; the governing figure gets the extreme
(max for SPONT/DIR_MR, min for DIR_LR), the others get the rest in shuffled order -- so round
value and figure identity are independent of physical history-position, and each figure appears
exactly once per record (frequency flat).

Shortcut bounds asserted EMPIRICALLY before freeze, SEPARATELY per subset:
  - every constant-physical-history-slot strategy scores exactly 1/K;
  - every one of the |pool|! fixed figure-preference orderings scores exactly 1/K
    (incl. the grid-order ordering, so a 'grid-position' strategy is covered);
  - each figure appears exactly once per record (frequency carries no signal).
So ONLY spontaneously reading the round stamp as recency can clear the SPONT order-sensitivity
bar or the DIRECT floor. Prints the sha256 that must go into PREREG.md.
"""
import hashlib
import itertools
import json
import os
import random
from collections import Counter

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stimuli.json")


def balanced_blocks(rng, n_blocks):
    """n_blocks distinct K-subsets of the pool, each figure in exactly n_blocks*K/|pool| blocks."""
    pool = C.LABELS
    if (n_blocks * C.K) % len(pool) != 0:
        raise ValueError("n_blocks*K must be divisible by pool size for exact balance")
    target_per = n_blocks * C.K // len(pool)
    for _ in range(200000):
        blocks, cnt = [], Counter()
        cand = list(itertools.combinations(pool, C.K))
        rng.shuffle(cand)
        for b in cand:
            if len(blocks) == n_blocks:
                break
            if any(cnt[x] >= target_per for x in b):
                continue
            blocks.append(list(b))
            cnt.update(b)
        if len(blocks) == n_blocks and all(cnt[x] == target_per for x in pool):
            return blocks
        rng.seed(rng.random())
    raise RuntimeError("could not build balanced blocks")


def build_subset(rng, n_blocks, query_of, rid_start):
    """query_of(j) -> one of SPONT / DIR_MR / DIR_LR for record j within a block. Governing figure
    = max-round for SPONT and DIR_MR, min-round for DIR_LR (the correct/scored figure)."""
    blocks = balanced_blocks(rng, n_blocks)
    records, rid = [], rid_start
    for bi, block in enumerate(blocks):
        for j in range(C.K):
            governing = block[j]                     # cycles all K members across the block
            target_pos = (j + bi) % C.K              # cycles all K physical slots across the block
            query = query_of(j)
            rounds = list(C.ROUND_SETS[rid % len(C.ROUND_SETS)])  # sorted ascending
            others = [x for x in block if x != governing]
            rng.shuffle(others)
            if query == "DIR_LR":
                extreme, rest = rounds[0], rounds[1:]     # governing = earliest
            else:
                extreme, rest = rounds[-1], rounds[:-1]    # governing = latest
            rng.shuffle(rest)
            fig_round = {governing: extreme}
            for x, r in zip(others, rest):
                fig_round[x] = r
            display = [None] * C.K
            display[target_pos] = {"round": fig_round[governing], "label": governing}
            slot = 0
            for x in others:
                while display[slot] is not None:
                    slot += 1
                display[slot] = {"round": fig_round[x], "label": x}
            # round -> figure map for diagnostics
            max_round_label = max(display, key=lambda d: d["round"])["label"]
            min_round_label = min(display, key=lambda d: d["round"])["label"]
            correct = governing  # by construction = max_round_label (SPONT/DIR_MR) or min (DIR_LR)
            records.append({
                "rid": rid,
                "subset": "spont" if query == "SPONT" else "direct",
                "block": f"{query[:3]}{bi}",
                "query": query,
                "present": sorted(block),
                "lines_display": display,
                "correct_label": correct,
                "max_round_label": max_round_label,
                "min_round_label": min_round_label,
                "target_pos": target_pos,
                "last_pos_label": display[-1]["label"],
                "first_pos_label": display[0]["label"],
            })
            rid += 1
    return records


def build():
    rng = random.Random(C.SEED0)
    spont = build_subset(rng, C.N_BLOCKS_SPONT, lambda j: "SPONT", 0)
    direct = build_subset(rng, C.N_BLOCKS_DIRECT,
                          lambda j: "DIR_MR" if j < C.K // 2 else "DIR_LR", len(spont))
    return spont + direct


def _slot_acc(records, slot):
    return sum(1 for r in records
               if r["lines_display"][slot]["label"] == r["correct_label"]) / len(records)


def _worst_pref_acc(records):
    """worst (best-for-attacker) fixed figure-preference ordering accuracy over `records`."""
    worst = 0.0
    for order in itertools.permutations(C.LABELS):
        rank = {nm: i for i, nm in enumerate(order)}
        c = sum(1 for r in records
                if min(r["present"], key=lambda x: rank[x]) == r["correct_label"])
        worst = max(worst, c / len(records))
    return worst


def assert_balance(records):
    for subset in ("spont", "direct"):
        rs = [r for r in records if r["subset"] == subset]
        n = len(rs)
        assert n > 0, f"{subset}: empty"
        # 1) governing physical slot uniform within each query => position-follower = 1/K
        for query in {r["query"] for r in rs}:
            qr = [r for r in rs if r["query"] == query]
            pos = Counter(r["target_pos"] for r in qr)
            assert set(pos) == set(range(C.K)) and len(set(pos.values())) == 1, \
                f"{subset}/{query}: target_pos not balanced: {dict(pos)}"
        # 2) every constant-physical-slot strategy scores exactly 1/K
        for slot in range(C.K):
            acc = _slot_acc(rs, slot)
            assert abs(acc - C.POS_CHANCE) < 1e-9, f"{subset} slot-{slot} follower acc {acc} != 1/K"
        # 3) within each present-set the correct figure is UNIFORM over members =>
        #    every fixed figure-preference ordering scores exactly 1/K
        by_block = {}
        for r in rs:
            by_block.setdefault(r["block"], []).append(r)
        for bi, brs in by_block.items():
            assert len(brs) == C.K, f"{subset} block {bi}: {len(brs)} records (expected {C.K})"
            corrects = Counter(r["correct_label"] for r in brs)
            assert set(corrects.values()) == {1}, \
                f"{subset} block {bi}: correct figure not uniform: {dict(corrects)}"
        worst = _worst_pref_acc(rs)
        assert abs(worst - C.POS_CHANCE) < 1e-9, \
            f"{subset}: best figure-preference ordering scores {worst:.4f} != 1/K (lexical leak!)"
        # 4) frequency flat: each figure appears exactly once per record; K distinct figs & rounds
        for r in rs:
            labs = [ln["label"] for ln in r["lines_display"]]
            rds = [ln["round"] for ln in r["lines_display"]]
            assert len(set(labs)) == C.K and len(set(rds)) == C.K
            assert sorted(labs) == r["present"]
            assert r["correct_label"] in r["present"]
        print(f"  [{subset}] geometry OK: {n} records ({len(by_block)} blocks x {C.K}); "
              f"position-follower acc = 1/K exactly; best figure-preference ordering acc = "
              f"{worst:.3f} (= 1/K); frequency flat.")
    # 5) SPONT correct == max-round (latest-governs); DIR_LR correct == min-round
    for r in records:
        if r["query"] in ("SPONT", "DIR_MR"):
            assert r["correct_label"] == r["max_round_label"]
        else:
            assert r["correct_label"] == r["min_round_label"]
    sp = [r for r in records if r["subset"] == "spont"]
    di = [r for r in records if r["subset"] == "direct"]
    print(f"  totals: {len(sp)} SPONT + {len(di)} DIRECT = {len(records)} records/model; "
          f"{len(records) * len(C.MODELS)} finding-bearing calls. Only stamp-reading clears "
          f"the SPONT order-sensitivity bar / the DIRECT floor ({C.DIRECT_FLOOR}).")


def main():
    records = build()
    assert_balance(records)
    blob = json.dumps({"records": records, "k": C.K, "term": C.TERM,
                       "figures": C.FIGURES,
                       "n_blocks_spont": C.N_BLOCKS_SPONT, "n_blocks_direct": C.N_BLOCKS_DIRECT,
                       "direct_floor": C.DIRECT_FLOOR, "pos_chance": C.POS_CHANCE,
                       "seed0": C.SEED0},
                      indent=2, sort_keys=True)
    open(OUT, "w").write(blob + "\n")
    sha = hashlib.sha256(blob.encode()).hexdigest()
    print(f"  wrote {OUT}")
    print(f"  stimuli.json sha256 = {sha}")
    print("  -> put this sha256 in PREREG.md before any finding-bearing call")


if __name__ == "__main__":
    main()
