#!/usr/bin/env python3
"""Score the VWSD grounding-headroom probe per the frozen design.

Reads raw/text.json (frozen covariate), raw/image.json, raw/distract.json. Reports, in the
order the design mandates:
  0. parse integrity per arm
  1. DISTRACT null FIRST (word-ablated gold-selection rate vs chance 0.10)
  2. main accuracy per arm per model
  3. per-item separability sep_i distribution + strata counts (mod-1 floor check, >=8/bin)
  4. test of record: image-rescue rate in text-failed vs text-succeeded cells (+ Spearman/OLS
     slope of Δ_i on sep_i as a descriptive companion, with the ceiling caveat)
Pure stdlib; no model calls.
"""
import json, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
MODELS = ["claude", "gpt", "gemini"]
CHANCE = 0.10

def load(arm):
    p = os.path.join(HERE, "raw", f"{arm}.json")
    return json.load(open(p)) if os.path.exists(p) else None

def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0, 0.0)
    p = k / n
    d = 1 + z*z/n
    c = p + z*z/(2*n)
    h = z*((p*(1-p)/n + z*z/(4*n*n))**0.5)
    return (p, (c-h)/d, (c+h)/d)

def spearman(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    def rank(v):
        s = sorted(range(n), key=lambda i: v[i])
        r = [0.0]*n
        i = 0
        while i < n:
            j = i
            while j < n and v[s[j]] == v[s[i]]:
                j += 1
            avg = (i + j - 1) / 2.0 + 1
            for k in range(i, j):
                r[s[k]] = avg
            i = j
        return r
    rx, ry = rank(xs), rank(ys)
    mx, my = sum(rx)/n, sum(ry)/n
    num = sum((rx[i]-mx)*(ry[i]-my) for i in range(n))
    den = (sum((rx[i]-mx)**2 for i in range(n)) * sum((ry[i]-my)**2 for i in range(n)))**0.5
    return num/den if den else None

def ols_slope(xs, ys):
    n = len(xs)
    mx, my = sum(xs)/n, sum(ys)/n
    den = sum((x-mx)**2 for x in xs)
    return sum((xs[i]-mx)*(ys[i]-my) for i in range(n))/den if den else None

def acc(recs, arm):
    by = defaultdict(lambda: [0, 0])  # model -> [correct, n_parsed]
    nfail = 0
    for r in recs:
        if r["arm"] != arm:
            continue
        if r["pick"] is None:
            nfail += 1
            continue
        by[r["model"]][1] += 1
        if r["correct"]:
            by[r["model"]][0] += 1
    return by, nfail

def main():
    text, image, distract = load("text"), load("image"), load("distract")
    if not (text and image):
        print("missing raw/text.json or raw/image.json — run the arms first.")
        sys.exit(0)

    print("=" * 70)
    print("0. PARSE INTEGRITY")
    for arm, recs in [("text", text), ("image", image), ("distract", distract or [])]:
        nf = sum(1 for r in recs if r["pick"] is None)
        print(f"   {arm:9s}: {len(recs)} calls, {nf} parse-fails")

    print("\n1. DISTRACTION NULL (reported FIRST; word-ablated, chance=0.10)")
    if distract:
        by, _ = acc(distract, "distract")
        for m in MODELS:
            k, n = by[m]
            p, lo, hi = wilson(k, n)
            flag = "  <-- >> chance" if lo > CHANCE else ""
            print(f"   {m:7s}: gold-selected {k}/{n} = {p:.3f}  Wilson[{lo:.3f},{hi:.3f}]{flag}")
        allk = sum(by[m][0] for m in MODELS); alln = sum(by[m][1] for m in MODELS)
        p, lo, hi = wilson(allk, alln)
        print(f"   POOLED : {allk}/{alln} = {p:.3f}  Wilson[{lo:.3f},{hi:.3f}]")
    else:
        print("   (distract arm not yet run)")

    print("\n2. MAIN ACCURACY per arm per model")
    for arm, recs in [("text", text), ("image", image)]:
        by, _ = acc(recs, arm)
        line = "  ".join(f"{m}:{by[m][0]}/{by[m][1]}={by[m][0]/max(by[m][1],1):.3f}" for m in MODELS)
        print(f"   {arm:6s}: {line}")

    # per-item maps
    def cell(recs, arm):
        d = {}
        for r in recs:
            if r["arm"] == arm and r["pick"] is not None:
                d[(r["item_id"], r["model"])] = 1 if r["correct"] else 0
        return d
    tc, gc = cell(text, "text"), cell(image, "image")
    items = sorted({iid for (iid, _) in tc})

    sep, delta = {}, {}
    for iid in items:
        tv = [tc[(iid, m)] for m in MODELS if (iid, m) in tc]
        gv = [gc[(iid, m)] for m in MODELS if (iid, m) in gc]
        if not tv or not gv:
            continue
        sep[iid] = sum(tv)/len(tv)
        delta[iid] = sum(gv)/len(gv) - sum(tv)/len(tv)

    print("\n3. SEPARABILITY sep_i DISTRIBUTION + STRATA (mod-1 floor >=8/bin)")
    from collections import Counter
    dist = Counter(round(sep[i], 3) for i in sep)
    print(f"   sep_i counts: {dict(sorted(dist.items()))}")
    saturated = [i for i in sep if sep[i] == 1.0]
    underdet = [i for i in sep if sep[i] <= 1/3 + 1e-9]
    print(f"   saturated (sep=1): {len(saturated)}   under-determined (sep<=1/3): {len(underdet)}")
    floor_ok = len(saturated) >= 8 and len(underdet) >= 8
    print(f"   floor (>=8/bin) {'MET' if floor_ok else 'NOT MET -> binned interaction NOT credited'}")

    print("\n4. TEST OF RECORD — image-rescue rate by text outcome (item x model cells)")
    rescue = [0, 0]   # [image-correct, n] among text-failed cells
    keep = [0, 0]     # among text-succeeded cells
    for (iid, m), t in tc.items():
        if (iid, m) not in gc:
            continue
        g = gc[(iid, m)]
        if t == 0:
            rescue[1] += 1; rescue[0] += g
        else:
            keep[1] += 1; keep[0] += g
    pr, lor, hir = wilson(*rescue)
    pk, lok, hik = wilson(*keep)
    print(f"   text-FAILED cells: image-correct {rescue[0]}/{rescue[1]} = {pr:.3f} Wilson[{lor:.3f},{hir:.3f}]")
    print(f"   text-OK     cells: image-correct {keep[0]}/{keep[1]} = {pk:.3f} Wilson[{lok:.3f},{hik:.3f}]")
    print("   (gating shape -> substantial rescue in text-FAILED cells, surviving the distraction null)")

    xs = [sep[i] for i in sep]; ys = [delta[i] for i in sep]
    rho = spearman(xs, ys); slope = ols_slope(xs, ys)
    print(f"\n   descriptive companion (ceiling-confounded): Spearman(sep,Δ)={rho:.3f} "
          f"OLS slope={slope:.3f}  (predicted negative; NOT the headline — see design)")
    print("=" * 70)

if __name__ == "__main__":
    main()
