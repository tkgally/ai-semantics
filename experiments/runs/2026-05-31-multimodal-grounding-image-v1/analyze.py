#!/usr/bin/env python3
"""Analyze multimodal-grounding-image-v1 (the frozen DV from PREREG).

For each model x framing:
  - ΔR separation = mean(rating | gold=same) - mean(rating | gold=different), per condition
  - the image-vs-text change in separation: Δsep = ΔR_image - ΔR_text  (prediction 2 ⇒ > 0)
  - per-item paired image-text rating diff, split by stratum (distinct-F vs same-T)
  - AUC of rating discriminating same vs different, per condition
  - distraction control: mean image-text diff on the same-T stratum (should be ~0; <0 = contamination)
  - cluster bootstrap CI over the 12 items for Δsep and for the prediction-3 contrast
Ratings: 4-pt and 0-100 analyzed on their own scales (reported separately). No pass bar.
"""
import json, os, statistics, random
HERE = os.path.dirname(os.path.abspath(__file__))
random.seed(20260531)

def load():
    return json.load(open(os.path.join(HERE, "raw", "results.json")))

def auc(pos, neg):
    # prob a random 'same' rating > a random 'different' rating (ties=0.5)
    if not pos or not neg:
        return float("nan")
    c = sum((1 if p > n else 0.5 if p == n else 0) for p in pos for n in neg)
    return c / (len(pos) * len(neg))

def cell(recs, model, framing, condition):
    rs = [r for r in recs if r["model"] == model and r["framing"] == framing
          and r["condition"] == condition and r["rating"] is not None]
    same = [r["rating"] for r in rs if r["gold"] == "same"]
    diff = [r["rating"] for r in rs if r["gold"] == "different"]
    return same, diff

def item_rating(recs, item_id, model, framing, condition):
    for r in recs:
        if (r["item_id"] == item_id and r["model"] == model and r["framing"] == framing
                and r["condition"] == condition):
            return r["rating"]
    return None

def main():
    recs = load()
    items = sorted({r["item_id"] for r in recs})
    strata = {r["item_id"]: r["stratum"] for r in recs}
    models = ["claude", "gpt", "gemini"]
    out = []
    n_na = sum(1 for r in recs if r["rating"] is None)
    out.append(f"total calls={len(recs)}  parse-fails(NA)={n_na}")
    for framing in ("durel", "scale"):
        out.append(f"\n================ framing: {framing} ================")
        for model in models:
            sT, dT = cell(recs, model, framing, "text")
            sI, dI = cell(recs, model, framing, "image")
            sepT = (statistics.mean(sT) - statistics.mean(dT)) if sT and dT else float("nan")
            sepI = (statistics.mean(sI) - statistics.mean(dI)) if sI and dI else float("nan")
            aucT, aucI = auc(sT, dT), auc(sI, dI)
            # per-item paired image-text diff by stratum
            diffs = {"distinct-F": [], "same-T": []}
            for it in items:
                rt = item_rating(recs, it, model, framing, "text")
                ri = item_rating(recs, it, model, framing, "image")
                if rt is not None and ri is not None:
                    diffs[strata[it]].append(ri - rt)
            mdF = statistics.mean(diffs["distinct-F"]) if diffs["distinct-F"] else float("nan")
            mdT = statistics.mean(diffs["same-T"]) if diffs["same-T"] else float("nan")
            # bootstrap CI for Δsep = sepI - sepT over items
            def boot_delta_sep():
                est = []
                for _ in range(2000):
                    samp = [random.choice(items) for _ in items]
                    def msep(cond):
                        ss, dd = [], []
                        for it in samp:
                            r = item_rating(recs, it, model, framing, cond)
                            if r is None:
                                continue
                            (ss if strata_gold(recs, it) == "same" else dd).append(r)
                        return (statistics.mean(ss) - statistics.mean(dd)) if ss and dd else None
                    a, b = msep("image"), msep("text")
                    if a is not None and b is not None:
                        est.append(a - b)
                est.sort()
                if len(est) < 20:
                    return (float("nan"), float("nan"))
                return est[int(.025*len(est))], est[int(.975*len(est))]
            lo, hi = boot_delta_sep()
            out.append(f"\n  [{model}]")
            out.append(f"    sep(same-diff): text={sepT:+.3f}  image={sepI:+.3f}  "
                       f"Δsep(img-txt)={sepI-sepT:+.3f}  CI95=[{lo:+.3f},{hi:+.3f}]")
            out.append(f"    AUC(same>diff): text={aucT:.3f}  image={aucI:.3f}")
            out.append(f"    mean image-text rating diff: distinct-F={mdF:+.3f}  same-T(distraction ctrl)={mdT:+.3f}")
            out.append(f"      prediction-3 contrast (distinctF push-apart vs sameT): {(-mdF)-(-mdT):+.3f}  "
                       f"[want distinct-F to DROP (mdF<0) more than same-T]")
    print("\n".join(out))
    open(os.path.join(HERE, "analysis.txt"), "w").write("\n".join(out))

# gold lookup helper
_GOLD = {}
def strata_gold(recs, item_id):
    if not _GOLD:
        for r in recs:
            _GOLD[r["item_id"]] = r["gold"]
    return _GOLD[item_id]

if __name__ == "__main__":
    main()
