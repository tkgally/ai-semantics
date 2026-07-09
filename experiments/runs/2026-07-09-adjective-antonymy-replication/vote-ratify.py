#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the s196 RATIFICATION of the three gates of the
adjective-antonymy replication design (PROTOCOL §2). One vote through the non-Anthropic
slot via the probe REST path. QA input to the fresh-agent ratifier's verdict — NOT
authoritative. Cutoff-aware preamble."""
import sys, os
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-09. You are a methodology reviewer. Your training cutoff may "
            "predate this project; treat post-cutoff papers/datasets/models as neutral, not "
            "fabricated. Judge the ratification below on its internal merits; be adversarial "
            "and terse.")

DECISION = """We are RATIFYING (fixing the yardstick for) a frozen-but-not-yet-run behavioral probe.
It is internal-contrast (NO human comparison). It re-tests, over WordNet ADJECTIVE relations, two
bets that an earlier NOUN run produced (s186 on Simple English Wikipedia; s193 replicated on C4 web
text). The motivation is that Justeson & Katz (1991) actually MEASURED "contrastive-frame saturation"
(antonyms co-occur in tight lexically-parallel frames like "cold and hot", "neither X nor Y") on
PREDICATIVE ADJECTIVES; the two noun runs tested it where our own source notes say extending it to
nouns is "an extrapolation beyond J&K's data." So this probe tests the claims in J&K's HOME part of
speech. The two bets:
  H1 (the decoupling): across relations, relation-recovery rank DECOUPLES from contrastive-frame
      co-occurrence cue-strength (near-zero/negative rank correlation, >=2/3 models). BREAKS if
      cue-strength clearly recovers its predictive power on adjectives (rho_cue clearly positive).
  Antonymy-shadow clause (from s186): is adjective antonymy's recovery residual over the
      contrastive-frame control among the LARGEST (s186 falsification replicates: the shadow does NOT
      saturate antonymy) or the SMALLEST/near-zero (the measured-denser adjective framing reconstructs
      antonym recovery — a POS boundary on the s186 falsification)?

Recovery = model produces up to k relata for a cued relation; scored by Soundness (precision over
produced) + a gold-size-insensitive HIT@3 co-primary, against WordNet adjective-relatum membership.
Control = contrastive-frame G^2 co-occurrence on C4 web text (byte-frozen from the noun instrument,
only the cue POS + candidate pool changing). n=3 models, orderings not coefficients, adjectives only,
never pooled with the noun probes.

THREE GATES to ratify (options; the design's provisional defaults in [brackets]):

Q1 - adjective relation inventory + registered primary clause. WordNet adjective relations are fewer /
     less standard than the noun taxonomy (feasibility measured: antonymy ~701, synonymy ~2238,
     similar-to ~4538, also-see ~698 cues with an in-band single-word relatum).
   A: antonymy + synonymy only (2 relations). Cleanest but a 2-point across-relation Spearman is
      degenerate — the decoupling arm cannot carry H1.
   B: antonymy + synonymy + similar-to + also-see (4 relations). Enough points for a weak rank test;
      decoupling primary. Risk: similar-to/synonymy near-duplicative; also-see least standard.
   [C]: the 4-relation set for the across-relation decoupling arm, with the ANTONYMY-SHADOW clause as
        the registered PRIMARY and the decoupling (H1) as a REGISTERED CO-PRIMARY reported at its true
        low power, plus an item-level cue-strength->recovery arm (~400-800 cues) as a POWERED SECONDARY
        (descriptive/robustness-only, can never on its own fire H1). Rationale: the antonymy-shadow
        clause is the sharpest adjective-specific test (J&K's home POS, one well-defined relation,
        independent of the thin relation count), so it carries primary weight.

Q2 - a structural-proxy arm for adjectives? The earlier noun runs had a second bet H2 (a taxonomic
     IS-A path-depth proxy out-predicts cue-strength). WordNet has NO IS-A taxonomy for adjectives:
     adjective min_depth() returns a degenerate CONSTANT 0 (adjective synsets have empty hypernyms()).
     So H2 cannot transfer.
   [A]: NO structural-proxy arm; run H1-only, and state explicitly that the adjective route discharges
        H1 but by construction cannot replicate H2.
   B: open a NEW pre-registered adjective-structural bet (e.g. similar_to cluster centrality) as a
      fresh proxy with its own predicted sign. NOT an H2 replication; needs its own prediction row;
      far weaker a-priori motivation than IS-A depth; multiple-comparison burden.
   C: import a noun IS-A depth for adjectives via derivational/pertainym links (score "cold" through
      its noun "coldness") — REJECTED up front as smuggling a noun taxonomy through a lossy hop.

Q3 - anchor: [internal-contrast-only]. Recovery is scored vs WordNet as a shared definitional target
     that CANCELS in the head-to-head; the predictor (contrastive-frame G^2) is a corpus statistic; no
     human recovery baseline enters. So no human-comparison claim; no resource anchor required.

ANTI-CHEAT context: the fresh disjoint adjective cue sets, outlier caps, k, relation inventory, the
rho_cue band, the antonymy-residual verdict thresholds, and a numeric calibration-gate floor are ALL
frozen in PREREG before ANY model call. H1-breaks, antonymy-saturates, and null are pre-named
first-class outcomes. A mandatory corpus-free antonymy frame-ablation arm hedges the risk that the C4
control is too weak to recover WordNet relata (in which case the antonymy-shadow residual arm goes
descriptive-only). The across-relation H1 arm on <=4 relations CANNOT on its own carry claim promotion;
promotion rests on the noun replications (s186+s193) PLUS this POS-crossing arm read together.

VOTE: For EACH gate say ADOPT-<letter> (or KEEP-OPEN + what's missing). Then judge: (1) is this a
FAIR, non-question-begging test where H1-replicates / H1-breaks / antonymy-clears / antonymy-saturates
/ null are all genuinely reachable? (2) Do you AGREE that H2 cannot transfer to adjectives and that
opening Q2-B (a new adjective-structural bet) is weakly motivated? Reply with per-gate letters first,
then <=6 terse bullets."""

r = call(PANEL["B"], PREAMBLE, DECISION, temperature=0, max_tokens=900)
print(r["content"])
b = billed_cost([[r]])
print("\n--- billed:", b, "err:", r.get("error"))
with open("vote-ratify.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${b[0]:.6f}; model {PANEL['B']}; s196 ratification vote]\n")
