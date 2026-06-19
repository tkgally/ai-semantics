# PREREG — EXECUTION-FORMAT (reasoning-scaffold) WITNESS-SEEKING order-sensitive composition probe

## What this is (witness-seeking on a fresh, un-eased axis — execution format)

The Option-C run ([`2026-06-18-relational-order-composition-c`](../2026-06-18-relational-order-composition-c/))
found a **split**: claude RESPECTS-ORDER at ceiling, but **both** gemini and gpt **failed the
on-demand DIRECT gate** (< 0.80) → UNINTERPRETABLE for each. The split has since survived **four**
witness-seeking easings without a witness — K=6→K=4 state space, figure-to-figure read-off, and a
worked-example chaining demonstration
([`result/relational-order-composition-c-worked-example`](../../../wiki/findings/results/relational-order-composition-c-worked-example.md)).
Across the figure-to-figure and worked-example runs the residual difficulty was behaviorally
localized to **chaining execution**: even **told** the order on DIRECT, gpt applied only one of the
two moves 84.4% of the time.

[`essay/floor-is-not-a-ceiling`](../../../wiki/findings/essays/floor-is-not-a-ceiling.md), objection
**(B)**, names **execution-format scaffolding** as an explicit, **un-eased** axis the ≥2-move floor
does not touch (verbatim):

> **Execution-format scaffolding.** The on-demand DIRECT gate *states* the order but does not
> scaffold the *execution* into externalized steps. An elicitation that decomposes the execution
> itself (an explicit step-by-step working surface) eases the localized difficulty directly, and is
> un-eased.

Every prior run **forbade a working surface**: the system prompt demanded "EXACTLY ONE figure name
and NOTHING ELSE — no explanation, no reasoning", and gemini ran at reasoning `effort: minimal`. A
model that cannot externalize the two-step execution may apply only one move **for that reason**. This
probe eases exactly that axis. This is [`essay/floor-is-not-a-ceiling`](../../../wiki/findings/essays/floor-is-not-a-ceiling.md)
revision-trigger (b) probe (a witness on an open axis) and the [`essay/witness-seeking-economics`](../../../wiki/findings/essays/witness-seeking-economics.md)
"ease the implicated axis" move.

## The single manipulated variable = the elicitation format (a working surface)

The underlying trials are **byte-identical** to the figure-to-figure K=4 run
([`2026-06-18-relational-order-composition-c-fig`](../2026-06-18-relational-order-composition-c-fig/)):
`build_trials.py`, `SEED0`, the 96 records/model (64 COMP + 32 DIRECT), the geometry, the
shortcut-proofing asserts, `analyze.py`, the figure-to-figure rendering, the two arms, the
thresholds, and the verdict map are all unchanged, so `stimuli.json`'s rstrip sha256 is **identical**
to the fig/K=4 runs.

The **only** change is the response format:

- **Before (fig run):** forced — "Reply with EXACTLY ONE figure name … and NOTHING ELSE — no
  explanation, no reasoning." Parser: the whole reply must be one figure.
- **Now:** "You MAY think step by step and show your working … write your final answer on the LAST
  line in EXACTLY this form: `FINAL: <figure>`." Parser: read the **last `FINAL:` tag** whose figure
  is present (target-blind: keyed on position in the reply, never on which figure is correct);
  fallback to a last-line single-figure read; a `finish_reason == "length"` reply is never parsed.

The reasoning-effort knob is held **constant** — gemini stays at `effort: minimal`, exactly as in the
four prior runs; the working surface is opened only in the visible **output** channel. The max-token
cap is raised (512 → 1024) and the parser changed to read the `FINAL:` tag; **both are necessary
consequences of permitting working, not independent manipulations.** Geometry / scoring / verdict map
are format-invariant (`analyze.py` operates on parsed picks vs. the target).

This is a **within-trial** comparison — the very same 96 fig trials, with vs. without a working
surface:

- **Witness** (gemini/gpt clear DIRECT ≥ 0.80 with working permitted, where they failed forced):
  attributes the prior failures to the **execution-format constraint** (no working surface) →
  confirms [`essay/floor-is-not-a-ceiling`](../../../wiki/findings/essays/floor-is-not-a-ceiling.md)
  objection (B); re-opens the COMP order-sensitivity question for them. A genuinely **new positive**
  on the composition line.
