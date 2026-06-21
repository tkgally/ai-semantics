# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 63 (UTC 2026-06-21) spent **$0.00** (a writing/method session, no
probe). **UTC-day 2026-06-21 spend = $0.00**, full **$5.00** available. The temporary $10 override (Tom,
JST June 20 only) **expired**; the standard $5/day is back in force. The single-run prefer-split flag
(~$2.50/run) is unchanged. Full ledger in [`config/budget.md`](config/budget.md).

## State

**Session 63 (UTC 2026-06-21, JST June 21) was PHILOSOPHICAL ($0.00)** — the track lean said weight
philosophical (two of the last three were empirical), and a revision was genuinely owed: session 62's
**~12% temp-0 label stochasticity** finding had been absorbed only as *local caveats* in two essays
(`witness-seeking-economics` trigger (g), `output-channel-confound` trigger (b)) and never named as a
general **reading discipline**.

- **What landed.** A new essay [`essay/point-estimate-is-a-draw`](wiki/findings/essays/point-estimate-is-a-draw.md)
  (the project's 17th): a **measurement-epistemics** reading discipline — a single-run accuracy at temp 0 is
  a **draw**, not a fixed quantity; single-run Wilson/bootstrap CIs capture within-run sampling error but
  **structurally miss** run-to-run jitter; **a between-X gap no larger than the jitter floor is not yet a
  finding**. It is the **measurement-level** sibling of `capability-split` (between-model split) and
  `concordant-verdict-hides-spread` (between-model magnitude) — both *phenomenon*-level; this one a level
  down. Threads the needle with `undischargeable-negative` (re-run to *measure* the noise floor is licit;
  re-run to "firm up" a null is not). Bite is **uneven by design** (hardest at small functional effects;
  barely at ceilings/clean separations; model-/instrument-specific — **not** a transferable constant).
- **Surgical revision.** [`essay/concordant-verdict-hides-spread`](wiki/findings/essays/concordant-verdict-hides-spread.md)
  got a 2026-06-21 revision-log entry pointing forward to the new sibling (its per-model-magnitude
  comparison — e.g. gpt's +0.056 — now carries the prior question "is the gap bigger than its own
  run-to-run jitter?"); **no clause changed**, the "single run" honesty-box caveat given a named mechanism.
- **Source queued.** A `base/wanted.md` entry for an open-access source on **temp-0 nondeterminism**
  (the *mechanism* — FP non-associativity / batching — is uncited in-repo and explicitly **not** fabricated;
  the essay rests only on the behavioral observation that the jitter occurs).
- **Cadence.** Independent adversarial coherence pass (fresh read-only agent) found **1 SHOULD-FIX** (a
  fabricated composite interval `0.708 [0.558, 0.849]` — that band is the published CI for the 33-item 0.727,
  not the 24-item 0.708) **+ 2 NITs** (a quote inflection; a temporal-order looseness) — **all fixed**, then
  re-verified. senselint **0 errors**; linkify clean; `decisions/open/` **empty**.

## Next concrete action — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. Apply any Tom
override first (the budget note above; check for any newer one).

**Track lean.** 59 phil · 60 emp · 61 phil · 62 emp · 63 **phil**. The last two alternated; no strong lean
either way. The empirical track has a clean, named, standing unit (below) — **weight the next session toward
EMPIRICAL** unless a philosophical revision is *genuinely* owed (do **not** manufacture).

1. **EMPIRICAL — the named trigger-(g) REDIRECT (now doubly-motivated): a repeated-run / multi-sample
   let-alone design.** Both session 62's result and the new `essay/point-estimate-is-a-draw` name this as the
   right next probe. The item ceiling (33) is reached; the binding limit is run-to-run label noise. Run the
   **same** forced-decomposition let-alone instrument **K times** (e.g. K = 5) at temp 0 and characterize the
   per-item label distribution + the across-run accuracy spread, **pinning the residual magnitude** (currently
   uncertain to ~±0.12) and giving the new essay its trigger-(a) datum (does jitter shrink on easier/ceiling
   items?). New axis (measurement, not item count) → **not** barred by the spent trigger-(g) exemption.
   Pre-flight: 33 let-alone items × K + one comp-corr control pass ≈ $0.39 × (33/63) × 5 + small ≈ **$1.0–1.3**
   — **single-day budgetable** (full $5 available); needs a fresh freeze (K-pass harness) + pre-run critic GO.
   *Confirm it is genuinely the highest-value empirical unit before spending — a measurement-characterization
   run, valuable but narrow.* **Side benefit:** its result would let the new essay's trigger (a)/(d) fire
   (narrow the bite to near-chance constructions, or graduate a stable small effect past the jitter read).
2. **PHILOSOPHICAL (only if genuinely owed — do not manufacture).** Session 63 discharged the
   label-stochasticity essay debt. Nothing further is obviously owed; the theory pages
   ([`theory/constructional-meaning-in-llms`](wiki/findings/theory/constructional-meaning-in-llms.md),
   [`theory/situating-llm-meaning`](wiki/findings/theory/situating-llm-meaning.md)) read results at their
   page strength (which already carry caveats), so no measurement-jitter note is *forced* there — open one
   only if a specific over-statement is found, not as symmetric padding.
3. **Longer-horizon alternatives (only if 1–2 are blocked):**
   - [`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md)
     needs a new frequency-matched-pair anchor decision *opened* first — a $0 line-opening unit.
   - [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
     needs a fine-polysemy image set not in-repo (setup, not one-session-runnable).
   - Fetch the queued **temp-0 nondeterminism** source (`base/wanted.md`) to fire the new essay's trigger (c).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**None.** (No decision was opened or left open this session.)

## Standing-override notes (for Tom, if he looks)

- Session 63 spent **$0.00** (a writing/method session); UTC-day 2026-06-21 spend **$0.00** of $5.
- Last session's "wobble" surprise — that an AI's answers flip about one-in-eight between two identical runs —
  is now written up as a plain rule: a single test score is a *draw*, not a fixed fact, so a small gap between
  two numbers only counts as a finding if it beats the wobble. The rule flags close calls and leaves big,
  clear, and ceiling results untouched; no finding changed. The honest next experiment is to run the same
  test several times and average (≈$1.0–1.3, within the day's $5). No monitor named; no overstatement.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC); UTC-day 2026-06-21 spend $0.00 (full $5 available).**
**No decisions open** — nothing to ratify; lean **EMPIRICAL** (the repeated-run/multi-sample let-alone
redirect — a new measurement axis, ~$1.0–1.3, needs a fresh freeze + pre-run critic GO) unless a
philosophical revision is genuinely owed. End squash-merged to `main`, website updated **with the JST
clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true
> remote `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch
> origin main` first**. (Session 63 found local == origin/main == the real head after a fetch, no staleness.)
> The project's real main is the chain of squash-merged session PRs.
