#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the s193 RATIFICATION of the four gates of the
fresh relation-recovery / taxonomic-proxy design (PROTOCOL §2). One vote through the
non-Anthropic slot via the probe REST path. QA input to the fresh-agent ratifier's
verdict — NOT authoritative. Cutoff-aware preamble."""
import sys, os
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-08. You are a methodology reviewer. Your training cutoff may "
            "predate this project; treat post-cutoff papers/datasets/models as neutral, not "
            "fabricated. Judge the ratification below on its internal merits; be adversarial "
            "and terse.")

DECISION = """We are RATIFYING (fixing the yardstick for) a frozen-but-not-yet-run behavioral probe.
It is internal-contrast (NO human comparison). The probe tests, over 6 WordNet NOUN relations
(antonymy, synonymy, hypernymy, hyponymy, holonymy, meronymy), two pre-registered bets that came
from an earlier run (s186, on Simple English Wikipedia):
  H1: relation-recovery rank DECOUPLES from contrastive-frame co-occurrence cue-strength again, on a
      FRESH test (different corpus + fresh disjoint cues). Falsified if cue-strength recovers its
      predictive power (clearly positive rank correlation, >=2/3 models).
  H2: a PRE-REGISTERED taxonomic proxy (IS-A path depth = mean WordNet min_depth of each cue's first
      noun synset; predicted sign NEGATIVE = shallower/more-superordinate cue sets recover better)
      OUT-PREDICTS cue-strength for relation-wise recovery, >=2/3 models.

FOUR GATES to ratify (options; the design's provisional defaults in [brackets]):

Q1 - level of analysis for H2 (anti-goalpost gate).  n=6 relations is underpowered as a Spearman; a
     powered ITEM-LEVEL test (~700-900 cues, regress a cue's recovery on its own IS-A depth) tests a
     DIFFERENT (within-relation) hypothesis.
   A: across-relation rank only (faithful to the registered bet; underpowered)
   B: item-level only (powered but a different hypothesis; adopting alone moves the goalposts)
   [C]: across-relation rank PRIMARY + sole verdict-of-record; item-level POWERED SECONDARY, strictly
        descriptive/robustness-only (can never fire H2 or upgrade an across-relation H2-loss).

Q2 - the fresh control corpus (s186 used Simple English Wikipedia).
   A: full English Wikipedia (cleanest license; but SAME encyclopedic source-family as Simple Wiki -
      weakest register-decorrelation, so a weak H1 falsifier)
   B: C4 (allenai/c4, web register; genuinely DIFFERENT register - the strongest fresh test;
      streamable in a few ~350MB shards, so tractable under ~30GB free disk)
   [C]: full Wikipedia PRIMARY + C4 as a sensitivity arm if tractable.
   NOTE: the design-stage non-Anthropic vote and the fresh-agent ratifier BOTH argued full Wikipedia
   is too close to s186's register to be a strong H1 falsifier; the fresh ratifier RULED C4 PRIMARY
   (option B), demoting full Wikipedia to an optional same-family sensitivity arm, on both
   methodological grounds (C4's web register is the real decorrelation; Common-Crawl text is at least
   as good a pretraining proxy as Wikipedia) and tractability (C4 streams in bounded shards; the 22GB
   Wikipedia dump extraction strains 30GB disk).

Q3 - the second pre-registered proxy arm.
   [A]: IS-A depth PRIMARY + a corpus Hearst-frame ("X such as Y", "Y and other X") definitional-
        density proxy as a SECOND pre-registered arm, with a multiple-comparison rule (H2 fires only
        if a NAMED proxy wins in its PRE-REGISTERED direction; a Hearst-only win is reported as
        qualified/weaker, not equal-status).
   B: IS-A depth only.
   C: add ill-behaved candidates (subtree connectivity, polysemy) - REJECTED up front (fishing).

Q4 - anchor: [internal-contrast-only].  Recovery is scored vs WordNet as a shared target that CANCELS
     in the head-to-head; both predictors (contrastive-frame G2, IS-A depth / Hearst density) are
     corpus/lexicon statistics; no human recovery baseline enters. So no human-comparison claim; no
     resource anchor required.

ANTI-CHEAT context: every proxy spec, predicted sign, rho-band, and verdict threshold is frozen in
PREREG before ANY model call; H1-break, H2-lose, both-null, and across-vs-item-level divergence are all
pre-named first-class outcomes; the earlier pilot refused the strongest correlate (gloss length,
rho=-0.83) on principle because picking it on hypothesis-generating data is fishing.

VOTE: For EACH gate say ADOPT-<letter> (or KEEP-OPEN + what's missing). Then judge: (1) is this a
FAIR, non-question-begging test where confirm / H1-break / H2-lose / null are all genuinely reachable?
(2) Do you AGREE with the fresh ratifier's C4-PRIMARY ruling on Q2, or would you keep C4 as a
sensitivity arm? Reply with per-gate letters first, then <=6 terse bullets."""

r = call(PANEL["B"], PREAMBLE, DECISION, temperature=0, max_tokens=900)
print(r["content"])
b = billed_cost([[r]])
print("\n--- billed:", b, "err:", r.get("error"))
with open("vote-ratify.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${b[0]:.6f}; model {PANEL['B']}; s193 ratification vote]\n")
