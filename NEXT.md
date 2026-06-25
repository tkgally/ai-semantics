# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-25**: sessions 104–108 spent **$4.72482** (all of it session 107, the VWSD v2 day-1 text-only build);
**sessions 108 and 109 each spent $0.** **If a session still opens on UTC 2026-06-25, only ≈$0.275 headroom remains — do NOT run any image arm today.** A fresh
UTC day resets to $5. **Check `date -u` first.** The IMAGE and DISTRACT arms (≈$6.9 each) must each be day-split across fresh UTC days regardless. Full ledger
in [`config/budget.md`](config/budget.md). Check for any newer Tom override too.

## State

**Session 109 (UTC 2026-06-25) — workflow, 2 waves + fresh adversarial coherence pass, $0.** Branch even with `main` at start (s108/#161 merged).
`decisions/open/` **EMPTY** → no ratification owed; no Tom override. A **philosophical-track** session (the empirical lever was budget-blocked — no fresh UTC day).
Three units landed:

1. **Croft 2001 ingested (wanted.md P2 discharged).** [`source/croft-2001-radical-construction-grammar`](wiki/base/sources/croft-2001-radical-construction-grammar.md)
   — the typological, non-reductionist wing of CxG (constructions as primitive units; categories construction-derived, distribution-defined, language-specific;
   internal structure = part–whole only). 2001 OUP book body **unreachable as OA** (OUP catalogue metadata-only; Google-Books JS-walled/blurb; archive.org has
   **no scan at all**) — quotes carried via **Croft's own self-archived author manuscript** (`Elsevier-RadicalCxG.pdf`, UNM page), author-primary, `status:
   secondary-only`, **NOT a human anchor**. Croft's book-page locators reported but unverified against the book.
2. **New theory page** [`theory/statistical-preemption-and-constructional-productivity`](wiki/findings/theory/statistical-preemption-and-constructional-productivity.md)
   — maps Goldberg-2006's two usage-based learning levers onto the existing constructional apparatus: **productivity** ↔ the held-out-item generalization test
   (Tier-3 + the way/caused-motion confirm bars); **preemption** ↔ a blocking signature the project has only **preconditions** for (coercion cancellability +
   form-keying), never an isolated test. That asymmetry is the finding. **Sharp bound:** Goldberg 2006 is a human-learning theory, **NOT a human anchor**;
   a behavioral match cannot separate meaning-conditioned preemption from a frequency confound. **No new empirical claim.** `refines` the main theory page.
3. **Essay enrichment:** [`essay/constructional-meaning-meets-frame`](wiki/findings/essays/constructional-meaning-meets-frame.md) gained a "usage-based 2006
   dimension" section + `depends-on source/goldberg-2006` + a cross-link to the new theory page. Explicitly an **enrichment, not a trigger discharge** (the
   essay's revision triggers concern the unread Goldberg 1995 / Fillmore 1982 primaries); the cousins-by-inheritance sorting is unchanged.

**Coherence pass (fresh read-only agent) caught + fixed before commit:** a **stitched Goldberg quote** on the theory page (now verbatim), two paraphrases
mis-marked as quotes (quotation marks removed), and the missing index entries. Worth remembering: even a $0 phil wave can ship a fabricated-by-stitching quote
— the adversarial pass earned its keep.

## ⚠ VWSD v2 — the empirical lever, still gated on a FRESH UTC day (UNCHANGED from s108)

The VWSD v2 day-1 build is **DONE, FROZEN, and critic-certified (GO-WITH-CONDITIONS)**. The result `result/vwsd-grounding-headroom-v2` still **does NOT exist
and is NOT cleared**. The spend-bearing IMAGE then DISTRACT arms require a **fresh UTC day**. Committed-file checksums: `frozen/descriptors.json` **`26616a55…`**
(NOT the `afe74f82…` descriptor-only pre-leak sha — see s108 correction), `frozen/run_items.json` `7f9e52fa…`, `raw/text.json` `3a9dfcbf…`.

### The THREE binding conditions the execution session MUST honor (from the s108 certification)

1. **Gemini Option-A floor elevation is a first-class caveat.** Gemini's floor is `.158` Wilson[.104,.234] (lower bound > chance .10). Any gemini-specific
   image-rescue / gating claim must (a) be read against gemini's own ≈`.158` floor, not bare `.10`; (b) carry the elevation as a foregrounded caveat on the
   result page; (c) be reported alongside the pooled (`.122`) and per-model reads (claude `.092` clean / gpt `.117` near-clean carry primary weight).
2. **Foreground the 0-intermediate-band gap.** The frozen draw has `sep_i ∈ {0, 1/3, 1}` only — **no 2/3 band**. The gating shape is read across a **bimodal**
   separability distribution; the **binned image-rescue contrast** (text-failed vs text-succeeded) is the test of record, **not** a graded `sep→rescue` slope;
   the continuous Spearman/OLS companion is doubly weakened (mechanical ceiling + 2/3 gap) and stays descriptive-only.
3. **DISTRACT null reported and credited FIRST.** No IMAGE-arm lift counts as grounding headroom unless it survives the word-ablated DISTRACT control
   (gold-selection vs chance `.10`, per-model and pooled), reported **before** the gating interaction (design condition c).

Plus the standing obligations: **re-measure claude's raised-`max_tokens=512` IMAGE per-call cost** in a small preflight (condition d — not the stale ~3×
placeholder); **day-split** under the $5 cap, each sub-batch under the $2.50 prudence flag (condition f); **images out of git**; **do NOT re-derive** the frozen
day-1 artifacts (descriptors / leak_i / run_items / text covariate); carry all four VWSD resource caveats verbatim-in-force; keep `leak_i` a **reported
covariate, never regressed out** (design B.4).

## ⚠ Do-not-re-grind note (still in force)

- **Composition / order-sensitive-composition / capability-split line is SATURATED — do NOT frame a new probe there.** (s99 verdict.)
- **Forced-both lexical line is CLOSED at R1 pending a NEW resource** ([`wanted.md`](wiki/base/wanted.md) P3).
- **VWSD v2 day-1 is DONE, FROZEN, critic-certified** — do **not** re-generate descriptors / re-draw the N=120 / re-run any day-1 arm.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `decisions/open/` is **EMPTY — no ratification owed.** (Apply any Tom override first if one appears.) The s108 GO is a
**pre-run-critic gate**, not a `decisions/open/` entry — honor the three binding conditions above; it needs no further ratification.

**Track lean — recent: 105 emp-reconcile+PHIL · 106 emp-design+PHIL · 107 emp-RUN(day-1) · 108 emp-GATE+PHIL · 109 PHIL(2 units).** The last session was
**pure philosophical**; the empirical loop is mid-run, gate cleared, blocked only on a fresh budget day. **Strongly weight empirical next IF a fresh UTC day
allows the image arm.** In rough priority:

1. **IF a FRESH UTC day (NOT 2026-06-25) — the IMAGE arm, day-split.** Re-measure claude raised-`max_tokens=512` per-call cost first (condition d, small
   preflight), then build the image arm by adding an `image-full` mode to `run.py` (claude `max_tokens=512`; gpt/gemini generous; low detail), reading images
   from `$VWSD_IMAGES`. Re-fetch the 572 MB zip (Drive id `15ed8TXY9Pzk68_SCooFm7AfkeFtCd16Q`, sha `b9f2f1e1…af8f`) + extract to `$VWSD_IMAGES`; **keep out of
   git**. IMAGE ≈$6.9 → split ~2 UTC days (~45–60 items/day, each sub-batch under the $2.50 flag). Then the **DISTRACT arm** (≈$6.9, ~2 days) — its **null
   reported FIRST**. Then write [`result/vwsd-grounding-headroom-v2`] honoring **all three binding conditions** + a fresh independent **post-run verifier**; the
   conjecture [`distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md) stays `proposed` until
   it lands. `analyze.py` already computes the full result sections once `raw/image.json` + `raw/distract.json` exist.
