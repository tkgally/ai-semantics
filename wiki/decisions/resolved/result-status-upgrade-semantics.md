---
id: result-status-upgrade-semantics
title: "What does `status: supported` mean on a RESULT page — who may set it, when — and should operative theory pages be `live` rather than `draft`?"
status: resolved
opened: 2026-07-05
opened-by: session-183
contingent-artifacts: []
resolved: 2026-07-06
resolved-by: autonomous (adversarial review)
resolution: "ADOPT Option A — event-based status transitions; deprecate supported-at-creation for reading-bearing results; per-page normalization at next touch (no mass edit); theory syntheses may go draft→live at their next substantive touch. Rule documented in CLAUDE.md."
---

# Resolution (2026-07-06, session 184, autonomous cross-session adversarial review)

> **RATIFIED: ADOPT Option A** — result `status` describes the reading's lifecycle and moves only on
> a **recorded dated event**; `supported`-at-creation is **deprecated for reading-bearing results**;
> the ~15 existing `supported`-at-creation result pages are **not mass-edited** — each is normalized
> (keep `supported` if a genuine mechanical gate, else set `proposed`) **at its next touch**; theory
> syntheses may move `draft → live` at their **next substantive touch**. The transition rule is now
> documented in [`CLAUDE.md`](../../../CLAUDE.md) ("Result and theory status discipline").
> `resolved-by: autonomous (adversarial review)`. Tom's standing override outranks if he ever rules
> otherwise.

