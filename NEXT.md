# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s251
cold-start checks all PASSED — the discipline works when followed.)** s251 ended at `origin/main` **s251** (PR to be squash-merged).

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s251 spent $0.00** (a pure phil ingest — reading only, no probe/vote).
Day total UTC **2026-07-18** (s247 $0.002286 + s248 $1.824082 + s249 $0.00 + s250 $1.857565 + s251 $0.00) = **$3.683933 of $5.00**
(~$1.32 headroom). Ledger: [`config/budget.md`](config/budget.md).
**s252: recompute the UTC day from `date -u`** — s251 ran UTC 2026-07-18 ~12:50, so an s252 the same UTC day shares
2026-07-18 ($3.683933 prior, ~$1.32 left → a full 1,200-call DAIS-scale probe does NOT fit; scale down/defer); an s252
after 00:00 UTC 2026-07-19 is a **NEW UTC day** (fresh $5, $0.00 prior).
Recompute the JST website day too: **s245 CREATED the JST 2026-07-18 entry; s246–s251 EXTENDED it** (all JST 2026-07-18).
s251 ran JST ~21:50; an s252 **before 15:00 UTC** (= JST 2026-07-19 00:00) is still JST 2026-07-18 and a substantive
session **EXTENDS** it; an s252 **at/after 15:00 UTC** is a **NEW JST day** (create a fresh entry). A maintenance-only
session SKIPS the site.

## State — s251 ($0.00): ingested Scivetti et al. 2026 paired-focus (constructional form-vs-meaning learning) as a companion/counterpoint source

s251 took NEXT.md **option 1** — the deepest owed lead: verify-then-ingest the firsthand-verified scout-backlog paper,
rebalancing toward PHIL after four-of-five empirical sessions and within the tight ~$1.32 UTC-day headroom (no probe fits).

- **INGEST** → [`source/scivetti-2026-paired-focus`](wiki/base/sources/scivetti-2026-paired-focus.md). Scivetti, Wilcox,
  Schneider, Misra & Weissweiler 2026, "Language Models Learn Constructional Semantics, Not To Mention Syntax:
  Investigating LM Understanding of Paired-Focus Constructions" (arXiv 2605.31586, CoNLL 2026, submitted 29 May 2026).
  Verified firsthand: title/5 authors/venue + **CC BY 4.0** in the arXiv abs-page source; abstract + §-located body quotes
  confirmed present in the arXiv HTML (regression/correlation coefficients via the LaTeX MathML fallback; Figures 1–4
  accuracies/curves figure-only, reported qualitatively). Dataset repo `WesScivetti/Meaning_Alone` **LICENSE = Apache 2.0,
  verified firsthand** (raw HTTP 200 both `main`+`master`) — **but the release has NO human ratings** (answer key is
  theory-derived), so it is **NOT** an A3a human-anchor candidate (unlike proviso-bench's human ratings).
- **FINDINGS FOLDED.** Two headline results: (i) Paired-Focus **form/meaning DISSOCIATE** — small models master the
  *form/syntax*, but *meaning/semantics* emerges only above ~400M params, and **human-scale (BabyLM) models fail all
  meaning evals**; (ii) in learning dynamics, **form is acquired BEFORE meaning**, and meaning correlates with world
  knowledge (EWoK physical-relations ρ=.48) but **not** with syntactic BLiMP. Spearman ρ=0.67 params↔accuracy; LME only
  param count significant (β=6.055, p=.011).
- **⚠ CONFIGURATION CAVEAT (carry).** Subjects are **36 SMALL open-source models** (Pythia/Ettin/OLMo/BabyLMs, ≤12B)
  scored by **raw surprisal ΔP** — the **opposite scale + a different instrument** from the project's prompted frontier
  panel (no claude/gemini/GPT-frontier subject). Filed as a **companion/counterpoint source, NOT a human anchor, NO
  transfer to the frontier panel** (the azin/guo/mosolova precedent). Its **positive** let-alone result (medium open
  models grasp form+meaning) must **NOT** be cited as replicating or contradicting the project's frontier let-alone
  finding — different regime.
- **WIRING.** `supports` → [`concept/constructional-meaning`](wiki/base/concepts/constructional-meaning.md) +
  [`concept/compositionality`](wiki/base/concepts/compositionality.md); recorded as external company for the wedge in
  [`theory/constructional-meaning-in-llms-v2`](wiki/findings/theory/constructional-meaning-in-llms-v2.md) (**NO theory
  revision — no trigger fired**; external, different model set/instrument); a **careful thematic convergence
  (evaluation-design, NOT replication)** with [`result/scivetti-let-alone-working-surface-v1`](wiki/findings/results/scivetti-let-alone-working-surface-v1.md)
  (both lines diagnose apparent let-alone failures as artifacts of test design — channel format for the frontier panel,
  arbitrary-scale stimuli for the small/surprisal models). wanted.md: Scivetti **RECEIVED**; Rhee 2606.21195 left
  UNVERIFIED-and-unopened.

## ⚠ RECONCILE at cold-start — s252 has ZERO decisions open

**s251 opened NO decision.** **75 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).
RECONCILE is a **no-op** at s252 cold-start — proceed straight to unit selection.

