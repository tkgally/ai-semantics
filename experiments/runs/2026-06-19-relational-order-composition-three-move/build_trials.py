#!/usr/bin/env python3
"""build_trials.py (no API) -- the frozen THREE-MOVE (deeper-composition) ORDER-SENSITIVE COMPOSITION
stimuli (three generic non-commuting permutations of six figures, stamp order = composition).

Three pairwise non-commuting derangements of the six positions (C.PERMS: FLIP, SLIDE, TWIST). For each
of the 6 stamp-orderings there is EXACTLY ONE start (C.CONFIGS) at which the true-stamp-order endpoint
is hit by NO other sub-path -- not the start, not any of the 3 single-move ends, not any of the 6
ordered-pair ends, and not any of the 5 OTHER full orderings (strict isolation, re-proven below). The
six chosen configs fall, one each, on the 6 target track positions, with the stamp-order balanced one
per ordering. A "block" fixes one config; its 6 records cycle the TARGET figure through all 6 shapes
once (target figure uniform) and cycle all 6 DISPLAY permutations of the three move-lines once (display
order decoupled from stamp order). COMP = 6 configs x 2 reps = 12 blocks (72 records); DIRECT = 6
configs x 1 rep = 6 blocks (36 records).

WHY THE 0.50 CEILING CARRIES OVER FROM THE TWO-MOVE INSTRUMENT. With three moves there are 3!=6
orderings. A reader that fails to order ALL THREE moves by their stamps can pin at most ONE move's slot
from the stamps and must fill the remaining two-move sub-order from the print/display order (which is
decoupled from stamps). It then produces the true ordering only when that remaining two-move sub-order
happens to match -- exactly HALF the time. So every such "half-composer" scores EXACTLY 0.50; every
fixed canonical order and the print-order reader score 1/6; every start / single-move / ordered-pair /
reversed-order reader scores 0; every figure / position picker scores 1/K = 1/6. ONLY ordering all
three moves by their stamps clears 0.50 (a genuine stamp-order composer scores 1.0). All of this is
brute-forced over the actual records in assert_balance below -- not asserted by hand. Prints the
sha256 that must go into PREREG.md.
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

ALL_ORDERS = list(itertools.permutations(C.MOVE_NAMES))   # the 6 full orderings


def _all_paths():
    """the 16 sub-paths from a start: () + 3 singles + 6 ordered pairs + 6 full orderings."""
    paths = [()]
    for r in (1, 2, 3):
        paths += list(itertools.permutations(C.MOVE_NAMES, r))
    return paths


PATHS = _all_paths()


def strict_isolated(start, order):
    """True iff the true-stamp-order endpoint is hit by NO other sub-path (the freeze guarantee)."""
    target = C.apply_seq(start, order)
    if target == start:
        return False
    return all(C.apply_seq(start, p) != target for p in PATHS if p != tuple(order))


def _build_block(cfg, query, bi, rid_start, place_rng):
    start, stamp_moves = cfg
    stamp_moves = tuple(stamp_moves)
    assert strict_isolated(start, stamp_moves), f"config {cfg} not strict-isolated"
    target_idx = C.apply_seq(start, stamp_moves)
    rev_idx = C.apply_seq(start, C.reverse_seq(stamp_moves))
    single_idx = {nm: C.op(nm, start) for nm in C.MOVE_NAMES}
    # within the block: cycle target figure over all 6 shapes; cycle all 6 display perms once,
    # shuffled INDEPENDENTLY of the figure cycle so figure and display order are decorrelated.
    disp_perms = list(C.DISPLAY_PERMS)
    place_rng.shuffle(disp_perms)
    records, rid = [], rid_start
    for j in range(C.K):
        target_shape = C.SHAPES[j]                       # cycles all 6 shapes once across the block
        others = [s for s in C.SHAPES if s != target_shape]
        place_rng.shuffle(others)
        track = [None] * C.K
        track[target_idx] = target_shape
        slot = 0
        for s in others:
            while track[slot] is not None:
                slot += 1
            track[slot] = s
        rounds = C.ROUND_TRIPLES[rid % len(C.ROUND_TRIPLES)]
        # stamp slots: slot k = (round rounds[k], move stamp_moves[k]); displayed in disp_perm order.
        disp_perm = disp_perms[j]
        hist_display = [{"round": rounds[k], "op": stamp_moves[k]} for k in disp_perm]
        display_moves = [stamp_moves[k] for k in disp_perm]
        records.append({
            "rid": rid, "subset": query.lower(), "block": f"{query[:4]}{bi}", "query": query,
            "present": list(C.SHAPES),
            "track": track,
            "start_idx": start, "start_shape": track[start],
            "stamp_moves": list(stamp_moves), "rounds": list(rounds),
            "order_label": "".join(m[0] for m in stamp_moves),  # e.g. "FST"
            "disp_perm": list(disp_perm), "display_moves": display_moves,
            "hist_display": hist_display,
            "target_idx": target_idx, "target_shape": target_shape,
            "rev_idx": rev_idx, "rev_shape": track[rev_idx],
            "single_shapes": [track[single_idx[nm]] for nm in C.MOVE_NAMES],
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
    comp = build_subset(C.CONFIGS * 2, "COMP", 0)        # 6 configs x 2 reps
    direct = build_subset(C.CONFIGS * 1, "DIRECT", len(comp))
    return comp + direct


# ---- idealized-reader scorers (analytic certification) -----------------------------------
def _rate(records, pick_fn):
    return sum(1 for r in records if pick_fn(r) == r["target_shape"]) / len(records)


def _const_fig(records, shape):
    return sum(1 for r in records if r["target_shape"] == shape) / len(records)


def _track_pos(records, pos):
    return sum(1 for r in records if r["track"][pos] == r["target_shape"]) / len(records)


def _full_order_pick(r, order):
    """apply the three moves in fixed type-order `order` (a canonical reader)."""
    return r["track"][C.apply_seq(r["start_idx"], order)]


def _print_pick(r):
    """apply the three moves in DISPLAY (printed) order."""
    return r["track"][C.apply_seq(r["start_idx"], tuple(r["display_moves"]))]


def _rev_pick(r):
    return r["rev_shape"]


def _half_composer_pick(r, pin_slot):
    """pin the stamp-correct move into slot `pin_slot`; fill the OTHER two slots in DISPLAY order.
    Produces the true ordering only when the remaining two-move sub-order matches the stamps."""
    stamp = list(r["stamp_moves"])
    pinned = stamp[pin_slot]
    remaining_in_display = [m for m in r["display_moves"] if m != pinned]
    produced = [None, None, None]
    produced[pin_slot] = pinned
    fill = iter(remaining_in_display)
    for k in range(3):
        if produced[k] is None:
            produced[k] = next(fill)
    return r["track"][C.apply_seq(r["start_idx"], tuple(produced))]


def _half_composer_canonfill_pick(r, pin_slot, canon):
    """pin the stamp-correct move into slot `pin_slot`; fill the other two slots in a FIXED type-order
    `canon`. (A second family of half-composers, to bound the ceiling from the other side.)"""
    stamp = list(r["stamp_moves"])
    pinned = stamp[pin_slot]
    remaining_in_canon = [m for m in canon if m != pinned]
    produced = [None, None, None]
    produced[pin_slot] = pinned
    fill = iter(remaining_in_canon)
    for k in range(3):
        if produced[k] is None:
            produced[k] = next(fill)
    return r["track"][C.apply_seq(r["start_idx"], tuple(produced))]


def assert_balance(records):
    EPS = 1e-9
    for subset in ("comp", "direct"):
        rs = [r for r in records if r["subset"] == subset]
        n = len(rs)
        assert n > 0, f"{subset}: empty"
        # 0) per-record integrity: track is a permutation; rounds strictly increasing; strict config.
        for r in rs:
            assert sorted(r["track"]) == sorted(C.SHAPES), f"{subset} rid {r['rid']}: track not perm"
            assert r["rounds"] == sorted(set(r["rounds"])), f"{subset} rid {r['rid']}: rounds not asc"
            assert strict_isolated(r["start_idx"], tuple(r["stamp_moves"])), \
                f"{subset} rid {r['rid']}: config not strict-isolated"
            assert r["target_shape"] == r["track"][r["target_idx"]]
            assert set(r["stamp_moves"]) == set(C.MOVE_NAMES), f"{subset} rid {r['rid']}: not 3 moves"
        # 1) target figure UNIFORM over the 6 shapes => const-figure picker = 1/K
        figc = Counter(r["target_shape"] for r in rs)
        assert set(figc) == set(C.SHAPES) and len(set(figc.values())) == 1, \
            f"{subset}: target figure not uniform: {dict(figc)}"
        for s in C.SHAPES:
            assert abs(_const_fig(rs, s) - C.POS_CHANCE) < EPS, f"{subset} const-fig {s} != 1/K"
        # 2) target TRACK POSITION balanced => fixed track-position picker <= 1/K
        for j in range(C.K):
            assert _track_pos(rs, j) <= C.POS_CHANCE + EPS, f"{subset} track-pos {j} > 1/K"
        # 3) stamp-order true-order balance (COMP only): each of the 6 orderings equally frequent
        if subset == "comp":
            oc = Counter(r["order_label"] for r in rs)
            assert len(oc) == 6 and len(set(oc.values())) == 1, f"{subset}: order not balanced {dict(oc)}"
            dc = Counter(tuple(r["disp_perm"]) for r in rs)
            assert len(dc) == 6 and len(set(dc.values())) == 1, f"{subset}: display not balanced {dict(dc)}"
        # 4) start / single-move / ordered-pair / reversed-order readers score 0 on the target
        assert _rate(rs, lambda r: r["start_shape"]) < EPS, f"{subset}: start reader != 0"
        for i, nm in enumerate(C.MOVE_NAMES):
            assert _rate(rs, lambda r, i=i: r["single_shapes"][i]) < EPS, \
                f"{subset}: single-move {nm} reader != 0"
        for pair in itertools.permutations(C.MOVE_NAMES, 2):
            a = _rate(rs, lambda r, pr=pair: r["track"][C.apply_seq(r["start_idx"], pr)])
            assert a < EPS, f"{subset}: ordered-pair {pair} reader {a} != 0"
        assert _rate(rs, _rev_pick) < EPS, f"{subset}: reversed-order reader != 0"
        # 5) the headline ceiling family (COMP only): canonical / print = 1/6; half-composers = 0.50.
        if subset == "comp":
            for order in ALL_ORDERS:
                a = _rate(rs, lambda r, o=order: _full_order_pick(r, o))
                assert abs(a - C.POS_CHANCE) < EPS, f"{subset}: canonical {order} {a} != 1/6"
            assert abs(_rate(rs, _print_pick) - C.POS_CHANCE) < EPS, f"{subset}: print-order != 1/6"
            hc_rates = []
            for k in range(3):
                a = _rate(rs, lambda r, k=k: _half_composer_pick(r, k))
                hc_rates.append(a)
                assert abs(a - C.PRINT_CEILING) < EPS, \
                    f"{subset}: half-composer (display-fill) pin {k} = {a} != 0.50"
            for k in range(3):
                for canon in ALL_ORDERS:
                    a = _rate(rs, lambda r, k=k, c=canon: _half_composer_canonfill_pick(r, k, c))
                    assert a <= C.PRINT_CEILING + EPS, \
                        f"{subset}: half-composer (canon-fill) pin {k} {canon} = {a} > 0.50"
                    hc_rates.append(a)
            # 6) the genuine stamp-order composer scores 1.0; the ceiling really is 0.50.
            stamp_rate = _rate(rs, lambda r: r["target_shape"])
            assert abs(stamp_rate - 1.0) < EPS, f"{subset}: stamp-order composer {stamp_rate} != 1.0"
            ceiling = max([_rate(rs, lambda r, o=o: _full_order_pick(r, o)) for o in ALL_ORDERS]
                          + [_rate(rs, _print_pick)] + hc_rates)
            assert abs(ceiling - C.PRINT_CEILING) < EPS, \
                f"{subset}: max non-composition reader {ceiling} != PRINT_CEILING 0.50"
        print(f"  [{subset}] geometry OK: {n} records ({len(set(r['block'] for r in rs))} blocks "
              f"x {C.K}); const-fig=1/K; track-pos<=1/K; "
              + ("canonical/print=1/6; half-composer=0.500; stamp-order=1.000; " if subset == "comp" else "")
              + "start/single-move/ordered-pair/reversed=0.000; freq flat.")
    cp = [r for r in records if r["subset"] == "comp"]
    di = [r for r in records if r["subset"] == "direct"]
    print(f"  totals: {len(cp)} COMP + {len(di)} DIRECT = {len(records)} records/model; "
          f"{len(records) * len(C.MODELS)} finding-bearing calls. Only ordering ALL THREE moves by "
          f"their STAMPS clears the {C.PRINT_CEILING} bar (deeper order-sensitive composition).")


def main():
    records = build()
    assert_balance(records)
    blob = json.dumps({"records": records, "k": C.K, "term": C.TERM, "shapes": C.SHAPES,
                       "n_blocks_comp": C.N_BLOCKS_COMP, "n_blocks_direct": C.N_BLOCKS_DIRECT,
                       "print_ceiling": C.PRINT_CEILING, "direct_floor": C.DIRECT_FLOOR,
                       "pos_chance": C.POS_CHANCE, "seed0": C.SEED0,
                       "perms": C.PERMS, "configs": C.CONFIGS},
                      indent=2, sort_keys=True)
    open(OUT, "w").write(blob + "\n")
    sha = hashlib.sha256(blob.encode()).hexdigest()
    print(f"  wrote {OUT}")
    print(f"  stimuli.json sha256 = {sha}")
    print("  -> put this sha256 in PREREG.md before any finding-bearing call")


if __name__ == "__main__":
    main()
