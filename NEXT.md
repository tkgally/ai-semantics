# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC-day **2026-06-24** (sessions s96–s100): **$4.260 spent** (all by s100 — the VWSD
probe). **$0.74 left for any later 2026-06-24 session.** Full ledger in [`config/budget.md`](config/budget.md).
**Check the clock (`date -u`)** — a later session is likely a new UTC day (full $5 resets). Check for any newer Tom
override before spending.

## State

**Session 100 (JST 2026-06-24 / UTC 2026-06-24) — EMPIRICAL: the project's FIRST image-native / multimodal RUN. $4.260.**
Branch even with `main` at start (s99/#151 merged; no PR to land). `decisions/open/` EMPTY — no ratification owed.

- **BUILT + RAN the VWSD grounding-headroom probe** under the resolved DV decision
  [`decisions/resolved/vwsd-grounding-headroom-dv`](wiki/decisions/resolved/vwsd-grounding-headroom-dv.md) (Option A /
  interaction-as-test-of-record / Q3 narrow human-anchored / 5 mods). Design frozen
  ([`design/vwsd-grounding-headroom-v1`](experiments/designs/vwsd-grounding-headroom-v1.md)); data **fetched +
  checksummed** (SemEval-2023 VWSD EN gold; images out of git — redistribution unconfirmed); fresh independent
  **pre-run critic GO** + **post-run verifier REPRODUCED**. Run dir `experiments/runs/2026-06-24-vwsd-grounding-headroom-v1/`.
- **Verdict: NEITHER CONFIRMS NOR FALSIFIES** the gating prediction →
  [`result/vwsd-grounding-headroom-v1`](wiki/findings/results/vwsd-grounding-headroom-v1.md). On a frozen 50-item subset
  the **caption-text baseline SATURATED** (per-model .86–.88; 40/50 text-separable; under-determined bin **7 < the
  mod-1 floor 8** → binned interaction **suppressed** per the frozen fallback). The **distraction null is CLEAN**
  (word-ablated gold-selection pooled **.093 ≈ chance**, picks spread across all 10 positions → selection is
  sense-driven, not salience). **Real images gave NO broad lift** over their captions (**gpt WORSE with images, .60 vs
  .86**; claude/gemini ≈ flat); image-rescue in text-failed cells only **4/16 = .25** (too thin to test). A bounded
  reappearance of the redundancy null ([`result/multimodal-grounding-image-v1`](wiki/findings/results/multimodal-grounding-image-v1.md))
  in an image-native *selection* task — **caption-leakage-confounded + underpowered**. Conjecture stays `proposed`;
  prediction-1-as-written remains open for a future **graded-image** resource.

## Why the probe is bounded (read before a v2)

Two co-equal limits, both flagged by the pre-run critic and carried in the result:
1. **Caption-leakage confound.** The text-only baseline shows candidates as gemini-authored captions, which often
   **name the referent** ("a pile of mustard seeds"), so "text-only separability" conflates linguistic
   under-determination with caption richness. The saturation is partly caption-driven. **A clean v2 needs a
   non-caption text baseline** (e.g. ask the model to commit to the sense from word+phrase alone) — but that re-opens
   the DV operationalization, so it would want a fresh `decisions/open/` entry + critic, not a quiet re-run.
2. **Floor not met / underpowered.** N=50, only 7 under-determined items, ~16 text-failed cells. A larger **stratified**
   draw from the 463 EN gold would populate both bins — but captioning the full 4090 EN images is **~$7.3**, over the
   day cap, so a v2 must subsample images smartly or split across days.
3. **Instrument nit:** 6 image parse-fails were all **claude reasoning-then-truncated at `max_tokens=16`** on
   rare-phrasing items — a v2 should raise claude's image-arm `max_tokens` (the text/distract arms were clean).

## ⚠ Do-not-re-grind note (still in force)

- **The composition / order-sensitive-composition / capability-split line is SATURATED — do NOT frame a new probe there.**
  (s99 scoping verdict; 8 instruments cover it.)
- **The forced-both lexical line is CLOSED at R1 pending a NEW resource** (graded in-context "neither sense dominates"
  signal, or an attested forced-both genre balance-unbiased by construction). ([`wanted.md`](wiki/base/wanted.md) P3.)
- Also DONE: function-word build-v2 (s69), lexical-bridging (s77), dative information-structure (s51 CONFIRM 3/3),
  **VWSD grounding-headroom selection probe (s100 — neither confirms nor falsifies)**. A VWSD v2 with a non-caption
  baseline + larger stratified N is the clean follow-up — *not* a re-grind (it tests the gating shape s100 could not),
  but it needs a fresh DV-refinement decision first.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — **no ratification owed.** Apply any Tom override.

**Track lean — recent: 96 PHIL · 97 PHIL-gw · 98 PHIL-gw · 99 EMPIRICAL-reconcile · 100 EMPIRICAL-RUN ($4.26).** The
probe drought is broken; **re-balance toward PHILOSOPHICAL** next. In priority order:

1. **PHILOSOPHICAL / track-feeding (recommended — absorb the s100 result).** Revise the grounding line to record the
   third bounded negative: the s100 run is a **bounded reappearance of the redundancy null** in image-native selection,
   consistent with the conjecture's general posture but not a test of its gating interaction, plus the honest
   caption-confound lesson. Candidate edits: [`theory/lexicon-grammar-continuum`](wiki/findings/theory/lexicon-grammar-continuum.md)'s
   third-axis section (currently records the two prior grounding negatives). Standing ingest candidates:
   Cruse / Murphy / Lyons lexical-semantics monographs (charter-core lexical); Goldberg 1995/2006 (constructional,
   `wanted.md` P1); Cappelen & Dever 2021.
2. **EMPIRICAL — scout the still-wanted graded-sense-image resource.** A graded human *sense-relatedness with
   disambiguating images per usage* set is **STILL WANTED** (THINGS = object-similarity, VWSD = binary — both miss it);
   it is what would let prediction-1-as-written finally run. Scout for one (or conclude none is openly available).
3. **EMPIRICAL — a VWSD v2** only behind a fresh `decisions/open/` DV-refinement (non-caption text baseline) + larger
   stratified N + raised claude `max_tokens`. **Do not quietly re-run** — the DV change is value-laden.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE.** `wiki/decisions/open/` is empty. (40 ratified to date; the VWSD DV gate ratified s99, BUILT+RUN s100. Full
  changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).)
