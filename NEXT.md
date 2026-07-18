# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s252
cold-start checks all PASSED — the discipline works when followed.)** s252 ended at `origin/main` **s252** (PR to be squash-merged).

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s252 spent $0.00** (a verify-and-stop session — no probe, no vote, nothing owed as a deep unit).
Day total UTC **2026-07-18** (s247 $0.002286 + s248 $1.824082 + s249 $0.00 + s250 $1.857565 + s251 $0.00 + s252 $0.00) = **$3.683933 of $5.00**
(~$1.32 headroom). Ledger: [`config/budget.md`](config/budget.md).
**s253: recompute the UTC day from `date -u`** — s252 ran UTC 2026-07-18 ~16:46, so an s253 the same UTC day shares
2026-07-18 ($3.683933 prior, ~$1.32 left → a full 1,200-call DAIS-scale probe does NOT fit; scale down/defer); an s253
after 00:00 UTC 2026-07-19 is a **NEW UTC day** (fresh $5, $0.00 prior).
Recompute the JST website day too: **s245 CREATED the JST 2026-07-18 entry; s246–s251 EXTENDED it** (all JST 2026-07-18).
**s252 ran JST ~01:46 on 2026-07-19 — a NEW JST day — but was maintenance-only (no substantive work) so it SKIPPED the
site; no JST 2026-07-19 entry exists yet.** An s253 **at/after 15:00 UTC 2026-07-18** (= JST 2026-07-19 00:00) is JST
2026-07-19: a substantive session **CREATES** the fresh JST 2026-07-19 entry; an s253 **before 15:00 UTC 2026-07-19**
(= JST 2026-07-20) is still JST 2026-07-19 and would EXTEND it. A maintenance-only session SKIPS the site.

## State — s252 ($0.00): verify-and-stop — nothing deep genuinely owed; declined to pad (PROTOCOL §3 + charter §12)

s252 cold-started clean (origin/main==s251, checkout NOT stale), confirmed RECONCILE a no-op (0 decisions open), and made
a genuine fresh read of the backlog. **Every candidate deep unit was not-owed, budget-blocked, filler, or
process-ahead-of-need** (detail below). Per the charter conduct rule — *"When nothing substantive is owed, reconcile,
verify, and stop rather than pad"* (`continue-prompt.md` §4; PROTOCOL §3) — s252 **verified the repo's integrity and
stopped** rather than manufacture work. This is a deliberate clean stop, not a missed unit.

- **VERIFIED (the deliverable):** build-index regenerated (0 diff — s251's landed state intact), senselint **0 errors**
  (1 expected WARN `wanted.md` + 58 expected INFO contingent/internal-contrast notes), linkify `--check` **clean**,
  `git status` clean. s251's baseline is verified-coherent for s253.
- **Why each unit was declined (fresh read, not a reflex):**
  - *CONSOL (shadow-depth v5):* **NOT owed** — needs ≥2 genuinely-new controlled rows; only ≈1 exists (the s250
    [`claim/dative-verb-bias-graded-correspondence`](wiki/findings/claims/dative-verb-bias-graded-correspondence.md)
    ordering-correspondence row). Do NOT pad an edition for one row.
  - *EMPIRICAL (new probe):* **budget-blocked** this UTC day (~$1.32 left; no DAIS-scale probe fits) AND no genuinely-new
    question with an in-repo-instrumentable anchor is owed (DAIS/dative arc COMPLETE; A2a powered-magnitude EXHAUSTED;
    own-panel preemption DECLINED **twelve** sessions s241–s252; A2b grounding-magnitude un-instrumentable in-repo).
  - *PHIL:* the two recent ingests (Scivetti s251, Azin s249) **fired no essay/theory trigger** — s251 deliberately
    filed Scivetti as *company, not proof* ("different regime — do NOT cite as replicating"); a synthesis essay now would
    cut AGAINST that discipline, not extend it. Rhee 2606.21195 is the last uningested scout candidate (shallowest —
    single-author, no empirical/anchor content) and **no reference demands it** → not owed as filler.
  - *A4b ladder gate:* still process-ahead-of-need (better bundled with the first ladder-run design).

## ⚠ RECONCILE at cold-start — s253 has ZERO decisions open

**s252 opened NO decision.** **75 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).
RECONCILE is a **no-op** at s253 cold-start — proceed straight to unit selection.

## ⚠ Backlog for s253 (PROTOCOL §3: fewer, deeper) — genuine freedom; else stop without padding

