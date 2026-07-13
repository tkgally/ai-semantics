#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s222 PRE-RUN CRITIQUE of the genitive-animacy POWERED
MAGNITUDE run (PROTOCOL sec.A3 decorrelation rule).

No new decision is opened (the design was ratified s218; the line is a promoted claim). This is a
pre-run critique of the MAGNITUDE run + POOLING analysis as frozen. QA input to the fresh-agent
pre-run critic (who keeps GO/NO-GO authority). One vote via panel.B (openai/gpt-5.4-mini),
cutoff-aware preamble prepended. Writes VOTE-critic-s222.json.
"""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-13. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.")

SYS = (PREAMBLE + "\n\nYou are an independent adversarial reviewer casting ONE decorrelation vote "
       "on whether a FROZEN behavioral-LLM MAGNITUDE probe + its POOLING analysis are sound to RUN "
       "AS-IS. The measurement instrument is already ratified and byte-frozen; the direction of the "
       "effect is an already-promoted claim. This run does ONE new thing: estimate the SIZE of the "
       "effect (a within-model magnitude + bootstrap interval) by adding a third disjoint item arm "
       "and pooling. You are NOT re-litigating the design or the direction; you are catching any way "
       "the POOLING or the new items could produce a MISLEADING magnitude/interval. Running fixes "
       "the YARDSTICK, never the result; a fresh arm that reverses or fails to be positive (NO-LIFT) "
       "is a first-class outcome. If you would prefer a change only because it would make a larger/"
       "cleaner magnitude more likely, that is a violation — flag it. Be terse and adversarial. End "
       "with a line 'VOTE: <GO | GO-WITH-CONDITIONS | NO-GO>'.")

USER = r"""
CONTEXT. Current LLMs track the English GENITIVE alternation's possessor-animacy constraint: animate
possessors favour the s-genitive ("the judge's decision"), inanimate favour the of-genitive ("the
decision of the judge") — a native-speaker acceptability direction (Dubois et al. 2023, 25 speakers,
openly licensed). Instrument = graded forced-choice: hold the possessum fixed, distribute 100 points
by naturalness between the two phrasings; s-pref = s_pts/(s_pts+of_pts); within-frame shift =
s-pref(animate) - s-pref(inanimate); human direction => shift > 0. Resampling unit = the frame. This
DIRECTION is already a promoted, standing claim: it was found on TWO disjoint 36-typical-frame runs
(s218 + rep2), both CONFIRM 3/3, both surviving a nonce-possessor "firewall" control (animacy carried
only by a gloss, orthographically balanced strings). The claim is scoped DIRECTION-ONLY because 36+36
frames are below the project's powered N (~100-150). Typical-arm magnitudes seen so far: claude ~0.14,
gemini ~0.166, gpt ~0.12.

WHAT THIS RUN DOES. Attach a MAGNITUDE + interval. It adds a THIRD, fresh, TYPICAL-ONLY arm of 36
frames (animate/collective/inanimate real possessors), every possessor lemma CERTIFIED disjoint from
BOTH prior arms (108 new lemmas, 0 of 214 shared). Within each frame, possessor length + final-
sibilancy + definiteness are matched across animacy levels (certified), so length/sibilancy/position/
always-s/always-of readers give within-frame shift 0. The new items were authored blind to model
responses. Then analyze_merged.py POOLS the three disjoint typical arms -> 108 frames and reports,
per model: the pooled mean shift = the magnitude, with a nonparametric bootstrap 95% CI over the 108
frames + a sign test.

WHAT IS BYTE-FROZEN vs NEW:
- Byte-IDENTICAL from s218/rep2 (sha-verified): probe.py, build_cooc_gen.py, the prompt, parser,
  graded forced-choice, resampling unit, covariate recipe.
- common.py identical except one budget constant (HARD_STOP_USD 1.90 -> 1.20; typical-only arm is
  cheaper). Never touches measurement.
- NEW: the 36-frame item set (build_items.py, certified); the merged covariate (same frozen recipe
  over all three arms' lemmas); and analyze_merged.py, the POOLING analysis (frozen before any call).

TWO DELIBERATE CHOICES YOU SHOULD PRESSURE-TEST:
1. NO NONCE ARM in this run. The shortcut firewall already replicated 3/3 twice (s218 CI-LB>0; rep2
   gpt leg decisive 25/36, sign-p 0.014). The magnitude the claim owes is a TYPICAL-arm quantity, so
   this arm re-runs only the typical arm (also keeps the paid run ~$0.81, inside the day's budget).
2. POOLING with prior data. The 108-frame pooled interval REUSES the 72 already-seen frames (whose
   magnitudes are known, ~0.12-0.17) plus 36 fresh-BLIND frames. To be honest the analysis ALSO
   reports the NEW-36-only estimate (the blind arm alone) and the PRIOR-72-only estimate, side by
   side. The pre-registered LIFT rule: magnitude is attached only if >=2/3 models have pooled CI-LB>0
   AND the fresh-36 arm is positive for those models (does not reverse); else NO-LIFT (claim stays
   direction-only).

THE COVARIATE (honest, weak). A frozen per-lemma marginal s-genitive propensity from UD-English-EWT
partials the possessor's marginal genitive-propensity out of the shift; it was near-vacuous in both
prior runs (R^2 <= 0.013). Reported as corroboration; the headline is the RAW pooled shift.

YOUR TASK. Vote GO / GO-WITH-CONDITIONS (say exactly what changes) / NO-GO (name the specific defect).
Address especially: (a) is a POOLED interval over 72-known + 36-blind frames a legitimate way to
"attach a magnitude", or does reusing the data that established the direction make the reported
interval misleadingly tight / circular — and does reporting new-36-only + prior-72-only alongside
adequately fence that? (b) is dropping the nonce arm defensible for a MAGNITUDE (not confirmatory)
run, or does the absence of the within-run firewall mean the pooled typical magnitude could be
inflated by a surface confound the frozen certification does not catch on these specific new items?
(c) is the LIFT rule (>=2/3 pooled CI-LB>0 AND fresh-36 positive) the right bar, or should the fresh
blind arm alone have to clear a threshold before any pooling is reported? Then the VOTE line.
"""

def main():
    r = call(PANEL["B"], SYS, USER, max_tokens=1600)
    cost, have, missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "cost_usd": cost, "n_have": have, "n_missing": missing,
           "content": r.get("content"), "error": r.get("error")}
    json.dump(out, open(os.path.join(os.path.dirname(__file__), "VOTE-critic-s222.json"), "w"), indent=2)
    print("=== VOTE (gpt-5.4-mini) ===")
    print(r.get("content") or f"ERROR: {r.get('error')}")
    print(f"\ncost=${cost:.6f} have={have} missing={missing}")

if __name__ == "__main__":
    main()
