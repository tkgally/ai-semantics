#!/usr/bin/env python3
"""Score the VWSD grounding-headroom NL-baseline (MAGNITUDE) probe per the frozen design.

FREEZE sections (run after desc-full + text-full + audit-full; these are what the
fresh independent pre-run critic reads against the OBSERVED distributions, design
condition e — BEFORE the reused IMAGE arm is read):
  A. parse integrity (text_nl + audit arms)
  B. TEXT-NL (fluent description) arm accuracy per model + per-item separability sep_nl_i
     distribution and strata counts, with the >=15/bin floor (carried from v2)
  C. ADEQUACY AUDIT — held-out referent-recovery, per auditor none/partial/high + the
     high-recovery rate, the TWO-AUDITOR MEAN, and the band [0.60, 0.95] check (P1/P2/P3,
     decisions/resolved/vwsd-nlbaseline-audit-params). OUT OF BAND => pre-run-critic NO-GO.

RESULT sections (only AFTER a fresh pre-run-critic GO — read the reused IMAGE arm):
  1. DISTRACT null FIRST (reused v2 word-ablated arm; chance 0.10) — credited before any lift
  2. main accuracy per arm (text_nl vs reused image)
  3. THE MAGNITUDE READ: residual width (fraction of NL-text-FAILED cells) + image-rescue
     rate in those cells vs text-OK cells; companion Spearman/OLS(Delta_nl, sep_nl_i).

Pure stdlib; no model calls. The reused IMAGE/DISTRACT arms are byte-identical-by-sha to v2
(image 6884eea0…430870, distract f8fbb6be…); this script never re-runs them.
"""
import json, os
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
MODELS = ["claude", "gpt", "gemini"]
AUDITORS = ["gpt", "gemini"]
CHANCE = 0.10
FLOOR = 15
BAND = (0.60, 0.95)

def load_raw(name):
    p = os.path.join(HERE, "raw", f"{name}.json")
    return json.load(open(p)) if os.path.exists(p) else None

