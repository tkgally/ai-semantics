# NEXT.md

## State

The project has **seven own-design `result` pages**: six behavioral probes (CC ceiling positive; CxNLI distinction negative; conative positive-with-divergence; caused-motion ceiling positive; way above-bar positive; argument-structure-coercion-v2, the first off-ceiling) **plus a new read-only instrument-disagreement re-analysis** (no new data, $0.00). Cumulative OpenRouter spend ≈ **$0.56** (unchanged this session). Eleven decisions ratified; **two open, both non-blocking**.

This session (2026-05-30, **workflow mode**) ran under a **degraded harness output-delivery channel** (tool results buffered and flushed in large irregular batches; see `log.md`). Work was kept durable via senselint-gated checkpoint commits. It shipped two units from the prior backlog + refreshed docs:

1. **New result — [`result/instrument-disagreement-reanalysis-v1`](wiki/findings/results/instrument-disagreement-reanalysis-v1.md):** a read-only re-analysis (no new API calls) of the two existing both-instrument runs, computing a per-model × per-construction |NLI gap − FC gap| statistic. **Near-null:** large disagreement (50 pp) is confined to the single gpt-5.4-mini × conative cell; the other 8 cells are ≤ 20.8 pp. Numbers reconciled by the orchestrator against the parents' `raw/results.json`. Advances [`open-question/instrument-sensitivity-constructional-inference`](wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md).
2. **New resource — [`resource/dwug-usage-graphs`](wiki/base/resources/dwug-usage-graphs.md):** DWUG catalogued + evaluated as the ratified Option-B graded lexical anchor candidate. The license/scale/counts/fetchability/fit verification breakdown is on the page. **Flagged for an adversarial read next session** (the independent coherence subagent was not separately re-run this session).
3. **Docs:** root `README.md` status refresh + `decisions/`→`wiki/decisions/` path fix; `wiki/index.md`, `wiki/base/resources/index.md`, `wiki/base/wanted.md` (DWUG status), `wiki/executive-summary.md` updated.

## Next concrete action (workflow-mode backlog)

1. **Adversarial read of [`resource/dwug-usage-graphs`](wiki/base/resources/dwug-usage-graphs.md)** — confirm the license + scale quotes are verbatim against the cited URLs and the fit assessment is sound. If DWUG verifies, freeze the polysemy/homonymy stratification and design the [`conjecture/lexical-sense-gradience`](wiki/findings/conjectures/lexical-sense-gradience.md) monotonicity probe (with its context-similarity control). If DWUG does not fit, evaluate CoSimLex (SemEval-2020 Task 3). This is the cheapest live unit — in-repo, read-only.
2. **Matched off-ceiling cancel-direction (harder conative) probe** — run alongside the coercion-v2 add-direction arm to **de-confound the add/cancel asymmetry from ceiling** (the headline open scientific question). Reuse the coercion-v2 harness in `experiments/runs/2026-05-29-argument-structure-coercion-probe-v2/`. The instrument re-analysis says: **run both instruments** (the one fragile cell is gpt-5.4-mini × conative, so the cancel-direction probe is exactly where instrument disagreement is most likely).
3. **v2b — subtler/implicit conflicting cue** (the bolted-down-object world-knowledge variant the coercion-v2 only deferred); same ratified difficulty gate, no new decision.
4. **Comparative-correlative v2** — unblocked (same ratified difficulty gate); [`design/comparative-correlative-v2`](experiments/designs/comparative-correlative-v2.md) can be built+frozen+run.
5. **AANN small-model lane** (when local compute is available) — the only clean path to true Option-A surprisal; OpenRouter exposes none. Held by Tom.
6. **Relational pilot** — fetch Clark & Wilkes-Gibbs 1986 (P1 in `wiki/base/wanted.md`) + do the multi-agent-LLM/alignment literature-read before promoting [`open-question/relational-meaning-pilot`](wiki/findings/open-questions/relational-meaning-pilot.md) to a design.

Run `python3 tools/senselint.py` (0 errors) + `python3 tools/linkify.py` before every commit. Keep claims modest; nulls first-class.

## Blocked / pending Tom (2 open decisions, both non-blocking)

- [`decisions/open/aann-panel-logprob-blocker`](wiki/decisions/open/aann-panel-logprob-blocker.md) — AANN held (Tom's call); the clean path needs local compute. Stays open/unrun. Not blocking other work.
- [`decisions/open/conflicting-cue-human-anchor`](wiki/decisions/open/conflicting-cue-human-anchor.md) — low-priority, non-blocking; tracks the pending human anchor for the internal-contrast-only coercion-v2 result. A one-liner from Tom closes it.

## Reminder for the next cold-start

Charter `PROJECT.md` (purpose/modesty §1/§2); schema `CLAUDE.md` (rule 6); run discipline `PROTOCOL.md` ("continue working" ⇒ workflow mode). **Read [`wiki/executive-summary.md`](wiki/executive-summary.md) first, then `wiki/index.md`**; reconcile `wiki/decisions/open/` (2 open, both non-blocking). **HARNESS NOTE:** this session hit an intermittent tool-output-delivery lag; if you see the same, commit via senselint-gated checkpoint scripts so completed work survives container reclamation, and prefer `run_in_background` for long subagents. The cheapest live unit is the **DWUG adversarial read** (#1 above — in-repo, read-only, no decision).
