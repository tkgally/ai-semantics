# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-26** spent **$3.83238** (all of it session 112, the VWSD v2 IMAGE arm). **If a session
still opens on UTC 2026-06-26, only ≈$1.17 headroom remains — NOT enough for the DISTRACT arm (≈$3.8); do not start it today.** A fresh UTC
day resets to $5 and re-enables a day-split DISTRACT arm. **Check `date -u` FIRST.** Full ledger in [`config/budget.md`](config/budget.md).
Check for any newer Tom override too.

## State

**Session 112 (UTC 2026-06-26) — single-unit empirical (the IMAGE arm execution is inherently serial), $3.83238.** First fresh UTC day after
the day-1 freeze, so the budget-blocked empirical lever fired. `decisions/open/` **EMPTY** → no ratification owed; no Tom override. The s108
pre-run-critic GO (GO-WITH-CONDITIONS) was already in hand — no fresh critic needed. What landed:

1. **VWSD v2 IMAGE arm RAN and is FROZEN — but it is RAW DATA, NOT a result.** `run.py image-full` over the frozen 120 × 3 models (design
   arm 4); added the IMAGE + DISTRACT arm code to [`run.py`](experiments/runs/2026-06-25-vwsd-grounding-headroom-v2/run.py) (prompts mirror v1
   verbatim; **condition (d)**: claude `max_tokens` 16→512; resumable + day-split with a per-sub-batch new-spend cost guard). Output
   `raw/image.json` — **360 records, 0 missing-cost, 0 parse-fails (all 3 models — v1's 6-claude-truncation bias is GONE), sha256
   `6884eea0…430870`**. Images re-fetched + sha-verified (`b9f2f1e1…af8f`, exact match to s100/s107; out of git).
2. **Condition (d) DISCHARGED with a measured number.** claude's re-measured raised-`max_tokens=512` cost = **$0.01244/call** (≈ v1's $0.0128;
   claude emits the bare digit, `raw_len=1`) — the design's conservative ~3× placeholder ($0.038 → $6.9 full arm) overcounts ~2×. Full IMAGE
   arm **$3.77035** (claude $1.49279 / gpt $0.32269 / gemini $1.95487) fit a **single** UTC day, run as **two 60-item sub-batches** ($1.871 +
   $1.835 new spend each, each under the $2.50 single-run prudence flag).
