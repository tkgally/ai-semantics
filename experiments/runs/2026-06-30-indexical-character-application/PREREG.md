# PREREG — indexical CHARACTER-application probe (2026-06-30, session 154)

**Frozen before any API call.** Manifest sha `503d907bc3f681f0992f8f53ad2b7252ae8ab7eecf711755518dee4a4b1301c8`
(prep.py `FROZEN_SHA`; probe.py refuses to run on drift).

## Question

Essay [`essay/indexical-character-learnable-content-supplied`](../../../wiki/findings/essays/indexical-character-learnable-content-supplied.md)
splits an indexical's meaning into Kaplan's **character** (the convention-fixed rule — "'I'
picks out the agent", "'today' picks out the day of the context") and **content** (the value at
a context). Its positive half: the **character** side is *distributionally native* — the kind of
convention a text-only learner is structurally suited to acquire — but it states this as an
**affordance, not a measured attainment**, and pre-registers **trigger (c)**: *a probe showing a
model systematically **mis-applies** an indexical's rule to a **clearly described** context would
contradict the "character is distributionally native" half and force a downgrade.*

This probe runs trigger (c). It asks each panel model to resolve a **single** indexical to its
content **against a fully DESCRIBED origo** (the agent/time/location are stated in the text). It
does **not** give the model an origo of its own (that is trigger (b), not tested here) — every
context is *described*, exactly the regime the essay says the model can "apply the character (the
rule) to flawlessly."

## Design (40 items, prep.py)

Single resolution target per item; answer scored by substring-accept against a frozen key.

- **C1 plain (10).** One stated origo; resolve 'I'/'you'/'here'/'now'/'today'/'my'/'this'.
- **C2 origo-shift (10).** Multi-turn dialogue, each turn's speaker+addressee stated; resolve
  'I'/'you'/'me'/'your' in a **non-first** turn (a model that globally fixes 'I' to the first
  speaker fails).
- **C3 embedded (10).** Reported speech with its **own** origo plus a salient **narrator-origo
  distractor**; resolve to the **embedded** speaker's origo (the quoted 'I'/'here'/'tomorrow',
  not the reporter's). Embedded date items compute the gold from the **embedded** utterance's
  stated date, with the narrator's reading date as a deliberate distractor.
- **C4 temporal arithmetic (10).** Single explicit origo date; resolve a relative temporal
  indexical ('yesterday', 'the day before yesterday', 'in three days', 'next Monday'…) to an
  absolute date. **Secondary / exploratory** (see verdict).

All stimuli are the **project's own synthetic constructions** (no external corpus, no license),
so the full text is committed (`items.json`). Date golds are **computed** (datetime) from explicit
base dates + signed offsets; every weekday word in a prompt is **asserted** against the actual
weekday, so no mis-stated date can ship. Keys are authored to be **unambiguous given the described
context** — the pre-run critic verifies this.

## Panel & settings

[`config/models.md`](../../../config/models.md) panel as **subjects**: claude-sonnet-4.6 (A),
gpt-5.4-mini (B), gemini-3.5-flash (C). Temperature 0. Brief reasoning permitted; the answer ends
in a marked `FINAL:` line (parsed by probe.py). Gemini reasoning `effort: minimal`
(config/models.md caveat). One run, one date, zero-shot.

## Pre-registered verdict map (analyze.py, frozen)

- **HEADLINE = pooled C1+C2+C3 CHARACTER-RULE accuracy** per model (resolving the indexical to
  the correct **described** content / origo).
- **Trigger (c) FIRES** for a model iff its pooled C1–C3 accuracy **< 0.85** AND the misses are
  genuine **wrong-entity / wrong-origo** resolutions (not empty/format-parse failures).
- **Near-ceiling pass (≥ 0.85, the expected outcome) = NON-FALSIFICATION.** It is **consistent
  with** the essay's "distributionally native" affordance half but **does not prove** it (an
  affordance is not provable from a ceiling); had a model failed, trigger (c) would have fired.
- **C4 is secondary/exploratory**, reported descriptively. A **direction** error ('yesterday' →
  a future date) is a rule error and is **flagged** for trigger-(c) consideration; a pure
  **magnitude** slip (right direction, wrong count) is reported separately and **fenced out** of
  the trigger-(c) judgement (it is date arithmetic, not indexical-rule mis-application).

The bar (0.85) and the C4 fencing are set **now, before any call**, and are not retuned after
seeing results (charter §8 operationalization gate).

## What this can and cannot show (anchor honesty)

- This is a **within-model behavioral** measure of character application against a stipulated
  key. It makes **NO human comparison** — it does not claim humans do better/worse, only whether
  each model applies the rule to a described context. The honest anchor type is therefore
  **`anchor: internal-contrast-only`**.
- Per [`CLAUDE.md`](../../../CLAUDE.md), `internal-contrast-only` is a **ratified terminal
  declaration** and **cannot be ratified in the session that opens it**. So the result page ships
  **`anchor: pending`** with a queued [`wiki/decisions/open/`](../../../wiki/decisions/open/)
  entry naming the anchor-type question, contingent until a later session ratifies (charter
  §12.3). No human anchor is fabricated.
- A pass **cannot** prove "distributionally native" (an affordance claim); it can only **fail to
  falsify** it. A fail **would** falsify it. The result is asymmetric by construction and is
  reported as such.

## Cost (pre-flight)

40 items × 3 models = 120 calls; short inputs (~250 tok), short outputs (A/B ~80 tok; gemini
reasoning minimal, capped 4096). Rate-card estimate ≈ $0.10–0.20; billed expectation (≤ ~4.5×
undercount) ≈ **$0.3–0.7**. Well under the $2.50 single-run flag and the $5.00/day (UTC) cap
($0 spent this UTC day). `ABORT_USD = 1.50` hard stop in probe.py.
