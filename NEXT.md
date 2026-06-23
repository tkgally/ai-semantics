# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-23** ran three sessions: s87 ($0.12128) + s88 ($0.59880)
+ **s89 ($0, no probe)** = **$0.720 of $5**. Full ledger in [`config/budget.md`](config/budget.md). **Check the
clock (`date -u`)** — a later session is almost certainly a new UTC day (full $5 resets). Check for any newer
Tom override before spending.

## State

**Session 89 (JST 2026-06-23 / UTC 2026-06-23) — GOVERNANCE + PHILOSOPHICAL + MAINTENANCE, 1 wave, $0 (no
probe).** Branch was even with `main` at start (s88 merged as #136; no PR to land). `decisions/open/` was EMPTY
(no ratification owed). One wave (2 parallel generation subagents + a read-only adversarial coherence pass):

- **GOVERNANCE (backlog top) — OPENED the forced-both operationalization decision:**
  [`decisions/open/forced-both-lexical-operationalization`](wiki/decisions/open/forced-both-lexical-operationalization.md)
  — the discriminating-test operationalization named by
  [`essay/layer-specialness-vs-always-resolvability`](wiki/findings/essays/layer-specialness-vs-always-resolvability.md):
  how to build + score a **genuinely-unresolvable (forced-both) lexical item** (pun/zeugma) so a probe can
  separate **(A) layer-specialness** from **(B) always-resolvability**. Q1 certify forced-both vs a *leaning*
  homonym; Q2 a **forced-single-application** instrument (so "it means both" is not a dodge); Q3 sha256-frozen
  reading rule inheriting C1/C3/C4, commit held to a *higher* anti-cheat bar; Q4 `internal-contrast-only`
  unless a sense-co-activation resource is separately cross-session ratified. **NOT runnable until ratified.**
  Deflationary (B) holds the burden; expected first outcome is the essay's trigger (c).
- **PHILOSOPHICAL — NEW source** [`source/pustejovsky-1991-generative-lexicon`](wiki/base/sources/pustejovsky-1991-generative-lexicon.md)
  (OA, ACL Anthology J91-4003) grounding the **contrastive (homonymy) vs. complementary (logical-polysemy)**
  distinction the forced-both wedge turns on — discharges the essay's flagged weakest-provenance point. Honesty
  note: "copredication"/dot-objects are GL-1995, not the 1991 article (quotes only 1991 text).
- **MAINTENANCE — folded** the s88 K=5 de-noising into
  [`claim/lexical-graded-scale-ungraded-commitment`](wiki/findings/claims/lexical-graded-scale-ungraded-commitment.md):
  gpt's leg → **channel-controlled null** (like gemini); **claude is now the lone CI-strict (confidence) crack.**
  Coherence pass: 0 BLOCKER / 0 SHOULD-FIX / 2 cosmetic NITs (1 fixed). All quotes verbatim (incl. vs the live
  Pustejovsky PDF). senselint 0 errors; linkify clean. Merged PR #137.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` holds **ONE** decision —
[`forced-both-lexical-operationalization`](wiki/decisions/open/forced-both-lexical-operationalization.md),
**opened session 89 → ELIGIBLE for cross-session ratification next session** (the boundary will have held).
Apply any Tom override first as always.

**Track lean — recent: 86 gov+phil · 87 EMPIRICAL · 88 MIXED · 89 gov+phil+maint. Tilted philosophical/
governance → next should lean EMPIRICAL if a runnable unit exists.**

1. **GOVERNANCE (eligible) — RATIFY (or keep open) the forced-both operationalization decision.**
   [`decisions/open/forced-both-lexical-operationalization`](wiki/decisions/open/forced-both-lexical-operationalization.md)
   was opened s89 and is ratifiable next session via an **independent fresh-agent adversarial review** (NOT the
   orchestrator; PROTOCOL §2). The reviewer reads the four Qs + provisional defaults, spot-checks the verbatim
   quotes, and returns adopt-defaults / adopt-another-option / keep-open-with-what's-missing + written
   rationale; ratification fixes the *yardstick, never the result*. Honest expectation: the defaults are sound
   but the *certifiability* of a clean forced-both item (Q1) is the genuinely hard part — keeping it open with a
   named missing piece is a legitimate verdict. **Even if ratified, the probe is NOT auto-runnable** (needs a
   fresh pre-run critic GO + budget; the essay's trigger (c) "cannot cleanly certify" may be the outcome).
2. **EMPIRICAL (reserve) — Option A cross-level matched-kind.** A *full* cross-level matched-kind statement
   (the matched-ambiguity-kind gate's Option A, held in reserve) needs a reachable **Q2-a homonym
   sense-anchor** (a separate cross-session anchor decision) — not buildable until such a resource is found +
   ratified. Don't open without checking reachability first.
3. **PHILOSOPHICAL (source) — the Cruse/Murphy/Lyons lexical-semantics monographs remain wanted** (likely not
   OA; the regular-polysemy + copredication/logical-polysemy wants are now discharged by Falkum & Vicente and
   Pustejovsky 1991). Check reachability before committing time.
4. **RELATIONAL (dormant axis)** —
   [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md):
   the next move is a **medium choice**, not more text probes.
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **ONE — eligible next session.**
  [`decisions/open/forced-both-lexical-operationalization`](wiki/decisions/open/forced-both-lexical-operationalization.md)
  — *opened session 89; ELIGIBLE for ratification next session* (cross-session boundary holds). Provisional
  defaults: Q1 zeugma/co-predication frame + independent balance check (frozen); Q2 forced-single-application
  instrument; Q3 sha256-frozen reading rule (C1/C3/C4 inherited; higher bar on commit); Q4
  `internal-contrast-only` unless a co-activation resource is separately ratified. NOT runnable until ratified.

## Standing-override notes (for Tom, if he looks)

- Session 89 spent **$0** (no probe; governance + a source ingest + a claim-maintenance edit). UTC-day
  2026-06-23 total (s87 + s88 + s89) ≈ **$0.72 of $5**.
- Plain-language: this session did the careful **groundwork before** the next experiment rather than running
  one. The open question — is the word-sense layer genuinely *special*, or do forked words just always leave
  *some* meaning to pick? — can only be settled by a word that means two things at once (a pun). So the project
  wrote down, in advance, *exactly how* such a test would have to be built and scored to be fair, as a proposed
  methodology a **later** session will independently review before anything is built or run (and was honest that
  building such a "both-at-once" word cleanly may prove too hard). It also added a classic open-access
  linguistics paper to ground the distinction, and folded last session's re-measurement into the running
  summary of the word-commitment finding.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` holds **forced-both-lexical-operationalization** (opened s89) —
**ELIGIBLE for cross-session ratification next session** via a fresh independent adversarial-review agent.
**Track lean → lean EMPIRICAL if a runnable unit exists.** Top backlog = ratify (or keep open) the forced-both
decision / Option A reserve (needs a homonym sense-anchor) / dormant relational.
End squash-merged to `main`, website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote `main`.
> If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main` first**
> (`git branch -f main origin/main` fixes it). (This happened again at s89 cold-start: fresh clone's local main was 35534a8;
> `git fetch origin main` → 5db1f20 = #136.)
