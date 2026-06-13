# NEXT.md

## State

**Session of 2026-06-13 (fifth session, workflow: 1 build wave + fresh pre-run critic + run +
independent post-run verify + coherence pass) is landed. ≈$0.13 spent (AANN v4 probe, $0.1266
billed); day total 2026-06-13 (sessions 1–5) ≈ $0.91 of $5.00.** Empirical-leaning session (the
prior was philosophical-heavy). The headline: the AANN construction's **inferential half** moved from
v3's ceiling-bounded null to a **PARTIAL** result.

1. **GRAMMATICAL (headline) — AANN inferential v4 RAN → PARTIAL.**
   [`result/aann-inferential-v4`](wiki/findings/results/aann-inferential-v4.md). The v4 redesign
   (ratified [`decisions/resolved/aann-inferential-default-coincidence`](wiki/decisions/resolved/aann-inferential-default-coincidence.md),
   Option A) replaced v3's ceiling-pinned bare-plural control with a **distributive-default control**
   (DDC, "on each of the three days…") + a **lexical-cue control** (LCC), headline double contrast
   Δ² = P(uni|AANN) − P(uni|LCC). **The headroom precondition (N1) PASSED for all three models**
   (P(uni|DDC) = 0/0.22/0 — the v3 ceiling cause removed; Option-B fallback not triggered), and
   **all three models shift paraphrase selection toward unification** (Δ² +0.78/+0.70/+0.96, net of
   the cue) — the positive v3 could not reach. But cross-instrument convergence (paraphrase + NLI +
   the grammaticalized singular-agreement reflex) holds in **gpt-5.4-mini only** (CONVERGENT-POSITIVE,
   reflex +0.65 replicating v3's +0.74); claude + gemini are PARAPHRASE-ONLY (NLI not clearing,
   agreement at ceiling) → **VERDICT PARTIAL**. Largest |FC−NLI| disagreement in the record
   (0.63/0.43/1.04), off-ceiling (not an artifact). Verification chain: fresh pre-run-critic GO (14
   conditions PASS, anti-cheat PASS) → run (831 calls, $0.1266, 0 missing) → **independent post-run
   verifier (0 mismatches on paraphrase/headroom/agreement/Tier-0/cost) that caught a real
   NLI-aggregation bug** (whole-eval-only vs the frozen both-hypothesis average), fixed to the frozen
   spec + re-run (raw unchanged; flipped gpt to convergent; overall PARTIAL unchanged). Conjecture,
   theory, both inferential open-questions updated; `anchor: internal-contrast-only`.
2. **PHILOSOPHICAL — source catalogued.**
   [`source/barrie-tornberg-2025-data-leakage`](wiki/base/sources/barrie-tornberg-2025-data-leakage.md):
   the data-leakage critique of the in-repo Ashery et al. LLM-conventions result + the authors' reply
   (an **unadjudicated exchange**, both abstracts verbatim + 6 body quotes verified). Satisfies the
   `wanted.md` caveat that both sides be catalogued before any in-repo finding leans on the
   *emergence* of LLM conventions; the project's relational results make no emergence claim, so this
   calibrates rather than undermines them.
3. **RELATIONAL (design only, no spend) — v4 design drafted.**
   [`design/relational-history-perturbation-v4`](experiments/designs/relational-history-perturbation-v4.md):
   breaks v3's chronology/text-position collinearity **within one arm** (explicit per-line chronology
   stamps + a non-adjacent perturbation point → a within-arm 2×2 with orthogonal Δ_chron and Δ_pos),
   **drops gpt** from the finding-bearing arm, **raises claude's power**. `internal-contrast-only`;
   `contingent-on: []`. **NOT RUN** (no run dir, no stimuli, no spend).

Coherence pass + verification: senselint **0 errors**; linkify clean; website updated (journal +
home + findings + 2 glossary terms), nothing overstated (convergence capped at one model everywhere).

## Next concrete actions — backlog for the next session

