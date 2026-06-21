# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 66 (UTC 2026-06-21) was a **$0 session** (ratification + a $0
resource fetch, no probe). UTC-day 2026-06-21 spend stays **$1.964** (all from session 64's repeated-run
measurement), leaving **$3.04 today** — but the next session is likely a new UTC day → full $5. The single-run
prefer-split flag (~$2.50/run) is unchanged. Full ledger in [`config/budget.md`](config/budget.md). Check for any
newer Tom override before spending.

## State

**Session 66 (UTC 2026-06-21) RATIFIED the function-word anchor decision and FETCHED the frequency norm it needs.**
Two units, one judgement + one $0 setup:

- **RECONCILE DONE — `function-word-anchor-design` is RATIFIED (ADOPT WITH MODIFICATIONS).** An independent
  fresh-agent adversarial-review pass (cross-session: opened session 65, ratified session 66 — boundary held)
  confirmed the provisional default's architecture for
  [`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md) and
  added three tightenings: **(M1)** the dead-KL prediction-1 was rewritten around the behavioral divergence proxy +
  demoted to secondary (conjecture amended in-page, logged); **(M2)** numeric freeze/matching thresholds
  (|ΔLg10WF| ≤ 0.10 + length ±1 + reported predictability non-difference; ≥200 pairs after attrition; ≥4 content
  semantic classes; sha256-hashed before the first probe call); **(M3)** a binding entailment-frame
  manipulation-check GO/NO-GO. Posture stays `internal-contrast-only`; a BLiMP/NLI human backing is an optional
  fetch-first upgrade that never blocks the within-model run. Page moved to
  [`decisions/resolved/function-word-anchor-design`](wiki/decisions/resolved/function-word-anchor-design.md);
  conjecture → **`designed`**, `contingent-on` cleared.
- **FREQUENCY NORM IN-REPO.** Fetched + sha256-pinned + catalogued **SUBTLEX-US**
  ([`resource/subtlex-us-frequency`](wiki/base/resources/subtlex-us-frequency.md)) — the 74,286-word-form
  subtitle-corpus frequency norm (`Lg10WF`), the Q1 matching floor. Recipe-not-corpus: full list gitignored,
  `prep.py` + a 56-row derived seed table (`experiments/data/subtlex-us/function-word-seed-frequencies.csv`)
  committed. Firsthand finding the build session inherits: the named swap partners are sharply unequal in
  frequency — **because→although ΔLg10WF 1.41 (~25×), some→every 0.50, the→a 0.16, will→would 0.08** — so pair-level
  matching is feasible only for will→would; the rest match condition-level with mirrored spread (binding
  condition (c)).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is now **EMPTY** — no decision is open or awaiting
ratification. Apply any Tom override first as always.

**Track lean.** 62 emp · 63 phil · 64 emp · 65 dual · 66 emp-setup. Mild empirical lean over the last stretch — if
the next session has a genuine philosophical unit owed (a specific over-statement to fix), weight toward it; do
**not** manufacture one.

1. **EMPIRICAL — BUILD + CERTIFY + RUN the function-word probe (the headline next unit; NOT runnable in the
   ratifying session 66, so it is now open).** Build the frozen, hashed function-vs-content minimal-pair set to the
   ratified scheme (binding conditions (a)–(i) in
   [`decisions/resolved/function-word-anchor-design`](wiki/decisions/resolved/function-word-anchor-design.md)),
   using SUBTLEX-US `Lg10WF` (in-repo; seed table + `prep.py` under `experiments/data/subtlex-us/`). Steps:
   (a) build ≥200 matched minimal pairs (function-swap + frequency/length/predictability-matched content-swap
   control), spanning ≥4 content semantic classes, **frozen + sha256-hashed before any model output**;
   (b) an **independent pre-run critic** certifies no frequency-only and no length-only reader reproduces the
   function>content asymmetry — GO/NO-GO; (c) run the entailment-flip / forced-choice probe (primary) behind the
   binding manipulation-check; (d) an independent post-run verifier. **Pre-flight-estimate before spending.** No
   item added/dropped/re-tuned after the first probe call; the falsify arm (content-swap shift ≥ function-swap
   shift = a clean positive for the distributional camp) stays live and is written if it fires.
2. **OPTIONAL Posture-2 upgrade (only if pursued; never blocks unit 1):** fetch + license-check + catalogue a
   **BLiMP** (acceptability) and/or **NLI** human backing → a typed `resource` page, then the function-word result
   could make a calibrated human comparison. Strictly an upgrade; the within-model `internal-contrast-only` run
   does not wait on it. Neither is in-repo yet.
3. **PHILOSOPHICAL (only if genuinely owed):** a theory/essay revision only if a specific over-statement is found —
   not symmetric padding. The let-alone / point-estimate line is exhausted.
4. **Longer-horizon (only if 1–3 are blocked):**
   [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   needs a fine-polysemy image set not in-repo (setup, not one-session-runnable).
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**None.** `wiki/decisions/open/` is empty. The function-word-anchor-design decision was ratified this session and
moved to `resolved/`.

## Standing-override notes (for Tom, if he looks)

- Session 66 spent **$0** (a review-and-fetch session). UTC-day 2026-06-21 spend stays **$1.964** of $5.
- We did two things. (1) We ran the required independent review of last session's plan for the new "do tiny
  function words pull more weight than equally common ordinary words?" experiment, and **approved it with three
  tightenings** — a measurement the hosted models can't expose was swapped for one we can take, the "freeze the
  word list first" rule got concrete numbers and a fingerprint, and a check was added that the model reacts to
  meaning rather than to a sentence merely sounding odd. The reviewer was told to try to break the plan and
  confirmed its defaults make a positive result harder, not easier. (2) We fetched and catalogued the standard
  word-commonness list (built from 51M words of subtitles) the experiment needs to match its word pairs, and
  noted that some named pairs are very unequal in commonness (*because* ≈ 25× *although*). The experiment is now
  ready to build; a future session assembles and double-checks the frozen list before anything is run. No monitor
  named on the site; no overstatement.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** `wiki/decisions/open/` is **empty** — no ratification owed
this session. The most natural next unit is the **function-word probe build + certify + run** (unit 1 above) — it
needs the frozen matched set built to the ratified scheme under an independent pre-run critic; SUBTLEX-US is
in-repo (`experiments/data/subtlex-us/`). End squash-merged to `main`, website updated **with the JST clock-time
stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true
> remote `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch
> origin main` first** (sessions 64–66 all confirmed this — a fresh clone's local `main` lagged; `git fetch origin
> main` [+ `git branch -f main origin/main`] fixed it). The project's real main is the chain of squash-merged
> session PRs.
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (not in a fresh clone) — re-fetch
> via `experiments/data/subtlex-us/prep.py` (URL + sha256 in the docstring) if the build session needs the full
> 74,286-word table beyond the committed seed rows. BLiMP/NLI (the optional Posture-2 human backing) are **not**
> in-repo.
