#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote (QA input) for the DESIGN pre-run critic of the s192-designed
fresh relation-recovery / taxonomic-proxy probe (H1 + H2). Routed via the probe REST path
(openrouter.py) per PROTOCOL 2 / A3 (decorrelation rule). Model: openai/gpt-5.4-mini (non-Anthropic
w.r.t. the harness orchestrator + the fresh-agent critic). This vote is QA INPUT to a fresh-agent
pre-run critic, which keeps GO/NO-GO authority. Cutoff-aware preamble.
"""
import os, sys, json
sys.path.insert(0, "/home/user/ai-semantics/experiments/lib")
from openrouter import call, billed_cost

RUNDIR = "/home/user/ai-semantics/experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy-design"
MODEL = "openai/gpt-5.4-mini"

PREAMBLE = ("Today is 2026-07-08. You may encounter references to papers, datasets, or models that "
            "postdate your training cutoff. Treat post-cutoff recency as neutral: a paper you do not "
            "recognize is not for that reason fabricated. Where you must rely on what you know, label "
            "it as such.\n\n"
            "You are an independent, adversarial PRE-RUN CRITIC for an autonomous research project on "
            "LLM semantics. You are reviewing the four METHODOLOGICAL gates of an EXPERIMENT DESIGN "
            "(not a research finding), and giving a GO / NO-GO on the design. You are ONE decorrelation "
            "vote; a separate fresh-agent critic holds final authority. Be skeptical and concrete. "
            "Ratification/GO fixes the yardstick, never a result — flag any sign a gate is motivated by "
            "wanting a particular empirical outcome (e.g. a test chosen because it would make H2 easier "
            "to confirm), and flag any goalpost-moving.")

VOTE_FORMAT = ("\n\nAnswer EXACTLY in this format:\n"
               "Q1: <A | B | C>\n"
               "Q2: <A | B | C>\n"
               "Q3: <A | B | C>\n"
               "Q4: <ADOPT internal-contrast-only | REJECT>\n"
               "OVERALL: <GO | GO-WITH-CONDITIONS | NO-GO>\n"
               "REASONS: <4-7 sentences, concrete, per gate where you diverge from the default>\n"
               "CONDITIONS: <numbered, only if any; else 'none'>")

BODY = """DESIGN — a FRESH lexical-relation-recovery probe testing two registered bets (H1, H2). Four
value-laden gates. INTERNAL-CONTRAST: three panel models as subjects, NO human comparison; verdict is an
across-relation RANKING direction on >=2/3 models (n=3, orderings not coefficients). Nothing has run.

BACKGROUND (established, not up for debate here):
- A prior probe (s186) over SIX WordNet NOUN relations (antonymy, synonymy, hypernymy, hyponymy,
  holonymy, meronymy), 130 cues/relation, scored model relatum-recovery (given a cue + relation name,
  produce valid relata) as Soundness S (precision over produced) with a gold-size-insensitive HIT@3
  co-primary, against a contrastive-frame co-occurrence (log-likelihood G2) control built from Simple
  English Wikipedia. It found a CUE-STRENGTH-RECOVERY DECOUPLING: across the six relations, raw recovery
  and corpus contrastive-frame cue-strength are ~uncorrelated (across-relation Spearman -0.086, 3/3):
  antonymy tops cue-strength but hypernymy tops recovery; meronymy is 2nd-most-cued yet worst-recovered.
- An essay turned that into TWO registered falsifiable bets. H1 (safer): on a FRESH test (fresh cues /
  different control corpus / adjective replication) recovery rank AGAIN decouples from cue-strength
  (near-zero-or-negative across-relation rank corr, >=2/3); falsified if cue-strength recovers predictive
  power (clearly positive) on the fresh set. H2 (riskier): recovery rank tracks a PRE-REGISTERED
  taxonomic/definitional-structure proxy BETTER than cue-strength; falsified if no such proxy
  out-predicts cue-strength.
