# Run: AANN agreement-reflex generalization v5 — 2026-06-14

**STATUS: RAN 2026-06-14 (sixth session) → REFLEX-GENERALIZES-TO-PANEL (bounded).** A fresh independent
pre-run critic GO'd the frozen design + `PREREG.md` + `stimuli.json` + `analyze.py` (0 BLOCKERs); the
probe ran (246 calls, **$0.0320 billed**, 0 missing in every arm); an independent post-run verifier
recomputed every number from raw (**0 mismatches**, no bug). Verdict: **gpt-5.4-mini REPLICATES**
(+0.43), **claude-sonnet-4.6 GENERALIZES-TO-PANEL** off the ceiling (+0.33, temporal-subset-driven,
one item above the bar), **gemini-3.5-flash CEILING-UNINFORMATIVE** (control was-rate 0.867). A
form/agreement-rung generalization, **not** an inference upgrade; `anchor: internal-contrast-only`.
Result page: [`result/aann-agreement-reflex-v5`](../../../wiki/findings/results/aann-agreement-reflex-v5.md).
Raw data in `raw/`; computed numbers in `results.json`; the frozen rules in `PREREG.md`
(`PREREG-draft.md` retained for the diff trail).

## What v5 is

NEXT.md backlog 2(a): **does gpt-5.4-mini's singular-agreement reflex (+0.74 v3 / +0.65 v4) generalize
across the panel and to held-out items?** *(reuses the v2 form-instrument family; no new decision.)*

The reflex: in the AANN frame (*A beautiful three days ___ what we needed*) gpt-5.4-mini picks singular
*was*; in the bare-plural control (*Three beautiful days ___ …*) it picks plural *were* — an agreement
**shift** of **+0.74 (v3) / +0.65 (v4)**. claude-sonnet-4.6 and gemini-3.5-flash sat at **ceiling**
(pick *was* for both frames), so the contrast was uninformative for them — **not** a failure. v5 tests:
(a) does gpt's reflex **replicate on fresh held-out items**, and (b) do claude/gemini show any
off-ceiling contrast on held-out items or **remain at ceiling**?

The **headline instrument is the v4 agreement arm, UNCHANGED** (same was/were forced choice, same
bare-plural control, same single-contrast indicator, same counterbalancing) — only the **items are
fresh held-out**. Result will be **`anchor: internal-contrast-only`** (within-model contrast; no
human-comparison claim; no in-repo resource anchors agreement behavior).

## File map

- `PREREG-draft.md` — the pre-registration draft (pinned integers: item counts per cell, the bar
  τ = +0.30, ceiling threshold 0.85, item floor 8, bootstrap seed 20260614 + 10,000 resamples,
  ABORT_USD = $0.25, the Tier-0 gate, the frozen verdict tree, scoring/parse rules; stimuli sha256
  placeholder, computed at freeze). Reviewed by a fresh pre-run critic; frozen as `PREREG.md` only on
  GO.
- `stimuli.json` — frozen, hand-authored (NO model calls). 30 held-out items (18 temporal / 12
  distance; all adjectives fresh, none from v3/v4), each with the `agreement` sub-object
  (`aann_frame`, `control_frame`, `agr_letter_was`) mirroring v4 exactly; 10 count-noun `diagnostic`
  items (descriptive-only); 12 `tier0` pairs (balanced).
- `probe.py` — three arms (`agreement` headline / `diagnostic` descriptive-only / `tier0`); per-slot
  max_tokens + gemini reasoning-minimal; one-retry parsing; billed-cost logging; ABORT_USD = $0.25;
  freeze + `analyze.py` guards (refuses to run without `PREREG.md`). **NOT executed.**
- `analyze.py` — the frozen analysis: agreement single shift + item-level bootstrap CI, the frozen
  verdict tree (REPLICATES / FAILS-TO-REPLICATE for gpt; CEILING-UNINFORMATIVE / GENERALIZES-TO-PANEL /
  NO-REFLEX for claude/gemini; overall REFLEX-IS-GPT-SPECIFIC-AND-REPLICATES /
  REFLEX-GENERALIZES-TO-PANEL / REFLEX-FAILS-TO-REPLICATE / INCONCLUSIVE, exhaustive with a final else),
  the descriptive-only count-noun diagnostic (fenced out of every verdict branch), the Tier-0 gate, and
  the item floor. `--selftest` runs 29 in-memory checks (no files, no calls), exercising every branch.

## Frozen geometry

- **Held-out items:** 30 (temporal 18 / distance 12; all adjectives fresh vs v3/v4).
- **Frames:** 2 per held-out item (AANN / bare-plural control) on the agreement arm; 1 per diagnostic
  item; 1 per Tier-0 pair.
- **Per model:** agreement 60 + diagnostic 10 + tier0 12 = **82**.
- **Total:** 82 × 3 = **246 calls.**

## Pre-flight budget ESTIMATE (NOT-RUN experiment)

246 calls. From v4's **measured billed** rate (831 calls / $0.1266 billed = **~$0.00015/call**):
**point estimate ≈ $0.037; expected ≈ $0.03–0.06 billed** with retries/variance. **Far under $1**;
**far under the $5.00/day budget cap.** ABORT_USD = $0.25 single-run flag. **Estimate only — the probe
has not run.**

## Execution order (once frozen, later session, after a FRESH pre-run-critic GO)

```
python3 analyze.py --selftest   # 29 checks, no calls — DONE
# fresh independent pre-run critic reviews design + PREREG-draft + stimuli
# orchestrator computes sha256(stimuli.json), records it, freezes PREREG.md only on GO — PENDING
python3 probe.py                # all arms, all models (refuses without PREREG.md + analyze.py)
python3 analyze.py              # reads raw/, writes results.json
# independent post-run verifier recomputes every number from raw before the result page
```

## Gate check (no new decision)

v5 stays inside the ratified agreement instrument class (Condition 3 of
[`decisions/resolved/aann-inferential-operationalization`](../../../wiki/decisions/resolved/aann-inferential-operationalization.md)):
it re-runs the load-bearing agreement discriminator unchanged on fresh held-out items. No new
operationalization, no `wiki/decisions/open/` entry, anchor (`internal-contrast-only`) already
ratified. The freeze + fresh-pre-run-critic gate still binds as a materials/PREREG review. See the
design's **§8 Gate check** for the full argument.
