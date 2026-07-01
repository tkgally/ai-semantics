# PREREG — the projection trigger-inventory probe

**Run:** `2026-07-01-projection-trigger-inventory` · **frozen** 2026-07-01 (session 160) ·
**manifest sha** `d0aa515e239413cda77a9b3968af56f95ae05be59ba32761ef3dd5ec6fa17b59` (pinned by the orchestrator after the pre-run critic signed off, session 160)

A **generalization test** of the session-158 projection probe
(`2026-07-01-presupposition-projection`). That run measured, within a model, whether a
**presupposition** projects (survives negation / question / conditional-antecedent embedding)
*more than* a **matched ordinary entailment**, across four trigger families (factive / aspectual /
definite / cleft). This run asks the same question with the same instrument for **four additional
trigger families the source explicitly names** — temporal clauses, manner adverbs, focus/exclusive
*only*, and presuppositional quantifiers — to test whether the s158 PROJECTION verdict generalizes.

Frozen *before* any probe call; the FREEZE GUARD in `probe.py` refuses to run unless the manifest
sha (pinned in `prep.py`) is intact, so the item set and verdict map cannot drift after the pre-run
critic signs off.

**This run REUSES the s158 measurement path.** The system prompt (`SYS`), the query wrapper
(`QUERY`), the four `FRAMES`, `build_items()`/`manifest_sha()`, the whole of `probe.py` and
`analyze.py`, and the verdict thresholds are **identical** to s158. The ONLY difference is the 12
base scenarios. Because the scoring path is byte-for-byte the same measurement, the ratified
`internal-contrast-only` argument for s158 transfers to this run.

## The one question (nothing wider)

> When a base sentence is embedded under an entailment-cancelling operator (negation / a polar
> question / a conditional antecedent), does a current model treat the base's **presupposition** as
> **surviving** (projecting) *more than* a **matched ordinary entailment** on the same base — the
> literature's "hallmark of presuppositions" (SEP §1.2) — **across four additional source-named
> trigger families** (temporal / manner / only / quantifier) beyond the four s158 already tested?

The measure is a **within-model contrast** between two legs of the same base: the presupposition
(P) leg vs. the matched entailment (E) leg, each queried across the four frames.

## Trigger inventory — grounded verbatim in the source

