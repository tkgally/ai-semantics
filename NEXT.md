# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s188 spent $0.00304875** (one non-Anthropic design decorrelation vote; everything else harness-model / $0).
So the UTC 2026-07-06 day total is **s184+s185+s186+s188 = $0.47985875** (s187 was $0). If `date -u` still shows
**2026-07-06**, the day stands at **≈$0.4799 of $5.00** (~$4.52 headroom); if **2026-07-07+**, a **fresh
$5.00**. Ledger: [`config/budget.md`](config/budget.md).

## State — s188 ($0.003): AANN quant×temporal inversion DESIGN + decision opened; wiki-coherence campaign CLOSED; taxonomic-proxy H2 pilot note

Workflow mode, one wave of 3 parallel bounded units + a design pre-run critic + a non-Anthropic vote + a
read-only adversarial coherence pass (CLEAN). Drew both tracks; **leaned empirical** (owed after s187's phil
lean) and **closed the standing campaign**.

- **EMPIRICAL DESIGN — the aann-quant-temporal-inversion probe `[designed, NOT frozen]`**
  ([`design/aann-quant-temporal-inversion-v1`](experiments/designs/aann-quant-temporal-inversion-v1.md)).
  Operationalizes [`open-question/aann-quant-temporal-inversion`](wiki/findings/open-questions/aann-quant-temporal-inversion.md)
  — the **one AANN cell where every panel model inverts the Mahowald human gradient** (quant×temporal, "a
  scant three days": humans rate it *highest* of four adjective classes, every model *lowest*; drop the cell
  → the temporal ranking flips positive 3/3). **Class-vs-lexical:** reuses the **byte-frozen v2b
  graded-acceptability instrument** (only the item set is new), K≈20 quant modifiers (~10 Mahowald-attested
  = anchored Arm 1 + ~10 beyond = internal-contrast Arm 2), powered N≈156, per-modifier inversion count.
  Opened [`decisions/open/aann-quant-temporal-inversion-design`](wiki/decisions/open/aann-quant-temporal-inversion-design.md)
  (Q1 anchor scope / Q2 class-vs-lexical threshold / Q3 baseline; provisional defaults **C / A / A**).
  **Design pre-run critic → GO-WITH-CONDITIONS** (no fabrication — every figure verified; **2 PREREG
  blockers + 10 SHOULD-FIX**) + **non-Anthropic vote → NO-GO** (convergent-in-substance); **all conditions
  recorded as binding on the freeze/ratification session** in
  [`REVIEW-design-s188.md`](experiments/runs/2026-07-06-aann-quant-temporal-inversion/REVIEW-design-s188.md).
- **CONSOLIDATION — wiki-coherence campaign P5 → CLOSED** ([`wiki/maintenance.md`](wiki/maintenance.md)).
  Fresh read-only spot re-audit: **all 12 s183 BLOCKERs held**, gates clean; it **caught new s186-antonymy
  back-annotation lag** (the s186 A1b falsification had reached the conjecture + antonymy-outlier essay +
  shadow-depth table + predictions, but NOT three downstream shadow-depth pages) → fixed with
  history-preserving dated boxes on [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md),
  [`essay/shadow-depth-cross-cuts-grain`](wiki/findings/essays/shadow-depth-cross-cuts-grain.md) (the symmetric
  antonymy trigger annotated **→ FIRED s186** at its site), [`essay/shortcut-vs-competence-mis-cut`](wiki/findings/essays/shortcut-vs-competence-mis-cut.md).
  `continue-prompt.md` §5 deleted; the campaign is closed with a dated summary in the ledger (page stays as
  the standing audit record).
- **PHILOSOPHICAL — the H2 taxonomic-proxy pilot note `[recorded]`**
  ([`note/taxonomic-proxy-recovery-pilot-v1`](wiki/findings/notes/taxonomic-proxy-recovery-pilot-v1.md)). A
  $0 exploratory WordNet pilot serving the decoupling essay's H2 bet: pre-registers **IS-A path depth** as
  the proxy for the future fresh relation-recovery probe, **refusing** the gloss-length exploratory maximum
  on principle, and **bars H2-firing** (exploratory over the same n=6 that generated the hypothesis).

## ⚠ RECONCILE at cold-start — ONE decision open (s189-eligible)

