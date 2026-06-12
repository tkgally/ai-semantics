#!/usr/bin/env python3
"""probe.py — relational history-perturbation probe (v2).

The decisive test of conjecture/commutative-convention: a fresh matcher sees a convention
record whose CONTENT MULTISET is fixed (2 descriptions of twin X + 2 of twin Y, uniform
positive feedback) and whose ORDER varies over all 6 arrangements of {X,X,Y,Y}, plus a
nonce coined term. COMMUTATIVE (the conjecture's bet): pick distribution invariant across
orders -> recency-pick rate ~ 0.5 among in-pair picks.

PRE-RUN CRITIC REVISIONS implemented (2026-06-12, before any finding-bearing call):
- B1 presentation-direction arm: each mixed trial runs "fwd" (earliest first) and "rev"
  (most recent first; lines physically reversed, chronology identical). Chronology-tracking
  follows the STATED-latest twin in both arms; an attention artifact follows the
  PHYSICALLY-last line in both.
- S1: ONE matcher figure-array permutation per (model, pair, sample) cluster, reused across
  all 6 orders x 2 directions and the cluster's consistent controls (v1 discipline).
- S3: transport-error / parse-fail calls are retried ONCE; persistent failures recorded NA.
- S2: preflight = gpt consistent controls only; liveness/preflight raw is never analyzed
  (the `full` run is the only finding-bearing dataset).

Mirrors the v1 probe prompt shape with ONE deliberate pre-registered change: history lines
carry NO round numbers (v1's lines kept "round k:" labels, so v1's shuffle was
reconstructible in principle; v2 conveys order purely by position + the stated direction).

Usage:
  python3 probe.py liveness    # 3 calls, one per model (~$0.01) — excluded from analysis
  python3 probe.py preflight   # gpt consistent controls only; billed-cost extrapolation
  python3 probe.py full        # full grid -> raw/results.json
"""
import json
import os
import random
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost  # noqa: E402

MODELS = {"claude": PANEL["A"], "gpt": PANEL["B"], "gemini": PANEL["C"]}
SEED0 = 20260612
MODEL_SEED_OFFSET = {"claude": 11, "gpt": 23, "gemini": 37}
REASONING = {"google/": {"effort": "minimal"}}

PROBE_SYS = (
    "You match an abstract figure to a record. Each figure is an 8x8 grid of '#' (filled) and '.' "
    "(empty). You are shown a record about ONE target figure plus a short label for it; decide "
    "which of your figures is that target. Reply with ONLY the label (e.g. {example}).")

INTRO = {
    "fwd": ("Your partner referred to ONE target figure over several rounds. What they said, "
            "in the order it happened (earliest first):"),
    "rev": ("Your partner referred to ONE target figure over several rounds. What they said, "
            "in reverse order (most recent first):"),
}


def reasoning_for(model):
    for pref, val in REASONING.items():
        if model.startswith(pref):
            return val
    return None


def grid_block(order, fig):
    out = []
    for label, cid in order:
        out.append(f"[{label}]")
        out.extend("  " + row for row in fig[cid]["grid"])
    return "\n".join(out)


def parse_label(txt, labels):
    if not txt:
        return None
    found = re.findall(r"[A-Za-z]+\s*\d+", txt)
    norm = [f.replace(" ", "").upper() for f in found]
    cand = [x for x in norm if x in labels]
    return cand[-1] if cand else None


def cluster_p_order(mname, pair, sample, canon):
    """Deterministic matcher array per (model, pair, sample) cluster — constant across the
    cluster's 6 orders x 2 directions and its consistent controls (critic S1)."""
    rng = random.Random(SEED0 + MODEL_SEED_OFFSET[mname] + 100 * pair + 10 * sample)
    ids = list(canon)
    rng.shuffle(ids)
    return [(f"P{i+1}", cid) for i, cid in enumerate(ids)]


def call_retry(model, sys_p, user, rsn, labels):
    """Call; retry ONCE on transport error or parse failure (critic S3)."""
    r = call(model, sys_p, user, max_tokens=128, reasoning=rsn)
    pick = parse_label(r.get("content"), labels)
    retried = False
    if r.get("error") or pick is None:
        retried = True
        r2 = call(model, sys_p, user, max_tokens=128, reasoning=rsn)
        pick2 = parse_label(r2.get("content"), labels)
        if pick2 is not None or not r.get("content"):
            usages = [u for u in (r.get("usage"), r2.get("usage")) if u]
            return r2, pick2, retried, usages
        usages = [u for u in (r.get("usage"), r2.get("usage")) if u]
        return r, pick, retried, usages
    return r, pick, retried, [r.get("usage", {})]


