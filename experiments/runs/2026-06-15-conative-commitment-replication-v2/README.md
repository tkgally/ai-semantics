# Run: 2026-06-15 — conative COMMITMENT-ONLY replication v2

**Design:** [`experiments/designs/conative-commitment-replication-v2.md`](../../designs/conative-commitment-replication-v2.md)
**Replicates:** the single positive effect of the v1 run
[`2026-06-15-conative-preference-commitment-v1`](../2026-06-15-conative-preference-commitment-v1/README.md)
— claude-sonnet-4.6's COMMITMENT-ONLY double contrast (Δ²_commit = +0.46, 95% CI [0.08, 0.79]).
**Ratified decision (no new one):** `decisions/resolved/fresh-construction-inferential-generalization`
(Option A — the conative).

## What this asks

Is claude's lone v1 effect — a commitment shift without a preference shift, the mirror of the AANN
dissociation, resting on one model / one item set / a wide CI — a **stable** single-model property
or **one-item-set noise**? Same instrument, thresholds, scoring, panel; only the verbs change (a
fresh, disjoint sample).

## Freeze

- `stimuli.json` — 40 items, seed 20260615, **sha256[:16] = `84e2e0d6afb4b5b6`**.
- `prep.py` — authoring + asserts (all PASS, incl. disjointness-from-v1); no API.
- `probe.py` — instrument code byte-for-byte from v1 (only the docstring differs; `diff` confirms);
  freeze guard requires a frozen `PREREG.md`.
- `analyze.py` — byte-for-byte from v1; `--selftest` re-passes (30 checks).
- `PREREG-draft.md` → `PREREG.md` after a fresh independent pre-run-critic GO.

## How to run (after PREREG freeze)

```
python3 prep.py                      # re-emits stimuli.json; sha must match 84e2e0d6afb4b5b6
OPENROUTER_API_KEY=... python3 probe.py     # 240 calls; writes raw/{A,B,C}-{paraphrase,nli}.json
python3 analyze.py                   # double contrast, bootstrap, headroom, verdict map -> results.json
```

## Result

> Filled after the run + independent post-run verification. Pre-flight spend ≈ $0.05 (expected
> $0.04–0.08 billed); `ABORT_USD = 0.50`. Day total 2026-06-15 before this run: $0.05.
