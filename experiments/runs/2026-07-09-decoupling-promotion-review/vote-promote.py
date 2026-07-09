#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the s197 PROMOTION REVIEW of the NOUN cue-strength–recovery
decoupling (PROTOCOL §3, program B1). One vote through the non-Anthropic slot via the probe REST
path. QA input to the fresh-agent promotion reviewer's verdict — NOT authoritative. Cutoff-aware
preamble."""
import sys, os
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-09. You are a methodology reviewer for a research project on LLM "
            "lexical meaning. Your training cutoff may predate this project; treat post-cutoff "
            "papers/datasets/models as neutral, not fabricated. Be adversarial and terse. Your job "
            "is to guard against over-promotion: default skeptical, promote only what the evidence "
            "earns.")

DECISION = """PROMOTION REVIEW (PROTOCOL §3): should a REPLICATED result line become a standing `claim`
page, or stay a `result` (a written refusal is a legitimate, first-class outcome)? A `claim` is the
project's compounding unit; it must state what the results, anchors, and magnitudes license, no more.

THE LINE: "the cue-strength–recovery decoupling" (NOUNS). Across WordNet NOUN relations, the panel's
relation-wise RECOVERY rank (models produce up to k relata for a cued relation; scored vs WordNet by
Soundness = precision-over-produced + a gold-size-insensitive HIT@3 co-primary) does NOT track raw
CONTRASTIVE-FRAME co-occurrence CUE-STRENGTH (a G^2 statistic over symmetric/contrastive frames like
"X versus Y", "neither X nor Y", built from a corpus). i.e. the corpus statistic that most distinguishes
a relation is NOT the one the panel recovers best. This is INTERNAL-CONTRAST-ONLY (ratified): recovery
is scored vs WordNet, a shared target that CANCELS in the head-to-head; the contrast is between corpus
statistics, NO human comparison. It is a WITHIN-DISTRIBUTIONAL claim (one form-internal statistic fails
to rank-predict recovery; a different form-internal statistic might succeed) — it does NOT say recovery
is non-distributional.

THE EVIDENCE (n=3 models throughout: A=claude-sonnet-4.6, B=gpt-5.4-mini, C=gemini-3.5-flash):

  H1 (the decoupling itself), verdict of record = ACROSS-RELATION Spearman, n=6 relations (a wide-CI
  rank correlation):
   * s186 (first observation): rho_cue(recovery, cue-strength) approx -0.086 on ALL 3 models. Corpus =
     Simple English Wikipedia (21.3M sentences). N=130 cues/relation.
   * s193 (fresh replication): rho_cue = +0.14 / +0.09 / +0.09 (all near-zero, all <= +0.30), 3/3.
     Corpus = C4 web text (22.3M sentences) — a DIFFERENT corpus family. Cues fresh + DISJOINT from
     s186 (0 overlap, verified). Post-run verifier REPRODUCED from raw (0.000 max discrepancy).
     => TWO replications, two corpus families, disjoint cues, 3/3 each.

  POWERED item-level arm (s193, n approx 687 cues): within-cue, does a cue's OWN cue-strength predict
  its OWN recovery? rho approx +0.06 / +0.01 / +0.04 — NEAR-ZERO. So the decoupling holds; but note the
  positive-replacement story (H2 below) is ALSO near-zero at item level => the depth effect (H2) is
  BETWEEN-RELATION only, not within-cue. The decoupling (H1) is an absence and holds at both grains.

  H2 (the proposed positive REPLACEMENT predictor — "what predicts recovery if cue-strength doesn't"):
  a PRE-REGISTERED taxonomic proxy, IS-A path depth, out-predicts cue-strength on 2/3 (rho_depth
  -0.20 / -0.37 / -0.37, predicted negative; clears the 0.20 margin on B and C, NOT A). SINGLE RUN
  (s193 only), between-relation only, and the co-registered corpus "Hearst-frame" proxy LOST
  (wrong-signed 0/3). So the positive half is thin: 2/3, one run.

  CROSS-POS (s196): the SAME decoupling tested on ADJECTIVES (Justeson & Katz 1991's MEASURED home POS
  for contrastive-frame saturation) DID NOT cleanly replicate: rho_cue = +0.4 / +0.8 / +0.4 (H1-PARTIAL),
  and the powered item-level arm AGREES (rho approx +0.25, all 3) — on adjectives cue-strength PARTIALLY
  predicts recovery. Reason: on nouns the decoupling was carried by HYPERNYMY (a low-cue-strength but
  taxonomically-central relation) being best-recovered, scrambling the rank; ADJECTIVES HAVE NO
  hypernymy (no IS-A taxonomy), so nothing scrambles the rank. So the clean decoupling is NOUN-SPECIFIC,
  carried by a taxonomic relation adjectives lack. The result page AND the essay both currently say:
  "the decoupling->claim promotion is BLOCKED — a claim needs the decoupling to hold across POS, and it
  did not." THE QUESTION THIS REVIEW MUST DECIDE: does a *NOUN-SCOPED* claim (explicitly not cross-POS)
  clear the bar, or does the whole line stay a result?

