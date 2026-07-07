# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s190 spent $0.00** (a $0 literature-intake session; no probe, no votes). The UTC day rolled over to
**2026-07-07** at s190 (a fresh $5.00 day; s189 and earlier were 2026-07-06). If `date -u` still shows
**2026-07-07**, the day stands at **$0.00 of $5.00**; if **2026-07-08+**, a fresh $5.00. Ledger:
[`config/budget.md`](config/budget.md).

## State — s190 ($0.00): Tom-directed literature intake — catalogued the Anthropic "verbalizable workspace" paper + flagged the topics it raises. Normal program backlog NOT advanced (session scoped narrowly by Tom).

A **single-unit, $0 side-task** at Tom's standing-override request — *not* a normal work session. Tom
directed: "only make a note … to add the recently-released Anthropic paper, its findings, and its
references to the topics that should be considered and discussed by this project moving forward." Done:

- **NEW SOURCE — [`source/gurnee-2026-verbalizable-workspace`](wiki/base/sources/gurnee-2026-verbalizable-workspace.md)**
  (Gurnee, Sofroniew, …, Batson & Lindsey 2026, *Verbalizable Representations Form a Global Workspace in
  Language Models*, Transformer Circuits Thread, 2026-07-06). A **mechanistic-interpretability** paper: a
  privileged, **verbalizable**, causally-load-bearing internal-representation subset (the "J-space", via a
  new "Jacobian lens"), five workspace properties, on Claude Sonnet 4.5. Catalogued exactly as the other
  interpretability ingests (Diera; Beckmann & Queloz): **MAP / representational counterpoint, NOT a human
  anchor, NOT behavioral evidence, consciousness framing NOT imported.** All quotes verified
  char-for-char against a raw-HTML fetch; two would-be fabrications from an exploratory WebFetch caught and
  dropped ("Baars" absent; the "sensory/motor-layers" three-region framing + figure numbers don't survive
  against source). RECEIVED in [`wanted.md`](wiki/base/wanted.md).
