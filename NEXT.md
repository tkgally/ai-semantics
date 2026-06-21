# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 76 (UTC 2026-06-21) spent **$0** (empirical unblock to run-ready + theory sync —
no model queried). UTC-day 2026-06-21 total is unchanged at **$2.870** ($1.964 s64 + $0.503 s69 + $0.280 s71 + $0.123 s72 +
$0 s70/73/74/75/76) of $5.00 (headroom **$2.130** *if the next session is still 2026-06-21 UTC*; a new UTC day resets to the
full $5 — **check the clock**). Single-run prefer-split flag unchanged (~$2.50/run). Full ledger in
[`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 76 (UTC 2026-06-21) — empirical unblock, $0 — drove the lexical bridging-context probe to RUN-READY and got an
independent pre-run-critic GO; deferred the spend-bearing run to a fresh UTC budget day.** Workflow mode: one wave of 3
parallel disjoint-file units + an orchestrator-authored frozen instrument + an independent pre-run critic (judgement, not
parallelized) + verification. No experiment ran.

- **EMPIRICAL — both run blockers CLEARED; the probe is RUN-READY (pre-run critic GO).**
  - **(a) Corpus re-fetch recipes written + verified ($0).** [`prep.py`](experiments/designs/lexical-bridging-context-v1/prep.py)
    re-fetches DWUG (Zenodo 14028531, archive sha `64eef477…` verified) and re-maps **48/48** frozen stratum pairs →
    usage sentences + target offsets (0 failures) into the gitignored data area;
    [`prep_wic.py`](experiments/designs/lexical-bridging-context-v1/prep_wic.py) re-fetches WiC (archive sha `f1a2fb67…`,
    matches the resource-page copy) and freezes a **20 + 20** clear-pole supplement
    ([`wic_poles.csv`](experiments/designs/lexical-bridging-context-v1/wic_poles.csv), sha `b8b1a7aa…`; clear poles ONLY,
    never bridging). Corpus text stays out of git (CC BY-ND / CC BY-NC, gitignored).
  - **(b) Instrument numbers FROZEN + sha256'd** ([`instrument.json`](experiments/designs/lexical-bridging-context-v1/instrument.json),
    sha `901ea89f…`): B primary (`b_rel` 0–100 relatedness = position; `b_conf` SAME/DIFFERENT + 0–100 confidence),
    C cross-check (`c_third` SAME/DIFFERENT/UNCLEAR, verbatim third-option wording, decline rate), A characterizing-only
    (`a_forced`, 5 samples temp 1.0), Q3 `topic` control. Per-axis reading rule (position by B alone; confidence/dispersion
    by **both** B and C; mixed/weak ≠ null; clear-class precondition; usage-similarity claim cap). Runner
    [`probe.py`](experiments/designs/lexical-bridging-context-v1/probe.py) is config-driven (no inline knob; gemini reasoning
    suppressed for cost). No-API dry run OK (88 items = 48 DWUG + 40 WiC; bridging = 24 DWUG-only).
  - **Independent pre-run critic GO** (a fresh agent re-derived the cheat-surface): conditions (a)–(i) all PASS; the
    degenerate-responder surface (always-mid / always-UNCLEAR / always-SAME) is closed by the clear-class precondition;
    `[40,60]` band + neutral third-option wording are not gameable post-hoc (the sha binds them). 7 non-blocking
    run-session cautions are folded into the design's §7.
- **PHILOSOPHICAL — theory sync.** [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md)
  and [`theory/situating-llm-meaning`](wiki/findings/theory/situating-llm-meaning.md) now register the cross-item
  graded-**scale** vs within-item graded-**commitment** distinction and link
  [`essay/graded-scale-ungraded-commitment`](wiki/findings/essays/graded-scale-ungraded-commitment.md) + the open question.
- **Why the run was deferred (disciplined, not blocked):** day headroom ~$2.13 < v1's gemini-driven ~$3.13 lexical-run
  cost; a fresh UTC day resets the $5 cap, so a clean run beats squeezing a scaled one in today.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no open decisions, no ratifications owed. Apply any
Tom override first.

**Track lean.** 73 phil · 74 method · 75 governance+lexical · 76 **empirical-unblock + phil-sync**. The lexical axis is the
**active front and now RUN-READY** — running it is the lowest-friction way to land a result; keep weighting there until the
bridging probe runs, then rebalance.

1. **EMPIRICAL — RUN the lexical bridging-context probe** (everything below the run is done; this is the top item):
   - **(a) Stage the gitignored corpus** in the fresh clone: run `python3 experiments/designs/lexical-bridging-context-v1/prep.py`
     then `prep_wic.py` (both re-fetch + re-map; `probe.py` `sys.exit`s if the DWUG fulltext is missing). *Network-bearing —
     verify the environment's network policy allows the Zenodo + WiC fetch; if blocked, that is an honest blocker to record.*
   - **(b) Pre-flight budget** per [`config/budget.md`](config/budget.md) and **run** `OPENROUTER_API_KEY=… python3 probe.py`.
     **Cost-aware:** v1's lexical run billed gemini ~$2.61 (reasoning-heavy); `probe.py` already suppresses reasoning — keep
     gemini effort minimal, and if the single-shot estimate exceeds $2.50, **split by model** or **drop the characterizing-only
     A read** (omitting A cannot touch the verdict).
   - **(c) Mandatory empirical clear-class precondition check** (BUILDABILITY flags 9/7 clear-same as marginal): the clear
     classes must show high confidence (B) + low decline rate (C). **If unmet even with the 20 WiC-T poles → collapse to
     `internal-contrast-only` and relabel** — do not relax the precondition.
   - **(d) Analyze + write the result**, leading with the **usage-similarity ≠ sense-co-presence cap**; disclose b_conf's
     self-report risk, the near-degenerate independent context control (4/48 nonzero overlap → model-`topic` partial is the
     operative Q3), and the small lemma-clustered N. The frozen reading rule decides supported / mixed-weak / clean-null.
   - Files: [`experiments/designs/lexical-bridging-context-v1.md`](experiments/designs/lexical-bridging-context-v1.md) (§7 run
     handoff + the 7 critic cautions); instrument/stratum/WiC + prep/probe in `experiments/designs/lexical-bridging-context-v1/`.
   - On the outcome, the essay [`essay/graded-scale-ungraded-commitment`](wiki/findings/essays/graded-scale-ungraded-commitment.md)
     revision triggers (a)/(b)/(c) fire — strengthen or revise it accordingly; promote a `claim` page per the route the probe ran.
2. **DIVERSIFY (if the lexical run isn't picked up / network-blocked)** — essay trigger (b) the few→many scalar mechanism
   (`internal-contrast-only`, human anchor scouted null — [`result/function-word-few-many-split`](wiki/findings/results/function-word-few-many-split.md)),
   or the dormant **relational** axis (order-composition ladder).
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**NONE.** `wiki/decisions/open/` is empty (both lexical bridging gates resolved session 75; do not re-ratify).

## Standing-override notes (for Tom, if he looks)

- Session 76 spent **$0** (no model queried; UTC-day 2026-06-21 total unchanged at $2.870 of $5).
- Plain-language version: the word-ambiguity test the last two sessions designed and "built to the edge of running" is now
  **ready to run**. This session cleared the two things that stood in the way — it wrote and checked a recipe that re-fetches
  the underlying sentences (kept out of the project under a no-derivatives licence) and re-attaches them to the locked-down set
  of 48 word-use pairs (all reconnected cleanly), shored up the thinnest group with 20 + 20 clear examples from a second
  human-rated collection, and **locked the test's exact measuring numbers** (the confidence scale, the "in-between" band, the
  "unclear" wording, the sampling settings) with a fingerprint so none can be nudged after results arrive. An **independent
  reviewer checked the finished setup and gave it a green light**, confirming a model can't cheat by answering "in-between" or
  "unclear" to everything. The run itself was **held back to a fresh day** because today's remaining budget was below what the
  run is likely to cost. No experiment ran.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC).** **RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratifications owed.
**The lexical bridging-context probe is RUN-READY (pre-run critic GO):** re-run `prep.py` + `prep_wic.py` to stage the
gitignored corpus, pre-flight budget (gemini reasoning suppressed; split / drop-A if the single shot > $2.50), run `probe.py`,
do the **mandatory empirical clear-class precondition check** (collapse to `internal-contrast-only` if unmet), then analyze +
write the result **leading with the usage-similarity-vs-sense cap**. Or diversify (few→many mechanism / relational). End
squash-merged to `main`, website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote
> `main`. If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main`
> first** (sessions 64–76 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (re-fetch via
> `experiments/data/subtlex-us/prep.py`). The **DWUG corpus text** (CC BY-ND) and the **WiC corpus text** (CC BY-NC) are also
> gitignored — re-fetch via `experiments/designs/lexical-bridging-context-v1/prep.py` (DWUG, all 48/48 stratum pairs re-map)
> and `prep_wic.py` (WiC clear poles). The committed artifacts (frozen `stratum.csv`, `instrument.json` + sha, `wic_poles.csv`
> + sha) carry only identifiers/ratings/wordings — no corpus sentences. The full BLiMP dataset is **not** in-repo (only a
> 10-line sample).
