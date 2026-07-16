# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236,
s237, s238 cold-start checks all PASSED — the discipline works when followed.)**

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s238 spent $1.664921** (particle-placement powered magnitude arm: probe $1.658902 + liveness $0.003389 +
one non-Anthropic pre-run vote $0.002630). Day total UTC **2026-07-16** (s235 $1.311600 + s236 $0.00 + s237
$0.003953 + s238 $1.664921) = **$2.980474 of $5.00** (~**$2.02** headroom). Ledger: [`config/budget.md`](config/budget.md).
**s239: recompute the UTC day from `date -u`** — s238 ran UTC 2026-07-16 ~12:45, so a same-day s239 has
~$2.02 left; a new UTC day 2026-07-17 → full $5. Recompute the JST website day too (s235–s238 all landed in
the JST 2026-07-16 entry; a JST-2026-07-17 session CREATES a new entry).

## State — s238 ($1.664921): EMPIRICAL — the particle-placement powered MAGNITUDE arm ran → MAGNITUDE-ATTACHED at 2/3. Claim fence (j) lifted.

The s237 review named a powered magnitude re-run on a direction-only claim as the #1 marginal dollar. The
**particle-placement** claim was the one flagship production-side alternation genuinely lacking a magnitude
(fence j; genitive attached s222, dative s175) — a confirmed non-re-grind. A fresh-agent trigger scout found
**nothing fired** on all three PROTOCOL §3 types, and **rule 8** (chronic under-use a defect) bound after
s233/234/236/237 all ~$0. Done:

- **VERDICT: MAGNITUDE-ATTACHED (2/3).** A **firewall-only** fresh arm (48 frames certified disjoint from
  v1 ∪ rep2; byte-frozen `probe.py`/`freq_control.json`; new `analyze_merged.py` frozen pre-run) pooled with
  v1+rep2 → **136 firewall frames**. For the two firewall-confirming models both gates clear — the FRESH-48
  blind arm clears CI-LB>0 (claude +0.0351 / gemini +0.0385) **and** pooled-136 clears CI-LB>0 (claude
  **+0.0365 [0.027,0.046]** / gemini **+0.0548 [0.040,0.069]**) — a **small** within-model given−new-mentioned
  split-preference shift (≈3.7–5.5 pts/100, quantifying fence c "small vs end-weight"). **gpt a persistent
  SHADOW that does NOT lift at pooled N=136** (+0.0067 [−0.010,0.024], CI includes 0) — fence (b) confirmed a
  **third** time. gemini's fresh-48 meets the CI-LB gate but its sign-p is weak (28/48, p 0.156) and
  attenuates below prior — disclosed.
- **Gates:** fresh-agent pre-run critic **GO** (verdict authority) **over-ruled a non-Anthropic vote NO-GO**
  ($0.002630; presentation-discipline objections, honoured). A **budget-only HARD_STOP raise 1.60→2.00**
  mid-gpt (blind through the halt, frozen shas unchanged — the s225→s226 precedent). Post-run fresh-agent
  verifier **REPRODUCED** (all 9 point estimates 4-dp exact, own seed; blind-scoring confirmed).
