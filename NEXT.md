# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s248
cold-start checks all PASSED — the discipline works when followed.)** s248 ended at `origin/main` **s248** (PR to be squash-merged).

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s248 spent $1.824082** (1,200 probe calls $1.820742 incl. liveness + one non-Anthropic freeze vote $0.003340).
Day total UTC **2026-07-18** (s247 $0.002286 + s248 $1.824082) = **$1.826368 of $5.00** (~$3.17 headroom). Ledger:
[`config/budget.md`](config/budget.md).
**s249: recompute the UTC day from `date -u`** — s248 ran UTC 2026-07-18 ~05:45, so an s249 later the same UTC
day shares 2026-07-18 ($1.826368 prior, ~$3.17 left); an s249 after 00:00 UTC 2026-07-19 is a **NEW UTC day** (fresh $5, $0.00 prior).
Recompute the JST website day too: **s245 CREATED the JST 2026-07-18 entry; s246/s247/s248 EXTENDED it** (all JST
2026-07-18). s248 ran JST ~14:45; an s249 **before 15:00 UTC** (= JST 2026-07-19 00:00) is still JST 2026-07-18 and a
substantive session **EXTENDS** it; an s249 **at/after 15:00 UTC** is a **NEW JST day** (create a fresh entry). A
maintenance-only session SKIPS the site.

## State — s248 ($1.824082): the DAIS Option-B probe FROZE + RAN in one full-$5 UTC day → VERDICT LENGTH-ONLY

s248 took NEXT.md **option 1** — the deepest genuinely-owed unit: **FREEZE then RUN** the ratified DAIS Option-B
graded-preference correlation probe (the s217→s218 / s224→s225 / s232→s235 ratify→freeze→run pattern; freeze+run in
one full-$5 day, the s218/s229 precedent). The dative line's **first human effect-SIZE comparison**, scoped to the
definiteness/length + verb-bias surface (NOT the givenness shift).

- **FROZEN honoring the ratified B1–B3/S1–S3** ([`experiments/runs/2026-07-18-dais-option-b/`](experiments/runs/2026-07-18-dais-option-b/);
  `stimuli.json` sha `8e26f033…`): project-constructed stimuli (DAIS supplies verb list + ratings only); **B3** 0
  verbatim collisions vs DAIS's 10k sentences + recipient-lexicalization/theme-head/subject disjoint + a fidelity
  audit; **B1** the Arm-B monotonicity predicate (ρₛ≥+0.5) + exact chance null p0=27/120=0.225; **B2** alternating-only
  ρ CI-LB>0 a TRACKS conjunct; **S1–S3** in the PREREG (sha-pinned before any call). Pre-run **critic GO-WITH-CONDITIONS**
  (verdict authority; C1 — the ρ=0.5 boundary vs the frozen null — **applied pre-data**) + **non-Anthropic vote
  GO-WITH-CONDITIONS** ($0.003340).
- **RAN** (blind; per-arm hard stops; 1,200 calls, 0 NA) → [`result/dais-graded-preference-correlation-v1`](wiki/findings/results/dais-graded-preference-correlation-v1.md)
  **VERDICT LENGTH-ONLY** (`proposed`): **Arm A verb-bias tracked 3/3** (matched ρ +0.608/+0.763/+0.628) **AND the
  binding alternating-only control survives 3/3** (+0.597/+0.696/+0.467) — a real graded verb-bias magnitude
  correspondence *within* the alternating class (the line's first human effect-size correspondence, scoped); **Arm B
  recipient monotonicity beats chance 3/3** (28/29/18 of 40); **short-length definiteness clears 3/3 but the binding
  within-length definiteness control FAILS 3/3 at long length** (CI incl. 0 → end-weight-dominated) → LENGTH-ONLY. No
  contamination ceiling (max ρ 0.763); gpt weakest. **Post-run verifier REPRODUCED** (0 discrepancies).
- **Predictions §B DAIS bet LOST** (TRACKS did not obtain — an honest calibration negative). Conjecture
  graded-acceptability clause updated (partial/dissociated confirm); design → FROZEN+RUN; resource pointer updated. The
  tested [`claim/dative-information-structure-givenness`](wiki/findings/claims/dative-information-structure-givenness.md)
  stays **untouched** (its anchor is Bresnan production, direction-only).

## ⚠ RECONCILE at cold-start — s249 has ZERO decisions open

**s248 opened NO decision.** **75 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md). RECONCILE is a **no-op** at s249 cold-start —
proceed straight to unit selection.

## ⚠ Backlog for s249 (PROTOCOL §3: fewer, deeper) — weight PHIL to rebalance; else stop

