---
type: claim
id: output-channel-working-surface
title: A forced single-token output channel masked a serial-inference capability on this panel, and a format-only working surface (everything else byte-identical, reasoning-effort held constant) flipped the verdict — replicated across task family (relational composition and let-alone scalar-construction NLI), operation pair, grid size, and composition depth; the effect is computation-specific (the bridging-context commitment null survives the identical channel control); channel NON-UPTAKE is a distinct third state, and with uptake forced one model shows a partial, below-baseline channel-controlled residual. A methodological claim, panel- and instrument-indexed
meaning-senses:
  - model-internal
  - functional-vs-formal
  - relational
  - constructional
  - inferential
  - human-comparison
status: supported
anchor: resource/scivetti-2025-cxnli-dataset
contingent-on: []
created: 2026-07-04
updated: 2026-07-04
links:
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: result/relational-order-composition-c-reasoning-scaffold
  - rel: depends-on
    target: result/relational-order-composition-c-altpair
  - rel: depends-on
    target: result/relational-order-composition-c-k6
  - rel: depends-on
    target: result/relational-order-composition-three-move
  - rel: depends-on
    target: result/scivetti-let-alone-working-surface-v1
  - rel: depends-on
    target: result/scivetti-let-alone-forced-decomposition-v1
  - rel: depends-on
    target: result/scivetti-let-alone-powered-rerun-v1
  - rel: depends-on
    target: result/lexical-bridging-context-working-surface-v1
  - rel: supports
    target: essay/output-channel-confound
  - rel: supports
    target: open-question/instrument-sensitivity-constructional-inference
---

# Claim: a forced single-token channel masked a serial-inference capability; a format-only working surface flipped the verdict — replicated, controlled, and bounded

> **Status: supported (PROMOTE-SCOPED) — 2026-07-04, session 177.** Cross-session, independent,
> adversarial claims-promotion review ([`PROTOCOL.md §3`](../../../PROTOCOL.md); program item B1) of
> the output-channel/working-surface line. The reviewer did no downstream work this session and
> produced none of the results. Promotion **fixes the yardstick, never the result** (see
> *Anti-cheat*). This is the project's first promoted **methodological** claim: its object is the
> *instrument* (the output channel), not any one construction or capability.
>
> *(Decorrelation note, [`PROTOCOL.md §3`](../../../PROTOCOL.md)/§2: the owed non-Anthropic panel
> vote was routed via the probe REST path — `openai/gpt-5.4-mini`, cutoff-aware preamble, billed
> `usage.cost` **$0.0038655** — and returned **PROMOTE WITH NARROWER SCOPE**: promote the masking,
> the flip, the boundary null, and the non-uptake state, but (1) keep the claim indexed to the
> tested tasks and panel rather than "serial-inference capabilities" generally, (2) drop the
> universal "every capability attribution must state its channel" sentence from the supported
> content (a recommendation, not a settled empirical claim), and (3) keep the let-alone flip
> explicitly 2-of-3. This fresh-agent verdict **adopts all three narrowings** — the statement below
> is written to them. The panel vote's fourth reservation (that "everything else held identical"
> should not carry weight) is **weighed and partially rebutted**: the format-only isolation is not
> an inference but a mechanically verified property of each run — byte-identical stimulus shas, a
> diffed probe library confirming only the format constants changed, and, on the bridging run, a
> dedicated `verify_format_only.py` byte-level audit — so the clause stays, as a description of the
> manipulation. Divergence weighed in writing; convergence on PROMOTE itself.)*

## Statement

On the ratified 3-model panel (`claude-sonnet-4.6`, `gpt-5.4-mini`, `gemini-3.5-flash`;
temperature-0 runs of 2026-06-19 through 2026-06-22), **a forced single-token/terse output channel
masked a serial-inference capability, and a format-only working surface — the same items, with only
the response format changed (step-by-step working permitted, a target-blind `FINAL:` tag parsed;
the reasoning-effort knob held constant) — flipped the failing verdicts**, in two independent task
families:

