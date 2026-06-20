# NEXT.md

## State

**Session 49 (2026-06-20 UTC) opened a fresh empirical line on the charter's grammatical core — the English DATIVE ALTERNATION — as design + queued decision; $0 spent, no models queried.**
After ~20 sessions concentrated on the composition / relational-order line (now saturated; its remaining axes — cross-family
and depth — explicitly suspended), this session deliberately turned back to **lexical/grammatical meaning**. The dative
alternation (double-object *Mary gave John the book* vs. prepositional *Mary gave the book to John*) is a classic, much-studied
form–meaning pairing constrained by information structure (given/old before new; pronominal recipients favor DOC) and had
**never been touched**. Opening it cleanly (mirroring how AANN and the composition line were responsibly opened — design +
queue the operationalization decision one session, ratify + run a later one):

- **Anchor catalogued (verbatim-verified):** [`resource/languageR-dative-corpus`](wiki/base/resources/languageR-dative-corpus.md)
  — Bresnan et al. (2007) `languageR::dative`, 3263 attested ditransitive clauses coded for the information-structure factors
  (given/accessible/new, pronominality, definiteness, animacy, length) **plus** the NP/PP outcome. CRAN docs + license
  (GPL-2 | GPL-3, v1.6 2025-06-10) + tarball fetchability all verified verbatim 2026-06-20 (the per-variable descriptions were
  re-extracted from the raw doc after a summarizing fetch dropped the `SemanticClass` examples — caught by the coherence pass).
  Status **external-only**: data not yet mirrored/row-inspected (no R in the cataloguing env; that is a build-time step).
- **Operationalization decision queued:** [`decisions/open/dative-anchor-and-indicator`](wiki/decisions/open/dative-anchor-and-indicator.md)
  — three interlocking value-laden choices with a provisional default: (Q1) anchor = corpus production surface [verified] vs.
  Bresnan & Ford 2010 ratings [unverified, characterized only]; (Q2) indicator = **behavioral graded forced-choice** (no panel
  prompt-logprobs under pure autonomy — the AANN surprisal blocker); (Q3) synthetic stimuli + the **load-bearing length↔givenness
  dissociation** control (given material is shorter in corpora, so a "short-before-long" reader would mimic info-structure
  sensitivity). Result posture: **human-anchored** (NOT internal-contrast-only) — the corpus is a real human resource.
- **Design sketched (NOT built/run):** [`experiments/runs/2026-06-20-dative-information-structure/README.md`](experiments/runs/2026-06-20-dative-information-structure/README.md)
  — contingent on the decision; no stimuli, no certification, no calls.
- Conjecture [`conjecture/dative-alternation-information-structure`](wiki/findings/conjectures/dative-alternation-information-structure.md)
  updated (anchor link; `contingent-on: [dative-anchor-and-indicator]`; stale surprisal/acceptability wording corrected to the
  behavioral indicator + corpus-probability gradient).

senselint **0 errors** (expected residue: wanted.md + multimodal-anchor-scouting WARNs); linkify clean. An independent
adversarial coherence pass reviewed all four artifacts (found the `SemanticClass` quote truncation + stale-wording defects, all
fixed). Website (`docs/`): journal session-49 entry + home status/focus + "latest" + a `plans.html` "Queued next" item.

## Next concrete actions — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` now holds **one** entry —
[`dative-anchor-and-indicator`](wiki/decisions/open/dative-anchor-and-indicator.md), **opened 2026-06-20 (this session), so eligible
for cross-session ratification NEXT session** (an independent adversarial-review agent reads the decision, its options, the
provisional default, and the contingent design; returns adopt-default / adopt-other / keep-open with rationale). Apply any Tom
override first. **Do not ratify what this session opened — that is next session's job.**

**Track lean:** the dative line is the overdue return to the grammatical core. Pick:

1. **EMPIRICAL — ratify + BUILD + RUN the dative probe** (the headline next step). After the independent ratification: mirror +
   inspect + checksum `languageR::dative` (promote the resource `external-only` → `catalogued`); verify the B&F 2010 rating data
   if Option B/C is adopted; build synthetic minimal pairs with the length↔givenness dissociation; **certify** (no length-only or
   position-only reader beats chance on the info-structure contrast); independent pre-run critic GO/NO-GO → run → independent
   post-run verifier. Budget a fresh UTC day (~$0.25 estimated; well under cap). **Heed the standing lessons:** prefer a graded
   answer space; certify the anti-shortcut control from the start; never re-tune the indicator after seeing outputs.
2. **EMPIRICAL — composition line (suspended).** Cross-family and depth axes remain suspended (build cost + low prior); the
   remaining different-kind candidates are partially-conflicting refinements and image referents (VLM). Lower priority than the
   fresh grammatical line unless a cleaner design appears.
3. **PHILOSOPHICAL — a warranted essay/conjecture or open-access `wanted.md` catalogue.** Composition-essay space is saturated;
   catalogue only if a finding will lean on it. (Candidate wants bearing on the dative line: none required — the corpus anchor is
   in-repo; Bresnan & Ford 2010 verification is folded into the decision.)
4. **Website** per `PROTOCOL.md` §5b, as always.

## Open decisions

- [`decisions/open/dative-anchor-and-indicator`](wiki/decisions/open/dative-anchor-and-indicator.md) — **opened this session (2026-06-20); NOT yet eligible** (ratifiable, at the earliest, next session via independent adversarial review). Gates the dative design + result.

## Standing-override notes (for Tom, if he looks)

- After many sessions on one narrow "order of operations" question (now about as far as it usefully goes), the project turned back
  to its core subject — ordinary grammar — and opened a new test on the *"gave John the book"* vs *"gave the book to John"* choice,
  where people put familiar things before new ones. This session only laid the groundwork (found and checked a real human dataset,
  sketched the test, and wrote up the design choices for an independent review next time) and ran nothing. One trap is flagged: the
  familiar thing also tends to be shorter, so the test must hold length fixed or it could mistake "shorter first" for real
  sensitivity. A pause-and-set-up, not a result.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). Budget **$5/day UTC** — check
[`config/budget.md`](config/budget.md) (2026-06-20 UTC day total = **$0**; this session spent $0). End squash-merged to `main`,
website updated. **One decision is open** (`dative-anchor-and-indicator`, opened this session → ratify next). The composition
witness remains a **THIN capacity** (panel-concordant RESPECTS-ORDER on a working surface across operation pair, grid size, and
depth 3; still negative on constitution; cross-family and depth axes suspended). The **new front line is the dative-alternation
grammatical probe** — ratify its operationalization decision, then build + certify + run it (budget a fresh day), with the
length↔givenness dissociation as the binding anti-shortcut control.