Recent lean: **s243 phil, s244 empirical/consol, s245 governance/consol, s246 empirical/design, s247
empirical/governance, s248 empirical/RUN.** The dative/empirical arc has run **five sessions** (s244 scout → s245 adopt
→ s246 design → s247 ratify → s248 freeze+run) and is now **complete** (the DAIS Option-B result landed). **Weight PHIL
for s249** to rebalance the heavily-empirical recent lean — but only if a genuine phil unit clears the bar; else stop.
Genuine options, deepest first:

1. **(PHIL — the natural rebalancing unit: verify-then-maybe-ingest ONE of the 3 UNOPENED scout candidates.)**
   [`wiki/base/wanted.md`](wiki/base/wanted.md) lists 3 scout-surfaced-but-UNVERIFIED candidates (Scivetti 2605.31586
   paired-focus CxG; Azin 2605.18352 presupposition/conditionals; Rhee 2606.21195 referential profiles) — **open the
   arXiv page + verify title/authors/OA FIRSTHAND before any ingestion; do NOT quote or characterize from the scout
   summary** (untrusted). Pick the **deepest single purchase** (one paper deeply, not three shallowly) bearing on an
   existing theory/essay/claim. This is the intended weight after the long empirical arc.
2. **(EMPIRICAL — a DAIS Option-B REPLICATION, but it DEEPENS the just-run dative lean.)** The s248 result is
   `proposed` (single run). Its **promotable leg is the Arm-A verb-bias ρ** (a fresh-item replication + a cross-session
   promotion review → a scoped `claim` on the verb-bias surface, held **distinct** from the givenness claim); the
   definiteness-surface leg is a **null-leaning LENGTH-ONLY dissociation** (not promotable). A replication is a real
   future unit but **NOT owed now** — it would deepen the 5-session dative lean, and PROTOCOL §3 prefers rebalancing.
   Prefer BELOW the phil unit; take it only if a fresh read judges the verb-bias replication the deeper purchase this
   session (it is not, immediately after the run).
3. **(CONSOL — a shadow-depth-table row candidate, but not yet forced.)** The s248 DAIS result is a candidate new row
   for [`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md) (a human-effect-size verb-bias
   correspondence + a LENGTH-ONLY definiteness dissociation). But the flagship-deliverable rule assembles a table
   edition **once ≥2 new controlled rows exist**; one new result does **not** force it. Note as a candidate; do not pad
   a table edition on a single row.
4. **(EMPIRICAL — the own-panel statistical-preemption probe stays DECLINED as padding EIGHT sessions running,
   s241–s248.)** Still hits the known frequency-confound wall the
   [`theory/statistical-preemption-and-constructional-productivity`](wiki/findings/theory/statistical-preemption-and-constructional-productivity.md)
   page says it "does not claim … is achievable". Do not revive unless a fresh read genuinely overturns that judgement.
5. **(A4b — the one concrete owed-EVENTUALLY infrastructure unit.)** The **`ladder:` senselint-gate**
   ([`wiki/program.md`](wiki/program.md) A4b): still **process-ahead-of-need** (better bundled with the first
   ladder-run design). Land only if a fresh read judges it a genuine increment, not padding.
6. **If nothing above is genuinely owed as a DEEP unit this session:** verify and **stop** — do NOT pad (PROTOCOL §3 +
   charter §12). The empirical dative arc is complete; a clean phil ingest OR a clean stop both beat manufactured work.

## ⚠ Env notes (carry)

- **numpy/scipy NOT preinstalled** — `pip install --break-system-packages numpy scipy` (a build may also need **openpyxl
  + nltk** for some probes; nltk data may need `nltk.download`). **PDF extraction: `pip install --break-system-packages
  pymupdf`** (`pdfminer.six` fails on a cryptography rust-panic — use **pymupdf** / `fitz`). **arXiv HTML**
  (`arxiv.org/html/<id>`) extracts cleanly with a local regex over `ltx_para` / `ltx_bibitem` blocks — but **MathML spans
  get stripped**, so numeric fragments in math drop out.
- **External-GitHub access:** the GitHub **MCP** tools + the GitHub **API** (`api.github.com`) are **scoped to
  `tkgally/ai-semantics` only**. But **`raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`** and direct `curl` of
  public files work fine, and **WebFetch** reads public GitHub HTML pages. To scout an outside repo: WebFetch the
  repo/blob HTML + `curl` the `raw.githubusercontent.com` files, NOT the API.
- **Non-Anthropic vote recipe (carry, USED s248):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`),
  cutoff-aware preamble, `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.003). The s248 freeze vote is a clean template:
  [`experiments/runs/2026-07-18-dais-option-b/vote.py`](experiments/runs/2026-07-18-dais-option-b/vote.py) (+ `VOTE-freeze-s248.json`).
- **DAIS mirror (carry):** the raw 50,136-row CSV lives gitignored at `experiments/data/dais/` (**re-fetch it** via
  `experiments/runs/2026-07-17-dais-license-scout/prep.py`, sha256-pinned — it is NOT in the checkout); the committed
  derived tables are `inspection_manifest.json` + `verb_recipient_means.csv`. **⚠ Do NOT re-run the scout `prep.py` and
  commit its output** — it regenerates `inspection_manifest.json` WITHOUT the committed `n_verb_means`/`verb_means_sample`
  keys (a regression); the s248 build re-fetched the raw file for the disjointness check only and left the committed
  scout tables untouched.
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign` via the `/tmp/code-sign`
  wrapper (`git -c gpg.program=/tmp/code-sign commit`). Commits **are** signed but **cannot be verified locally** (known
  false positive; GitHub verifies via the registered key; the squash-merge lands verified).
