# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** Session 87 ran on UTC-day **2026-06-23** and spent **$0.12128**
(the within-lexical probe). UTC-day 2026-06-23 total so far ≈**$0.12** of $5. Full ledger in
[`config/budget.md`](config/budget.md). **Check the clock (`date -u`)** — a later session may be a new
UTC day (full $5 resets). Check for any newer Tom override before spending.

## State

**Session 87 (JST 2026-06-23 / UTC 2026-06-23) — EMPIRICAL MARQUEE; $0.121 spent.** Branch was even
with `main` at start (Session 86 merged as #134; no PR to land). The headline:

- **BUILT + FROZE + RAN the within-lexical scalar-vs-disjunctive probe → SURVIVAL 3/3**
  ([`result/within-lexical-scalar-vs-disjunctive-v1`](wiki/findings/results/within-lexical-scalar-vs-disjunctive-v1.md)),
  the marquee from last session's backlog, under the resolved gate
  [`decisions/resolved/matched-ambiguity-kind-cross-level`](wiki/decisions/resolved/matched-ambiguity-kind-cross-level.md)
  (Option B + Q2-b + nuisance-matching freeze). One frozen lexical commitment instrument (inherited
  verbatim from the cross-level lexical leg) applied to a **scalar** arm (DWUG bridging, reused) and a
  **disjunctive** arm (12 author-built balanced homonyms — bank, crane, file, mole, organ, trunk, tank,
  punch, plot, pupil, ring, club — `internal-contrast-only`). Nuisance-matched (SUBTLEX Lg10WF median
  gap **0.00**, length mean gap **0.46**, noun frame; register residual disclosed, cuts toward survival).
  On the disjunctive homonyms **all 3 models commit** (near-zero UNCLEAR: claude 1/12, gpt 0/12, gemini
  0/12), decline not elevated within-arm + indistinguishable from the scalar bridging leg → **SURVIVAL
  3/3** (the higher anti-cheat bar). So the lexical commit-without-hedging is **not** an artifact of the
  softer scalar stimulus — it holds for a genuine lexical disjunction.
- **The essay [`essay/ambiguity-kind-not-level`](wiki/findings/essays/ambiguity-kind-not-level.md) was
  REVISED — its trigger (b) FIRED:** the "kind, not level" reading **dissolves at R2 for the lexical
  case** (status draft → **revised**; the kind-reading retracted for the lexical case, kept visible; the
  conceptual scalar/disjunctive contrast survives). The deflationary "three rhyming facts" reading is
  **reinforced for the level axis** — the lexical leg really is the odd one out, about the **word-sense
  layer**, not the kind.
- **One load-bearing residual is disclosed and bounds the claim:** a balanced homonym is still
  *resolvable-by-committing-to-a-reading*, where a relational same-round dual-binding is literally
  unresolvable — so "word-sense layer special" vs "balanced homonym still affords resolution" is not
  fully isolated. (Plus 4/12 leaning items + register + scalar-flavoured gloss all cut toward survival;
  the pre-registered clean-8 subset gives the same verdict.)
- **Process:** workflow mode, build→freeze→certify (15/15 PASS)→independent pre-run critic **GO**
  (result-neutral; flagged 4/12 leans → clean-8 pre-registered before any output)→run ($0.121, 0
  missing/error, 252/252 parsed)→independent post-run verifier **REPRODUCED** every cell + cost +
  corpus-safety. senselint 0 errors; linkify clean; index + budget + website (JST 10:20 stamp;
  journal/home/findings/plans) updated.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — **no decision is owed
ratification** next session. Apply any Tom override first as always.

**Track lean — recent: 84 empirical · 85 PHILOSOPHICAL · 86 governance+phil · 87 EMPIRICAL.
Slightly empirical-recent → next can lean PHILOSOPHICAL (or a mixed wave).**

1. **PHILOSOPHICAL (natural next) — sharpen the SURVIVAL residual into an essay/conjecture.** The new
   result's load-bearing caveat — a balanced homonym is still *resolvable-by-committing* where a
   relational dual-binding is not — is a genuinely interesting seam: is the lexical commit-without-hedging
   "the word-sense layer is special" or "word-sense is the one level where every ambiguity stays
   resolvable-by-a-reading"? An essay distinguishing **layer-specialness** from **always-resolvability**
   (and noting what *would* separate them) is the cleanest philosophical-track unit; it would `refine`
   [`essay/ambiguity-kind-not-level`](wiki/findings/essays/ambiguity-kind-not-level.md) and
   [`essay/graded-scale-ungraded-commitment`](wiki/findings/essays/graded-scale-ungraded-commitment.md).
2. **PHILOSOPHICAL (still-open from session 86) — ingest a *regular/systematic (Apresjan) polysemy*
   source.** The SEP "Ambiguity" ingest (session 86) grounded the basic polysemy/homonymy carving but did
   NOT develop regular/systematic polysemy (flagged in
   [`source/sennet-2021-ambiguity-sep`](wiki/base/sources/sennet-2021-ambiguity-sep.md)). An open-access
   source (Apresjan-style) or the Cruse/Murphy/Lyons monographs (still in
   [`base/wanted.md`](wiki/base/wanted.md)) would further strengthen the kind axis. Check reachability first.
3. **EMPIRICAL (cheap, still-open from 82/82b — the verdict resolver).** BYTE-IDENTICAL REPEATED-RUNS
   (K≥5) test of gpt's forced-decomposition lexical leg: sessions 82/82b disagreed (MIXED/WEAK vs
   channel-CONTROLLED) by ~2 of 24 decline items, at/under the ~12% temp-0 jitter. Re-run #128's frozen
   instrument (`dceafa9d…`) K≥5× over the same 88 items; read the de-noised majority-vote/range on the
   decline axis. ~$0.25–1.25. Honest closure of that channel check.
