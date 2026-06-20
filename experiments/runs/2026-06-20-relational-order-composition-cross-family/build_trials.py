#!/usr/bin/env python3
"""build_trials.py (no API) -- the frozen CROSS-FAMILY (heterogeneous-operation) ORDER-SENSITIVE
COMPOSITION stimuli: two transparently different operation kinds (a SPATIAL swap + an ATTRIBUTE
recolor), cross-conditional so they NON-COMMUTE on the coined token DAX's final color. Stamp order =
composition.

THE FOUR GEOMETRY CELLS = recolor_target {a = DAX's start spot, b = the swap partner} x stamp_first
{SWAP, RECOLOR}. DAX always starts on spot a and is moved by the SWAP; the RECOLOR targets one of the
two swap spots. Simulating DAX's (spot,color) through the two ops in stamp order gives final color C0
(DAX's start color) in cells {SWAP-first@a, RECOLOR-first@b} and Cr (the recolor color) in cells
{SWAP-first@b, RECOLOR-first@a}. So the answer is fixed by NEITHER the stamp order alone NOR the
geometry alone -- only by BOTH together: composing the spatial and attribute updates IN STAMP ORDER.

WHY THE 0.50 CEILING (re-proven over the actual records in assert_balance): with the four cells
equally frequent the answer is C0 half the time and Cr half the time, so EVERY non-composing reader
tops out at exactly 0.50 -- report-C0 (= SWAP-only / ignore-recolor), report-Cr (= assume the repaint
always lands on DAX), recolor-only (ignore the swap), apply-both-in-a-FIXED-order (either way),
apply-both-in-PRINT-order, and every fixed-spot initial/final-color or const-color reader. ONLY a
reader that applies the two operations in the per-trial STAMP order clears 0.50 (= 1.0). All brute-
forced below, not asserted by hand. (Unlike the homogeneous-permutation runs where a reversed-order
reader scored 0, here a fixed-order reader scores 0.50 -- with two heterogeneous ops and a binary
{C0,Cr} answer a fixed order is right half the time, exactly as canonical/print readers scored 0.50
in the original two-move STEP/FLIP run. The ceiling and its interpretive force are identical.)

Prints the sha256 that must go into PREREG.md.
"""
import hashlib
import json
import os
from collections import Counter

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stimuli.json")

ALL_ORDERS = [("SWAP", "RECOLOR"), ("RECOLOR", "SWAP")]


def _recolor_spot(rec):
    return rec["a"] if rec["recolor_target"] == "a" else rec["b"]


def full_state(rec, order):
    """The color on each of the K spots after applying the two ops in `order` (tracks ALL tokens, for
    the fixed-spot-color reader family). SWAP exchanges the two spots' colors; RECOLOR repaints."""
    colors = list(rec["init_colors"])
    a, b, rt = rec["a"], rec["b"], _recolor_spot(rec)
    for nm in order:
        if nm == "SWAP":
            colors[a], colors[b] = colors[b], colors[a]
        else:
            colors[rt] = rec["recolor_color"]
    return colors


def _build_block(cell, geom, query, rid_start, ncolors, round_pair_idx):
    """One block: fixes the cell (recolor_target, stamp_first) and the (a,b) geometry; cycles the
    ANSWER color over `ncolors` of the 6 colors (so the const-color picker is at chance) and the 2
    display orders (so the print-order reader hits 0.50). DAX's start spot a carries C0; the other
    spots carry distinct distractor colors disjoint from {C0, Cr}."""
    recolor_target, stamp_first = cell
    a, b = geom
    stamp_order = (stamp_first, "RECOLOR" if stamp_first == "SWAP" else "SWAP")
    answer_is_c0 = cell in (("a", "SWAP"), ("b", "RECOLOR"))
    records, rid = [], rid_start
    for j in range(ncolors):
        ans_color = C.COLORS[j % C.NUM_COLORS]
        other = C.COLORS[(j + 3) % C.NUM_COLORS]            # the non-answer of {C0, Cr}; distinct
        if answer_is_c0:
            c0, cr = ans_color, other
        else:
            c0, cr = other, ans_color
        assert c0 != cr
        # distractor colors for the non-DAX spots: disjoint from {c0, cr}, distinct, rotated.
        pool = [c for c in C.COLORS if c not in (c0, cr)]
        pool = pool[j % len(pool):] + pool[:j % len(pool)]
        init_colors = [None] * C.K
        init_colors[a] = c0
        di = 0
        for p in range(C.K):
            if p == a:
                continue
            init_colors[p] = pool[di]
            di += 1
        rounds = C.ROUND_PAIRS[round_pair_idx % len(C.ROUND_PAIRS)]
        round_pair_idx += 1
        disp_perm = C.DISPLAY_PERMS[j % 2]
        rec = {
            "rid": rid, "subset": query.lower(), "block": f"{query[:4]}-{cell[1][0]}{recolor_target}-{a}{b}",
            "query": query, "a": a, "b": b, "recolor_target": recolor_target,
            "stamp_first": stamp_first, "stamp_order": list(stamp_order),
            "start_color": c0, "recolor_color": cr, "init_colors": init_colors,
            "rounds": list(rounds), "disp_perm": list(disp_perm),
            "cell_label": f"{stamp_first[0]}@{recolor_target}",
        }
        rec["display_order"] = [stamp_order[i] for i in disp_perm]
        rec["hist_display"] = [{"round": rounds[i], "op": stamp_order[i], "desc": C.op_desc(rec, stamp_order[i])}
                               for i in disp_perm]
        rec["target_color"] = C.final_color(rec, stamp_order)
        rec["rev_color"] = C.final_color(rec, tuple(reversed(stamp_order)))
        records.append(rec)
        rid += 1
    return records, round_pair_idx


