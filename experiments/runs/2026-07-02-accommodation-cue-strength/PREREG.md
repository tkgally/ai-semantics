# PREREG — the accommodation / cue-strength probe

> **FROZEN DESIGN — NOT YET RUN.** Awaiting an independent pre-run-critic GO and a run session
> (164+). **No API call has been made.** The committed run dir is design-only: `PREREG.md`,
> `README.md`, `prep.py`, `probe.py`, `analyze.py`, `items.json` — no `raw/`, no `results.json`.

**Run:** `2026-07-02-accommodation-cue-strength` · **frozen** 2026-07-02 · **manifest sha**
`55ad85693de0b1f343d28b810cf06e0b09316559abcbc490d2fd881ead55a36a`

Follow-up to [`result/presupposition-accommodation-v1`](../../../wiki/findings/results/presupposition-accommodation-v1.md)
(run `2026-07-01-presupposition-accommodation`, verdict GATED-ACCOMMODATION 3/3). Tests the
**cue-strength arm** of
[`conjecture/presupposition-environment-gated-both-directions`](../../../wiki/findings/conjectures/presupposition-environment-gated-both-directions.md).
Frozen *before* any probe call; the FREEZE GUARD in `probe.py` refuses to run unless the manifest sha
above is intact, so the item set and verdict map cannot drift after the pre-run critic signs off.

## The one question (nothing wider)

> v1 found a **partial** accommodation gate: under a single "contradicting" context the panel still
> endorsed the explicitly-denied presupposition **a third to a half of the time**
> (contradicting-endorse 0.33 / 0.58 / 0.42). Is that gate **graded by cue strength** — does a
> **stronger** surface contradiction gate **harder** (lower endorsement) than a **weaker** one?

The measure is a **within-model contrast** across four CONTEXT conditions on the SAME trigger
sentence: **supported** / **neutral** / **weak_contra** / **strong_contra**. The new signal is
`strength_gradient = weak_contra_endorse − strong_contra_endorse` (positive ⇒ stronger gates harder).

This is exactly the conjecture's stated **confirming** evidence: "Accommodation's partial gate turning
out to be **graded by cue strength** (a stronger surface contradiction gates harder), paralleling
projection's graded frame effect." A **flat** gate (weak ≈ strong) is the honest **null** on that arm
— a partial falsifier of the graded-cue reading (the gate would be on/off, not graded).

## Grounding in the source (§5 accommodation)

Follows [`source/beaver-geurts-denlinger-2021-presupposition-sep`](../../../wiki/base/sources/beaver-geurts-denlinger-2021-presupposition-sep.md)
§5, which introduces accommodation via Karttunen (1974: 191, quoted verbatim on the source page):
"the listener is entitled and expected to extend [the context] as required." The source also states
accommodation is **contested** (§5) and **non-uniform** — "accommodation isn't always equally easy
(or hard)" (§5.1). The graded-by-strength hypothesis is a direct within-model reading of that
non-uniformity: if a hedged denial and a categorical denial gate to different degrees, the gate is
graded, not all-or-nothing. The source enters only as an a-priori map of *where* the phenomenon is
environment-sensitive, **never** as a human baseline.

## Scope cap — LOAD-BEARING (read before citing any result)

Any labelled outcome is a **within-model behavioral contrast ONLY**. It does **not**:
- make **any human comparison** — no human accommodation baseline is claimed, measured, or needed.
  The signal is a *within-model* asymmetry across the four contexts.
- certify that the model has a **semantic** representation of presupposition/assertion or of
  accommodation; the contrast is behavioral (endorsement of backgrounded content), read off
  forced-choice answers.
- adjudicate any **theory of accommodation**; it uses the context-strength contrast as an
  operationalization.

**The v1 alternative reading carries over, sharpened.** v1's pre-run critic noted the gate leg cannot
behaviorally separate genuine accommodation-*blocking* from generic **contradiction-detection +
yes-bias**. This follow-up does **not** dissolve that ambiguity — but it does add a discriminating
texture: a mechanism that is *pure* contradiction-detection (any explicit ¬P → NO) predicts weak and
strong denials gate **equally** (both contain an explicit ¬P) → a **FLAT** gate; a mechanism sensitive
to *surface cue strength* predicts a **graded** gate. So GRADED-GATE vs FLAT-GATE is itself
informative about which description fits, within the `internal-contrast-only` fence. This is a reading
of the within-model contrast, **not** a claim the model computes accommodation.

