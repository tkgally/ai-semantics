# Run: AANN inferential v3 — 2026-06-13

**STATUS: DESIGNED / FROZEN, NOT RUN.** Materials are built, frozen, and runnable-later;
**NO model API calls have been made** (this is a $0 design-and-build unit). The run awaits an
independent **pre-run critic**; `probe.py` refuses to run until `PREREG-draft.md` is reviewed
and committed as `PREREG.md` (and refuses to run if `analyze.py` is absent).

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
- `stimuli.json` — 32 base items (temporal 13 / distance 10 / object 9), each with AANN +
  control + U/D paraphrases (+ counterbalance + overlap counts) + NLI hypotheses + was/were
  pair + local-fluency direction + expert-stipulated key + item-level dispute flags; + 24
  Tier-0 pairs. 11 under-pressure items; 6 disputed-key flags.
- `probe.py` — four arms (paraphrase 192 / nli 384 / agreement 192 / tier0 72 calls);
  per-slot max_tokens + gemini reasoning-minimal; one-retry parsing; billed-cost logging;
  ABORT_USD = $0.50; freeze + `analyze.py` guards (refuses to run without `PREREG.md`).
- `analyze.py` — the frozen pre-registered analysis: AANN-vs-control shifts per arm,
  agreement-discriminator-weighted headline gating, |FC − NLI| per-model statistic, Tier-0
  gate, disputed-coding + under-pressure sensitivity, the convergence/verdict map.
  `--selftest` runs 29 in-memory checks (no files, no calls).

## Pre-flight budget estimate

744 calls. From v2b **measured billed** single-token-arm rates (so the ~4.5× rate-card
undercount is already absorbed): **point estimate ≈ $0.13; expected ≈ $0.13–0.25 billed**
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