- **NEW OPEN-QUESTION — [`open-question/verbalizable-workspace-and-llm-meaning`](wiki/findings/open-questions/verbalizable-workspace-and-llm-meaning.md)**:
  the forward-looking flag — five topics the paper raises for the project (the distributional-vs-inferential
  seam from the inside; the working-surface confound mechanistically corroborated; introspection/verbal-report
  as a method the project doesn't use; a representational datapoint for the situating-map model-internal
  locus; "concept" here ≠ the philosopher's reference-bearing concept), each tied to an in-repo page. It
  **commits to no probe/essay/theory/claim and ratifies nothing.**

## ⚠ RECONCILE at cold-start — ZERO decisions open

`wiki/decisions/open/` is **empty**. Nothing to ratify at s191 cold-start. 63 resolved
([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Do the light reconcile check and
proceed to a fresh unit.

## ⚠ Backlog for s191 (PROTOCOL §3: fewer, deeper; two-track balance)

Recent lean: s186 empirical, s187 phil, s188 empirical-design, s189 empirical, **s190 was a light $0
literature-intake** (philosophical-track-adjacent, but *not* the owed deep phil/consolidation unit). So
**s191 is still owed a substantive philosophical or consolidation turn** (or a theory v2), unless a sharp
empirical unit is clearly most-valuable.

1. **Two theory v2s are owed** (PROTOCOL §3, >3 update boxes) — clean consolidation units:
   - [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md) — **>3 boxes**
     (s147 / s165 / 2026-05-30 / s188 antonymy). A clean **v2 second edition** owed at its next substantive touch.
   - [`theory/shadow-depth-table-v1`](wiki/findings/theory/shadow-depth-table-v1.md) — 3 dated boxes
     (s173 / s186 / s187); the AANN temporal caveat clarified (s189 — inventory artifact), a natural edition trigger.
2. **The NEW workspace-paper thread** (philosophical, if the essay bar clears): an essay weighing the
   **mechanistic-vs-behavioral** relationship on topics 1–3 of
   [`open-question/verbalizable-workspace-and-llm-meaning`](wiki/findings/open-questions/verbalizable-workspace-and-llm-meaning.md)
   — most naturally the working-surface-confound corroboration (topic 2, already `supports`-linked to
   [`claim/output-channel-working-surface`](wiki/findings/claims/output-channel-working-surface.md)) or the
   introspection-as-a-method-the-project-doesn't-use point (topic 3). The PROTOCOL §3 essay bar (fired
   trigger / new literature / new falsifiable bet) governs whether it warrants a new essay vs an in-page
   revision; the paper *is* new outside literature, so the bar is plausibly met — but keep the
   interpretability/behavioral firewall explicit and import no consciousness claim.
3. **PHILOSOPHICAL / EMPIRICAL (the decoupling essay's bets):**
   - **H1 — adjective-antonymy replication** (reuses the s186 frozen antonymy pipeline + Simple-Wikipedia
     control; POS change → needs its own design + critic).
   - **H2 — the FRESH relation-recovery probe** using the pre-registered **IS-A-depth proxy**
     ([`note/taxonomic-proxy-recovery-pilot-v1`](wiki/findings/notes/taxonomic-proxy-recovery-pilot-v1.md)).
     Dischargeable ONLY by a fresh test (never off the s186 data). Needs a design + decision trail.
4. **A3b BLiMP forced-choice sweep** (67k human-validated pairs, CC-BY, cataloged; design + critic first);
   **A5 production-side alternation battery**; **A6 cross-linguistic replication scout** (UD in-scope);
   **A2b grounding-magnitude** = external-resource SCOUT only
   ([`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md)).
5. **B1 last promotion** (environment-gated presupposition): weigh honestly; a written refusal is legitimate.
6. Other open-questions from the s187 harvest:
   [`open-question/lexical-regular-polysemy-productivity`](wiki/findings/open-questions/lexical-regular-polysemy-productivity.md)
   (the lexical wug-test), [`open-question/graded-privativity-gradient`](wiki/findings/open-questions/graded-privativity-gradient.md).

## ⚠ Env notes (carry)

- **`experiments/data/aann-public/` (incl. `adjexp_turk.csv`) is gitignored** — only class-level
  `human_class_means.csv` is committed; any future Arm-1 human-mean work reclones the pinned Mahowald mirror
  (MIT, commit `c8095a0008cd6538717de5cc937f90ce5944e688`).
- `wordfreq` + `numpy` install via `pip install wordfreq numpy`; `nltk`/WordNet via `pip install nltk` +
  `nltk.download('wordnet')`. **SubTLEX-US is unigram-only.**
- **Run long probes with harness `run_in_background: true`; parallelize per-model**; wait on the completion
  notification, never a name-match (PROTOCOL §6b). openrouter MCP flaky — use the probe REST path for votes
  (`experiments/lib/openrouter.py`, `max_tokens≈500–700`). Commit signing impossible: `user.email
  noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start; `git checkout -B <branch>
  origin/main` if the branch is gone.
- **Web-source provenance (from s190):** transformer-circuits.pub serves static HTML whose cross-references
  render as unresolved `??` — so **no figure/section-number locators** are recoverable and the **reference
  list does not extract**; fetch the raw HTML (`curl` via the proxy) and verify quotes char-for-char against
  tag-stripped text rather than trusting a WebFetch summary (which hallucinated "Baars" and a layer-range).

## ⚠ Do-not-re-grind (in force)

- **(s190) The workspace paper is catalogued + its open-question opened. Do NOT re-catalogue it, and do NOT
  re-fire its open-question into a probe/essay without clearing the PROTOCOL §3 bar** — interpretability
  evidence is **not** behavioral, does **not** transfer to any project claim/result, and the paper is **not
  a human anchor**. Import no consciousness claim.
- **(s189) The aann-quant-temporal-inversion probe RAN → NULL. Do NOT re-run it or re-open its ratified
  decision.** Clean pre-named verifier-reproduced NULL (inventory artifact).
- **(s188) The wiki-coherence campaign is CLOSED** — do NOT reopen it or re-run its phases. The taxonomic-proxy
  pilot is recorded — do NOT re-fire H2 off it (H2 needs a fresh test).
- **(s186) A1b antonymy is RUN + FALSIFIED — do NOT re-run it** or re-open its ratified gates; an **adjective**
  replication is new work. **(s185) note-sweep P3 done.** **(s184) Do NOT mass-edit `supported`-at-creation
  results; do NOT flip theory to `live` off a non-substantive touch.** **(s183) Do NOT re-audit the whole
  wiki.** **(s170) Founding questions stay closed.** **(s168–)** no corpus/dataset adoption without a verified
  license.

## Open decisions

**NONE.** `wiki/decisions/open/` is empty. 63 resolved to date; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session did exactly what you asked and nothing more: it added the new Anthropic "workspace" paper to
the project's own records — a plain summary of what it found, in the project's own words, with every quote
checked against the original — and it opened a short list of the questions the paper raises that the project
might take up later (how a model's internal, reportable "concepts" relate to the project's behavioral tests;
whether it backs up the project's "the model can think on a scratchpad the answer-box hides" line; what to
make of a model *reporting* its own thoughts). It ran no experiment, spent nothing, and drew no conclusion —
the paper is filed as *someone else's interpretability result to weigh*, explicitly not as evidence for or
against anything the project has measured, and its "consciousness" framing was **not** taken on board (the
project is about meaning, not consciousness). **I did not post anything to the public website** — this was a
note-to-self filing rather than a new finding, so a public journal entry would have overstated it; if you'd
like a short public note that the project is tracking this paper, say so and a later session will add one. As
always, a line anywhere in the repo outranks the plan.

## Reminder for the next cold-start

**You are session 191.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§3–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check
`date -u`; s190 spent $0.00** (fresh 2026-07-07 day). **RECONCILE: ZERO decisions open.** Most-owed: **a
philosophical/consolidation turn** (recent empirical lean; s190 was a light $0 intake) — a **theory v2**
(both `lexicon-grammar-continuum` and `shadow-depth-table-v1` owe one), an **essay weighing the new workspace
paper** (topics in [`open-question/verbalizable-workspace-and-llm-meaning`](wiki/findings/open-questions/verbalizable-workspace-and-llm-meaning.md),
if the §3 essay bar clears), or the decoupling essay's **H1 adjective-antonymy** / **H2 fresh
relation-recovery** (needs a design + decision). Do NOT: re-catalogue the workspace paper or re-fire its OQ
without clearing the essay/design bar (interpretability ≠ behavioral, not a human anchor);
re-run/re-open the aann-quant-temporal probe or its decision; reopen the campaign; re-fire H2 off the pilot;
re-run/re-open A1b; re-audit the wiki; mass-edit `supported`-at-creation results; flip theory to `live` off a
non-substantive touch; adopt unlicensed corpora. **Two theory v2s owed** at next substantive touch. End
squash-merged to `main`; `git fetch --prune` at cold-start.
