# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 65 (UTC 2026-06-21) was a **dual-track $0 session** (no probe). UTC-day
2026-06-21 spend stands at **$1.964** (all from session 64's repeated-run measurement), leaving **$3.04 today** —
but the next session is likely a new UTC day → full $5. The single-run prefer-split flag (~$2.50/run) is unchanged.
Full ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 65 (UTC 2026-06-21) was DUAL-TRACK ($0, no probe)** — both NEXT.md-named zero-spend units, one per track,
generated in parallel (workflow mode, 1 wave) with a lead adversarial coherence pass.

- **EMPIRICAL line-opening — the function-word anchor decision is now OPEN.**
  [`decisions/open/function-word-anchor-design`](wiki/decisions/open/function-word-anchor-design.md) is the
  operationalization/anchor gate for
  [`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md)
  (does swapping a *function* word shift LLM behavior more than swapping a frequency-matched *content* word?).
  Three interlocking sub-questions surfaced with options + a provisional default: **Q1** what "frequency-matched"
  means (corpus-norm floor → +length/context-predictability, pair-level where the swap partners permit; the set
  **frozen + hashed before any model output is seen**; the high-frequency-content-word constraint stated openly as
  the cheat-surface the conjecture itself flags); **Q2** the logprob-free indicator (entailment-flip / forced-choice
  rate **primary** — prediction-1's KL is **not runnable** under the panel logprob blocker; a sampled-continuation
  divergence proxy **secondary only**); **Q3** stimuli + posture (synthetic minimal pairs; result posture defaults
  to **`internal-contrast-only`** — the predictions are a within-model contrast — with a *fetch-and-catalogue-first*
  human backing [BLiMP / NLI] as an optional upgrade that never blocks the within-model run). Anti-cheat: the
  default makes a spurious **positive harder**, and the falsify arm (content-swap shift ≥ function-swap shift = a
  clean positive for the distributional camp) stays live. The conjecture's `contingent-on` now names the decision.
- **PHILOSOPHICAL-adjacent source-fetch — essay trigger (c) DISCHARGED.** Fetched + catalogued the temp-0
  nondeterminism source: [`source/he-2025-defeating-nondeterminism`](wiki/base/sources/he-2025-defeating-nondeterminism.md)
  (He & Thinking Machines Lab 2025, OA engineering blog). **Mechanism:** not per-kernel randomness (the forward-pass
  kernels are run-to-run deterministic) but **load-dependent batch-size variation × non-batch-invariant kernels**
  (FP non-associativity the ultimate numeric cause; the common "concurrency" half a red herring).
  [`essay/point-estimate-is-a-draw`](wiki/findings/essays/point-estimate-is-a-draw.md) revised: trigger (c) marked
  **discharged**, the essay now grounds *why* the jitter occurs — **but explicitly not its magnitude** on the
  project's forced-choice instruments (that stays the K=5 measurement) and **no** claim about the panel's batching.
  The reading discipline itself is unchanged. `wanted.md` temp-0 entry → **received**.
- **Cadence.** Subagent drafted the decision page (fresh general-purpose, ~46k tok), lead-reviewed; source quotes
  verified-vs-characterized split flagged honestly. senselint **0 errors**; linkify clean.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` now has **one entry** —
[`decisions/open/function-word-anchor-design`](wiki/decisions/open/function-word-anchor-design.md), opened by
session 65. It is **eligible for cross-session ratification** (independent adversarial-review pass — verify the
session boundary holds; this session must not have opened it). Apply any Tom override first.

**Track lean.** 62 emp · 63 phil · 64 emp · 65 **dual**. No strong lean. The next session's most natural unit is
the **ratification** above (a judgement unit, fits either track's discipline).

1. **RATIFY (or modify/reject) the function-word-anchor-design decision** via an independent adversarial-review
   pass — fresh agent, re-derive the cheat-surface independently, check the provisional default is not
   result-motivated, confirm the falsify arm stays live. **If ratified**, the function-word probe becomes
   *buildable* — but it is **not one-session-runnable yet**: it needs a **frequency-norm resource fetched +
   catalogued first** (SUBTLEX-US / COCA / BNC — none in-repo), and, only if Posture 2 is chosen, a BLiMP/NLI
   human backing fetched + promoted. So a clean post-ratification unit is the **$0 frequency-norm fetch +
   resource-page build**, which then unblocks the build+probe session.
2. **EMPIRICAL build + run (after 1 + the resource fetch):** build the frozen, hashed function-word minimal-pair
   set to the ratified scheme under an independent pre-run critic (no item added/dropped after the first call),
   then run the entailment-flip / forced-choice probe. Pre-flight-estimate before spending.
3. **PHILOSOPHICAL (only if genuinely owed):** a theory/essay revision only if a specific over-statement is found
   — not symmetric padding. The let-alone / point-estimate line is exhausted; do not manufacture a revision.
4. **Longer-horizon (only if 1–3 are blocked):**
   - [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
     needs a fine-polysemy image set not in-repo (setup, not one-session-runnable).
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**One open:** [`decisions/open/function-word-anchor-design`](wiki/decisions/open/function-word-anchor-design.md)
(opened session 65, 2026-06-21) — eligible for ratification, at the earliest, **next session**. No probe runs
before it is ratified.

## Standing-override notes (for Tom, if he looks)

- Session 65 spent **$0** (a reading-and-planning session). UTC-day 2026-06-21 spend stays **$1.964** of $5.
- We tied off two loose ends. (1) Two sessions ago we wrote down that a single test score is a *draw*, not a fixed
  fact, but had no cited explanation for *why* identical runs disagree. We found and catalogued an open engineering
  write-up that explains it: it's not mainly random rounding on parallel hardware — the model's own arithmetic is
  repeatable — but busy servers bundle requests into batches whose size shifts with load, and a few common
  operations round slightly differently depending on the batch. We were careful to note this explains *why* the
  wobble exists, not *how big* it is on any test, and says nothing about the specific services we use. (2) We drew
  up the (not-yet-approved) ground rules for a fresh experiment on whether tiny *function* words carry more weight
  than equally common content words — written openly and frozen in advance, with the defaults set to make a
  positive result harder. A later session must review and approve the plan before it runs. No monitor named; no
  overstatement.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** one decision is open
(`function-word-anchor-design`) and is **eligible for ratification this session** — run the independent
adversarial-review pass before anything else. The let-alone empirical line is exhausted. End squash-merged to
`main`, website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true
> remote `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch
> origin main` first** (sessions 64 & 65 both confirmed this — a fresh clone's local `main` lagged; `git fetch
> origin main` [+ `git branch -f main origin/main`] fixed it). The project's real main is the chain of
> squash-merged session PRs.
>
> ⚠ **Empirical re-run note:** the Scivetti upstream data (the now-exhausted let-alone line) is gitignored and
> **not** in a fresh clone. The *next* empirical line (function words) instead needs a **frequency-norm** fetched
> and catalogued first (SUBTLEX-US / COCA / BNC) — not in-repo yet.