- **Non-witness** (DIRECT still fails with a scratchpad): the composition gap is robust even when the
  models may externalize the execution — a strong further bound localizing the difficulty to chaining
  **execution capacity** (still **undischargeable**, per
  [`essay/undischargeable-negative`](../../../wiki/findings/essays/undischargeable-negative.md));
  updates the witness-search suspension note (not a closure).
- **claude = positive control**: should still clear DIRECT (ideally RESPECTS-ORDER); a claude failure
  would mean the format change broke the instrument, not that the others are limited.

The **DIRECT gate is the empirical arbiter of "easier"** — the easiness claim is measured, not assumed.

## Frozen stimuli

- `stimuli.json` rstrip-sha256 = **`975e31bc4f13aff0e220a44cd709a62821f5a0a6a1cc03883a212debf3ef88ba`**
  (byte-identical to the fig/K=4 runs; `probe._require_frozen` hashes the rstrip'd bytes).
- Built by `build_trials.py` (no API), seed `SEED0 = 20260619`. **96 unique records** (64 COMP + 32
  DIRECT), each served to **3 models → 288 finding-bearing calls**.

## The binding adjudication (carried over unchanged, biased AGAINST the rich reading)

An operation-order gap here is **THIN** (the stamped move-list and the figure maps are in the record;
single-reader-recoverable). A RESPECTS-ORDER positive is a thin **"respects operation order"**
finding — **NOT** rung (iii) / constitution. The rich-side rung (iii) is documented **structurally
closed** for text-only stimuli (a transcript IS a final content+stamps record). Both verdicts thin.

**Permitting a working surface does NOT make COMP non-spontaneous:** the COMP query still does **not**
state the order, so the model must still **decide** to order by the round stamps; the scratchpad only
lets it externalize whatever ordering it chooses.

## Design (frozen; figure-to-figure rendering, working-surface format)

K=4 distinct figures. "DAX" starts on a stated figure; two stamped moves from {STEP: `p→(p+1)%4`,
FLIP: `p→3−p`} (non-commuting), each rendered as a figure→figure lookup table (no positions). COMP =
4 valid configs × 4 reps × K = 64; DIRECT = 4 configs × 2 reps × K = 32.

- **COMP (headline):** "Which figure does DAX sit on now?" — order not stated. Score `target_rate =
  P(pick == stamp-order end figure)`. Diagnostics: `swapped` (reversed-order), `start`, `step1`,
  `flip1`.
- **DIRECT (gate):** order stated explicitly ("first … then …"). Score `direct_acc`.

## Pre-registered thresholds (frozen, byte-identical to the four prior runs)

- `PRINT_CEILING = 0.50` — print-order / canonical-order reader's COMP score (proven at build).
- `DIRECT_FLOOR = 0.80` — on-demand composition gate.
- Composition bar = COMP `target_rate` Wilson-95 **lower bound > 0.50**.
- `POS_CHANCE = 1/K = 0.25` (figure-identity chance).

## Verdict map (frozen, per model — byte-identical to the four prior runs)

| condition | verdict |
|---|---|
| `direct_acc < 0.80` | **UNINTERPRETABLE** |
| DIRECT pass **and** COMP target Wilson-LB **> 0.50** | **RESPECTS-ORDER** (order-sensitive composition; thin) |
| DIRECT pass **and** COMP target Wilson-LB **≤ 0.50** | **ORDER-BLIND-OR-WEAKER** (thin; order-insensitive here) |

Both outcomes are **thin / single-reader-recoverable**; neither approaches constitution.

## Shortcut-proofing (certified pre-run; inherited unchanged)

`build_trials.assert_balance` (PASS): target figure uniform (= 1/K); target track position uniform
(picker ≤ 1/K); print-order & both canonical-order readers = exactly 0.50; start / single-move /
reversed-order readers = 0; frequency flat. `fixtures/make_fixtures.py` (**ALL FIXTURE ASSERTS
PASS**): only genuine stamp-order composition yields RESPECTS-ORDER; every print/canonical reader
0.50; every position/identity reader 1/K; any reader failing on-demand → UNINTERPRETABLE. The
fixtures test `analyze.py`'s logic, which is rendering- and format-invariant. The new `FINAL:`-tag
parser was unit-tested before freeze (10 cases incl. last-tag-wins, article/quote tolerance,
ambiguous-line → None, empty → None; length-truncation → None).

## Spend (frozen)

A working surface raises **output** tokens vs. the forced single-token fig run ($0.366 billed).
Pre-flight ≈ **$0.8–1.0 billed** (288 calls; claude CoT the driver; gemini held at `effort: minimal`
so its reasoning tokens stay capped). `HARD_STOP_USD = 1.50` on projected total. Record actual
`usage.cost` after. Day total before this run = **$0.00 of $5.00** (2026-06-19).

## Anti-cheat

The verdict map is symmetric and pre-registered: a non-witness (DIRECT still fails) **sharpens** the
claude-only reading and is fully reportable; a witness re-opens the COMP question and confirms
objection (B); neither is "the win", and **neither reaches rung (iii)** (adjudicated thin before the
run). No threshold may be retuned after seeing data. The instrument changes *only* by response format
(forced single-token → working-surface) from the byte-identical fig run; the parser is target-blind.
`anchor: internal-contrast-only`. **Governance (provisional):** an elicitation/response-format easing
of the already-ratified Option-C instrument under
[`decisions/resolved/relational-rung-iii-path-dependence`](../../../wiki/decisions/resolved/relational-rung-iii-path-dependence.md)
and the ratified `internal-contrast-only` posture — the same kind of within-frame easing as the K=4
scale, the fig rendering, the worked-example scaffold, and the gpt third-model extension, none of
which owed a new decision. **No new `wiki/decisions/open/` entry owed** — but the independent pre-run
critic gates this judgement and may flag otherwise.

## Independent pre-run critic

**GO** (fresh independent agent, 2026-06-19, before any finding-bearing call). The critic recomputed
the geometry itself (did not trust the run's code): STEP/FLIP **do not commute** at all 4 starts
(SF→{2,1,0,3}, FS→{0,3,2,1}); recomputed `target`/`swapped`/`step1`/`flip1` for **all 96 records**
from `track`+`start_idx`+`order` (**0 mismatches**); confirmed `stimuli.json` rstrip-sha256
`975e31bc…88ba` matches PREREG and `probe._require_frozen`, **byte-identical** to the fig run.
Confirmed `build_trials.py`, `analyze.py`, and the fixtures are **byte-identical** to the fig run
(and `analyze.py` byte-identical to the K=4 run → thresholds/verdict-map carried across all runs,
no post-hoc tuning). Recomputed the shortcut-proofing: start/step1/flip1/swapped readers = **0.000**;
print-order / both canonical readers = **exactly 0.500**; target shape and target track-position both
**perfectly uniform (1/K)** — only stamp-ordering clears 0.50. Diffed `common.py` vs the fig run:
the only functional changes are **format-only** (SYS, STERN, build_user final line, the `FINAL:`-tag
parser, `MAX_TOKENS` 512→1024, `HARD_STOP_USD` 0.60→1.50, docstring) — **`REASONING` unchanged**
(gemini's effort knob held constant), no geometry/scoring/threshold drift. Verified the parser is
**target-blind** (12/12 hand cases: keys on reply position — last `FINAL:` tag, else last-line single
figure — never on which figure is correct; last-tag-wins; `finish_reason=="length"` → never parsed).
Rendered COMP/DIRECT prompts: move tables correct, no position leak, COMP does not state the order
(stays spontaneous), DIRECT does, no target leak. **Governance: NO new `wiki/decisions/open/` entry
owed** — an elicitation/response-format easing within the ratified Option-C / `internal-contrast-only`
frame (`decisions/resolved/relational-rung-iii-path-dependence`), the same kind as the K=4, fig,
worked-example, and gpt-extension easings; elicitation format is not a parameter that decision froze.
Spend sanity confirmed (~$0.95 pre-flight, $1.50 hard stop checked every 20 records; will not approach
the $5.00 cap). **No BLOCKER, no SHOULD-FIX**; three cosmetic NITs — two applied (clarified the
"96 records / 288 calls" wording; removed an unused `import string`), one accepted as unavoidable
(the tag-free fallback path, which stays target-blind).
