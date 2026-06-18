# PREREG — Option-C order-sensitive composition, THIRD-MODEL generality extension (gpt-5.4-mini)

**This is a generality re-run of an already-frozen, already-certified design on one additional,
in-panel model.** It adds **no** new design, threshold, stimulus, or indicator. It runs the
byte-identical frozen Option-C instrument on `openai/gpt-5.4-mini` (panel.B), the third panel model,
to test whether the order-sensitive **composition** verdict generalizes beyond `claude-sonnet-4.6`
(which RESPECTS-ORDER) or is a one-model property. The sibling run
[`../2026-06-18-relational-order-composition-c/`](../2026-06-18-relational-order-composition-c/) already
ran claude (RESPECTS-ORDER) + gemini (UNINTERPRETABLE).

## Frozen stimuli (byte-identical to the sibling run — NOT regenerated)

- `stimuli.json` sha256 (trailing-newline-stripped blob, as `probe.py` computes it) =
  **`89f078e3621f7fb8bbbfd59dcc87bd3e628253f7904c739c76f19e9576374cfc`** — identical to the sibling
  run's frozen sha.
- On-disk `sha256sum stimuli.json` =
  `249f892fd4a49be184ddb8d7e4a5847a15107d11cde4edc1acaa90507c7023c1` (= the same blob **plus** one
  trailing `\n`). This is the expected build-log newline quirk, **not** stimulus drift; `cmp` against
  the sibling file is byte-identical.
- Built by `build_trials.py` (no API), seed `SEED0 = 20260618`. 108 records/model (72 COMP + 36
  DIRECT), **1 model (gpt) → 108 finding-bearing calls** (+ 1 liveness).

## Why gpt is eligible (independent pre-run critic GO, 2026-06-18)

1. **No panel-change decision is owed.** `openai/gpt-5.4-mini` **is** `panel.B`
   ([`config/models.md`](../../../config/models.md) line 12). The budget panel-change rule
   ([`config/budget.md`](../../../config/budget.md)) fires only for a model *not currently in the
   panel*; its antecedent is false here. This is ordinary in-discipline work: a ratified frozen
   design re-run on an in-panel model.
2. **The reason gpt was dropped from the relational line does not apply.** gpt was dropped from the
   earlier relational **history-perturbation** line for a **stimulus-generation** reason — it could
   not supply solo-decodable near-twin *descriptions* at the required difficulty in the
   harvest-based design
   ([`result/relational-history-perturbation-v4`](../../../wiki/findings/results/relational-history-perturbation-v4.md):
   *"two harvest+certification attempts showed it cannot supply solo-decodable near-twin descriptions
   at this difficulty"*;
   [`result/relational-stamp-comprehension-b`](../../../wiki/findings/results/relational-stamp-comprehension-b.md):
   *"gpt was dropped … for a stimulus-generation reason, not a comprehension one"*). The Option-C
   instrument uses **fully synthetic** frozen stimuli (STEP/FLIP on a 6-track, coined token DAX — no
   model-generated descriptions, no harvest, no per-model certification). The drop reason is
   structurally inapplicable; gpt is eligible as a **subject**.

## Hypothesis & question (unchanged from the design)

Does a coined token's recovered referent depend on the **order** in which two **non-commuting**
operations (STEP, FLIP on a 6-track) were applied across stamped rounds — for gpt-5.4-mini? This is
the generality test named by [`essay/capability-split`](../../../wiki/findings/essays/capability-split.md)
revision trigger (a) and the result's "not a both-model finding" honesty note.

## Frozen verdict map (unchanged, symmetric, per model)

| condition | verdict |
|---|---|
| `direct_acc < 0.80` | **UNINTERPRETABLE** |
| DIRECT pass **and** COMP target Wilson-LB **> 0.50** | **RESPECTS-ORDER** (order-sensitive composition; thin) |
| DIRECT pass **and** COMP target Wilson-LB **≤ 0.50** | **ORDER-BLIND-OR-WEAKER** (thin; order-insensitive here) |

Thresholds frozen: `PRINT_CEILING = 0.50`, `DIRECT_FLOOR = 0.80`, composition bar = COMP target
Wilson-95 **lower bound > 0.50**. A gpt gate-fail is a legitimate **UNINTERPRETABLE result**, not a
run failure. No indicator is retuned.

## Scope & anchor (carried over byte-for-byte)

- **`anchor: internal-contrast-only`; no human-comparison claim.** A within-model contrast over
  balanced / order-permuted content.
- **Adjudicated THIN, not rung (iii).** Any gpt RESPECTS-ORDER positive is reported as *"respects
  operation order,"* never promoted to constitution. The rich-side rung (iii) stays documented
  **structurally closed** for text-only stimuli regardless of outcome.
- One operationalization (STEP/FLIP, 6-track, two moves, two rounds, text figures).

## Spend

1 model × ~108 finding-bearing calls + 1 liveness, pre-flight ≈ **$0.08–0.12** (gpt-5.4-mini is the
cheap panel model; the sibling run billed claude $0.232 / gemini $0.064 for 108 calls each).
`HARD_STOP_USD = 0.55`. Day total 2026-06-18 before this run ≈ $0.298 (the sibling claude+gemini
run); well inside the $5.00/day cap. Billed `usage.cost` recorded after, 0-missing target.

## Pre-run checks (no API) — ALL PASS

`build_trials.assert_balance` + `fixtures/make_fixtures.py` re-run on the copied (byte-identical)
stimuli before any finding-bearing call; verdict map certified on six idealized readers. Stamp-order
reader → RESPECTS-ORDER (1.000); print-order / canonical → ORDER-BLIND-OR-WEAKER (0.500);
figure / track-position / direct-fail readers → UNINTERPRETABLE.
