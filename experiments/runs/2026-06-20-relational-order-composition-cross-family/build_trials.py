#!/usr/bin/env python3
"""build_trials.py (no API) -- the frozen CROSS-FAMILY (heterogeneous-operation) ORDER-SENSITIVE
COMPOSITION stimuli, POSITION-ANCHORED readout, MATCHED-PAIR design: two transparently different
operation kinds (a SPATIAL swap + an ATTRIBUTE recolor), non-commuting on the color at a FIXED queried
spot (the "DAX spot"). Stamp order = composition.

THE MATCHED-PAIR CONSTRUCTION (the fix for the geometry-x-cell confound an independent pre-run critic
found, 2026-06-20). Every prior attempt balanced the MARGINALS (stamp_first 36:36, etc.) but left the
visible swap-pair geometry CORRELATED with the order/cell -- and since the SWAP move names its spots,
that geometry is fully visible, so a reader keyed on geometry recovered the answer above 0.50 without
reading the round stamps. This design removes that by construction: each "unit" fixes the ENTIRE
visible scene (the swap pair a,b; the readout spot s; the recolor target m; the full initial coloring;
the recolor color; and the physical print order of the two op-lines) and emits a MATCHED PAIR of
records that differ ONLY in which op carries the earlier round stamp (SWAP-first vs RECOLOR-first).
The two records of a pair therefore have IDENTICAL visible content except the round numbers attached
to the two op-lines, and OPPOSITE answers. So stamp order is independent of EVERYTHING visible except
the round stamps themselves: any reader that does not read the per-op round stamps -- including a
reader keyed on the swap-pair / any visible-geometry signature -- is forced to exactly 0.50 (it gets
one record of each pair right). ONLY a reader that reads the round stamps and applies the two ops in
stamp order clears 0.50 (= 1.0). assert_balance proves this two ways: the brute-forced reader family
AND a geometry-oracle upper bound (the best a reader keyed on the full visible-minus-stamps signature
can do).

THE FOUR LOGICAL CELLS = readout_type {SAME = the DAX spot s IS the recolor target m; DIFF = s is the
non-recolored swap spot} x stamp_first {SWAP, RECOLOR}. The answer at spot s is Cr (the recolor color)
in cells {(SAME,SWAP),(DIFF,RECOLOR)} and C_oth (the OTHER swap spot's initial color) in
{(SAME,RECOLOR),(DIFF,SWAP)}; the DAX spot's own initial color is always overwritten, so it is never
the answer. Each unit contributes exactly one Cr-answer record and one C_oth-answer record.

Prints the sha256 that must go into the PREREG before any finding-bearing call.
"""
import hashlib
import json
import os
from collections import Counter, defaultdict

import common as C

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stimuli.json")


def _geometries():
    """All 16 visible geometries: 4 swap pairs x 4 (readout spot s, recolor target m) on the swap
    spots. Perfectly balances the swap pair, the readout spot s (each spot 4x), and readout_type
    (8 SAME / 8 DIFF)."""
    geos = []
    for (a, b) in C.GEOMS:
        for (s, m) in [(a, a), (b, b), (a, b), (b, a)]:
            geos.append((a, b, s, m))
    return geos


GEOMETRIES = _geometries()


def _assign_colors(o, s, a, b, cr, coth):
    """Initial coloring of the K spots: spot o = C_oth; spot s = a color distinct from BOTH answers
    (it is overwritten either way); the remaining distractor spots distinct; all initials disjoint
    from the recolor color Cr."""
    used = {cr, coth}
    cs = next(c for c in C.COLORS if c not in used)          # init color of the readout spot s
    used.add(cs)
    init = [None] * C.K
    init[o] = coth
    init[s] = cs
    fill = (c for c in C.COLORS if c not in used)
    for p in range(C.K):
        if init[p] is None:
            init[p] = next(fill)
    return init


def _make_record(rid, query, geo, cr, coth, stamp_first, rounds, print_swap_first):
    a, b, s, m = geo
    o = b if s == a else a
    readout_type = "SAME" if s == m else "DIFF"
    stamp_order = (stamp_first, "RECOLOR" if stamp_first == "SWAP" else "SWAP")
    init_colors = _assign_colors(o, s, a, b, cr, coth)
    # round attached to each op (lower round = earlier = stamp_first)
    op_round = {stamp_order[0]: rounds[0], stamp_order[1]: rounds[1]}
    display_ops = ("SWAP", "RECOLOR") if print_swap_first else ("RECOLOR", "SWAP")
    rec = {
        "rid": rid, "subset": query.lower(),
        "block": f"{query[:4]}-{readout_type[0]}{stamp_first[0]}-s{s}m{m}-{a}{b}",
        "query": query, "a": a, "b": b, "s": s, "o": o, "m": m,
        "readout_type": readout_type, "stamp_first": stamp_first,
        "stamp_order": list(stamp_order), "recolor_color": cr,
        "init_colors": init_colors, "rounds": list(rounds),
        "display_order": list(display_ops),
        "print_swap_first": print_swap_first,
        "cell_label": f"{readout_type}@{stamp_first[0]}",
    }
    rec["hist_display"] = [{"round": op_round[op], "op": op, "desc": C.op_desc(rec, op)}
                           for op in display_ops]
    rec["target_color"] = C.answer_color(rec)
    rec["rev_color"] = C.color_at(rec, tuple(reversed(stamp_order)), s)
    return rec


