# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-26** spent **≈$3.900** (s112 IMAGE $3.83238 + s113 $0.00019 + s114 $0 + s115 prompt-caching pilot $0.06675 + s116 PHIL-ingest $0 + **s117 PHIL-ingest $0**). Only
**≈$1.10 headroom** remains on UTC 2026-06-26 — NOT enough for the DISTRACT arm (≈$3.8); **do not start it on 2026-06-26.** A fresh UTC day (**≥ 2026-06-27**) resets to $5 and
re-enables the day-split DISTRACT arm — **that is the priority lever. Check `date -u` FIRST.** Full ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override too.

## State

**Session 117 (UTC 2026-06-26) — philosophical-track ingest wave, $0, no research probe.** Same UTC day as s112–116, headroom too thin for the DISTRACT lever, so another $0 two-track non-empirical
session in workflow mode (1 fan-out wave of 3 parallel ingest subagents + read-only coherence pass + orchestrator integration). `decisions/open/` was **EMPTY** at start → no ratification owed; no Tom override. The wave targeted the genuinely under-covered **prototype / graded-category** region (the weight-bearing tradition behind [`result/lexical-sense-gradience-v1`](wiki/findings/results/lexical-sense-gradience-v1.md)). What landed:

1. **THREE sources ingested** (each its own page; coherence pass = **0 BLOCKERs**):
   - [`source/rosch-mervis-1975-family-resemblances`](wiki/base/sources/rosch-mervis-1975-family-resemblances.md) — **received, PRIMARY-DIRECT** (Colorado course-page scan of *Cognitive Psychology* 7(4):573–605; journal pagination). The family-resemblance attribute-overlap method (pp. 581–582), the six Spearman typicality correlations 0.84–0.94 (p < .001, Table 2, p. 582), and the closing "empirical confirmation of Wittgenstein's (1953) argument" (p. 605). OCR artifacts ("criterial"→"criteria1", "p < .001"→"p < .OOl") flagged. `refines` the concept page **and** `source/wittgenstein-1953-philosophical-investigations` (the experiment operationalizes §§66–67).
   - [`source/rosch-1975-cognitive-representations`](wiki/base/sources/rosch-1975-cognitive-representations.md) — **secondary-only** (JEP:General 104(3):192–233). OA primary **authoritatively unreachable** (Unpaywall `oa_status: closed`, `oa_locations: []`; Semantic Scholar `CLOSED`; academia.edu/CORE/scispace 403/Cloudflare). Findings carried via **Rosch's own 1978 "Principles of Categorization"** retrospective, pinned to the **1975b** citation key; **no page within 192–233 asserted as read.** `supports → result/lexical-sense-gradience-v1` is **theory-grounding only** (that result's anchor stays its DURel/Usim resource). **The Rosch 1975 PRIMARY stays wanted.**
   - [`source/lewis-1970-general-semantics`](wiki/base/sources/lewis-1970-general-semantics.md) — **received, PRIMARY-DIRECT** (David K. Lewis papers author-estate self-archive, *Synthese* 22 original pp. 18–67). The **Markerese argument** (pp. 18–19) + meaning-as-truth-conditions (pp. 22–23) + intension-as-function (pp. 23–25) + compositional phrase-marker tree (pp. 31–33). The LLM-application is flagged in-page as the project's interpretive use, not a Lewis claim.
   - All three are **theory / empirical-psychology sources, NOT human anchors** (predate LLMs; ground the theory, never a model result).
2. **Integration (orchestrator).** [`concept/frame-and-prototype-semantics`](wiki/base/concepts/frame-and-prototype-semantics.md): the two Rosch legs **discharged** (primary + secondary), the prototype section now carries Rosch & Mervis's own numbers + Wittgenstein-confirmation quote, "Honest gaps" rewritten to the new mixed provenance, `updated`→2026-06-26, three new `depends-on` links. **Fixed a STALE defect:** the page (last touched 2026-05-31) still said Fillmore was "not in-repo" — but [`source/fillmore-1982-frame-semantics`](wiki/base/sources/fillmore-1982-frame-semantics.md) has been in-repo (secondary-only) since **s103**; corrected on both the concept page and in `wanted.md` (its Fillmore entry was also stale at `wanted`). `wanted.md` statuses updated (Lewis→RECEIVED, Rosch pair→PARTIALLY RECEIVED, Fillmore→SECONDARY-ONLY). `wiki/index.md` catalog: 3 new source rows + concept-page row refreshed.
3. **Verify + website.** senselint **0 errors** (2 expected WARN, 41 INFO); linkify clean. Website: journal entry + home-page status + "The latest" + 1 new glossary term (`prototype` / family resemblance), JST 18:00, session 117.

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
- **The reference / internalism-vs-externalism philosophical cell is SATURATED** (s114).
- **Prompt-caching is MEASURED and adopted as a default-off opt-in** (s115) — do NOT re-run the pilot.
- **Truth-conditional + holism founding primaries are IN-REPO** (s116: Tarski 1944, Davidson 1967, Quine 1951; Frege s110, Wittgenstein s115) — do NOT re-ingest.
- **The PROTOTYPE / graded-category founding region is NOW COVERED** (s117: Rosch & Mervis 1975 primary + Rosch 1975 secondary-only; Fillmore 1982 already in since s103; Wittgenstein family-resemblance s115) — do **NOT** re-ingest. Of that cluster, only **Lakoff 1987** (book-walled), **Fillmore 1985**, and the **Rosch 1975 PRIMARY** (OA-unreachable) remain not-in-repo. Of the truth-conditional fault line, only **Montague PTQ 1973** remains not-in-repo (book-walled).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `decisions/open/` is **EMPTY** — no ratification owed (apply any Tom override first if one appears). The s108 GO is a pre-run-critic gate already
cleared; honor the three binding conditions above; no further ratification needed there.

