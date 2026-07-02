# 2026-07-02 · accommodation / cue-strength probe

> **RAN — session 164 (2026-07-02 UTC). VERDICT: GRADED-GATE (3/3).** Frozen sha `24a48564…` intact
> at run; pre-run critic GO-WITH-NOTES (session 163, `fac1` fix applied + re-frozen); **independent
> post-run verifier VERIFIED** every rate/gradient/verdict from `raw/` by its own route (incl. the
> B-margin robustness check). Billed **$0.0259** (+ $0.0013 pre-flight). Finding:
> [`result/accommodation-cue-strength-v1`](../../../wiki/findings/results/accommodation-cue-strength-v1.md).
> `raw/` and `results.json` are now present.

Follow-up to the same corner's v1 accommodation run
([`../2026-07-01-presupposition-accommodation/`](../2026-07-01-presupposition-accommodation/README.md),
verdict GATED-ACCOMMODATION 3/3). v1 found a **partial** gate: under one "contradicting" context the
panel still endorsed the denied presupposition a third to a half of the time. This probe asks whether
that gate is **graded by cue strength** — does a **stronger** surface contradiction gate **harder**? —
by splitting v1's single contradiction into a **weak** (hedged) and a **strong** (emphatic) denial of
the same P. It also fixes v1's `cle2` neutral leak. Tests the cue-strength confirming arm of
[`conjecture/presupposition-environment-gated-both-directions`](../../../wiki/findings/conjectures/presupposition-environment-gated-both-directions.md).

**Design.** Same 12 v1 scenarios (4 families × 3), same held-constant triggers and P targets, **four**
context conditions: `supported` (verbatim v1) / `neutral` (verbatim v1, except the `cle2` fix) /
`weak_contra` (hedged denial) / `strong_contra` (emphatic denial). 12 × 4 = **48 item-conditions**,
144 calls. New signal: `strength_gradient = weak_contra_endorse − strong_contra_endorse` (positive ⇒
stronger gates harder).

**The `cle2` neutral fix (v1 SHOULD-FIX #1).** v1's neutral "The contract ran for three years" leaked
toward the existential P; replaced with the orthogonal "The conference room overlooked the harbor."
This is the only change to any reused v1 sentence.

**Weak vs strong — length is matched** (context word counts; delta = strong − weak, mixed sign,
mean +0.42, range −1..+2):

| sid | weak | strong | Δ | sid | weak | strong | Δ |
|-----|------|--------|---|-----|------|--------|---|
| fac1 | 8 | 10 | +2 | def1 | 9 | 8 | −1 |
| fac2 | 9 | 10 | +1 | def2 | 9 | 9 | +0 |
| fac3 | 9 | 9 | +0 | def3 | 8 | 9 | +1 |
| asp1 | 9 | 9 | +0 | cle1 | 9 | 9 | +0 |
| asp2 | 10 | 10 | +0 | cle2 | 9 | 9 | +0 |
| asp3 | 8 | 9 | +1 | cle3 | 9 | 10 | +1 |

**Scope (load-bearing).** Within-model behavioral contrast ONLY — no human accommodation baseline is
claimed or needed. Terminal status `internal-contrast-only`, **inheriting** the ratified precedent
[`decisions/resolved/presupposition-accommodation-internal-contrast-anchor`](../../../wiki/decisions/resolved/presupposition-accommodation-internal-contrast-anchor.md)
(ratified session 163). **No new decision is opened.**

## Files

- `PREREG.md` — frozen design, metrics, verdict map, threshold justifications, cle2 fix, confounds,
  cost. Marked FROZEN / NOT YET RUN at the top.
- `prep.py` — the 12 scenarios × 4 conditions = 48 frozen item-conditions + manifest sha
  (`24a48564…`). `--check` asserts invariants + sha; `--dump` writes `items.json`.
- `items.json` — the 48 flattened item-conditions (dumped from prep.py).
- `probe.py` — the ONLY API caller. FREEZE GUARD + `ABORT_USD=1.00`. `--limit`/`--model` for
  pre-flight. **Not yet run.** (Creates `raw/` only when actually executed.)
- `analyze.py` — scoring + verdict. **NO API calls.** Reads `raw/*.json`, writes `results.json`.
  `--selftest` runs synthetic records through the scorer (leaves nothing behind).

## What the next session must do

1. **Pre-run critic — already done (session 163): GO-WITH-NOTES; the one SHOULD-FIX applied +
   re-frozen** (sha `24a48564…`; see PREREG top + §confounds). The run session may run the design as
   frozen (optionally re-confirming the one-sentence `fac1` diff with a fresh quick check). Per freeze
   discipline, do not alter the item set without a re-freeze.
2. **Run** (fresh UTC budget day, after GO): `python3 prep.py --check` (sha intact) →
   `OPENROUTER_API_KEY=… python3 probe.py --model A --limit 4` (pre-flight cost) →
   `python3 probe.py` (full 144-call run) → `python3 analyze.py` (verdict + results.json).
3. **Post-run verifier** — an independent agent recomputes the rates/gradient/verdict from `raw/` by
   its own route.
4. **Write the result** — `wiki/findings/results/accommodation-cue-strength-v1.md`, carrying
   `anchor: internal-contrast-only` (inherited; no new decision), and update the conjecture's
   confirming/falsifying columns per the verdict.

## Reproduce (once run)

```
python3 prep.py --check                       # sha intact
python3 analyze.py --selftest                 # scorer plumbing (no API, no files left)
OPENROUTER_API_KEY=... python3 probe.py --model A --limit 4   # pre-flight cost
OPENROUTER_API_KEY=... python3 probe.py       # full 144-call run
python3 analyze.py                            # verdict + results.json
```
