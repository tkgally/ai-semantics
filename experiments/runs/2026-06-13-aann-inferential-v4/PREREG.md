# PREREG — AANN inferential v4 (paraphrase-FC primary + NLI convergent + agreement discriminator, DOUBLE-CONTRAST against a distributive-default control)

**STATUS: FROZEN 2026-06-13, BEFORE any model call.** This pre-registration was frozen from the reviewed draft after a **fresh independent pre-run critic returned GO** (condition-by-condition PASS on all six new + eight inherited conditions; anti-cheat PASS; analyze.py fidelity PASS; all 23 items judged buildable, none failing N1/N2). The earlier `-draft` is retained in this directory as the pre-freeze record. `probe.py` refuses to run while only the draft exists
(and refuses to run if `analyze.py` is absent — the analysis code is part of the freeze).
**No v4 model call may be made until** (a) the governing decisions are ratified
(DONE: 2026-06-13 autonomous adversarial review for both
[`aann-inferential-default-coincidence`](../../../wiki/decisions/resolved/aann-inferential-default-coincidence.md)
and [`aann-inferential-operationalization`](../../../wiki/decisions/resolved/aann-inferential-operationalization.md))
**and** (b) this draft passes the fresh pre-run critic and is committed as `PREREG.md`.
A **NO-GO on N1/N2 buildability triggers the Option-B fallback (§8 of the design), not a
run.** Design-writing is not probe-running; building these materials makes no calls.

**Design:** [`experiments/designs/aann-construction-v4-inferential.md`](../../designs/aann-construction-v4-inferential.md)
(frozen; carries the six-new + eight-inherited condition → design-location checklist in its §0).
**Governing decisions (the spec):**
[`decisions/resolved/aann-inferential-default-coincidence`](../../../wiki/decisions/resolved/aann-inferential-default-coincidence.md)
(ADOPT Option A — distributive-default control — under **six** amended binding conditions; Option B
the binding fallback) + the inherited
[`decisions/resolved/aann-inferential-operationalization`](../../../wiki/decisions/resolved/aann-inferential-operationalization.md)
(**eight** binding conditions; all inherited except the Condition-2 minimal-pair clause, re-justified
in design §3.3). The v4 result stays fixed at **`anchor: internal-contrast-only`** scored against
an explicitly **expert-stipulated** literature key. This run tests the **inferential half** of
[`conjecture/aann-construction`](../../../wiki/findings/conjectures/aann-construction.md).

## Why v4 exists (the v3 cause this design removes)

v3 ([`result/aann-inferential-v3`](../../../wiki/findings/results/aann-inferential-v3.md)) returned a
**ceiling-bounded NULL**: no model shifted the unification-vs-distributive reading relative to the
**bare-plural** control *three beautiful days*, **because the models already read that bare plural as
a unified evaluated stretch nearly every time.** v3's documented control raw rates (quoted verbatim,
the cause v4 removes; no new numbers invented): paraphrase control **0.78 / 0.96 / 1.00**
(claude / gpt / gemini); NLI control **0.87 / 0.83 / 1.00**. The AANN-vs-control shift subtracts a
baseline already at the unification ceiling, leaving no headroom. v4's single structural change:
replace the ceiling-pinned bare-plural paraphrase/NLI control with a **distributive-default control
(DDC)** whose baseline reading is genuinely distributive, and add a **lexical-cue control (LCC)** arm
that proves any measured shift is the **construction's**, not the imported itemizing cue's.

## What is tested (the indicator, fixed pre-run)

The construction makes a model draw the **unification / whole-evaluation** inference — *a beautiful
three days* = one unified evaluated stretch, NOT three separately-evaluated days — measured **only**
as the **double contrast Δ²** (inherited Condition I2 as amended; new Condition N2), never the raw
AANN rate, never a human-comparison claim (Condition N5/I5).

## Primary instrument (Condition I1 — fixed before any call)

**Arm A (paraphrase forced-choice) is PRIMARY.** Arm B (entailment NLI) is the convergent robustness
arm. The **agreement (was/were) sub-probe** is the **load-bearing discriminator** (Condition I3/N4),
reported separately and weighted above the paraphrase arm; its control stays the **bare plural**
(N4), not the DDC. No instrument is reselected after seeing outputs.

## The three premise frames (the double-contrast geometry, Conditions N1+N2)

Each base item carries three premise frames; the paraphrase and NLI arms iterate all three:

1. **AANN** — the construction, verbatim from v3. *We spent a beautiful three days in Rome.*
2. **DDC (distributive-default control)** — explicitly itemizing, adjective predicated per-unit,
   baseline reading genuinely distributive. *On each of the three days in Rome, it was beautiful.*
   This is the **N1 headroom frame**.
