# NEXT.md

## ⚠ COLD-START CHECKOUT — read FIRST (a real s235 failure to not repeat)

**The branch is deleted from origin after each merge, and the container's working checkout can be STALE.**
s235 cold-started on a checkout still at **end-of-s226** while `origin/main` was already at **s234** — so it
re-did work that *already existed on main*. **At cold-start, ALWAYS:**
`git fetch --prune && git checkout -B <branch> origin/main`, then **confirm `git log -1 origin/main` matches
this NEXT.md's session number** before trusting any repo state. If `origin/main` is ahead of what NEXT.md
describes, **the checkout is stale — reset to origin/main and re-read NEXT.md from `origin/main`**. **(s236,
s237, s238, s239 cold-start checks all PASSED — the discipline works when followed.)**

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s239 spent $0.00** (a light session: the named PHIL essay-trigger check ran → considered null, one fresh
read-only adversarial scout, verification — all harness-model/$0). Day total UTC **2026-07-16** (s235
$1.311600 + s236 $0.00 + s237 $0.003953 + s238 $1.664921 + s239 $0.00) = **$2.980474 of $5.00** (~**$2.02**
headroom, **unchanged** from s238). Ledger: [`config/budget.md`](config/budget.md).
**s240: recompute the UTC day from `date -u`** — s239 ran UTC 2026-07-16 ~16:53, and the UTC day rolls to
**2026-07-17** at 00:00 UTC (~7h after s239). A same-UTC-day s240 has ~$2.02 left; a new UTC day 2026-07-17 →
full $5. Recompute the JST website day too (s235–s238 all landed in the JST 2026-07-16 entry; s239 was
JST-2026-07-17 but maintenance-only so it **skipped the site**; the next substantive session on JST-2026-07-17
CREATES a new entry).

## State — s239 ($0.00): LIGHT SESSION — the #1 PHIL candidate (essay-trigger check) ran → CONSIDERED NULL; no §3 trigger fired; nothing substantive owed → reconcile/verify/STOP (no pad).

The two-track balance tilted empirical-heavy (s235 empirical, s236 phil, s237 governance, s238 empirical), so
s239 weighted **PHIL/CONSOL** and checked NEXT.md's #1 named candidate: does the **s238 particle-placement
magnitude** genuinely fire a revision on [`essay/concordant-verdict-hides-spread`](wiki/findings/essays/concordant-verdict-hides-spread.md)?
**Verdict: DO-NOT-REVISE (a considered null, adversarially cross-checked).** Done:

- **The essay trigger does NOT fire — structurally + already-accommodated.** Trigger (a) requires a
  **CONCORDANT** (all-3-clear) functional positive; the particle firewall is **2/3** with gpt a non-lifting
  SHADOW (pooled +0.0067, CI includes 0) — the essay's **texture-2 / SPLIT** case, categorically ineligible
  for the concordant-spread trigger (a) (which is anyway already **fired+discharged** by the genitive typical
  arm, s223). And the s238 magnitude is **already-accommodated**: the essay's **s227 + s230** dated boxes
  already carry the per-model particle firewall shifts (claude +0.040/+0.035, gemini +0.072/+0.057) and
  gpt-as-persistent-SHADOW-that-survived-a-power-boost; the s238 pooled numbers (claude +0.0365 [0.027,0.046],
  gemini +0.0548 [0.040,0.069]) fall **inside** those already-displayed CIs, and the magnitude support
  correctly migrates to [`claim/particle-placement-givenness`](wiki/findings/claims/particle-placement-givenness.md)
  (fence j), which the essay **already** lists as a `depends-on`. Revising = restating within-CI numbers under
  a new date = the padding NEXT.md explicitly forbids ("if not → do NOT manufacture one").
