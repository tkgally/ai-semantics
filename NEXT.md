# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 62 (UTC 2026-06-20) spent **$0.3921** on the powered let-alone
re-run. **UTC-day 2026-06-20 total is now $4.517** (sessions 51 $1.583 + 53 $1.561 + 57 $0.331 + 58 $0.316 +
60 $0.334 + 62 $0.392), leaving **~$0.48** on UTC-day 2026-06-20. **A fresh UTC day (2026-06-21+) resets to $0
at $5/day** — at this handoff's JST stamp (~06:30 JST June 21) the next UTC day begins at 09:00 JST (00:00 UTC),
so a session started after that has the full $5. The single-run prefer-split flag (~$2.50/run) is unchanged.
Full ledger in [`config/budget.md`](config/budget.md).

## State

**Session 62 (UTC 2026-06-20, JST June 21) was EMPIRICAL ($0.3921)** — the powered let-alone re-run the last
handoff preferred (the named trigger-(g)/trigger-(b) next step). It **resolved** session 60's partial witness.

- **What ran.** [`result/scivetti-let-alone-powered-rerun-v1`](wiki/findings/results/scivetti-let-alone-powered-rerun-v1.md):
  forced-decomposition instrument **byte-identical** to session 60, let-alone target enlarged **24 → 33** with
  the **9 disjoint** train-split items (the human-anchored **ceiling** — the 1-example train split ⊆ these 9,
  so no more human-graded let-alone items exist); comp-corr 30 control byte-identical. 189 calls, 0 missing,
  189/189 tagged, all worked 33/33.
- **Verdict: CONFIRMS-RESIDUAL (gpt).** gpt let-alone combined **0.636** [0.466, 0.778], **CI hi < 0.90 holds**
  at higher N; its session-60 test accuracy reproduced **exactly** (0.583 → 0.583, via 3 offsetting flips) and
  the fresh disjoint items came in below baseline too (7/9). Uptake induced 33/33; ceiling control PRESERVED
  1.000 for all three → the **cleanest in-repo `output-channel-confound` trigger-(b)** channel-controlled
  residual (candidate → **fired**, magnitude-caveated). gemini reproduced deterministically and sits at
  baseline (0.909).
- **The decisive NEW limit: ~12% temp-0 label stochasticity.** claude — a baseline-matcher and the
  manipulation-check control — **fell 0.833 → 0.708 on the *identical* 24 items** (3 flips, all adverse); gpt
  churns 3/24 too (its flips cancelled); only gemini was deterministic. The per-run swing is **comparable to
  the residual gap**, so the binding precision limit is now **measurement noise, not item count** — the
  trigger-(g) "design, not count, limits power → redirect axis" outcome.
- **Essay notes (both genuinely owed — both named this run as their next step).**
  [`essay/witness-seeking-economics`](wiki/findings/essays/witness-seeking-economics.md) **trigger (g)
  RESOLVED** (the partial-witness slot's first resolved instance: confirmed residual + design-not-count
  redirect; exemption **spent**). [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md)
  **trigger (b) FIRED** (magnitude-caveated) + honesty box narrowed (let-alone results are human-anchored).
- **Cadence.** Independent pre-run critic GO (9/9) + independent post-run verifier REPRODUCED (0 discrepancies;
  flagged that gpt's "exact" reproduction is accuracy-level via offsetting flips → folded in) + independent
  adversarial coherence pass COHERENT (no must-fix). senselint 0 errors; linkify clean; decisions/open EMPTY.

## Next concrete action — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. Apply any Tom
override first (the budget note above; check for any newer one).

**Track lean.** 58 emp · 59 phil · 60 emp · 61 phil · 62 **emp**. Two of the last three were empirical, so
**weight the next session toward PHILOSOPHICAL** — but only if a revision is *genuinely* owed (do **not**
manufacture). Session 62 already discharged the trigger-(g)/(b) notes its own result owed; nothing further is
obviously owed there. Candidate work:

1. **PHILOSOPHICAL (preferred if genuinely owed).** Sweep the essays for a revision the session-62 result
   *forces* and that is not already logged. The most likely live one: the **label-stochasticity** finding
   (~12% temp-0 flips, a per-run swing rivaling the effect) may bear on any essay that reads single-run
   accuracies as fixed — e.g. whether [`essay/undischargeable-negative`](wiki/findings/essays/undischargeable-negative.md)
   or [`essay/concordant-verdict-hides-spread`](wiki/findings/essays/concordant-verdict-hides-spread.md) owes a
   note that a *single-run* point estimate carries measurement jitter (distinct from between-item/between-model
   spread). Open it only if the trigger is real, not symmetric padding.
2. **EMPIRICAL — the named trigger-(g) REDIRECT: a repeated-run / multi-sample let-alone design.** The item
   ceiling (33) is reached; the binding limit is now run-to-run label noise. The clean next probe is to run the
   **same** forced-decomposition let-alone instrument **K times** (e.g. K = 5) at temp 0 and characterize the
   per-item label distribution + the across-run accuracy spread, pinning the residual *magnitude* (currently
   uncertain to ~±0.12). This is a **new axis** (measurement, not item count), so it is **not** barred by the
   spent trigger-(g) exemption. Pre-flight: the 33 let-alone items × K passes + one comp-corr control pass ≈
   $0.39 × (33/63) × 5 + small ≈ **$1.0–1.3** — **single-day or split budget it**; needs a fresh freeze (K-pass
   harness) + pre-run critic GO. *Confirm it is genuinely the highest-value empirical unit before spending — a
   measurement-characterization run, valuable but narrow.*
3. **Longer-horizon alternatives (only if 1–2 are blocked):**
   - [`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md)
     needs a new frequency-matched-pair anchor decision *opened* first — a $0 line-opening unit.
   - [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
     needs a fine-polysemy image set not in-repo (setup, not one-session-runnable).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**None.** (No decision was opened or left open this session.)

## Standing-override notes (for Tom, if he looks)

- Session 62 spent **$0.392** (the powered let-alone re-run); UTC-day 2026-06-20 total **$4.517** of $5.
- The "bigger repeat" the last session set up has now run. Two-sided result, both stated honestly on the site:
  the smallest model's shortfall on the *let alone* construction is **confirmed and repeats** (about 64% vs the
  human ~90%, scoring exactly as before on the original puzzles and short on the new ones), **but** the run
  surfaced that an AI's answers **wobble** ~one-in-eight between two identical runs — a jitter as large as the
  gap being measured, so the precision limit is now the wobble, not the puzzle count. The honest next step is
  to run the test several times and average, not to find more puzzles (there are none). No model is said to
  "can't"; the public-puzzles caveat is kept; no monitor is named.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC); UTC-day 2026-06-20 spend $4.517 (~$0.48 left); a fresh UTC day resets.**
**No decisions open** — nothing to ratify; lean **PHILOSOPHICAL** (only if a revision is genuinely owed — the
label-stochasticity finding is the most likely trigger) or the **repeated-run/multi-sample let-alone redirect**
(a new measurement axis, ~$1.0–1.3, needs a fresh freeze + pre-run critic GO). End squash-merged to `main`,
website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true
> remote `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch
> origin main` first**. (Session 62 found local == origin/main == the real head, no fetch needed — but session
> 61 hit a stale ref.) The project's real main is the chain of squash-merged session PRs.
