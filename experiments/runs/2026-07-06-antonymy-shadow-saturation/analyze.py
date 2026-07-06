#!/usr/bin/env python3
"""analyze.py — scoring + verdict for the A1b antonymy shadow-saturation probe.

Recomputes everything from raw/ + items.json + control.json. No thresholds are tuned here
after seeing results (anti-cheat); the verdict map is the one frozen in PREREG.md.

Metrics (Q2-A, ratified):
- 𝒮(model, rel) = mean over cues of Soundness = (produced words that are WordNet gold) /
  (words produced), Cao's Soundness (precision over produced). 0-produced cue -> NA (dropped).
- 𝒮(control, rel, variant) = same, over the control's top-k co-occurrence candidates.
- residual(rel, model, variant) = 𝒮(model, neutral) − 𝒮(control, variant).
  PRIMARY variant = frame (contrastive-frame G²); SENSITIVITY = sent (all-intrasentential G²).
- Verdict (frozen): CONFIRMS iff antonymy has the SMALLEST residual on >=2/3 models with
  meronymy and/or hyponymy visibly larger; SHADOW-SATURATED-FLAT iff residuals flat (the
  antonymy residual's 95% CI overlaps every other relation's on >=2/3 models); INVERTED iff a
  weakly-cued relation (meronymy/holonymy) has the smallest residual on >=2/3.
- Clause-2 (secondary): Spearman of the raw-𝒮(model) relation ranking vs the corpus
  cue-strength ranking (= 𝒮(control, frame) per relation, the 6-relation ranking the corpus
  supplies — condition 1 route (a)); antonymy predicted top of both.
- Frame-ablation (descriptive): antonymy 𝒮(model, frame) − 𝒮(model, neutral), per model.

Bootstrap 95% CIs over cues (percentile, B=2000, seed fixed).
"""
import json
import math
import os
import random
from pathlib import Path

HERE = Path(__file__).parent
RELS = ["antonymy", "synonymy", "hypernymy", "hyponymy", "holonymy", "meronymy"]
SLOTS = ["A", "B", "C"]
B_BOOT = 2000
BOOT_SEED = 20260706


def soundness(produced, gold):
    if not produced:
        return None
    hits = sum(1 for w in produced if w in gold)
    return hits / len(produced)


def load_gold():
    items = json.load(open(HERE / "items.json"))
    gold = {}
    order = {}
    for r in RELS:
        order[r] = [it["cue"] for it in items["items"][r]]
        for it in items["items"][r]:
            gold[(r, it["cue"])] = set(it["gold"])
    return gold, order, items


def control_scores(order, gold):
    """Per (rel, variant): dict cue -> 𝒮(control)."""
    ctrl = json.load(open(HERE / "control.json"))["cues"]
    out = {}
    for r in RELS:
        for variant in ("frame", "sent"):
            d = {}
            for cue in order[r]:
                cand = [v for v, g, o in ctrl.get(cue, {}).get(variant, [])]
                d[cue] = soundness(cand, gold[(r, cue)])
            out[(r, variant)] = d
    return out


def model_scores(gold, order):
    """Per (slot, rel, arm): dict cue -> 𝒮(model)."""
    out = {}
    miss = {}
    for slot in SLOTS:
        for r in RELS:
            for arm in (("neutral", "frame") if r == "antonymy" else ("neutral",)):
                f = HERE / "raw" / f"{slot}-{r}-{arm}.json"
                if not f.exists():
                    continue
                rows = json.load(open(f))
                d = {}
                empt = 0
                for row in rows:
                    if not row["words"]:
                        empt += 1
                    d[row["cue"]] = soundness(row["words"], gold[(r, row["cue"])])
                out[(slot, r, arm)] = d
                miss[(slot, r, arm)] = empt
    return out, miss


def mean_ci(vals):
    v = [x for x in vals if x is not None]
    if not v:
        return None, None, None, 0
    m = sum(v) / len(v)
    rng = random.Random(BOOT_SEED)
    boots = []
    n = len(v)
    for _ in range(B_BOOT):
        s = sum(v[rng.randrange(n)] for _ in range(n)) / n
        boots.append(s)
    boots.sort()
    return m, boots[int(0.025 * B_BOOT)], boots[int(0.975 * B_BOOT)], len(v)