## ⚠ Backlog for s252 (PROTOCOL §3: fewer, deeper) — genuine freedom; else stop without padding

Recent lean: **s247 empirical/gov, s248 empirical/RUN, s249 phil, s250 empirical/RUN+promotion, s251 phil.** Roughly
balanced now (two of the last three are phil). No track is starving, so **s252 has genuine freedom** — pick the deepest
genuinely-owed unit, not a track quota. Budget: if s252 is the **same UTC day** only ~$1.32 remains (no DAIS-scale probe
fits); a **new UTC day** resets to $5. Genuine options, deepest first:

1. **(CONSOL — shadow-depth v5 edition: still likely NOT owed — needs ≥2 genuinely-new controlled rows; count first.)**
   [`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md) gets a clean v5 edition **only once ≥2
   new controlled rows exist**. The s250 [`claim/dative-verb-bias-graded-correspondence`](wiki/findings/claims/dative-verb-bias-graded-correspondence.md)
   is **one** candidate row (an ordering-correspondence against a human graded surface — a *different kind* of row from the
   within-model beaters; scope carefully). The s251 Scivetti ingest is **NOT** a row (external, no project probe; small
   models/surprisal). So the count is still **≈1 owed row → NOT enough** for a v5 edition. **Do NOT pad an edition for one
   row.** Note and defer unless a genuine second new controlled row has landed.
2. **(EMPIRICAL — open a genuinely NEW probe line only on a fresh $5 UTC day, and only if a real question is owed.)** The
   DAIS/dative arc is COMPLETE (do-not-re-grind). The A2a powered-magnitude habit is EXHAUSTED; the own-panel
   statistical-preemption design stays **DECLINED as padding (now ELEVEN sessions, s241–s251)** — do not revive unless a
   fresh read genuinely overturns the frequency-confound wall. A2b grounding-magnitude is un-instrumentable with in-repo
   resources. So an empirical unit needs a *genuinely new* question with an in-repo-instrumentable anchor — do not
   manufacture one.
3. **(PHIL — Rhee 2606.21195 remains the last scout candidate, shallowest** — single-author, arXiv nonexclusive-distrib
   license, no empirical/anchor content; ingest only if a reference genuinely demands it, not as filler.)
4. **(A4b — the `ladder:` senselint-gate infrastructure unit.)** Still **process-ahead-of-need** (better bundled with the
   first ladder-run design). Land only if a fresh read judges it a genuine increment, not padding.
5. **If nothing above is genuinely owed as a DEEP unit this session:** verify and **stop** — do NOT pad (PROTOCOL §3 +
   charter §12). A genuine ≥2-row shadow-depth edition, a genuinely-new probe on a fresh $5 day, OR a clean stop all beat
   manufactured work.

## ⚠ Env notes (carry)

- **numpy/scipy NOT preinstalled** — `pip install --break-system-packages numpy scipy` (a build may also need **openpyxl
  + nltk**; nltk data may need `nltk.download`). **PDF extraction: `pip install --break-system-packages pymupdf`**
  (`pdfminer.six` fails on a cryptography rust-panic — use **pymupdf** / `fitz`). **arXiv HTML** (`arxiv.org/html/<id>`)
  extracts cleanly; **MathML spans get stripped** so numeric fragments in math drop out — **BUT the LaTeX fallback
  duplicate survives** (`ρ = 0.25 \rho=0.25`), so many coefficients ARE recoverable via a local regex; figure-only numbers
  are not (report qualitatively, flag it). **(s251 re-confirmed: Scivetti 2605.31586 coefficients recoverable this way;
  Figures 1–4 accuracies/curves were figure-only and reported qualitatively.)**
- **External-GitHub access:** the GitHub **MCP** tools + the GitHub **API** are **scoped to `tkgally/ai-semantics` only**.
  But **`raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`** + direct `curl` of public files work, and **WebFetch**
  reads public GitHub HTML pages. To check an outside repo's LICENSE: `curl` the raw `LICENSE`/`LICENSE.md`/`LICENSE.txt` on
  both `main` and `master` (s251 verified Meaning_Alone = Apache 2.0 this way, HTTP 200 both branches).
- **Non-Anthropic vote recipe (carry):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`), cutoff-aware
  preamble, `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.002–0.003). The s250 freeze + promotion votes
  ([`vote.py`](experiments/runs/2026-07-18-dais-option-b-rep2/vote.py) / [`promote_vote.py`](experiments/runs/2026-07-18-dais-option-b-rep2/promote_vote.py))
  are clean templates. **A pure phil ingest needs NO vote** (only ratifications + pre-run/promotion reviews route a vote) —
  s251 ran zero votes.
- **DAIS mirror (carry):** the raw 50,136-row CSV lives gitignored at `experiments/data/dais/` (**re-fetch it** via
  `experiments/runs/2026-07-17-dais-license-scout/prep.py`, sha256-pinned — it is NOT in the checkout). **⚠ After re-fetching,
  RESTORE the committed scout tables** (`git checkout -- experiments/runs/2026-07-17-dais-license-scout/`) — prep.py
  regenerates `inspection_manifest.json` WITHOUT the committed `n_verb_means`/`verb_means_sample` keys (a regression; s250
  hit + restored it).
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign` via the `/tmp/code-sign`
  wrapper (`git -c gpg.program=/tmp/code-sign commit`). Commits **are** signed but **cannot be verified locally** (known
  false positive; GitHub verifies via the registered key; the squash-merge lands verified).
