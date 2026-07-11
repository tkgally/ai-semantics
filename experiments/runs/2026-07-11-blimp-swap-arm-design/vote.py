"""s209 — one NON-ANTHROPIC decorrelation vote on the BLiMP R1 CONTENT-WORD-SWAP arm design gates.
PROTOCOL §2/§A3: QA input to the fresh-agent critic (who keeps verdict authority). panel.B (gpt-5.4-mini),
cutoff-aware preamble. Records usage.cost via billed_cost(). Writes VOTE-s209.json + prints a summary."""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = (
    "Today is 2026-07-11. You may encounter references to papers, datasets, or models that postdate "
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
Design under review: a CONTENT-WORD-SWAP behavioral control (the second required arm of a two-arm
training-confound control) for one already-run result.

Background. An earlier probe (BLiMP forced-choice sweep: 40 human-validated English grammatical minimal-pair
paradigms, 3 closed chat models, temperature 0, behavioral 2-alternative forced choice, both orders)
produced reading R1 = PROFILE-ALIGNED: per model, the Spearman across the 40 paradigms of the model's
per-paradigm forced-choice accuracy vs BLiMP's per-paradigm HUMAN agreement is positive on all three
(rho_prof = +0.606 / +0.543 / +0.628, n=40, all CIs exclude 0). Interpretation: "the panel is grammatically
hard where humans are hard." A binding freeze condition (C8/G8) declared R1 NON-PROMOTABLE to a claim
without controlling a training-frequency confound, and required BOTH: (arm 1) a corpus-frequency covariate
partialled from rho_prof — ALREADY RUN, returned SURVIVES-COVARIATE 3/3 (partial rho +0.572/+0.510/+0.606),
a ROBUSTNESS result, NOT a promotion, because it reuses the already-known accuracies and controls only a
SURFACE-LEXICAL C4 frequency proxy; and (arm 2) THIS content-word-swap arm, which G8 makes REQUIRED for any
human-comparison PROMOTION. Promotion candidacy requires SURVIVES (arm 1) AND SWAP-STABLE (arm 2).

What the swap arm tests. BLiMP is public and contamination-bounded (absolute accuracy 0.87-0.94 = an upper
bound). If the panel is right on the frozen BLiMP items partly because it has SEEN those exact strings, then
rho_prof partly measures which paradigms were better memorized, not shared grammatical-difficulty structure.
Replace the OPEN-CLASS content words (nouns, main-verb lemmas, adjectives, adverbs, proper names) with
NOVEL, FREQUENCY-MATCHED words, re-inflected to preserve morphology, while holding EXACT the contrast locus
(the one token that differs between the good and bad member) and the whole closed-class functional skeleton
(determiners, auxiliaries, complementizers, negation, quantifiers, wh-words, prepositions). If per-paradigm
accuracy is STABLE under swap, the profile does not ride on exact-string memorization. Fresh items + fresh
calls => the swapped accuracies are UNKNOWN at freeze, so (unlike the covariate arm) the designer cannot
tune the swap to a target; the only DoF is the build, fenced by a fresh-agent verifier reproducing the
swap-build from the frozen recipe before any item is scored.

Scope honesty (stated in the design): SWAP-STABLE rules out exact-string / lexical-item memorization; it
does NOT control CONSTRUCTION frequency (a content-swapped island is still a rare construction) — that is
the covariate arm's job, and even both arms reach construction frequency only indirectly. anchor = BLiMP
human agreement (human-comparison), never internal-contrast-only.

This design turns the swap-arm operationalization into three gates (it does NOT re-open Q1-C/Q2-A/Q3-A/G8,
all already ratified — only HOW the swap arm is built and scored).

Q1 (paradigm & item selection — accuracy-blind AND human-agreement-blind):
  A [DEFAULT] = 3 shallow + 3 deep = 6 paradigms, chosen within each depth stratum by a deterministic
      SWAPPABILITY score (count of open-class positions swappable without touching the contrast locus; ties
      by UID alphabetical), blind to accuracy and human agreement; ORIGINAL condition = the frozen 30 items
      per paradigm RE-RUN FRESH this session (so Delta-acc = acc_swap - acc_orig is a within-run PAIRED
      quantity, no known-accuracy exposure). ~2160 calls, ~$0.3-0.5.
  B = the >=2 + >=2 minimum (4 paradigms); cheaper, but no within-stratum replication.
  C = reuse the frozen prior original accuracies as the baseline (don't re-run originals); halves calls but
      re-imports the known-accuracy exposure the swap arm exists to escape.

Q2 (THE CRUX — the swap operationalization: frequency-balancing norm + POS/morphology preservation):
  A [DEFAULT] = SUBTLEX-US Lg10WF banding (a HUMAN-VALIDATED subtitle frequency norm, license-verified,
      recipe-not-corpus) + a FROZEN hand-curated POS-labelled content lexicon; each replacement matched
      within +-0.10 Lg10WF of the original, same POS, re-inflected. The plain 2009 SUBTLEX file has NO POS,
      so POS labelling is a curation DoF (frozen + verifier-reproduced).
  B = fetch + license-check the 2012 "SUBTLEX-US with PoS" file for auditable POS selection (removes the
      curation DoF; adds a not-yet-in-repo fetch under a no-unlicensed-adoption rule; fall back to A if the
      license check fails).
  C = C4 log-frequency banding (reuse the covariate arm's machinery): balances the swap on the SAME corpus
      family as the covariate arm, but on a PRETRAINING PROXY, not the human-validated norm. Sensitivity
      cross-check only; rejected as primary.

Q3 (grammaticality re-validation WITHOUT human subjects + promotion scope):
  A [DEFAULT] = mechanical construction-preservation + integrity check (POS/morphology match; contrast locus
      byte-identical; real-word membership in-band; no new agreement coincidence); a broken pair is dropped,
      logged, reported; a paradigm below a usable-pair floor is dropped and power re-stated; the lead
      spot-audits a fixed sample AS RESEARCHER (not a human-subject acceptability task). SWAP-STABLE (with
      the prior SURVIVES) => R1 becomes a promotion-review CANDIDATE (a later, separate, cross-session
      adversarial review writes the claim). SWAP-DROPS => R1 refused; the shadow-depth table's grammar-side
      row keeps only its within-panel DEPTH-GRADED sibling.
  B = add an automated acceptability screen (frozen parser / off-panel LLM) to drop semantically anomalous
      swaps; tighter, but its own DoF and risks importing a model's grammaticality opinion into the
      instrument.
  C = treat SWAP-STABLE as writing the R1 claim this session (no separate promotion review).

Verdict (INHERITED from the already-ratified parent design, not re-opened): SWAP-STABLE iff within-stratum
mean |Delta-acc| <= 0.05 on BOTH the shallow and deep strata for >=2/3 models; SWAP-DROPS iff mean
Delta-acc <= -0.05 within a stratum on >=2/3; else SWAP-INCONCLUSIVE. Both orders, position-bias netted;
the s205 INSTRUMENT-FAILURE guard carried verbatim. Cost of the RUN ~$0.3-0.5; ABORT_USD ~1.0. This design
session's only spend is this one vote.

Give, concisely:
1. Overall GO / GO-WITH-CONDITIONS / NO-GO on running this swap arm after gate ratification.
2. A per-gate vote: Q1 (A/B/C), Q2 (A/B/C), Q3 (A/B/C), each one line of rationale.
3. The single biggest methodological risk in the SWAP CONSTRUCTION itself (grammaticality / frequency /
   selectional anomaly), and the one freeze-time condition you would add.
4. Is the swap arm as designed a strong enough control that SWAP-STABLE + the prior SURVIVES-COVARIATE
   jointly license a HUMAN-COMPARISON promotion CANDIDACY (a later review still writes the claim)? Or is
   there a residual confound both arms miss that should bound the candidacy? One paragraph.
5. Any place the design looks aimed at a desired result (anti-cheat), or "none".
"""

def main():
    r = call(PANEL["B"], SYSTEM, USER, max_tokens=1600)
    cost, n, n_missing = billed_cost([[r]])  # billed_cost returns (cost, n, n_missing)
    out = {"model": PANEL["B"], "usage": r.get("usage"),
           "billed_cost": cost, "n": n, "n_missing": n_missing,
           "error": r.get("error"), "content": r.get("content")}
    with open(os.path.join(os.path.dirname(__file__), "VOTE-s209.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("=== NON-ANTHROPIC DECORRELATION VOTE (panel.B =", PANEL["B"], ") ===")
    print("billed_cost: $%.6f (n=%d, missing=%d)" % (cost or 0, n, n_missing))
    print("error:", r.get("error"))
    print("---")
    print(r.get("content"))

if __name__ == "__main__":
    main()
