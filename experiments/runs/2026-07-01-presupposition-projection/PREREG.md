# PREREG — the presupposition / projection probe

**Run:** `2026-07-01-presupposition-projection` · **frozen** 2026-07-01 (session 158) ·
**manifest sha** `e3a04cdd7e3ebbc955b916c15c7d11349ee4d5eb2dbf612c5de12cc1cf6877f9`

Pre-registers the behavioral angle named in
[`open-question/presupposition-projection-corner`](../../../wiki/findings/open-questions/presupposition-projection-corner.md)
(opened session 157) and the bet stated in
[`conjecture/presupposition-projection-vs-entailment`](../../../wiki/findings/conjectures/presupposition-projection-vs-entailment.md).
Frozen *before* any probe call; the FREEZE GUARD in `probe.py` refuses to run unless the manifest
sha above is intact, so the item set and verdict map cannot drift after the pre-run critic signs off.

## The one question (nothing wider)

> When a base sentence is embedded under an entailment-cancelling operator (negation / a polar
> question / a conditional antecedent), does a current model treat the base's **presupposition** as
> **surviving** (projecting) *more than* a **matched ordinary entailment** on the same base — the
> literature's "hallmark of presuppositions" (SEP §1.2)?

The measure is a **within-model contrast** between two legs of the same base: the presupposition
(P) leg vs. the matched entailment (E) leg, each queried across the four frames.

## Scope cap — LOAD-BEARING (read before citing any result)

A positive is a **within-model behavioral contrast ONLY**. It does **not**:
- make **any human comparison** — no human projectivity / projection-judgment baseline is claimed,
  measured, or needed. The signal is *P survives more than E within the same model*, not *the model
  matches human projection judgments*.
- certify that the model has a **semantic** representation of presupposition vs. assertion; the
  contrast is behavioral (endorsement of an inference under embedding), read off forced-choice
  answers.
- adjudicate the **projection problem** or any theory of presupposition; it uses the projection
  diagnostic as an operationalization, not as a claim about how projection works.

**Anchor discipline (surface, do not self-ratify).** The terminal `internal-contrast-only` status
this within-model design would carry is **not** self-ratified in the session that runs the probe.
When the result is written, a `wiki/decisions/open/` entry is opened
(`presupposition-projection-internal-contrast-anchor`) and the result carries **`anchor: pending`**
contingent on it, until an **independent later session** ratifies (charter §12.3). This run opens
that decision; it does not close it.

## Panel & settings

Panel per [`config/models.md`](../../../config/models.md): `panel.A` = anthropic/claude-sonnet-4.6,
`panel.B` = openai/gpt-5.4-mini, `panel.C` = google/gemini-3.5-flash. Temperature 0; one date;
zero-shot; text-only, single-turn (no tools); gemini `reasoning={"effort":"minimal"}`
(config/models.md caveat); billed `usage.cost` recorded. The system prompt
("You are a careful reader. Answer the user's question directly.") never mentions presupposition,
projection, or the "right" answer.

## Design — 12 matched base scenarios x 2 targets x 4 frames = 96 item-conditions

`prep.py` freezes the items (the project's OWN synthetic items — no external corpus). Four trigger
families, three scenarios each (SEP §1.1 inventory):

| family | trigger | presupposition P (projects) | matched entailment E (cancels) |
|--------|---------|------------------------------|--------------------------------|
| **factive** | realize / discover / know | the complement fact | the subject's coming-to-know / awareness |
| **aspectual** | stop / continue / resume | the prior state | the current state |
| **definite** | definite description / relative-clause definite | existence of the referent | the main predication |
| **cleft** | it-cleft | the existential ("someone Y-ed") | the exhaustive identification ("X specifically Y-ed") |

Each base is embedded under **four frames** and each framed sentence is queried against **both**
targets (P and E):

| frame | class | role |
|-------|-------|------|
| **plain** | non-cancelling | SANITY baseline — both P and E should be endorsed when the base is plainly asserted |
| **negation** | cancelling | canonical "negation test" (SEP §1.2) |
| **question** | cancelling | polar-question embedding (SEP §1.2) |
| **conditional** | cancelling | conditional-antecedent embedding (SEP §1.2) |

Each item is one forced-choice completion: *"Consider only the following statement: '<framed
sentence>'. Taking that statement at face value, does it follow that: <target>? Answer with exactly
one word — YES, NO, or UNCLEAR."* The three-way choice lets a cancelled entailment be marked
UNCLEAR rather than forced to a false YES. `endorsed` == answer parses to YES (`analyze.py`).

**The projection signature.** P endorsed across ALL four frames (survives the three cancelling
frames); E endorsed in the PLAIN frame but DROPPED under the three cancelling frames. Both legs
endorsed in the plain frame is the built-in **sanity control**: a model that will not endorse P or E
even when the base is plainly asserted has an uninterpretable cancelling-frame profile (control
failure) — the same guard role the origo probe's anchored-control arm played.

## Metrics (pre-specified, direction fixed)

Per model, from the parsed answers (`analyze.py`):
- **plain_presup_endorse / plain_entail_endorse** — P- and E-endorse rate in the plain frame
  (sanity floors).
- **presup_survival** — P-endorse rate over the 3 cancelling frames (should be HIGH if P projects).
- **entail_survival** — E-endorse rate over the 3 cancelling frames (should be LOW if E cancels).
- **projection_gap** = presup_survival − entail_survival (the within-model projection signal).
- per-frame P/E endorse rates (descriptive; shows *which* embedding, if any, breaks projection).

## Verdict map (thresholds fixed NOW; may be tightened, never loosened)

```
SANITY  = 0.75   per-model plain-frame floor on BOTH P and E; below it a model is control-FAILED.
SURVIVE = 0.60   per-model presup_survival floor for a projection reading.
GAP     = 0.30   per-model projection_gap floor for a projection reading.
FLATBAND= 0.15   per-model |projection_gap| below which the two legs are flat (no projection).
```

- **PROJECTION** — ≥ 2 of 3 models pass SANITY AND have presup_survival ≥ SURVIVE AND
  projection_gap ≥ GAP.
- **FLAT / NULL** — ≥ 2 of 3 models pass SANITY AND have |projection_gap| < FLATBAND (the
  presupposition leg does **not** project above the matched-entailment leg).
- **MIXED** — anything else (sanity failures, split panel, or partial signal).

A null (FLAT) is a first-class result and is written as such (charter §4). Sanity failure is a
control-failure outcome that voids the strong reading, reported honestly (as the origo probe's
anchored-control failure was).

## Cost

96 conditions × 3 models = 288 single-turn, single-word completions. Historical comparators: the
288-call add-arm calibration billed **$0.068**; a 72-call battery billed **$0.017**. Pre-flight
expectation here is **≈ $0.05–0.15** (gemini's minimal-reasoning tokens dominate). `ABORT_USD =
1.00` hard-stops a runaway; the run is far under the $2.50 single-run flag and the $5.00/day cap.
A real pre-flight (`--limit` on one model) is measured and recorded before the full run.

## What a positive / null would feed

- **PROJECTION** → supports the conjecture; a within-model behavioral finding that current decoders
  reproduce the projection asymmetry the semantics literature documents (with the `internal-contrast-only`
  caveat and the pending anchor decision).
- **FLAT / NULL** → falsifies the conjecture's bet; the models treat presupposition and matched
  entailment alike under embedding — written as a null.
- **MIXED / sanity failure** → the forced-choice instrument or item set is confounded; reported as
  such, no projection claim made.
