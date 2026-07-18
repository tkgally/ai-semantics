# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s249
cold-start checks all PASSED — the discipline works when followed.)** s249 ended at `origin/main` **s249** (PR to be squash-merged).

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s249 spent $0.00** (a pure reading/ingest — no probe, no vote). Day total UTC **2026-07-18** (s247 $0.002286 +
s248 $1.824082 + s249 $0.00) = **$1.826368 of $5.00** (~$3.17 headroom). Ledger: [`config/budget.md`](config/budget.md).
**s250: recompute the UTC day from `date -u`** — s249 ran UTC 2026-07-18 ~07:10, so an s250 the same UTC day shares
2026-07-18 ($1.826368 prior, ~$3.17 left); an s250 after 00:00 UTC 2026-07-19 is a **NEW UTC day** (fresh $5, $0.00 prior).
Recompute the JST website day too: **s245 CREATED the JST 2026-07-18 entry; s246/s247/s248/s249 EXTENDED it** (all JST
2026-07-18). s249 ran JST ~16:10; an s250 **before 15:00 UTC** (= JST 2026-07-19 00:00) is still JST 2026-07-18 and a
substantive session **EXTENDS** it; an s250 **at/after 15:00 UTC** is a **NEW JST day** (create a fresh entry). A
maintenance-only session SKIPS the site.

## State — s249 ($0.00): PHIL rebalance — verified 3 scout candidates firsthand, ingested the deepest (Azin et al. 2026 presupposition/conditionals)

s249 took NEXT.md **option 1** — the natural rebalancing unit after the five-session dative/empirical arc (s244→s248):
**verify-then-ingest ONE of the 3 unopened s240-scout candidates**, opening the arXiv page firsthand first.

- **All THREE scout candidates verified FIRSTHAND** on arXiv (existence/authors/OA/license — the scout summary is
  untrusted): Scivetti et al. **2605.31586** (paired-focus CxG, CC BY 4.0, CoNLL 2026); Azin, Yu, Singh & Jouravlev
  **2605.18352** (presupposition/conditionals, CC BY 4.0, CoNLL 2026); Rhee **2606.21195** (referential profiles,
  single-author, arXiv nonexclusive-distrib license, 29pp conceptual — **no empirical/anchor content**). All three exist
  with authors/titles matching the scout.
- **INGESTED the deepest single purchase — Azin et al. 2026** → [`source/azin-2026-presupposition-conditionals`](wiki/base/sources/azin-2026-presupposition-conditionals.md)
  (chosen over Scivetti/Rhee because it lands on a **live project line with an open gap** — the presupposition/projection
  line + the A3a human-anchor null). A parallel **human-vs-LLM** study of the **proviso** problem (presupposition in a
  conditional's **consequent**, modulated by antecedent relevance; 90 sentences; 120 Prolific participants; subjects
  GPT-5/Gemini-2.5-flash/Llama/Qwen — **no claude subject**). Headline: humans blend probability+relevance, LLMs align
  weakly (best ρ≈0.25–0.38; GPT-5 n.s.), and the best human-aligner has the **worst** pragmatic-reasoning-checklist
  compliance → **"surface pattern matching rather than pragmatic competence."** All quotes firsthand-verified in the arXiv
  HTML; license CC BY 4.0 firsthand on the abs page. **Companion/counterpoint, NOT a human anchor, no transfer to the
  frontier panel.**
- **⚠ CONFIGURATION CAVEAT (caught by reading, not the scout):** Azin's **proviso/consequent-trigger** cell is
  **structurally distinct** from the project's headline **antecedent-of-conditional** collapse
  ([`result/conditional-projection-rescue-v1`](wiki/findings/results/conditional-projection-rescue-v1.md)) — a companion
  on the broad phenomenon, **not** an item-matched corroboration. Wired + scoped as such everywhere.
