#!/usr/bin/env python3
"""Score the VWSD grounding-headroom probe v2 per the frozen design.

DAY-1 sections (run after the text-only build; these are what the next-session pre-run
critic reads against the OBSERVED distributions, design condition e):
  A. parse integrity (text + floor arms)
  B. TEXT (descriptor) arm accuracy per model + per-item separability sep_i distribution
     and strata counts, with the raised >=15/bin floor (design B.5)
  C. Option-A FLOOR arm accuracy (must sit at/near chance 0.10) — the calibration check
  D. Option-C leak-audit distribution (0/1/2) + correlation of leak_i with sep_i (the
     Option-C circularity warning, design analysis)

RESULT sections (only once the IMAGE + DISTRACT arms exist, day 2+):
  1. DISTRACT null FIRST (word-ablated gold-selection rate vs chance 0.10)
  2. main accuracy per arm; 3. test of record = image-rescue in text-failed cells (+ the
     ceiling-confounded Spearman/OLS companion).
Pure stdlib; no model calls.
"""
import json, os
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
MODELS = ["claude", "gpt", "gemini"]
CHANCE = 0.10
FLOOR = 15

def load_raw(name):
    p = os.path.join(HERE, "raw", f"{name}.json")
    return json.load(open(p)) if os.path.exists(p) else None

def load_desc():
    p = os.path.join(HERE, "frozen", "descriptors.json")
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
    if n == 0:
        return None
    mx, my = sum(xs)/n, sum(ys)/n
    den = sum((x-mx)**2 for x in xs)
    return sum((xs[i]-mx)*(ys[i]-my) for i in range(n))/den if den else None

def acc(recs, arm):
    by = defaultdict(lambda: [0, 0])
    for r in recs:
        if r["arm"] != arm or r["pick"] is None:
            continue
        by[r["model"]][1] += 1
        if r["correct"]:
            by[r["model"]][0] += 1
    return by

def cell(recs, arm):
    d = {}
    for r in recs:
        if r["arm"] == arm and r["pick"] is not None:
            d[(r["item_id"], r["model"])] = 1 if r["correct"] else 0
    return d