- **Standing NIT (not a decision):** the `operational` meaning-sense tag (on the five construct-validity source pages)
  is not in [`wiki/meaning-senses.md`](wiki/meaning-senses.md)'s controlled vocabulary; senselint does not enforce vocab
  on `base/` pages, so it is tolerated. Low priority.

## Standing-override notes (for Tom, if he looks)

- Session 100 spent **$4.260** (UTC-day 2026-06-24 total, s96–s100 = $4.260 of $5). The first experiment in this project
  to show a model **real pictures**, not just text.
- Plain-language: the picture-and-words experiment finally ran. It asked whether showing a model the candidate pictures
  helps it pick the right meaning of an ambiguous word — specifically where the words alone leave it unsettled. The
  honest answer is **inconclusive either way**: when each picture was first turned into a short written description, the
  models already chose correctly ~87% of the time, so most cases were settled by words and too few "unsettled" ones
  remained to run the intended comparison cleanly (so, per the frozen plan, it wasn't reported). What did hold up: the
  **anti-cheating control was clean** (with the word removed, models picked the right picture only at chance), and the
  **real pictures gave no broad improvement** over the written descriptions — one model did worse with them. An
  independent reviewer signed off before spending and re-derived every number afterwards.

## Reminder for the next cold-start

**You are session 101.** The previous slot was **`s100`** (BUILT+RAN the VWSD grounding-headroom probe → neither
confirms nor falsifies; caption-text saturated, clean distraction null, no broad image lift; $4.260).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60)
then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — a new UTC day resets the full $5.
**RECONCILE FIRST:** `decisions/open/` is **EMPTY** — no ratification owed.
**Track lean → re-balance toward PHILOSOPHICAL** after the s100 empirical run (absorb the result into the grounding
theory page / conjecture), OR scout the still-wanted **graded-sense-image** resource, OR a lexical/constructional
primary ingest. A **VWSD v2** wants a fresh DV-refinement decision first (non-caption text baseline) — do not quietly
re-run. Composition SATURATED + forced-both CLOSED — no re-grind.
End squash-merged to `main`, website updated **with the JST clock-time stamp**.
