# Run: AANN inferential v3 — 2026-06-13

**STATUS: REPAIRED → re-frozen → fresh pre-run critic → RUN (see results below).** The prior
session built and froze the materials; its independent pre-run critic returned **NO-GO** over a
real object-class stimulus defect. This (later) session applied the pre-authorized repair, had a
**fresh** independent pre-run critic review the repaired materials, and — on its GO — froze
`PREREG.md` and ran the probe. The run results and post-run verification are recorded at the
bottom of this file.

## Repair applied this session (2026-06-13, a later session than the NO-GO)

Per the pre-authorized repair list (carried in the prior handoff), and because no data existed
(so this is not anti-retuning — no result could have motivated it):

- **B1 + B2 — object/mass class DROPPED.** The "formed one continuous stretch / were a single
  continuous stretch" unification paraphrase is anomalous for mass/area nouns (pounds, acres,
  kilos are not a *stretch*), and the dollar items dropped their plural measure noun and were not
  well-formed AANN of the target shape. Rather than re-author 9 bespoke object paraphrases (the
  exact place the prior critic found the defect, and a fresh-defect risk), the object class was
  **dropped entirely**. Temporal (13) + distance (10) = **23 items** remain; for these *genuine
  extents* the "continuous stretch" unification reading is the natural one, so dropping object
  **sharpens** the construct test rather than degrading it. The result is **scoped to temporal +
  distance measure nouns only** (stated on the result page).
- **B3 — parser fixed.** `parse_ab` / `parse_yesno` now strip markdown-bold `*`, quotes, and
  backticks (full-string fast path and last-token scan), so gemini's `**A**` / `**YES**` parse;
  verified on `**A**`→A, `"YES"`→YES, `**NO**`→NO, `maybe`→None.
- **S1 — `noun_sg("yards")` → "yard"** (was "yards"); the foil now reads "Each **yard**
  individually was lonely."
- **S2 — parity scope documented.** The lexical-overlap parity metric deliberately measures
  *premise-content* overlap (adj/num/noun) and excludes the unification/distributive contrast
  vocabulary (which is the manipulation, not overlap); documented in `prep.py`. The metric is a
  construction-time guarantee, not a discriminating filter.
- **S4 — class balance + under-pressure re-checked.** 23 items (temporal 13 / distance 10); 10
  under-pressure (distributive locally-fluent) items survive (≥6 required); 1 disputed-key item
  (the yards inventory-edge item — the object items carried the other flags and are gone). The
  29-check `analyze.py --selftest` passes; counterbalance + parity assertions in `prep.py` pass.

**Budget note:** 624 calls (208/model × 3) ≈ **$0.11 point estimate** (from v2b's measured
$0.0793/432-call rate of the identical single-token shape); cannot plausibly exceed $1. Budget was
never the constraint — stimulus validity was.

## What it tests

Tests the **inferential half** of
[`conjecture/aann-construction`](../../../wiki/findings/conjectures/aann-construction.md) —
does the construction make a model **draw the unification / whole-evaluation inference**
(*a beautiful three days* = one unified evaluated stretch, NOT three separately-evaluated
days) — left untested by v2, which supported only the productive-gradient half
([`result/aann-behavioral-gradient-v2`](../../../wiki/findings/results/aann-behavioral-gradient-v2.md)).

The indicator is the **AANN-vs-control SHIFT**, never the raw AANN rate; the result will be
**`anchor: internal-contrast-only`** (within-model contrast; **no human-comparison claim**).

## Design / governance

- Design: [`experiments/designs/aann-construction-v3-inferential.md`](../../designs/aann-construction-v3-inferential.md)
  (frozen; carries the 8-condition → design-location checklist in its §0).
- Governing decision (the spec): [`decisions/resolved/aann-inferential-operationalization`](../../../wiki/decisions/resolved/aann-inferential-operationalization.md)
  — ADOPT DEFAULT WITH CONDITIONS, **eight binding conditions**, ratified 2026-06-13
  (autonomous adversarial review); the `internal-contrast-only` terminal state is ratified for
  the v3 result by that adoption.