3. **NO result page, NO headroom claim — by design.** Binding condition 3 (design condition c) requires the **DISTRACT null reported FIRST**
   before any image lift counts as grounding headroom. The DISTRACT arm has **not** run. `analyze.py` prints preliminary image-accuracy numbers
   (claude .850 / gpt .592 / gemini .867) but they **carry no weight** and were **not** written into any finding. The conjecture
   [`distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md) stays
   `proposed`; `result/vwsd-grounding-headroom-v2` still **does NOT exist and is NOT cleared**.

## ⚠ VWSD v2 — the lever now points at the DISTRACT arm, then the result (UNCHANGED gate, one arm advanced)

The day-1 freeze and the IMAGE arm are DONE and FROZEN. Committed-file checksums: `frozen/descriptors.json` **`26616a55…`**,
`frozen/run_items.json` `7f9e52fa…`, `raw/text.json` `3a9dfcbf…`, **`raw/image.json` `6884eea0…430870` (NEW this session)**. Do **NOT**
re-run any completed arm or re-derive any frozen day-1 artifact.

### The THREE binding conditions the result session MUST honor (from the s108 certification — STILL IN FORCE)

1. **Gemini Option-A floor elevation is a first-class caveat.** Gemini's floor is `.158` Wilson[.104,.234] (lower bound > chance .10). Any
   gemini-specific image-rescue / gating claim must (a) be read against gemini's own ≈`.158` floor, not bare `.10`; (b) carry the elevation as a
   foregrounded caveat on the result page; (c) be reported alongside the pooled (`.122`) and per-model reads (claude `.092` clean /
   gpt `.117` near-clean carry primary weight).
2. **Foreground the 0-intermediate-band gap.** The frozen draw has `sep_i ∈ {0, 1/3, 1}` only — **no 2/3 band**. The gating shape is read across a
   **bimodal** separability distribution; the **binned image-rescue contrast** (text-failed vs text-succeeded) is the test of record, **not** a
   graded `sep→rescue` slope; the continuous Spearman/OLS companion is doubly weakened (mechanical ceiling + 2/3 gap) and stays descriptive-only.
3. **DISTRACT null reported and credited FIRST.** No IMAGE-arm lift counts as grounding headroom unless it survives the word-ablated DISTRACT
   control (gold-selection vs chance `.10`, per-model and pooled), reported **before** the gating interaction (design condition c).

Plus the standing obligations: **images out of git**; **day-split** the DISTRACT arm under the $5 cap, each sub-batch under the $2.50 flag (use
`IMG_LIMIT=60` + `IMG_ABORT_USD`); carry all four VWSD resource caveats verbatim-in-force; keep `leak_i` a **reported covariate, never regressed
out**; the claude `max_tokens=512` cost is now a measured number ($0.01244/call), not a placeholder — DISTRACT will cost ≈ IMAGE (~$3.8).

## ⚠ Do-not-re-grind note (still in force)

- **Composition / order-sensitive-composition / capability-split line is SATURATED — do NOT frame a new probe there.** (s99 verdict.)
- **Forced-both lexical line is CLOSED at R1 pending a NEW resource** ([`wanted.md`](wiki/base/wanted.md) P3).
- **VWSD v2 day-1 + IMAGE arm are DONE, FROZEN** — do **not** re-generate descriptors / re-draw the N=120 / re-run the IMAGE or any day-1 arm.

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `decisions/open/` is **EMPTY — no ratification owed.** (Apply any Tom override first if one appears.) The s108
GO is a **pre-run-critic gate**, not a `decisions/open/` entry — it is already cleared; honor the three binding conditions above; no further
ratification needed.

**Track lean — recent: 107 emp-RUN(day-1) · 108 emp-GATE+PHIL · 109 PHIL · 110 PHIL · 111 PHIL · 112 emp-RUN(IMAGE).** The empirical lever is
mid-run and should keep firing while a fresh budget day allows — finish it before swinging back to philosophy. In rough priority:

1. **IF a FRESH UTC day (NOT 2026-06-26) — the DISTRACT arm, day-split, then the result.** Run `run.py distract-full` over the frozen 120 × 3
   (the code is already in `run.py`; word+phrase ablated, "pick the most prototypical/canonical/everyday image"; same images, low detail). It is
   ≈$3.8 → split into **two 60-item sub-batches** (`IMG_LIMIT=60 python3 run.py distract-full` twice; each under the $2.50 flag), with
   `$VWSD_IMAGES` set to the re-fetched zip (Drive id `15ed8TXY9Pzk68_SCooFm7AfkeFtCd16Q`, sha `b9f2f1e1…af8f`; **keep out of git**). Then write
   [`result/vwsd-grounding-headroom-v2`] — **DISTRACT null reported and credited FIRST**, then the binned image-rescue interaction, honoring all
   **three binding conditions** and a fresh independent **post-run verifier**; promote the conjecture only as the evidence warrants (it stays
   `proposed` unless the result clears the gate). `analyze.py` already computes every result section once `raw/distract.json` exists.
2. **PHILOSOPHICAL fallback ($0), only if still budget-blocked** (a fresh UTC day with <≈$3.8 headroom, or DISTRACT deferred): **only Kripke**
   remains of the named externalist-reference primaries (note: ingesting him re-arms the reference essays' pure-causal trigger (a)/(c) and the
   stereotype essay's "fourth component" question). Other live phil primaries: **Wittgenstein 1953** P2 (meaning-as-use, ungrounds
   [`concept/truth-conditional-and-use-meaning`](wiki/base/concepts/truth-conditional-and-use-meaning.md) pole (b)); **Cruse 1986 / Murphy 2003**
   lexical-semantics P2; **Chomsky 2000 / Fodor 1987** for the **internalist** pole of `referential-meaning` (now lopsided — externalist side
   well-anchored, internalist side still characterization-only); Tarski/Davidson/Montague for the truth-conditional lineage. A short
   theory/essay synthesis connecting existing sourced material is also fine. **Avoid** re-grinding the constructional empirical lines.
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `decisions/open/` is empty. **41 ratified to date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Session 112 spent **$3.83238** (UTC day 2026-06-26) — the picture half of the cleaner picture-and-words experiment.
- Plain-language: the first fresh budget day in three opened, so the experiment's spending step ran. Three models were each shown the ten real
  candidate images for 120 word puzzles and asked to pick the one matching the intended sense. All 360 answers came back clean (none dropped or
  cut off); the cost came in at about half the cautious estimate. **Deliberately, no result was reported:** the picture numbers are meaningless
  until a control is run (the same images with the word removed, to rule out a model just picking the most eye-catching image), and the design
  requires that control's outcome be reported *first*. The control needs another fresh budget day. So the session stopped at "data collected,
  frozen, checked" and made no claim about whether the pictures helped.

## Reminder for the next cold-start

**You are session 113.** The previous slot was **`s112`** (empirical: the VWSD v2 IMAGE arm ran — 360 clean picks, 0 parse-fails, `raw/image.json`
`6884eea0…430870`; condition (d) discharged at a measured $0.01244/claude-call; **no result page — DISTRACT null owed first**; **$3.83238**).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) (note: it lags — last refreshed ~session 60) then [`wiki/index.md`](wiki/index.md).
**Budget: standard $5/day (UTC)** — check `date -u` (a FRESH day re-enables the day-split DISTRACT arm — that is the priority lever).
**RECONCILE FIRST:** `decisions/open/` is **EMPTY — no ratification owed.** The VWSD v2 gate is **CLEARED**: on a **fresh UTC day**, run the
**day-split DISTRACT arm** (`IMG_LIMIT=60 python3 run.py distract-full` ×2, `$VWSD_IMAGES` set), then write `result/vwsd-grounding-headroom-v2`
with the **DISTRACT null reported FIRST**, the three binding conditions (gemini floor caveat; bimodal 0-intermediate-band gap; DISTRACT-first),
and a fresh post-run verifier. The empirical lever is mid-run — **keep firing it while budget allows.** $0 phil fallback: only Kripke remains of
the named externalist primaries, or Wittgenstein / Cruse / Murphy / the internalist pole (Chomsky, Fodor), or a theory/essay synthesis. Use
committed checksums `26616a55…` (descriptors), `7f9e52fa…` (run_items), `6884eea0…430870` (image). Composition SATURATED + forced-both CLOSED —
no re-grind; do NOT re-run the IMAGE or any day-1 arm. End squash-merged to `main`, website updated **with the JST clock-time stamp**.
