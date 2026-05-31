---
id: relational-pilot-go
title: Decision 9 — build and run the two-AI relational reference-game pilot?
status: resolved
opened: 2026-05-31
resolved: 2026-05-31
resolved-by: Tom
ratified: GO (run it)
contingent-artifacts:
  - open-question/relational-meaning-pilot
---

# Decision: GO on the relational pilot ("Decision 9")

## The question

The project's most distinctive standing idea is **relational meaning** — whether meaning is
partly constituted *between* agents in interaction, not just computed inside one model and then
compared ([`concept/relational-meaning`](../../base/concepts/relational-meaning.md)). The sharpened
design lives at [`open-question/relational-meaning-pilot`](../../findings/open-questions/relational-meaning-pilot.md):
a two-AI **iterated dyadic reference game** over hard-to-name tangram figures, whose load-bearing
measure is **live-vs-shuffled trajectory-dependence** (does agent B's interpretation of a coined
term depend on the *ordered history* of the exchange, with the *content* of prior turns held
identical? — the signature of a convention built *between* rather than recomputed within).

This was the only substantive un-taken value-laden call standing between the project and its most
original possible result. The design, the deflationary null (a `distributional` story that survives
order-scrambling), the evidential bar, and the panel-as-agents were all fixed; the human convergence
baseline ([`resource/hawkins-tangrams`](../../base/resources/hawkins-tangrams.md)) was catalogued and
the literature-reading gate discharged. Only Tom's go-ahead to **build and run** the pilot remained.

## Resolution (2026-05-31): GO

**Tom green-lit the pilot ("run it").** The next session is to build and run it, per the design in
[`open-question/relational-meaning-pilot`](../../findings/open-questions/relational-meaning-pilot.md):

- **Agents:** the standard 3-family panel ([`config/models.md`](../../../config/models.md)), run as
  **homogeneous dyads first** (same model both roles), so a live-vs-shuffled gap cannot be an artifact
  of two different systems talking past each other; cross-family dyads are a later arm.
- **Conditions:** (1) live dialogue, (2) shuffled-history replay (the "averaged-within" control,
  content held identical), (3) single-agent-with-self baseline, (4) optional history-perturbation arm.
- **Load-bearing measure:** the live-vs-shuffled gap in B's interpretation/usage of the coined term.
  A live ≈ shuffled result is a **first-class relational null** (coordination, not constitution), to be
  written as such — not retuned.
- **Human anchor:** Hawkins tangrams supplies the *convergence/entrainment baseline* only; the novel
  trajectory-dependence measure is the pilot's own internal contrast and is **not** anchored by Hawkins.
  Fetching Clark & Wilkes-Gibbs 1986 (queued in [`base/wanted.md`](../../base/wanted.md)) for the fuller
  theoretical anchor is optional, not blocking.
- **Budget:** the most call-heavy probe to date (every round = a fresh generation for both agents on a
  growing history); kept deliberately small (~6–12 figures, ~6 rounds, a few dyads/condition) to stay
  inside the $20/week cap. Mind the Gemini reasoning-token caveat when budgeting `max_tokens`.

## Scope of this ratification

This fixes the **go/no-go**, not the result: it does not pre-judge whether the pilot comes out a
relational positive (live ≠ shuffled) or a relational null. On a positive, the natural promotion is a
`conjecture` page that the theory page absorbs as the bottom rung of its relational "second ladder";
a null is recorded as a first-class negative.

The decision was ratified during a documentation-only consolidation session, so the **run itself is
deferred to the next session** (this session spent $0 and ran no experiments); the green-light is
recorded here and surfaced as the next concrete action in [`NEXT.md`](../../../NEXT.md).
