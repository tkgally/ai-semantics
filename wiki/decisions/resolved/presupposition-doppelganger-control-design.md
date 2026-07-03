---
id: presupposition-doppelganger-control-design
title: How is the matched surface-cue doppelgänger for the presupposition corner constructed (D1 substitution / D2 structure-defeat / both), and what is the residual scoring key?
status: resolved
opened: 2026-07-03
opened-by: session-172
resolved: 2026-07-03
resolved-by: autonomous (adversarial review)
resolved-in-session: 173
contingent-artifacts:
  - design/presupposition-doppelganger-control-v1
---

# Decision: the presupposition doppelgänger control — construction and scoring key

## Resolution — 2026-07-03 (session 173): ADOPT DEFAULT (Q-A Both, Q-B as stated), RATIFY-WITH-NIT

**`resolved-by: autonomous (adversarial review)`.** Ratified cross-session (opened s172, ratified
s173 — a session boundary apart, per [`PROJECT.md`](../../../PROJECT.md) §12.3). An independent
fresh-agent reviewer (which did no downstream work) read this decision, the contingent design
[`design/presupposition-doppelganger-control-v1`](../../../experiments/designs/presupposition-doppelganger-control-v1.md),
the served essay [`essay/shadow-depth-cross-cuts-grain`](../../findings/essays/shadow-depth-cross-cuts-grain.md),
and the prior result [`result/presupposition-projection-v1`](../../findings/results/presupposition-projection-v1.md)
in full, and one decorrelated vote was routed through a non-Anthropic panel model (`panel.B` =
`openai/gpt-5.4-mini`, cutoff-aware preamble; [`PROTOCOL.md`](../../../PROTOCOL.md) §2 C5).

**Verdict: RATIFY-WITH-NIT** — the provisional default is sound to run under binding conditions
S1–S4. Adopt **Q-A: Both** (D1 powered/verdict-bearing over negation+question; D2 descriptive) and
**Q-B** as stated (residual metric; frames = negation+question; SANITY 0.60 / RESID 0.30 /
FLATBAND 0.15; verdict map with the null first-class).

**The two votes DIVERGED; the dissent was weighed and rebutted** (not smuggled — [`CLAUDE.md`](../../../CLAUDE.md)
rule 5). The fresh-agent reviewer **RATIFIED**; the non-Anthropic vote **REJECTED**, raising three
objections, each of which the fresh reviewer addressed on the merits:

- **Dissent 1 — "D1 mixes heterogeneous operations; dropping the definite family makes the powered
  residual unstable across families."** Rebuttal (reviewer test a, PASS): the three retained families
  are linguistically correct matched controls (factive `realize→suspect`; aspectual
  `stop→consider` with the gerund held constant; cleft→plain assertion, discriminating on negation);
  the definite family genuinely is **not** a matched control (trigger and doppelgänger share almost
  no surface material), so **S1** (drop it from the powered residual, carry it exploratory/D2-only) is
  the correct fix, and **S2** (per-family primary, pooled only secondary) surfaces the heterogeneity
  rather than smoothing it.
- **Dissent 2 — "restricting the primary residual to negation+question is outcome-based, not clean
  pre-registration."** Rebuttal (reviewer test b, PASS): the restriction is grounded in
  projection-v1's conditional collapse (verified 0.417/0.167/0.167 in that run's `results.json`),
  which dates 2026-07-01 and **predates** this 2026-07-03 design. The decisive tell against a
  positive-hunt is **N2** and it checks out directionally: excluding the conditional *raises*
  trigger_project, which if anything makes a **positive (BEATS)** residual *easier* — but BEATS is
  the **under-licensed** outcome (B1), so the restriction cannot be a hunt for the outcome that
  matters. Including the conditional would only dilute both legs toward floor.
- **Dissent 3 — "the verdict map is too easy to steer toward a positive residual rather than a genuine
  shadow-saturation test."** Rebuttal (reviewer test c, PASS + B1/B2): because a positive residual is
  under-licensed (a verb-sensitive surface-cue follower reconstructs it) and does **not** move the
  corner or fire the essay's trigger, there is **no incentive to steer toward it**; the SHADOW-SATURATED
  null is the cleanly-licensed diagnostic prize and is kept first-class in the map. The choice that
  makes the *preferred* (null) conclusion harder to reach is the opposite of p-hacking.

**Fabrication check PASS** (SEP quotes verbatim + located; projection-v1's 0.42/0.17/0.17 conditional
collapse and negation+question projection confirmed against `results.json`).

