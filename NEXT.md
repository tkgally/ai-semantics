# NEXT.md

## ⚠ Budget note — read first

**Standard cap: $5.00/day (UTC).** UTC day **2026-06-26** spent **≈$3.900** (s112 IMAGE $3.83238 + s113 $0.00019 + s114 $0 + **s115 prompt-caching pilot $0.06675**). Only
**≈$1.10 headroom** remains on UTC 2026-06-26 — NOT enough for the DISTRACT arm (≈$3.8); **do not start it today.** A fresh UTC day (**≥ 2026-06-27**) resets to $5 and
re-enables the day-split DISTRACT arm — **that is the priority lever. Check `date -u` FIRST.** Full ledger in [`config/budget.md`](config/budget.md). Check for any newer Tom override too.

## State

**Session 115 (UTC 2026-06-26) — tooling pilot + philosophical ingest, $0.067, no research probe.** Same UTC day as s112–114, headroom too thin for the DISTRACT lever, so a
two-track non-empirical-research session. `decisions/open/` was **EMPTY** at start → no ratification owed; no Tom override. What landed:

1. **PROMPT-CACHING PILOT — ran the $0-stakes measurement the s114-ratified decision authorized.** Run dir [`experiments/runs/2026-06-26-prompt-caching-pilot/`](experiments/runs/2026-06-26-prompt-caching-pilot/results.md).
   Matched cold-vs-cached on one repeated-prefix probe class. **Outputs byte-identical cold vs cached on all 3 models** (output-neutral). MEASURED: **gpt implicit −82.7%** (auto, no flag),
   **gemini explicit `cache_control` −82.7%** (its *implicit* caching did NOT fire via OpenRouter's route, contra the catalog flag), **claude explicit −91.4%** on reads — ~92–99% of the
   prefix cached. **Two decision assumptions overturned:** (a) of the panel only gpt caches implicitly — gemini needs the explicit breakpoint like claude; (b) the saving is **material
   (~83–91%), not the expected small null**, on input-dominated single-token-output probes (it shrinks only on reasoning-heavy gemini runs, where output+reasoning at $9/MT dominate).
   **Action (resolution-authorized, default-OFF):** [`experiments/lib/openrouter.py`](experiments/lib/openrouter.py) gained an opt-in `call(..., cache_prefix=False)` (byte-identical
   body when off → **no existing probe or frozen design perturbed**; verified) + a `CACHE_READ` card + cache-aware `estimated_cost()` (cached tokens discounted; identical to old formula
   when `cached=0`). Pilot result appended to the resolved decision page; lever **not retired** (saving is material). **Adoption is per-probe.**
2. **WITTGENSTEIN 1953 PI INGESTED** → [`source/wittgenstein-1953-philosophical-investigations`](wiki/base/sources/wittgenstein-1953-philosophical-investigations.md) (type source, status received, NOT a human anchor).
   Closes the named `wanted.md` P2 gap + the "not in-repo; characterization" Wittgenstein leg of [`concept/truth-conditional-and-use-meaning`](wiki/base/concepts/truth-conditional-and-use-meaning.md) pole (b).
   Two-route OA: **§§43/7/66/67 primary-direct** (PD German, wittgensteinproject.org); **English §§43/23/66/201/243 carried-via-secondary** (OA SEP); Anscombe translation NOT sourced
   (copyright); §§201/243 at lower secondary-only strength. Coherence pass **independently re-verified all 12 quotes verbatim** against the cited sources. Concept page + `wanted.md` updated.
3. **Coherence pass** (fresh read-only agent): 0 BLOCKERS; 2 SHOULD-FIX (index coverage → added to `wiki/index.md`; gpt/claude raw uncommitted → `gpt_claude_raw.json` written) + 1 NIT (§7
   continuation hedge) — all applied. **senselint 0 errors** (2 expected WARN, 41 INFO); **linkify clean**. **Website + index dashboard updated** (JST 14:09, session 115).

**Note for any future gemini run:** `gemini-3.5-flash` now **rejects** `reasoning:{enabled:false}` and `{effort:none}` (HTTP 400 "Reasoning is mandatory"); only `{effort:minimal}` is accepted.
The project already uses `effort:minimal`, so nothing breaks — but do NOT try to fully suppress gemini reasoning.

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
- **Prompt-caching is now MEASURED and adopted as a default-off opt-in** — do NOT re-run the pilot. The lever is available per-probe (`cache_prefix=True` for gemini/claude; gpt implicit).

## Next concrete action — backlog for the next session

**RECONCILE FIRST (PROTOCOL §2):** `decisions/open/` is **EMPTY** — no ratification owed (apply any Tom override first if one appears). The s108 GO is a pre-run-critic gate already
cleared; honor the three binding conditions above; no further ratification needed there.

**Track lean — recent: 110 PHIL · 111 PHIL · 112 emp-RUN(IMAGE) · 113 tooling · 114 governance · 115 tooling-pilot+PHIL.** The empirical RESEARCH lever is mid-run and overdue to fire
the moment a fresh budget day allows. In rough priority:

1. **IF a FRESH UTC day (≥ 2026-06-27) — the DISTRACT arm, day-split, then the result.** Run `run.py distract-full` over the frozen 120 × 3 (code already in `run.py`; word+phrase
   ablated, "pick the most prototypical/canonical/everyday image"; same images, low detail). ≈$3.8 → split into **two 60-item sub-batches** (`IMG_LIMIT=60 python3 run.py distract-full`
   twice; each under the $2.50 flag), `$VWSD_IMAGES` set to the re-fetched zip (Drive id `15ed8TXY9Pzk68_SCooFm7AfkeFtCd16Q`, sha `b9f2f1e1…af8f`; **keep out of git**). Then write
   [`result/vwsd-grounding-headroom-v2`] — **DISTRACT null reported and credited FIRST**, then the binned image-rescue interaction, honoring all **three binding conditions** + a fresh
   independent **post-run verifier**; promote the conjecture [`distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   only as the evidence warrants. `analyze.py` already computes every result section once `raw/distract.json` exists. *(Optional: the DISTRACT prompt re-sends a fixed instruction prefix
   per item — `cache_prefix=True` on the gemini/claude calls would now cut input cost, but the bill is image-token-dominated so the saving is modest; not required.)*
2. **PHILOSOPHICAL fallback ($0), only if still budget-blocked.** **Avoid the saturated reference/internalism cell.** Live, *non-reference* phil primaries worth ingesting (OA permitting):
   **Cruse 1986 / Murphy 2003** lexical-semantics (likely book-walled like Goldberg/Croft — carry via author/secondary if so); or the **Tarski/Davidson/Montague** truth-conditional-pole
   primaries (the remaining `wanted.md` legs of the truth-conditional gap, now that Frege + Wittgenstein are both in-repo). A non-reference theory/essay synthesis is also fine — but the
   use-theoretic-method region is now well-covered (concept + theory pages + the Wittgenstein primary), so prefer a genuinely under-covered region.
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

- **NONE OPEN.** `prompt-caching-repeated-prefix-probes` (opened s113, ratified s114) had its authorized **pilot run this session (s115)** and a "Pilot result" addendum appended to the
  resolved page; **42 ratified to date.** Full changelog [`wiki/decisions/resolved/index.md`](wiki/decisions/resolved/index.md).

## Standing-override notes (for Tom, if he looks)

- Session 115 spent **≈$0.067** (UTC day 2026-06-26; day total ≈$3.900 of $5.00).
- Plain-language: the budget for today was mostly used by the picture experiment two sessions ago, so no new experiment ran. The session ran the free cost-saving trial you'd asked for
  before switching the service's cheaper re-read pricing on — and it was a pleasant surprise: the saving is **large (about 83–91%) on the project's cheap one-word-answer runs**, not the
  small amount we'd braced for, and the models' answers came back identical character-for-character. So the discount was switched on as an **optional, off-by-default** setting that leaves
  every existing experiment untouched. (One wrinkle measurement caught: one model the project expected to discount automatically actually needs to be asked explicitly.) The session also
  read and recorded the founding philosophy text behind the project's whole method — Wittgenstein's "a word's meaning is its use" — quoting it from a public-domain edition. The picture
  experiment's word-removed control is still the next spending step and waits for a fresh budget day.

## Reminder for the next cold-start

**You are session 116.** The previous slot was **`s115`** (tooling pilot + PHIL, $0.067: ran the authorized prompt-caching pilot → caching adopted as a **default-off** `cache_prefix`
opt-in [byte-identical when unused] + cache-aware estimate; ingested **Wittgenstein 1953 PI** = the use-pole founding primary). Before s115 was **`s114`** (governance + maintenance, $0).
Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then
[`wiki/index.md`](wiki/index.md). **Budget: standard $5/day (UTC)** — check `date -u` (a FRESH day ≥ 2026-06-27 re-enables the day-split DISTRACT arm — that is the priority lever).
**RECONCILE FIRST:** `decisions/open/` is **EMPTY** — no ratification owed. The VWSD v2 gate is **CLEARED**: on a **fresh UTC day**, run the **day-split DISTRACT arm** (`IMG_LIMIT=60
python3 run.py distract-full` ×2, `$VWSD_IMAGES` set), then write `result/vwsd-grounding-headroom-v2` with the **DISTRACT null reported FIRST**, the three binding conditions (gemini floor
caveat; bimodal 0-intermediate-band gap; DISTRACT-first), and a fresh post-run verifier. Use committed checksums `26616a55…` (descriptors), `7f9e52fa…` (run_items), `6884eea0…430870`
(image). **gemini reasoning can no longer be fully suppressed — use `{effort:minimal}`.** Composition SATURATED + forced-both CLOSED + reference-cell SATURATED — no re-grind; do NOT
re-run the IMAGE/day-1/caching-pilot. End squash-merged to `main`, website updated **with the JST clock-time stamp**.
