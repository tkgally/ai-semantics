#!/usr/bin/env python3
"""build_trials.py (no API) -- the frozen CROSS-FAMILY (heterogeneous-operation) ORDER-SENSITIVE
COMPOSITION stimuli, POSITION-ANCHORED readout: two transparently different operation kinds (a SPATIAL
swap + an ATTRIBUTE recolor), non-commuting on the color at a FIXED queried spot (the "DAX spot").
Stamp order = composition.

THE FOUR GEOMETRY CELLS = readout_type {SAME = the DAX spot s IS the recolor target m; DIFF = s is the
non-recolored swap spot} x stamp_first {SWAP, RECOLOR}. The DAX spot s is one of the two swap spots,
so both ops are live at s. Simulating the color at s through the two ops in stamp order gives the
answer Cr (the recolor color) in cells {(SAME,SWAP),(DIFF,RECOLOR)} and C_oth (the OTHER swap spot's
initial color) in {(SAME,RECOLOR),(DIFF,SWAP)}. The DAX spot's own initial color is always overwritten
(swapped out or recolored), so it is never the answer. The answer is fixed by NEITHER the stamp order
alone NOR the geometry alone -- only by both: composing the spatial and attribute updates IN STAMP
ORDER.

POSITION-ANCHORED, not object-anchored: an independent pre-run critic (2026-06-20) found that anchoring
the readout to the MOVED token ("what color is DAX?") admits a stamp-using single-op shortcut
(apply-only-the-earlier-op scored 0.75, falsely clearing the bar), because following the moved object
makes the spatial op a relabeling under which the attribute op is inert in most cells. Anchoring the
readout to a FIXED spot s removes this: at a fixed spot BOTH ops are live in every cell (SWAP fixes
which token occupies s; RECOLOR fixes a color), so every single-op and stamp-using-PARTIAL reader caps
at 0.50. This certification therefore brute-forces those partial readers EXPLICITLY (apply-only-
earlier, apply-only-later, apply-only-print-first/second), the very shortcuts that broke the
object-anchored design.

WHY THE 0.50 CEILING (re-proven over the actual records in assert_balance): with the four cells equally
frequent the answer is C_oth half the time and Cr half the time, so EVERY non-composing reader tops
out at exactly 0.50. ONLY a reader that applies the two operations in the per-trial STAMP order clears
0.50 (= 1.0).

Prints the sha256 that must go into the PREREG before any finding-bearing call.
"""
import hashlib
import json
import os
from collections import Counter

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stimuli.json")


def _build_block(cell, geom, primary, query, rid_start, ncolors, round_pair_idx):
    """One block: fixes the cell (readout_type, stamp_first) and the (a,b) swap geometry; `primary`
    picks which swap spot is the DAX readout spot s (the other is `o`). Cycles the ANSWER color over
    `ncolors` of the 6 colors and the 2 display orders. The recolor color is disjoint from every
    spot's initial color (so fixed-spot-initial readers stay clean)."""
    readout_type, stamp_first = cell
    a, b = geom
    s = primary
    o = b if primary == a else a            # the OTHER swap spot
    m = s if readout_type == "SAME" else o  # recolor target
    stamp_order = (stamp_first, "RECOLOR" if stamp_first == "SWAP" else "SWAP")
    answer_is_cr = cell in (("SAME", "SWAP"), ("DIFF", "RECOLOR"))
    records, rid = [], rid_start
    for j in range(ncolors):
        ans_color = C.COLORS[j % C.NUM_COLORS]
        # assign the 4 distinct initial colors + a disjoint recolor color, so that the cell's answer
        # (Cr or C_oth = init[o]) equals ans_color and cycles over all 6 colors across the block.
        if answer_is_cr:
            recolor_color = ans_color
            init_pool = [c for c in C.COLORS if c != recolor_color]            # 5 colors, Cr excluded
            init_pool = init_pool[j % 5:] + init_pool[:j % 5]
            init_colors = [None] * C.K
            spots_in_order = [o] + [p for p in range(C.K) if p != o]           # o first (any color)
            for idx, p in enumerate(spots_in_order):
                init_colors[p] = init_pool[idx]
        else:  # answer is C_oth = init color of spot o
            init_oth = ans_color
            rest = [c for c in C.COLORS if c != init_oth]
            rest = rest[j % 5:] + rest[:j % 5]
            recolor_color = rest[0]                                            # disjoint from inits
            other_inits = [c for c in rest[1:] if c != recolor_color][:C.K - 1]
            init_colors = [None] * C.K
            init_colors[o] = init_oth
            fill = iter(other_inits)
            for p in range(C.K):
                if p != o:
                    init_colors[p] = next(fill)
        rounds = C.ROUND_PAIRS[round_pair_idx % len(C.ROUND_PAIRS)]
        round_pair_idx += 1
        disp_perm = C.DISPLAY_PERMS[j % 2]
        rec = {
            "rid": rid, "subset": query.lower(),
            "block": f"{query[:4]}-{readout_type[0]}{stamp_first[0]}-s{s}m{m}",
            "query": query, "a": a, "b": b, "s": s, "o": o, "m": m,
            "readout_type": readout_type, "stamp_first": stamp_first,
            "stamp_order": list(stamp_order), "recolor_color": recolor_color,
            "init_colors": init_colors, "rounds": list(rounds), "disp_perm": list(disp_perm),
            "cell_label": f"{readout_type}@{stamp_first[0]}",
        }
        rec["display_order"] = [stamp_order[i] for i in disp_perm]
        rec["hist_display"] = [{"round": rounds[i], "op": stamp_order[i],
                                "desc": C.op_desc(rec, stamp_order[i])} for i in disp_perm]
        rec["target_color"] = C.answer_color(rec)
        rec["rev_color"] = C.color_at(rec, tuple(reversed(stamp_order)), s)
        records.append(rec)
        rid += 1
    return records, round_pair_idx