- **WIRING:** `supports` → [`essay/projection-defeasible-by-frame`](wiki/findings/essays/projection-defeasible-by-frame.md)
  (external convergence — **but NO essay revision, NO trigger fired**); `refines` → [`concept/inferential-meaning`](wiki/base/concepts/inferential-meaning.md);
  a scoped companion note on the conditional-collapse result; **candidate 5** in the A3a scout
  [`resource/presupposition-projection-human-anchor-scouting`](wiki/base/resources/presupposition-projection-human-anchor-scouting.md)
  — the first *designed/normed/human-rated* conditional-presupposition release surfaced, **BUT license UNVERIFIED** (repo
  LICENSE → HTTP 404 firsthand; CC BY 4.0 covers the paper, not the data — the NOPE/Cao precedent) → **NOT adopted**
  (cataloguing ≠ adoption). **A3a stays `[x]`** (ADOPT-A "adopt none yet" verdict unchanged). wanted.md: Azin RECEIVED.

## ⚠ RECONCILE at cold-start — s250 has ZERO decisions open

**s249 opened NO decision.** **75 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).
RECONCILE is a **no-op** at s250 cold-start — proceed straight to unit selection.

## ⚠ Backlog for s250 (PROTOCOL §3: fewer, deeper) — weight EMPIRICAL (but genuine freedom); else stop

Recent lean: **s244 empirical/consol, s245 governance/consol, s246 empirical/design, s247 empirical/governance, s248
empirical/RUN, s249 phil.** s249 was the deliberate phil rebalance, so **s250 has genuine freedom** — but the standing
empirical lead is real. Genuine options, deepest first:

1. **(EMPIRICAL — the deepest owed lead: the DAIS Option-B verb-bias ρ REPLICATION + promotion review.)** The s248 result
   [`result/dais-graded-preference-correlation-v1`](wiki/findings/results/dais-graded-preference-correlation-v1.md) is
   `proposed` (single run). Its **promotable leg is the Arm-A verb-bias ρ** (a fresh-item replication → a cross-session
   promotion review → a scoped `claim` on the verb-bias surface, held **distinct** from the givenness claim). The
   definiteness-surface leg is a **null-leaning LENGTH-ONLY dissociation** (not promotable). This is a **real, deep,
   genuinely-owed** unit (a powered fresh-item re-run at ~100–150 items, ≲$2). It deepens the dative lean, but s249
   already rebalanced, so it is a fair pick now.
2. **(PHIL — the next-deepest verified scout candidate: Scivetti et al. 2026 paired-focus CxG.)** Already verified firsthand
   at s249 (2605.31586, CC BY 4.0). A new construction family (paired-focus: "let alone", "much less") + a
   semantics-emerges-later-than-syntax training-dynamics result — bears on the constructional-meaning line + shadow-depth.
   A clean deep ingest if s250 wants to keep weighting phil. (Rhee 2606.21195 is available but shallowest — single-author,
   nonexclusive-distrib license, no empirical/anchor content; ingest only if a reference genuinely demands it.)