**[`decisions/open/aann-quant-temporal-inversion-design`](wiki/decisions/open/aann-quant-temporal-inversion-design.md)
— opened s188, ELIGIBLE for ratification from s189.** To ratify: an independent **fresh adversarial-review
agent** (not this design's author) + **one non-Anthropic decorrelation vote**, **weighing the recorded s188
critic + vote conditions** (see the decision's "Design-review inputs the ratification must weigh" section and
[`REVIEW-design-s188.md`](experiments/runs/2026-07-06-aann-quant-temporal-inversion/REVIEW-design-s188.md)):
Q1-C conditioned on the S1 human-N feasibility gate; **Q2 — weigh Q2-B (a monotone/continuous primary
criterion) vs Q2-A**, both reviewers judged the 0.70/0.30 count wording arbitrary; Q3-A adopt. Then apply the
verdict (move to `wiki/decisions/resolved/`, `resolved-by: autonomous (adversarial review)`), promote/scope
the design, and proceed to freeze. **62 resolved to date** ([`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Wiki-coherence campaign — CLOSED (s188). Do NOT reopen.

P1 (s183) → P2 (s184) → P3 (s185) → P4 (s187) → **P5 (s188) → CLOSED**. `continue-prompt.md` §5 is deleted.
[`wiki/maintenance.md`](wiki/maintenance.md) stays as the standing audit record; ordinary future maintenance
accretes there (dated, history-preserving) but the *campaign* is over — no more phases.

## ⚠ Empirical backlog (the aann design is the lead — ratify then freeze+run)

1. **THE LEAD: freeze + run the aann-quant-temporal-inversion probe** — **only after the decision ratifies
   (s189)**. Freeze `prep.py` + `PREREG` **honoring the recorded conditions** (B1 per-modifier
   noun×numeral×template balance; B2 NULL-vs-CLASS/LEXICAL precedence; S1 reclone `adjexp_turk.csv` + gate
   Arm 1 on per-modifier rating-N; S2 tourist/tourish on anchored items; S3–S10). Freeze-stage pre-run
   critic + non-Anthropic vote; run the reused v2b instrument (~660 calls, ≈$0.10–0.20); post-run
   recompute-from-raw verifier; a `result` page (Arm 1 `anchors:` → Mahowald, Arm 2 internal-contrast). A
   **$0 companion first look** at Arm 1 is legitimate: the v2/rep2 anchored arms already rated Mahowald's own
   quant×temporal items (design §7).
2. **adjective-antonymy replication** (reuses the s186 frozen pipeline + the Simple-Wikipedia control) — the
   decoupling essay's **H1** (does the decoupling replicate?). Needs its own design + critic (POS change).
3. **the decoupling essay's H2 — the FRESH relation-recovery probe** using the **pre-registered IS-A-depth
   proxy** ([`note/taxonomic-proxy-recovery-pilot-v1`](wiki/findings/notes/taxonomic-proxy-recovery-pilot-v1.md)).
   H2 is dischargeable ONLY by a fresh test (fresh set / different corpus / adjective replication), never off
   the s186 data. A future design governs the multiple-proxy-arm surface (the note flags it).
4. **A3b BLiMP forced-choice sweep** (67k human-validated pairs, CC-BY, cataloged; design + critic first);
   **A5 production-side alternation battery**; **A6 cross-linguistic replication scout** (UD in-scope);
   **A2b grounding-magnitude** = external-resource SCOUT only ([`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md)).
5. **B1 last promotion** (environment-gated presupposition): weigh honestly; a written refusal is legitimate.
6. Other open-questions from the s187 harvest: [`open-question/lexical-regular-polysemy-productivity`](wiki/findings/open-questions/lexical-regular-polysemy-productivity.md)
   (the lexical wug-test), [`open-question/graded-privativity-gradient`](wiki/findings/open-questions/graded-privativity-gradient.md).

## ⚠ Theory-edition flags (carry — BOTH owe a v2 at next substantive touch, PROTOCOL §3)

- [`theory/shadow-depth-table-v1`](wiki/findings/theory/shadow-depth-table-v1.md) — 3 dated update boxes
  (s173 / s186 / s187).
- [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md) — **now >3 boxes**
  (s147 / s165 / 2026-05-30 / s188 antonymy). A clean **v2 second edition** owed at its next substantive
  touch (self-flagged in the s188 box). Not forced in a maintenance pass.

## ⚠ Env notes (carry)

- `nltk`/WordNet + `numpy` install via `pip install nltk numpy` + `nltk.download('wordnet')` (the s188
  taxonomic pilot used them). **SubTLEX-US is unigram-only.** **`experiments/data/aann-public/` (incl.
  `adjexp_turk.csv`) is gitignored** — only class-level `human_class_means.csv` is committed; the aann freeze
  session must reclone the pinned mirror (see design S1). **Run long probes with harness `run_in_background:
  true`; parallelize per-model** — shell `&`-backgrounding gets killed when the Bash tool returns; never
  name-match waits (PROTOCOL §6b). openrouter MCP flaky — use the probe REST path for votes
  (`experiments/lib/openrouter.py`, `max_tokens≈500–700`). Commit signing impossible: `user.email
  noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start; `git checkout -B <branch>
  origin/main` if the branch is gone. **Wait for ALL wave agents to complete before committing/coherence-passing.**

## ⚠ Do-not-re-grind (in force)

- **(s188) The wiki-coherence campaign is CLOSED — do NOT reopen it or re-run its phases.** The aann design
  is **written + reviewed** (GO-WITH-CONDITIONS) — do NOT redo it; **freeze + run next session** after its
  decision ratifies, honoring the recorded B1/B2/S1–S10 conditions. The taxonomic-proxy pilot is **recorded**
  — do NOT re-fire H2 off it (it explicitly bars that; H2 needs a fresh test). Do NOT re-ratify the aann
  decision in a session that treats it as this-session-opened.
- **(s186) A1b antonymy is RUN + FALSIFIED — do NOT re-run it** or re-open its ratified gates; do NOT
  re-scout its corpus. An **adjective** replication is new work. **(s185) note-sweep P3 done.** **(s184) Do
  NOT mass-edit `supported`-at-creation results; do NOT flip theory to `live` off a non-substantive touch.**
  **(s183) Do NOT re-audit the whole wiki.** **(s182) No B3 destructive essay merges.** **(s181) A2a re-runs
  DONE.** **(s179) Cite theory -v2s.** **(s170) Founding questions stay closed.** **(s168–)** no
  corpus/dataset adoption without a verified license.

## Next concrete actions — backlog for session 189 (PROTOCOL §3: fewer, deeper)

1. **RECONCILE first:** ratify [`decisions/open/aann-quant-temporal-inversion-design`](wiki/decisions/open/aann-quant-temporal-inversion-design.md)
   (fresh reviewer + non-Anthropic vote, weighing the recorded critic/vote conditions; **decide Q2-A vs
   Q2-B**). Then, if ADOPT, **freeze + run** the probe (the lead empirical unit) honoring B1/B2/S1–S10 — a
   powered, human-anchored, cheap run.
2. **PHILOSOPHICAL / EMPIRICAL companion:** the decoupling essay's H2 fresh relation-recovery design (uses
   the pre-registered IS-A-depth proxy) OR the adjective-antonymy H1 replication — either advances the
   just-registered bet. A $0 Arm-1 companion re-analysis is a legitimate warm-up.
3. **A theory v2** is owed on both [`theory/shadow-depth-table-v1`](wiki/findings/theory/shadow-depth-table-v1.md)
   and [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md) at their next
   substantive touch — a clean consolidation unit if an edition-worthy edit arises.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md): a substantive session → extend **today's** JST entry
   (check `TZ=Asia/Tokyo date`).

## Open decisions

**ONE:** [`decisions/open/aann-quant-temporal-inversion-design`](wiki/decisions/open/aann-quant-temporal-inversion-design.md)
(opened s188; **eligible for ratification s189+**, never the opening session). 62 resolved to date;
changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- This session designed (did not run) a sharp new experiment on the one place a model's feel for grammar
  visibly parts ways with people's — it rates "a scant three days" *low* where people rate it *high* — and
  sent the design's judgement-calls out for the independent review the project requires before any spend
  (a fresh reviewer found it sound with fixes to make first; an outside-company model, asked to poke holes,
  converged on the same list). It also **closed the months-long wiki tidy-up campaign** you asked for: a
  final spot-check found the earlier fixes had held and caught three pages left un-updated after the
  "opposites" result, now corrected. The campaign established that the wiki's *findings* were sound
  throughout; what had lagged was the paperwork. Almost nothing was spent. If you want the empirical /
  philosophical balance or the pace of the new experiment paced differently, a line anywhere in the repo
  outranks the plan.

## Reminder for the next cold-start

**You are session 189.** Entry [`continue-prompt.md`](continue-prompt.md) (its §5 campaign section is now
**deleted — the campaign is closed**); charter [`PROJECT.md`](PROJECT.md) (§12); discipline
[`PROTOCOL.md`](PROTOCOL.md) (§3–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md) (now an audit record, not an
open campaign). **Budget: $5/day UTC — check `date -u`; s184–188 spent ≈$0.4799** (2026-07-06). **RECONCILE:
ONE decision open — ratify `aann-quant-temporal-inversion-design`** (weigh Q2-A vs Q2-B). Most-owed: **ratify
then FREEZE + RUN the aann probe** honoring the recorded B1/B2/S1–S10 conditions. Do NOT: reopen the
campaign, redo/re-run the aann design blind, re-fire H2 off the pilot, re-run/re-open A1b, re-audit the wiki,
mass-edit `supported`-at-creation results, flip theory to `live` off a non-substantive touch, B3 merges, A2a
re-runs, founding-question re-opens, unlicensed corpus adoption. **Two theory v2s owed** at next substantive
touch (`shadow-depth-table-v1`, `lexicon-grammar-continuum`). End squash-merged to `main`; `git fetch
--prune` at cold-start.
