#!/usr/bin/env python3
"""build_figures.py — deterministic abstract "tangram-like" referent figures.

WHY TEXT GRIDS (operationalization, surfaced in decisions/open/relational-pilot-operationalization)
---------------------------------------------------------------------------------------------------
The pilot needs HARD-TO-NAME referents presented BYTE-IDENTICALLY to every agent and across
the live / ordered-replay / shuffled-replay conditions (the shuffle control demands the prior
turns be reorderable as exact text). Image input would (a) balloon the per-call token cost on a
deliberately call-heavy iterated probe and (b) complicate exact content-holding. So v1 renders
each referent as an 8x8 grid of '#'/'.'. Two design pressures are built in:
  - HARD TO NAME: organic random-accretion blobs, no conventional single-word label, so agents
    must coin and compress a holistic/figurative label (the tangram dynamic) rather than read off
    a name. A director WORD BUDGET (enforced in game.py, not here) blocks exhaustive cell-listing,
    forcing the holistic label the entrainment curve needs.
  - CONFUSABLE: the 6 figures form 3 near-twin PAIRS (a base blob + a few-cell perturbation). A
    holistic label is therefore ambiguous WITHIN a pair, so which figure a coined term settles on
    can in principle depend on the interaction trajectory -- giving the live-vs-shuffled contrast
    something to detect if relational constitution is real (and a clean null if it is not).

Deterministic: fixed SEED -> identical figures every run. The frozen artifact is figures.json
(canonical ids F0..F5 + grids) with its sha256 printed; PREREG.md pins that hash before any
finding-bearing model call.

Pure stdlib.
"""
import hashlib
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
SIZE = 8
SEED = 20260531          # frozen
N_PAIRS = 3              # -> 6 figures
BLOB_CELLS = 19          # filled cells per base blob (of 64)
TWIN_FLIPS = 4           # cells changed to make a near-twin (confusable within pair)


def grow_blob(rng, n_cells):
    """Random-accretion contiguous blob: start centre-ish, repeatedly add a cell
    adjacent to the current shape. Yields organic, hard-to-name forms."""
    start = (rng.randint(2, 5), rng.randint(2, 5))
    shape = {start}
    while len(shape) < n_cells:
        frontier = []
        for (r, c) in shape:
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < SIZE and 0 <= nc < SIZE and (nr, nc) not in shape:
                    frontier.append((nr, nc))
        if not frontier:
            break
        shape.add(rng.choice(frontier))
    return shape


def make_twin(rng, shape):
    """A confusable near-twin: flip TWIN_FLIPS cells (remove some filled border
    cells, add some adjacent empty cells), keeping it contiguous-ish and same-ish size."""
    shape = set(shape)
    for _ in range(TWIN_FLIPS):
        if rng.random() < 0.5 and len(shape) > BLOB_CELLS - 3:
            # remove a removable (non-cut-ish) border cell
            border = [cell for cell in shape]
            shape.discard(rng.choice(border))
        else:
            frontier = []
            for (r, c) in shape:
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < SIZE and 0 <= nc < SIZE and (nr, nc) not in shape:
                        frontier.append((nr, nc))
            if frontier:
                shape.add(rng.choice(frontier))
    return shape


def render(shape):
    return ["".join("#" if (r, c) in shape else "." for c in range(SIZE))
            for r in range(SIZE)]


def hamming(a, b):
    return len(set(a) ^ set(b))


def main():
    rng = random.Random(SEED)
    figures = {}
    shapes = {}
    fid = 0
    for p in range(N_PAIRS):
        base = grow_blob(rng, BLOB_CELLS)
        twin = make_twin(rng, base)
        for shape in (base, twin):
            cid = f"F{fid}"
            figures[cid] = {"id": cid, "pair": p, "grid": render(shape)}
            shapes[cid] = shape
            fid += 1

    payload = {"size": SIZE, "seed": SEED, "n_figures": len(figures),
               "note": "abstract hard-to-name referents; 3 confusable near-twin pairs (pair field)",
               "figures": figures}
    blob = json.dumps(payload, indent=2, sort_keys=True)
    out = os.path.join(HERE, "figures.json")
    with open(out, "w") as f:
        f.write(blob + "\n")
    sha = hashlib.sha256(blob.encode()).hexdigest()

    # human-readable preview + a confusability report
    print(f"wrote {out}\nsha256({os.path.basename(out)} content)= {sha}\n")
    ids = list(figures)
    for cid in ids:
        fill = sum(row.count("#") for row in figures[cid]["grid"])
        print(f"{cid} (pair {figures[cid]['pair']}, {fill} cells):")
        for row in figures[cid]["grid"]:
            print("   " + row)
        print()
    print("pairwise Hamming distance (cells differing); within-pair twins should be SMALL,")
    print("cross-pair should be LARGER (confusable twins, distinct themes):")
    print("     " + "  ".join(ids))
    for a in ids:
        row = []
        for b in ids:
            row.append(f"{hamming(shapes[a], shapes[b]):2d}")
        print(f"{a}  " + "  ".join(row))


if __name__ == "__main__":
    main()
