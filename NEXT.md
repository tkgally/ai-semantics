# NEXT.md

## ⚠ PROJECT COMPLETE — recorded 2026-07-20 from Tom's direct instruction (standing override)

On 2026-07-20 Tom declared the project **finished**: the repository is now public and archival,
the final plain-language report is published as the `docs/` website (source:
`project-history/20260719-capstone-report.md`), and the old monitoring site and complete-project
snapshot have been **deleted** — `docs/` no longer hosts the journal, and the website duty in
`PROTOCOL.md` §5b is retired with it. **No further research sessions are owed.** If a scheduled
session nonetheless starts here: do NOT run probes or spend budget, do NOT modify `docs/` (it is
the final report site, not the journal), and do NOT rewrite the historical content below.
Verify `git status` is clean, confirm `origin/main` is intact, and stop. This notice outranks
everything below it (Tom's standing override, `PROJECT.md` §12.3). Everything below is preserved
as the project's final operational state, for the record.


## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236–s257
cold-start checks all PASSED — the discipline works when followed.)** s257 ended at `origin/main` **s257** (PR to be squash-merged).

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s257 spent $0.00** (a 6th-consecutive verify-and-stop — no probe, no vote; the only edits are handoff bookkeeping).
**s254, s255, s256 AND s257 all ran the fresh UTC day 2026-07-19** (s247–s253 all fell on the now-closed 2026-07-18 UTC day, $3.683933 of $5).
Day total UTC **2026-07-19** = **$0.00 of $5.00** (full $5 headroom — s254/s255/s256/s257 each added $0.00).
Ledger: [`config/budget.md`](config/budget.md).
**s258: recompute the UTC day from `date -u`** — s257 ran UTC 2026-07-19 ~12:46, so an s258 **before 00:00 UTC 2026-07-20**
shares 2026-07-19 ($0.00 prior → **a full DAIS-scale ~1,200-call probe fits comfortably** on the fresh $5); an s258 **at/after 00:00
UTC 2026-07-20** is a **NEW UTC day** (fresh $5, $0.00 prior) either way.
Recompute the JST website day too: **s245 CREATED the JST 2026-07-18 entry; s246–s251 EXTENDED it** (all JST 2026-07-18).
**s252–s257 were all maintenance-only so all SKIPPED the site; no JST 2026-07-19 entry exists yet** (s252/s253 ran JST 2026-07-19;
s254 ran JST 2026-07-19 ~09:46; s255 ~13:45; s256 ~17:46; s257 ~21:46). An s258 **before 15:00 UTC 2026-07-19**
(= JST 2026-07-20) is still JST 2026-07-19: a substantive session **CREATES** the fresh JST 2026-07-19 entry; an s258 **at/after 15:00 UTC
2026-07-19** is JST 2026-07-20 and a substantive session CREATES that day's entry. A maintenance-only session SKIPS the site either way.

## State — s257 ($0.00): 6th-consecutive verify-and-stop — repo STILL byte-identical to s256 (only s256's own PR intervened on origin/main), so per NEXT.md's own instruction a fast confirm-and-stop, not a re-sweep

s257 cold-started clean (`git fetch --prune` / `git checkout -B origin/main`; origin/main==s256 `9ad84b0` #317, checkout was one commit behind [container at s255 `3cbd38f`] but **not problematically stale — origin/main matched NEXT.md's expected s256**, so reset-and-proceed — 23rd consecutive pass),
confirmed RECONCILE a no-op (0 decisions open), and opened on the **SAME fresh $5 UTC day 2026-07-19 as s254/s255/s256** ($0.00 prior). The
decisive fact: **`origin/main` did NOT advance beyond s256's handoff** (`3cbd38f→9ad84b0` was s256's *own* PR squash-merging; no other session
intervened) — so on a byte-identical repo **no new trigger item can have surfaced** (a logical certainty). NEXT.md's standing instruction for
exactly this case: *"if origin/main is STILL unchanged from s256, fast-confirm-and-stop rather than re-sweep — s254's six-check stands as the deep
audit."* s257 followed it: confirmed integrity + no new item, and — per the charter conduct rule *"When nothing substantive is owed, reconcile,
verify, and stop rather than pad"* — **stopped cleanly.** This session also surfaced the plateau to Tom via the routine's notification channel
(a single heads-up).

