---
type: result
id: scivetti-let-alone-working-surface-v1
title: The let-alone near-chance failure is largely an output-channel artifact — 2 of 3 models reach the human baseline once given a working surface; the weakest model largely declines the surface and does not recover
meaning-senses:
  - constructional
  - inferential
  - human-comparison
  - model-internal
status: proposed
contingent-on: []
created: 2026-06-20
updated: 2026-06-20
links:
  - rel: anchors
    target: resource/scivetti-2025-cxnli-dataset
  - rel: depends-on
    target: source/scivetti-2025-beyond-memorization
  - rel: refines
    target: result/scivetti-cxnli-answer-key-v1
  - rel: supports
    target: essay/output-channel-confound
  - rel: supports
    target: essay/undischargeable-negative
  - rel: depends-on
    target: essay/floor-is-not-a-ceiling
  - rel: depends-on
    target: theory/constructional-meaning-in-llms
  - rel: depends-on
    target: source/li-2024-cot-serial
---

# Result: let-alone working-surface format probe v1

A **format-only** follow-up to [`result/scivetti-cxnli-answer-key-v1`](scivetti-cxnli-answer-key-v1.md)
(session 57), which found the phrasal scalar **let-alone** at near-chance for all three
panel models (claude 0.542 / gpt 0.458 / gemini 0.667; 3-way chance ≈ 0.33) under a
**forced single-token** NLI channel ("Output a single digit 0, 1, or 2 and nothing
else"). The project's own methodological spine
([`essay/output-channel-confound`](../essays/output-channel-confound.md),
[`essay/undischargeable-negative`](../essays/undischargeable-negative.md),
[`essay/floor-is-not-a-ceiling`](../essays/floor-is-not-a-ceiling.md)) says a
forced-format near-chance negative must have its **output channel** varied before it can
be read as anything stronger than a channel-bounded, instrument-relative effect-null. This
probe runs that witness-seeking control. Run record:
[`experiments/runs/2026-06-20-scivetti-let-alone-working-surface/`](../../../experiments/runs/2026-06-20-scivetti-let-alone-working-surface/README.md).

**One-line finding.** Given a **working surface** (step-by-step reasoning permitted, a
`FINAL: <digit>` tag parsed), with everything else byte-identical to session 57, the
let-alone failure is **substantially a forced-format / output-channel artifact for 2 of 3
models**: claude (0.542 → **0.792**) and gemini (0.667 → **0.917**) each jump ~25 points
on the *same items* (within-item sign test 7 gains / 1 loss, p = 0.035) to reach the
≈0.90 human native-speaker baseline. But the weakest model, **gpt-5.4-mini, does not
recover** (0.458 → 0.375, near 3-way chance) — and the post-run verifier found *why*: it
**largely declined the offered surface**, emitting bare one-token `FINAL: N` answers on
16 of 24 let-alone items (0 reasoning tokens on every item). So gpt's persistence is
**non-uptake of the channel**, not a demonstrated channel-controlled failure. The
comparative-correlative ceiling control is **PRESERVED** for all three (stays at
0.967–1.000), so the working surface did not break the instrument.

## What ran

- **Design: format-only.** The ONLY manipulated variable vs session 57 is the response
  format (forced single token → working surface). Held byte-identical: the SAME 24
  let-alone + 30 comparative-correlative test items (subset sha `9be31a8fea8d7f16`;
  full-set sha `1c5cffb18c5ef78e` == session 57's, verified — same corpus, re-cloned
  upstream @ `82699473`); the 0/1/2 NLI label *definitions* (copied verbatim from
  session-57 `NLI_SYS`); the gold labels (NOT shown); the panel; temperature 0; and
  **gemini `reasoning effort: minimal` held constant** — so the contrast isolates the
  **output channel**, not the reasoning budget (exactly as the 2026-06-19 working-surface
  witness re-run did).
- **Cells.** let-alone (n = 24) — the TARGET; comparative-correlative (n = 30) — a
  CEILING CONTROL (forced-format 1.000 / 0.900 / 1.000 in session 57).
- **Integrity.** 54 rows/model, **0 missing**, **162/162 parsed via the `FINAL:` tag**
  (0 last-digit fallbacks), **0 missing `usage.cost`**.
- **Cost** (billed `usage.cost`): **$0.3164** (claude $0.164 / gpt $0.015 / gemini
  $0.138; claude the CoT cost driver). Under the $2.50 single-run flag.
- **Governance.** A format/instrument extension under the already-ratified Scivetti
  answer-key anchor (ratified 2026-05-29) + `constructional-divergence-operationalization`;
  it does **not** change *what* is scored against the human gold (same labels, same gold)
  — only *how* the label is produced. **No new decision owed** (independent pre-run critic
  GO, fresh agent; precedent: the 2026-06-19 working-surface re-run, "format-only … no new
  decision owed"). Independent post-run verifier (fresh agent) **REPRODUCED** every
  number from raw.

## Results

Human reference (fixed, not retuned): Scivetti Exp-1 native-speaker accuracy ≈ 0.90.
3-way chance ≈ 0.33. comparative-correlative carries the **ratified anchor**; let-alone is
**descriptive** from the same human-annotated release (not individually anchored), exactly
as session 57. Within-item paired counts: `b` = forced-WRONG → working-surface-RIGHT
(gains); `c` = forced-RIGHT → ws-WRONG (losses); one-sided exact binomial on the `b+c`
discordant pairs.

### let-alone (n = 24) — the target

| model | forced (s57) | working surface | Δ | gains / losses | sign-test p | verdict | vs human 0.90 |
|---|---:|---:|---:|---:|---:|---|---|
| claude-sonnet-4.6 | 0.542 | **0.792** [0.595, 0.908] | +0.250 | 7 / 1 | 0.035 | **LIFTS** | MATCHES (CI covers 0.90) |
| gpt-5.4-mini | 0.458 | **0.375** [0.212, 0.573] | −0.083 | 2 / 4 | — | **UNCHANGED** | BELOW |
| gemini-3.5-flash | 0.667 | **0.917** [0.742, 0.977] | +0.250 | 7 / 1 | 0.035 | **LIFTS** | MATCHES (CI covers 0.90) |

### comparative-correlative (n = 30) — ceiling control

| model | forced (s57) | working surface | control guard |
|---|---:|---:|---|
| claude-sonnet-4.6 | 1.000 | 1.000 [0.886, 1.000] | **PRESERVED** |
| gpt-5.4-mini | 0.900 | 0.967 [0.833, 0.994] | **PRESERVED** |
| gemini-3.5-flash | 1.000 | 1.000 [0.886, 1.000] | **PRESERVED** |

## Interpretation (modest)

1. **The let-alone "near-chance failure" was, for the two stronger models, an
   output-channel artifact — not a competence-absence.** claude and gemini each gain 25
   points on the identical items the moment they may externalize their reasoning, with the
   gains concentrated and the sign test clearing (7 → 1 in both). This is exactly the shape
   [`essay/output-channel-confound`](../essays/output-channel-confound.md) predicts when a
   forced single-token channel masks a **serial** computation: let-alone inference is
   scalar/pragmatic (order two clauses on a scale, then compute the a-fortiori direction),
   and that multi-step work cannot be done in one emitted token. With a working surface it
   surfaces, and the inference comes out right at the human level.
2. **It refines that essay's scope claim.** The essay explicitly scoped *single-premise
   NLI* **out** of the output-channel confound ("gives the model no masked working to lose
   … there is no masked working because there is no working"). This result shows the scope
   line is not drawn at the *task* (NLI vs not) but at the *computation*: a single-premise
   NLI item whose inference is **scalar/serial** (let-alone) **does** carry masked working,
   so the channel masks it — whereas the argument-structure NLI items (who-did-what-to-whom)
   were already at ceiling in one token. NLI is not monolithically "no working." This is
   [`essay/output-channel-confound`](../essays/output-channel-confound.md) **revision trigger (a)** (a second output-channel
   masking, on a different capability) **FIRED** — corroborating the confound and sharpening
   its scope condition from "task type" to "is the inference serial."
3. **The weakest model did not take up the offered surface — so its persistence is
   channel non-uptake, NOT a clean channel-survival.** gpt-5.4-mini stays at 0.375 (≈
   chance), but the verifier showed it answered **16 of 24** let-alone items as a bare
   one-token `FINAL: N` (0 reasoning tokens on *every* item); only 3 of its 15 misses show
   any reasoning, and those 3 are genuine scalar-inference errors (it argues to "neutral"
   where the let-alone scale entails contradiction/entailment). So the channel was *opened*
   but, for gpt, largely *not used*. This is the methodologically important refinement: a
   working surface is an **affordance**, and [`essay/output-channel-confound`](../essays/output-channel-confound.md)'s **revision
   trigger (b)** (a serial negative that *survives* a widened channel) requires the model to
   externalize the computation **and still fail** — gpt mostly did not externalize, so (b)
   is **NOT cleanly fired** and stays open. gpt's let-alone failure is therefore neither
   shown channel-bounded-and-cleared (claude/gemini) nor shown channel-controlled-and-
   surviving; it is **channel-not-taken-up** — a model that answers a scalar construction in
   one token even when given room. Per
   [`essay/undischargeable-negative`](../essays/undischargeable-negative.md) it remains
   **not** a capability-absence; the clean (b) test now needs an arm that *induces uptake*
   (few-shot demonstrations of working the scale, or a forced-decomposition prompt) before
   gpt's near-chance can be read as channel-controlled.
4. **The session-57 "scalar-phrasal axis" reading is substantially revised.** The clean
   cross-model dissociation session 57 found (argument-structure at baseline, scalar-phrasal
   at chance) is **not** a content-type *competence* boundary: 2/3 models reach the human
   baseline on the scalar construction once the channel is widened. What remains is
   model-graded — the scalar construction is *channel-sensitive* (its inference is serial,
   so a one-token channel masks it) and only the weakest model fails it with room to work.
   The recurring model ordering holds: gpt-5.4-mini is again the fragile member (weakest
   overall in session 57; CONFIRM that did not replicate in the dative v2).

## What this does and does not license

**Does license:** a project-owned, revisable statement that the let-alone forced-format
near-chance result of session 57 is, for claude and gemini, **substantially an
output-channel artifact** — both reach native-speaker accuracy on the *same items* given a
working surface — while gpt-5.4-mini **largely declines the offered surface** and does not
recover. The format contrast (forced vs working surface) is a **within-model, internal
contrast**; the
per-construction accuracy-vs-0.90 leg is anchored for comp-correlative (ratified) and
descriptive for let-alone (same scoping as session 57).

**Does NOT license:**
- **A capability-absence — or even a channel-controlled negative — for gpt.** The
  undischargeable-negative discipline forbids "gpt cannot do let-alone"; and because gpt
  largely **declined** the working surface (bare one-token answers, 0 reasoning tokens), the
  wide channel was not actually exercised, so its near-chance is **not** even shown to be
  channel-controlled. It is channel-*not-taken-up*, with uptake-inducing axes (few-shot,
  forced decomposition) untried.
- **A "models have scalar-construction meaning" verdict.** Answer-key agreement under
  possible contamination (let-alone items are public; see session 57 *Limits*). The lift is
  a *channel* finding (within-item, format-vs-format) and is the robust signal here; the
  absolute match to 0.90 inherits session 57's contamination caveat.
- **A tight magnitude.** n = 24 (let-alone); the CIs are wide and the two MATCHES verdicts
  rest on CIs that *cover* 0.90, not point estimates at it (0.792, 0.917). The within-item
  sign test, not the absolute level, is the powered claim.
- **A 3/3 dissolution like the relational-composition witness.** There the wide channel
  took all three models to ceiling; here it is **2/3**, and the split (claude/gemini vs gpt)
  is real.

## Limits

- **Small N, single run/date/framing.** let-alone n = 24; one working-surface format. The
  within-item paired design removes between-item variance (so a 25-point shift is
  detectable at n = 24), but a smaller channel effect could be missed, and gpt's
  non-recovery is one framing of the wide channel.
- **Contamination (inherited).** Public items; a *match* cannot distinguish learned
  construction-meaning from memory. The robust signals are the **channel effect** (claude/
  gemini lift) and the **gpt non-recovery**, both relative contrasts.
- **One working-surface design, and uptake is not forced.** "Working surface" here is
  free-form CoT + a FINAL tag — an *affordance*, not a requirement. claude and gemini took
  it up (24/24 reasoned, CoT medians ~1040 / ~1430 chars); gpt-5.4-mini largely did not
  (16/24 bare, 0 reasoning tokens). So this design cleanly establishes the channel effect
  only for models that *use* the surface; reading gpt's persistence requires an
  uptake-inducing channel (few-shot, forced decomposition) that this run did not include.
- **Shared priors (charter §2.5).** The human baseline (Scivetti, aggregate) is the
  independent bearing for the accuracy leg; the format contrast is model-internal.

## Provenance

- Human anchor: [`resource/scivetti-2025-cxnli-dataset`](../../base/resources/scivetti-2025-cxnli-dataset.md)
  (CxNLI Exp-1 gold + ≈0.90 native-speaker baseline; ratified 2026-05-29).
  Source: [`source/scivetti-2025-beyond-memorization`](../../base/sources/scivetti-2025-beyond-memorization.md).
- Operationalization (NLI answer-key) governed by the already-ratified
  [`decisions/resolved/constructional-divergence-operationalization`](../../decisions/resolved/constructional-divergence-operationalization.md);
  the working-surface format is an instrument extension under it (no new decision owed;
  independent pre-run critic GO, fresh agent).
- Mechanism plausibility for the channel effect (serial computation needs a surface):
  [`source/li-2024-cot-serial`](../../base/sources/li-2024-cot-serial.md), via
  [`essay/output-channel-confound`](../essays/output-channel-confound.md).
- No license upstream → read in place, **not mirrored**; the working-surface CoT (which
  restates source text) is **gitignored** under `raw/cot/`; the committed artifact is
  `raw/{slot}-labels.json` (item_id + gold + label + parse_mode + content sha256 + usage,
  NO text). Numbers reproducible from the committed `raw/` + `analyze.py` + the session-57
  `raw/` against a local Scivetti clone. Independent post-run verifier (fresh agent)
  **REPRODUCED** every accuracy, Wilson CI, paired count, sign-test p-value, the billed
  cost, parse integrity, and CoT genuineness — and surfaced the uptake nuance above
  (claude/gemini 24/24 reasoned; gpt 16/24 bare one-token answers, 0 reasoning tokens; the
  committed `content_sha256` exactly binds the gitignored CoT, 0 mismatches; no gold-leak
  path into prompt or parse).

## Status

`status: proposed`, `contingent-on: []` (the governing operationalization decision and the
Scivetti anchor are both ratified). What is `proposed` is the project's reading. Promotion
past `proposed` awaits Tom's review and ideally a robustness arm on gpt's non-recovery
(few-shot / alternate framing / the disjoint train-split let-alone items — the next witness
axes the undischargeable-negative discipline names).
