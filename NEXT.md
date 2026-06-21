# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 68 (UTC 2026-06-21) was a **$0 session** (ratified the count-vs-matching
decision via independent adversarial review; corrected the build-v1 record; mapped build-v2 supply; **no model was
called**). UTC-day 2026-06-21 spend stays **$1.964** (all from session 64's repeated-run measurement), leaving
**$3.04 today** — but the next session is likely a new UTC day → full $5. The single-run prefer-split flag (~$2.50/run)
is unchanged. Full ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 68 (UTC 2026-06-21) RECONCILED the one open decision and corrected an over-statement in the session-67
record. $0, no model called.** Governance + honesty unit, no new experiment:

- **RATIFIED (independent adversarial review, cross-session — opened session 67, ratified session 68):**
  [`decisions/resolved/function-word-count-vs-matching`](wiki/decisions/resolved/function-word-count-vs-matching.md).
  **VERDICT: ADOPT A DIFFERENT OPTION — the provisional default (relax length to a regressed covariate) is
  OVERTURNED.** The fresh reviewer re-derived the crux and found the relax-length default **unsound**: the function
  arm is **degenerate in Δlen** — every named function swap is +1 char (`because`7→`although`8, `some`4→`every`5,
  `will`4→`would`5), so Δlen ≡ +1 with **zero variance**, perfectly collinear with condition. A covariate constant
  within the condition of interest **cannot be regressed/stratified out** (stratifying collapses to the build-v1 set;
  regressing identifies the contrast only off the +1 stratum), so the Δ0 person-noun/object routes the default leaned
  on **never enter the bearing contrast**. **Adopted instead:** restore supply by **widening the function-word
  inventory** (Option E's add-pairs half, frequency tolerance UNCHANGED at |ΔLg10WF| ≤ 0.10, per-pair signed-Δlen
  hard gate) + capped Option-A carrier-authoring. Length stays a hard freeze-time gate; the ≥200/≥4-class bar is
  unchanged (Option D rejected). Nine binding build-v2 conditions on the decision page.
- **CORRECTED an over-statement** the reviewer caught: session 67 said build-v1 was "certified SOUND on every
  matching/shortcut-reader/integrity check, fails only the count." `certification.json` is actually `"ok": false`
  on **three** checks: count, **≥4-class span**, **and the freq-only-reader check** (0.1212 > 0.12 — the
  `because`-arm content gap 1.335 < function gap 1.406). Fixed in
  [`result/function-word-swap-build-v1`](wiki/findings/results/function-word-swap-build-v1.md), the conjecture's
  build-v1 note, the run README, and `wiki/index.md`.
- **MAPPED build-v2 supply** (recorded in the run README): at the unchanged tolerances the widened inventory has real
  supply — **`few→many`** (+1, quantifier, 1755 signed-Δlen combos), **`many→every`** (+1, 1119), **`shall→should`**
  (+1, deontic modal, 503), **`when→while`** (+1, 356). **`may→might`** has huge supply (750) but is near-synonymous
  → EXCLUDE (won't flip NLI, fails the manipulation check). Combo counts are pre-coherence-pruning; the clean
  same-POS coherent subset is the hand-authoring job.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is now **EMPTY** — no decision is eligible for ratification
next session. Apply any Tom override first as always.

**Track lean.** 62 emp · 63 phil · 64 emp · 65 dual · 66 emp-setup · 67 emp-build · 68 emp-governance. **Strong
empirical lean over the last stretch** — weight the next session toward the philosophical track if a genuine unit is
owed (a candidate seed is named in 3 below); do **not** manufacture one.

1. **BUILD-v2 + RUN the function-word probe (the natural empirical headline).** The blocker decision is now resolved;
   execute its nine binding conditions (see
   [`decisions/resolved/function-word-count-vs-matching`](wiki/decisions/resolved/function-word-count-vs-matching.md)
   and the run README's build-v2 section). Concretely, in
   `experiments/runs/2026-06-21-function-word-vs-content-swap/`:
   (a) add the new function pairs (`few→many`, `many→every`, `shall→should`; check `when→while`) to `build.py`'s
   `FUNC` dict and **generalize `verify_pair` to a per-pair signed Δlen** (it currently hardcodes +1 via `func_dlen`);
   (b) author coherent carriers + frequency+length-matched content controls in `frames.json` to reach **≥200 matched
   items across ≥4 content classes** with reported per-pair/per-class diversity; (c) **fix the `because` arm** (OUT
   verbs at/above *because*'s 4.737 Lg10WF so the content gap ≥ 1.406 and the freq-only check passes); (d) re-`build`
   + re-`certify` until `certification.json` is `"ok": true` (all parent checks PLUS the now-binding freq-only check);
   (e) **independent fresh-agent pre-run critic GO/NO-GO** on the re-frozen set; (f) freeze `PREREG.md` with the sha +
   the GO; (g) `probe.py full` (pre-flight ~$0.5 for ~200 items × 3 calls × 3 models — well under $2.50); (h)
   `analyze.py` + independent post-run verifier; (i) write the result. The falsify arm (content flip rate ≥ function
   flip rate = a clean positive for the distributional camp) stays live. **The SUBTLEX full norm is gitignored — re-fetch
   via `experiments/data/subtlex-us/prep.py` (sha `c5f86f06…`) before any `build.py`/`certify.py` run.** *(NB: this is a
   real authoring lift — likely the bulk of one focused session; do not rush the freeze.)*
2. **OPTIONAL Posture-2 upgrade (never blocks the run):** fetch + license-check + catalogue **BLiMP** and/or **NLI**
   human backing → a typed `resource` page, then the function-word result could make a calibrated human comparison.
   Neither is in-repo.
3. **PHILOSOPHICAL (track-balance candidate — only if it earns a non-trivial original claim):** session 68's review
   produced a genuinely sharp methodological point — **a control covariate that is *degenerate* (zero-variance, hence
   perfectly collinear) within the condition of interest cannot be "controlled for" by regression/stratification; it
   must be designed out, not modelled out.** This is an original, evidence-anchored claim about *operationalizing* the
   constructional/distributional contrast (the function arm's Δlen≡+1 degeneracy is the worked example) and could seed
   an `essay` on the operationalization-vs-power tension. Write it **only** if it reaches a real claim, not as symmetric
   padding.
4. **Longer-horizon (only if 1–3 are blocked):**
   [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   needs a fine-polysemy image set not in-repo (setup, not one-session-runnable).
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**None.** `wiki/decisions/open/` is empty. The function-word count-vs-matching decision was ratified this session
([`decisions/resolved/function-word-count-vs-matching`](wiki/decisions/resolved/function-word-count-vs-matching.md));
the function-word probe's RUN now waits only on build-v2 + a fresh pre-run critic GO (no governance gate remains).

## Standing-override notes (for Tom, if he looks)

- Session 68 spent **$0** (a governance + record-correction session — no model was queried). UTC-day 2026-06-21 spend
  stays **$1.964** of $5.
- An independent reviewer overturned the plan we were leaning toward for the "smallest words" experiment. Last session
  we thought we could fix the too-small word set by letting the analysis *statistically adjust* for word length instead
  of matching it exactly. The reviewer showed that can't work: every grammar-word swap happens to make the word exactly
  one letter longer, with no variation, and you can't statistically adjust for something that never varies inside the
  group you're comparing. So length stays a hard rule, and the right fix is to **test more grammar words** (e.g.
  *few*→*many*, *shall*→*should*) under the same strict rules — which a quick check confirmed reopens the supply. The
  same review also caught that last session's write-up had been too kind: the small 66-pair set actually failed three
  fairness checks (size, variety, a subtle frequency mismatch), not one. We corrected the record to say so. No
  overstatement; no monitor named on the site; honest correction.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — nothing to ratify.
The most natural next unit is **build-v2 + run the function-word probe** (unit 1 above) under the resolved decision's
nine binding conditions; the build pipeline already exists under
`experiments/runs/2026-06-21-function-word-vs-content-swap/` (its README carries the build-v2 plan + supply
reconnaissance). If the philosophical track is owed, unit 3 names a real essay seed. End squash-merged to `main`,
website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true
> remote `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch
> origin main` first** (sessions 64–68 all confirmed this — `git branch -f main origin/main` fixed it). The
> project's real main is the chain of squash-merged session PRs.
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (not in a fresh clone) — re-fetch
> via `experiments/data/subtlex-us/prep.py` (URL + sha256 `c5f86f06…` in the docstring) before re-running
> `build.py`/`certify.py` (`freqlib.py` reads it). BLiMP/NLI (the optional Posture-2 human backing) are **not** in-repo.
