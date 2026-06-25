# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** New UTC day **2026-06-25**: session 104 spent **$0** (no probe). **Full $5 available.**
Full ledger in [`config/budget.md`](config/budget.md). **Check the clock (`date -u`)** before spending; check for any newer Tom
override too.

## State

**Session 104 (JST/UTC 2026-06-25) — EMPIRICAL-decision + PHILOSOPHICAL wave. $0, no probe.**
New UTC day (full $5 reset); branch even with `main` at start (s103/#155 merged; no PR to land). `decisions/open/` was EMPTY at
start — no ratification owed. 1-wave workflow, 3 parallel disjoint subagents + a fresh read-only adversarial coherence pass
(**0 BLOCKERS, 0 SHOULD-FIX**; 3 non-blocking NITs, all pre-hedged).

- **Opened [`decisions/open/vwsd-grounding-headroom-dv-v2`](wiki/decisions/open/vwsd-grounding-headroom-dv-v2.md)** — the
  empirical-track lead. Surfaces the **value-laden v2 non-caption-baseline gate** for a VWSD grounding-headroom probe. v1 (s100)
  RAN and returned *neither-confirms-nor-falsifies*, primarily because its gemini-authored candidate **captions named the
  referent**, contaminating the per-item text-separability covariate (the caption baseline **saturated**, suppressing the
  gating interaction). Core question: **what non-caption text baseline** makes "separability" measure *linguistic*
  under-determination not caption richness? Provisional defaults — **Q1 Option B** (sense-neutral visual-form descriptor +
  Option-A chance-floor calibration arm + Option-C leakage-audit covariate), **Q2** larger **stratified** draw clearing a
  re-stated per-stratum floor, **Q3** v1's narrow human-anchored posture unchanged; binding pre-spend conditions (a)–(f) incl.
  new **(d) raise claude image-arm `max_tokens`** (v1 lost 6 claude image answers to truncation@16). **status: open, ratifiable
  ONLY by a later session;** anti-cheat note (yardstick, not result; must not be run/re-tuned by the opening session).
- **Wrote [`essay/frame-semantics-third-company`](wiki/findings/essays/frame-semantics-third-company.md)** — the project's
  **24th essay** (draft), explicit **third panel** of [`essay/two-distributional-hypotheses`](wiki/findings/essays/two-distributional-hypotheses.md).
  Original **three-way sorting**: adds **Fillmore's evoked frame** (structured background of relational world-knowledge) as a
  third reading of "knowing a word by its company," distinct from Harris's co-occurrence neighbourhood and Firth's situation. A
  frame is a structure of *inferential* relations, so whether a model "has the frame" is **not** the co-occurrence question the
  objective instantiates but the open Piantadosi–Hill-vs-Bender–Koller question — **declined here**. Payoff = precision: a
  distributional success names the Harris company precisely, is **silent** on the Fillmore frame. Fillmore premise
  secondary-and-preview-sourced, revision trigger armed; no new empirical claim.
- **Catalogued [`source/goldberg-1995-constructions`](wiki/base/sources/goldberg-1995-constructions.md)** — Goldberg 1995
  *Constructions* (charter-core constructional primary; caused-motion/way/coercion lines). **Primary UNREACHABLE as OA**
  (in-print Chicago book; Google-Books preview JS-walled/no body text; Princeton self-archives 403; Sci-Hub not attempted by
  policy). **`status: secondary-only`** (Firth/Fillmore precedent): the construction definition (p. 4) + caused-motion/way
  stimulus locators (pp. 152/163/165/199–218) carried **via fetched named Boas CxG chapters + 1 preprint + 1 excerpt page**
  (p. 1 thesis the weakest link, flagged), every quote flagged "primary NOT consulted." **Not a human anchor.**
- Coherence pass: **0 BLOCKERS / 0 SHOULD-FIX** (every load-bearing quote verified char-for-char vs its in-repo source; v1
  Limitation quotes 1/2/3 verbatim; primary/secondary discipline clean; decision is yardstick-only; essay declines the dispute;
  Goldberg asserts no primary read; links/tags resolve). senselint 0 errors (2 expected WARNs + 41 internal-contrast INFOs);
  linkify clean. Approx subagent tokens: ~58k essay + ~66k decision + ~96k Goldberg + ~114k coherence.

## ⚠ Do-not-re-grind note (still in force)

- **Composition / order-sensitive-composition / capability-split line is SATURATED — do NOT frame a new probe there.**
  (s99 verdict; 8 instruments cover it.)
- **Forced-both lexical line is CLOSED at R1 pending a NEW resource** (graded in-context no-dominance signal, or an attested
  forced-both genre balance-unbiased by construction). ([`wanted.md`](wiki/base/wanted.md) P3.)
- **Graded-sense-image resource STILL WANTED (s101 scout: none openly available).** VWSD v2 (below) is the clean follow-up —
  *not* a re-grind, but it needs the fresh DV-refinement decision RATIFIED first.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` has **ONE entry — [`decisions/open/vwsd-grounding-headroom-dv-v2`](wiki/decisions/open/vwsd-grounding-headroom-dv-v2.md)**,
**opened session 104 → ELIGIBLE for ratification next session** (cross-session boundary will hold). Run the independent
adversarial-review pass: read the decision, its Q1/Q2/Q3 options + provisional defaults + binding conditions and the v1 result
it responds to; return ADOPT-DEFAULT / ADOPT-MODIFIED / KEEP-OPEN with written rationale; the reviewer must be a **fresh agent**,
and ratification fixes the **yardstick, never the result**. Apply Tom override first if any.

**Track lean — recent: 100 EMP-RUN · 101 PHIL · 102 PHIL · 103 PHIL · 104 PHIL+empirical-decision.** The empirical *loop* is
genuinely gated (can't run VWSD v2 until its v2 decision is ratified, which is a later session's job; composition saturated;
forced-both closed). In rough priority:

1. **RATIFY the v2 DV decision** (above) — the gating step. If **ADOPT**, a **build-and-run VWSD v2** becomes the top empirical
   lever, but ratify≠run: a build session must then author `experiments/designs/vwsd-grounding-headroom-v2.md` under the resolved
   gate (Option-B sense-neutral visual-form descriptors + leak-audit frozen+checksummed; stratified draw clearing the floor;
   raised claude `max_tokens`), fetch+checksum images out of git, pass a **fresh pre-run critic GO**, then run. Budget: a full-N
   descriptor pass is >$5/day → **subsample/stratify smartly or day-split** (a fresh UTC day's $5; pre-flight first). So a clean
   VWSD v2 result is **≥2 sessions out** (ratify this session, build+run a later one).
2. **PHILOSOPHICAL — keep the distributional/constructional thread alive ($0):** the two-essay arc (Harris/Firth two-ideas +
   Fillmore third-company) plus the now-in-repo [`source/goldberg-1995-constructions`](wiki/base/sources/goldberg-1995-constructions.md)
   invites a short essay or concept-revision tying **Goldberg's constructional meaning** (the construction itself carries
   inferential content) to the **frame** thread — i.e. how an argument-structure construction *evokes* a scene the verb alone
   doesn't, a constructional cousin of Fillmore's frame. Small, sound, $0. (Disjoint from the existing essays.)
3. **PHILOSOPHICAL — another primary OA ingest ($0):** still-wanted charter-core **Goldberg 2006 *Constructions at Work***
   (P1; Google-Books id `LHrcqeZmUN4C` noted, not read) or **Croft 2001** (P2). Mark `unreachable`/`secondary-only` honestly if
   so (Firth/Fillmore/Goldberg-1995 precedent). Or, if a later session reaches a legitimate Goldberg 1995 full text, re-verify
   its quotes/locators and consider promoting from `secondary-only`.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **ONE OPEN:** [`decisions/open/vwsd-grounding-headroom-dv-v2`](wiki/decisions/open/vwsd-grounding-headroom-dv-v2.md) —
  *opened session 104 (2026-06-25); NOT yet eligible (opened this session); **eligible for ratification next session.***
  (40 ratified to date. Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)
- **Standing NIT (not a decision):** the `operational` meaning-sense tag (on the construct-validity source pages) is not in
  [`wiki/meaning-senses.md`](wiki/meaning-senses.md)'s controlled vocabulary; senselint does not enforce vocab on `base/` pages,
  so it is tolerated. **Companion:** three source pages now carry a deliberate non-standard `status: secondary-only` (Firth s102,
  Fillmore s103, Goldberg-1995 s104) — primary-unreachable markers, logged, not enforced by senselint.

## Standing-override notes (for Tom, if he looks)

- Session 104 spent **$0** (new UTC day 2026-06-25; full $5 untouched).
- Plain-language: a planning-and-writing session. Before re-running the picture-and-words experiment, it wrote down a hard
  measurement question — the last run's "words alone" baseline described each candidate picture with a caption that often *named*
  the thing, giving the answer away, so "difficulty from words" was contaminated — and proposed a cleaner fix, to be approved by
  a *later* session before any spending. It also added a third sense of "knowing a word by the company it keeps" (Fillmore's
  structured-knowledge *frame*, alongside last sessions' Harris-words and Firth-situation), and made an honest, thin page for
  Goldberg's 1995 *Constructions* whose original couldn't be found freely.

## Reminder for the next cold-start

**You are session 105.** The previous slot was **`s104`** (opened the VWSD v2 non-caption-baseline decision + wrote the
frame-semantics-third-company essay + catalogued Goldberg 1995 as secondary-only; $0).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then
[`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — check `date -u`.
**RECONCILE FIRST:** `decisions/open/` has **ONE entry (vwsd-grounding-headroom-dv-v2, opened s104) — ELIGIBLE next session.**
Ratify it via a fresh adversarial-review pass (ADOPT / ADOPT-MODIFIED / KEEP-OPEN, written rationale). If ADOPT, a build-and-run
VWSD v2 is the top empirical lever but is **≥1 further session out** (ratify≠run; needs design + pre-run critic + a fresh-day
budget). Good $0 phil fallback: a **Goldberg-construction-meets-frame essay** now that Goldberg 1995 is in-repo, or a
**Goldberg 2006 / Croft 2001** ingest. Composition SATURATED + forced-both CLOSED + graded-sense-image resource STILL WANTED —
no re-grind. End squash-merged to `main`, website updated **with the JST clock-time stamp**.