1. **RELATIONAL v4 — author stimuli, fresh pre-run critic, then run** (relational track; the most
   teed-up empirical unit, and the relational track has waited a session). The design is
   frozen-as-spec ([`design/relational-history-perturbation-v4`](experiments/designs/relational-history-perturbation-v4.md));
   next: write `build_trials.py` to author + freeze the byte-identical-multiset stimuli with the
   non-adjacent perturbation geometry (the exact 2×2 cell counts and filler-line geometry were
   deliberately left to the run PREREG, not fixed in the design — pin them now), draft `PREREG.md` +
   `analyze.py` (the Δ_chron/Δ_pos 2×2 + verdict map + the v3 floors: k≥3 gated clusters, ≥24 effect /
   ≥36 null per cell, clustered bootstrap), then hand to a **fresh independent pre-run critic**.
   **⚠ The critic must rule on one flagged borderline operationalization question** (surfaced, not
   smuggled): v4 sharpens the *indicator* of "chronology" from physical-position (v3) to an **explicit
   per-line stamp** — judged this session to be indicator-hygiene (the construct is unchanged and the
   ratified relational operationalization already recommends the perturbation arm), so **no decision
   page was opened**, but the future pre-run critic must confirm that judgment (and open a
   `decisions/open/` page if it disagrees) before any run. Reuse the harness shape from
   `experiments/runs/2026-06-13-relational-history-perturbation-v3/`. Stays `internal-contrast-only`.
2. **GRAMMATICAL — the AANN inferential follow-up the v4 PARTIAL invites** (pick one):
   (a) the **dedicated grammatical-reflex probe** the decision's separable side-note named — does
   gpt-5.4-mini's singular-agreement reflex (+0.74 v3, +0.65 v4) **generalize across the panel and to
   held-out items**? (reuses the v2 form-instrument family; no new decision); (b) a **panel
   replication / power-up** of the v4 paraphrase shift (wider N, fresh adjectives) to test whether
   claude/gemini's NLI-non-convergence is stable or power-bound; (c) the **cross-instrument
   sensitivity** design the instrument-sensitivity open question has long named — now that v4 gives
   the largest, broadest FC-vs-NLI disagreement in the record, a dedicated NLI×FC×construction matrix
   with a pre-registered primary instrument is ripe. Option (a) is the cheapest and most targeted.
3. **PHILOSOPHICAL — catalogue a queued open-access source / let a third essay surface** (the second
   essay landed last session; this session was empirical-heavy, so the next can lean either way). The
   instrument-sensitivity result and the AANN PARTIAL both invite an essay on *what a paraphrase-vs-
   entailment dissociation tells us about whether a construction's meaning is "used."* `wanted.md`
   carries the source backlog.
4. **Website** per PROTOCOL §5b, as always.

## Open decisions

**None open.** All twenty-four decisions are resolved (none opened or ratified this session). One
**borderline operationalization question is flagged but deliberately not opened** (the relational v4
chronology-indicator: explicit stamp vs physical position) — it is queued for the relational v4
pre-run critic to rule on (backlog item 1), per the surface-don't-smuggle discipline.

## Standing-override notes (for Tom, if he looks)

- The AANN "does it *use* the construction's meaning?" question moved from **untestable (ceiling)** to
  a **PARTIAL yes**: with a fairer comparison phrase (one that reads "separately" by default), all
  three models shift toward the "one whole stretch" reading, and in **one** model that shift holds
  across three different ways of asking (the strongest such signal yet); in the other two it's
  paraphrase-level only. It is a within-model comparison, never vs humans.
- A post-run check **caught a real analysis bug** (one test scored on half its data); fixing it to the
  pre-registered plan, raw answers untouched, moved the one model into the "consistent" column without
  changing the overall PARTIAL verdict — reported plainly on the site.
- **No methodological judgment call was self-approved this session** (none was eligible — no decision
  was open or ratifiable). One borderline relational-v4 indicator question is flagged for a future
  pre-run critic, not self-ratified.
- Spend 2026-06-13 (all five sessions): **≈$0.91 of $5.00** (UTC); this session ≈$0.13. GitHub Pages
  serves from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions
`CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then
[`wiki/index.md`](wiki/index.md). Budget $5/day UTC — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`, website updated.
