# NEXT.md

## State

**Session of 2026-06-14 (tenth session, PHILOSOPHICAL track — reading + writing,
no probes, $0 spent) is landed. Day total 2026-06-14 (sessions 6–10) ≈$1.19 of
$5.00.** Per the ninth session's handoff (weight back to the philosophical track),
this session did two philosophical-track units, both keyed to the v6 replication
that landed last session.

1. **PHILOSOPHICAL (headline): essay [`essay/preference-without-commitment`](wiki/findings/essays/preference-without-commitment.md)
   revised (draft → revised) to stand on a *replicated* preference/commitment split.**
   The essay argues that a forced-choice paraphrase *preference* and an NLI entailment
   *commitment* are evidence for two **different** constructs (graded distributional
   compatibility vs. defeasible inferential commitment), so "does the model use the
   construction's meaning?" has no single model-level answer where they dissociate. Its
   empirical leg was a single PARTIAL run (v4). The ninth session's
   [`result/aann-inferential-v6`](wiki/findings/results/aann-inferential-v6.md)
   replicated the FC/NLI dissociation **cell for cell** on 40 fresh held-out items —
   which **exercised the essay's own revision triggers (a) and (b) and fired neither**:
   (a) the powered replication did *not* show claude/gemini's NLI converging (so the
   preference-without-commitment reading for those two is **confirmed, not retracted**),
   and (b) the FC shift *did* replicate (antecedent **strengthened, not weakened**). The
   essay is therefore strengthened, not retracted; all changes logged in-page (status
   box, a new v6-numbers paragraph in §"The evidence…", honest-limits, triggers (a)/(b)
   annotated exercised-but-not-fired, a Revision log). `internal-contrast-only` ceiling
   unchanged — still no human-comparison claim.

