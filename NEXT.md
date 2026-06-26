# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-26** spent **≈$3.900** (s112 IMAGE $3.83238 + s113 $0.00019 + s114 $0 + s115 prompt-caching pilot $0.06675 + **s116 PHIL-ingest $0**). Only
**≈$1.10 headroom** remains on UTC 2026-06-26 — NOT enough for the DISTRACT arm (≈$3.8); **do not start it on 2026-06-26.** A fresh UTC day (**≥ 2026-06-27**) resets to $5 and
re-enables the day-split DISTRACT arm — **that is the priority lever. Check `date -u` FIRST.** Full ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override too.

## State

**Session 116 (UTC 2026-06-26) — philosophical-track ingest wave, $0, no research probe.** Same UTC day as s112–115, headroom too thin for the DISTRACT lever, so a $0 two-track non-empirical
session in workflow mode (1 ingest wave + read-only coherence pass + integration). `decisions/open/` was **EMPTY** at start → no ratification owed; no Tom override. What landed:

1. **THREE truth-conditional / holism founding primaries ingested** (the genuinely under-covered region — the "SILENT cell" of [`concept/truth-conditional-and-use-meaning`](wiki/base/concepts/truth-conditional-and-use-meaning.md), now that Frege + Wittgenstein are both in-repo):
   - [`source/tarski-1944-semantic-conception-of-truth`](wiki/base/sources/tarski-1944-semantic-conception-of-truth.md) — Convention T + schema "(T) X is true iff p" + snow-is-white (§4), satisfaction (§11), object-/meta-language + Liar (§§7–9). OA Chrucky transcription, §-located. **Honest limit:** 1944 article *outlines* the recursion the unread **1933 monograph** gives in full; Part II not fetched.
   - [`source/davidson-1967-truth-and-meaning`](wiki/base/sources/davidson-1967-truth-and-meaning.md) — "to give truth conditions is a way of giving the meaning of a sentence" (p. 310), "(T) s is T iff p" (p. 309), finitude (p. 304), anti-entity (p. 307), holism (p. 308), Convention-T dependence. UH OA scan, page-located; Tarski-order *reversal* flagged as interpretation, not a quote. **1984 *Inquiries* NOT read.**
   - [`source/quine-1951-two-dogmas`](wiki/base/sources/quine-1951-two-dogmas.md) — two dogmas (§I), analyticity/synonymy circle (§§I/IV), confirmation holism (corporate body §V–§VI; "unit of empirical significance is the whole of science" §VI), field-of-force (§VI). ditext/Chrucky OA — **a 1951/1961 composite, no PR pagination** (flagged; fine-grained §§1/3/4/6 quotes need a 1951 PR scan to re-verify). ***Word and Object* 1960 NOT in-repo.**
   - All three are **theory sources, NOT human anchors** (licence no model-comparison claim). Coherence pass (fresh read-only agent): **0 BLOCKERS**, every famous quote verified against canonical wording; `referential` meaning-sense dropped from the Quine page on review (over-reach); Davidson venue nit trimmed.
2. **Concept-page legs discharged** (orchestrator integration): [`concept/truth-conditional-and-use-meaning`](wiki/base/concepts/truth-conditional-and-use-meaning.md) (Tarski + Davidson legs — only Montague now "not in-repo"); [`concept/semantic-holism`](wiki/base/concepts/semantic-holism.md) (Quine 1951 + Davidson 1967 legs — *Word and Object* 1960 + *Inquiries* 1984 still out); [`concept/compositionality`](wiki/base/concepts/compositionality.md) (Davidson finitude/productivity + Tarski recursion-core notes — Montague PTQ still out). `wanted.md` statuses → RECEIVED; `wiki/index.md` catalog updated; typed-link graphs synced.
3. **Verify + website.** senselint **0 errors** (2 expected WARN, 41 INFO); linkify clean. Website: journal entry + home-page status + 2 new glossary terms (`truth-conditions`, `holism`), JST 15:19, session 116.

**Note for any future gemini run (unchanged):** `gemini-3.5-flash` now **rejects** `reasoning:{enabled:false}` and `{effort:none}` (HTTP 400 "Reasoning is mandatory"); only `{effort:minimal}` is accepted. The project already uses `effort:minimal`, so nothing breaks.

## ⚠ VWSD v2 — the lever still points at the DISTRACT arm, then the result (UNCHANGED gate; IMAGE arm DONE, FROZEN)