**NIT (folded into S3, already binding):** the design's Powered-N note headlines "128 verdict-bearing
item-conditions/model" before clarifying that only the two projecting frames carry the residual
(~64 residual-bearing conditions/model, dropping to ~48 once the definite family goes per S1). S3
already binds the freezing session to relabel honestly; **any citation uses the residual-bearing N
(~64, →~48 without definites), never 128.**

**Calibration observation carried to the freezing session (not a fix):** projection-v1 shows the
models *do* track projection under negation, and factivity is distributionally salient, so a
positive/BEATS or MIXED residual is **at least as likely** as the null. The design's honest downgrade
of BEATS (B1) means the probe is well-posed either way, but the "null is the prize" language is a
statement of **value-if-obtained, not a prediction** — the result must not read as if the null were
expected.

The design's `contingent-on` is now **cleared**: the freezing session (this one, s173) may freeze and
run under S1–S4, honoring B1/B2, the NIT (S3 N-labeling), and the calibration note. The eventual
result carries `anchor: internal-contrast-only` (surfaced here, not self-ratified).

---

## Original decision (as opened s172)

## Why this is owed

[`essay/shadow-depth-cross-cuts-grain`](../../findings/essays/shadow-depth-cross-cuts-grain.md)
places the presupposition/projection corner at the **shadow-saturated** end of the grammatical pole:
its within-model behavior (projection survives negation, collapses under the conditional antecedent;
accommodation is context-gated) is, on the essay's reading, *fully reconstructable* by "follow the
surface cue — the licensing environment leaves the trigger's cue on the surface, and the model
follows it." The essay is explicit (Honesty box; first Revision trigger) that this placement is a
**reading/bet, not a controlled result**, because **no matched surface-cue control** has been run
that would show presupposition *fails* to beat a distributional shadow the way the comparative
correlative *passes*. Program item **A1a** ([`wiki/program.md`](../../program.md)) names exactly this
control as the flagship's highest-leverage owed empirical unit.

The projection run ([`result/presupposition-projection-v1`](../../findings/results/presupposition-projection-v1.md))
already carries a within-base matched-**entailment** control (P vs. E on the same base). The new
increment this decision governs is a **surface-cue doppelgänger**: items that carry the *same*
surface cue (the trigger word-form and its local frame) but **lack** the presuppositional structure.
The **residual** = (trigger P-endorsement under cancelling frames) − (doppelgänger P-endorsement
under the same frames). **The two outcomes are not epistemically symmetric** (pre-run critic B1/B2,
s172 — see the Pre-run critic input section below):

- A **null residual** = **shadow-saturated**, a **measured** saturated row (not a reading). This is
  the **cleanly-licensed diagnostic** outcome: the model endorses the content equally for the trigger
  and its non-presupposing doppelgänger, so it is not tracking the presuppositional structure — the
  whole point of the control, and the higher-value outcome for the flagship.
- A **positive residual** does **NOT** establish "presupposition beats the surface-cue shadow" and
  does **not** move the corner to the beater side. A *verb-sensitive* surface-cue follower — which any
  distributional learner is — reconstructs a D1 residual, because D1 varies the trigger **word** (its
  distribution differs), unlike the comparative-correlative beater which varies only the construction
  over the **same words**. A positive residual shows at most that endorsement is **keyed to the
  trigger word-form above bare complement presence** — itself distributionally encoded — and merely
  **warrants re-examining** the placement (weighted toward the cleft family, the one construction-grain
  leg). Both outcomes are reported first-class; the asymmetry in what each licenses is stated.

Constructing a "same surface cue, no presuppositional structure" doppelgänger is value-laden and
non-obvious, and the residual's scoring key involves genuine sub-choices. This page surfaces both
rather than smuggling a default ([`CLAUDE.md`](../../../CLAUDE.md) rule 5).

## Question

**(Q-A)** How is the matched surface-cue doppelgänger constructed — by non-trigger substitution
(D1), by structure-defeat on the same word-form (D2), or by running both? **(Q-B)** What is the
residual scoring key — the residual metric, which frames enter it, the per-model threshold, and the
panel verdict map?

## Options

### Q-A — doppelgänger construction