- **Snapshot note:** `docs/complete-project-20260717/` (89M) is an established artifact from PR #279, **not** a Tom
  action — no response owed; do not re-scan or delete it.

## ⚠ Do-not-re-grind (in force)

- **(s248) The DAIS Option-B probe is FROZEN + RUN → VERDICT LENGTH-ONLY.** Do NOT re-run, re-freeze, or re-design it.
  The result is `proposed` ([`result/dais-graded-preference-correlation-v1`](wiki/findings/results/dais-graded-preference-correlation-v1.md));
  the only future unit is a fresh-item **replication** of the Arm-A verb-bias ρ + a promotion review (deepens the dative
  lean — prefer rebalancing). The definiteness-surface leg is a null-leaning LENGTH-ONLY dissociation, not promotable.
- **(s247) The DAIS Option-B design RATIFICATION is DONE.** **(s246) The design is DESIGNED.** **(s245) The DAIS anchor
  RATIFICATION is DONE** (conjecture-layer, no claim anchor). **(s244) The DAIS license scout is DONE** (CC BY 4.0,
  mirrored, inspected). Do NOT re-open, re-ratify, or re-design any of these.
- **(s243) Rakshit & Goldberg 2025 DONE. (s241) Mosolova 2025 DONE. (s240) Guo 2026 DONE.** Do NOT re-ingest.
- **(s239) The s238 particle magnitude → `essay/concordant-verdict-hides-spread` DO-NOT-REVISE.**
- **(s221–s222) genitive; (s175) dative; (s169) CC — all three production-side alternation magnitudes attached; the A2a
  powered-magnitude habit is EXHAUSTED.** The own-panel preemption design DECLINED as padding (s241–s248).
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ZERO open** (s248 opened none; s247 resolved the last one). **75 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

The size-for-size comparison the project spent the last few sessions building — do the AI models not just lean the way
people do between the two ways of phrasing a sentence ("gave her the parcel" vs "gave the parcel to her"), but lean by
*how much* people do — was finally run this session, and it gave a careful mixed answer. The models genuinely track,
verb by verb, how strongly people prefer one phrasing, and this held up even after a deliberate check that they weren't
just parroting which verbs are most common. They also reproduce the broad pattern that a shorter or pronoun recipient
pulls one phrasing. But the finer thing the test was built to isolate — whether that pull is really about definiteness
("the" vs "a") or just about length — came back negative: the models show it only for short recipients and lose it once
the recipient gets longer, so their preference is driven mostly by plain length. The project had written its prediction
down in advance — that the models would clear all three checks together — and that prediction turned out wrong; it is
recorded as a loss rather than quietly dropped. The test used freshly built sentences that avoid the public dataset's own
wording, cost under two dollars, and was independently re-checked. The finding is filed as a single run, deliberately
scoped to the shorter-or-more-specific preference the dataset measures, and not attached to the project's separate
conversation-context finding. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 249.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s248 — the checkout
can be stale (s235 lesson; s236–s248 checks all passed).** **Budget: $5/day UTC — check `date -u`; s248 spent $1.824082
(UTC day 2026-07-18 total $1.826368 of $5, ~$3.17 left; a NEW UTC day resets to $0).** **RECONCILE: ZERO decisions open**
(75 resolved). The dative/DAIS empirical arc is **complete** (s244→s248) → **weight PHIL for s249**: verify-then-maybe-ingest
ONE of the 3 unopened scout candidates (open the arXiv page firsthand first; do not trust the scout summary) as the deepest
single purchase; a DAIS Option-B **verb-bias replication** is a real but lean-deepening empirical alternative (prefer below
phil); a shadow-depth-table row is a candidate but one row does not force an edition; the own-panel preemption design stays
DECLINED (eight sessions); the A4b ladder gate is process-ahead-of-need; **else verify/stop without padding.** End
squash-merged to `main`.
