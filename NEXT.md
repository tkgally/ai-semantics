# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-24** (sessions s96 + s97 + s98 + s99): **$0** spent (all reading/writing,
no probe). Full $5 still available for any later 2026-06-24 session. Full ledger in [`config/budget.md`](config/budget.md).
**Check the clock (`date -u`)** — a later session is likely a new UTC day (full $5 resets). Check for any newer Tom
override before spending. **Next session is expected to SPEND** (the VWSD probe — see below); pre-flight-estimate it,
and watch the image/reasoning-token cost driver (gemini image tokens; keep images small / `effort:minimal`).

## State

**Session 99 (JST 2026-06-24 / UTC 2026-06-24) — EMPIRICAL-leaning RECONCILIATION + groundwork, $0 (no probe).** Branch
even with `main` at start (s98/#150 merged; no PR to land). `decisions/open/` had ONE eligible entry (the VWSD DV gate,
opened s98); it was **RATIFIED this session** and is now empty.

- **RECONCILE (PROTOCOL §2) — RATIFIED the VWSD DV decision** (cross-session: opened s98, ratified s99; boundary held).
  An independent fresh-agent adversarial review returned **ADOPT MODIFIED**: **Q1 Option A** (image-conditioned
  selection accuracy vs a text-only baseline), **Q2 the interaction** (per-item text-only separability × image-induced
  selection improvement, predicted **negative**) **as the sole test of record**, **Q3 narrow human-anchored posture**
  (tests the gating *shape*, NOT prediction-1-as-written, NOT reference) — with **5 tightening modifications** (numeric
  stratification floor; text-only baseline frozen to a checksummed file before any image condition; distraction-null
  reported first; mandatory power/coarseness caveat; conjecture scope note). Anti-cheat PASS. Moved to
  [`decisions/resolved/vwsd-grounding-headroom-dv`](wiki/decisions/resolved/vwsd-grounding-headroom-dv.md); resolved-index +
  conjecture scope note applied. **The VWSD probe is now BUILDABLE** (the design is cleared to author; the *result* is
  still gated on a fresh pre-run critic GO — a NO-GO defers).
- **EMPIRICAL groundwork — scouted THINGS-data** as the candidate **graded** image resource the ratification reserved
  for prediction-1-as-written → [`resource/things-data-triplets`](wiki/base/resources/things-data-triplets.md) (`status:
  scouted`). **Verdict: DOES NOT CLEANLY FIT** — 4.70M human odd-one-out judgments give graded *whole-object similarity*,
  a different construct from the conjecture's graded *within-word sense relatedness with disambiguating images* (no
  same-word/different-sense pairs, no polysemy structure). Right shape (graded+image+human+multi-rater), wrong axis. Could
  anchor a distinct representational-alignment question; NOT a drop-in for DWUG's graded sense anchor. License caveat:
  behavioral CC0 reported-but-not-primary-verified (OSF node_license=null; Figshare+ 403); base images restricted.
- **EMPIRICAL probe scoping (no probe run) — the composition line is SATURATED.** An independent scoping agent confirmed
  the order-sensitive-composition / capability-split line is at a well-earned terminus: 8 instruments already cover it
  (base, K=4, K=6, alt-pair, figure-to-figure, three-move, reasoning-scaffold, worked-example); every plausible new
  angle is done, re-grinding, a suspended-on-cost build (cross-family dyads), or out-of-scope (non-relational domain).
  **Do NOT frame a "new" composition probe — it would be padding.** (This is why s99 ran no probe: the only
  run-a-probe-now option was a composition re-grind, correctly declined.)

Adversarial coherence pass (fresh read-only agent): **NO BLOCKERS**; 2 SHOULD-FIX — (1) NEXT.md old `decisions/open/`
links (self-resolved by this handoff rewrite → resolved path); (2) conjecture `updated:` bumped 2026-05-31→2026-06-24.
2 NITs noted, not actioned (a provenance-table locator mixing quote+verdict; the `human-comparison` tag on a
does-not-anchor-*this*-conjecture resource — both defensible). senselint 0 errors; linkify clean. Website (journal +
home + latest card) updated, JST stamp **June 24, 2026, 14:28 JST**.

## ⚠ Do-not-re-grind note (still in force — expanded this session)

- **The composition / order-sensitive-composition / capability-split line is SATURATED — do NOT frame a new probe there.**
  (s99 scoping verdict; 8 instruments cover it.) The capability-split essay's trigger (c) "cross-task pattern" stays
  live but needs *distinct* probes on *other* lines, not another composition rendering.
- **The forced-both lexical line is CLOSED at R1 pending a NEW resource.** Twice NO-GO'd (s91, s94). Runnable only with a
  per-item, in-context, *graded* "neither sense dominates in *this* sentence" signal (sentence-grain, graded), or an
  attested forced-both genre balance-unbiased by construction. ([`wanted.md`](wiki/base/wanted.md) P3.)
- Also DONE: function-word build-v2 (s69), lexical-bridging (s77), dative information-structure (tested s51, CONFIRM 3/3).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — **no ratification owed.** Apply any Tom override.

**Track lean — recent: 95 PHIL · 96 PHIL · 97 PHIL-groundwork · 98 PHIL-groundwork · 99 EMPIRICAL-reconciliation ($0).**
**FIVE sessions without a model query.** But the gate is now lifted: **the next session SHOULD BUILD + RUN the VWSD
grounding-headroom probe** — a clean, human-anchored, spend-bearing probe, ratify≠run cleared (s99 ratified; s100 may
run). In priority order:

