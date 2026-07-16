# PREREG — verb-particle placement object-givenness, POWERED MAGNITUDE (MAG), program A5 / A2a

**Frozen 2026-07-16 (session 238), before any finding-bearing model call.** The powered magnitude re-run
that attaches a **within-model magnitude + bootstrap interval** to the promoted, standing `claim`
[`claim/particle-placement-givenness`](../../../wiki/findings/claims/particle-placement-givenness.md)
(`status: supported`, s229), which is scoped **DIRECTION-ONLY** with **no magnitude** — its fence (j):
*"No powered/pooled magnitude arm was run … A magnitude would be a future powered arm."* Unlike the
genitive (fence (i) magnitude ATTACHED s222) and the dative (magnitude attached s175), the particle claim
carries no size for its load-bearing, shortcut-immune referential effect. This run attaches it by adding a
**third disjoint FIREWALL arm** and **POOLING** the three firewall runs (the A2a-merged pattern that
attached the genitive's magnitude, s222 N=108, and the dative's, s175 N=100).

**Why now (economics).** The s237 instrument-line-continuation review
([`note/blimp-swap-line-continuation-review-v1`](../../../wiki/findings/notes/blimp-swap-line-continuation-review-v1.md))
ranked *"a powered magnitude re-run on an already-promoted direction-only claim"* the **#1 marginal
dollar** — *"a real strengthening, not a bar-placement tweak"* — explicitly **contrasted against** the
completionism it rejected (the verb-swap arm). Of the named candidates the particle is the only one
genuinely lacking a magnitude (genitive/dative both attached), so the #1 recommendation lands here.

**No new decision is opened.** A within-design powered re-run under the ratified, resolved design
[`decisions/resolved/particle-placement-anchor-and-indicator`](../../../wiki/decisions/resolved/particle-placement-anchor-and-indicator.md)
(s225, ADOPT-WITH-MODIFICATION Q1-A / Q2-i / Q3 human-anchored on direction). Re-uses the byte-frozen
**measurement** instrument on new disjoint items with a **new pooled analysis** (the dative-s175 /
genitive-mag-s222 pattern), carrying a fresh-agent pre-run critic + one non-Anthropic decorrelation vote,
but no new cross-session ratification.

Conjecture: [`conjecture/particle-placement-givenness`](../../../wiki/findings/conjectures/particle-placement-givenness.md).
Human anchor: [`resource/particle-placement-givenness-human-anchor`](../../../wiki/base/resources/particle-placement-givenness-human-anchor.md)
(Kim, Lee & Lee 2016, PACLIC 30, CC BY 4.0) — **direction only** (given object → split order). The anchor
licenses the *direction*; the *magnitude* this run reports is an **internal within-model** quantity
(Kim/Gries give no comparable model-scale effect size), reported as a within-model contrast, **not** a
human-comparison of sizes.

## Frozen artifacts (sha256 — `probe.py full` refuses unless both appear here)

- `stimuli.json`     : `181461b2fa0616afe1840a0fce753d9d7ddd22757b8f41fbcfc482f7e01c9264`
- `freq_control.json`: `cd472475cfae6f03862cd12ffc9421cd085d8abca831e2cccf1edd7a42da20d7`

`stimuli.json` built + certified by `build_items.py` (**CERTIFICATION PASS**; report in
`certification.json`). `freq_control.json` = the **rep2** covariate, kept **byte-identical** purely to
satisfy `probe.py`'s freeze gate — the firewall-only magnitude analysis (`analyze_merged.py`) does **not**
use the Arm-1 definiteness covariate.

## What is byte-frozen from v1/rep2, and the documented difference

- **Byte-identical (sha-verified):** `probe.py` (`eb50f881…`), `freq_control.json` (`cd472475…`). The
  indicator, the prompt (`common.SYS_*` / `USER_*`), the parser, the graded-forced-choice, the resampling
  unit (the frame), and the firewall context template-triple (`build_items.CTX`, re-used byte-identical)
  are all unchanged.
