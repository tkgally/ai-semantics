#!/usr/bin/env python3
"""analyze.py — scoring + verdict for the presupposition doppelgänger probe. NO API CALLS.

Reads raw/*.json. For each item the model answered YES / NO / UNCLEAR; `endorsed` == the answer parses
to YES. The primary measure is a WITHIN-MODEL residual over the POWERED families (factive/aspectual/
cleft; the definite family is EXPLORATORY per S1 and NEVER enters the verdict):

  trigger_project  — trigger-leg P-endorse over the PROJECTING frames (negation + question).
  doppel_project   — D1 doppelgänger-leg P-endorse over the same frames.
  residual         — trigger_project - doppel_project  (the within-model shadow-beating signal).

Reported per-family as PRIMARY (S2 — heterogeneous control types), pooled over the powered families
as secondary. Descriptive (never verdict-bearing):
  conditional_residual — the same difference under the CONDITIONAL frame (projection-v1 showed trigger
                         collapses there; both legs near-floor; uninformative for the shadow question).
  plain_doppel_endorse — D1 doppelgänger P-endorse in the PLAIN frame (a direct read on surface-following).
  d2_residual          — trigger_project - d2_endorse (D2 metalinguistic structure-defeat leg).
  definite_residual    — the same residual on the EXPLORATORY definite family (cue degrades; descriptive).

VERDICT (thresholds pre-registered in PREREG.md / the ratified decision — NOT tuned here):
  SANITY   = 0.60   per-model trigger_project floor (projecting frames); below it a model is control-FAILED.
  RESID    = 0.30   per-model residual floor to count as "beats the doppelgänger".
  FLATBAND = 0.15   per-model |residual| below which trigger ≈ doppelgänger (shadow-saturated).

THE TWO VERDICTS ARE NOT EPISTEMICALLY SYMMETRIC (B1/B2 — read the header before citing):
  BEATS-DOPPELGANGER (>= 2/3 sanity-passing models residual >= RESID) → endorsement is KEYED TO THE
     TRIGGER WORD-FORM above bare complement presence. This does NOT establish "beats the distributional
     shadow" and does NOT move the corner to the beater side (a verb-sensitive surface-cue account
     reconstructs a D1 residual). Warrants re-examination, weighted toward the CLEFT family; does not
     fire the essay's revision trigger.
  SHADOW-SATURATED (FLAT) (>= 2/3 sanity-passing models |residual| < FLATBAND) → the doppelgänger endorses
     the same content just as much; a surface-cue account has no residual to answer for. The
     cleanly-licensed, first-class MEASURED result (charter §4) — the whole point of the control.
  MIXED — anything else (sanity failure, split panel, partial signal). Reported; no shadow claim.

Computed BOTH per family (primary) and pooled over the powered families (secondary). N1: a sanity
failure may reduce the panel to 2 models — any 2/2 verdict is flagged. S4: verdict-map SENSITIVITY under
nearby cutoffs is reported.

Usage: python3 analyze.py     # prints per-model tables + verdict; writes results.json
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent

SANITY = 0.60
RESID = 0.30
FLATBAND = 0.15

POWERED_FAMILIES = ("factive", "aspectual", "cleft")
PROJECTING = ("negation", "question")


def parse_endorse(answer):
    """Return 'YES' / 'NO' / 'UNCLEAR' / None from the model's raw answer (first standalone token)."""
    if not answer:
        return None
    m = re.search(r"\b(yes|no|unclear)\b", answer.strip(), re.IGNORECASE)
    return m.group(1).upper() if m else None


def rate(pair):
    x, n = pair
    return round(x / n, 3) if n else 0.0


def _endorsed(r):
    return 1 if parse_endorse(r.get("answer")) == "YES" else 0


def leg_rate(recs, *, family=None, families=None, leg, frames=None, powered=None):
    """P-endorse rate over records matching the filters. frames=None means any frame."""
    x = n = 0
    for r in recs:
        if leg is not None and r["leg"] != leg:
            continue
        if family is not None and r["family"] != family:
            continue
        if families is not None and r["family"] not in families:
            continue
        if powered is not None and r["powered"] != powered:
            continue
        if frames is not None and r["frame"] not in frames:
            continue
        x += _endorsed(r)
        n += 1
    return [x, n]