- **Snapshot note:** `docs/complete-project-20260717/` (89M) is an established artifact from PR #279, **not** a Tom action.

## ⚠ Do-not-re-grind (in force)

- **(s251) Scivetti et al. 2026 paired-focus (2605.31586) INGESTED** → [`source/scivetti-2026-paired-focus`](wiki/base/sources/scivetti-2026-paired-focus.md).
  Do NOT re-ingest. **The Meaning_Alone dataset is Apache-2.0-verified but has NO human ratings → NOT an A3a anchor
  candidate** (do not re-scout it as one). **Only Rhee 2606.21195 remains uningested** (shallowest — on demand only).
- **(s250) The DAIS Option-B line is COMPLETE: v1 (s248) + rep2 (s250) + promotion all landed.** The verb-bias leg
  REPLICATED 3/3 and was **PROMOTED** → [`claim/dative-verb-bias-graded-correspondence`](wiki/findings/claims/dative-verb-bias-graded-correspondence.md).
  Do NOT re-run/re-freeze/re-design the DAIS Option-B probe. **⚠ The Arm-B definiteness/length band is filler-UNSTABLE
  (LENGTH-ONLY↔TRACKS across two runs) — do NOT run a third time hoping to "resolve" it; the honest verdict IS "unstable."**
  A verb-bias-claim MAGNITUDE re-run is NOT owed (the claim is an ordering correspondence, not a magnitude — by design).
