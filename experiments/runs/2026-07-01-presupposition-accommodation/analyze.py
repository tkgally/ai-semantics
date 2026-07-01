#!/usr/bin/env python3
"""analyze.py — scoring + verdict for the presupposition / accommodation probe. NO API CALLS.

Reads raw/*.json. For each item the model answered YES / NO / UNCLEAR; `endorsed` == the answer
parses to YES. Per (model), over the frozen 36 conditions (12 scenarios x 3 context conditions):

  supported_endorse     — P-endorse rate in the SUPPORTED context (sanity: P is literally stated,
                          so this should be high; below the floor the model cannot read the text
                          and its neutral/contradicting behavior is uninterpretable).
  neutral_endorse       — P-endorse rate in the NEUTRAL context (the ACCOMMODATION rate: with P
                          unestablished but unopposed, does the model supply it?).
  contradicting_endorse — P-endorse rate in the CONTRADICTING context (should be LOW if the model
                          gates accommodation against an explicitly denied presupposition).
  accommodation_gap     — neutral_endorse - contradicting_endorse (the within-model GATING signal).

VERDICT (thresholds pre-registered in PREREG.md — NOT tuned here):
  SANITY   = 0.75  per-model supported_endorse floor; below it the model is control-FAILED.
  ACCOM    = 0.60  per-model neutral_endorse floor to count as "accommodates".
  GAP      = 0.30  per-model accommodation_gap floor for context-GATING.
  FLATBAND = 0.15  per-model |accommodation_gap| below which neutral and contradicting are flat
                   (no gating — the model treats the two contexts alike).
  LOWACC   = 0.40  per-model neutral_endorse ceiling below which the model does NOT accommodate.

  Per-model qualitative label (sanity_ok required for all three non-null labels):
    gated_accommodation : neutral_endorse >= ACCOM AND accommodation_gap >= GAP
    blanket_yes         : neutral_endorse >= ACCOM AND |accommodation_gap| < FLATBAND
    no_accommodation    : neutral_endorse < LOWACC

  Panel verdict:
    GATED-ACCOMMODATION : >= 2 of 3 sanity-passing models are gated_accommodation.
    BLANKET-YES         : >= 2 of 3 sanity-passing models are blanket_yes.
    NO-ACCOMMODATION    : >= 2 of 3 sanity-passing models are no_accommodation.
    MIXED               : anything else (sanity failures, split panel, partial signal).

Every outcome is a first-class result: BLANKET-YES and NO-ACCOMMODATION are honest nulls on the
"context-gated accommodation" reading and are written as such (charter §4). Sanity failure voids the
strong reading and is reported honestly.

Usage: python3 analyze.py     # prints per-model tables + verdict; writes results.json
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent

SANITY = 0.75
ACCOM = 0.60
GAP = 0.30
FLATBAND = 0.15
LOWACC = 0.40

CONDITIONS = ("supported", "neutral", "contradicting")


def parse_endorse(answer):
    """Return 'YES' / 'NO' / 'UNCLEAR' / None from the model's raw answer (first standalone token)."""
    if not answer:
        return None
    m = re.search(r"\b(yes|no|unclear)\b", answer.strip(), re.IGNORECASE)
    return m.group(1).upper() if m else None


def rate(x, n):
    return round(x / n, 3) if n else 0.0


def summarize(slot, recs):
    cells = {c: [0, 0] for c in CONDITIONS}  # [endorsed, n]
    byfam = {}  # family -> condition -> [endorsed, n]
    unparsed = 0
    for r in recs:
        e = parse_endorse(r.get("answer"))
        if e is None:
            unparsed += 1
        endorsed = 1 if e == "YES" else 0
        c = r["condition"]
        cells[c][0] += endorsed
        cells[c][1] += 1
        fam = byfam.setdefault(r["family"], {cc: [0, 0] for cc in CONDITIONS})
        fam[c][0] += endorsed
        fam[c][1] += 1
    sup = rate(cells["supported"][0], cells["supported"][1])
    neu = rate(cells["neutral"][0], cells["neutral"][1])
    con = rate(cells["contradicting"][0], cells["contradicting"][1])
    out = {
        "slot": slot,
        "n": len(recs),
        "unparsed": unparsed,
        "supported_endorse": sup,
        "neutral_endorse": neu,
        "contradicting_endorse": con,
        "accommodation_gap": round(neu - con, 3),
        "per_family": {f: {c: rate(v[c][0], v[c][1]) for c in CONDITIONS}
                       for f, v in sorted(byfam.items())},
    }
    out["sanity_ok"] = sup >= SANITY
    out["gated_accommodation"] = (out["sanity_ok"] and neu >= ACCOM
                                  and out["accommodation_gap"] >= GAP)
    out["blanket_yes"] = (out["sanity_ok"] and neu >= ACCOM
                          and abs(out["accommodation_gap"]) < FLATBAND)
    out["no_accommodation"] = out["sanity_ok"] and neu < LOWACC
    return out


def verdict(per_model):
    gated = [m["slot"] for m in per_model if m["gated_accommodation"]]
    blanket = [m["slot"] for m in per_model if m["blanket_yes"]]
    none = [m["slot"] for m in per_model if m["no_accommodation"]]
    failed = [m["slot"] for m in per_model if not m["sanity_ok"]]
    if len(gated) >= 2:
        return ("GATED-ACCOMMODATION",
                f"{len(gated)}/3 models ({','.join(gated)}) pass sanity (supported >= {SANITY}) AND "
                f"accommodate (neutral >= {ACCOM}) AND gate (neutral-contradicting >= {GAP}).")
    if len(blanket) >= 2:
        return ("BLANKET-YES",
                f"{len(blanket)}/3 models ({','.join(blanket)}) accommodate (neutral >= {ACCOM}) but "
                f"do NOT gate (|neutral-contradicting| < {FLATBAND}): P is endorsed even when the "
                f"context contradicts it — a blanket yes-bias, not context-gated accommodation.")
    if len(none) >= 2:
        return ("NO-ACCOMMODATION",
                f"{len(none)}/3 models ({','.join(none)}) pass sanity but do NOT accommodate "
                f"(neutral < {LOWACC}): an unestablished presupposition is not supplied.")
    return ("MIXED",
            f"gated={gated}, blanket={blanket}, none={none}, sanity_failed={failed}; "
            f"no >=2 majority for any single pole.")


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
              f"  gated={m['gated_accommodation']}  blanket={m['blanket_yes']}"
              f"  none={m['no_accommodation']}")
        print(f"  supported={m['supported_endorse']:.2f}  neutral={m['neutral_endorse']:.2f}"
              f"  contradicting={m['contradicting_endorse']:.2f}"
              f"  accommodation_gap={m['accommodation_gap']:+.2f}")
        for fam in ("factive", "aspectual", "definite", "cleft"):
            v = m["per_family"].get(fam)
            if v:
                print(f"    {fam:10s} sup={v['supported']:.2f}  neu={v['neutral']:.2f}"
                      f"  con={v['contradicting']:.2f}")
    label, rationale = verdict(per_model)
    print("\n" + "=" * 82)
    print(f"VERDICT: {label}\n  {rationale}")
    (HERE / "results.json").write_text(json.dumps(
        {"thresholds": {"SANITY": SANITY, "ACCOM": ACCOM, "GAP": GAP,
                        "FLATBAND": FLATBAND, "LOWACC": LOWACC},
         "verdict": label, "rationale": rationale, "per_model": per_model}, indent=2) + "\n")
    print("\nwrote results.json")


if __name__ == "__main__":
    main()
