#!/usr/bin/env python3
"""build_trials.py (no API) — the frozen RUNG-(ii) INTEGRATION stimuli.

Two independent balanced-block rosters over a 16-figure space (4 shapes x 4 patterns). A block is
a 2x2 sub-grid {s_a, s_b} x {p_a, p_b} -> 4 present figures. Within a block, K=4 records cycle the
integration TARGET through all 4 present figures once, under a Latin square that also cycles the
target's physical grid slot through all 4 slots once.

  INTEG  : N_BLOCKS_INTEG blocks x K records -> 48 records/model. query = "INTEG" (no instruction
           to combine). The TARGET = the unique figure matching BOTH the earlier SHAPE constraint
           and the latest PATTERN constraint. The headline.
  DIRECT : N_BLOCKS_DIRECT blocks x K records -> 32 records/model. Same stimuli; the query
           explicitly restates both constraints and asks for the figure (on-demand conjunction gate).

For each record with target (sT, pT) in block {s_a,s_b} x {p_a,p_b}:
  earlier turn (low stamp)  : "DAX was a {sT}"   -> matches {(sT,p_a),(sT,p_b)} (2 figures)
  latest  turn (high stamp) : "DAX was {pT}"     -> matches {(s_a,pT),(s_b,pT)} (2 figures)
  TARGET = (sT,pT) (unique both-match); distractors = the shape-only, the pattern-only, the neither.

Shortcut bounds asserted EMPIRICALLY before freeze, SEPARATELY per subset:
  - every constant-grid-slot follower scores exactly 1/K = 0.25;
  - within each block the TARGET is uniform over the 4 present figures => every fixed figure-
    IDENTITY preference scores exactly 1/K (analytic; spot-checked over all 16 constant-figure
    pickers + 20000 random full orderings);
  - every concrete SINGLE-attribute reader (latest-pattern-only = overwrite; earlier-shape-only),
    under each of four tie-breaks, scores <= OVERWRITE_CEILING = 0.50 (each constraint matches
    exactly 2 present figures incl. the target);
  - each present figure appears once (frequency flat); 4 distinct figures & 2 distinct rounds.
So only conjoining the LATEST and the EARLIER turn (integration) can clear the 0.50 bar. Prints the
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

ALL_FIGS = [(s, p) for s in C.SHAPES for p in C.PATTERNS]   # 16 canonical figures
FIG_KEY = {f: i for i, f in enumerate(ALL_FIGS)}            # stable pool index per figure


def balanced_blocks(rng, n_blocks):
    """n_blocks distinct (shape-pair, pattern-pair) 2x2 grids with each shape in exactly
    n_blocks/2 blocks and each pattern in exactly n_blocks/2 blocks (each block carries 2 shapes
    + 2 patterns). Aims (not required) to keep #blocks-per-figure uniform too."""
    if (2 * n_blocks) % len(C.SHAPES) != 0 or (2 * n_blocks) % len(C.PATTERNS) != 0:
        raise ValueError("2*n_blocks must be divisible by |shapes| and |patterns|")
    s_target = 2 * n_blocks // len(C.SHAPES)
    p_target = 2 * n_blocks // len(C.PATTERNS)
    shape_pairs = list(itertools.combinations(C.SHAPES, 2))
    pat_pairs = list(itertools.combinations(C.PATTERNS, 2))
    cand = [(sp, pp) for sp in shape_pairs for pp in pat_pairs]   # 6 x 6 = 36
    for _ in range(400000):
        rng.shuffle(cand)
        blocks, scnt, pcnt = [], Counter(), Counter()
        for sp, pp in cand:
            if len(blocks) == n_blocks:
                break
            if any(scnt[s] >= s_target for s in sp) or any(pcnt[p] >= p_target for p in pp):
                continue
            blocks.append((sp, pp))
            scnt.update(sp)
            pcnt.update(pp)
        if (len(blocks) == n_blocks and all(scnt[s] == s_target for s in C.SHAPES)
                and all(pcnt[p] == p_target for p in C.PATTERNS)):
            return blocks
        rng.seed(rng.random())
    raise RuntimeError("could not build balanced blocks")


