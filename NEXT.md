# NEXT.md

## ⚠ Budget note — read first

**The temporary $10/day cap (Tom, JST June 20 only) has expired by the clock.** It applied only through
**2026-06-20 15:00 UTC** (= end of JST June 20). From **JST June 21 (2026-06-20 15:00 UTC onward)** the cap is
back to the **standard $5.00/day (UTC)** unless Tom says otherwise. **Today's UTC-day spend (2026-06-20) is
$3.791** (sessions 51 $1.583 + 53 $1.561 + 57 $0.331 + 58 $0.316). A **fresh UTC day (2026-06-21+) resets to
$0 at the standard $5/day cap.** The single-run prefer-split flag (~$2.50/run) is unchanged. Full note in
[`config/budget.md`](config/budget.md).

## State

**Session 58 (2026-06-20 UTC) was EMPIRICAL with a real philosophical payoff ($0.316 billed).** It ran the
witness-seeking output-channel control the project's own method essays prescribe for session 57's `let-alone`
near-chance failure: [`result/scivetti-let-alone-working-surface-v1`](wiki/findings/results/scivetti-let-alone-working-surface-v1.md).
Re-ran the **SAME** 24 `let-alone` + 30 comparative-correlative (ceiling control) CxNLI items under a
**working surface** (step-by-step + `FINAL:` tag), **format-only** (everything else byte-identical, gemini
reasoning-effort held constant, full-set sha == session 57's). Verdict: **2/3 models LIFT to the human ≈0.90
baseline on the same items** (claude 0.542→0.792, gemini 0.667→0.917; within-item sign test 7 gains/1 loss,
p=0.035 each; control PRESERVED) → **the `let-alone` failure was largely an output-channel artifact, NOT a
scalar-phrasal competence boundary**. This **fires [`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md)
revision trigger (a)** (a second channel-masking, on a *grammatical-meaning* capability) and **refines its
scope** (the cut is "is the inference *serial*," not "is it single-premise NLI"). The theory page's session-57
"scalar-phrasal axis" reading was **revised** accordingly (no new content-type axis owed). **Honest residue:**
gpt-5.4-mini did NOT recover (0.375) — but the post-run verifier found it largely **declined** the offered
surface (16/24 bare one-token answers, 0 reasoning tokens), so its persistence is **channel non-uptake**, not a
demonstrated channel-controlled survival; **trigger (b) stays OPEN** (the essay now names a third state —
channel-not-taken-up — between channel-bounded and channel-controlled). Ran under the **already-ratified**
Scivetti anchor + `constructional-divergence-operationalization` — **no new decision owed** (independent
pre-run critic GO + independent post-run verifier REPRODUCED incl. CoT genuineness + content_sha256↔CoT
binding, both fresh agents). senselint **0 errors**; linkify clean; open-decisions dir **empty**.

## Next concrete action — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. Apply any Tom
override first (the budget note above; check for any newer one).

**Track lean.** 51 emp($) · 52 phil · 53 emp($) · 54 phil · 55 emp(gov,$0) · 56 emp(gov,$0) · 57 emp($) · 58
emp($, with essay+theory revision). The empirical track has run four of the last five sessions; the
philosophical track got *revision* engagement this session (output-channel-confound scope + theory) but no
**new** first-class essay/concept since 54. **Weight the next session toward PHILOSOPHICAL** unless the
gpt-uptake empirical unit (below) is judged the higher-value, tractable move.

1. **EMPIRICAL (the clean trigger-(b) test) — induce uptake on gpt's `let-alone`.** This session's gpt result
   is confounded: the working surface was *offered* but gpt mostly *declined* it (bare one-token answers). To
   tell **channel-controlled** (gpt reasons and still fails → trigger (b) fires) from **non-uptake** (gpt just
   won't use the surface), re-run gpt (and, for contrast, the two that lifted) on the SAME `let-alone` items
   with an **uptake-inducing** channel: a few-shot demonstration of working a `let-alone` scale, or a
   forced-decomposition prompt that *requires* the steps before the `FINAL:` tag. **Governance:** still the
   ratified Scivetti answer-key anchor; a *format* change that does not alter what is scored against the human
   gold is an instrument extension (precedent: this session) — **but few-shot adds demonstration items**, so
   check whether the demonstrations could leak/alter scoring; if a demonstration is built from *held-out*
   (train-split) `let-alone` items disjoint from the 24 test items, it is clean — otherwise surface a
   `decisions/open/` page. Pre-flight ~$0.1–0.3 (working-surface CoT makes claude the driver). Cheap; cadence
   (frozen → pre-run critic GO → probe → post-run verifier).
2. **PHILOSOPHICAL (preferred by track-lean) — a genuine revision-trigger sweep, not a manufactured essay.**
   The session-58 result touches several method essays: it fired `output-channel-confound` trigger (a) and
   added the **channel-not-taken-up** third state — is that worth promoting from the essay's trigger-(b) note
   into the body (a sharpening of the confound: "vary the channel *actually used*, not merely offered")? Also
   check whether [`open-question/instrument-sensitivity-constructional-inference`](wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md)
   should absorb the `let-alone` datum as a new instrument-sensitivity instance (forced-token vs working-surface
   is a third axis alongside FC-vs-NLI and model-specific). **If it fits cleanly with no revision owed, say so
   and do the empirical unit instead — do not manufacture an essay.**
3. **Other live forward bets (need setup, not one-session-runnable):**
   [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
   (needs a fine-polysemy image set, not in-repo) and
   [`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md)
   (needs a new frequency-matched-pair anchor decision opened first — a line-opening, $0 unit).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**None.** (No decision was opened or left open this session.)

## Standing-override notes (for Tom, if he looks)

- **Your temporary $10/day cap for JST June 20 has expired by the clock (it ended 15:00 UTC June 20); JST June
  21 is back to $5/day.** This session spent **$0.316** of it; UTC-day total $3.791.
- This session followed up last session's "let alone" gap. By re-running the *same* puzzles but letting the
  models show their working (changing nothing else), **two of three reached the human ~90% level on the very
  same items** — so that gap was mostly a one-word-answer-format trap, not a real hole in their grammar. The
  smallest model didn't recover, but it had largely declined the room to reason. The site states this no more
  strongly than the wiki, names no monitor, and flags the public-puzzles caveat.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: temp $10 cap EXPIRED (15:00 UTC 2026-06-20) → standard $5/day; today's UTC spend $3.791; a fresh UTC
day resets.** **No decisions open** — nothing to ratify; lean **philosophical** (revision-trigger sweep on the
output-channel/uptake finding), with the gpt-uptake `let-alone` empirical follow-up as the alternative. End
squash-merged to `main`, website updated **with the JST clock-time stamp**.
