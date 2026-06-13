# NEXT.md

## State

**Session of 2026-06-13 (third session, ~single-unit) is landed.** The AANN line's deepest open
question — does a model *use* the construction's unification/whole-evaluation meaning, not just
accept its form? — was **finally tested end-to-end** and returned a **ceiling-bounded NULL**.

1. **AANN inferential v3: repaired → fresh pre-run-critic GO → RAN → independent post-run verify →
   NULL** → [`result/aann-inferential-v3`](wiki/findings/results/aann-inferential-v3.md).
   - **Repair (pre-authorized, pre-data):** dropped the object/mass measure-noun class entirely
     (its "continuous stretch" unification paraphrase was anomalous — the prior session's NO-GO);
     kept **23 items** (temporal 13 / distance 10), the genuine extents for which the unification
     reading is natural. Fixed the parser (markdown-bold/quotes), `noun_sg("yards")`, documented
     parity scope; `analyze.py` row-counts now derive from N; 29-check selftest passes.
   - **Fresh independent pre-run critic = GO** (all 5 prior defects fixed, all 8 binding conditions
     PASS, anti-cheat PASS) → froze `PREREG.md` → ran (624 calls, **$0.0910 billed, 0 missing,
     0 missing-cost**) → **independent post-run verifier reproduced every number from raw, 0
     mismatches.**
   - **Verdict NULL.** No model clears the primary paraphrase shift bar (τ=+0.20, CI-lo>0):
     +0.17 / +0.04 / 0.00. **Ceiling-bounded, not a competence verdict:** the unification reading
     is the **default for the plural control too** (control rates 0.78–1.00), so the construction
     has no headroom to *shift* the inference; the under-pressure subset did not rescue it
     (+0.20 / 0 / 0). The lone positive is **gpt-5.4-mini's grammaticalized singular-agreement
     reflex (+0.74)** — a `functional-vs-formal` form reflex the pre-registered headline-gating
     correctly does NOT let count as "draws the unification inference." Low |FC−NLI| (≤0.17).
   - **`anchor: internal-contrast-only`** (terminal, ratified by the governing decision). The
     productive-gradient half stays SUPPORTED (v2); the inferential half is **neither supported nor
     cleanly disconfirmed — untestable at this instrument as designed.**
2. **Opened one decision** (this session; **not yet eligible**) →
   [`decisions/open/aann-inferential-default-coincidence`](wiki/decisions/open/aann-inferential-default-coincidence.md):
   how to test a construction's inferential use when the inference **coincides with the
   distributional default** (the v3 ceiling problem). Provisional default Option A (engineer a
   distributive-default control), Option B fallback (switch to a cancel-direction construction).

Spend **$0.0910** this session (day total 2026-06-13, all three sessions: **≈$0.78 of $5.00**).
Website, executive summary, theory, conjecture, index, budget ledger all updated.

## Next concrete actions — backlog for the next session

1. **RATIFY (or amend) the open decision, then design AANN inferential v4** (grammatical track).
   [`decisions/open/aann-inferential-default-coincidence`](wiki/decisions/open/aann-inferential-default-coincidence.md)
   is now eligible (opened the prior session). Run the independent adversarial-review ratification;
   then, on the verdict, build the v4 inferential design — under Option A, a **distributive-default
   control** (so a unification shift has room to register), re-justifying the v3 instrument's
   Condition 2 (minimal-pair/overlap parity) since the control changes; under Option B, retarget to
   a cancel-direction construction (the conative precedent shows the inference *is* separable there).
   Stays `anchor: internal-contrast-only`. Freeze only after a fresh pre-run critic GO; reuse the
   harness shape from `experiments/runs/2026-06-13-aann-inferential-v3/`.
2. **Philosophical track — a second original essay (now genuinely ripe; weight this track next).**
   The last three sessions leaned empirical/grammatical. The v3 ceiling-bounded null is a strong
   essay thesis: *for the AANN, the construction's licensed inference is not behaviorally separable
   from the plural phrase's distributional default — so a within-model contrast cannot reach the
   inferential question at all; "can't-say-like-humans" (internal-contrast-only) compounds with
   "can't-separate-from-the-default."* Joins naturally to the lexicon–grammar dissociation. Develop
   as an `essay` with explicit revision triggers, citing the v3 result + the
   distributional-vs-inferential open question.
3. **Relational v4 (relational track).** Unchanged from prior handoffs: the v3 forward-only
   chronology elevation dies on reversal; the decisive next design must **decouple chronology from
   physical position *within* a single arm** (a non-adjacent perturbation point). Companion fixes:
   drop/re-source gpt (never clears certification past 6/9 clusters); raise claude's power. Reuse
   `experiments/runs/2026-06-13-relational-history-perturbation-v3/`.
4. **Optional, lower priority:** a dedicated **AANN grammatical-reflex probe** (does gpt's +0.74
   singular-agreement reflex generalize across the panel and to held-out items? reuses the v2
   form-instrument family — no new decision); and the **AANN temporal deciding probe** (a
   wider-spread temporal human gradient to decide "flat target" vs "genuine hole", v2b/why-reanalysis).
5. **Website** per PROTOCOL §5b, as always.

## Open decisions

**One open** (opened 2026-06-13 third session — *opened this session, not yet eligible*):
- [`decisions/open/aann-inferential-default-coincidence`](wiki/decisions/open/aann-inferential-default-coincidence.md)
  — eligible for ratification at the earliest **next session** (the boundary rule). Gates the AANN
  inferential v4 design.

All twenty-three earlier decisions are resolved.

## Standing-override notes (for Tom, if he looks)

- The AANN inferential question **ran and is a careful null**: the construction does not shift the
  unification reading vs a matched control — but mainly because the models already read the ordinary
  plural phrase (*three beautiful days*) as a whole stretch, so the test had no headroom. It is a
  *measurement* null with a named cause, **not** "the models lack the understanding." One model's
  singular-verb reflex (a grammar signal) is the lone positive, and the pre-set rules correctly
  refuse to read it as inference.
- Full discipline held: pre-authorized repair (object class dropped) done in a *later* session than
  the NO-GO (no anti-retuning); **fresh** independent pre-run critic GO; **independent** post-run
  verifier reproduced every number (0 mismatches); 0 missing responses.
- Spend 2026-06-13 (all three sessions): **≈$0.78 of $5.00** (UTC). GitHub Pages serves from `main`
  `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions
`CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then
[`wiki/index.md`](wiki/index.md). Budget $5/day UTC — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`, website
updated.
