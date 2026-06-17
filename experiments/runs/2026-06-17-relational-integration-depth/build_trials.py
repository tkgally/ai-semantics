#!/usr/bin/env python3
"""build_trials.py (no API) -- the frozen INTEGRATION-UNDER-LOAD stimuli (burial depth 2).

Two independent balanced-block rosters over a 64-figure space (4 shapes x 4 patterns x 4 colors).
A block is a 2x2x2 sub-grid {s_a,s_b} x {p_a,p_b} x {c_a,c_b} -> 8 present figures. Within a block,
K=8 records cycle the integration TARGET through all 8 present figures once, under a Latin square
that also cycles the target's physical grid slot through all 8 slots once.

  INTEG  : N_BLOCKS_INTEG blocks x K records -> 48 records/model. query = "INTEG" (no instruction
           to combine). The TARGET = the unique figure matching the EARLIEST SHAPE constraint AND
           the MIDDLE PATTERN constraint AND the LATEST COLOR constraint. The headline.
  DIRECT : N_BLOCKS_DIRECT blocks x K records -> 32 records/model. Same stimuli; the query
           explicitly restates all three constraints and asks for the figure (on-demand gate).

For each record with target (sT,pT,cT) in block {s_a,s_b}x{p_a,p_b}x{c_a,c_b}:
  earliest turn (lowest stamp)  : "DAX was a {sT}"  -> matches the 4 figures with shape sT
  middle   turn (middle stamp)  : "DAX was {pT}"    -> matches the 4 figures with pattern pT
  latest   turn (highest stamp) : "DAX was {cT}"    -> matches the 4 figures with color cT
  TARGET = (sT,pT,cT) (unique all-three-match).
  The three "one-attribute-flipped" twins are the diagnostic distractors:
    twin_shape   = differs only in shape   (matches pattern+color) = the RECENT-TWO (drop-earliest) pick
    twin_pattern = differs only in pattern (matches shape+color)
    twin_color   = differs only in color   (matches shape+pattern)

Shortcut bounds asserted EMPIRICALLY before freeze, SEPARATELY per subset (re-derivable by the
independent pre-run critic):
  - every constant-grid-slot follower scores exactly 1/K = 0.125 (target slot uniform, Latin square);
  - within each block the TARGET is uniform over the 8 present figures => every fixed figure-
    IDENTITY preference scores exactly 1/K (analytic; spot-checked over all 64 constant-figure
    pickers present + 20000 random full orderings);
  - every SINGLE-attribute reader (shape-only / pattern-only / color-only=overwrite), under each of
    four tie-breaks, scores <= SINGLE_ATTR_CEILING = 0.25 (each single constraint matches exactly 4
    present figures incl. the target);
  - every TWO-attribute reader (drop ONE turn: {pattern,color}=recent-two/drop-earliest;
    {shape,color}; {shape,pattern}), under each of four tie-breaks, scores <= TWO_ATTR_CEILING =
    0.50 (each pair matches exactly 2 present figures incl. the target);
  - each present figure appears once (frequency flat); 8 distinct figures & 3 distinct rounds with
    earliest(shape) < middle(pattern) < latest(color) stamps.
So ONLY conjoining ALL THREE turns (incl. the buried earliest shape) can clear the 0.50 bar. The
distractor-slot placement is SEARCHED (deterministic seed offsets off SEED0) so the slot tie-breaks
land at their analytic values. Prints the sha256 that must go into PREREG.md.
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

ALL_FIGS = [(s, p, c) for s in C.SHAPES for p in C.PATTERNS for c in C.COLORS]  # 64 canonical
FIG_KEY = {f: i for i, f in enumerate(ALL_FIGS)}                                # stable pool index

# the two-attribute readers that DROP exactly one turn (the load-bearing alternatives):
#   drop earliest shape -> keep {pattern,color} (RECENT-TWO); drop middle pattern -> keep {shape,color};
#   drop latest color   -> keep {shape,pattern}.
TWO_ATTR_KEEP = [("pattern", "color"), ("shape", "color"), ("shape", "pattern")]
ONE_ATTR_KEEP = [("shape",), ("pattern",), ("color",)]


def balanced_blocks(rng, n_blocks):
    """n_blocks distinct (shape-pair, pattern-pair, color-pair) 2x2x2 grids with each shape, each
    pattern and each color used in exactly 2*n_blocks/4 blocks (each block carries 2 of each)."""
    for axis in (C.SHAPES, C.PATTERNS, C.COLORS):
        if (2 * n_blocks) % len(axis) != 0:
            raise ValueError("2*n_blocks must be divisible by each axis length")
    s_t = 2 * n_blocks // len(C.SHAPES)
    p_t = 2 * n_blocks // len(C.PATTERNS)
    c_t = 2 * n_blocks // len(C.COLORS)
    shape_pairs = list(itertools.combinations(C.SHAPES, 2))
    pat_pairs = list(itertools.combinations(C.PATTERNS, 2))
    col_pairs = list(itertools.combinations(C.COLORS, 2))
    cand = [(sp, pp, cp) for sp in shape_pairs for pp in pat_pairs for cp in col_pairs]  # 6*6*6
    for _ in range(400000):
        rng.shuffle(cand)
        blocks, scnt, pcnt, ccnt = [], Counter(), Counter(), Counter()
        seen = set()
        for sp, pp, cp in cand:
            if len(blocks) == n_blocks:
                break
            if (sp, pp, cp) in seen:
                continue
            if (any(scnt[s] >= s_t for s in sp) or any(pcnt[p] >= p_t for p in pp)
                    or any(ccnt[c] >= c_t for c in cp)):
                continue
            blocks.append((sp, pp, cp))
            seen.add((sp, pp, cp))
            scnt.update(sp)
            pcnt.update(pp)
            ccnt.update(cp)
        if (len(blocks) == n_blocks
                and all(scnt[s] == s_t for s in C.SHAPES)
                and all(pcnt[p] == p_t for p in C.PATTERNS)
                and all(ccnt[c] == c_t for c in C.COLORS)):
            return blocks
        rng.seed(rng.random())
    raise RuntimeError("could not build balanced blocks")


def _attrs(fig):
    return {"shape": fig[0], "pattern": fig[1], "color": fig[2]}


def _build_subset_once(blocks, query, rid_start, place_rng):
    records, rid = [], rid_start
    for bi, (sp, pp, cp) in enumerate(blocks):
        block_figs = [(s, p, c) for s in sp for p in pp for c in cp]   # canonical 2x2x2 order, 8
        for j in range(C.K):
            target = block_figs[j]                          # cycles all 8 members across the block
            target_pos = (j + bi) % C.K                     # cycles all 8 grid slots across block
            sT, pT, cT = target
            triple = C.ROUND_TRIPLES[rid % len(C.ROUND_TRIPLES)]
            r_shape, r_pattern, r_color = triple[0], triple[1], triple[2]  # earliest<mid<latest
            others = [f for f in block_figs if f != target]
            place_rng.shuffle(others)                        # randomize distractor slot fill
            display = [None] * C.K
            display[target_pos] = target
            slot = 0
            for f in others:
                while display[slot] is not None:
                    slot += 1
                display[slot] = f
            disp = [{"label": f"G{i+1}", "shape": f[0], "pattern": f[1], "color": f[2]}
                    for i, f in enumerate(display)]
            target_label = disp[target_pos]["label"]
            # diagnostic one-attribute-flipped twins
            twin = {}
            for d in disp:
                fa = (d["shape"], d["pattern"], d["color"])
                if fa == target:
                    continue
                diff = [a for a in ("shape", "pattern", "color")
                        if _attrs(fig=fa)[a] != _attrs(fig=target)[a]]
                if len(diff) == 1:
                    twin[diff[0]] = d["label"]
            hist = [{"round": r_shape, "kind": "shape", "value": sT},
                    {"round": r_pattern, "kind": "pattern", "value": pT},
                    {"round": r_color, "kind": "color", "value": cT}]
            hist_display = hist[:]
            place_rng.shuffle(hist_display)
            records.append({
                "rid": rid, "subset": query.lower(), "block": f"{query[:3]}{bi}", "query": query,
                "present": [d["label"] for d in disp],
                "display": disp, "hist_display": hist_display,
                "shape": sT, "pattern": pT, "color": cT,
                "r_shape": r_shape, "r_pattern": r_pattern, "r_color": r_color,
                "fig_key": FIG_KEY[target],
                "correct_label": target_label,                 # integration target (all three)
                "twin_shape_label": twin.get("shape"),          # RECENT-TWO (drop earliest) pick
                "twin_pattern_label": twin.get("pattern"),
                "twin_color_label": twin.get("color"),
                "target_pos": target_pos,
                "last_pos_label": disp[-1]["label"],
                "first_pos_label": disp[0]["label"],
            })
            rid += 1
    return records


def _reader_acc(records, keep, tiebreak):
    """reader that keeps ONLY the target's values of the attributes in `keep` (tuple), narrows to
    the present figures matching ALL of them, then breaks the tie by `tiebreak`. acc = P(pick==
    target). keep size 1 -> single-attr (4 cands); size 2 -> two-attr (2 cands)."""
    n = 0
    for r in records:
        cands = [(i, d) for i, d in enumerate(r["display"])
                 if all(d[a] == r[a] for a in keep)]
        exp = {1: 4, 2: 2, 3: 1}[len(keep)]
        assert len(cands) == exp, f"keep={keep} expected {exp} cands, got {len(cands)}"
        if tiebreak == "slot_lo":
            pick = min(cands, key=lambda t: t[0])[1]
        elif tiebreak == "slot_hi":
            pick = max(cands, key=lambda t: t[0])[1]
        elif tiebreak == "key_lo":
            pick = min(cands, key=lambda t: FIG_KEY[(t[1]["shape"], t[1]["pattern"], t[1]["color"])])[1]
        else:
            pick = max(cands, key=lambda t: FIG_KEY[(t[1]["shape"], t[1]["pattern"], t[1]["color"])])[1]
        n += 1 if pick["label"] == r["correct_label"] else 0
    return n / len(records)


def build_subset(rng, n_blocks, query, rid_start):
    """Build a subset, then SEARCH the distractor placement (deterministic seed offsets off SEED0)
    until every TWO-attribute reader's slot_lo tie-break == exactly 0.50 (so slot_hi == 0.50 too,
    they sum to 1) AND every single-attribute reader <= 0.25 under all four tie-breaks. The
    target_pos Latin square already pins the grid-position follower to exactly 1/K independently of
    placement. Reproducible: the accepted offset is the smallest that balances."""
    blocks = balanced_blocks(rng, n_blocks)
    for off in range(400000):
        place_rng = random.Random(C.SEED0 + 100000 + off + (0 if query == "INTEG" else 50))
        records = _build_subset_once(blocks, query, rid_start, place_rng)
        ok = all(abs(_reader_acc(records, keep, "slot_lo") - 0.5) < 1e-9 for keep in TWO_ATTR_KEEP)
        if ok:
            ok1 = all(_reader_acc(records, keep, tb) <= C.SINGLE_ATTR_CEILING + 1e-9
                      for keep in ONE_ATTR_KEEP
                      for tb in ("slot_lo", "slot_hi", "key_lo", "key_hi"))
            if ok1:
                return records, off
    raise RuntimeError(f"{query}: could not balance tie-breaks")


def build():
    rng = random.Random(C.SEED0)
    integ, off_i = build_subset(rng, C.N_BLOCKS_INTEG, "INTEG", 0)
    direct, off_d = build_subset(rng, C.N_BLOCKS_DIRECT, "DIRECT", len(integ))
    print(f"  accepted placement offsets: INTEG={off_i}, DIRECT={off_d}")
    return integ + direct


def _slot_acc(records, slot):
    return sum(1 for r in records
               if r["display"][slot]["label"] == r["correct_label"]) / len(records)


def _const_fig_acc(records, fig):
    n = 0
    for r in records:
        present = {(d["shape"], d["pattern"], d["color"]): d["label"] for d in r["display"]}
        if fig in present:
            n += 1 if present[fig] == r["correct_label"] else 0
    return n / len(records)


def _worst_pref_sample(records, rng, n_samp=20000):
    worst = 0.0
    figs = ALL_FIGS[:]
    for _ in range(n_samp):
        rng.shuffle(figs)
        rank = {f: i for i, f in enumerate(figs)}
        c = 0
        for r in records:
            present = [(d["shape"], d["pattern"], d["color"]) for d in r["display"]]
            top = min(present, key=lambda f: rank[f])
            lab = {(d["shape"], d["pattern"], d["color"]): d["label"] for d in r["display"]}[top]
            c += 1 if lab == r["correct_label"] else 0
        worst = max(worst, c / len(records))
    return worst


def assert_balance(records):
    rng = random.Random(C.SEED0 + 1)
    for subset in ("integ", "direct"):
        rs = [r for r in records if r["subset"] == subset]
        n = len(rs)
        assert n > 0, f"{subset}: empty"
        # 1) target grid slot uniform => position-follower = 1/K
        pos = Counter(r["target_pos"] for r in rs)
        assert set(pos) == set(range(C.K)) and len(set(pos.values())) == 1, \
            f"{subset}: target_pos not balanced: {dict(pos)}"
        for slot in range(C.K):
            acc = _slot_acc(rs, slot)
            assert abs(acc - C.POS_CHANCE) < 1e-9, f"{subset} slot-{slot} follower acc {acc} != 1/K"
        # 2) within each block the target is UNIFORM over the 8 present figures
        by_block = {}
        for r in rs:
            by_block.setdefault(r["block"], []).append(r)
        for bi, brs in by_block.items():
            assert len(brs) == C.K, f"{subset} block {bi}: {len(brs)} records (expected {C.K})"
            corrects = Counter(r["correct_label"] for r in brs)
            assert set(corrects.values()) == {1}, \
                f"{subset} block {bi}: target not uniform over present figs: {dict(corrects)}"
        # 2b) figure-identity preference: constant-figure pickers + random orderings <= 1/K
        for fig in ALL_FIGS:
            acc = _const_fig_acc(rs, fig)
            assert acc <= C.POS_CHANCE + 1e-9, f"{subset} const-fig {fig} acc {acc} > 1/K"
        worst_pref = _worst_pref_sample(rs, rng)
        assert worst_pref <= C.POS_CHANCE + 1e-9, \
            f"{subset}: best sampled figure-preference ordering {worst_pref:.4f} > 1/K (leak!)"
        # 3) single-attribute readers <= 0.25 under every tie-break
        one_scores = {}
        for keep in ONE_ATTR_KEEP:
            for tb in ("slot_lo", "slot_hi", "key_lo", "key_hi"):
                a = _reader_acc(rs, keep, tb)
                one_scores[f"{keep[0]}/{tb}"] = round(a, 4)
                assert a <= C.SINGLE_ATTR_CEILING + 1e-9, \
                    f"{subset} single-attr {keep}/{tb} acc {a} > SINGLE_ATTR_CEILING"
        # 4) two-attribute (drop-one-turn) readers <= 0.50 under every tie-break
        two_scores = {}
        for keep in TWO_ATTR_KEEP:
            for tb in ("slot_lo", "slot_hi", "key_lo", "key_hi"):
                a = _reader_acc(rs, keep, tb)
                two_scores["+".join(keep) + "/" + tb] = round(a, 4)
                assert a <= C.TWO_ATTR_CEILING + 1e-9, \
                    f"{subset} two-attr {keep}/{tb} acc {a} > TWO_ATTR_CEILING"
        # 4b) full integrator (all three) = 1.000 (sanity)
        full = _reader_acc(rs, ("shape", "pattern", "color"), "slot_lo")
        assert abs(full - 1.0) < 1e-9, f"{subset}: full integrator acc {full} != 1.0"
        # 5) structural: distinct figures; twins present; 3 distinct rounds; earliest<mid<latest
        for r in rs:
            figs = [(d["shape"], d["pattern"], d["color"]) for d in r["display"]]
            assert len(set(figs)) == C.K, f"{subset} rid {r['rid']}: figures not distinct"
            assert r["twin_shape_label"] and r["twin_pattern_label"] and r["twin_color_label"], \
                f"{subset} rid {r['rid']}: twin structure broken"
            assert r["r_shape"] < r["r_pattern"] < r["r_color"], \
                f"{subset} rid {r['rid']}: stamps not earliest(shape)<mid(pattern)<latest(color)"
            both = [d["label"] for d in r["display"] if d["shape"] == r["shape"]
                    and d["pattern"] == r["pattern"] and d["color"] == r["color"]]
            assert both == [r["correct_label"]], f"{subset} rid {r['rid']}: all-three not unique"
        print(f"  [{subset}] geometry OK: {n} records ({len(by_block)} blocks x {C.K}); "
              f"slot-follower={C.POS_CHANCE:.3f}; best fig-pref(sampled)={worst_pref:.3f} (<=1/K); "
              f"single-attr max={max(one_scores.values()):.3f} (<={C.SINGLE_ATTR_CEILING}); "
              f"two-attr max={max(two_scores.values()):.3f} (<={C.TWO_ATTR_CEILING}); "
              f"full-integrator={full:.3f}; freq flat.")
        print(f"      single-attr readers: {one_scores}")
        print(f"      two-attr (drop-one-turn) readers: {two_scores}")
    ig = [r for r in records if r["subset"] == "integ"]
    di = [r for r in records if r["subset"] == "direct"]
    print(f"  totals: {len(ig)} INTEG + {len(di)} DIRECT = {len(records)} records/model; "
          f"{len(records) * len(C.MODELS)} finding-bearing calls. Only conjoining ALL THREE turns "
          f"(incl. the buried earliest SHAPE) clears the {C.TWO_ATTR_CEILING} bar.")


def main():
    records = build()
    assert_balance(records)
    blob = json.dumps({"records": records, "k": C.K, "term": C.TERM,
                       "shapes": C.SHAPES, "patterns": C.PATTERNS, "colors": C.COLORS,
                       "n_blocks_integ": C.N_BLOCKS_INTEG, "n_blocks_direct": C.N_BLOCKS_DIRECT,
                       "single_attr_ceiling": C.SINGLE_ATTR_CEILING,
                       "two_attr_ceiling": C.TWO_ATTR_CEILING, "direct_floor": C.DIRECT_FLOOR,
                       "pos_chance": C.POS_CHANCE, "seed0": C.SEED0},
                      indent=2, sort_keys=True)
    open(OUT, "w").write(blob + "\n")
    sha = hashlib.sha256(blob.encode()).hexdigest()
    print(f"  wrote {OUT}")
    print(f"  stimuli.json sha256 = {sha}")
    print("  -> put this sha256 in PREREG.md before any finding-bearing call")


if __name__ == "__main__":
    main()
