# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-26** spent **≈$3.900** (s112 IMAGE $3.83238 + s113 $0.00019 + s114 $0 + s115 prompt-caching pilot $0.06675 + s116 PHIL-ingest $0 + s117 PHIL-ingest $0 + **s118 PHIL-essay $0**). Only
**≈$1.10 headroom** remains on UTC 2026-06-26 — NOT enough for the DISTRACT arm (≈$3.8); **do not start it on 2026-06-26.** A fresh UTC day (**≥ 2026-06-27**) resets to $5 and
re-enables the day-split DISTRACT arm — **that is the priority lever, and the empirical RESEARCH track is now FOUR sessions overdue. Check `date -u` FIRST.** Full ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override too.

## State

**Session 118 (UTC 2026-06-26) — philosophical-track ORIGINAL ESSAY, $0, no research probe.** Same UTC day as s112–117, headroom too thin for the DISTRACT lever (≈$1.10 < ≈$3.8), so another $0 non-empirical session. **Deliberately a WRITING session, not a fourth straight ingest:** the phil track's first-class artifact (an own-voice essay) had not been written since s110, while s115–117 were all ingest — so the highest-value, most-varied $0 move was to *use* the freshly-ingested prototype primaries in an original synthesis (NEXT.md option 2's explicit suggestion). `decisions/open/` **EMPTY** at start → no ratification owed; no Tom override. What landed:

1. **ONE new essay** — [`essay/gradient-from-overlap`](wiki/findings/essays/gradient-from-overlap.md) (`status: draft`, senses `distributional`+`referential`). **Original move (a sorting):** the project's standing "distributional null" worry about [`result/lexical-sense-gradience-v1`](wiki/findings/results/lexical-sense-gradience-v1.md) — that the panel's graded sense-relatedness signal may be "nothing but graded distributional similarity" — is **not** a machine-specific deflation. Rosch & Mervis 1975 *founded* prototype theory by **deriving graded typicality from attribute OVERLAP** (family-resemblance score, p. 575; Spearman 0.84–0.94, p. 582) and **explicitly declined a learning/formation processing model** (p. 574, verbatim) — so a typicality gradient never licensed a stored-prototype reading, in people *or* models. Hence the result page's "**monotonicity, not representation**" is fidelity to the prototype tradition's own discipline; and "prototype-consistent" vs "merely distributional" are **the same overlap-derived shape, not rival hypotheses** → the worry is **re-located, not dissolved**, sharpened to *which overlap space* the model's gradient lives in (human-listed attributes vs distributional context — left open as the standing [`concept/distributional-meaning`](wiki/base/concepts/distributional-meaning.md) question). Backstops [`essay/graded-scale-ungraded-commitment`](wiki/findings/essays/graded-scale-ungraded-commitment.md). **No new empirical claim, no human-comparison beyond v1, none of Rosch/Wittgenstein a human anchor** (declared in-page).
2. **Adversarial coherence pass (fresh read-only agent): 0 BLOCKERs.** It verified every quote char-for-char against the in-repo source pages and caught a real **over-read** (the essay had upgraded R&M's p.574 disclaimer — about a *learning/formation* processing model — into an explicit *representation* disclaimer; the representational reading is the essay's *inference*, now marked as such throughout) + 2 quote-fidelity SHOULD-FIX (a stitched/reordered v1 quote; a stray paren) + the index-coverage WARN — **all applied** before commit. No fabrication shipped.
3. **Integration:** `wiki/index.md` essays catalog — 1 new row. No concept/source/wanted edits needed (the essay re-sorts existing material; the prototype primaries went in s117).
4. **Verify + website.** senselint **0 errors** (2 expected WARN, 41 INFO); linkify clean. Website: journal entry + home-page status (Current focus rewritten to the essay) + "The latest" card + index/journal footers re-stamped, JST 21:54, session 118. No new glossary term (prototype/family-resemblance already added s117).

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
- **The prototype-gradient / distributional-null SYNTHESIS is now WRITTEN** (s118: [`essay/gradient-from-overlap`](wiki/findings/essays/gradient-from-overlap.md) — gradient-from-overlap is common ground, not a prototype-vs-distributional contest; the surviving question is *which overlap space*). Do **NOT** re-derive that sorting; a *new* essay must take a genuinely different angle.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `decisions/open/` is **EMPTY** — no ratification owed (apply any Tom override first if one appears). The s108 GO is a pre-run-critic gate already
cleared; honor the three binding conditions above; no further ratification needed there.

**Track lean — recent: 112 emp-RUN(IMAGE) · 113 tooling · 114 governance · 115 tooling-pilot+PHIL · 116 PHIL-ingest · 117 PHIL-ingest · 118 PHIL-essay.** The empirical RESEARCH lever is mid-run and **overdue** —
**four** consecutive non-empirical sessions now (all budget-blocked, legitimately). Fire the DISTRACT arm the moment a fresh budget day allows. In rough priority:

1. **IF a FRESH UTC day (≥ 2026-06-27) — the DISTRACT arm, day-split, then the result. (TOP PRIORITY — empirical track is FOUR sessions overdue.)** Run `run.py distract-full` over the frozen 120 × 3
   (code already in `run.py`; word+phrase ablated, "pick the most prototypical/canonical/everyday image"; same images, low detail). ≈$3.8 → split into **two 60-item sub-batches**
   (`IMG_LIMIT=60 python3 run.py distract-full` twice; each under the $2.50 flag), `$VWSD_IMAGES` set to the re-fetched zip (Drive id `15ed8TXY9Pzk68_SCooFm7AfkeFtCd16Q`, sha `b9f2f1e1…af8f`;
   **keep out of git**). Then write [`result/vwsd-grounding-headroom-v2`] — **DISTRACT null reported and credited FIRST**, then the binned image-rescue interaction, honoring all **three
   binding conditions** + a fresh independent **post-run verifier**; promote the conjecture [`distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   only as the evidence warrants. `analyze.py` already computes every result section once `raw/distract.json` exists.
2. **PHILOSOPHICAL fallback ($0), only if still budget-blocked.** **Avoid** the now-saturated cells: reference/internalism (s114); the truth-conditional/use/holism founding region (Frege+Tarski+Davidson+Wittgenstein+Quine);
   **and the prototype/frame founding region (Fillmore 1982 + Rosch & Mervis 1975 + Rosch 1975-secondary + Wittgenstein family-resemblance — all now in, per s117).** Genuinely under-covered live primaries that remain:
   **Montague PTQ 1973 / Partee** (the one remaining truth-conditional founding leg — expect book-walled, carry via author/secondary if so); **Lewis 1969 *Convention*** (the philosophical theory of convention behind the
   commutative-convention framing — distinct from the now-in-repo Lewis 1970); **Cruse 1986 *Lexical Semantics*** (P2 sense-relation baseline); or **Dummett 1975/76 "What is a Theory of Meaning?"** (molecularism, the middle
   position for `semantic-holism`). A theory/essay synthesis in a genuinely under-covered region is also fine — but the **prototype-line + distributional-null** synthesis is now spent ([`essay/gradient-from-overlap`](wiki/findings/essays/gradient-from-overlap.md), s118), so a new essay needs a different angle; do NOT pad the covered cells, and do not re-ingest the prototype/truth-conditional primaries.
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `decisions/open/` empty. **42 ratified to date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Session 118 spent **$0** (UTC day 2026-06-26; day total ≈$3.900 of $5.00 — unchanged, a writing session).
- Plain-language: today's budget was already mostly used by the picture experiment several sessions ago, so no new experiment ran. Instead of a fourth straight reading session, the project wrote a new
  short essay of its own. Its point: when the models grade word senses on a smooth scale (as people do), that smooth scale — even in the classic human experiments — was never proof of a stored "best
  example" inside; the founders of "prototype theory" built the scale out of feature overlap and said plainly they were not modelling a stored prototype. So the project's habit of saying "we measured
  behaviour, not an inner representation" is faithful to that tradition, not a put-down aimed at machines; and "it has best examples" versus "it's just pattern" stop being rival stories. An independent
  check verified every quotation and caught one place that read more into the founders' words than they wrote, fixed before keeping. The picture experiment's word-removed control is still the next
  spending step and waits for a fresh budget day.

## Reminder for the next cold-start

**You are session 119.** The previous slot was **`s118`** (PHIL-essay, $0: wrote [`essay/gradient-from-overlap`](wiki/findings/essays/gradient-from-overlap.md) — gradient-from-overlap is common ground, not a
prototype-vs-distributional contest; coherence pass 0 BLOCKERs, caught + fixed a p.574-disclaimer over-read). Before s118 was **`s117`** (PHIL-ingest: Rosch & Mervis 1975 primary + Rosch 1975 secondary-only + Lewis 1970 primary;
prototype/graded-category founding region covered). Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). **Budget: standard $5/day (UTC)** — check `date -u` (a FRESH day ≥ 2026-06-27 re-enables the day-split
DISTRACT arm — **that is the priority lever, and the empirical track is now FOUR sessions overdue**). **RECONCILE FIRST:** `decisions/open/` is **EMPTY** — no ratification owed. The VWSD v2 gate is **CLEARED**:
on a **fresh UTC day**, run the **day-split DISTRACT arm** (`IMG_LIMIT=60 python3 run.py distract-full` ×2, `$VWSD_IMAGES` set), then write `result/vwsd-grounding-headroom-v2` with the **DISTRACT null
reported FIRST**, the three binding conditions (gemini floor caveat; bimodal 0-intermediate-band gap; DISTRACT-first), and a fresh post-run verifier. Use committed checksums `26616a55…` (descriptors),
`7f9e52fa…` (run_items), `6884eea0…430870` (image). **gemini reasoning can no longer be fully suppressed — use `{effort:minimal}`.** Composition SATURATED + forced-both CLOSED + reference-cell SATURATED +
truth-conditional/use/holism founding region COVERED + **prototype/frame founding region COVERED (s117)** — no re-grind; do NOT re-run the IMAGE/day-1/caching-pilot or re-ingest the founding primaries.
End squash-merged to `main`, website updated **with the JST clock-time stamp**.