- **`common.py`:** identical **except** the pure-budget constant `HARD_STOP_USD` 3.80 → **1.60**
  (documented in-file), because this arm is **firewall-only** (48 frames × 6 firewall trials × 3 models =
  864 calls, ~$1.32 vs rep2's ~$3.1). It never touches measurement or the frozen stimuli sha.
- **`build_items.py`:** builds the **fresh, disjoint, FIREWALL-ONLY** item set (48 frames). Arms 1
  (definiteness) & 3 (length) are **dropped** — the magnitude the claim owes is the firewall `shift2`, and
  the definiteness direction + firewall survival already replicated 2/2 runs (the genitive-MAG typical-only
  analog: there the typical arm carried the magnitude and the nonce firewall was dropped; here the firewall
  carries the magnitude and the definiteness/length arms are dropped).
- **`analyze_merged.py`:** the **NEW pre-registered pooling analysis** (below), frozen here before any
  model call. The frozen `analyze.py` computes a single-run verdict; this run's finding is a **pooled
  magnitude**, so the analysis is new.

## The item set (build_items.py — certification PASS)

A **fresh, FIREWALL-ONLY arm of 48 frames**. Every (verb, particle, noun) triple and every object noun is
**DISJOINT from BOTH v1 AND rep2** (48 fresh nouns, 0 overlap with the 88 prior triples / 86 prior nouns;
certification check (D), extended to v1 ∪ rep2). Every (verb, particle) pair is drawn from the frozen
38-pair set so the byte-frozen `VERB_LEMMA` + `freq_control.json` cover every frame (D3). The firewall
context template-triple is re-used byte-identical from v1/rep2 (certified parallel: 2 clauses, 1 comma,
declarative, 14 words each, object noun 1/1/0 in given/newment/new, no verb-particle / heavy-NP leak). The
scored strings are held **byte-identical** (`the {noun}`) across given/newment/new, so **every enumerated
scored-string shortcut reader yields within-frame firewall shift exactly 0** (certification check (2)).

## Pre-registered analysis (analyze_merged.py — frozen here, before any model call)

Resampling unit = the FRAME, keyed by (run, frame_id) so the three runs pool as mutually-disjoint units.
Per model, the within-frame firewall shift `shift2(frame) = mean(split-pref|GIVEN) − mean(split-pref|NEW-MENTIONED)`
(the byte-frozen decisive Option-A leg), pooled across the three **disjoint** firewall arms:

    v1 (40) + rep2 (48) + mag (48 fresh-blind) = 136 pooled firewall frames.

**PRIMARY (headline) — pooled magnitude.** Per model: the pooled-frame **mean shift2** = the within-model
magnitude, with a nonparametric bootstrap **95% CI over the 136 frames** (seed 20260716, n=10000) + a
one-sided sign test.

**REPORTED ALONGSIDE (honesty; the genitive-MAG discipline):** the **FRESH-48-only** estimate (the
magnitude on the never-seen mag items alone — the blind check) and the **PRIOR-88-only** estimate
(v1 + rep2), so the reader sees that the pooled interval reuses prior data and can read the fresh-only
magnitude on its own.

## Pre-registered readout (symmetric — a null/weak result is first-class)

The claim is scoped **2/3**: the firewall positive covers **claude + gemini**; **gpt is a persistent,
replicated SHADOW** (its determiner effect never survives the firewall — fences a/b). So the magnitude
attaches to **claude + gemini**, and **gpt is a displayed SHADOW, never averaged and NOT gated**.

- **MAGNITUDE ATTACHED** iff **(gate 1, standalone blind)** the FRESH-48 mag arm clears **CI-LB > 0 for
  BOTH claude and gemini** — the same bar each prior firewall arm cleared for the two confirming models —
  **AND (gate 2, pooled)** the POOLED-136 CI-LB > 0 for **both claude and gemini**. Then the magnitude the
  claim carries = the per-model **pooled** point shift2 + intervals for claude+gemini, reported as a
  **conditional update**, with the fresh-48-only and prior-88-only estimates shown alongside. This lifts
  claim **fence (j)** from magnitude-absent → **magnitude-attached (within-model)**; the human-anchor scope
  stays **direction-only**.
- **PARTIAL / PROVISIONAL** if the pooled-136 CI-LB > 0 for both claude+gemini but the FRESH-48 blind arm
  is positive yet does **not** clear its own CI-LB for both (48 frames underpowered for a tight fresh
  interval): report the pooled magnitude as **provisional**, the fresh arm shown, fence (j) softened but
  **not** fully discharged — a larger fully-fresh arm still owed.
- **NO-LIFT** if the FRESH-48 arm **reverses** or is non-positive for either of claude/gemini, or the
  pooled CI-LB ≤ 0 for either — the claim stays direction-only-no-magnitude and the note records why.
- **gpt is NOT part of any gate; its estimate is reported.** If gpt's pooled firewall **unexpectedly**
  clears CI-LB > 0 (the SHADOW lifting at pooled N), that is a **first-class disclosure** — reported, not
  folded into the 2/3 headline without a fresh cross-session look.

The **direction** + firewall-survival are **not** re-adjudicated here (a promoted claim); this run
estimates the **size** and decides, on the fresh blind arm's standalone behaviour first, whether to attach.

## Budget

Pre-flight ~**$1.32** billed (864 calls; claude ~$0.71, gemini ~$0.50, gpt ~$0.11, at v1/rep2 observed
per-call prices). UTC 2026-07-16 spend before this run **$1.315553** (s235 $1.311600 + s237 $0.003953) →
projected **~$2.64 of $5.00**; under the $2.50 single-run prudence flag per model and well under the $5/day
cap. `HARD_STOP_USD = 1.60`. Plus one non-Anthropic decorrelation vote (~$0.004).