**Anchor discipline — `anchor: internal-contrast-only`, INHERITED (no new decision).** This design's
terminal status is `internal-contrast-only`, **inheriting** the already-ratified precedent
[`decisions/resolved/presupposition-accommodation-internal-contrast-anchor`](../../../wiki/decisions/resolved/presupposition-accommodation-internal-contrast-anchor.md)
(opened session 162, ratified session 163 by an independent fresh-agent adversarial review). The
scoring path is identical in kind to v1 — every quantity feeding the verdict is a within-model
endorsement rate over the model's own YES/NO/UNCLEAR answers, with **no human key** — so the same
terminal declaration applies and **no new `wiki/decisions/open/` entry is opened**. The run session
writes the result carrying `anchor: internal-contrast-only` and cites this inherited precedent; it
does **not** self-ratify anything new.

## Panel & settings

Panel per [`config/models.md`](../../../config/models.md): `panel.A` = anthropic/claude-sonnet-4.6,
`panel.B` = openai/gpt-5.4-mini, `panel.C` = google/gemini-3.5-flash. Temperature 0; text-only,
single-turn (no tools); zero-shot; gemini `reasoning={"effort":"minimal"}` (config/models.md caveat);
billed `usage.cost` recorded. The system prompt ("You are a careful reader. Answer the user's question
directly.") — reused **verbatim** from v1 — never mentions presupposition, accommodation, or the
"right" answer. The forced-choice QUERY wrapper is also verbatim v1.

## Design — 12 base scenarios × 4 context conditions = 48 item-conditions

`prep.py` freezes the items (the project's OWN synthetic items — no external corpus). Reuses the SAME
12 v1 scenarios: four trigger families, three each, with the **trigger sentence and presupposition P
held constant, verbatim from v1**:

| family | trigger | presupposition P (the backgrounded content) |
|--------|---------|----------------------------------------------|
| **factive** | realize / discover / know | the complement fact |
| **aspectual** | stop / continue / resume | the prior state |
| **definite** | definite description / possessive / relative-clause definite | existence of the referent |
| **cleft** | it-cleft | the existential ("someone Y-ed") |

Each scenario holds ONE **trigger** (carries P, constant across conditions) and precedes it with a
one-sentence **context** (full discourse = context + " " + trigger). **Four** conditions (was three
in v1 — the added grade splits v1's single contradiction into weak/strong):

| condition | context sentence | role | provenance |
|-----------|------------------|------|-----------|
| **supported** | explicitly STATES P | SANITY / retrieval floor | **verbatim v1** |
| **neutral** | topic-adjacent, bears on P neither way | the ACCOMMODATION test | **verbatim v1** (except `cle2`, fixed below) |
| **weak_contra** | a MILD / hedged denial of P | weak gate | new |
| **strong_contra** | an EMPHATIC / categorical denial of the SAME P | strong gate | v1's contradiction, strengthened |

**The weak/strong manipulation.** weak_contra and strong_contra deny the **same proposition** (¬P)
and differ **only in surface strength**: weak_contra uses an evidential/epistemic **downtoner** over
the negation ("it was unclear whether", "it was doubtful that", "reportedly not", "apparently not",
"seemingly"); strong_contra uses **intensifiers + absolute quantifiers** ("definitely not … at all",
"certainly not … in any way", "never … at all", "no one at all", "no … whatsoever", "absolutely
nothing"). Register and length are held close so the contrast is **strength, not verbosity** (see
§confounds).

### The `cle2` neutral FIX (LOUD — v1 SHOULD-FIX #1)

v1's pre-run critic flagged that `cle2`'s neutral context **leaked** toward P. v1 neutral:
*"The contract ran for three years"* — a contract that ran pragmatically implies it was **awarded to
someone**, i.e. it tilts *toward* the existential P ("someone won the contract") instead of bearing on
it neither way. Here `cle2`'s neutral is replaced with a **fully orthogonal setting fact**:

> **v1 (leaky):** "The contract ran for three years."
> **this run (fixed):** "The conference room overlooked the harbor."

The replacement bears on "someone won the contract" **neither way** and has **no lexical/pragmatic
overlap** with winning/awarding/bidding — a pure setting detail, matching the role v1's other neutrals
play (e.g. "The office was on the fourth floor"). **This is the ONLY change to any reused v1 sentence;
every other supported/neutral sentence is verbatim v1.**

The four `cle2` conditions in full (the fix, verifiable):
- supported: "The contract had been awarded to one of the bidders."
- neutral: **"The conference room overlooked the harbor."**  ← the fix (was "The contract ran for three years")
- weak_contra: "The contract had apparently not been awarded to anyone."
- strong_contra: "The contract was never awarded to anyone at all."

Sample second scenario (`fac1`, P = "the safe had been left open"):
- supported: "The safe had been left open all night."
- neutral: "The office was on the fourth floor."
- weak_contra: "It was unclear whether the safe had been left open."
- strong_contra: "The safe had definitely not been left open at all."

Each item is one forced choice — *"Consider only the following text: '<context> <trigger>'. Taking
that text at face value, does it follow that: <P>? Answer with exactly one word — YES, NO, or
UNCLEAR."* `endorsed` == answer parses to YES (`analyze.py`).

**The GRADED-GATE signature.** P endorsed in **supported** (retrieval) AND **neutral**
(accommodation), with endorsement **decreasing as contradiction strength rises**
(weak_contra_endorse > strong_contra_endorse). A **flat** profile (weak ≈ strong) is the null.

## Metrics (pre-specified, direction fixed)

Per model, from the parsed answers (`analyze.py`), each a **within-model rate over the model's own
YES/NO/UNCLEAR** answers (no human key):
- **supported_endorse** — P-endorse rate in the supported context (sanity floor).
- **neutral_endorse** — P-endorse rate in the neutral context (the accommodation rate).
- **weak_contra_endorse** — P-endorse rate under the hedged denial.
- **strong_contra_endorse** — P-endorse rate under the emphatic denial.
- **strength_gradient** = weak_contra_endorse − strong_contra_endorse (**the new signal**; positive ⇒
  stronger contradiction gates harder).
- **accommodation_gap** = neutral_endorse − strong_contra_endorse (the overall gate, vs the strongest
  contradiction — the v1 gate, re-anchored on strong_contra).
- per-family endorse rates per condition (descriptive; enables a later family decomposition).

## Verdict map (thresholds fixed NOW; may be tightened, never loosened)

```
SANITY     = 0.75   per-model supported_endorse floor; below it a model is control-FAILED.
ACCOM      = 0.60   per-model neutral_endorse floor to count as "accommodates".
GAP        = 0.30   per-model accommodation_gap floor to count as gating overall (neutral vs strong).
GRAD       = 0.15   per-model strength_gradient floor to count as "graded-by-strength".
FLATBAND   = 0.10   per-model |strength_gradient| below which weak ≈ strong (gate NOT graded).
NOGATEBAND = 0.15   per-model accommodation_gap below which even the STRONG contradiction fails to
                    lower endorsement (blanket yes-bias). Inherits v1's FLATBAND role/value.
LOWACC     = 0.40   per-model neutral_endorse ceiling below which the model does NOT accommodate.
```

**Threshold justifications** (12 items/condition ⇒ one item = 1/12 ≈ **0.083**; each threshold is
stated as an item count so it is legible, not tuned — there is no data to tune to):
- **SANITY 0.75** — retrieval floor. P is literally asserted in the supported context; a model that
  cannot endorse it on ≥ 9/12 items cannot read the frame, making its other cells uninterpretable.
  Same value as v1 (comparability).
- **ACCOM 0.60** — accommodating requires supplying the unmet P on a clear majority (≥ ~7/12) of
  neutral items. Same value as v1.
- **GAP 0.30** — the overall gate must drop endorsement by ≥ ~3.6/12 items from neutral to the
  *strongest* contradiction to count as gating at all. Same bar as v1's gate (there measured against
  the single contradiction); kept identical so v1's gate result stays directly comparable.
- **GRAD 0.15** — the *second-order* difference between two contradiction strengths (weak vs strong)
  is expected to be **subtler** than the first-order neutral→contradiction drop, so its floor is set
  below GAP: ≥ ~1.8/12 items must flip between weak and strong to call the gate graded. Chosen a
  priori as "≥ ~2 items of movement," not fitted.
- **FLATBAND 0.10** — |gradient| ≤ ~1.2/12 items ⇒ operationally weak ≈ strong (an on/off gate). The
  **deliberate dead-band** between FLATBAND (0.10) and GRAD (0.15) means a single-item wobble (0.083)
  is called **neither** clearly graded **nor** clearly flat → the model is unlabeled and contributes
  only to MIXED. This refuses to force a borderline case into a headline.
- **NOGATEBAND 0.15** — accommodation_gap < ~1.8/12 items ⇒ even the strong contradiction barely
  lowers endorsement ⇒ a blanket yes-bias. Inherits v1's FLATBAND value (0.15), which played the same
  "no gate" role there.
- **LOWACC 0.40** — neutral < ~4.8/12 items ⇒ the model isn't supplying the unmet P, so there is no
  accommodation to grade. Same value as v1.

Per-model label (sanity_ok required; a model may match none → contributes only to MIXED):
- **graded_gate** — accommodates AND strength_gradient ≥ GRAD (the conjecture's prediction).
- **flat_gate** — accommodates AND accommodation_gap ≥ GAP AND |strength_gradient| < FLATBAND (gates
  overall, but on/off, not graded — the null / partial falsifier).
- **blanket_yes** — accommodates AND accommodation_gap < NOGATEBAND (even strong barely gates).
- **no_accommodation** — neutral_endorse < LOWACC.

Panel verdict (priority order):
- **GRADED-GATE** — ≥ 2 of 3 sanity-passing models are graded_gate. *Confirms the cue-strength arm.*
- **FLAT-GATE** — ≥ 2 of 3 are flat_gate. *Honest null on / partial falsifier of the graded-cue arm.*
- **BLANKET-YES** — ≥ 2 of 3 are blanket_yes. *Inherited null on the gating reading.*
- **NO-ACCOMMODATION** — ≥ 2 of 3 are no_accommodation. *Inherited null.*
- **MIXED** — anything else (sanity failures, split panel, dead-band, partial signal).

Every outcome is first-class and reportable as a real finding, including the nulls (charter §4).
GRADED-GATE would feed the conjecture's confirming column; FLAT-GATE would feed its falsifying column
(the gate is on/off, favoring the "generic contradiction-detection" reading over "graded by surface
cue"). Sanity failure voids the strong reading and is reported honestly.

## Confounds a pre-run critic should scrutinize

1. **Is any "weak" denial too weak to count as a denial?** weak_contra hedges a categorical negation
   with an evidential/epistemic downtoner ("it was unclear whether P", "apparently not P",
   "reportedly not P") — it still asserts ¬P, just non-committally. A critic should judge whether the
   hedges are genuine denials (the intent) or drift into *mere uncertainty* that leaves P open (which
   would make weak_contra behave like a second neutral, inflating weak_contra_endorse and the
   gradient for the wrong reason). Borderline items to eyeball: `fac1` ("It was unclear whether…"),
   `fac2` ("It was doubtful that…") — these are the softest and closest to "open," by design the
   weakest denials.
2. **Length / verbosity confound.** The weak-vs-strong context word counts are near-identical:
   per-item delta (strong − weak) ranges **−1 to +1**, mean **+0.25** words, and the sign is
   **mixed** (one −1, seven 0, four +1), so length is not systematically correlated with strength.
   `prep.py --check` asserts |delta| ≤ 2 per item. Any residual gradient is therefore attributable to
   surface *strength*, not sentence length. (Full table in `README.md`.)
3. **The genuine-blocking vs contradiction-detection ambiguity is NOT resolved** (see §scope). A FLAT
   gate is consistent with pure contradiction-detection; a GRADED gate is consistent with
   cue-strength sensitivity — but neither certifies mechanism. The `internal-contrast-only` fence
   holds; do not read a mechanism claim into either verdict.
4. **`cle2` neutral fix is a single-item change to a v1-verbatim set.** A critic should confirm the
   replacement ("The conference room overlooked the harbor.") truly bears on "someone won the
   contract" neither way and introduces no *new* leak (e.g. toward a different presupposition).
5. **Small Ns** — 12 items/condition, n=3 models, three 2026 commercial models, project-authored
   synthetic stimuli. Direction-of-effect only; no coverage claim. Each threshold moves in ~0.083
   steps, so a one-model verdict can hinge on a single item — reported as texture, not smoothed.

## Cost

48 item-conditions × 3 models = **144** single-turn, single-word completions — larger than v1's
108-call battery (which billed **$0.0191**) by the ratio 144/108, so pre-flight expectation is
**≈ $0.02–0.06** (gemini's minimal-reasoning tokens dominate; temp 0; ≤16-token answers on A/B,
512-token cap on gemini for reasoning headroom). `ABORT_USD = 1.00` hard-stops a runaway; the run is
far under the $2.50 single-run flag and the **$5.00/day (UTC)** cap. **It must run on a fresh UTC
budget day, after a pre-run-critic GO**, with a real pre-flight (`--limit` on one model) measured and
recorded before the full run.

## What each outcome would feed

- **GRADED-GATE** → within-model evidence that current decoders gate accommodation *proportionally to
  surface contradiction strength* — the cue-strength confirming evidence the conjecture names, and a
  point toward the distributional-cue description over an invariant presupposition/assertion split
  (with the `internal-contrast-only` caveat; inherited anchor). Would strengthen (not prove)
  [`conjecture/presupposition-environment-gated-both-directions`](../../../wiki/findings/conjectures/presupposition-environment-gated-both-directions.md).
- **FLAT-GATE** → the gate is **on/off**, not graded: a hedged and an emphatic denial gate equally.
  An honest **null** on the graded-cue arm and a **partial falsifier** of it; would favor the
  "generic contradiction-detection" reading of v1's partial gate. Written as such.
- **BLANKET-YES / NO-ACCOMMODATION** → the inherited nulls (yes-bias, or no accommodation to grade).
- **MIXED / sanity failure** → instrument or item set confounded, or the panel splits; reported as
  such, no cue-strength claim made.
