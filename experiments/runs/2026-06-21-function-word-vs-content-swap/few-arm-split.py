#!/usr/bin/env python3
"""few-arm-split.py — re-analysis of the `few`->`many` function-word arm.

No model API calls, no spend: re-reads the raw NLI records already in-repo and
locates the cross-model panel split documented in
result/function-word-swap-run-v2 to ONE quantifier reading.

For each model, over the 126 `few`-arm items (arm==matched, ftype==few), per item:
  base = NLI(premise_base="Few X ...", hyp_base="All of the X ...")
  fn   = NLI(premise_fn ="Many X ...", hyp_base="All of the X ...")
NLI label encoding (from probe.py): 0=entailment, 1=neutral, 2=contradiction.
flip_fn = (fn label != base label).

Outputs:
  - few-arm-split.json  (machine-readable, per model)
  - a printed table to stdout
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
LABELS = {0: "entailment", 1: "neutral", 2: "contradiction"}
MODELS = ["claude", "gpt", "gemini"]


def load_few_ids():
    items = json.load(open(os.path.join(HERE, "stimuli.json")))["items"]
    few = [x for x in items if x["arm"] == "matched" and x["ftype"] == "few"]
    return {x["id"] for x in few}


def load_records(model):
    path = os.path.join(HERE, "raw", f"{model}-nli.json")
    recs = json.load(open(path))
    return recs


def analyze(model, few_ids):
    recs = load_records(model)
    # index by (id, cond) -> int label, restricted to the few arm
    by_id = {}
    for r in recs:
        if r.get("ftype") != "few" or r.get("arm") != "matched":
            continue
        if r["id"] not in few_ids:
            continue
        if r["cond"] not in ("base", "fn"):
            continue
        by_id.setdefault(r["id"], {})[r["cond"]] = int(r["value"])

    base_dist = {0: 0, 1: 0, 2: 0}
    fn_dist = {0: 0, 1: 0, 2: 0}
    joint = {}  # (base_label, fn_label) -> count
    flips = 0
    n = 0
    for iid, d in by_id.items():
        if "base" not in d or "fn" not in d:
            continue
        b, f = d["base"], d["fn"]
        n += 1
        base_dist[b] += 1
        fn_dist[f] += 1
        joint[(b, f)] = joint.get((b, f), 0) + 1
        if f != b:
            flips += 1

    return {
        "model": model,
        "n": n,
        "flip_fn": round(flips / n, 4) if n else None,
        "base_dist": {LABELS[k]: v for k, v in base_dist.items() if v},
        "fn_dist": {LABELS[k]: v for k, v in fn_dist.items() if v},
        "joint": {
            f"{LABELS[bk][:3]}->{LABELS[fk][:3]}": joint[(bk, fk)]
            for (bk, fk) in sorted(joint)
        },
    }


def main():
    few_ids = load_few_ids()
    out = {"few_n_items": len(few_ids), "label_encoding": LABELS, "models": {}}
    for m in MODELS:
        out["models"][m] = analyze(m, few_ids)

    json.dump(out, open(os.path.join(HERE, "few-arm-split.json"), "w"), indent=2)

    # Printed table
    print(f"few arm: {len(few_ids)} items (arm==matched, ftype==few)")
    print("base = NLI(Few X -> All X) ; fn = NLI(Many X -> All X)")
    print("label encoding: 0=entailment 1=neutral 2=contradiction\n")
    hdr = f"{'model':8} {'n':>4} {'flip_fn':>8}  {'base dist':28} {'fn dist':28} joint transitions"
    print(hdr)
    print("-" * len(hdr))
    for m in MODELS:
        a = out["models"][m]
        bd = ", ".join(f"{k}:{v}" for k, v in a["base_dist"].items())
        fd = ", ".join(f"{k}:{v}" for k, v in a["fn_dist"].items())
        jt = ", ".join(f"{k}:{v}" for k, v in a["joint"].items())
        print(f"{m:8} {a['n']:>4} {a['flip_fn']:>8}  {bd:28} {fd:28} {jt}")


if __name__ == "__main__":
    main()
