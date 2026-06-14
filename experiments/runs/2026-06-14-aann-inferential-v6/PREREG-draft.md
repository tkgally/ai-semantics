# PREREG (DRAFT) — AANN inferential v6: powered panel replication of v4 (fresh held-out adjectives, wider N)

**STATUS: DRAFT, written BEFORE any model call.** To freeze: a **fresh independent
pre-run critic** must return **GO** on this PREREG + the design + `stimuli.json` +
`probe.py`/`analyze.py`; the orchestrator then commits this as `PREREG.md` (this
draft retained for the diff trail). `probe.py` refuses to run while only the draft
exists, and refuses to run if `analyze.py` is absent. **No new decision** is opened:
v6 runs under the already-ratified AANN inferential instruments, so the cross-session
ratification gate is already satisfied (the yardstick is fixed; only a fresh item set
is introduced). A whole-design **HEADROOM-FAIL** (< 2 models clear N1) routes to the
Option-B named null, not a forced positive — identical to v4.

**Design:** [`experiments/designs/aann-construction-v6-inferential.md`](../../designs/aann-construction-v6-inferential.md).
**Governing decisions (the spec, unchanged):**
[`decisions/resolved/aann-inferential-default-coincidence`](../../../wiki/decisions/resolved/aann-inferential-default-coincidence.md)
+ [`decisions/resolved/aann-inferential-operationalization`](../../../wiki/decisions/resolved/aann-inferential-operationalization.md).
Result anchor fixed at **`internal-contrast-only`**; key **expert-stipulated**.

## What v6 is

A **clean replication** of v4 with **one change: the item set** (40 fresh held-out
items, temporal 20 / distance 20, vs v4's 23). The instrument, parsing, four arms,
thresholds, headroom gate, verdict map, and analysis code are **identical to v4**
(`analyze.py` byte-identical save run name / design path / bootstrap seed 20260614;
`probe.py` logic byte-identical, ABORT raised 0.50 → 0.75 for the larger N).

## Pre-registered questions (fixed before any call)

1. Does the panel-wide paraphrase double-contrast shift **hold up powered** (≥ 2 of 3
   models reach Δ² positivity on the fresh, larger, held-out set)?
2. Does **gpt-5.4-mini's cross-instrument convergence** (paraphrase + NLI + agreement)
   **replicate** on fresh held-out adjectives?

**Replication expectation (direction only, no magnitude claim):** if v4 was real, v6
returns **PARTIAL or SUPPORTED** and gpt-5.4-mini is again **CONVERGENT-POSITIVE**. A
NULL, a LEXICAL-CUE ARTIFACT verdict, or gpt failing to replicate each **weakens** the
v4 reading and is reported as a first-class result.

## The indicator, frozen (identical to v4)

The construction makes a model draw the **unification / whole-evaluation** inference,
measured **only** as the **double contrast Δ² = P(uni|AANN) − P(uni|LCC)** on the
PRIMARY paraphrase forced-choice arm — never the raw AANN rate, never a
human-comparison claim. NLI (affirm-rate Δ² over unification + whole-eval hypotheses,
**both-hypothesis** aggregation) is the convergent arm; the singular-agreement
(was/were) shift vs the **bare-plural** control (N4) is the load-bearing
discriminator. No instrument is reselected after seeing outputs.

## The three premise frames (per item)

1. **AANN** — the construction. *We spent a magical three days in Venice.*
2. **DDC (distributive-default control, N1 headroom frame)** — *On each of the three
   days in Venice, it was magical.*
3. **LCC (lexical-cue control, N2 construction-isolating)** — *On each of the three
   magical days in Venice, we wandered.* Δ² = P(uni|AANN) − P(uni|LCC).

## Arms (four; all required; 1392 calls = 464/model × 3)

*(40 base items, temporal 20 / distance 20.)*

| Arm | Items × frames × models | Calls | Bearing |
|---|---|---|---|
| `paraphrase` | 40 × 3 frames × 3 | 360 | PRIMARY: U/D forced choice over {aann,ddc,lcc}; indicator = **Δ²** |
| `nli` | 40 × 2 hyp × 3 frames × 3 | 720 | CONVERGENT: affirm-rate **Δ²** (unification + whole-eval) |
| `agreement` | 40 × 2 ({aann, bare-plural}) × 3 | 240 | DISCRIMINATOR (load-bearing): singular-agreement shift |
| `tier0` | 24 pairs × 3 | 72 | gate-bearing manipulation check, per model |

Per model: paraphrase 120 + nli 240 + agreement 80 + tier0 24 = **464**; total
**1392**. An absent or partial file for **any** arm makes the run **INCOMPLETE** (no
substantive verdict).

## Frozen inputs (committed before the run; built by `prep.py`, no model calls)

- `stimuli.json` — seed 20260614, **40 hand-authored base items**. All 40 adjectives
  are **held-out** (disjoint from v4's 21 and the v5-reflex probe's 30, asserted) and
  consonant-initial (asserted). Each item carries the three frames, the bare-plural
  control (agreement arm), the two U/D paraphrase options with seeded A/B
  counterbalance and equal lexical-overlap parity (N3), per-item
  `control_lexical_delta`, the NLI unification + whole-evaluation hypotheses, the
  was/were agreement pair with seeded counterbalance, per-item local-fluency
  direction (I4), the expert-stipulated unification key (N5/I5/I6), and the
  item-level `key_disputed` flag (1 item: `freezing forty yards`). 24 Tier-0 pairs
  (first 6 base AANN × the 4 Mahowald degenerate variants, position counterbalanced).
  - **Under-pressure subset (I4):** 22 items where the distributive paraphrase is the
    locally-fluent continuation; analysed separately.
- **Expert-stipulated key (N5/I5/I6):** the unification reading is the AANN-licensed
  answer per the design author's coding of the published AANN semantics (Solt 2007;
  Dalrymple & King 2019; Bylinina & Nouwen 2018 — named, NOT quoted, not in-repo). A
  scoring key, **not** a human anchor.
