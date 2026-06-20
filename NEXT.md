# NEXT.md

## ⚠ Budget note — read first

**The temporary $10/day cap (Tom, JST June 20 only) expires at the clock at 2026-06-20 15:00 UTC** (= end of
JST June 20; this session landed ~14:40 UTC, just under the wire). **Any session at or after 15:00 UTC is back
to the standard $5.00/day (UTC)** unless Tom says otherwise — i.e. the next session almost certainly runs under
the standard $5 cap. Either way today's spend is well under both.
**Today's UTC-day spend (2026-06-20) is $4.125** (sessions 51 $1.583 + 53 $1.561 + 57 $0.331 + 58 $0.316 +
**60 $0.334**). A **fresh UTC day (2026-06-21+) resets to $0 at the standard $5/day cap.** The single-run
prefer-split flag (~$2.50/run) is unchanged. Full ledger in [`config/budget.md`](config/budget.md).

## State

**Session 60 (2026-06-20 UTC) was EMPIRICAL ($0.334 spent) — the clean trigger-(b) gpt-uptake `let-alone`
test the previous two sessions queued.** It ran the uptake-inducing **forced-decomposition** re-run →
[`result/scivetti-let-alone-forced-decomposition-v1`](wiki/findings/results/scivetti-let-alone-forced-decomposition-v1.md)
(status `proposed`; anchors [`resource/scivetti-2025-cxnli-dataset`](wiki/base/resources/scivetti-2025-cxnli-dataset.md),
let-alone leg descriptive, comp-correlative the ratified-anchor ceiling control).

- **Single manipulated variable vs session 58:** the *offered* free-form working surface → a **mandatory,
  construction-neutral, answer-blind 3-step decomposition** (premise paraphrase / hypothesis paraphrase /
  link) required before the `FINAL:` tag. **No demonstration items** (lowest-governance-risk uptake-forcer →
  the few-shot leak caveat does not apply → **no new decision owed**). Held byte-identical: same 24 let-alone
  + 30 comp-corr items (subset sha `9be31a8fea8d7f16`, full-set == s57/58 `1c5cffb18c5ef78e`), 0/1/2 defs
  verbatim, gold not shown, panel, temp 0, gemini `effort: minimal` held constant.
- **Cadence honored:** independent fresh-agent pre-run critic **GO** (8/8 checks; byte-level single-variable
  diff; no demo items; no gold leak; verdict-map + uptake-check pre-registered incl. the honest
  "uptake-not-induced → method-null" branch) → frozen `PREREG.md` → probe → independent fresh-agent post-run
  verifier **REPRODUCED** (every acc/Wilson/sign-test + the uptake check + content_sha256↔CoT binding +
  CoT genuineness + no gold-leak; 0 discrepancies).
- **Verdict — UPTAKE INDUCED for all 3; all UNCHANGED vs offered; gpt PARTIAL recovery.** Forcing the steps
  took gpt from offered-but-declined (median **8** completion tokens, 16/24 bare) to genuinely-exercised
  (median **120**, 24/24 worked) — **closing session 58's "channel-not-taken-up" hole.** With the channel
  actually used, gpt's let-alone rose **0.375 → 0.583** (+0.21, 7 gains / 2 losses) — **directional but
  underpowered** (within-item sign test p = 0.090, does **not** clear the pre-registered 0.05 bar → verdict
  UNCHANGED) — and it **stays BELOW** the ≈0.90 human baseline (CI hi 0.755) where claude (0.833) and gemini
  (0.875) sit. So gpt's let-alone is a **partial output-channel effect** (part channel-bounded, part survives
  the exercised channel): the closest in-repo `essay/output-channel-confound` **trigger-(b) CANDIDATE**
  (direction present, power not yet there) — **not** a clean firing, and **not** a "channel artifact for gpt"
  reading. claude/gemini stay at baseline (manipulation check: the scaffold is benign, not teaching), comp-corr
  ceiling control PRESERVED 3/3.

Inter-feeding edits (genuinely owed, not manufactured): `essay/output-channel-confound` trigger (b) → CANDIDATE
partially-fired + a body forward-note in the uptake subsection (channel-not-taken-up resolved to a *mixture* of
channel-bounded + channel-controlled, vindicating the verify-uptake clause); `result/scivetti-let-alone-working-surface-v1`
forward-note (the named uptake arm ran → "artifact or bound?" resolves to **partly each**);
`open-question/instrument-sensitivity-constructional-inference` session-60 update (output-channel sensitivity is
**graded within** a model, not all-or-none). senselint **0 errors**; linkify clean; open-decisions dir **empty**.

## Next concrete action — backlog for the next session

**Reconcile first (PROTOCOL §2):** `wiki/decisions/open/` is **empty** — nothing to ratify. Apply any Tom
override first (the budget note above; check for any newer one).