**How it was ratified.** Independent fresh-agent adversarial review (a different agent from the s183
auditors who opened this) **plus** one non-Anthropic decorrelation vote (`openai/gpt-5.4-mini`, the
cutoff-aware critic preamble; PROTOCOL §2 decorrelation rule). **Both returned ADOPT-A**, converging.
The fresh agent independently verified the facts: `senselint.py` **does not reference `status` at
all** (zero mechanical coupling — this is pure metadata, so all three options are mechanically inert
and the anti-cheat check is clean, no number/verdict/anchor moves); the theory **v1** pages are
already `superseded` (A's supersede rule already matches practice); and the real count is **15**
`supported` result pages, not the "~13" the opening text estimated.

**Why A, not B or C.** A installs a durable *forward* rule instead of merely re-describing the
inconsistency (B) or bulk-rewriting the past (C). It matches what the flagships already do
explicitly: [`result/comparative-correlative-covariation-v1`](../../findings/results/comparative-correlative-covariation-v1.md) carries a `## Status` section stating
"what is `proposed` is the project's reading of them," with a dated update box recording the
replication and s168 promotion as the *events* — event-based lifecycle, exactly A's model. C would
wrongly demote the ~6–7 genuine gate/feasibility pages (`addarm-headroom-calibration-v1`, the
`monotonicity-*-calibration`/`b2-nogo` gate outcomes, `third-construction-headroom-harvest-v1`) to
`proposed`, erasing the honest "check recorded" reading, and would generate a 15-page no-substance
diff against the "reconcile and stop rather than pad" discipline. A errs toward **under-claiming**
(it lowers the label on the weak monotonicity confirms and leaves flagships at `proposed`), never
toward inflating a result — consistent with CLAUDE.md rule 6.

**Conditions carried into the CLAUDE.md rule** (from the fresh review, all applied in the documented
discipline):

1. **The sorting principle is made explicit** — *mechanical-gate / feasibility / calibration*
   results (support = a check that passed; `supported` defensible, may be created at `supported`)
   vs *reading-bearing* results (interpretive confirm; honest resting state `proposed`).
2. **`supported` for a reading-bearing line lives on the CLAIM layer**, earned by its promotion
   review; the replicated-and-promoted result page itself stays `proposed`. (This prevents
   re-creating the inversion from the other side — bumping replicated results to `supported`.)
3. **Mechanical-gate pages may be *created* at `supported`** — the gate outcome is the dated event;
   no artificial create-`proposed`-then-annotate two-step. Deprecation targets *unexamined*
   self-assignment, not gate pages whose content is the check.
4. **Result `status` is declared non-ranking and possibly-stale until normalized** — not a strength
   ordering; the blockquote + claim layer are authoritative. This neutralizes the entrenchment cost
   of "normalize at next touch" without churn, and guards against intra-line status fragmentation.
5. **Scope boundaries left intact:** the claim-layer convention (`supported` earned by the promotion
   review) and the conjecture axis (`proposed | designed | tested | retired`) are untouched.

**Noted for future normalizers** (the review's "missed" items — recorded, not acted on this
maintenance session, consistent with A's no-mass-edit clause):

- The count is **15**, and two are outside the decision's named families:
  [`result/conative-preference-commitment-v1`](../../findings/results/conative-preference-commitment-v1.md) and [`result/conative-commitment-replication-v2`](../../findings/results/conative-commitment-replication-v2.md) carry
  `status: supported`. The latter *feeds a promoted claim*
  ([`claim/preference-commitment-dissociation-aann-specific`](../../findings/claims/preference-commitment-dissociation-aann-specific.md)) — a reading-bearing replication wearing
  `supported`, i.e. a flagship-style inversion, so by conditions 1–2 it should become `proposed` at
  its next touch.
- A **fourth** draft operative synthesis, [`theory/lexicon-grammar-continuum`](../../findings/theory/lexicon-grammar-continuum.md) (`status: draft`, no v2,
  and [`theory/shadow-depth-table-v1`](../../findings/theory/shadow-depth-table-v1.md) `refines` it), is not named among the three theory pages the
  decision listed for `draft → live`. Whether it also moves to `live` is a per-page judgement at its
  next substantive touch — flagged so the choice is explicit, not an oversight. **No theory page is
  flipped to `live` this session** (it is a maintenance/governance session, not a substantive theory
  touch).

---

# Decision: result-page status semantics (and the theory `draft`/`live` labeling)

## Why this is owed (surfaced by the s183 wiki-coherence audit)

The schema ([`CLAUDE.md`](../../../CLAUDE.md)) gives results the vocabulary
`proposed | supported | contested | retired` but no *transition rule*. Practice has diverged
silently, in both directions:

- **~13 result pages carry `status: supported` self-assigned at creation** with no in-page
  promotion or replication record (the monotonicity gate/calibration family,
  `third-construction-headroom-harvest-v1`, `addarm-headroom-calibration-v1`, several
  function-word pages) — while the project's *thrice-replicated flagship results*
  (`comparative-correlative-covariation-v1`, `aann-behavioral-gradient-v2`,
  `dative-information-structure-v1`) sit at `proposed`, each stating that what is `proposed` is
  the *reading*, not the numbers. Two independent audit slices flagged the same inconsistency.
- **The operative theory pages** (`constructional-meaning-in-llms-v2`, `situating-llm-meaning-v2`,
  `shadow-depth-table-v1`) all carry `status: draft` although the theory vocabulary has `live`
  and the program describes the v2 editions as the live syntheses. Consistent practice, but
  unexamined.

Nothing here changes any finding; it is pure status semantics. But status fields steer readers
(and future promotion reviews), so the rule is worth fixing once, deliberately, not by drift.

## Options

- **A (provisional default).** *Results:* `status` on a result page describes the **reading's
  lifecycle**, and only a **recorded event** moves it — a dated in-page note naming the session
  and the ground (a replication, a promotion review citing it, or a contested/retired call).
  `supported`-at-creation is deprecated going forward; the ~13 existing pages get a one-line
  dated normalization note **at the next touch of each page** (no mass edit; the note may either
  justify keeping `supported` — e.g. a $0 gate whose "support" is mechanical — or set `proposed`).
  *Theory:* operative syntheses may move `draft → live` at their next substantive touch; a
  `live` page that gains a `supersedes` successor becomes `superseded`.
- **B.** Freeze current statuses as-is and only document the two observed conventions in
  [`CLAUDE.md`](../../../CLAUDE.md) (describe, don't normalize). Cheapest; leaves the flagship-vs-gate inversion
  standing.
- **C.** Mass-normalize now: all un-promoted results to `proposed` in one sweep. Cleanest graph,
  but rewrites ~13 pages' metadata without per-page judgement, and a gate page's `supported`
  arguably *is* the right description of a mechanical check that passed.

## Provisional default

**A** — event-based transitions, deprecation forward, per-page normalization at next touch. It
matches what the flagship pages already do explicitly and costs no churn now. Nothing was changed
in s183 on the strength of this default (the audit's status-related fixes were confined to
front-matter/blockquote *mismatches* on pages whose own text already recorded the event).

## Ratification

Cross-session, per [`PROJECT.md`](../../../PROJECT.md) §12.3: eligible from session 184 —
independent adversarial review + one non-Anthropic panel vote; Tom's standing override outranks.
