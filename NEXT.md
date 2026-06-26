# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-26** spent **$3.83276** (s112 VWSD v2 IMAGE arm $3.83238 + s113 $0.00019 MCP test + s114 $0). **Only ≈$1.17
headroom remains on UTC 2026-06-26 — NOT enough for the DISTRACT arm (≈$3.8); do not start it today.** A fresh UTC day (**≥ 2026-06-27**) resets to $5 and
re-enables the day-split DISTRACT arm — **that is the priority lever. Check `date -u` FIRST.** Full ledger in [`config/budget.md`](config/budget.md). Check for any
newer Tom override too.

## State

**Session 114 (UTC 2026-06-26) — governance + maintenance, $0, no probe.** Same UTC day as s112/s113, headroom too thin for the empirical lever, so a $0 session.
`decisions/open/` held **ONE** eligible entry at start → **RATIFIED**; no Tom override. What landed:

1. **RECONCILE — `prompt-caching-repeated-prefix-probes` RATIFIED (ADOPT THE DEFAULT unchanged).** Opened s113 (Tom-directed), eligible this session
   (cross-session boundary held). An independent fresh-agent adversarial review adopted the provisional default as written: **keep the probe harness on the
   cold-read path** ([`experiments/lib/openrouter.py`](experiments/lib/openrouter.py) UNCHANGED); gate any caching behind a **$0-stakes matched cold-vs-cached
   pilot** (byte-identical outputs + measured saving) before adoption; implicit-caching gemini/gpt first, Anthropic `cache_control` only if its share justifies it;
   if the saving is small (the expected gemini case — output+reasoning at $9/MT dominate, caching touches only input), record the null and retire. **Code-checked
   against openrouter.py:** `billed_cost()` sums the API-returned `usage.cost` (cache line items already folded in → recorded figure stays correct);
   `RATE_CARD`/`estimated_cost()` model only `(prompt, completion)`, so a cached run would be **over-estimated** until a cache-aware term is added. Anti-cheat PASS
   (no result depends on it). Moved to [`wiki/decisions/resolved/prompt-caching-repeated-prefix-probes.md`](wiki/decisions/resolved/prompt-caching-repeated-prefix-probes.md);
   index count **41 → 42**; `decisions/open/` now **EMPTY**.
2. **Refreshed [`wiki/executive-summary.md`](wiki/executive-summary.md)** (it had lagged at session 92 — ~20 sessions behind): new top entry stamped session 114 +
   a plain-language catch-up of the 93–113 arc (the forked-word/SemEval line, the picture-and-words VWSD line with its DISTRACT control still owed, and the
   externalist-primaries reading). No finding changed.
3. **Website + index dashboard updated**; harnesses UNCHANGED.

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

- **Composition / order-sensitive-composition / capability-split line is SATURATED — do NOT frame a new probe there.** (s99 verdict.)
- **Forced-both lexical line is CLOSED at R1 pending a NEW resource** ([`wanted.md`](wiki/base/wanted.md) P3; SemEval pun corpus ratified s93 as a *partial* anchor —
  co-activation only, no in-item balance, so Q1-ii dominance step still owed).
- **VWSD v2 day-1 + IMAGE arm are DONE, FROZEN** — do **not** re-generate descriptors / re-draw N=120 / re-run the IMAGE or any day-1 arm.
- **The reference / internalism-vs-externalism philosophical cell is now effectively SATURATED** (confirmed s114): five+ cross-referential essays
  ([`reference-as-premise-bound`](wiki/findings/essays/reference-as-premise-bound.md), [`reference-denials-disunified`](wiki/findings/essays/reference-denials-disunified.md),
  [`stereotype-without-the-expert`](wiki/findings/essays/stereotype-without-the-expert.md), [`inherited-not-constituted`](wiki/findings/essays/inherited-not-constituted.md))
  plus the concept and `situating-llm-meaning` theory pages already cover the membership antecedent, the "which role" sharpening, and the three-pole denial
  disunity. **A new reference essay would be redundant padding** — weight $0 phil work toward a *different* region (see fallback below).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `decisions/open/` is **EMPTY** — no ratification owed (apply any Tom override first if one appears). The s108 GO is a
pre-run-critic gate, not a `decisions/open/` entry — already cleared; honor the three binding conditions above; no further ratification needed there.

**Track lean — recent: 108 emp-GATE+PHIL · 109 PHIL · 110 PHIL · 111 PHIL · 112 emp-RUN(IMAGE) · 113 tooling · 114 governance+maintenance.** The empirical lever is
mid-run and should keep firing the moment a fresh budget day allows. In rough priority:

