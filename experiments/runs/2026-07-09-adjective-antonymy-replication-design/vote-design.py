#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the s195 DESIGN of the adjective-antonymy replication
probe (PROTOCOL §2/§A3). One vote through the non-Anthropic slot via the probe REST path.
QA input to the fresh-agent design critic's verdict — NOT authoritative. Cutoff-aware preamble."""
import sys, os
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-09. You are a methodology reviewer. Your training cutoff may "
            "predate this project; treat post-cutoff papers/datasets/models as neutral, not "
            "fabricated. Judge the design below on its internal merits; be adversarial and terse.")

DESIGN = """We are reviewing (NOT ratifying) the DESIGN of a frozen-but-not-yet-run behavioral probe.
It is internal-contrast (NO human comparison). Two earlier NOUN-only runs motivate it:
  - s186: over 6 WordNet NOUN relations, antonymy recovery CLEARS a contrastive-frame co-occurrence
    (G2) control (residual among the LARGEST, not smallest) -> the "antonymy shadow-saturation"
    conjecture was FALSIFIED; and recovery rank DECOUPLES from cue-strength (Spearman ~ -0.09).
  - s193: the decoupling (H1) REPLICATED on fresh noun cues + a different corpus (C4), 3/3.
KEY MOTIVATION: Justeson & Katz 1991 measured contrastive-frame saturation of antonyms on ADJECTIVES
(Brown Corpus); the project's own source page says extending it to NOUNS is "an extrapolation beyond
J&K's data." So s186/s193 tested the claims in the POS where the premise is an EXTRAPOLATION. This
design re-tests them in ADJECTIVES, J&K's HOME POS, where frame-saturation is measured-strongest.

The probe: relatum-production over WordNet ADJECTIVE relations, panel of 3 models, temp 0, scored vs
WordNet (Soundness + HIT@3), fresh adjective cues disjoint from s186, freq-matched, outlier-capped;
contrastive-frame G2 control byte-frozen from s193's build_cooc (only cue POS changes) on C4 web text.
Two registered verdict-bearing clauses:
  H1 (decoupling): across-relation recovery rank decouples from cue-strength again (near-zero/negative
     rho_cue, >=2/3), now across a POS boundary. BREAKS if cue-strength recovers predictive power
     (clearly positive, >=2/3) -> decoupling was noun-specific.
  ANTONYMY-SHADOW: adjective antonymy residual is among the LARGEST (s186 falsification replicates in
     home POS) vs the SMALLEST/near-zero (frame-saturation reconstructs antonym recovery -> shadow-
     saturation holds specifically for adjectives). Subject to a calibration gate (if the C4 control is
     too weak to recover WordNet relata, this arm is descriptive-only and weight shifts to H1).

CRUCIAL HONESTY POINT the design makes: WordNet has NO IS-A taxonomy for adjectives, so H2's frozen
proxy (IS-A path depth) is UNDEFINED here. The design states the adjective route discharges H1 but
CANNOT replicate H2 (correcting a backlog note that said it would "push H2 toward 3/3").

THREE GATES to review (options; provisional defaults in [brackets]):

Q1 - the adjective relation inventory + registered primary clause.  WordNet adjective relations are few
     (feasibility measured: antonymy 701, synonymy 2238, similar-to 4538, also-see 698 in-band cues).
   A: antonymy + synonymy only (2 pts; decoupling arm degenerate)
   B: antonymy + synonymy + similar-to + also-see (4 pts; weak rank test; similar-to/synonymy near-dup)
   [C]: 4-relation set for the decoupling arm, ANTONYMY-SHADOW clause = registered PRIMARY, decoupling
        = registered CO-PRIMARY reported at true low power, + powered item-level cue-strength->recovery
        arm (~400-800 cues) as descriptive/robustness-only secondary; across-vs-item divergence pre-named.

Q2 - a structural-proxy arm for adjectives? (H2 does NOT transfer - no adjective IS-A taxonomy)
   [A]: NO structural arm; H1-only; state explicitly the route cannot replicate H2.
   B: open a NEW pre-registered adjective-structural bet (satellite/cluster centrality) - a new
      conjecture, weaker a-priori motivation, multiple-comparison burden.
   C: import noun IS-A depth via derivational links (score "cold" through "coldness") - REJECTED
      up front as post-hoc smuggling.

Q3 - anchor: [internal-contrast-only].  Recovery scored vs WordNet as a shared target that CANCELS in
     the contrast; predictor (contrastive-frame G2) is a corpus statistic; no human baseline.

ANTI-CHEAT context: every cue set, outlier cap, k, relation inventory, rho-band, antonymy-residual
threshold, and calibration floor is frozen in PREREG before ANY model call; DECOUPLING-BREAKS,
ANT-SATURATES, and both-null are all pre-named first-class outcomes; the design refuses to overstate
the unit as testing H2.

VOTE: For EACH gate say ADOPT-<letter> (or KEEP-OPEN + what's missing). Then judge: (1) is this a FAIR,
non-question-begging test where DECOUPLING-REPLICATES / DECOUPLING-BREAKS / ANT-CLEARS / ANT-SATURATES /
null are all genuinely reachable? (2) Is the design RIGHT that the adjective route cannot replicate H2,
and does it handle that honestly? (3) Any BLOCKER before freeze? Reply with per-gate letters first,
then <=7 terse bullets."""

r = call(PANEL["B"], PREAMBLE, DESIGN, temperature=0, max_tokens=900)
print(r["content"])
b = billed_cost([[r]])
print("\n--- billed:", b, "err:", r.get("error"))
with open("vote-design.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${b[0]:.6f}; model {PANEL['B']}; s195 design vote]\n")