**Track lean — recent: 112 emp-RUN(IMAGE) · 113 tooling · 114 governance · 115 tooling-pilot+PHIL · 116 PHIL-ingest · 117 PHIL-ingest.** The empirical RESEARCH lever is mid-run and **overdue** —
**three** consecutive non-empirical sessions now. Fire the DISTRACT arm the moment a fresh budget day allows. In rough priority:

1. **IF a FRESH UTC day (≥ 2026-06-27) — the DISTRACT arm, day-split, then the result. (TOP PRIORITY — empirical track is three sessions overdue.)** Run `run.py distract-full` over the frozen 120 × 3
   (code already in `run.py`; word+phrase ablated, "pick the most prototypical/canonical/everyday image"; same images, low detail). ≈$3.8 → split into **two 60-item sub-batches**
   (`IMG_LIMIT=60 python3 run.py distract-full` twice; each under the $2.50 flag), `$VWSD_IMAGES` set to the re-fetched zip (Drive id `15ed8TXY9Pzk68_SCooFm7AfkeFtCd16Q`, sha `b9f2f1e1…af8f`;
   **keep out of git**). Then write [`result/vwsd-grounding-headroom-v2`] — **DISTRACT null reported and credited FIRST**, then the binned image-rescue interaction, honoring all **three
   binding conditions** + a fresh independent **post-run verifier**; promote the conjecture [`distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   only as the evidence warrants. `analyze.py` already computes every result section once `raw/distract.json` exists.
2. **PHILOSOPHICAL fallback ($0), only if still budget-blocked.** **Avoid** the now-saturated cells: reference/internalism (s114); the truth-conditional/use/holism founding region (Frege+Tarski+Davidson+Wittgenstein+Quine);
   **and the prototype/frame founding region (Fillmore 1982 + Rosch & Mervis 1975 + Rosch 1975-secondary + Wittgenstein family-resemblance — all now in, per s117).** Genuinely under-covered live primaries that remain:
   **Montague PTQ 1973 / Partee** (the one remaining truth-conditional founding leg — expect book-walled, carry via author/secondary if so); **Lewis 1969 *Convention*** (the philosophical theory of convention behind the
   commutative-convention framing — distinct from the now-in-repo Lewis 1970); **Cruse 1986 *Lexical Semantics*** (P2 sense-relation baseline); or **Dummett 1975/76 "What is a Theory of Meaning?"** (molecularism, the middle
   position for `semantic-holism`). A theory/essay synthesis in a genuinely under-covered region is also fine (e.g. an essay drawing the now-fully-sourced prototype line + the standing distributional null together) — but do NOT pad the covered cells, and do not re-ingest the prototype/truth-conditional primaries.
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `decisions/open/` empty. **42 ratified to date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Session 117 spent **$0** (UTC day 2026-06-26; day total ≈$3.900 of $5.00 — unchanged, another reading session).
- Plain-language: today's budget was already mostly used by the picture experiment several sessions ago, so no new experiment ran. The session instead read and recorded three founding texts behind
  one of the project's own findings — that the models grade word senses on a smooth scale much as people do. Two are the founding experiments of "prototype theory" (Rosch & Mervis 1975, read at first
  hand; Rosch 1975, recorded second-hand because no free copy of the original could be found — flagged honestly), and one (Lewis 1970) is the warning that translating a sentence into a formal code is
  not the same as giving its meaning. A stale note on the project's own page — wrongly saying a frame-semantics source wasn't yet in the library — was also corrected. The picture experiment's
  word-removed control is still the next spending step and waits for a fresh budget day.

## Reminder for the next cold-start

**You are session 118.** The previous slot was **`s117`** (PHIL-ingest, $0: Rosch & Mervis 1975 primary + Rosch 1975 secondary-only + Lewis 1970 primary; prototype/graded-category founding region
now covered; stale Fillmore "not in-repo" flag corrected on [`concept/frame-and-prototype-semantics`](wiki/base/concepts/frame-and-prototype-semantics.md)). Before s117 was **`s116`** (truth-conditional + holism
founding primaries: Tarski 1944, Davidson 1967, Quine 1951). Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). **Budget: standard $5/day (UTC)** — check `date -u` (a FRESH day ≥ 2026-06-27 re-enables the day-split
DISTRACT arm — **that is the priority lever, and the empirical track is now THREE sessions overdue**). **RECONCILE FIRST:** `decisions/open/` is **EMPTY** — no ratification owed. The VWSD v2 gate is **CLEARED**:
on a **fresh UTC day**, run the **day-split DISTRACT arm** (`IMG_LIMIT=60 python3 run.py distract-full` ×2, `$VWSD_IMAGES` set), then write `result/vwsd-grounding-headroom-v2` with the **DISTRACT null
reported FIRST**, the three binding conditions (gemini floor caveat; bimodal 0-intermediate-band gap; DISTRACT-first), and a fresh post-run verifier. Use committed checksums `26616a55…` (descriptors),
`7f9e52fa…` (run_items), `6884eea0…430870` (image). **gemini reasoning can no longer be fully suppressed — use `{effort:minimal}`.** Composition SATURATED + forced-both CLOSED + reference-cell SATURATED +
truth-conditional/use/holism founding region COVERED + **prototype/frame founding region COVERED (s117)** — no re-grind; do NOT re-run the IMAGE/day-1/caching-pilot or re-ingest the founding primaries.
End squash-merged to `main`, website updated **with the JST clock-time stamp**.
