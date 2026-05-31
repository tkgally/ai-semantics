# NEXT.md

## State

The project is **three-axis**: **grammatical** (live, robust — 11 own-design results), **lexical**
(live: clauses a+c supported; clause **b** — the distinctive polysemy-vs-homonymy *discreteness* bet —
a **powered null** at the WiC anchor), and **multimodal / grounding** (two negatives). **No finding
changed in the consolidation work below.**

Two sessions are recorded here:

1. **Consolidation pass (2026-05-31, merged as PR #32).** Documentation only — no experiments, $0.
   Refreshed both theory pages to absorb the latest results; hardened the provenance of 8 source pages
   (re-verifying quotes verbatim where fetchable, keeping honest flags where not — e.g. corrected three
   paraphrased Harnad quotes and an ARO "Table 1" error); swept the index/catalog for stale
   anchor/contingent notes; refreshed two open-questions and the multimodal conjecture. No finding
   created, changed, promoted, or retired.

2. **Decisions recorded (2026-05-31, this follow-up branch).** Tom reviewed the three pending decisions
   and ruled. These are now written into the wiki:
   - **Relational pilot ("Decision 9") = GO.** Green-lit; see
     [`decisions/resolved/relational-pilot-go`](wiki/decisions/resolved/relational-pilot-go.md).
     **This is now the next concrete action** (the run is deferred to the next session, since this one is
     documentation-only).
   - **AANN probe = keep HOLD.** No `TOGETHER_API_KEY` added; the AANN surprisal path stays blocked.
     Reaffirmed in [`decisions/open/cloud-compute-path`](wiki/decisions/open/cloud-compute-path.md)
     (stays open).
   - **`open-question/lexical-polysemy-gradience` reverted to `open`** (Tom preferred it stay live rather
     than "answered" — its distinctive discrete-regime sub-arm is a powered null, not a positive
     resolution). Still largely addressed; held open for a future graded, homonymy-enriched clause-(b) test.

## Next concrete action — RUN THE RELATIONAL PILOT (green-lit)

**Build and run the two-AI iterated dyadic reference-game pilot** per the design in
[`open-question/relational-meaning-pilot`](wiki/findings/open-questions/relational-meaning-pilot.md) and
the ratified [`decisions/resolved/relational-pilot-go`](wiki/decisions/resolved/relational-pilot-go.md):

- **Agents:** the 3-family panel, **homogeneous dyads first** (same model in both roles); cross-family a later arm.
- **Conditions:** (1) live dialogue, (2) shuffled-history replay (content identical, order destroyed — the
  deflationary "averaged-within" control), (3) single-agent-with-self baseline, (4) optional history-perturbation arm.
- **Load-bearing measure:** the **live-vs-shuffled gap** in B's interpretation/usage of the coined term.
  A live ≈ shuffled outcome is a **first-class relational null** (coordination, not constitution) — write it, don't retune it.
- **Human anchor:** [`resource/hawkins-tangrams`](wiki/base/resources/hawkins-tangrams.md) supplies the
  convergence/entrainment baseline only; the trajectory-dependence measure is the pilot's own internal contrast.
  Fetching Clark & Wilkes-Gibbs 1986 (in [`base/wanted.md`](wiki/base/wanted.md)) is optional, not blocking.
- **Discipline:** freeze + commit stimuli (sha256) before any call; ≥1 independent pre-run critic + ≥1
  post-run verifier. **Budget:** the most call-heavy probe to date — keep it small (~6–12 figures, ~6 rounds,
  a few dyads/condition) to stay under the $20/week cap; mind the Gemini reasoning-token cost when setting `max_tokens`.
- On a positive, promote to a `conjecture` and let the theory page absorb it as the bottom rung of the relational "second ladder".

## Still on hold / pending Tom

- **AANN probe** — HOLD (Tom's reaffirmed call): no logprob path on the current panel; a Together
  `echo+logprobs` path would unblock the Option-A surprisal for <$1 **if** Tom later adds a
  `TOGETHER_API_KEY` ([`decisions/open/cloud-compute-path`](wiki/decisions/open/cloud-compute-path.md),
  [`decisions/open/aann-panel-logprob-blocker`](wiki/decisions/open/aann-panel-logprob-blocker.md)).
- **Image probe v2 / VWSD** — un-gated but low-motivation (text-only panel already saturates the
  word-sense cases tried); worth it only to push the grounding axis into genuinely image-native territory.

## Reminder for the next cold-start

Charter `PROJECT.md`; schema `CLAUDE.md`; run discipline `PROTOCOL.md` ("continue working" ⇒ workflow
mode). **Read [`wiki/executive-summary.md`](wiki/executive-summary.md) first, then `wiki/index.md`**;
reconcile `wiki/decisions/open/` (2 open, the non-blocking AANN/compute pair). **The headline for the next
run: the relational pilot is GREEN-LIT — it is the next experiment to build and run.** It is the project's
most distinctive next step; do it under the freeze + pre/post-critic discipline and the budget cap.