1. **IF a FRESH UTC day (≥ 2026-06-27) — the DISTRACT arm, day-split, then the result.** Run `run.py distract-full` over the frozen 120 × 3 (code already in
   `run.py`; word+phrase ablated, "pick the most prototypical/canonical/everyday image"; same images, low detail). ≈$3.8 → split into **two 60-item sub-batches**
   (`IMG_LIMIT=60 python3 run.py distract-full` twice; each under the $2.50 flag), `$VWSD_IMAGES` set to the re-fetched zip (Drive id
   `15ed8TXY9Pzk68_SCooFm7AfkeFtCd16Q`, sha `b9f2f1e1…af8f`; **keep out of git**). Then write [`result/vwsd-grounding-headroom-v2`] — **DISTRACT null reported and
   credited FIRST**, then the binned image-rescue interaction, honoring all **three binding conditions** + a fresh independent **post-run verifier**; promote the
   conjecture [`distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md) only as the evidence
   warrants (stays `proposed` unless the result clears the gate). `analyze.py` already computes every result section once `raw/distract.json` exists.
2. **PHILOSOPHICAL fallback ($0), only if still budget-blocked.** **Avoid the saturated reference/internalism cell** (see do-not-re-grind note). Live, *non-reference*
   phil primaries worth ingesting (open-access permitting; never fabricate around an unreachable fetch): **Wittgenstein 1953** P2 (meaning-as-use, ungrounds
   [`concept/truth-conditional-and-use-meaning`](wiki/base/concepts/truth-conditional-and-use-meaning.md) pole (b)); **Cruse 1986 / Murphy 2003** lexical-semantics
   P2; the **internalist** primaries **Chomsky 2000 / Fodor 1987** *only if* they add something the saturated reference essays don't already carry. A theory/essay
   synthesis on a non-reference region (the constructional/lexical empirical findings; the use-theoretic methodological bet) is also fine.
3. **Optional, low-priority ($0): the prompt-caching pilot** the s114-resolved decision authorizes — a scoped, $0-stakes matched cold-vs-cached pair on one
   repeated-prefix probe class to measure the real saving + confirm byte-identical outputs. Not urgent; not a correctness gate; do it only if no higher-value unit
   is tractable.
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `prompt-caching-repeated-prefix-probes` (opened s113) was **ratified s114** (ADOPT DEFAULT; harness unchanged; pilot-before-adopt). **42 ratified to
  date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Session 114 spent **$0** (UTC day 2026-06-26). A short governance + housekeeping session.
- Plain-language: the budget for today was already mostly used by the picture experiment two sessions ago, so no experiment ran. The session settled the
  money-saving question you flagged last session (whether to use the service's cheaper re-read pricing): an independent review said **leave the machinery as it is
  for now**, and only switch caching on after a free trial proves it changes no model answer and actually saves a worthwhile amount — likely small on the costliest
  runs, where the bill is the model's reasoning, not the repeated instructions. The spending records stay correct either way. The session also brought the
  plain-language summary, which had fallen ~20 sessions behind, back up to date. The picture experiment's control (the same images with the word removed) is still
  the next spending step and waits for a fresh budget day.

## Reminder for the next cold-start

**You are session 115.** The previous slot was **`s114`** (governance + maintenance, $0: ratified `prompt-caching-repeated-prefix-probes` = ADOPT DEFAULT/harness
unchanged; refreshed the executive summary from its session-92 lag; updated the website + index dashboard). Before s114 was **`s113`** (Tom-directed tooling,
$0.00019: OpenRouter MCP eval + stale `RATE_CARD` fix + opened the prompt-caching decision). Before s113 was **`s112`** (VWSD v2 IMAGE arm ran — 360 clean picks,
`raw/image.json` `6884eea0…430870`; **no result page — DISTRACT null owed first**; **$3.83238**).

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md)
(now refreshed this session) then [`wiki/index.md`](wiki/index.md). **Budget: standard $5/day (UTC)** — check `date -u` (a FRESH day ≥ 2026-06-27 re-enables the
day-split DISTRACT arm — that is the priority lever). **RECONCILE FIRST:** `decisions/open/` is **EMPTY** — no ratification owed. The VWSD v2 gate is **CLEARED**: on a
**fresh UTC day**, run the **day-split DISTRACT arm** (`IMG_LIMIT=60 python3 run.py distract-full` ×2, `$VWSD_IMAGES` set), then write
`result/vwsd-grounding-headroom-v2` with the **DISTRACT null reported FIRST**, the three binding conditions (gemini floor caveat; bimodal 0-intermediate-band gap;
DISTRACT-first), and a fresh post-run verifier. The empirical lever is mid-run — **keep firing it while budget allows.** $0 phil fallback: **avoid the saturated
reference/internalism cell**; prefer a non-reference primary (Wittgenstein / Cruse / Murphy) or a non-reference theory/essay synthesis. Use committed checksums
`26616a55…` (descriptors), `7f9e52fa…` (run_items), `6884eea0…430870` (image). Composition SATURATED + forced-both CLOSED + reference-cell SATURATED — no re-grind;
do NOT re-run the IMAGE or any day-1 arm. End squash-merged to `main`, website updated **with the JST clock-time stamp**.
