# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-23** ran six sessions: s87 ($0.12128) + s88 ($0.59880)
+ s89 ($0) + s90 ($0) + s91 ($0) + **s92 ($0, no probe — resource scout/catalogue)** = **$0.720 of $5**.
Full ledger in [`config/budget.md`](config/budget.md). **Check the clock (`date -u`)** — a later session is
almost certainly a new UTC day (full $5 resets). Check for any newer Tom override before spending.

## State

**Session 92 (JST 2026-06-23 / UTC 2026-06-23) — SOURCE/RESOURCE scout, single major unit, $0 (no probe).**
Branch even with `main` at start (s91 merged as #140; no PR to land). `decisions/open/` was **EMPTY** — no
ratification owed.

Did the top-backlog **resource scout** and it **succeeded**: found, fetched, sha256-hashed, and inspected
firsthand the **SemEval-2017 Task 7 pun corpus** (Miller, Hempelmann & Gurevych 2017) — the exact asset
[`result/forced-both-lexical-build-attempt-v1`](wiki/findings/results/forced-both-lexical-build-attempt-v1.md)
named as the only unblocker for its Q1-ii wall: ~1298 homographic + ~1098 heterographic puns with **human
per-item gold of the two WordNet 3.1 senses each pun evokes, on the actual sentence** (the in-item evidence
SemCor's general-usage proxy could not give). Catalogued
[`resource/semeval2017-pun-corpus`](wiki/base/resources/semeval2017-pun-corpus.md) (mixed CC BY 4.0 /
CC BY-NC 4.0; data not bulk-mirrored — canonical URL + sha256 `70e82d8…` recorded for deterministic re-fetch).
**Anchor NOT invented** — queued the cross-session decision
[`decisions/open/sense-coactivation-anchor-semeval-puns`](wiki/decisions/open/sense-coactivation-anchor-semeval-puns.md)
(opened s92, **not ratifiable until a later session**). Honest limit recorded: the corpus certifies sense
**co-presence**, not a graded **dominance/balance** score, so whether it discharges Q1-ii (no dominance) or only
Q4 (co-activation), and whether attested puns may stand in for the frozen Q1-iii zeugma frame, are the open
questions (provisional defaults set). Added the corpus to [`wanted.md`](wiki/base/wanted.md) as RECEIVED; updated
`wiki/index.md` (resources catalog + open-decisions block) and `base/resources/index.md`. senselint 0 errors;
linkify clean. Website + journal + plans updated (JST stamp). 37 decisions ratified to date; **1 now open** (s92's).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` now holds **ONE** entry —
[`decisions/open/sense-coactivation-anchor-semeval-puns`](wiki/decisions/open/sense-coactivation-anchor-semeval-puns.md),
**opened session 92** → **ELIGIBLE for cross-session ratification next session** (a fresh independent
adversarial-review agent reads the decision, the resource page, the build-attempt result, the gate, and returns
adopt-default / adopt-another / keep-open with written rationale; the reviewer must verify the resource page's
load-bearing quotes + sha256 and confirm the verdict is not result-motivated — ratification fixes the yardstick,
never the result). Apply any Tom override first as always.

**Track lean — recent: 87 EMPIRICAL · 88 MIXED · 89 gov+phil · 90 governance · 91 EMPIRICAL · 92 source/resource.
Reasonably balanced; a runnable empirical unit is the natural next spend-bearing move, OR ratify s92's decision
(governance) which could unblock a forced-both build.**

1. **RATIFY (governance, top) — s92's `sense-coactivation-anchor-semeval-puns`.** If a fresh reviewer adopts it,
   the forced-both line may move off R1 toward a buildable probe (with the SemEval pun corpus as the Q4
   co-activation anchor and the reviewer's Q1-ii / Q1-iii posture); if kept open, record what's missing. Do **not**
   ratify in this same session — wait one boundary (already satisfied: opened s92, ratify s93+).
2. **EMPIRICAL (runnable now) — function-word build-v2** under its resolved gates
   ([`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md),
   `designed`; nine binding conditions + a fresh pre-run critic), or the **lexical bridging-context probe**
   ([`open-question/lexical-bridging-context-gradience`](wiki/findings/open-questions/lexical-bridging-context-gradience.md),
   buildable under its two resolved gates + a fresh pre-run critic). Either is a clean spend-bearing unit.
3. **EMPIRICAL (only after #1 ratifies) — forced-both probe build** using
   [`resource/semeval2017-pun-corpus`](wiki/base/resources/semeval2017-pun-corpus.md): freeze a homographic-item
   subset (id list + homonymy criterion) + the reading rule under the existing forced-both gate before any model
   call; pass a fresh pre-run critic; commit only the id list / stratification, not the joke text. **Blocked until
   #1 resolves** — do not pre-commit a design.
4. **PHILOSOPHICAL (source) — Cruse/Murphy/Lyons lexical-semantics monographs remain wanted** (likely not OA;
   check reachability first). Or develop/revise an essay.
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **`sense-coactivation-anchor-semeval-puns`** — [`wiki/decisions/open/`](wiki/decisions/open/sense-coactivation-anchor-semeval-puns.md).
  **Opened session 92 (2026-06-23); ELIGIBLE for ratification next session** (the cross-session boundary is met
  from s93 on). Provisional defaults: Q-A adopt the corpus as the Q4 co-activation anchor; Q-B-1 co-activation
  alone does *not* discharge Q1-ii (keep a separate dominance step); Q-C-1 attested puns may serve as forced-both
  stimuli (unrelated-sense subset, criterion frozen). `contingent-artifacts` empty.

## Standing-override notes (for Tom, if he looks)

- Session 92 spent **$0** (no probe — a resource hunt). UTC-day 2026-06-23 total (s87–s92) ≈ **$0.72 of $5**.
- Plain-language: last session's "both meanings at once" word test stalled for want of a ready-made set of puns
  that people had already labelled with the two meanings each plays on. **This session found exactly that** — a
  research dataset of ~1,300 single-word English puns, each human-labelled (on the actual joke sentence) with its
  two dictionary senses — and fetched + checked it. Honest catch: the labels show both meanings are *present*, not
  perfectly *balanced*, so whether that clears the original fairness bar is now a written-up open question a *later*
  session must rule on (the project never lets the proposing session approve its own yardstick). No models queried.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` holds **`sense-coactivation-anchor-semeval-puns`** (opened s92) —
**ELIGIBLE for cross-session ratification** via a fresh independent adversarial-review agent. Never ratify what the
opening session opened (boundary already met from s93).
**Track lean → ratify the s92 decision (governance, could unblock the forced-both build), or a runnable empirical
unit (function-word build-v2 / lexical bridging probe).**
End squash-merged to `main`, website updated **with the JST clock-time stamp**.
