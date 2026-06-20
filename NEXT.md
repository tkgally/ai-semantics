# NEXT.md

## ⚠ Budget note — read first

**The temporary $10/day cap (Tom, JST June 20 only) is expiring by the clock.** JST June 20 = UTC
2026-06-19 15:00 → 2026-06-20 15:00. **Operative rule:** at or before **2026-06-20 15:00 UTC** the
cap is $10; from **2026-06-20 15:00 UTC onward (JST June 21) it reverts to the standard $5/day**
unless Tom says otherwise. **Today's UTC-day spend (2026-06-20) is $3.475** (sessions 51 $1.583 + 53
$1.561 + 57 $0.331). A **fresh UTC day (2026-06-21+) resets to $0 at the standard $5/day cap.** The
single-run prefer-split flag (~$2.50/run) is unchanged. Full note in [`config/budget.md`](config/budget.md).

## State

**Session 57 (2026-06-20 UTC) was EMPIRICAL, a spending probe ($0.331 billed) — a real finding.** It
cashed the project's long-standing IOU: the **Scivetti CxNLI answer-key probe**
([`result/scivetti-cxnli-answer-key-v1`](wiki/findings/results/scivetti-cxnli-answer-key-v1.md)).
For the first time the panel was scored against the **actual human-annotated** Scivetti items (not
the project's synthetic minimal pairs), on the **full** 390-item Exp-1 base task across all 8
constructions, NLI labels vs per-item gold vs the ≈0.90 native-speaker baseline. Verdict: **2/3
models match the human baseline** (claude 0.903 / gemini 0.915, CIs cover 0.90; gpt-5.4-mini 0.813,
BELOW), and the **one cross-model failure is the phrasal scalar `let-alone`** (0.46–0.67, near 3-way
chance) — not any argument-structure construction. This **discharges
[`result/cxnli-distinction-divergence-v1`](wiki/findings/results/cxnli-distinction-divergence-v1.md)
limit 1** (full base set, not a 20-item subsample). Add-vs-cancel base accuracy is small and
sign-inconsistent → recorded as *consistent-with, not a test of*,
[`conjecture/constructional-monotonicity-asymmetry`](wiki/findings/conjectures/constructional-monotonicity-asymmetry.md)
(first empirical touch). Ran under the **already-ratified** Scivetti anchor + the
`constructional-divergence-operationalization` decision — **no new decision owed** (independent
pre-run critic GO + independent post-run verifier REPRODUCED, both fresh agents). senselint **0
errors** (expected residue: wanted.md + multimodal-anchor-scouting WARNs; 32 internal-contrast
INFOs); linkify clean; open-decisions dir **empty**.

## Next concrete action — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. Apply
any Tom override first (the budget note above; check for any newer one).

**Track lean.** 51 emp($) · 52 phil · 53 emp($) · 54 phil · 55 emp(gov,$0) · 56 emp(gov,$0) · 57
emp($). The empirical track has now produced a fresh finding; the **philosophical track has gone
quiet since session 54** (two governance + one empirical-finding session since). **Weight the next
session toward PHILOSOPHICAL**, with the let-alone empirical follow-up as the alternative if a
revision is genuinely owed and tractable.

1. **PHILOSOPHICAL (preferred) — a genuine revision-trigger check on the let-alone finding.** The
   new result is a *clean dissociation*: the panel reaches human NLI accuracy on argument-structure
   constructions (who-did-what-to-whom) but fails a **scalar / pragmatic phrasal construction**
   (`let-alone`) at near-chance, consistently across 3 models. Does this exercise a revision trigger
   on [`theory/constructional-meaning-in-llms`](wiki/findings/theory/constructional-meaning-in-llms.md)
   (the ladder currently frames the easy/hard split as add-vs-cancel and unambiguous-vs-divergent —
   does an *argument-structure-vs-scalar-phrasal* split add a new axis?) or on an essay (e.g. the
   undischargeable-negative taxonomy, or the distributional-shadow discipline — is scalar/pragmatic
   inference a place where the distribution under-determines)? **If it fits cleanly with no revision
   owed, say so and do the empirical unit instead — do not manufacture an essay.**
2. **EMPIRICAL (alternative) — pin down the let-alone failure (same ratified anchor, no new
   decision).** The discriminating signal is single-run, zero-shot, one framing. A cheap follow-up
   under the *same* ratified Scivetti anchor: re-run `let-alone` (and a near-chance comparison
   construction) under an **alternate framing** (few-shot, or a working-surface/CoT format) to test
   whether the failure is robust competence-absence or a zero-shot/instrument artifact. n is small
   (24 let-alone items) — consider widening with the Exp-1 train split if a clean disjoint set
   exists. Pre-flight ~ $0.1–0.3; follow the cadence (frozen → pre-run critic GO → probe → post-run
   verifier). **Note:** a framing *change* is a stimulus/instrument extension under the ratified
   answer-key operationalization (precedent: the relational-line K/pair/depth extensions) — but if
   it would alter *what is scored against the human gold*, surface a `decisions/open/` page first.
3. **Other live forward bets (need setup, not one-session-runnable):**
   [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   (needs a fine-polysemy image set, not in-repo) and
   [`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md)
   (needs a new frequency-matched-pair anchor decision opened first — a line-opening, $0 unit).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**None.** (No decision was opened or left open this session.)

## Standing-override notes (for Tom, if he looks)

- **Your temporary $10/day cap for JST June 20 is essentially used up by the clock; JST June 21
  reverts to $5/day.** This session spent **$0.331** of it; UTC-day total $3.475 of $10.
- This session ran a real experiment: it graded the three models against a **human answer key** of
  390 grammar puzzles (the long-deferred test). Two of three reached the ~90% native-speaker score;
  the smallest model and — for *all three* — the "let alone" construction fell well short. The site
  states the contamination caveat plainly (public items → failures, not matches, are the robust
  signal), refers to no monitor, and reports nothing more strongly than the wiki.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions
`CLAUDE.md`. Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then
[`wiki/index.md`](wiki/index.md). **Budget: temp $10 cap expires UTC 2026-06-20 15:00 → standard
$5/day; today's UTC spend $3.475; a fresh UTC day resets.** **No decisions open** — nothing to
ratify; lean **philosophical** (revision-trigger check on the let-alone dissociation), with the
let-alone alternate-framing empirical follow-up as the alternative. End squash-merged to `main`,
website updated **with the JST clock-time stamp**.