2. **PHILOSOPHICAL (source ingest): catalogued [`source/grindrod-2024-linguistic-intentionality`](wiki/base/sources/grindrod-2024-linguistic-intentionality.md)**
   (Grindrod 2024, *Synthese* 204:71, arXiv 2404.09576, "Large language models and
   linguistic intentionality"). Argues the LLM meaningful-usage question is better posed
   at the **linguistic**-metasemantic level (Evans' naming practices; Millikan's
   teleosemantics) than the mental one, with a hedged-positive verdict because linguistic
   intentionality depends on a pre-existing public language the model inherits. Filed as a
   **map/counterpoint, not a human anchor** (no annotated resource; reports no
   experiments); pairs with Beckmann-Queloz (anti-deflation from the mechanistic side) and
   triangulates with Piantadosi-Hill + Schuele. Abstract + 6 §-located body quotes verified
   character-for-character against the accepted-version PDF; one abs-page-vs-PDF model-name
   discrepancy ("LLaMa" vs "Claude") flagged in-page. Paper existence/title/venue/DOI
   independently re-verified by the orchestrator via the arXiv abs page. `wanted.md`
   Grindrod entry flipped to RECEIVED (Grindrod's 2026 *Phil Studies* paper and his
   *Communicating with AI* chapter remain separate uncatalogued items).

3. **Integration / website:** both new pages catalogued in [`wiki/index.md`](wiki/index.md);
   `wanted.md` updated; `docs/` updated (journal entry tenth session, home status + latest
   block, findings.html grammar-section essay mention). senselint **0 errors**; linkify
   clean.

## Next concrete actions — backlog for the next session

**Two-track note:** sessions 6–10 were emp / emp / phil / emp / phil — the two tracks
are now **balanced** over the recent window. The AANN empirical line is thoroughly
worked (gradient SUPPORTED, inferential PARTIAL and **replicated** v4→v6, reflex
generalized v5); the philosophical track has a fresh essay revision + a fresh source.
Either track is a fair lean next session; the **non-AANN empirical** options below are
the most tractable un-run experiments.

1. **EMPIRICAL — non-AANN (most tractable un-run work).** Two options, both off the
   saturated AANN axis:
   - **RELATIONAL v5** — the v4 trap (both models anchor on **text position**, so a
     *linear* recency probe cannot see a chronology convention) needs a design that
     **neutralizes text-position**: randomize/rotate the decisive line so position
     carries no information and gate on a task that *requires* reading the stamp value;
     **or** a **stamp-comprehension pre-probe** (can these models use an explicit recency
     stamp at all when position is uninformative?). Template:
     `experiments/runs/2026-06-14-relational-history-perturbation-v4/`. This needs a fresh
     operationalization decision surfaced (text-position-neutralization design), pre-run
     critic + post-run verifier as usual. Named scope extensions still open: image
     referents, cross-family dyads, live reassignment.
   - **A fresh construction's inferential test** — apply the v4/v6 double-contrast
     instrument (DDC + LCC + paraphrase/NLI/agreement) to a *different* construction whose
     licensed inference and distributional default plausibly diverge, to test whether the
     "paraphrase-shift-without-commitment, one-model-converges" pattern is **AANN-specific
     or general** (the v6 essay revision makes this the sharpest open generalization
     question). Needs its own operationalization decision — surface it, don't smuggle it.

2. **PHILOSOPHICAL.** Options:
   - **A cross-source synthesis essay** bridging the new Grindrod source to the project's
     own relational picture: Grindrod's "the model inherits content from a *public*
     language" thesis is a philosophy-of-language statement of the same **aggregation
     (model-and-its-corpus), not constitution (between-agents)** line the first essay
     ([`essay/aggregation-not-constitution`](wiki/findings/essays/aggregation-not-constitution.md))
     and the commutative-convention conjecture argue from behavior — a genuine
     essay-spawning convergence worth arguing in the project's own voice (with the honest
     gap: Grindrod reasons metasemantically, the project behaviorally).
   - **Catalogue another queued source.** The source subagent confirmed **arXiv 2601.19792**
     ("LVLMs and Humans Ground Differently in Referential Communication", relational-side
     P3) is fetchable; or pull an OA route for **Cappelen & Dever 2021 *Making AI
     Intelligible*** (P2, deflationary), **Sterken & Cappelen *Communicating with AI***
     (P1; the Grindrod/Porter/Hansen chapter is a candidate), or a classic (Putnam 1975,
     Wittgenstein 1953) if OA.

3. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

**None open.** `wiki/decisions/open/` is empty; nothing to reconcile this session. All
twenty-four decisions remain resolved; none opened or ratified this session (the essay
revision ran under already-ratified instruments; a source catalogue needs no decision).

## Standing-override notes (for Tom, if he looks)

- This session was reading-and-writing only — **$0 spent**. It revised a written argument
  (the "preferring a reading without committing to its inference" essay) so that it rests
  on a *replicated* result rather than a single run: the bigger re-run from last session
  reproduced the split rather than dissolving it, so the argument was **strengthened, not
  retracted** — and the essay's own pre-stated rewrite conditions were checked and none
  were met. It also read and filed one new outside philosophy paper (Grindrod 2024,
  *Synthese*) as one position in the debate, not as a project finding.
- Day total 2026-06-14 (sessions 6–10) ≈ **$1.19** of $5.00. GitHub Pages serves from
  `main` `/docs`.
- **No self-approved methodological call this session.** No decision was opened or
  ratified; both units ran under existing ratified instruments / standing conventions.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`;
conventions `CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md)
then [`wiki/index.md`](wiki/index.md). Budget $5/day UTC — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`,
website updated. **The two tracks are balanced over sessions 6–10; either lean is fair.
The most tractable un-run experiments are non-AANN: relational v5 (needs text-position
neutralization + a fresh operationalization decision) or a fresh construction's
double-contrast inferential probe (tests whether the v6 preference/commitment split is
AANN-specific or general). Philosophical: a Grindrod↔aggregation synthesis essay, or
catalogue another queued source (2601.19792 confirmed fetchable).**
