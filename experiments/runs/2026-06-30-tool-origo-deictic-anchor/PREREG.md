# PREREG — the as-if origo probe (tool as deictic anchor)

**Run:** `2026-06-30-tool-origo-deictic-anchor` · **frozen** 2026-06-30 (session 156) ·
**manifest sha** `74763523f7070a13f37d8970fd229f51eb3a452a3d2c82aeb6c58ea389ffcec3`

Pre-registers question **(iii)** of [`conjecture/tool-origo-deictic-anchor`](../../../wiki/findings/conjectures/tool-origo-deictic-anchor.md)
— the one behaviorally testable residue that [`essay/origo-supplied-not-occupied`](../../../wiki/findings/essays/origo-supplied-not-occupied.md)
isolates from the architectural claim (i) and the channel claim (ii). This document is frozen
*before* any probe call; the FREEZE GUARD in `probe.py` refuses to run unless the manifest sha
above is intact, so the item set and verdict map cannot drift after the pre-run critic signs off.

## The one question (nothing wider)

> Given a clock/location **tool** is available, does the panel **spontaneously** treat tool-state
> as the deictic anchor for an **unanchored** ‘now’/‘here’/‘today’ — issuing the tool call without
> being told to, and binding the indexical's content to the value the tool returns?

## Scope cap — LOAD-BEARING (read before citing any result)

A positive is an **as-if behavioral contrast ONLY**, at **`anchor: internal-contrast-only`**
strength. It does **not**:
- certify the **architectural** claim (i) — that the model "occupies" a Kaplanian context;
- bear on the **channel** claim (ii) — a tool-return is itself *described text the model
  conditions on*; resolving to tool-state is resolving to **more described context** through a
  different surface, not to a context the model is the agent of;
- make **any human comparison**, in either direction (no human baseline claimed, measured, or
  needed).

Any reading **stronger than as-if** (e.g. "the tool makes the origo *occupied*") must FIRST open
the deferred `wiki/decisions/open/` gate the conjecture names ("can a tool-return count as an
*occupied* rather than a *described* origo?"), mark the result contingent on it, and leave
ratification to a later independent session. **This run makes no such claim**, so it opens no gate.

## Panel & settings

Panel per [`config/models.md`](../../../config/models.md): `panel.A` = anthropic/claude-sonnet-4.6,
`panel.B` = openai/gpt-5.4-mini, `panel.C` = google/gemini-3.5-flash. All three list `tools` +
`tool_choice` in the OpenRouter `supported_parameters` catalog (verified 2026-06-30). Temperature
0; one date; zero-shot; `tool_choice` = **auto** (a call is the model's own move); gemini
`reasoning={"effort":"minimal"}` (config/models.md caveat); billed `usage.cost` recorded.

## Design — three arms over 15 matched base scenarios (5 time / 5 date / 5 location)

45 item-conditions total (`prep.py`; the project's OWN synthetic items — no external corpus).

| arm | text | tools | what it isolates |
|-----|------|-------|------------------|
| **test** | unanchored (no narrated origo) + indexical question | available | as-if signal: spontaneous query + resolution to tool-state |
| **control** | anchored (narrates an origo, values **distinct** from the nonce) + same question | available | does the panel resolve from the narrated origo and NOT spuriously override it with the tool? |
| **baseline** | same unanchored text as `test` | **none** | deflationary fallback shape (refuse / hedge / parametric default) when no tool exists |

Both tools (`get_current_time`, `get_current_location`) are exposed together on every tool-arm
item, so the tool is not the only salient affordance and the model must pick the relevant one.

**Nonce tool returns** (un-memorizable; logged): `get_current_time()` → time **17:42**, date
**3021-11-08** (weekday Tuesday); `get_current_location()` → city **Qethport**, region **Vandrel
Province**, country **Meridonia**. Because these cannot be a training-prior coincidence,
"resolved to tool-state" = the final answer contains a nonce token, and **cannot occur in the
no-tool baseline at all** — a *structural* guarantee that the test-arm resolution signal is
tool-attributable (this is stronger than the conjecture's sketch, which asked the baseline to
*empirically* not already produce the answer).

## Metrics (pre-specified, direction fixed)

Per (model, arm), scored in `analyze.py` from the FINAL natural-language answer:
- **spontaneous_query_rate** (test) — fraction of items on which the model issued a tool call
  without being told to (system prompt never mentions tools; `tool_choice` auto).
- **resolution_to_tool_state_rate** (test) — fraction whose final answer contains a nonce token
  for the item's indexical (`prep.NONCE_ACCEPT`).
- **spurious_override_rate** (control) — fraction whose final answer contains the nonce token
  (i.e. overrode the narrated origo with the tool); should be **low**. Descriptive companion:
  **resolve_from_narrated_rate** (answer contains the narrated value).
- **hedge_rate / answered_rate** (baseline) — heuristic characterization of the deflationary
  fallback (no-access/uncertainty phrases vs. a produced answer). Descriptive only; not a gate.

Query and resolution are scored **separately** (de-confound: a model may call the tool and still
answer from a default).

## Verdict map (thresholds fixed NOW; may be tightened, never loosened)

Thresholds `T = 0.80` (test spontaneous-query and resolution), `OVR = 0.20` (control override
ceiling). Applied over the 3 models:

- **CONFIRM (as-if bet holds).** For **≥ 2 of 3** models, `spontaneous_query_rate ≥ 0.80` **AND**
  `resolution_to_tool_state_rate ≥ 0.80`, **AND** each of those models keeps control
  `spurious_override_rate ≤ 0.20`. Reported strictly as an **as-if** contrast,
  `internal-contrast-only`; explicitly **not** as "the model occupies a context."
- **NULL (deflationary alternative holds).** For **≥ 2 of 3** models,
  `spontaneous_query_rate < 0.80` **OR** `resolution_to_tool_state_rate < 0.80` — the panel
  predominantly refuses/hedges/defaults rather than spontaneously adopting tool-state. A
  first-class result: even handed a clock/location tool, a text-only model does not spontaneously
  treat tool-state as a deictic origo for an unanchored ‘now’/‘here’ — consistent with the parent
  essay's "no deictic origo" reading at the behavioral grain (without bearing on (i)/(ii)).
- **MIXED (reported as mixed).** Models split; or query-without-resolve (calls the tool but answers
  from a default); or the control fails (`spurious_override_rate > 0.20` on a model that otherwise
  clears the test thresholds — an uninterpretable control voids that model's test reading).

## Pre-flight cost

Smoke test (2026-06-30, 3 items) billed: claude ~$0.005, gemini ~$0.0005, gpt ~$0.0003 per
completed 2-turn tool item. Full run ≈ 45 item-conditions × 3 models (test/control are 2-turn;
baseline 1-turn) ≈ **$0.25–0.8 billed** (claude the driver; the ~4.5× historical undercount is
folded into the upper end). Well under the **$2.50 single-run** flag and today's **$5.00/day (UTC)**
cap (UTC-2026-06-30 prior spend: session 154 $0.0752, session 155 $0). `ABORT_USD = 1.50` in
`probe.py` hard-stops a runaway bill.

## What a positive would and would not add

Would add: a bounded, pre-registered **as-if** datum — on unanchored deictic items, given a
clock/location tool, the panel spontaneously queries it and binds ‘now’/‘here’ to tool-state,
while correctly resolving a *narrated* origo without spurious override. Would **not** add: any
claim that the model occupies a context (i), any dent in the channel claim (ii), or any human
comparison. The ceiling is the point, not a hedge.
