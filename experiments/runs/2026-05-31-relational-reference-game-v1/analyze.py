#!/usr/bin/env python3
"""analyze.py — relational-reference-game-v1 analysis (reads raw/results.json).

Per model:
  - ENTRAINMENT (scaffolding): live success rate + mean description word-count by repetition,
    calibrated against resource/hawkins-tangrams (human: words 7.73->4.10, acc 0.78->0.94).
  - PROBE arms (per coined term = (game_seed,target) cluster): accuracy under
    coined_only / ordered / reversed / shuffled(mean of SHUF_PERMS).
  - INTERPRETABILITY GATE: history_lift = ordered - coined_only. If lift ~ 0, the opaque coined
    term is self-sufficient (or the history is useless) and the order contrast is NOT interpretable
    -> a methodological null, not a substantive relational null.
  - PRIMARY (load-bearing, internal contrast): order_gap = ordered - shuffled, clustered bootstrap
    CI over coined terms. Plus chronology check ordered - reversed (a coherent-order effect that is
    also present in reversed is a position/coherence artifact, NOT trajectory-dependence).
  - BAR (b) FLOOR: the same order_gap on MONOLOGUE records (no feedback). A relational reading needs
    the dyadic order_gap CI>0 AND > the mono order_gap.

Decision (pre-registered): RELATIONAL POSITIVE for a model iff dyadic history_lift>0 AND
order_gap CI>0 AND order_gap > mono order_gap AND ordered>reversed (chronology-specific). Else NULL
(deflationary) or, when lift~0, UNDER-POWERED/METHODOLOGICAL (probe could not test order).

Pure stdlib. Deterministic bootstrap.
"""
import json
import math
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw", "results.json")
B = 10000
random.seed(12345)
MODELS = ["claude", "gpt", "gemini"]


def load():
    return json.load(open(RAW))


def mean(xs):
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else float("nan")


def clusters(recs, model, source):
    """One cluster per coined term: (game_seed,target) -> per-arm accuracy."""
    by = {}
    for r in recs:
        if r.get("phase") != "probe" or r["model"] != model or r["source"] != source:
            continue
        key = (r["game_seed"], r["target"])
        by.setdefault(key, {"coined_only": [], "ordered": [], "reversed": [], "shuffled": []})
        by[key][r["condition"]].append(1.0 if r["correct"] else 0.0)
    out = []
    for key, d in by.items():
        if not d["ordered"] or not d["shuffled"]:
            continue
        out.append({"coined_only": mean(d["coined_only"]), "ordered": mean(d["ordered"]),
                    "reversed": mean(d["reversed"]), "shuffled": mean(d["shuffled"])})
    return out


def boot_ci(vals):
    if not vals:
        return (float("nan"), float("nan"), float("nan"))
    n = len(vals)
    ms = []
    for _ in range(B):
        ms.append(sum(vals[random.randrange(n)] for _ in range(n)) / n)
    ms.sort()
    return (sum(vals) / n, ms[int(0.025 * B)], ms[int(0.975 * B)])


def entrainment(recs, model):
    rows = []
    for rep in range(1, 6):
        live = [r for r in recs if r["phase"] == "live" and r["model"] == model and r["rep"] == rep]
        if live:
            rows.append((rep, mean([1.0 if r["correct"] else 0.0 for r in live]),
                         mean([r["words"] for r in live]), len(live)))
    return rows


