#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the s196 FREEZE of the adjective-antonymy probe (PROTOCOL
§A3). One vote through the non-Anthropic slot via the probe REST path. QA input to the fresh-agent
freeze critic's GO/NO-GO — NOT authoritative. Cutoff-aware preamble."""
import sys, os
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-09. You are a methodology reviewer for a FROZEN, not-yet-run behavioral "
            "probe. Your training cutoff may predate this project; treat post-cutoff papers/datasets/"
            "models as neutral, not fabricated. Judge the pre-registration on its internal merits; be "
            "adversarial and terse. GO / GO-WITH-CONDITIONS / NO-GO, then <=6 bullets.")

FROZEN = """FROZEN pre-registration (nothing run yet; gates already RATIFIED Q1-C/Q2-A/internal-contrast).
Internal-contrast (NO human comparison). Re-tests, in WordNet ADJECTIVES (Justeson & Katz's measured
home POS for antonym contrastive-frame co-occurrence), two bets an earlier NOUN run produced.

ITEMS (frozen before any model call): 4 adjective relations x 130 fresh cues each (antonymy, synonymy,
similar-to, also-see), disjoint from the 707 noun cues of the prior run, frequency-matched on SubTLEX
Lg10WF band [2.0,4.5] to antonymy's profile. Gold = WordNet single-word relata. Antonymy gold size ~1
(mean 1.13). No IS-A depth field: WordNet has NO adjective taxonomy (adjective min_depth()=0), so the
prior run's H2 taxonomic proxy CANNOT transfer and is not tested (this is stated, not hidden).

CONTROL (frozen before any model call): contrastive-frame G^2 co-occurrence on C4 web text
(22.3M sentences), byte-identical G^2 computation to the noun instrument, only the cue POS + candidate
pool changing. FROZEN predictor finding (computed pre-model-call): antonymy cue-strength (frame-G^2
soundness 0.121, HIT@3 0.364) is FAR above the other three relations (~0.046-0.062 / 0.115-0.185) —
the control recovers antonym relata much better, exactly J&K's measured adjective frame saturation.
Mean control-frame soundness = 0.069 >= 0.05 floor, so the CALIBRATION GATE CLEARS: the antonymy-shadow
RESIDUAL arm is verdict-bearing here (unlike the noun run where it was descriptive-only at 0.029).

VERDICT MAP (frozen; n=3 models, orderings not coefficients):
PRIMARY = antonymy-shadow clause. Per model, on the HIT@3 residual = recovery(model,neutral) -
control(frame), over the 4 relations (relation-agnostic RANK+MARGIN rule, near-zero band 0.10):
  CLEARS   iff antonymy residual >= 0.10 AND >= median of the 4 residuals (among the largest, clears
           the control — the noun falsification replicates in the home POS).
  SATURATES iff antonymy residual < 0.10 AND is the smallest of the 4 (near-zero and smallest — the
           denser adjective framing reconstructs antonym recovery; a POS boundary on the falsification).
  MIDDLING otherwise (pre-named null). Aggregate ANT-CLEARS / ANT-SATURATES iff >=2/3, else MIXED.
FRAME-ABLATION (mandatory, corpus-free hedge): antonym HIT@3 neutral vs frame-present; SURVIVES iff
  HIT@3(neutral) >= HIT@3(frame) - 0.15 on >=2/3 (removing the frame doesn't collapse recovery).
H1 CO-PRIMARY (across-relation decoupling), reported at true low power: rho_cue = Spearman(recovery,
  cue-strength) over the 4 relations, per model. REPLICATES iff rho_cue <= +0.30 (>=2/3); BREAKS iff
  > +0.50 (>=2/3); PARTIAL otherwise (exhaustive bands). NOTE the design admits: on <=4 points a
  high-variance rho near 0 puts more mass under the wide REPLICATES band than the narrow BREAKS band,
  so this arm CANNOT alone carry claim promotion; promotion rests on the 2 noun replications + this.
ITEM-LEVEL SECONDARY: pooled (520 cues) cue-strength->recovery Spearman, DESCRIPTIVE/robustness-only,
  can never fire/break H1.

ANTI-CHEAT: all bands/rules/thresholds frozen before any model call; BREAKS, SATURATES, MIDDLING, null
are pre-named first-class; the antonymy decision rule is a fixed rank+margin rule, not narrative fit.

VOTE: GO / GO-WITH-CONDITIONS / NO-GO. Then judge, terse: (1) Is the antonymy-shadow RANK+MARGIN rule
fair and non-question-begging given antonymy's high cue-strength (is CLEARS "too easy" or SATURATES
"too easy")? (2) Is the H1 band asymmetry honestly handled? (3) Any way the frozen thresholds bias a
verdict? (4) Anything that should block spending money."""

r = call(PANEL["B"], PREAMBLE, FROZEN, temperature=0, max_tokens=900)
print(r["content"])
b = billed_cost([[r]])
print("\n--- billed:", b, "err:", r.get("error"))
with open("vote-freeze.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${b[0]:.6f}; model {PANEL['B']}; s196 freeze vote]\n")