The day-1 freeze and the IMAGE arm are DONE and FROZEN (s107 + s112). Committed-file checksums: `frozen/descriptors.json` **`26616a55…`**, `frozen/run_items.json`
`7f9e52fa…`, `raw/text.json` `3a9dfcbf…`, **`raw/image.json` `6884eea0…430870`**. Images re-fetched + sha-verified (`b9f2f1e1…af8f`; **kept out of git**). Do **NOT**
re-run any completed arm or re-derive any frozen day-1 artifact. **NO result page exists yet, and `result/vwsd-grounding-headroom-v2` is NOT cleared** — the
DISTRACT null must be reported FIRST.

### The THREE binding conditions the result session MUST honor (from the s108 certification — STILL IN FORCE)

1. **Gemini Option-A floor elevation is a first-class caveat.** Gemini's floor is `.158` Wilson[.104,.234] (lower bound > chance .10). Any gemini-specific
   image-rescue / gating claim must (a) be read against gemini's own ≈`.158` floor, not bare `.10`; (b) carry the elevation as a foregrounded caveat; (c) be
   reported alongside the pooled (`.122`) and per-model reads (claude `.092` clean / gpt `.117` near-clean carry primary weight).
2. **Foreground the 0-intermediate-band gap.** The frozen draw has `sep_i ∈ {0, 1/3, 1}` only — **no 2/3 band**. The gating shape is read across a **bimodal**
   separability distribution; the **binned image-rescue contrast** (text-failed vs text-succeeded) is the test of record, **not** a graded `sep→rescue` slope; the
   continuous Spearman/OLS companion is doubly weakened (mechanical ceiling + 2/3 gap) and stays descriptive-only.
3. **DISTRACT null reported and credited FIRST.** No IMAGE-arm lift counts as grounding headroom unless it survives the word-ablated DISTRACT control
   (gold-selection vs chance `.10`, per-model and pooled), reported **before** the gating interaction (design condition c).

Plus the standing obligations: **images out of git**; **day-split** the DISTRACT arm under the $5 cap, each sub-batch under the $2.50 flag (use `IMG_LIMIT=60` +
`IMG_ABORT_USD`); carry all four VWSD resource caveats verbatim-in-force; keep `leak_i` a **reported covariate, never regressed out**; the claude `max_tokens=512`
cost is a measured number ($0.01244/call), not a placeholder — DISTRACT will cost ≈ IMAGE (~$3.8).

## ⚠ Do-not-re-grind note (still in force)

- **Composition / order-sensitive-composition / capability-split line is SATURATED** (s99). **Forced-both lexical line CLOSED at R1 pending a NEW resource** (`wanted.md` P3).
- **VWSD v2 day-1 + IMAGE arm are DONE, FROZEN** — do **not** re-generate descriptors / re-draw N=120 / re-run the IMAGE or any day-1 arm.
- **The reference / internalism-vs-externalism philosophical cell is SATURATED** (s114) — a new reference essay is redundant padding; weight $0 phil work toward a *different* region.
- **Prompt-caching is MEASURED and adopted as a default-off opt-in** (s115) — do NOT re-run the pilot. Lever available per-probe (`cache_prefix=True` for gemini/claude; gpt implicit).
- **Truth-conditional + holism founding primaries are NOW IN-REPO** (s116: Tarski 1944, Davidson 1967, Quine 1951; Frege s110, Wittgenstein s115) — do NOT re-ingest. Of the truth-conditional/use fault-line, only **Montague PTQ 1973** remains not-in-repo (book-walled; expect secondary-only like Goldberg/Croft).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `decisions/open/` is **EMPTY** — no ratification owed (apply any Tom override first if one appears). The s108 GO is a pre-run-critic gate already
cleared; honor the three binding conditions above; no further ratification needed there.

**Track lean — recent: 111 PHIL · 112 emp-RUN(IMAGE) · 113 tooling · 114 governance · 115 tooling-pilot+PHIL · 116 PHIL-ingest.** The empirical RESEARCH lever is mid-run and **overdue** —
two consecutive non-empirical sessions now. Fire the DISTRACT arm the moment a fresh budget day allows. In rough priority:

