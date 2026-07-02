#!/usr/bin/env python3
"""analyze.py — scoring + verdict for the accommodation / cue-strength probe. NO API CALLS.

Reads raw/*.json. For each item the model answered YES / NO / UNCLEAR; `endorsed` == the answer
parses to YES (parse_endorse, over the model's OWN token — there is NO human key anywhere in this
path). Per (model), over the frozen 48 conditions (12 scenarios x 4 context conditions):

  supported_endorse      — P-endorse rate in the SUPPORTED context (sanity: P is literally stated,
                           so this should be high; below the floor the model cannot read the text and
                           its other cells are uninterpretable). WITHIN-MODEL rate.
  neutral_endorse        — P-endorse rate in the NEUTRAL context (the ACCOMMODATION rate: with P
                           unestablished but unopposed, does the model supply it?). WITHIN-MODEL rate.
  weak_contra_endorse    — P-endorse rate under a MILD/hedged denial of P. WITHIN-MODEL rate.
  strong_contra_endorse  — P-endorse rate under an EMPHATIC/categorical denial of the SAME P.
                           WITHIN-MODEL rate.

  strength_gradient      = weak_contra_endorse - strong_contra_endorse
                           POSITIVE => a stronger surface contradiction gates HARDER (lower
                           endorsement) — the cue-strength prediction of
                           conjecture/presupposition-environment-gated-both-directions.
  accommodation_gap      = neutral_endorse - strong_contra_endorse
                           the OVERALL within-model gate (as in v1, but measured against the
                           STRONGEST contradiction).

Every quantity is a WITHIN-MODEL rate over that model's own YES/NO/UNCLEAR answers; NO human anchor
enters the scoring. This probe is `internal-contrast-only`, inheriting the ratified precedent
decisions/resolved/presupposition-accommodation-internal-contrast-anchor (session 163). No human
comparison is claimed.

VERDICT (thresholds pre-registered in PREREG.md — NOT tuned here; there is no data to tune to):
  SANITY     = 0.75  per-model supported_endorse floor; below it the model is control-FAILED.
  ACCOM      = 0.60  per-model neutral_endorse floor to count as "accommodates".
  GAP        = 0.30  per-model accommodation_gap floor to count as gating overall (neutral vs strong).
  GRAD       = 0.15  per-model strength_gradient floor to count as "graded-by-strength".
  FLATBAND   = 0.10  per-model |strength_gradient| below which weak approx strong (gate NOT graded).
  NOGATEBAND = 0.15  per-model accommodation_gap below which even the STRONG contradiction fails to
                     lower endorsement (a blanket yes-bias). Inherits v1's FLATBAND role/value.
  LOWACC     = 0.40  per-model neutral_endorse ceiling below which the model does NOT accommodate.
  (12 items/condition => one item = 1/12 ~ 0.083; so 0.15 ~ 1.8 items, 0.10 ~ 1.2, 0.30 ~ 3.6.)

  Per-model qualitative label (sanity_ok required for all non-null labels):
    graded_gate      : accommodates AND strength_gradient >= GRAD
                       (endorsement falls as contradiction strengthens — the conjecture's prediction)
    flat_gate        : accommodates AND accommodation_gap >= GAP AND |strength_gradient| < FLATBAND
                       (gates overall, but weak approx strong: contradiction is on/off, not graded —
                        a NULL / partial FALSIFIER of the graded-cue arm)
    blanket_yes      : accommodates AND accommodation_gap < NOGATEBAND
                       (even the strong contradiction barely lowers endorsement — a yes-bias)
    no_accommodation : neutral_endorse < LOWACC
                       (an unestablished presupposition is not supplied at all)
  (A model can fall in NONE of these — e.g. accommodates, gradient in the 0.10-0.15 dead-band, gap in
   the 0.15-0.30 band — in which case it is unlabeled and contributes only to MIXED.)

  Panel verdict (priority order):
    GRADED-GATE      : >= 2 of 3 sanity-passing models are graded_gate.
    FLAT-GATE        : >= 2 of 3 sanity-passing models are flat_gate.
    BLANKET-YES      : >= 2 of 3 sanity-passing models are blanket_yes.
    NO-ACCOMMODATION : >= 2 of 3 sanity-passing models are no_accommodation.
    MIXED            : anything else (sanity failures, split panel, dead-band, partial signal).

Every outcome is a first-class result. GRADED-GATE confirms the cue-strength arm of the conjecture;
FLAT-GATE is an honest NULL on that arm (the gate is on/off, not graded) and a partial falsifier;
BLANKET-YES / NO-ACCOMMODATION are the inherited nulls; all are written as such (charter §4). Sanity
failure voids the strong reading and is reported honestly.

Usage: python3 analyze.py                 # prints per-model tables + verdict; writes results.json
       python3 analyze.py --selftest      # NO API, NO files left behind: run synthetic records
                                          # through summarize/verdict and assert the plumbing.
"""
import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent

SANITY = 0.75
ACCOM = 0.60
GAP = 0.30
GRAD = 0.15
FLATBAND = 0.10
NOGATEBAND = 0.15
LOWACC = 0.40

CONDITIONS = ("supported", "neutral", "weak_contra", "strong_contra")


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
    weak = rate(cells["weak_contra"][0], cells["weak_contra"][1])
    strong = rate(cells["strong_contra"][0], cells["strong_contra"][1])
    out = {
        "slot": slot,
        "n": len(recs),
        "unparsed": unparsed,
        "supported_endorse": sup,
        "neutral_endorse": neu,
        "weak_contra_endorse": weak,
        "strong_contra_endorse": strong,
        "strength_gradient": round(weak - strong, 3),
        "accommodation_gap": round(neu - strong, 3),
        "per_family": {f: {c: rate(v[c][0], v[c][1]) for c in CONDITIONS}
                       for f, v in sorted(byfam.items())},
    }
    out["sanity_ok"] = sup >= SANITY
    accommodates = out["sanity_ok"] and neu >= ACCOM
    out["accommodates"] = accommodates
    out["graded_gate"] = accommodates and out["strength_gradient"] >= GRAD
    out["flat_gate"] = (accommodates and out["accommodation_gap"] >= GAP
                        and abs(out["strength_gradient"]) < FLATBAND)
    out["blanket_yes"] = accommodates and out["accommodation_gap"] < NOGATEBAND
    out["no_accommodation"] = out["sanity_ok"] and neu < LOWACC
    return out


def verdict(per_model):
    graded = [m["slot"] for m in per_model if m["graded_gate"]]
    flat = [m["slot"] for m in per_model if m["flat_gate"]]
    blanket = [m["slot"] for m in per_model if m["blanket_yes"]]
    none = [m["slot"] for m in per_model if m["no_accommodation"]]
    failed = [m["slot"] for m in per_model if not m["sanity_ok"]]
    if len(graded) >= 2:
        return ("GRADED-GATE",
                f"{len(graded)}/3 models ({','.join(graded)}) pass sanity (supported >= {SANITY}) AND "
                f"accommodate (neutral >= {ACCOM}) AND gate HARDER under a stronger contradiction "
                f"(weak-endorse - strong-endorse >= {GRAD}): the accommodation gate is GRADED by cue "
                f"strength, the cue-strength prediction of the environment-gated conjecture.")
    if len(flat) >= 2:
        return ("FLAT-GATE",
                f"{len(flat)}/3 models ({','.join(flat)}) accommodate AND gate overall "
                f"(neutral-strong >= {GAP}) but weak approx strong (|gradient| < {FLATBAND}): the "
                f"contradiction acts as an ON/OFF gate, NOT graded by strength — an honest NULL on "
                f"(partial falsifier of) the graded-cue arm.")
    if len(blanket) >= 2:
        return ("BLANKET-YES",
                f"{len(blanket)}/3 models ({','.join(blanket)}) accommodate (neutral >= {ACCOM}) but "
                f"even the STRONG contradiction barely lowers endorsement (neutral-strong < "
                f"{NOGATEBAND}): a blanket yes-bias, not a gate. Null on the gating reading.")
    if len(none) >= 2:
        return ("NO-ACCOMMODATION",
                f"{len(none)}/3 models ({','.join(none)}) pass sanity but do NOT accommodate "
                f"(neutral < {LOWACC}): an unestablished presupposition is not supplied. Null.")
    return ("MIXED",
            f"graded={graded}, flat={flat}, blanket={blanket}, none={none}, sanity_failed={failed}; "
            f"no >=2 majority for any single pole.")


def _print_and_write(per_model, write=True):
    print("=" * 82)
    for m in per_model:
        print(f"\n[{m['slot']}]  n={m['n']}  unparsed={m['unparsed']}  sanity_ok={m['sanity_ok']}"
              f"  graded={m['graded_gate']}  flat={m['flat_gate']}"
              f"  blanket={m['blanket_yes']}  none={m['no_accommodation']}")
        print(f"  supported={m['supported_endorse']:.2f}  neutral={m['neutral_endorse']:.2f}"
              f"  weak={m['weak_contra_endorse']:.2f}  strong={m['strong_contra_endorse']:.2f}")
        print(f"  strength_gradient={m['strength_gradient']:+.2f}"
              f"  accommodation_gap={m['accommodation_gap']:+.2f}")
        for fam in ("factive", "aspectual", "definite", "cleft"):
            v = m["per_family"].get(fam)
            if v:
                print(f"    {fam:10s} sup={v['supported']:.2f}  neu={v['neutral']:.2f}"
                      f"  weak={v['weak_contra']:.2f}  strong={v['strong_contra']:.2f}")
    label, rationale = verdict(per_model)
    print("\n" + "=" * 82)
    print(f"VERDICT: {label}\n  {rationale}")
    if write:
        (HERE / "results.json").write_text(json.dumps(
            {"thresholds": {"SANITY": SANITY, "ACCOM": ACCOM, "GAP": GAP, "GRAD": GRAD,
                            "FLATBAND": FLATBAND, "NOGATEBAND": NOGATEBAND, "LOWACC": LOWACC},
             "verdict": label, "rationale": rationale, "per_model": per_model}, indent=2) + "\n")
        print("\nwrote results.json")
    return label