3. **LCC (lexical-cue control)** — the **same** itemizing cue, adjective **attributive** on the plural
   noun, **no AANN**, an ordinary plural. *On each of the three beautiful days in Rome, we relaxed.*
   The **construction-isolating** control (N2): algebraically Δ² = P(uni|AANN) − P(uni|LCC).

## Arms (four; all required; 831 calls = 277/model × 3)

*(Geometry: 23 base items, temporal 13 / distance 10; object/mass class stays dropped.)*

| Arm | Items × frames × models | Calls | Bearing |
|---|---|---|---|
| `paraphrase` | 23 × 3 frames × 3 | 207 | PRIMARY: U/D forced choice over {aann,ddc,lcc}; indicator = **Δ²** |
| `nli` | 23 × 2 hyp × 3 frames × 3 | 414 | CONVERGENT: affirm-rate **Δ²** (unification + whole-eval) |
| `agreement` | 23 × 2 ({aann, bare-plural}) × 3 | 138 | DISCRIMINATOR (load-bearing): singular-agreement shift |
| `tier0` | 24 pairs × 3 | 72 | gate-bearing manipulation check, per model |

Per model: paraphrase 69 + nli 138 + agreement 46 + tier0 24 = **277**; total **831**.
An absent or partial file for **any** arm (e.g. after a budget abort) makes the run **INCOMPLETE**:
no substantive verdict is emitted.

## Frozen inputs (committed before the run; built by `prep.py`, no model calls)

- `stimuli.json` — seed 20260613, **23 hand-authored base items** (temporal 13 / distance 10; object
  class dropped). Each item carries: the three premise frames (`frames.aann` / `frames.ddc` /
  `frames.lcc`); the bare-plural control (`control_bare_plural`, agreement arm only, N4); the **same
  two paraphrase options** U/D as v3, presented identically across all three frames, with **seeded A/B
  counterbalance** (`fc_letter_unification`) and per-item **paraphrase-option lexical-overlap counts**
  (Condition N3 — all 23 items have **equal** U/D premise overlap, parity asserted in `prep.py`, its
  scope documented); per-item **`control_lexical_delta`** (the count of content words the DDC
  adds/removes vs the AANN premise — N3; the LCC carries the same itemizing cue, asserted); NLI
  unification + whole-evaluation hypotheses (+ distributive foil); the was/were agreement pair with
  seeded counterbalance (`agr_letter_was`); per-item **local-fluency direction** (Condition I4); the
  **expert-stipulated** unification key (Condition N5/I5/I6); item-level **`key_disputed`** flag (1
  item — the yards inventory-edge item). The 24 Tier-0 pairs (6 base AANN frames × the 4 Mahowald
  degenerate variants `reverse_mods`/`no_mod`/`no_plural`/`no_a`, AANN position counterbalanced) are
  built mechanically.
  - **Under-pressure subset (Condition I4):** 10 items where the **distributive** paraphrase is the
    locally-fluent continuation; the DDC is *itself* the under-pressure condition by construction; the
    subset's Δ² is analysed separately.
  - **Adjectives are evaluatively-loaded;** items where world-knowledge **alone** forces unification
    were excluded at authoring.
- **Expert-stipulated key (Condition N5/I5/I6), verbatim in `stimuli.json`:** the unification reading
  is the AANN-licensed answer per the design author's coding of the published AANN semantics (Solt
  2007 unit-coercion; Dalrymple & King 2019; Bylinina & Nouwen 2018 — named as the analyses the
  stipulation rests on, NOT quoted; they are not in-repo). A scoring key, **not** a behavioral-human
  anchor.
- `analyze.py` **exists at freeze** with the headroom gate + thresholds + Δ² + headline-gating +
  full verdict map baked in (selftested: 38 checks, including a clean CONVERGENT-POSITIVE scenario and
  a HEADROOM-FAIL scenario); `probe.py` refuses to run without it. The post-run verifier recomputes
  from raw with independent code.

## Frozen instrument (per-model settings)

Temperature 0; max_tokens 64 (A `claude-sonnet-4.6`, B `gpt-5.4-mini`) / 512 (C `gemini-3.5-flash`,
`reasoning: {"effort": "minimal"}`), per `config/models.md`. Counterbalancing lives in the frozen
stimuli; `analyze.py` maps the chosen **letter back to content** so position bias is blocked at the
stimulus level.

