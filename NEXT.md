# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 69 (UTC 2026-06-21) spent **$0.50294** (the function-word probe build-v2
run: $0.50213 full + $0.00081 liveness). UTC-day 2026-06-21 total is now **$1.964 (s64) + $0.503 (s69) = $2.467 of
$5.00**. The next session is likely a new UTC day → full $5. Single-run prefer-split flag unchanged (~$2.50/run).
Full ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 69 (UTC 2026-06-21) BUILT, FROZE, RAN, and WROTE UP the function-word-vs-content-word swap probe — the
grammatical-core empirical headline — and added one philosophical essay. Dual-track, $0.503.**

- **EMPIRICAL — [`result/function-word-swap-run-v2`](wiki/findings/results/function-word-swap-run-v2.md): CONFIRM
  3/3, non-uniformly.** Build-v2 of the ratified
  [`decisions/resolved/function-word-count-vs-matching`](wiki/decisions/resolved/function-word-count-vs-matching.md):
  added `few`→`many` as the new quantifier arm (`many`→`every` was rejected — breaks number agreement), restored the
  adjective content class, fixed the `because` arm. **206 matched items, 4 content classes, four function arms**
  (because/some/will/few), file sha `4763740e…`, certified `"ok": true` (max-positive shortcut-reader asymmetry
  **0.0** — every content pair's |ΔLg10WF| gap held ≥ its arm's function gap). **Two independent fresh-agent
  pre-run critics** (first NO-GO on a coarse-θ-grid that hid a +0.136 freq-residual peak + a few-arm violation →
  both fixed → second **GO**). Ran the 3-model panel (1914 NLI calls, 0 unparsed, **$0.502 billed**); independent
  fresh-agent **post-run verifier reproduced every number to the digit**. **All three models CONFIRM**:
  function-word swaps flip 3-way NLI far more than frequency+length-matched content swaps (content flip 1–4%,
  falsify arm un-fired) — claude +0.340 [0.277,0.408], gpt +0.825 [0.767,0.879], gemini +0.859 [0.811,0.903].
  **NON-UNIFORM across function-word types:** `because`→`although` and `some`→`every` strong & panel-consistent;
  **`will`→`would` near-null in all three** (modal future→conditional doesn't shift the inference); **`few`→`many`
  splits the panel** (claude +0.095 vs gpt/gemini +0.96). `few` is 61% of items → dominates the pooled magnitude.
  Prediction 3 holds at the content-CLASS level, NOT the function-TYPE level. Conjecture
  [`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md) → **`tested`**.
- **PHILOSOPHICAL — [`essay/design-out-not-model-out`](wiki/findings/essays/design-out-not-model-out.md)** (18th
  essay, draft): a control covariate that is *degenerate* (zero within-condition variance, collinear with the
  manipulation) cannot be controlled by regression/stratification — it must be designed out at construction time.
  Worked from the function-word length-delta case; draws the line at within-condition variance; prices the supply cost.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no decision is eligible for ratification
next session. Apply any Tom override first as always. (Essays/results created this session are findings, not
decisions; they need no ratification — but essays are re-examined as evidence moves.)

**Track lean.** 64 emp · 65 dual · 66 emp · 67 emp · 68 emp-gov · 69 **dual** (ran a probe + wrote an essay). Balanced
this session; weight the next by the backlog's real priorities, not forced symmetry.

1. **EMPIRICAL follow-up on the non-uniformity (the natural next headline).** The run produced two sharp,
   citable sub-findings worth a focused probe:
   (a) **Is the modal null general?** `will`→`would` was near-null in all three models. A clean follow-up:
   widen the MODAL arm (e.g. `shall`→`should` — deontic, found in session-68 supply but coherence-marginal; or
   `can`→`could`) under the same frozen+certified discipline, to test whether *modal* function-word swaps generally
   fail to shift NLI (a real boundary on the conjecture) or whether `will`→`would` is idiosyncratic. Same pipeline
   in `experiments/runs/2026-06-21-function-word-vs-content-swap/` (add the arm to `build.py` FUNC + `frames.json`,
   re-freeze, fresh pre-run critic, run). NB the freq+length+coherence matching is hard for high-gap modal arms.
   (b) **Why does `few`→`many` split the panel?** claude treated few/many as inference-equivalent against "all";
   gpt/gemini did not. A small targeted quantifier probe (or a re-read of claude's raw on the few arm) could pin
   whether this is a quantifier-scope reading difference. Cheap.
2. **PHILOSOPHICAL (track-balance candidate — only if it earns a real claim):** the run's headline result is itself
   an essay seed — **"function words" are not one category for inference**: the inference-flip effect is
   *type-specific* (strong for subordinator + existential/universal quantifier; null for the future modal;
   model-split for the paucal/multal quantifier). This is an original, evidence-anchored claim about how
   constructional load distributes across closed-class items — could seed an essay refining
   [`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md)'s
   prediction 3. Write it only if it reaches a real claim, not as symmetric padding.
3. **OPTIONAL Posture-2 upgrade (never blocks a run):** fetch + license-check + catalogue **BLiMP** and/or **NLI**
   human backing → a typed `resource` page, so the function-word result could make a calibrated human comparison.
   Neither is in-repo.
4. **Longer-horizon (only if 1–3 are blocked):**
   [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   needs a fine-polysemy image set not in-repo (setup, not one-session-runnable).
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**None.** `wiki/decisions/open/` is empty.

## Standing-override notes (for Tom, if he looks)

- Session 69 spent **$0.503** (UTC-day 2026-06-21 total $2.467 of $5).
- The "smallest words" experiment that had been blocked for several sessions finally **ran**. The answer is a clear
  "yes" in all three models — swapping a small grammar word for a related one (because→although, some→every) flips
  the model's logic far more than swapping an equally common ordinary word — but it is **not uniform**: the
  will→would swap barely moved any model, and few→many split them (two flipped on it, one didn't). Two independent
  reviewers vetted the test before it ran (the first caught two real flaws, which were fixed). The honest reading is
  swap-by-swap, not one number, and the public site says so.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — nothing to ratify.
The most natural next unit is an **empirical follow-up on the non-uniformity** (unit 1: is the modal null general?
why does few→many split?) and/or the **type-specificity essay** (unit 2). The function-word pipeline lives at
`experiments/runs/2026-06-21-function-word-vs-content-swap/`. End squash-merged to `main`, website updated **with
the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true
> remote `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch
> origin main` first** (sessions 64–69 all confirmed this — `git branch -f main origin/main` fixed it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (not in a fresh clone) — re-fetch
> via `experiments/data/subtlex-us/prep.py` (URL + sha256 `c5f86f06…` in the docstring) before re-running
> `build.py`/`certify.py` (`freqlib.py` reads it). BLiMP/NLI (the optional Posture-2 human backing) are **not** in-repo.
