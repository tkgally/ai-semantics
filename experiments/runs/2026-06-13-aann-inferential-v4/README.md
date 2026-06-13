# Run: AANN inferential v4 — 2026-06-13

**STATUS: NOT RUN — pre-run critic pending.** The materials (`prep.py` → `stimuli.json`,
`analyze.py`, `probe.py`, `PREREG-draft.md`) are built and self-tested with **zero model
calls**. The v4 probe may run **only after** a **fresh independent pre-run critic** (not this
design's author/orchestrator) reviews the frozen design + `PREREG.md` + `stimuli.json` and
returns **GO**. A **NO-GO on N1/N2 buildability triggers the Option-B fallback (cancel-direction
/ conative route), not a run.** `probe.py` refuses to run until `PREREG.md` (and `analyze.py`)
are present. There is **no `raw/` with model data** — none exists.

## What v4 is

The second attempt at the **inferential half** of
[`conjecture/aann-construction`](../../../wiki/findings/conjectures/aann-construction.md) — does the
AANN construction (*a beautiful three days*) make a model **draw the unification / whole-evaluation
inference** (one unified evaluated stretch, NOT three separately-evaluated days), measured **only**
as a within-model contrast, never a raw AANN rate, never a human-comparison claim?

The indicator is now a **double contrast Δ²** (not v3's single shift); the result will be
**`anchor: internal-contrast-only`** (within-model contrast; **no human-comparison claim**).

## Why v4 (the v3 ceiling cause it removes)

v3 ([`result/aann-inferential-v3`](../../../wiki/findings/results/aann-inferential-v3.md)) returned a
**ceiling-bounded NULL**: no model shifted the unification-vs-distributive reading relative to the
**bare-plural** control *three beautiful days*, **because the models already read that bare plural as
a unified evaluated stretch nearly every time.** v3's control raw rates (quoted verbatim — the cause
v4 removes; **no new numbers invented**):

- paraphrase control unification rate: **0.78 / 0.96 / 1.00** (claude / gpt / gemini);
- NLI control affirm rate: **0.87 / 0.83 / 1.00**.

The AANN-vs-control shift subtracts a baseline already at the unification ceiling, so there is no
headroom to detect the construction's contribution. (v3's one off-ceiling positive was the
**agreement** arm — gpt-5.4-mini +0.739, control *was*-rate 0.22 — which v4 keeps unchanged, with the
bare-plural control, per Condition N4.)

**v4's single structural change:** replace the ceiling-pinned bare-plural paraphrase/NLI control with
a **distributive-default control (DDC)** whose baseline reading is genuinely distributive, and add a
**lexical-cue control (LCC)** arm that proves any measured shift is the **construction's**, not the
imported itemizing cue's.

## The frame design (three premise frames per item)

| Frame | What it is | Example (item: *beautiful three days in Rome*) |
|---|---|---|
| **AANN** | the construction (verbatim v3) | *We spent a beautiful three days in Rome.* |
| **DDC** | distributive-default control (N1 headroom frame); adjective predicated per-unit, baseline genuinely distributive | *On each of the three days in Rome, it was beautiful.* |
| **LCC** | lexical-cue control (N2 construction-isolating arm); same itemizing cue, adjective attributive, **no AANN** | *On each of the three beautiful days in Rome, we relaxed.* |
| (agreement control) | **bare plural** (N4 — agreement arm only, NOT the DDC) | *Three beautiful days ___ what we needed.* |

The two paraphrase options are presented identically across all three frames:
- **U (unification):** *The three days formed one continuous stretch, beautiful as a whole.*
- **D (distributive):** *Each of the three days was individually beautiful.*

## The N1 / N2 logic (what makes the double contrast interpretable)

- **N1 — headroom precondition.** The DDC's whole purpose is to read **distributive** at baseline, so
  the AANN has somewhere to shift the reading *to*. Read **pre-headline, per model**:
  P(unification | DDC) must be off-ceiling — **PASS ≤ 0.30; MARGINAL ≤ 0.50; HEADROOM-FAIL > 0.50**.
  If fewer than 2 of 3 models clear, the design **did not remove the v3 cause** → **OPTION-B NAMED
  NULL**. This is the pre-registered proof that the ceiling cause is actually gone (not assumed).
- **N2 — lexical-cue control.** Because the DDC imports an itemizing cue ("on each of the … days"), a
  raw AANN-vs-DDC shift could be a **lexical-cue artifact**, not evidence the AANN *licenses*
  unification. The LCC carries the **same** cue **without** the AANN, so the headline is the **double
  contrast**:
  - AANN shift = P(uni|AANN) − P(uni|DDC)
  - lexical-cue shift = P(uni|LCC) − P(uni|DDC)
  - **Δ² = AANN shift − lexical-cue shift = P(uni|AANN) − P(uni|LCC)** (the construction's net
    contribution). If the cue alone moves the reading as much as the AANN does, Δ² → 0 and the
    paraphrase arm is a **LEXICAL-CUE ARTIFACT** — disqualified from the headline. This is the
    structural bias *against a free positive* the ratification demands.

