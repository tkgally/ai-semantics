# NEXT.md

## State

The project has **ten own-design `result` pages** (seven prior + **three new off-ceiling probes this session**) plus the read-only instrument re-analysis. This session (2026-05-30, **workflow mode**) ran the four-unit slate Tom selected — **A + B + C + D** — as four committed waves, landing in PR **#24**:

1. **A — DWUG adversarial read + lexical probe design.** Independent verification of [`resource/dwug-usage-graphs`](wiki/base/resources/dwug-usage-graphs.md): **VERDICT YES-WITH-CAVEATS** (DWUG verifies as the Option-B graded lexical anchor). Fixed a **BLOCKER** (annotator count ~4 → **9 for EN**) + upgraded figures to primary-verified. DWUG verifying unblocked the project's **first lexical probe design**, [`design/lexical-sense-gradience-v1`](experiments/designs/lexical-sense-gradience-v1.md), with a queued operationalization decision.
2. **B — [`result/conative-cancel-direction-v2`](wiki/findings/results/conative-cancel-direction-v2.md):** the matched off-ceiling cancel probe **de-confounds the add/cancel asymmetry from ceiling** — it **survives** (license-easier-than-suppress is about *direction*; gpt-5.4-mini fails suppression under NLI, gemini over-suppresses under FC).
3. **C — [`result/coercion-implicit-cue-v2b`](wiki/findings/results/coercion-implicit-cue-v2b.md):** decoders affirm a *physically impossible* coercion at 90–100% from an **implicit** world-knowledge cue, floor only under an **explicit** denial → the add-v2 "H-deep" is **explicit-outcome parsing, not world-model integration**.
4. **D — [`result/comparative-correlative-covariation-v2`](wiki/findings/results/comparative-correlative-covariation-v2.md):** the v1 CC ceiling **survives** off-ceiling stress (follow-construction vs world ~100%; multi-step composition 100%, incl. the diagnostic neg×neg=pos). The most robust constructional positive.

All three probes: own frozen stimuli (sha256-pinned, independent adversarial pre-run critiques applied), behavioral NLI+FC on the ratified panel, **0 NA**, numbers independently re-verified from raw JSON (CLEAN). Theory page revised (9th own-design result; asymmetry de-confounded; H-deep bounded; the unifying *"follow the stated construction over world knowledge"* observation).

**Two process notes (both disclosed in-repo):** (a) a **hardcoded-`ITEMS`-path bug** in the copied `probe.py` made B and C first run the *old* coercion-v2 stimuli (~$0.30 wasted, no result contaminated; fixed + re-run); (b) **budget tracking undercounts** — the probe's token-estimate is ~4.5× below actual OpenRouter billing (`usage.cost`); `config/budget.md` now carries actual figures and a flagged fix. Real spend is low single dollars, far under the $20/mo cap.

## Next concrete action (workflow-mode backlog)

1. **Run the first lexical probe** — the cheapest *new-axis* unit. DWUG is verified and the design is written. Gate first on Tom ratifying [`decisions/open/lexical-sense-gradience-operationalization`](wiki/decisions/open/lexical-sense-gradience-operationalization.md) (instrument / stratification / context-control — provisional default recorded), then mirror `dwug_en.zip` (CC BY-ND permits verbatim mirror) into `experiments/data/dwug/`, build the within-period pair set + a WordNet polysemy/homonymy stratification, freeze, run. Opens the **lexical** axis (every prior finding is constructional).
2. **Fix the budget-tracking method** (small maintenance, no API) — make `analyze.py`/the harness record the API-returned `usage.cost` instead of the stale local rate card; backfill is impossible for discarded runs but future rows should be actual.
3. **v2b remaining arms** — the near-miss form controls + multi-step composition the caused-motion v2b deferred; and a **CC v3** (embedded-CC under negation/modal/counterfactual) — same ratified gate, no new decision.
4. **AANN small-model lane** (held by Tom) — still the only clean path to true Option-A surprisal; needs local compute.
5. **Relational pilot** — fetch Clark & Wilkes-Gibbs 1986 (P1 in [`wiki/base/wanted.md`](wiki/base/wanted.md)) + the multi-agent-LLM literature read before promoting [`open-question/relational-meaning-pilot`](wiki/findings/open-questions/relational-meaning-pilot.md) to a design.

Run `python3 tools/senselint.py` (0 errors) + `python3 tools/linkify.py` before every commit. Claims modest; nulls first-class. **When copying a `probe.py`, fix its hardcoded `ITEMS` path first** (this session's bug).

## Blocked / pending Tom (3 open decisions, all non-blocking)

- [`decisions/open/lexical-sense-gradience-operationalization`](wiki/decisions/open/lexical-sense-gradience-operationalization.md) — **new (2026-05-30); gates the first lexical probe.** Instrument (behavioral panel vs small-model lane) / polysemy-homonymy stratification source / context-similarity control / synchronic filter. Provisional default recorded; a one-liner ratifies it. Non-blocking (a new axis, not a pending-result follow-up).
- [`decisions/open/aann-panel-logprob-blocker`](wiki/decisions/open/aann-panel-logprob-blocker.md) — AANN held (Tom's call); clean path needs local compute. Not blocking other work.
- [`decisions/open/conflicting-cue-human-anchor`](wiki/decisions/open/conflicting-cue-human-anchor.md) — low-priority, non-blocking; tracks the pending human anchor for the internal-contrast-only conflicting-cue results (now four of them: coercion-v2 + the three v2/v2b results this session). A one-liner closes it.

## Reminder for the next cold-start

Charter `PROJECT.md` (purpose/modesty §1/§2); schema `CLAUDE.md` (rule 6); run discipline `PROTOCOL.md` ("continue working" ⇒ workflow mode). **Read [`wiki/executive-summary.md`](wiki/executive-summary.md) first, then `wiki/index.md`**; reconcile `wiki/decisions/open/` (3 open, all non-blocking). The cheapest live *new-axis* unit is the **lexical probe** (#1 above — anchor verified, design written, gated only on a one-line operationalization ratification).
