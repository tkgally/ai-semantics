# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did the s227 particle-fold that *already existed on main* before catching it (the redundant PR was closed
unmerged, the branch reset, real work lost to rework). **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**, do not
build on the stale tree. **(s236 AND s237 cold-start checks both PASSED — the discipline works when followed.)**

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s237 spent $0.003953** (one non-Anthropic decorrelation vote on a $0 governance review; everything else
harness-model). Day total UTC **2026-07-16** (sessions 235 $1.311600 + 236 $0.00 + 237 $0.003953) =
**$1.315553 of $5.00** (~**$3.68** headroom). Ledger: [`config/budget.md`](config/budget.md).
**s238: recompute the UTC day from `date -u`** — s237 ran UTC 2026-07-16 ~08:45, so a same-day s238 has
~$3.68 left; a new UTC day 2026-07-17 → full $5. Recompute the JST website day too (s235/s236/s237 all
landed in the JST 2026-07-16 entry).

## State — s237 ($0.003953): GOVERNANCE — the A3b/C8 BLiMP swap line was reviewed at its twice-controlled ceiling → STOP-FOR-NOW-WITH-CONDITIONS. No finding moved; R1 unchanged.

The deepest genuinely-owed unit was the **instrument-line-continuation review** the PROTOCOL §3 governor
required before any third swap-type arm. Two swap arms have run (s210 SUBTLEX-matched → SWAP-INCONCLUSIVE;
s235 dual-band C4-matched → STILL-INCONCLUSIVE), so a verb-swap arm would be the **third redesign on R1** and
trips the governor. Conducted the review; did **not** run the arm. Done:

- **Verdict: STOP-FOR-NOW-WITH-CONDITIONS** — a fresh independent adversarial reviewer (verdict authority) +
  a convergent non-Anthropic decorrelation vote (`gpt-5.4-mini`, $0.003953, **STOP-AT-CEILING**). The
  **decisive ground**: **no swap arm can promote R1** — construction-frequency (not lexical identity) is the
  binding uncontrolled alternative, and every swap arm holds the construction fixed. Even a best-case
  verb-swap SWAP-STABLE leaves R1 not construction-frequency-controlled, single-run (replication owed), and a
  DROP interpretively muddy. Anti-cheat: both flag the pull to run the third arm as coverage/completionism,
  not information economics → supports STOP.
- **Reopening conditions (written into the note):** (1) a **construction-frequency instrument** — a
  *different* instrument, not a third swap — becomes buildable and R1 survives partialling it out;
  (2) a goal-flip from "promote R1" to "cleanly establish R1 rides on exposure"; (3) Tom / a C8-gate change.
  Absent one of these, **a verb-swap arm is NOT owed and NOT to be run** (running it is the padded "busy" move
  the governor forbids).
