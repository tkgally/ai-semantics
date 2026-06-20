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
import math
import os
from collections import Counter, defaultdict

import common as C


def _wilson_lb(k, n, z=1.96):
    if n == 0:
        return 0.0
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "stimuli.json")


# FOUR geometries (a, b, s, m), one per swap pair, chosen so the readout spot s is uniform over the
# 4 spots and readout_type is balanced (2 SAME where s==m, 2 DIFF where s!=m). Using only 4 geometries
# is deliberate: each geometry is paired with ALL 12 round pairs (build() below), so that CONDITIONING
# on the (always-visible) geometry gives the SAME overlapping round distribution as the marginal --
# which collapses the geometry x single-round-line reader (the freeze-#5 killer) back to chance. With
# more geometries than round-pair slots, geometry would correlate with which round pairs appear and a
# geometry-conditional round reader would leak.
GEOMETRIES = [
    (0, 1, 0, 0),   # SAME, s=0, recolor the DAX spot
    (1, 2, 1, 2),   # DIFF, s=1, recolor the other swap spot
    (2, 3, 2, 2),   # SAME, s=2
    (3, 0, 3, 0),   # DIFF, s=3
]


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
    records, rid = [], 0
    npairs = len(C.ROUND_PAIRS)   # 12 round pairs
    ng = len(GEOMETRIES)          # 4 geometries
    # COMP: 4 geometries x 12 round pairs = 48 units; each unit emits the MATCHED PAIR (both orders)
    # = 96 records. Every geometry is crossed with EVERY round pair exactly once, so conditioning on
    # the visible geometry leaves the full overlapping round distribution (defeats the geometry x
    # single-round-line reader). Colors make the answer uniform over the 6 colors; print order
    # balanced 6:6 within each geometry.
    u = 0
    for gi in range(ng):
        for pi in range(npairs):
            geo = GEOMETRIES[gi]
            cr = C.COLORS[(pi + gi) % C.NUM_COLORS]          # color decorrelated from the round pair
            coth = C.COLORS[(pi + gi + 3) % C.NUM_COLORS]
            rounds = C.ROUND_PAIRS[pi]
            print_swap_first = True                          # constant print order (SWAP
            #   listed first): zero correlation with stamp order; nothing to condition a round reader on
            for stamp_first in ("SWAP", "RECOLOR"):          # the matched pair
                records.append(_make_record(rid, "COMP", geo, cr, coth, stamp_first, rounds,
                                            print_swap_first))
                rid += 1
            u += 1
    # DIRECT: 4 geometries x 4 round pairs x both orders = 32 records (order is stated, so round
    # magnitude is moot); enough for the on-demand gate.
    for gi in range(ng):
        for j in range(4):
            geo = GEOMETRIES[gi]
            cr = C.COLORS[u % C.NUM_COLORS]
            coth = C.COLORS[(u + 3) % C.NUM_COLORS]
            rounds = C.ROUND_PAIRS[(gi * 3 + j) % npairs]
            print_swap_first = True
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


def _round_on_op(r, op):
    """The round number printed on the line for operation `op` (SWAP or RECOLOR)."""
    return r["rounds"][0] if r["stamp_first"] == op else r["rounds"][1]


def _round_on_print_pos(r, pos):
    """The round number on the op printed in physical position `pos` (0 = first printed)."""
    op = r["display_order"][pos]
    return _round_on_op(r, op)


def _best_single_round_reader(rs, value_fn, cond_fn=None):
    """The strongest reader keyed on ONE op-line's absolute round value (optionally CONDITIONED on a
    visible feature `cond_fn`, e.g. the geometry): group by (cond, value) and predict the majority
    stamp_first per group (optimal predictor). Because matched pairs make the answer determined by
    stamp_first, this reader's ANSWER accuracy equals its stamp_first-prediction accuracy. A reader
    that conditions on geometry + ONE round value still does NOT compare the two rounds, so it must
    cap at 0.50 -- the freeze-#5 leak was exactly this geometry-conditional version. Returns
    (k_correct, n)."""
    groups = defaultdict(Counter)
    for r in rs:
        key = (cond_fn(r) if cond_fn else None, value_fn(r))
        groups[key][r["stamp_first"]] += 1
    k = sum(max(c.values()) for c in groups.values())
    return k, len(rs)


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
        # print order is CONSTANT (SWAP listed first): zero correlation with stamp order, and nothing
        # to condition a single-round-line reader on. A print-order reader is still capped via the
        # brute-forced `print-order@s` reader below.
        assert len(set(tuple(r["display_order"]) for r in rs)) == 1, f"{subset}: print order not constant"
        # MATCHED-PAIR + geometry-oracle: the strongest visible-geometry reader caps at 0.50
        oracle = _geometry_oracle_rate(rs)
        assert oracle <= C.PRINT_CEILING + EPS, \
            f"{subset}: geometry-oracle reader = {oracle} > 0.50 (visible geometry leaks the answer)"
        # SINGLE-ROUND-LINE readers: a reader keyed on ONE op-line's absolute round value (the lexical
        # round-magnitude shortcut). The order is determined only on the COMP arm (DIRECT states it).
        round_lb_worst = 0.0
        if subset == "comp":
            line_fns = [("SWAP-line", lambda r: _round_on_op(r, "SWAP")),
                        ("RECOLOR-line", lambda r: _round_on_op(r, "RECOLOR")),
                        ("print-first-line", lambda r: _round_on_print_pos(r, 0)),
                        ("print-second-line", lambda r: _round_on_print_pos(r, 1))]
            # marginal AND conditional on the GENERALIZABLE / STRUCTURAL features a model could key on
            # per-prompt with a CONSISTENT (causal) relationship to the order: the round magnitude
            # itself, and the salient geometry / readout_type (each crossed with ALL round pairs, so
            # geometry is independent of the pair). These are the real shortcuts. NOTE (documented
            # residual, NOT certified): conditioning on per-prompt CONTENT (the exact recolor color)
            # leaves a small in-sample correlation (best (recolor_color, swap-round) reader ~0.656,
            # Wilson-LB ~0.557) -- an OVERFITTING artifact of the 96-record frozen set, not a strategy
            # a model could apply to a fresh prompt (the recolor color is causally irrelevant to the
            # order). Fully erasing even that is combinatorially hard in a small frozen set; this run
            # is SUSPENDED before any spend (see README / the witness-seeking-economics suspension),
            # so the gap is moot, but it is recorded honestly here rather than hidden.
            cond_fns = [("marginal", None),
                        ("|geometry", lambda r: (r["a"], r["b"], r["s"], r["m"])),
                        ("|readout_type", lambda r: r["readout_type"])]
            for ltag, lfn in line_fns:
                for ctag, cfn in cond_fns:
                    k, nn = _best_single_round_reader(rs, lfn, cfn)
                    lb = _wilson_lb(k, nn)
                    round_lb_worst = max(round_lb_worst, lb)
                    assert lb <= C.PRINT_CEILING + EPS, \
                        f"comp: single-round-line reader '{ltag}{ctag}' rate={k/nn:.4f} " \
                        f"Wilson-LB={lb:.4f} > 0.50 (round magnitude leaks the order)"
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
              f"cells/stamp_first/readout_type/readout-spot balanced; print order constant; "
              f"geometry-oracle = {oracle:.4f}; "
              + (f"worst single-round-line reader Wilson-LB = {round_lb_worst:.4f} (<= {C.PRINT_CEILING}); "
                 f"worst brute-forced non-composing reader = '{worst_name}' at {worst:.4f}; "
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
