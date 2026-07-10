"""s204 — one NON-ANTHROPIC decorrelation vote on the BLiMP forced-choice sweep design gates.
PROTOCOL §2/§A3: QA input to the fresh-agent critic (who keeps verdict authority). panel.B (gpt-5.4-mini),
cutoff-aware preamble. Records usage.cost via billed_cost(). Writes VOTE-s204.json + prints a summary."""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = (
    "Today is 2026-07-10. You may encounter references to papers, datasets, or models that postdate "
    "your training cutoff. Treat post-cutoff recency as neutral: a paper you do not recognize is not "
    "for that reason fabricated. Where you must rely on what you know, label it as such."
)

SYSTEM = (
    PREAMBLE + "\n\nYou are an independent, adversarial PRE-RUN design critic for an autonomous "
    "research project on LLM meaning. Your job is to find fatal flaws BEFORE any money is spent, and to "
    "vote GO / GO-WITH-CONDITIONS / NO-GO on each value-laden gate. Be skeptical and concrete. "
    "Ratification fixes the measuring yardstick, never the desired result — flag any choice that looks "
    "aimed at a particular outcome. Reply in compact structured prose."
)

USER = r"""
Design under review: a BLiMP forced-choice sweep (behavioral 2-alternative forced choice on human-validated
English grammatical minimal pairs). BLiMP = 67 paradigms x 1,000 minimal pairs (sentence_good vs
sentence_bad), template-generated, CC-BY, aggregate human agreement 96.4%. CRUCIALLY, BLiMP also ships
PER-PARADIGM human agreement (raw_results/summary/human_validation_summary.csv; columns
Condition,accepted,total_mean,count; e.g. determiner_noun_agreement_1=0.958, npi_present_1=0.83,
only_npi_scope=0.72, wh_island=0.73; range ~0.47-0.99), verified firsthand.

The panel is 3 closed chat models (Anthropic / OpenAI / Google), LOGPROB-FREE, temperature 0, zero-shot.

TWO readings:
  (1, PRIMARY, human-anchored) Profile alignment: per model, Spearman across the selected paradigms of the
      model's per-paradigm forced-choice accuracy vs BLiMP's per-paradigm human agreement. Are models hard
      exactly where humans are hard?
  (2, SECONDARY, within-panel) Depth gradient: does error concentrate on structurally-deep paradigms
      (islands, NPI scope, long-distance/distractor agreement) vs locally-detectable ones (adjacent
      determiner-noun / regular subject-verb agreement)? This operationalizes a "shadow-depth" axis:
      local agreement is n-gram-detectable, islands/scope require structural representation.

THREE value-laden GATES, each with a provisional default:

Q1 (paradigm set + depth axis):
  A = AANN-adjacent agreement family only (no depth spread; rejected).
  B [DEFAULT] = depth-stratified ~9-12 paradigms across 4 strata (shallow-local / medium-distractor /
      deep-NPI-quantifier / deep-island), list+stratum-assignment frozen by a written locality rule BEFORE
      any model call, reported as a selected (not exhaustive) subset.
  C = full 67-paradigm sweep (removes curation objection; ~5.6x cost, dilutes depth focus).

Q2 (forced-choice elicitation + position-bias control):
  A [DEFAULT] = behavioral 2AFC, BOTH presentation orders per item, position-bias netted (order-averaged
      accuracy primary + consistency accuracy + order-flip diagnostic); 2x calls.
  B = single fixed-random order (half the calls; uncontrolled position bias).
  C = isolated absolute acceptability rating (discards the minimal-pair contrast).

Q3 (contamination scope + anchor declaration): BLiMP is synthetic, published 2019, widely trained on, so
    absolute accuracy is a contamination upper bound.
  A [DEFAULT] = load-bearing findings are RELATIVE (profile alignment + depth gradient); absolute accuracy
      reported as an upper bound; anchor = HUMAN-COMPARISON via BLiMP's per-paradigm human agreement (NOT
      internal-contrast-only). Rationale: memorization inflates accuracy roughly uniformly, so the relative
      difficulty profile is robust where absolutes are not.
  B = add a lexical-perturbation contamination control (novel content words; risks breaking template
      grammaticality; build cost).
  C = decline the unit as contamination-uninterpretable.

Powered N ~100-120 items/paradigm; ~6,600 calls; est. $0.6-1.6; hard ABORT_USD ~$2.0; gemini reasoning
suppressed; pre-register a split if the freeze re-estimate exceeds $2.50.

Give, concisely:
1. An overall GO / GO-WITH-CONDITIONS / NO-GO on running this design after gate ratification.
2. A per-gate vote: Q1 (A/B/C), Q2 (A/B/C), Q3 (A/B/C), each one line of rationale.
3. The single biggest methodological risk you see, and the one freeze-time condition you would add.
4. Any place the design looks aimed at a desired result (anti-cheat), or "none".
"""

def main():
    r = call(PANEL["B"], SYSTEM, USER, max_tokens=1400)
    cost = billed_cost([[r]])
    out = {"model": PANEL["B"], "usage": r.get("usage"), "billed_cost": cost,
           "error": r.get("error"), "content": r.get("content")}
    with open(os.path.join(os.path.dirname(__file__), "VOTE-s204.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("=== NON-ANTHROPIC DECORRELATION VOTE (panel.B =", PANEL["B"], ") ===")
    print("billed_cost: $%.6f" % (cost or 0))
    print("error:", r.get("error"))
    print("---")
    print(r.get("content"))

if __name__ == "__main__":
    main()
