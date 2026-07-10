#!/usr/bin/env python3
"""Independent verifier — does NOT import analyze.py. Recompute from raw/ + items.json."""
import json, math
from pathlib import Path
from collections import defaultdict

HERE = Path(".")
RAW = HERE / "raw"
items = json.load(open("items.json"))
PARA = {p["uid"]: p for p in items["paradigms"]}
UIDS = [p["uid"] for p in items["paradigms"]]
SLOTS = ["A", "B", "C"]

SHALLOW = {"local"}
DEEP = {"scope", "island"}

# frozen constants
PROFILE_ALIGNED = 0.40
PROFILE_DIVERGES = 0.20
SATURATION_SD = 0.03
DEPTH_MARGIN = 0.05
R2H_MARGIN = 0.05
POSLOCK_FAIL = 0.50
ANS1_EXTREME = 0.40
F4_FLOOR = 0.60


def spearman(x, y):
    n = len(x)
    def rank(v):
        idx = sorted(range(n), key=lambda i: v[i])
        r = [0.0]*n
        i = 0
        while i < n:
            j = i
            while j+1 < n and v[idx[j+1]] == v[idx[i]]:
                j += 1
            avg = (i + j) / 2.0  # 0-based avg rank
            for k in range(i, j+1):
                r[idx[k]] = avg
            i = j+1
        return r
    rx, ry = rank(x), rank(y)
    mx, my = sum(rx)/n, sum(ry)/n
    rx = [a-mx for a in rx]; ry = [a-my for a in ry]
    num = sum(a*b for a,b in zip(rx,ry))
    den = math.sqrt(sum(a*a for a in rx)*sum(b*b for b in ry))
    return num/den if den else float("nan")


def mean(v): return sum(v)/len(v)
def sd(v):
    m = mean(v); return math.sqrt(sum((x-m)**2 for x in v)/(len(v)-1))

# ---- integrity + per-paradigm accuracy ----
integrity = []
total_calls = 0
unparsed = 0
per_model_acc = {}      # slot -> {uid: acc}
per_model_diag = {}

for slot in SLOTS:
    acc_by_uid = {}
    ans1 = 0
    slot_calls = 0
    poslock_num = poslock_den = 0
    for uid in UIDS:
        f = RAW / f"{slot}-{uid}.json"
        if not f.exists():
            integrity.append(f"MISSING {f}")
            continue
        rows = json.load(open(f))
        slot_calls += len(rows)
        if len(rows) != 60:
            integrity.append(f"{slot}-{uid}: {len(rows)} rows (!=60)")
        by_pair = defaultdict(dict)
        for r in rows:
            total_calls += 1
            ch = r["choice"]
            if ch is None:
                unparsed += 1
            if ch == 1:
                ans1 += 1
            # verify 'correct' field self-consistency
            if ch is not None:
                exp = (ch == r["good_pos"])
                if bool(r["correct"]) != exp:
                    integrity.append(f"{slot}-{uid} pair {r['pairID']} {r['order']}: correct field mismatch")
            if r["order"] in by_pair[r["pairID"]]:
                integrity.append(f"{slot}-{uid} pair {r['pairID']} dup order {r['order']}")
            by_pair[r["pairID"]][r["order"]] = r
        if len(by_pair) != 30:
            integrity.append(f"{slot}-{uid}: {len(by_pair)} pairs (!=30)")
        pair_oa = []
        for pid, od in by_pair.items():
            if set(od.keys()) != {"gf", "gs"}:
                integrity.append(f"{slot}-{uid} pair {pid}: orders {sorted(od.keys())}")
            # order-averaged: correct iff choice==good_pos, average over orders present
            cs = []
            for o in ("gf", "gs"):
                if o in od and od[o]["choice"] is not None:
                    cs.append(1.0 if od[o]["choice"] == od[o]["good_pos"] else 0.0)
            if cs:
                pair_oa.append(sum(cs)/len(cs))
            if "gf" in od and "gs" in od and od["gf"]["choice"] is not None and od["gs"]["choice"] is not None:
                poslock_den += 1
                if od["gf"]["choice"] == od["gs"]["choice"]:
                    poslock_num += 1
        acc_by_uid[uid] = mean(pair_oa)
    per_model_acc[slot] = acc_by_uid
    per_model_diag[slot] = {
        "ans1_rate": ans1/slot_calls,
        "poslock_rate": poslock_num/poslock_den if poslock_den else float("nan"),
        "n_calls": slot_calls,
    }

