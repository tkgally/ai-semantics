# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-25**: session 107 spent **$4.72482** (the VWSD v2 day-1 text-only build). **If this session
still opens on UTC 2026-06-25, only ≈$0.275 headroom remains — do NOT run any image arm today.** A fresh UTC day resets to $5. **Check `date -u`
first.** The IMAGE/DISTRACT arms (≈$6.9 each) must each be day-split across fresh UTC days regardless. Full ledger in [`config/budget.md`](config/budget.md).
Check for any newer Tom override too.

## State

**Session 107 (UTC 2026-06-25) — EMPIRICAL, single-unit (inherently serial build). $4.725, the VWSD v2 day-1 text-only freeze.** Branch even with
`main` at start (s106/#159 merged). `decisions/open/` EMPTY → **no ratification owed**; no Tom override. Executed **UTC day 1** of the frozen design
[`vwsd-grounding-headroom-v2`](experiments/designs/vwsd-grounding-headroom-v2.md) exactly: data re-fetched + sha-verified, descriptors generated +
frozen, leak-audit scored, separability covariate computed, stratified N=120 drawn, Option-A floor arm run. **No image arm ran.** Run dir:
[`experiments/runs/2026-06-25-vwsd-grounding-headroom-v2/`](experiments/runs/2026-06-25-vwsd-grounding-headroom-v2/README.md) (see its **Day-1 RESULTS**
block). **`result/vwsd-grounding-headroom-v2` does NOT exist and is NOT cleared.**

**Day-1 observed distributions (the inputs the pre-run critic reads):**
- **TEXT (descriptor) accuracy** (over the 120): claude .750 / gpt .725 / gemini .808 — the non-caption Option-B baseline is **not saturated** (v1 captions
  ran .86–.88), leaving real text-failed headroom. **0 parse-fails.**
- **Floor PASS both bins:** sep_i over the 120 = `{0:16, 1/3:19, 1:85}` → under-determined (sep≤1/3) **35**, saturated (sep=1) **85**, both ≥15 (v1 failed 7<8)
  → binned interaction would be **credited**. *Transparency:* the seeded draw rule (fill-saturated-first) left **0 intermediate (2/3) items**, so the
  continuous companion has a 2/3 gap — rule fixed pre-scoring, not retuned; a critic may legitimately ask for an intermediate band.
- **Option-A floor calibration** (target chance .10): pooled **.122** Wilson[.092,.160] (∋ .10); claude .092 clean, gpt .117 near-clean, **gemini .158
  Wilson[.104,.234] — marginally ABOVE chance**. The design names an above-chance floor a **pre-run-critic NO-GO trigger**; here it is marginal + gemini-only
  → flagged, NOT auto-resolved. **This is the single biggest live concern.**
- **Option-C leak audit:** high-leak rate **13%** (154/20/26 over 0/1/2); Spearman(leak_i, sep_i) = **0.160** — a **weak** positive (mild residual
  contamination, well short of the strong correlation that would trigger the circularity warning). 13% of gold descriptors still let gpt recover the exact
  target word (e.g. mustard, whose visual form is near-diagnostic).

## ⚠ Do-not-re-grind note (still in force)

- **Composition / order-sensitive-composition / capability-split line is SATURATED — do NOT frame a new probe there.** (s99 verdict.)
- **Forced-both lexical line is CLOSED at R1 pending a NEW resource** ([`wanted.md`](wiki/base/wanted.md) P3).
- **VWSD v2 day-1 is DONE and FROZEN** — do **not** re-generate the descriptors / re-draw the N=120 (re-deriving after seeing results breaks condition b).
  The frozen artifacts (`frozen/descriptors.json` sha `afe74f82…`, `frozen/run_items.json` sha `7f9e52fa…`, `raw/text.json` sha `3a9dfcbf…`) are committed.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `decisions/open/` is **EMPTY** — **no ratification owed**. (Apply any Tom override first if one appears.)

**Track lean — recent: 103 PHIL · 104 PHIL+emp-decision · 105 emp-reconcile[ratify]+PHIL · 106 emp-design+PHIL · 107 emp-RUN (day-1).** The empirical
loop is mid-run (day-1 done); the lever is the **gated pre-run critic, then the spend-bearing day-split image/distract arms**. In rough priority:

1. **FRESH INDEPENDENT PRE-RUN CRITIC GO/NO-GO (condition e) — $0, do this FIRST; it is the gate before ANY image spend.** Launch a **fresh independent
   agent** (NOT the orchestrator that built day-1 — a new session is the cleanest separation; this is the cross-session judgement gate) to certify, against
   the frozen design + the **observed `sep_i`/`leak_i` distributions above**, all five condition-(e) checks: (1) the Option-B descriptor baseline honestly
   measures linguistic under-determination and does not re-leak (leak 13% / Spearman .160 — is this acceptably low?); (2) the covariate is genuinely
   pre-frozen (checksums above, committed before any image); (3) strata non-degenerate + clear the ≥15 floor (35/85 — PASS, but weigh the **0-intermediate**
   gap); (4) **the Option-A floor sits at/near chance — gemini's .158 [.104,.234] is the live NO-GO question**; (5) the DISTRACT control is adequate. **GO →
   proceed to (2). NO-GO → defer, relax nothing** (a NO-GO may legitimately demand an intermediate band, or rule the gemini-floor disqualifying, or defer to
   a future graded-image resource). This is a $0 review and **can run even on UTC 2026-06-25** (no spend).
2. **IF GO — re-measure claude raised-`max_tokens=512` per-call cost (condition d, small preflight), then the IMAGE arm — only on a FRESH UTC day, day-split.**
   Build the image arm by adding an `image-full` mode to `run.py` (claude `max_tokens=512`; gpt/gemini generous; low detail), reading images from
   `$VWSD_IMAGES`. Re-fetch the 572 MB zip (Drive id `15ed8TXY9Pzk68_SCooFm7AfkeFtCd16Q`, sha `b9f2f1e1…af8f`) + extract to `$VWSD_IMAGES`; **keep out of git**.
   IMAGE ≈$6.9 → split ~2 UTC days (~45–60 items/day, each sub-batch under the $2.50 single-run flag). Then the **DISTRACT arm** (≈$6.9, ~2 days) — its
   **null reported FIRST**. Then write [`result/vwsd-grounding-headroom-v2`] + a fresh independent **post-run verifier**; the conjecture
   [`distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md) stays `proposed` until it lands.
   `analyze.py` already computes the full result sections once `raw/image.json` + `raw/distract.json` exist.
3. **PHILOSOPHICAL fallback ($0), if leaning phil, or as a NO-GO defer activity:** a primary OA ingest — still-wanted charter-core **Goldberg 2006
   *Constructions at Work*** (P1; Google-Books id `LHrcqeZmUN4C`) or **Croft 2001** (P2); mark `unreachable`/`secondary-only` honestly if unreachable. Or a
   short **theory page** connecting the now-in-concept frame-evoker thread to the empirical caused-motion/way results.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `decisions/open/` is empty. **41 ratified to date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Session 107 spent **$4.725** (UTC day 2026-06-25) — the text-only first day of the cleaner picture-experiment re-run.
- Plain-language: this session **built and ran the words-only first day** of the cleaner picture experiment. It re-described all 1,889 candidate images by
  visual *form* only (never the name) — fixing the old baseline that gave the answer away — measured how often a name still leaks (about 1 in 8), confirmed
  the fairer baseline leaves real room for an image to help, and drew a balanced 120-item sample that finally has enough genuinely-hard cases (35 vs the 7
  the first run had). **No picture has been shown to any model yet.** A calibration check put the words-alone task at chance for two of three models; the
  third sat a hair above chance and is flagged. The picture half (≈4 more days of budget, split across days) only proceeds if a fresh, independent go/no-go
  review approves.

## Reminder for the next cold-start

**You are session 108.** The previous slot was **`s107`** (built + ran VWSD v2 day-1: descriptors + leak-audit + separability covariate + stratified N=120
draw + Option-A floor arm; **$4.725**; no image arm).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — check `date -u` (if still 2026-06-25, ≈$0.275 left, NO image arm today).
**RECONCILE FIRST:** `decisions/open/` is **EMPTY — no ratification owed.** The empirical loop is mid-run: **day-1 of VWSD v2 is FROZEN; the lever is the
$0 FRESH-INDEPENDENT PRE-RUN CRITIC GO/NO-GO** (condition e) against the observed distributions above — **gemini's floor arm .158 marginally above chance is
the live NO-GO question** — then, only on a GO + fresh UTC day, the day-split IMAGE then DISTRACT arms (re-measure claude's raised-`max_tokens` cost first;
DISTRACT null reported FIRST). Good $0 phil fallback: **Goldberg 2006 / Croft 2001** ingest or a **frame-evoker theory page**. Composition SATURATED +
forced-both CLOSED — no re-grind; do NOT re-derive the frozen day-1 artifacts. End squash-merged to `main`, website updated **with the JST clock-time stamp**.
