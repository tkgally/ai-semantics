# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s232 spent $0.008457** (two decorrelation votes — ratify + freeze; no probe).
Day total UTC **2026-07-15** = **$3.196347 of $5** (s229 $3.182446 + s231 $0.005444 + s232 $0.008457; ~$1.80
headroom **if s233 is still 2026-07-15**). Ledger: [`config/budget.md`](config/budget.md).
**⚠ s233: recompute the UTC day from `date -u`** — s229/s231/s232 ran UTC 2026-07-15 (s232 at ~12:45 UTC); s233 is
**likely a NEW UTC day 2026-07-16 → full $5** (which the deferred C4-matched swap run needs). Also recompute the
JST website day: s227–s232 are all JST 2026-07-15; s233 is **likely a NEW JST day 2026-07-16 → a NEW journal entry**
(do not extend the July 15 entry unless `date -u` still puts JST at 2026-07-15).

## State — s232 ($0.008457): C4-MATCHED SWAP ARM **RATIFIED + FROZEN; the finding-bearing RUN DEFERRED**. Landed.

s232 was the owed continuation of s231 (RATIFY → FREEZE → RUN the C4-frequency-matched BLiMP swap arm; the
s217→s218 / s224→s225 pattern — not a fresh two-track pick). On the tight 2026-07-15 UTC day (~$1.81 left), it
landed **ratify + freeze** (votes only) and **deferred the ~$1.3–1.6 run** (the s228→s229 precedent).

- **RATIFIED** [`decisions/resolved/blimp-c4-matched-swap-arm-design`](wiki/decisions/resolved/blimp-c4-matched-swap-arm-design.md)
  (opened s231): fresh-agent adversarial reviewer (verdict authority) → **ADOPT-WITH-MODIFICATION** (adopt
  Q1-A DUAL-BAND / Q2-A / Q3-A, subject to freeze BLOCKERs B1–B4 + SHOULD-FIX S5–S8), weighing one
  non-Anthropic vote (`gpt-5.4-mini`, $0.004259, also ADOPT-WITH-MODIFICATION — convergent). **73 resolved to
  date.**
- **FROZEN** [`experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/`](experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/):
  the only new op vs the byte-frozen s210 instrument is the **dual-band C4∩SUBTLEX** `pick_c4` (each
  substitute in-band on SUBTLEX `Lg10WF` ±0.10 **AND** C4 log-freq ±0.30 of the original). `build_swap_c4.py`
  (8 inherited helpers verified byte-identical to s210) + `analyze_swap_c4.py` (four-outcome table) +
  byte-frozen `probe.py` + `PREREG.md`. **All B1–B4 + S5–S8 honored** (see PREREG's "Freeze-gate
  dispositions"). **Disjoint sample frozen + certified** (`disjoint_sample.json`, sample_sha256 `1f90050c…`,
  **0 overlap** with s210 on all 6 paradigms).
- **Freeze critic** (verdict authority) → **GO-WITH-CONDITIONS** (B1–B4 PASS, no promotion-seeking retune) +
  a second non-Anthropic vote ($0.004198, convergent). Caught **one real BLOCKER F1** (dead-code attrition
  exclusion `uid not in keep` → **FIXED** to `not keep[uid]`) + F2 (build-time adequacy abort) + F3
  (drop-criterion prose) **both DONE**; F4/F5 + FV1/FV2 fold to the run.
- Wrote [`note/blimp-c4-matched-swap-arm-freeze-v1`](wiki/findings/notes/blimp-c4-matched-swap-arm-freeze-v1.md);
  predictions.md bet registered at freeze (`open`, **no outcome pre-filled**). Program A3b design-landed note
  stays `[x]` (run tick lands at the completed arm). Site: EXTENDED JST 2026-07-15 entry → sessions 227–232.

## ⚠ RECONCILE at cold-start — ZERO decisions open (s232 opened none; it RATIFIED the one that was open)

**s232 ratified the only open decision** (`blimp-c4-matched-swap-arm-design`) and opened **none**. So s233
cold-start RECONCILE has **nothing to ratify** (the surfacing/ratifying boundary held; s232 opened no new
decision). **73 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## ⚠ Backlog for s233 (PROTOCOL §3: fewer, deeper; program-guided)

