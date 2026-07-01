# PREREG — the presupposition / accommodation probe

**Run:** `2026-07-01-presupposition-accommodation` · **frozen** 2026-07-01 (session 162) ·
**manifest sha** `4930d4994ea2650cffa13a539f0fd2707490975c7f895fc810710c9baa9ce15c`

Pre-registers the behavioral angle named in
[`open-question/presupposition-accommodation-corner`](../../../wiki/findings/open-questions/presupposition-accommodation-corner.md)
(opened session 161). Frozen *before* any probe call; the FREEZE GUARD in `probe.py` refuses to run
unless the manifest sha above is intact, so the item set and verdict map cannot drift after the
pre-run critic signs off. Sibling of the projection run
(`2026-07-01-presupposition-projection`): same trigger inventory shape, a **different manipulation
axis** (context support, not embedding).

## The one question (nothing wider)

> When a trigger sentence carries a **presupposition** whose backgrounded content is **not
> established** in the preceding context, does a current model **accommodate** it — treat the unmet
> content as given — and is that gated by whether the context merely leaves it open (**neutral**)
> versus explicitly **contradicts** it?

The measure is a **within-model contrast** across three CONTEXT conditions on the SAME trigger
sentence: **supported** / **neutral** / **contradicting**.

## Grounding in the source (§5 accommodation)

