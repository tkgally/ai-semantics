---
id: relational-anchor-shortlist
title: Which human dyadic-interaction resource should anchor the relational-meaning pilot?
status: open
opened: 2026-05-29
opened-by: orchestrator
contingent-artifacts:
  - open-question/relational-meaning-pilot
---

# Decision: relational-meaning anchor shortlist

## Question

The [`open-question/relational-meaning-pilot`](../../findings/open-questions/relational-meaning-pilot.md) proposes a concrete minimal pilot — an iterated dyadic reference game between two LLM agents, with a live-vs-shuffled-history contrast as the discriminator for whether a convention is *constituted between* agents rather than *computed within each and aggregated*. Per the charter's independent-human-bearing commitment ([`PROJECT.md`](../../../PROJECT.md) §2.5) and always-on rule 5, any relational result needs a human-generated dyadic-interaction resource as its anchor before it can be promoted. None is in-repo. This decision picks the anchor (and queues the fetch).

The anchor must supply at least one of: (a) a human convergence/entrainment curve over rounds against which the LLM dyads' behavior can be compared, or (b) a documented dyadic paradigm whose design the pilot can mirror so that "minimal" is grounded in an established human task.

## Options

### A. Clark & Wilkes-Gibbs 1986, "Referring as a collaborative process" (provisional default)

- **What:** the canonical referential-communication / tangram-naming study; dyads collaboratively coin and compress shared labels for hard-to-name figures over repeated rounds.
- **What it grounds:** the pilot's task design directly (the iterated reference game is modeled on this paradigm) and the human entrainment/compression curve the LLM dyads would be compared against.
- **Why provisional default:** its paradigm maps one-to-one onto the proposed pilot; it is the most-cited single demonstration of collaborative reference; it is a discrete, fetchable paper.
- **Limit:** it documents the human convergence pattern but does not itself run the live-vs-shuffled control that is the pilot's load-bearing contrast — so it anchors the *task and the human convergence baseline*, not the trajectory-dependence measure (which is novel to the LLM probe).

### B. HCRC Map Task corpus (Anderson et al. 1991)

- **What:** a corpus of task-oriented human dialogues with referential alignment in a goal-directed setting.
- **What it grounds:** corpus-grade entrainment statistics in goal-directed dyads; larger N than a single experiment.
- **Limit:** it is route-description, not a coin-a-label-for-a-novel-figure paradigm, so the mapping to the pilot's reference game is looser; richer for entrainment, weaker for label-coinage.

### C. Krauss & Weinheimer 1964/1966 reference-phrase-shortening studies

- **What:** the earlier reference-phrase-shortening experiments documenting the convergence curve.
- **What it grounds:** the entrainment/compression measure's calibration.
- **Limit:** older, less complete documentation; largely subsumed by Clark & Wilkes-Gibbs for the pilot's purposes.

### D. Pickering & Garrod 2004 interactive-alignment framework (theoretical anchor only)

- **What:** the most-cited mechanistic model of dialogue alignment-across-levels.
- **What it grounds:** the theoretical framing — what alignment predicts and, importantly, what it does *not* claim about meaning-constitution.
- **Limit:** a framework, not a rated dataset; it cannot serve as the empirical human anchor, only as the theoretical backdrop. Best used *alongside* one of A–C.

## Provisional default (in force until Tom ratifies)

**Option A** (Clark & Wilkes-Gibbs 1986) as the primary empirical anchor, with **Option D** (Pickering & Garrod 2004) as the theoretical backdrop. The pilot stays at `open-question` / `anchor: pending` until the anchor is fetched and Tom ratifies.

Rationale: (i) the pilot's task is a direct instance of the Clark & Wilkes-Gibbs paradigm; (ii) it gives a human convergence baseline the LLM dyads can be compared against; (iii) it is a single fetchable paper, queued in [`base/wanted.md`](../../base/wanted.md).

## What would change the default

- If the pilot's emphasis shifts toward corpus-scale entrainment statistics rather than label-coinage, promote Option B (Map Task).
- If Tom names a different dyadic resource (e.g. a more recent LLM-vs-human reference-game dataset with released per-round data), adopt it.

## Notes for the resolver

Tom: a one-line ratification is enough — "A stands", "use Map Task", or name a specific resource. Reminder: no new human-subject collection — existing released datasets/paradigms only. The pilot itself is also gated on a literature-reading step (multi-agent-LLM + alignment) before it promotes to a design; this decision only fixes the *anchor*, not the readiness to run.
