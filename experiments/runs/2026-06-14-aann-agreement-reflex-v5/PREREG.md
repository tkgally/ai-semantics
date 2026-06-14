# PREREG (FROZEN) — AANN agreement-reflex generalization v5 (held-out replication + panel generalization of the singular-agreement reflex)

**STATUS: FROZEN 2026-06-14, BEFORE any model call.** A fresh independent pre-run critic reviewed
the design + this PREREG + the frozen `stimuli.json` + `analyze.py` and returned **GO** (decision-class
PASS — inside the ratified instrument class, no new decision; anti-cheat PASS — τ=+0.30 biases against a
free positive; freshness/fidelity/verdict-tree/provenance/anchor all PASS; 0 BLOCKERs). This file is the
frozen pre-registration; `probe.py` runs against it. `probe.py` refuses to run while only the draft exists (and refuses to run if `analyze.py`
is absent — the analysis code is part of the freeze). **No v5 model call may be made until** this draft
passes the fresh pre-run critic and is committed as `PREREG.md`. **This probe has NOT run; no v5
number exists anywhere; every cost figure below is an ESTIMATE for a not-run experiment.** Design-writing
is not probe-running; building these materials makes no calls.

**Design:** [`experiments/designs/aann-agreement-reflex-generalization-v5.md`](../../designs/aann-agreement-reflex-generalization-v5.md)
(frozen). **Governing decision (the spec; NO new decision is taken by v5):**
[`decisions/resolved/aann-inferential-operationalization`](../../../wiki/decisions/resolved/aann-inferential-operationalization.md)
— its **Condition 3** makes the **grammaticalized singular/plural agreement sub-probe** the
**load-bearing discriminator**, controlled by the **bare plural**. v5 reuses that ratified instrument
**unchanged**, on **fresh held-out items**; the result stays fixed at **`anchor: internal-contrast-only`**
scored against an explicitly **expert-stipulated** key. This run tests the **agreement-reflex
generalization** half of [`conjecture/aann-construction`](../../../wiki/findings/conjectures/aann-construction.md).

## Why v5 exists (the question, quoting v3/v4 verbatim — no new numbers)

gpt-5.4-mini's singular-agreement reflex on the AANN: it picks singular *was* for the AANN frame but
plural *were* for the bare-plural control. The two prior results, **quoted verbatim**:

- v3 ([`result/aann-inferential-v3`](../../../wiki/findings/results/aann-inferential-v3.md)):
  **+0.739 · CI [0.57, 0.91] · POSITIVE** — "raw 'was' rate, AANN / control: 0.96 / 0.22".
- v4 ([`result/aann-inferential-v4`](../../../wiki/findings/results/aann-inferential-v4.md)):
  **+0.652** CI[0.43,0.87] · **POS** — "raw 'was' rate, AANN / bare-plural ctrl: 0.957 / 0.304";
  "The grammaticalized reflex **replicates v3** (v3: +0.74; v4: +0.65)."
- claude-sonnet-4.6 and gemini-3.5-flash, both runs: agreement shift **0 · not pos (ceiling)** — "raw
  'was' rate, AANN / bare-plural ctrl: 1.00 / 1.00" — at CEILING, so the contrast was **uninformative**
  for them (structurally blind), **not** a demonstrated failure.

v3 and v4 reused the **same** base items. v5 asks whether (a) gpt's reflex **replicates on fresh
held-out items** and (b) whether claude/gemini show **any off-ceiling contrast** on fresh items or
**remain at ceiling** (confirming the v3/v4 structural-blindness reading on a second sample).

## What is tested (the indicator, fixed pre-run)

The **headline instrument is the v4 agreement arm, UNCHANGED**: a was/were forced choice over two
conditions per held-out item — **AANN frame** vs **bare-plural control frame** — with the indicator
the **single contrast**

> **agreement shift = P(was | AANN) − P(was | bare-plural control)**, per model.

