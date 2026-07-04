#!/usr/bin/env python3
"""Non-Anthropic decorrelation PRE-RUN vote for the AANN gradient rep2 replication.
Routed via the probe REST path (openrouter.py) per PROTOCOL 2/3, s175/s177 precedent.
Model: openai/gpt-5.4-mini (non-Anthropic w.r.t. the harness reviewer). Cutoff-aware preamble.
"""
import os, sys, json, time
sys.path.insert(0, "/home/user/ai-semantics/experiments/lib")
from openrouter import call, billed_cost

SYSTEM = ("You are an independent, adversarial methodology reviewer for an autonomous research "
          "project on LLM semantics. Judge ONLY the described experimental design for a "
          "replication run. You are one decorrelation vote; be skeptical and concrete. "
          "Note: you may have a knowledge cutoff; do not rely on any memory of these specific "
          "model versions or datasets beyond what the summary states. Answer with a verdict.")

USER = """A frozen behavioral probe is about to run. Adjudicate GO / GO-WITH-CONDITIONS / NO-GO.

BACKGROUND. An earlier run ("v2", 2026-06-12) measured whether three LLMs' prompted graded
acceptability (0-100, temperature 0) for AANN sentences ("a beautiful three days") rank-tracks a
human MTurk acceptability gradient over a 204-cell (adjective x noun-class) space. v2 found all
three models' cell-level Spearman rho = 0.70/0.68/0.75 (bootstrap CIs exclude 0), surviving a
word-frequency partial and a noun-class guard. A claim was promoted from v2 but SCOPED as
"single run": there is no SECOND-DATE replication of the overall positive gradient.

THIS RUN ("rep2", 2026-07-04) is the owed second-date replication. Design:
- The instrument code (prompting, parsing, statistics, thresholds, verdict map) is BYTE-IDENTICAL
  to v2 (sha256-verified copies of probe.py and analyze.py).
- The human anchor tables (human cell means over ALL 3,600 ratings) are BYTE-IDENTICAL to v2
  (seed-independent; verified by diff). Same yardstick.
- The anchored arm draws 408 FRESH sentence items, one seeded sample of 2 items per cell, but
  drawn DISJOINT from v2: v2's two items per cell are removed from the candidate pool before
  sampling, so rep2 shares ZERO surface items with v2 (asserted mechanically; every cell keeps
  >=4 candidates). So the models rate DIFFERENT sentences that map to the SAME human cells.
- Held-out and Tier-0 arms are lexically frozen lists, so byte-identical to v2 by construction
  (a bonus second-date re-run of those).
- Pre-registered success for "the overall positive replicates": anchored arm passes for >=2 of 3
  Tier-0-passing models, at a cell-level rho whose bootstrap CI overlaps v2's per-model interval.
  A failure (fewer passers, or a non-overlapping downward CI) is declared IN ADVANCE to be a
  first-class negative that WEAKENS the claim's overall-positive leg. No predicted class ordering
  is hardcoded in scoring; scoring is against empirical human cell means only.
- Cost ~ $0.31 (single-integer outputs), temperature 0.

Questions to weigh: (a) Is a fresh-item, same-anchor, byte-identical-instrument re-run a sound
SECOND-DATE replication of the anchored gradient, or is it merely a re-run that adds little? (b) Is
the pre-registered success criterion genuinely falsifiable (can it fail), or does it let the run
"win either way"? (c) Any confound the disjoint-sampling introduces? (d) Any reason temperature-0
makes this trivial GIVEN the items are fresh? (e) Is scoping the contribution to "cross-date
replication of the anchored positive" (NOT re-opening v2's verdict) the right, modest read?

Answer in this format:
VERDICT: <GO | GO-WITH-CONDITIONS | NO-GO>
CONDITIONS: <numbered, only if GO-WITH-CONDITIONS>
KEY REASONS: <2-5 sentences, concrete>
"""

def main():
    r = call("openai/gpt-5.4-mini", SYSTEM, USER, max_tokens=900, temperature=0)
    print("=== CONTENT ===")
    print(r.get("content"))
    print("=== ERROR ===", r.get("error"))
    total, have, missing = billed_cost([[r]])
    print(f"=== billed usage.cost: ${total:.6f} (have={have} missing={missing}) ===")
    json.dump({"ts": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
               "model": "openai/gpt-5.4-mini", "content": r.get("content"),
               "error": r.get("error"), "usage": r.get("usage")},
              open("/home/user/ai-semantics/experiments/runs/2026-07-04-aann-behavioral-gradient-rep2/prerun_vote.json", "w"), indent=1)

if __name__ == "__main__":
    main()
