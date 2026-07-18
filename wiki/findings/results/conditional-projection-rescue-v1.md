---
type: result
id: conditional-projection-rescue-v1
title: "The conditional-antecedent projection collapse is ROBUST — commitment, consequent-position, and speaker-belief framings do not restore panel projection (claude alone is rescued by commitment framing)"
meaning-senses:
  - inferential
  - distributional
status: proposed
anchor: internal-contrast-only
contingent-on: []
created: 2026-07-01
updated: 2026-07-01
links:
  - rel: refines
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: result/presupposition-projection-v1
  - rel: depends-on
    target: source/beaver-geurts-denlinger-2021-presupposition-sep
  - rel: depends-on
    target: essay/projection-defeasible-by-frame
  - rel: depends-on
    target: concept/inferential-meaning
  - rel: depends-on
    target: concept/distributional-meaning
---

# Result: the conditional-projection-rescue probe v1

A follow-up to [`result/presupposition-projection-v1`](presupposition-projection-v1.md) (session 158),
which found the panel reproduces presupposition **projection** under negation/question embedding but
that projection **COLLAPSES under the conditional antecedent** for all three models (presupposition-survival
0.42 / 0.17 / 0.17). This probe asks the sharp follow-up: is that collapse **rescuable** by an explicit
framing, or a **robust** feature of the text-trained behavior? Run record:
[`experiments/runs/2026-07-01-conditional-projection-rescue/`](../../../experiments/runs/2026-07-01-conditional-projection-rescue/README.md);
frozen [`PREREG.md`](../../../experiments/runs/2026-07-01-conditional-projection-rescue/PREREG.md),
manifest sha `c88ef626…`.

**One-line finding.** The pre-registered verdict is **ROBUST-COLLAPSE**. The base arm replicated the
s158 conditional collapse **exactly** (presup-endorse 0.42 / 0.17 / 0.17, identical to the s158
conditional cell), and **no rescue framing restored projection for ≥2/3 models**: the collapse
survives a speaker-**commitment** framing, a **consequent-position** relocation, and a
speaker-**belief** framing at the panel level. The one informative nuance: **claude alone is rescued
by the commitment framing** (presup-endorse 0.42 → 0.75, entail stays 0.00), and belief framing lifts
its presup-leg above the entail-leg for all three models — but only claude clears the survival floor,
so the panel verdict is that the conditional-antecedent collapse is a **genuine within-panel limit**,
not an artifact of the neutral s158 query.

## Scope — LOAD-BEARING (read before citing)

**Within-model contrast only; no human comparison.** The signal is *how a model's presupposition
endorsement changes (or does not) across framings, and whether the presupposition leg survives more
than the matched-entailment leg within an arm* — **not** *the model matches human projection judgments*.
No human projectivity baseline is claimed, measured, or needed. The result does **not** certify that a
model *represents* presupposition-vs-assertion semantically; it reads endorsement of an inference under
embedding/framing off forced-choice answers (text-consistency is not mechanism). Anchor is
**`anchor: internal-contrast-only`**, inheriting the parent line ratified this session by an
independent adversarial review
([`decisions/resolved/presupposition-projection-internal-contrast-anchor`](../../decisions/resolved/presupposition-projection-internal-contrast-anchor.md));
this follow-up stays strictly within that within-model contrast and opens no new anchor decision.

## What ran

- **Panel** ([`config/models.md`](../../../config/models.md)): `anthropic/claude-sonnet-4.6` (A),
  `openai/gpt-5.4-mini` (B), `google/gemini-3.5-flash` (C), as subjects. Temperature 0; text-only,
  single-turn, zero-shot; gemini `reasoning={"effort":"minimal"}`. Neutral system prompt (identical to
  s158) that never mentions presupposition, projection, or the right answer.
- **Items.** 12 base scenarios **reused verbatim from s158** (same 4 trigger families — factive /
  aspectual / definite / cleft, 3 each — same presupposition (P) and matched-entailment (E) targets,
  same antecedent-conditional sentences) × **4 arms** × 2 targets = **96 item-conditions** per model,
  288 calls total. The four arms:
  - **base** — the s158 conditional-antecedent frame + neutral query, verbatim (replication anchor).
  - **commit** — same sentence, query reframed as a sincere speaker **assertion** asking what the
    speaker is thereby **committed to**.
  - **conseq** — the same trigger relocated to the **consequent** of a conditional with a neutral,
    unrelated antecedent (a non-antecedent position; doubles as a position control).
  - **belief** — same sentence, query asks whether the **speaker believes** the target.
- **Cost.** **$0.0526 billed** (claude $0.0307 / gpt $0.0099 / gemini $0.0119), 0 missing cost,
  **0 unparsed** answers; plus a $0.0026 pre-flight (8 claude items) = **$0.0552** this run. UTC-2026-07-01
  day total after this run **$0.1038** of $5.00 (s158 $0.0486 + this $0.0552). Far under the $2.50
  single-run flag.

