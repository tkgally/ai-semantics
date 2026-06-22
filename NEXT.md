# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-22** total ≈ **$4.34** of $5.00 (77 $0.756 + 79 ≈$2.83 + 82
$0.251 + 82b $0.274 + 84 ≈$0.23). **Session 85 spent $0.00** (philosophical, no probe). Leaving ≈$0.66 on 2026-06-22.
**If the next session is a new UTC day (2026-06-23+), the full $5 resets — check the clock** (`date -u`). Full ledger in
[`config/budget.md`](config/budget.md). Check for any newer Tom override before spending.

## State

**Session 85 (JST 2026-06-23 / UTC 2026-06-22) — PHILOSOPHICAL marquee (corrected the empirical-heavy lean; $0 spent).**
Branch was even with `main` at start (Session 84 merged as #132; no PR to land). `wiki/decisions/open/` was EMPTY at start —
no ratification owed. The headline:

- **NEW essay [`essay/ambiguity-kind-not-level`](wiki/findings/essays/ambiguity-kind-not-level.md)** ("Kind, not level") —
  digests the Session-84 dissolution by **re-reading** it: the dissolution's commit/decline split is more parsimoniously
  indexed by the **kind** of indeterminacy than by the **level**. The models *commit* on a **scalar** ambiguity (a graded
  similarity with a *nearer pole* to lean to — the lexical bridging stimulus) and *decline* on a **disjunctive** one (two
  complete readings/bindings, *both/neither*, no nearer pole — the constructional/relational items), so the lexical leg's
  specialness may be the **softness of its stimulus, not the word-sense layer**. **Explicitly does NOT revive** the dissolved
  level-conjecture: kind is confounded with level in that design, so the reading is held at **R1** on the
  [`convergence ladder`](wiki/findings/essays/cross-level-convergence-ladder.md), *not* asserted as a finding, and routed to
  the matched-ambiguity-kind probe. No new empirical claim; no human comparison. (status: draft)
- **OPENED a decision** [`decisions/open/matched-ambiguity-kind-cross-level`](wiki/decisions/open/matched-ambiguity-kind-cross-level.md)
  (surface only; **session 85; NOT ratifiable until session 86+**) — how to certify **matched ambiguity *kind*** across/within
  levels (so the discrete-vs-graded contrast is fair) + the **anchor posture for a genuinely-disjunctive lexical class** (a
  balanced homonym context is **not** a DWUG usage-similarity midpoint, so the resolved lexical anchor cap does **not** transfer).
  Provisional default **Option B** (keep DWUG; *add* a balanced-homonym disjunctive lexical class as a *within-lexical*
  scalar-vs-disjunctive contrast, level held fixed) + Q2 anchor **`internal-contrast-only`** unless a homonym sense-resource is
  separately ratified later. No anchor invented.
- **Cross-linked the three level-home essays** ([`graded-scale-ungraded-commitment`](wiki/findings/essays/graded-scale-ungraded-commitment.md),
  [`aggregation-not-constitution`](wiki/findings/essays/aggregation-not-constitution.md),
  [`preference-without-commitment`](wiki/findings/essays/preference-without-commitment.md)) with a CROSS-LEVEL NOTE: each level's
  own finding **stands** (nothing retracted); only the cross-level *join* failed equalization (R2 dissolution). Pointer to the
  kind-not-level successor reading.
- **Process:** workflow mode, one wave — 2 parallel subagents (decision page + adversarial coherence pass), orchestrator wrote
  the marquee essay + the three cross-links + integration. Coherence pass: 0 BLOCKERs; 1 SHOULD-FIX (a quoted-punctuation slip)
  + 2 NITs (added emphasis inside a quote; a "read-out" phrasing near the causal line) — **all fixed**. senselint 0 errors;
  linkify clean; index + website (JST 01:54 stamp; index/journal/findings §5/plans) updated.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` now holds **ONE** decision —
[`matched-ambiguity-kind-cross-level`](wiki/decisions/open/matched-ambiguity-kind-cross-level.md), **opened session 85 →
eligible for cross-session ratification from session 86+**. The next session **owes its independent adversarial-review
ratification** (fresh agent, not the orchestrator that does the downstream work; verdict = adopt default Option B / adopt
another / keep open; apply per PROTOCOL §2). Apply any Tom override first.

**Track lean — recent: 82 empirical · 83 empirical-build+phil · 84 empirical · 85 PHILOSOPHICAL. Now balanced → next may lean
EMPIRICAL** (a fresh UTC day likely resets the full $5).

1. **EMPIRICAL (if the matched-ambiguity-kind decision ratifies) — BUILD the within-lexical scalar-vs-disjunctive probe.** On
   an ADOPT-Option-B ratification, build + freeze (sha256 before output) the design: keep the DWUG scalar-bridging lexical class,
   ADD a balanced-homonym disjunctive lexical class, same frozen shared instrument + C1–C4 inherited unchanged; `internal-contrast-only`
   for the disjunctive arm. Freeze-before-results; fresh pre-run critic GO + budget check before any spend. The first-class
   outcomes are pre-declared (survival = lexical commits even on a balanced homonym → lexical-as-layer; collapse = %UNCLEAR rises →
   the softness reading). Pre-flight cheap (~$0.10–0.30, same shape as the Session-84 run).
2. **EMPIRICAL (cheap, still-open from 82/82b — the verdict resolver).** BYTE-IDENTICAL REPEATED-RUNS (K≥5) test of gpt's
   forced-decomposition lexical leg: sessions 82/82b disagreed (MIXED/WEAK vs channel-CONTROLLED) by ~2 of 24 decline items, at/under
   the ~12% temp-0 jitter. Re-run **#128's frozen instrument** (`dceafa9d…`) K≥5× at temp 0 over the same 88 items, read the
   de-noised majority-vote / range on the decline axis. ~$0.25–1.25. The honest closure of that channel check.
3. **PHILOSOPHICAL (only if a phil unit is wanted) — ingest a lexicography source for the kind axis.** The new essay's weakest
   provenance point (flagged in-page) is that the scalar-vs-disjunctive / polysemy-vs-homonymy distinction stands on
   [`concept/polysemy`](wiki/base/concepts/polysemy.md) + the result's caveat alone. An open-access semantics/lexicography source
   on regular-vs-irregular ambiguity (or systematic polysemy vs homonymy) would strengthen it; check reachability before committing.
4. **RELATIONAL (dormant axis)** — [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md):
   the next move is a **medium choice**, not more text probes (any real probe needs a human anchor flagged `pending` or an
   `internal-contrast-only` posture, and would open a `wiki/decisions/open/` entry).
5. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **[`matched-ambiguity-kind-cross-level`](wiki/decisions/open/matched-ambiguity-kind-cross-level.md)** — *opened this session
  (session 85), **NOT yet eligible** for ratification; eligible from session 86+.* The matched-ambiguity-kind follow-up to the
  Session-84 dissolution. Provisional default Option B (within-lexical scalar-vs-disjunctive contrast) + Q2-b
  (`internal-contrast-only`). Thirty-five decisions ratified to date ([`decisions/resolved/index.md`](wiki/decisions/resolved/index.md)).

## Standing-override notes (for Tom, if he looks)

- Session 85 spent **$0.00** (philosophical thinking session; no probe). UTC-day 2026-06-22 total unchanged at ≈$4.34 of $5.
- Plain-language version: this session **re-read** last session's clean negative and sharpened it. Last session found the
  "confident on every hard case" habit belongs to the *word-sense* layer alone. This session noticed the word layer was handed
  a **milder kind** of puzzle (an in-between similarity, with a closer answer to lean to) than the other layers (genuine forks
  with no closer answer), so the models may be **consistent** — committing when there's a nearer answer, hedging when there isn't —
  and the real dividing line may be the *kind* of ambiguity, not the layer. This is filed as a sharper **question**, not a revival
  of the abandoned "one trait" claim, and a follow-up test was queued for a *later* session to approve: give the word layer a truly
  forked case ("bank": river or money?) and see whether it still commits. Nothing here is a comparison to human behaviour.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then
[`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` holds **ONE** decision — `matched-ambiguity-kind-cross-level` (opened session 85,
**eligible for ratification from session 86+**). The next session **owes its independent adversarial-review ratification**.
**Track lean → now balanced (85 was phil).** Natural next marquee is **EMPIRICAL**: on an ADOPT ratification, build+freeze the
within-lexical scalar-vs-disjunctive probe (backlog 1); or run the cheap K-run resolver (backlog 2). End squash-merged to `main`,
website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote `main`.
> If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main` first** (sessions
> 64–85 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list is **gitignored** (re-fetch via
> `experiments/data/subtlex-us/prep.py`). The **DWUG corpus text** (CC BY-ND) and the **WiC corpus text** (CC BY-NC) are
> also gitignored — re-fetch via the lexical v1 `prep.py` (DWUG, 48/48 stratum pairs re-map) and **`map_wic_fulltext.py`**
> (maps the committed frozen WiC manifest to text). The **cross-level probe** (`cross-level-shared-instrument-v1`) reuses
> those same gitignored full-text files at run time via its `items_lexical.json` sha-manifest; its committed `raw/` is
> safe (short labels + item-id/lemma pointers, **no corpus text** — verified). The lexical working-surface and
> forced-decomposition probes' committed `raw/` is **sanitized** (`sanitize_raw.py`). The full BLiMP dataset is **not**
> in-repo (only a sample).
