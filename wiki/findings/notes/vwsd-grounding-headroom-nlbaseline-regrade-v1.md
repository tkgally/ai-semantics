---
type: note
id: vwsd-grounding-headroom-nlbaseline-regrade-v1
title: "VWSD NL-baseline magnitude run — re-graded under the ratified VALID (category-match) scorer, and STILL deferred (clean degenerate NO-GO): the held-out two-judge cross-only category-match re-grade of the stored auditor guesses puts the fluent referent-naming channel's strict referent-recovery at 0.438, BELOW the [0.60,0.95] competence floor. So the s128 scorer-validity fix did NOT rescue the channel — a fresh independent critic verified the 0.438 is a VALID rate (HIGH verdicts not rubber-stamped; PARTIAL/NONE not over-strict; inter-judge kappa 0.608), not a scorer artifact, so the s127 'the channel is competent, ~64/70 are faithful recoveries' optimism is not borne out. IMAGE arm STILL not read; prediction 3 ('narrow headroom') STILL untested. No magnitude result. $0.406."
meaning-senses:
  - grounded.perceptual
  - distributional
  - referential.sense
status: recorded
anchor: internal-contrast-only
contingent-on:
  - []
created: 2026-06-28
updated: 2026-07-06
links:
  - rel: depends-on
    target: note/vwsd-grounding-headroom-nlbaseline-audit-v1
  - rel: depends-on
    target: conjecture/distributional-saturation-grounding-headroom
  - rel: depends-on
    target: result/vwsd-grounding-headroom-v2
  - rel: depends-on
    target: resource/vwsd-semeval-2023
  - rel: depends-on
    target: concept/grounding
  - rel: depends-on
    target: concept/polysemy
---

# Result: the VWSD NL-baseline magnitude run, re-graded under the ratified valid scorer, is STILL deferred — a clean degenerate NO-GO, not a scorer artifact this time

> **Reclassified 2026-07-06 (session 185, campaign P3 / program B6): result → note.** A re-grade of the already-stored auditor guesses that is STILL deferred (clean degenerate NO-GO); no magnitude was read — a re-analysis/deferral record, not a new measurement. Per the `note` page type (CLAUDE.md) it carries **no new measurement about LLM meaning**; `status: recorded`. History-preserving reclassification — nothing measured, scoped, or decided on this page changes.

> **Status: proposed (2026-06-28, session 128).** The follow-through on
> [`note/vwsd-grounding-headroom-nlbaseline-audit-v1`](vwsd-grounding-headroom-nlbaseline-audit-v1.md)
> (the s127 build+freeze+deferral). Session 128 cross-session **ratified a valid recovery-scorer**
> ([`decisions/resolved/vwsd-nlbaseline-recovery-scorer-validity`](../../decisions/resolved/vwsd-nlbaseline-recovery-scorer-validity.md),
> ADOPT Q-A WITH MODIFICATIONS) and **re-graded the stored auditor guesses** under it. The re-graded
> adequacy audit reads **0.438**, **still OUT OF BAND** against the fixed band `[0.60, 0.95]` — this time
> on the **degenerate (below-floor) side**, and a fresh independent pre-run critic verified the 0.438 is
> a **valid** strict-referent-recovery rate (not a scorer artifact in either direction). So the
> magnitude read is **deferred again**, the reused IMAGE arm is **still not read**, and the conjecture's
> "narrow headroom" sub-bet (prediction 3) **remains UNTESTED.** This page makes **no** human-comparison
> claim (the magnitude vs human gold was never read), hence `anchor: internal-contrast-only`.

## What this is (and why it stopped here, again)

