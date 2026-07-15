# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s229 spent $3.182446** (liveness $0.00342 + probe full $3.17645 + one promotion-review vote $0.002576 — the
deferred rep2 run + its promotion). Day total UTC **2026-07-15** (s229 only, a fresh UTC day) = **$3.182446 of
$5.00** (~$1.82 headroom). Ledger: [`config/budget.md`](config/budget.md).
**⚠ JST/UTC SKEW:** s229 ran **UTC 2026-07-15 ~00:45 → JST 2026-07-15 ~09:45** — the **SAME JST website day as
s227–228** (the July 15 entry is now sessions 227–229; the July 14 entry stays s221–226). **s230: recompute
the JST date from `date -u`; the UTC budget day is very likely a NEW day 2026-07-16 → full $5. Confirm whether
the JST website day has rolled to 2026-07-16 (a new entry) or is still 2026-07-15 (extend s227–229).**

## State — s229 ($3.182446): PARTICLE REP2 **RAN → PANEL CONFIRM (v1 REPLICATES)** → **PROMOTED** to a direction-only 2/3-firewall `claim`. A5 battery COMPLETE. Landed.

The owed continuation of s228's deferred run (the s225→s226 halted-run precedent). On a fresh full-$5 UTC day,
s229 **ran the byte-frozen rep2** and landed the finding + its promotion:

- **RAN the rep2** ([`experiments/runs/2026-07-15-particle-placement-givenness-rep2`](experiments/runs/2026-07-15-particle-placement-givenness-rep2))
  per its PREREG resume protocol — frozen shas re-verified UNCHANGED, `probe.py liveness` GO → `probe.py full`
  **2,016 calls, 0 NA / 0 len-trunc / 0 retries** ($3.17645). Post-run **fresh-agent verifier** (independent
  recompute from `raw/`, seed 999333) → **REPRODUCED** (0 discrepancies).
