# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-24** (sessions s96–s103): **$4.260 spent** (all by s100 — the VWSD
probe; s101, s102, s103 each spent $0). At s103 wind-up (20:45 UTC 2026-06-24) **~$0.74 left for any further 2026-06-24
session.** Full ledger in [`config/budget.md`](config/budget.md). **Check the clock (`date -u`)** — a later session is
almost certainly a new UTC day (full $5 resets). Check for any newer Tom override before spending.

## State

**Session 103 (JST 2026-06-25 / UTC 2026-06-24) — PHILOSOPHICAL distributional-lineage wave. $0, no probe.**
Branch even with `main` at start (s102/#154 merged; no PR to land). `decisions/open/` EMPTY — no ratification owed.
1-wave workflow, 3 parallel subagents (concept-revision + essay + source-ingest) + a fresh read-only adversarial
coherence pass (no blockers; one optional NIT applied).

- **Revised [`concept/distributional-meaning`](wiki/base/concepts/distributional-meaning.md)** — the s102 follow-on. Replaced
  the two "(not in-repo)" parentheticals with real links to the now-in-repo primaries: Harris cited as **primary-read**
  ("difference of meaning correlates with difference of distribution," p. 156), Firth cited as **reliably attributed via
  secondary sources** (never primary-read). Added a **"Historiographic caveat"** paragraph weaving the **Firth↔Harris
  divergence** (Harris form-internal vs Firth situated "context of situation"; secondary-sourced via Brunila & LaViolette
  2022), plus a cross-link to the new essay. Two `depends-on` links added to YAML.
- **Wrote [`essay/two-distributional-hypotheses`](wiki/findings/essays/two-distributional-hypotheses.md)** — the project's
  **23rd essay** (draft). Original **sorting**: "the distributional hypothesis" is two ideas; the next-token/embedding
  objective instantiates the **Harris** (form-internal) reading and **not** the **Firth** (situated) one, so NLP's Firth
  slogan "borrows Firth's words for Harris's idea" and **re-labels, not resolves**, the grounding question. Takes no side
  on Piantadosi–Hill. No new empirical claim; revision trigger armed against the Firth-secondary dependency.
- **Catalogued [`source/fillmore-1982-frame-semantics`](wiki/base/sources/fillmore-1982-frame-semantics.md)** — frame
  semantics (charter-core lexical↔grammatical tie; ancestor of CxG/FrameNet). **Primary UNREACHABLE as OA** (Scribd JS-wall,
  ResearchGate/academia.edu 403, 1976/1985 primaries paywalled). **`status: secondary-only`** (non-standard, like Firth;
  logged): two opening sentences read firsthand via a registration-walled **2006-reprint preview** (pagination from p. 373,
  NOT the 1982 original), the "By the term 'frame'…" definition via metaphorhacker.net (no locator). **No 1982-original page
  number asserted as read.** Honest emptiness held throughout.
- Coherence pass: **0 BLOCKERS** (quote integrity, primary/secondary discipline, anchor discipline, no smuggled empirical
  claim, links/tags all clean); applied its one optional NIT (hedged the essay's "Firth's is situated" sub-head). senselint
  0 errors; linkify clean. Approx subagent token use: ~143k across the 3 generators + ~50k coherence pass.

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

**Track lean — recent: 99 EMPIRICAL-reconcile · 100 EMPIRICAL-RUN ($4.26) · 101 PHIL · 102 PHIL · 103 PHIL.**
**THREE philosophical sessions in a row → next should lean EMPIRICAL if a fresh UTC day gives budget.** In rough priority:

1. **EMPIRICAL — a VWSD v2** (the standing top empirical lever) only behind a fresh `decisions/open/` **DV-refinement**
   decision (non-caption text baseline so "text separability" stops conflating linguistic under-determination with caption
   richness) + larger **stratified** N from the 463 EN gold + **raised claude image-arm `max_tokens`** (s100 lost 6 claude
   image answers to truncation@16). Captioning the full 4090 EN images is ~$7.3 (>cap) → subsample smartly or split across
   days. **Do not quietly re-run** — the DV change is value-laden, so surface it first; ratification is a *later* session's
   job. (Needs a fresh UTC day for budget — at s103 wind-up only ~$0.74 remained on 2026-06-24.)
2. **PHILOSOPHICAL — a constructional essay tying frame semantics to the distributional founders ($0):** now that
   [`source/fillmore-1982-frame-semantics`](wiki/base/sources/fillmore-1982-frame-semantics.md) is in-repo, the natural
   companion to this session's distributional essay is a short essay on Fillmore's "company" as a **structured knowledge
   frame** vs Harris/Firth's **co-occurrence neighbourhood** — i.e. a third reading of "knowing a word by its company."
   Possibly ties to the [`essay/two-distributional-hypotheses`](wiki/findings/essays/two-distributional-hypotheses.md)
   sorting. Small, sound, $0.
3. **PHILOSOPHICAL — another primary OA ingest ($0):** still-wanted charter-core item **Goldberg 1995/2006**
   (constructional, P1 — books, OA-uncertain; try author self-archives / chapter previews). Or, if a later session reaches
   a legitimate full text of **Fillmore 1982/1985**, re-verify the Fillmore source's quotes and consider promoting it from
   `secondary-only`. Mark `unreachable` honestly if so (as Firth/Fillmore were).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty. (40 ratified to date. Full changelog
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)
- **Standing NIT (not a decision):** the `operational` meaning-sense tag (on the five construct-validity source pages)
  is not in [`wiki/meaning-senses.md`](wiki/meaning-senses.md)'s controlled vocabulary; senselint does not enforce vocab
  on `base/` pages, so it is tolerated. Low priority. **Companion:** two source pages now carry a deliberate non-standard
  `status: secondary-only` (Firth s102, Fillmore s103) — primary-unreachable markers, logged, not enforced by senselint.

## Standing-override notes (for Tom, if he looks)

- Session 103 spent **$0** (UTC-day 2026-06-24 total stays $4.260 of $5, all from the s100 picture experiment).
- Plain-language: a reading-and-writing session that built on the last one. It took the two 1950s statements of the idea
  behind today's language models — "you can know a word by the company it keeps" — and showed they are really two different
  ideas: Harris meant the neighbouring *words* (inside language), Firth meant the whole *situation* a word is used in.
  Today's models, trained on text alone, only have Harris's half. A new short essay draws the consequence — quoting Firth's
  famous line as the motto for these models borrows his words for Harris's idea and makes the models sound more grounded
  than they are. The session also made an honest, thin page for a third classic (Fillmore's "frame semantics") whose
  original couldn't be found freely.

## Reminder for the next cold-start

**You are session 104.** The previous slot was **`s103`** (revised the distributional concept page + wrote the
two-distributional-hypotheses essay + catalogued Fillmore 1982 frame-semantics as secondary-only; $0).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5; **check `date -u`** (s103 ran late on UTC 2026-06-24).
**RECONCILE FIRST:** `decisions/open/` is **EMPTY** — no ratification owed.
**Track lean → last THREE were PHIL; lean EMPIRICAL if budget allows.** Top empirical lever: a **VWSD v2** behind a fresh
DV-refinement decision (do **not** quietly re-run). Good $0 phil fallback: a **frame-semantics-vs-distributional essay**
now that Fillmore is in-repo. Composition SATURATED + forced-both CLOSED + graded-sense-image resource STILL WANTED — no
re-grind. End squash-merged to `main`, website updated **with the JST clock-time stamp**.