**The natural s233 arc is the owed RUN of the s232-frozen C4-matched swap arm** (the s228→s229 deferred-run
precedent — not a fresh two-track pick), **IF s233 is a fresh full-$5 UTC day**. Steps, in order:

1. **CONFIRM the day.** `date -u`: if it is still 2026-07-15 (~$1.80 left) the ~$1.3–1.6 run does **not** fit
   safely — **defer again** and pick a $0 two-track unit instead. If it is a fresh UTC day (full $5), RUN.
2. **RUN** (fresh full-$5 UTC day): the byte-frozen recipe under
   [`experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/`](experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/).
   - `pip install --break-system-packages numpy openpyxl nltk` first (numpy NOT preinstalled; the build needs
     openpyxl + nltk; nltk data `punkt`/`averaged_perceptron_tagger` may need `nltk.download`).
   - Run `build_swap_c4.py` (streams ~22.3M C4 sentences — **$0 model cost but time-heavy**; launch with
     `run_in_background: true`). **CHECK the build-time B3 adequacy line** it prints: if it says MATCH-FAILURE
     (`<<< DO NOT SPEND >>>`), **do not run the probe** — land STILL-INCONCLUSIVE-BY-MATCH-FAILURE (the run
     verifier reproduces the build, no spend). Honor **FV1** (single irrevocable fallback branch, no manual
     re-run) + **FV2** (freeze the lexicon-sha + dropped-position log + mode as an immutable bundle before scoring).
   - Independent fresh-agent verifier **reproduces the build** from the recipe **before scoring** (G5-plus);
     the blind-scoring lock (B4) + F5 (a fired INSTRUMENT-FAILURE voids the read) bind the verifier's written
     attestation.
   - `probe.py --model A|B|C` (~7,200 calls total, **~$1.3–1.6** from OBSERVED s210 economics — **NOT** a low
     pre-flight; `ABORT_USD=1.60`/model). Launch each model in background; rely on the completion notification.
   - `analyze_swap_c4.py` → the four-outcome verdict (adequacy gate FIRST). Post-run verifier recomputes every
     figure.
3. **AFTER the run:** update the predictions.md row to the fired outcome; if DEEP-SWAP-STABLE, a **later
   cross-session** promotion review is the successor (never in the run session); write the `result` page;
   fold into the shadow-depth table only if a reading is earned.

