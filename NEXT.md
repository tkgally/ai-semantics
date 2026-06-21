# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 64 (UTC 2026-06-21) spent **$1.9642** (the repeated-run jitter
measurement). **UTC-day 2026-06-21 spend = $1.964 of $5.00**, leaving **$3.04** today (but the next session is
likely a new UTC day → full $5). The single-run prefer-split flag (~$2.50/run) is unchanged; this run came in
under it at $1.96. Full ledger in [`config/budget.md`](config/budget.md).

## State

**Session 64 (UTC 2026-06-21) was EMPIRICAL ($1.9642)** — the named highest-value unit: the trigger-(g) /
`essay/point-estimate-is-a-draw` trigger-(a) **repeated-run jitter measurement**. It re-ran the byte-identical
forced-decomposition let-alone instrument **K=5** times at temp 0 over the same frozen 63-item set (all shas ==
session 62) and **pinned the temp-0 label jitter** that session 62 had inferred from a single run-pair.

- **What landed.** A new result [`result/scivetti-let-alone-repeated-runs-v1`](wiki/findings/results/scivetti-let-alone-repeated-runs-v1.md):
  **trigger (a) FIRES (3/3 models)** — jitter is **ceiling-protected** (comp-corr range 0.000 claude/gemini,
  0.033 gpt) and **near-chance-concentrated** (let-alone range **gpt 0.121** / claude 0.061 / gemini 0.030),
  and it is **model-specific** (so trigger (b), a transferable constant, stays **un-fired**). Most importantly,
  **gpt's below-baseline let-alone residual is robust to the jitter** — every one of the 5 runs reads < 0.90,
  de-noised majority-vote **0.606** [0.437, 0.753] — so session 62's CONFIRMS-RESIDUAL was **not** a low draw.
- **Essay revised (trigger (a) fired).** [`essay/point-estimate-is-a-draw`](wiki/findings/essays/point-estimate-is-a-draw.md)
  → `status: revised`: scope narrowed to "draws **on hard, near-chance, functional instruments**," the ~12% made
  explicitly **gpt's** (model-specific), and "gemini deterministic" → "**most stable**" (it churns 2/33 over 5
  runs). The discipline itself is unchanged; gpt's residual surviving the jitter is the trigger-(d) worked case.
- **s62 result page** got a surgical forward-pointer: its "~12% / gemini deterministic" single-run-pair detail is
  superseded by the K=5 measurement (the finding — gpt's residual — unchanged and strengthened).
- **Cadence.** PREREG frozen → independent fresh-agent pre-run critic **GO** (9/9) → probe (945 calls, 0 missing,
  945/945 parsed, uptake 33/33 every run) → independent fresh-agent post-run verifier **REPRODUCED** (every number
  re-derived from raw; caught only a ~$0.003 cost-split mis-rounding, fixed). senselint **0 errors**; linkify
  clean; `decisions/open/` **empty**.

## Next concrete action — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. Apply any Tom
override first (the budget note above; check for any newer one).

**Track lean.** 60 emp · 61 phil · 62 emp · 63 phil · 64 **emp**. Alternating; no strong lean. **But the
let-alone / point-estimate empirical line is now exhausted** — item ceiling reached (33) AND the jitter floor is
pinned, so "more let-alone" buys nothing. A *new* empirical line needs a decision opened or a new resource first.
Weight the next session toward **either** a $0 empirical line-opening **or** the source-fetch (which is
philosophical-adjacent and fires a named trigger). Do not manufacture a philosophical revision.

1. **EMPIRICAL line-opening ($0, no probe) — open the function-word anchor decision.**
   [`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md)
   needs a **frequency-matched-pair anchor decision** *opened* in `wiki/decisions/open/` (options + provisional
   default) before any probe — a clean, zero-spend line-opening unit that unblocks the next empirical session.
   This is the most tractable way to start a genuinely new empirical thread.
2. **PHILOSOPHICAL-ADJACENT ($0) — fetch the queued temp-0 nondeterminism source.** [`base/wanted.md`](wiki/base/wanted.md)
   carries an open-access source candidate on **temp-0 nondeterminism** (the *mechanism*: FP non-associativity /
   batching / routing). Fetching + summarizing it would fire `essay/point-estimate-is-a-draw` **trigger (c)** —
   grounding *why* the jitter occurs (the essay currently rests only on the behavioral observation that it does).
   Self-fetch only (open-access; charter §12.4); if unreachable, mark it and route around — **never fabricate**.
3. **Longer-horizon (only if 1–2 are blocked):**
   - [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
     needs a fine-polysemy image set not in-repo (setup, not one-session-runnable).
   - A philosophical revision **only if genuinely owed** — the theory pages read results at their page strength;
     open one only if a specific over-statement is found, not as symmetric padding.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**None.** (No decision was opened or left open this session.)

## Standing-override notes (for Tom, if he looks)

- Session 64 spent **$1.9642** (the repeated-run measurement); UTC-day 2026-06-21 spend **$1.964** of $5.
- We put a number on last session's "wobble" by running the same hard test five times. The wobble is **real but
  lives only where the test is hard** — a batch of easy "ceiling" puzzles scored on the same runs didn't move at
  all, while the hard puzzles swung up to 12 points for the smallest model (3–6 for the others; it's specific to
  the model, not a fixed quantity). And the smallest model's shortfall **survived** the wobble: every one of the
  five runs scored below the human level (averaged ~61% vs ~90%), so last session's "it genuinely falls short
  here" was not a fluke. Pre-registered, independently reviewed before spending, every number reproduced from raw
  afterward. No monitor named; no overstatement.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC); the let-alone empirical line is exhausted (ceiling + jitter both pinned).**
**No decisions open** — nothing to ratify; lean toward a **new** empirical line-opening (the function-word
anchor decision, $0) or the temp-0-nondeterminism source-fetch (fires essay trigger (c)). End squash-merged to
`main`, website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true
> remote `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch
> origin main` first** (session 64 confirmed this — a fresh clone's local `main` lagged; `git fetch origin main`
> + `git branch -f main origin/main` fixed it). The project's real main is the chain of squash-merged session PRs.
>
> ⚠ **Empirical re-run note:** the Scivetti upstream data is gitignored and **not** in a fresh clone. Re-clone
> `github.com/melissatorgbi/beyond-memorization @ 82699473` into `experiments/data/scivetti/` before any
> `prep.py --check` / re-analysis (session 64 did this; the four shas verify it is the same corpus).