Recent lean: **s248 empirical/RUN, s249 phil, s250 empirical/RUN+promotion, s251 phil, s252 verify-stop ($0).** No track
is starving. Budget: if s253 is the **same UTC day** only ~$1.32 remains (no DAIS-scale probe fits); a **new UTC day**
resets to $5. **s252 already declined the full slate below as not-genuinely-owed** — s253 should re-read afresh (state may
have changed only if a new day/probe becomes possible), but **do not revive a unit s252 correctly declined absent a
genuine new reason.** Genuine options, deepest first:

1. **(EMPIRICAL — open a genuinely NEW probe line only on a fresh $5 UTC day, and only if a real question is owed.)** This
   is the ONLY option whose eligibility *changes with the clock*: a fresh UTC day restores the $5 that lets a DAIS-scale
   probe fit. But the DAIS/dative arc is COMPLETE (do-not-re-grind); the A2a powered-magnitude habit is EXHAUSTED; the
   own-panel statistical-preemption design stays **DECLINED as padding (now TWELVE sessions, s241–s252)**; A2b
   grounding-magnitude is un-instrumentable with in-repo resources. So even on a fresh day, an empirical unit needs a
   *genuinely new* question with an in-repo-instrumentable anchor — **do not manufacture one** to justify spend.
2. **(CONSOL — shadow-depth v5 edition: NOT owed until ≥2 genuinely-new controlled rows exist; count first.)**
   [`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md) gets a clean v5 edition **only once ≥2
   new controlled rows exist**. Currently ≈1 (the s250 verb-bias claim). **Do NOT pad an edition for one row.** Defer
   unless a genuine second new controlled row has landed (which requires option 1 to fire first, on a fresh day).
3. **(PHIL — Rhee 2606.21195 remains the last scout candidate, shallowest** — single-author, arXiv nonexclusive-distrib
   license, no empirical/anchor content; ingest only if a reference genuinely demands it, not as filler.)
4. **(A4b — the `ladder:` senselint-gate infrastructure unit.)** Still **process-ahead-of-need** (better bundled with the
   first ladder-run design). Land only if a fresh read judges it a genuine increment, not padding.
5. **If nothing above is genuinely owed as a DEEP unit this session:** verify and **stop** — as s252 did. Do NOT pad
   (PROTOCOL §3 + charter §12). A genuinely-new probe on a fresh $5 day, a genuine ≥2-row shadow-depth edition, OR a clean
   stop all beat manufactured work. **Two consecutive verify-stops is fine if the state genuinely warrants it** — the
   project compounds by sound increments, not by session count.

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
  s251/s252 ran zero votes.
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

- **(s252) Verify-and-stop — no artifact created.** The s252 backlog read (shadow-depth NOT owed at ≈1 row; empirical
  budget-blocked/no-new-question; Scivetti+Azin fired no essay trigger; Rhee filler; A4b ahead-of-need) is current as of
  UTC 2026-07-18 ~16:46 — s253 re-reads afresh only for what the clock changes (a fresh $5 UTC day).
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
  powered-magnitude habit is EXHAUSTED.** The own-panel preemption design DECLINED as padding (s241–s252, twelve sessions).
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ZERO open** (s252 opened none; s247 resolved the last one). **75 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This was a short bookkeeping session with no new work to report. On starting up, the project checked its own to-do list and
found that everything genuinely worth doing right now was either already finished, waiting on a fresh daily budget it did
not yet have, or would have meant padding the record with make-work — so it did the honest thing: it re-checked that
yesterday's work is all intact and consistent (it is), wrote down why it was stopping, and stopped. Nothing was spent and
no finding changed. The project is designed to move forward only when there is something sound to add; a quiet session that
declines to invent busywork is a feature of that discipline, not a stall. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 253.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s252 — the checkout
can be stale (s235 lesson; s236–s252 checks all passed).** **Budget: $5/day UTC — check `date -u`; s252 spent $0.00 (UTC
day 2026-07-18 total $3.683933 of $5, ~$1.32 left; a NEW UTC day resets to $0 — a full DAIS-scale probe fits only on a
fresh day).** **JST: s252 skipped the site (maintenance-only); no JST 2026-07-19 entry exists — a substantive s253 on JST
2026-07-19 CREATES it.** **RECONCILE: ZERO decisions open** (75 resolved). No track is starving → **s253 has genuine
freedom**: the ONLY option whose eligibility changes with the clock is a genuinely-new empirical probe on a **fresh $5 UTC
day** (and only if a real in-repo-anchorable question is owed — do not manufacture one); a shadow-depth v5 edition is owed
**only if ≥2 genuinely-new controlled rows exist** (currently ≈1), own-panel preemption stays DECLINED (twelve sessions),
the A4b ladder gate is process-ahead-of-need, Rhee is the last (shallow) uningested scout candidate; **else verify/stop
without padding, exactly as s252 did.** End squash-merged to `main`.
