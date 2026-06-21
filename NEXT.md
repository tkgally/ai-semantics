# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 74 (UTC 2026-06-21) spent **$0** (a planning/groundwork session — no
model queried). UTC-day 2026-06-21 total is unchanged at **$2.870** ($1.964 s64 + $0.503 s69 + $0 s70 + $0.280
s71 + $0.123 s72 + $0 s73 + $0 s74) of $5.00 (headroom **$2.130** *if the next session is still 2026-06-21 UTC*; a
new UTC day resets to the full $5 — check the clock). Single-run prefer-split flag unchanged (~$2.50/run). Full
ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 74 (UTC 2026-06-21) — dual-track planning/groundwork, $0 — cleared the path to reopen the lexical axis,
added a possible human yardstick (BLiMP), and recorded an honest null on the scalar human anchor.** Workflow mode:
one wave of 4 parallel bounded units + an independent read-only adversarial coherence pass (clean — no
BLOCKERs/SHOULD-FIX content defects; 3 hygiene fixes applied: dropped a stray `type:decision`, registered the two
new resource pages in both indexes), then a small synthesis edit. No experiment ran.

- **EMPIRICAL/governance — the two lexical bridging-context gate decisions are now OPEN** (named, not opened, by
  [`open-question/lexical-bridging-context-gradience`](wiki/findings/open-questions/lexical-bridging-context-gradience.md)
  last session). Both ratify **cross-session** (earliest next session):
  - [`decisions/open/lexical-bridging-context-operationalization`](wiki/decisions/open/lexical-bridging-context-operationalization.md)
    — how to measure "intermediate, less-confident" within-item behavior (Option A spread/entropy, B graded-confidence,
    C "both/unclear" third option), frozen before any data; provisional default a frozen B+C panel with B–C agreement,
    A characterizing-only. Names the failure mode (tuning the instrument until intermediacy appears) and the first-class
    null.
  - [`decisions/open/lexical-bridging-context-anchor`](wiki/decisions/open/lexical-bridging-context-anchor.md) — what
    human-grounded signal certifies an item as "genuinely bridging" (Option 1 DWUG mid-scale/high-disagreement pairs,
    2 WiC for the clear poles only, 3 engineered constructions = `internal-contrast-only`, strictly weaker). Provisional
    default the DWUG-derived stratum; per-item rater thinness forced as the load-bearing caveat.
- **EMPIRICAL infrastructure — BLiMP catalogued** as [`resource/blimp`](wiki/base/resources/blimp.md) (Warstadt et al.
  2020 TACL; 67k acceptability minimal pairs, 96.4% human agreement, CC-BY README-prose; 67 files fetched + schema
  inspected, 10-line sample sha256-pinned, full set not committed). It is the optional non-blocking **Posture-2
  human-acceptability upgrade** named in [`decisions/resolved/function-word-anchor-design`](wiki/decisions/resolved/function-word-anchor-design.md).
  **Acceptability only** — cannot anchor entailment/implicature/sense-similarity.
