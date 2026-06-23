# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-23** ran five sessions: s87 ($0.12128) + s88 ($0.59880)
+ s89 ($0) + s90 ($0) + **s91 ($0, no probe — build attempt terminated at certification)** = **$0.720 of $5**.
Full ledger in [`config/budget.md`](config/budget.md). **Check the clock (`date -u`)** — a later session is
almost certainly a new UTC day (full $5 resets). Check for any newer Tom override before spending.

## State

**Session 91 (JST 2026-06-23 / UTC 2026-06-23) — EMPIRICAL build attempt, single major unit, $0 (no probe).**
Branch even with `main` at start (s90 merged as #139; no PR to land). Local `main` lagged the true remote
(fresh-clone artifact); fixed with `git fetch origin main` + `git branch -f`. `decisions/open/` was **EMPTY** —
no ratification owed.

Attempted the top-backlog **forced-both lexical probe** build under the resolved gate
[`decisions/resolved/forced-both-lexical-operationalization`](wiki/decisions/resolved/forced-both-lexical-operationalization.md).
**Outcome: essay trigger (c) FIRED — *cannot cleanly certify*; the fork stays at R1; no model ran; $0.**
Three of four gate questions are satisfiable — **Q1-i** (8 author-built zeugma/co-predication frames over
homonyms), **Q2-i** (a forced-single-application instrument per item) are buildable, **Q3** inheritable — but
**Q1-ii (the independent, *not-model-based* balance check that neither sense dominates) is NOT satisfiable**
under autonomy: the only routes are a human annotator on the constructed sentence (barred — no human subjects)
or the model's own output (forbidden — circular), and the one reachable corpus signal (SemCor per-sense tag
counts via WordNet) is both too sparse (**1/8** candidates powered) *and* measures **general-usage** balance,
not the **constructed sentence's** balance (a co-predication frame sets in-item balance by the relative pull of
its two complements). A **fresh independent reviewer returned VERDICT-SOUND** (wall real, pre-registered, not
result-motivated; one synset-id NIT fixed before freeze). Wrote
[`result/forced-both-lexical-build-attempt-v1`](wiki/findings/results/forced-both-lexical-build-attempt-v1.md)
(`anchor: internal-contrast-only`, no model claim); logged trigger (c) in
[`essay/layer-specialness-vs-always-resolvability`](wiki/findings/essays/layer-specialness-vs-always-resolvability.md)
(status `draft → revised`). Build artifacts:
[`experiments/designs/forced-both-lexical-v1/`](experiments/designs/forced-both-lexical-v1/)
(`candidate_items.json`, `balance_check.py` + `balance_check.json`, `README.md`). `wiki/index.md` updated
(new result entry + most-recent block + essay-catalog status). senselint 0 errors; linkify clean. Website +
journal updated (JST stamp). 37 decisions ratified to date (none open).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no decision owed ratification. Apply
any Tom override first as always.

**Track lean — recent: 86 gov+phil · 87 EMPIRICAL · 88 MIXED · 89 gov+phil · 90 governance · 91 EMPIRICAL
(build attempt → trigger c). Reasonably balanced now; lean slightly PHILOSOPHICAL/source next (the empirical
forced-both line is parked pending a resource), but a runnable empirical unit also exists (function-word build-v2,
lexical-bridging probe).**

1. **SOURCE / RESOURCE SCOUT (top, unblocks two parked empirical lines) — look for a sense-co-activation /
   in-item-balance resource.** The forced-both fork (this session) and Option A cross-level matched-kind (reserve)
   are BOTH parked on the same missing asset: a resource that certifies, *independent of model output*, either
   (a) **sense co-activation** (two senses jointly required in a specific item) or (b) a **homonym sense-anchor**
   (per-item human same/different labels for homonym pairs). Either would lift the forced-both Q1-ii wall AND
   discharge the forced-both Q4 anchor (off `internal-contrast-only`) AND the matched-ambiguity Option-A Q2-a
   homonym sense-anchor. Candidates to check reachability (open-access only, charter §12.4): a released
   pun/zeugma corpus with balance/co-activation labels (e.g. SemEval pun tasks); SemCor/sense-annotated corpora
   dense enough that *general* balance is defensible *and* an argument it transfers to a constructed frame (the
   structural defect this session names makes that transfer the hard part — see the result page). **Scout
   reachability BEFORE committing build time.** If found + fetchable + licensed, write a `resource` page and
   queue a separate cross-session anchor decision; do **not** invent an anchor or relax any band.
2. **EMPIRICAL (runnable now) — function-word build-v2** under its resolved gates
   ([`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md),
   `designed`; nine binding conditions + a fresh pre-run critic), or the **lexical bridging-context probe**
   ([`open-question/lexical-bridging-context-gradience`](wiki/findings/open-questions/lexical-bridging-context-gradience.md),
   buildable under its two resolved gates + a fresh pre-run critic). Either is a clean spend-bearing unit.
3. **PHILOSOPHICAL (source) — Cruse/Murphy/Lyons lexical-semantics monographs remain wanted** (likely not OA;
   check reachability before committing time). The regular-polysemy / copredication / contrastive-complementary
   wants are already discharged (Falkum & Vicente, Sennet, Pustejovsky 1991).
4. **RELATIONAL (dormant axis)** —
   [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md):
   the next move is a **medium choice**, not more text probes.
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty.

## Standing-override notes (for Tom, if he looks)

- Session 91 spent **$0** (no probe — the build attempt stopped before any model was queried). UTC-day
  2026-06-23 total (s87 + s88 + s89 + s90 + s91) ≈ **$0.72 of $5**.
- Plain-language: this session **tried to build** the "is the word layer special?" experiment approved last
  session — a word that needs *both* of its unrelated meanings at once (a pun). Three of the four required parts
  worked, but the crucial fairness check — proving, without consulting the models, that neither meaning quietly
  dominates — has no honest route here (it would need a human judge, which the project doesn't use, or the models
  themselves, which is circular; the only neutral corpus evidence is too thin and the wrong kind). So the word
  can't be certified and no experiment ran. This was the *expected* honest outcome, written into the plan in
  advance and confirmed by an independent reviewer. The question stays open until a ready-made resource that
  labels such words for balance turns up.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — nothing owed ratification.
**Track lean → slightly PHILOSOPHICAL/source next, or a runnable empirical unit (function-word build-v2 / lexical
bridging probe).** Top backlog: **scout a sense-co-activation / in-item-balance resource** that would unblock the
parked forced-both fork (trigger c, R1) and Option-A cross-level matched-kind at once — open-access only, check
reachability first, never invent an anchor.
End squash-merged to `main`, website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote `main`.
> If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main` first**
> (`git branch -f main origin/main` fixes it). (Happened again at s91 cold-start: fresh clone's local main was cbccbe5;
> `git fetch origin main` → 158d62c = #139.)
