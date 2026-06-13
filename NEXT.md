# NEXT.md

## State

**Session of 2026-06-13 (workflow mode, 3 waves) is landed.** Two probes ran end-to-end under
full discipline (independent pre-run critic + frozen PREREG + run + independent post-run
verifier, **0 mismatches each**); one source catalogued; one new decision surfaced. Spend
**≈$0.69 of $5.00** (UTC day). No ratification this session (none was eligible — the only open
decision was opened *this* session).

1. **Relational v3 — the commutativity test, second attempt** →
   [`result/relational-history-perturbation-v3`](wiki/findings/results/relational-history-perturbation-v3.md).
   The v2 verifier's five-item fix-list was implemented and it **worked mechanically** (0
   truncation / 0 NA / 0 retries; strict-compliance 1.000; gemini at full power — gate 0.92, 7/9
   clusters, both trial-floors passed). Verdict **INCONCLUSIVE/MIXED** (gemini, claude); gpt
   **METHODOLOGICAL NULL** (1/6 clusters — stimulus quality still its weak point even after
   certification + one top-up). The clean read (gemini) shows a forward chronology elevation
   (ρ_chron 0.780) that **does not survive direction reversal** — the post-run verifier corrected
   a first-pass over-claim: this is **not** "physical position over chronology" (rev ρ_phys
   collapses to exactly 0.5, refuting that; forward ρ_chron ≡ ρ_phys by construction). Defensible
   claim: the forward elevation is **direction-fragile**. Conjecture stays `proposed`. 384 calls,
   $0.386 billed.
2. **AANN v2b — temporal held-out widening** →
   [`result/aann-temporal-heldout-v2b`](wiki/findings/results/aann-temporal-heldout-v2b.md).
   Widening the temporal held-out stratum 5× (16 → 80 items) under the same ratified v2 instrument
   confirms v2 caveat 2 was real: the temporal stratum is **uniformly negative at every grain**
   for all three models → held-out AANN **productivity is noun-class-dependent**. Refines (does
   not overturn) the v2 SUPPORTED verdict. Fresh Tier-0 passes all 3; framing agrees 0.82–0.94.
   432 calls, $0.0793 billed.
3. **Philosophical track:** [`source/milliere-buckner-2024-philosophical-intro-i`](wiki/base/sources/milliere-buckner-2024-philosophical-intro-i.md)
   catalogued (abstract + 7 verbatim quotes; grounds the grounding / symbol-grounding /
   deflationary / compositionality / inferential / referential concept pages). Part II
   (arXiv 2405.03207) stays in the backlog.
4. **New open decision surfaced** (see below). Website, executive summary, budget ledger all
   updated.

## Next concrete actions — backlog for the next session

1. **Ratify (or keep open) the AANN inferential-arm decision** (eligible this session for the
   first time): [`decisions/open/aann-inferential-operationalization`](wiki/decisions/open/aann-inferential-operationalization.md)
   — run the independent adversarial-review pass on its three indicator options (paraphrase FC /
   NLI / generation-and-code) **and** its anchor sub-question (Mahowald's acceptability ratings
   do not anchor an inference measure; default = internal-contrast-only + a literature-stipulated
   key). Provisional default: A+B two-instrument package, FC primary. If ratified, the AANN v3
   inferential design becomes buildable — the grammatical track's deepest open question (does the
   model *use* the unification/evaluation meaning, not just rate acceptability?).
2. **Relational v4 (relational track).** The v3 open question is now precisely located: a
   forward-only chronology elevation of unknown origin that dies on reversal. The decisive next
   design must **decouple chronology from physical position *within* a single arm** (a
   non-adjacent perturbation point), because the forward arm conflates them by construction and
   the reversed arm lands at chance at this power. Two companion fixes: drop or re-source gpt
   (its descriptions never clear certification past 6/9 clusters), and raise claude's power
   (floor36 unmet at 5/9 clusters). Cross-family (heterogeneous) dyads and image referents remain
   the scope-extension options. Reuse `experiments/runs/2026-06-13-relational-history-perturbation-v3/`
   machinery.
3. **AANN follow-ups (grammatical track), if not doing the inferential arm yet.** The temporal
   productivity hole (v2b) is now a *finding*; a natural question is *why* time-words fail — is it
   the small temporal noun inventory, a frequency artifact, or genuine? A within-class analysis on
   the existing v2 + v2b raw ($0) could scope it before any new spend. Also: the tourish-typo
   template depresses ratings — a typo-free template replication would clean the category boundary.
4. **Philosophical track.** Catalogue **Millière & Buckner 2024 Part II** (arXiv 2405.03207, the
   "new frontiers" half) — the natural completion of the Part-I survey now in repo. A second essay
   only if ripe.
5. **Website** per PROTOCOL §5b, as always.

## Open decisions

- [`decisions/open/aann-inferential-operationalization`](wiki/decisions/open/aann-inferential-operationalization.md)
  — **opened 2026-06-13 (this session); NOT yet eligible — ratifiable next session at the
  earliest** (PROJECT.md §12.3). Indicator + anchor for the AANN meaning-clause probe. Any AANN
  v3 inferential design/run is contingent on it.

## Standing-override notes (for Tom, if he looks)

- No ratification ran this session: the only open decision was opened this session, and a decision
  is never ratifiable in the session that opened it (PROTOCOL §2). It is queued for next session.
- Both probes' verifiers ran clean (0 mismatches). The relational v3 verifier caught and
  corrected an over-claim in the orchestrator's first-pass reading ("position not chronology") —
  the result page and all cross-references carry the corrected, weaker claim.
- Spend 2026-06-13: **$0.69 of $5.00** (UTC). GitHub Pages still serves from `main` `/docs`.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions
`CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then
[`wiki/index.md`](wiki/index.md). Budget $5/day UTC — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`, website
updated.
