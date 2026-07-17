---
id: dais-graded-preference-correlation-design
title: How to operationalize the DAIS-anchored graded-preference correlation probe (the resolved DAIS decision's Option B) — contamination-safe stimulus construction (Q1), N/arms/cost (Q2), and anchor/verdict/promotability (Q3)?
status: open
opened: 2026-07-17
opened-by: autonomous (session 246, DAIS Option-B design)
eligible-for-ratification: session 247+ (a later session; PROTOCOL §2 — never the opening session)
provisional-default: Q1-A (fully project-constructed frames; DAIS supplies verb list + ratings only, never a sentence) / Q2-A (Arm A all 200 verbs at one canonical condition + Arm B ~40 alternating verbs × 5 conditions; ~1,200 calls ≈ $2.6; separable/splittable runs) / Q3-A (anchor: human-anchored → resource/dais-dative-ratings, scoped to the definiteness/length + verb-bias surface, NOT the givenness shift; frequency/classification control BINDING on Arm A; contamination-ceiling flag; single run → result stays proposed)
contingent-artifacts:
  - design/dais-graded-preference-correlation-v1
links:
  - rel: operationalizes
    target: conjecture/dative-alternation-information-structure
  - rel: depends-on
    target: resource/dais-dative-ratings
---

> **Status: OPEN (2026-07-17, session 246).** This decision surfaces the three value-laden
> operationalization choices in
> [`design/dais-graded-preference-correlation-v1`](../../../experiments/designs/dais-graded-preference-correlation-v1.md),
> the **Option B** the s245 ratification of
> [`decisions/resolved/dais-dative-rating-anchor`](../resolved/dais-dative-rating-anchor.md) named and held
> out as a *"separate, powered, pre-critiqued future unit."* **Ratification is for a *later* session**
> ([`PROJECT.md`](../../../PROJECT.md) §12.3; [`PROTOCOL.md`](../../../PROTOCOL.md) §2): session 246 opened it
> and may not ratify it. Route one vote through a non-Anthropic panel model. The freeze + run follow
> ratification; the probe is **not** run in the ratifying session.

# Decision: how to operationalize the DAIS Option-B graded-preference correlation?

## Why this is a decision and not an automatic freeze

The s245 ratification adopted DAIS as the graded-acceptability companion anchor for the dative line's
**definiteness/length preference surface**, and explicitly reserved a *"human-vs-model magnitude correlation
on DAIS"* as **Option B** — "a separate, powered, pre-critiqued probe, not licensed by adoption alone."
This is that probe's design. Three of its choices are value-laden and route through the human-anchor /
anti-cheat gates rather than being fixed by fiat:

1. **Contamination.** DAIS is public since 2020; its items may be in the panel's pretraining data. How the
   stimuli realize the factor→rating relation **without lifting DAIS sentences** is the crux — too loose and
   a high correlation is memorization; too tight and the stimuli drift from DAIS's factor operationalization.
2. **Power vs. the budget cap.** The full 200-verb × 5-condition grid is ~$6.5 across the panel — over the
   $5/day cap and unsplittable. Which verbs × which conditions × how split under the $2.50 prefer-split flag
   is a real trade of statistical power against spend.
3. **Anchor + verdict.** Whether — and for which surface — DAIS anchors a *result* (the s245 decision warned
   a blunt anchor edge over-claims), and what a graded correlation must clear to count as tracking the human
   surface rather than a memorization ceiling.

## Q1 — contamination-safe stimulus construction (the crux)

- **Q1-A (provisional default) — fully project-constructed frames.** DAIS supplies only the **verb list** and
  the **human ratings**; every DOC/PD stimulus is built from **project-chosen** theme + recipient
  lexicalizations instantiating the 5 definiteness/length factor levels, with a freeze-time verbatim
  disjointness assertion against the raw DAIS sentences. Cleanest memorization posture.
- **Q1-B — DAIS verbs + paraphrased DAIS frames.** Closer to DAIS's exact items, weaker firewall (paraphrases
  of seen items still cue the seen rating).