1. **EMPIRICAL (spend-bearing) — BUILD + RUN the VWSD grounding-headroom probe** per the resolved decision
   [`decisions/resolved/vwsd-grounding-headroom-dv`](wiki/decisions/resolved/vwsd-grounding-headroom-dv.md) (Option A,
   interaction-as-test-of-record, 5 mods). Steps:
   1. **Author `experiments/designs/vwsd-grounding-headroom-v1.md`** (the frozen prereg): DV = the per-item
      *text-only separability × image-induced selection-improvement* interaction, predicted negative; the **numeric
      stratification floor** (≥ a stated min items per under-determined/saturated stratum, distribution reported); the
      **distraction control** (same-referent / surface-dissimilarity) reported FIRST; the **power/coarseness caveat**
      (a flat interaction = "no detectable gating OR underpowered"). Anchor only to the **gold EN test (463) + trial
      (16)** — training is silver.
   2. **Fetch** the **572 MB resized EN test images + gold EN queries** (Drive/OneDrive, no registration), **checksum**,
      **keep images OUT of git** (redistribution UNCONFIRMED — fetch-at-runtime only, no re-host). CC-BY-NC = non-commercial
      research OK.
   3. **Compute + FREEZE** the per-model, per-item **text-only separability** covariate to a **checksummed file BEFORE
      any image condition runs** (mod 2 — no retuning; mechanically auditable).
   4. **Pre-flight budget estimate** (image-input + the gemini image/reasoning-token driver — keep images small,
      `effort:minimal`; this could be the priciest run in a while — split/scale if >\$2.50/run or if it would take the
      UTC day over \$5). **Pass a fresh independent pre-run critic GO/NO-GO** against the frozen design (mod 1: strata
      non-degenerate; no surface-dissimilarity-only reader beats the interaction). **NO-GO defers, never relaxes.**
   5. **Run** (image-conditioned + text-only + distraction-control arms), score the interaction, **report the distraction
      null first**, carry the power caveat, independent post-run verifier. Write `result/vwsd-grounding-headroom-v1`
      with the Q3 narrow `human-comparison` scope (gating shape, NOT prediction-1-as-written) + all four VWSD resource
      caveats (binary gold; limited annotator independence; image-redist unconfirmed; silver training).
   - **If the build snags** (images unfetchable in-env, or pre-run critic NO-GO): record the honest build-attempt
     outcome ($0 or minimal), and fall to item 2 or 3.
2. **PHILOSOPHICAL / track-feeding fallback** (if the VWSD build can't complete cleanly). The grounding line's
   "**future graded-image resource**" (graded human *sense-relatedness with disambiguating images per usage*) is **STILL
   WANTED** — THINGS (object-similarity) and VWSD (binary) both miss it; scout for one (or conclude none is openly
   available). Other standing candidates: Cruse / Murphy / Lyons lexical-semantics monographs (charter-core lexical);
   Goldberg 1995/2006 (constructional, `wanted.md` P1); Cappelen & Dever 2021.
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty. (40 ratified to date — the VWSD DV gate ratified s99; full changelog
  [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)
- **Standing NIT (not a decision):** the `operational` meaning-sense tag (on the five construct-validity source pages)
  is not in [`wiki/meaning-senses.md`](wiki/meaning-senses.md)'s controlled vocabulary; senselint does not enforce vocab
  on `base/` pages, so it is tolerated. Low priority.

## Standing-override notes (for Tom, if he looks)

- Session 99 spent **$0** (a reconciliation + groundwork session). UTC-day 2026-06-24 total (s96–s99) = **$0 of $5**.
- Plain-language: this session **approved** the measurement plan for the planned picture-and-words experiment (an
  independent reviewer signed off, with five conditions that make a misleading result harder to get), so a future
  session can now build and run it. It also checked whether a big public dataset (4.7M human "odd one out" judgments)
  could supply the finer similarity score the plan gives up, and found it **doesn't fit** (it rates how alike whole
  objects look, not how related two senses of a word are) — recorded so a later session won't reach for it by mistake.
  An independent check re-verified the write-ups. No models were queried. **Five sessions running have queried no
  model** — because the clean probes were gated (approvals/data), not for lack of will; this session lifted the main
  gate, and the next session is set up to actually run the picture experiment.

## Reminder for the next cold-start

**You are session 100.** The previous slot was **`s99`** (ratified the VWSD DV decision + scouted THINGS-data
[does-not-fit] + confirmed the composition line saturated, $0).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5. **Expect to SPEND** (the VWSD probe).
**RECONCILE FIRST:** `decisions/open/` is **EMPTY** — no ratification owed.
**Track lean → FIVE non-probe sessions (s95–s99); the gate is now lifted — the next move SHOULD BUILD + RUN the VWSD
grounding-headroom probe** (Option A per the resolved DV decision; author the frozen design, fetch+checksum the 572 MB
EN test [images out of git], freeze the text-only separability covariate to a checksummed file, pre-flight the
image-token cost, pass a fresh pre-run critic GO, run, verify). Fallback: scout the still-wanted graded-sense-image
resource, or a lexical/constructional primary ingest. Composition is SATURATED and forced-both CLOSED — do not re-grind.
End squash-merged to `main`, website updated **with the JST clock-time stamp**.
