#!/usr/bin/env python3
"""Independent post-run verifier. Does NOT import analyze.py.
Recomputes every headline stat from raw JSONL with an independent bootstrap seed."""
import json, hashlib, statistics
from collections import defaultdict
import numpy as np

RUN = "/home/user/ai-semantics/experiments/runs/2026-07-15-particle-placement-givenness-rep2"
MODELS = ["claude", "gemini", "gpt"]
SEED = 999333
NBOOT = 10000

# ---- 1. hashes ----
def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

EXP_STIM = "3544656488431d15eb15dada53b46b2b7573ef647a4c9499f81bece2f2d29826"
EXP_FREQ = "cd472475cfae6f03862cd12ffc9421cd085d8abca831e2cccf1edd7a42da20d7"
stim_h = sha(f"{RUN}/stimuli.json")
freq_h = sha(f"{RUN}/freq_control.json")
print("=== HASH CHECK ===")
print(f"stimuli.json      {stim_h}  {'OK' if stim_h==EXP_STIM else 'MISMATCH'}")
print(f"freq_control.json {freq_h}  {'OK' if freq_h==EXP_FREQ else 'MISMATCH'}")

# ---- load ----
data = {}
for m in MODELS:
    rows = [json.loads(l) for l in open(f"{RUN}/raw/probe-{m}.jsonl")]
    data[m] = rows

# ---- 1b. completeness ----
print("\n=== COMPLETENESS ===")
total_cost = 0.0
for m in MODELS:
    rows = data[m]
    n = len(rows)
    na = sum(1 for r in rows if r["split_pref"] is None)
    trunc = sum(1 for r in rows if r["finish_reason"] not in ("stop", "end_turn"))
    ret = sum(1 for r in rows if r.get("retried"))
    mcost = sum(u.get("cost", 0.0) for r in rows for u in r.get("usage", []))
    total_cost += mcost
    print(f"{m:7s} n={n} na={na} truncated={trunc} retried={ret} cost=${mcost:.5f}")
print(f"TOTAL BILLED COST: ${total_cost:.5f}")

# ---- helper: cell = mean split_pref over A/B replicates ----
def cells(rows):
    """returns dict[(frame,arm,cond)] -> mean split_pref over replicates"""
    acc = defaultdict(list)
    for r in rows:
        acc[(r["frame"], r["arm"], r["condition"])].append(r["split_pref"])
    return {k: statistics.mean(v) for k, v in acc.items()}

def frames_of(rows):
    return sorted({r["frame"] for r in rows})

def shifts(cell, frames, arm, hi, lo):
    out = []
    for f in frames:
        a = cell.get((f, arm, hi)); b = cell.get((f, arm, lo))
        if a is None or b is None:
            raise ValueError(f"missing cell {f} {arm} {hi}/{lo}")
        out.append(a - b)
    return out

def boot_ci(vals, rng):
    arr = np.asarray(vals, float)
    n = len(arr)
    idx = rng.integers(0, n, size=(NBOOT, n))
    means = arr[idx].mean(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))

print("\n=== PER-MODEL SHIFTS (independent, seed 999333) ===")
results = {}
for m in MODELS:
    rng = np.random.default_rng(SEED)  # same seed each model, matching analyze convention of fixed seed
    rows = data[m]
    cell = cells(rows)
    frames = frames_of(rows)
    assert len(frames) == 48, f"{m} has {len(frames)} frames"

    s1 = shifts(cell, frames, "definiteness", "definite", "indefinite")
    s2 = shifts(cell, frames, "firewall", "given", "newment")          # decisive
    s2_desc = shifts(cell, frames, "firewall", "given", "new")          # descriptive
    s3 = shifts(cell, frames, "length", "short", "long")

    s1m, s2m, s2dm, s3m = (statistics.mean(x) for x in (s1, s2, s2_desc, s3))
    s1lo, s1hi = boot_ci(s1, np.random.default_rng(SEED))
    s2lo, s2hi = boot_ci(s2, np.random.default_rng(SEED))
    s3lo, s3hi = boot_ci(s3, np.random.default_rng(SEED))

    pos1 = sum(1 for x in s1 if x > 0)
    pos2 = sum(1 for x in s2 if x > 0)
    pos3 = sum(1 for x in s3 if x > 0)

    cond_fw = s2m > 0 and s2lo > 0
    arm1_consistent = s1m > 0
    arm1_reversal = s1m < 0
    cond_fw_strong = s1m > 0 and s1lo > 0
    cond_len = s3m > 0 and s3lo > 0

    if cond_fw and arm1_consistent and not arm1_reversal:
        verdict = "CONFIRM" if cond_fw_strong else "CONFIRM-firewall-borne"
    elif (not cond_fw) and arm1_consistent:
        verdict = "SHADOW"
    elif cond_fw and not cond_len:
        verdict = "WEAK"
    else:
        verdict = "FALSIFY"

    results[m] = dict(cond_fw=cond_fw, arm1_consistent=arm1_consistent,
                      arm1_reversal=arm1_reversal, cond_fw_strong=cond_fw_strong,
                      cond_len=cond_len, verdict=verdict, s1m=s1m)

    print(f"\n[{m}] verdict={verdict}")
    print(f"  firewall shift2 (given-newment): {s2m:+.4f} [{s2lo:.4f},{s2hi:.4f}]  {pos2}/48  cond_fw={cond_fw}")
    print(f"  firewall descriptive given-new : {s2dm:+.4f}")
    print(f"  definiteness shift1            : {s1m:+.4f} [{s1lo:.4f},{s1hi:.4f}]  {pos1}/48  strong={cond_fw_strong}")
    print(f"  length shift3                  : {s3m:+.4f} [{s3lo:.4f},{s3hi:.4f}]  {pos3}/48  cond_len={cond_len}")

# ---- panel ----
print("\n=== PANEL ===")
n_fw = sum(1 for m in MODELS if results[m]["cond_fw"])
n_a1 = sum(1 for m in MODELS if results[m]["arm1_consistent"])
n_rev = sum(1 for m in MODELS if results[m]["arm1_reversal"])
n_strong = sum(1 for m in MODELS if results[m]["cond_fw_strong"])
n_len = sum(1 for m in MODELS if results[m]["cond_len"])
n_s1pos = sum(1 for m in MODELS if results[m]["s1m"] > 0)

if n_fw >= 2 and n_a1 >= 2 and n_rev < 2:
    panel = "CONFIRM" if n_strong >= 2 else "CONFIRM-firewall-borne"
elif n_s1pos >= 2 and n_fw < 2:
    panel = "SHADOW"
elif n_fw >= 2 and n_len < 2:
    panel = "WEAK"
else:
    panel = "FALSIFY"

print(f"PANEL VERDICT: {panel}")
print(f"  cond_fw {n_fw}/3, arm1_consistent {n_a1}/3, arm1_reversal {n_rev}/3, "
      f"cond_fw_strong {n_strong}/3, cond_len {n_len}/3, definiteness>0 {n_s1pos}/3")