1. **Relational order-sensitive composition** (within-model contrast only): both previously-failing
   models flipped from four-instrument UNINTERPRETABLE to RESPECTS-ORDER at/near ceiling on
   byte-identical trials (gemini DIRECT **0.656 → 1.000**, gpt **0.250 → 0.969**), and the
   working-surface composition capacity **replicated across operation pair (D4 → A4), grid size
   (K=4 → K=6), and composition depth (2 → 3 moves)** — all three models RESPECTS-ORDER in every
   cell.
2. **Let-alone scalar-construction NLI** (human-anchored leg): **2 of 3** models lifted **+0.250**
   on the *same* 24 items (within-item sign test 7 gains / 1 loss, **p = 0.035** each) to CIs
   covering the **≈0.90** native-speaker baseline (claude 0.542 → 0.792, gemini 0.667 → 0.917),
   with the comparative-correlative ceiling control preserved.

Three qualifiers are part of the claim, not footnotes to it:

- **The effect is computation-specific, not universal.** The identical format-only channel control
  applied to a *non-serial* behavior — the lexical bridging-context "ungraded commitment" null —
  largely **did not** dissolve it: the null survived a genuinely-used working surface
  (channel-controlled) for the models that took the surface up. A widened channel flips verdicts
  where the probed inference is serial and externalizable, and demonstrably not everywhere.
- **Channel non-uptake is a distinct third state.** A model can *decline* an offered surface
  (gpt answered 16/24 let-alone items and ≥85% of bridging framings as bare one-token replies, 0
  reasoning tokens); its unchanged failure is then *inconclusive* — neither channel-bounded nor
  channel-controlled — and must not be read as a survival.
- **With uptake forced, a partial channel-controlled residual exists.** Forcing gpt to externalize
  (median 8 → 120 completion tokens, 24/24 worked) lifted it **+0.208** (directional; sign test
  p = 0.090, underpowered) yet left it **below** the ≈0.90 baseline at the item ceiling (combined
  0.636, Wilson CI hi **0.778 < 0.90**), a residual that held in every one of five repeated runs —
  so the masking story does not absorb everything: part of one model's gap survives a
  genuinely-exercised wide channel (magnitude unpinned by ~12% temp-0 label stochasticity).

The claim is **indexed**: it asserts masking-and-flip *for these tasks, this panel, these dates and
instruments* — per the decorrelation vote's narrowing, it does not assert that single-channel
verdicts are unreliable for serial inference in general, and the "state the channel a capability
attribution is indexed to" discipline remains the (draft) essay's recommendation, which this claim
*motivates* but does not itself assert as supported content.

## Grounds — the composition witness and its three replication axes (within-model contrast)

The witness ([`result/relational-order-composition-c-reasoning-scaffold`](../results/relational-order-composition-c-reasoning-scaffold.md)):
four prior instruments forbade a working surface ("EXACTLY ONE figure name … no explanation, no
reasoning") and gemini/gpt failed the on-demand DIRECT gate on all four (gemini 0.583 / 0.594 /
0.656 / 0.625; gpt 0.194 / 0.438 / 0.250 / 0.156; claude, the positive control, 0.861–1.000). The
fifth run, on **byte-identical** trials (same stimulus sha), changed **only** the response format.
Verdict: all three RESPECTS-ORDER; the result page's own reading, quoted verbatim: "the
four-instrument gemini/gpt negative was an artifact of the **forced single-token format** (no
working surface), **not** a composition-capacity limit." Its CoT-genuineness check is decisive: on
every reverse-printed COMP record the visible working explicitly re-sorts the moves by round stamp
(a print-order reader would score exactly 0.50).

The three replication axes, each a single-variable variation, each pre-run-critic-gated GO and
independently reproduced from raw (picks matched 288/288 or 324/324):