- **D1 — cue-matched non-trigger substitution.** Replace the presupposition trigger with a minimally
  different **non-presuppositional** predicate in the *same* frame, holding the target content and as
  much surrounding material as possible constant:
  - factive `realized that S` (presupposes S) → non-factive `suspected that S` / `was convinced that
    S` (does **not** presuppose S). Under negation, `didn't realize that S` still yields S while
    `didn't suspect that S` does not.
  - aspectual `stopped V-ing` (presupposes prior V-ing) → `considered V-ing` / `planned to V` (does
    not). The gerund complement is held constant, so the local surface cue is closely matched.
  - it-cleft `It was X who Y-ed` (presupposes someone Y-ed) → plain assertion `X Y-ed`. Discriminating
    cell is **negation**: `It wasn't X who Y-ed` projects existence; `X didn't Y` cancels it.
  - definite `the X` (presupposes existence/uniqueness of X) → an indefinite / intensional-opaque
    frame that does not entail existence.
  - **Confound to state honestly:** the substituted word has different lexical semantics and
    co-occurrence, so the surface-cue *strength* is only **approximately** matched. A positive
    residual could in principle reflect the substituted predicate's different distribution rather
    than presuppositional structure per se. This is D1's core weakness, and it is worst for the
    **definite** family, where removing the existence presupposition forces dropping the definite
    article or adding an opaque operator (so the surface cue degrades most there).
- **D2 — cue-scrambled / structure-defeat.** Keep the trigger **word-form** but defeat the
  presuppositional reading structurally — a metalinguistic / quotation framing, or a frame in which
  the same word-form does not trigger. **Better cue-match** (same word), **worse uniformity** across
  the four trigger families and worse composition with the four embedding frames (metalinguistic
  framing does not embed naturally under negation/question/conditional), and it introduces its own
  quotation-framing artifact.
- **Both (provisional default).** Run **D1 as the powered, verdict-bearing primary residual** and
  **D2 as a reduced descriptive robustness leg**. Rationale: D1 and D2 fail in **opposite**
  directions — D1's weakness is the substituted word's different distribution; D2's weakness is
  heterogeneity and the quotation artifact — so a residual that appears in **both** is far stronger
  evidence than either alone, and D2 directly probes D1's key confound (if D1 shows a residual but
  D2 does not, the D1 residual is more likely the lexical-distribution confound than presuppositional
  structure). Running D1 alone leaves the "it's just the different word" objection unanswered; running
  D2 alone cannot reach powered N with uniform items.

### Q-B — residual scoring key

- **Residual metric.** Per model, `residual = trigger_project − doppel_project`, where `*_project`
  is the P-endorse rate over the **projecting** cancelling frames.
