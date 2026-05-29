# NEXT.md

## State

The project now has **six own-design `result` pages** spanning the upper (Tier 3→4) evidence ladder — five behavioral minimal-pair positives/negatives plus the **first off-ceiling** result — all read-only against the panel, all 0-NA, cumulative OpenRouter spend ≈ **$0.56** against the $20/mo soft cap ([`config/budget.md`](config/budget.md)).

This session (2026-05-29) ran in two parts:

1. **Tom ratified all four open decisions** (interactive). Applied per PROTOCOL §2 (PR #20):
   - **relational-anchor-shortlist → Option A** (Clark & Wilkes-Gibbs 1986 + Pickering & Garrod 2004 backdrop) — resolved; pilot still needs the paper fetched + a literature-read.
   - **cc-v2-difficulty-operationalization → UNIFY + default** — resolved; one difficulty gate now governs CC + caused-motion + way (+ companion conative) v2.
   - **lexical-sense-gradience-anchor → Option B** (a different graded set, **not** Usim — verified-but-unfetchable/unlicensed) — resolved; replacement anchor (DWUG / CoSimLex) to be identified+verified.
   - **aann-panel-logprob-blocker → HELD.** Tom ratified "swap in models," but a **live-API check voided the premise**: only Qwen + OpenAI-gpt4o expose logprobs (not deepseek/grok/etc.) → no 3-family panel; and the *primary* surprisal indicator (Option A) is uncomputable on OpenRouter at all (no echo/prompt-logprobs). Re-surfaced; **Tom chose to hold AANN** (the clean path — the small-model lane for true Option-A surprisal — needs local compute). Stays open/unrun.

2. **Ran the first off-ceiling own-design probe** (the redirected "do other work") → [`result/argument-structure-coercion-v2`](wiki/findings/results/argument-structure-coercion-v2.md). A conflicting-cue stress test of the two add-direction ceilings (caused-motion + way): hold the construction + verb constant, append an explicit clause **denying** the added inference. **Result: the v1 ceilings are cue-sensitive, not a brittle template** — all three models drop to **floor on the cue items (affirm 0–20%, 60–100 pp drop), 3/3 models, both instruments, both constructions** (template/H-default reading 0/3). This *upgrades* the modest reading of the v1 add-direction positives (they survive an off-ceiling stress test). Calibration: only an *explicit* cue tested; construction asymmetry on the `resist` arm (way coerces traversal even on self-motion-precluding verbs); internal-contrast-only. **Note:** both the pre- and post-run adversarial passes were orchestrator self-reviews — the subagent failed 3× on transient API 529 (server overload); numbers were verified by hand against committed `raw/results.json`.

## Next concrete action (workflow-mode backlog — all now-unblocked or fetch-gated)

1. **DWUG/CoSimLex lexical-anchor verification** (the lexical Option-B follow-through — attempted this session but the verification subagent hit the 529 outage). Fetch+verify **DWUG** (graded usage-similarity, reportedly CC BY — confirm license/scale/counts/fetchability), else **CoSimLex**; if good, mirror to `experiments/data/` + write a resource page; then the lexical conjecture's monotonicity probe can be designed (with the polysemy/homonymy stratification frozen first).
2. **v2b — subtler conflicting cue + the matched cancel-direction.** The v2 result tested only an *explicit* denial. Two clean follow-ups under the **same ratified difficulty gate** (no new decision): (a) a subtler world-knowledge / implicit cue (the design's bolted-down-object variant) to see if cue-sensitivity survives a non-explicit cue; (b) a matched off-ceiling **cancel-direction** (harder conative) probe to **de-confound the add/cancel asymmetry from ceiling** (the design's headline scientific question). Reuse the v2 harness in `experiments/runs/2026-05-29-argument-structure-coercion-probe-v2/`.
3. **Comparative-correlative v2** is also now unblocked (same ratified difficulty gate) — the CC v1 ceiling has no off-ceiling test yet; [`design/comparative-correlative-v2`](experiments/designs/comparative-correlative-v2.md) can be built+frozen+run.
4. **AANN small-model lane (when compute is available).** Tom held AANN because the only clean path (B2: self-host a small open-weight model for true Option-A surprisal) needs local compute. If a future environment has it, that is the way to finally run the one priority-1 probe; the OpenRouter API cannot do it.
5. **Relational pilot:** fetch Clark & Wilkes-Gibbs 1986 (now the ratified anchor, priority in `wanted.md`) + do the multi-agent-LLM/alignment literature-read before promoting the pilot to a design.

Run `senselint.py` (0 errors) + `linkify.py` before every commit. Keep claims modest; nulls first-class. **If subagents keep 529'ing, do adversarial passes as orchestrator self-reviews and say so** (reduced independence is honest; silent skipping is not).

## Blocked / pending Tom (2 open decisions)

- [`decisions/open/aann-panel-logprob-blocker`](wiki/decisions/open/aann-panel-logprob-blocker.md) — AANN held (Tom's call); the clean path needs local compute. Stays open/unrun. Not blocking other work.
- [`decisions/open/conflicting-cue-human-anchor`](wiki/decisions/open/conflicting-cue-human-anchor.md) — **low-priority, non-blocking.** Tracks the pending human anchor for the internal-contrast-only v2 result; default = leave internal-contrast-only. A one-liner from Tom closes it.

## Reminder for the next cold-start

Charter `PROJECT.md` (purpose/modesty §1/§2); schema `CLAUDE.md` (rule 6); run discipline `PROTOCOL.md` ("continue working" ⇒ workflow mode). Read `wiki/index.md` before opening pages; **reconcile `wiki/decisions/open/` first** (2 open, both non-blocking). The project now has **six own-design result pages** (CC ceiling positive; CxNLI distinction negative; conative positive-with-divergence; caused-motion ceiling positive; way above-bar positive; **argument-structure-coercion-v2 — first off-ceiling, showing the add-direction ceilings are cue-sensitive not template**). Reusable harnesses: minimal-pair NLI+FC in `experiments/runs/2026-05-29-*/` (build_items.py → freeze CSV → probe.py → analyze.py); the v2 conflicting-cue harness is the template for v2b. **Datasets:** Mahowald=MIT (mirror OK), Scivetti=no-license (read in place), Usim=unfetchable+unlicensed (retired), DWUG=candidate (verify next). **AANN:** OpenRouter exposes no usable surprisal path (only Qwen+gpt-4o give next-token logprobs; none give echo/prompt-logprobs); the small-model lane is the only way and needs local compute. **Subagent infra was 529-flaky this session** — self-review fallback is acceptable if disclosed.
