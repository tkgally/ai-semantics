# PREREG — presupposition doppelgänger (matched surface-cue) control

**Run:** `2026-07-03-presupposition-doppelganger` · **session 173** · program item **A1a**.
**Frozen manifest sha:** `4500fc5b2c66a6d35355ed80b6f7d7a60090ce80476cf8faf0533ac8d97a183a` (prep.py `--check`).
**Design of record:** [`design/presupposition-doppelganger-control-v1`](../../designs/presupposition-doppelganger-control-v1.md).
**Ratified gate:** [`decisions/resolved/presupposition-doppelganger-control-design`](../../../wiki/decisions/resolved/presupposition-doppelganger-control-design.md)
(opened s172, **ratified s173** — autonomous adversarial review, RATIFY-WITH-NIT, + one non-Anthropic
panel vote; the vote dissented REJECT and was weighed and rebutted, see the resolved decision page).

## The one question (nothing wider)

The presupposition/projection corner behaves within-model as if the model **follows the trigger's
surface cue**: the presupposition survives negation, collapses under the conditional antecedent
([`result/presupposition-projection-v1`](../../../wiki/findings/results/presupposition-projection-v1.md)),
and is context-gated in accommodation
([`result/presupposition-accommodation-v1`](../../../wiki/findings/results/presupposition-accommodation-v1.md)).
Does that behavior beat a **matched surface-cue doppelgänger** — items carrying the *same* trigger
word-form and local frame but **without** the presuppositional structure — or does the doppelgänger
endorse the same content just as much (a **measured** shadow-saturated corner)?

The measure is a **within-model residual**: `trigger P-endorse − D1 doppelgänger P-endorse`, over the
two PROJECTING frames (negation + question) where the trigger projects.

## THE TWO OUTCOMES ARE NOT EPISTEMICALLY SYMMETRIC — read before citing (B1/B2)

- **NULL residual (trigger ≈ doppelgänger) = SHADOW-SATURATED** is the **cleanly-licensed, diagnostic**
  outcome: the model endorses `P` equally for "didn't realize that S" and "didn't suspect that S", i.e.
  it is not tracking factivity/presuppositional structure — a genuine shadow-saturated signature that
  soundly supports the essay's placement. **This is the higher-value, first-class MEASURED result**
  (charter §4). It converts the essay's *reading* into a measured saturated row.
- **POSITIVE residual is UNDER-LICENSED** and does **not** show "presupposition beats the distributional
  shadow." A verb-sensitive surface-cue follower — which any distributional next-token learner is, since
  `realize`/`suspect` differ distributionally — produces a positive D1 residual because **D1 varies the
  WORD**. The decisive disanalogy with the comparative-correlative beater: CC clears controls that reuse
  the **same words** and vary only the construction; D1 (factive/aspectual) varies the word. So a
  positive residual shows at most that endorsement is **keyed to the trigger word-form above bare
  complement presence** — itself distributionally encoded. It **warrants re-examination** (weighted toward
  the **cleft** family, the one leg holding content words constant) and does **NOT** fire the essay's
  first revision trigger, which requires a residual a surface-cue account *cannot* reconstruct, held
  stably across frames.

**Calibration (ratification note, s173):** projection-v1 shows the models *do* track projection under
negation and factivity is distributionally salient, so a **positive/BEATS or MIXED residual is at least
as likely as the null.** The "null is the prize" language above is **value-if-obtained, not a
prediction.** The probe is well-posed either way.

## Design (frozen — see prep.py)

Project's own synthetic items (no external corpus). **Four trigger families** (SEP §1.1 inventory):

| family | scenarios | powered? | trigger → D1 doppelgänger | target P |
|--------|-----------|----------|---------------------------|----------|
| factive | 6 | **yes** | factive `realized/knew/…that S` → non-factive `suspected/believed/…that S` | S |
| aspectual | 6 | **yes** | `stopped/resumed/continued V-ing` → `considered V-ing` (gerund held constant) | prior state |
| cleft | 6 | **yes** | it-cleft `It was X who Y-ed` → plain assertion `X Y-ed` (same content words) | existential "someone Y-ed" |
| definite | 4 | **NO (S1)** | definite `the X who…` → intensional/indefinite `looking for an X to…` | existence |

Each scenario yields a **trigger leg** and a **D1 doppelgänger leg**, each embedded under **4 frames**
(plain / negation / question / conditional), plus a **D2** structure-defeat leg (the trigger word-form
kept, presupposition defeated by a metalinguistic/quotation framing; single sentence, descriptive).
Item form is one forced choice identical to the sibling runs: *"Consider only the following statement:
'⟨sentence⟩'. Taking that statement at face value, does it follow that: ⟨P⟩? Answer with exactly one
word — YES, NO, or UNCLEAR."* `endorsed` == parses to YES (analyze.py).

- **Total item-conditions/model:** 22 scenarios × (2 legs × 4 frames + 1 D2) = **198** (594 calls / panel).
- **Powered, verdict-bearing residual N (S3, honest count):** only the two projecting frames of the
  three powered families carry the residual → **72 residual-bearing conditions/model** (36 trigger + 36
  doppelgänger; ~18 obs/leg/family/model). **NOT 198, and NOT 128.** ~6× the founding 3-per-family pilot,
  adequate for direction-of-effect, well under the spend flag.

