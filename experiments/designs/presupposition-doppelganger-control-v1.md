---
type: design
id: presupposition-doppelganger-control-v1
title: "Presupposition doppelgänger control v1 — does presupposition beat a MATCHED surface-cue shadow, or is the corner measurably shadow-saturated? (within-model residual over a cue-matched non-trigger doppelgänger)"
meaning-senses:
  - inferential
  - distributional
  - constructional
status: draft
anchor: pending
contingent-on:
  - presupposition-doppelganger-control-design
created: 2026-07-03
updated: 2026-07-03
links:
  - rel: operationalizes
    target: essay/shadow-depth-cross-cuts-grain
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: result/presupposition-accommodation-v1
  - rel: depends-on
    target: essay/presupposition-environment-gated
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/inferential-meaning
---

# Design v1 — the presupposition doppelgänger (matched surface-cue) control

> **STATUS: DRAFT DESIGN — NOT FROZEN, DOES NOT RUN THIS SESSION.** This is a draft-PREREG, not a
> frozen run: it carries **no manifest sha**. It is `contingent-on`
> [`decisions/open/presupposition-doppelganger-control-design`](../../wiki/decisions/open/presupposition-doppelganger-control-design.md),
> which surfaces the doppelgänger-construction and scoring-key choices this design adopts as a
> **provisional default**. The intended path (mirroring the two sibling presupposition runs): a
> **later** session ratifies that decision via independent adversarial review (one non-Anthropic
> panel vote), then freezes this design's `prep.py` on a manifest sha, has an independent pre-run
> critic sign off, and runs it. Nothing here may be promoted to a finding until the probe has
> actually run. Every claim below is provisional and stated at the weak strength the essay it serves
> assigns the presupposition placement.

Program item **A1a** ([`wiki/program.md`](../../wiki/program.md)): the matched surface-cue control the
shadow-depth essay names as **owed**. It is the flagship's highest-leverage empirical unit because it
converts the presupposition *reading* in the shadow-depth table into a **measured** row — either a
measured saturated row (fails to beat the doppelgänger) or a move to the beater side (a residual over
the doppelgänger). Sibling runs mirrored: `2026-07-01-presupposition-projection`,
`2026-07-01-presupposition-accommodation`.

## The one question (nothing wider)

> The presupposition/projection corner behaves within-model as if the model **follows the trigger's
> surface cue**: the presupposition survives negation, collapses under the conditional antecedent
> ([`result/presupposition-projection-v1`](../../wiki/findings/results/presupposition-projection-v1.md)),
> and is context-gated in accommodation
> ([`result/presupposition-accommodation-v1`](../../wiki/findings/results/presupposition-accommodation-v1.md)).
> Does that behavior beat a **matched surface-cue doppelgänger** — items carrying the *same* trigger
> word-form and local frame but **without** the presuppositional structure — or does the doppelgänger
> endorse the same content just as much (a **measured** shadow-saturated corner)?

The measure is a **within-model residual**: `trigger P-endorse − doppelgänger P-endorse`, over the
cancelling frames where the trigger projects. A pure surface-cue follower behaves the **same** on
both legs (null residual); a system tracking the presupposition/assertion split behaves **differently**
(positive residual).

## Grounding in the source (SEP §1.1–§1.3)