HONEST CASE **FOR** a noun-scoped claim:
 - Two independent replications, two corpus families, disjoint cues, 3/3 each — a stronger replication
   record than several already-promoted claims (some single-run-flagged).
 - It survived its control comparison: the decoupling is a comparison of two DIRECTLY-MEASURED rankings;
   the weak-control caveat (a fired calibration gate) only affects the separate RESIDUAL arm, not the
   decoupling.
 - The s196 POS boundary is CHARACTERIZING, not disconfirming: it explains the mechanism (taxonomic
   centrality via hypernymy) and gives the claim a clean scope (nouns, where the taxonomy exists).
 - internal-contrast-only is ratified, so no human-anchor obligation blocks it.

HONEST CASE **AGAINST** (stay a result / written refusal):
 - The verdict of record is a WIDE-CI n=6 Spearman, twice. "Twice-replicated" = two agreeing 6-point
   rank correlations; the powered arm (n~687) speaks to item level, where the effect is between-relation
   only. Is a twice-agreeing n=6 rank correlation a firm enough base for a STANDING claim?
 - It is a NEGATIVE/ABSENCE claim ("cue-strength does NOT rank-predict recovery"). The claims layer is
   mostly positive capability/sensitivity claims; is an absence the right thing to promote, vs. leaving
   it as a well-documented result the essay already reads?
 - The POSITIVE replacement (H2 taxonomic depth) — the interesting, forward-looking half — is 2/3,
   SINGLE run, between-relation only, Hearst arm lost. A claim would either omit H2 (promoting only the
   absence) or lean on a thin single-run positive.
 - The result + essay already say promotion is "blocked"; scoping to nouns is a real move, but is it
   rescuing a claim the evidence doesn't quite carry, or honestly recognizing a noun-scoped fact?

YOUR VOTE. State ONE of:
  PROMOTE-NOUN-SCOPED  (a claim earns it; say exactly what scope: the H1 absence only, or H1+H2; what
                        magnitude/interval language is honest given n=6 Spearman; what must be disclaimed)
  REFUSE               (stays a result; say what evidence a future run would need to earn promotion)
  PROMOTE-WITH-DIFFERENT-SCOPE  (specify)
Then <=7 terse bullets of rationale. Be adversarial: if you PROMOTE, name the single sentence the claim
must NOT say; if you REFUSE, name the single strongest FOR-argument you are overriding and why."""

r = call(PANEL["B"], PREAMBLE, DECISION, temperature=0, max_tokens=1000)
print(r["content"])
b = billed_cost([[r]])
print("\n--- billed:", b, "err:", r.get("error"))
with open("vote-promote.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${b[0]:.6f}; model {PANEL['B']}; s197 promotion-review vote]\n")
