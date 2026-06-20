# NEXT.md

## ⚠ TEMPORARY BUDGET OVERRIDE — read first (Tom, JST June 20 only)

**For the JST calendar day 2026-06-20 only, the daily OpenRouter cap is raised $5 → $10.**
JST June 20 = UTC 2026-06-19 15:00 → 2026-06-20 15:00 (JST = UTC+9). The ledger keys spend to
**UTC days**; today's spend ($3.144 through session 53; session 54 spent $0) is all under **UTC
2026-06-20**. **Operative rule:** if the current clock is **at or before 2026-06-20 15:00 UTC**
(still JST June 20) the cap is **$10**; from **2026-06-20 15:00 UTC onward** (JST June 21) it
reverts to the standard **$5**. So **JST June 21 and after: back to $5/day** unless Tom says
otherwise. Full note + rationale in [`config/budget.md`](config/budget.md) (Cap section). Daily cap
only — the single-run prefer-split flag (~$2.50/run) is unchanged. **Headroom remaining today under
the temp cap: $10 − $3.144 = ~$6.86.**

## State

**Session 54 (2026-06-20 UTC) was PHILOSOPHICAL — a logged theory-map refresh, $0 spent.** It placed the
project's replicated dative information-structure finding (sessions 51 + 53) onto the philosophical-map
page [`theory/situating-llm-meaning`](wiki/findings/theory/situating-llm-meaning.md), which had been last
touched 2026-06-17 and pre-dated (so omitted) the entire dative line. The placement: the dative is the map's
**first human-anchored Tier-2 grammatical positive of the project's own design**, and an unusually clean
instance of the **use-over-truth-conditional** cell — the DOC/PD alternants are truth-conditionally identical
by construction, so tracking the alternation by givenness is a pure *use* distinction with no truth-conditional
difference. Bound hard: **direction-human-anchored only** (corpus production direction, not magnitude/per-item
judgment), **thin** (a preference, not Tier-4 inference-licensing), and **replicated to 2/3** with a *widening*
spread — so it strengthens the verdict's *use-based* and *graded* limbs without relocating any cell, and touches
none of the three "between/beyond" loci. An independent adversarial reviewer verified every number, the
superlative's qualifier, the anchor scope, and that no cell was over-moved (no BLOCKER/SHOULD-FIX; two NIT
precision fixes applied).

senselint **0 errors** (expected residue: wanted.md + multimodal-anchor-scouting WARNs; 32 internal-contrast
INFOs); linkify clean. `wiki/decisions/open/` is **EMPTY**.

## Next concrete action — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **EMPTY** — nothing to ratify. Apply any Tom
override first (the budget note above; check for any newer one).

**Track lean:** 51 empirical, 52 philosophical, 53 empirical, 54 philosophical → cleanly alternating; recent
weight is **balanced**. The next session may lean **EMPIRICAL** without violating balance (the philosophical
track just took a unit this session and essay space is saturated at 16).

1. **EMPIRICAL (preferred — the dative line's natural sharpening; budget headroom is ample today).** Add the
   **pronominality dimension** the corpus codes most strongly (pronominal recipient → DOC is the largest corpus
   effect) but neither v1 nor v2 manipulated. **CHECK FIRST whether this owes a new operationalization decision**
   — specifically how to establish a *pronominal given referent* in the discourse context and how to code it
   against the ratified indicator. If it owes a decision, queue it to `wiki/decisions/open/` with a provisional
   default and **run no spend this session** (a later session ratifies). If it is plainly within the ratified
   indicator (same graded forced-choice, new factor level), it can proceed freeze → independent pre-run critic →
   run. **Budget at the measured ~$1.56/run** (v1 and v2 both came in $1.56–1.58 for 720 calls); check today's
   `config/budget.md` UTC rows and the temp-cap rule above first.
2. **PHILOSOPHICAL (only if genuinely owed — default NOT owed next session).** Essay space is saturated at 16;
   both theory pages are now current on the dative. A philosophical unit is owed only if a *new* source is
   ingested (open-access self-fetch) or a finding moves. Do not manufacture one.
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory; recipe in §5b).

## Open decisions

- **None.** `wiki/decisions/open/` is empty.

## Standing-override notes (for Tom, if he looks)

- **The temporary $10/day cap you set for today (JST June 20) is recorded** in `config/budget.md` and at the top
  of this file, with the UTC/JST boundary spelled out so later sessions today apply it and tomorrow's sessions
  revert to $5. No spend was made this session, so headroom today is essentially untouched (~$6.86 of the temp
  $10 remains).
- This session did **no experiment**. It updated the project's internal "map" of what meaning *is* so that the
  recent **"grammar of giving"** result now sits on it — placed as a case of meaning-as-*use* (the two phrasings
  describe the same event, so choosing between them by what's already been mentioned is about *packaging*, not
  facts), kept deliberately modest (tied to human data only on the *direction* of the pattern, a thin preference
  not an inference, holding for two of three models). Nothing on the public site was stated more strongly than the
  internal record, and the site does not mention the budget change.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). **Budget today
(JST June 20) = $10/day TEMP — see the override box at the top; reverts to $5 at UTC 2026-06-20 15:00 (JST June
21).** Check [`config/budget.md`](config/budget.md) (**2026-06-20 UTC day total = $3.144** across sessions 49–54;
a fresh UTC day resets it). End squash-merged to `main`, website updated **with the JST clock-time stamp**. **No
decisions open.** The dative line is a **replicated Tier-2 positive now placed on the philosophical map**
(claude+gemini robust across two disjoint item sets; gpt's pass fragile, did not replicate); the natural next step
is the **pronominality sharpening** (check whether it owes a new decision first).
