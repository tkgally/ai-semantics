# PREREG-draft — AANN inferential v3 (paraphrase-FC primary + NLI convergent + agreement discriminator)

**STATUS: DRAFT, written 2026-06-13 BEFORE any model call.** Named `-draft` so the
orchestrator's independent **pre-run critic** can review it before it is frozen as
`PREREG.md`. `probe.py` refuses to run while only the draft exists (and refuses to run
if `analyze.py` is absent — the analysis code is part of the freeze). **No v3 model call
may be made until** (a) the governing decision is ratified (DONE: 2026-06-13 autonomous
adversarial review) **and** (b) this draft passes the pre-run critic and is committed as
`PREREG.md`. Design-writing is not probe-running; building these materials makes no calls.

**Design:** [`experiments/designs/aann-construction-v3-inferential.md`](../../designs/aann-construction-v3-inferential.md).
**Governing decision (the spec):** [`decisions/resolved/aann-inferential-operationalization`](../../../wiki/decisions/resolved/aann-inferential-operationalization.md)
— ADOPT DEFAULT WITH CONDITIONS, **eight binding pre-run conditions**, the v3 result fixed
at **`anchor: internal-contrast-only`** scored against an explicitly **expert-stipulated**
literature key. This run tests the **inferential half** of
[`conjecture/aann-construction`](../../../wiki/findings/conjectures/aann-construction.md)
(v2 supported only the productive-gradient half).

## What is tested (the indicator, fixed pre-run)

The construction makes a model draw the **unification / whole-evaluation** inference — *a
beautiful three days* = one unified evaluated stretch, NOT three separately-evaluated days
— measured **only** as the **AANN-vs-control shift** (Condition 2), never the raw AANN rate,
never a human-comparison claim (Condition 5).

## Primary instrument (Condition 1 — fixed before any call)

**Arm A (paraphrase forced-choice) is PRIMARY.** Arm B (entailment NLI) is the convergent
robustness arm. The **agreement (was/were) sub-probe** is the **load-bearing discriminator**
(Condition 3), reported separately and weighted above the paraphrase arm. No instrument is
reselected after seeing outputs.

## Arms (four; all required; 624 calls = 208/model × 3)

*(Geometry after the 2026-06-13 object-class drop: 23 base items, temporal 13 / distance 10.)*

| Arm | Items × models | Calls | Bearing |
|---|---|---|---|
| `paraphrase` | 46 (23×{AANN,control}) × 3 | 138 | PRIMARY: U/D forced choice; indicator = unification-choice shift |
| `nli` | 92 (23×2 hyp×{AANN,control}) × 3 | 276 | CONVERGENT: affirm-rate shift (unification + whole-eval) |
| `agreement` | 46 (23×{AANN,control}) × 3 | 138 | DISCRIMINATOR (load-bearing): singular-agreement shift |
| `tier0` | 24 pairs × 3 | 72 | gate-bearing manipulation check, per model |

An absent or partial file for **any** arm (e.g. after a budget abort) makes the run
**INCOMPLETE**: no substantive verdict is emitted.

## Frozen inputs (committed before the run; built by `prep.py`, no model calls)

- `stimuli.json` — seed 20260613, **23 hand-authored base items** spanning two of Mahowald's
  measure-noun classes (temporal 13, distance 10; the object/mass class was dropped in the
  2026-06-13 repair — see README). Each item carries: AANN sentence + lexically-matched
  non-AANN control; U/D paraphrase pair with **seeded A/B counterbalance**
  (`fc_letter_unification`); per-item **lexical-overlap counts** (Condition 2 — all 23 items
  have **equal** U/D premise overlap, parity asserted in `prep.py`, its scope documented);
  NLI unification + whole-evaluation hypotheses (+ distributive foil); was/were agreement pair
  with seeded counterbalance (`agr_letter_was`); **per-item local-fluency direction**
  (Condition 4); the **expert-stipulated** unification key (Condition 5/6); item-level
  **`key_disputed`** flag (1 item — the yards inventory-edge item; the object items that
  carried the other flags are gone). The 24 Tier-0 pairs (6 base AANN frames — all temporal —
  × the 4 Mahowald degenerate variants `reverse_mods`/`no_mod`/`no_plural`/`no_a`, AANN
  position counterbalanced) are built mechanically.
  - **Under-pressure subset (Condition 4):** 10 items where the **distributive** paraphrase
    is the locally-fluent continuation; analysed separately.
  - **Adjectives are evaluatively-loaded** (the construction's semantics is partly
    evaluative); items where world-knowledge **alone** forces unification were excluded at
    authoring.
- **Expert-stipulated key (Condition 5/6), verbatim in `stimuli.json`:** the unification
  reading is the AANN-licensed answer per the design author's coding of the published AANN
  semantics (Solt 2007 unit-coercion; Dalrymple & King 2019; Bylinina & Nouwen 2018 — named
  as the analyses the stipulation rests on, NOT quoted; they are not in-repo). A scoring key,
  **not** a behavioral-human anchor.
- `analyze.py` **exists at freeze** with the thresholds + headline-gating + convergence rule
  baked in (selftested: 29 checks); `probe.py` refuses to run without it. The post-run
  verifier recomputes from raw with independent code.

## Frozen instrument (per-model settings)

Temperature 0; max_tokens 64 (A `claude-sonnet-4.6`, B `gpt-5.4-mini`) / 512
(C `gemini-3.5-flash`, `reasoning: {"effort": "minimal"}`), per `config/models.md`.
Counterbalancing lives in the frozen stimuli; the probe sends the counterbalanced letter and
`analyze.py` maps the chosen **letter back to content** (unification vs distributive; was vs
were; AANN vs ill-formed) so position bias is blocked at the stimulus level.

