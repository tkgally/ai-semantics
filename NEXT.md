# NEXT.md

## State

All five P1 source pages are now `received`: Bender & Koller 2020, Lyre 2024, Piantadosi & Hill 2022, Weissweiler et al. 2023, and Mahowald et al. 2024. All have section-level verbatim quotes extracted from arXiv HTML or ar5iv. Three open decisions remain pending Tom (`decisions/open/aann-stimulus-source.md`, `decisions/open/aann-operationalization.md`, `decisions/open/way-construction-anchor.md`).

## Next concrete action

**The reading list is complete. The source base is now ready to anchor findings pages.** The next action is to write the first **result** or **claim** page, OR to run the AANN probe against the panel — whichever Tom ratifies.

The most tractable unblocked path (no pending decisions):

1. **Write a `claim` page** grounded in Mahowald et al. 2024 — claim that LLM performance on structural acceptability tasks (e.g., AANN) is evidence of *formal* competence, not *functional* competence, and therefore does not constitute evidence about constructional meaning in the full sense. This claim is directly groundable right now: `anchors: resource/mahowald-2023-aann-stimuli` + `depends-on: source/mahowald-2024-dissociating`. It does not require running any probe.

   - File: `wiki/findings/claims/formal-competence-aann-ceiling.md` (draft name)
   - Status: `proposed`
   - Meaning-senses: `functional-vs-formal`, `constructional`
   - This is the theoretical wedge that makes the AANN probe scientifically interesting.

2. **Alternatively:** Await Tom's ratification of `aann-operationalization` and `aann-stimulus-source` and then run the AANN probe.

Files the next run will need:

- `wiki/meaning-senses.md` — controlled vocabulary
- `wiki/base/sources/mahowald-2024-dissociating.md` — grounds the formal/functional claim
- `wiki/base/resources/mahowald-2023-aann-stimuli.md` — anchor resource
- `wiki/findings/conjectures/aann-construction.md` — the conjecture the claim qualifies
- `decisions/open/aann-operationalization.md` — check if ratified

## Blocked pending Tom

- `decisions/open/aann-stimulus-source.md` — ratify Mahowald 2023 as primary anchor (default), or switch.
- `decisions/open/aann-operationalization.md` — ratify continuation-likelihood contrast + T1 threshold (default), or switch.
- `decisions/open/way-construction-anchor.md` — ratify Option A (Goldberg 1995 examples as seed, anchor: pending), or supply corpus annotation (Option B), or identify published inference data (Option C). "Option A stands" is sufficient.

Charter-level points worth Tom's attention when convenient:

- Panel is still on a single liveness probe; confirm or rotate after the first real probe-run.
- `wiki/base/wanted.md` P1 list still has Sterken & Cappelen (forthcoming) and Grindrod (2024–25 monograph) outstanding; neither is gating any active probe.

## Reminder for the next cold-start

Charter: `PROJECT.md`. Schema: `CLAUDE.md`. Run discipline: `PROTOCOL.md`. Read `wiki/index.md` before opening individual pages. **Reconcile `decisions/open/` first.** **Commit and merge to the default branch before stopping.**
