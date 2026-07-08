#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the FROZEN pre-run probe (PROTOCOL §A3). One vote through the
non-Anthropic slot via the probe REST path. QA input to the fresh-agent critic's GO/NO-GO — not
authoritative. Cutoff-aware preamble."""
import sys, os
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-08. You are a methodology reviewer. Your training cutoff may predate "
            "this project; treat post-cutoff papers/datasets/models as neutral, not fabricated. Judge "
            "only the frozen design below on its internal merits; be adversarial and terse.")

DESIGN = """A FROZEN behavioral probe (no model data collected yet). Internal-contrast, NO human comparison.

QUESTION over 6 WordNet NOUN relations (antonymy, synonymy, hypernymy, hyponymy, holonymy, meronymy):
 H1 - does panel relation-recovery rank DECOUPLE again from contrastive-frame co-occurrence cue-strength,
      on a FRESH test (fresh cues + a DIFFERENT corpus)?  (s186 found Spearman ~ -0.086 on Simple Wikipedia)
 H2 - does a PRE-REGISTERED taxonomic proxy OUT-PREDICT cue-strength for relation-wise recovery?
      Primary proxy = IS-A path depth (mean WordNet min_depth of each cue's first noun synset),
      predicted sign NEGATIVE (shallower/more-superordinate cue sets recover better).
      Second arm = a corpus Hearst-frame ("X such as Y","Y and other X") definitional-density,
      predicted sign POSITIVE; a Hearst-only win is reported QUALIFIED/weaker, never equal-status.

FRESHNESS: cues are DISJOINT from the 707 s186 cue lemmas (asserted 0 overlap). Achieved N per relation
120 except antonymy 87 (WordNet nominal antonym sparsity after excluding s186's antonymy cues — reported,
not padded). Frequency-matched on SubTLEX-US Lg10WF band [2.0,4.5]. The control corpus is C4 (web register,
allenai/c4, ODC-BY), DIFFERENT source-family from s186's Simple English Wikipedia; 3 shards streamed,
achieved 22.3M sentences / 388M tokens (>= s186's 21.3M / ~320M). The contrastive-frame G2 computation
(Dunning log-likelihood over co-occurrence restricted to symmetric/contrastive frames, window<=4) is
BYTE-IDENTICAL to s186 (verified by assertion); only the corpus + IO adapter changed.

SCORING: recovery per relation = mean raw Soundness (precision over produced); HIT@3 co-primary.
cue-strength per relation = mean Soundness of the control's top-3 (frame variant). rho_cue/rho_depth/
rho_hearst = across-relation Spearman (n=6, tie-naive) of recovery vs each predictor, PER MODEL.

VERDICT MAP (frozen, exhaustive):
 H1: REPLICATES iff rho_cue <= +0.30 on >=2/3 models; BREAKS iff rho_cue > +0.50 on >=2/3;
     PARTIAL/AMBIGUOUS otherwise (no uncovered middle).
 H2: a proxy WINS for a model iff |rho_proxy| - |rho_cue| >= 0.20 AND in its predicted direction.
     TAXONOMIC-PROXY-WINS iff IS-A depth wins >=2/3 (primary); WINS-QUALIFIED iff only Hearst wins;
     else LOSES. The ACROSS-RELATION n=6 result is the SOLE verdict of record; an item-level
     (~687-cue) depth-vs-recovery regression is reported but DESCRIPTIVE/NON-DECISIVE (cannot fire H2).
 Pre-named nulls: rho_cue and rho_depth both near-zero; or across-vs-item-level divergence.

FROZEN PREDICTOR VECTORS (computed pre-recovery, no model data): cue-strength antonymy 0.149 >> hyponymy
0.036 > holonymy 0.031 > meronymy 0.019 > hypernymy 0.008 > synonymy 0.006; IS-A depth antonymy 6.13
(shallowest) < hyponymy 6.38 < meronymy 6.87 < synonymy 6.95 < hypernymy 7.01 < holonymy 7.20 (deepest);
Hearst density ~flat 0.012-0.015. n=3 models, orderings not coefficients, nouns only. Cost ~$0.4, ABORT $1.50.

VOTE: (1) Is this a FAIR, non-question-begging test where H1-replicate, H1-break, H2-win, H2-lose, and
null are ALL genuinely reachable? (2) Given IS-A depth ranks hypernymy DEEP, is H2 genuinely at risk
(not rigged to win)? (3) Any anti-cheat hole (something tunable after results, a proxy that could be
swapped)? Reply: VERDICT: GO | GO-WITH-CONDITIONS | NO-GO, then <=6 terse bullets (BLOCKER/SHOULD-FIX/NIT + fix)."""

r = call(PANEL["B"], PREAMBLE, DESIGN, temperature=0, max_tokens=900)
print(r["content"])
b = billed_cost([[r]])
print("\n--- billed:", b, "err:", r.get("error"))
with open("vote-freeze.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${b[0]:.6f}; model {PANEL['B']}; s193 freeze-stage vote]\n")