3. **(CONSOL — a shadow-depth-table row candidate, but not yet forced.)** The s248 DAIS result is a candidate new row for
   [`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md) (a human-effect-size verb-bias
   correspondence + a LENGTH-ONLY definiteness dissociation). The flagship-deliverable rule assembles a table edition
   **once ≥2 new controlled rows exist**; one new result does **not** force it. Note as a candidate; do not pad an edition.
4. **(EMPIRICAL — the own-panel statistical-preemption probe stays DECLINED as padding NINE sessions running, s241–s249.)**
   Still hits the known frequency-confound wall the
   [`theory/statistical-preemption-and-constructional-productivity`](wiki/findings/theory/statistical-preemption-and-constructional-productivity.md)
   page says it "does not claim … is achievable". Do not revive unless a fresh read genuinely overturns that judgement.
5. **(A4b — the one concrete owed-EVENTUALLY infrastructure unit.)** The **`ladder:` senselint-gate**
   ([`wiki/program.md`](wiki/program.md) A4b): still **process-ahead-of-need** (better bundled with the first ladder-run
   design). Land only if a fresh read judges it a genuine increment, not padding.
6. **If nothing above is genuinely owed as a DEEP unit this session:** verify and **stop** — do NOT pad (PROTOCOL §3 +
   charter §12). A clean DAIS verb-bias replication, a clean Scivetti ingest, OR a clean stop all beat manufactured work.

## ⚠ Env notes (carry)

- **numpy/scipy NOT preinstalled** — `pip install --break-system-packages numpy scipy` (a build may also need **openpyxl
  + nltk** for some probes; nltk data may need `nltk.download`). **PDF extraction: `pip install --break-system-packages
  pymupdf`** (`pdfminer.six` fails on a cryptography rust-panic — use **pymupdf** / `fitz`). **arXiv HTML**
  (`arxiv.org/html/<id>`) extracts cleanly; **MathML spans get stripped**, so numeric fragments in math drop out — **BUT
  the LaTeX fallback duplicate survives** (`ρ = 0.25 \rho=0.25`), so many coefficients ARE recoverable via a local regex;
  figure-only numbers are not (report qualitatively, flag it). (s249 used a local `curl` of `arxiv.org/html/<id>` + a
  Python tag-strip to firsthand-verify quotes — clean.)
- **External-GitHub access:** the GitHub **MCP** tools + the GitHub **API** (`api.github.com`) are **scoped to
  `tkgally/ai-semantics` only**. But **`raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`** and direct `curl` of
  public files work fine, and **WebFetch** reads public GitHub HTML pages. To scout an outside repo: WebFetch the
  repo/blob HTML + `curl` the `raw.githubusercontent.com` files, NOT the API. (s249: a raw-file LICENSE 404-check on an
  outside repo worked; the GitHub landing page returned **403 via the proxy**, so the API `license` field is unreadable —
  rest license verdicts on raw-file 404s + the abs-page/README prose, as the A3a scout does.)
- **Non-Anthropic vote recipe (carry, USED s248):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`),
  cutoff-aware preamble, `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.003). The s248 freeze vote is a clean template:
  [`experiments/runs/2026-07-18-dais-option-b/vote.py`](experiments/runs/2026-07-18-dais-option-b/vote.py). (A pure phil
  ingest like s249 needs NO vote — only ratifications + pre-run critiques of probes route a vote.)
- **DAIS mirror (carry):** the raw 50,136-row CSV lives gitignored at `experiments/data/dais/` (**re-fetch it** via
  `experiments/runs/2026-07-17-dais-license-scout/prep.py`, sha256-pinned — it is NOT in the checkout); the committed
  derived tables are `inspection_manifest.json` + `verb_recipient_means.csv`. **⚠ Do NOT re-run the scout `prep.py` and
  commit its output** — it regenerates `inspection_manifest.json` WITHOUT the committed `n_verb_means`/`verb_means_sample`
  keys (a regression). A DAIS verb-bias replication (option 1) re-fetches the raw file for its own disjointness/human-target
  build only; leave the committed scout tables untouched.
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign` via the `/tmp/code-sign`
  wrapper (`git -c gpg.program=/tmp/code-sign commit`). Commits **are** signed but **cannot be verified locally** (known
  false positive; GitHub verifies via the registered key; the squash-merge lands verified).
- **Snapshot note:** `docs/complete-project-20260717/` (89M) is an established artifact from PR #279, **not** a Tom
  action — no response owed; do not re-scan or delete it.

## ⚠ Do-not-re-grind (in force)

- **(s249) Azin et al. 2026 (2605.18352) INGESTED** → [`source/azin-2026-presupposition-conditionals`](wiki/base/sources/azin-2026-presupposition-conditionals.md).
  Do NOT re-ingest. Its proviso-bench dataset is **candidate 5 in the A3a scout, license UNVERIFIED, NOT adopted** — do NOT
  adopt without a firsthand-verified data license AND a cross-session ratified anchor decision (and note the proviso-vs-antecedent
  configuration mismatch). **The other 2 scout candidates are verified-to-exist but UNINGESTED:** Scivetti 2605.31586 (a
  real future phil unit), Rhee 2606.21195 (shallowest — ingest only on demand).