The was/were letter position is counterbalanced per item (`agr_letter_was`); `analyze.py` maps the
chosen letter back to content, so position bias is blocked at the stimulus level. This is the **same**
machinery and the **same** control (bare plural) as v3/v4; only the **items are fresh held-out**.

## Held-out freshness (binding, asserted in stimuli + checked by the critic)

All 30 held-out adjectives are **fresh**: none of the 21 v3/v4 adjectives may reappear (*beautiful,
gruelling, glorious, miserable, restful, punishing, memorable, turbulent, sleepless, hectic, blissful,
brutal, frantic, scenic, muddy, breathtaking, steep, lonely, treacherous, dazzling, relentless*). Each
adjective × measure-noun combination is fresh. Classes are **temporal + distance only** (genuine
extents). `stimuli.json` carries the exclusion list in `freshness_note`; the pre-run critic verifies
zero overlap.

## Arms (three; the agreement arm is the only verdict-bearing one)

*(Geometry: 30 held-out items, temporal 18 / distance 12; 10 count-noun diagnostics; 12 Tier-0 pairs.)*

| Arm | Items × frames × models | Calls | Bearing |
|---|---|---|---|
| `agreement` | 30 × 2 ({aann, bare-plural}) × 3 | 180 | **HEADLINE** (verdict-bearing): singular-agreement single shift |
| `diagnostic` | 10 count-noun × 1 × 3 | 30 | **DESCRIPTIVE-ONLY**, NEVER verdict-bearing: P(were) on genuine count plurals |
| `tier0` | 12 pairs × 1 × 3 | 36 | gate-bearing manipulation check, per model |

Per model: 60 + 10 + 12 = **82**; total **246**. An absent or partial **agreement** file (e.g. after a
budget abort) makes the run **INCOMPLETE**: no verdict is emitted.

## Frozen inputs (committed before the run; hand-authored, no model calls)

- `stimuli.json` — seed 20260614. **30 held-out items** (temporal 18 / distance 12), each with: the
  `aann` and `control_bare_plural` sentences and an `agreement` sub-object carrying `aann_frame`,
  `control_frame`, and the seeded `agr_letter_was` counterbalance (15 A / 15 B) — the v4 agreement
  sub-structure, mirrored exactly. Plus **10 count-noun diagnostic** items (each with a `diagnostic`
  sub-object: `control_frame`, `agr_letter_was`, `expected: "were"`), and **12 Tier-0 pairs** (6
  singular-subject + 6 plural-subject; correct-answer letter balanced 6 A / 6 B; was-position balanced
  6 A / 6 B and uncorrelated with subject number). The expected-agreement **key** (singular *was* =
  AANN-licensed) is recorded per item as **expert-stipulated**.
- **Stimuli sha256 (FROZEN at GO):** `36f2f58221f8188423838be6de76a404a8958f08d068eae354188dd8fa028154` — `sha256(stimuli.json)`, pinned at the moment of the
  pre-run-critic GO, 2026-06-14. Re-verify before reading any result.
- `analyze.py` **exists at freeze** with the verdict tree + thresholds baked in (selftested: 29
  in-memory checks, no files/calls — every per-model and overall branch, the descriptive-only
  diagnostic fence, the Tier-0 gate, the item floor, bootstrap determinism); `probe.py` refuses to run
  without it.

## Frozen instrument (per-model settings)

Temperature 0; max_tokens 64 (A `claude-sonnet-4.6`, B `gpt-5.4-mini`) / 512 (C `gemini-3.5-flash`,
`reasoning: {"effort": "minimal"}`), per `config/models.md` — identical to v3/v4. Counterbalancing lives
in the frozen stimuli; `analyze.py` maps the chosen **letter back to content**.

**Parsing.** Full-string A/B, else the LAST standalone A/B token (v2b last-token convention,
markdown-bold-stripping). One verbatim retry per unparseable response, then missing.