def build():
    records, rid, rpi = [], 0, 0
    # COMP: 4 cells x 3 geoms = 12 blocks x 6 colors = 72 records.
    for bi in range(12):
        cell = C.CELLS[bi // 3]
        geom = C.GEOMS[bi % 4]
        blk, rpi = _build_block(cell, geom, "COMP", rid, C.NUM_COLORS, rpi)
        records += blk
        rid += len(blk)
    # DIRECT: 4 cells x 3 geoms = 12 blocks x 3 colors = 36 records.
    for bi in range(12):
        cell = C.CELLS[bi // 3]
        geom = C.GEOMS[bi % 4]
        blk, rpi = _build_block(cell, geom, "DIRECT", rid, 3, rpi)
        records += blk
        rid += len(blk)
    return records


# ---- idealized-reader scorers (analytic certification) -----------------------------------
def _rate(records, pick_fn):
    return sum(1 for r in records if pick_fn(r) == r["target_color"]) / len(records)


def _composer(r):
    return C.final_color(r, tuple(r["stamp_order"]))


def _noncomposing_readers():
    """A comprehensive family of readers that do NOT use the per-trial STAMP order. Each must score
    <= PRINT_CEILING (0.50). (The genuine stamp-order composer is excluded and asserted == 1.0.)"""
    fams = {}
    # const-color (one per color)
    for c in C.COLORS:
        fams[f"const-{c}"] = (lambda r, c=c: c)
    # identity readers
    fams["start-color(C0)"] = lambda r: r["start_color"]
    fams["recolor-color(Cr)"] = lambda r: r["recolor_color"]
    # single-op-only readers (apply just ONE op to DAX)
    fams["swap-only"] = lambda r: C.final_color(r, ("SWAP",))
    fams["recolor-only"] = lambda r: C.final_color(r, ("RECOLOR",))
    # fixed-order readers (apply BOTH but in a fixed order, ignoring stamps)
    fams["fixed-SWAP-first"] = lambda r: C.final_color(r, ("SWAP", "RECOLOR"))
    fams["fixed-RECOLOR-first"] = lambda r: C.final_color(r, ("RECOLOR", "SWAP"))
    # print/display-order reader
    fams["print-order"] = lambda r: C.final_color(r, tuple(r["display_order"]))
    # fixed-spot initial-color readers
    for p in range(C.K):
        fams[f"init-spot{p}"] = (lambda r, p=p: r["init_colors"][p])
    # fixed-spot FINAL-color under each FIXED order (non-composing: fixed order, not stamp order)
    for p in range(C.K):
        fams[f"final-spot{p}-SWAPfirst"] = (lambda r, p=p: full_state(r, ("SWAP", "RECOLOR"))[p])
        fams[f"final-spot{p}-RECOLORfirst"] = (lambda r, p=p: full_state(r, ("RECOLOR", "SWAP"))[p])
    return fams


def assert_balance(records):
    EPS = 1e-9
    for subset in ("comp", "direct"):
        rs = [r for r in records if r["subset"] == subset]
        n = len(rs)
        assert n > 0, f"{subset}: empty"
        # 0) per-record integrity
        for r in rs:
            assert r["a"] != r["b"], f"{subset} rid {r['rid']}: a==b"
            assert r["start_color"] != r["recolor_color"], f"{subset} rid {r['rid']}: C0==Cr"
            assert r["init_colors"][r["a"]] == r["start_color"], f"{subset} rid {r['rid']}: DAX init color"
            assert len(set(r["init_colors"])) == C.K, f"{subset} rid {r['rid']}: init colors not distinct"
            assert set(r["init_colors"]).issubset(set(C.COLORS))
            assert r["rounds"][0] < r["rounds"][1], f"{subset} rid {r['rid']}: rounds not ascending"
            assert set(r["stamp_order"]) == set(C.MOVE_NAMES), f"{subset} rid {r['rid']}: not both ops"
            # distractor spots disjoint from {C0, Cr}
            for p in range(C.K):
                if p != r["a"]:
                    assert r["init_colors"][p] not in (r["start_color"], r["recolor_color"]), \
                        f"{subset} rid {r['rid']}: distractor spot {p} not disjoint from C0/Cr"
            assert r["target_color"] == _composer(r), f"{subset} rid {r['rid']}: target != composer"
        # 1) the genuine stamp-order composer scores exactly 1.0
        comp_rate = _rate(rs, _composer)
        assert abs(comp_rate - 1.0) < EPS, f"{subset}: stamp-order composer {comp_rate} != 1.0"
        # 2) cell / order / target balance
        cellc = Counter(r["cell_label"] for r in rs)
        assert len(cellc) == 4 and len(set(cellc.values())) == 1, f"{subset}: cells not balanced {dict(cellc)}"
        sfc = Counter(r["stamp_first"] for r in rs)
        assert len(set(sfc.values())) == 1, f"{subset}: stamp_first not balanced {dict(sfc)}"
        rtc = Counter(r["recolor_target"] for r in rs)
        assert len(set(rtc.values())) == 1, f"{subset}: recolor_target not balanced {dict(rtc)}"
        if subset == "comp":  # display order is decoupled/balanced only where it matters (the
            dc = Counter(tuple(r["disp_perm"]) for r in rs)  # spontaneous COMP arm); DIRECT states it
            assert len(dc) == 2 and len(set(dc.values())) == 1, f"{subset}: display not balanced {dict(dc)}"
        # 3) DAX start spot balanced over the K spots (position neutralization)
        ac = Counter(r["a"] for r in rs)
        assert len(ac) == C.K and len(set(ac.values())) == 1, f"{subset}: DAX start spot not uniform {dict(ac)}"
        bc = Counter(r["b"] for r in rs)
        assert len(bc) == C.K and len(set(bc.values())) == 1, f"{subset}: swap partner spot not uniform {dict(bc)}"
        # 4) the NON-COMPOSING reader family is capped at PRINT_CEILING = 0.50 -- a property of the
        # SPONTANEOUS COMP arm (in DIRECT the order is stated, so print/fixed-order readers ARE the
        # composer; the ceiling logic does not apply, exactly as in the three-move analyze).
        worst, worst_name = 0.0, None
        if subset == "comp":
            fams = _noncomposing_readers()
            for name, fn in fams.items():
                a = _rate(rs, fn)
                if a > worst:
                    worst, worst_name = a, name
                assert a <= C.PRINT_CEILING + EPS, f"{subset}: non-composing reader '{name}' = {a} > 0.50"
        # 5) COMP-only: answer uniform over the 6 colors => const-color = 1/6 exactly
        if subset == "comp":
            ansc = Counter(r["target_color"] for r in rs)
            assert set(ansc) == set(C.COLORS) and len(set(ansc.values())) == 1, \
                f"comp: answer color not uniform {dict(ansc)}"
            for c in C.COLORS:
                assert abs(_rate(rs, lambda r, c=c: c) - C.POS_CHANCE) < EPS, f"comp: const-{c} != 1/6"
        print(f"  [{subset}] geometry OK: {n} records ({len(set(r['block'] for r in rs))} blocks); "
              f"composer=1.000; cells/stamp_first/recolor_target/display/start-spot balanced; "
              f"worst non-composing reader = '{worst_name}' at {worst:.4f} (<= {C.PRINT_CEILING}); "
              + ("answer uniform over 6 colors (const=1/6)." if subset == "comp" else "manip-check set."))
    cp = [r for r in records if r["subset"] == "comp"]
    di = [r for r in records if r["subset"] == "direct"]
    print(f"  totals: {len(cp)} COMP + {len(di)} DIRECT = {len(records)} records/model; "
          f"{len(records) * len(C.MODELS)} finding-bearing calls. Only composing the SWAP and the "
          f"RECOLOR in STAMP order clears the {C.PRINT_CEILING} bar (cross-family order-sensitive "
          f"composition).")


def main():
    records = build()
    assert_balance(records)
    blob = json.dumps({"records": records, "k": C.K, "term": C.TERM, "colors": C.COLORS,
                       "n_blocks_comp": C.N_BLOCKS_COMP, "n_blocks_direct": C.N_BLOCKS_DIRECT,
                       "print_ceiling": C.PRINT_CEILING, "direct_floor": C.DIRECT_FLOOR,
                       "pos_chance": C.POS_CHANCE, "seed0": C.SEED0,
                       "cells": [list(c) for c in C.CELLS], "geoms": [list(g) for g in C.GEOMS]},
                      indent=2, sort_keys=True)
    open(OUT, "w").write(blob + "\n")
    sha = hashlib.sha256(blob.encode()).hexdigest()
    print(f"  wrote {OUT}")
    print(f"  stimuli.json sha256 = {sha}")
    print("  -> put this sha256 in PREREG.md before any finding-bearing call")


if __name__ == "__main__":
    main()