The four families here are drawn from the trigger list the source names immediately after the four
s158 families. From [`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../../wiki/base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md)
(§1.1), verbatim:

> "The list continues with temporal clauses ('before', 'after', 'since'), manner adverbs, sortally
> restricted predicates ('bachelor'), quantifiers, names, and intonation (focus, contrast)."

This run lexicalizes four of those classes: **temporal clauses** (before / after / since),
**manner adverbs**, **intonation (focus, contrast)** — lexicalized as *only* — and **quantifiers**.
The behavioral diagnostic is unchanged; the source's characterization of it (§1.2), verbatim:

> "The hallmark of presuppositions, as well as the most thoroughly studied presuppositional
> phenomenon, is _projection_ (Langendoen and Savin, 1971)."

and, on what projection is:

> "In all these examples, sentence (2) is embedded under various operators. What is notable is that
> whereas the statements in (4) do not follow from any of these embeddings (and would not be
> expected to follow according to classical logics), the presuppositions do follow. We say that the
> presuppositions are _projected_."

The source is explicit that projection is **defeasible, not absolute** (§1.3): "Presuppositions
typically project, but often do not …". So the human pattern this probe operationalizes is graded,
not a clean survival-under-all-embeddings rule — a bound carried into the reading of any result.

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
(`projection-trigger-inventory-internal-contrast-anchor`) and the result carries **`anchor:
pending`** contingent on it, until an **independent later session** ratifies (charter §12.3). This
run opens that decision; it does not close it. (The scoring path being identical to s158, the s158
internal-contrast argument transfers — but ratification is still a later-session act, never
self-applied here.)

## Panel & settings

Panel per [`config/models.md`](../../../config/models.md): `panel.A` = anthropic/claude-sonnet-4.6,
`panel.B` = openai/gpt-5.4-mini, `panel.C` = google/gemini-3.5-flash. Temperature 0; one date;
zero-shot; text-only, single-turn (no tools); gemini `reasoning={"effort":"minimal"}`
(config/models.md caveat); billed `usage.cost` recorded. The system prompt
("You are a careful reader. Answer the user's question directly.") never mentions presupposition,
projection, or the "right" answer. (All settings IDENTICAL to s158.)

## Design — 12 matched base scenarios x 2 targets x 4 frames = 96 item-conditions

`prep.py` freezes the items (the project's OWN synthetic items — no external corpus). Four trigger
families, three scenarios each (SEP §1.1 inventory, the four families beyond s158's set):

| family | trigger | presupposition P (projects) | matched entailment E (cancels) |
|--------|---------|------------------------------|--------------------------------|
| **temporal** | temporal clause (before / after / since) | the subordinate-clause event happened | the main-clause event (the ordinary assertion) |
| **manner** | manner adverb (reluctantly / cleverly / loudly) | the underlying action occurred (the VP happened) | the manner property held (it was done in that manner) |
| **only** | focus/exclusive *only* (intonation: focus, contrast) | the prejacent (the focused subject did the thing) | the exhaustive claim (no one other than the focus did it) |
| **quantifier** | both / neither / each of the two | the existence/cardinality presupposition (the two-member set exists) | the scopal predication (the predicate held of them) |

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

**Known weak pairs (flagged for the pre-run critic).** Two families carry a softer projection
prediction than the s158 set and should be read with that caveat:
- **manner** — negating a manner adverb ("Owen didn't reluctantly sign the contract") is genuinely
  scope-ambiguous: the projecting reading (he signed, just not reluctantly) competes with a
  "he didn't sign at all" reading. The projection prediction is weaker here than for factives.
  The question/conditional frames project the VP-occurrence more cleanly than negation does.
- **only** — the negation frame is written as "X wasn't the only one who …", which carries the
  prejacent (X did it) as an entailment/presupposition of the relative-clause structure; this is
  the standard prejacent-projection reading, but the exact endorsement can vary by how a model
  scopes "not … only". The E leg (exhaustivity) should cancel cleanly under all three frames.

These are honest bounds, not defects: the design still tests whether P survives *more than* the
matched E within each model, and per-family per-frame rates are reported so a soft pair shows up
rather than being hidden in the aggregate.

## Metrics (pre-specified, direction fixed)

Per model, from the parsed answers (`analyze.py` — IDENTICAL to s158):
- **plain_presup_endorse / plain_entail_endorse** — P- and E-endorse rate in the plain frame
  (sanity floors).
- **presup_survival** — P-endorse rate over the 3 cancelling frames (should be HIGH if P projects).
- **entail_survival** — E-endorse rate over the 3 cancelling frames (should be LOW if E cancels).
- **projection_gap** = presup_survival − entail_survival (the within-model projection signal).
- per-frame P/E endorse rates (descriptive; shows *which* embedding, if any, breaks projection).

## Verdict map (thresholds fixed NOW; may be tightened, never loosened — IDENTICAL to s158)

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
s158 run of this exact instrument, and the 288-call add-arm calibration billed **$0.068**; a
72-call battery billed **$0.017**. Pre-flight expectation here is **≈ $0.05–0.15** (gemini's
minimal-reasoning tokens dominate). `ABORT_USD = 1.00` hard-stops a runaway; the run is far under
the $2.50 single-run flag and the $5.00/day cap. A real pre-flight (`--limit` on one model) is
measured and recorded before the full run.

## What a positive / null would feed

- **PROJECTION** → supports generalization of the s158 within-model projection asymmetry to the new
  families; a within-model behavioral finding that current decoders reproduce the projection
  asymmetry across a wider slice of the source's trigger inventory (with the
  `internal-contrast-only` caveat and the pending anchor decision).
- **FLAT / NULL** → the models treat presupposition and matched entailment alike under embedding in
  these families; written as a null, and a bound on the s158 generalization.
- **MIXED / sanity failure** → the forced-choice instrument or item set is confounded for these
  families (the flagged manner/only weak pairs are the first suspects); reported as such, no
  projection claim made.
