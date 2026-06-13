# NEXT.md

## State

**Session 2 of the autonomous era (third June-12 session) is landed.** Three things changed.
(1) **Tom's standing instruction applied first**: the public site now carries
`noindex/nofollow/noai` meta tags on all six pages plus `docs/robots.txt` (see the
standing-override note below for the domain-root caveat). (2) **The AANN line ran end-to-end in
one session**: the second autonomous ratification round adopted the behavioral instrument
([`decisions/resolved/aann-behavioral-operationalization`](wiki/decisions/resolved/aann-behavioral-operationalization.md),
nine binding conditions) → Mahowald repo mirrored/verified (MIT) → frozen v2 design + PREREG →
independent pre-run critic (added the decisive noun-class guard) → probe (1,782 calls, 0
missing, $0.3125) → independent post-run verifier (0 mismatches) →
[`result/aann-behavioral-gradient-v2`](wiki/findings/results/aann-behavioral-gradient-v2.md):
**SUPPORTED** — all 3 models track the human Exp-2 gradient (cell ρ 0.68–0.75) and replicate it
on frequency-matched held-out adjectives (0.75–0.83; temporal stratum does NOT replicate —
caveat 2). [`conjecture/aann-construction`](wiki/findings/conjectures/aann-construction.md) is
`tested`; the **inferential half is untested**. (3) **Philosophical track**: Schuele 2025
catalogued (first in-repo "sense-without-reference" argument); **Brennan & Clark 1996 fetched
and verified** → essay trigger c-ii exercised:
[`essay/aggregation-not-constitution`](wiki/findings/essays/aggregation-not-constitution.md)
(now `revised`) and [`conjecture/commutative-convention`](wiki/findings/conjectures/commutative-convention.md)
human-contrast clauses corrected — the source grounds partner-specificity/historicity, **not**
order-sensitivity ("frequency over recency"). Spend 2026-06-12 (both sessions): **$0.60** of
$5.00. Website updated (journal, home, findings, plans, glossary + 2 new entries, footers).

## Next concrete actions — backlog for the next session

1. **AANN v3 — the inferential arm (grammatical track's priority).** The v2 result is
   gradient-tracking only; the conjecture's distinctive *meaning* clause (unification +
   evaluation: does the model draw the "unified, evaluated stretch" paraphrase/inferences?)
   is untested. The indicator choice is a value-laden operationalization call → **open a
   `wiki/decisions/open/` page first** (options: paraphrase forced-choice vs entailment-style
   NLI vs generation-and-code; provisional default + anchor question — Mahowald's ratings do
   NOT anchor an inference measure), ratifiable the following session. Cheap companion fix in
   the same unit: widen the **temporal held-out cells** (v2 caveat 2 — the one stratum that
   failed to replicate; 4 cells was too thin to read).
2. **Relational v3 (relational track).** Unchanged from last handoff: the perturbation
   follow-up with the verifier's fix-list (truncation-proof single-token elicitation;
   re-certified gpt stimuli; more clusters; pre-registered minimum-cluster guard). The essay's
   corrected human-contrast clause adds a reason to run it: the human side no longer presumes
   non-commutativity, so the LLM-side answer carries more of the contrast's weight.
3. **Philosophical track.** Catalogue Millière & Buckner 2024 (arXiv 2401.03910, the two-part
   philosophical survey — the strongest remaining queued source). A second essay only if ripe;
   one live candidate thesis: what the Brennan-Clark correction does to the
   aggregation-vs-constitution bet (the human pole of "non-commutative" is now an open
   empirical question, not an anchor).
4. **Website** per PROTOCOL §5b, as always.

## Open decisions

- **None.** All twenty-two surfaced decisions are resolved. (Item 1 above will open a new one.)

## Standing-override notes (for Tom, if he looks)

- **Your robots/no-scraping instruction is applied** (first action of the session): all six
  `docs/` pages carry `<meta name="robots" content="noindex, nofollow, noarchive, nosnippet,
  noimageindex, noai, noimageai">`, and `docs/robots.txt` disallows all crawlers plus ~20 named
  AI bots. One honest technical caveat: GitHub Pages serves this site under a path prefix
  (`…github.io/ai-semantics/`), and crawlers only read robots.txt at the **domain root** — so
  the meta tags are the binding mechanism; the robots.txt is belt-and-braces. If you want a
  root-level robots.txt too, that requires a `tkgally.github.io` user-site repo (your call —
  outside this repo's reach).
- The second autonomous ratification round ran (AANN instrument, adversarial review, rationale
  on the resolved page); the probe ran the same session — permitted because the decision was
  opened in an *earlier* session (same sequencing as the relational v2 precedent).
- GitHub Pages serves from `main` `/docs` (unchanged).

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions
`CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then
[`wiki/index.md`](wiki/index.md). Budget $5/day UTC — check today's ledger rows in
[`config/budget.md`](config/budget.md) before any probe. End squash-merged to `main`, website
updated.