- A $0, deliberately NON-CIRCULAR pilot pre-registered ONE proxy on principle: IS-A PATH DEPTH
  (WordNet min_depth of each cue's first noun synset, averaged per relation), predicted sign NEGATIVE
  (more-superordinate/shallower cue sets recover better). The pilot explicitly REFUSED the strongest
  correlate it found (gloss length, rho -0.83) because picking the top correlate on the
  hypothesis-generating data is fishing; IS-A depth (rho -0.60) was chosen for being the most standard
  operationalization of "position in the hierarchy", well-behaved, and theory-set in sign.
- The scoring gates (WordNet-target Soundness/HIT@3 residual; internal-contrast-only anchor) and the G2
  control construction were RATIFIED for the s186 sibling and are REUSED here, not re-litigated.

This design changes exactly three things vs s186 to make it a FRESH test: fresh cues disjoint from
s186's 780 (freq-matched, outlier-capped); a DIFFERENT control corpus; and a pre-registered taxonomic
proxy (IS-A depth) computed BEFORE recovery is seen. It DROPS the s186 frame-ablation arm.

GATE Q1 — LEVEL OF ANALYSIS FOR H2 (the anti-goalpost-moving gate; load-bearing):
The essay registered H2 as an ACROSS-RELATION rank hypothesis (recovery rank vs proxy rank over the 6
relations, head-to-head vs cue-strength rank). But n=6 relations cannot be a significant Spearman. IS-A
depth is a PER-CUE property, so a far more powerful ITEM-LEVEL test exists (regress a cue's recovery on
its own IS-A depth, N ~ 700-900). Choosing item-level ALONE silently redefines H2 after the fact.
- A: across-relation rank ONLY (6 points). Faithful to the exact registered bet; underpowered.
- B: item-level cue-depth regression ONLY (~700-900 items; powered). Powered, but a DIFFERENT
  hypothesis (within-relation cue-depth -> recovery); adopting it alone moves the goalposts.
- C (provisional default): across-relation rank PRIMARY and verdict-bearing (n=6, reported with its wide
  CI), PLUS the item-level analysis as a POWERED SECONDARY reported side-by-side. Head-to-head of record
  stays |rho(depth,recovery)| vs |rho(cue-strength,recovery)| across relations, >=2/3; item-level buys
  power and guards an n=6 fluke WITHOUT changing what H2 was registered to predict; a divergence between
  the two levels is itself a first-class reported outcome.

GATE Q2 — THE FRESH CONTROL CORPUS (both cleared a firsthand license scout):
s186 used Simple English Wikipedia. H1's falsifier wants a DIFFERENT corpus so a positive H1 outcome
can't be a same-corpus artifact.
- A: full English Wikipedia (CC BY-SA 4.0 + GFDL). Cleanest license, best pretraining proxy, billions of
  words; but SAME source family as Simple Wikipedia (encyclopedic) -> weakest register-decorrelation.
- B: C4 (allenai/c4, ODC-BY). Web register, genuinely different; strongest fresh test; heavier fetch
  (~305GB, streamable, only fixed cue set counted).
- C (provisional default): full English Wikipedia PRIMARY + C4 as a labelled register-decorrelation
  SENSITIVITY arm iff tractable; if only one is tractable, Wikipedia primary and the C4 arm deferred and
  NAMED (honest scope note, not silent drop).

GATE Q3 — THE SECOND PRE-REGISTERED PROXY ARM:
The pilot pre-registered IS-A depth alone but flagged that the essay's actual "definitional-frame
statistic" means CORPUS Hearst-style hypernym frames ("X such as Y", "Y and other X"); WordNet gloss
length is only a cheap echo (deliberately NOT frozen). The Q2 corpus is fetched anyway, so a corpus
Hearst-frame proxy is nearly free.
- A (provisional default): IS-A depth PRIMARY + a corpus Hearst-frame definitional-density proxy as a
  SECOND pre-registered arm; per the essay H2 fires if ANY pre-registered taxonomic/definitional proxy
  out-predicts cue-strength (>=2/3); both specs + predicted signs frozen before recovery; a
  pre-registered multiple-comparison rule (a NAMED proxy must win in its PRE-REGISTERED direction).
- B: IS-A depth ONLY (simplest; forgoes a nearly-free arm; leaves the essay's named candidate untested).
- C: add ill-behaved candidates (subtree connectivity, polysemy). REJECTED up front by the pilot.

GATE Q4 — ANCHOR:
- Provisional default ADOPT internal-contrast-only: recovery is scored vs WordNet as a shared
  definitional target that CANCELS in the head-to-head; predictors (G2 cue-strength, IS-A depth, Hearst)
  are corpus/lexicon statistics; no human baseline enters -> no human-comparison claim, no resource
  anchor required (following the s186 sibling's ratified anchor exactly).

YOUR TASK: vote each gate; give an OVERALL GO / GO-WITH-CONDITIONS / NO-GO on the design proceeding to
freeze after cross-session ratification. Focus especially on Q1: is C a genuine anti-goalpost-moving
safeguard, or does the powered item-level secondary risk becoming the de-facto verdict? Flag any way the
design could confirm H2 for the wrong reason, any residual goalpost-moving, and any freeze-time
condition you would bind."""

def main():
    resp = call(MODEL, PREAMBLE, BODY + VOTE_FORMAT, max_tokens=900,
                reasoning={"effort": "minimal"})
    out = resp.get("content", "")
    cost = billed_cost([[resp]])
    with open(os.path.join(RUNDIR, "vote_stdout.txt"), "w") as f:
        f.write(out + "\n\n---\nbilled_cost_usd: " + str(cost) + "\n")
    json.dump({"model": MODEL, "content": out, "usage": resp.get("usage"),
               "error": resp.get("error"), "billed_cost_usd": cost},
              open(os.path.join(RUNDIR, "vote.json"), "w"), indent=2)
    print(out)
    print("\n---\nbilled_cost_usd:", cost)

if __name__ == "__main__":
    main()
