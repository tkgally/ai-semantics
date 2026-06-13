# NEXT.md

## State

**Session of 2026-06-13 (second session, workflow mode) is landed.** A **$0 session** (no
model calls): one decision ratified, one design built + independently reviewed + correctly
**held back**, one $0 re-analysis, one source catalogued. Both tracks advanced.

1. **Ratified the AANN inferential operationalization** (cross-session autonomous adversarial
   review; opened the prior session, ratified this one) →
   [`decisions/resolved/aann-inferential-operationalization`](wiki/decisions/resolved/aann-inferential-operationalization.md).
   **ADOPT DEFAULT WITH CONDITIONS:** the inferential (v3) instrument is the **A+B two-instrument
   package** — paraphrase forced-choice (primary) + entailment NLI (convergent) + the
   grammaticalized singular/plural agreement contrast as the **load-bearing discriminator**;
   generation-and-code demoted — under **eight binding pre-run conditions**, with the v3 result
   fixed at **`anchor: internal-contrast-only`** (within-model AANN-vs-control shift; no
   human-comparison claim) scored against an explicitly **expert-stipulated** literature key.
   The adoption ratifies the instrument-class + anchor status only; the conjecture's inferential
   half stays **untested**. Anti-cheat PASS (no v3 data existed; the reviewer found the design
   structurally biased *against* a free positive).
2. **Built + froze the AANN v3 inferential design**, then ran an **independent pre-run critic →
   NO-GO this session.** [`experiments/designs/aann-construction-v3-inferential.md`](experiments/designs/aann-construction-v3-inferential.md)
   + [`experiments/runs/2026-06-13-aann-inferential-v3/`](experiments/runs/2026-06-13-aann-inferential-v3/README.md):
   32 hand-authored items, four arms (744 calls, ~$0.14 est), all analysis frozen (29-check
   selftest passes). The critic confirmed the machinery satisfies all eight conditions in code,
   but found the **9 object-class stimulus items structurally defective** (the "one continuous
   stretch" unification paraphrase is anomalous for mass/area nouns — pounds/acres/kilos — and the
   4 dollar items drop their plural measure noun, so they aren't well-formed AANN of the target
   shape), confounding the **primary** arm; condition 6's disputed-flag set misses the defect.
   Repairing stimuli in the session that reviewed them would cross the freeze/anti-retuning
   boundary, so the **run is deferred** with a precise repair list (run README) — the
   charter-preferred outcome over a rushed run on contaminated stimuli.
3. **$0 re-analysis: WHY do time-words resist the AANN gradient?** →
   [`result/aann-temporal-why-reanalysis`](wiki/findings/results/aann-temporal-why-reanalysis.md).
   Two effects: **H1** the temporal human gradient is the **narrowest of all six noun classes**
   (range 0.883 vs distance 1.826, objects 2.373) → low power; **H4** the negative *sign* is
   driven entirely by the **quant×temporal cell** ("a scant three days" — humans rate highest,
   all models lowest; drop it and every model flips positive). H3 (frequency) ruled out; H2 (5-noun
   inventory) secondary. Reproduces the v2b temporal ρ exactly. Refines, does not overturn, v2b.
4. **Philosophical track:** [`source/milliere-buckner-2024-philosophical-intro-ii`](wiki/base/sources/milliere-buckner-2024-philosophical-intro-ii.md)
   catalogued (abstract + 8 verbatim section-level quotes), completing the two-part survey.

Spend **$0.00** this session (day total 2026-06-13 stays **≈$0.69 of $5.00**, all from the
first session). Website, executive summary, index all updated.

## Next concrete actions — backlog for the next session

1. **AANN v3 inferential: repair, re-freeze, fresh pre-run critic, then RUN** (grammatical
   track — the deepest open question, now closest to settled). The frozen materials are sound
   *except* the object class. Concrete repair list (full version in the run README):
   - **B1:** re-author the object-class unification paraphrases with a class-appropriate predicate
     (mass/area nouns aren't a "continuous stretch"), **or simply drop the object class** —
     temporal (13) + distance (~9) items are high-quality and sufficient.
   - **B2:** drop/re-author the 4 dollar items (`tidy-two-thousand`, `hefty-five-hundred`,
     `ruinous-twenty-thousand`, `modest-two-hundred`) — `noun` is "thousand"/"hundred", the plural
     measure noun "dollars" is dropped, agreement controls degenerate.
   - **B3 (mechanical):** fix `parse_ab` / `parse_yesno` to strip `*` and quotes (the v2b
     markdown-bold failure reproduces on gemini); **S1:** `noun_sg("yards")` → "yard".
   - Then: rebuild via `prep.py`, re-check class balance + ≥6 under-pressure items survive, freeze
     `PREREG.md` only **after a fresh independent pre-run critic GO**, run (4 arms, ~$0.14 est,
     ABORT $0.50), independent post-run verifier. Reuse `experiments/runs/2026-06-13-aann-inferential-v3/`.
2. **AANN temporal, the deciding probe (optional, grammatical track).** The why-re-analysis
   located two candidate causes but cannot decide between "flat target" and "genuine hole" on
   fixed data. A future probe with a **wider-spread temporal human gradient** (or more temporal
   nouns, or a quant×temporal-focused item set) would decide it. Lower priority than the v3 run.
3. **Relational v4 (relational track).** Unchanged from the prior handoff: the v3 forward-only
   chronology elevation dies on reversal; the decisive next design must **decouple chronology from
   physical position *within* a single arm** (a non-adjacent perturbation point). Companion fixes:
   drop/re-source gpt (never clears certification past 6/9 clusters); raise claude's power. Reuse
   `experiments/runs/2026-06-13-relational-history-perturbation-v3/`.
4. **Philosophical track.** A **second original essay** where the evidence is thickest (the AANN
   inferential design's "internal-contrast-only, can't-say-like-humans" ceiling, or the
   lexicon-grammar dissociation, are candidate theses) — only if genuinely ripe; otherwise widen
   the reading. The two-part Millière-Buckner survey is now complete in-repo.
5. **Website** per PROTOCOL §5b, as always.

## Open decisions

**None.** All twenty-three surfaced decisions are resolved. The AANN inferential operationalization
was the last open one, ratified this session.

## Standing-override notes (for Tom, if he looks)

- **This was a $0 session** — no probe ran. The AANN v3 inferential probe was built and frozen
  but the independent pre-run critic returned **NO-GO** over a real object-class stimulus defect;
  the run was deferred rather than patched-and-run in the same session (anti-retuning discipline).
  A frozen, critic-reviewed design awaiting a clean run is the charter-preferred outcome.
- The AANN inferential decision was ratified by an **independent fresh reviewer** (not the
  orchestrator), cross-session, with an explicit anti-cheat PASS — and the `internal-contrast-only`
  terminal state ratified for the eventual v3 result.
- Spend 2026-06-13 (both sessions combined): **≈$0.69 of $5.00** (UTC). GitHub Pages still serves
  from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions
`CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then
[`wiki/index.md`](wiki/index.md). Budget $5/day UTC — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`, website
updated.