4. **EMPIRICAL (harder, held in reserve) — Option A cross-level matched-kind.** A *full* cross-level
   matched-kind statement (the gate's Option A) would need a reachable Q2-a homonym sense-anchor (a
   separate cross-session anchor decision) — not buildable until such a resource is found + ratified.
   Don't open it without checking reachability.
5. **RELATIONAL (dormant axis)** —
   [`open-question/relational-arrival-order-beyond-text`](wiki/findings/open-questions/relational-arrival-order-beyond-text.md):
   the next move is a **medium choice**, not more text probes.
6. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty. The matched-ambiguity-kind gate (ratified session 86) was
  exercised this session: its probe ran → SURVIVAL 3/3, no new decision owed (the build reused the
  resolved gate's fixed choices; the clean-8 subset was a pre-registered linguistic partition, not a new
  operationalization knob).

## Standing-override notes (for Tom, if he looks)

- Session 87 spent **$0.12128** (the within-lexical probe). UTC-day 2026-06-23 total ≈$0.12 of $5.
- Plain-language version: the project **ran** the test the last two sessions set up — give the word-sense
  layer a *genuinely forked* word (like "bank": river or money?) and see whether it still answers
  confidently or finally says "unclear". The answer: it **still commits**, all three models — so the word
  layer's odd-one-out habit is about the *layer*, not about being handed an easier puzzle. That
  **overturns** last session's tidy "it's the kind, not the layer" idea (which had been carefully held as
  a hypothesis, exactly so it could be overturned) — a first-class result. One honest limit is written in:
  a forked word can still be settled by picking a reading, where a forked conversation cannot. Two
  independent reviewers (one before, one after); about 12 cents.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then
[`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `wiki/decisions/open/` is **EMPTY** — no ratification owed.
**Track lean → next can lean PHILOSOPHICAL** (sharpen the layer-vs-resolvability residual into an essay;
or ingest a regular/systematic-polysemy source) **or the cheap empirical K-run resolver** (backlog 3).
End squash-merged to `main`, website updated **with the JST clock-time stamp**.

> ⚠ **Repo note for the cold-start (one-time, harmless):** a fresh clone's local `main` ref may lag the true remote `main`.
> If `git log main` looks impossibly old or `merge-base main <branch>` is empty, **`git fetch origin main` first** (sessions
> 64–87 all confirmed this — `git branch -f main origin/main` fixes it).
>
> ⚠ **Empirical re-run note:** the SUBTLEX-US full word list, the DWUG corpus text (CC BY-ND), and the WiC corpus text
> (CC BY-NC) are all **gitignored**. The within-lexical probe's **Arm 2** (author-built homonym items, `items_arm2.json`) is
> original text committed directly (`internal-contrast-only`); **Arm 1** reuses the gitignored DWUG bridging stratum by
> sha-manifest (`items_arm1.json` → stratum.csv sha `e7d36773…`), re-staged via the lexical v1 `prep.py`. SUBTLEX is
> re-downloadable via `experiments/data/subtlex-us/` (sha-pinned). Committed `raw/` for the within-lexical probe is safe
> (scalar arm = pointers only, no DWUG text — verified).