def selftest():
    """NO API, NO files: push synthetic records through the scorer and assert each verdict fires.

    Leaves NOTHING behind (never touches raw/ or results.json). Confirms the parse -> per-condition
    rate -> gradient -> verdict plumbing before the real (unrun) probe is ever executed.
    """
    def mk(slot, sup, neu, weak, strong):
        """Build 48 synthetic recs with the requested per-condition YES-counts (out of 12)."""
        recs = []
        plan = {"supported": sup, "neutral": neu, "weak_contra": weak, "strong_contra": strong}
        fams = ["factive", "aspectual", "definite", "cleft"]
        for cond, yes_n in plan.items():
            for i in range(12):
                ans = "YES" if i < yes_n else ("NO" if i % 2 else "UNCLEAR")
                recs.append({"condition": cond, "family": fams[i % 4], "answer": ans})
        return recs

    # A: graded gate (neutral 12, weak 9, strong 3 -> gradient +0.50, gap +0.75)
    # B: graded gate (neutral 11, weak 8, strong 4 -> gradient +0.33, gap +0.58)
    # C: flat gate   (neutral 12, weak 4, strong 3 -> gradient +0.08 < 0.10, gap +0.75 >= 0.30)
    cases = {"A": (12, 12, 9, 3), "B": (12, 11, 8, 4), "C": (12, 12, 4, 3)}
    per_model = [summarize(s, mk(s, *cs)) for s, cs in cases.items()]
    label = _print_and_write(per_model, write=False)
    assert label == "GRADED-GATE", f"expected GRADED-GATE (A,B graded), got {label}"
    assert per_model[0]["graded_gate"] and per_model[1]["graded_gate"]
    assert per_model[2]["flat_gate"] and not per_model[2]["graded_gate"]

    # Now flip to a FLAT-GATE majority: A,C flat (weak approx strong, but gate overall), B graded.
    cases2 = {"A": (12, 12, 4, 3), "B": (12, 11, 8, 4), "C": (12, 12, 3, 3)}
    pm2 = [summarize(s, mk(s, *cs)) for s, cs in cases2.items()]
    assert verdict(pm2)[0] == "FLAT-GATE", f"expected FLAT-GATE, got {verdict(pm2)[0]}"

    # BLANKET-YES: accommodate but strong barely lowers endorsement (gap < NOGATEBAND).
    cases3 = {"A": (12, 12, 12, 11), "B": (12, 12, 12, 11), "C": (12, 12, 9, 3)}
    pm3 = [summarize(s, mk(s, *cs)) for s, cs in cases3.items()]
    assert verdict(pm3)[0] == "BLANKET-YES", f"expected BLANKET-YES, got {verdict(pm3)[0]}"

    # NO-ACCOMMODATION: neutral below LOWACC for a majority.
    cases4 = {"A": (12, 3, 2, 1), "B": (12, 2, 1, 1), "C": (12, 12, 9, 3)}
    pm4 = [summarize(s, mk(s, *cs)) for s, cs in cases4.items()]
    assert verdict(pm4)[0] == "NO-ACCOMMODATION", f"expected NO-ACCOMMODATION, got {verdict(pm4)[0]}"

    # SANITY failure -> voids labels -> MIXED.
    cases5 = {"A": (5, 12, 9, 3), "B": (6, 12, 4, 3), "C": (12, 12, 9, 3)}
    pm5 = [summarize(s, mk(s, *cs)) for s, cs in cases5.items()]
    assert verdict(pm5)[0] == "MIXED", f"expected MIXED (2 sanity fails), got {verdict(pm5)[0]}"

    print("\nselftest OK — all five verdict branches fire; nothing written.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        selftest()
        return
    per_model = []
    for slot in ("A", "B", "C"):
        f = HERE / "raw" / f"{slot}.json"
        if not f.exists():
            print(f"(missing raw/{slot}.json — skipping)")
            continue
        recs = json.loads(f.read_text())
        per_model.append(summarize(slot, recs))
    if not per_model:
        sys.exit("no raw results found (design-only run dir — probe.py has not been run)")
    _print_and_write(per_model, write=True)


if __name__ == "__main__":
    main()
