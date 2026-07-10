"""s205 — one NON-ANTHROPIC decorrelation vote on the FROZEN BLiMP sweep (pre-run critic QA input).
PROTOCOL §A3: GO/NO-GO authority stays with the fresh-agent critic. panel.B (gpt-5.4-mini), cutoff-aware
preamble. Records usage.cost. Writes VOTE-freeze-s205.json. Distinct from the ratification vote."""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = (
    "Today is 2026-07-10. You may encounter references to papers, datasets, or models that postdate "
    "your training cutoff. Treat post-cutoff recency as neutral. Where you rely on what you know, label it.")

SYSTEM = (PREAMBLE + "\n\nYou are an independent adversarial PRE-RUN critic. The design gates are already "
    "ratified; your job is to catch any FATAL flaw in the FROZEN instrument/PREREG BEFORE money is spent, "
    "and vote GO / GO-WITH-CONDITIONS / NO-GO. Be concrete. Flag any choice aimed at a desired result.")

USER = r"""
FROZEN probe (nothing changeable after this without re-freezing). BLiMP behavioral 2AFC sweep, ratified
Q1-B/Q2-A/Q3-A + C8.

INSTRUMENT (frozen, human-agreement-BLIND selection):
- 40 paradigms = EVERY paradigm in the on-axis BLiMP linguistics_term categories (determiner_noun_agreement;
  the local + `distractor_` split of subject_verb_agreement; npi_licensing; quantifiers; island_effects;
  filler_gap_dependency). No within-category hand-picking. Off-axis categories (binding, anaphor_agreement,
  argument_structure, s-selection, control_raising, irregular_forms, ellipsis) excluded with structural reasons.
- Depth strata (structural): local(12, shallow) / medium-distractor(2) / scope=npi+quantifiers(11, deep) /
  island=islands+filler-gap(15, deep). Reading-2 contrast: shallow=local vs deep=scope+island.
- N=30 minimal pairs/paradigm, seed 20260710; BOTH presentation orders per pair (position-bias netted).
  Prompt: "Which of these two sentences is the more grammatically acceptable... Answer ONLY 1 or 2."
- Human anchor: BLiMP per-paradigm total_mean (committed CSV). All 40 clear the F4 0.60 floor (min 0.606).
- 2 low-agreement paradigms (0.514, 0.47) have NO data file on master (404) -> excluded for data-availability
  (not their values); flagged as mildly conservative for reading 1.

VERDICT MAP (frozen thresholds; >=2/3 models):
- R1 (PRIMARY, human-anchored, DESCRIPTIVE/DIRECTIONAL ONLY per C8): rho_prof = Spearman(acc, human) over
  40 paradigms, per model, bootstrap CI. ALIGNED rho>+0.40 / DIVERGES rho<+0.20 / [.20,.40] INCONCLUSIVE.
  n=40 => p<0.05 at rho~0.31 (genuinely powered), but non-promotable this run per C8 regardless.
- R2 (within-panel, verdict-bearing): DEPTH-GRADED iff mean acc(shallow)-mean acc(deep) >= +0.05 on >=2/3.
- R2h (human-anchored): EXCEEDS-HUMAN-DIP iff (panel depth-gap - human depth-gap) > +0.05 on >=2/3.
- F3 saturation: per-model acc SD < 0.03 => rho INCONCLUSIVE (contamination diagnostic = abs-acc dispersion).
- Instrument-failure: position-lock>0.50 AND |P(answer=1)-0.5|>0.40 on >=2/3 => void accuracy readings.
- Absolute accuracy = contamination UPPER BOUND, never the headline.

COST: 40x30x2x3 = 7,200 calls; est $0.6-1.6 (under the $2.50 split flag); gemini reasoning suppressed
(effort minimal, max_tokens 128); per-model ABORT_USD 1.60. Temp 0, zero-shot.

Give concisely:
1. GO / GO-WITH-CONDITIONS / NO-GO on running THIS frozen probe now.
2. Any FATAL flaw in the frozen instrument, scoring, or verdict map (be specific).
3. Biggest residual risk + one freeze condition you'd add (or "none").
4. Anti-cheat: anything aimed at a desired result, or "none".
"""

def main():
    r = call(PANEL["B"], SYSTEM, USER, max_tokens=1200)
    cost = billed_cost([[r]])
    json.dump({"model": PANEL["B"], "usage": r.get("usage"), "billed_cost": cost,
               "error": r.get("error"), "content": r.get("content")},
              open(os.path.join(os.path.dirname(__file__), "VOTE-freeze-s205.json"), "w"), indent=2)
    print("=== NON-ANTHROPIC FREEZE VOTE (panel.B =", PANEL["B"], ") ===")
    print("billed_cost:", cost, "error:", r.get("error"))
    print("---"); print(r.get("content"))

if __name__ == "__main__":
    main()
