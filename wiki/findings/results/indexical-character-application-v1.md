---
type: result
id: indexical-character-application-v1
title: The 2026 panel applies indexical CHARACTER to fully described contexts at ceiling (120/120), including embedded-origo and temporal-arithmetic items — a clean non-falsification of the essay's "distributionally native" half
meaning-senses:
  - referential
  - distributional
  - model-internal
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-06-30
updated: 2026-06-30
links:
  - rel: supports
    target: essay/indexical-character-learnable-content-supplied
  - rel: depends-on
    target: source/braun-2015-indexicals-sep
  - rel: depends-on
    target: concept/distributional-meaning
  - rel: depends-on
    target: concept/referential-meaning
---

# Result: indexical character-application probe v1

This is the **first empirical touch** on the project's indexicality / deixis corner (opened
session 153). It runs the behavioral test that
[`essay/indexical-character-learnable-content-supplied`](../essays/indexical-character-learnable-content-supplied.md)
pre-registered as its **trigger (c)**: *"A probe showing a model systematically **mis-applies** an
indexical's rule to a clearly **described** context … would contradict the 'character is
distributionally native' half."* Run record:
[`experiments/runs/2026-06-30-indexical-character-application/`](../../../experiments/runs/2026-06-30-indexical-character-application/README.md);
frozen design [`PREREG.md`](../../../experiments/runs/2026-06-30-indexical-character-application/PREREG.md),
manifest sha `503d907b…`.

