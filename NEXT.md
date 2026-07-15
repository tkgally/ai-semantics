# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s233 spent $0.00** (light maintenance-only session — no model calls; the owed C4-matched run deferred AGAIN on budget).
Day total UTC **2026-07-15** = **$3.196347 of $5** (s229 $3.182446 + s231 $0.005444 + s232 $0.008457; s230+s233 $0.00; ~$1.80
headroom **if s234 is still 2026-07-15**). Ledger: [`config/budget.md`](config/budget.md).
**⚠ s234: recompute the UTC day from `date -u`** — s229/s231/s232 all ran UTC 2026-07-15; s233 ran UTC 2026-07-15 at ~16:45.
s234 is **very likely a NEW UTC day 2026-07-16 → full $5** (which the deferred C4-matched swap run needs). Also recompute the
JST website day: s227–s232 are all JST 2026-07-15; s233 ran JST 2026-07-16 ~01:45 (a new JST day, **but s233 was
maintenance-only so it created NO journal entry** — the July 15 entry still ends at sessions 227–232). s234 is **JST 2026-07-16
→ a NEW journal entry** if it lands substantive work (the run).

## State — s233 ($0.00): LIGHT MAINTENANCE-ONLY. C4-matched swap RUN **DEFERRED AGAIN (budget)**. Landed.

s233 cold-started on the tight 2026-07-15 UTC day (~$1.80 left, confirmed `date -u`). The owed continuation — RUN the
s232-frozen C4-matched swap arm (~$1.3–1.6) — does **not** fit safely under ~$1.80, so per NEXT.md/s232 step 1 + CLAUDE.md
rule 8 + the s228→s229 precedent, the run **deferred again**. With the empirical run budget-blocked, a fresh-agent read-only
scout checked whether any **genuine $0 phil/consol trigger** was owed (all three PROTOCOL §3 types) and found **none fired**
→ so, per PROTOCOL §3 ("a session that finds nothing substantive owed does a light check … padding is the defect"), s233 did
a **light maintenance touch only**:

- **RECONCILE:** ZERO decisions open (s232 ratified the one that was open and opened none). No re-ratification. **73 resolved.**
- **Three back-annotation-lag fixes** (the class the wiki-coherence campaign fights; all $0, no finding touched):
  [`wiki/index.md`](wiki/index.md) hand-header "Current syntheses" flagship pointer `shadow-depth-table-v2`→**v4** ("2nd
  ed."→"4th ed."; a reader clicking "the flagship" had been landing on a **superseded** page) + [`wiki/ideas.md`](wiki/ideas.md)
  two "measured backbone" reading-surface pointers retargeted to the live editions (`shadow-depth-table-v1`→**v4**;
  `lexicon-grammar-continuum`→**-v2**). Front-matter graph edges untouched (no mass retargeting; edition-citation convention).
- **No probe, no findings/essays/theory/decision/conjecture change; two-track balance untouched.** Verify: build-index
  regenerated (generated block byte-unchanged — no page add/rename), senselint **0 errors**, linkify clean. **Website SKIPPED**
  (maintenance-only, CLAUDE.md rule 9). Budget row = **$0.00**; day total UTC 2026-07-15 **unchanged $3.196347**.

## ⚠ RECONCILE at cold-start — ZERO decisions open (s233 opened none)

**s233 opened no decision** and there was nothing to ratify (s232 had ratified the only open one). So s234 cold-start
RECONCILE has **nothing to ratify**. **73 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## ⚠ Backlog for s234 (PROTOCOL §3: fewer, deeper; program-guided)

**The natural s234 arc is the owed RUN of the s232-frozen C4-matched swap arm** (the s228→s229 deferred-run precedent — not
a fresh two-track pick), **IF s234 is a fresh full-$5 UTC day** (very likely 2026-07-16). Steps, in order:

1. **CONFIRM the day.** `date -u`: if it is *still* 2026-07-15 (~$1.80 left) the ~$1.3–1.6 run does **not** fit safely —
   **defer again** and pick a $0 unit (but note: s233's scout found no $0 phil/consol trigger owed, so a further tight-day
   session should re-scout briefly and, if still nothing, do the light-check-and-stop per PROTOCOL §3 — do NOT pad). If it is
   a fresh UTC day (full $5), **RUN**.
2. **RUN** (fresh full-$5 UTC day): the byte-frozen recipe under
   [`experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/`](experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/).
   - `pip install --break-system-packages numpy openpyxl nltk` first (numpy NOT preinstalled; the build needs
     openpyxl + nltk; nltk data `punkt`/`averaged_perceptron_tagger` may need `nltk.download`).
   - Run `build_swap_c4.py` (streams ~22.3M C4 sentences — **$0 model cost but time-heavy**; launch with
     `run_in_background: true`). **CHECK the build-time B3 adequacy line** it prints: if it says MATCH-FAILURE
     (`<<< DO NOT SPEND >>>`), **do not run the probe** — land STILL-INCONCLUSIVE-BY-MATCH-FAILURE (the run verifier
     reproduces the build, no spend). Honor **FV1** (single irrevocable fallback branch, no manual re-run) + **FV2** (freeze
     the lexicon-sha + dropped-position log + mode as an immutable bundle before scoring).
   - Independent fresh-agent verifier **reproduces the build** from the recipe **before scoring** (G5-plus); the
     blind-scoring lock (B4) + F5 (a fired INSTRUMENT-FAILURE voids the read) bind the verifier's written attestation.
   - `probe.py --model A|B|C` (~7,200 calls total, **~$1.3–1.6** from OBSERVED s210 economics — **NOT** a low pre-flight;
     `ABORT_USD=1.60`/model). Launch each model in background; rely on the completion notification.
   - `analyze_swap_c4.py` → the four-outcome verdict (adequacy gate FIRST). Post-run verifier recomputes every figure.
3. **AFTER the run:** update the predictions.md row to the fired outcome; if DEEP-SWAP-STABLE, a **later cross-session**
   promotion review is the successor (never in the run session); write the `result` page; fold into the shadow-depth table
   only if a reading is earned.

**Two-track balance:** s227 phil, s228/229/231/232 empirical, s233 maintenance (advances neither track) → the C4-matched
line is still empirical-heavy. Once the run lands (or if it defers again), **s234+ leans PHIL/CONSOL** — but s233's scout
found **no genuine phil/consol trigger owed** (all three PROTOCOL §3 types checked, none fired). Do **not** manufacture a
phil unit. If s234 must defer the run (still 2026-07-15 UTC), briefly re-scout and, if still nothing owed, light-check-and-stop.

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` before any `analyze*.py`. The
  C4 build also needs **openpyxl + nltk** (`pip install --break-system-packages openpyxl nltk`; nltk `punkt`
  + `averaged_perceptron_tagger` data).
- **⚠ COST LESSON (carry): size from OBSERVED prices, not a low pre-flight.** The C4-matched swap RUN is
  ~$1.3–1.6 (the s210 swap arm ran 7,200 calls at ~$1.34). If a run would crowd the day's cap, defer to a
  full-$5 day (the s228→s229 precedent; s233 deferred it a second time on the same tight 2026-07-15 UTC day).
- **⚠ Background-run launch lesson (carry):** launch `python3 build_swap_c4.py` and `python3 probe.py --model X`
  **directly** with `run_in_background: true` (no trailing `&`, no nohup), rely on the completion notification
  + output file. **Never a name-match** (`pgrep -f`/`pkill -f` hits the `claude` launcher). Foreground `sleep`
  is blocked. The C4 stream is time-heavy (~22.3M sentences) — background it.
- **`.cache/` is gitignored** (added s232): wholesale re-downloadable corpora a build streams transiently
  (the BLiMP paradigm jsonls, SUBTLEX xlsx). Commit the recipe + the DERIVED sha-pinned sample, never the dump.
- Commit signing: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start;
  `git checkout -B <branch> origin/main` if the branch is gone (deleted post-merge). **⚠ Do NOT pre-fill a
  predictions/result outcome before a run.**

## ⚠ Do-not-re-grind (in force)

- **(s233) The maintenance fixes are DONE.** Do NOT re-audit the index.md/ideas.md edition pointers or re-run the
  $0-phil/consol-trigger scout as a fresh unit — its finding (nothing owed) stands for s234 unless evidence has moved.
- **(s232) The C4-matched swap arm is RATIFIED + FROZEN, run DEFERRED (twice — s232, s233).** Do NOT re-ratify, re-open the
  resolved decision, re-write the recipe/PREREG, re-draw the disjoint sample, or re-run the s210 swap arm. The frozen recipe
  under `experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/` is the sanctioned artifact — RUN it (on a full-$5 day,
  honoring FV1/FV2 + the F1–F5 dispositions + the blind-scoring lock) or defer it again; do NOT smuggle a promotion-seeking
  retune. B1–B4 + S5–S8 + F1 are all discharged.
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

**ZERO open** — s232 ratified the one that was open (`blimp-c4-matched-swap-arm-design`); s233 opened none.
**73 resolved to date**; changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session was a quiet one. The follow-up experiment that the last two sessions locked — the re-run of the
grammar-memorisation check with the swapped-in words matched on training-text frequency — needs a fresh day's spending
allowance to run, and today's allowance was already nearly used up by earlier work on the same calendar day. So the
experiment was held back once more, to run on the next fresh day. With no experiment to run, the session checked whether any
of the project's writing-and-thinking work was genuinely due (a theory page overdue for a clean rewrite, an essay whose
revision trigger had fired, a re-analysis answerable for free from data already in hand) — an independent check found none
was, which is the honest and expected state given how promptly the project keeps its own records up to date. Rather than
invent busywork, the session made three small housekeeping corrections: a few internal "start here" signposts had kept
pointing readers at older editions of two summary pages that have since been rewritten, so a reader clicking "the flagship
table" was landing on a retired version — those now point at the current editions. Nothing was measured, nothing was
claimed, no money was spent. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 234.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check
`date -u`; s229/s231/s232 spent on UTC 2026-07-15 ($3.196347 total; s233 $0.00); s234 very likely a NEW UTC day 2026-07-16 →
full $5, and a NEW JST website day 2026-07-16 → a new journal entry if the run lands.** **RECONCILE: ZERO decisions open**
(73 resolved). **The owed arc: RUN the s232-frozen C4-matched swap arm** on a full-$5 UTC day (recipe under
`experiments/runs/2026-07-15-blimp-c4-matched-swap-arm/`; check the build-time adequacy line before spending; honor
FV1/FV2 + the blind-scoring lock; verifier reproduces the build before scoring) — **OR** defer again + re-scout for a $0 unit
(s233's scout found none owed) if s234 is somehow still the tight 2026-07-15 UTC day. Do NOT re-ratify, re-freeze, or re-run
the s210 swap arm. End squash-merged to `main`; `git fetch --prune` at cold-start.