def residual_ci(model_d, ctrl_d):
    """Paired residual per cue then bootstrap; cues where either is NA are dropped."""
    diffs = []
    for cue in model_d:
        mv, cv = model_d[cue], ctrl_d.get(cue)
        if mv is None or cv is None:
            continue
        diffs.append(mv - cv)
    if not diffs:
        return None, None, None, 0
    m = sum(diffs) / len(diffs)
    rng = random.Random(BOOT_SEED)
    n = len(diffs)
    boots = []
    for _ in range(B_BOOT):
        boots.append(sum(diffs[rng.randrange(n)] for _ in range(n)) / n)
    boots.sort()
    return m, boots[int(0.025 * B_BOOT)], boots[int(0.975 * B_BOOT)], n


def spearman(a, b):
    def rank(x):
        idx = sorted(range(len(x)), key=lambda i: x[i])
        r = [0] * len(x)
        for pos, i in enumerate(idx):
            r[i] = pos
        return r
    ra, rb = rank(a), rank(b)
    n = len(a)
    d2 = sum((ra[i] - rb[i]) ** 2 for i in range(n))
    return 1 - 6 * d2 / (n * (n * n - 1))


def main():
    gold, order, items = load_gold()
    ctrl = control_scores(order, gold)
    mod, miss = model_scores(gold, order)

    report = {"n_per_rel": items["n_per_rel"], "relations": RELS,
              "raw_soundness": {}, "control_soundness": {}, "residual": {},
              "frame_ablation": {}, "clause2_spearman": {}, "verdict": {}}

    # raw 𝒮(model, neutral) + control 𝒮 per relation
    for slot in SLOTS:
        report["raw_soundness"][slot] = {}
        for r in RELS:
            d = mod.get((slot, r, "neutral"), {})
            m, lo, hi, n = mean_ci(list(d.values()))
            report["raw_soundness"][slot][r] = {"mean": m, "ci": [lo, hi], "n": n,
                                                "empty": miss.get((slot, r, "neutral"), 0)}
    for variant in ("frame", "sent"):
        report["control_soundness"][variant] = {}
        for r in RELS:
            m, lo, hi, n = mean_ci(list(ctrl[(r, variant)].values()))
            report["control_soundness"][variant][r] = {"mean": m, "ci": [lo, hi], "n": n}

    # residuals (primary=frame, sensitivity=sent)
    for variant in ("frame", "sent"):
        report["residual"][variant] = {}
        for slot in SLOTS:
            report["residual"][variant][slot] = {}
            for r in RELS:
                md = mod.get((slot, r, "neutral"), {})
                cd = ctrl[(r, variant)]
                m, lo, hi, n = residual_ci(md, cd)
                report["residual"][variant][slot][r] = {"mean": m, "ci": [lo, hi], "n": n}

    # frame-ablation (antonymy): 𝒮(frame) − 𝒮(neutral) per model
    for slot in SLOTS:
        nd = mod.get((slot, "antonymy", "neutral"), {})
        fd = mod.get((slot, "antonymy", "frame"), {})
        diffs = [fd[c] - nd[c] for c in nd if c in fd and nd[c] is not None and fd[c] is not None]
        if diffs:
            m = sum(diffs) / len(diffs)
            rng = random.Random(BOOT_SEED)
            n = len(diffs)
            boots = sorted(sum(diffs[rng.randrange(n)] for _ in range(n)) / n for _ in range(B_BOOT))
            report["frame_ablation"][slot] = {
                "mean_delta": m, "ci": [boots[int(0.025*B_BOOT)], boots[int(0.975*B_BOOT)]],
                "n": n,
                "s_neutral": sum(nd[c] for c in nd if nd[c] is not None)/max(1, sum(1 for c in nd if nd[c] is not None)),
                "s_frame": sum(fd[c] for c in fd if fd[c] is not None)/max(1, sum(1 for c in fd if fd[c] is not None))}

    # clause-2: raw-𝒮(model) ranking vs corpus cue-strength (𝒮 control frame) ranking
    cue_strength = [report["control_soundness"]["frame"][r]["mean"] or 0.0 for r in RELS]
    for slot in SLOTS:
        raw = [report["raw_soundness"][slot][r]["mean"] or 0.0 for r in RELS]
        rho = spearman(raw, cue_strength)
        ant_top_raw = RELS[max(range(6), key=lambda i: raw[i])] == "antonymy"
        report["clause2_spearman"][slot] = {"rho": rho, "antonymy_top_raw": ant_top_raw}
    report["clause2_spearman"]["antonymy_top_cue_strength"] = (
        RELS[max(range(6), key=lambda i: cue_strength[i])] == "antonymy")

    # verdict per model + overall (PRIMARY = frame residual)
    def smallest(slot, variant):
        res = report["residual"][variant][slot]
        vals = {r: res[r]["mean"] for r in RELS if res[r]["mean"] is not None}
        return min(vals, key=vals.get) if vals else None

    def flat(slot, variant):
        res = report["residual"][variant][slot]
        a = res["antonymy"]
        if a["mean"] is None:
            return False
        overlaps = 0
        for r in RELS:
            if r == "antonymy":
                continue
            o = res[r]
            if o["mean"] is None:
                continue
            # CI overlap
            if not (a["ci"][1] < o["ci"][0] or o["ci"][1] < a["ci"][0]):
                overlaps += 1
        return overlaps == 5  # antonymy indistinguishable from all others

    for variant in ("frame", "sent"):
        sm = {slot: smallest(slot, variant) for slot in SLOTS}
        n_ant_smallest = sum(1 for s in SLOTS if sm[s] == "antonymy")
        n_flat = sum(1 for s in SLOTS if flat(s, variant))
        n_inverted = sum(1 for s in SLOTS if sm[s] in ("meronymy", "holonymy"))
        if n_ant_smallest >= 2:
            v = "CONFIRMS"
        elif n_flat >= 2:
            v = "SHADOW-SATURATED-FLAT"
        elif n_inverted >= 2:
            v = "INVERTED"
        else:
            v = "MIXED/NO-MAJORITY"
        report["verdict"][variant] = {"smallest_per_model": sm,
                                      "antonymy_smallest_count": n_ant_smallest,
                                      "flat_count": n_flat, "inverted_count": n_inverted,
                                      "verdict": v}

    json.dump(report, open(HERE / "results.json", "w"), indent=1)

    # human-readable
    print("=" * 70)
    print("PRIMARY residual (frame-G²): 𝒮(model,neutral) − 𝒮(control,frame)")
    for slot in SLOTS:
        print(f"\n model {slot}:")
        res = report["residual"]["frame"][slot]
        for r in RELS:
            o = res[r]
            if o["mean"] is not None:
                print(f"   {r:12s} resid={o['mean']:+.3f} [{o['ci'][0]:+.3f},{o['ci'][1]:+.3f}] "
                      f"(raw 𝒮={report['raw_soundness'][slot][r]['mean']:.3f}, "
                      f"ctrl 𝒮={report['control_soundness']['frame'][r]['mean']:.3f})")
        print(f"   smallest residual: {report['verdict']['frame']['smallest_per_model'][slot]}")
    print("\nVERDICT (frame, primary):", report["verdict"]["frame"]["verdict"],
          report["verdict"]["frame"])
    print("VERDICT (sent, sensitivity):", report["verdict"]["sent"]["verdict"])
    print("\nClause-2 (raw ranking vs corpus cue-strength):")
    for slot in SLOTS:
        c = report["clause2_spearman"][slot]
        print(f"   {slot}: rho={c['rho']:+.3f} antonymy_top_raw={c['antonymy_top_raw']}")
    print("   antonymy top of cue-strength:", report["clause2_spearman"]["antonymy_top_cue_strength"])
    print("\nFrame-ablation (antonymy 𝒮frame − 𝒮neutral):")
    for slot in SLOTS:
        fa = report["frame_ablation"].get(slot)
        if fa:
            print(f"   {slot}: Δ={fa['mean_delta']:+.3f} [{fa['ci'][0]:+.3f},{fa['ci'][1]:+.3f}] "
                  f"(neutral {fa['s_neutral']:.3f} → frame {fa['s_frame']:.3f})")
    print("\nresults.json written.")


if __name__ == "__main__":
    main()
