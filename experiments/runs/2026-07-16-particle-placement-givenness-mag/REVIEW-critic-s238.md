# Pre-run gate — particle-placement-givenness MAGNITUDE arm (s238)

Two independent pre-run gates on the frozen firewall-only magnitude run + pooled analysis (no new
decision; a within-design powered re-run under the ratified s225 design). The **fresh-agent critic holds
GO/NO-GO authority**; the non-Anthropic decorrelation vote is QA input to weigh (PROTOCOL §2).

## Fresh-agent adversarial critic (verdict authority) → **GO**

A fresh agent that authored none of this run reproduced every check from the frozen files:

1. **Frozen-instrument fidelity — PASS.** `probe.py` byte-identical across v1/rep2/mag (`eb50f881…`);
   `common.py` differs from rep2 **only** in `HARD_STOP_USD 3.80 → 1.60` (a pure budget constant, in-file
   documented); `freq_control.json` byte-identical (`cd472475…`, carried only to satisfy the freeze gate —
   the firewall-only analysis never reads the Arm-1 covariate); the firewall `CTX` template-triple
   byte-identical to rep2. No measurement drift.
2. **Disjointness — PASS against v1 ∪ rep2.** Certification (D) unions both prior runs' triples+nouns
   before testing; re-running `build_items.py` reproduced sha `181461b2…` bit-for-bit with
   `shared_triples: []`, `shared_nouns: []`, 48 distinct triples / 48 distinct fresh nouns / all 38
   (verb,particle) pairs covered by the frozen `freq_control.json` + `VERB_LEMMA`.
3. **Firewall-only scope — SOUND.** The magnitude fence (j) is owed on the load-bearing, shortcut-immune
   firewall shift2. Arm 1 (definiteness) is confoundable (exactly where gpt shadows); Arm 3 (length) is
   secondary/non-gating. Dropping them is the correct inverse of the genitive-mag precedent (there the
   typical arm carried the magnitude and the replicated firewall was dropped; here the firewall carries it
   and the replicated definiteness/length arms are dropped). Nothing owed is missed.
4. **Pooled analysis — PARITY CONFIRMED, inflation fenced.** `analyze_merged.firewall_frame_shifts`
   computes shift2 identically to the frozen `analyze.py`; the critic ran it over the existing v1/rep2 raw
   and reproduced **every published prior number** (v1 +0.0400/+0.0719/+0.0177; rep2 +0.0349/+0.0568/+0.0048;
   n=40+48+48=136). The **double-gate** (gate 1 FRESH-48 standalone CI-LB>0 for claude+gemini AND gate 2
   pooled-136 CI-LB>0) makes the 88 reused direction-establishing frames unable to manufacture the
   verdict — the blind fresh-48 must clear its own interval first; fresh-48-only / prior-88-only /
   pooled-136 all reported side by side; NO-LIFT and PARTIAL branches honest and symmetric.
5. **Anti-cheat — no result-fixing path.** The givenness manipulation lives entirely in the frozen,
   byte-identical CTX template; the scored strings are byte-identical across GIVEN/NEWMENT/NEW so every
   enumerated scored-string reader yields within-frame shift = 0 (item authoring can add baseline noise but
   cannot inject a differential given→split shift); gpt cannot be dropped to rescue a 2/3 (it is the
   pre-named replicated shadow, reported either way); analysis frozen pre-call; budget clean. Judged a
   **real strengthening, not completionism** — it attaches a powered within-model size + CI to the one
   named candidate genuinely lacking a magnitude.
6. **Linguistic validity — SOUND.** All 48 are canonical separable transitive phrasal verbs, natural in
   both orders with a definite object. Two mildly-marked combos (f06 *cleared off the beaker*, f14 *locked
   up the strongbox*) and idiomatic doublets (f04 *carried off the trophy*, f25 *put out the candle*) are
   **immune from distorting shift2** — any baseline oddness is held constant across the three
   byte-identical-scored-string conditions and cancels in the within-frame GIVEN−NEWMENT difference.

**Non-blocking write-up conditions (all already mandated by PREREG; held to at the result):** report the
FRESH-48-only interval as prominently as the pooled; if MAGNITUDE-ATTACHED, label the size **within-model**
(anchor scope stays direction-only); if gpt's pooled firewall unexpectedly clears CI-LB>0, disclose it as
first-class, not folded into the 2/3 headline. **VERDICT: GO.**

## Non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.002630, `VOTE-critic-s238.json`) → **NO-GO** (weighed, over-ruled on the merits)

The vote dissented NO-GO on three framing grounds: (1) the pooled 136-frame CI reuses 88
direction-establishing frames → misleadingly tight *if* the headline attaches the pooled CI as the
magnitude; (2) dropping Arms 1 & 3 "narrows the estimand to the easiest surviving leg" (selective-
magnification risk); (3) gpt's non-gated behavior must be a separate stability/result class, not an
afterthought. Bottom line: *"acceptable as a descriptive update only if the pooled estimate is clearly
labeled as a partially reused, post-directional-scope magnitude and not used as the primary attached
effect size."*

Per PROTOCOL §2 the vote is signal to weigh, not a tiebreak. The fresh-agent critic (authority) weighed it
and **over-ruled it on the merits**, and the frozen PREREG already embeds its substantive asks:

- **On (1):** the PREREG's PRIMARY gate is the **FRESH-48 standalone blind arm** (gate 1) — the pooled is
  reported as "attached" only if the blind fresh arm independently clears CI-LB>0 first, and the pooled is
  explicitly labeled *"a conditional update … tighter by construction because 88/136 reused,"* with
  fresh-48-only and prior-88-only shown alongside. This is the genitive-s222-mag discipline verbatim. The
  vote's "don't use pooled as the primary attached effect size" is honored by leading with the fresh-48
  blind magnitude.
- **On (2):** the premise is **inverted** — the firewall is the *hardest, smallest, load-bearing* leg
  (claude/gemini +0.04/+0.06; gpt fails it), not the easiest. Firewall-only yields the **most
  conservative** estimand, the opposite of selective magnification; the confoundable definiteness arm
  (+0.10, where gpt also "shifts") would give a *larger* number, and it is deliberately **not** the
  reported magnitude.
- **On (3):** granted and already in the PREREG — gpt is reported as a first-class displayed SHADOW and any
  pooled-N lift is a first-class disclosure, never folded into the 2/3 headline.

The divergence is **recorded as a genuine minority position on presentation discipline**, weighed, and
answered — not smoothed over. It sharpens the write-up rules; it does not block the run.

## Outcome

**GO.** Proceed to `probe.py liveness` → `probe.py full` (blind; all 3 models before `analyze_merged.py`),
then an independent post-run verifier.
