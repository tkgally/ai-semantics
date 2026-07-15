"""s232 — one NON-ANTHROPIC decorrelation vote on the FREEZE of the BLiMP R1 C4-matched swap arm (does the
frozen recipe correctly + BLINDLY implement the ratified Q1-A/Q2-A/Q3-A gates and honor B1-B4 + S5-S8?).
PROTOCOL §A3/§2: QA input to the fresh-agent freeze critic (verdict authority). panel.B (gpt-5.4-mini)."""
import json, os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lib")))
from openrouter import PANEL, call, billed_cost

PREAMBLE = (
    "Today is 2026-07-15. You may encounter references to papers, datasets, or models that postdate "
    "your training cutoff. Treat post-cutoff recency as neutral: a paper you do not recognize is not "
    "for that reason fabricated. Where you must rely on what you know, label it as such."
)
SYSTEM = (
    PREAMBLE + "\n\nYou are an independent, adversarial PRE-RUN FREEZE critic for an autonomous research "
    "project on LLM meaning. The value-laden gates are already ratified; your job is narrower: does the "
    "FROZEN recipe implement them BLINDLY and correctly, with every load-bearing number pinned before any "
    "model call, no residual analyst discretion, and no promotion-seeking retune? Vote GO / "
    "GO-WITH-CONDITIONS / NO-GO on freezing + (later) running. Be concrete. Reply in compact structured prose."
)
USER = r"""
FREEZE under review: a C4-FREQUENCY-MATCHED BLiMP content-word-swap arm, ratified this session
ADOPT-WITH-MODIFICATION (Q1-A DUAL-BAND / Q2-A / Q3-A) subject to four BLOCKERs + four SHOULD-FIX. The run is
DEFERRED (budget); this vote is on whether the FROZEN recipe is sound to run as-is.

Context. A prior swap arm (replace BLiMP content words with novel SUBTLEX-frequency-matched same-POS words on
6 frame-safe paradigms, 3 shallow + 3 deep) dropped DEEP-stratum 2AFC accuracy 3/3 (Δ̄acc −0.095/−0.057/−0.072,
CIs excl 0) BUT the swap set was +0.204 log-units rarer in a C4 pretraining proxy, so the drop is confounded
(memorization vs pretraining-rarity). This successor matches the swaps on C4 frequency TOO (dual-band), re-runs,
and reads a SYMMETRIC four-outcome map. It is designed KNOWING the prior deep-drop magnitudes.

The FROZEN recipe (pinned constants, all decided before any model call, blind to accuracies):
- Q1-A dual-band: substitute in-band on BOTH SUBTLEX Lg10WF (±0.10) AND C4 log-freq (±0.30) of the original
  FORM; eligible = the intersection; selection seeded-deterministic by per-position ITEM-HASH (no free seed).
- B1: C4 half-width fixed at 0.30 (single value, not floating); POOL_FLOOR=5 (a position with <5 in-both-band
  candidates is DROPPED-AND-LOGGED, never band-widened); TRIGGER_FRAC=0.25 (if >25% of eligible positions are
  dropped for below-floor intersection, the WHOLE build re-runs under Q1-B C4-primary) — a frequency-only,
  accuracy-blind switch computed at build time.
- B2 (anti-seed-shopping): the ONLY seed is 20260715 (date-derived, pre-announced), used only to draw the
  disjoint subsample; substitute selection is seed-FREE (per-position sha256 of uid|pid|i), so there is no
  output-selecting seed to scan; PREREG forbids seed scanning; the run verifier attests the seed reproduces
  the committed lexicon.
- B3 (adequacy): EXACT |signed set-mean C4 gap| ≤ 0.05 (computed pre-model-call at the pinned 22.3M-sentence
  stream scale); above ⇒ STILL-INCONCLUSIVE-BY-MATCH-FAILURE, no DROPS/STABLE read.
- B4 (blind-scoring lock): scoring code + exclusions + the four-outcome table frozen before any re-run; the
  run verifier attests no human-readable intermediate output inspected until the whole batch is scored.
- S5: single pinned C4 stream scale = 22.3M sentences (3 shards), band + adequacy report at the same scale.
- S6: per-word C4 gap report + a soft directional-cancellation flag (a small set-mean hiding large both-sign
  per-word gaps is made visible).
- S7: SAMPLE_N 130→160 headroom; USABLE_FLOOR=60/paradigm; a below-floor DEEP paradigm dropped; ≥2 deep →
  deep-2 re-verdict; <2 deep → ATTRITION-INCONCLUSIVE.
- Q2-A: 6 s210 paradigms both strata; sample DISJOINT from the s210 sample BY CONSTRUCTION (drawn from pairs
  MINUS the s210 kept ids, certified 0 overlap at freeze); ORIGINAL re-run fresh (no known-accuracy exposure).
- Q3-A four-outcome map, ±0.05 bands identical for DEEP-STILL-DROPS (refuse) and DEEP-SWAP-STABLE (bounded
  cross-session candidacy). Instrument (elicitation, 6 paradigms, substitution recipe, ±0.05 bands) inherited
  BYTE-IDENTICAL from the prior arm; the 8 morphology/detok/locus helpers verified byte-identical.
- The C4-matched swap-build is independently reproduced by a fresh-agent verifier from the recipe BEFORE any
  item is scored (G5-plus). Cost of the deferred run ~$1.3-1.6 (7,200 calls) from OBSERVED prior economics.

Give, concisely:
1. Overall: GO / GO-WITH-CONDITIONS / NO-GO on freezing + running this recipe as-is.
2. Is the dual-band + pool-floor + trigger switch genuinely BLIND and free of post-hoc discretion? Any residual
   knob a determined analyst could still turn after seeing the C4 counts (which are accuracy-blind)?
3. Is |signed set-mean C4 gap| ≤ 0.05 the RIGHT adequacy criterion, or does the per-word directional-
   cancellation flag (S6) need to be a HARD gate rather than a reported flag?
4. Given the known prior drop, is seed-pinning + seed-free substitute selection + verifier-reproduced build +
   blind-scoring lock enough, or is a further guard needed? One paragraph.
5. Any place the frozen recipe looks aimed at a desired result, or "none".
"""
def main():
    r = call(PANEL["B"], SYSTEM, USER, max_tokens=1600)
    cost, n, n_missing = billed_cost([[r]])
    out = {"model": PANEL["B"], "usage": r.get("usage"), "billed_cost": cost, "n": n,
           "n_missing": n_missing, "error": r.get("error"), "content": r.get("content")}
    with open(os.path.join(os.path.dirname(__file__), "VOTE-freeze-s232.json"), "w") as f:
        json.dump(out, f, indent=2)
    print("=== NON-ANTHROPIC FREEZE VOTE (panel.B =", PANEL["B"], ") ===")
    print("billed_cost: $%.6f (n=%d, missing=%d)" % (cost or 0, n, n_missing))
    print("error:", r.get("error")); print("---"); print(r.get("content"))

if __name__ == "__main__":
    main()