def residual_block(recs, *, family=None, families=None):
    """trigger_project, doppel_project, residual over the two projecting frames, + descriptive rates."""
    tp = leg_rate(recs, family=family, families=families, leg="trigger", frames=PROJECTING)
    dp = leg_rate(recs, family=family, families=families, leg="doppel", frames=PROJECTING)
    tp_r, dp_r = rate(tp), rate(dp)
    # descriptive
    t_cond = rate(leg_rate(recs, family=family, families=families, leg="trigger", frames=("conditional",)))
    d_cond = rate(leg_rate(recs, family=family, families=families, leg="doppel", frames=("conditional",)))
    plain_d = rate(leg_rate(recs, family=family, families=families, leg="doppel", frames=("plain",)))
    plain_t = rate(leg_rate(recs, family=family, families=families, leg="trigger", frames=("plain",)))
    d2 = rate(leg_rate(recs, family=family, families=families, leg="d2"))
    return {
        "trigger_project": tp_r, "doppel_project": dp_r,
        "residual": round(tp_r - dp_r, 3),
        "n_trigger_proj": tp[1], "n_doppel_proj": dp[1],
        "conditional_residual": round(t_cond - d_cond, 3),
        "conditional_trigger": t_cond, "conditional_doppel": d_cond,
        "plain_trigger_endorse": plain_t, "plain_doppel_endorse": plain_d,
        "d2_endorse": d2, "d2_residual": round(tp_r - d2, 3),
    }


def label_for(block, sanity=SANITY, resid=RESID, flatband=FLATBAND):
    """Per-model, per-family qualitative label from a residual block."""
    sane = block["trigger_project"] >= sanity
    if not sane:
        return "control_failed"
    if block["residual"] >= resid:
        return "beats"
    if abs(block["residual"]) < flatband:
        return "saturated"
    return "mixed"


def panel_verdict(labels):
    """Panel verdict over per-model labels (list). Returns (verdict, rationale, n_sane)."""
    sane = [l for l in labels if l != "control_failed"]
    beats = [l for l in labels if l == "beats"]
    sat = [l for l in labels if l == "saturated"]
    n_sane = len(sane)
    two_of = 2
    if len(beats) >= two_of:
        v = "BEATS-DOPPELGANGER"
        r = (f"{len(beats)}/3 models residual >= {RESID} — endorsement KEYED TO THE TRIGGER WORD-FORM "
             f"(NOT 'beats the shadow', NOT a move to the beater side; a verb-sensitive surface-cue "
             f"account reconstructs a D1 residual).")
    elif len(sat) >= two_of:
        v = "SHADOW-SATURATED"
        r = (f"{len(sat)}/3 models |residual| < {FLATBAND} — the doppelgänger endorses the same content "
             f"just as much; a surface-cue account has no residual to answer for. Measured saturated row.")
    else:
        v = "MIXED"
        r = f"beats={len(beats)}, saturated={len(sat)}, control_failed={3 - n_sane}; no >=2 majority."
    if n_sane == 2:
        r += " [N1: panel reduced to 2 sanity-passing models — verdict rests on 2/2.]"
    return v, r, n_sane


def sensitivity(per_model_blocks, family_key):
    """S4: recompute the family/pooled panel verdict under nearby cutoffs."""
    grid = []
    for resid in (0.25, 0.30, 0.35):
        for flat in (0.10, 0.15, 0.20):
            labels = [label_for(b[family_key], resid=resid, flatband=flat) for b in per_model_blocks]
            v, _, _ = panel_verdict(labels)
            grid.append({"RESID": resid, "FLATBAND": flat, "verdict": v})
    return grid


