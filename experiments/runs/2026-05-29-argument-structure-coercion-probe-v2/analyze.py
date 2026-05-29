"""Analyze the off-ceiling argument-structure coercion v2 probe (2026-05-29).

Indicator: affirm-construction-inference rate (FC YES, or NLI label 0 = entailment).
Per construction (caused-motion, way) x condition (canonical d1, resist d2, cue d3):
  - canonical affirm rate  (expect high / ~ceiling -> replicates v1; the anchor)
  - cue affirm rate        (KEY: low = cue-respecting/H-deep; high = template/H-default)
  - canonical - cue DROP   (the discriminator)
  - resist affirm rate     (anomalous coercion; mechanical affirm = H-default)
  - degradation shape across d1<d2<d3 (monotone shallow = graceful; flat-then-cliff = brittle)

Reading rule (RATIFIED cc-v2-difficulty-operationalization, report-the-rate):
  cue affirm >=70% in >=2/3 models = robustly template / cue-ignoring (H-default);
  ~chance / low = cue-respecting (H-deep). No pass bar that manufactures a result;
  the null in either direction is first-class. No threshold retuned after the run.
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
PANEL = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}


def affirm(arm, pred):
    if pred is None:
        return None
    return pred == "0" if arm == "nli" else pred == "YES"


def rate(recs):
    vals = [r["affirm"] for r in recs if r["affirm"] is not None]
    return (round(sum(vals) / len(vals) * 100, 1), len(vals)) if vals else (None, 0)


def main():
    out = {"per_model": {}, "reading_rule": "cue affirm >=70% in >=2/3 = template/H-default; "
           "~chance/low = cue-respecting/H-deep (report-the-rate, ratified)"}
    print("\n===== ARGUMENT-STRUCTURE COERCION v2 — affirm-construction-inference rate =====")
    print("KEY = cue affirm rate (low=H-deep/cue-respecting; high=H-default/template) + canonical-cue drop.\n")
    for slot, name in PANEL.items():
        m = {"model": name}
        for arm in ("nli", "fc"):
            recs = json.load(open(os.path.join(RAW, f"{arm}_{slot}.json")))
            for r in recs:
                r["affirm"] = affirm(arm, r["pred"])
            for con in ("caused-motion", "way"):
                cr = [r for r in recs if r["construction"] == con]
                byc = {c: [r for r in cr if r["condition"] == c]
                       for c in ("canonical", "resist", "cue")}
                canon, _ = rate(byc["canonical"])
                resist, _ = rate(byc["resist"])
                cue, _ = rate(byc["cue"])
                drop = None if canon is None or cue is None else round(canon - cue, 1)
                # degradation monotone? canonical>=resist>=cue
                seq = [x for x in (canon, resist, cue) if x is not None]
                monotone = all(seq[i] >= seq[i+1] for i in range(len(seq)-1)) if len(seq) == 3 else None
                m[f"{con}_{arm}"] = {"canonical": canon, "resist": resist, "cue": cue,
                                     "canonical_minus_cue_drop": drop, "monotone_decline": monotone}
        out["per_model"][slot] = m
        for con in ("caused-motion", "way"):
            for arm in ("nli", "fc"):
                a = m[f"{con}_{arm}"]
                print(f"[{name:<18} {con:<13} {arm.upper():<3}] canon={a['canonical']}%  "
                      f"resist={a['resist']}%  cue={a['cue']}%  DROP={a['canonical_minus_cue_drop']}pp  "
                      f"monotone={a['monotone_decline']}")
        print()
    # cross-model cue summary
    print("--- cue affirm rate (the discriminator), per construction/instrument ---")
    for con in ("caused-motion", "way"):
        for arm in ("nli", "fc"):
            cues = [out["per_model"][s][f"{con}_{arm}"]["cue"] for s in PANEL]
            n_template = sum(1 for c in cues if c is not None and c >= 70)
            print(f"  {con:<13} {arm.upper():<3}: cue affirm = {cues}  -> >=70% (template) in {n_template}/3 models")
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