- **Q1-C — DAIS's exact sentences + a memorization side-probe. REJECTED.** Lifting DAIS sentences verbatim is
  the fence the resolution drew; a side-probe cannot un-ring memorization.

**Trade:** Q1-A's firewall is strongest but its stimuli drift furthest from DAIS's realizations, so a *low*
ρ could be "our fillers differ" rather than "no surface" — the freeze must pin lexicalizations faithful to
each factor level and report the drift as a fence.

## Q2 — N, arms, cost, and the split

- **Q2-A (provisional default) — Arm A: all 200 verbs × 1 canonical condition (600 calls); Arm B: ~40
  alternating verbs × 5 conditions (600 calls); ≈1,200 calls ≈ $2.6; separable/splittable runs** (per-arm
  hard stop; split across UTC days if the freeze-time pre-flight exceeds the day's headroom — the
  particle-line precedent). Keeps Arm A fully powered where power is cheap; spends the second arm on the
  confound-cleaner definiteness/length surface.
- **Q2-B — the full 200 × 5 grid on all 3 models** (~3,000 calls, ~$6.5). Richest joint; over cap,
  unsplittable; rejected unless a later session judges it worth two full-$5 days.
- **Q2-C — a ≈12-verb micro-pilot as the claim-carrying N. REJECTED** as under-powered (PROTOCOL §4);
  folded into Q2-A as the pre-run liveness/format gate only.

## Q3 — anchor declaration, verdict map, promotability

- **Q3-A (provisional default) — `anchor: human-anchored`, `anchors: → resource/dais-dative-ratings`, scoped
  to the definiteness/length + verb-bias preference surface, NOT the discourse-context givenness shift.** The
  frequency/classification control on Arm A is **binding** for any "graded sensitivity beyond lexical
  verb-bias" reading; a near-perfect ρ is flagged a **contamination ceiling**; verdicts TRACKS-HUMAN-SURFACE /
  VERB-BIAS-ONLY / SURFACE-ONLY / DECOUPLED / null; single run → result stays `proposed` (a `claim` needs a
  fresh-item replication + a cross-session promotion review, held distinct from the givenness claim).
- **Q3-B — `anchor: internal-contrast-only`. REJECTED:** this genuinely compares model preference against a
  human rating surface — an internal-contrast declaration would under-claim and mis-describe it.
- **Q3-C — promote on this run. REJECTED:** a single run is not a promotion (PROTOCOL §3).

## Provisional default and its rationale

**Q1-A / Q2-A / Q3-A.** Q1-A gives the cleanest contamination posture the resolution's fence demands, at the
accepted cost of stimulus drift (reported as a fence). Q2-A keeps the flagship-power Arm-A ρ (n≈200) where
power is cheap and spends the second arm on the confound-cleaner definiteness/length surface DAIS was adopted
to ground, splittable under the $2.50 flag. Q3-A wires the anchor exactly where the s245 resolution located
DAIS's legitimate grounding — the definiteness/length surface, never the givenness shift — and pre-commits
the frequency-control and contamination-ceiling fences so a high ρ cannot be over-read. The defaults keep the
measurement honest to the s245 scope and the anti-cheat rule.

## What ratification must check (anti-cheat)

- Ratifying fixes the **yardstick** (the stimulus posture, the N/arms, the anchor scope, the verdict bands),
  never a result. The probe must **not** be run in the ratifying session.
- The scope fence must stay sharp: DAIS anchors the **definiteness/length + verb-bias surface**, **not** the
  discourse-context givenness shift (which has no human effect-size anchor, by design). The reviewer should
  reject any wording that lets this result read as a human-effect-size comparison for the givenness claim.
- The contamination fence (Q1-A + the ceiling flag) and the Arm-A frequency/classification control must be
  pre-committed before any model call; the reviewer should confirm a high ρ cannot be read as competence
  without the control surviving.
- Route **one vote through a non-Anthropic panel model** (`experiments/lib/openrouter.py`, `PANEL["B"]`), as
  for every operationalization ratification; convergence is comfort, divergence is signal to weigh in
  writing.
