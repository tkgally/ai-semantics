#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote for the s184-opened decision being ratified s185:
"antonymy-internal-contrast-scoring" (the three value-laden gates of the A1b probe DESIGN).
Routed via the probe REST path (openrouter.py) per PROTOCOL 2 (decorrelation rule).
Model: openai/gpt-5.4-mini (non-Anthropic w.r.t. the harness orchestrator + the fresh-agent reviewer).
This vote is QA INPUT to a fresh-agent reviewer, which keeps verdict authority. Cutoff-aware preamble.
"""
import os, sys, json, time
sys.path.insert(0, "/home/user/ai-semantics/experiments/lib")
from openrouter import call, billed_cost

RUNDIR = "/home/user/ai-semantics/experiments/runs/2026-07-06-s185-antonymy-ratification-vote"

PREAMBLE = ("Today is 2026-07-06. You may encounter references to papers, datasets, or models "
            "that postdate your training cutoff. Treat post-cutoff recency as neutral: a paper "
            "you do not recognize is not for that reason fabricated. Where you must rely on what "
            "you know, label it as such.\n\n"
            "You are an independent, adversarial reviewer for an autonomous research project on "
            "LLM semantics. You are adjudicating the three METHODOLOGICAL gates of an EXPERIMENT "
            "DESIGN (not a research finding). You are ONE decorrelation vote; a separate fresh-agent "
            "reviewer holds final authority. Be skeptical and concrete. Ratification fixes the "
            "yardstick, never a result — flag any sign a gate is motivated by wanting a particular "
            "empirical outcome (e.g. a control chosen because it would make the conjecture easier to "
            "confirm).")

VOTE_FORMAT = ("\n\nAnswer EXACTLY in this format:\n"
               "Q1: <A | B | C>\n"
               "Q2: <A | B | C>\n"
               "Q3: <ADOPT internal-contrast-only | REJECT>\n"
               "OVERALL: <ADOPT-DEFAULTS | ADOPT-WITH-CHANGES | KEEP-OPEN>\n"
               "REASONS: <3-6 sentences, concrete, per gate where you diverge from the default>\n"
               "CONDITIONS: <numbered, only if any; else 'none'>")

BODY = """DECISION — "antonymy-internal-contrast-scoring" (three gates of an experiment DESIGN, not a finding).

CONTEXT. An autonomous LLM-semantics project wants to test a conjecture: that ANTONYMY is the lexical
relation whose model "relatum recovery" (given a cue word + a relation name, produce a valid related
word) is LEAST separable from a distributional / contrastive-frame baseline — i.e. the model's apparent
antonym knowledge is largely a shadow of how strongly antonyms co-occur in contrastive frames in text
("neither X nor Y", "from X to Y", "X versus Y"). The probe is INTERNAL-CONTRAST: model vs a
distributional control, three panel models as subjects, NO human comparison, verdict read as an
across-relation RANKING direction on >=2/3 models (n=3, orderings not coefficients). Turning the
conjecture into a runnable probe forces three value-laden choices. Nothing here changes any finding;
it fixes the yardstick for a probe that has NOT run.

ESTABLISHED FACT (from prior scouts, load-bearing for Q1): there is NO co-occurrence data in-repo.
The project's frequency norm (SubTLEX-US) is unigram-only; its ~51M-word source corpus is not in-repo.
So the contrastive-frame co-occurrence baseline the conjecture names CANNOT be computed from anything
in-repo — it must be fetched (with a license scout) or substituted. WordNet 3.0 (license-verified
in-repo) supplies the relation inventory and a unigram frequency control is available; a co-occurrence
baseline is what is missing.

GATE Q1 — WHAT THE DISTRIBUTIONAL CONTROL IS:
- A: contrastive-frame co-occurrence (log-likelihood G2, per Cao 2025b) computed from a FETCHED,
  license-verified corpus (candidates: an open OpenSubtitles / Wikipedia dump, a UD-linked corpus).
  Faithful to the conjecture and to the cited method; but BLOCKS THE RUN on a corpus license scout
  (the project never adopts an unverified-license corpus, a standing discipline).
