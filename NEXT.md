# NEXT.md

## ⚠ Budget note — read first

**The temporary $10/day cap (Tom, JST June 20 only) expires by the clock at 2026-06-20 15:00 UTC** (= end of JST
June 20). From **2026-06-20 15:00 UTC onward (JST June 21+)** the cap is back to the **standard $5.00/day (UTC)**
unless Tom says otherwise. **Today's UTC-day spend (2026-06-20) is $3.791** (sessions 51 $1.583 + 53 $1.561 + 57
$0.331 + 58 $0.316; **session 59 spent $0**). A **fresh UTC day (2026-06-21+) resets to $0 at the standard
$5/day cap.** The single-run prefer-split flag (~$2.50/run) is unchanged. Full note in
[`config/budget.md`](config/budget.md).

## State

**Session 59 (2026-06-20 UTC) was PHILOSOPHICAL ($0 spent) — a genuine revision-trigger sweep, not a
manufactured essay.** It took session 58's output-channel/uptake finding
([`result/scivetti-let-alone-working-surface-v1`](wiki/findings/results/scivetti-let-alone-working-surface-v1.md))
and judged the revisions genuinely owed, then made two edits:

1. **[`essay/output-channel-confound`](wiki/findings/essays/output-channel-confound.md) — promoted the
   "channel-not-taken-up" insight from a trigger-(b) NOTE into the BODY** (new subsection *"Offering a channel
   is not exercising it: uptake as a control condition"*). Rationale: the insight corrects the **control** the
   essay prescribes (vary the output channel before reading a forced-format negative), and the control lives in
   the body — so the missing clause **"vary the channel *actually used*, not merely the channel offered; verify
   uptake model-by-model; read a declined surface as *inconclusive* (channel-not-taken-up), never a survival"**
   belongs in the body, not buried in a trigger. Small matching adds to "What this essay is not" bullet 2 + the
   Honesty box; trigger-(b) note annotated as promoted (originating event stays). YAML `depends-on`
   result/scivetti-let-alone-working-surface-v1 added.
2. **[`open-question/instrument-sensitivity-constructional-inference`](wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md)
   — added the OUTPUT CHANNEL as a *fourth* instrument-sensitivity mechanism**, distinct from the FC-vs-NLI
   *input* axis the page's three prior mechanisms track. The let-alone forced-token→working-surface lift
   (2/3 models to baseline) is the datum; page **stays `open`**; gpt non-uptake honesty note carried; YAML
   `depends-on` both scivetti results.

No new probe; no human-comparison or capability claims added (gpt stays **channel-not-taken-up**, not
channel-controlled). Independent read-only **adversarial coherence pass** (fresh agent): **no blockers**, every
number/quote faithful to the result page, "fourth mechanism" count correct, no closure asserted; one NIT (a
reworded phrase inside quote marks) fixed → paraphrase. senselint **0 errors**; linkify clean; open-decisions
dir **empty**.

## Next concrete action — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. Apply any Tom
override first (the budget note above; check for any newer one).

**Track lean.** 54 phil · 55 emp(gov,$0) · 56 emp(gov,$0) · 57 emp($) · 58 emp($, w/ essay+theory revision) ·
59 **phil($0)**. The philosophical track is now re-engaged (a real control-sharpening landed, no fabrication).
**Weight the next session toward EMPIRICAL** — and the cleanest empirical move is the one the last two sessions
queued and this session's essay edit makes load-bearing:

1. **EMPIRICAL (preferred) — the clean trigger-(b) test: induce uptake on gpt's `let-alone`.** Session 58's gpt
   result is confounded (working surface *offered* but mostly *declined* — 16/24 bare one-token answers, 0
   reasoning tokens). The essay now states explicitly (body §"Offering a channel is not exercising it") that a
   clean (b) test must **induce uptake** before gpt's persistence can be read as channel-controlled. Re-run gpt
   (and, for contrast, claude+gemini who lifted) on the SAME 24 `let-alone` items with an **uptake-inducing**
   channel: a **forced-decomposition** prompt that *requires* the working steps before the `FINAL:` tag, and/or
   a **few-shot demonstration** of working a `let-alone` scale. **Governance:** still the ratified Scivetti
   answer-key anchor + `constructional-divergence-operationalization`; a *format* change that does not alter
   what is scored against the human gold is an instrument extension (precedent: sessions 58, and the 2026-06-19
   working-surface re-run) — **but few-shot adds demonstration items**, so check whether the demonstrations
   could leak/alter scoring; **if a demonstration is built from *held-out* (train-split) `let-alone` items
   disjoint from the 24 test items, it is clean — otherwise surface a `decisions/open/` page**. Forced
   decomposition (no demo items) is the lower-governance-risk option and may be the cleaner first arm. Pre-flight
   ~$0.1–0.3 (working-surface CoT makes claude the cost driver). Cadence: frozen → independent pre-run critic GO
   → probe → independent post-run verifier (incl. CoT genuineness + content_sha256↔CoT binding).
2. **PHILOSOPHICAL alternatives (only if the empirical unit is blocked or a decision must be opened first):**
   - [`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md)
     needs a new frequency-matched-pair anchor decision *opened* first — a $0 line-opening unit.
   - [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
     needs a fine-polysemy image set not in-repo (setup, not one-session-runnable).
3. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**None.** (No decision was opened or left open this session.)

## Standing-override notes (for Tom, if he looks)

- **Your temporary $10/day cap for JST June 20 expires 15:00 UTC June 20; JST June 21+ is back to $5/day.**
  Session 59 spent **$0**; UTC-day total stays $3.791.
- This session did no experiments. It sharpened one of the project's own method rules in light of last
  session's result: a model failing under a one-word answer format should be re-tested with "room to think,"
  but last session showed one model was *given* the room and mostly *ignored* it — so the rule now says the
  re-test only counts if the model actually uses the room (otherwise it's inconclusive, not a verdict). The
  site states this no more strongly than the wiki, names no monitor, and flags nothing as a finding.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: temp $10 cap EXPIRES 15:00 UTC 2026-06-20 → standard $5/day; today's UTC spend $3.791; a fresh UTC
day resets.** **No decisions open** — nothing to ratify; lean **EMPIRICAL** (the clean trigger-(b)
gpt-uptake `let-alone` test, induce uptake via forced decomposition / held-out few-shot). End squash-merged to
`main`, website updated **with the JST clock-time stamp**.
