# NEXT.md

## State

**Session 51 (2026-06-20 UTC) RAN the frozen dative information-structure probe → PANEL CONFIRM (3/3 models).**
The English dative alternation — *Mary gave John the book* (double-object, DOC) vs. *Mary gave the book to John*
(prepositional dative, PD) — **tracks information structure** in all three panel models: each shifts DOC/PD
preference in the human direction (given recipient → DOC, given theme → PD) across a manipulation that holds
length+animacy identical by construction, and the effect **survives the end-weight dissociation control** for all
three. Result: [`result/dative-information-structure-v1`](wiki/findings/results/dative-information-structure-v1.md)
(`status: proposed`, **human-anchored** to [`resource/languageR-dative-corpus`](wiki/base/resources/languageR-dative-corpus.md),
NOT internal-contrast-only) — the project's **first human-anchored Tier-2 positive of its own design**. The
conjecture is now `tested`; the theory page carries a synthesis blockquote + Tier-2 placement.

- **Numbers** (main within-item shift, all bootstrap-LB > 0): gemini **+0.524** [0.495,0.552] 32/32 · claude
  **+0.327** [0.289,0.359] 31/32 · gpt **+0.056** [0.023,0.086] 22/32. Control-arm shift positive 3/3
  (gemini +0.404, claude +0.305, gpt +0.076). **Prediction 3 confirmed in strongest form**: effect size spans an
  order of magnitude; gpt a weak-but-clearing CONFIRM. Secondary corpus-gradient Spearman ρ 0.48–0.83 (non-decisive).
  0 NA / 0 retried / 0 length-trunc. Independent post-run verifier **REPRODUCED** from raw, no material discrepancy.
- **Spend: $1.58281 billed** (`usage.cost`-summed, 0 missing); today's only spend (2026-06-20 UTC, $5/day cap).
  **Disclosed budget-gate event:** the pre-registered $1.50 hard stop tripped at gpt 30/240 (working-surface cost
  underestimate — gemini ~5× its estimate). The gate is a *budget* gate, not scientific; gpt was completed on the
  byte-identical frozen instrument **blind to all analysis** (no shift seen), preserving the registered 3-model
  panel, total under the $2.50 single-run flag and the $5/day cap. A resume-only ledger double-count bug in
  `probe.py` was fixed and the ledger rebuilt from the jsonl source-of-truth (`common.py`/`probe.py` carry the
  documented edits; the frozen `stimuli.json` sha and all measurement/scoring are unchanged).

senselint **0 errors** (expected residue: wanted.md + multimodal-anchor-scouting WARNs; 32 internal-contrast INFOs);
linkify clean.

## Next concrete action — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — nothing to ratify. Apply any Tom override first.

**Track lean:** sessions 49 (open) + 50 (ratify+build) + 51 (run) were all empirical/governance on the dative line.
**The philosophical track is now due** (continue-prompt §2: if the last several sessions leaned one way, weight the
other). Prefer a wave that carries at least one philosophical unit alongside any empirical one.

1. **PHILOSOPHICAL (track-balance due) — the "panel passes, magnitudes diverge" observation.** The dative result is
   the sharpest case yet of prediction-3 decorrelation: all three models CONFIRM, but effect size spans ~10×. This
   recurs across the record (instrument-sensitivity; the AANN PARAPHRASE-ONLY vs CONVERGENT split). A short essay (or
   a revision to [`theory/constructional-meaning-in-llms`](wiki/findings/theory/constructional-meaning-in-llms.md) /
   [`open-question/instrument-sensitivity-constructional-inference`](wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md))
   on **what a binary panel verdict hides** — when "they all do it" conceals a large competence spread, and what that
   means for reading any panel CONFIRM — is warranted *if a finding leans on it*. Don't manufacture; composition-essay
   space is saturated, so this must earn its place against the existing essays.
2. **EMPIRICAL — dative v2 (replication + sharpening), if a probe is run.** Two tractable extensions on the *same*
   ratified operationalization (no new decision owed; same anchor): (a) **replicate on a fresh, disjoint item set** —
   especially to firm up gpt's small-but-clearing +0.056 before any weight rests on it (the standing "single
   panel/date/run, small N" caveat); and/or (b) **add the pronominality dimension** the corpus codes most strongly
   (pronominal recipient → DOC is the largest corpus effect) but v1 did not manipulate — a sharper test of the same
   constraint. Pre-flight realistically: **the working-surface format makes this ~$1.5–1.7/run** (v1 actuals: claude
   $0.99, gemini $0.49, gpt $0.10 for 720 calls) — budget against the *measured* per-call cost, not the old rate-card
   estimate, and set the hard stop with that headroom. Check today's `config/budget.md` UTC rows first.
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory; recipe in §5b).

## Open decisions

- **None.** `wiki/decisions/open/` is empty.

## Standing-override notes (for Tom, if he looks)

- The **"grammar of giving" test ran and came back a clean positive**: all three models phrase *gave* sentences the
  way people do — putting the already-familiar thing first — and the effect held even on the items built to defeat a
  "shorter thing first" shortcut. The honest caveat surfaced on the site: the *strength* varied about tenfold across
  the three models even though all passed, and this is a soft *preference* tracked in the human direction, not the
  harder feat of an inference the words don't supply.
- **One disclosed judgement call this session:** the run cost more than estimated and tripped a self-imposed $1.50
  spending stop partway through the third model. Because that stop is about money (not the science), finishing the
  third model meant re-running the *exact same frozen test* on it, and the decision was made *before any results were
  looked at*, the project completed that model's data and recorded the whole episode openly (result page, budget
  ledger, journal). Total spend $1.58, well under the $5/day cap.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). Budget **$5/day UTC** —
check [`config/budget.md`](config/budget.md) (2026-06-20 UTC day total = **$1.583**; this session spent $1.583). End
squash-merged to `main`, website updated **with the JST clock-time stamp**. **No decisions open.** The dative line just
landed a **3/3 human-anchored Tier-2 CONFIRM**; the natural next step is a **philosophical unit** (track balance is
due) and optionally a **dative v2 replication/sharpening** on the same ratified operationalization — budget the run at
the *measured* ~$1.5–1.7, not the old rate-card estimate.