## Instrument (A+B package, A primary)

- **Arm A — paraphrase forced-choice (PRIMARY):** unification vs distributive paraphrase,
  AANN premise vs lexically-matched control; indicator = unification-choice shift.
- **Arm B — entailment NLI (convergent):** affirm-rate shift on unification + whole-evaluation
  hypotheses.
- **Agreement (was/were) sub-probe — LOAD-BEARING DISCRIMINATOR:** singular-agreement shift;
  reported separately and weighted above the paraphrase arm; gates the headline wording.
- **Tier-0** manipulation check (AANN well-formed vs Mahowald degenerate variants), gate
  ≥ 20/24 per model, pre-declared failure consequence.

## Files

- `PREREG-draft.md` — the pre-registration draft (frozen thresholds, convergence rule, Tier-0
  gate + failure consequence, pre-flight budget, headline decision rule — all stated BEFORE any
  data). Named `-draft` for the pre-run critic; the orchestrator freezes it as `PREREG.md`.
- `prep.py` — hand-authored stimulus build (NO model calls); asserts lexical-overlap parity
  (Condition 2) and counterbalance balance. → `stimuli.json`.
- `stimuli.json` — 23 base items (temporal 13 / distance 10; object class dropped in repair),
  each with AANN + control + U/D paraphrases (+ counterbalance + overlap counts) + NLI
  hypotheses + was/were pair + local-fluency direction + expert-stipulated key + item-level
  dispute flag; + 24 Tier-0 pairs. 10 under-pressure items; 1 disputed-key flag.
- `probe.py` — four arms (paraphrase 138 / nli 276 / agreement 138 / tier0 72 calls);
  per-slot max_tokens + gemini reasoning-minimal; one-retry parsing; billed-cost logging;
  ABORT_USD = $0.50; freeze + `analyze.py` guards (refuses to run without `PREREG.md`).
- `analyze.py` — the frozen pre-registered analysis: AANN-vs-control shifts per arm,
  agreement-discriminator-weighted headline gating, |FC − NLI| per-model statistic, Tier-0
  gate, disputed-coding + under-pressure sensitivity, the convergence/verdict map.
  `--selftest` runs 29 in-memory checks (no files, no calls).

## Pre-flight budget estimate

624 calls. From v2b **measured billed** single-token-arm rates (so the ~4.5× rate-card
undercount is already absorbed): **point estimate ≈ $0.11; expected ≈ $0.11–0.20 billed**
with retries/variance. **Well under $1** at this geometry; flag required only if a later
geometry change could exceed $1 (it cannot here). ABORT_USD = $0.50 single-run flag. Under the
$5.00/day budget.

## 8-condition checklist

The 8 binding conditions → where each is satisfied are mapped in the design's **§0 condition
table** ([`aann-construction-v3-inferential.md`](../../designs/aann-construction-v3-inferential.md)),
and re-stated in `PREREG-draft.md`. In brief: (1) primary lock A; (2) shift indicator + overlap
parity; (3) agreement discriminator headline-gating; (4) under-pressure subset; (5)
internal-contrast-only + expert-stipulated key + chief-cost statement; (6) disputed codings
flagged + sensitivity-tested; (7) |FC−NLI| named statistic + convergence rule + Tier-0 gate;
(8) frozen thresholds + pre-flight budget + named null fallback.

## Execution order (once frozen, later session)

```
python3 prep.py             # writes stimuli.json (no model calls) — DONE
# orchestrator freezes PREREG.md after the independent pre-run critic's GO
python3 analyze.py --selftest   # 29 checks, no calls
python3 probe.py            # all arms, all models (refuses without PREREG.md + analyze.py)
python3 analyze.py          # reads raw/, writes results.json
```