2. **PHILOSOPHICAL fallback ($0), if still budget-blocked or leaning phil:** a primary OA ingest from [`wanted.md`](wiki/base/wanted.md) (e.g. **Putnam 1975**
   "The Meaning of 'Meaning'" P2; **Wittgenstein 1953** P2; **Cruse 1986 / Murphy 2003** lexical-semantics P2) — mark `unreachable`/`secondary-only` honestly if
   unreachable. **Note:** the constructional-source backlog is now well-covered (Goldberg 1995 + 2006 + Croft 2001 all in, all secondary-only); fresh phil work
   may be better spent on the **philosophy-of-meaning** primaries or a theory/essay synthesis than on more CxG ingests. A short theory/essay unit connecting
   existing sourced material is also fine. **Avoid** re-grinding the constructional empirical lines (do-not-re-grind note above).
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `decisions/open/` is empty. **41 ratified to date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Session 109 spent **$0** (UTC day 2026-06-25). A library + synthesis session: no models queried.
- Plain-language: shelved a second founding grammar book (Croft 2001) honestly — book unreachable, author's own summary catalogued and clearly flagged — and
  wrote a synthesis taking a theory of *how people learn grammar* and asking, with no new claim about any model, which existing experiments would and would not
  count as evidence under it. The load-bearing caution is written in: it is a human-learning theory, **not** a yardstick to grade a model against; ordinary
  word-frequency statistics could mimic the same behaviour. An independent skeptic checked both pieces and caught a quote that had been mis-stitched (fixed to
  verbatim) before anything was kept.

## Reminder for the next cold-start

**You are session 110.** The previous slot was **`s109`** (philosophical: Croft 2001 ingest + statistical-preemption theory page + essay enrichment; **$0**).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — check `date -u` (if still 2026-06-25, ≈$0.275 left, NO image arm today; a fresh day resets to $5).
**RECONCILE FIRST:** `decisions/open/` is **EMPTY — no ratification owed.** The VWSD v2 gate is **CLEARED (GO-WITH-CONDITIONS)**: on a **fresh UTC day**, the
lever is the **day-split IMAGE then DISTRACT arms** — re-measure claude's raised-`max_tokens` cost first (d); honor the **three binding conditions** (gemini
floor caveat; bimodal 0-intermediate-band gap; DISTRACT null FIRST); fresh post-run verifier. The last session was pure phil — **weight empirical next if the
budget day allows**. $0 phil fallback: a philosophy-of-meaning primary ingest (Putnam/Wittgenstein/Cruse/Murphy) or a theory/essay synthesis — the
constructional ingests are now well-covered. Use committed checksum `26616a55…` for `frozen/descriptors.json`. Composition SATURATED + forced-both CLOSED — no
re-grind; do NOT re-derive the frozen day-1 artifacts. End squash-merged to `main`, website updated **with the JST clock-time stamp**.
