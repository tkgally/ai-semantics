#!/usr/bin/env python3
"""build_trials.py (no API) -- the frozen EASIER (K=4) WITNESS ORDER-SENSITIVE COMPOSITION stimuli.

Two balanced rosters over a 4-figure track (the same STEP/FLIP non-commuting pair as the K=6 Option-C
run, only smaller). STEP (p->(p+1)%4) and FLIP (p->3-p) are the dihedral generators of a 4-ring; they
DO NOT COMMUTE, so applying them in stamp order (lower round first) lands "DAX" on a DIFFERENT figure
than applying them reversed.

At K=4 there are EXACTLY 4 valid base configs -- (start_pos, true stamp order in {SF=STEP-then-FLIP,
FS=FLIP-then-STEP}) -- and they fall, one each, on the 4 target track positions with the order
balanced 2 SF / 2 FS. (A config is "valid" iff the stamp-order target differs from the start, both
single-move ends, and the reversed-order/swapped end, so those readers score 0.) A "block" fixes one
config; its K=4 records cycle the TARGET figure (the stamp-order end figure) through all 4 shapes
once. The 16 COMP blocks = the 4 valid configs x 4 reps (target position uniform over the 4
positions, order balanced 8 SF / 8 FS); the 8 DIRECT blocks = the 4 configs x 2 reps. Within each
block, 2 records print the two move-lines in stamp order and 2 reversed (print order decoupled from
stamp order). All 4 shapes are present in every record (answer space = the 4 shapes).

Shortcut bounds asserted EMPIRICALLY before freeze, SEPARATELY per subset:
  - every constant-figure / figure-preference picker scores exactly 1/K = 1/4 (target uniform over
    the 4 shapes; all 4 present every record);
  - every fixed track-position picker scores <= 1/K (COMP: exactly 1/4, target position uniform);
  - the PRINT-ORDER reader (apply the moves in printed order) and BOTH canonical fixed-order readers
    (always STEP-then-FLIP; always FLIP-then-STEP) score EXACTLY 0.50 (print order matched to stamp
    order in half the records; true order balanced 50/50);
  - the START reader, each SINGLE-MOVE reader (STEP-only / FLIP-only from start) and the REVERSED-
    order ("swapped") reader score exactly 0 on the target (excluded by valid-config construction);
  - frequency flat (4 distinct figures once each).
So no figure / track-position / print-order / canonical-order / start / single-move / reversed-order
shortcut can clear the 0.50 bar; ONLY ordering the two moves by their stamps (stamp-order = order-
sensitive COMPOSITION) scores above it (a genuine stamp-order reader scores 1.0). Prints the sha256
that must go into PREREG.md.
"""
import hashlib
import json
import os
import random
from collections import Counter

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stimuli.json")


def valid_config(start, order):
    """target (stamp-order end) must differ from start, both single-move ends, and the swapped
    (reversed-order) end -- so start / single-move / swapped readers score 0 on the target."""
    t = C.apply_order(start, order)
    step1 = C.op_step(start)
    flip1 = C.op_flip(start)
    sw = C.swapped_pos(start, order)
    return t not in (start, step1, flip1) and t != sw


# The 4 valid base configs at K=4: one per target track position, order balanced 2 SF / 2 FS.
#   (0,"SF") -> target pos 2 ; (2,"SF") -> target pos 0   [the two SF configs]
#   (1,"FS") -> target pos 3 ; (3,"FS") -> target pos 1   [the two FS configs]
# (asserted valid + balanced by assert_balance below, exactly as enumerated at design time.)
VALID_CONFIGS = [(0, "SF"), (2, "SF"), (1, "FS"), (3, "FS")]

# COMP: the 4 valid configs x 4 reps = 16 blocks (target position uniform over 0..3, order balanced
# 8 SF / 8 FS). DIRECT: the 4 configs x 2 reps = 8 blocks (on-demand composition gate).
COMP_CONFIGS = VALID_CONFIGS * 4
DIRECT_CONFIGS = VALID_CONFIGS * 2


