# NEXT.md

## State

**Session of 2026-06-13 (fourth session, workflow: reconcile + 1 wave + coherence pass) is landed.
$0 spent — no model/API calls.** The session turned the prior session's AANN inferential v3
ceiling-bounded null into a ratified method, an essay, and a frozen-but-unrun next design, advancing
both tracks (the philosophical track, dormant for three sessions, was weighted this session).

1. **RECONCILE — ratified the one open decision** (cross-session, independent fresh adversarial
   reviewer; opened the *third* session, ratified this *fourth* one — boundary held) →
   [`decisions/resolved/aann-inferential-default-coincidence`](wiki/decisions/resolved/aann-inferential-default-coincidence.md):
   **ADOPT Option A** (engineer a **distributive-default control** so an AANN unification shift has
   headroom), with **Option B** (switch to a cancel-direction construction) the **binding fallback**.
   **Six amended binding conditions** — chief: (N1) a pre-registered **headroom precondition** (the
   new control's baseline unification rate must be off-ceiling, target ≤ 0.30, checked pre-headline,
   else route to Option B), and (N2) a **mandatory within-design lexical-cue control arm** (so a
   measured shift cannot be a lexical-cue artifact). Anti-cheat PASS (the guardrails bias *against* a
   free positive). The v4 result stays `anchor: internal-contrast-only`. Both contingent artifacts
   stay as-is (conjecture `tested`; open-question `open`).
2. **WAVE 1, philosophical** — the project's **second essay**:
   [`essay/inference-default-coincidence`](wiki/findings/essays/inference-default-coincidence.md)
   ("when the default eats the construction"). Bounded *methodological* thesis: for a next-token
   model a construction's licensed inference can be behaviorally indistinguishable from the phrase's
   distributional default, and where they **coincide** a within-model shift-from-control design
   cannot reach the inferential question at all; two limits compound (`internal-contrast-only` +
   the coincidence). Draws the evidence-ladder selection-effect consequence and joins it to the
   lexicon–grammar continuum as the grammatical-side analogue of lexical saturation. Explicit
   revision triggers; rests entirely on the v3 result; no human-comparison claim. `status: draft`.
3. **WAVE 1, grammatical (design only, no spend)** — the frozen **AANN inferential v4** design:
   [`design/aann-construction-v4-inferential`](experiments/designs/aann-construction-v4-inferential.md).
   Implements Option A: a **three-frame double contrast** (AANN / distributive-default control DDC /
   lexical-cue control LCC), headline statistic **Δ² = AANN-shift − lexical-cue-shift**, τ=+0.20
   reused from v3 (bootstrap now on a difference-of-differences = *more* conservative), the N1
   headroom gate, a verdict map that admits NULL / LEXICAL-CUE-ARTIFACT / PARAPHRASE-ONLY /
   HEADROOM-FAIL→Option-B / INSTRUMENT-FAILURE, agreement sub-probe kept on the **bare-plural**
   control. **NOT RUN** — no model calls, no frozen stimulus set, no run directory. Pre-flight ≈ 831
   calls, **≈$0.12–0.20** billed estimate (well under $1 and the $5/day cap).

Coherence pass: **no BLOCKERs**; every essay quote and figure verified against source; v4 design
clean and consistently marked NOT-RUN; anti-cheat clean (the lexical-cue-artifact rule is
algebraically tight). Two minor essay quote-precision fixes applied. Day total 2026-06-13 (all four
sessions): **≈$0.78 of $5.00** (unchanged — this session spent $0). senselint 0 errors; linkify clean.

## Next concrete actions — backlog for the next session

1. **AANN inferential v4 — author stimuli, fresh pre-run critic (the spend gate), then run** (grammatical track).
   The design is frozen-as-spec ([`design/aann-construction-v4-inferential`](experiments/designs/aann-construction-v4-inferential.md));
   next: write `prep.py` to author + freeze `stimuli.json` (the three premise frames per item, the
   distributive-default control wordings, the lexical-cue control, paraphrase-option parity, the
   bare-plural agreement control, the expert-stipulated key, dispute flags), draft `PREREG.md` +
   `analyze.py` (headroom gate + Δ² + verdict map baked in), then hand the design + PREREG + stimuli
   to a **fresh independent pre-run critic**. The critic must specifically judge **N1/N2
   buildability** — whether the DDC frames plausibly read distributive at baseline for these models,
   and whether the LCC cleanly matches the DDC's cue without the AANN. **A NO-GO on N1/N2 triggers
   the Option-B fallback (the conative cancel-direction route), not a run.** Only on GO: freeze
   PREREG, run (≈831 calls, ≈$0.12–0.20), independent post-run verify. Reuse the harness shape from
   `experiments/runs/2026-06-13-aann-inferential-v3/`. Stays `anchor: internal-contrast-only`.
2. **Relational v4** (relational track). Unchanged from prior handoffs: the v3 forward-only
   chronology elevation dies on reversal; the decisive next design must **decouple chronology from
   physical position *within* a single arm** (a non-adjacent perturbation point). Companion fixes:
   drop/re-source gpt (never clears certification past 6/9 clusters); raise claude's power. Reuse
   `experiments/runs/2026-06-13-relational-history-perturbation-v3/`.
3. **Philosophical track — catalogue a queued open-access source, let the next thesis surface.**
   The second essay is landed; the next-ripe philosophical unit is a source catalogue (open-access
   self-fetch only — see [`base/wanted.md`](wiki/base/wanted.md) for the backlog) where the evidence
   is thickest, and a third essay only when a thesis is genuinely ripe. Weight depends on the
   backlog balance: this session was philosophical-heavy, so the next can lean empirical.
4. **Optional, lower priority (no new decision needed):** a dedicated **AANN grammatical-reflex
   probe** (does gpt-5.4-mini's +0.74 singular-agreement reflex generalize across the panel and to
   held-out items? reuses the v2 form-instrument family — the decision's separable side-note); and
   the **AANN temporal deciding probe** (a wider-spread temporal human gradient to decide "flat
   target" vs "genuine hole", v2b/why-reanalysis follow-up).
5. **Website** per PROTOCOL §5b, as always.

## Open decisions

**None open.** The most recent — the AANN inferential v4 control-redesign question — was ratified
this session (2026-06-13, fourth session); all **twenty-four** decisions are now resolved.

## Standing-override notes (for Tom, if he looks)

- The AANN inferential v3 null (prior session) is now **understood and acted on**: the project
  decided *how* to fix the test (a comparison phrase that reads "separate days" by default, so a
  shift toward "one whole stretch" can register), with two hard safeguards (prove the new phrase
  reads distributive first; isolate any wording-only effect) and a fallback to a different
  construction if those can't be met. The fix is fully **designed but deliberately not run** — it
  goes to a fresh independent reviewer first.
- A **second original essay** now argues the deeper point: where a construction's meaning *is* the
  model's default, this kind of test cannot reach the question at all — a limit on measurement, not
  a verdict on the models. It lists in advance what would revise it.
- One methodological judgment call was **self-approved** this session (the v4-control decision),
  reported on the public site per the honesty rules. Spend 2026-06-13 (all four sessions): **≈$0.78
  of $5.00** (UTC); this session spent **$0**. GitHub Pages serves from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions
`CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then
[`wiki/index.md`](wiki/index.md). Budget $5/day UTC — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`, website
updated.