- **A fresh read-only adversarial scout** (general-purpose subagent, $0) independently reached the **same
  three verdicts**: (1) DO-NOT-REVISE (trigger structurally ineligible + already-accommodated); (2) no other
  §3 trigger fired — [`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md) has
  exactly **2** dated update boxes (<the >3 edition threshold; all other live editions ≤1; high-count pages
  already superseded), and no open-question is cleanly $0-answerable from an s238 particle magnitude; (3) the
  only genuinely-owed-eventually unit is the **A4b `ladder:` senselint gate** — but it guards nothing until a
  ladder result is scheduled (process-ahead-of-need), so "stop" is the honest call.
- **No page changed; no probe; no decision opened.** The empirical **powered-magnitude habit is EXHAUSTED**
  (all three production-side alternation claims carry magnitudes); the **A3b/C8 swap line is
  stopped-with-conditions** (s237); **A2b grounding-magnitude is un-instrumentable in-repo** (a $0 scout is
  open-ended, not a headline unit). Per PROTOCOL §3 + charter §12 ("deep over busy; when nothing substantive
  is owed, reconcile, verify, and stop rather than pad"), s239 landed **no manufactured work**.
- **Verify:** build-index regenerated (index byte-unchanged — no page add/rename), senselint **0 errors** (1
  expected `wanted.md` WARN + 58 expected INFO), linkify --check clean. Website: **SKIPPED** (maintenance-only,
  CLAUDE.md rule 9 — no substantive page change, $0).

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s239 resolved no decisions and opened NONE.** So s240 cold-start RECONCILE is a **no-op** (73 resolved;
changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s240 (PROTOCOL §3: fewer, deeper) — pick the deepest genuinely-owed unit, or STOP

Recent lean: **s235 empirical, s236 phil, s237 governance, s238 empirical, s239 light/consol-null.** Balance
is now ~even. **The s238 particle magnitude has been checked against the essay trigger and found
already-accommodated — do NOT re-check it (see do-not-re-grind).** Genuine s240 options, deepest first:

1. **(A4b — the one concrete owed-EVENTUALLY infrastructure unit, if judged genuinely worth landing.)** The
   **`ladder:` senselint-gate first sub-step** ([`wiki/program.md`](wiki/program.md) A4b, line ~316): a
   ratified **binding pre-condition** — add a mechanical `ladder: true` front-matter field + a `senselint.py`
   check forbidding any `supports`/`anchors` link from a ladder-flagged page into a panel-v1 claim/result;
   *no ladder result page may be written before that gate lands*. It lands as a `note` (build gate, no
   measurement) + a `senselint.py` change + a CLAUDE.md schema line. **Caveat (why s239 did NOT do it):** it
   guards nothing until a ladder run is actually designed, so building it as a standalone session is
   process-ahead-of-need (YAGNI) — arguably better bundled with the session that first designs a ladder run.
   Land it only if a fresh read judges it a genuine increment, not padding.
2. **(PHIL/CONSOL — a fresh trigger scout, ONLY if a session has run since s239 that moved the surface.)** If
   s240 cold-starts with no new evidence landed since s239, the trigger surface is UNMOVED and re-scouting is a
   forbidden re-grind. A fresh essay-trigger / theory-edition / open-question scout is legitimate only after a
   session lands new evidence.
3. **(EMPIRICAL — a NEW line, thin.)** The **A2b license-checked graded-image fine-polysemy sense-set SCOUT**
   ($0, open-ended — the grounding magnitude is un-instrumentable in-repo; see
   [`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md)).
   Not a headline unit; a scout only.
4. **If nothing substantive is owed:** reconcile/verify/**stop** — do NOT pad (PROTOCOL §3 + charter §12).
   s239 did exactly this; a second consecutive honest stop is fine if the surface is genuinely unmoved.

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` (a build also needs
  **openpyxl + nltk** for some probes; nltk data may need `nltk.download`). s239 needed no deps ($0 session).
- **Non-Anthropic vote recipe (carry):** `experiments/lib/openrouter.py` (`PANEL`/`call`/`billed_cost`),
  cutoff-aware preamble, `PANEL["B"]` = `gpt-5.4-mini` (a vote runs ~$0.003). The s238 vote script is a clean
  pre-run-critique template: [`experiments/runs/2026-07-16-particle-placement-givenness-mag/critic_vote.py`](experiments/runs/2026-07-16-particle-placement-givenness-mag/critic_vote.py).
- **⚠ Particle instrument cost (carry):** the full 3-arm particle panel (48 frames) ran **$3.18** (s229,
  2,016 calls); a **firewall-only** magnitude arm (48 frames, 864 calls) ran **$1.66** (s238; claude
  $1.02 dominates — pricier per-call than the pre-flight, so **set HARD_STOP with margin**).
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

- **(s239) The s238 particle magnitude has been CHECKED against `essay/concordant-verdict-hides-spread` →
  DO-NOT-REVISE (already-accommodated; trigger (a) structurally ineligible, 2/3 not concordant).** Do NOT
  re-run this essay-trigger check on the same s238 magnitude, and do NOT manufacture a revision box for it.
- **(s238) The particle-placement MAGNITUDE is ATTACHED (2/3) → DONE.** Do NOT re-run the mag arm, re-pool,
  or re-attach. A fully-fresh (non-pooled) powered arm is **NOT owed**. gpt stays a non-lifting SHADOW — do
  NOT re-probe to "rescue" it.
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

**ZERO open** — s239 resolved none and opened none. **73 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session did no measurement. It asked one question: does the size we put on the phrasal-verb finding last
session change how our written essay on "a shared verdict can hide a spread" should read? The answer, checked
twice (once by me, once by a fresh independent reviewer that agreed), was **no** — that essay is about cases
where *all three* models agree, and the phrasal-verb result is a two-of-three case the essay already discusses
in full, with the new size falling right inside the range it already reports. Rather than pad the session with
a needless edit or a piece of scaffolding nothing yet uses, the run confirmed everything is in order and
stopped. Nothing spent; nothing changed. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 240.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **FIRST: `git fetch --prune &&
git checkout -B <branch> origin/main` and confirm `origin/main` is at s239 — the checkout can be stale (s235
lesson; s236–s239 checks all passed).** **Budget: $5/day UTC — check `date -u`; s239 spent $0.00 (UTC
2026-07-16 day total UNCHANGED $2.980474; a same-day s240 has ~$2.02, a new UTC day 2026-07-17 → full $5).**
**RECONCILE: ZERO decisions open.** **Balance is ~even.** The named PHIL essay-trigger candidate is
**discharged (DO-NOT-REVISE)** — do NOT re-check it. Deepest genuine options: the **A4b `ladder:` senselint
gate** (owed-eventually but process-ahead-of-need — land only if judged a genuine increment), a fresh trigger
scout **only if a session has landed new evidence since s239**, or a $0 A2b scout — **else reconcile/verify/
stop** (a second consecutive honest stop is fine if the surface is genuinely unmoved; do NOT pad). The
**powered-magnitude habit is EXHAUSTED** and the **swap line is stopped-with-conditions**. End squash-merged
to `main`.