def build():
    records, rid, u = [], 0, 0
    # COMP: 3 color-reps x 16 geometries = 48 units; each unit emits the MATCHED PAIR (both orders)
    # -> 96 records. Colors per unit make the answer uniform over the 6 colors.
    for rep in range(3):
        for geo in GEOMETRIES:
            cr = C.COLORS[u % C.NUM_COLORS]
            coth = C.COLORS[(u + 3) % C.NUM_COLORS]
            rounds = C.ROUND_PAIRS[u % len(C.ROUND_PAIRS)]
            print_swap_first = (u % 2 == 0)
            for stamp_first in ("SWAP", "RECOLOR"):          # the matched pair
                records.append(_make_record(rid, "COMP", geo, cr, coth, stamp_first, rounds,
                                            print_swap_first))
                rid += 1
            u += 1
    # DIRECT: 1 color-rep x 16 geometries = 16 units -> 32 records (the order is stated, so the
    # matched pair just supplies both on-demand directions).
    for geo in GEOMETRIES:
        cr = C.COLORS[u % C.NUM_COLORS]
        coth = C.COLORS[(u + 3) % C.NUM_COLORS]
        rounds = C.ROUND_PAIRS[u % len(C.ROUND_PAIRS)]
        print_swap_first = (u % 2 == 0)
        for stamp_first in ("SWAP", "RECOLOR"):
            records.append(_make_record(rid, "DIRECT", geo, cr, coth, stamp_first, rounds,
                                        print_swap_first))
            rid += 1
        u += 1
    return records


# ---- idealized-reader scorers (analytic certification) -----------------------------------
def _rate(records, pick_fn):
    return sum(1 for r in records if pick_fn(r) == r["target_color"]) / len(records)


def _composer(r):
    return C.color_at(r, tuple(r["stamp_order"]), r["s"])


def _noncomposing_readers():
    """A family of readers that do NOT apply the two ops in the per-trial STAMP order. EVERY one must
    score <= PRINT_CEILING (0.50). Includes the stamp-using PARTIAL readers and a fixed-order-by-
    swap-pair reader (the two shortcuts that broke earlier designs)."""
    fams = {}
    for c in C.COLORS:
        fams[f"const-{c}"] = (lambda r, c=c: c)
    fams["recolor-color(Cr)"] = lambda r: r["recolor_color"]
    fams["init@s"] = lambda r: r["init_colors"][r["s"]]
    fams["init@o"] = lambda r: r["init_colors"][r["o"]]
    fams["swap-only@s"] = lambda r: C.color_at(r, ("SWAP",), r["s"])
    fams["recolor-only@s"] = lambda r: C.color_at(r, ("RECOLOR",), r["s"])
    fams["apply-only-EARLIER@s"] = lambda r: C.color_at(r, (r["stamp_order"][0],), r["s"])
    fams["apply-only-LATER@s"] = lambda r: C.color_at(r, (r["stamp_order"][1],), r["s"])
    fams["apply-only-PRINT-FIRST@s"] = lambda r: C.color_at(r, (r["display_order"][0],), r["s"])
    fams["apply-only-PRINT-SECOND@s"] = lambda r: C.color_at(r, (r["display_order"][1],), r["s"])
    fams["fixed-SWAP-first@s"] = lambda r: C.color_at(r, ("SWAP", "RECOLOR"), r["s"])
    fams["fixed-RECOLOR-first@s"] = lambda r: C.color_at(r, ("RECOLOR", "SWAP"), r["s"])
    fams["reverse-stamp@s"] = lambda r: r["rev_color"]
    fams["print-order@s"] = lambda r: C.color_at(r, tuple(r["display_order"]), r["s"])
    for p in range(C.K):
        fams[f"init-spot{p}"] = (lambda r, p=p: r["init_colors"][p])
        fams[f"final-spot{p}-SWAPfirst"] = (lambda r, p=p: C.color_at(r, ("SWAP", "RECOLOR"), p))
        fams[f"final-spot{p}-RECOLORfirst"] = (lambda r, p=p: C.color_at(r, ("RECOLOR", "SWAP"), p))
    return fams


