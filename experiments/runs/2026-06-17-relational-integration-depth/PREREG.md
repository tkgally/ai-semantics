# PREREG (FROZEN) — relational INTEGRATION-UNDER-LOAD probe (burial depth 2)

**FROZEN 2026-06-17 after independent pre-run critic GO** (fresh agent: reproduced the sha; re-derived every shortcut bound from scratch — position 0.125, single-attr ≤0.25, every drop-one-turn reader exactly 0.50 incl. RECENT-TWO, full integrator 1.000; false-positive of a true-0.50 reader clearing the bar ≈ 3% [k≥31/48]; ALL FIXTURES PASS; ruled **no new decision owed**; BLOCKERS none, SHOULD-FIX none). Internal-contrast-only (the ratified relational posture; no human comparison; no new decision
owed — a depth generalization of an established within-model contrast with a symmetric verdict map).

## Frozen stimuli

- `stimuli.json` sha256 = **`7f0197fb24834a80cd7e6d3364708b2eb23a484567d93f5423187c66d2f984ef`**
- `python3 build_trials.py` is deterministic (SEED0=20260617); accepted placement offsets
  INTEG=2397, DIRECT=76 (smallest that balances the slot tie-breaks). Re-running reproduces the sha.

## Question

result/relational-integration-rung-ii (depth 1) showed both models INTEGRATE a compatible earlier
turn at ceiling, but is SATURATED and flags "more turns" as untested harder load. **Does integration
survive greater BURIAL DEPTH?** Three compatible stamped turns (earliest=shape, middle=pattern,
latest=color) over a 2×2×2 = 8-figure grid; the earliest (shape) turn is buried under two later
turns. A RECENT-TWO reader that keeps the latest two and DROPS the buried earliest scores exactly
0.50. Beating 0.50 requires retaining all three including the deeply-buried earliest.

## Panel & elicitation (frozen)

- Models: `claude-sonnet-4.6` (PANEL.A) + `gemini-3.5-flash` (PANEL.C). gemini `reasoning:{effort:minimal}`.
- K=8 present figures; `N_BLOCKS_INTEG=6` → 48 INTEG/model; `N_BLOCKS_DIRECT=4` → 32 DIRECT/model.
  **80 records/model × 2 = 160 finding-bearing calls.**
- Forced single-label; `MAX_TOKENS=512` (length-truncated replies never parsed); one stern retry
  then NA. `HARD_STOP_USD=0.50` on projected billed cost. Pre-flight ≈ $0.15.

## Frozen thresholds & verdict map

- `pos_chance` = 1/8 = 0.125; `SINGLE_ATTR_CEILING` = 0.25; `TWO_ATTR_CEILING` = 0.50;
  `DIRECT_FLOOR` = 0.80; integration bar = INTEG target-rate Wilson-95 **lower bound > 0.50**.
- **UNINTERPRETABLE** — `direct_acc < 0.80` (on-demand conjunction-of-three failed here).
- **INTEGRATION-UNDER-LOAD** — DIRECT gate passed AND INTEG target Wilson-95 LB > 0.50 ⇒ the buried
  earliest turn survives depth-2 load; rung-(ii) integration is robust to "more turns".
- **PARTIAL-OR-OVERWRITE** — DIRECT gate passed AND INTEG target Wilson-95 LB ≤ 0.50 ⇒ a turn is
  shed under load (the earliest most plausibly, as an elevated twin_shape/recent-two rate); bounds
  the integration claim to depth 1.

## Shortcut-proofing (certified at build + on idealized-reader fixtures)

`build_trials.assert_balance` proves per subset (re-derivable by the critic): grid-position
follower = 0.125 exactly; figure-identity preference ≤ 0.125 (16+ constant-figure pickers + 20 000
random orderings); every single-attribute reader ≤ 0.25 under four tie-breaks; every two-attribute
(drop-one-turn) reader = exactly 0.50 under four tie-breaks; full integrator = 1.000; frequency
flat; 3 distinct rounds with earliest(shape) < middle(pattern) < latest(color). `fixtures/
make_fixtures.py` certifies the verdict map on six idealized readers (`integrator` →
INTEGRATION-UNDER-LOAD; `recent_two` / `overwrite` → PARTIAL-OR-OVERWRITE; `gridpos` / `figpref` /
`direct_fail` → UNINTERPRETABLE). **ALL FIXTURES PASS.**

## Anti-cheat

Symmetric verdict map: a ceiling STRENGTHENS the rung-(ii) reading; a drop to ~0.50 BOUNDS it.
Neither is the "wanted" result; the bar is pre-registered; the roster is shortcut-proof by
construction; the stimuli sha is frozen before any finding-bearing call. The result stays
`anchor: internal-contrast-only` regardless of outcome.
