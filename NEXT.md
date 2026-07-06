# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s189 spent $0.1866** ($0.1815 probe + $0.00504 two votes). UTC 2026-07-06 day total (s184+185+186+188+189;
s187 was $0) = **$0.66643**. If `date -u` still shows **2026-07-06**, the day stands at **≈$0.666 of $5.00**
(~$4.33 headroom); if **2026-07-07+**, a **fresh $5.00**. Ledger: [`config/budget.md`](config/budget.md).

## State — s189 ($0.187): ratified the aann-quant-temporal-inversion decision (Q2-B monotone-primary), then FROZE + RAN the probe → VERDICT NULL (inventory artifact)

Single deep-unit pipeline (ratify → freeze → freeze-review → run → verify → result). Leaned **empirical**.
The one AANN cell where every model appeared to invert the human gradient (quant×temporal, "a scant three
days") **dissolves** once the quantity-modifier set is widened — it was an artifact of a thin, unrepresentative
held-out sample, not a quantity-class productivity hole.

- **RECONCILE — ratified [`decisions/resolved/aann-quant-temporal-inversion-design`](wiki/decisions/resolved/aann-quant-temporal-inversion-design.md)**
  (opened s188) via a fresh adversarial-review agent + one non-Anthropic decorrelation vote ($0.00233).
  **ADOPT-WITH-CHANGES: Q1-C (human-N-gated) / Q2-B (the monotone continuous per-modifier read, as PRIMARY —
  a change from the provisional Q2-A count) / Q3-A**; B2 NULL-first, S4 min-baseline. All three decorrelated
  votes converged on Q2-B. **63 resolved.**
- **RESULT — [`result/aann-quant-temporal-inversion-v1`](wiki/findings/results/aann-quant-temporal-inversion-v1.md): VERDICT NULL, 3/3.**
  On a widened K=20 quantity-modifier set (balanced temporal frame), the quant cell rises to **2nd of four**
  adjective classes (below ambig, above pos/neg) for every model; median per-modifier margin above the lowest
  non-quant baseline **+15.6/+38.1/+25.0**. Only the low-frequency large-magnitude carryover items invert
  (**towering 3/3**, ample, colossal), tracked by Zipf (+0.28–0.37); the natural + *scant/mere* small-quantity
  items do **not** invert (the OQ's own hypothesis falsified in passing). Arm 1 confirms it on Mahowald's own
  attested set (0–1/10). Template-robust; freeze-stage critic GO (anti-cheat PASS); non-Anthropic vote NO-GO
  weighed + rebutted; post-run verifier REPRODUCED (0 discrepancies, no fabrication). Scoped
  [`result/aann-temporal-why-reanalysis`](wiki/findings/results/aann-temporal-why-reanalysis.md) H4 +
  [`claim/aann-behavioral-gradient`](wiki/findings/claims/aann-behavioral-gradient.md) temporal caveat;
  answered [`open-question/aann-quant-temporal-inversion`](wiki/findings/open-questions/aann-quant-temporal-inversion.md);
  [`predictions.md`](wiki/predictions.md) bet **LOSS**.

## ⚠ RECONCILE at cold-start — ZERO decisions open

`wiki/decisions/open/` is **empty**. Nothing to ratify at s190 cold-start. 63 resolved
([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Do the light reconcile check and
proceed to a fresh unit.

## ⚠ Backlog for s190 (PROTOCOL §3: fewer, deeper; two-track balance)

Recent lean: s186 empirical, s187 phil, s188 empirical-design, s189 empirical. **s190 is owed a
philosophical or consolidation turn** (or a theory v2), unless a sharp empirical unit is clearly most-valuable.

1. **A theory v2 is owed on BOTH edition-flagged pages** (PROTOCOL §3, >3 update boxes) — a clean
   consolidation unit, and s189's result feeds one:
   - [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md) — **>3 boxes**
     (s147 / s165 / 2026-05-30 / s188 antonymy). A clean **v2 second edition** owed at its next substantive touch.
   - [`theory/shadow-depth-table-v1`](wiki/findings/theory/shadow-depth-table-v1.md) — 3 dated boxes
     (s173 / s186 / s187); the AANN temporal caveat is now clarified (s189 — inventory artifact), a natural
     edition trigger.
2. **PHILOSOPHICAL / EMPIRICAL (the decoupling essay's bets):**
   - **H1 — adjective-antonymy replication** (reuses the s186 frozen antonymy pipeline + Simple-Wikipedia
     control; POS change → needs its own design + critic). Does the antonymy decoupling replicate on J&K's
     home POS?
   - **H2 — the FRESH relation-recovery probe** using the pre-registered **IS-A-depth proxy**
     ([`note/taxonomic-proxy-recovery-pilot-v1`](wiki/findings/notes/taxonomic-proxy-recovery-pilot-v1.md)).
     H2 is dischargeable ONLY by a fresh test (fresh set / different corpus / adjective replication), never off
     the s186 data. Needs a design + decision trail (the multiple-proxy-arm surface).
3. **A3b BLiMP forced-choice sweep** (67k human-validated pairs, CC-BY, cataloged; design + critic first);
   **A5 production-side alternation battery**; **A6 cross-linguistic replication scout** (UD in-scope);
   **A2b grounding-magnitude** = external-resource SCOUT only
   ([`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md)).
4. **B1 last promotion** (environment-gated presupposition): weigh honestly; a written refusal is legitimate.
5. Other open-questions from the s187 harvest:
   [`open-question/lexical-regular-polysemy-productivity`](wiki/findings/open-questions/lexical-regular-polysemy-productivity.md)
   (the lexical wug-test), [`open-question/graded-privativity-gradient`](wiki/findings/open-questions/graded-privativity-gradient.md).

## ⚠ Env notes (carry)

- **`experiments/data/aann-public/` (incl. `adjexp_turk.csv`) is gitignored** — only class-level
  `human_class_means.csv` is committed; the s189 run recloned the pinned mirror (MIT, commit
  `c8095a0008cd6538717de5cc937f90ce5944e688`). Any future Arm-1 human-mean work reclones it.
- `wordfreq` + `numpy` install via `pip install wordfreq numpy` (s189 used them; `wordfreq` has no
  `__version__` attr but works). `nltk`/WordNet install via `pip install nltk` + `nltk.download('wordnet')`.
  **SubTLEX-US is unigram-only.**
- **Run long probes with harness `run_in_background: true`; parallelize per-model** (s189 ran 3 per-model
  background tasks, each writing disjoint `raw/`); wait on the completion notification, never a name-match
  (PROTOCOL §6b). openrouter MCP flaky — use the probe REST path for votes
  (`experiments/lib/openrouter.py`, `max_tokens≈500–700`). Commit signing impossible: `user.email
  noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start; `git checkout -B <branch>
  origin/main` if the branch is gone.

## ⚠ Do-not-re-grind (in force)

- **(s189) The aann-quant-temporal-inversion probe RAN → NULL. Do NOT re-run it or re-open its ratified
  decision.** The verdict is a clean, pre-named, verifier-reproduced NULL (inventory artifact); a re-run
  duplicates done work. Do NOT re-ratify the decision.
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

This session ran the sharp experiment the previous session had designed — the one place a model's feel for
grammar looked like it flatly *reversed* against people's ("a scant three days": people rate it high, models
rate it low). Tested on a broad, natural set of quantity words instead of the handful the earlier probe used,
**the reversal vanished** — it was an artifact of a few rare, odd words ("a towering three days") the earlier
sample happened to over-use; ordinary quantity words, and even "a scant three days" itself, come out rated
natural. The project's own advance bet (that the reversal was real) lost, cleanly — which is the finding: the
one apparent hole in how models handle this construction turns out to be a quirk of word-choice. About $0.19
was spent. If you want the empirical/philosophical balance or the pace paced differently, a line anywhere in
the repo outranks the plan.

## Reminder for the next cold-start

**You are session 190.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§3–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md) (audit record, not an open
campaign). **Budget: $5/day UTC — check `date -u`; s184–189 spent ≈$0.666** (2026-07-06). **RECONCILE: ZERO
decisions open.** Most-owed: **a philosophical/consolidation turn is owed** (recent empirical lean) — a
**theory v2** (both `lexicon-grammar-continuum` and `shadow-depth-table-v1` owe one), or the decoupling
essay's **H1 adjective-antonymy** / **H2 fresh relation-recovery** (needs a design + decision). Do NOT:
re-run/re-open the aann-quant-temporal probe or its decision, reopen the campaign, re-fire H2 off the pilot,
re-run/re-open A1b, re-audit the wiki, mass-edit `supported`-at-creation results, flip theory to `live` off a
non-substantive touch, adopt unlicensed corpora. **Two theory v2s owed** at next substantive touch. End
squash-merged to `main`; `git fetch --prune` at cold-start.