def _build_block(cfg, query, bi, rid_start, place_rng):
    start, order = cfg
    assert valid_config(start, order), f"invalid config {cfg}"
    op_lo, op_hi = C.ORDER_OPS[order]
    target_idx = C.apply_order(start, order)
    swapped_idx = C.swapped_pos(start, order)
    step1_idx, flip1_idx = C.op_step(start), C.op_flip(start)
    # display-order split: exactly K//2 "stamp" + K//2 "rev" per block, shuffled across the figure
    # cycle so display-order is decorrelated from which shape is the target.
    disp_orders = ["stamp"] * (C.K // 2) + ["rev"] * (C.K - C.K // 2)
    place_rng.shuffle(disp_orders)
    records, rid = [], rid_start
    for j in range(C.K):
        target_shape = C.SHAPES[j]                       # cycles all 4 shapes once across the block
        others = [s for s in C.SHAPES if s != target_shape]
        place_rng.shuffle(others)
        track = [None] * C.K
        track[target_idx] = target_shape
        slot = 0
        for s in others:
            while track[slot] is not None:
                slot += 1
            track[slot] = s
        pair = C.ROUND_PAIRS[rid % len(C.ROUND_PAIRS)]
        r_lo, r_hi = pair[0], pair[1]
        line_lo = {"round": r_lo, "op": op_lo}
        line_hi = {"round": r_hi, "op": op_hi}
        display_order = disp_orders[j]
        hist_display = [line_lo, line_hi] if display_order == "stamp" else [line_hi, line_lo]
        records.append({
            "rid": rid, "subset": query.lower(), "block": f"{query[:4]}{bi}", "query": query,
            "present": list(C.SHAPES),
            "track": track,
            "start_idx": start, "start_shape": track[start],
            "order": order, "op_lo": op_lo, "op_hi": op_hi, "r_lo": r_lo, "r_hi": r_hi,
            "display_order": display_order, "hist_display": hist_display,
            "target_idx": target_idx, "target_shape": target_shape,
            "swapped_idx": swapped_idx, "swapped_shape": track[swapped_idx],
            "step1_shape": track[step1_idx], "flip1_shape": track[flip1_idx],
        })
        rid += 1
    return records


def build_subset(configs, query, rid_start):
    place_rng = random.Random(C.SEED0 + (0 if query == "COMP" else 50))
    records, rid = [], rid_start
    for bi, cfg in enumerate(configs):
        block = _build_block(cfg, query, bi, rid, place_rng)
        records += block
        rid += len(block)
    return records


def build():
    comp = build_subset(COMP_CONFIGS, "COMP", 0)
    direct = build_subset(DIRECT_CONFIGS, "DIRECT", len(comp))
    return comp + direct


# ---- idealized-reader scorers (analytic certification) -----------------------------------
def _const_fig_acc(records, shape):
    """'always pick figure `shape`' -- all 4 shapes present every record, so this is just
    P(target == shape)."""
    return sum(1 for r in records if r["target_shape"] == shape) / len(records)


def _track_pos_acc(records, pos):
    """'always pick the figure at track position `pos`' -- P(track[pos] == target)."""
    return sum(1 for r in records if r["track"][pos] == r["target_shape"]) / len(records)


def _print_order_acc(records):
    """apply the two moves in PRINTED order -> target when display=='stamp', swapped otherwise."""
    n = 0
    for r in records:
        pick = r["target_shape"] if r["display_order"] == "stamp" else r["swapped_shape"]
        n += 1 if pick == r["target_shape"] else 0
    return n / len(records)


def _canonical_acc(records, canon):
    """always apply `canon` order (SF or FS) regardless of stamps. final position = apply_order on
    the canon order; that figure is the pick."""
    n = 0
    for r in records:
        idx = C.apply_order(r["start_idx"], canon)
        pick = r["track"][idx]
        n += 1 if pick == r["target_shape"] else 0
    return n / len(records)


def _reader_acc(records, key):
    """fixed-strategy reader keyed by a record field giving a shape (start/single-move/swapped)."""
    return sum(1 for r in records if r[key] == r["target_shape"]) / len(records)


def assert_balance(records):
    for subset in ("comp", "direct"):
        rs = [r for r in records if r["subset"] == subset]
        n = len(rs)
        assert n > 0, f"{subset}: empty"
        # 0) every record has all 4 distinct shapes; latest move-round > earlier; valid config
        for r in rs:
            assert sorted(r["track"]) == sorted(C.SHAPES), f"{subset} rid {r['rid']}: track not perm"
            assert r["r_hi"] > r["r_lo"], f"{subset} rid {r['rid']}: stamps not ordered"
            assert valid_config(r["start_idx"], r["order"]), f"{subset} rid {r['rid']}: invalid cfg"
            assert r["target_shape"] == r["track"][r["target_idx"]]
        # 1) target figure UNIFORM over the 4 shapes => const-figure / figure-pref picker = 1/K
        figc = Counter(r["target_shape"] for r in rs)
        assert set(figc) == set(C.SHAPES) and len(set(figc.values())) == 1, \
            f"{subset}: target figure not uniform: {dict(figc)}"
        for s in C.SHAPES:
            a = _const_fig_acc(rs, s)
            assert abs(a - C.POS_CHANCE) < 1e-9, f"{subset} const-fig {s} acc {a} != 1/K"
        # 2) target TRACK POSITION balanced => fixed track-position picker <= 1/K
        posc = Counter(r["target_idx"] for r in rs)
        for j in range(C.K):
            a = _track_pos_acc(rs, j)
            assert a <= C.POS_CHANCE + 1e-9, f"{subset} track-pos {j} picker {a} > 1/K"
        if subset == "comp":
            assert set(posc) == set(range(C.K)) and len(set(posc.values())) == 1, \
                f"{subset}: target track position not uniform: {dict(posc)}"
        # 3) print-order & both canonical fixed-order readers = EXACTLY 0.50 (COMP only)
        if subset == "comp":
            po = _print_order_acc(rs)
            assert abs(po - C.PRINT_CEILING) < 1e-9, f"{subset} print-order acc {po} != 0.50"
            for canon in ("SF", "FS"):
                ca = _canonical_acc(rs, canon)
                assert abs(ca - C.PRINT_CEILING) < 1e-9, \
                    f"{subset} canonical-{canon} acc {ca} != 0.50"
            # true order balanced 50/50
            oc = Counter(r["order"] for r in rs)
            assert oc["SF"] == oc["FS"], f"{subset}: order not balanced {dict(oc)}"
            # display-order balanced 50/50
            dc = Counter(r["display_order"] for r in rs)
            assert dc["stamp"] == dc["rev"], f"{subset}: display order not balanced {dict(dc)}"
        # 4) start / single-move / swapped readers score 0 on the target
        for key in ("start_shape", "step1_shape", "flip1_shape", "swapped_shape"):
            a = _reader_acc(rs, key)
            assert a < 1e-9, f"{subset} reader {key} acc {a} != 0 (must never hit target)"
        print(f"  [{subset}] geometry OK: {n} records ({len(set(r['block'] for r in rs))} blocks "
              f"x {C.K}); const-fig={C.POS_CHANCE:.3f}; track-pos<=1/K; "
              + ("print/canonical=0.500; " if subset == "comp" else "")
              + "start/single-move/swapped=0.000; freq flat.")
    cp = [r for r in records if r["subset"] == "comp"]
    di = [r for r in records if r["subset"] == "direct"]
    print(f"  totals: {len(cp)} COMP + {len(di)} DIRECT = {len(records)} records/model; "
          f"{len(records) * len(C.MODELS)} finding-bearing calls. Only ordering the two moves by "
          f"their STAMPS clears the {C.PRINT_CEILING} bar (order-sensitive composition).")


def main():
    records = build()
    assert_balance(records)
    blob = json.dumps({"records": records, "k": C.K, "term": C.TERM, "shapes": C.SHAPES,
                       "n_blocks_comp": C.N_BLOCKS_COMP, "n_blocks_direct": C.N_BLOCKS_DIRECT,
                       "print_ceiling": C.PRINT_CEILING, "direct_floor": C.DIRECT_FLOOR,
                       "pos_chance": C.POS_CHANCE, "seed0": C.SEED0},
                      indent=2, sort_keys=True)
    open(OUT, "w").write(blob + "\n")
    sha = hashlib.sha256(blob.encode()).hexdigest()
    print(f"  wrote {OUT}")
    print(f"  stimuli.json sha256 = {sha}")
    print("  -> put this sha256 in PREREG.md before any finding-bearing call")


if __name__ == "__main__":
    main()