def _visible_sig(r):
    """Everything a reader can see EXCEPT which op carries which round stamp: the spots, the recolor
    target+color, the full coloring, the physical print order, and the SET of round numbers (not their
    op-assignment). A reader keyed on this signature is the strongest non-composing reader."""
    return (r["a"], r["b"], r["s"], r["m"], r["recolor_color"], tuple(r["init_colors"]),
            tuple(r["display_order"]), tuple(sorted(r["rounds"])))


def _geometry_oracle_rate(rs):
    """Upper bound on any reader keyed on the visible-minus-stamps signature: group by signature and
    take the most common answer in each group. With matched pairs this is exactly 0.50."""
    groups = defaultdict(list)
    for r in rs:
        groups[_visible_sig(r)].append(r["target_color"])
    best = sum(max(Counter(g).values()) for g in groups.values())
    return best / len(rs)


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
            assert (r["s"] == r["m"]) == (r["readout_type"] == "SAME")
            assert len(set(r["init_colors"])) == C.K, f"{subset} rid {r['rid']}: inits not distinct"
            assert r["recolor_color"] not in r["init_colors"], f"{subset} rid {r['rid']}: Cr in inits"
            assert r["rounds"][0] < r["rounds"][1], f"{subset} rid {r['rid']}: rounds not ascending"
            assert set(r["stamp_order"]) == set(C.MOVE_NAMES)
            assert r["target_color"] != r["rev_color"], \
                f"{subset} rid {r['rid']}: not order-discriminating"
            assert r["target_color"] == _composer(r)
            assert r["init_colors"][r["s"]] != r["target_color"], \
                f"{subset} rid {r['rid']}: init@s == answer"
        comp_rate = _rate(rs, _composer)
        assert abs(comp_rate - 1.0) < EPS, f"{subset}: stamp-order composer {comp_rate} != 1.0"
        # marginal balance
        for key in ("cell_label", "stamp_first", "readout_type", "s", "a"):
            c = Counter(r[key] for r in rs)
            assert len(set(c.values())) == 1, f"{subset}: {key} not balanced {dict(c)}"
        c = Counter(tuple(r["display_order"]) for r in rs)
        assert len(c) == 2 and len(set(c.values())) == 1, f"{subset}: print order not balanced {dict(c)}"
        # MATCHED-PAIR + geometry-oracle: the strongest visible-geometry reader caps at 0.50
        oracle = _geometry_oracle_rate(rs)
        assert oracle <= C.PRINT_CEILING + EPS, \
            f"{subset}: geometry-oracle reader = {oracle} > 0.50 (visible geometry leaks the answer)"
        worst, worst_name = 0.0, None
        if subset == "comp":
            for name, fn in _noncomposing_readers().items():
                a = _rate(rs, fn)
                if a > worst:
                    worst, worst_name = a, name
                assert a <= C.PRINT_CEILING + EPS, f"comp: non-composing reader '{name}' = {a} > 0.50"
            ansc = Counter(r["target_color"] for r in rs)
            assert set(ansc) == set(C.COLORS) and len(set(ansc.values())) == 1, \
                f"comp: answer color not uniform {dict(ansc)}"
            for c0 in C.COLORS:
                assert abs(_rate(rs, lambda r, c=c0: c) - C.POS_CHANCE) < EPS, f"comp: const-{c0} != 1/6"
        print(f"  [{subset}] geometry OK: {n} records; composer=1.000; "
              f"cells/stamp_first/readout_type/readout-spot/print-order balanced; "
              f"geometry-oracle (strongest visible-geometry reader) = {oracle:.4f} (<= {C.PRINT_CEILING}); "
              + (f"worst brute-forced non-composing reader = '{worst_name}' at {worst:.4f}; "
                 f"answer uniform over 6 colors (const=1/6)." if subset == "comp" else "manip-check set."))
    cp = [r for r in records if r["subset"] == "comp"]
    di = [r for r in records if r["subset"] == "direct"]
    print(f"  totals: {len(cp)} COMP + {len(di)} DIRECT = {len(records)} records/model; "
          f"{len(records) * len(C.MODELS)} finding-bearing calls. Matched pairs make stamp order "
          f"independent of all visible geometry: ONLY reading the round stamps and composing in stamp "
          f"order clears the {C.PRINT_CEILING} bar.")


def main():
    records = build()
    assert_balance(records)
    blob = json.dumps({"records": records, "k": C.K, "term": C.TERM, "colors": C.COLORS,
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
