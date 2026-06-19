# Design — three-move (deeper-composition) order-sensitive composition probe

**Run dir:** `experiments/runs/2026-06-19-relational-order-composition-three-move/`
**Status:** built + certified; PREREG frozen pending the independent pre-run critic GO.
**Lineage:** the >2-move DEPTH axis of the Option-C order-sensitive composition line
(`relational-order-composition-c.md` → fig → worked-example → gpt → working-surface (witness) →
alt-pair → K=6 → **this**).

## Question

Does the working-surface composition **witness** survive a **deeper serial-composition load**? Every
prior Option-C run composed exactly two non-commuting moves. The working-surface run found that opening
a scratchpad flips gemini and gpt to RESPECTS-ORDER on the two-move task; alt-pair and K=6 replicated a
two-move composition **capacity**. `source/li-2024-cot-serial` predicts the load-bearing axis is serial
**depth**, and the K=6 run showed a suggestive gpt COMP dip across instruments. This probe is the
`essay/output-channel-confound` **trigger-(b) contrast case**: a **third** stamped non-commuting move —
does a serial-depth gap **survive** the wide working-surface channel (channel-controlled bound) or does
the channel absorb the deeper load (capacity extends to depth 3)?

## Manipulated variable

The **number of moves, 2 → 3**, holding the working-surface format, figure→figure rendering, `TERM`,
thresholds, verdict map, and thin adjudication identical. As a **forced consequence** the dihedral
STEP/FLIP pair is replaced by three **generic non-commuting permutations** — the dihedral group cannot
be shortcut-proofed at three moves (its products collapse; exhaustive search finds no K≤12 config that
isolates the true ordering).

## Instrument

Three derangement permutations of six figures (`FLIP=[1,5,4,2,0,3]`, `SLIDE=[4,2,5,0,3,1]`,
`TWIST=[3,0,1,5,2,4]`), pairwise non-commuting, shown to the model only as figure→figure tables. Six
strict-valid configs (one start per ordering; targets span all 6 positions). COMP (order not stated,
72 records) vs DIRECT (order stated, 36 records) × 3 models = 324 calls.

## Why the 0.50 ceiling still holds (the key design move)

With 3 moves there are 6 orderings. A reader that fails to order all three by their stamps can pin at
most one slot from the stamps and must fill the remaining two-move sub-order from the print order →
correct exactly half the time → **0.50**. Canonical/print readers → 1/6; start/single/pair/reverse →
0; figure/position → 1/K. Only ordering **all three** by stamps beats 0.50. Same bar as the two-move
runs, deeper task. Brute-forced over the actual records in `assert_balance`; the verdict logic is
end-to-end tested in `fixtures/make_fixtures.py` (the half-composer fixture lands at exactly 0.50 and
reads as a null).

## Verdict map (frozen)

- `direct_acc < 0.80` → **UNINTERPRETABLE**.
- DIRECT pass and COMP Wilson-LB > 0.50 → **RESPECTS-ORDER** (deeper 3-move composition; thin).
- DIRECT pass and COMP Wilson-LB ≤ 0.50 → **ORDER-BLIND-OR-WEAKER** (thin).

All thin / single-reader-recoverable; `anchor: internal-contrast-only`; no human-comparison claim.
Governance: surfaced as a within-frame depth variation owing no new decision; the pre-run critic gates
that judgement.

## Spend

Pre-flight ≈ $1.0–1.4 billed (324 calls; deeper CoT than the $0.80 K=6 run). `HARD_STOP_USD = 1.80`.