1. **IF a FRESH UTC day (≥ 2026-06-27) — the DISTRACT arm, day-split, then the result. (TOP PRIORITY — empirical track is overdue.)** Run `run.py distract-full` over the frozen 120 × 3
   (code already in `run.py`; word+phrase ablated, "pick the most prototypical/canonical/everyday image"; same images, low detail). ≈$3.8 → split into **two 60-item sub-batches**
   (`IMG_LIMIT=60 python3 run.py distract-full` twice; each under the $2.50 flag), `$VWSD_IMAGES` set to the re-fetched zip (Drive id `15ed8TXY9Pzk68_SCooFm7AfkeFtCd16Q`, sha `b9f2f1e1…af8f`;
   **keep out of git**). Then write [`result/vwsd-grounding-headroom-v2`] — **DISTRACT null reported and credited FIRST**, then the binned image-rescue interaction, honoring all **three
   binding conditions** + a fresh independent **post-run verifier**; promote the conjecture [`distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   only as the evidence warrants. `analyze.py` already computes every result section once `raw/distract.json` exists.
2. **PHILOSOPHICAL fallback ($0), only if still budget-blocked.** **Avoid** the saturated reference/internalism cell **and** the now-covered truth-conditional/use/holism founding region
   (Frege+Tarski+Davidson+Wittgenstein+Quine all in). Genuinely under-covered live primaries: **Montague PTQ 1973 / Partee** (the one remaining truth-conditional founding leg — expect
   book-walled, carry via author/secondary if so); the **prototype/frame** cluster (**Rosch 1975 / Rosch & Mervis 1975** family-resemblance experiments; **Fillmore 1982/1985** frame
   semantics — both ground [`concept/frame-and-prototype-semantics`](wiki/base/concepts/frame-and-prototype-semantics.md), a less-developed region); or **Lewis 1970 "General
   Semantics"** (the Markerese argument). A theory/essay synthesis in a genuinely under-covered region is also fine — but do NOT pad the well-covered cells.
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `decisions/open/` empty. **42 ratified to date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Session 116 spent **$0** (UTC day 2026-06-26; day total ≈$3.900 of $5.00 — unchanged, this was a reading session).
- Plain-language: today's budget was already mostly used by the picture experiment two sessions ago, so no new experiment ran. The session instead read and recorded three founding texts
  on the "truth-conditions" side of the theory of meaning — Tarski (making "is true" precise), Davidson (truth-conditions as a way of giving meaning), and Quine's "Two Dogmas" (the
  "holism" idea that sentences face evidence only as a whole connected body — which bears on the strongest case for a language model having meaning). With Frege and Wittgenstein, read
  earlier, four of the five founding texts of this old debate are now in the project's library, quoted at first hand. The picture experiment's word-removed control is still the next
  spending step and waits for a fresh budget day.

## Reminder for the next cold-start

**You are session 117.** The previous slot was **`s116`** (PHIL-ingest, $0: Tarski 1944 + Davidson 1967 + Quine 1951 ingested = the truth-conditional + holism founding primaries; concept-page
legs discharged on truth-conditional/holism/compositionality; only Montague PTQ now not-in-repo of that fault line). Before s116 was **`s115`** (tooling pilot + Wittgenstein PI, $0.067).
Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then
[`wiki/index.md`](wiki/index.md). **Budget: standard $5/day (UTC)** — check `date -u` (a FRESH day ≥ 2026-06-27 re-enables the day-split DISTRACT arm — **that is the priority lever, and the
empirical track is now overdue**). **RECONCILE FIRST:** `decisions/open/` is **EMPTY** — no ratification owed. The VWSD v2 gate is **CLEARED**: on a **fresh UTC day**, run the **day-split
DISTRACT arm** (`IMG_LIMIT=60 python3 run.py distract-full` ×2, `$VWSD_IMAGES` set), then write `result/vwsd-grounding-headroom-v2` with the **DISTRACT null reported FIRST**, the three binding
conditions (gemini floor caveat; bimodal 0-intermediate-band gap; DISTRACT-first), and a fresh post-run verifier. Use committed checksums `26616a55…` (descriptors), `7f9e52fa…` (run_items),
`6884eea0…430870` (image). **gemini reasoning can no longer be fully suppressed — use `{effort:minimal}`.** Composition SATURATED + forced-both CLOSED + reference-cell SATURATED +
truth-conditional/use/holism founding region COVERED — no re-grind; do NOT re-run the IMAGE/day-1/caching-pilot or re-ingest the founding primaries. End squash-merged to `main`, website
updated **with the JST clock-time stamp**.
