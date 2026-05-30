"""Analyze the implicit-world-knowledge caused-motion cue probe (v2b, 2026-05-30).

Indicator: affirm-caused-motion rate (FC YES, or NLI label 0 = entailment) on
"<subj>'s <gerund> caused <obj> to move".

Per model x instrument:
  canonical_affirm     (light object; expect ~ceiling -> the v1/v2 anchor)
  implicit_wk_affirm   (immovable object via in-premise descriptor; NO outcome stated)
  explicit_affirm      (immovable object + explicit outcome denial; the v2-style calibration)
KEY discriminator:
  implicit_minus_explicit = implicit_wk_affirm - explicit_affirm
     ~0  => model blocks the impossible coercion from world knowledge alone (strong H-deep)
     >0  => model needs the explicit outcome statement (world knowledge alone insufficient)
  canonical_to_implicit_drop, canonical_to_explicit_drop  (the two cue strengths)

Reading rule (RATIFIED report-the-rate): no manufactured pass bar; headline is the
implicit-vs-explicit gap + the two drops, per instrument. The NLI-vs-FC gap on the
implicit-wk cell is itself reported (premise-internal NLI may affirm; FC engages world
knowledge). No threshold tuned after the run.
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
    out = {"per_model": {}, "indicator": "affirm-caused-motion rate",
           "reading_rule": "report-the-rate; headline = implicit-wk vs explicit gap + "
           "canonical->cue drops, per instrument (no pass bar)"}
    print("\n===== IMPLICIT-WK CAUSED-MOTION CUE v2b — affirm-caused-motion rate =====")
    print("canonical(light obj)=ceiling anchor; implicit-wk(immovable, no outcome)=world-"
          "knowledge test; explicit(immovable + outcome denial)=v2-style calibration.\n")
    for slot, name in PANEL.items():
        m = {"model": name}
        for arm in ("nli", "fc"):
            recs = json.load(open(os.path.join(RAW, f"{arm}_{slot}.json")))
            for r in recs:
                r["affirm"] = affirm(arm, r["pred"])
            byc = {c: [r for r in recs if r["condition"] == c]
                   for c in ("canonical", "implicit-wk", "explicit")}
            canon, _ = rate(byc["canonical"])
            impl, _ = rate(byc["implicit-wk"])
            expl, _ = rate(byc["explicit"])
            ime = None if (impl is None or expl is None) else round(impl - expl, 1)
            d_i = None if (canon is None or impl is None) else round(canon - impl, 1)
            d_e = None if (canon is None or expl is None) else round(canon - expl, 1)
            m[arm] = {"canonical": canon, "implicit_wk": impl, "explicit": expl,
                      "implicit_minus_explicit": ime,
                      "canonical_to_implicit_drop": d_i, "canonical_to_explicit_drop": d_e}
        out["per_model"][slot] = m
        for arm in ("nli", "fc"):
            a = m[arm]
            print(f"[{name:<18} {arm.upper():<3}] canon={a['canonical']}%  "
                  f"implicit-wk={a['implicit_wk']}%  explicit={a['explicit']}%  | "
                  f"impl-expl={a['implicit_minus_explicit']}pp  "
                  f"drop(canon->impl)={a['canonical_to_implicit_drop']}pp  "
                  f"drop(canon->expl)={a['canonical_to_explicit_drop']}pp")
        print()
    print("--- key discriminator: implicit-wk vs explicit affirm (per instrument) ---")
    for arm in ("nli", "fc"):
        impl = [out["per_model"][s][arm]["implicit_wk"] for s in PANEL]
        expl = [out["per_model"][s][arm]["explicit"] for s in PANEL]
        print(f"  {arm.upper():<3}: implicit-wk = {impl}  | explicit = {expl}")
    json.dump(out, open(os.path.join(RAW, "results.json"), "w"), indent=1)
    print(f"\nwrote {os.path.join(RAW, 'results.json')}")


if __name__ == "__main__":
    main()