### Binding conditions honored (from the ratified decision)

- **S1** — the **definite family is dropped from the powered/verdict-bearing residual** (`powered=False`
  in prep.py; analyze.py excludes it from all verdicts). Its D1 is not a matched control (trigger and
  doppelgänger share almost no surface material). Carried **exploratory/descriptive only**.
- **S2** — **per-family reported as PRIMARY** (heterogeneous control types); pooled-powered residual
  **secondary**. The **cleft** family is the sole construction-grain leg (B1 exception) and carries the
  most interpretable signal.
- **S3** — honest N as above; any citation uses the **residual-bearing N (~72 → 36/leg)**, never 198/128.
- **S4** — analyze.py reports **verdict-map sensitivity** under RESID ∈ {0.25, 0.30, 0.35} × FLATBAND ∈
  {0.10, 0.15, 0.20}.
- **N1** — a sanity failure may reduce the panel to 2; analyze.py flags any 2/2 verdict.
- **N2** — dropping the conditional frame from the primary **raises** trigger_project and works **against**
  the preferred null (not a positive-hunt); the conditional is reported as `conditional_residual`.

**Frame restriction is PRE-REGISTERED, not post-hoc.** Pooling the primary residual over negation +
question (excluding the conditional) is grounded in projection-v1's already-published conditional
collapse (P-survival 0.42 / 0.17 / 0.17, verified in that run's `results.json`; 2026-07-01, predates
this design 2026-07-03). Fixed before any call.

## Metrics (analyze.py, pre-specified, direction fixed)

Per model, per family and pooled over the powered families:
`trigger_project` (trigger P-endorse over neg+question), `doppel_project` (D1 doppel over the same),
`residual = trigger_project − doppel_project`. Descriptive: `conditional_residual`, `plain_doppel_endorse`,
`d2_residual = trigger_project − d2_endorse`, and the exploratory `definite` residual.

## Verdict map (thresholds fixed NOW; may be tightened, never loosened)

```
SANITY   = 0.60   per-model trigger_project floor (projecting frames); below it a model is control-FAILED.
RESID    = 0.30   per-model residual floor to count as "beats the doppelgänger".
FLATBAND = 0.15   per-model |residual| below which trigger ≈ doppelgänger (shadow-saturated).
```

- **BEATS-DOPPELGANGER** — ≥ 2/3 sanity-passing models `residual ≥ RESID`. → endorsement **keyed to the
  trigger word-form above bare complement presence**. NOT "beats the distributional shadow", NOT a move
  to the beater side (B1); warrants re-examination (cleft-weighted); does not fire the essay's trigger.
- **SHADOW-SATURATED (FLAT)** — ≥ 2/3 sanity-passing models `|residual| < FLATBAND`. → the doppelgänger
  endorses the same content just as much; the cleanly-licensed **measured saturated row** (charter §4).
- **MIXED** — anything else (sanity failure / split panel / partial signal). No shadow claim.

Computed **per family (primary)** and **pooled (secondary)**. A control failure (trigger does not
reproduce projection) voids the strong reading and is reported.

## Scope cap — LOAD-BEARING (read before citing any result)

Any labelled outcome is a **within-model behavioral contrast ONLY**, mirroring the two sibling runs. It
makes **no human comparison** (no human projection/doppelgänger baseline is claimed, measured, or
needed), does not certify that the model **represents** a presupposition/assertion split, and does not
adjudicate the projection problem. **Anchor discipline:** the result carries `anchor: pending` →
eventual `internal-contrast-only` (surfaced via the resolved doppelgänger decision, **not**
self-ratified in this run session).

## Grounding in the source (SEP §1.1–§1.3)

From [`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../../wiki/base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md),
used **only** as the a-priori map of which constructions trigger presuppositions (never a human
baseline). The doppelgänger substitutions are the **project's own construction** (the complement of the
source's trigger inventory: a non-factive for a factive, etc.); that the substitutes are non-presupposing
is standard linguistic knowledge, carried at the project's own risk, not attributed to the source.

## Cost (pre-flight)

594 single-word completions. Comparator: the projection battery (288 calls) billed $0.0486
(`usage.cost`-summed) ≈ $0.000169/call → **≈ $0.06–0.20** billed (gemini minimal-reasoning tokens
dominate the variance). `ABORT_USD = 1.00` hard-stops a runaway. A `--limit` pre-flight on one model is
measured and recorded before the full run.

## Files

- `prep.py` — frozen stimulus set + FREEZE GUARD (manifest sha above). `--check` / `--dump`.
- `items.json` — the 198 dumped item-conditions.
- `probe.py` — the ONLY API caller (text-only, temp 0, gemini reasoning minimal). Writes `raw/*.json`.
- `analyze.py` — scoring + pre-registered verdict + S4 sensitivity (NO API calls). Writes `results.json`.
- `raw/` — per-model raw answers.