## Numbers (from `results.json`; independently reproduced)

**Per model, per arm** (presup-endorse P / entail-endorse E over 12 items each; gap = P − E; lift =
P − base-P):

| model | base P/E | commit P/E (lift) | conseq P/E (lift) | belief P/E (lift) |
|-------|----------|-------------------|-------------------|-------------------|
| A claude-sonnet-4.6 | 0.42 / 0.08 | **0.75** / 0.00 (**+0.33, RESCUED**) | 0.50 / 0.00 (+0.08) | 0.58 / 0.00 (+0.17) |
| B gpt-5.4-mini | 0.17 / 0.17 | 0.00 / 0.00 (−0.17) | 0.42 / **0.42** (+0.25, yes-shift) | 0.58 / 0.25 (+0.42) |
| C gemini-3.5-flash | 0.17 / 0.00 | 0.25 / 0.00 (+0.08) | 0.42 / 0.00 (+0.25) | 0.25 / 0.00 (+0.08) |

Verdict per the frozen map (RESCUE 0.60 / GAP 0.30 / BASE_COLLAPSE_MAX 0.60 / YESBIAS 0.60):
**ROBUST-COLLAPSE** — base collapse replicated in 3/3 models; a rescue arm counts only if ≥2/3 models
reach presup-endorse ≥ 0.60 with gap ≥ 0.30, and **only claude-commit** (0.75) clears the floor, so
**every rescue arm is NOT-RESCUED** at the panel level.

- **Base replication is exact.** base presup-endorse **0.42 / 0.17 / 0.17** equals the s158 conditional
  cell to the decimal — the collapse is not a one-run fluke; it reproduced under a fresh run on the
  same items. (base entail-endorse is 0.08 / **0.17** / 0.00 vs s158's 0.08 / 0.08 / 0.00 — gpt's
  control leg is one item higher, 2/12 vs 1/12, an unremarkable fresh-resample drift on the yes-bias
  control that leaves the collapse anchor and the verdict untouched.)
