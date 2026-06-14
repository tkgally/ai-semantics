# 2026-06-14 — AANN inferential v6 (powered panel replication of v4)

**Verdict: PARTIAL — replicates [v4](../2026-06-13-aann-inferential-v4/) cell-for-cell
on a fresh, larger, held-out item set.** Result page:
[`wiki/findings/results/aann-inferential-v6.md`](../../../wiki/findings/results/aann-inferential-v6.md).

## What this is

A clean replication of the AANN inferential v4 PARTIAL result, with the **single
change** being the item set: **40 fresh hand-authored base items** (temporal 20 /
distance 20, vs v4's 23), whose **40 adjectives are all held-out** (disjoint from v4's
21 and the v5-reflex probe's 30, asserted in `prep.py`). Instrument, parsing, four
arms, thresholds, headroom gate, verdict map, and analysis code are **identical to v4**
(`analyze.py` byte-identical save run name / design path / bootstrap seed 20260614 and
N-robust `--selftest` fractions; `probe.py` logic identical, ABORT 0.50→0.75). **No new
decision** — runs under the already-ratified AANN inferential instruments; result
`anchor: internal-contrast-only`.

## Result

Both pre-registered questions answered **yes**:
1. **Panel-wide paraphrase shift holds powered:** all 3 models paraphrase Δ² positive
   (+0.875 / +0.575 / +0.90, CIs clear of 0; headroom PASS all, DDC 0 / 0.225 / 0).
2. **gpt-5.4-mini cross-instrument convergence replicates:** CONVERGENT-POSITIVE again
   (paraphrase + NLI Δ² +0.225 + agreement +0.60); claude + gemini PARAPHRASE-ONLY
   (NLI null, agreement flat at ceiling). Tier-0 24/24 all.

Overall **PARTIAL** (3 paraphrase-positive ≥2, but only 1 CONVERGENT-POSITIVE <2).

## Discipline

- **Fresh pre-run critic: GO** (no BLOCKER/SHOULD-FIX; all 14 binding conditions PASS;
  replication fidelity + anti-cheat verified; held-out adjectives verified; selftest 38
  checks). NIT-1 (stale seed docstring) fixed pre-freeze.
- **Independent post-run verifier: VERIFIED** (recomputed every headline number from
  raw with independent code — 0 mismatches; confirmed the v4 NLI-aggregation bug class
  is absent here).
- **Cost: $0.2138 billed** (`usage.cost`-summed; 0 missing-cost calls; 0 missing
  responses in every arm). Day total 2026-06-14 after this run ≈ $1.19 of $5.00.

## Files

- `prep.py` — stimulus authoring (40 fresh items; held-out + three-frame + parity
  asserts). No model calls. → `stimuli.json` (seed 20260614).
- `probe.py` — panel calls (logic identical to v4); refuses to run without frozen
  `PREREG.md` + `analyze.py`.
- `analyze.py` — frozen analysis (identical to v4 save run name/path/seed); `--selftest`
  38 checks.
- `PREREG.md` (frozen after critic GO) / `PREREG-draft.md` (pre-freeze diff trail).
- `raw/` — per-(model,arm) JSON + `cost-log.txt` + `run-log.txt`.
- `results.json` — `analyze.py` output.
