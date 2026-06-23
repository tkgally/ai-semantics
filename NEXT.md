# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-23** ran four sessions: s87 ($0.12128) + s88 ($0.59880)
+ s89 ($0) + **s90 ($0, no probe)** = **$0.720 of $5**. Full ledger in [`config/budget.md`](config/budget.md).
**Check the clock (`date -u`)** — a later session is almost certainly a new UTC day (full $5 resets). Check for
any newer Tom override before spending.

## State

**Session 90 (JST 2026-06-23 / UTC 2026-06-23) — GOVERNANCE (ratification), single major unit, $0 (no probe).**
Branch was even with `main` at start (s89 merged as #138; no PR to land). Local `main` lagged the true remote
(fresh-clone artifact — see cold-start note below); fixed with `git fetch origin main` + `git branch -f`.
`decisions/open/` held **ONE** decision, eligible this session:

- **RATIFIED** [`decisions/resolved/forced-both-lexical-operationalization`](wiki/decisions/resolved/forced-both-lexical-operationalization.md)
  (opened s89 → eligible s90; the cross-session boundary held). A **fresh, independent adversarial reviewer**
  (not the orchestrator) returned **ADOPT DEFAULTS** for all four questions: **Q1-iii** (zeugma/co-predication
  frame + an independent, not-model-based balance check, both sha256-frozen — confirmed to **fail safe**: an
  item that can't be certified independent of model output is *declared uncertified*, never let through);
  **Q2-i** (a forced-single-application instrument on which "it means both" is structurally not a dodge);
  **Q3** (sha256-frozen reading rule, `answer-both` kept as its own class, **commit held to a higher anti-cheat
  bar** + clean-subset check, C1/C3/C4 inherited); **Q4** (`internal-contrast-only` unless a sense-co-activation
  resource is separately cross-session ratified — no anchor invented). **Quote-integrity PASS** (load-bearing
  quotes verified character-for-character against the essay, the two result pages, `concept/polysemy`,
  `resource/dwug-usage-graphs`); **anti-cheat PASS** (every default makes a spurious (A) win *harder*; the
  "cannot cleanly certify" NULL is first-class; verdict **not** result-motivated). `contingent-artifacts` empty
  — the essay [`essay/layer-specialness-vs-always-resolvability`](wiki/findings/essays/layer-specialness-vs-always-resolvability.md)
  is `contingent-on: []`, held at **R1**, unaffected (nothing promoted/retired).

Integrated: moved open→resolved with full review record; changelog entry in
[`decisions/resolved/index.md`](wiki/decisions/resolved/index.md); `wiki/index.md` updated (count 36→37; no
decision now open; Most-recent block; moved-path link fix; essay catalog entry notes the gate is now buildable).
senselint 0 errors; linkify clean. Website + journal updated (JST stamp). 37 decisions ratified to date.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no decision owed ratification. Apply
any Tom override first as always.

**Track lean — recent: 86 gov+phil · 87 EMPIRICAL · 88 MIXED · 89 gov+phil+maint · 90 governance. Heavily
tilted governance/philosophical → next should lean EMPIRICAL, and now a runnable unit exists.**

1. **EMPIRICAL (top — now buildable) — build + freeze the forced-both lexical probe under the resolved gate.**
   [`decisions/resolved/forced-both-lexical-operationalization`](wiki/decisions/resolved/forced-both-lexical-operationalization.md)
   is ratified, so the yardstick is fixed and a build session may now construct + sha256-freeze: (a) a
   forced-both stimulus set certified via the **Q1-iii** two-part criterion — a zeugma/co-predication syntactic
   frame **plus** an *independent (not model-based)* balance check that neither sense dominates; (b) a **Q2-i**
   forced-single-application instrument on which "it means both" cannot complete the task; (c) the **Q3**
   frozen reading rule (response classes → (A)-commit / (B)-decline; `answer-both` its own class; clear-class
   precondition → per-model NO-GO; higher bar on commit) — all frozen **before** any model output, then a
   **fresh independent pre-run critic GO/NO-GO** + a budget check before any spend. **Honest expectation: the
   Q1 certification is the hard part** — the essay's trigger (c) "cannot cleanly certify a forced-both item
   rather than a leaning homonym" may well fire, in which case the fork stays at R1 and that is a legitimate,
   first-class outcome (NOT a failure). Do **not** relax any band to force a runnable item. The grounding for
   the contrastive-vs-complementary (homonymy-vs-logical-polysemy) distinction the build turns on is in-repo:
   [`source/pustejovsky-1991-generative-lexicon`](wiki/base/sources/pustejovsky-1991-generative-lexicon.md) +
   [`source/falkum-vicente-2015-polysemy`](wiki/base/sources/falkum-vicente-2015-polysemy.md) +
   [`concept/polysemy`](wiki/base/concepts/polysemy.md).
2. **EMPIRICAL (reserve) — Option A cross-level matched-kind.** A *full* cross-level matched-kind statement
   (the matched-ambiguity-kind gate's Option A, held in reserve) needs a reachable **Q2-a homonym sense-anchor**
   (a separate cross-session anchor decision) — not buildable until such a resource is found + ratified. Don't
   open without checking reachability first. (Note: a sense-**co-activation** resource would *also* discharge
   the forced-both Q4 anchor, lifting it off `internal-contrast-only` — worth scouting once.)
3. **PHILOSOPHICAL (source) — the Cruse/Murphy/Lyons lexical-semantics monographs remain wanted** (likely not
   OA; the regular-polysemy + copredication/logical-polysemy + contrastive/complementary wants are now
   discharged by Falkum & Vicente, Sennet, and Pustejovsky 1991). Check reachability before committing time.
4. **RELATIONAL (dormant axis)** —
   [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md):
   the next move is a **medium choice**, not more text probes.
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty (the only entry,
  [`forced-both-lexical-operationalization`](wiki/decisions/resolved/forced-both-lexical-operationalization.md),
  was ratified this session and moved to `resolved/`).

## Standing-override notes (for Tom, if he looks)

- Session 90 spent **$0** (no probe; a governance ratification only). UTC-day 2026-06-23 total
  (s87 + s88 + s89 + s90) ≈ **$0.72 of $5**.
- Plain-language: this session ran the **independent review** that the project's rules require before the
  test-plan written last session can be adopted. A separate reviewer re-read the whole plan, checked every
  quoted passage word-for-word, confirmed it makes a spurious "the word layer is special" answer *harder* (not
  easier) to manufacture — including that its trickiest step fails safe — and signed it off. The plan is now
  fixed, so a future session **may** build and run the "both-meanings-at-once" (pun/zeugma) test, though only
  after a fresh go/no-go check and within budget, and with the standing honest caveat that building such a word
  cleanly may prove too hard (in which case the question stays open rather than getting a forced answer).

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — nothing owed ratification.
**Track lean → lean EMPIRICAL — a runnable unit now exists:** build + freeze the forced-both lexical probe under
the ratified gate (top backlog), under a fresh pre-run critic + budget; honest expectation is trigger (c)
"cannot cleanly certify". Reserve: Option A (needs a homonym sense-anchor) / dormant relational (medium choice).
End squash-merged to `main`, website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote `main`.
> If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main` first**
> (`git branch -f main origin/main` fixes it). (Happened again at s90 cold-start: fresh clone's local main was cbccbe5;
> `git fetch origin main` → 50e2edf = #138.)
