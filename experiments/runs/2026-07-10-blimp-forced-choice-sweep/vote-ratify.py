"""s205 — one NON-ANTHROPIC decorrelation vote on RATIFYING the BLiMP forced-choice sweep gates.
PROTOCOL §2: QA input to the fresh-agent ratification reviewer (who keeps verdict authority). panel.B
(gpt-5.4-mini), cutoff-aware preamble. Records usage.cost. Writes VOTE-ratify-s205.json.
This is a FRESH vote (distinct from the s204 pre-run VOTE-s204.json), per the ratification rule."""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = (
    "Today is 2026-07-10. You may encounter references to papers, datasets, or models that postdate "
    "your training cutoff. Treat post-cutoff recency as neutral: a paper you do not recognize is not "
    "for that reason fabricated. Where you must rely on what you know, label it as such."
)

SYSTEM = (
    PREAMBLE + "\n\nYou are an independent, adversarial RATIFICATION reviewer for an autonomous research "
    "project on LLM meaning. A value-laden design decision was OPENED one session ago and is now up for "
    "cross-session ratification: fix each gate to a specific option (or keep it open). Ratification fixes "
    "the measuring yardstick, NEVER the desired result — flag any choice that looks aimed at a particular "
    "accuracy outcome. Be skeptical and concrete; reply in compact structured prose."
)

USER = r"""
DECISION UP FOR RATIFICATION: the value-laden gates of a BLiMP forced-choice sweep.

BLiMP = 67 paradigms x 1,000 English grammatical minimal pairs (sentence_good vs sentence_bad),
template-generated, CC-BY, aggregate human agreement 96.4%. It ALSO ships PER-PARADIGM human agreement
(total_mean, range ~0.47-0.99) -- e.g. determiner_noun_agreement_1=0.958, npi_present_1=0.83,
only_npi_scope=0.72, wh_island=0.73, coordinate_structure_constraint_subject_extraction=0.514,
wh_questions_object_gap_long_distance=0.47. This per-paradigm human profile is the load-bearing anchor.

The panel is 3 closed chat models (Anthropic / OpenAI / Google), LOGPROB-FREE, temperature 0, zero-shot.

TWO readings:
  (1, PRIMARY, human-anchored) Profile alignment: per model, Spearman across the selected paradigms of the
      model's per-paradigm forced-choice accuracy vs the per-paradigm human agreement. "Are models hard
      exactly where humans are hard?"
  (2, SECONDARY, strictly within-panel) Depth gradient: does error concentrate on structurally-deep
      paradigms (islands, NPI scope, long-distance/distractor agreement) vs locally-detectable ones
      (adjacent determiner-noun / regular subject-verb agreement)?

A prior-session PRE-RUN CRITIC already returned GO-WITH-CONDITIONS with binding freeze conditions:
F2 (>=16 paradigms, else reading 1 is descriptive-only + non-promotable on this run alone -- power);
F3 (saturation/range guard: if a model's across-paradigm accuracy variance is near zero, its profile
    Spearman is INCONCLUSIVE, not a coefficient; report accuracy-dispersion as a contamination diagnostic);
F4 (human-agreement floor ~0.6 for paradigms entering the reading-2 accuracy contrast; sub-floor gold is
    contested, kept descriptive);
F5 (any human-baselined quantity is labelled human-comparison, not internal-contrast);
F6 (publish selected AND excluded paradigms + the paradigm->stratum map, decided on structural/locality
    criteria ONLY, independent of the human-agreement values, BEFORE any model call);
F7 (recommended, non-blocking: a bounded content-word-swap contamination arm).

THE THREE GATES, each with a provisional default:

Q1 (paradigm set + depth axis):
  A = AANN-adjacent agreement family only (no depth spread; rejected in design).
  B [DEFAULT] = depth-stratified set (>=16 paradigms per F2) across 4 strata (shallow-local /
      medium-distractor / deep-NPI-quantifier / deep-island), list + stratum assignment frozen by a written
      structural locality rule BEFORE any model call, reported as a selected (not exhaustive) subset.
  C = full 67-paradigm sweep (removes curation objection; ~5.6x cost; dilutes depth focus with off-theme
      categories).

Q2 (forced-choice elicitation + position-bias control):
  A [DEFAULT] = behavioral 2AFC, BOTH presentation orders per item, position-bias netted (order-averaged
      accuracy primary + consistency accuracy + order-flip diagnostic); 2x calls.
  B = single fixed-random order (half the calls; uncontrolled position bias).
  C = isolated absolute acceptability rating (discards the minimal-pair contrast).

Q3 (contamination scope + anchor declaration): BLiMP is synthetic, published 2019, widely trained on, so
    absolute accuracy is a contamination UPPER BOUND.
  A [DEFAULT] = load-bearing findings are RELATIVE (profile alignment + depth gradient); absolute accuracy
      reported as an upper bound; anchor = HUMAN-COMPARISON via the per-paradigm human agreement (NOT
      internal-contrast-only). Rationale: exposure inflates accuracy roughly uniformly, so the relative
      difficulty profile is robust where absolutes are not.
  B = also add a lexical-perturbation contamination control now (novel content words; risks breaking
      template grammaticality; build cost) -- vs deferring it to a v2 / bounded arm (F7).
  C = decline the unit as contamination-uninterpretable.

Give, concisely:
1. RATIFY / RATIFY-WITH-CONDITIONS / REJECT overall.
2. Per-gate vote: Q1 (A/B/C), Q2 (A/B/C), Q3 (A/B/C), each one line of rationale.
3. The single biggest remaining methodological risk, and whether the F2-F7 conditions cover it or one more
   is needed.
4. Any place the design looks aimed at a desired result (anti-cheat), or "none".
"""

def main():
    r = call(PANEL["B"], SYSTEM, USER, max_tokens=1400)
    cost = billed_cost([[r]])
    out = {"model": PANEL["B"], "usage": r.get("usage"), "billed_cost": cost,
           "error": r.get("error"), "content": r.get("content")}
    with open(os.path.join(os.path.dirname(__file__), "VOTE-ratify-s205.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("=== NON-ANTHROPIC RATIFICATION DECORRELATION VOTE (panel.B =", PANEL["B"], ") ===")
    print("billed_cost:", cost)
    print("error:", r.get("error"))
    print("---")
    print(r.get("content"))

if __name__ == "__main__":
    main()