- **VERIFIED (the deliverable):** build-index regenerated (0 diff — s256's landed state intact), senselint **0 errors**
  (1 expected WARN `wanted.md` + 58 expected INFO contingent/internal-contrast notes), linkify `--check` **clean**,
  `git status` clean. s256's baseline is verified-coherent for s258.
- **Confirm (not re-sweep) — ALL NOT-OWED (s254's six-check sweep remains the standing deep audit of this unchanged state):**
  1. *Theory-edition:* NO live theory page carries >3 dated update boxes ([`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md)
     has **2** [s229, s238]; the rest ≤2; every `-v2/-v3/-v4` page is itself the fresh edition, originals `superseded`). 5 draft-status
     live theory pages are **deferred-not-owed** (draft→live only at next *substantive* touch).
  2. *Essay triggers:* the ~50-essay phil web ([`wiki/ideas.md`](wiki/ideas.md)) is mature; every fired essay trigger's revision is
     applied; **NO new fired trigger since s254** (the essay bar — a fired trigger / new literature / a new falsifiable bet — has
     nothing new to satisfy it; no ingest or result has landed since s254; s255/s256/s257 were all $0 stops).
  3. *$0-answerable open-questions:* none of the 12 open OQs is answerable purely by re-reading in-repo files; the one $0 leg was already
     harvested into `note/instrument-disagreement-reanalysis-v1`.
  4. *Promotion review:* every replicated+controlled reading-bearing result already has its `claim` (genitive, particle, DAIS-verb-bias,
     aann, CC, dative ×3, sense-gradience, relation-recovery, relational-order, output-channel — all ✓); the un-promoted multi-run lines
     (bridging=null, scivetti-let-alone=residual-feeds-output-channel, coercion=internal-contrast, conative=fails-replicate) are correctly
     unpromoted. Nothing dangling.
  5. *Prediction-ledger lag:* no row with a known outcome left un-updated (~22 `open` rows genuinely await un-landed probes/anchors).
  6. *Genuinely-new probe (the clock-sensitive check):* even on the fresh $5 day, **NO** genuinely-new in-repo-instrumentable, anchored
     question is owed — A2b (**un-instrumentable in-repo**; in-house build barred by no-human-subjects), A4b (ladder-gate **infrastructure,
     ahead-of-need**), A4d (logprob pilot — corroborative lane, ahead-of-need), B1/B3 (`[~]` ongoing, no dangling promotion), **A3c**
     (declined as null-on-null padding s254). DAIS/dative arc COMPLETE; A2a EXHAUSTED; own-panel preemption DECLINED **seventeen**
     sessions (s241–s257); Rhee 2606.21195 filler.
- **A3c stays DECLINED (confirmed, NOT re-run):** per NEXT.md's standing instruction, a stop *need only confirm no new $0/anchored
  item has surfaced — not re-run the A3c analysis*. The repo is unchanged since s254 named+dispositioned A3c, so
  **no new such item has surfaced and A3c stays declined**. (Lancaster norms $0 re-analysis = null-on-null: [`result/lexical-perceptual-grounding-moderation-v1`](wiki/findings/results/lexical-perceptual-grounding-moderation-v1.md)
  already returned a clean NULL; post-v1 targets are a replication of that same graded scale or themselves nulls → no live positive for
  grounding to moderate. Re-becomes live only if a *new* grounding-sensitive positive lexical effect lands.)

## ⚠ RECONCILE at cold-start — s258 has ZERO decisions open

**s257 opened NO decision.** **75 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).
RECONCILE is a **no-op** at s258 cold-start — proceed straight to unit selection.

## ⚠ Backlog for s258 (PROTOCOL §3: fewer, deeper) — genuine freedom; else stop without padding

Recent lean: **s248 empirical/RUN, s249 phil, s250 empirical/RUN+promotion, s251 phil, s252–s257 verify-stop ($0 each).**
No track is starving (the last *work* sessions were balanced). Budget: if s258 is the **same UTC day 2026-07-19** the full $5 is
available ($0.00 prior → a DAIS-scale probe fits); a **new UTC day** also resets to $5. **s252–s257 all declined the full slate below as
not-genuinely-owed** (s254 with an independent six-check sweep + the A3c disposition; s255/s256/s257 confirming the unchanged repo) — s258 should
re-read afresh (state changes only if a new probe genuinely becomes owed, which requires main to have advanced with new *work*), but **do not revive a
unit s252–s257 correctly declined absent a genuine new reason.** Genuine options, deepest first:

1. **(EMPIRICAL — open a genuinely NEW probe line only if a real question with an in-repo-instrumentable anchor is owed.)** The fresh
   $5 makes a DAIS-scale probe *fit budget-wise* — but budget is not the binding constraint; a **genuinely-new anchored question is.**
   The DAIS/dative arc is COMPLETE (do-not-re-grind); the A2a powered-magnitude habit is EXHAUSTED; own-panel statistical-preemption
   stays **DECLINED as padding (seventeen sessions, s241–s257)**; A2b grounding-magnitude is un-instrumentable with in-repo resources;
   **A3c is dispositioned as null-on-null padding (s254).** So an empirical unit needs a *genuinely new* question — **do not manufacture
   one** to justify spend on a fresh day.
2. **(CONSOL — shadow-depth v5 edition: NOT owed until ≥2 genuinely-new controlled rows exist; count first.)**
   [`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md) gets a clean v5 edition **only once ≥2 new
   controlled rows exist** (v4 carries only 2 dated update boxes — under the edition threshold). Currently ≈1 (the s250 verb-bias
   claim). **Do NOT pad an edition for one row.** Defer unless a genuine second new controlled row has landed (needs option 1 first).
3. **(PHIL — Rhee 2606.21195 remains the last scout candidate, shallowest** — single-author, arXiv nonexclusive-distrib license, no
   empirical/anchor content; ingest only if a reference genuinely demands it, not as filler.)
4. **(A4b — the `ladder:` senselint-gate infrastructure unit.)** Still **process-ahead-of-need** (better bundled with the first
   ladder-run design). Land only if a fresh read judges it a genuine increment, not padding.
5. **If nothing above is genuinely owed as a DEEP unit this session:** verify and **stop** — as s252–s257 did. Do NOT pad
   (PROTOCOL §3 + charter §12). A genuinely-new probe, a genuine ≥2-row shadow-depth edition, OR a clean stop all beat manufactured
   work. **Consecutive verify-stops are fine if the state genuinely warrants it** — the project compounds by sound increments, not by
   session count. **⚠ But note the standing-override observation below:** six consecutive honest stops (s252–s257, four now on a
   full fresh $5) signal a genuine *plateau* on the established lines. A seventh stop is fine if the state warrants — but if s258 finds the
   repo STILL unchanged from s257 (`origin/main`==s257, no merge intervening), the honest move is a fast confirm-and-stop, **not** a
   from-scratch re-sweep (that would itself be padding); s254's independent six-check already stands as the deep audit on this state.

## ⚠ Env notes (carry)

- **numpy/scipy NOT preinstalled** — `pip install --break-system-packages numpy scipy` (a build may also need **openpyxl
  + nltk**; nltk data may need `nltk.download`). **PDF extraction: `pip install --break-system-packages pymupdf`**
  (`pdfminer.six` fails on a cryptography rust-panic — use **pymupdf** / `fitz`). **arXiv HTML** (`arxiv.org/html/<id>`)
  extracts cleanly; **MathML spans get stripped** so numeric fragments in math drop out — **BUT the LaTeX fallback
  duplicate survives** (`ρ = 0.25 \rho=0.25`), so many coefficients ARE recoverable via a local regex; figure-only numbers
  are not (report qualitatively, flag it).
- **External-GitHub access:** the GitHub **MCP** tools + the GitHub **API** are **scoped to `tkgally/ai-semantics` only**.
  But **`raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>`** + direct `curl` of public files work, and **WebFetch**
  reads public GitHub HTML pages. To check an outside repo's LICENSE: `curl` the raw `LICENSE`/`LICENSE.md`/`LICENSE.txt` on
  both `main` and `master`.
- **Non-Anthropic vote recipe (carry):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`), cutoff-aware
  preamble, `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.002–0.003). The s250 freeze + promotion votes
  ([`vote.py`](experiments/runs/2026-07-18-dais-option-b-rep2/vote.py) / [`promote_vote.py`](experiments/runs/2026-07-18-dais-option-b-rep2/promote_vote.py))
  are clean templates. **A pure phil ingest needs NO vote** (only ratifications + pre-run/promotion reviews route a vote) —
  s251–s257 ran zero votes.
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

- **(s257) 6th-consecutive verify-and-stop — no artifact created.** origin/main did not advance beyond s256's handoff (only s256's own PR
  merged 3cbd38f→9ad84b0), so s254's independent six-check sweep stands as the deep audit; s257 only re-verified integrity + confirmed no new
  item surfaced (following NEXT.md's explicit fast-confirm-not-re-sweep instruction) + surfaced the plateau to Tom once via the notification channel.
- **(s256) 5th-consecutive verify-and-stop — no artifact created.** origin/main did not advance since s255 (same commit 745e5fd), so
  s254's independent six-check sweep stands; s256 only re-verified integrity + confirmed no new item surfaced.
- **(s255) 4th-consecutive verify-and-stop — no artifact created.** origin/main did not advance since s254 (same commit c9bd0b8), so
  s254's independent six-check sweep stands; s255 only re-verified integrity + confirmed no new item surfaced.
- **(s254) 3rd-consecutive verify-and-stop — the one artifact was the A3c disposition** (declined as null-on-null padding; program.md
  A3c, dated s254). An independent SIX-check sweep against the LIVE pages found all six trigger types + the fresh-day empirical option
  NOT-OWED. **A3c is named/dispositioned — do NOT re-run its analysis, just confirm no new $0/anchored item has surfaced.**
- **(s253) 2nd-consecutive verify-and-stop; (s252) verify-and-stop — no artifact created.** s254's six-check sweep re-confirmed both.
- **(s251) Scivetti et al. 2026 paired-focus (2605.31586) INGESTED** → [`source/scivetti-2026-paired-focus`](wiki/base/sources/scivetti-2026-paired-focus.md).
  Do NOT re-ingest. **The Meaning_Alone dataset is Apache-2.0-verified but has NO human ratings → NOT an A3a anchor
  candidate.** **Only Rhee 2606.21195 remains uningested** (shallowest — on demand only).
- **(s250) The DAIS Option-B line is COMPLETE: v1 (s248) + rep2 (s250) + promotion all landed.** The verb-bias leg
  REPLICATED 3/3 and was **PROMOTED** → [`claim/dative-verb-bias-graded-correspondence`](wiki/findings/claims/dative-verb-bias-graded-correspondence.md).
  Do NOT re-run/re-freeze/re-design the DAIS Option-B probe. **⚠ The Arm-B definiteness/length band is filler-UNSTABLE
  (LENGTH-ONLY↔TRACKS across two runs) — do NOT run a third time; the honest verdict IS "unstable."** A verb-bias-claim MAGNITUDE
  re-run is NOT owed (the claim is an ordering correspondence, not a magnitude — by design).
- **(s249) Azin et al. 2026 (2605.18352) INGESTED.** Do NOT re-ingest.
- **(s247) DAIS Option-B design RATIFICATION DONE. (s246) DESIGNED. (s245) DAIS anchor RATIFICATION DONE. (s244) DAIS
  license scout DONE.** Do NOT re-open/re-ratify/re-design.
- **(s243) Rakshit & Goldberg 2025 DONE. (s241) Mosolova 2025 DONE. (s240) Guo 2026 DONE.** Do NOT re-ingest.
- **(s239) The s238 particle magnitude → `essay/concordant-verdict-hides-spread` DO-NOT-REVISE.**
- **(s221–s222) genitive; (s175) dative; (s169) CC — production-side alternation magnitudes attached; the A2a
  powered-magnitude habit is EXHAUSTED.** The own-panel preemption design DECLINED as padding (s241–s257, seventeen sessions).
- **(A3c, s254) Lancaster norms $0 re-analysis DECLINED as null-on-null padding** — do NOT run; re-becomes live only if a new
  grounding-sensitive positive lexical effect lands.
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ZERO open** (s257 opened none; s247 resolved the last one). **75 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This was the sixth short bookkeeping session in a row. Three sessions back, starting with a fresh full day's budget, an independent
reviewer went through the entire list of things the project might owe — including whether any genuinely new experiment was now
worth running — and the answer came back that nothing of that kind is outstanding: the established lines of work are complete, and no
genuinely new question the project can measure with its own resources is waiting. Each session since (including this one) has confirmed
that nothing has changed — the shared record has not moved — re-checked that all recent work is intact and consistent (it is), and
stopped. Nothing was spent and no finding changed.

Six honest stops in a row — four now with money available to spend — are worth naming plainly: the project has reached a genuine
**plateau** on the lines it set for itself. This is not stagnation and not a failure of effort; it is that the current program's open
items are each either finished, impossible to measure with the resources the project is allowed to use, or infrastructure that is better
built alongside the work that would first need it. The one high-value input that would break the plateau is a genuinely **new direction** —
the charter explicitly allows scope to extend outward while keeping meaning as the focus. Choosing such a direction is a value-laden call,
and the project's own rules say it should not manufacture one just to look busy; a steer from you on where to point next would be the most
useful thing right now. **This session sent you a single notification to that effect** (rather than letting the plateau sit only in this
file), so you have a heads-up without needing to open the repo. Absent a steer, the project will keep making the honest call — verify,
confirm, and stop — rather than pad. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 258.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md) (§12);
discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program [`wiki/program.md`](wiki/program.md).
Navigate via [`wiki/index.md`](wiki/index.md), [`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md).
**FIRST: `git fetch --prune && git checkout -B <branch> origin/main` and confirm `origin/main` is at s257 — the checkout
can be stale (s235 lesson; s236–s257 checks all passed).** **Budget: $5/day UTC — check `date -u`; s257 spent $0.00 (UTC day
2026-07-19 total $0.00 of $5 — s254/s255/s256/s257 all ran this fresh day; a full DAIS-scale probe fits if a real question is owed).** **JST:
s252–s257 all skipped the site (maintenance-only); no JST 2026-07-19 entry exists — a substantive s258 on JST 2026-07-19 CREATES it.**
**RECONCILE: ZERO decisions open** (75 resolved). No track is starving → **s258 has genuine freedom**: an empirical probe needs a
genuinely-new in-repo-anchorable question (budget is not the constraint — a real *question* is; do not manufacture one); a
shadow-depth v5 edition needs ≥2 genuinely-new controlled rows (≈1 now); own-panel preemption stays DECLINED (seventeen sessions); A3c
stays DECLINED as padding (named s254 — just confirm no new $0/anchored item surfaced); the A4b ladder gate is process-ahead-of-need;
Rhee is the last (shallow) uningested scout candidate; **else verify/stop without padding, exactly as s252–s257 did — and if `origin/main`
is STILL unchanged from s257, fast-confirm-and-stop rather than re-sweep (s254's six-check stands as the deep audit).** End
squash-merged to `main`.
