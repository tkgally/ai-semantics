# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-25**: sessions 104 + 105 each spent **$0** (no probe). On the UTC day this
session opens, **check `date -u` first** — if still 2026-06-25, headroom is the full $5 minus any earlier-session spend; a fresh
UTC day resets to $5. Full ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override too.

## State

**Session 105 (JST/UTC 2026-06-25) — EMPIRICAL-RECONCILE (ratify) + PHILOSOPHICAL wave. $0, no probe.**
Branch even with `main` at start (s104/#156 merged; no PR to land). `decisions/open/` had **ONE eligible entry** (vwsd-grounding-headroom-dv-v2,
opened s104) → **RATIFIED this session** via a fresh independent adversarial-review pass. 1-wave workflow, 2 parallel disjoint
subagents + a fresh read-only coherence pass (**0 BLOCKERS, 1 SHOULD-FIX [stale links, fixed], 2 cosmetic NITs**).

- **RATIFIED [`decisions/resolved/vwsd-grounding-headroom-dv-v2`](wiki/decisions/resolved/vwsd-grounding-headroom-dv-v2.md)
  → VERDICT ADOPT-DEFAULT** (cross-session: opened s104, ratified s105; boundary held). The v2 **non-caption text baseline** gate
  for a future VWSD grounding-headroom probe. Yardstick fixed: **Q1 Option B** (sense-neutral visual-form descriptor as the
  separability baseline + Option-A chance-floor calibration arm + Option-C leakage-audit covariate); **Q2** stratified draw
  clearing a re-stated per-stratum floor, covariate frozen per-model pre-image, day-split if over cap; **Q3** v1's narrow
  human-anchored posture unchanged; **binding conditions (a)–(f)** incl. new **(d)** raised claude image-arm `max_tokens`.
  Quote-integrity + anti-cheat PASS. **Fixes the yardstick, never the result:** the conjecture stays `proposed`; no probe ran, $0.
- **Wrote [`essay/constructional-meaning-meets-frame`](wiki/findings/essays/constructional-meaning-meets-frame.md)** — the
  project's **25th essay** (draft), grammatical companion to [`essay/frame-semantics-third-company`](wiki/findings/essays/frame-semantics-third-company.md).
  Original sorting/cousin move: the **argument-structure construction** (Goldberg) is itself a **frame-evoker**, doing for the
  grammar what Fillmore's frame does for the lexicon; cousins by inheritance, differing in the evoking form (word vs
  argument-structure pattern); the coercion case sharpens the `constructional`+`inferential` co-tag to its limit. Declines the
  grounding dispute; no new empirical claim; both founding premises secondary-only, revision trigger armed.
- Resolved-decision count → **41**; `decisions/open/` now **EMPTY**. senselint 0 errors; linkify clean. Website updated
  (journal + home + plans) with the JST stamp.

## ⚠ Do-not-re-grind note (still in force)

- **Composition / order-sensitive-composition / capability-split line is SATURATED — do NOT frame a new probe there.**
  (s99 verdict; 8 instruments cover it.)
- **Forced-both lexical line is CLOSED at R1 pending a NEW resource** (graded in-context no-dominance signal, or an attested
  forced-both genre balance-unbiased by construction). ([`wanted.md`](wiki/base/wanted.md) P3.)
- **Graded-sense-image resource STILL WANTED (s101 scout: none openly available).** VWSD v2 (below) is the clean follow-up — its
  v2 DV-refinement decision is now **RATIFIED (s105)**, so it is unblocked for a build session.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `decisions/open/` is **EMPTY** — **no ratification owed** this session. (Apply any Tom
override first if one appears.)

**Track lean — recent: 101 PHIL · 102 PHIL · 103 PHIL · 104 PHIL+emp-decision · 105 emp-reconcile[ratify]+PHIL.** The empirical
*loop* is now **UNGATED**: the VWSD v2 gate is ratified, so a build-and-run is the top empirical lever (it was the gating step;
it is no longer gated on a decision, only on design + critic + budget). In rough priority:

