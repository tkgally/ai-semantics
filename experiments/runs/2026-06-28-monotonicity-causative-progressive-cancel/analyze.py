"""Analyze the causative-inchoative PROGRESSIVE cancel-suppression calibration (s140).

Indicator: affirm-the-result rate (NLI label 0 = entailment, or FC YES) on "The <obj>
<inch>.", per condition. Report-the-rate (matched to conative-cancel-v2; NO pass bar
tuned after data). Emits raw/gate.json.

Per model x instrument:
  default_affirm     (expect ~ceiling -> re-confirms the s139 held default, the anchor)
  progressive_affirm (LOW = good suppression; the imperfective paradox cancels the result)
  cue_affirm         (does the explicit result-consequence re-license? high = updates)
DERIVED:
  suppression_no_cue = 100 - progressive_affirm
  cue_following      = cue_affirm
  prog_to_cue_shift  = cue_affirm - progressive_affirm

READING (stated before the run; no threshold tuned after):
  - default ~ceiling, progressive meaningfully below it (suppression_no_cue > 0), cue
    re-licensing (shift > 0) => the conative-shaped cancel pattern => the matched
    within-verbal add-vs-cancel BATTERY can be built (frozen ADD arm + this cancel arm).
  - progressive ~ default (no suppression) => the C1-style aspectual-weakness outcome =>
    sharpened principled-limit finding (held verbal default exists, panel resists its
    aspectual cancel).
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
SLOTS = {"A": "claude-sonnet-4.6", "B": "gpt-5.4-mini", "C": "gemini-3.5-flash"}
CONDS = ["default", "progressive", "cue"]


def affirm(rec, instrument):
    p = rec["pred"]
    if p is None:
        return None
    return (p == "0") if instrument == "nli" else (p == "YES")


def load(instrument, slot):
    return json.load(open(os.path.join(RAW, f"{instrument}_{slot}.json")))


def rate(recs, condition, instrument):
    vals = [affirm(r, instrument) for r in recs if r["condition"] == condition]
    vals = [v for v in vals if v is not None]
    return round(sum(vals) / len(vals) * 100, 1) if vals else None


def per_verb_progressive(recs, instrument):
    """Per-stem progressive affirm (0/1), to expose gradual-COS vs punctual heterogeneity
    (pre-run critic note: melt/dissolve cancel more softly than break/shatter)."""
    out = {}
    for r in recs:
        if r["condition"] != "progressive":
            continue
        a = affirm(r, instrument)
        if a is not None:
            out[r["stem"]] = int(a)
    return out


def main():
    out = {"indicator": "affirm-the-result rate on 'The <obj> <inch>.' (NLI primary)",
           "reading_rule": "report-the-rate; suppression_no_cue = 100 - progressive_affirm; "
           "conative-shaped pattern (default~ceiling, progressive suppressed, cue re-licenses) "
           "=> build matched battery; no-suppression => sharpened principled-limit",
           "per_model": {}}
    print("\n===== CAUSATIVE-INCHOATIVE PROGRESSIVE cancel — affirm-RESULT rate =====")
    print("default=held entailment (s139 ceiling anchor); progressive=suppression (LOW=good); "
          "cue=re-licensing under explicit result consequence.\n")
    for slot, name in SLOTS.items():
        m = {"model": name}
        for arm in ("nli", "fc"):
            recs = load(arm, slot)
            d = rate(recs, "default", arm)
            p = rate(recs, "progressive", arm)
            c = rate(recs, "cue", arm)
            supp = None if p is None else round(100 - p, 1)
            shift = None if (c is None or p is None) else round(c - p, 1)
            m[arm] = {"default": d, "progressive": p, "cue": c,
                      "suppression_no_cue": supp, "cue_following": c,
                      "prog_to_cue_shift": shift,
                      "progressive_by_verb": per_verb_progressive(recs, arm)}
        out["per_model"][slot] = m
        for arm in ("nli", "fc"):
            a = m[arm]
            print(f"[{name:<18} {arm.upper():<3}] default={a['default']}%  "
                  f"progressive={a['progressive']}%  cue={a['cue']}%  | "
                  f"suppression(no-cue)={a['suppression_no_cue']}pp  "
                  f"cue-following={a['cue_following']}%  shift={a['prog_to_cue_shift']}pp")
        print()
    json.dump(out, open(os.path.join(RAW, "gate.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
