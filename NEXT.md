# NEXT.md

## State

The project has **six own-design `result` pages** spanning the upper (Tier 3→4) evidence ladder (five behavioral minimal-pair positives/negatives + the first off-ceiling result), all read-only, all 0-NA, cumulative OpenRouter spend ≈ **$0.56** against the $20/mo soft cap ([`config/budget.md`](config/budget.md)). Eleven decisions ratified; **two open, both non-blocking**.

This session (2026-05-29, **wiki-maintenance in workflow mode**, no new experiments) did housekeeping + completeness work, not probing:

1. **New deliverable — [`wiki/executive-summary.md`](wiki/executive-summary.md)**: a plain-language summary of the project's purpose and current state, linked from `index.md` "What to do next". **Standing task: refresh it at the end of every session** (Tom's request). It is intentionally jargon-light for a non-specialist reader; keep it factually faithful to the result pages + `NEXT.md`.
2. **Two new base concept pages filling genuine referential gaps**: [`concept/relational-meaning`](wiki/base/concepts/relational-meaning.md) (the `relational` meaning-sense had no concept home — the charter's distinctive "second ladder" axis; trajectory-dependence / live-vs-shuffled discriminator; anchor ratified-but-unfetched, no fabricated quotes) and [`concept/coercion`](wiki/base/concepts/coercion.md) (constructional coercion — the construction overriding the verb; central to 4 of 6 results; records the add-vs-cancel asymmetry modestly, confounded-with-ceiling). Both wired into the theory page + the relational pilot's link graph.
3. **Consistency fixes**: removed a duplicated "Resolved decisions" block in `wiki/index.md` (11 ratified, now listed once); added the missing `wic-graded-usage-similarity` entry to `wiki/base/resources/index.md` (it was in the main index but absent from the resources catalog).

Method: 2 waves — Wave 1 (orchestrator + 2 generation subagents + 1 read-only adversarial coherence pass: 0 BLOCKERs, 1 SHOULD-FIX applied = dropped 4 backwards `supports→result` links from the coercion page); Wave 2 (orchestrator integration/consistency). senselint 0 errors + linkify clean on every commit. Subagent tokens ≈210k.

## Next concrete action (workflow-mode backlog — experimental units are all fetch/compute/Tom-gated)

1. **DWUG/CoSimLex lexical-anchor verification** (the lexical Option-B follow-through — 529'd two sessions ago). Fetch+verify **DWUG** (graded usage-similarity, reportedly CC BY — confirm license/scale/counts/fetchability), else **CoSimLex**; if good, mirror to `experiments/data/` + write a resource page; then the lexical conjecture's monotonicity probe can be designed (freeze the polysemy/homonymy stratification first).
2. **v2b — subtler conflicting cue + the matched cancel-direction.** The v2 result tested only an *explicit* denial. Two clean follow-ups under the **same ratified difficulty gate** (no new decision): (a) a subtler world-knowledge / implicit cue (the bolted-down-object variant) to see if cue-sensitivity survives a non-explicit cue; (b) a matched off-ceiling **cancel-direction** (harder conative) probe to **de-confound the add/cancel asymmetry from ceiling** (the headline scientific question — see [`concept/coercion`](wiki/base/concepts/coercion.md)). Reuse the v2 harness in `experiments/runs/2026-05-29-argument-structure-coercion-probe-v2/`.
3. **Comparative-correlative v2** is unblocked (same ratified difficulty gate) — the CC v1 ceiling has no off-ceiling test yet; [`design/comparative-correlative-v2`](experiments/designs/comparative-correlative-v2.md) can be built+frozen+run.
4. **AANN small-model lane (when compute is available).** Tom held AANN; the only clean path (self-host a small open-weight model for true Option-A surprisal) needs local compute. OpenRouter exposes no usable surprisal path.
5. **Relational pilot:** fetch Clark & Wilkes-Gibbs 1986 (the ratified anchor, P1 in `wanted.md`) + do the multi-agent-LLM/alignment literature-read before promoting the pilot to a design. The conceptual groundwork now lives in [`concept/relational-meaning`](wiki/base/concepts/relational-meaning.md) + [`open-question/relational-meaning-pilot`](wiki/findings/open-questions/relational-meaning-pilot.md).

Run `senselint.py` (0 errors) + `linkify.py` before every commit. Keep claims modest; nulls first-class. **If subagents keep 529'ing, do adversarial passes as orchestrator self-reviews and say so.** Update `executive-summary.md` at wind-up.

## Blocked / pending Tom (2 open decisions, both non-blocking)

- [`decisions/open/aann-panel-logprob-blocker`](wiki/decisions/open/aann-panel-logprob-blocker.md) — AANN held (Tom's call); the clean path needs local compute. Stays open/unrun. Not blocking other work.
- [`decisions/open/conflicting-cue-human-anchor`](wiki/decisions/open/conflicting-cue-human-anchor.md) — **low-priority, non-blocking.** Tracks the pending human anchor for the internal-contrast-only v2 result; default = leave internal-contrast-only. A one-liner from Tom closes it.

## Reminder for the next cold-start

Charter `PROJECT.md` (purpose/modesty §1/§2); schema `CLAUDE.md` (rule 6); run discipline `PROTOCOL.md` ("continue working" ⇒ workflow mode). **Read [`wiki/executive-summary.md`](wiki/executive-summary.md) first for orientation, then `wiki/index.md`**; reconcile `wiki/decisions/open/` (2 open, both non-blocking). Six own-design result pages (CC ceiling positive; CxNLI distinction negative; conative positive-with-divergence; caused-motion ceiling positive; way above-bar positive; argument-structure-coercion-v2 — first off-ceiling, add-direction ceilings are cue-sensitive not template). Reusable harnesses in `experiments/runs/2026-05-29-*/`. **Datasets:** Mahowald=MIT (mirror OK), Scivetti=no-license (read in place), Usim=unfetchable+unlicensed (retired as anchor — Option B), DWUG=candidate (verify next). **AANN:** OpenRouter exposes no usable surprisal path; the small-model lane needs local compute. New concept homes this session: [`concept/relational-meaning`](wiki/base/concepts/relational-meaning.md), [`concept/coercion`](wiki/base/concepts/coercion.md).