- **PHILOSOPHICAL/empirical feed — honest null on the scalar human anchor.**
  [`resource/scalar-implicature-anchor-scouting`](wiki/base/resources/scalar-implicature-anchor-scouting.md) scouted
  van Tiel et al. 2016 (on-target quantifier rate, paywalled/OA-PDF-403), Pankratz & van Tiel 2025 (CC BY but
  adjectival/off-target), VAQUUM (appropriateness ≠ implicature-rate; license unverified), Scivetti CxNLI (single gold,
  no quantifiers): **no clean openly-licensed quantifier-specific human implicature-rate set found.** So essay trigger
  (b)'s human-comparison upgrade stays **blocked**; `internal-contrast-only` is the honest posture. Logged as a
  "NOT FIRED" status note under trigger (b) of
  [`essay/function-words-not-one-category`](wiki/findings/essays/function-words-not-one-category.md) (no claim changed).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` now holds **TWO** decisions, both opened **this session
(74)** and therefore **eligible for ratification by the next session** (an independent fresh-agent adversarial-review
pass each — never the session that opened them, and never the orchestrator that did this session's downstream work).
Apply any Tom override first. The two:
- `lexical-bridging-context-operationalization` — *opened session 74, eligible next session.*
- `lexical-bridging-context-anchor` — *opened session 74, eligible next session.*
Ratifying fixes the **yardstick, never the result**. If a reviewer keeps one open, carry it forward with what's missing.

**Track lean.** 69 emp · 70 dual · 71 dual · 72 dual · 73 philosophical+diversify · 74 **method/groundwork (lexical-gov
+ infra + philosophical scouting)**. The modal/function-word line stays saturated; both tracks are alive. Keep
weighting toward the lexical axis and diversification rather than squeezing the modal line further.

1. **RECONCILE → then EMPIRICAL/diversify — the lexical bridging-context probe.** Ratify the two gates above
   (cross-session). Once ratified, the probe is **buildable**: construct + certify a frozen 3-class set (clearly-same /
   clearly-different / bridging) per the ratified instrument and anchor, pass an independent pre-run critic, then run
   (spend-bearing). Anchor default DWUG ([`resource/dwug-usage-graphs`](wiki/base/resources/dwug-usage-graphs.md)) — mind
   the per-item rater thinness the resource page and the anchor decision both flag. Lowest-friction way to advance the
   reopened lexical axis.
2. **PHILOSOPHICAL/EMPIRICAL — essay trigger (b), the few→many scalar mechanism.** The human-anchor sub-route is now
   scouted to a **null** (see [`resource/scalar-implicature-anchor-scouting`](wiki/base/resources/scalar-implicature-anchor-scouting.md)),
   so the live sub-route is a **mechanism probe**, `internal-contrast-only`: a quantifier-scope probe (`some`/`many`/`most`/`all`
   × scalar upper-bounding) pinning *why* the panel divides on "Many X → All X"
   ([`result/function-word-few-many-split`](wiki/findings/results/function-word-few-many-split.md)). A within-model
   contrast, no human-comparison claim, until a quantifier-specific human set turns up. (If a future literature refresh
   finds the van Tiel 2016 quantifier rates via a reachable OA route, the human-comparison upgrade reopens.)
3. **OPTIONAL — exercise the BLiMP Posture-2 upgrade for the function-word line.** [`resource/blimp`](wiki/base/resources/blimp.md)
   is now in-repo; the function-word swap results (all `internal-contrast-only`) could gain a human-**acceptability**
   comparison on the determiner-noun/quantifier/NPI overlap. Acceptability ≠ entailment, so it backs the form side, not
   the entailment-flip indicator — frame carefully. Never blocks a within-model run.
4. **DIVERSIFY further — the relational axis** (order-composition ladder, dormant since ~s44) for a different kind of
   rebalancing if the lexical unit isn't picked up.
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**TWO, both opened session 74, both eligible for ratification next session (cross-session rule):**
- [`decisions/open/lexical-bridging-context-operationalization`](wiki/decisions/open/lexical-bridging-context-operationalization.md)
  — *opened session 74; eligible next session.*
- [`decisions/open/lexical-bridging-context-anchor`](wiki/decisions/open/lexical-bridging-context-anchor.md)
  — *opened session 74; eligible next session.*

## Standing-override notes (for Tom, if he looks)

- Session 74 spent **$0** (no model queried; UTC-day 2026-06-21 total unchanged at $2.870 of $5).
- Plain-language version: a planning session with one honest dead-end. It cleared the path to reopen the project's
  quieter *word-meaning* thread by writing down — as formal proposals for a *later* session to approve — the two
  judgment calls a future "do models get less sure on deliberately ambiguous words?" test must settle first: how to
  measure "less sure," and how to certify a word is genuinely ambiguous using human-rated data. It also catalogued a
  standard human-checked grammar benchmark (BLiMP) as a *possible* future way to compare the models to people on
  grammatical well-formedness. And it went looking for published human data on how people read quantity words like
  *many*/*few* (to ask which model reading matches people on a recent split) and **came up empty** — the on-target
  study is paywalled, the free data covers other words — so that comparison stays out of reach and the result remains a
  contrast among the models only. No experiment ran.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** `wiki/decisions/open/` holds **two** decisions (both lexical
bridging gates, opened session 74) — **both eligible for ratification next session** via independent fresh-agent
adversarial review (never the orchestrator). **The modal/function-word line is saturated; keep weighting to the
lexical axis:** after ratifying the two gates, the **lexical bridging-context probe** becomes buildable (build + certify
+ critic + run, spend-bearing); or pursue **essay trigger (b)** (the few→many scalar mechanism, now `internal-contrast-only`
because the human anchor scouted null), or a **dormant axis** (relational). End squash-merged to `main`, website updated
**with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote
> `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main`
> first** (sessions 64–74 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (not in a fresh clone) — re-fetch via
> `experiments/data/subtlex-us/prep.py` before re-running any `build.py`/`certify.py` that reads `freqlib.py`. The modal
> stimuli themselves are committed. The full BLiMP dataset is **not** in-repo (only a 10-line sample); re-fetch from the
> repo BLiMP catalogues if a probe needs it.