**Missingness (per arm):** > 10% = mandatory caveat; > 25% = instrument failure for that arm. The
agreement arm absent/partial = **INCOMPLETE**.

## Pinned integers (τ, thresholds, floors, seeds, ABORT) — baked in `analyze.py`, no post-hoc tuning

- **Replication / generalization bar τ = +0.30, INCLUSIVE** (shift ≥ +0.30 passes). A **"positive"**
  shift additionally needs the **item-level bootstrap 95% CI lower bound > 0 (STRICT)**. A degenerate
  zero-width CI (an all-ceiling 0/0 cell) carries **no inferential weight** — it can never be positive.
  *(τ is set higher than v3/v4's +0.20 deliberately: this is a replication/generalization test, so the
  bar to declare the held-out reflex present is stricter than the original detection bar. It is fixed
  here, before any v5 output exists; never retuned.)*
- **Ceiling threshold = 0.85, INCLUSIVE** — claude/gemini with a control "was"-rate ≥ 0.85 are
  CEILING-UNINFORMATIVE (the discriminator is structurally blind; **not** a failure).
- **Bootstrap: 10,000 item-level resamples, seed 20260614, percentile 95% CI.**
- **Item floor = 8 gated items** per verdict-bearing cell (in both conditions); below it the cell is
  INCONCLUSIVE-CELL.
- **Tier-0 GATE: pass = ≥ 10/12 correct** (inclusive) per model; > 25% missing = instrument failure.
  Pre-declared failure consequence: a model failing Tier-0 has its agreement numbers reported
  **descriptively only** (INCONCLUSIVE-CELL, kept out of the positive branches); if the **reflex-bearer
  (gpt)** fails Tier-0, the overall verdict is **INCONCLUSIVE**.
- **ABORT_USD = $0.25** single-run flag in `probe.py` (pre-flight ESTIMATE ~$0.03–0.06).

## Frozen scoring / parse rules

- **Agreement / diagnostic / Tier-0 indicator:** `chose_was` = 1 iff the chosen letter equals
  `agr_letter_was` (else 0; None if missing). Diagnostic reports P(were) = 1 − P(was). Tier-0 "correct"
  = chosen letter is the one whose form equals `grammatical_form`.
- **Shift:** item-level mean of (P(was|AANN) − P(was|control)) over items present in BOTH conditions.
- No averaging across arms; the diagnostic is computed in its own function flagged
  `descriptive_only`/`never_verdict_bearing` and enters **no** verdict branch.

## Frozen verdict tree (per model, then overall) — ordered if/else AS CODE, with an explicit final else

**Per the reflex-bearing model (gpt-5.4-mini, slot B):**
- **REPLICATES** if shift ≥ τ (+0.30) **and** bootstrap CI-lower > 0; **else FAILS-TO-REPLICATE.**

**Per claude (A) / gemini (C):**
- **CEILING-UNINFORMATIVE** if control "was"-rate ≥ 0.85 (structurally blind, as in v3/v4 — not a
  failure);
- else **GENERALIZES-TO-PANEL** if shift ≥ τ and CI-lower > 0;
- else **NO-REFLEX.**

*(Any cell below the item floor or whose model failed Tier-0 → INCONCLUSIVE-CELL, kept out of the
positive branches.)*