| working-surface instrument (all 2026-06-19) | claude DIRECT / COMP | gemini DIRECT / COMP | gpt DIRECT / COMP |
|---|---|---|---|
| witness: K=4 STEP/FLIP (D4) | 1.000 / 1.000 | 1.000 / 1.000 | 0.969 [0.843, 0.995] / 0.953 [0.871, 0.984] |
| operation pair: K=4 CYCLE/SWAP (A4) ([`result/relational-order-composition-c-altpair`](../results/relational-order-composition-c-altpair.md)) | 1.000 / 1.000 | 1.000 / 1.000 | 1.000 / 0.906 [0.810, 0.956] |
| grid size: K=6 STEP/FLIP (D6) ([`result/relational-order-composition-c-k6`](../results/relational-order-composition-c-k6.md)) | 1.000 / 1.000 | 1.000 / 1.000 | 1.000 / 0.861 [0.763, 0.923] |
| depth: 3 moves, generic S6 ([`result/relational-order-composition-three-move`](../results/relational-order-composition-three-move.md)) | 1.000 / 1.000 | 1.000 / 1.000 | 1.000 / 0.903 [0.813, 0.952] |

All COMP bars are Wilson-95 LB > 0.50 against shortcut readers that top out at exactly 0.50; all
DIRECT gates ≥ 0.80 passed. gpt's residual COMP misses are reversed-order or table-lookup slips,
**not** the single-move signature that defined its forced-format failure (that signature "vanishes
the moment a working surface is allowed"). All four pages are ratified
`anchor: internal-contrast-only` — this component of the claim is a **within-model format-vs-format
contrast** and carries **no human comparison**; the verdicts are THIN ("respects operation order",
not constitution).

## Grounds — the let-alone flip (human-anchored leg) and the ceiling control

[`result/scivetti-let-alone-working-surface-v1`](../results/scivetti-let-alone-working-surface-v1.md),
format-only against the session-57 forced single-digit channel, same 24 items:

| model | forced (s57) | working surface | Δ | gains / losses | sign-test p | vs human ≈0.90 |
|---|---:|---:|---:|---:|---:|---|
| claude-sonnet-4.6 | 0.542 | **0.792** [0.595, 0.908] | +0.250 | 7 / 1 | 0.035 | MATCHES (CI covers 0.90) |
| gemini-3.5-flash | 0.667 | **0.917** [0.742, 0.977] | +0.250 | 7 / 1 | 0.035 | MATCHES (CI covers 0.90) |
| gpt-5.4-mini | 0.458 | 0.375 [0.212, 0.573] | −0.083 | 2 / 4 | — | BELOW — **non-uptake** (16/24 bare one-token, 0 reasoning tokens) |

The comparative-correlative ceiling control stayed at 0.967–1.000 for all three, so the surface did
not break the instrument. The result page's licensed reading, quoted: the let-alone near-chance
result is, "for claude and gemini, **substantially an output-channel artifact**" while gpt
"**largely declines the offered surface** and does not recover." This is the cross-task-family
replication of the masking: a different instrument family (single-premise NLI), a different
capability (scalar constructional inference), a human-anchored yardstick — same flip under the same
format-only manipulation. The **direction** of the wide-channel at-baseline level for claude/gemini
is corroborated across three wide-channel runs (offered surface 0.792 / 0.917; forced decomposition
0.833 / 0.875; powered re-run 0.708 / 0.909), with claude's level jittering ~0.12 per run — the
within-item paired lift itself (p = 0.035) was measured once per model.

## The boundary control — where the channel does NOT flip the verdict

[`result/lexical-bridging-context-working-surface-v1`](../results/lexical-bridging-context-working-surface-v1.md)
ran the identical format-only manipulation (byte-level audited by its `verify_format_only.py`) on a
**non-serial** behavior: the "graded scale, ungraded commitment" null. Outcome, per that page's
headline: the null "is, in the main, channel-CONTROLLED — it is not a forced-format artifact."
gemini took up the surface fully and the commitment null **survived** (confidence not lower on
bridging, decline 0%); claude took up the surface and its *categorical-decline* null held (only its
self-reported confidence number drifted lower, 82.6 → 75.2); gpt again declined the surface (≥85%
bare answers). This is the control that keeps the claim honest in both directions: the working
surface is not a magic accuracy lever — it dissolves negatives where a serial computation was
denied a surface, and leaves a genuine (non-serial) commitment posture standing.

## The third state and the residual — non-uptake, then a partial channel-controlled bound

- **Non-uptake (twice observed, same model).** gpt declined the offered surface on let-alone
  (16/24 bare, 0 reasoning tokens) and on bridging (≥85% bare across framings, medians 8–15
  tokens), while claude/gemini reasoned on every item. A declined surface leaves the channel
  unwidened in fact; the unchanged failure is **inconclusive**, not a survival.
- **Uptake forced → partial effect.**
  [`result/scivetti-let-alone-forced-decomposition-v1`](../results/scivetti-let-alone-forced-decomposition-v1.md):
  a construction-neutral, answer-blind 3-step scaffold induced uptake (gpt median 8 → 120
  completion tokens, 24/24 worked; ceiling control preserved; claude/gemini unchanged at baseline,
  so the scaffold is benign, not teaching). gpt rose 0.375 → **0.583** [0.388, 0.755] (+0.208,
  7 gains / 2 losses, p = 0.090 → pre-registered verdict UNCHANGED), still **below** baseline.
- **Residual confirmed at the item ceiling, magnitude unpinned.**
  [`result/scivetti-let-alone-powered-rerun-v1`](../results/scivetti-let-alone-powered-rerun-v1.md)
  (33 items = the human-annotated maximum): gpt combined **0.636** [0.466, 0.778], **CI hi 0.778 <
  0.90** → CONFIRMS-RESIDUAL, with uptake 33/33 and the session-60 test accuracy reproduced exactly
  (0.583 → 0.583). The same run exposed **~12% temp-0 run-to-run label flips** (claude, a
  baseline-matcher, fell 0.833 → 0.708 on identical items via 3 adverse flips), so the residual is
  **directional with magnitude unpinned**; the K=5 repeated-run follow-up recorded on that page
  found gpt's residual below 0.90 **in every one of five runs** (de-noised majority-vote 0.606),
  with model-specific swing (gpt ~±0.12 / claude ~0.06 / gemini ~0.03). So part of one model's
  let-alone gap is channel-bounded (uptake helps) and part **survives a genuinely-exercised wide
  channel** — the masking claim is bounded on this side too.

## Human-comparison leg (let-alone only — descriptive, contamination-caveated)

The human anchor is [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
(CxNLI Exp-1 gold labels + the ≈0.90 native-speaker accuracy baseline; answer-key
operationalization ratified 2026-05-29). What it grounds here is exactly what the result pages
state: the comparative-correlative control carries the **ratified anchor**; the let-alone
accuracy-vs-0.90 leg is **descriptive** from the same human-annotated release (not individually
anchored), and the "MATCHES" verdicts rest on CIs that *cover* 0.90 (point estimates 0.792, 0.917),
not on point equality. The items are public, so an answer-key match cannot distinguish learned
construction-meaning from memory (the inherited contamination caveat); the **robust, powered signal
is the within-item format contrast** (7/1 sign tests, p = 0.035), which is model-internal. The
composition component makes **no** human-comparison claim at all (ratified
`internal-contrast-only` on every C-series page). This claim's human-comparison content is
therefore exactly: *given a working surface, two of three models' let-alone accuracy became
statistically compatible with the human baseline on the same items where the forced channel had
them near chance* — nothing stronger.

## What this claim does NOT say

- **Not "the models compose (or infer) without a working surface."** The witness page is explicit,
  quoted verbatim: it "does **not** show the models compose *without* a working surface (they do
  not, robustly, across four instruments) — the finding is precisely that the **format** gates the
  behavior." The narrow-channel negatives were true verdicts about a channel-indexed capability.
- **Not a universal instrument law.** Per the decorrelation vote's adopted narrowing: masking-and-
  flip is asserted for these two task families, this panel, these instruments and dates. The
  general "single-instrument verdicts are unreliable" moral and the "state your channel index"
  norm live in [`essay/output-channel-confound`](../essays/output-channel-confound.md) (status:
  draft) and in [`open-question/instrument-sensitivity-constructional-inference`](../open-questions/instrument-sensitivity-constructional-inference.md),
  which this claim supports as their strongest worked evidence — it does not promote them.
- **Not "the working surface always helps."** The bridging-context commitment null survived the
  identical control; the wide channel dissolves *serial-computation* negatives, and the one tested
  non-serial behavior stood.
- **Not "gpt cannot do let-alone" — and not a clean 3/3 flip.** The let-alone flip is 2 of 3; gpt's
  persistence under the *offered* surface is non-uptake (inconclusive), and under *forced* uptake
  it is a partial, below-baseline residual whose magnitude is unpinned (~±0.12 temp-0 swing). The
  undischargeable-negative discipline forbids the "cannot" reading throughout.
- **Not a wide-channel capability ceiling or a mechanism claim.** A wide-channel positive indexes a
  *scaffolded* capability (compose-given-a-scratchpad), not compose-in-one-step; no depth ≥4 bound
  was sought (suspended on budget, reopenable); and nothing here is about model internals — the
  serial-computation mechanism has theory-of-computation *plausibility* grounding only (li-2024,
  cited at that strength on the result and essay pages).
- **Not a model ranking.** The panel is concordant on every working-surface composition cell;
  "gpt is the fragile member" on let-alone/uptake is an observed per-model pattern, not a quality
  verdict.
- **Not rung (iii) / constitution, and not a representational claim.** All composition verdicts are
  THIN ("respects operation order", single-reader-recoverable); all findings are behavioral.

## Bounds

- **Single panel, single era, one run per cell (the lead bound).** All three C-series replication
  axes are the *same* three models, the same operationalization family (figure→figure lookup
  tables, working-surface elicitation), run on the same UTC day (2026-06-19), one run per cell.
  They vary the instrument's geometry genuinely (D4 / A4 / D6 / S6; K=4 / K=6; depth 2 / 3) but are
  not cross-date or cross-panel replications. The let-alone side has three wide-channel runs and a
  K=5 repeated-run study, but n is small (24–33 items, the resource's ceiling).
- **Temp-0 stochasticity caps precision.** ~3/24 labels flip per run on let-alone for claude and
  gpt (gemini most stable); single-run point estimates on that construction carry ~±0.12 (gpt)
  spread. Directions and paired within-item contrasts are the robust signals; absolute levels are
  draws.
- **Uptake is model-graded and must be verified per model.** Two of the five channel-control runs
  cited here would have been misread (a non-uptake as a survival) without the verifier's uptake
  check; the claim's own force is conditional on that discipline.
- **The boundary control is one behavior.** "Computation-specific, not universal" rests on one
  non-serial null (bridging commitment) surviving the control, plus the argument-structure NLI
  items already at ceiling in one token; other non-serial behaviors are untested.
- **Contamination (let-alone leg).** Public items; the ≈0.90 comparison inherits the caveat; the
  within-item lifts and the C-series contrasts do not.
- **Shared priors.** Three same-era commercial models; the human baseline (let-alone leg) is the
  only independent bearing, and it is aggregate, not per-item.

## Anchor

This claim carries `anchor: resource/scivetti-2025-cxnli-dataset` with an `anchors:` link to
[`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
because one component — the let-alone lift **to the ≈0.90 human native-speaker baseline** — is a
human-comparison statement, and that resource (ratified 2026-05-29) is what grounds it, at exactly
the strength the underlying pages license: aggregate baseline, descriptive for let-alone,
contamination-caveated, CI-covers not point-match. The composition component carries **no** human
comparison: its four result pages are ratified `anchor: internal-contrast-only`, and this claim
cites them strictly as within-model format-vs-format contrasts. The reviewer weighed the
alternative scoping — a purely within-model claim under `anchor: internal-contrast-only` — and
rejected it: that terminal state would require a ratification this claim does not have, and it
would force dropping the line's human-anchored component, which is load-bearing (it is what makes
the masking finding a cross-task-family replication rather than a one-family observation). Option
(a) states more while fabricating nothing.

## Anti-cheat

Promotion fixes the **yardstick** — the pre-registered gates (DIRECT ≥ 0.80, Wilson-LB > 0.50
against 0.50-ceiling shortcut readers; the within-item sign test at 0.05; the fixed ≈0.90 human
reference, never retuned) — **never the result.** Every gate predates its result; every run was
pre-run-critic-gated (GO) with frozen, sha-pinned stimuli, and independently reproduced from raw by
a fresh post-run verifier (288/288, 324/324, 324/324 picks matched on the C-series; every
accuracy, CI, paired count, p-value, uptake metric, and billed cost on the Scivetti and bridging
runs). The reviewer produced none of the results. The exciting over-reads — "the models could
always do it and the negatives were errors," "CoT unlocks true capability" (unindexed), "the
channel explains gpt's gap" (it explains part; a residual survives), or "2/3 models match human
let-alone competence" (a contaminated absolute match) — are exactly what the channel-indexing, the
non-uptake state, the residual, the boundary null, and the descriptive/contamination caveats
refuse. The decorrelation vote's narrower-scope verdict was adopted in full on scope; its one
reservation not adopted (the "everything else held identical" clause) is retained because it is a
mechanically verified property of the runs, not an interpretive add-on — recorded here so the
divergence is auditable. Refusal was weighed: the line clears the replication prong more strongly
than the s176 single-run promotions (two task families, three geometry axes, three wide-channel
let-alone runs, a repeated-run study, and a genuine boundary control), so refusing would have been
under-claiming past the evidence, which is its own miscalibration.

## Status

`status: supported`, scoped. What is supported: on this panel and these instruments, (i) a forced
single-token channel produced capability-negatives that a format-only working surface flipped to
at/near-ceiling passes — for both failing models on order-sensitive composition (byte-identical
trials; replicated across operation pair, grid size, and depth 2→3) and for 2 of 3 models on
let-alone scalar-construction NLI (+0.250 within-item, p = 0.035, to CIs covering the ≈0.90 human
baseline; ceiling control preserved); (ii) the effect is computation-specific — the non-serial
bridging-context commitment null survived the identical control for every model that took the
surface up; (iii) channel non-uptake is a real, recurring third state that renders an unchanged
failure inconclusive; and (iv) with uptake forced, gpt's let-alone shows a directional,
below-baseline channel-controlled residual (0.636, CI hi 0.778 < 0.90; held in 5/5 repeated runs;
magnitude unpinned by ~12% temp-0 label stochasticity). `supported` attaches to exactly that —
not to any unindexed capability claim, universal instrument law, mechanism, ranking, or
representational reading, all disclaimed above. The eight underlying result pages remain
`status: proposed` (this promotion consolidates; it does not restate their per-run readings).
`contingent-on: []` — the governing operationalizations and anchors (the CxNLI answer-key anchor,
the Option-C internal-contrast-only frame) are ratified. Resolved-by: autonomous (adversarial
review), session 177, with the non-Anthropic decorrelation vote recorded above. The natural next
strengthening is a cross-date or cross-panel re-run of one composition cell and one let-alone
wide-channel arm (the ladder lane, once built, is the cheap route).