def main():
    per_model = []
    for slot in ("A", "B", "C"):
        f = HERE / "raw" / f"{slot}.json"
        if not f.exists():
            print(f"(missing raw/{slot}.json — skipping)")
            continue
        recs = json.loads(f.read_text())
        unparsed = sum(1 for r in recs if parse_endorse(r.get("answer")) is None)
        blocks = {"pooled": residual_block(recs, families=POWERED_FAMILIES)}
        for fam in POWERED_FAMILIES:
            blocks[fam] = residual_block(recs, family=fam)
        blocks["definite"] = residual_block(recs, family="definite")  # exploratory
        per_model.append({"slot": slot, "n": len(recs), "unparsed": unparsed, "blocks": blocks})

    if not per_model:
        sys.exit("no raw results found")

    print("=" * 88)
    for m in per_model:
        b = m["blocks"]
        pooled = b["pooled"]
        print(f"\n[{m['slot']}]  n={m['n']}  unparsed={m['unparsed']}")
        print(f"  POOLED(powered)  trigger_project={pooled['trigger_project']:.2f}  "
              f"doppel_project={pooled['doppel_project']:.2f}  residual={pooled['residual']:+.2f}  "
              f"label={label_for(pooled)}")
        print(f"    descriptive: cond_resid={pooled['conditional_residual']:+.2f}  "
              f"plain_doppel={pooled['plain_doppel_endorse']:.2f}  "
              f"d2_endorse={pooled['d2_endorse']:.2f}  d2_resid={pooled['d2_residual']:+.2f}")
        for fam in POWERED_FAMILIES:
            fb = b[fam]
            print(f"    {fam:10s} trig={fb['trigger_project']:.2f} doppel={fb['doppel_project']:.2f} "
                  f"resid={fb['residual']:+.2f} ({label_for(fb)})  "
                  f"[cond_resid={fb['conditional_residual']:+.2f} plain_doppel={fb['plain_doppel_endorse']:.2f}]")
        db = b["definite"]
        print(f"    definite*  trig={db['trigger_project']:.2f} doppel={db['doppel_project']:.2f} "
              f"resid={db['residual']:+.2f}  (*EXPLORATORY — not in verdict; cue degrades)")

    # Panel verdicts: per-family (primary) + pooled (secondary)
    print("\n" + "=" * 88)
    fam_verdicts = {}
    for fam in POWERED_FAMILIES + ("pooled",):
        labels = [label_for(m["blocks"][fam]) for m in per_model]
        v, r, n_sane = panel_verdict(labels)
        fam_verdicts[fam] = {"verdict": v, "rationale": r,
                             "per_model_labels": {m["slot"]: label_for(m["blocks"][fam]) for m in per_model}}
        tag = "PRIMARY" if fam in POWERED_FAMILIES else "secondary"
        print(f"[{fam:8s} {tag}] {v}\n    {r}")

    # cleft note (B1: the one construction-grain leg)
    print("\n  NOTE (B1): the CLEFT family is the sole construction-grain leg (holds content words "
          "constant, varies only the cleft structure); its residual is the one that speaks — weakly — "
          "to a construction-grain shadow. factive/aspectual residuals are lexical (D1 varies the word) "
          "and are reconstructable by a verb-sensitive surface-cue account, so they do NOT beat the shadow.")

    # S4 sensitivity for pooled + cleft
    sens = {"pooled": sensitivity([m["blocks"] for m in per_model], "pooled"),
            "cleft": sensitivity([m["blocks"] for m in per_model], "cleft")}
    print("\n  S4 SENSITIVITY (pooled powered) — verdict under nearby cutoffs:")
    for row in sens["pooled"]:
        print(f"    RESID={row['RESID']} FLATBAND={row['FLATBAND']} -> {row['verdict']}")

    out = {
        "thresholds": {"SANITY": SANITY, "RESID": RESID, "FLATBAND": FLATBAND},
        "powered_families": list(POWERED_FAMILIES),
        "projecting_frames": list(PROJECTING),
        "family_verdicts": fam_verdicts,
        "headline_family_primary": {f: fam_verdicts[f]["verdict"] for f in POWERED_FAMILIES},
        "pooled_secondary": fam_verdicts["pooled"]["verdict"],
        "sensitivity": sens,
        "per_model": per_model,
        "scope": "internal-contrast-only (within-model residual; no human comparison). anchor: pending.",
        "asymmetry_note": ("null (SHADOW-SATURATED) = cleanly-licensed diagnostic prize; a positive "
                           "(BEATS) residual is under-licensed — 'keyed to the trigger word-form', "
                           "reconstructable by a verb-sensitive surface-cue account, does not fire the "
                           "essay's revision trigger (B1/B2)."),
    }
    (HERE / "results.json").write_text(json.dumps(out, indent=2) + "\n")
    print("\nwrote results.json")


if __name__ == "__main__":
    main()