- **Artifacts:** [`note/blimp-swap-line-continuation-review-v1`](wiki/findings/notes/blimp-swap-line-continuation-review-v1.md)
  (`recorded`, `anchor: human-anchored`, no new measurement — never cite as claim support) + a dated STOP
  annotation on the [`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md) form-(iv)
  box (a continuation of the same s235-annotated revision-trigger bullet — **no new edition, no number/reading
  changed**) + program A3b tick. **R1 stays descriptive/non-promotable, unchanged; the C8 chain stays closed.**
- **Verify:** senselint **0 errors** / linkify clean / build-index regenerated (notes 19→20). Website:
  **EXTENDED** the JST 2026-07-16 entry (dateline → sessions 235–237, a blue s237 pill + one paragraph) +
  home Last-updated/Current-focus/Spending/"The latest" mirrored.

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s237 resolved no decisions and opened NONE** (a §3 governance review recorded as a `note`, not a decision
trail). So s238 cold-start RECONCILE is a **no-op** (73 resolved; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s238 (PROTOCOL §3: fewer, deeper) — pick the deepest genuinely-owed unit, or STOP

Recent lean: **s235 empirical (run), s236 phil, s237 governance/consol.** Two-track balance is ~even — **no
forced weighting.** Pick the deepest genuinely-owed unit; if nothing substantive is owed, reconcile/verify/**stop**
(do NOT pad; PROTOCOL §3 + charter §12).

1. **(EMPIRICAL — the honest highest-information candidate, but check tractability first.)** The s237 review
   named the best marginal spend as a **powered-magnitude re-run on an already-promoted, magnitude-deferred
   claim** (the claims layer is what compounds): candidates are the **particle-placement** claim
   ([`claim/particle-placement-givenness`](wiki/findings/claims/particle-placement-givenness.md), promoted
   direction-only s229, no magnitude) or the **genitive** claim
   ([`claim/genitive-alternation-animacy`](wiki/findings/claims/genitive-alternation-animacy.md), promoted
   direction-only s221, magnitude partly measured s222 — check whether a *fresh-item powered* magnitude is
   still owed or already discharged before re-running; do NOT re-grind s222). A powered re-run is a real
   strengthening (~$1–1.5, powered N ~100–150). Confirm the claim genuinely lacks a powered independent
   magnitude before designing — else this is a forbidden re-grind.
2. **(EMPIRICAL — a NEW line, if #1 is already discharged.)** The **A2b license-checked graded-image
   fine-polysemy sense-set SCOUT** (a $0 scout only — the grounding magnitude is un-instrumentable with
   in-repo resources; see [`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md));
   OR a within-family **A4b ladder** first-substep (the `ladder:` senselint gate). Each opens a decision only
   a later session can ratify.
3. **(PHIL/CONSOL — check for a genuine trigger, do NOT manufacture one.)** A fresh-agent scout of the three
   PROTOCOL §3 trigger types (theory pages >3 update boxes; fired-but-unacted essay triggers; $0-answerable
   open-questions). s233/s234 found none fired; s236 discharged the one the s235 result fired; s237 moved no
   finding — so **most likely nothing new is owed** here. If so, do NOT re-scout as a fresh unit (a forbidden
   re-grind).

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` (a build also needs
  **openpyxl + nltk**; nltk data `punkt`/`punkt_tab`/`averaged_perceptron_tagger[_eng]` may need
  `nltk.download`). s237 needed none of this (no probe — one vote via `experiments/lib/openrouter.py`).
- **Non-Anthropic vote recipe (carry):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`),
  cutoff-aware preamble, `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.004). The s237 vote script is a clean
  template: [`experiments/runs/2026-07-16-blimp-swap-line-continuation-review/vote-continuation.py`](experiments/runs/2026-07-16-blimp-swap-line-continuation-review/vote-continuation.py).
- **C4 stream is reachable** through the proxy (allenai/c4 shards via HuggingFace, 302→CDN; ~22.3M sentences
  over 3 shards ≈ 15–25 min, $0 model cost). The `build_cooc_c4.py` adapter at
  `experiments/runs/2026-07-08-relation-recovery-taxonomic-proxy/` is import-pinned; do NOT re-adopt.
- **⚠ COST (carry):** a full 3-model 7,200-call 2AFC BLiMP panel ran **$1.31–1.34** (claude dominates ~$0.82;
  gemini cheap ~$0.28 with reasoning suppressed; gpt ~$0.21). A powered alternation re-run (~2,000 calls)
  ran **$3.18** (s229). `ABORT_USD` per-model bounds each but **not** the day cap.
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign=true` via the
  `/tmp/code-sign` wrapper. Commits **are** signed (gpgsig SSH header present) but **cannot be verified
  locally** (no `allowedSignersFile`, no `ssh-keygen`; the signing pubkey file is 0 bytes); `git log %G?`
  shows `N` and the stop-hook flags "Unverified" — a **local-verify false positive**, not a defect. GitHub
  verifies them via the registered key; the squash-merge lands verified.
- **Run-launch (when a probe is actually owed):** launch `python3 probe.py --model A|B|C` and build scripts
  **directly** with `run_in_background: true` (no `nohup`/`&`); rely on the completion notification.
  Blind-scoring lock (B4): run ALL 3 models before `analyze`. Never name-match to detect completion.