- **Which frames enter the residual (the load-bearing sub-choice).**
  - **(i, provisional default)** Pool over **negation + question** only — the frames where
    [`result/presupposition-projection-v1`](../../findings/results/presupposition-projection-v1.md)
    already showed the trigger *does* project (so there is a projection signal for the doppelgänger to
    differ from). Report the **conditional** frame separately as descriptive, because projection-v1
    found projection **collapses** under the conditional antecedent for every model
    (P-survival 0.42 / 0.17 / 0.17) — so both legs are near-floor there and the frame is uninformative
    for the shadow question. This frame choice is **fixed now, before any call**, grounded in an
    already-published frame asymmetry, so it is pre-registration, not post-hoc frame-picking.
  - **(ii)** Pool over **all three** cancelling frames (incl. conditional). Rejected as default: the
    conditional collapse dilutes the residual toward zero on *both* legs, which would bias the verdict
    toward SHADOW-SATURATED for a reason (the trigger doesn't project there either) that is unrelated
    to the doppelgänger question.
- **Sanity floor.** Per model, `trigger_project ≥ 0.60` (mirrors projection-v1 `SURVIVE`): if the
  trigger does not reproduce projection in the projecting frames, the residual is uninterpretable and
  the model is control-FAILED for this probe.
- **Per-model threshold & verdict map** (mirror the projection / accommodation PREREG style;
  thresholds fixed **now**, may tighten, never loosen):
  ```
  SANITY   = 0.60   trigger_project floor (projecting frames); below it a model is control-FAILED.
  RESID    = 0.30   per-model residual floor to count as "beats the doppelgänger".
  FLATBAND = 0.15   per-model |residual| below which trigger ≈ doppelgänger (shadow-saturated).
  ```
  - **BEATS-DOPPELGANGER** — ≥ 2/3 sanity-passing models have `residual ≥ RESID`. → the endorsement
    is **keyed to the trigger word-form above bare complement presence** (a lexical/constructional
    discrimination). **NOT** "beats the distributional shadow" and **NOT** a move to the beater side
    (pre-run critic B1: a verb-sensitive surface-cue account reconstructs a D1 residual). Warrants
    re-examining the placement, weighted toward the cleft family; does not fire the essay's trigger.
  - **SHADOW-SATURATED (FLAT)** — ≥ 2/3 sanity-passing models have `|residual| < FLATBAND`. → the
    doppelgänger endorses the same content just as much; a surface-cue account has **no residual to
    answer for**. This converts the essay's *reading* into a **measured saturated row** — the whole
    point of the control, and a first-class outcome written as such (charter §4).
  - **MIXED** — anything else (sanity failures, split panel, partial signal).

## Provisional default (used by the contingent artifact, pending ratification)

- **Q-A: Both** — D1 powered/verdict-bearing, D2 reduced/descriptive. It most cleanly isolates
  "presuppositional structure" from "cue-word presence": D1 supplies the powered structural contrast,
  D2 controls D1's lexical-distribution confound, and a convergent residual across both is required
  before any move off the saturated end is claimed at more than weak strength.
- **Q-B: residual metric as stated; frames = negation + question (option i); SANITY 0.60 / RESID 0.30
  / FLATBAND 0.15; verdict map as above.** Every outcome first-class, the SHADOW-SATURATED null
  explicitly so.

The contingent design [`design/presupposition-doppelganger-control-v1`](../../../experiments/designs/presupposition-doppelganger-control-v1.md)
is written to this default in **provisional** language and states nothing more strongly than its
source result/essay pages. The eventual result would carry `anchor: internal-contrast-only` (or
`anchor: pending`) — a within-model contrast making **no human comparison** — surfaced via this
decision, **never self-ratified** in the session that runs it.

## Pre-run critic input (session 172)

The contingent design was reviewed this session by an independent fresh-agent pre-run critic + one
non-Anthropic panel vote (`panel.B`) → **GO-WITH-CONDITIONS** (fabrication check PASS: all SEP quotes
verbatim + located). Two conceptual corrections were **applied to both this decision and the design
this session** — they sharpen the provisional default rather than replace it, so the default remains
ratifiable:

- **B1.** A positive residual does not license "beats the distributional shadow" (a verb-sensitive
  surface-cue account reconstructs a D1 residual, since D1 varies the *word*); the BEATS mapping is
  corrected throughout to "keyed to the trigger word-form above bare complement presence — warrants
  re-examination, not a move to the beater side." The **cleft** family is the partial exception (it
  varies only the construction over the same words).
- **B2.** The null (SHADOW-SATURATED) is the cleanly-licensed diagnostic outcome; the positive is
  under-licensed. Stated in the framing and verdict map.

Four **binding conditions on the freezing session** (carried in the design page, not resolved here):
**S1** drop the definite family from the powered residual (its D1 is not a matched control — trigger
and doppelgänger share almost no surface material) → exploratory/D2-only or redesign; **S2** report
per-family as primary (the families are heterogeneous control types), pooled only secondary; **S3**
relabel the powered N honestly (only ~64 residual-bearing conditions/model carry the residual, not
128; consider 5–6 scenarios per remaining family); **S4** report verdict-map sensitivity under nearby
cutoffs. NITs: **N1** a sanity failure may reduce the panel to 2 models (flag any 2/2 verdict);
**N2** the conditional-frame exclusion works *against* the preferred null, so it is not a positive-hunt.

A **later** ratifying session should confirm B1/B2 are honestly reflected and that the freezing
session honors S1–S4 before the probe runs.

## Ratification note

Opened by **session 172**; **not** ratifiable by it (charter §12.3 — only a later session ratifies,
via independent adversarial review, routing **one vote through a non-Anthropic panel model**,
[`config/models.md`](../../../config/models.md) §Task→model, with the cutoff-aware preamble). A later session should test the
default against: (a) whether the D1 substitutions genuinely remove the presupposition while matching
the surface cue as closely as claimed (the definite family is the honest weak point); (b) whether the
negation+question frame restriction is a legitimate pre-registration or a disguised
positive-hunt (the grounding in projection-v1's published collapse is the defense to weigh); and
(c) whether the verdict map keeps the null (SHADOW-SATURATED) genuinely first-class rather than a
disappointment. It then either ratifies `resolved-by: autonomous (adversarial review)` or replaces
the default. Tom's standing override outranks any autonomous ratification.
