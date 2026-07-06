#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the FROZEN pre-run design (PROTOCOL §A3).
One vote through openai/gpt-5.4-mini via the probe REST path. QA input to the fresh-agent
critic's GO/NO-GO — not authoritative. Cutoff-aware preamble."""
import sys, os, json, time
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("You are a methodology reviewer. Your training cutoff may predate this project; "
            "judge only the design described below on its internal merits — do not defer to "
            "remembered conventions. Be adversarial and terse.")

DESIGN = """A frozen behavioral probe (no model data collected yet). Internal-contrast, no human comparison.

QUESTION: over 6 WordNet NOUN relations (antonymy, synonymy, hypernymy, hyponymy, holonymy, meronymy),
is ANTONYMY the relation whose panel relatum-recovery is LEAST separable from a distributional control
(smallest residual), while meronymy/hyponymy keep a larger residual?

ITEMS: N=130 cue nouns per relation; frequency-matched on SubTLEX-US Lg10WF (medians 3.005-3.015, band
[2.0,4.5], upper bound drops iconic high-freq outlier pairs). Gold = word-form WordNet relata; antonymy/
synonymy/holonymy/meronymy one-hop, hypernymy/hyponymy transitive-closure depth<=4 (because the prompts
invite any-level, and the model gives valid multi-hop relata). Gold sizes differ by relation (antonymy
~1, hyponymy ~24) — a real WordNet fan-out property.

CONTROL (computed with NO reference to the panel): contrastive-frame G2 (Dunning log-likelihood over
co-occurrence restricted to symmetric/contrastive frames — 'X versus Y','neither X nor Y','from X to Y',
adjacency + coordinators, window<=4) from Simple English Wikipedia (CC BY-SA 4.0; 21.3M sentences;
candidate pool = 6810 content nouns). For each cue the control ranks all candidates by G2, takes top-3.
Sentence-level G2 is a reported sensitivity.

SCORING (Soundness = precision over produced, Cao 2025): residual(rel,model) = S(model,neutral-prompt) −
S(control), same 3-slot budget and same gold for both, bootstrap 95% CI over cues. Pre-run fact (control
only, no model): mean S(control,frame) = antonymy 0.077 vs 0.010-0.023 for the other five — antonymy is
by far the most distributionally cued (clause 2).

GUARDS: residual scores model and control on the SAME gold (fan-out cancels; big gold lowers residual =
conservative against the conjecture for hyponymy); a size-matched sensitivity re-runs on |gold|<=5 cues.
A frame-ablation arm (antonymy S with contrastive frame present vs suppressed) is model-internal.

VERDICT MAP (frozen): CONFIRMS iff antonymy smallest residual on >=2/3 models w/ meronymy/hyponymy
larger; SHADOW-SATURATED-FLAT (null) iff antonymy CI overlaps all others on >=2/3; INVERTED iff a weakly-
cued relation smallest on >=2/3; else MIXED. Instrument caveat named in advance: control is blind top-3
precision, structurally low, so if model recovery is uniformly high the residual ~ tracks raw recovery
and INVERTED/MIXED is a live honest outcome. Cost ~$0.4-0.9, ABORT_USD=2.50.

Vote: is this a FAIR, non-question-begging test where all outcomes (confirm / null / inverted) are
genuinely reachable, and the control faithfully represents 'what co-occurrence alone predicts'? Reply:
VERDICT: GO | GO-WITH-CONDITIONS | NO-GO, then <=5 bullet issues (each BLOCKER/SHOULD-FIX/NIT + fix)."""

r = call(PANEL["B"], PREAMBLE, DESIGN, temperature=0, max_tokens=650)
print(r["content"])
print("\n--- billed:", billed_cost([[r]])[0], "err:", r.get("error"))
with open("vote-nonanthropic.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${billed_cost([[r]])[0]:.6f}; model {PANEL['B']}]\n")