def _build_subset_once(blocks, query, rid_start, place_rng):
    records, rid = [], rid_start
    for bi, (sp, pp) in enumerate(blocks):
        block_figs = [(s, p) for s in sp for p in pp]      # canonical 2x2 order, 4 figures
        for j in range(C.K):
            target = block_figs[j]                          # cycles all 4 members across the block
            target_pos = (j + bi) % C.K                     # cycles all 4 grid slots across block
            sT, pT = target
            pair = C.ROUND_PAIRS[rid % len(C.ROUND_PAIRS)]
            r_lo, r_hi = pair[0], pair[1]                   # earlier=shape, latest=pattern
            others = [f for f in block_figs if f != target]
            place_rng.shuffle(others)                        # randomize distractor slot fill
            display = [None] * C.K
            display[target_pos] = target
            slot = 0
            for f in others:
                while display[slot] is not None:
                    slot += 1
                display[slot] = f
            disp = [{"label": f"G{i+1}", "shape": f[0], "pattern": f[1]}
                    for i, f in enumerate(display)]
            target_label = disp[target_pos]["label"]
            # classify the three distractors
            latest_only = pattern_only = earlier_only = shape_only = neither = None
            for d in disp:
                if d["label"] == target_label:
                    continue
                sm, pm = (d["shape"] == sT), (d["pattern"] == pT)
                if pm and not sm:
                    pattern_only = d["label"]   # latest-only (overwrite) distractor
                elif sm and not pm:
                    shape_only = d["label"]      # earlier-only distractor
                else:
                    neither = d["label"]
            # history display order randomized (shape line / pattern line)
            hist = [{"round": r_lo, "kind": "shape", "value": sT},
                    {"round": r_hi, "kind": "pattern", "value": pT}]
            hist_display = hist[:]
            place_rng.shuffle(hist_display)
            records.append({
                "rid": rid, "subset": query.lower(), "block": f"{query[:3]}{bi}", "query": query,
                "present": [d["label"] for d in disp],
                "display": disp, "hist_display": hist_display,
                "shape": sT, "pattern": pT, "r_lo": r_lo, "r_hi": r_hi,
                "fig_key": FIG_KEY[target],
                "correct_label": target_label,           # integration target (both-match)
                "latest_only_label": pattern_only,        # overwrite "other pattern-match"
                "earlier_only_label": shape_only,         # earlier "other shape-match"
                "neither_label": neither,
                "target_pos": target_pos,
                "last_pos_label": disp[-1]["label"],
                "first_pos_label": disp[0]["label"],
            })
            rid += 1
    return records


def build_subset(rng, n_blocks, query, rid_start):
    """Build a subset, then SEARCH the distractor placement (deterministic seed offsets off SEED0)
    until BOTH single-attribute slot tie-breaks score EXACTLY 0.50 -- i.e. the target is the lower
    grid slot of its pattern-pair in exactly half the records, and of its shape-pair in half. This
    removes the only placement-dependent slot leak (the target_pos Latin square already pins the
    grid-position follower to exactly 1/K independently of placement; the pool-index tie-breaks are
    structurally 0.50 already). Reproducible: the accepted offset is the smallest that balances."""
    blocks = balanced_blocks(rng, n_blocks)
    for off in range(200000):
        place_rng = random.Random(C.SEED0 + 100000 + off + (0 if query == "INTEG" else 50))
        records = _build_subset_once(blocks, query, rid_start, place_rng)
        if (abs(_attr_only_acc(records, "pattern", "slot_lo") - 0.5) < 1e-9
                and abs(_attr_only_acc(records, "shape", "slot_lo") - 0.5) < 1e-9):
            return records
    raise RuntimeError(f"{query}: could not balance slot tie-breaks")


def build():
    rng = random.Random(C.SEED0)
    integ = build_subset(rng, C.N_BLOCKS_INTEG, "INTEG", 0)
    direct = build_subset(rng, C.N_BLOCKS_DIRECT, "DIRECT", len(integ))
    return integ + direct


def _slot_acc(records, slot):
    return sum(1 for r in records
               if r["display"][slot]["label"] == r["correct_label"]) / len(records)


def _const_fig_acc(records, fig):
    """'always pick figure `fig` (by description) when present' picker accuracy."""
    n = 0
    for r in records:
        present = {(d["shape"], d["pattern"]): d["label"] for d in r["display"]}
        if fig in present:
            n += 1 if present[fig] == r["correct_label"] else 0
    return n / len(records)


def _worst_pref_sample(records, rng, n_samp=20000):
    """worst (best-for-attacker) full figure-IDENTITY preference ordering over a random sample."""
    worst = 0.0
    figs = ALL_FIGS[:]
    for _ in range(n_samp):
        rng.shuffle(figs)
        rank = {f: i for i, f in enumerate(figs)}
        c = 0
        for r in records:
            present = [(d["shape"], d["pattern"]) for d in r["display"]]
            top = min(present, key=lambda f: rank[f])
            lab = {(d["shape"], d["pattern"]): d["label"] for d in r["display"]}[top]
            c += 1 if lab == r["correct_label"] else 0
        worst = max(worst, c / len(records))
    return worst