[`note/vwsd-grounding-headroom-nlbaseline-audit-v1`](vwsd-grounding-headroom-nlbaseline-audit-v1.md)
deferred the s127 magnitude run because the held-out adequacy audit read OUT OF BAND under the ratified
**deterministic literal-target-word-lemma** scorer (two-auditor mean high-recovery **0.342** < the floor
0.60). An independent s127 critic diagnosed that as a **scorer-validity artifact** (VWSD target words are
technical/Latinate/variant/proper-noun forms a competent description names by common name) and judged,
on a hand-read, that **most of the ~70 "none" items (≈64) were faithful category recoveries** — i.e.
that the channel was probably competent and only the scorer was wrong. Session 128 cross-session ratified the fix
the s127 critic called for (a held-out **model** re-grade of *category match*), with strengthenings
(two held-out judges, **cross-only**; judged against the human gold `{word, phrase}`; a strict
semantic-referent-identity rubric forbidding string overlap; mandatory (a) word-referent / (b)
recovered-referent / (c) verdict fields for hand-audit), and re-graded the **stored** guesses under it —
**no re-authoring, text-only, no images.**

**The result: the valid scorer did NOT rescue the channel.** The two-judge cross-only band metric is
**0.438**, *higher* than the literal-lemma 0.342 (so the literal scorer **was** partly under-counting,
as diagnosed) but **still below the 0.60 floor** — a **degenerate-side NO-GO**. The rigorous two-judge
category-match says the fluent channel's held-out referent recovery is **~44% high, ~45% partial, ~11%
none**: most of the literal-"none" items the s127 critic eyeballed as "faithful category recoveries" are,
under a strict standard, **partial** (the auditor recovered the *scene / a hypernym / a co-present
object*, not the *specific* depicted referent), not high. So the s127 *"the channel is competent"*
optimism is **not borne out** by the rigorous re-grade.

## The gate that fired (the test of record for *admissibility*, before any magnitude read)

Re-graded adequacy audit, **two-judge mean high-recovery = 0.438** (gpt-judge × gemini-guesses
46/120 = 0.383; gemini-judge × gpt-guesses 59/120 = 0.492), against the ratified, **fixed** band
`[0.60, 0.95]` → **OUT OF BAND, below the lower bound** → a fresh independent pre-run-critic **NO-GO
that defers the magnitude read and relaxes nothing** (run-dir
[`PRERUN-CRITIC-REGRADE.md`](../../../experiments/runs/2026-06-28-vwsd-grounding-headroom-nlbaseline/PRERUN-CRITIC-REGRADE.md)).

**This time the NO-GO is NOT a scorer artifact — the critic verified validity in *both* directions:**

- **Not too lenient (HIGH side).** The critic hand-read **all 105 cross-leg HIGH verdicts** for
  word-referent ≟ recovered-referent. The judges award HIGH on **zero-string-overlap** synonym/Latinate/
  variant pairs while naming the shared referent (`thymus`→thyme, `ara`→hyacinth macaw, `aquila`→golden
  eagle, `mescal`→mezcal, `gantlet`→gauntlet, `mike`→microphone, `supporter`→jockstrap) — the rubric
  working as designed, **not** literal string-matching. No HIGH is an (a)≠(b) rubber-stamp; if anything
  the HIGH side is slightly lenient, so 0.438 is an **upper-ish** estimate.
- **Not too strict (the mirror PARTIAL/NONE side).** All 32 cross-leg NONE verdicts are validly *none*
  (genuine different-referent misses). A seed-fixed sample of 45 of the 103 cross-leg PARTIALs are
  genuinely partial (hypernym/whole-for-part, co-present object, related-but-different-specific,
  scene-not-object). **No** genuine same-specific-referent recovery was wrongly demoted to partial.
  Reaching the 0.60 floor would require **39 of 103 partials** to be wrongly-demoted highs; the critic
  found at most a handful of borderline cases — an order of magnitude short.
- **Stable boundary.** Inter-judge agreement: pooled exact 0/1/2 = 0.683, high-vs-not = 0.808,
  Cohen-κ(high) = **0.608** (substantial); the self-vs-cross leniency deltas are small and
  opposite-signed (cross-only is working). **0.438 is a valid strict-referent-category-recovery rate.**

## What this does and does NOT establish

- **Does NOT** test prediction 3 ("narrow headroom"): the magnitude was never read. The bet stays
  **UNTESTED** — neither supported nor refuted. The conjecture
  [`conjecture/distributional-saturation-grounding-headroom`](../conjectures/distributional-saturation-grounding-headroom.md)
  stays **`proposed`**.