**Track lean.** 55 emp · 56 emp · 57 emp · 58 emp · 59 **phil($0)** · 60 **emp($)**. The recent record is
empirical-heavy with one philosophical session. **Weight the next session toward PHILOSOPHICAL** — but only if a
revision is *genuinely owed* (do not manufacture an essay). If nothing is owed, the cleanest empirical move is
the powered let-alone re-run below.

1. **PHILOSOPHICAL (preferred *if owed*) — a genuine revision-trigger sweep.** Session 60 just turned
   `essay/output-channel-confound` trigger (b) into a *candidate partial firing* and added the body forward-note;
   check whether any *further* revision is owed by the partial-effect result — e.g. does
   [`essay/undischargeable-negative`](wiki/findings/essays/undischargeable-negative.md) or
   [`essay/witness-seeking-economics`](wiki/findings/essays/witness-seeking-economics.md) want a note that the
   output-channel control can return a *graded* (partial) verdict, not just clear/survive? Judge honestly; if the
   session-60 edits already discharge it, **write the null** and pivot to the empirical unit. (A $0 unit if owed.)
2. **EMPIRICAL (preferred if no philosophical revision is owed) — the POWERED let-alone re-run.** gpt's +0.21
   is the right *direction* for a channel-controlled residual but **underpowered** (n = 24, 9 discordant pairs,
   sign-test p = 0.090). Re-run with **more let-alone items** to resolve it. Two sources of fresh items, both
   needing a setup step: (a) the **disjoint train-split** let-alone items (`CxNLI_3_examples_train.csv` / the
   1-example train file in the same upstream repo — already cloned this session under
   `experiments/data/scivetti/`, gitignored) — *check these are disjoint from the 24 test items and balanced*;
   (b) a **free-form uptake-forcer** ("write at least N sentences of working") that separates *uptake* from the
   *3-step scaffold structure* (a `Limits` caveat of the v1 result). Same ratified Scivetti anchor +
   `constructional-divergence-operationalization`; forced decomposition with no demo items was already cleared as
   no-new-decision — but **adding train-split items is a new item set**, so re-freeze + re-certify + a fresh
   pre-run critic GO, and confirm disjointness. Pre-flight ~$0.3–0.5 (working-surface CoT, claude the driver).
3. **Longer-horizon alternatives (only if 1–2 are blocked):**
   - [`conjecture/function-word-substitutability`](wiki/findings/conjectures/function-word-substitutability.md)
     needs a new frequency-matched-pair anchor decision *opened* first — a $0 line-opening unit.
   - [`conjecture/distributional-saturation-grounding-headroom`](wiki/findings/conjectures/distributional-saturation-grounding-headroom.md)
     needs a fine-polysemy image set not in-repo (setup, not one-session-runnable).
4. **Website** per [`PROTOCOL.md §5b`](PROTOCOL.md) — **with the JST clock-time stamp** (mandatory).

## Open decisions

**None.** (No decision was opened or left open this session.)

## Standing-override notes (for Tom, if he looks)

- **Your temporary $10/day cap for JST June 20 has expired (15:00 UTC June 20); we are back to $5/day.**
  Session 60 spent **$0.334**; UTC-day 2026-06-20 total = **$4.125** of $5.
- This session ran the experiment the last two were building toward. Two sessions ago a model failed a hard
  grammar puzzle under a one-word answer; giving it room to reason helped two of three models but the third
  mostly *ignored* the room. This session *required* the third model to write out its working — it did, and the
  result is an honest in-between: forcing the working closed *part* of its gap (it rose from 38% to 58%) but
  left it *below* the human ~90% level the other two reach. So the cramped answer format was hiding *some* of
  the ability, not all of it. The 20-point rise (on 24 puzzles) is suggestive, not statistically settled — a
  bigger puzzle set is the next step. The site states this no more strongly than the wiki, names no monitor.

## Reminder for the next cold-start

Entry `continue-prompt.md`; charter `PROJECT.md` (§12); discipline `PROTOCOL.md`; conventions `CLAUDE.md`.
Read [`wiki/executive-summary.md`](wiki/executive-summary.md) then [`wiki/index.md`](wiki/index.md).
**Budget: temp $10 cap EXPIRED 15:00 UTC 2026-06-20 → standard $5/day; today's UTC spend $4.125; a fresh UTC
day resets.** **No decisions open** — nothing to ratify; lean **PHILOSOPHICAL** (a genuine revision sweep only
if owed — the session-60 partial-effect result may already be discharged) **else the POWERED let-alone re-run**
(more items — train-split or a free-form uptake-forcer — to resolve gpt's underpowered +0.21). End
squash-merged to `main`, website updated **with the JST clock-time stamp**.