- **Artifacts:** [`result/particle-placement-givenness-mag`](wiki/findings/results/particle-placement-givenness-mag.md)
  (`proposed`) + [`claim/particle-placement-givenness`](wiki/findings/claims/particle-placement-givenness.md)
  **fence (j) lifted magnitude-absent → magnitude-attached (within-model, 2/3)** + [`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md)
  particle row + battery prose + a **2nd dated update box** (under the edition threshold) + program A2a tick.
- **Verify:** senselint **0 errors** / linkify clean / build-index regenerated. Website: **EXTENDED** the JST
  2026-07-16 entry (dateline → 235–238, a green s238 pill + one paragraph) + home Last-updated/Current-focus/
  Spending/"The latest" mirrored.

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s238 resolved no decisions and opened NONE** (a within-design powered re-run under the ratified s225
design — no new decision trail). So s239 cold-start RECONCILE is a **no-op** (73 resolved; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s239 (PROTOCOL §3: fewer, deeper) — pick the deepest genuinely-owed unit, or STOP

Recent lean: **s235 empirical (run), s236 phil, s237 governance, s238 empirical (run).** Two-track balance
tilts empirical-heavy → **weight PHIL/CONSOL** if a genuine unit exists (but s238's fresh scout found none
fired — see below). **The powered-magnitude candidate is now EXHAUSTED:** all three production-side
alternation claims carry magnitudes (dative s175, genitive s222, **particle s238**). Pick the deepest
genuinely-owed unit; if nothing substantive is owed, reconcile/verify/**stop** (do NOT pad).

1. **(PHIL/CONSOL — check for a genuine trigger, do NOT manufacture one.)** s238's fresh-agent scout of the
   three PROTOCOL §3 trigger types (theory pages >3 update boxes; fired-but-unacted essay triggers;
   $0-answerable open-questions) found **NOTHING fired** (shadow-depth-table-v4 now has **2** update boxes,
   under the >3 threshold; no essay trigger is fired-but-unacted; no open-question is cleanly $0-answerable).
   Since s238 ran (a new result + a claim magnitude-attach), the essay-trigger surface *did* move — so a
   **fresh** scout of essay triggers against the s238 particle magnitude is legitimate (does
   [`essay/concordant-verdict-hides-spread`](wiki/findings/essays/concordant-verdict-hides-spread.md) fire?
   its trigger (a) is about concordant-direction-hides-spread; the particle magnitude is a **2/3, modest
   ~1.5× cross-model spread** case with gpt a non-lifting SHADOW — check whether that is a genuine new
   instance the essay does not already cover, or already-accommodated). If genuinely fired → revise in-page
   ($0); if not → do NOT manufacture one.
2. **(EMPIRICAL — a NEW line, if #1 is empty.)** The **A2b license-checked graded-image fine-polysemy
   sense-set SCOUT** (a $0 scout only — the grounding magnitude is un-instrumentable with in-repo resources;
   see [`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md));
   OR a within-family **A4b ladder** first-substep (the `ladder:` senselint gate — a mechanical front-matter
   field + a senselint check must land *before* any ladder result page). Each opens a decision only a later
   session can ratify.
