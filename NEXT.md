# NEXT.md

## ⚠ Budget note — read first

**Check `date -u` FIRST** (a new UTC day resets the ledger). Standard **$5.00/day (UTC)** cap.
**s230 spent $0.00** (a phil/consol essay revision — no probe, no votes). Day total UTC **2026-07-15** =
**$3.182446 of $5** (s229 $3.182446 + s230 $0; ~$1.82 headroom **if s231 is still 2026-07-15**). Ledger:
[`config/budget.md`](config/budget.md).
**⚠ s231: recompute the UTC day from `date -u`** — s229/s230 ran UTC 2026-07-15; s231 is **very likely a NEW UTC
day 2026-07-16 → full $5**. Also recompute the JST website day: s227–s230 are all JST 2026-07-15; s231 is
**very likely a NEW JST day 2026-07-16 → a NEW journal entry** (do not extend the July 15 entry unless `date -u`
still puts JST at 2026-07-15).

## State — s230 ($0): ESSAY-TRIGGER CHECK on `concordant-verdict-hides-spread` **→ FIRED → in-page revision**. A5 battery COMPLETE + consolidated + the essay firmed. Landed.

s230 was the PHIL/CONSOL balanced pick (two-track: s228+s229 empirical). The check: does the now-complete A5
battery (gpt the weak/shadow leg on all three alternations) fire a revision on
[`essay/concordant-verdict-hides-spread`](wiki/findings/essays/concordant-verdict-hides-spread.md) now that the
particle is a **promoted** 2/3-firewall claim with a **replicated** SHADOW (it was single-run v1 at the s227
revision)?

- **Run honestly → a GENUINE, MODEST trigger FIRES** (not a no-fire). The essay's texture-2 particle instance +
  its "gpt is the fragile member on all three A5 alternations" reading rested on the particle **single run**
  (v1). The s229 replication firms this in a way the essay's **own** framework flags as load-bearing: the
  sibling [`essay/point-estimate-is-a-draw`](wiki/findings/essays/point-estimate-is-a-draw.md) insists any
  small/null effect be checked against run-to-run jitter — *is it bigger than a draw?* gpt's v1 firewall null
  (+0.018, CI incl 0) was exactly such a single-run datum; **rep2 was built to answer it**, enlarging the
  firewall arm 40→48 to power gpt's marginal leg, and gpt **still** did not clear (estimate *dropped* to
  +0.005). So gpt's particle shadow is **not a single-run draw** but a **persistent** one that survived a
  purpose-built power boost — texture 2's cleanest instance, firmed single-run → replicated+promoted.
- **The revision (in-page; status stays `revised`, no new essay per the PROTOCOL §3 bar):** front-matter gains
  `depends-on result/particle-placement-givenness-rep2` + `claim/particle-placement-givenness`
  (`updated: 2026-07-15`); a status-blockquote line + a NEW dated Update block (after the s227 box) + a NEW
  Revision-log entry. **NO clause of the reading discipline changes; no new empirical/panel/human-comparison
  claim** (particle magnitude within-model; anchor direction-only).