**Parsing.** Paraphrase/agreement/Tier-0: full-string A/B, else the LAST standalone A/B token (v2b
last-token convention, markdown-bold-stripping). NLI: full-string YES/NO, else the LAST standalone
YES/NO token. One verbatim retry per unparseable response, then missing.

**Missingness (per arm):** >10% = mandatory caveat; >25% = instrument failure for that arm. Any
required arm absent/partial = **INCOMPLETE**.

## Headroom-precondition gate (Condition N1) — checked PRE-HEADLINE, per model

Read **before** any AANN contrast is interpreted. For each model, the DDC baseline unification rate
P(unification | DDC) on the primary paraphrase arm must be materially off-ceiling:

- **P(uni|DDC) ≤ 0.30 → PASS** (headroom; the model's Δ² is interpreted).
- **0.30 < P(uni|DDC) ≤ 0.50 → MARGINAL** (interpreted only with a mandatory reduced-headroom caveat).
- **P(uni|DDC) > 0.50 → HEADROOM-FAIL** (the v3 cause is NOT removed for this model; its
  paraphrase/NLI numbers are reported descriptively and **excluded** from the headline).
- **Whole-design gate:** if **fewer than 2 of 3 models** clear (PASS/MARGINAL), the v4 paraphrase/NLI
  headline **must not be interpreted at all** → **HEADROOM-FAIL → OPTION-B NAMED NULL** (§8): record
  the inferential half as terminally untestable-at-paraphrase-instrument for AANN and redirect to the
  cancel-direction (conative) route.

The NLI arm carries an analogous DDC-baseline check, **reported alongside but not gating** the
primary (paraphrase) headline.

## Frozen thresholds and statistics (per model) — baked in `analyze.py`, no post-hoc tuning

From the three frame rates per arm:

- **AANN shift** = P(uni|AANN) − P(uni|DDC).
- **lexical-cue shift** = P(uni|LCC) − P(uni|DDC).
- **Double contrast Δ²** = (AANN shift) − (lexical-cue shift) = P(uni|AANN) − P(uni|LCC) — **the
  headline.** The construction's contribution net of the lexical cue.

- **Δ² threshold τ = +0.20, INCLUSIVE** (Δ² ≥ +0.20 passes). A **"positive"** Δ² additionally needs
  the **item-level bootstrap 95% CI lower bound > 0 (STRICT)**, 10,000 resamples over items, seed
  20260613, on the per-item AANN−LCC difference. τ is **reused from v3 unchanged** (a net shift under
  20 pp on a binary forced choice is not distinguishable from labelling noise at this item count); the
  bootstrap is on the *difference of differences*, which is *more* conservative than v3's single
  difference — biased **against** a free positive, as the ratification demands. **No threshold is set
  or retuned after any pilot/dry-run output (Condition I8).**
- **Agreement shift** (load-bearing, N4) = P(was|AANN) − P(was|bare-plural control); same τ + bootstrap
  CI-lower > 0. (Single contrast — the bare plural is the right control because singular agreement on a
  plural head is distributionally dispreferred, so the distributional story predicts the *opposite* of
  the inferential story; no lexical-cue control is needed there.)
- **Tier-0 GATE:** pass = **≥ 20/24 AANN-preferred** (inclusive); >25% missing = instrument failure.
  **Pre-declared failure consequence (Condition I7):** a model failing Tier-0 has its inferential
  numbers reported **descriptively only** and is **excluded** from the ≥2-of-3 count; fewer than 2
  Tier-0 passers ⇒ **INSTRUMENT FAILURE**.
- **Named disagreement statistic (Condition I7):** **|FC Δ² − NLI Δ²|** per model, fed to
  [`open-question/instrument-sensitivity-constructional-inference`](../../../wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md),
  **never averaged away**. Flag (mandatory per-model fragility caveat) if ≥ 0.30 (inclusive).
- **Disputed-coding sensitivity (Condition I6):** the paraphrase-arm Δ² positivity is recomputed
  excluding the 1 item-level `key_disputed` item; if positivity changes, a mandatory caveat attaches.

## Frozen verdict map (per model, then stratum) — pre-declared (Conditions N1, N2, I3, I7)

Per model (over Tier-0-passing, headroom-clearing models), after the headroom gate:

- **CONVERGENT-POSITIVE:** Δ²(FC) positive **AND** Δ²(NLI) positive **AND** agreement shift positive.
  Headline: "the construction shifts inferential behaviour, including the grammaticalized singular
  reflex, relative to a matched control, in the direction the published semantics predicts."
- **PARAPHRASE-ONLY (Condition I3/N4 headline gate):** Δ²(FC) positive but the **agreement** shift
  null. Headline: **"shift in paraphrase selection WITHOUT the grammaticalized reflex"** — **not**
  "draws the unification inference."
- **PARAPHRASE-PLUS-REFLEX-NO-NLI:** Δ²(FC) + agreement positive but NLI not — not full convergence;
  flagged for the disagreement statistic.
- **LEXICAL-CUE ARTIFACT (new, Condition N2):** the **AANN shift** ≥ τ **but Δ² < τ** (or CI straddles
  0) **because the lexical-cue shift accounts for it** (operationally: AANN shift ≥ τ **and**
  lexical-cue shift ≥ (AANN shift − τ)). The paraphrase arm is a lexical-cue artifact for that model:
  the imported itemizing cue, not the AANN construction, moved the reading. It **cannot carry the
  headline.**
- **NULL:** Δ²(FC) not positive and the lexical-cue-artifact condition does not apply.

**Stratum verdict (over Tier-0-passing, headroom-clearing models only):**

- **SUPPORTED (inferential half):** ≥ 2 CONVERGENT-POSITIVE.
- **PARTIAL (paraphrase/constructional shift without full convergence):** ≥ 2 reach paraphrase Δ²
  positivity but < 2 CONVERGENT-POSITIVE.
- **LEXICAL-CUE ARTIFACT:** ≥ 2 LEXICAL-CUE ARTIFACT — the apparent shift is the imported cue; the
  double contrast did its job. A first-class outcome.
- **NULL:** < 2 reach even paraphrase positivity (and not a lexical-cue artifact) — a first-class null.
- **HEADROOM-FAIL → OPTION-B NAMED NULL:** < 2 models clear the headroom precondition (§8).
- **INSTRUMENT FAILURE:** < 2 Tier-0 passers.

Every outcome — including every null, the lexical-cue-artifact outcome, and the headroom-fail outcome
— is a first-class result on the eventual `wiki/findings/results/aann-inferential-v4.md` page.

## Anchor discipline (Condition N5/I5)

The result will carry **`anchor: internal-contrast-only`** (within-model **double** contrast; **no
human-comparison claim**), the terminal state carried forward from both governing decisions. Mahowald
linked **only** as stimulus provenance / v2 gradient anchor — never as the inference anchor (Mahowald's
MTurk data are 1–10 acceptability ratings; no human there was asked the unification-vs-distributive
question). The literature key is **expert-stipulated**, labelled as such everywhere. The result page
carries the **chief-cost statement verbatim:** *the v4 can never say "models draw the inference the
way humans do" — only that the construction shifts inferential behaviour relative to a matched
control, in the direction the published semantics predicts.*

## Spend (config/budget.md) — pre-flight estimate (Condition I8)

831 calls (277/model × 3: paraphrase 207 + nli 414 + agreement 138 + tier0 72). Pre-flight from v3's
**measured billed** rate: v3 ran **624 calls for $0.0910 billed** = **$0.0001458 per call** (billed
`usage.cost`, the ~4.5× rate-card undercount already absorbed). At the same per-call shape and rate,
**831 × $0.0001458 ≈ $0.121 billed** (point estimate); with the one verbatim retry per unparseable
response and variance, **expected ≈ $0.12–0.20 billed**. This lands **well under $1** and **well under
the $5.00/day UTC budget cap** ([`config/budget.md`](../../../config/budget.md)); it is **not**
flaggable as a >$1 run at this geometry. Single-run **ABORT_USD = $0.50** flag coded in `probe.py`,
well under the day cap. Actual billed `usage.cost` recorded in `raw/cost-log.txt` and the run record
**after** the later, post-critic run; **calls with missing `usage.cost` are counted and logged**,
never silently discarded.

## Named-null fallback to Option B (Condition N6, binding)

If — at design or fresh-pre-run-critic time — no distributive-default control can be built that
satisfies Conditions N1 (a credible off-ceiling baseline) and N2 (a matched lexical-cue control that
makes the double contrast interpretable), **the design must not run.** The disciplined outcome is to
record the AANN inferential half as **terminally untestable-at-paraphrase-instrument**, and redirect
inferential effort to **Option B**: the **cancel-direction / conative route**
([`result/conative-minimal-pair-divergence-v1`](../../../wiki/findings/results/conative-minimal-pair-divergence-v1.md)
shows that route works). The same redirect is the verdict-map outcome if the run proceeds but
**HEADROOM-FAIL** fires post-hoc.

DRAFT written 2026-06-13, before any model call. To freeze: the orchestrator commits this as
`PREREG.md` **only after** the **fresh independent pre-run critic's GO** (this draft retained for the
diff trail). A **NO-GO on N1/N2 buildability redirects to Option B, not to a run.**