## Files

- `PREREG-draft.md` — the pre-registration draft (the three frames, the headroom precondition + its
  pre-registered thresholds, Δ² + τ + bootstrap, the full verdict map, the named-null/Option-B
  fallback, anchor + verbatim chief-cost, expert-stipulated key, frozen counts, pre-flight budget —
  all stated BEFORE any data). Named `-draft` for the fresh pre-run critic; the orchestrator freezes
  it as `PREREG.md` only on GO.
- `prep.py` — hand-authored stimulus build (NO model calls); authors the three frames per item;
  asserts paraphrase-option lexical-overlap parity (N3), counterbalance balance, three-frame presence,
  and that the LCC carries the DDC's itemizing cue (N2). → `stimuli.json`.
- `stimuli.json` — 23 base items (temporal 13 / distance 10; object class dropped), each with the
  three premise frames + bare-plural control + U/D paraphrases (+ counterbalance + overlap counts) +
  `control_lexical_delta` + NLI hypotheses + was/were pair + local-fluency direction +
  expert-stipulated key + item-level dispute flag; + 24 Tier-0 pairs. 10 under-pressure items; 1
  disputed-key flag.
- `probe.py` — four arms (paraphrase 207 / nli 414 / agreement 138 / tier0 72 calls); paraphrase + NLI
  iterate the three frames, agreement + tier0 keep two conditions; per-slot max_tokens + gemini
  reasoning-minimal; one-retry parsing; billed-cost logging; ABORT_USD = $0.50; freeze + `analyze.py`
  guards (refuses to run without `PREREG.md`). **NOT executed by this session.**
- `analyze.py` — the frozen pre-registered analysis: the headroom-precondition gate (pre-headline),
  the double-contrast Δ² per arm with item-level bootstrap CI, the agreement-discriminator-weighted
  headline gating, |FC Δ² − NLI Δ²| per-model statistic, Tier-0 gate, disputed-coding + under-pressure
  sensitivity, and the full verdict map (incl. LEXICAL-CUE ARTIFACT and HEADROOM-FAIL → Option-B).
  `--selftest` runs 38 in-memory checks (no files, no calls), including a clean CONVERGENT-POSITIVE
  scenario and a HEADROOM-FAIL scenario.

## Frozen geometry

- **Base items:** 23 (temporal 13 / distance 10; object/mass class stays dropped).
- **Premise frames:** 3 per item (AANN / DDC / LCC) on paraphrase + NLI; 2 conditions on agreement
  (AANN / bare-plural control) and Tier-0 (AANN / ill-formed).
- **Per model:** paraphrase 69 + nli 138 + agreement 46 + tier0 24 = **277**.
- **Total:** 277 × 3 = **831 calls** (vs v3's 624; the added LCC frame raises paraphrase + NLI by ~33%).

## Pre-flight budget estimate

831 calls. From v3's **measured billed** rate (624 calls / $0.0910 billed = **$0.0001458/call**, the
~4.5× rate-card undercount already absorbed): **point estimate ≈ $0.12; expected ≈ $0.12–0.20 billed**
with retries/variance. **Well under $1** at this geometry; **well under the $5.00/day budget cap.**
ABORT_USD = $0.50 single-run flag.

## Condition checklist

The **six new** binding conditions (`aann-inferential-default-coincidence`) + the **eight inherited**
conditions (`aann-inferential-operationalization`) → where each is satisfied are mapped in the
design's **§0 condition tables**
([`aann-construction-v4-inferential.md`](../../designs/aann-construction-v4-inferential.md)) and
re-stated in `PREREG-draft.md`. In brief: N1 headroom precondition (analyze.py pre-headline gate); N2
lexical-cue control arm + double contrast; N3 paraphrase-option parity unchanged + `control_lexical_delta`;
N4 agreement discriminator stays bare-plural-controlled; N5 internal-contrast-only + expert-stipulated
key + chief-cost verbatim; N6 named-null / Option-B fallback. Inherited: I1 primary lock A; I2 (amended)
double-contrast indicator; I3 agreement headline-gating; I4 under-pressure subset; I5 anchor; I6
disputed-coding sensitivity; I7 |FC−NLI| + Tier-0 gate; I8 frozen thresholds + budget + named null.

## Execution order (once frozen, later session, after a FRESH pre-run-critic GO)

```
python3 prep.py                 # writes stimuli.json (no model calls) — DONE
python3 analyze.py --selftest   # 38 checks, no calls — DONE
# fresh independent pre-run critic reviews design + PREREG-draft + stimuli
# orchestrator freezes PREREG.md only after the critic's GO  — PENDING
python3 probe.py                # all arms, all models (refuses without PREREG.md + analyze.py)
python3 analyze.py              # reads raw/, writes results.json
# independent post-run verifier recomputes every number from raw before the result page
```

## Run results

**NOT RUN — placeholder.** This section will be filled by a later, post-critic session after the probe
runs and an independent post-run verifier recomputes every number from raw. No model calls have been
made; no results exist.
