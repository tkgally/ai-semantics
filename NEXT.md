# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-22** total ≈ **$4.34** of $5.00 (77 $0.756 + 79 ≈$2.83 + 82
$0.251 + 82b $0.274 + **84 ≈$0.23** [run $0.20656 + pre-flight ≈$0.02]). Leaving ≈$0.66 on 2026-06-22.
**If the next session is a new UTC day (2026-06-23+), the full $5 resets — check the clock** (`date -u`). Full ledger in
[`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 84 (UTC 2026-06-22) — EMPIRICAL marquee: RAN the shared-instrument cross-level probe → DISSOLVE 3/3 (the
first-class null).** Branch was even with `main` at start (no PR to land). `wiki/decisions/open/` was EMPTY — no
ratification owed. The headline:

- **RAN + VERIFIED the cross-level shared-instrument probe** (`experiments/designs/cross-level-shared-instrument-v1/`,
  frozen instrument sha `3cdfe178…` unchanged through the run) under the resolved gate
  [`decisions/resolved/cross-level-shared-instrument-operationalization`](wiki/decisions/resolved/cross-level-shared-instrument-operationalization.md)
  (Option A + C1–C4). One frozen graded SAME/DIFFERENT/UNCLEAR + 0–100 confidence instrument applied **identically** at
  the lexical / constructional / relational legs. **444 calls, $0.20656 billed, 0 missing/error, 444/444 parsed.**
  Verdict **DISSOLVE 3/3** → [`result/cross-level-shared-instrument-v1`](wiki/findings/results/cross-level-shared-instrument-v1.md):
  the *discrete-on-the-moment* posture (commit on the ambiguous item, ≈0% UNCLEAR) holds **only at the lexical level**;
  at constructional + relational the **same models** take UNCLEAR **elevated** on the genuinely-ambiguous item
  (graded-on-moment). The aggregate/moment shape **does not survive instrument-equalization** → the deflationary
  "three rhyming instrument-specific facts" default stands. `anchor: internal-contrast-only` (gate Q4). gpt's
  constructional leg was a C3 NO-GO (it over-declines its own clear controls, 35% > 20%).
- **Process:** measured budget pre-flight caught a **confidence-parser bug** in the runner (`probe.py`'s first-`\d+`
  parse captured the digit inside `READING1`/`FIGURE1` etc., and leaked "Round 5" stamps) → fixed to *integer-after-token*,
  `instrument.json` byte-identical (C2 sha intact), **fresh independent critic re-GO** confirmed anti-cheat-neutral
  (commit `58083ca`). **Two** independent pre-run critic GOs (design+instrument; parser fix) + an independent post-run
  verifier that **REPRODUCED every cell + all 18 bootstrap CIs to the digit**, parse integrity, cost, corpus-safety.
- **Downstream:** conjecture [`cross-level-gradience-aggregate-not-moment`](wiki/findings/conjectures/cross-level-gradience-aggregate-not-moment.md)
  `designed → tested` (its pre-registered *dissolution* outcome); OQ
  [`gradience-population-not-moment`](wiki/findings/open-questions/gradience-population-not-moment.md) deflationary
  default now **evidenced**; essay [`cross-level-convergence-ladder`](wiki/findings/essays/cross-level-convergence-ladder.md)
  **trigger (b) FIRED** (the anticipated worked example of a rhyme correctly *not* promoted at R2). senselint 0 errors;
  linkify clean; index + budget + website (JST 23:45 stamp; index/journal/findings §5/plans) updated.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — no decision is open, so **no ratification is owed**
next session (unless this/a later session opens one). Apply any Tom override first.

**Track lean — recent: 82 empirical · 83 empirical-build+phil · 84 empirical. Empirical-heavy → next should lean
PHILOSOPHICAL.**

1. **PHILOSOPHICAL (marquee, no spend — corrects the track lean).** Digest the dissolution. The "graded-aggregate /
   discrete-moment" cross-level shape is now empirically **three instrument-specific facts, not one property** — the
   project's standing deflationary default is now *evidenced*, not just assumed. A short **essay or theory note** is owed:
   (a) what the *lexical specialness* means (why does the word-sense layer alone commit-without-hedging, while the same
   models readily decline on genuinely ambiguous sentences and underdetermined dialogue?); (b) cross-link/lightly note in
   the three level-home essays ([`graded-scale-ungraded-commitment`](wiki/findings/essays/graded-scale-ungraded-commitment.md),
   [`aggregation-not-constitution`](wiki/findings/essays/aggregation-not-constitution.md),
   [`preference-without-commitment`](wiki/findings/essays/preference-without-commitment.md)) that the cross-level *join*
   failed equalization (each level's own finding stands; only the unification fell). No retraction owed — the legs were
   always scoped to their own levels.
2. **EMPIRICAL (the honest residual of the dissolution; would OPEN a new decision — surface, don't decide in-session).**
   The dissolution's load-bearing caveat is that the three levels' "ambiguous" classes are not the same *kind* of
   indeterminacy (lexical usage-similarity midpoint = milder; constructional structural / relational same-round dual-bind =
   genuine both/neither). A **matched-ambiguity-kind** cross-level follow-up — equalize the *kind* of ambiguity (e.g. truly
   two-sense lexical items genuinely ambiguous in a single context, matched to the structural/relational genuine
   ambiguities) — would test whether the lexical specialness *survives* a harder lexical ambiguity or was an artifact of
   the milder bridging stimulus. This needs an **operationalization decision** (how to certify "matched ambiguity kind"
   across levels, and a human anchor or `internal-contrast-only` posture for the new lexical class) → **open a
   `wiki/decisions/open/` entry** (options + provisional default), ratify a *later* session. Pre-flight cheap (~$0.10–0.25).
3. **EMPIRICAL (cheap, still-open from 82/82b — the verdict resolver).** BYTE-IDENTICAL REPEATED-RUNS (K≥5) test of gpt's
   forced-decomposition lexical leg: sessions 82/82b disagreed (MIXED/WEAK vs channel-CONTROLLED) by ~2 of 24 decline items,
   at/under the ~12% temp-0 jitter. Re-run **#128's frozen instrument** (`dceafa9d…`) K≥5× at temp 0 over the same 88 items,
   read the de-noised majority-vote / range on the decline axis. ~$0.25–1.25. The honest closure of that channel check.
4. **RELATIONAL (dormant axis)** — [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md):
   the next move is a **medium choice**, not more text probes (any real probe needs a human anchor flagged `pending` or an
   `internal-contrast-only` posture, and would open a `wiki/decisions/open/` entry).
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **None.** `wiki/decisions/open/` is empty. Thirty-five decisions ratified to date
  ([`decisions/resolved/index.md`](wiki/decisions/resolved/index.md)). Session 84 opened none (the cross-level run reused
  the resolved gate's fixed choices; the parser fix was a runner-bug correction faithful to the frozen format, not a new
  operationalization knob). The **matched-ambiguity-kind follow-up (backlog 2) is the candidate the next session would open.**

## Standing-override notes (for Tom, if he looks)

- Session 84 spent **≈$0.23** (run $0.20656 + pre-flight ≈$0.02; UTC-day 2026-06-22 total ≈$4.34 of $5).
- Plain-language version: this session **ran the fair test** built last session — one question asked in identical wording at
  three layers of meaning (word senses, grammar, conversation reference) — and it came back a **clean negative**: the
  recurring "confident on every single hard case" pattern is **specific to the word-sense layer** and does **not** hold up
  when you measure all three layers the same way, so it is three coincidences rather than one underlying trait. A pre-flight
  spot-check caught and fixed a bug in the scoring code before any result was read; two independent reviewers approved the
  run and another reproduced every number afterward. Nothing here is stated as a comparison to human behaviour.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then
[`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratification owed (unless one is opened).
**Track lean → empirical-heavy (82–84).** The marquee next unit is **PHILOSOPHICAL** (digest the cross-level dissolution:
what the lexical specialness means; note the failed join in the three level-home essays); pair with the cheap empirical
K-run resolver, or open the matched-ambiguity-kind decision (surface only). End squash-merged to `main`, website updated
**with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote `main`.
> If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main` first** (sessions
> 64–84 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (re-fetch via
> `experiments/data/subtlex-us/prep.py`). The **DWUG corpus text** (CC BY-ND) and the **WiC corpus text** (CC BY-NC) are
> also gitignored — re-fetch via the lexical v1 `prep.py` (DWUG, 48/48 stratum pairs re-map) and **`map_wic_fulltext.py`**
> (maps the committed frozen WiC manifest to text). The **cross-level probe** (`cross-level-shared-instrument-v1`) reuses
> those same gitignored full-text files at run time via its `items_lexical.json` sha-manifest; its committed `raw/` is
> safe (short labels + item-id/lemma pointers, **no corpus text** — verified). The lexical working-surface and
> forced-decomposition probes' committed `raw/` is **sanitized** (`sanitize_raw.py`). The full BLiMP dataset is **not**
> in-repo (only a sample).