- **(s248) The DAIS Option-B probe is FROZEN + RUN → VERDICT LENGTH-ONLY.** Do NOT re-run, re-freeze, or re-design it.
  The result is `proposed`; the only future unit is a fresh-item **replication** of the Arm-A verb-bias ρ + a promotion
  review (option 1 above). The definiteness-surface leg is a null-leaning LENGTH-ONLY dissociation, not promotable.
- **(s247) The DAIS Option-B design RATIFICATION is DONE. (s246) DESIGNED. (s245) The DAIS anchor RATIFICATION is DONE**
  (conjecture-layer, no claim anchor). **(s244) The DAIS license scout is DONE** (CC BY 4.0, mirrored, inspected). Do NOT
  re-open, re-ratify, or re-design any of these.
- **(s243) Rakshit & Goldberg 2025 DONE. (s241) Mosolova 2025 DONE. (s240) Guo 2026 DONE.** Do NOT re-ingest.
- **(s239) The s238 particle magnitude → `essay/concordant-verdict-hides-spread` DO-NOT-REVISE.**
- **(s221–s222) genitive; (s175) dative; (s169) CC — all three production-side alternation magnitudes attached; the A2a
  powered-magnitude habit is EXHAUSTED.** The own-panel preemption design DECLINED as padding (s241–s249).
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ZERO open** (s249 opened none; s247 resolved the last one). **75 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session did no experiment — it read. After several sessions of running a grammar comparison, the project turned to its
reading list: three recently-published papers it had only heard about second-hand. It opened all three, confirmed by hand
that each is real and freely available, and then took the single most relevant one properly into its library rather than
skimming all three. That paper compares people and four AI models on a quiet assumption tucked inside "if…" sentences —
when "his sister" in "If John flies to London, his sister will pick him up" takes for granted that John has a sister. The
study found people blend how likely and how relevant the background fact is, while the models agree with people only
weakly, and — pointedly — the model whose numbers look most human-like is the one whose written reasoning is least
coherent, which the authors read as surface pattern-matching rather than real grasp. The project filed the paper as outside
*company* for an argument it already makes in its own voice, being careful to note it tests different models and a
neighbouring version of the puzzle, not the exact one the project has measured. The most useful by-product was the study's
released set of human ratings — exactly the kind of human data the project has long wanted to turn one of its own
model-only findings into a proper human comparison. It logged those ratings as a candidate for that job and then, on
inspection, declined to use them, because the data carries no verifiable licence and, in any case, measures the neighbouring
version of the question. Recording "found it, checked it, holding off" is the honest posture. A line anywhere in the repo
outranks this note.

## Reminder for the next cold-start

**You are session 250.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s249 — the checkout
can be stale (s235 lesson; s236–s249 checks all passed).** **Budget: $5/day UTC — check `date -u`; s249 spent $0.00 (UTC
day 2026-07-18 total $1.826368 of $5, ~$3.17 left; a NEW UTC day resets to $0).** **RECONCILE: ZERO decisions open** (75
resolved). s249 was the phil rebalance → **weight EMPIRICAL for s250 (with genuine freedom): the DAIS Option-B verb-bias ρ
REPLICATION + promotion review** is the deepest genuinely-owed lead (the s248 result's promotable Arm-A leg → a scoped
verb-bias `claim`, held distinct from the givenness claim); a Scivetti paired-focus CxG ingest is the next-deepest phil
alternative (already verified); a shadow-depth row is a candidate but one row does not force an edition; own-panel preemption
stays DECLINED (nine sessions); the A4b ladder gate is process-ahead-of-need; **else verify/stop without padding.** End
squash-merged to `main`.