def build():
    records, rid, rpi = [], 0, 0
    for bi in range(12):                                  # COMP: 4 cells x 3 geoms x 6 colors = 72
        cell = C.CELLS[bi // 3]
        geom = C.GEOMS[bi % 4]
        primary = geom[(bi // 4) % 2]                     # cycle the readout spot over all 4 spots
        blk, rpi = _build_block(cell, geom, primary, "COMP", rid, C.NUM_COLORS, rpi)
        records += blk
        rid += len(blk)
    for bi in range(12):                                  # DIRECT: 4 cells x 3 geoms x 3 colors = 36
        cell = C.CELLS[bi // 3]
        geom = C.GEOMS[bi % 4]
        primary = geom[(bi // 4) % 2]
        blk, rpi = _build_block(cell, geom, primary, "DIRECT", rid, 3, rpi)
        records += blk
        rid += len(blk)
    return records


# ---- idealized-reader scorers (analytic certification) -----------------------------------
def _rate(records, pick_fn):
    return sum(1 for r in records if pick_fn(r) == r["target_color"]) / len(records)


def _composer(r):
    return C.color_at(r, tuple(r["stamp_order"]), r["s"])


def _noncomposing_readers():
    """A comprehensive family of readers that do NOT apply the two ops in the per-trial STAMP order.
    EVERY one must score <= PRINT_CEILING (0.50). Includes the stamp-using PARTIAL readers
    (apply-only-the-earlier/later op, apply-only-the-print-first/second op) that broke the
    object-anchored design."""
    fams = {}
    for c in C.COLORS:
        fams[f"const-{c}"] = (lambda r, c=c: c)
    fams["recolor-color(Cr)"] = lambda r: r["recolor_color"]
    fams["init@s"] = lambda r: r["init_colors"][r["s"]]
    fams["init@o"] = lambda r: r["init_colors"][r["o"]]
    # single-op readouts at s
    fams["swap-only@s"] = lambda r: C.color_at(r, ("SWAP",), r["s"])
    fams["recolor-only@s"] = lambda r: C.color_at(r, ("RECOLOR",), r["s"])
    # stamp-using PARTIAL readers (the object-anchored killers)
    fams["apply-only-EARLIER@s"] = lambda r: C.color_at(r, (r["stamp_order"][0],), r["s"])
    fams["apply-only-LATER@s"] = lambda r: C.color_at(r, (r["stamp_order"][1],), r["s"])
    fams["apply-only-PRINT-FIRST@s"] = lambda r: C.color_at(r, (r["display_order"][0],), r["s"])
    fams["apply-only-PRINT-SECOND@s"] = lambda r: C.color_at(r, (r["display_order"][1],), r["s"])
    # both ops, but in a FIXED / reversed / print order (not the per-trial stamp order)
    fams["fixed-SWAP-first@s"] = lambda r: C.color_at(r, ("SWAP", "RECOLOR"), r["s"])
    fams["fixed-RECOLOR-first@s"] = lambda r: C.color_at(r, ("RECOLOR", "SWAP"), r["s"])
    fams["reverse-stamp@s"] = lambda r: r["rev_color"]
    fams["print-order@s"] = lambda r: C.color_at(r, tuple(r["display_order"]), r["s"])
    # fixed-spot readouts (initial + under each fixed order) at every spot
    for p in range(C.K):
        fams[f"init-spot{p}"] = (lambda r, p=p: r["init_colors"][p])
        fams[f"final-spot{p}-SWAPfirst"] = (lambda r, p=p: C.color_at(r, ("SWAP", "RECOLOR"), p))
        fams[f"final-spot{p}-RECOLORfirst"] = (lambda r, p=p: C.color_at(r, ("RECOLOR", "SWAP"), p))
    return fams


def assert_balance(records):
    EPS = 1e-9
    for subset in ("comp", "direct"):
        rs = [r for r in records if r["subset"] == subset]
        n = len(rs)
        assert n > 0, f"{subset}: empty"
        for r in rs:
            assert r["a"] != r["b"], f"{subset} rid {r['rid']}: a==b"
            assert r["s"] in (r["a"], r["b"]) and r["m"] in (r["a"], r["b"]), \
                f"{subset} rid {r['rid']}: s/m not on swap spots"
            assert (r["s"] == r["m"]) == (r["readout_type"] == "SAME"), \
                f"{subset} rid {r['rid']}: readout_type mismatch"
            assert len(set(r["init_colors"])) == C.K, f"{subset} rid {r['rid']}: inits not distinct"
            assert r["recolor_color"] not in r["init_colors"], \
                f"{subset} rid {r['rid']}: recolor color not disjoint from inits"
            assert set(r["init_colors"]).issubset(set(C.COLORS))
            assert r["rounds"][0] < r["rounds"][1], f"{subset} rid {r['rid']}: rounds not ascending"
            assert set(r["stamp_order"]) == set(C.MOVE_NAMES), f"{subset} rid {r['rid']}: not both ops"
            # genuine order-sensitivity: the answer differs under the reversed order
            assert r["target_color"] != r["rev_color"], \
                f"{subset} rid {r['rid']}: not order-discriminating (target == reverse)"
            assert r["target_color"] == _composer(r), f"{subset} rid {r['rid']}: target != composer"
            # the DAX spot's own initial color is never the answer
            assert r["init_colors"][r["s"]] != r["target_color"], \
                f"{subset} rid {r['rid']}: init@s == answer (readout not overwritten)"
        comp_rate = _rate(rs, _composer)
        assert abs(comp_rate - 1.0) < EPS, f"{subset}: stamp-order composer {comp_rate} != 1.0"
        cellc = Counter(r["cell_label"] for r in rs)
        assert len(cellc) == 4 and len(set(cellc.values())) == 1, f"{subset}: cells not balanced {dict(cellc)}"
        sfc = Counter(r["stamp_first"] for r in rs)
        assert len(set(sfc.values())) == 1, f"{subset}: stamp_first not balanced {dict(sfc)}"
        tc = Counter(r["readout_type"] for r in rs)
        assert len(set(tc.values())) == 1, f"{subset}: readout_type not balanced {dict(tc)}"
        sc = Counter(r["s"] for r in rs)
        assert len(sc) == C.K and len(set(sc.values())) == 1, f"{subset}: readout spot not uniform {dict(sc)}"
        if subset == "comp":
            dc = Counter(tuple(r["disp_perm"]) for r in rs)
            assert len(dc) == 2 and len(set(dc.values())) == 1, f"{subset}: display not balanced {dict(dc)}"
        # the NON-COMPOSING reader family is capped at PRINT_CEILING = 0.50 (COMP arm)
        worst, worst_name = 0.0, None
        if subset == "comp":
            for name, fn in _noncomposing_readers().items():
                a = _rate(rs, fn)
                if a > worst:
                    worst, worst_name = a, name
                assert a <= C.PRINT_CEILING + EPS, f"{subset}: non-composing reader '{name}' = {a} > 0.50"
            ansc = Counter(r["target_color"] for r in rs)
            assert set(ansc) == set(C.COLORS) and len(set(ansc.values())) == 1, \
                f"comp: answer color not uniform {dict(ansc)}"
            for c in C.COLORS:
                assert abs(_rate(rs, lambda r, c=c: c) - C.POS_CHANCE) < EPS, f"comp: const-{c} != 1/6"
        print(f"  [{subset}] geometry OK: {n} records ({len(set(r['block'] for r in rs))} blocks); "
              f"composer=1.000; cells/stamp_first/readout_type/readout-spot balanced; "
              + (f"worst non-composing reader = '{worst_name}' at {worst:.4f} (<= {C.PRINT_CEILING}); "
                 f"answer uniform over 6 colors (const=1/6)." if subset == "comp" else "manip-check set."))
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
    print("  -> put this sha256 in the PREREG before any finding-bearing call")


if __name__ == "__main__":
    main()