def load_nldesc():
    p = os.path.join(HERE, "frozen", "nl_descriptors.json")
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
    text = load_raw("text_nl")
    image, distract = load_raw("image"), load_raw("distract")
    nld = load_nldesc()

    print("=" * 72)
    print("FREEZE sections (NL channel; read by the pre-run critic before the IMAGE arm)")
    sep = {}
    if not text:
        print("  no text_nl covariate yet (run text-full).")
    else:
        print("\nA. PARSE INTEGRITY")
        nf = sum(1 for r in text if r["pick"] is None)
        print(f"   text_nl: {len(text)} calls, {nf} parse-fails")

        print("\nB. TEXT-NL (fluent description) ARM accuracy + separability sep_nl_i")
        by = acc(text, "text_nl")
        print("   " + "  ".join(
            f"{m}:{by[m][0]}/{by[m][1]}={by[m][0]/max(by[m][1],1):.3f}" for m in MODELS))
        tc = cell(text, "text_nl")
        items = sorted({iid for (iid, _) in tc})
        for iid in items:
            tv = [tc[(iid, m)] for m in MODELS if (iid, m) in tc]
            if tv:
                sep[iid] = sum(tv)/len(tv)
        dist = Counter(round(sep[i], 3) for i in sep)
        print(f"   sep_nl_i counts: {dict(sorted(dist.items()))}  (n={len(sep)})")
        saturated = [i for i in sep if sep[i] == 1.0]
        underdet = [i for i in sep if sep[i] <= 1/3 + 1e-9]
        inter = [i for i in sep if abs(sep[i]-2/3) < 1e-9]
        print(f"   under-determined (sep_nl<=1/3): {len(underdet)}   intermediate (2/3): {len(inter)}"
              f"   saturated (sep_nl=1): {len(saturated)}")
        ok = len(saturated) >= FLOOR and len(underdet) >= FLOOR
        print(f"   floor (>={FLOOR}/bin): under-det {'PASS' if len(underdet)>=FLOOR else 'FAIL'}, "
              f"saturated {'PASS' if len(saturated)>=FLOOR else 'FAIL'} "
              f"-> binned read {'CREDITED' if ok else 'NOT credited (fall back to continuous/cell)'}")
        if not ok and len(underdet) < FLOOR:
            print("   NOTE: a below-floor under-determined bin means the fluent NL channel SATURATED")
            print("   (few text-failed cells) -> the residual is NARROW BY DIRECT OBSERVATION, an")
            print("   informative prediction-3-supporting outcome (reported, NOT patched by re-binning).")

    if nld and nld.get("audit"):
        print("\nC. ADEQUACY AUDIT (held-out referent recovery; 0 none /1 partial /2 high)")
        audit = nld["audit"]
        n = len(audit)
        per_auditor = {}
        for a in AUDITORS:
            vals = [v["auditors"][a]["recovery_score"] for v in audit.values() if a in v["auditors"]]
            d = {s: sum(1 for x in vals if x == s) for s in (0, 1, 2)}
            hi = d[2] / max(len(vals), 1)
            per_auditor[a] = hi
            print(f"   {a:7s}: none/partial/high = {d[0]}/{d[1]}/{d[2]}  (n={len(vals)})  "
                  f"high-recovery rate = {hi:.3f}")
        mean_hi = sum(per_auditor[a] for a in AUDITORS) / len(AUDITORS)
        inband = BAND[0] <= mean_hi <= BAND[1]
        print(f"   TWO-AUDITOR MEAN high-recovery = {mean_hi:.3f}   band {BAND}")
        print(f"   => {'IN BAND (channel admissible)' if inband else 'OUT OF BAND => pre-run-critic NO-GO (defers, relaxes nothing)'}")
        for a in AUDITORS:
            if per_auditor[a] > BAND[1]:
                print(f"      !! per-auditor {a} high-recovery {per_auditor[a]:.3f} > upper {BAND[1]} (oracle-scrutiny signal)")
            if per_auditor[a] < BAND[0]:
                print(f"      !! per-auditor {a} high-recovery {per_auditor[a]:.3f} < lower {BAND[0]} (degenerate-scrutiny signal)")

    # ---- RESULT sections (only after a pre-run-critic GO) ----
    if text and image:
        print("\n" + "=" * 72)
        print("RESULT sections (reused IMAGE arm present — read only after a pre-run-critic GO)")
        print("\n1. DISTRACTION NULL (reused v2 arm, reported FIRST; word-ablated, chance=0.10)")
        if distract:
            dby = acc(distract, "distract")
            for m in MODELS:
                k, nn = dby[m]
                p, lo, hi = wilson(k, nn)
                flag = "  <-- >> chance" if lo > CHANCE else ""
                print(f"   {m:7s}: {k}/{nn} = {p:.3f}  Wilson[{lo:.3f},{hi:.3f}]{flag}")
            allk = sum(dby[m][0] for m in MODELS); alln = sum(dby[m][1] for m in MODELS)
            p, lo, hi = wilson(allk, alln)
            print(f"   POOLED : {allk}/{alln} = {p:.3f}  Wilson[{lo:.3f},{hi:.3f}]")
        else:
            print("   (distract arm missing — must be reported before crediting any lift)")

        print("\n2. MAIN ACCURACY")
        for arm, recs in [("text_nl", text), ("image", image)]:
            by = acc(recs, arm)
            print("   " + arm + ": " + "  ".join(
                f"{m}:{by[m][0]/max(by[m][1],1):.3f}" for m in MODELS))

        tc, gc = cell(text, "text_nl"), cell(image, "image")
        common = [(iid, m) for (iid, m) in tc if (iid, m) in gc]
        ncells = len(common)
        nfail = sum(1 for k in common if tc[k] == 0)
        print("\n3. THE MAGNITUDE READ")
        print(f"   residual width = NL-text-FAILED cells / all cells = {nfail}/{ncells} = "
              f"{nfail/max(ncells,1):.3f}  (small => narrow headroom; large => wide)")
        rescue, keep = [0, 0], [0, 0]
        for (iid, m) in common:
            g = gc[(iid, m)]
            (rescue if tc[(iid, m)] == 0 else keep)[1] += 1
            (rescue if tc[(iid, m)] == 0 else keep)[0] += g
        pr, lor, hir = wilson(*rescue)
        pk, lok, hik = wilson(*keep)
        print(f"   image-rescue in NL-text-FAILED cells: {rescue[0]}/{rescue[1]} = {pr:.3f} Wilson[{lor:.3f},{hir:.3f}]")
        print(f"   image acc where NL-text-OK         : {keep[0]}/{keep[1]} = {pk:.3f} Wilson[{lok:.3f},{hik:.3f}]")
        # per-model rescue
        print("   per-model rescue in NL-text-failed cells:")
        for m in MODELS:
            rk = [0, 0]
            for (iid, mm) in common:
                if mm == m and tc[(iid, mm)] == 0:
                    rk[1] += 1; rk[0] += gc[(iid, mm)]
            p, lo, hi = wilson(*rk)
            print(f"      {m:7s}: {rk[0]}/{rk[1]} = {p:.3f} Wilson[{lo:.3f},{hi:.3f}]")

        # companion: per-item Delta_nl = mean_m(image) - mean_m(text_nl) vs sep_nl_i (mechanical-ceiling caveat)
        items = sorted({iid for (iid, _) in tc})
        deltas, seps = [], []
        for iid in items:
            tv = [tc[(iid, m)] for m in MODELS if (iid, m) in tc]
            gv = [gc[(iid, m)] for m in MODELS if (iid, m) in gc]
            if tv and gv and iid in sep:
                deltas.append(sum(gv)/len(gv) - sum(tv)/len(tv)); seps.append(sep[iid])
        rho = spearman(seps, deltas)
        sl = ols_slope(seps, deltas)
        print(f"\n   COMPANION (mechanical-ceiling caveat in force): Spearman(sep_nl_i, Delta_nl) = "
              f"{rho if rho is None else round(rho,3)}, OLS slope = {sl if sl is None else round(sl,3)} "
              f"(conjecture predicts negative; demoted — binary ceiling makes raw negative partly mechanical)")
    print("=" * 72)

if __name__ == "__main__":
    main()