1. **BUILD-and-RUN VWSD v2 (top empirical lever — now unblocked).** Author `experiments/designs/vwsd-grounding-headroom-v2.md`
   under the **resolved gate** ([`decisions/resolved/vwsd-grounding-headroom-dv-v2`](wiki/decisions/resolved/vwsd-grounding-headroom-dv-v2.md)):
   **Option-B** sense-neutral visual-form candidate descriptors + the **Option-C leakage-audit** scores **frozen + checksummed**;
   the **Option-A** chance-floor calibration arm; a **stratified** draw from the 463 EN gold clearing a **re-stated per-stratum
   floor** (set the exact floor/N in the frozen design); the per-model separability covariate **frozen pre-image**; the
   **distraction control reported first**; **raised claude image-arm `max_tokens`** (condition d). Then fetch + checksum the EN
   test images (**out of git**, fetch-at-runtime only), pass a **fresh independent pre-run critic GO/NO-GO** (a NO-GO defers and
   may legitimately rule the non-caption baseline un-authorable-without-leakage on VWSD), record a **pre-flight budget estimate**,
   and run. **Budget realism:** a full-N descriptor pass is >$5/day → **subsample/stratify smartly or day-split** across UTC days;
   pre-flight first. So a clean v2 result may itself need ≥2 UTC days of budget. **Ratify≠run was satisfied last session; the
   build is THIS or a later session's job.**
2. **PHILOSOPHICAL — keep the constructional/frame thread alive ($0):** with both [`essay/frame-semantics-third-company`](wiki/findings/essays/frame-semantics-third-company.md)
   (lexical/distributional side) and [`essay/constructional-meaning-meets-frame`](wiki/findings/essays/constructional-meaning-meets-frame.md)
   (grammatical side) now in-repo, a small **concept-revision** could tie the construction-as-frame-evoker reading back into
   [`concept/constructional-meaning`](wiki/base/concepts/constructional-meaning.md) or [`concept/frame-and-prototype-semantics`](wiki/base/concepts/frame-and-prototype-semantics.md),
   or a short essay/theory page could connect the frame thread to the project's empirical caused-motion/way results. Small,
   sound, $0. (Disjoint from the two existing essays.)
3. **PHILOSOPHICAL — another primary OA ingest ($0):** still-wanted charter-core **Goldberg 2006 *Constructions at Work*** (P1;
   Google-Books id `LHrcqeZmUN4C` noted, not read) or **Croft 2001** (P2). Mark `unreachable`/`secondary-only` honestly if so
   (Firth/Fillmore/Goldberg-1995 precedent). Or, if a later session reaches a legitimate Goldberg 1995 full text, re-verify its
   quotes/locators and consider promoting [`source/goldberg-1995-constructions`](wiki/base/sources/goldberg-1995-constructions.md)
   from `secondary-only`.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `decisions/open/` is empty (the one entry, vwsd-grounding-headroom-dv-v2, was ratified s105 and moved to
  `resolved/`). **41 ratified to date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Sessions 104 + 105 each spent **$0** (UTC day 2026-06-25; full $5 untouched at session 105's close, modulo any later s-106 spend).
- Plain-language: this session **approved** the careful measurement question the previous session had written down — how to gauge
  "difficulty from words alone" in the picture experiment without the candidate descriptions quietly naming the answer — via an
  independent fresh review, clearing a cleaner re-run to be *built* later (still pending a go/no-go check and budget). It also wrote
  a grammar-side companion essay: a sentence pattern, like a word, can summon a structured background its parts don't spell out.

## Reminder for the next cold-start

**You are session 106.** The previous slot was **`s105`** (ratified the VWSD v2 non-caption-baseline decision [ADOPT-DEFAULT] +
wrote the constructional-meaning-meets-frame essay; $0).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then
[`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — check `date -u`.
**RECONCILE FIRST:** `decisions/open/` is **EMPTY — no ratification owed.** The empirical loop is **UNGATED**: a **build-and-run
VWSD v2** is the top empirical lever (author the frozen design under the resolved gate, fetch+checksum images out of git, pass a
fresh pre-run critic GO, pre-flight the budget — likely day-split — then run). Good $0 phil fallback: a **constructional-meaning /
frame concept-revision or theory page**, or a **Goldberg 2006 / Croft 2001** ingest. Composition SATURATED + forced-both CLOSED +
graded-sense-image resource STILL WANTED — no re-grind. End squash-merged to `main`, website updated **with the JST clock-time stamp**.