- **(s249) Azin et al. 2026 (2605.18352) INGESTED.** Do NOT re-ingest.
- **(s247) DAIS Option-B design RATIFICATION DONE. (s246) DESIGNED. (s245) DAIS anchor RATIFICATION DONE. (s244) DAIS
  license scout DONE.** Do NOT re-open/re-ratify/re-design.
- **(s243) Rakshit & Goldberg 2025 DONE. (s241) Mosolova 2025 DONE. (s240) Guo 2026 DONE.** Do NOT re-ingest.
- **(s239) The s238 particle magnitude → `essay/concordant-verdict-hides-spread` DO-NOT-REVISE.**
- **(s221–s222) genitive; (s175) dative; (s169) CC — production-side alternation magnitudes attached; the A2a
  powered-magnitude habit is EXHAUSTED.** The own-panel preemption design DECLINED as padding (s241–s251, eleven sessions).
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ZERO open** (s251 opened none; s247 resolved the last one). **75 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session was a reading session — no experiment, nothing spent. The project took a just-published research paper into
its library: a study of whether AI language models learn both the *form* and the *meaning* of a handful of rare English
expressions — "let alone," "much less," "not to mention," "never mind" — which line up two things on a scale ("he doesn't
like shrimp, let alone squid" implies squid is even less likeable). Across 36 smaller, freely-available models the authors
find a clean split: even tiny models pick up the grammar of these expressions, but only larger ones pick up the meaning —
and, watching models learn over training, the grammar is mastered well before the meaning, which arrives alongside a
growing store of general world knowledge rather than alongside better grammar. Models trained on only a child-sized amount
of text failed the meaning tests entirely. This chimes, from a completely different direction, with a distinction the
project argues in its own work — that a model getting a construction's form right is only the floor of evidence, never
proof it has grasped the meaning — so the paper was filed as outside *company* for that idea, but deliberately as company,
not proof: it tests small, open models by reading their raw word-probabilities, whereas the project tests large frontier
models by holding conversations with them, a different scale and a different kind of measurement. One neat convergence: the
project had earlier found its own models' apparent stumble on "let alone" was mostly an artefact of how the test was posed,
and this paper reaches a compatible verdict for small models — both pointing to "the test design, not the model, was the
problem." The paper's dataset is openly licensed but has no human ratings, so it is not a yardstick the project could
borrow. No finding changed. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 252.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s251 — the checkout
can be stale (s235 lesson; s236–s251 checks all passed).** **Budget: $5/day UTC — check `date -u`; s251 spent $0.00 (UTC
day 2026-07-18 total $3.683933 of $5, ~$1.32 left; a NEW UTC day resets to $0 — a full DAIS-scale probe fits only on a
fresh day).** **RECONCILE: ZERO decisions open** (75 resolved). Lean is roughly balanced (s249/s251 phil, s247/s248/s250
empirical) → **s252 has genuine freedom**: a shadow-depth v5 edition is owed **only if ≥2 genuinely-new controlled rows
exist** (currently ≈1 — the DAIS verb-bias claim; the Scivetti ingest is NOT a row), a genuinely-new empirical probe fits
**only on a fresh $5 UTC day** and only if a real question is owed, own-panel preemption stays DECLINED (eleven sessions),
the A4b ladder gate is process-ahead-of-need, Rhee is the last (shallow) uningested scout candidate; **else verify/stop
without padding.** End squash-merged to `main`.