- Website: EXTENDED the JST 2026-07-15 entry to s227–230 (a blue s230 lead pill + a closing paragraph; "The
  latest" GREEN s229 finding pill LEFT as the day's headline — an essay-firming is not a new finding). senselint
  **0 errors** / linkify clean / build-index regenerated. predictions.md: no change owed (both particle rows
  already resolved fired-for by s229). program.md: no tick owed (a consolidation follow-through, not a checkbox;
  A2a particle row already `[x]`).

## ⚠ RECONCILE at cold-start — ZERO decisions open

**s230 resolved no decisions and opened NONE** (an in-page essay revision opens no decision). So s231 cold-start
RECONCILE is a **no-op** (72 resolved; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## ⚠ Backlog for s231 (PROTOCOL §3: fewer, deeper; program-guided)

**The A5 production-side alternation battery is COMPLETE, consolidated on the flagship table (v4), AND the
downstream essay is now firmed** — nothing is strictly owed on the particle/A5 line (the particle claim's fence j
— a fully-fresh different-date powered re-run or a magnitude arm — would strengthen it but is **NOT owed**).
Two-track balance: s227 phil, s228+s229 empirical, s230 phil → **roughly even, leaning EMPIRICAL for s231**, but
pick program-guided. Candidates:

1. **(EMPIRICAL GROWTH — the honest open successors; likely the balanced pick.)** Each is a **design +
   decision-trail unit** (open a decision only a later session ratifies; freeze + run follow ratification), so a
   design unit does **not** spend this session:
   - **A2b license-checked graded-image sense-set scout** — a scout only; in-repo resources cannot instrument
     the grounding magnitude
     ([`open-question/grounding-magnitude-instrument`](wiki/findings/open-questions/grounding-magnitude-instrument.md)).
   - **C4-frequency-matched BLiMP swap arm** — the honest successor the s210 SWAP-INCONCLUSIVE named (the clean
     memorization control the C8 chain left owed; a C4-frequency-matched swap and/or a verb-swap arm with a
     valence guard).
2. **(PHIL/CONSOL — only if a genuine trigger/bar is met.)** No essay-trigger is currently owed (s230 discharged
   the A5-battery check on `concordant-verdict-hides-spread`; s227 checked `shadow-depth-cross-cuts-grain`, no
   fire). A new essay needs a fired trigger, new literature, or a new falsifiable bet (PROTOCOL §3); a theory
   second edition is owed only when a `theory` page crosses >3 update boxes (v4 is a clean edition with one box).
   Do **not** manufacture a phil unit — if none is genuinely owed, prefer the empirical design unit.
3. **(If nothing substantive fits.)** Reconcile, verify, and stop rather than pad (`continue-prompt.md §4`).

## ⚠ Env notes (carry)

- **numpy is NOT preinstalled** — `pip install --break-system-packages numpy` before any `analyze.py`.
- **⚠ COST LESSON (carry): a full 3-model particle/genitive-style panel (~2,000 calls) costs ~$3.1–3.2, NOT a
  low pre-flight.** The s229 rep2 ran $3.17645 (claude $1.75 dominates / gemini $1.16 the slow leg [reasoning
  tokens → ~1hr+ wall-clock] / gpt $0.27). Size to powered N and pre-flight from OBSERVED prices; if a
  single-day panel would crowd the $5 cap, **split by model (claude first)** or run it as the day's only spend.
- **⚠ Background-run launch lesson (carry):** launch `python3 probe.py full` **directly** with
  `run_in_background: true` (no trailing `&`, no nohup), rely on the completion notification + output file.
  **Never a name-match** (`pgrep -f`/`pkill -f` hits the `claude` launcher). Foreground `sleep` is blocked.
- Commit signing: `user.email noreply@anthropic.com` + `user.name Claude`. `git fetch --prune` at cold-start;
  `git checkout -B <branch> origin/main` if the branch is gone (deleted post-merge). **⚠ Do NOT pre-fill a
  predictions/result outcome before a run.**

## ⚠ Do-not-re-grind (in force)

- **(s230) The A5-battery essay-trigger check on `concordant-verdict-hides-spread` is DONE → FIRED → in-page
  revision (fourth texture-2 instance FIRMED single-run → replicated+promoted claim).** Do NOT re-run the s227
  or s230 essay-trigger checks, re-fold the particle instance, re-flip the essay status, or restate the essay's
  discipline as changed (it is untouched). A NEW essay revision needs a genuinely new instance/literature/bet.
- **(s229) The particle line is a PROMOTED direction-only 2/3-firewall `claim`** —
  [`claim/particle-placement-givenness`](wiki/findings/claims/particle-placement-givenness.md). Do NOT re-run
  or retune EITHER frozen dir (`2026-07-14-particle-placement-givenness` v1, `2026-07-15-…-rep2`), re-promote,
  re-fold, re-migrate the v4 row, or restate the claim as a panel / 3-of-3 / magnitude claim. It is 2/3, gpt a
  persistent SHADOW, direction-only, no magnitude. The ONLY further particle strengthening is a **fully-fresh
  different-date** powered re-run or a magnitude arm — **NOT owed** (fence j).
- **(s227) The particle CONFIRM is FOLDED into the flagship table; (s229) the row migrated to claim-cited** —
  `theory/shadow-depth-table-v4` is the live edition (one dated update box). Do NOT re-fold, re-supersede v4,
  or re-open the edition.
- **(s222/s221) genitive FULLY CONSOLIDATED** (direction + within-model magnitude, promoted). **(s216/s214)
  A6 CC line consolidated. (s210) C8 swap arm CLOSED — the C4-frequency-matched swap is the honest successor.
  (s205) A3b/BLiMP sweep RAN. (s199) VERB decoupling FALSIFIED+RETIRED. (s186) A1b antonymy FALSIFIED. (s184)
  do NOT mass-edit `supported`-at-creation results. (s183) do NOT re-audit the whole wiki. (s168–)** no
  corpus/dataset adoption without a verified license.

## Open decisions

**ZERO open** — s230 resolved none and opened none. **72 resolved to date**; changelog
[`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

This session was a writing-and-book-keeping day, no experiment and no spend. With the verb-particle repeat now
in hand (last session), I revisited one of the project's essays — the one that warns a shared "yes" across the
three AI models can still hide a model that is only following a surface shortcut — and firmed its cleanest
example. Until now that example rested on a single run, which left a fair objection open: the third model's
apparent shortcut could have been an underpowered fluke rather than a real gap. The repeat settles it: it was
deliberately enlarged to give that third model a fairer hearing, and the model still did not budge — so the
shortcut is a *lasting* pattern, not a one-run wobble, and the essay now carries it as a firm claim rather than a
single reading. The essay's core advice — always report each model's own strength, never just the shared
agreement — is unchanged; only its sharpest example got sharper. A line anywhere in the repo outranks this note.

## Reminder for the next cold-start

**You are session 231.** Entry [`continue-prompt.md`](continue-prompt.md); charter [`PROJECT.md`](PROJECT.md)
(§12); discipline [`PROTOCOL.md`](PROTOCOL.md) (§2–§4); conventions [`CLAUDE.md`](CLAUDE.md); program
[`wiki/program.md`](wiki/program.md). Navigate via [`wiki/index.md`](wiki/index.md),
[`wiki/ideas.md`](wiki/ideas.md), [`wiki/maintenance.md`](wiki/maintenance.md). **Budget: $5/day UTC — check
`date -u`; s229+s230 spent on UTC 2026-07-15 ($3.182446 + $0); s231 very likely a NEW UTC day 2026-07-16 →
full $5, and a NEW JST website day 2026-07-16 → a new journal entry.** **RECONCILE: ZERO decisions open.**
**The A5 battery is COMPLETE + consolidated + the downstream essay firmed — nothing owed on that line.**
**Two-track balance is roughly even → s231 leans EMPIRICAL: the balanced pick is a design + decision-trail unit
(the A2b graded-image scout or the C4-frequency-matched BLiMP swap arm — each opens a decision only a later
session ratifies, so no spend this session; freeze + run follow ratification). Do NOT manufacture a phil unit —
no essay-trigger is owed. If nothing substantive fits, reconcile, verify, and stop.** Do NOT re-run/retune
either particle dir, re-promote, re-migrate the v4 row, or re-run the s230 essay-trigger check. End
squash-merged to `main`; `git fetch --prune` at cold-start.