def main():
    # day-1 covariate: prefer the frozen 120 (raw/text.json); fall back to the pool scoring
    text = load_raw("text") or load_raw("pool_text")
    floor = load_raw("floor")
    image, distract = load_raw("image"), load_raw("distract")
    desc = load_desc()

    print("=" * 72)
    print("DAY-1 (text-only freeze) sections")
    if not text:
        print("  no text covariate yet (run text-full / draw_stratified.py).")
    else:
        print("\nA. PARSE INTEGRITY")
        for nm, recs in [("text", text), ("floor", floor)]:
            if recs:
                nf = sum(1 for r in recs if r["pick"] is None)
                print(f"   {nm:6s}: {len(recs)} calls, {nf} parse-fails")

        print("\nB. TEXT (descriptor) ARM accuracy + separability sep_i")
        by = acc(text, "text")
        print("   " + "  ".join(
            f"{m}:{by[m][0]}/{by[m][1]}={by[m][0]/max(by[m][1],1):.3f}" for m in MODELS))
        tc = cell(text, "text")
        items = sorted({iid for (iid, _) in tc})
        sep = {}
        for iid in items:
            tv = [tc[(iid, m)] for m in MODELS if (iid, m) in tc]
            if tv:
                sep[iid] = sum(tv)/len(tv)
        dist = Counter(round(sep[i], 3) for i in sep)
        print(f"   sep_i counts: {dict(sorted(dist.items()))}  (n={len(sep)})")
        saturated = [i for i in sep if sep[i] == 1.0]
        underdet = [i for i in sep if sep[i] <= 1/3 + 1e-9]
        inter = [i for i in sep if abs(sep[i]-2/3) < 1e-9]
        print(f"   under-determined (sep<=1/3): {len(underdet)}   intermediate (2/3): {len(inter)}"
              f"   saturated (sep=1): {len(saturated)}")
        ok = len(saturated) >= FLOOR and len(underdet) >= FLOOR
        print(f"   floor (>={FLOOR}/bin): under-det {'PASS' if len(underdet)>=FLOOR else 'FAIL'}, "
              f"saturated {'PASS' if len(saturated)>=FLOOR else 'FAIL'} "
              f"-> binned interaction {'CREDITED' if ok else 'NOT credited (fall back)'}")

        if floor:
            print("\nC. Option-A FLOOR (bare index labels) — calibration (target ~0.10)")
            fby = acc(floor, "floor")
            for m in MODELS:
                k, n = fby[m]
                p, lo, hi = wilson(k, n)
                flag = "  <-- ABOVE chance, instrument suspect" if lo > CHANCE else ""
                print(f"   {m:7s}: {k}/{n} = {p:.3f}  Wilson[{lo:.3f},{hi:.3f}]{flag}")
            allk = sum(fby[m][0] for m in MODELS); alln = sum(fby[m][1] for m in MODELS)
            p, lo, hi = wilson(allk, alln)
            print(f"   POOLED : {allk}/{alln} = {p:.3f}  Wilson[{lo:.3f},{hi:.3f}]")

        if desc and desc.get("leak"):
            print("\nD. Option-C LEAK AUDIT (held-out gpt referent recovery; 0 none /1 partial /2 high)")
            leak = desc["leak"]
            ld = Counter(v["leak_score"] for v in leak.values())
            n = sum(ld.values())
            print(f"   leak distribution: {dict(sorted(ld.items()))}  (n={n}; "
                  f"high-leak rate = {ld.get(2,0)/max(n,1):.3f})")
            # correlation of leak_i with sep_i over items both have
            common = [iid for iid in sep if iid in leak]
            if len(common) >= 3:
                rho = spearman([leak[i]["leak_score"] for i in common], [sep[i] for i in common])
                mag = ("strong -> residual-contamination WARNING" if abs(rho) >= 0.4
                       else "moderate" if abs(rho) >= 0.25 else "weak -> mild residual contamination")
                print(f"   Spearman(leak_i, sep_i) over {len(common)} items = {rho:.3f}  ({mag})")

    # ---- RESULT sections (day 2+) ----
    if text and image:
        print("\n" + "=" * 72)
        print("RESULT sections (image arm present)")
        print("\n1. DISTRACTION NULL (reported FIRST; word-ablated, chance=0.10)")
        if distract:
            dby = acc(distract, "distract")
            for m in MODELS:
                k, n = dby[m]
                p, lo, hi = wilson(k, n)
                flag = "  <-- >> chance" if lo > CHANCE else ""
                print(f"   {m:7s}: {k}/{n} = {p:.3f}  Wilson[{lo:.3f},{hi:.3f}]{flag}")
        else:
            print("   (distract arm not yet run — must be reported before crediting any lift)")
        print("\n2. MAIN ACCURACY")
        for arm, recs in [("text", text), ("image", image)]:
            by = acc(recs, arm)
            print("   " + arm + ": " + "  ".join(
                f"{m}:{by[m][0]/max(by[m][1],1):.3f}" for m in MODELS))
        tc, gc = cell(text, "text"), cell(image, "image")
        rescue, keep = [0, 0], [0, 0]
        for (iid, m), t in tc.items():
            if (iid, m) not in gc:
                continue
            g = gc[(iid, m)]
            (rescue if t == 0 else keep)[1] += 1
            (rescue if t == 0 else keep)[0] += g
        pr, lor, hir = wilson(*rescue)
        pk, lok, hik = wilson(*keep)
        print("\n3. TEST OF RECORD — image rescue by text outcome")
        print(f"   text-FAILED cells: {rescue[0]}/{rescue[1]} = {pr:.3f} Wilson[{lor:.3f},{hir:.3f}]")
        print(f"   text-OK     cells: {keep[0]}/{keep[1]} = {pk:.3f} Wilson[{lok:.3f},{hik:.3f}]")
    print("=" * 72)

if __name__ == "__main__":
    main()