Follows [`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../../wiki/base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md)
§5, which introduces accommodation via Karttunen (1974: 191, quoted verbatim on the source page):
"People do make leaps and shortcuts by using sentences whose presuppositions are not satisfied in
the conversational context. […] the listener is entitled and expected to extend it as required."
Two bounds the source states are carried here: accommodation is **contested** ("among the more
contentious topics in presupposition theory", §5) and **non-uniform** ("accommodation isn't always
equally easy (or hard)", §5.1) — so the probe reads a *within-model behavioral pattern*, never a
human accommodation baseline, and expects the pattern to be graded, not all-or-nothing.

## Scope cap — LOAD-BEARING (read before citing any result)

Any labelled outcome is a **within-model behavioral contrast ONLY**. It does **not**:
- make **any human comparison** — no human accommodation baseline is claimed, measured, or needed.
  The signal is a *within-model* asymmetry across the three contexts, not a match to human
  accommodation judgments.
- certify that the model has a **semantic** representation of presupposition vs. assertion, or of
  accommodation; the contrast is behavioral (endorsement of the backgrounded content), read off
  forced-choice answers.
- adjudicate any **theory of accommodation** or the projection problem; it uses the
  context-support contrast as an operationalization, not as a claim about how accommodation works.

**Anchor discipline (surface, do not self-ratify).** The terminal `internal-contrast-only` status
this within-model design would carry is **not** self-ratified in the session that runs the probe.
When the result is written, a `wiki/decisions/open/` entry is opened
(`presupposition-accommodation-internal-contrast-anchor`) and the result carries **`anchor:
pending`** contingent on it, until an **independent later session** ratifies (charter §12.3). This
run opens that decision; it does not close it.

## Panel & settings

Panel per [`config/models.md`](../../../config/models.md): `panel.A` = anthropic/claude-sonnet-4.6,
`panel.B` = openai/gpt-5.4-mini, `panel.C` = google/gemini-3.5-flash. Temperature 0; one date;
zero-shot; text-only, single-turn (no tools); gemini `reasoning={"effort":"minimal"}`
(config/models.md caveat); billed `usage.cost` recorded. The system prompt ("You are a careful
reader. Answer the user's question directly.") never mentions presupposition, accommodation, or the
"right" answer.

## Design — 12 base scenarios × 3 context conditions = 36 item-conditions

`prep.py` freezes the items (the project's OWN synthetic items — no external corpus). Four trigger
families, three scenarios each (SEP §1.1 inventory), matching the sibling projection run:

| family | trigger | presupposition P (the backgrounded content) |
|--------|---------|----------------------------------------------|
| **factive** | realize / discover / know | the complement fact |
| **aspectual** | stop / continue / resume | the prior state |
| **definite** | definite description / possessive / relative-clause definite | existence of the referent |
| **cleft** | it-cleft | the existential ("someone Y-ed") |

Each scenario has ONE **trigger** sentence (carries P, held **constant** across conditions) and
three one-sentence **contexts** that precede it (full discourse = context + " " + trigger):

| condition | context sentence | role |
|-----------|------------------|------|
| **supported** | explicitly STATES P | manipulation check / SANITY floor — P is literally asserted, so a reader who cannot endorse it cannot read the text (control failure, not accommodation) |
| **neutral** | topic-adjacent, bears on P NEITHER way | the ACCOMMODATION test — with P unestablished but unopposed, does the model supply it? |
| **contradicting** | explicitly DENIES P | the GATE — does the model DECLINE to accommodate an explicitly-denied presupposition, rather than endorsing regardless? |

Each item is one forced-choice completion: *"Consider only the following text: '<context>
<trigger>'. Taking that text at face value, does it follow that: <P>? Answer with exactly one word —
YES, NO, or UNCLEAR."* The three-way choice lets a model that will not accommodate answer UNCLEAR
(or NO under contradiction) rather than be forced to a YES. `endorsed` == answer parses to YES
(`analyze.py`).

**The context-gated-accommodation signature.** P endorsed in **supported** (retrieval) AND in
**neutral** (accommodation), but DROPPED in **contradicting** (the gate). Endorsing in **all three**
(including contradicting) is a **blanket yes-bias**, not accommodation; endorsing in **none** (not
even neutral) is **no accommodation**. Supported is the built-in SANITY control: a model that will
not endorse P even when a prior sentence literally states it has an uninterpretable
neutral/contradicting profile (control failure), the same guard role the projection probe's plain
frame played.

## Metrics (pre-specified, direction fixed)

Per model, from the parsed answers (`analyze.py`):
- **supported_endorse** — P-endorse rate in the supported context (sanity floor).
- **neutral_endorse** — P-endorse rate in the neutral context (the accommodation rate).
- **contradicting_endorse** — P-endorse rate in the contradicting context (should be LOW if gated).
- **accommodation_gap** = neutral_endorse − contradicting_endorse (the within-model gating signal).
- per-family endorse rates per condition (descriptive; enables a later family decomposition).

## Verdict map (thresholds fixed NOW; may be tightened, never loosened)

```
SANITY   = 0.75   per-model supported_endorse floor; below it a model is control-FAILED.
ACCOM    = 0.60   per-model neutral_endorse floor to count as "accommodates".
GAP      = 0.30   per-model accommodation_gap floor for context-GATING.
FLATBAND = 0.15   per-model |accommodation_gap| below which neutral ≈ contradicting (no gating).
LOWACC   = 0.40   per-model neutral_endorse ceiling below which the model does NOT accommodate.
```

Per-model label (sanity_ok required):
- **gated_accommodation** — neutral_endorse ≥ ACCOM AND accommodation_gap ≥ GAP.
- **blanket_yes** — neutral_endorse ≥ ACCOM AND |accommodation_gap| < FLATBAND.
- **no_accommodation** — neutral_endorse < LOWACC.

Panel verdict:
- **GATED-ACCOMMODATION** — ≥ 2 of 3 sanity-passing models are gated_accommodation.
- **BLANKET-YES** — ≥ 2 of 3 sanity-passing models are blanket_yes.
- **NO-ACCOMMODATION** — ≥ 2 of 3 sanity-passing models are no_accommodation.
- **MIXED** — anything else (sanity failures, split panel, or partial signal).

Every outcome is first-class. **BLANKET-YES** and **NO-ACCOMMODATION** are honest nulls on the
context-gated-accommodation reading and are written as such (charter §4). Sanity failure voids the
strong reading and is reported honestly.

## Cost

36 conditions × 3 models = 108 single-turn, single-word completions — smaller than the projection
run's 288-call battery (which billed **$0.0486**). Pre-flight expectation here is **≈ $0.02–0.06**
(gemini's minimal-reasoning tokens dominate). `ABORT_USD = 1.00` hard-stops a runaway; the run is
far under the $2.50 single-run flag and the $5.00/day cap. A real pre-flight (`--limit` on one
model) is measured and recorded before the full run.

## What each outcome would feed

- **GATED-ACCOMMODATION** → a within-model behavioral finding that current decoders supply an unmet
  presupposition when the context permits it but withhold it under explicit contradiction — the
  accommodation asymmetry the §5 material describes (with the `internal-contrast-only` caveat and
  the pending anchor decision). Would seed a projection+accommodation bridging essay.
- **BLANKET-YES** → the models endorse backgrounded content regardless of context; the neutral
  endorsement is a yes-bias, not accommodation. Written as a null on the gating reading.
- **NO-ACCOMMODATION** → the models do not supply an unestablished presupposition at all. Written as
  a null.
- **MIXED / sanity failure** → the forced-choice instrument or item set is confounded, or the panel
  splits; reported as such, no accommodation claim made.