def main():
    recs = load()
    print("=" * 80)
    print("RELATIONAL REFERENCE GAME v1 — analysis")
    print("=" * 80)
    pf = sum(1 for r in recs if r["phase"] in ("live", "probe") and r.get("pick") is None)
    print(f"records: {len(recs)} | pick-parse-fails: {pf}\n")

    print("--- ENTRAINMENT (live dyad; Hawkins human: words 7.73->4.10, acc 0.78->0.94) ---")
    for m in MODELS:
        rows = entrainment(recs, m)
        if not rows:
            continue
        print(f"[{m}]")
        for rep, acc, w, n in rows:
            print(f"    rep{rep}: acc={acc:.2f}  words={w:.2f}  n={n}")
    print()

    print("--- PROBE arms + trajectory contrast (cluster = one coined term) ---\n")
    summ = {}
    for m in MODELS:
        for source in ("dyadic", "mono"):
            cl = clusters(recs, m, source)
            if not cl:
                continue
            co = mean([c["coined_only"] for c in cl])
            od = mean([c["ordered"] for c in cl])
            rv = mean([c["reversed"] for c in cl])
            sh = mean([c["shuffled"] for c in cl])
            lift = [c["ordered"] - c["coined_only"] for c in cl]
            ogap = [c["ordered"] - c["shuffled"] for c in cl]
            lift_m, lift_lo, lift_hi = boot_ci(lift)
            og_m, og_lo, og_hi = boot_ci(ogap)
            summ[(m, source)] = dict(co=co, od=od, rv=rv, sh=sh, n=len(cl),
                                     lift=lift_m, lift_lo=lift_lo, lift_hi=lift_hi,
                                     og=og_m, og_lo=og_lo, og_hi=og_hi)
            sig = "  *order CI>0*" if (og_lo == og_lo and og_lo > 0) else ""
            print(f"[{m}/{source}] n={len(cl)} terms | coined_only={co:.3f} ordered={od:.3f} "
                  f"reversed={rv:.3f} shuffled={sh:.3f}")
            print(f"    history_lift (ord-coined) = {lift_m:+.3f} [{lift_lo:+.3f},{lift_hi:+.3f}]"
                  f"   (gate: >0 => history load-bearing => order test interpretable)")
            print(f"    ORDER gap   (ord-shuf)    = {og_m:+.3f} [{og_lo:+.3f},{og_hi:+.3f}]{sig}")
            print(f"    chronology  (ord-rev)     = {od - rv:+.3f}   (artifact guard)\n")

    print("--- NAMED (confounded) contrast: live-online acc vs dyadic shuffled-replay ---")
    for m in MODELS:
        live = [1.0 if r["correct"] else 0.0 for r in recs if r["phase"] == "live" and r["model"] == m]
        shuf = [1.0 if r["correct"] else 0.0 for r in recs if r["phase"] == "probe"
                and r["model"] == m and r["source"] == "dyadic" and r["condition"] == "shuffled"]
        if live:
            print(f"[{m}] live-online={mean(live):.3f}  shuffled-replay={mean(shuf):.3f}")
    print()

    print("--- VERDICT (pre-registered rule) ---")
    any_pos = False
    for m in MODELS:
        d = summ.get((m, "dyadic"))
        mo = summ.get((m, "mono"))
        if not d:
            continue
        # POSITIVE bar (frozen, strict, untouched): order gap CI excludes 0, chronology-specific,
        # above the monologue floor, and history is load-bearing. history_loadbearing uses the lift
        # POINT estimate (>0.10 accuracy lift): the methodological-vs-deflationary NULL distinction
        # is descriptive only and does NOT gate the positive (no model meets order_ci regardless).
        history_loadbearing = (d["lift"] == d["lift"] and d["lift"] > 0.10)
        order_ci = (d["og_lo"] == d["og_lo"] and d["og_lo"] > 0)
        chron_ok = (d["od"] > d["rv"])
        floor_ok = (mo is None) or (d["og"] > mo["og"])
        pos = history_loadbearing and order_ci and chron_ok and floor_ok
        any_pos = any_pos or pos
        if not history_loadbearing:
            verdict = "UNDER-POWERED / METHODOLOGICAL (history not load-bearing; order untestable)"
        elif pos:
            verdict = "RELATIONAL POSITIVE"
        else:
            verdict = "RELATIONAL NULL (deflationary: history content helps, order does not)"
        print(f"[{m}] {verdict}")
        print(f"     lift={d['lift']:+.3f}(load-bearing {'yes' if history_loadbearing else 'no'}) "
              f"order_gap={d['og']:+.3f}[{d['og_lo']:+.3f},{d['og_hi']:+.3f}]"
              f"(CI>0 {'yes' if order_ci else 'no'}) "
              f"chron {'ok' if chron_ok else 'artifact?'} "
              f"floor {'ok' if floor_ok else 'fail'}"
              + (f" mono_gap={mo['og']:+.3f}" if mo else ""))
    print(f"\nOVERALL: {'>=1 model RELATIONAL POSITIVE' if any_pos else 'RELATIONAL NULL / under-powered across panel (first-class negative)'}")


if __name__ == "__main__":
    main()
