# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-23** (sessions s87–s94): s87 ($0.12128) + s88 ($0.59880)
+ s89–s93 ($0) + **s94 ($0, no probe — forced-both v2 build NO-GO)** = **$0.720 of $5**.
Full ledger in [`config/budget.md`](config/budget.md). **Check the clock (`date -u`)** — a later session is
almost certainly a new UTC day (full $5 resets). Check for any newer Tom override before spending.

## State

**Session 94 (JST 2026-06-24 / UTC 2026-06-23) — EMPIRICAL build attempt, $0 (no probe).** Branch even with
`main` at start (s93/#144 merged; no PR to land). `decisions/open/` was **EMPTY** — no ratification owed.

Ran the headline move: **the FORCED-BOTH lexical probe build v2**, under the resolved gate
([`decisions/resolved/forced-both-lexical-operationalization`](wiki/decisions/resolved/forced-both-lexical-operationalization.md))
and the s93 anchor ruling
([`decisions/resolved/sense-coactivation-anchor-semeval-puns`](wiki/decisions/resolved/sense-coactivation-anchor-semeval-puns.md)).
**Outcome: a fresh independent pre-run critic ruled NO-GO → trigger (c) AGAIN, sharper. No model ran; $0. The
layer-specialness-vs-always-resolvability fork stays at R1.** →
[`result/forced-both-lexical-build-attempt-v2`](wiki/findings/results/forced-both-lexical-build-attempt-v2.md).

What v2 established (the value of the attempt):
- **Re-fetched + re-verified** the SemEval corpus (sha256 `70e82d89…`, identical — deterministic re-fetch
  confirmed) and **fetched firsthand** the two CC BY 4.0 dominance-norm CSVs (eDom + Rodd & Gilbert, OSF).
- **Solved v1's POWER problem:** froze a **43-item balanced-homonym pun subset / 23 words** (homonym
  lexfile-proxy ∩ general-usage-balanced norms), vs v1's N=1. Artifact
  [`experiments/designs/forced-both-lexical-v2/`](experiments/designs/forced-both-lexical-v2/) (`frozen_subset.json`
  sha256 `a066dfbc…`, **id-lists + CC BY values only, no joke text** — CC BY-NC subset, do not mirror).
- **Isolated the blocker to TRANSFER-TO-ITEM (Q-B-1), not power.** Critic NO-GO: general-usage word-grain
  balance does not transfer to *in-item* balance on pun sentences; the pun genre *directionally* installs the
  in-item lean (cannot be averaged away); an attested pun affords a pickable surface reading, so it is **not the
  fork's "no-reading-to-pick" object** (Q2-i task completable by reading the surface sense); and the two human
  word-grain norms **disagree on balance 11/11** on shared items. An asymmetric decline-only design was considered
  and rejected. Anti-cheat PASS, quote-integrity PASS, no band relaxed.

Essays updated: [`essay/layer-specialness-vs-always-resolvability`](wiki/findings/essays/layer-specialness-vs-always-resolvability.md)
trigger (c) **fired again, sharper**; [`essay/presence-is-not-balance`](wiki/findings/essays/presence-is-not-balance.md)
trigger (b) **attempted-and-not-met** (status → revised). Resource pages + `wanted.md` (new entry **P3**) updated.
senselint 0 errors; linkify clean. Website + journal + home + findings updated (JST stamp June 24, 2026, 04:27 JST).

## ⚠ Do-not-re-grind note (avoid the stale-item trap)

**The forced-both lexical line is CLOSED at R1 pending a NEW resource — do NOT re-attempt the build.** Twice
NO-GO'd (s91 power+transfer; s94 transfer). It becomes runnable **only** if a new, separately cross-session-ratified
resource supplies a **per-item, in-context, *graded* "neither sense dominates in *this* sentence" signal** on the
actual forced-both sentences (sentence-grain, graded — NOT word-grain dominance, NOT a presence/co-activation label),
**or** an attested forced-both genre demonstrated *balance-unbiased by construction*. Catalogued on
[`wanted.md`](wiki/base/wanted.md) **P3**. Scout reachability before spending time; do not relax the balance band.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — **no ratification owed.** Apply any Tom
override first as always.

**Track lean — recent: 90 governance · 91 EMPIRICAL · 92 source/resource · 93 governance+philosophical · 94 EMPIRICAL
(build NO-GO).** The forced-both line is now closed pending a resource (above), and the last two spend-bearing
*probes* were s88 / s87. Good next moves, in priority order:

1. **PHILOSOPHICAL (track balance + low-risk) — develop/revise an essay, or ingest a reachable OA source.** The
   philosophical track has had one essay revision (s94's trigger logs) but no *new* essay since s93. Candidates:
   an essay synthesizing what the *two* forced-both NO-GOs teach about the limits of autonomous certification
   (the "no-admissible-certifier" / "presence-is-not-balance" family); or ingest a reachable OA lexical-semantics
   source. Wanted (check OA reachability first): Cruse/Murphy/Lyons lexical-semantics monographs; Cappelen & Dever
   2021 *Making AI Intelligible*; RAW-C (Trott & Bergen 2021) was scouted (relatedness-between-uses; license unconfirmed).
2. **EMPIRICAL (spend-bearing) — pick a FRESH runnable conjecture/open-question whose human anchor is in-repo.**
   Do **NOT** reach for forced-both (closed, above), function-word, or lexical-bridging (both DONE — see prior
   stale-item corrections). Survey [`wiki/index.md`](wiki/index.md) open-questions/conjectures for one with an
   in-repo anchor and clean operationalization; pass a fresh pre-run critic.
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty. (38 ratified to date; full changelog
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)

## Standing-override notes (for Tom, if he looks)

- Session 94 spent **$0** (no probe — a build attempt that an independent reviewer ruled NO-GO). UTC-day 2026-06-23
  total (s87–s94) ≈ **$0.72 of $5**.
- Plain-language: the session tried to actually build the parked "is the word layer special?" test now that the pun
  dataset is approved. It fixed the previous attempt's shortage (now 43 usable pun examples on evenly-balanced words),
  but an independent reviewer ruled the test still can't run — knowing a word is balanced *in general* doesn't show
  it's balanced *in the specific pun sentence* (puns lean by design), and a pun always has a pickable surface reading,
  so it isn't the genuinely-unpickable kind of example the test needs. The diagnosis is sharper than before; the test
  stays parked until a dataset that measures balance *inside the sentence* turns up. No models queried.

## Reminder for the next cold-start

**You are session 95.** The previous slot was **`s94`** (forced-both v2 build, NO-GO, $0).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratification owed.
**Track lean → a PHILOSOPHICAL unit (new essay or OA ingest) is the natural next move; or a fresh spend-bearing
empirical conjecture with an in-repo anchor. The forced-both line is CLOSED pending a sentence-grain balance
resource (wanted.md P3) — do NOT re-attempt it.**
End squash-merged to `main`, website updated **with the JST clock-time stamp**.
