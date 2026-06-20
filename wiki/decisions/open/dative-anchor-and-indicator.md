---
id: dative-anchor-and-indicator
title: How to operationalize the dative-alternation information-structure probe — which human anchor, and which logprob-free behavioral indicator?
status: open
opened: 2026-06-20
opened-by: autonomous (session opening the dative empirical line)
contingent-artifacts:
  - design/dative-information-structure-v1
  - conjecture/dative-alternation-information-structure
---

# Decision: anchor + indicator for the dative-alternation probe

## Why this exists

This session opens the empirical line for
[`conjecture/dative-alternation-information-structure`](../../findings/conjectures/dative-alternation-information-structure.md)
— a classic, much-studied English form–meaning pairing (double-object *Mary gave
John the book* vs. prepositional *Mary gave the book to John*), constrained by
information structure (given/old before new; pronominal recipients favor the
double-object form). It is the project's first probe squarely back on the charter's
**grammatical-meaning** core after a long run of composition / relational-order work.

The human anchor is now in-repo as a `resource`:
[`resource/languageR-dative-corpus`](../../base/resources/languageR-dative-corpus.md)
(Bresnan et al. 2007; `languageR::dative`; 3263 corpus observations coded for the
information-structure factors plus the NP/PP outcome). But *how* the probe is run
involves three value-laden choices that a session must not auto-take (CLAUDE.md
rule 5). They are surfaced here together because they interlock.

**This page was opened 2026-06-20 and may be ratified, at the earliest, by a later
session's independent adversarial-review pass. No probe runs before that
ratification.** The drafted design ([`experiments/runs/2026-06-20-dative-information-structure/README.md`](../../../experiments/runs/2026-06-20-dative-information-structure/README.md))
is contingent on this decision.

## The three sub-questions

### Q1 — Which human anchor?

- **Option A (corpus production surface)** — `languageR::dative`. The human signal
  is *speakers' realization choices* (NP/PP) as a function of the coded factors;
  the gradient is the Bresnan et al. logistic-regression **predicted probability**
  per factor configuration. **Verifiably fetchable and licensed** (GPL; tarball
  confirmed 2026-06-20). It grounds production *probability*, not graded per-item
  naturalness.
- **Option B (rating data)** — Bresnan & Ford (2010) gradient naturalness ratings
  (100-point split across the two variants). Directly matches the conjecture's
  *graded-acceptability* clause and is the human task a graded forced-choice
  indicator most resembles. **Fetchability / licensing / per-item availability are
  unverified**, and no body text could be extracted in the cataloguing environment;
  verbatim verification would be a precondition of adopting it.
- **Option C (both)** — corpus for the within-condition production-preference test;
  B&F ratings as a convergent gradient cross-check *if* its data clears the
  verification bar at build time. Heaviest; strongest if both anchors agree.

### Q2 — Which indicator (what the model produces)?

The conjecture as written (2026-05-28) proposed a **surprisal / continuation-likelihood**
indicator. That is **unavailable under pure autonomy**: OpenRouter exposes no
prompt/echo-logprobs on the panel models — the exact blocker that retired the AANN
surprisal instrument ([`decisions/resolved/aann-panel-logprob-blocker`](../resolved/aann-panel-logprob-blocker.md)).
So a **behavioral** indicator is required, and which one is a choice:

- **Option (i) — graded forced-choice preference** (provisional default). Given a
  controlled discourse context and the two phrasings of the same ditransitive
  proposition, the model distributes 100 points (or rates each on a fixed scale) by
  naturalness. Mirrors the B&F human task → enables like-for-like human comparison;
  yields a graded signal for the monotonicity test. Risk: the model may anchor on a
  shallow cue (length) rather than information structure — handled by the Q3
  control.
- **Option (ii) — open production / continuation.** The model continues a context
  and we code the realization it produces (NP vs PP). More naturalistic, closer to
  the corpus's own measure, but far less controllable (free generation introduces
  lexical/length variance the design cannot hold fixed) and harder to score blind.

### Q3 — Synthetic vs. corpus-derived stimuli, and the length control

- **Stimuli.** Lifting attested corpus sentences risks **training-data
  contamination** (especially WSJ). Provisional default: **synthetic minimal
  pairs** built to the corpus factor structure (the corpus anchors the *factor →
  outcome* relation, not specific items), as the held-out approach did for AANN.
- **The load-bearing control.** In the corpus, **length and givenness are
  correlated** (given/pronominal material is typically shorter). A preference shift
  the design wants to credit to *information structure* could instead be a
  *short-before-long* processing preference. The design **must dissociate length
  from givenness** (e.g. cross givenness with matched lengths, and include
  length-matched given/new minimal pairs). This is precisely where a loop could
  cheat by item selection, so the dissociation is a **binding condition**, not a
  nicety — to be certified by the pre-run critic before any spend.

## Provisional default (to be adopted, modified, or rejected next session)

- **Anchor:** Option A (corpus) as the verified primary; **queue Option B
  verification** (fetch + license + per-item availability + verbatim) and fold B&F
  ratings in as a convergent cross-check only if it clears that bar — i.e. start at
  Option A, upgrade toward Option C opportunistically.
- **Indicator:** Option (i), graded forced-choice production preference (behavioral,
  logprob-free).
- **Stimuli:** synthetic minimal pairs, **length and animacy held constant** while
  givenness / pronominality of recipient vs. theme are manipulated, with a
  length-matched given/new contrast as the anti-shortcut control; built and
  certified at the build session under an independent pre-run critic.
- **Result anchor posture:** **human-anchored** (NOT `internal-contrast-only`). The
  corpus (and, if adopted, the ratings) *is* a human resource, so this result may
  make a calibrated human-comparison claim — does the model's preference track the
  human production / acceptability gradient — unlike the composition-line results
  that were within-model contrasts. The claim stays calibrated to whichever anchor
  is adopted (production probability for A; graded acceptability for B).

## What the reviewer should weigh

1. Is the corpus (production-probability) anchor an honest match for a conjecture
   phrased around "human acceptability ratings", or does the rating-anchor clause
   make Option B/ C a precondition rather than an upgrade? (The conjecture's
   "confirm" criterion currently names "human acceptability scores".)
2. Is the graded forced-choice indicator (Option i) introducing a measure the human
   anchor does not license (the corpus has no per-item rating to regress against —
   only an aggregate probability), and if so should the within-model
   condition-shift test (which the corpus *does* license) be primary, with the
   human-gradient correlation secondary?
3. Is the length/givenness dissociation specified tightly enough to bind the build
   session, or does it need numeric thresholds (matched length distributions; a
   minimum number of length-matched given/new pairs)?
4. Is the synthetic-stimulus choice the right contamination defense, or does it
   weaken the corpus anchor (the factor→outcome relation is estimated on attested
   items; synthetic items may fall outside its support)?

## Anti-cheat note

Ratifying this decision fixes the **yardstick** (which anchor, which indicator,
which control), never the **result**. The probe must not be run, nor the indicator
re-tuned, in the session that ratifies — and a NO-GO from the build session's
pre-run critic (e.g. on the length control) defers the run rather than relaxing the
control.
