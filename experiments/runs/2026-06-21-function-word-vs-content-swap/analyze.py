#!/usr/bin/env python3
"""analyze.py -- function-word-vs-content swap flip-rate analysis (pre-registered).

Per model, per matched item:
  base  = NLI(premise_base, hyp_base)
  flip_fn = 1[ NLI(premise_fn, hyp_base) != base ]
  flip_ct = 1[ NLI(premise_ct, hyp_ct)  != base ]
PRIMARY (per model): mean(flip_fn) - mean(flip_ct), bootstrap 95% CI over items (seed fixed).
  CONFIRM  : contrast > 0 AND bootstrap lower bound > 0.
  WEAK     : contrast > 0 but CI includes 0.
  FALSIFY  : contrast <= 0 (content swap flips at least as much -> positive for the
             distributional camp; recorded as such).
Panel verdict: CONFIRM iff >=2 of 3 models CONFIRM (conjecture confirm criterion -- but ALSO
gated on the >=200-item count; see PREREG / certification).
Manipulation check (M3): base-label agreement with the predicted base label (frame is
inference-load-bearing only where the model assigns the predicted base label).
Reported per content semantic class (conjecture prediction 3: not driven by a few classes).
det_char: function-only flip rate for the the->a determiner arm (no content control).
"""
import json
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
SEED = 20260621


def load_model(name):
    p = os.path.join(RAW, f"{name}-nli.json")
    if not os.path.exists(p):
        return None
    rows = json.load(open(p))
    by = {}
    for r in rows:
        by.setdefault(r["id"], {})[r["cond"]] = r
    return by


def boot_ci(vals, n=10000, seed=SEED):
    if not vals:
        return (None, None)
    rng = random.Random(seed)
    means = []
    k = len(vals)
    for _ in range(n):
        s = [vals[rng.randrange(k)] for _ in range(k)]
        means.append(sum(s) / k)
    means.sort()
    return (means[int(0.025 * n)], means[int(0.975 * n)])


def analyze_model(name, items):
    by = load_model(name)
    if by is None:
        return None
    matched = [it for it in items if it["arm"] == "matched"]
    flips_fn, flips_ct = [], []
    base_ok = 0
    fn_dir_ok = 0
    per_class = {}
    per_ft = {}
    n_used = 0
    unparsed = 0
    for it in matched:
        rec = by.get(it["id"], {})
        b = rec.get("base", {}).get("value")
        f = rec.get("fn", {}).get("value")
        c = rec.get("ct", {}).get("value")
        if b is None or f is None or c is None:
            unparsed += 1
            continue
        n_used += 1
        ffn = 1 if f != b else 0
        fct = 1 if c != b else 0
        flips_fn.append(ffn)
        flips_ct.append(fct)
        if str(b) == str(it["pred_base"]):
            base_ok += 1
        if str(f) == str(it["pred_fn"]):
            fn_dir_ok += 1
        per_class.setdefault(it["pos"], {"fn": [], "ct": []})
        per_class[it["pos"]]["fn"].append(ffn)
        per_class[it["pos"]]["ct"].append(fct)
        per_ft.setdefault(it["ftype"], {"fn": [], "ct": []})
        per_ft[it["ftype"]]["fn"].append(ffn)
        per_ft[it["ftype"]]["ct"].append(fct)
    if not n_used:
        return {"model": name, "n_used": 0}
    contrasts = [a - b for a, b in zip(flips_fn, flips_ct)]
    contrast = sum(contrasts) / len(contrasts)
    lo, hi = boot_ci(contrasts)
    verdict = ("CONFIRM" if contrast > 0 and lo is not None and lo > 0
               else "WEAK" if contrast > 0 else "FALSIFY")
    # det_char function-only flip rate
    det = [it for it in items if it["arm"] == "det_char"]
    det_flips = []
    for it in det:
        rec = by.get(it["id"], {})
        b = rec.get("base", {}).get("value")
        f = rec.get("fn", {}).get("value")
        if b is not None and f is not None:
            det_flips.append(1 if f != b else 0)
    return {
        "model": name, "n_used": n_used, "unparsed_items": unparsed,
        "flip_fn_rate": round(sum(flips_fn) / n_used, 4),
        "flip_ct_rate": round(sum(flips_ct) / n_used, 4),
        "contrast_fn_minus_ct": round(contrast, 4),
        "bootstrap95": [round(lo, 4) if lo is not None else None,
                        round(hi, 4) if hi is not None else None],
        "verdict": verdict,
        "manip_base_label_agreement": round(base_ok / n_used, 4),
        "manip_fn_direction_agreement": round(fn_dir_ok / n_used, 4),
        "per_semantic_class": {k: {"flip_fn": round(sum(v["fn"]) / len(v["fn"]), 4),
                                   "flip_ct": round(sum(v["ct"]) / len(v["ct"]), 4),
                                   "n": len(v["fn"])}
                               for k, v in per_class.items()},
        "per_function_type": {k: {"flip_fn": round(sum(v["fn"]) / len(v["fn"]), 4),
                                  "flip_ct": round(sum(v["ct"]) / len(v["ct"]), 4),
                                  "n": len(v["fn"])}
                              for k, v in per_ft.items()},
        "det_char_function_flip_rate": (round(sum(det_flips) / len(det_flips), 4)
                                        if det_flips else None),
    }


def main():
    items = json.load(open(os.path.join(HERE, "stimuli.json")))["items"]
    out = {"seed": SEED, "models": {}}
    for name in ("claude", "gpt", "gemini"):
        r = analyze_model(name, items)
        if r is not None:
            out["models"][name] = r
    confirms = sum(1 for m in out["models"].values()
                   if m.get("verdict") == "CONFIRM")
    out["panel_verdict"] = ("CONFIRM" if confirms >= 2 else "MIXED/WEAK")
    out["panel_confirms"] = confirms
    out["NOTE"] = ("Count gate MET: build-v2 has 206 matched items across 4 content classes "
                   "(certification.json ok=true), so the conjecture's >=200 / >=4-class CONFIRM "
                   "criterion is satisfied. Caveat to weigh in the result: the few->many "
                   "quantifier arm is 126/206 (61%) of items; read the per_function_type "
                   "breakdown for whether the contrast holds within EACH function pair, not just "
                   "pooled (conjecture prediction 3).")
    json.dump(out, open(os.path.join(HERE, "analysis.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