**Overall verdict (exhaustive; final else explicit):**
- **REFLEX-GENERALIZES-TO-PANEL** — ≥ 1 of {claude, gemini} GENERALIZES (outranks gpt's own outcome);
- else **REFLEX-IS-GPT-SPECIFIC-AND-REPLICATES** — gpt REPLICATES and neither other model generalizes;
- else **REFLEX-FAILS-TO-REPLICATE** — gpt FAILS-TO-REPLICATE and neither other model generalizes;
- else **INCONCLUSIVE** — the final else (e.g. gpt's cell INCONCLUSIVE-CELL and no other generalizes).

Every outcome — including REFLEX-FAILS-TO-REPLICATE, every CEILING-UNINFORMATIVE cell, and INCONCLUSIVE
— is a **first-class result** on the eventual result page. No threshold is retuned post-hoc.

## Descriptive-only count-noun ceiling diagnostic (NON-GATING)

10 true count-noun bare plurals (*Three excited dogs ___ waiting at the gate* → *were*). Reports, per
model, **P(were) on genuine count plurals**, to characterise whether a ceiling model's AANN/bare-plural
ceiling is **notional-singular-for-quantity-subjects** (it can still pick *were* for an ordinary count
plural) rather than a blanket "always picks *was*." **DESCRIPTIVE-ONLY — fenced out of every verdict
branch in code** (`analyze_diagnostic` is flagged `descriptive_only`/`never_verdict_bearing`; the
selftest asserts the diagnostic never appears in the verdict basis).

## Anchor discipline (`internal-contrast-only`)

The result will carry **`anchor: internal-contrast-only`** (within-model AANN-vs-bare-plural agreement
shift; **no human-comparison claim**). **No in-repo resource anchors agreement-reflex behavior** — no
human AANN-agreement dataset exists in the repo — so no human-comparison claim is possible or attempted.
[`resource/mahowald-2023-aann-stimuli`](../../../wiki/base/resources/mahowald-2023-aann-stimuli.md) is
**CLASS PROVENANCE ONLY** (the temporal/distance measure-noun classes); Mahowald's MTurk data are 1–10
acceptability ratings, never an agreement anchor. The expected-agreement key (singular *was* =
AANN-licensed) is **EXPERT-STIPULATED** (Solt 2007 unit-coercion; Dalrymple & King 2019; Bylinina &
Nouwen 2018 — named, NOT quoted, NOT in-repo). The result page carries the **chief-cost statement
verbatim:** *the v5 can never say "models pick the singular agreement the way humans do" — only that
the construction shifts the within-model singular-agreement choice relative to a matched bare-plural
control, in the direction the published AANN semantics predicts.*

## Gate check — NO new decision (inside the ratified instrument class)

v5 takes **no new operationalization decision** and needs **no `wiki/decisions/open/` entry**: it
re-runs the **ratified** agreement load-bearing discriminator (Condition 3 of
[`decisions/resolved/aann-inferential-operationalization`](../../../wiki/decisions/resolved/aann-inferential-operationalization.md))
unchanged, on fresh held-out items (the v2/v2b held-out-generalization move, within the v2
form-instrument family). The anchor (`internal-contrast-only`) is already ratified for this line. The
freeze + fresh-pre-run-critic gate still binds, but as a **materials/PREREG** review, not a new
operationalization ratification. Hence the design is `contingent-on: []`.

## Spend (config/budget.md) — pre-flight ESTIMATE for a NOT-RUN experiment

246 calls (82/model × 3: agreement 180 + diagnostic 30 + tier0 36). **ESTIMATE** from v4's **measured
billed** rate (831 calls / $0.1266 billed = **~$0.00015 per call**): **246 × ~$0.00015 ≈ $0.037**
(point estimate); with the one verbatim retry per unparseable response and variance, **expected ≈
$0.03–0.06 billed.** **Far under $1** and **far under the $5.00/day UTC budget cap.** Single-run
**ABORT_USD = $0.25** flag coded in `probe.py`. **These are estimates for a not-run experiment**; the
actual billed `usage.cost` would be recorded in `raw/cost-log.txt` and the run record **after** the
later, post-critic run, with calls missing `usage.cost` counted and logged, never silently discarded.

FROZEN 2026-06-14 after the fresh independent pre-run critic's GO. `sha256(stimuli.json)` = `36f2f58221f8188423838be6de76a404a8958f08d068eae354188dd8fa028154`,
recorded above. The `-draft` file is retained for the diff trail.
