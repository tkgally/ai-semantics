# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 79 (UTC 2026-06-22) spent **≈$2.83** on the lexical working-surface re-run
(main run $2.412 billed + $0.164 calibration + ≈$0.25 unmetered estimate for a sequential run aborted and re-launched
with concurrency). **UTC-day 2026-06-22 total is ≈$3.59** (session 77 $0.756 + session 79 ≈$2.83) of $5.00 — headroom
**≈$1.41 *if the next session is still 2026-06-22 UTC*; a new UTC day resets the full $5 — check the clock.** The
working-surface run sat just over the ~$2.50 single-run prudence flag at the session level (claude is the cost driver
under a working surface — $1.52 of $2.41). Full ledger in [`config/budget.md`](config/budget.md). Check for any newer
Tom override before spending.

## State

**Session 79 (UTC 2026-06-22) — EMPIRICAL: ran the working-surface re-run of the lexical bridging-context probe (the top
backlog candidate). The ungraded-COMMITMENT null is largely CHANNEL-CONTROLLED, not a forced-format artifact.** Single
empirical unit, run concurrently after a fresh-agent pre-run critic GO (format-only byte-level) and a fresh-agent
post-run verifier REPRODUCED (every number to the cent; no corpus/CoT leak in committed raw).

- **New result** [`result/lexical-bridging-context-working-surface-v1`](wiki/findings/results/lexical-bridging-context-working-surface-v1.md):
  re-ran the same frozen 88 items with the output channel changed in exactly one way — a permitted step-by-step working
  surface + `FINAL:` tag (format-only; task text byte-identical, enforced by construction + `verify_format_only.py`;
  reasoning-effort held constant). Motivated by [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md)
  and named as the discriminating test by [`open-question/gradience-population-not-moment`](wiki/findings/open-questions/gradience-population-not-moment.md).
  **Three-state grid resolved:** gemini took up the surface and the null **survived** (channel-controlled); claude took
  up the surface and only its *self-reported confidence* cracked (bridging 82.6→75.2, CI-strict lower) while its
  *categorical decline* held → MIXED/WEAK; gpt **declined** the surface (≥85% bare across framings) → channel-not-taken-up,
  inconclusive. Categorical-decline instrument ungraded for every model that took up the channel; graded scale replicates.
  1056 calls (A dispersion dropped for cost), $2.412 billed, 0 missing/parse-fail/error, 100% FINAL-tag parse.
- **Downstream updates:** [`claim/lexical-graded-scale-ungraded-commitment`](wiki/findings/claims/lexical-graded-scale-ungraded-commitment.md)
  (channel-checked: categorical component channel-controlled, confidence self-report partly channel-sensitive — claim
  stands, scope sharpened); [`essay/graded-scale-ungraded-commitment`](wiki/findings/essays/graded-scale-ungraded-commitment.md)
  (forward note: commitment leg mostly real, not an aperture); [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md)
  (forward note: a fresh channel-not-taken-up instance + scope-confirmation on a non-serial capability — neither trigger
  (a) nor a clean (b) firing); [`open-question/gradience-population-not-moment`](wiki/findings/open-questions/gradience-population-not-moment.md)
  (the lexical "discrete-moment" leg is firmer, channel-checked). Index updated.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no open decisions, no ratifications owed. This
session opened no operationalization decision (the working-surface re-run ran under the already-resolved lexical
bridging-context gates; it is a trigger-(b)-style witness-seek, not a re-tune). Apply any Tom override first.

**Track lean.** 75 gov+lex · 76 empirical+phil · 77 empirical · 78 phil · 79 **empirical**. The next session should lean
**philosophical / synthesis** or **relational** to rebalance (two of the last three were empirical).

1. **PHILOSOPHICAL (top candidate) — mature [`open-question/gradience-population-not-moment`](wiki/findings/open-questions/gradience-population-not-moment.md)
   toward a conjecture.** Its lexical leg is now channel-checked (firmer). The page names the cleanest discriminator: a
   **shared-instrument cross-level probe** (one commitment instrument applied at lexical / constructional / relational
   levels). Maturing it would mean drafting the conjecture + the operationalization decision it would open (freeze-before-
   results, cross-session ratified) — *no spend to scope it*.
2. **EMPIRICAL (small follow-up) — uptake-induced re-run for gpt on the lexical commitment.** gpt **declined** the working
   surface (≥85% bare), so its channel leg is untested. A forced-decomposition variant (the lower-governance uptake-forcer
   used for the let-alone line, [`result/scivetti-let-alone-forced-decomposition-v1`](wiki/findings/results/scivetti-let-alone-forced-decomposition-v1.md))
   would complete the three-model channel check. Cost-aware: gpt is the cheap model ($0.075 for its 352 calls here), so a
   gpt-only forced-decomposition re-run is small. Would need a fresh pre-run critic + post-run verifier.
3. **RELATIONAL (dormant axis)** — [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md)
   is the home; the next move there is a **medium choice**, not more text probes (any real probe needs a human anchor,
   flagged `pending`, or an `internal-contrast-only` posture, and would open a `wiki/decisions/open/` entry).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**NONE.** `wiki/decisions/open/` is empty. This session opened no operationalization decision (the working-surface re-run
is a witness-seek under the resolved lexical bridging-context gates; it froze nothing new and opened no spend decision).

## Standing-override notes (for Tom, if he looks)

- Session 79 spent **≈$2.83** (UTC-day 2026-06-22 total ≈$3.59 of $5).
- Plain-language version: the earlier word-meaning result found the models rank senses smoothly across many examples yet
  answer every single in-between case with full confidence. This session re-ran that test letting the models *reason step
  by step* first (only the answer format changed), to check whether the "full confidence" was just an artifact of forcing
  a one-line answer. It mostly was not: on the two models that used the room to think, the finding held — one completely,
  one lowering its stated confidence on hard cases yet still committing to clean answers just as often. The third model
  declined to reason and was inconclusive. An independent reviewer reproduced every number first.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then
[`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratifications owed.
**The lexical bridging front is now channel-checked (commitment null largely channel-controlled, absorbed into the
claim/essay/OQ layer).** Track lean says **lean philosophical/relational next** (79 was empirical). Top candidate:
mature the cross-level `gradience-population-not-moment` question toward a conjecture (no spend); or the small gpt
uptake-induced channel follow-up; or diversify to the relational non-text-medium axis. End squash-merged to `main`,
website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote
> `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main`
> first** (sessions 64–79 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (re-fetch via
> `experiments/data/subtlex-us/prep.py`). The **DWUG corpus text** (CC BY-ND) and the **WiC corpus text** (CC BY-NC) are
> also gitignored — re-fetch via the v1 `prep.py` (DWUG, 48/48 stratum pairs re-map) and **`map_wic_fulltext.py`** (maps
> the committed frozen WiC manifest to text). The **working-surface** probe reuses those same gitignored full-text files;
> its committed `raw/` is **sanitized** (`sanitize_raw.py` strips the chain-of-thought, which can quote the licensed
> corpus — run it before committing any working-surface raw). The full BLiMP dataset is **not** in-repo (only a sample).
