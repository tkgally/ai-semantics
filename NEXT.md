# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-25**: sessions 104–107 + **108** combined spent **$4.72482** (all of it session 107, the VWSD v2
day-1 text-only build; **session 108 spent $0**). **If this session still opens on UTC 2026-06-25, only ≈$0.275 headroom remains — do NOT run any image
arm today.** A fresh UTC day resets to $5. **Check `date -u` first.** The IMAGE and DISTRACT arms (≈$6.9 each) must each be day-split across fresh UTC
days regardless. Full ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override too.

## State

**Session 108 (UTC 2026-06-25) — workflow, 1 wave (critic gate + 1 phil ingest), $0.** Branch even with `main` at start (s107/#160 merged).
`decisions/open/` **EMPTY** → no ratification owed; no Tom override. Two units landed:

1. **THE GATE IS CLEARED (conditionally).** A **fresh independent pre-run critic** (condition e) certified the frozen VWSD v2 day-1 build against the
   observed `sep_i`/`leak_i` distributions and returned **GO-WITH-CONDITIONS**. Certification committed at
   [`experiments/runs/2026-06-25-vwsd-grounding-headroom-v2/pre-run-critic-certification.md`](experiments/runs/2026-06-25-vwsd-grounding-headroom-v2/pre-run-critic-certification.md).
   The critic re-ran `analyze.py` offline (every day-1 number reproduced exactly), proved the `descriptors.json` sha discrepancy is a **stale pre-leak
   snapshot, not tampering** (it reconstructed the descriptor-only object and hashed it to **exactly `afe74f82…`**, confirming the 1889 descriptor phrases
   are byte-identical and the freeze is genuinely pre-image), inspected the descriptors by hand (v1's "mustard seeds" leak genuinely fixed → "mixed spices",
   scored no-leak), and ruled gemini's marginal `.158` Option-A floor **NOT disqualifying but a binding per-model caveat**. The result
   `result/vwsd-grounding-headroom-v2` still **does NOT exist and is NOT cleared**.
2. **PHIL ingest:** Goldberg 2006 *Constructions at Work* catalogued → [`source/goldberg-2006-constructions-at-work`](wiki/base/sources/goldberg-2006-constructions-at-work.md).
   Book body **unreachable as OA** (Google-Books preview-walled; OUP metadata-only; archive.org borrow-only; SIL review 403) — quotes carried via **Goldberg's
   own self-archived 2009 *Cognitive Linguistics* précis** (DOI 10.1515/COGL.2009.005), **author-primary** but a précis restatement (one book locator only,
   "Goldberg 2006:5"). `status: secondary-only`; theory source, **not a human anchor**. `wanted.md` Goldberg-2006 entry updated to secondary-only.

## ⚠ Checksum-record correction (this session)

- **The committed `frozen/descriptors.json` hashes to `26616a55…`, NOT the `afe74f82…` recorded in s107's NEXT.md/log.md.** This is innocent: `afe74f82…`
  was the **descriptor-only pre-leak** sha (printed by `descriptor-full`); the later `leak-full` step **appended** the `leak{}` field, giving the committed
  file `26616a55…`. The s108 critic proved this by exact reconstruction. **Use `26616a55…` as the committed-file checksum henceforth.** The other two match:
  `frozen/run_items.json` `7f9e52fa…`, `raw/text.json` `3a9dfcbf…`.

## The THREE binding conditions the execution session MUST honor (from the certification)

1. **Gemini Option-A floor elevation is a first-class caveat.** Gemini's floor is `.158` Wilson[.104,.234] (lower bound > chance .10). Any gemini-specific
   image-rescue / gating claim must (a) be read against gemini's own ≈`.158` floor, **not** bare `.10`; (b) carry the elevation as a foregrounded caveat on
   the result page; (c) be reported alongside the pooled and per-model reads. Pooled (`.122`) and claude (`.092` clean) / gpt (`.117` near-clean) carry primary weight.
2. **Foreground the 0-intermediate-band gap.** The frozen draw has `sep_i ∈ {0, 1/3, 1}` only — **no 2/3 band**. The result must state plainly the gating
   shape is read across a **bimodal** separability distribution; the **binned image-rescue contrast** (text-failed vs text-succeeded) is the test of record,
   **not** a graded `sep→rescue` slope; the continuous Spearman/OLS companion is doubly weakened (mechanical ceiling + 2/3 gap) and stays descriptive-only.
3. **DISTRACT null reported and credited FIRST.** No IMAGE-arm lift counts as grounding headroom unless it survives the word-ablated DISTRACT control
   (gold-selection vs chance `.10`, per-model and pooled), reported **before** the gating interaction (design condition c).

Plus the design's standing obligations: **re-measure claude's raised-`max_tokens=512` IMAGE per-call cost** in a small preflight (condition d — do not run
on the stale ~3× placeholder); **day-split** under the $5 cap, each sub-batch under the $2.50 prudence flag (condition f); **images out of git**; **do NOT
re-derive** the frozen day-1 artifacts (descriptors / leak_i / run_items / text covariate); carry all four VWSD resource caveats verbatim-in-force; keep
`leak_i` a **reported covariate, never regressed out** (design B.4).

## ⚠ Do-not-re-grind note (still in force)

- **Composition / order-sensitive-composition / capability-split line is SATURATED — do NOT frame a new probe there.** (s99 verdict.)
- **Forced-both lexical line is CLOSED at R1 pending a NEW resource** ([`wanted.md`](wiki/base/wanted.md) P3).
- **VWSD v2 day-1 is DONE, FROZEN, and now critic-certified (GO-WITH-CONDITIONS)** — do **not** re-generate the descriptors / re-draw the N=120 / re-run
  any day-1 arm (re-deriving after seeing results breaks the no-retuning commitment). The frozen artifacts are committed; checksums above.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `decisions/open/` is **EMPTY** — **no ratification owed.** (Apply any Tom override first if one appears.) The s108 GO is
a **pre-run-critic gate**, not a `decisions/open/` entry — it needs no further ratification; just honor the three binding conditions above.

**Track lean — recent: 104 PHIL+emp-decision · 105 emp-reconcile[ratify]+PHIL · 106 emp-design+PHIL · 107 emp-RUN(day-1) · 108 emp-GATE+PHIL.** The
empirical loop is mid-run; the gate is cleared; the lever is now the **spend-bearing day-split IMAGE then DISTRACT arms** — which require a **fresh UTC day**.
In rough priority:

1. **IF a FRESH UTC day (NOT 2026-06-25) — re-measure claude raised-`max_tokens=512` per-call cost (condition d, small preflight), then the IMAGE arm,
   day-split.** Build the image arm by adding an `image-full` mode to `run.py` (claude `max_tokens=512`; gpt/gemini generous; low detail), reading images from
   `$VWSD_IMAGES`. Re-fetch the 572 MB zip (Drive id `15ed8TXY9Pzk68_SCooFm7AfkeFtCd16Q`, sha `b9f2f1e1…af8f`) + extract to `$VWSD_IMAGES`; **keep out of git**.
   IMAGE ≈$6.9 → split ~2 UTC days (~45–60 items/day, each sub-batch under the $2.50 single-run flag). Then the **DISTRACT arm** (≈$6.9, ~2 days) — its
   **null reported FIRST**. Then write [`result/vwsd-grounding-headroom-v2`] honoring **all three binding conditions** + a fresh independent **post-run
   verifier**; the conjecture [`distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   stays `proposed` until it lands. `analyze.py` already computes the full result sections once `raw/image.json` + `raw/distract.json` exist.
2. **PHILOSOPHICAL fallback ($0), if leaning phil or stuck on a non-fresh UTC day:** a primary OA ingest — **Croft 2001 *Radical Construction Grammar*** (P2)
   or another still-wanted item; mark `unreachable`/`secondary-only` honestly if unreachable. Or a short **theory page** connecting the now-sourced Goldberg-2006
   usage-based/statistical-preemption thread to the empirical caused-motion/way/coercion results (the frame-evoker line in
   [`concept/constructional-meaning`](wiki/base/concepts/constructional-meaning.md) + the two companion essays). Optionally strengthen the two essays' Goldberg
   premises now that the **2006** usage-based definition is citable as author-précis-attributed (their revision triggers concern the 1995/Fillmore *primaries*,
   so this is an enrichment, not a trigger discharge).
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `decisions/open/` is empty. **41 ratified to date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Session 108 spent **$0** (UTC day 2026-06-25). A checkpoint + library session: no models queried.
- Plain-language: this session ran the **independent go/no-go review** the rules require before spending on the picture half of the cleaner picture-experiment.
  A fresh reviewer re-derived every first-day number (all reproduced), confirmed nothing was re-tuned and the old answer-giveaway is gone, resolved a
  scary-looking file-fingerprint mismatch as innocent (proven by reconstructing the original fingerprint), and returned **go — with conditions**: one of three
  models sits a hair above chance on a calibration control, made a binding caveat rather than a reason to scrap. The picture half waits for a fresh budget day.
  It also shelved a founding grammar book (Goldberg 2006) honestly — the book unreachable, but the author's own published summary catalogued and clearly flagged.

## Reminder for the next cold-start

**You are session 109.** The previous slot was **`s108`** (pre-run-critic GO-WITH-CONDITIONS gate on VWSD v2 + Goldberg 2006 phil ingest; **$0**).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — check `date -u` (if still 2026-06-25, ≈$0.275 left, NO image arm today).
**RECONCILE FIRST:** `decisions/open/` is **EMPTY — no ratification owed.** The VWSD v2 gate is **CLEARED (GO-WITH-CONDITIONS)**: on a **fresh UTC day**, the
lever is the **day-split IMAGE then DISTRACT arms** — re-measure claude's raised-`max_tokens` cost first (d); honor the **three binding conditions** (gemini
floor caveat; bimodal 0-intermediate-band gap; DISTRACT null FIRST); DISTRACT null reported FIRST; fresh post-run verifier. Good $0 phil fallback: **Croft 2001**
ingest or a **Goldberg-2006 usage-based → empirical theory page**. Use committed checksum `26616a55…` for `frozen/descriptors.json`. Composition SATURATED +
forced-both CLOSED — no re-grind; do NOT re-derive the frozen day-1 artifacts. End squash-merged to `main`, website updated **with the JST clock-time stamp**.