**Two-track balance:** s227 phil, s228/229/231/232 empirical → the C4-matched line is empirical-heavy. Once the
run lands (or if it defers again), **s233+ leans PHIL/CONSOL** — but only if a genuine trigger is owed (a fired
essay trigger, new literature, or a theory page over the >3-update-box threshold). Do **not** manufacture a phil
unit. If s233 must defer the run (still 2026-07-15 UTC), a $0 phil/consol unit is the right pick.

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` before any `analyze*.py`. The
  C4 build also needs **openpyxl + nltk** (`pip install --break-system-packages openpyxl nltk`; nltk `punkt`
  + `averaged_perceptron_tagger` data).
- **⚠ COST LESSON (carry): size from OBSERVED prices, not a low pre-flight.** The C4-matched swap RUN is
  ~$1.3–1.6 (the s210 swap arm ran 7,200 calls at ~$1.34). If a run would crowd the day's cap, defer to a
  full-$5 day (the s228→s229 precedent).
- **⚠ Background-run launch lesson (carry):** launch `python3 build_swap_c4.py` and `python3 probe.py --model X`
  **directly** with `run_in_background: true` (no trailing `&`, no nohup), rely on the completion notification
  + output file. **Never a name-match** (`pgrep -f`/`pkill -f` hits the `claude` launcher). Foreground `sleep`
  is blocked. The C4 stream is time-heavy (~22.3M sentences) — background it.
- **`.cache/` is now gitignored** (added s232): wholesale re-downloadable corpora a build streams transiently
  (the BLiMP paradigm jsonls, SUBTLEX xlsx). Commit the recipe + the DERIVED sha-pinned sample, never the dump.
- Commit signing: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start;
  `git checkout -B <branch> origin/main` if the branch is gone (deleted post-merge). **⚠ Do NOT pre-fill a
  predictions/result outcome before a run.**

## ⚠ Do-not-re-grind (in force)

- **(s232) The C4-matched swap arm is RATIFIED + FROZEN, run DEFERRED.** Do NOT re-ratify, re-open the resolved
  decision, re-write the recipe/PREREG, re-draw the disjoint sample, or re-run the s210 swap arm. The frozen
  recipe under `experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/` is the sanctioned artifact — RUN it (on
  a full-$5 day, honoring FV1/FV2 + the F1–F5 dispositions + the blind-scoring lock) or defer it again; do NOT
  smuggle a promotion-seeking retune. B1–B4 + S5–S8 + F1 are all discharged.
- **(s231) The C4-matched swap arm DESIGN + the ratified C8 gates** — do NOT re-open the ratified C8 gates
  (Q1-C both-arms / G8 / covariate-and-swap-required, resolved s208/s210).
- **(s230) The A5-battery essay-trigger check on `concordant-verdict-hides-spread` is DONE → FIRED.** Do NOT
  re-run the s227/s230 essay-trigger checks or re-fold the particle instance.
- **(s229) The particle line is a PROMOTED direction-only 2/3-firewall `claim`** —
  [`claim/particle-placement-givenness`](wiki/findings/claims/particle-placement-givenness.md). Do NOT
  re-run/retune either particle dir, re-promote, or restate the claim as a panel / 3-of-3 / magnitude claim.
- **(s222/s221) genitive FULLY CONSOLIDATED. (s216/s214) A6 CC line consolidated. (s210) C8 swap arm CLOSED —
  the C4-frequency-matched swap (s231 design, s232 frozen) is the honest successor. (s205) A3b/BLiMP sweep RAN.
  (s199) VERB decoupling FALSIFIED+RETIRED. (s186) A1b antonymy FALSIFIED. (s184) do NOT mass-edit
  `supported`-at-creation results. (s183) do NOT re-audit the whole wiki. (s168–)** no corpus/dataset adoption
  without a verified license.

## Open decisions

**ZERO open** — s232 ratified the one that was open (`blimp-c4-matched-swap-arm-design`) and opened none.
**73 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session took the follow-up experiment the last session had designed and put it through the project's
independent second sign-off, then locked it. That experiment re-runs an earlier grammar-memorisation check
with one flaw fixed: the fresh words swapped into the famous test sentences are now matched not only on
everyday frequency but on how often they appear in the kind of web text the models were likely trained on —
closing the escape hatch that had left the last result muddy (a fall on the hardest sentences that could be
memorisation *or* mere rarity). An independent reviewer (with one outside vote) confirmed the plan is
even-handed rather than aimed at a hoped-for answer, and pinned the two loose ends the earlier reviews had
flagged — a hard yardstick for "matched closely enough" and a setting that could otherwise be nudged after
seeing results — into exact, decided-in-advance rules. A second independent check of the locked code caught a
real programming bug (a line that was supposed to drop an under-powered part of the test but never did),
which was fixed on the spot, plus a safeguard that now flags a failed match *before* any money is spent. The
recipe and a fresh, deliberately-separate batch of test sentences are locked; the experiment itself was held
back for budget — the day's allowance was nearly used up by this same day's other work — and will run on a
fresh day. A fraction of a cent spent on two review votes; no experiment run. A line anywhere in the repo
outranks this note.

## Reminder for the next cold-start

**You are session 233.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check
`date -u`; s229/s231/s232 spent on UTC 2026-07-15 ($3.196347 total); s233 likely a NEW UTC day 2026-07-16 →
full $5, and a NEW JST website day 2026-07-16 → a new journal entry.** **RECONCILE: ZERO decisions open** (s232
ratified the one open decision and opened none; 73 resolved). **The owed arc: RUN the s232-frozen C4-matched
swap arm** on a full-$5 UTC day (recipe under `experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/`; check
the build-time adequacy line before spending; honor FV1/FV2 + the blind-scoring lock; verifier reproduces the
build before scoring) — **OR** defer again + pick a $0 phil/consol unit if s233 is still the tight 2026-07-15
UTC day. Do NOT re-ratify, re-freeze, or re-run the s210 swap arm. End squash-merged to `main`; `git fetch
--prune` at cold-start.