def _attr_only_acc(records, attr, tiebreak):
    """single-attribute reader: keep ONLY `attr` (pattern=latest/overwrite or shape=earlier),
    narrow to the (exactly 2) present figures matching the target's value of that attr, then break
    the tie by `tiebreak` in {slot_lo, slot_hi, key_lo, key_hi}. Accuracy = P(pick == target)."""
    n = 0
    for r in records:
        tv = r[attr]                                   # target's value of this attribute
        cands = [(i, d) for i, d in enumerate(r["display"]) if d[attr] == tv]
        assert len(cands) == 2, f"attr {attr} not 2-way: {len(cands)}"
        if tiebreak == "slot_lo":
            pick = min(cands, key=lambda t: t[0])[1]
        elif tiebreak == "slot_hi":
            pick = max(cands, key=lambda t: t[0])[1]
        elif tiebreak == "key_lo":
            pick = min(cands, key=lambda t: FIG_KEY[(t[1]["shape"], t[1]["pattern"])])[1]
        else:
            pick = max(cands, key=lambda t: FIG_KEY[(t[1]["shape"], t[1]["pattern"])])[1]
        n += 1 if pick["label"] == r["correct_label"] else 0
    return n / len(records)


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
        # 2) within each block the target is UNIFORM over the 4 present figures
        by_block = {}
        for r in rs:
            by_block.setdefault(r["block"], []).append(r)
        for bi, brs in by_block.items():
            assert len(brs) == C.K, f"{subset} block {bi}: {len(brs)} records (expected {C.K})"
            corrects = Counter(r["correct_label"] for r in brs)
            assert set(corrects.values()) == {1}, \
                f"{subset} block {bi}: target not uniform over present figs: {dict(corrects)}"
        # 2b) figure-identity preference: 16 constant-figure pickers + random orderings <= 1/K
        for fig in ALL_FIGS:
            acc = _const_fig_acc(rs, fig)
            assert acc <= C.POS_CHANCE + 1e-9, f"{subset} const-fig {fig} acc {acc} > 1/K"
        worst_pref = _worst_pref_sample(rs, rng)
        assert worst_pref <= C.POS_CHANCE + 1e-9, \
            f"{subset}: best sampled figure-preference ordering {worst_pref:.4f} > 1/K (leak!)"
        # 3) single-attribute (overwrite / earlier-only) readers <= 0.50 under every tie-break
        attr_scores = {}
        for attr in ("pattern", "shape"):
            for tb in ("slot_lo", "slot_hi", "key_lo", "key_hi"):
                a = _attr_only_acc(rs, attr, tb)
                attr_scores[f"{attr}/{tb}"] = round(a, 4)
                assert a <= C.OVERWRITE_CEILING + 1e-9, \
                    f"{subset} single-attr {attr}/{tb} acc {a} > OVERWRITE_CEILING"
        # 4) structural: exactly one both-match (target), one pattern-only, one shape-only, one
        #    neither; 4 distinct figures; 2 distinct rounds; latest(pattern) round > earlier(shape)
        for r in rs:
            figs = [(d["shape"], d["pattern"]) for d in r["display"]]
            assert len(set(figs)) == C.K, f"{subset} rid {r['rid']}: figures not distinct"
            assert r["latest_only_label"] and r["earlier_only_label"] and r["neither_label"], \
                f"{subset} rid {r['rid']}: distractor structure broken"
            labs = {r["correct_label"], r["latest_only_label"], r["earlier_only_label"],
                    r["neither_label"]}
            assert labs == set(r["present"]), f"{subset} rid {r['rid']}: label partition broken"
            assert r["r_hi"] > r["r_lo"], f"{subset} rid {r['rid']}: latest not after earlier"
            # the target is the unique present figure with target's shape AND target's pattern
            both = [d["label"] for d in r["display"]
                    if d["shape"] == r["shape"] and d["pattern"] == r["pattern"]]
            assert both == [r["correct_label"]], f"{subset} rid {r['rid']}: both-match not unique"
        print(f"  [{subset}] geometry OK: {n} records ({len(by_block)} blocks x {C.K}); "
              f"slot-follower={C.POS_CHANCE:.3f}; best fig-pref(sampled)={worst_pref:.3f} (<=1/K); "
              f"single-attr max={max(attr_scores.values()):.3f} (<={C.OVERWRITE_CEILING}); freq flat.")
        print(f"      single-attr readers: {attr_scores}")
    ig = [r for r in records if r["subset"] == "integ"]
    di = [r for r in records if r["subset"] == "direct"]
    print(f"  totals: {len(ig)} INTEG + {len(di)} DIRECT = {len(records)} records/model; "
          f"{len(records) * len(C.MODELS)} finding-bearing calls. Only conjoining the earlier "
          f"(shape) AND latest (pattern) turn clears the {C.OVERWRITE_CEILING} integration bar.")


def main():
    records = build()
    assert_balance(records)
    blob = json.dumps({"records": records, "k": C.K, "term": C.TERM,
                       "shapes": C.SHAPES, "patterns": C.PATTERNS,
                       "n_blocks_integ": C.N_BLOCKS_INTEG, "n_blocks_direct": C.N_BLOCKS_DIRECT,
                       "overwrite_ceiling": C.OVERWRITE_CEILING, "direct_floor": C.DIRECT_FLOOR,
                       "pos_chance": C.POS_CHANCE, "seed0": C.SEED0},
                      indent=2, sort_keys=True)
    open(OUT, "w").write(blob + "\n")
    sha = hashlib.sha256(blob.encode()).hexdigest()
    print(f"  wrote {OUT}")
    print(f"  stimuli.json sha256 = {sha}")
    print("  -> put this sha256 in PREREG.md before any finding-bearing call")


if __name__ == "__main__":
    main()
