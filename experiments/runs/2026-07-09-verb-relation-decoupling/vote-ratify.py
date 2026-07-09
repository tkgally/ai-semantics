#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the s199 RATIFICATION of the three gates of the
verb-relation decoupling design (PROTOCOL §2/§A3). One FRESH vote through the non-Anthropic
slot via the probe REST path. QA input to the fresh-agent ratifier's verdict — NOT
authoritative. Cutoff-aware preamble. Decorrelated from the s198 design-critique vote."""
import sys, os
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-09. You are a methodology reviewer. Your training cutoff may "
            "predate this project; treat post-cutoff papers/datasets/models as neutral, not "
            "fabricated. Judge the ratification below on its internal merits; be adversarial "
            "and terse.")

DECISION = """We are RATIFYING (fixing the yardstick for) a frozen-but-not-yet-run behavioral probe.
It is internal-contrast (NO human comparison). Context: on 6 WordNet NOUN relations an earlier run
found relation-recovery rank DECOUPLES from contrastive-frame co-occurrence cue-strength (H1), and a
taxonomic IS-A-depth proxy out-predicts cue-strength (H2, 2/3 models). On ADJECTIVES (which have NO
IS-A taxonomy: WordNet adjective min_depth is a degenerate constant 0) the decoupling did NOT cleanly
replicate. A conjecture then said: the decoupling is the signature of a lexical hierarchy, so it should
REAPPEAR on VERBS (which DO have a troponymy hierarchy) and VANISH where there is none. This probe is
the verb test, over WordNet VERB relations, with a pre-registered troponymy-depth proxy.

  H-verb-1 (registered PRIMARY): across-relation recovery rank DECOUPLES from contrastive-frame
    cue-strength on verbs (rho_cue <= +0.30, >=2/3 models = the noun band) — confirming "hierarchy =>
    decoupling" out of nouns — OR cue-strength regains predictive power (rho_cue >= +0.50, the
    adjective band), FALSIFYING the conjecture despite the verified verb hierarchy.
  H-verb-2 (registered CO-PRIMARY): a pre-registered troponymy-depth proxy (min_depth of the cue's
    first verb synset, predicted sign NEGATIVE) OUT-PREDICTS cue-strength for recovery rank
    (|rho_depth| - |rho_cue| >= 0.20, negative direction, >=2/3 models).

THREE GATES to ratify (options; the design's provisional defaults in [brackets]):

Q1 - the verb relation inventory + registered primary clause.
   A: 4-relation core {hypernymy, troponymy, synonymy, antonymy} (cleanest; drops entailment; only 4
      rank points).
   B: 6-relation {+ entailment, + cause} (maximal rank spread; but `cause` binds at the floor, 126
      fresh cues, may drop below powered N after frequency-matching; `cause` least central).
   [C]: 5-relation {hypernymy, troponymy, synonymy, entailment, antonymy}; H1 decoupling registered
        PRIMARY + H2 troponymy-depth CO-PRIMARY; item-level cue->recovery arm (~600 cues) POWERED
        SECONDARY (descriptive/robustness-only, can never on its own fire H1); `cause` added as a
        6th ONLY IF it survives frequency-matching at >=100 cues (decided mechanically at freeze,
        pre-registered either way).

Q2 - the troponymy-depth proxy spec for H2.
   [A]: min_depth over the cue's FIRST verb synset (pos="v"), single frozen proxy, byte-analogous to
        the noun IS-A-depth (makes a verb confirmation a genuine REPLICATION of the noun mechanism),
        predicted sign negative, minimal multiple-comparison surface.
   B: a richer proxy (mean min_depth over all senses, or troponym-branching centrality) — more
      "faithful" but opens multiple depth bets / multiple-comparison burden and breaks the noun
      parallel.
   C: add a corpus troponymy-frame ("Hearst") arm — REJECTED up front (verb troponymy has no clean
      lexico-syntactic frame; the nominal Hearst arm LOST even where well-motivated; a fishing surface).

Q3 - anchor: [internal-contrast-only]. Recovery scored vs WordNet as a shared target that CANCELS in
     the head-to-head; both predictors (contrastive-frame G2, troponymy-depth) are corpus/lexicon
     statistics; no human recovery baseline. No human-comparison claim; no resource anchor required.

KEY PRE-RUN FINDING (a prior design critic caught this; it is folded into the freeze conditions): the
between-relation mean troponymy-depths are NEAR-DEGENERATE on verbs — hypernymy 2.47, synonymy 2.31,
troponymy 2.24, entailment 2.24, antonymy 1.56 (four within 0.23; antonymy the lone shallow outlier),
and antonymy's shallow depth is CONFOUNDED with its high contrastive-frame cue-strength (its frames ARE
antonym frames). So on verbs a DEPTH-FAILS is pre-registered UNDER-POWERED/uninformative, NOT a clean
falsifier; a DEPTH-OUT-PREDICTS stays informative. H1 (the headline decoupling) is unaffected and stands
on its own. "Decisive" means "the registered next/third-point test," not a crucial experiment that
ISOLATES hierarchy (verbs confound POS with hierarchy as nouns do; DECOUPLING-BREAKS is the clean
falsifier, a positive is confirmatory third-point evidence).

ANTI-CHEAT context: the fresh disjoint cue sets (POS-agnostic-surface-disjoint from 1,740 prior cue
lemmas), the outlier cap, k, the relation inventory (incl. the mechanical cause-inclusion rule + a
thin-relation fallback for CORE relations), the depth-proxy spec, the rho_cue bands, the rho_depth
margin, and the calibration floor are ALL frozen in PREREG before ANY model call; the G2/co-occurrence
computation is byte-frozen from the noun run (only cue POS -> verbs, candidate pool -> verbs). H1-break,
H2-lose, and the nulls are pre-named first-class outcomes.

VOTE: For EACH gate say ADOPT-<letter> (or KEEP-OPEN + what's missing). Then judge: (1) is this a FAIR,
non-question-begging test where DECOUPLING-REAPPEARS / DECOUPLING-BREAKS / DEPTH-OUT-PREDICTS /
DEPTH-FAILS / null are all genuinely reachable? (2) Given the near-degenerate depth spread, is treating
DEPTH-FAILS as under-powered (not a falsifier) the honest call, or does it over-protect H2? Reply with
per-gate letters first, then <=6 terse bullets."""

r = call(PANEL["B"], PREAMBLE, DECISION, temperature=0, max_tokens=900)
print(r["content"])
b = billed_cost([[r]])
print("\n--- billed:", b, "err:", r.get("error"))
with open("vote-ratify.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${b[0]:.6f}; model {PANEL['B']}; s199 ratification vote]\n")
