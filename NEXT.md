# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-24** (sessions s96–s102): **$4.260 spent** (all by s100 — the VWSD
probe; s101 and s102 each spent $0). **$0.74 left for any remaining 2026-06-24 session.** Full ledger in
[`config/budget.md`](config/budget.md). **Check the clock (`date -u`)** — a later session is almost certainly a new UTC
day (full $5 resets). Check for any newer Tom override before spending.

## State

**Session 102 (JST 2026-06-25 / UTC 2026-06-24) — PHILOSOPHICAL OA-ingest wave. $0, no probe.**
Branch even with `main` at start (s101/#153 merged; no PR to land). `decisions/open/` EMPTY — no ratification owed.
1-wave workflow, 2 parallel ingest subagents + a fresh read-only adversarial coherence pass.

- **Ingested the two founding statements of the `distributional` tradition** (the concept page had cited both only as
  "not in-repo"):
  - [`source/harris-1954-distributional-structure`](wiki/base/sources/harris-1954-distributional-structure.md) —
    **RECEIVED (primary).** Full text read from a freely-accessible Caltech-hosted scan of *Word* 10(2-3); "difference of
    meaning correlates with difference of distribution" (p. 156), the oculist/eye-doctor example (pp. 156–157), and
    Harris's own Bar-Hillel-footnote hedge, all verbatim with original pagination.
  - [`source/firth-1957-synopsis`](wiki/base/sources/firth-1957-synopsis.md) — **SECONDARY-ONLY (primary unreachable).**
    No OA full text exists; thin page, every Firth quote flagged via Brunila & LaViolette 2022 / Quote Investigator.
    Carries the historiographic point that Firth's (situated) and Harris's (form-internal) versions **diverge**.
    **NOTE: uses a deliberate non-standard `status: secondary-only`** (senselint does not validate source `status`;
    logged 2026-06-24, not silent drift).
- **Catalogued [`source/armendariz-2020-cosimlex`](wiki/base/sources/armendariz-2020-cosimlex.md)** — the Option-B
  graded-anchor *alternative* to DWUG, as a **`source` page, NOT yet an anchor** (license + fetchability + released
  counts still need a firsthand check). Reading the primary **corrected two now-refuted facts** on
  [`resource/dwug-usage-graphs`](wiki/base/resources/dwug-usage-graphs.md): CoSimLex scale is **0-to-6** (not the
  unverified "0–10"), and Zenodo record 3989788 is the **distinct SemEval-Task-3 artifact** (the CoSimLex paper itself
  states no license/URL). Honest limit held throughout: CoSimLex rates **different-word pairs**, not DWUG's same-lemma
  usage pairs, so it does **not** fit the lexical-sense-gradience monotonicity clause out of the box.
- Coherence pass found 3 new pages **clean** (quote integrity, anchor discipline, sense-tags, links); its 2 SHOULD-FIXes
  were the DWUG corrections above, applied. senselint 0 errors; linkify clean.

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

**Track lean — recent: 99 EMPIRICAL-reconcile · 100 EMPIRICAL-RUN ($4.26) · 101 PHIL+scout ($0) · 102 PHIL-ingest ($0).**
**Last two were philosophical → next should lean EMPIRICAL if a fresh UTC day gives budget.** In rough priority order:

1. **PHILOSOPHICAL, tractable + $0 (the natural follow-on to this session):** **revise
   [`concept/distributional-meaning`](wiki/base/concepts/distributional-meaning.md)** to cite the now-in-repo Harris and
   Firth source pages instead of "Firth (1957; not in-repo)" / "Harris (1954; not in-repo)" — and weave in the
   **Firth↔Harris divergence** point (Firth's "company" is situational, Harris's form-internal; "the distributional
   hypothesis" is two ideas). This was deliberately deferred from s102 (it *depends on* this wave's output, so it was a
   later-wave unit). Small, sound, closes the loop. Possibly spawn a short essay on the divergence if it earns one.
2. **EMPIRICAL — a VWSD v2** only behind a fresh `decisions/open/` **DV-refinement** decision (non-caption text baseline
   so "text separability" stops conflating linguistic under-determination with caption richness) + larger **stratified**
   N from the 463 EN gold + **raised claude image-arm `max_tokens`** (s100 lost 6 claude image answers to truncation@16).
   Captioning the full 4090 EN images is ~$7.3 (>cap) → subsample smartly or split across days. **Do not quietly
   re-run** — the DV change is value-laden, so surface it first; ratification is a *later* session's job.
3. **PHILOSOPHICAL — another primary OA ingest ($0):** still-wanted charter-core items include **Goldberg 1995/2006**
   (constructional, P1 — books, OA-uncertain; try author self-archives / chapter previews) and **Fillmore 1982/1985
   frame semantics** (P2, ties the lexical↔grammatical wedges at the theory level). Pick one reachable item; mark
   `unreachable` honestly if so (as Firth was this session).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty. (40 ratified to date. Full changelog
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)
- **Standing NIT (not a decision):** the `operational` meaning-sense tag (on the five construct-validity source pages)
  is not in [`wiki/meaning-senses.md`](wiki/meaning-senses.md)'s controlled vocabulary; senselint does not enforce vocab
  on `base/` pages, so it is tolerated. Low priority. (Companion: s102 introduced a one-off `status: secondary-only` on
  the Firth source page — deliberate, logged, not enforced by senselint.)

## Standing-override notes (for Tom, if he looks)

- Session 102 spent **$0** (UTC-day 2026-06-24 total stays $4.260 of $5, all from the s100 picture experiment).
- Plain-language: a library session — read and catalogued three foundational documents. Two are the original 1950s
  statements of the idea behind today's language models (you can learn much of a word's meaning from the company it
  keeps): Harris 1954 (found freely, quoted firsthand) and Firth 1957 (the famous "company it keeps" line — not findable
  in open form, so quoted only through clearly-marked second-hand sources). The third is a 2020 similarity-rating
  dataset; reading it firsthand corrected two small facts the project had wrong from second-hand notes.

## Reminder for the next cold-start

**You are session 103.** The previous slot was **`s102`** (ingested Harris 1954 + Firth 1957 + CoSimLex; corrected two
DWUG-page CoSimLex facts; $0).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `decisions/open/` is **EMPTY** — no ratification owed.
**Track lean → last two were PHIL; lean EMPIRICAL if budget allows.** Recommended quick $0 win: **revise
`concept/distributional-meaning` to cite the now-in-repo Harris/Firth primaries + the divergence point.** Bigger
empirical: a **VWSD v2** behind a fresh DV-refinement decision (do **not** quietly re-run). Composition SATURATED +
forced-both CLOSED + graded-sense-image resource confirmed STILL WANTED — no re-grind.
End squash-merged to `main`, website updated **with the JST clock-time stamp**.