- **Does NOT** make any human-comparison claim. The re-grade is a within-panel audit (held-out models
  recovering referents from a model-authored channel against the human-authored `{word, phrase}` spec);
  no model-vs-human recovery rate, no rescue rate against gold, no IMAGE arm. `anchor:
  internal-contrast-only`.
- **Does** establish a methodological result that **refines, and partly corrects, the s127 read**: the
  literal-lemma 0.342 **was** partly a scorer artifact (the valid scorer lifts it to 0.438), but the
  s127 critic's stronger claim — that the channel was *competent* and the NO-GO *only* a scorer artifact
  — is **downgraded**: under a valid, two-sided-audited, held-out **category-match** standard the fluent
  referent-naming channel's strict referent-recovery is **0.438, below the ratified competence floor**.
  So on VWSD this competence-audited fluent-channel route to the magnitude is **blocked under the
  ratified standard** — whether because the model-authored channel genuinely under-recovers the specific
  sense, or because VWSD's polysemous targets make *specific* referent recovery from a description alone
  intrinsically hard (a held-out reader recovers "a horse show," not "the Appendix Quarter Horse"), the
  two are not separated here and both defer the read. A **different magnitude instrument** (e.g. the
  conjecture's contemplated graded-image / fine-polysemy resource) may be needed to test prediction 3.
  *[Pointer, s183: that instrument question was then scoped —
  [`open-question/grounding-magnitude-instrument`](../open-questions/grounding-magnitude-instrument.md):
  no in-repo resource clears the requirements; an externally-released graded-image fine-polysemy set
  is the only route.]*

## A non-blocking yardstick nuance (surfaced, not acted on)

The band `[0.60, 0.95]` was calibrated (the audit-params decision, P3) against v2's *de-referenced
literal-lemma* `.130` floor, but the metric is now the more-generous *category-match* rate. The pre-run
critic reasoned this through and found it **strengthens, not threatens, the NO-GO**: a category-match
scorer would *raise* the de-referenced floor too (v2's stripped descriptors would score some category
hits the literal scorer missed), pushing the lower edge **UP, not down** — so a re-derived floor would
make `[0.60, 0.95]` look, if anything, *too lenient*. There is **no** reading on which the
band-transfer issue rescues the run. It is queued in [`NEXT.md`](../../../NEXT.md) as a **non-blocking** open-decision
*candidate* (re-derive the band explicitly on the category-match metric, for cleanliness) for a later
session — **not** opened this session, because it changes nothing here and a result already stands under
the ratified fixed band.

## Anti-cheat record

The scorer fix was ratified (s128, independent cross-session review) **before** the re-grade ran; the
frozen rubric (sha `55a67e39…`) was committed to git **before** any re-graded number was seen; the
re-grade re-scored only the **already-stored** guesses (no re-authoring, no images); the band
`[0.60, 0.95]` was **not** relaxed; the IMAGE arm was **not** read; no magnitude artifact exists. A
fresh independent pre-run critic (distinct from the orchestrator who ran the re-grade and from the
ratifying reviewer) returned the NO-GO with anti-cheat PASS, verified scorer validity in both
directions, and formed no narrow/wide preference. The diagnosis that 0.438 is a *valid* low rate (not an
artifact) **does not license proceeding** — it confirms the honest read is *defer*.

## Spend

$0.40582 billed (UTC 2026-06-28): re-grade preflight $0.01301 (16 calls) + full re-grade $0.39281 (480
calls; held-out two-judge cross-only category-match, gemini `effort:minimal`). 0 missing cost, 480/480
parsed. No spend on the reused IMAGE/DISTRACT arms (not read). Under the day's cap (Tom's temporary
$20/day UTC override for 2026-06-28). The spend bought the **valid certification** the s127 deferral
owed; the magnitude read remains deferred for a *substantive* reason (the channel is below the
competence floor), not a measurement artifact.
