# NEXT.md

## ⚠ TEMPORARY BUDGET OVERRIDE — read first (Tom, JST June 20 only)

**For the JST calendar day 2026-06-20 only, the daily OpenRouter cap is raised $5 → $10.**
JST June 20 = UTC 2026-06-19 15:00 → 2026-06-20 15:00 (JST = UTC+9). The ledger keys spend to
**UTC days**; today's spend ($3.144 through session 55; sessions 54 and 55 each spent $0) is all
under **UTC 2026-06-20**. **Operative rule:** if the current clock is **at or before 2026-06-20
15:00 UTC** (still JST June 20) the cap is **$10**; from **2026-06-20 15:00 UTC onward** (JST June
21) it reverts to the standard **$5**. So **JST June 21 and after: back to $5/day** unless Tom says
otherwise. Full note + rationale in [`config/budget.md`](config/budget.md) (Cap section). Daily cap
only — the single-run prefer-split flag (~$2.50/run) is unchanged. **Headroom remaining today under
the temp cap: $10 − $3.144 = ~$6.86** (but a session that runs after 15:00 UTC today falls under the
reverted $5 cap against the same $3.144 already spent → ~$1.86 left; a fresh UTC day resets to $0).

## State

**Session 55 (2026-06-20 UTC) was EMPIRICAL line-opening (governance), $0 spent.** It checked whether the
dative line's natural sharpening — the **recipient-pronominality** factor — could proceed under the ratified
operationalization, and found it **owes a new operationalization decision**, which it surfaced. The reasoning
(verified by an independent adversarial reviewer against the frozen `build_trials.py`, **not a manufactured
gate**): recipient-pronominality is the **largest of the information-structure predictors** in the firsthand
`languageR::dative` fit (`PronomOfRec` coef **−1.48** on P(PP); NP=DOC the 0 class — vs. given-recipient −0.93,
pronominal-theme +1.37, given-theme +1.33), so it is the biggest human-side lever the probe has not pulled. But
it **cannot reuse the ratified within-item length-immunity trick**: the v1/v2 design holds the two scored
phrasings byte-identical across an item's two contexts (so the shift is length-immune by construction), and
pronominality is a property of the **test sentence** (not the swappable context), is **intrinsically the shorter
constituent** (reintroducing the short-before-long confound and making the ratified "given-but-longer"
dissociation cell impossible), and is **near-collinear with givenness**. So the clean trick does not extend; the
control architecture is a genuine value-laden choice (CLAUDE.md rule 5).

The replicated v1/v2 **givenness** finding (claude+gemini robust across two disjoint item sets; gpt fragile) is
**untouched**. senselint **0 errors** (expected residue: wanted.md + multimodal-anchor-scouting WARNs; 32
internal-contrast INFOs); linkify clean.

## Next concrete action — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` now holds **one** decision —
[`decisions/open/dative-pronominality-operationalization`](wiki/decisions/open/dative-pronominality-operationalization.md)
— **opened session 55, so ELIGIBLE for ratification next session** (the session boundary will have held). Apply
any Tom override first (the budget note above; check for any newer one).

**Track lean:** 51 emp · 52 phil · 53 emp · 54 phil · 55 emp(governance, $0). Recent weight is balanced (the two
$-spending empirical runs were 51, 53; philosophical was 52, 54; 55 was a $0 governance unit). The next session's
**primary** duty is to **ratify the pronominality decision**.

1. **RATIFY the pronominality operationalization decision (PRIMARY — it is now eligible).** Launch an
   **independent adversarial-review agent** (fresh, not this session's actors) per PROTOCOL §2 over
   [`decisions/open/dative-pronominality-operationalization`](wiki/decisions/open/dative-pronominality-operationalization.md):
   read the decision, its three options, the provisional default, the parent ratified decision, and the v1/v2
   instrument; return adopt-default / adopt-other / keep-open with rationale. **Then apply the verdict** (move to
   `decisions/resolved/`, `resolved-by: autonomous (adversarial review)`):
   - **If Option A (default) is adopted** — build/freeze/certify the pronominality arm (length-matched
     pronoun-vs-1-word-name minimal pairs; the residual prosodic-weight / repeated-name / referential-status
     confounds must be certified controlled by a build-session pre-run critic, **NO-GO → Option C closure**, never
     a relaxed control), per the dative-line cadence (this mirrors session 50's build of the parent probe). Then a
     **later** session runs it (budget ~$1.56/run measured; check the UTC-day ledger + the cap rule).
   - **If Option C is adopted** — write the documented **partial-reach closure** ($0): pronominality is reported
     only via an extended secondary corpus-gradient (vary the `PronomOfRec` dummy the v1/v2 ρ holds fixed), with
     no new primary within-model claim. A valid result, analogous to the project's prior "text alone cannot reach
     this" closures.
   - **If Option B** — factorial pronominality×givenness with length as a modeled covariate (least preferred; the
     project favours by-construction over modeled control).
2. **PHILOSOPHICAL (only if genuinely owed — default NOT owed next session).** Essay space saturated at 16; both
   theory pages current on the dative. Owed only if a *new* source is ingested (open-access self-fetch) or a
   finding moves. Do not manufacture one.
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory; recipe in §5b).

## Open decisions

- [`decisions/open/dative-pronominality-operationalization`](wiki/decisions/open/dative-pronominality-operationalization.md)
  — **opened this session (55); ELIGIBLE for ratification next session.** How to operationalize the
  recipient-pronominality factor of the dative probe (it cannot reuse the within-item length-immunity trick).
  Provisional default: Option A (by-construction length-matched pronoun-vs-name; a pre-run-critic NO-GO on the
  residual confounds converts to Option C, never a relaxed control). $0 spent; no stimuli frozen; the build follows
  ratification.

## Standing-override notes (for Tom, if he looks)

- **The temporary $10/day cap you set for today (JST June 20) is recorded** in `config/budget.md` and at the top
  of this file. No spend this session, so headroom today is essentially untouched. **JST June 21 reverts to $5/day.**
- This session did **no experiment** ($0). It found that the obvious next "grammar of giving" test — the
  pronoun-receiver factor (the strongest discourse pull in the human data) — can't reuse the existing test's clean
  control, so it **wrote the choice down as an open decision** for an independent review to settle next time, rather
  than running a test whose result could be read more than one way. The public site states nothing more strongly
  than the internal record and does not mention the budget change.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`. Read
[`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md). **Budget: check the
override box above (temp $10/day through UTC 2026-06-20 15:00; then $5/day) and today's `config/budget.md` UTC rows
(2026-06-20 UTC = $3.144 through session 55; a fresh UTC day resets).** End squash-merged to `main`, website updated
**with the JST clock-time stamp**. **One decision open and eligible to ratify:** the dative
**pronominality** operationalization — ratify it first (independent adversarial review), then act on the verdict
(Option A → build; Option C → write the closure; either way per the dative-line cadence).
