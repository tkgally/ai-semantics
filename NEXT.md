# NEXT.md

## State

**Session 53 (2026-06-20 UTC) was EMPIRICAL — dative v2, a fresh-item REPLICATION; spent $1.561.**
Re-ran the session-51 dative information-structure probe
([`result/dative-information-structure-v1`](wiki/findings/results/dative-information-structure-v1.md), 3/3 CONFIRM)
on a **fully disjoint** 32+12-item set (0 shared subj/rec/thm items, 0 shared contexts), under the **same ratified
operationalization** ([`decisions/resolved/dative-anchor-and-indicator`](wiki/decisions/resolved/dative-anchor-and-indicator.md)) —
no new decision owed. Result: [`result/dative-information-structure-v2`](wiki/findings/results/dative-information-structure-v2.md),
**panel CONFIRM but 2/3, not 3/3**.

- **claude (+0.325 vs v1 +0.327) and gemini (+0.500 vs +0.524) reproduced almost exactly** (both 32/32, both survive
  the end-weight control 12/12 → CONFIRM). **gpt's v1 CONFIRM did NOT replicate**: shift fell to **+0.018, CI
  [−0.011, 0.047] includes 0 → WEAK** (15/32 — a coin flip). The order-of-magnitude effect-size **spread reproduced
  and WIDENED** (gemini-to-gpt ≈9×→≈27×); the spread did **not** compress.
- This fires revision trigger (c) of [`essay/concordant-verdict-hides-spread`](wiki/findings/essays/concordant-verdict-hides-spread.md)
  in the **strengthening** direction → **logged revision, status `draft`→`revised`** (v1's concordant 3/3 demonstrably
  hid a fragile member; the "wants replication" caveat is **discharged**). Theory page, v1 back-pointer, index,
  exec-summary all updated.
- Instrument frozen (`stimuli.json` sha `32d3e622…cddbf9b`; certification PASS), **independent fresh-agent pre-run
  critic GO** + **independent post-run verifier REPRODUCED** from raw (billed exact, 720/720 doc_pref rechecked).
  0 NA/retry/trunc. Hard stop $2.00 never tripped.
- **Spend: $1.561** (claude $0.979 + gemini $0.471 + gpt $0.105 + liveness $0.005). **Day total 2026-06-20 UTC
  (sessions 49–53) = $3.144 of $5.00.**

senselint **0 errors** (expected residue: wanted.md + multimodal-anchor-scouting WARNs; 32 internal-contrast INFOs);
linkify clean.

## Next concrete action — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — nothing to ratify. Apply any Tom override first.

**Track lean:** sessions 49–51 empirical, 52 philosophical, 53 empirical → recent weight is **heavily empirical**.
Per the charter's track-balance rule, **the next session should lean PHILOSOPHICAL** — *but only if a unit is
genuinely owed* (do not manufacture; essay space is saturated at 16, and essay-16 was just revised, not re-opened).

1. **PHILOSOPHICAL (preferred by track-balance, only if real).** The v2 result is fresh evidence the philosophical
   track can metabolize *without a new essay*: candidate units, pick the one genuinely owed —
   (a) a **logged refresh** of [`theory/situating-llm-meaning`](wiki/findings/theory/situating-llm-meaning.md) if the
   now-*replicated-but-2/3* dative status changes where the finding sits on the map (the
   [`theory/constructional-meaning-in-llms`](wiki/findings/theory/constructional-meaning-in-llms.md) box was already
   updated this session — check whether the situating page needs the same); or
   (b) if — and only if — the "fragile vs robust panel membership, revealed by replication" idea is a *distinct*
   contribution from essay-16's "carry the spread" (it may not be), a short open-question page rather than a new
   essay. **Default: no new essay; a logged theory-refresh at most.**
2. **EMPIRICAL (the dative line's natural sharpening, if the next session leans empirical instead).** Add the
   **pronominality dimension** the corpus codes most strongly (pronominal recipient → DOC is the largest corpus
   effect) but neither v1 nor v2 manipulated. **Check first whether this owes a new operationalization decision**
   (how to establish a *pronominal* given referent in the discourse context, and its coding) — if so, queue it to
   `wiki/decisions/open/` with a provisional default and run no spend this session; if it is plainly within the
   ratified indicator (same graded forced-choice, new factor level), it can proceed freeze→critic→run. **Budget at
   the measured ~$1.56/run** (v1 and v2 both came in $1.56–1.58 for 720 calls); check today's `config/budget.md`
   UTC rows first.
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory; recipe in §5b).

## Open decisions

- **None.** `wiki/decisions/open/` is empty.

## Standing-override notes (for Tom, if he looks)

- This session **re-ran the "grammar of giving" test on a completely fresh set of sentences** (44 new scenarios,
  nothing shared with the first run). The two stronger models repeated their result almost exactly; the **weakest
  model's earlier pass did not hold up** — on the new sentences its effect shrank to nearly zero. So the overall
  verdict is still a pass, but **two of three** rather than all three, and the gap between strongest and weakest grew
  **wider**. This is the previous session's reading rule (report each model's size; don't read "they all pass" as
  "they all pass equally") earning its keep: the original "all three pass" quietly contained one fragile member.
- Two independent fresh-agent reviewers were used as required (one certified the test before any money was spent;
  one re-computed every number from the raw data afterward — both clean). Spend $1.56, within the daily limit.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). Budget **$5/day UTC** —
check [`config/budget.md`](config/budget.md) (**2026-06-20 UTC day total = $3.144** across sessions 49–53; a fresh UTC
day resets it). End squash-merged to `main`, website updated **with the JST clock-time stamp**. **No decisions open.**
The dative line is now a **replicated Tier-2 positive** (claude+gemini robust across two disjoint item sets; gpt's
pass fragile, did not replicate); the natural next steps are a **philosophical track-balance unit** (only if owed) or
the **pronominality sharpening** (check whether it owes a new decision first).
