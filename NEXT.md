# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-24** (sessions s96–s101): **$4.260 spent** (all by s100 — the VWSD
probe; s101 spent $0). **$0.74 left for any later 2026-06-24 session.** Full ledger in [`config/budget.md`](config/budget.md).
**Check the clock (`date -u`)** — a later session is likely a new UTC day (full $5 resets). Check for any newer Tom
override before spending.

## State

**Session 101 (JST 2026-06-24 / UTC 2026-06-24) — PHILOSOPHICAL track-feed + EMPIRICAL scout. $0, no probe.**
Branch even with `main` at start (s100/#152 merged; no PR to land). `decisions/open/` EMPTY — no ratification owed.
1-wave workflow, 2 parallel subagents + fresh read-only adversarial coherence pass.

- **Absorbed the s100 VWSD result into the grounding theory + conjecture.** Both
  [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md) (third-axis section +
  status-hook) and [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
  (top status + "The proposal" lead) had framed the grounding axis as **"two negatives"**; now framed as **two bounded
  clear-homonym negatives PLUS one inconclusive image-native VWSD run** ([`result/vwsd-grounding-headroom-v1`](wiki/findings/results/vwsd-grounding-headroom-v1.md))
  that **neither confirms nor falsifies** the gating prediction — held the "not a clean third null" line throughout.
  Coherence pass re-verified every s100 number vs the result page (all match), all links resolve; 1 BLOCKER + 1
  SHOULD-FIX found and applied.
- **Scouted the still-wanted graded-sense-image resource → NONE FOUND** (open channels, 2026-06-24). The field
  bifurcates: graded sense-relatedness sets (DURel/CoSimLex/Usim/GWSC/SCWS) are **text-only**; image-paired word-sense
  sets (VWSD, PolCLIP) use **binary/selection** gold. Strongest near-miss = **AdMIRe (SemEval-2025 Task 1, arXiv
  2503.15358; CC BY 4.0 reported, NOT primary-verified)** — graded ordinal *image-ranking* of literal-vs-idiomatic
  compound interpretation per usage, **wrong axis**. Recorded in [`wanted.md`](wiki/base/wanted.md) (Multimodal/grounded
  section): the want **STAYS OPEN**.

## ⚠ Do-not-re-grind note (still in force)

- **The composition / order-sensitive-composition / capability-split line is SATURATED — do NOT frame a new probe there.**
  (s99 scoping verdict; 8 instruments cover it.)
- **The forced-both lexical line is CLOSED at R1 pending a NEW resource** (graded in-context "neither sense dominates"
  signal, or an attested forced-both genre balance-unbiased by construction). ([`wanted.md`](wiki/base/wanted.md) P3.)
- **The graded-sense-image resource is confirmed STILL WANTED (s101 scout: none openly available).** A VWSD v2 with a
  non-caption baseline + larger stratified N is the clean empirical follow-up — *not* a re-grind, but it needs a fresh
  DV-refinement decision first.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — **no ratification owed.** Apply any Tom override.

**Track lean — recent: 97 PHIL-gw · 98 PHIL-gw · 99 EMPIRICAL-reconcile · 100 EMPIRICAL-RUN ($4.26) · 101 PHIL+scout ($0).**
Balanced; next can lean either. In rough priority order:

1. **PHILOSOPHICAL — a primary open-access ingest (recommended; $0).** Several charter-core lexical/constructional
   primaries are still `wanted` and plausibly OA-reachable: **CoSimLex (SemEval-2020 Task 3, arXiv 1912.05320)** — a
   graded in-context word-similarity *paper* (text-only; the alternative graded anchor to DWUG, [`wanted.md`](wiki/base/wanted.md) P2);
   **Goldberg 1995/2006** (constructional, P1 — books, OA-uncertain, try author self-archives / chapter previews);
   **Fillmore 1982/1985 frame semantics** (P2, ties the lexical↔grammatical wedges at the level of semantic theory).
   Pick one reachable item, ingest with verbatim quotes + locators (no fabrication; mark `unreachable` honestly if so).
2. **EMPIRICAL — a VWSD v2** only behind a fresh `decisions/open/` **DV-refinement** (non-caption text baseline so
   "text separability" stops conflating linguistic under-determination with caption richness) + larger **stratified** N
   from the 463 EN gold + **raised claude image-arm `max_tokens`** (s100 lost 6 claude image answers to truncation@16).
   Captioning the full 4090 EN images is ~$7.3 (>cap) → subsample smartly or split across days. **Do not quietly
   re-run** — the DV change is value-laden, so surface it first; ratification is a *later* session's job.
3. **PHILOSOPHICAL — develop/revise an essay** if an ingest or the s100 result spawns a revision trigger (the grounding
   line now carries the third, inconclusive outcome — check whether any essay leans on the old "two negatives" framing).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty. (40 ratified to date; the VWSD DV gate ratified s99, BUILT+RUN s100,
  absorbed into theory s101. Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)
- **Standing NIT (not a decision):** the `operational` meaning-sense tag (on the five construct-validity source pages)
  is not in [`wiki/meaning-senses.md`](wiki/meaning-senses.md)'s controlled vocabulary; senselint does not enforce vocab
  on `base/` pages, so it is tolerated. Low priority.

## Standing-override notes (for Tom, if he looks)

- Session 101 spent **$0** (UTC-day 2026-06-24 total stays $4.260 of $5, all from the s100 picture experiment).
- Plain-language: a writing-and-bookkeeping session. Last session's picture-and-words experiment was written into the
  project's theory **as an honest "inconclusive" — not a third negative**: it neither confirmed nor disproved the idea,
  because the words alone already settled most cases. And a search confirmed that the one kind of dataset that *could*
  settle the question cleanly — sliding-scale human ratings of how related two *uses* of a word are, each paired with a
  picture — does not yet appear to exist in open form, so the gap is real and recorded.

## Reminder for the next cold-start

**You are session 102.** The previous slot was **`s101`** (absorbed the s100 VWSD result into the grounding theory +
conjecture as a *third, inconclusive* outcome; scouted the graded-sense-image resource → NONE FOUND; $0).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `decisions/open/` is **EMPTY** — no ratification owed.
**Track lean balanced → either track is fair game.** Recommended: a **primary OA ingest** (CoSimLex paper / Goldberg /
Fillmore — $0), OR a **VWSD v2** behind a fresh DV-refinement decision (non-caption baseline + larger stratified N +
raised claude `max_tokens`) — do **not** quietly re-run. Composition SATURATED + forced-both CLOSED + graded-sense-image
resource confirmed STILL WANTED — no re-grind.
End squash-merged to `main`, website updated **with the JST clock-time stamp**.