def run_trials(mname, model, stim, trials):
    fig = stim["figures"]
    canon = sorted(fig.keys())
    rsn = reasoning_for(model)
    recs = []
    for t in trials:
        p_order = cluster_p_order(mname, t["pair"], t["sample"], canon)
        p_block = grid_block(p_order, fig)
        labels = {l for l, _ in p_order}
        label_list = ", ".join(l for l, _ in p_order)
        lines = t["lines"] if t["direction"] == "fwd" else list(reversed(t["lines"]))
        hist = "\n".join(f'- partner said "{d}" -> you FOUND it' for d in lines)
        user = (f"Your figures:\n{p_block}\n\n{INTRO[t['direction']]}\n{hist}\n\n"
                f"The target is referred to as: \"{t['nonce']}\"\n\n"
                f"Which of your figures is it? Reply with only the label ({label_list}).")
        r, pick, retried, usages = call_retry(model, PROBE_SYS.format(example=p_order[0][0]),
                                              user, rsn, labels)
        pick_cid = next((c for l, c in p_order if l == pick), None)
        rec = dict(t)
        rec.update({"model": mname, "pick": pick, "pick_cid": pick_cid,
                    "retried": retried, "raw": r.get("content"),
                    "usage": usages, "err": r.get("error")})
        if t["kind"] == "mixed":
            rec["in_pair"] = pick_cid in (t["X"], t["Y"])
            rec["picked_chron_last"] = (pick_cid == t["last"]) if rec["in_pair"] else None
            phys_last = t["last"] if t["direction"] == "fwd" else t["first"]
            rec["picked_phys_last"] = (pick_cid == phys_last) if rec["in_pair"] else None
        else:
            rec["correct"] = (pick_cid == t["target"])
        recs.append(rec)
    return recs


def flat_cost(recs):
    flat = []
    for r in recs:
        u = r.get("usage")
        if isinstance(u, list):
            flat += [{"usage": x} for x in u if x]
        elif u:
            flat.append({"usage": u})
    return billed_cost([flat])


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "liveness"
    stim = json.load(open(os.path.join(HERE, "stimuli.json")))
    os.makedirs(os.path.join(HERE, "raw"), exist_ok=True)
    if mode == "liveness":
        recs = []
        for mname, model in MODELS.items():
            r = run_trials(mname, model, stim, stim["trials"][mname][:1])[0]
            print(f"  {mname:7s}: pick={r['pick']!r} raw={r['raw']!r} "
                  f"cost={[u.get('cost') for u in r['usage']]}")
            recs.append(r)
        tot, have, miss = flat_cost(recs)
        print(f"liveness billed=${tot:.5f} (have={have} missing={miss}) — NOT analyzed")
    elif mode == "preflight":
        ctrl = [t for t in stim["trials"]["gpt"] if t["kind"] == "consistent"]
        recs = run_trials("gpt", MODELS["gpt"], stim, ctrl)
        json.dump(recs, open(os.path.join(HERE, "raw", "preflight.json"), "w"), indent=2)
        tot, have, miss = flat_cost(recs)
        nfail = sum(1 for r in recs if r["pick"] is None)
        acc = sum(1 for r in recs if r.get("correct")) / len(recs)
        n_full = sum(len(stim["trials"][m]) for m in MODELS)
        print(f"PREFLIGHT (gpt, {len(recs)} consistent controls): {nfail} parse-fails, "
              f"control acc={acc:.2f}, billed=${tot:.5f} (have={have} missing={miss})")
        print(f"  full-run extrapolation: {n_full} calls ~= ${tot/len(recs)*n_full:.3f} "
              f"(claude pricier, gemini cheaper) — NOT analyzed; full supersedes")
    elif mode == "full":
        allrecs = []
        for mname, model in MODELS.items():
            print(f"=== {mname} ===")
            rs = run_trials(mname, model, stim, stim["trials"][mname])
            allrecs += rs
            json.dump(allrecs, open(os.path.join(HERE, "raw", "results.json"), "w"), indent=2)
            t, h, m = flat_cost(rs)
            print(f"  {mname}: {len(rs)} records, billed=${t:.5f}")
        tot, have, miss = flat_cost(allrecs)
        print(f"\nFULL: {len(allrecs)} records, billed=${tot:.5f} (have={have} missing={miss})")
    else:
        print("usage: probe.py [liveness|preflight|full]")


if __name__ == "__main__":
    main()