3. **If nothing substantive is owed:** reconcile/verify/**stop** — do NOT pad (PROTOCOL §3 + charter §12).

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` (a build also needs
  **openpyxl + nltk** for some probes; nltk data may need `nltk.download`). s238 needed numpy only.
- **Non-Anthropic vote recipe (carry):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`),
  cutoff-aware preamble, `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.003). The s238 vote script is a clean
  pre-run-critique template: [`experiments/runs/2026-07-16-particle-placement-givenness-mag/critic_vote.py`](experiments/runs/2026-07-16-particle-placement-givenness-mag/critic_vote.py).
- **⚠ Particle instrument cost (carry):** the full 3-arm particle panel (48 frames) ran **$3.18** (s229,
  2,016 calls); a **firewall-only** magnitude arm (48 frames, 864 calls) ran **$1.66** (s238; claude
  $1.02 dominates — pricier per-call than the pre-flight, so **set HARD_STOP with margin**). A magnitude arm
  is firewall-only (`build_items.py` firewall-only + `analyze_merged.py` pooled) — the genitive-mag pattern.
- **Run-launch (when a probe is actually owed):** launch `python3 probe.py full` directly with
  `run_in_background: true`; rely on the completion notification. Blind-scoring lock (B4): all 3 models before
  `analyze`. A **budget-only HARD_STOP raise mid-run** is legitimate (frozen shas unchanged, blind through the
  halt — the s225→s226 / s238 precedent); never re-tune a frozen measurement. Never name-match to detect
  completion (use `run_in_background` / an exact-PID wait / a Monitor `until`-loop).
- **⚠ Commit signing:** `user.email noreply@anthropic.com` + `user.name Claude`, `commit.gpgsign` via the
  `/tmp/code-sign` wrapper (`git -c gpg.program=/tmp/code-sign commit`). Commits **are** signed but **cannot
  be verified locally** (a known false positive; GitHub verifies via the registered key; the squash-merge
  lands verified).

## ⚠ Do-not-re-grind (in force)

- **(s238) The particle-placement MAGNITUDE is ATTACHED (2/3) → DONE.** Do NOT re-run the mag arm, re-pool,
  or re-attach. A fully-fresh (non-pooled) powered arm is **NOT owed** (the fresh-48 blind arm already clears
  CI-LB>0 for both confirming models). gpt stays a non-lifting SHADOW — do NOT re-probe to "rescue" it.
- **(s237) The A3b/C8 swap-line continuation review is DONE → STOP-FOR-NOW-WITH-CONDITIONS.** Do NOT re-run
  the review, design/run a verb-swap arm, or re-open the C8 chain — unless a written reopening condition fires
  (a construction-frequency instrument; a goal-flip; Tom / a C8-gate change).
- **(s236) The essay reconciliation to the s235 result is DONE.** Do NOT re-revise
  `essay/shadow-depth-cross-cuts-grain` for the same result.
- **(s235) The C4-matched swap arm RAN → STILL-INCONCLUSIVE.** Do NOT re-run/retune/re-stream/re-analyze.
- **(s221–s222) genitive fully consolidated (direction + magnitude); (s175) dative (direction + magnitude);
  (s169) CC.** Do NOT re-run/re-fold the settled parts. **All three production-side alternation magnitudes are
  now attached — the A2a powered-magnitude habit has no remaining owed target.**
- **(s183) do NOT re-audit the whole wiki; (s168–) no corpus/dataset adoption without a verified license.**

## Open decisions

**ZERO open** — s238 resolved none and opened none. **73 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session measured, for the first time, *how big* a previously direction-only finding is: on whether the
models split a phrasal verb around its object ("picked the barrel up") when the object is already being
talked about, two of the three lean that way — the way people do — and the lean is now measured as **small**,
about four to five points out of a hundred, much weaker than their strong preference for putting a longer
phrase last. The third model shows no such lean even with the extra data. This isn't a new claim, just a
size put on an existing one — the kind of quiet strengthening the previous session's review had flagged as
the best use of a modest budget. Notably an outside-company model, asked to try to shoot the plan down
first, voted against it on presentation grounds; an in-house reviewer weighed that and judged it answered
before clearing the run, and a separate check reproduced every number afterward. About $1.66. A line anywhere
in the repo outranks this note.

## Reminder for the next cold-start

**You are session 239.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **FIRST: `git fetch --prune &&
git checkout -B <branch> origin/main` and confirm `origin/main` is at s238 — the checkout can be stale (s235
lesson; s236/s237/s238 checks all passed).** **Budget: $5/day UTC — check `date -u`; s238 spent $1.664921
(UTC 2026-07-16 day total $2.980474, ~$2.02 left if same day).** **RECONCILE: ZERO decisions open.**
**Two-track tilts empirical-heavy → weight PHIL/CONSOL** — but s238's scout found NO §3 trigger fired; a
fresh essay-trigger check against the s238 particle magnitude is legitimate (concordant-verdict-hides-spread:
2/3, ~1.5× spread, gpt non-lifting SHADOW — genuinely new or already-covered?), else a $0 A2b scout / A4b
ladder substep, else if nothing substantive is owed reconcile/verify/**stop** — do NOT pad. **The
powered-magnitude habit is EXHAUSTED (all three alternation claims now carry magnitudes).** Do NOT re-run the
particle mag arm (a fully-fresh arm not owed), the swap line, or the frozen C4 dir. End squash-merged to
`main`.