- **commit** rescues **only claude** (0.42 → 0.75, entail stays 0.00 — a genuine projection restoration,
  not a yes-bias). For **gpt commit LOWERS** presup-endorse to 0.00 (it reads "everything the speaker is
  committed to" as *more* restrictive and refuses the antecedent's backgrounded content); gemini barely
  moves (0.25).
- **conseq** (non-antecedent position) lifts presup-endorse modestly (0.50 / 0.42 / 0.42) but for **gpt
  the entail leg rises equally** (E 0.42, gap 0.00) — a **global yes-shift, not a rescue**, caught by
  the **gap gate** (gap 0.00 < 0.30), not the yes-bias flag (E 0.42 stays under the 0.60 flag
  threshold). So even relocating the trigger out of the antecedent does not cleanly restore panel
  projection — the collapse is **not narrowly antecedent-position-specific**.
- **belief** lifts the presup-leg above the entail-leg in all three (gap +0.58 / +0.33 / +0.25) but
  clears the survival floor in none (0.58 / 0.58 / 0.25) — the direction is right everywhere, the
  magnitude reaches the bar nowhere.

**A qualitative split worth recording** (from the raw answers). **gemini** returns **UNCLEAR** to
almost everything under a conditional — presupposition *and* matched entailment alike — across all four
arms: its "collapse" is a **blanket refusal to extract any inference from a hypothetical**, not a
P-specific failure. **claude** is the one model whose presupposition endorsement is **framing-sensitive**:
UNCLEAR under the bare "consider the statement" query, but a clean **YES (P) / NO (E)** once the same
conditional is framed as a committed speaker assertion or a speaker belief. **gpt** is erratic — the
commitment framing *suppresses* its presupposition endorsement while the belief framing *inflates both
legs*.

## Interpretation (calibrated)

- **What the data support.** The conditional-antecedent projection collapse found in s158 is **robust**
  at the panel level: it reproduces exactly under a fresh run and survives three distinct framings
  designed to rescue it (commitment, consequent-position, speaker-belief). This adjudicates the s158
  follow-up question toward the **"genuine limit of the text-trained projection behavior"** reading over
  the **"surface-cue artifact of the neutral query"** reading — the collapse is not merely an effect of
  *how the question was asked*.
- **The rescue is model-specific, not panel-general.** claude's presupposition endorsement is
  recoverable by an explicit speaker-commitment framing (0.42 → 0.75), so for *one* model the collapse
  is partly a framing effect; but this does not generalize (gpt's commit framing lowers it; gemini's
  barely moves), so it does not lift the panel verdict. The honest statement is *robust across the
  panel, rescuable within claude by commitment framing*.
- **What the data do NOT support.** (i) No human comparison — no human projectivity baseline is
  measured or claimed. (ii) No mechanism claim — endorsing (or declining) a projected inference off a
  forced-choice answer is text-consistent-with a description, not evidence the model computes a
  presupposition/assertion split. (iii) The **conseq** arm's failure to restore projection is subject to
  a known alternative reading (the pre-run critic's advisory a): a model could read the projected
  presupposition *conditionally* ("*if* the neutral antecedent, someone Y-ed") and answer UNCLEAR to the
  unconditional target without a genuine projection failure — so conseq under-rescue is reported as an
  alternative reading, not proof that projection is dead in the consequent. (iv) The commit/belief arms
  change the **speech-act framing** ("a speaker sincerely asserts") relative to base's "consider the
  statement," so they differ from base in two coupled ways (the commitment/belief question *and* the
  speaker scene); a clean decomposition of which did the work is not available (pre-run critic advisory c).
- **Feeds the essay.** This adjudicates the puncture test of
  [`essay/projection-defeasible-by-frame`](../essays/projection-defeasible-by-frame.md): the ROBUST
  outcome **strengthens the "genuine limit" reading** the essay pre-registered — the conditional-frame
  defeasibility is a standing boundary of the behavior, not a rescuable cue effect (with the claude
  exception noted). The essay's core description — projection here is frame-shaped, not item-scattered —
  is untouched.

## Gates

- **Pre-run critic (independent fresh agent): GO** (conditional on the anchor ratification, which
  landed this session). All stimulus checks PASSED: base is a byte-identical replication of s158's
  conditional query + sentences; the arm factorization isolates position (base↔conseq) and framing
  (base↔commit/belief) cleanly item-by-item; the neutral antecedents in conseq establish neither P nor
  E; the framing wrappers are not leading and the E leg stays a fair yes-bias control; the verdict map
  is symmetric (a global yes-shift lands as a yes-bias flag, not a false rescue). Advisories (a) conseq
  conditional-reading, (b) report yes-bias flags + unparsed, (c) commit/belief couple framing+speech-act
  — all carried into this page.
- **Post-run verifier (independent fresh agent): REPRODUCED** — every per-model, per-arm figure
  re-derived from `raw/*.json` with independent scoring; base replication of the s158 conditional cell
  confirmed; the gpt-conseq yes-shift and the claude-commit genuine rescue confirmed; 0 missing / 0
  unparsed. (See wind-up note.)

## What this feeds

Discharges the **conditional-collapse follow-up** branch named in s158's result and [`NEXT.md`](../../../NEXT.md): the
conditional-antecedent projection collapse is a **robust within-panel limit**, rescuable within claude
alone by an explicit commitment framing. Refines
[`result/presupposition-projection-v1`](presupposition-projection-v1.md) (the collapse is now shown
robust, not a query artifact) and adjudicates the puncture test of
[`essay/projection-defeasible-by-frame`](../essays/projection-defeasible-by-frame.md) toward its
genuine-limit reading. Opens a possible narrower follow-up (why does an explicit *commitment* framing
rescue claude but *suppress* gpt? — a model-difference in how "speaker commitment" is read), left for a
later session.

**External companion (session 249, no change to this result):** an independent human-vs-LLM study of
conditional presupposition — [`source/azin-2026-presupposition-conditionals`](../../base/sources/azin-2026-presupposition-conditionals.md)
(Azin et al. 2026, CoNLL 2026) — reaches a **broadly convergent** reading (LLM presupposition behavior
looks like "surface pattern matching rather than pragmatic competence", with weak human alignment). It
is recorded as **companion, not corroboration**: Azin studies the **proviso** cell (trigger in the
*consequent*, modulated by antecedent relevance), a **different structural configuration** from this
result's **antecedent**-of-conditional collapse, on a non-project model set — so it does not replicate
or strengthen this specific result, and this page's `internal-contrast-only` scope is untouched.

**Update (session 166): that follow-up ran** →
[`result/commitment-framing-model-difference-v1`](commitment-framing-model-difference-v1.md) (verdict
**PARTIAL**). The model difference reproduced. **claude** reads "committed" **inclusively** (a
backgrounding-reader: its `commit` presup-endorse 0.75 clusters with a "takes for granted" pole 0.83,
above a "main point" pole 0.42) — that is *why* commit rescues it. But **gpt's suppression is NOT the
predicted narrow reading**: it keeps presup-endorse low under *every* framing including the explicitly
backgrounding pole (max 0.33), so its poles do not separate — a **general** low-projection floor, which
retires the "gpt reads commitment restrictively" conjecture. The scene-vs-wording confound (advisory c
above) stays **coupled** for claude (scene +0.17, wording +0.17), not cleanly decomposed.
