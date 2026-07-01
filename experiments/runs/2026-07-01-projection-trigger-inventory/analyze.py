#!/usr/bin/env python3
"""analyze.py — scoring + verdict for the presupposition / projection probe. NO API CALLS.

Reads raw/*.json. For each item the model answered YES / NO / UNCLEAR; `endorsed` == the answer
parses to YES. Per (model), over the frozen 96 conditions:

  plain_presup_endorse  — P-endorse rate in the PLAIN frame (sanity: should be high).
  plain_entail_endorse  — E-endorse rate in the PLAIN frame (sanity: should be high).
  presup_survival       — P-endorse rate over the 3 CANCELLING frames (neg / question / cond).
  entail_survival       — E-endorse rate over the 3 CANCELLING frames.
  projection_gap        — presup_survival - entail_survival (the within-model projection signal).

VERDICT (thresholds pre-registered in PREREG.md — NOT tuned here):
  SANITY = 0.75   per-model plain-frame floor on BOTH P and E; a model below it is control-FAILED
                  (its cancelling-frame contrast is uninterpretable).
  SURVIVE = 0.60  per-model presup_survival floor for a projection reading.
  GAP = 0.30      per-model projection_gap floor for a projection reading.
  FLATBAND = 0.15 per-model |projection_gap| below which the two legs are "flat" (no projection).

  PROJECTION : >= 2 of 3 models pass SANITY AND have presup_survival >= SURVIVE AND
               projection_gap >= GAP.
  FLAT/NULL  : >= 2 of 3 models pass SANITY AND have |projection_gap| < FLATBAND.
  MIXED      : anything else (sanity failures, split panel, or partial signal).

Usage: python3 analyze.py     # prints per-model tables + verdict; writes results.json
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent

SANITY = 0.75
SURVIVE = 0.60
GAP = 0.30
FLATBAND = 0.15

CANCELLING = ("negation", "question", "conditional")


def parse_endorse(answer):
    """Return 'YES' / 'NO' / 'UNCLEAR' / None from the model's raw answer (first standalone token)."""
    if not answer:
        return None
    m = re.search(r"\b(yes|no|unclear)\b", answer.strip(), re.IGNORECASE)
    return m.group(1).upper() if m else None


def rate(x, n):
    return round(x / n, 3) if n else 0.0


def summarize(slot, recs):
    # buckets keyed by (frame_class, target_type): frame_class in {plain, cancel}
    cells = {"plain": {"presup": [0, 0], "entail": [0, 0]},   # [endorsed, n]
             "cancel": {"presup": [0, 0], "entail": [0, 0]}}
    perframe = {f: {"presup": [0, 0], "entail": [0, 0]} for f in
                ("plain",) + CANCELLING}
    unparsed = 0
    for r in recs:
        e = parse_endorse(r.get("answer"))
        if e is None:
            unparsed += 1
        endorsed = 1 if e == "YES" else 0
        fc = "cancel" if r["cancelling"] else "plain"
        tt = r["target_type"]
        cells[fc][tt][0] += endorsed
        cells[fc][tt][1] += 1
        perframe[r["frame"]][tt][0] += endorsed
        perframe[r["frame"]][tt][1] += 1
    plain_p = rate(cells["plain"]["presup"][0], cells["plain"]["presup"][1])
    plain_e = rate(cells["plain"]["entail"][0], cells["plain"]["entail"][1])
    surv_p = rate(cells["cancel"]["presup"][0], cells["cancel"]["presup"][1])
    surv_e = rate(cells["cancel"]["entail"][0], cells["cancel"]["entail"][1])
    out = {
        "slot": slot,
        "n": len(recs),
        "unparsed": unparsed,
        "plain_presup_endorse": plain_p,
        "plain_entail_endorse": plain_e,
        "presup_survival": surv_p,
        "entail_survival": surv_e,
        "projection_gap": round(surv_p - surv_e, 3),
        "per_frame": {f: {"presup": rate(v["presup"][0], v["presup"][1]),
                          "entail": rate(v["entail"][0], v["entail"][1])}
                      for f, v in perframe.items()},
    }
    out["sanity_ok"] = plain_p >= SANITY and plain_e >= SANITY
    out["projection_model"] = (out["sanity_ok"] and surv_p >= SURVIVE
                               and out["projection_gap"] >= GAP)
    out["flat_model"] = out["sanity_ok"] and abs(out["projection_gap"]) < FLATBAND
    return out


def verdict(per_model):
    proj = [m["slot"] for m in per_model if m["projection_model"]]
    flat = [m["slot"] for m in per_model if m["flat_model"]]
    failed = [m["slot"] for m in per_model if not m["sanity_ok"]]
    if len(proj) >= 2:
        return ("PROJECTION",
                f"{len(proj)}/3 models ({','.join(proj)}) pass sanity (plain P&E >= {SANITY}) AND "
                f"show projection (presup_survival >= {SURVIVE}, gap >= {GAP}).")
    if len(flat) >= 2:
        return ("FLAT/NULL",
                f"{len(flat)}/3 models ({','.join(flat)}) pass sanity but are flat "
                f"(|gap| < {FLATBAND}): the presupposition leg does not project above the "
                f"matched-entailment leg.")
    return ("MIXED",
            f"projection={proj}, flat={flat}, sanity_failed={failed}; no >=2 majority for either "
            f"pole.")


def main():
    per_model = []
    for slot in ("A", "B", "C"):
        f = HERE / "raw" / f"{slot}.json"
        if not f.exists():
            print(f"(missing raw/{slot}.json — skipping)")
            continue
        recs = json.loads(f.read_text())
        per_model.append(summarize(slot, recs))
    if not per_model:
        sys.exit("no raw results found")
    print("=" * 82)
    for m in per_model:
        print(f"\n[{m['slot']}]  n={m['n']}  unparsed={m['unparsed']}  sanity_ok={m['sanity_ok']}"
              f"  projection={m['projection_model']}  flat={m['flat_model']}")
        print(f"  plain:  presup_endorse={m['plain_presup_endorse']:.2f}"
              f"  entail_endorse={m['plain_entail_endorse']:.2f}")
        print(f"  cancel: presup_survival={m['presup_survival']:.2f}"
              f"  entail_survival={m['entail_survival']:.2f}"
              f"  projection_gap={m['projection_gap']:+.2f}")
        pf = m["per_frame"]
        for fr in ("plain", "negation", "question", "conditional"):
            print(f"    {fr:12s} P={pf[fr]['presup']:.2f}  E={pf[fr]['entail']:.2f}")
    label, rationale = verdict(per_model)
    print("\n" + "=" * 82)
    print(f"VERDICT: {label}\n  {rationale}")
    (HERE / "results.json").write_text(json.dumps(
        {"thresholds": {"SANITY": SANITY, "SURVIVE": SURVIVE, "GAP": GAP, "FLATBAND": FLATBAND},
         "verdict": label, "rationale": rationale, "per_model": per_model}, indent=2) + "\n")
    print("\nwrote results.json")


if __name__ == "__main__":
    main()