From [`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../wiki/base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md)
(quotes verbatim, section locators; the entry is unpaginated). The design uses the source **only** as
the a-priori map of which constructions trigger presuppositions and where projection lives — never as
a human baseline.

- The corner and its triggers (§1.1): "Expressions and constructions carrying presuppositions are
  called "presupposition triggers", forming a large class including definites and factive verbs."
- The signature the probe imports (§1.2): "The hallmark of presuppositions, as well as the most
  thoroughly studied presuppositional phenomenon, is _projection_ (Langendoen and Savin, 1971)." And:
  "whereas the statements in (4) do not follow from any of these embeddings … the presuppositions do
  follow. We say that the presuppositions are _projected_."
- The diagnostic guidance the design follows (§1.2): "Projection from embeddings, especially negation,
  is standardly used as a diagnostic for presupposition (hence the term "negation test"). However it
  is important to try several types of embedding when testing for presupposition …" — hence the four
  frames.
- The defeasibility that motivates the frame restriction in scoring (§1.3): "Presuppositions typically
  project, but often do not …" — consistent with projection-v1's observed conditional-frame collapse.
- The four trigger families and their carried inferences, verbatim from the §1.1 trigger list:
  factives — "Berlusconi knows that he is signing the end of Berlusconism. → Berlusconi is signing the
  end of Berlusconism."; aspectual — "China has stopped stockpiling metals. → China used to stockpile
  metals."; cleft — "It was Jesus who set me free. → Somebody set me free."; definite descriptions —
  "The Prime Minister of Trinidad and Tobago stood up and wagged his finger. → Trinidad and Tobago
  have a (unique) prime minister."

**Provenance note (weaker than page-level for one step):** the source page lists what *is* a trigger
but does **not** state the contrastive non-triggers (e.g. that `suspect`/`consider` do **not**
presuppose). The doppelgänger substitutions are the **project's own construction**, defined as the
complement of the source's trigger inventory (a non-factive for a factive, a non-aspectual for an
aspectual, etc.); no quote is invented for them. That the substitutes are non-presupposing is standard
linguistic knowledge, carried at the project's own risk, not attributed to the source.

## Scope cap — LOAD-BEARING (read before citing any result)

Any labelled outcome is a **within-model behavioral contrast ONLY**, mirroring the two sibling runs.
It does **not**:

- make **any human comparison** — no human projection/doppelgänger baseline is claimed, measured, or
  needed. The signal is *the trigger leg endorses the content more than the matched doppelgänger leg,
  within the same model*, not *the model matches human judgments*.
- certify that the model **represents** a presupposition/assertion split; the contrast is behavioral
  (endorsement of an inference under embedding, read off forced-choice answers — text-consistency is
  not mechanism).
- adjudicate the projection problem or any theory of presupposition.

**Anchor discipline (surface, do not self-ratify).** The eventual result would carry
`anchor: internal-contrast-only` — a within-model contrast making no human-comparison claim, so no
resource anchor is required. That terminal status is **not** self-ratified in the session that runs
the probe: it is surfaced via
[`decisions/open/presupposition-doppelganger-control-design`](../../wiki/decisions/open/presupposition-doppelganger-control-design.md)
(opened s172) and the result carries `anchor: pending` until an **independent later session** ratifies
(charter §12.3). This design does not close that decision.

## Panel & settings

Panel per [`config/models.md`](../../config/models.md): `panel.A`, `panel.B`, `panel.C` as subjects
(do not hardcode slugs). Temperature 0; one date; zero-shot; text-only, single-turn (no tools);
`panel.C` (gemini) `reasoning={"effort":"minimal"}` per the config caveat (reasoning tokens otherwise
consume the visible-answer budget); billed `usage.cost` recorded per call. Neutral system prompt
("You are a careful reader. Answer the user's question directly.") that never mentions presupposition,
projection, triggers, doppelgängers, or the "right" answer.

## Design — item scheme

`prep.py` (frozen next session) generates the project's **own** synthetic items — no external corpus.
Four trigger families matching the sibling runs (SEP §1.1 inventory), **4 scenarios each = 16 base
scenarios** (up from the founding pilots' 3-per-family / 12 total — the powered upgrade, §Cost).

Each base scenario yields **two legs**:

- **Trigger leg** — the presupposition trigger (reproduces projection-v1). Target `P` = the
  backgrounded content the trigger presupposes.
- **D1 doppelgänger leg** — a minimally different **non-presupposing** predicate in the same frame,
  **same target `P`** (the content the trigger presupposed), as much surrounding material held
  constant as the substitution allows.

Each leg is embedded under **4 frames** (as in projection-v1): **plain** (baseline), **negation**,
**question**, **conditional** (antecedent). Item form is one forced choice, identical to the sibling
runs: *"Consider only the following statement: '&lt;framed sentence&gt;'. Taking that statement at
face value, does it follow that: &lt;P&gt;? Answer with exactly one word — YES, NO, or UNCLEAR."*
`endorsed` == parses to YES (`analyze.py`).

**D1 battery** = 16 scenarios × 2 legs × 4 frames = **128 item-conditions/model** (384 calls) — the
powered, verdict-bearing residual.

**D2 descriptive robustness leg** (per the decision's "both" default) = the **same 16 trigger
word-forms** with the presupposition **structurally defeated** by a metalinguistic / quotation framing
(e.g. *"Someone wrote the sentence 'The auditor realized that the accounts had been falsified,' though
whether the accounts were actually falsified was never established."*). Reduced scope — **16
item-conditions/model** (one structure-defeating framing each; 48 calls), explicitly **descriptive,
not verdict-bearing**. Its residual (trigger − D2, reusing the trigger baseline from D1) is reported
alongside D1 to probe D1's key confound (the substituted word's different distribution); its
metalinguistic-framing artifact and family heterogeneity are named, not smoothed.

### Worked example items (enough to freeze `prep.py`)

**Factive** — trigger `realized that S`, doppelgänger `suspected that S`; target `P` = "S".

| frame | trigger leg | D1 doppelgänger leg |
|-------|-------------|---------------------|
| plain | The auditor realized that the accounts had been falsified. | The auditor suspected that the accounts had been falsified. |
| negation | The auditor didn't realize that the accounts had been falsified. | The auditor didn't suspect that the accounts had been falsified. |
| question | Did the auditor realize that the accounts had been falsified? | Did the auditor suspect that the accounts had been falsified? |
| conditional | If the auditor realized that the accounts had been falsified, she resigned. | If the auditor suspected that the accounts had been falsified, she resigned. |

Target `P` (both legs): *"The accounts had been falsified."* Trigger projects `P` under negation/question; the non-factive doppelgänger does **not** entail `P` in any frame. A structure-tracker: trigger high, doppelgänger low → residual. A surface-cue follower keyed to the on-surface complement clause: both endorse → null.

**Aspectual** — trigger `stopped V-ing`, doppelgänger `considered V-ing` (gerund complement held constant); target `P` = the prior state.

| frame | trigger leg | D1 doppelgänger leg |
|-------|-------------|---------------------|
| plain | The refinery stopped flaring gas at night. | The refinery considered flaring gas at night. |
| negation | The refinery didn't stop flaring gas at night. | The refinery didn't consider flaring gas at night. |
| question | Did the refinery stop flaring gas at night? | Did the refinery consider flaring gas at night? |
| conditional | If the refinery stopped flaring gas at night, complaints fell. | If the refinery considered flaring gas at night, complaints fell. |

Target `P`: *"The refinery used to flare gas at night."* (Verbatim source schema: "China has stopped stockpiling metals. → China used to stockpile metals.") `stopped` presupposes prior flaring and survives negation; `considered` entails no prior flaring.

**Cleft** — trigger it-cleft `It was X who Y-ed`, doppelgänger plain assertion `X Y-ed`; target `P` = the existential.

| frame | trigger leg | D1 doppelgänger leg |
|-------|-------------|---------------------|
| plain | It was the deputy who authorized the transfer. | The deputy authorized the transfer. |
| negation | It wasn't the deputy who authorized the transfer. | The deputy didn't authorize the transfer. |
| question | Was it the deputy who authorized the transfer? | Did the deputy authorize the transfer? |
| conditional | If it was the deputy who authorized the transfer, the audit stands. | If the deputy authorized the transfer, the audit stands. |

Target `P`: *"Someone authorized the transfer."* (Source schema: "It was Jesus who set me free. → Somebody set me free.") **Discriminating cell = negation:** the cleft `It wasn't the deputy who authorized the transfer` projects the existential; the plain `The deputy didn't authorize the transfer` cancels it. (In the *plain* frame the plain assertion entails the existential too, so plain is not discriminating for this family — the residual is carried by the cancelling frames, as scored.)

**Definite** — trigger definite description `the X` (with content restrictor), doppelgänger an intensional/indefinite frame that removes the existence entailment; target `P` = existence/uniqueness. **This is the family where D1's cue-match is weakest** (removing the existence presupposition forces dropping the definite article or adding an opaque operator, so the surface cue degrades most here — flagged honestly; this is where D2 matters most).

| frame | trigger leg | D1 doppelgänger leg (cue degrades — flagged) |
|-------|-------------|----------------------------------------------|
| plain | The consultant who audited the merger flew to Geneva. | Regulators were looking for a consultant to audit the merger. |
| negation | The consultant who audited the merger didn't fly to Geneva. | Regulators weren't looking for a consultant to audit the merger. |
| question | Did the consultant who audited the merger fly to Geneva? | Were regulators looking for a consultant to audit the merger? |
| conditional | If the consultant who audited the merger flew to Geneva, the deal is closing. | If regulators were looking for a consultant to audit the merger, the deal is stalling. |

Target `P`: *"A consultant audited the merger."* The definite (with its relative-clause restrictor) presupposes such a consultant exists and projects it under negation; the intensional `looking for a consultant to audit the merger` (opaque) does **not** entail one exists. The article/opacity change is the honest weak point recorded above.

## Metrics (pre-specified, direction fixed — from the decision's scoring key)

Per model, from parsed answers (`analyze.py`):

- **trigger_project** — trigger-leg P-endorse rate over the **projecting** cancelling frames
  (**negation + question**).
- **doppel_project** — D1 doppelgänger-leg P-endorse rate over the same frames.
- **residual** = `trigger_project − doppel_project` (the within-model shadow-beating signal).
- **conditional_residual** — the same difference under the **conditional** frame, reported
  **descriptively only** (projection-v1 showed the trigger collapses there — 0.42/0.17/0.17 — so both
  legs are near-floor and the cell is uninformative for the shadow question).
- **plain_doppel_endorse** — D1 doppelgänger P-endorse in the **plain** frame, descriptive: a high
  value is itself a direct read on surface-following (endorsing the complement content despite the
  non-presupposing predicate).
- **d2_residual** — `trigger_project − D2_endorse`, descriptive robustness leg (not verdict-bearing).
- per-family decomposition of every rate (descriptive; n thin per family — flagged, as in the sibling
  runs).

**Frame restriction is pre-registered, not post-hoc:** pooling the primary residual over negation +
question (excluding the conditional) is fixed **now**, grounded in projection-v1's already-published
conditional collapse — not chosen after seeing results.

## Verdict map (thresholds fixed NOW; may be tightened, never loosened)

```
SANITY   = 0.60   per-model trigger_project floor (projecting frames); below it a model is control-FAILED.
RESID    = 0.30   per-model residual floor to count as "beats the doppelgänger".
FLATBAND = 0.15   per-model |residual| below which trigger ≈ doppelgänger (shadow-saturated).
```

- **BEATS-DOPPELGANGER** — ≥ 2/3 **sanity-passing** models have `residual ≥ RESID`. → the
  presupposition beats a **matched surface-cue** shadow; the corner **moves toward the beater side**
  of the shadow-depth table (a measured residual over a matched control).
- **SHADOW-SATURATED (FLAT)** — ≥ 2/3 sanity-passing models have `|residual| < FLATBAND`. → the
  doppelgänger endorses the same content just as much; a surface-cue account has **no residual to
  answer for**. This is a **first-class MEASURED result** written as such (charter §4) — it converts
  the essay's *reading* into a measured saturated row, the whole point of the control.
- **MIXED** — anything else (sanity failure, split panel, partial signal). Reported honestly; no
  shadow claim made.

A control failure (trigger does not reproduce projection) voids the strong reading and is reported, as
projection-v1's sanity discipline requires.

## Cost (pre-flight estimate)

D1 battery **384 calls** (128 conditions/model × 3) + D2 descriptive **48 calls** = **~432
single-turn, single-word completions**. Comparator: the projection battery of **288 calls billed
$0.0486** (`usage.cost`-summed) — ≈ $0.000169/call. Scaling: **≈ $0.06–0.15** billed (gemini's
minimal-reasoning tokens dominate the variance). `ABORT_USD = 1.00` hard-stops a runaway. Comfortably
under the **$2.50** single-run prudence flag and the **$5.00/day** cap. A real pre-flight (`--limit`
on one model) is measured and recorded before the full run, per `config/budget.md`.

**Powered-N note (PROTOCOL §4).** The D1 primary residual rests on **128 verdict-bearing
item-conditions/model** (64 trigger + 64 doppelgänger across 4 frames; **32 trigger + 32 doppelgänger
in the two projecting frames that carry the residual**) — ~10× the founding 12-scenario pilots, the
powered upgrade PROTOCOL §4 asks of a claim-carrying probe, while staying well under the spend flag.

## What each outcome feeds

- **BEATS-DOPPELGANGER** → the presupposition corner **moves toward the beater side** of the
  shadow-depth table ([`theory/shadow-depth-table-v1`](../../wiki/findings/theory/shadow-depth-table-v1.md)),
  and fires the first Revision trigger of
  [`essay/shadow-depth-cross-cuts-grain`](../../wiki/findings/essays/shadow-depth-cross-cuts-grain.md)
  ("a matched-control probe showed the presupposition corner beats a distributional shadow"): the
  grammatical pole would then carry **two beaters**, not a beater and a saturated corner. Strength
  gated by whether **D2** corroborates D1 (if only D1, the lexical-distribution confound keeps the
  move weak).
- **SHADOW-SATURATED (null residual)** → a **measured saturated row**: the presupposition placement in
  the shadow-depth table stops being a reading/bet and becomes a controlled failure-to-beat-a-shadow,
  parallel to (and stronger than) the antonymy corner. Written as a null (charter §4) — the honest,
  first-class outcome, and arguably the higher-value one for the flagship (it retires an owed control
  with a measurement rather than a bet).
- **MIXED / sanity failure** → the doppelgänger construction or item set is confounded (e.g. the
  definite family's cue degradation dominates); reported as such, no shadow claim, feeds a v2
  redesign — subject to the instrument stopping rule (PROTOCOL §3) if nulls recur across redesigns.