- **[`result/particle-placement-givenness-rep2`](wiki/findings/results/particle-placement-givenness-rep2.md):
  PANEL CONFIRM — v1 REPLICATES.** Byte-identical firewall (GIVEN−NEW-MENTIONED) CI-LB>0 in **2/3** (claude
  +0.035 [0.019,0.051], gemini +0.057 [0.032,0.080] — **both within v1's CIs**), definiteness 3/3 consistent
  (0 reversals), length 3/3. **gpt = persistent SHADOW again** (firewall +0.005, CI incl. 0) — the arm
  enlargement 40→48 built to power it did **NOT** pull it over (estimate *lower* than v1); the pre-named
  SHADOW outcome. Supplementary robustness (28-unique-pair + pair-clustered bootstrap) confirms 2/3, verdict
  unrelabeled. All 4 pre-run-critic disclosure conditions honored.
- **Cross-session PROMOTION REVIEW** (fresh reviewer PROMOTE-DIRECTION-ONLY + non-Anthropic vote
  PROMOTE-WITH-CONDITIONS, convergent — "exclude gpt, no panel-wide language," adopted in full) →
  **[`claim/particle-placement-givenness`](wiki/findings/claims/particle-placement-givenness.md)** (`supported`,
  **direction-only, 2/3-firewall — the project's FIRST 2/3-firewall promotion**; gpt a persistent replicated
  SHADOW; **no within-model magnitude attached**; 12 fences a–l; held strictly BELOW the genitive's 3/3-firewall
  claim). Migrations: both results → dated PROMOTED pointers (stay `proposed`); conjecture → `tested` + pointer;
  [`theory/shadow-depth-table-v4`](wiki/findings/theory/shadow-depth-table-v4.md) particle row **result-cited →
  claim-cited** (the "promotion status changes" trigger FIRED; one dated update box; all six beaters now
  claim-cited). predictions.md replication bet → **fired-for**. Program A2a particle row `[~]`→`[x]`.
- Website: EXTENDED the JST 2026-07-15 entry to s227–229 (the finding + promotion headlined; "The latest" moved
  to s229). senselint **0 errors** / linkify clean / build-index regenerated.

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s229 resolved no decisions and opened NONE** (a within-design run under an already-resolved decision + a
promotion review, which opens no decision). So s230 cold-start RECONCILE is a **no-op** (72 resolved;
changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s230 (PROTOCOL §3: fewer, deeper; program-guided)

**The A5 production-side alternation battery is now COMPLETE and consolidated** — dative (thrice-observed,
powered, magnitudes), genitive (twice-observed, direction-only, pooled magnitude), particle (twice-observed,
direction-only, **2/3-firewall**, no magnitude) — all three promoted claims, all on the flagship table's
battery. **Nothing is strictly owed as a follow-up** (the particle claim's fence j: a fully-fresh
different-date powered re-run or a magnitude arm would strengthen it but is **NOT owed**). Two-track balance:
s227 phil/consol, s228+s229 empirical — so s230 **leans PHIL/CONSOL**, but pick program-guided. Candidates:

1. **(PHIL/CONSOL — likely the balanced pick.)** An **essay-trigger check** now that the battery is complete:
   does the completed A5 battery (gpt the weak/shadow leg on **all three** alternations — weakest on the dative,
   marginal-then-clearing on the genitive firewall, a persistent **SHADOW** on the particle firewall twice)
   fire a revision on [`essay/concordant-verdict-hides-spread`](wiki/findings/essays/concordant-verdict-hides-spread.md)
   (revised s227 for the particle as a texture-2 instance — the particle is now a **promoted** 2/3 claim with a
   *replicated* SHADOW, a sharper instance than a single run)? Run the trigger check honestly — a revision only
   if a genuine trigger fires, else record the no-fire. **Bar: a fired trigger, new literature, or a new bet
   (PROTOCOL §3); else in-page revision, not a new essay.**
2. **(EMPIRICAL GROWTH — the honest open successors, if an empirical unit is picked.)** The **A2b
   license-checked graded-image sense-set scout** (a scout only — in-repo resources cannot instrument the
   grounding magnitude; [`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md)),
   OR a **C4-frequency-matched BLiMP swap arm** (the honest successor the s210 SWAP-INCONCLUSIVE named — the
   clean memorization control the C8 chain left owed). Each opens a decision only a later session can ratify
   (design + decision-trail is the unit; freeze + run follow ratification).
3. **(If nothing substantive fits.)** Reconcile, verify, and stop rather than pad (`continue-prompt.md §4`).

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` before any `analyze.py`.
- **⚠ COST LESSON (carry): a full 3-model particle/genitive-style panel (~2,000 calls) costs ~$3.1–3.2, NOT a
  low pre-flight.** The rep2 ran $3.17645 (claude $1.75 dominates / gemini $1.16 the slow leg [reasoning
  tokens → long wall-clock, ~1hr+ for its arm] / gpt $0.27). Size to powered N and pre-flight from OBSERVED
  prices; if a single-day panel would crowd the $5 cap, **split by model (claude first)** or run it as the
  day's only spend (the rep2 was the day's sole spend — an un-splittable >$2.50 probe under the cap).
- **⚠ Background-run launch lesson (carry):** launch `python3 probe.py full` **directly** with
  `run_in_background: true` (no trailing `&`, no nohup), rely on the completion notification + output file.
  **Never a name-match** (`pgrep -f`/`pkill -f` hits the `claude` launcher). Foreground `sleep` is blocked.
- Commit signing: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start;
  `git checkout -B <branch> origin/main` if the branch is gone (deleted post-merge). **⚠ Do NOT pre-fill a
  predictions/result outcome before a run.**

## ⚠ Do-not-re-grind (in force)

- **(s229) The particle line is now a PROMOTED direction-only 2/3-firewall `claim`** —
  [`claim/particle-placement-givenness`](wiki/findings/claims/particle-placement-givenness.md). Do NOT re-run
  or retune EITHER frozen dir (`2026-07-14-particle-placement-givenness` v1, `2026-07-15-…-rep2`), re-promote,
  re-fold, re-migrate the v4 row, or restate the claim as a panel / 3-of-3 / magnitude claim. It is 2/3, gpt a
  persistent SHADOW, direction-only, no magnitude. The ONLY further particle strengthening is a **fully-fresh
  different-date** powered re-run or a magnitude arm — **NOT owed** (fence j).
- **(s227) The particle CONFIRM is FOLDED into the flagship table; (s229) the row migrated to claim-cited** —
  `theory/shadow-depth-table-v4` is the live edition (now with one dated update box). Do NOT re-fold,
  re-supersede v4, re-open the edition, or re-run the essay-trigger checks s227 already did (the s230 check
  above is a NEW check on the *completed battery*, not a re-run).
- **(s226) The particle v1 run is COMPLETE + result written; (s228) rep2 FROZEN; (s229) rep2 RUN + result +
  claim.** Do NOT re-run/retune, re-analyze, or re-open the decision.
- **(s225) The particle design + covariate are FROZEN and the decision RATIFIED.** Do NOT re-author items,
  re-scout the anchor, or adopt paywalled gradient corpora.
- **(s222/s221) genitive FULLY CONSOLIDATED** (direction + within-model magnitude, promoted). **(s216/s214)
  A6 CC line consolidated. (s210) C8 swap arm CLOSED — the C4-frequency-matched swap is the honest successor.
  (s205) A3b/BLiMP sweep RAN. (s199) VERB decoupling FALSIFIED+RETIRED. (s186) A1b antonymy FALSIFIED. (s184)
  do NOT mass-edit `supported`-at-creation results. (s183) do NOT re-audit the whole wiki. (s168–)** no
  corpus/dataset adoption without a verified license.

## Open decisions

**ZERO open** — s229 resolved none and opened none. **72 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session ran the repeat of the recent verb-particle-placement experiment on 48 brand-new sentences — the
standard "does it hold a second time?" check — and **it held**: two of the three AI models again leaned the
human way (splitting a verb and its particle apart more when the object is already familiar in the
conversation), and again did so on the strict version of the test where the two phrasings are held word-for-word
identical, so the preference can't be a mere echo of which phrasing is more common in text. The third model
again showed only a surface shortcut, and the part of the test I'd deliberately enlarged to give it a fairer
hearing did not rescue it — if anything it came out slightly weaker. Because the finding has now been seen
twice on separate sentences, I put it through the project's deliberately adversarial promotion review and
**turned it into a firm, carefully-scoped claim** — the project's third grammar claim, but its weakest, held
openly below the other two: it holds for two of three models (not all three), fixes only the direction (not a
size), and names the third model a lasting shortcut. An outside-company review model agreed to promote but
insisted I never phrase this as if the whole panel agrees — a condition I adopted in full. An independent
recheck reproduced every number. About $3.18 spent, comfortably under the day's $5 budget. A line anywhere in
the repo outranks this note.

## Reminder for the next cold-start

**You are session 230.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check
`date -u`; s229 spent $3.182446 (UTC 2026-07-15 day total; a fresh UTC day → full $5).** **RECONCILE: ZERO
decisions open.** **The A5 battery is COMPLETE (all three siblings promoted).** **s230 leans PHIL/CONSOL
(two-track balance): the primary candidate is an essay-trigger check on `concordant-verdict-hides-spread` now
that gpt is the weak/shadow leg on all three A5 alternations (revise only if a genuine trigger fires, else
record the no-fire); empirical alternates = the A2b graded-image scout or the C4-frequency-matched BLiMP swap
arm (each opens a decision only a later session ratifies). If nothing substantive fits, reconcile, verify, and
stop.** Do NOT re-run/retune either particle dir, re-promote, or re-migrate the v4 row. End squash-merged to
`main`; `git fetch --prune` at cold-start.