humans = [PARA[u]["human_agreement"] for u in UIDS]

# human depth gap
hsh = mean([PARA[u]["human_agreement"] for u in UIDS if PARA[u]["stratum"] in SHALLOW])
hdp = mean([PARA[u]["human_agreement"] for u in UIDS if PARA[u]["stratum"] in DEEP])
human_gap = hsh - hdp

def strat_mean(acc_by_uid, keys):
    v = [acc_by_uid[u] for u in UIDS if PARA[u]["stratum"] in keys and PARA[u]["human_agreement"] >= F4_FLOOR]
    return mean(v), len(v)

print(f"TOTAL CALLS: {total_calls}  UNPARSED: {unparsed}")
print(f"human shallow {hsh:.4f} deep {hdp:.4f} gap {human_gap:+.4f}")
print(f"integrity issues: {len(integrity)}")
for i in integrity[:50]:
    print("  ", i)

summary = {}
for slot in SLOTS:
    acc_by_uid = per_model_acc[slot]
    acc = [acc_by_uid[u] for u in UIDS]
    rho = spearman(acc, humans)
    a_sd = sd(acc)
    sh, _ = strat_mean(acc_by_uid, SHALLOW)
    dp, _ = strat_mean(acc_by_uid, DEEP)
    gap = sh - dp
    d = per_model_diag[slot]
    summary[slot] = {
        "rho": rho, "abs_acc": mean(acc), "acc_sd": a_sd,
        "acc_min": min(acc), "acc_max": max(acc),
        "shallow": sh, "deep": dp, "depth_gap": gap,
        "saturated": a_sd < SATURATION_SD,
        "ans1_rate": d["ans1_rate"], "poslock": d["poslock_rate"],
        "excess": gap - human_gap,
    }
    print(f"\n[{slot}] rho={rho:+.4f} abs_acc={mean(acc):.4f} SD={a_sd:.4f} "
          f"({min(acc):.2f}-{max(acc):.2f}) sat={a_sd<SATURATION_SD}")
    print(f"     shallow={sh:.4f} deep={dp:.4f} depth_gap={gap:+.4f} excess_over_human={gap-human_gap:+.4f}")
    print(f"     ans1={d['ans1_rate']:.4f} poslock={d['poslock_rate']:.4f}")

def maj(pred): return sum(1 for s in SLOTS if pred(s)) >= 2
aligned = maj(lambda s: (not summary[s]["saturated"]) and summary[s]["rho"] > PROFILE_ALIGNED)
diverges = maj(lambda s: (not summary[s]["saturated"]) and summary[s]["rho"] < PROFILE_DIVERGES)
r1 = "PROFILE-ALIGNED" if aligned else ("PROFILE-DIVERGES" if diverges else "PROFILE-INCONCLUSIVE")
graded = maj(lambda s: summary[s]["depth_gap"] >= DEPTH_MARGIN)
r2 = "DEPTH-GRADED" if graded else "DEPTH-FLAT"
exceeds = maj(lambda s: summary[s]["excess"] > R2H_MARGIN)
tracks = maj(lambda s: abs(summary[s]["excess"]) <= R2H_MARGIN)
r2h = "EXCEEDS-HUMAN-DIP" if exceeds else ("TRACKS-DIP" if tracks else "BELOW-HUMAN-DIP")
instr = maj(lambda s: summary[s]["poslock"] > POSLOCK_FAIL and abs(summary[s]["ans1_rate"]-0.5) > ANS1_EXTREME)

print("\n--- VERDICTS (independent) ---")
print("R1:", r1)
print("R2:", r2, {s: round(summary[s]["depth_gap"],4) for s in SLOTS})
print("R2h:", r2h)
print("instrument_failure:", instr)

json.dump({"summary": {s: {k: summary[s][k] for k in summary[s]} for s in SLOTS},
           "r1": r1, "r2": r2, "r2h": r2h, "instr": instr,
           "human_gap": human_gap, "total_calls": total_calls, "unparsed": unparsed,
           "integrity": integrity}, open("verify_out.json","w"), indent=1)
