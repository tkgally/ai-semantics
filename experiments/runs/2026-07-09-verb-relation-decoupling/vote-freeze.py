#!/usr/bin/env python3
"""Non-Anthropic decorrelation vote on the s199 FREEZE of the verb-relation decoupling probe
(PROTOCOL §A3). One FRESH vote through the non-Anthropic slot via the probe REST path — QA input to
the fresh-agent freeze critic's GO/NO-GO, NOT authoritative. Cutoff-aware preamble. This reviews the
FROZEN artifacts (built before any model call), not the gates (already ratified s199)."""
import sys, os
sys.path.insert(0, os.path.abspath("../../lib"))
from openrouter import PANEL, call, billed_cost

PREAMBLE = ("Today is 2026-07-09. You are a methodology reviewer. Your training cutoff may predate this "
            "project; treat post-cutoff papers/datasets/models as neutral. Be adversarial and terse. "
            "This is a FREEZE check: the gates are already ratified; you judge whether the frozen "
            "artifacts honor the anti-cheat fence and whether it is safe to spend ~$0.40 on the run.")

FREEZE = """A verb-relation lexical-recovery probe is FROZEN (nothing run yet). Internal-contrast, no
human comparison. It tests, over WordNet VERB relations, whether relation-recovery rank DECOUPLES from
contrastive-frame co-occurrence cue-strength (H1) as it does for nouns, and whether a pre-registered
troponymy-depth proxy out-predicts cue-strength (H2). Everything below was computed BEFORE any model call.

FROZEN FACTS (from prep.py / build_cooc_c4.py, seed 20260709):
- 6 relations, FRESH cues POS-agnostic-disjoint from 1,740 prior cue lemmas (asserted 0 overlap):
  antonymy N=130, synonymy 130, hypernymy 130, troponymy 130, entailment 130, cause 126 (776 cues).
- `cause` INCLUDED as a 6th by a mechanical rule frozen BEFORE inspection: achieved matched-N 126 >= 100.
- Frequency band Lg10WF [2.0,4.5], all relations matched to antonymy's fresh per-bin profile.
- Contrastive-frame G2 control on C4 (22,329,495 sentences — byte-identical volume to the noun run),
  signed_g2 + compute_control asserted BYTE-IDENTICAL to the frozen noun-run build (only cue POS ->
  verbs, candidate pool -> verbs). The corpus Hearst arm is DROPPED (no clean verb troponymy frame).

FROZEN PREDICTORS (pre-recovery; corpus + WordNet only):
- cue-strength (frame-G2): antonymy 0.0923, troponymy 0.0487, synonymy 0.0308, hypernymy 0.0207,
  cause 0.0106, entailment 0.0051.
- troponymy-depth (min_depth of cue's first verb synset; predicted NEGATIVE): antonymy 1.577,
  cause 1.690, entailment 2.154, hypernymy 2.192, synonymy 2.208, troponymy 2.431.
- NOTE: antonymy is BOTH highest cue-strength AND shallowest depth (its frames ARE antonym frames) ->
  ρ_cue-positive and ρ_depth-negative are ALIGNED via antonymy (reverse of the noun case).

FROZEN B1 NUMERIC DEGENERACY BOUND (the ratifier's binding condition, decided BEFORE any model call):
- Bound: DEGEN_MAX_RANGE = 0.50 on the NON-antonymy CORE-4 mean-depth range {synonymy, hypernymy,
  troponymy, entailment} (the fixed backbone, independent of the mechanical cause decision).
- Achieved on the frozen sample: CORE-4 range = 0.277 (troponymy 2.431 - entailment 2.154) < 0.50
  => DEPTH SPREAD FROZEN "DEGENERATE" => H2 under-powered SYMMETRICALLY: a DEPTH-FAILS is
  non-falsifying, AND a DEPTH-OUT-PREDICTS is flagged under-powered / not noun-equivalent.
- (Transparency: cause-inclusive non-antonymy range is 0.741 and full-set SD 0.304, recorded but NOT
  driving the verdict; the wider spread rides on cause + antonymy.)

FROZEN VERDICT MAP: H1 exhaustive bands ρ_cue <= +0.30 REAPPEARS / (+0.30,+0.50] INCONCLUSIVE /
> +0.50 BREAKS, >=2/3 models. H2 depth wins iff |ρ_depth|-|ρ_cue| >= 0.20 AND ρ_depth negative, >=2/3;
then the B1/B2 under-power gate applies. All frozen in PREREG before any model call. Cost est ~$0.40,
ABORT_USD 1.50.

JUDGE (terse): (1) GO or NO-GO for spending ~$0.40 on the run? (2) Is the B1 bound honest — i.e. was
0.50-on-CORE-4 a defensible pre-commitment, or does defining degeneracy on CORE-4 (excluding the
mechanically-included shallow `cause`) look like gaming in EITHER direction? (3) Any anti-cheat leak: a
threshold that could be tuned post-hoc, a relation silently dropped, the byte-freeze claim, the fresh-cue
disjointness? (4) Anything that would make you STOP the run. Reply GO/NO-GO first, then <=6 bullets."""

r = call(PANEL["B"], PREAMBLE, FREEZE, temperature=0, max_tokens=900)
print(r["content"])
b = billed_cost([[r]])
print("\n--- billed:", b, "err:", r.get("error"))
with open("vote-freeze.txt", "w") as f:
    f.write(r["content"] + f"\n\n[billed ${b[0]:.6f}; model {PANEL['B']}; s199 freeze vote]\n")