**Parsing.** Paraphrase/agreement/Tier-0: full-string A/B, else the LAST standalone A/B token
(v2b last-token convention). NLI: full-string YES/NO, else the LAST standalone YES/NO token.
One verbatim retry per unparseable response, then missing.

**Missingness (per arm):** >10% = mandatory caveat; >25% = instrument failure for that arm.
Any required arm absent/partial = **INCOMPLETE**.

## Frozen thresholds and statistics (per model) — baked in `analyze.py`, no post-hoc tuning

**Shift = mean(AANN indicator) − mean(control indicator)**, paired per item, over items
present in both conditions; bootstrap **95% CI, 10,000 resamples over items, seed 20260613**.

- **Shift threshold τ = +0.20, INCLUSIVE** (shift ≥ +0.20 passes). A **"positive"** shift
  additionally needs **CI lower bound > 0 (STRICT)**.
- **Tier-0 GATE:** pass = **≥ 20/24 AANN-preferred** (inclusive); >25% missing = instrument
  failure. **Pre-declared failure consequence (Condition 7):** a model failing Tier-0 has its
  inferential numbers reported **descriptively only** and is **excluded** from the ≥2-of-3
  count; fewer than 2 Tier-0 passers ⇒ **INSTRUMENT FAILURE** (no substantive verdict).
- **Named disagreement statistic (Condition 7):** **|FC shift − NLI shift|** per model, fed
  to [`open-question/instrument-sensitivity-constructional-inference`](../../../wiki/findings/open-questions/instrument-sensitivity-constructional-inference.md),
  **never averaged away**. Flag (mandatory per-model instrument-fragility caveat) if
  ≥ 0.30 (inclusive).
- **Disputed-coding sensitivity (Condition 6):** the paraphrase-arm positivity is recomputed
  excluding the 1 item-level `key_disputed` item; if positivity changes, a mandatory caveat
  attaches.

## Frozen verdict map (per model, then stratum) — pre-declared convergence rule (Condition 7)

Per model (gated on Tier-0 at the stratum step):

- **CONVERGENT-POSITIVE:** Arm A shift positive **AND** Arm B shift positive **AND**
  agreement shift positive. Headline: "the construction shifts inferential behaviour,
  including the grammaticalized singular reflex, in the predicted direction."
- **PARAPHRASE-ONLY (Condition 3 headline gate):** Arm A positive but the **agreement** shift
  null. Headline: **"shift in paraphrase selection WITHOUT the grammaticalized reflex"** —
  **not** "draws the unification inference."
- **PARAPHRASE-PLUS-REFLEX-NO-NLI:** A + agreement positive but NLI not — not full
  convergence; flagged for the disagreement statistic.
- **NULL:** Arm A not positive.

**Stratum verdict (over Tier-0-passing models only):**

- **SUPPORTED (inferential half):** ≥ 2 CONVERGENT-POSITIVE.
- **PARTIAL (paraphrase/constructional shift without full convergence):** ≥ 2 reach
  paraphrase positivity (PARAPHRASE-ONLY / PLUS-REFLEX / CONVERGENT) but < 2 CONVERGENT.
- **NULL:** < 2 reach even paraphrase positivity — written as a first-class null.
- **INSTRUMENT FAILURE:** < 2 Tier-0 passers.

Every outcome, including the null, is a first-class result on the eventual
`wiki/findings/results/aann-inferential-v3.md` page. **No threshold is set or retuned after
any pilot/dry-run output (Condition 8).**

## Anchor discipline (Condition 5)

The result will carry **`anchor: internal-contrast-only`** (within-model AANN-vs-control
shift; **no human-comparison claim**), ratified for the v3 result by the governing decision's
adoption. Mahowald linked **only** as stimulus provenance / v2 gradient anchor. The literature
key is **expert-stipulated**, labelled as such everywhere. The result page carries the
**chief-cost statement verbatim:** *the v3 can never say "models draw the inference the way
humans do" — only that the construction shifts inferential behaviour relative to a matched
control, in the direction the published semantics predicts.*

## Spend (config/budget.md) — pre-flight estimate (Condition 8)

624 calls (208/model × 3: paraphrase 138 + nli 276 + agreement 138 + tier0 72). Pre-flight
from v2b's **measured billed** single-token-arm per-call rates (A ≈ $0.00033, B ≈ $0.00008,
C ≈ $0.00012): per-model ≈ $0.069 (A) + $0.017 (B) + $0.025 (C) → **point estimate ≈ $0.11**
across all three models; with the one verbatim retry and variance, **expected ≈ $0.11–0.20
billed**. These are *billed* v2b rates, so the known ~4.5× rate-card undercount is **already
absorbed**, not added on top. This lands **well under $1** at this geometry; **if a later
geometry change could push it over $1, that must be flagged** (it cannot here). Single-run
**ABORT_USD = $0.50** flag coded in `probe.py` (well under the $2.50 single-run flag and the
$5.00/day budget). Actual billed `usage.cost` recorded in `raw/cost-log.txt` and the run
record; **calls with missing `usage.cost` are counted and logged**, never silently discarded.

## Named null fallback (Condition 8)

If the pre-run critic judges that neither arm can be given a defensible internal-contrast
validity argument at this tier, the **ratified fallback is the charter-preferred null**: leave
the inferential half an open question with the governing decision page and the v3 design as its
record, rather than run an uninterpretable probe.

DRAFT written 2026-06-13, before any model call. To freeze: the orchestrator commits this as
`PREREG.md` after the independent pre-run critic's GO (this draft retained for the diff trail).
