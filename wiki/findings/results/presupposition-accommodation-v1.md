---
type: result
id: presupposition-accommodation-v1
title: "All three models accommodate an unmet presupposition in a neutral context and substantially withhold it under explicit contradiction (verdict GATED-ACCOMMODATION 3/3) — but the gate is partial and non-uniform, leaving a residual yes-bias on existential triggers"
meaning-senses:
  - inferential
  - distributional
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-01
updated: 2026-07-05
links:
  - rel: operationalizes
    target: open-question/presupposition-accommodation-corner
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: the presupposition / accommodation probe v1

The first probe on the presupposition **accommodation** sub-corner
([`open-question/presupposition-accommodation-corner`](../open-questions/presupposition-accommodation-corner.md),
opened session 161). Where the projection line
([`result/presupposition-projection-v1`](presupposition-projection-v1.md) and
[`result/projection-trigger-inventory-v1`](projection-trigger-inventory-v1.md)) holds a
presupposition fixed and varies the **embedding** (does it survive negation/question/conditional?),
this probe holds the trigger sentence fixed and varies the **context**: is the backgrounded content
already **supported**, merely **new** (neutral), or explicitly **contradicted**? The diagnostic is
the SEP survey's §5 **accommodation** material
([`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md),
Karttunen 1974: 191: "the listener is entitled and expected to extend [the context] as required").
Run record:
[`experiments/runs/2026-07-01-presupposition-accommodation/`](../../../experiments/runs/2026-07-01-presupposition-accommodation/README.md);
frozen [`PREREG.md`](../../../experiments/runs/2026-07-01-presupposition-accommodation/PREREG.md),
manifest sha `4930d499…`.

**One-line finding.** The pre-registered verdict is **GATED-ACCOMMODATION (3/3)**. Every model
endorses the unmet presupposition in the **neutral** context (neutral-endorse **1.00 / 0.92 / 1.00**)
— accommodating backgrounded content the discourse never established — while **withholding** it
substantially under **explicit contradiction** (contradicting-endorse **0.33 / 0.58 / 0.42**),
clearing the frozen gating bar (accommodation-gap **+0.67 / +0.33 / +0.58**, all ≥ 0.30). So the
neutral endorsement is **not** a blanket yes-bias: it is sensitive to whether the context permits the
presupposition. But the gate is **partial** (contradicting-endorse is well above zero — the models
still endorse an explicitly-denied presupposition a third to a half of the time) and **non-uniform**
across trigger families (below), exactly the graded picture the source's §5.1 "accommodation isn't
always equally easy" warns to expect.

## Scope — LOAD-BEARING (read before citing)

**Within-model contrast only; no human comparison.** The signal is a *within-model asymmetry across
three contexts* — accommodate in neutral, withhold under contradiction — **not** *the model matches
human accommodation behavior*. No human accommodation baseline is claimed, measured, or needed. The
result does **not** certify that a model *represents* presupposition-vs-assertion or accommodation
semantically; it reads endorsement of backgrounded content off forced-choice answers
(text-consistency is not mechanism).

**A behavioral alternative reading is explicitly on the table (from the pre-run critic).** The
supported/neutral/contradicting profile that scores `gated_accommodation` is also consistent with a
simpler mechanism: a "does it follow?" **yes-bias** (endorse P in neutral) **plus generic
contradiction-detection** (say NO in contradicting because the discourse contains an explicit ¬P,
mostly *never / no one / nothing* or a lexical antonym). This probe cannot behaviorally separate
genuine accommodation-*blocking* from ordinary contradiction-detection, and does not claim to. The
`internal-contrast-only` framing already fences this: the finding is the within-model *contrast*
between the two contexts, not a claim that the model computes accommodation. The residual yes-bias is
visible directly in the data (see cleft, below), so the alternative reading is not hypothetical — it
is part of the picture.

**Anchor is `anchor: internal-contrast-only`** (terminal), ratified 2026-07-02 (session 163) by an
independent fresh-agent adversarial review —
[`decisions/resolved/presupposition-accommodation-internal-contrast-anchor`](../../decisions/resolved/presupposition-accommodation-internal-contrast-anchor.md),
opened session 162, ratified session 163 (the cross-session boundary held per charter §12.3). Every
quantity feeding the verdict is a within-model endorsement rate over the model's own YES/NO/UNCLEAR
answers — no human key in the scoring path — so the within-model contrast needs no resource anchor.
Ratification fixed the **yardstick, never the result**: every number and caveat below stands as
written.

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A),
  `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C), as subjects. Temperature 0; text-only,
  single-turn, zero-shot; gemini `reasoning={"effort":"minimal"}`. A neutral system prompt ("You are
  a careful reader…") that never mentions presupposition, accommodation, or the right answer.
- **Items.** 12 project-authored base scenarios across **4 trigger families** (factive / aspectual /
  definite / cleft; 3 each — the same inventory shape as the sibling projection run) × **3 context
  conditions** (supported / neutral / contradicting) = **36 item-conditions** per model, 108 calls
  total. Each scenario holds ONE trigger sentence constant and precedes it with a one-sentence
  context that **states** P (supported), is **topic-adjacent** to P (neutral), or **denies** P
  (contradicting). Each item is one forced choice — *"does it follow that: &lt;P&gt;? YES / NO /
  UNCLEAR."* `endorsed` == answer parses to YES.
- **Cost.** **$0.0191 billed** (`usage.cost`-summed: claude $0.0114 / gpt $0.0033 / gemini $0.0045),
  0 missing cost, **0 unparsed** answers. Far under the $2.50 single-run flag; UTC-2026-07-01 day
  total after this run **$0.1719** of $5.00.
- **Discipline.** Frozen before any call (FREEZE GUARD on manifest sha `4930d499…`); an **independent
  pre-run critic** returned **GO** with two SHOULD-FIX items (recorded below); an **independent
  post-run verifier** recomputed every rate from the raw answers by its own route and reproduced the
  table and the GATED-ACCOMMODATION (3/3) verdict exactly (**VERIFIED**).

## Numbers (from `results.json`; independently reproduced)

**Per model** (P-endorse rate per condition; gap = neutral − contradicting):

| model | supported | neutral | contradicting | accommodation-gap | sanity | label |
|-------|-----------|---------|---------------|-------------------|--------|-------|
| A claude-sonnet-4.6 | 1.00 | **1.00** | 0.33 | **+0.67** | ✓ | gated_accommodation |
| B gpt-5.4-mini | 1.00 | **0.92** | 0.58 | +0.33 | ✓ | gated_accommodation |
| C gemini-3.5-flash | 1.00 | **1.00** | 0.42 | **+0.58** | ✓ | gated_accommodation |

**Per family** (contradicting-endorse — where the gate does and does not bite; supported = neutral =
1.00 almost everywhere, so the discriminating cell is contradicting):

| model | factive | aspectual | definite | cleft |
|-------|---------|-----------|----------|-------|
| A | **0.00** | 0.33 | 0.33 | 0.67 |
| B | 0.67 | **0.00** | 0.67 | **1.00** |
| C | 0.33 | 0.33 | 0.67 | 0.33 |

**Verdict** (frozen thresholds SANITY 0.75 / ACCOM 0.60 / GAP 0.30 / FLATBAND 0.15 / LOWACC 0.40):
gated = {A,B,C}, blanket = {}, none = {} → 3/3 majority → **GATED-ACCOMMODATION**.

## Reading it

- **Accommodation is real and near-ceiling.** With the presupposition unestablished but unopposed,
  all three models supply it almost every time (neutral 1.00 / 0.92 / 1.00). A discourse-processor
  that refused to go beyond what was literally stated would answer NO/UNCLEAR here; instead the panel
  "extends the context as required," the behavior the §5 source names.
- **The gate bites — the neutral YES is not a blanket yes-bias.** Endorsement drops sharply when a
  prior sentence explicitly denies the presupposition (gap +0.67 / +0.33 / +0.58, all clearing the
  0.30 bar). The post-run verifier confirmed the drop is carried by genuine NO/UNCLEAR answers in the
  contradicting condition (e.g. "The safe had been securely locked the whole time. Sam realized that
  the safe had been left open." → NO/UNCLEAR), not a parse artifact. So the panel's accommodation is
  **context-sensitive**, not indiscriminate.
- **But the gate is partial, not a clean block.** Contradicting-endorse is 0.33–0.58, not near zero:
  the models still endorse an explicitly-contradicted presupposition a third to a half of the time.
  The trigger's presupposition and the discourse's denial *both* pull, and the denial only partly
  wins. This is the graded, "not always equally easy" accommodation the source flags, showing up as a
  within-panel attenuation rather than an on/off gate.
- **Non-uniform by family — a residual yes-bias localized to existentials.** The gate is cleanest on
  **factive** (A 0.00) and **aspectual** (B 0.00) triggers and weakest on **cleft**/existential
  triggers — **gpt-5.4-mini endorses the cleft existential 100% of the time even under explicit
  contradiction** ("The memo was never leaked to anyone. It was the intern who leaked the memo." →
  YES). For B on clefts the gate is fully open: it supplies "someone leaked the memo" regardless of a
  sentence saying nobody did. This is exactly the yes-bias pocket the pre-run critic warned could
  survive the design, now **located** rather than hypothetical: the panel-level gating verdict is
  carried by the other families, and one model has a trigger family where accommodation is
  indiscriminate. Reported, not smoothed over.

## Relation to the projection line (why the corner is now two-signature)

The presupposition corner now has **both** of its behavioral signatures measured within-model:

- **Projection** (survival under embedding) is **frame-gated** — near-perfect under negation,
  collapsing under the conditional antecedent
  ([`essay/projection-defeasible-by-frame`](../essays/projection-defeasible-by-frame.md)).
- **Accommodation** (supply under unmet context) is **contradiction-gated** — near-ceiling in a
  neutral context, attenuated (partially) under explicit contradiction.

Both are **environment-gated** rather than blanket: the models track whether the *licensing context*
permits the presuppositional inference, in both directions. That parallel is a candidate for a
philosophical bridge (queued in [`NEXT.md`](../../../NEXT.md)), not asserted here. *[Pointer, s183:
that bridge landed — [`essay/presupposition-environment-gated`](../essays/presupposition-environment-gated.md).]*

## Pre-run critic SHOULD-FIX items (carried as stated limitations)

The independent pre-run critic returned GO with no blockers and two SHOULD-FIX items; per freeze
discipline the design the critic reviewed was run unchanged, and both are documented here:

1. **`cle2` neutral context mildly leaks toward P.** "The contract ran for three years" pragmatically
   implies the contract was in force (awarded to someone), so this one neutral item tilts *toward* the
   existential presupposition rather than bearing on it neither way — nudging neutral-endorse up by at
   most one item on one model. Since neutral-endorse is already at ceiling (1.00 / 0.92 / 1.00) and
   the accommodation reading rests on the neutral-vs-contradicting *gap*, this single-item leak does
   not affect the verdict; a future iteration would swap it for a fully orthogonal fact.
2. **The gate leg cannot behaviorally separate accommodation-blocking from generic
   contradiction-detection + yes-bias.** Stated in full under Scope (the alternative reading). Fenced
   by the `internal-contrast-only` framing; surfaced, not hidden.

## Honest bounds

- **Behavioral, within-model, no human comparison** (see Scope). `anchor: internal-contrast-only`
  (ratified session 163); makes no claim a model *computes*
  accommodation, and admits the yes-bias+contradiction-detection alternative reading explicitly.
- **The gate is partial and one family is a yes-bias pocket.** GATED-ACCOMMODATION is the panel
  verdict, not a per-family or per-model clean block; contradicting-endorse 0.33–0.58 and B/cleft =
  1.00 are the honest texture.
- **Small Ns, n=3 models, three 2026 commercial models, 12 project-authored synthetic scenarios.** No
  coverage claim; direction-of-effect only, scoped to these families and this three-context design.
- **Supported is a retrieval floor, not accommodation.** The 1.00 supported-endorse is a sanity
  control (P is literally stated); the accommodation claim rests entirely on the neutral cell and the
  contradicting gate.