- `analyze.py` exists at freeze with the headroom gate + thresholds + Δ² +
  headline-gating + full verdict map baked in (`--selftest`: 38 checks pass);
  `probe.py` refuses to run without it. The post-run verifier recomputes from raw with
  independent code.

## Frozen instrument (per-model settings; identical to v4)

Temperature 0; max_tokens 64 (A `claude-sonnet-4.6`, B `gpt-5.4-mini`) / 512
(C `gemini-3.5-flash`, `reasoning: {"effort": "minimal"}`). Counterbalancing in the
frozen stimuli; `analyze.py` maps the chosen letter back to content.

**Parsing.** Paraphrase/agreement/Tier-0: full-string A/B, else the LAST standalone
A/B token (markdown-bold-stripping). NLI: full-string YES/NO, else the LAST standalone
YES/NO token. One verbatim retry per unparseable response, then missing.

**Missingness (per arm):** >10% = mandatory caveat; >25% = instrument failure for that
arm. Any required arm absent/partial = INCOMPLETE.

## Frozen thresholds (identical to v4; baked in `analyze.py`, no post-hoc tuning)

- **Δ² threshold τ = +0.20, INCLUSIVE**; a "positive" Δ² also needs the item-level
  bootstrap 95% CI lower bound > 0 (STRICT), 10,000 resamples, **seed 20260614**, on
  the per-item AANN−LCC difference.
- **Headroom gate (N1, pre-headline, per model):** P(uni|DDC) ≤ 0.30 PASS / ≤ 0.50
  MARGINAL (caveat) / > 0.50 HEADROOM-FAIL (excluded from headline). Whole-design: <
  2 of 3 clear → **HEADROOM-FAIL → OPTION-B NAMED NULL**.
- **Agreement shift** = P(was|AANN) − P(was|bare-plural control); same τ + bootstrap.
- **Tier-0 GATE:** ≥ 20/24 AANN-preferred (inclusive); > 25% missing = instrument
  failure; a failing model's numbers are descriptive-only and excluded from the
  ≥2-of-3 count; < 2 passers → INSTRUMENT FAILURE.
- **Named disagreement |FC Δ² − NLI Δ²|** per model, flag ≥ 0.30, fed to the
  instrument-sensitivity open question, never averaged away.
- **Disputed-coding sensitivity (I6):** paraphrase Δ² positivity recomputed excluding
  the 1 `key_disputed` item; a change attaches a mandatory caveat.

## Frozen verdict map (per model, then stratum) — identical to v4

Per model (over Tier-0-passing, headroom-clearing models): **CONVERGENT-POSITIVE**
(Δ²FC + Δ²NLI + agreement all positive) / **PARAPHRASE-ONLY** (Δ²FC positive,
agreement null → "shift WITHOUT the grammaticalized reflex") /
**PARAPHRASE-PLUS-REFLEX-NO-NLI** / **LEXICAL-CUE ARTIFACT** (AANN shift ≥ τ but Δ² < τ
because the lexical cue accounts for it) / **NULL**.

Stratum (over Tier-0-passing, headroom-clearing models): **SUPPORTED** (≥ 2
CONVERGENT-POSITIVE) / **PARTIAL** (≥ 2 paraphrase-positive, < 2 convergent) /
**LEXICAL-CUE ARTIFACT** (≥ 2) / **NULL** (< 2 paraphrase-positive, not artifact) /
**HEADROOM-FAIL → OPTION-B NAMED NULL** (< 2 clear headroom) / **INSTRUMENT FAILURE**
(< 2 Tier-0 passers). Every outcome — including every null and the headroom-fail —
is a first-class result.

## Anchor discipline (N5/I5)

Result carries **`anchor: internal-contrast-only`** + the chief-cost statement
verbatim. The key is expert-stipulated; Mahowald linked only as measure-noun class
provenance.

## Spend (config/budget.md) — pre-flight estimate (I8)

1392 calls. From v4's measured billed rate ($0.0001524/call), **1392 × $0.0001524 ≈
$0.212** point estimate; **expected ≈ $0.20–0.35 billed** with retries/variance. Well
under $1; day total before this run ≈ $0.974 of $5.00, so the run lands the day total
near ~$1.2–1.3 — well under cap. Single-run **ABORT_USD = $0.75** coded in `probe.py`.
Actual billed `usage.cost` recorded after the post-critic run; missing-cost calls
counted and logged.

DRAFT written 2026-06-14, before any model call. To freeze: the orchestrator commits
this as `PREREG.md` **only after** the fresh independent pre-run critic's GO.