**One-line finding.** All three panel models resolve a single indexical to its **content** against
a fully **described origo** at **ceiling — 120/120 items, every condition, every model** —
including the hard embedded-reported-speech items (binding 'here'/'I'/'tomorrow' to the *embedded*
speaker's origo over a salient narrator distractor) and multi-step temporal-date arithmetic. The
pre-registered verdict is a **NON-FALSIFICATION**: trigger (c) does not fire. This is **consistent
with** the essay's "character is distributionally native" claim and **does not prove** it — by
construction the test could only *falsify* the affordance (a failure), never *establish* it (a
ceiling).

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A),
  `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C), as **subjects** (charter §6).
  Temperature 0; brief reasoning permitted with a marked `FINAL:` answer line; gemini reasoning
  `effort: minimal`. One run, one date, zero-shot.
- **Items.** 40 **project-authored** synthetic stimuli (no external corpus; full text committed),
  10 per condition, single resolution target each:
  - **C1 plain** — one stated origo; resolve 'I'/'you'/'here'/'now'/'today'/'my'/'this'.
  - **C2 origo-shift** — multi-turn dialogue, each turn's speaker+addressee stated; resolve
    'I'/'you'/'me'/'your' in a **non-first** turn (a model that globally fixes 'I' to the first
    speaker fails).
  - **C3 embedded** — reported speech with its **own** origo + a salient **narrator-origo
    distractor**; resolve to the **embedded** speaker's origo. Date items keyed to the embedded
    utterance's date, not the narrator's reading date.
  - **C4 temporal-arithmetic** — single explicit origo date; resolve a relative temporal
    indexical ('yesterday', 'the day before yesterday', 'in three days', 'next Monday'…) to an
    absolute date. **Secondary/exploratory** (see *Verdict*).
- **Integrity.** 120/120 calls, **0 missing `usage.cost`**, **all `parse_mode = "final"`** (no
  empty/fallback), 0 unparseable.
- **Cost** (billed `usage.cost`): **$0.0752** (claude $0.0358 / gpt $0.0072 / gemini $0.0322).
  Under the $2.50 single-run flag; $0 → $0.075 of the $5.00/day (UTC) cap.

## Results

| model | C1 | C2 | C3 | char (C1–C3) | C4 | overall |
|---|---:|---:|---:|---:|---:|---:|
| claude-sonnet-4.6 | 1.000 | 1.000 | 1.000 | **1.000** | 1.000 | 1.000 |
| gpt-5.4-mini | 1.000 | 1.000 | 1.000 | **1.000** | 1.000 | 1.000 |
| gemini-3.5-flash | 1.000 | 1.000 | 1.000 | **1.000** | 1.000 | 1.000 |

Representative hard-item answers (all three models, verbatim `FINAL:`): C3 'here' →
**Cairo** (witness in Cairo; journalist in London) and **the Alps** (soldier stationed there;
Sparta/Athens distractors); C3 embedded 'tomorrow' → **2026-02-04** (letter written 3 Feb; read
10 Jun) and **2026-05-21**; C2 Turn-2 'I' → **Frank** (not the first speaker); C4 'the day before
yesterday' (ref Fri 27 Feb) → **2026-02-25**, 'next Monday' (ref Tue 5 May) → **2026-05-11**.

## Verdict (pre-registered, not retuned)

The bar was fixed **before** the run (PREREG §verdict): trigger (c) **FIRES** for a model iff its
pooled **C1–C3 character-rule accuracy < 0.85** with **wrong-entity/wrong-origo** misses (not
parse failures). Observed: **1.000** for every model. Trigger (c) **does not fire** →
**NON-FALSIFICATION**.

- **C4 was secondary/exploratory** and fenced out of the trigger judgement (a pure date-arithmetic
  slip is computation, not indexical-rule mis-application; only a *direction* error — 'yesterday'
  resolved to the future — would have counted as a rule error). It also came back 1.000, with **0**
  errors of any kind, so the fence was never load-bearing.

## Interpretation (modest)

1. **The "character" half of the essay's split survives its first behavioral test.** The essay
   located the **character** of an indexical (the convention-fixed rule) on the *distributional*
   side of the project's divide and the **content** (the value at an occupied context) on the
   *grounding* side — but stated the character side as an **affordance, not a measured attainment**.
   This probe supplies the missing behavioral check on the affordance: across described contexts of
   rising difficulty (plain → speaker-relative rebinding → embedded origo with a distractor → date
   arithmetic), the panel applies the rule to the **described** content without a single miss.
2. **What is at ceiling is exactly the "described, not occupied" regime the essay scopes to.**
   Every origo here is *supplied by the text*; the model is never asked to read an origo it
   *occupies* (that is trigger (b), untouched). So the result speaks only to the half the essay
   says a text-only model should handle for free — and it does.
3. **Cross-model uniformity.** Unlike several prior probes (e.g.
   [`result/scivetti-cxnli-answer-key-v1`](scivetti-cxnli-answer-key-v1.md), where gpt-5.4-mini
   trailed), here the three families are **indistinguishable at ceiling**, consistent with
   character-application being a low-bar, broadly-acquired competence rather than a
   capability-separating one.

## What this does and does not license

**Does license:** a within-model statement that, on these 40 described-context items, the 2026
panel applies indexical *character* (resolving 'I'/'you'/'here'/'now'/'today'/relative-date terms
to the described content/origo) at ceiling, **without falsifying** the essay's "distributionally
native" reading — including under embedding and multi-step temporal arithmetic.

**Does NOT license:**
- **Proof of the affordance.** A ceiling **cannot** establish "distributionally native" (an
  affordance is a claim about *fit*, not a measured maximum); it can only **fail to falsify** it.
  The asymmetry is by construction and pre-registered.
- **Any human comparison.** No human baseline is claimed, measured, or needed (`anchor: pending`,
  default internal-contrast-only — see *Status*). The result says nothing about whether people
  resolve described indexicals better, worse, or the same.
- **Anything about the CONTENT half.** The essay's load-bearing claim is that *content* needs an
  **occupied** origo a text-only model lacks. This probe deliberately stays in the **described**
  regime and so bears **only** on the character half. It is **not** evidence on grounding,
  reference, or trigger (b) (an origo-occupying setup).
- **A ceiling on harder cases.** A positive ceiling cannot prove that no *still*-harder described
  context (deeper nesting, conflicting multi-origo chains, exotic calendar conventions) would trip
  a model — only that none of the 40 here did.

## Limits

- **Single run, one date, one framing, n=40 (10/condition).** A ceiling with no errors gives no
  spread to characterize; the small per-condition cells cannot separate "robustly perfect" from
  "perfect here." The informative load rode on C3/C4 (C1/C2 are near-trivial by design — the probe
  is a *falsification* test, so an easy ceiling on C1/C2 cannot masquerade as confirmation under
  the pre-registered logic).
- **Stipulated key, not a human gradient.** Each item's correct answer is fixed by the described
  context; this is answer-key resolution, never a per-item human distribution.
- **Synthetic stimuli.** Project-authored items, transparent and uncontaminated by construction,
  but not naturalistic discourse.
- **Shared-prior caveat (charter §2.5).** Three decoders agreeing at ceiling on an easy-for-them
  task is weak evidence on its own; the result's value is the **failed falsification** of a
  *specific* pre-registered prediction, not the agreement per se.

## Provenance

- Tests [`essay/indexical-character-learnable-content-supplied`](../essays/indexical-character-learnable-content-supplied.md)
  trigger (c); the character/content distinction is from
  [`source/braun-2015-indexicals-sep`](../../base/sources/braun-2015-indexicals-sep.md) (Kaplan,
  survey strength). Concepts: [`concept/distributional-meaning`](../../base/concepts/distributional-meaning.md),
  [`concept/referential-meaning`](../../base/concepts/referential-meaning.md).
- **Anchor: `internal-contrast-only`** (terminal), ratified 2026-06-30 (session 155, autonomous
  adversarial review) via [`decisions/resolved/indexical-character-anchor-type`](../../decisions/resolved/indexical-character-anchor-type.md):
  the result makes **no human-comparison claim** — its headline is a within-model accuracy against a
  stipulated answer key — so no resource anchor is required. The ratification fixes the **yardstick,
  not the result**: the ceiling figures and the "non-falsification, not proof" reading are unchanged.
  No human anchor is fabricated.
- Independent fresh-agent **pre-run critic**: **GO-WITH-NOTES** (no blockers; verified every date
  gold + weekday by hand, found no genuinely ambiguous item, confirmed key tightness and anchor
  honesty; two analysis-layer date-format SHOULD-FIXes applied to `analyze.py` before the run —
  widening acceptance of correct date surface forms only, frozen manifest sha unchanged).
- Independent fresh-agent **post-run verifier**: **REPRODUCED** — independently re-scored all 120
  records and hand-derived the gold for every C3/C4 item, confirming the 1.000 figures, the parse
  integrity (120/120 `final`), and the billed cost.
- Numbers reproducible from committed `raw/` + `analyze.py`; stimuli + key in `prep.py` /
  `items.json` (sha-pinned).

## Status

`status: proposed`, `anchor: internal-contrast-only` (terminal; ratified 2026-06-30, session 155,
autonomous adversarial review — see [`decisions/resolved/indexical-character-anchor-type`](../../decisions/resolved/indexical-character-anchor-type.md)),
`contingent-on: []`. What is `proposed` is the project's reading (a non-falsification, not a proof).
The anchor field is now terminal; promotion of the finding past `proposed` awaits Tom's review.
