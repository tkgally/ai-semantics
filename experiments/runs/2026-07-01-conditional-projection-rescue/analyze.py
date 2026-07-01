#!/usr/bin/env python3
"""analyze.py — scoring + rescue verdict for the conditional-projection-rescue probe. NO API CALLS.

Reads raw/*.json. For each item the model answered YES / NO / UNCLEAR; `endorsed` == YES. Per
(model, arm) over the 12 scenarios x 2 targets:

  presup_endorse  — P-endorse rate in this arm (12 items).
  entail_endorse  — E-endorse rate in this arm (12 items). The YES-BIAS CONTROL: a framing that
                    just makes the model say YES to everything lifts E too.
  gap             — presup_endorse - entail_endorse (the within-arm projection signal).

The design (see PREREG):
  base    — REPLICATES the s158 conditional-antecedent cell. presup_endorse here should be LOW
            (reproduce the collapse). If it is NOT low, replication is anomalous -> flag.
  commit/conseq/belief — three RESCUE arms. Each "rescues" (per model) if presup_endorse >= RESCUE
            AND gap >= GAP. A rescue arm restores projection where BASE collapsed.

VERDICT (thresholds pre-registered in PREREG.md — NOT tuned here):
  RESCUE = 0.60          per-model per-arm presup_endorse floor to count as projection RESTORED.
  GAP    = 0.30          per-model per-arm (presup - entail) floor to count as restored.
  BASE_COLLAPSE_MAX = 0.60   base-arm presup_endorse must be BELOW this for >=2/3 models to
                             confirm the s158 collapse replicated (design validity anchor).
  YESBIAS = 0.60         per-arm entail_endorse at/above this flags a yes-shift confound on that arm.

  Per rescue arm (panel level):
    RESCUED     : >= 2/3 models rescued (presup_endorse >= RESCUE AND gap >= GAP).
    NOT-RESCUED : >= 2/3 models NOT rescued (presup_endorse < RESCUE).
    MIXED       : otherwise.

  Overall headline is the list of rescue arms that came back RESCUED (with the yes-bias flags).
  If BASE did not replicate the collapse (>=2/3 models base presup_endorse >= BASE_COLLAPSE_MAX),
  the run is a REPLICATION-ANOMALY and rescue readings are reported with that caveat.

Usage: python3 analyze.py     # prints per-model/arm tables + verdict; writes results.json
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent

RESCUE = 0.60
GAP = 0.30
BASE_COLLAPSE_MAX = 0.60
YESBIAS = 0.60

ARMS = ("base", "commit", "conseq", "belief")
RESCUE_ARMS = ("commit", "conseq", "belief")


def parse_endorse(answer):
    """Return 'YES' / 'NO' / 'UNCLEAR' / None from the model's raw answer (first standalone token)."""
    if not answer:
        return None
    m = re.search(r"\b(yes|no|unclear)\b", answer.strip(), re.IGNORECASE)
    return m.group(1).upper() if m else None


def rate(x, n):
    return round(x / n, 3) if n else 0.0


def summarize(slot, recs):
    cells = {a: {"presup": [0, 0], "entail": [0, 0]} for a in ARMS}  # [endorsed, n]
    unparsed = 0
    for r in recs:
        e = parse_endorse(r.get("answer"))
        if e is None:
            unparsed += 1
        endorsed = 1 if e == "YES" else 0
        cells[r["arm"]][r["target_type"]][0] += endorsed
        cells[r["arm"]][r["target_type"]][1] += 1
    per_arm = {}
    for a in ARMS:
        p = rate(cells[a]["presup"][0], cells[a]["presup"][1])
        en = rate(cells[a]["entail"][0], cells[a]["entail"][1])
        per_arm[a] = {"presup_endorse": p, "entail_endorse": en, "gap": round(p - en, 3),
                      "yesbias_flag": en >= YESBIAS}
    base_p = per_arm["base"]["presup_endorse"]
    out = {"slot": slot, "n": len(recs), "unparsed": unparsed, "per_arm": per_arm,
           "base_collapsed": base_p < BASE_COLLAPSE_MAX}
    out["rescued_arms"] = {
        a: (per_arm[a]["presup_endorse"] >= RESCUE and per_arm[a]["gap"] >= GAP)
        for a in RESCUE_ARMS}
    out["rescue_lift"] = {a: round(per_arm[a]["presup_endorse"] - base_p, 3) for a in RESCUE_ARMS}
    return out


def verdict(per_model):
    n = len(per_model)
    base_ok = sum(1 for m in per_model if m["base_collapsed"])
    replicated = base_ok >= 2
    arm_verdict = {}
    for a in RESCUE_ARMS:
        rescued = sum(1 for m in per_model if m["rescued_arms"][a])
        notr = sum(1 for m in per_model if m["per_arm"][a]["presup_endorse"] < RESCUE)
        if rescued >= 2:
            arm_verdict[a] = "RESCUED"
        elif notr >= 2:
            arm_verdict[a] = "NOT-RESCUED"
        else:
            arm_verdict[a] = "MIXED"
    rescued_list = [a for a in RESCUE_ARMS if arm_verdict[a] == "RESCUED"]
    if not replicated:
        headline = (f"REPLICATION-ANOMALY: only {base_ok}/{n} models reproduced the base collapse "
                    f"(base presup_endorse < {BASE_COLLAPSE_MAX}); rescue readings are caveated.")
    elif rescued_list:
        headline = (f"PARTIAL/RESCUED: base collapse replicated ({base_ok}/{n}); "
                    f"rescued by {rescued_list}; per-arm {arm_verdict}.")
    else:
        headline = (f"ROBUST-COLLAPSE: base collapse replicated ({base_ok}/{n}); NO rescue arm "
                    f"restored projection for >=2/3 models; per-arm {arm_verdict}.")
    return {"replicated_base_collapse": replicated, "base_ok": base_ok, "n": n,
            "arm_verdict": arm_verdict, "rescued_arms": rescued_list, "headline": headline}


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
        print(f"\n[{m['slot']}]  n={m['n']}  unparsed={m['unparsed']}  "
              f"base_collapsed={m['base_collapsed']}")
        for a in ARMS:
            pa = m["per_arm"][a]
            lift = f"  lift_vs_base={m['rescue_lift'][a]:+.2f}" if a in RESCUE_ARMS else ""
            resc = f"  RESCUED={m['rescued_arms'][a]}" if a in RESCUE_ARMS else ""
            yb = "  [YES-BIAS]" if pa["yesbias_flag"] else ""
            print(f"    {a:8s} P={pa['presup_endorse']:.2f}  E={pa['entail_endorse']:.2f}"
                  f"  gap={pa['gap']:+.2f}{lift}{resc}{yb}")
    v = verdict(per_model)
    print("\n" + "=" * 82)
    print(f"VERDICT: {v['headline']}")
    (HERE / "results.json").write_text(json.dumps(
        {"thresholds": {"RESCUE": RESCUE, "GAP": GAP, "BASE_COLLAPSE_MAX": BASE_COLLAPSE_MAX,
                        "YESBIAS": YESBIAS},
         "verdict": v, "per_model": per_model}, indent=2) + "\n")
    print("\nwrote results.json")


if __name__ == "__main__":
    main()
