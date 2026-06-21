# Modal-arm-widening probe (session 71, 2026-06-21)

**A focused follow-up to [`result/function-word-swap-run-v2`](../../../wiki/findings/results/function-word-swap-run-v2.md)
that fires essay revision trigger (a) of
[`essay/function-words-not-one-category`](../../../wiki/findings/essays/function-words-not-one-category.md).**

## The question

run-v2 confirmed [`conjecture/function-word-substitutability`](../../../wiki/findings/conjectures/function-word-substitutability.md)
3/3, but the per-arm breakdown showed the modal arm `will`→`would` (future→conditional) was
**near-null in all three models** (claude 0/20, gpt 0/20, gemini 3/20). The companion essay reads
this as "modal flavor is the kind of shift this [3-way NLI] instrument is insensitive to" — but
flags it as a **one-pair observation** and names the widened-modal-arm probe as the decisive test:

> **(a) A widened modal arm.** If a probe widens the modal arm beyond `will`→`would` … and the
> near-null generalizes, the essay's "modal flavor is the kind of shift this instrument is
> insensitive to" reading **strengthens** from a one-pair observation to a type-level fact. If
> instead some modal contrast flips strongly, the reading **narrows**: it was idiosyncratic to
> `will`→`would`, not modal flavor as such.

This probe widens the modal arm across **three modal flavors** and asks: does the modal null
generalize, or is it specific to future→conditional?

## Design (frozen)

Five arms, same instrument/matching/posture as run-v2 (3-way NLI entailment-flip;
internal-contrast-only):

**Modal sweep (the question):**

| arm | swap | flavor | hypothesis | predicted flip |
|-----|------|--------|------------|----------------|
| `will`→`would` (n=20, REUSE run-v2) | future → conditional | replication of the null | "is going to {verb}" | ENT→NEU |
| `shall`→`should` (n=18, NEW) | deontic obligation → advisory | strength drop, same flavor | "is required to {verb} the {obj}" | ENT→NEU |
| `must`→`might` (n=20, NEW) | deontic necessity → epistemic possibility | strength drop, flavor cross | "is required to {verb} the {obj}" | ENT→NEU |

**In-run positive controls (prove the NLI instrument flips on a real inferential change here):**

| arm | swap | predicted flip |
|-----|------|----------------|
| `some`→`every` (n=28, REUSE run-v2) | existential → universal | NEU→ENT |
| `because`→`although` (n=32, REUSE run-v2) | causal → concessive | ENT→CON |

Total **118 matched items**, 4 content semantic classes (adj/noun_person/noun_thing/verb — the
adj class comes from the reused `because` arm). The two NEW modal arms use an **"is required to"**
hypothesis so the swap is predicted to flip ENT→NEU: `shall`/`must` ≈ *required*; `should` (advisory)
and `might` (possibility) are **not** *required*, so a competent reader drops the entailment. The
content control swaps a frequency+length-matched content verb (predicted **not** to flip).

### Predicted-flip defensibility (the crux the pre-run critic checks)

- `shall`→`should`: "The bidder shall buy the lot" → "…is required to buy the lot" = **ENT**
  (legal/deontic *shall* = obligation). "The bidder **should** buy the lot" → "…is required to…"
  = **NEU** (advisory ≠ required).
- `must`→`might`: "The auditor must find the form" → "…is required to find the form" = **ENT**
  (deontic necessity = obligation). "The auditor **might** find the form" → "…is required to…" =
  **NEU** (epistemic possibility ≠ required). The swap crosses deontic→epistemic, but the
  necessity→possibility contrast is exactly the modal-**strength** dimension most likely to be
  truth-conditional — the sharpest test of whether these models read modal-encoded inference.

### Matching (build.py `verify_pair`) — UNCHANGED from run-v2

Each content swap matched to its MODAL pair within **|ΔLg10WF| ≤ 0.10** at both ends (SUBTLEX-US),
**signed Δlen == function Δlen** (per-pair), and **content gap ≥ function gap** so no frequency-only
or length-only reader can manufacture the asymmetry. `certify.py` → `certification.json`
`"ok": true`: max-positive freq-only and len-only shortcut-reader asymmetry **both 0.0**, monotone
pooled (func_gap−content_gap) = −0.0527 (content-favoring, conservative).

- `shall`→`should` rests on **one** content pair (`buy`→`give`): the gap-0.759 supply ceiling under
  faithful matching admits essentially one clean transitive pair — the same single-out-word
  thinness run-v2's `because`/`some`/`will` arms carried (`matching-report.json`
  `single_out_word_classes`). `must`→`might` carries three (`find`→`leave`, `call`→`leave`,
  `put`→`move`).

## Governance: no new decision owed

The instrument is ratified
([`decisions/resolved/function-word-anchor-design`](../../../wiki/decisions/resolved/function-word-anchor-design.md)),
the matching discipline is ratified and **unchanged**, the inventory-widening method (add function-word
pairs at the unchanged ±0.10 tolerance) is ratified
([`decisions/resolved/function-word-count-vs-matching`](../../../wiki/decisions/resolved/function-word-count-vs-matching.md)),
and the result is `internal-contrast-only` (no new human claim). This is **not** a re-test of the
conjecture (already `tested`): it is a per-arm characterization of modal behavior. The only relaxation
vs run-v2 is the count gate — `certify.py` uses a **per-arm power gate** (≥15 items/arm) in place of
the conjecture's ≥200-item confirm bar, because the statistical unit here is the per-arm flip rate,
not a pooled conjecture verdict. The ≥4-content-class span is kept (and passes). This relaxation is
surfaced here and in `PREREG.md` for the independent pre-run critic to rule on.

## Pre-flight budget

118 matched × 3 NLI calls × 3 models = 1,062 finding-bearing calls + 3 liveness. Single-digit NLI is
cheap (run-v2: 1,914 calls = $0.502). Estimate **~$0.28–0.40 billed**. `ABORT_USD` = $1.00 (probe.py).
UTC-2026-06-21 headroom at session start: $5.00 − $2.467 (s64+s69+s70) = **$2.533**. Record actual
billed `usage.cost` after.

## Files

`freqlib.py` · `build.py` · `frames.json` · `stimuli.json` (file sha + canonical sha in
`certification.json`/`PREREG.md`) · `certify.py` · `certification.json` · `matching-report.json` ·
`probe.py` · `analyze.py`. `raw/` holds per-model NLI outputs after the run.

## Pipeline

(1) `build.py` → `frames.json`+`stimuli.json`+`matching-report.json`; (2) `certify.py` until
`"ok": true`; (3) **independent fresh-agent pre-run critic** GO/NO-GO; (4) freeze `PREREG.md` (sha +
GO); (5) `probe.py liveness` then `probe.py full`; (6) `analyze.py` + **independent post-run
verifier**; (7) write the result page.