## ⚠ Do-not-re-grind (in force)

- **(s237) The A3b/C8 swap-line continuation review is DONE → STOP-FOR-NOW-WITH-CONDITIONS.** Do NOT re-run
  the review, do NOT design/run a verb-swap arm, do NOT re-open the C8 chain — **unless a written reopening
  condition fires** (a construction-frequency instrument; a goal-flip; Tom / a C8-gate change). The verb-swap
  arm is not owed.
- **(s236) The essay reconciliation is DONE.** `essay/shadow-depth-cross-cuts-grain` is reconciled to the
  s235 result. Do NOT re-revise it for the same result, re-open the s211/s236 boxes, or manufacture a fresh
  essay trigger from the same evidence.
- **(s235) The C4-matched swap arm RAN → STILL-INCONCLUSIVE.** Do NOT re-run/retune the frozen dir, re-stream
  C4, re-analyze, or re-open the decision. R1 is unchanged.
- **(s227–s229) The particle-placement line is CONSOLIDATED** (v1 s226, rep2 s229, promoted direction-only
  2/3-firewall `claim`, folded into shadow-depth-table-v4). Do NOT re-run/re-fold/re-promote — **but a
  fresh-item powered MAGNITUDE re-run is still legitimately owed** (the claim is direction-only, no magnitude;
  s237 named it the best marginal spend — that is s238 candidate #1, NOT a re-grind).
- **(s221–s222) genitive fully consolidated** (direction s221, magnitude partly measured s222 — check whether
  a fresh-item powered magnitude is still owed before touching); **(s175) dative; (s169) CC.** Do NOT
  re-run/re-fold the settled parts.
- **(s233/s234) The tight-day maintenance touches are done**; (s183) do NOT re-audit the whole wiki;
  (s168–) no corpus/dataset adoption without a verified license.

## Open decisions

**ZERO open** — s237 resolved none and opened none. **73 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session made a deliberate decision to **stop** a line of experiments rather than spend more on it. Over
the last weeks the project ran two versions of a "swap the ordinary words, keep the grammar" check, trying to
tell whether the models are genuinely good at hard grammar or just echoing famous test sentences they'd seen
in training. Both came back "can't tell yet." The obvious next move was a third version (also swapping the
verbs). An independent review — with an outside-company model as a second opinion, both agreeing — concluded
that no word-swap version can actually settle the question, because swapping words always leaves the
*construction* the same, and the real open doubt is whether the models do well on a construction just because
it's *common* in training text. So the honest call was to rest the line at its twice-checked ceiling, save
the budget for work that can move a result, and write down the exact condition under which the line would
reopen (the day a different, construction-frequency test becomes buildable). Nothing in the project's map of
findings moved; the only money spent was a fraction of a cent on the outside vote. A line anywhere in the
repo outranks this note.

## Reminder for the next cold-start

**You are session 238.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **FIRST: `git fetch --prune &&
git checkout -B <branch> origin/main` and confirm `origin/main` is at s237 — the checkout can be stale (s235
lesson; s236 + s237 checks both passed).** **Budget: $5/day UTC — check `date -u`; s237 spent $0.003953 (UTC
2026-07-16 day total $1.315553 with s235/s236, ~$3.68 left if same day).** **RECONCILE: ZERO decisions open.**
**Two-track balance ~even** — no forced weighting. **Deepest genuinely-owed candidate:** a **powered-magnitude
re-run on an already-promoted magnitude-deferred claim** (particle-placement or genitive — confirm the
magnitude is genuinely still owed, do NOT re-grind), else a $0 A2b scout / A4b ladder substep, else if nothing
substantive is owed reconcile/verify/**stop** — do NOT pad. Do NOT: run a verb-swap BLiMP arm (the s237 review
stopped that line; not owed unless a reopening condition fires), re-revise the reconciled essay, re-run the
frozen C4 dir. End squash-merged to `main`.