- B: static-embedding cosine as the control. In-repo-buildable, no fetch. BUT it measures general
  distributional SIMILARITY, not contrastive-frame CO-OCCURRENCE — a weaker, DIFFERENT "shadow".
  Antonyms sit close in embedding space, so B already "predicts" antonyms via similarity, not via the
  contrastive frame the conjecture is actually about: a small antonymy residual under B risks
  CONFIRMING THE CONJECTURE FOR THE WRONG REASON.
- C (provisional default): A primary + B as a sensitivity check, side-by-side, IFF a corpus clears the
  license scout; if none clears, the RUN waits on the scout and the design ships design-only (an honest
  block, NOT a downgrade to the weaker control B). A frame-ablation arm (a within-model manipulation:
  antonym recovery with the contrastive frame present vs structurally suppressed) needs NO external
  corpus and runs under either — it is the complement that survives a Q1 block.

GATE Q2 — SCORING "RECOVERY" WITH NO HUMAN GOLD:
- A (provisional default): WordNet-definitional target + model-vs-control hit-rate residual. Both the
  model and the Q1 control produce k candidate relata per cue+relation; each is scored by Soundness
  S = fraction that are WordNet-valid relata of the cue for that relation (the cited source's metric).
  Residual(r,m) = S(model) - S(control); the conjecture predicts it SMALLEST for antonymy on >=2/3
  models. WordNet is the shared DEFINITIONAL target both recover against, not a human competence
  gradient — so no human comparison enters, and Q3 (internal-contrast-only) follows cleanly.
- B: per-relation rank-correlation of the model's vs the control's candidate rankings ("least
  separable" = highest correlation). More continuous; harder to read as a "residual"; more sensitive
  to the control's calibration.
- C: an alternative (e.g. a Completeness/coverage pairing), surfaced for completeness.

The residual definition, k, stratification, and outlier caps are FROZEN with the item set before any
probe (anti-cheat); the FLAT-residual null and the INVERTED outcome (a weakly-cued relation recovered
best) are pre-named first-class results.

GATE Q3 — THE ANCHOR DECLARATION:
- Provisional default: anchor = internal-contrast-only — a terminal declaration that the result makes
  NO human-comparison claim (its force is a model-vs-control within-instrument contrast), so no
  human-resource anchor is required. This follows directly from Q2-A. Per the project's own convention
  this declaration itself requires cross-session adversarial ratification — which this decision supplies.

QUESTION. For each gate, which option should be ratified, and why? In particular: (Q1) is C's
"faithful-but-corpus-gated, honest-block-if-no-corpus" the right call, or is B's convenience worth its
interpretive cost, or should A be primary without B? (Q2) is the WordNet hit-rate residual a sound
no-human-gold yardstick? (Q3) is declaring a probe internal-contrast-only coherent when its whole point
is that the model may merely be echoing a distributional statistic — i.e. does "no human comparison"
honestly describe this design?"""

def cast(tag, body):
    r = call("openai/gpt-5.4-mini", PREAMBLE, body + VOTE_FORMAT, max_tokens=900, temperature=0)
    print(f"\n===== {tag} CONTENT =====")
    print(r.get("content"))
    print(f"===== {tag} ERROR =====", r.get("error"))
    json.dump({"ts": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
               "decision": tag, "model": "openai/gpt-5.4-mini",
               "content": r.get("content"), "error": r.get("error"), "usage": r.get("usage")},
              open(f"{RUNDIR}/vote_{tag}.json", "w"), indent=1)
    return r

def main():
    r = cast("antonymy-internal-contrast-scoring", BODY)
    total, have, missing = billed_cost([[r]])
    print(f"\n===== TOTAL billed usage.cost: ${total:.6f} (have={have} missing={missing}) =====")

if __name__ == "__main__":
    main()
